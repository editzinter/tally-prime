use std::process::Command;
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
        .invoke_handler(tauri::generate_handler![greet])
        .setup(|app| {
            // Find the backend executable path dynamically
            let resource_path = app.path().resolve("backend/tally-backend.exe", tauri::path::BaseDirectory::Resource).unwrap();
            
            println!("Starting backend at: {:?}", resource_path);
            let child = Command::new(&resource_path)
                .spawn()
                .expect("Failed to start backend");
                
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
