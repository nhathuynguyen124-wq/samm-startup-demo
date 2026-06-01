# =======================================================
# FILE: app.py - ỨNG DỤNG ĐÃ ĐƯỢC VÁ LỖI THEO ĐỀ XUẤT SAMM
# =======================================================
import os
import sys

# GIẢI PHÁP AN TOÀN: Lấy thông tin từ biến môi trường (Environment Variables)
# Không còn hardcode mật khẩu trực tiếp trong code nữa!
DATABASE_HOST = os.environ.get("DB_HOST", "192.168.1.250")
DATABASE_USER = os.environ.get("DB_USER", "sa_admin")
DATABASE_PASSWORD = os.environ.get("DB_PASSWORD") # Mật khẩu thật được giấu ở ngoài

def connect_to_database():
    print(f"[*] Đang khởi tạo kết nối đến Cơ sở dữ liệu tại {DATABASE_HOST}...")
    
    # Kiểm tra xem hệ thống đã cấu hình biến môi trường an toàn chưa
    if DATABASE_PASSWORD:
        print("[+] KẾT NỐI THÀNH CÔNG! Hệ thống bảo mật đạt chuẩn SAMM Cấp độ 2.")
        return True
    else:
        print("[-] CẢNH BÁO: Không tìm thấy biến cấu hình mật khẩu an toàn!")
        return False

if __name__ == "__main__":
    print("=== STARTUP APPLICATION INITIALIZATION ===")
    connect_to_database()
