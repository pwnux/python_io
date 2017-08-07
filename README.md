# README #
***Đặng Văn Diện - craig@trueplus.vn***

***sdt: 0973706583***

### Problem
Không thường xuyên check được website có thông tin gì mới
### Solution
Sử dụng Python web scraping, kiểm tra xem có bài viết mới, nếu có
gửi SMS tới điện thoại
##### Ý tưởng: 
1. Database: Sử dụng MongoDB để lưu trữ link các bài viết
2. Sử dụng thư viện Python requests để lấy html của trang web
3. Dùng Beautiful Soup để parse, truy xuất thông tin
4. Trích xuất link cần thiết lưu vào database
5. Chạy trên server như Heroku, dùng cron để chạy tự động mỗi 3h
nếu có link chưa tồn tại trong cơ sở dữ liệu thì lưu vào đồng
thời gửi tin nhắn xuống điện thoại thông báo
6. Dùng Twillo API để gửi tin nhắn


### How do I get set up? ###
* Download and install MongoDb 
* Start MongoDB
* pip install -r requirements.txt
* Run