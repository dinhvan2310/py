# Playwright Script - Inject JS vào Tab với URL Xác Định

Script này sử dụng Playwright để:
- Mở Chrome browser
- Theo dõi và phát hiện khi tab với URL xác định được mở
- Tự động inject JavaScript script vào tab đó ngay lập tức
- Xử lý phím F5 (refresh)

## Cài đặt

1. Cài đặt dependencies:
```bash
pip install -r requirements.txt
```

2. Cài đặt Playwright browsers:
```bash
playwright install chromium
```

## Sử dụng

1. **Tìm đường dẫn Chrome Profile (tùy chọn)**:
   ```bash
   python find_chrome_profile.py
   ```
   Script này sẽ hiển thị tất cả Chrome profiles trên máy bạn và hướng dẫn copy đường dẫn.

2. **Chỉnh sửa cấu hình** trong file `playwright_inject.py`:
   - `TARGET_URL`: URL bạn muốn theo dõi (mặc định: `https://example.com`)
   - `INJECT_SCRIPT_FILE`: Tên file JavaScript để inject (mặc định: `inject_script.js`)
   - `CHROME_PROFILE_PATH`: Đường dẫn Chrome Profile (để `None` nếu muốn dùng profile tạm thời)
     - Ví dụ: `r"C:\Users\trand\AppData\Local\Google\Chrome\User Data\Default"`

3. **Chỉnh sửa script JavaScript** trong file `inject_script.js`:
   - File này chứa code JavaScript sẽ được inject vào trang
   - Bạn có thể chỉnh sửa file này để thay đổi hành vi của script

4. **Chạy script**:
```bash
python playwright_inject.py
```

## Cấu trúc File

- `playwright_inject.py` - Script Python chính
- `inject_script.js` - File JavaScript sẽ được inject vào trang (có thể chỉnh sửa)
- `find_chrome_profile.py` - Helper script để tìm đường dẫn Chrome Profile
- `requirements.txt` - Dependencies Python

## Ví dụ

- `TARGET_URL = "https://example.com"` - Theo dõi trang example.com
- `inject_script.js` - Script JS sẽ được inject vào trang (có thể chỉnh sửa file này)

Script sẽ tự động inject JS từ file `inject_script.js` vào bất kỳ tab nào có URL khớp với TARGET_URL.

## Lưu ý

- Nếu file `inject_script.js` không tồn tại, script sẽ sử dụng script mặc định
- Bạn có thể chỉnh sửa `inject_script.js` mà không cần sửa code Python


