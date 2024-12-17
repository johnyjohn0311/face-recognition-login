Hướng dẫn chạy file code
1) Sau khi tải file code về tạo một thư mục trống, chuyển file code đã tải về vào thư mục vừa tạo
2) Mở màn hình command prompt hoặc terminal trên vs code, chuyển hướng đến thư mục vừa tạo và thực hiện cài đặt thư mục .venv với câu lệnh py -m venv .venv
3) Sau khi cài đặt thư mục .venv thành công, tiếp tục thực hiện câu lệnh Scripts/activate để khởi tạo môi trường ảo đối với window
4) Sau khi khởi tạo môi trường ảo xong chuyển hướng khỏi thư mục .venv và thực hiện cài đặt django trong thư mục được tạo với câu lệnh py -m pip install Django
5) Tiếp tục chuyển hướng đến thư mục facereg sau đó gõ py manage.py runserver để chạy chương trình, nó sẽ xuất hiện địa chỉ của trang web

Hướng dẫn tạo tài khoản admin
1) Trên màn hình command prompt hoặc terminal trên vs code điều hướng đến thư mục facereg
2) Gõ câu lệnh sau để tạo tài khoản admin py manage.py createsuperuser
3) Tiếp đến nhập vào username là tên người dùng, email có thể bỏ qua bằng cách nhấn enter, tiếp tục thực hiện đặt mật khẩu và xác nhận mật khẩu
