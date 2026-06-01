# =================================================================
# FILE: app.py - ỨNG DỤNG CORE WEB SERVICE CỦA STARTUP
# =================================================================
import os
import sys

# CẤU HÌNH KẾT NỐI HỆ THỐNG (HIỆN TRẠNG MỨC ĐỘ 0)
DATABASE_HOST = "192.168.1.250"
DATABASE_USER = "sa_admin"

# LỖI BẢO MẬT CHÍ MẠNG: Lập trình viên hardcode mật khẩu Master của DB vào mã nguồn công khai
DATABASE_PASSWORD = "super_secret_password_123" 

def connect_to_database():
    print(f"[*] Đang khởi tạo kết nối đến Cơ sở dữ liệu tại {DATABASE_HOST}...")
    # Giả lập logic kết nối sử dụng tài khoản và mật khẩu trên
    if DATABASE_USER == "sa_admin" and DATABASE_PASSWORD == "super_secret_password_123":
        print("[+] KẾT NỐI THÀNH CÔNG! Hệ thống đã sẵn sàng phục vụ khách hàng.")
        return True
    else:
        print("[-] KẾT NỐI THẤT BẠI: Sai thông tin xác thực.")
        return False

if __name__ == "__main__":
    print("=== STARTUP APPLICATION INITIALIZATION ===")
    connect_to_database()
