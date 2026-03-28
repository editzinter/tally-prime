use std::process::Command;
#[cfg(target_os = "windows")]
use std::os::windows::process::CommandExt;
use std::sync::Mutex;
use std::time::Duration;
use tauri::Manager;

struct BackendProcess(Mutex<Option<std::process::Child>>);

#[tauri::command]
fn greet(name: &str) -> String {
    format!("Hello, {}! You've been greeted from Rust!", name)
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_opener::init())
        .plugin(tauri_plugin_process::init())
        .plugin(tauri_plugin_updater::Builder::new().build())
        .invoke_handler(tauri::generate_handler![greet])
        .setup(|app| {
            // Find the backend executable path dynamically based on OS
            #[cfg(target_os = "windows")]
            let resource_path = app.path().resolve("backend/tally-backend.exe", tauri::path::BaseDirectory::Resource).unwrap();
            
            #[cfg(not(target_os = "windows"))]
            let resource_path = app.path().resolve("backend/tally-backend", tauri::path::BaseDirectory::Resource).unwrap();
            
            println!("Starting backend at: {:?}", resource_path);
            
            #[cfg(target_os = "windows")]
            let mut cmd = Command::new(&resource_path);
            #[cfg(target_os = "windows")]
            let child = cmd.creation_flags(0x08000000).spawn().expect("Failed to start backend");
            
            #[cfg(not(target_os = "windows"))]
            let child = Command::new(&resource_path).spawn().expect("Failed to start backend");
                
            app.manage(BackendProcess(Mutex::new(Some(child))));
            
            let app_handle = app.handle().clone();
            
            // Spawn a thread to wait a few seconds for the backend to start,
            // then redirect the main window to the Django server.
            std::thread::spawn(move || {
                std::thread::sleep(Duration::from_secs(3));
                
                // Attempt to navigate the main window
                if let Some(window) = app_handle.get_webview_window("main") {
                    println!("Redirecting to Tally Backend...");
                    let _ = window.navigate("http://127.0.0.1:8000/home".parse().unwrap());
                }
            });
            
            Ok(())
        })
        .on_window_event(|window, event| {
            if let tauri::WindowEvent::Destroyed = event {
                // When the main window is destroyed, kill the backend
                if let Some(state) = window.try_state::<BackendProcess>() {
                    if let Ok(mut child_lock) = state.0.lock() {
                        if let Some(mut child) = child_lock.take() {
                            let _ = child.kill();
                        }
                    }
                }
            }
        })
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
