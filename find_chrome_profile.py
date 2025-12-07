"""
Script helper để tìm đường dẫn Chrome Profile
"""
import os
from pathlib import Path

def find_chrome_profiles():
    """Tìm tất cả Chrome profiles trên Windows"""
    username = os.getenv('USERNAME')
    if not username:
        username = os.getenv('USER')
    
    chrome_base = Path(f"C:/Users/{username}/AppData/Local/Google/Chrome/User Data")
    
    if not chrome_base.exists():
        print("❌ Không tìm thấy thư mục Chrome User Data")
        print(f"   Đã tìm tại: {chrome_base}")
        return
    
    print("=" * 60)
    print("🔍 Tìm thấy các Chrome Profiles:")
    print("=" * 60)
    
    profiles = []
    
    # Profile mặc định
    default_profile = chrome_base / "Default"
    if default_profile.exists():
        profiles.append(("Default", default_profile))
    
    # Các profile khác
    for item in chrome_base.iterdir():
        if item.is_dir() and item.name.startswith("Profile "):
            profiles.append((item.name, item))
    
    if not profiles:
        print("❌ Không tìm thấy profile nào")
        return
    
    print(f"\nTổng cộng: {len(profiles)} profile(s)\n")
    
    for i, (name, path) in enumerate(profiles, 1):
        print(f"{i}. {name}")
        print(f"   Đường dẫn: {path}")
        print(f"   Copy dòng này vào CHROME_PROFILE_PATH:")
        print(f'   CHROME_PROFILE_PATH = r"{path}"')
        print()
    
    print("=" * 60)
    print("\n💡 Cách sử dụng:")
    print("1. Copy một trong các đường dẫn trên")
    print("2. Dán vào file playwright_inject.py, biến CHROME_PROFILE_PATH")
    print("3. Chạy lại playwright_inject.py")

if __name__ == "__main__":
    find_chrome_profiles()

