from playwright.sync_api import sync_playwright, Page
import time
import os

user_data_dir = r"C:\Users\trand\AppData\Local\Google\Chrome\User Data\Profile 1"
INJECT_SCRIPT_FILE = "inject_script.js"

inject_script = ""
if os.path.exists(INJECT_SCRIPT_FILE):
    try:
        with open(INJECT_SCRIPT_FILE, 'r', encoding='utf-8') as f:
            inject_script = f.read()
        print(f"✓ Đã đọc script từ {INJECT_SCRIPT_FILE} ({len(inject_script)} ký tự)")
    except Exception as e:
        print(f"⚠ Không thể đọc file: {e}")
else:
    print(f"⚠ File {INJECT_SCRIPT_FILE} không tồn tại")

with sync_playwright() as p:
    browser = p.chromium.launch_persistent_context(
        user_data_dir=user_data_dir,
        channel="chrome",
        headless=False,
        args=[
            "--no-first-run",
            "--no-default-browser-check",
            "--disable-blink-features=AutomationControlled",
            "--start-maximized"
        ],
        no_viewport=True
    )
    
    if inject_script:
        browser.add_init_script(inject_script)
        print("✓ Đã đăng ký add_init_script")
    
    print("=" * 60)
    print("Chrome đã được mở")
    print("Nhấn Ctrl+C để tắt browser")
    print("=" * 60)
    
    try:
        while True:
            browser.add_init_script(inject_script)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n" + "=" * 60)
        print("Đang đóng browser...")
        print("=" * 60)
        browser.close()
        print("✓ Đã đóng!")
