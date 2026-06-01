#!/bin/bash
# ------------------------------------------------------------------
# SCRIPT SAO LƯU DỮ LIỆU HÀNG ĐÊM CỦA STARTUP (HIỆN TRẠNG MỨC ĐỘ 0)
# ------------------------------------------------------------------

# Cấu hình thư mục nguồn và thư mục lưu trữ
SOURCE_DIR="/var/www/html/startup_app/storage"
BACKUP_DIR="/home/ubuntu/backups" # ĐIỂM YẾU CHẾT NGƯỜI LƯU TẠI CHỖ

echo "=== Bắt đầu quy trình sao lưu: $(date) ==="

# Tiến hành nén thư mục dữ liệu thành file .tar.gz thông thường
tar -czf $BACKUP_DIR/backup_data_$(date +%F).tar.gz $SOURCE_DIR

echo "=== Sao lưu hoàn tất thành công! ==="
exit 0
