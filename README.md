#**Hướng dẫn chạy file code**
1) Sau khi tải file code về tạo một thư mục trống, chuyển file code đã tải về vào thư mục vừa tạo
2) Mở màn hình command prompt hoặc terminal trên vs code, chuyển hướng đến thư mục vừa tạo và thực hiện cài đặt thư mục .venv với câu lệnh
```python
   py -m venv .venv
```
3) Sau khi cài đặt thư mục .venv thành công, tiếp tục thực hiện câu lệnh
```python
   Scripts/activate để khởi tạo môi trường ảo đối với window
```
4) Sau khi khởi tạo môi trường ảo xong chuyển hướng khỏi thư mục .venv và thực hiện cài đặt django trong thư mục được tạo với câu lệnh
```python
    py -m pip install Django
```
5) Tiếp tục chuyển hướng đến thư mục facereg sau đó gõ câu lệnh sau để chạy chương trình, nó sẽ xuất hiện địa chỉ của trang web
```python
   py manage.py runserver
```

**Hướng dẫn tạo tài khoản admin**
1) Trên màn hình command prompt hoặc terminal trên vs code điều hướng đến thư mục facereg
2) Gõ câu lệnh sau để tạo tài khoản admin
```python
    py manage.py createsuperuser
```
3) Tiếp đến nhập vào username là tên người dùng, email có thể bỏ qua bằng cách nhấn enter, tiếp tục thực hiện đặt mật khẩu và xác nhận mật khẩu

**Cấu trúc thư mục**
1) Thư mục facereg là thư mục chính dùng để chạy chương trình, trong đó có file utils.py làm nhiệm vụ trích xuất ra khuôn mặt và so sánh hình ảnh, file view.py nhận dữ liệu hình ảnh từ người dùng chụp qua webcam và lưu vào cơ sở dữ liệu vào thư mục media/login, cũng như lưu thông tin người dùng đăng ký vào cơ sở dữ liệu
2) Thư mục media dùng để chứa các file hình ảnh người dùng đăng tải lên qua webcam hoặc thông qua cpanel, với media/profile chứa hình ảnh người dùng đã đăng ký đăng tải hình ảnh lên thông qua cpanel, với media./login chứa hình ảnh người dùng chụp qua webcam
3) Thư mục static lưu trữ các file html, css và javascript, file login.js có chức năng chụp hình của người dùng đăng nhập thông qua webcam và gửi đến server thông qua ajax
4) Thư mục profiles phục vụ cho việc tạo form lấy dữ liệu người dùng đăng ký
5) Thư mục login phục vụ cho việc lấy dữ liệu hình ảnh người dùng chụp qua webcam và lưu vào cơ sở dữ liệu
6) Thư mục ouput chứa các hình ảnh khuôn mặt được trích xuất ra để so sánh
   
**Giải thích chương trình**<br/><br/>Đầu tiên người dùng có thể đăng ký để tạo tài khoản của mình, sau khi đã đăng ký thì người dùng có thể đăng hình ảnh có chứa khuôn mặt của mình lên thông qua cpanel trên trang admin ở mục profile, ảnh của người dùng sẽ được lưu trữ trong thư mục media/profile.<br/>Để truy cập cpanel trên trang admin để thực hiện các thao tác chỉnh sửa người dùng có thể tạo tài khoản admin như hướng dẫn ở trên. Sau khi đăng ký thì người dùng sẽ được chuyển đến một trang giao diện khác chỉ những người dùng nào đã đăng ký hoặc đăng nhập thành công mới có thể truy cập.<br/><br/>Lúc này người dùng có thể đăng xuất để kiểm tra phần đăng nhập, người dùng sẽ truy cập vào mục đăng nhập và chụp ảnh khuôn mặt thông qua webcam, hình ảnh sẽ được gửi tới server để lưu vào database vào ảnh sẽ được lưu trữ trong thư mục media/login.<br/>Hình ảnh người dùng chụp để đăng nhập qua webcam sẽ được chuyển thành ảnh xám và trích xuất ra khuôn mặt để so sánh lần lượt với từng ảnh trong cơ sở dữ liệu bằng cách sử dụng công thức histogram, việc trích xuất ảnh khuôn mặt sẽ sử dụng mô hình haarcascade trong học máy để thực hiện.<br/><br/>Giá trị sử dụng công thức correlation sẽ nằm trong khoảng từ 0 đến 1, giá trị cho ra càng gần 1 thì độ tương tự giữa hai khuôn mặt càng cao. Hình ảnh khuôn mặt được trích xuất ra từ ảnh người dụng chụp để đăng nhập qua webcam và ảnh khuôn mặt được trích xuất từ danh sách các ảnh trong cơ sở dữ liệu sẽ được lưu trữ vào cùng thư mục output để so sánh.<br/>Biến best_match là kết quả so sánh từng cặp ảnh một sau khi sử dụng công thức correlation.

**Lưu ý:**
1) Ảnh cần được chụp trong môi trường đủ sáng hay ảnh phải chụp rõ được khuôn mặt để mô hình có thể tìm được khuôn mặt trên bức hình, nếu không sẽ luôn không thể đăng nhập.
2) Hoặc ảnh vẫn đủ rõ để nhận diện được khuôn mặt nhưng khi chụp trong môi trường không quá lí tưởng thì kết quả so sánh sử dụng công thức correlation cũng không quá chính xác, nghĩa là cho dù hai khuôn mặt có là cùng của một người thì kết quả cho ra độ tương tự cũng chỉ >= 0.7. Vậy nên, có thể đặt lại ngưỡng để người dùng có thể đăng nhập thành công là 0.7.
