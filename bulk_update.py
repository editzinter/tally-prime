"""
Comprehensive Utilitarian Terminal Design System enforcer.
Covers ALL rgb(), rgba(), hex, and named-color inline styles 
across every Django template file.
"""
import os
import re

TEMPLATE_DIR = r"c:\Users\Administrator\Downloads\Tally-Prime-main\App1\templates"
COPY_TARGETS = [
    r"c:\Users\Administrator\Downloads\Tally-Prime-main\tally-desktop\src-tauri\backend\_internal\App1\templates",
    r"c:\Users\Administrator\Downloads\Tally-Prime-main\tally-desktop\src-tauri\target\debug\backend\_internal\App1\templates",
]

# Design System Tokens
TERMINAL_SLATE = "#172026"
INDUSTRIAL_GREY = "#BCC3C8"
LEDGER_WHITE = "#F8F9FA"
INPUT_CREAM = "#FEFBEA"
STRUCTURAL_BLUE = "#2E5085"
OPERATOR_AMBER = "#F5B935"

def fix_file(content):
    # ===== TEXT COLORS =====
    # rgb(59, 159, 252) -> Structural Blue (blue heading text)
    content = re.sub(r'color:\s*rgb\(\s*59\s*,\s*159\s*,\s*252\s*\)', f'color: {STRUCTURAL_BLUE}', content)
    # rgb(15, 14, 14) -> Terminal Slate (hover dark text)
    content = re.sub(r'color:\s*rgb\(\s*15\s*,\s*14\s*,\s*14\s*\)', f'color: {TERMINAL_SLATE}', content)
    # rgb(0, 9, 105) -> Terminal Slate (btn_2 hover)
    content = re.sub(r'color:\s*rgb\(\s*0\s*,\s*9\s*,\s*105\s*\)', f'color: {TERMINAL_SLATE}', content)
    # rgb(255, 255, 255) -> Ledger White (close button, etc.)
    content = re.sub(r'color:\s*rgb\(\s*255\s*,\s*255\s*,\s*255\s*\)', f'color: {LEDGER_WHITE}', content)
    # rgb(248, 242, 242) -> Ledger White (currency heading)
    content = re.sub(r'color:\s*rgb\(\s*248\s*,\s*242\s*,\s*242\s*\)', f'color: {LEDGER_WHITE}', content)
    # rgb(0, 0, 65) -> Terminal Slate
    content = re.sub(r'color:\s*rgb\(\s*0\s*,\s*0\s*,\s*65\s*\)', f'color: {TERMINAL_SLATE}', content)
    # rgb(0, 104, 214) -> Structural Blue
    content = re.sub(r'color:\s*rgb\(\s*0\s*,\s*104\s*,\s*214\s*\)', f'color: {STRUCTURAL_BLUE}', content)
    # rgb(128, ...) orange hover
    content = re.sub(r'color:\s*rgb\(\s*255\s*,\s*128\s*,\s*0\s*\)', f'color: {OPERATOR_AMBER}', content)
    # rgb(103, 175, 220) -> Structural Blue (button/form color)
    content = re.sub(r'color:\s*rgb\(\s*103\s*,\s*175\s*,\s*220\s*\)', f'color: {STRUCTURAL_BLUE}', content)
    # color: black -> Terminal Slate (NEVER use pure black)
    content = re.sub(r'color:\s*black\b', f'color: {TERMINAL_SLATE}', content)
    # color: white -> Ledger White
    content = re.sub(r'color:\s*white\b', f'color: {LEDGER_WHITE}', content)
    # color: goldenrod -> Operator Amber
    content = re.sub(r'color:\s*goldenrod\b', f'color: {OPERATOR_AMBER}', content)

    # ===== BACKGROUND COLORS =====
    # rgb(222, 242, 255) -> Industrial Grey (light blue canvas)
    content = re.sub(r'background(?:-color)?:\s*rgb\(\s*222\s*,\s*242\s*,\s*255\s*\)', f'background-color: {INDUSTRIAL_GREY}', content)
    # rgb(142, 211, 250) -> Ledger White (secondary blue)
    content = re.sub(r'background(?:-color)?:\s*rgb\(\s*142\s*,\s*211\s*,\s*250\s*\)', f'background-color: {LEDGER_WHITE}', content)
    # rgb(27, 117, 173) -> Terminal Slate (dark blue panels)
    content = re.sub(r'background(?:-color)?:\s*rgb\(\s*27\s*,\s*117\s*,\s*173\s*\)', f'background-color: {TERMINAL_SLATE}', content)
    # rgb(0, 104, 214) -> Terminal Slate
    content = re.sub(r'background(?:-color)?:\s*rgb\(\s*0\s*,\s*104\s*,\s*214\s*\)', f'background-color: {TERMINAL_SLATE}', content)
    # background: rgb(0, 104, 214) (shorthand)
    content = re.sub(r'background:\s*rgb\(\s*0\s*,\s*104\s*,\s*214\s*\)', f'background: {TERMINAL_SLATE}', content)
    # rgb(115, 201, 255) -> Ledger White (modal header)
    content = re.sub(r'background(?:-color)?:\s*rgb\(\s*115\s*,\s*201\s*,\s*255\s*\)', f'background-color: {LEDGER_WHITE}', content)
    # rgb(103, 175, 220) -> Terminal Slate
    content = re.sub(r'background(?:-color)?:\s*rgb\(\s*103\s*,\s*175\s*,\s*220\s*\)', f'background-color: {TERMINAL_SLATE}', content)
    # rgba(0,0,0,0.2-0.4) -> Ledger White
    content = re.sub(r'background(?:-color)?:\s*rgba\(\s*0\s*,\s*0\s*,\s*0\s*,\s*0?\.\s*[234]\s*\)', f'background-color: {LEDGER_WHITE}', content)
    # rgba(240, 248, 255, 0) -> Ledger White (transparent button bg)
    content = re.sub(r'background(?:-color)?:\s*rgba\(\s*240\s*,\s*248\s*,\s*255\s*,\s*0\s*\)', f'background-color: {LEDGER_WHITE}', content)
    # orange -> Operator Amber
    content = re.sub(r'background(?:-color)?:\s*orange\b', f'background-color: {OPERATOR_AMBER}', content)
    # rgb(181, 213, 240) -> Operator Amber
    content = re.sub(r'background(?:-color)?:\s*rgb\(\s*181\s*,\s*213\s*,\s*240\s*\)', f'background-color: {OPERATOR_AMBER}', content)
    # #ffecd9 -> Operator Amber (hover)
    content = re.sub(r'background(?:-color)?:\s*#ffecd9', f'background-color: {OPERATOR_AMBER}', content, flags=re.IGNORECASE)
    # rgb(204, 212, 228) -> Ledger White (createcompony bg)
    content = re.sub(r'background(?:-color)?:\s*rgb\(\s*204\s*,\s*212\s*,\s*228\s*\)', f'background-color: {LEDGER_WHITE}', content)

    # ===== BORDERS =====
    # rgb(218, 218, 218) -> Structural Blue
    content = re.sub(r'solid\s+rgb\(\s*218\s*,\s*218\s*,\s*218\s*\)', f'solid {STRUCTURAL_BLUE}', content)
    # rgb(177, 203, 225) -> Structural Blue
    content = re.sub(r'solid\s+rgb\(\s*177\s*,\s*203\s*,\s*225\s*\)', f'solid {STRUCTURAL_BLUE}', content)
    # rgb(121, 186, 255) -> Structural Blue
    content = re.sub(r'solid\s+rgb\(\s*121\s*,\s*186\s*,\s*255\s*\)', f'solid {STRUCTURAL_BLUE}', content)
    # rgb(103, 175, 220...) in borders
    content = re.sub(r'solid\s+rgb\(\s*103\s*,\s*175\s*,\s*220\s*(?:,\s*[\d.]+)?\s*\)', f'solid {STRUCTURAL_BLUE}', content)
    # rgb(0, 0, 0, 0) transparent borders -> Structural Blue
    content = re.sub(r'solid\s+rgb\(\s*0\s*,\s*0\s*,\s*0\s*,\s*0\s*\)', f'solid {STRUCTURAL_BLUE}', content)
    # generic border-bottom: 1px solid black -> Structural Blue
    content = re.sub(r'solid\s+black\b', f'solid {STRUCTURAL_BLUE}', content)

    # ===== BANNED EFFECTS =====
    # Remove backdrop-filter: blur (banned)
    content = re.sub(r'backdrop-filter:\s*blur\([^)]*\)\s*;?', '', content)
    content = re.sub(r'-webkit-backdrop-filter:\s*blur\([^)]*\)\s*;?', '', content)
    # Remove any box-shadow (banned)
    content = re.sub(r'box-shadow:\s*[^;]+;', 'box-shadow: none;', content)
    # Remove any text-shadow (banned)
    content = re.sub(r'text-shadow:\s*[^;]+;', '', content)
    # Remove any border-radius > 2px
    content = re.sub(r'border-radius:\s*\d+px', 'border-radius: 0px', content)

    # ===== FONTS =====
    content = re.sub(r"font-family:\s*Arial,\s*Helvetica,\s*sans-serif", "font-family: 'Geist', sans-serif", content)
    content = re.sub(r"font-family:\s*['\"]?Poppins['\"]?,\s*sans-serif", "font-family: 'Geist', sans-serif", content)
    content = re.sub(r"font-family:\s*['\"]?Muli['\"]?,\s*sans-serif", "font-family: 'Geist', sans-serif", content)

    # ===== REMAINING GENERIC CATCH-ALL =====
    # Any remaining background-color: #2f516f -> Industrial Grey
    content = content.replace('#2f516f', INDUSTRIAL_GREY)
    content = content.replace('#213b52', TERMINAL_SLATE)

    return content

def inject_fonts(content):
    """Ensure Geist + JetBrains Mono fonts are available."""
    font_links = '''    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/geist@1.0.3/dist/fonts/geist-sans/style.css">'''
    
    if "JetBrains" not in content and "</head>" in content:
        content = content.replace("</head>", font_links + "\n</head>")
    return content

def process_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_content = fix_file(content)
    new_content = inject_fonts(new_content)
    
    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True
    return False

if __name__ == "__main__":
    changed = 0
    total = 0
    for fname in os.listdir(TEMPLATE_DIR):
        if fname.endswith(".html"):
            total += 1
            src = os.path.join(TEMPLATE_DIR, fname)
            if process_file(src):
                changed += 1
                print(f"  FIXED: {fname}")
            else:
                print(f"  OK:    {fname}")
            
            # Copy to all target dirs
            for target_dir in COPY_TARGETS:
                dst = os.path.join(target_dir, fname)
                os.makedirs(target_dir, exist_ok=True)
                with open(src, "r", encoding="utf-8") as f:
                    data = f.read()
                with open(dst, "w", encoding="utf-8") as f:
                    f.write(data)
    
    print(f"\nDone. Fixed {changed}/{total} template files.")
