# Auto send message facebook.

Bạn bận bịu vì không có thời gian nhắn tin với người yêu, hãy để phần mềm thực hiện giúp bạn.
Sử dụng python3 + selenium + phantomjs tự động nhắn tin cho người ấy theo giờ đã định sẵn
hàng ngày qua messenger.

Sử dụng:
Thay đổi username, password, và url messenger của người đó ở file config.
(Chú ý url messenger phải ở dạng di động. Truy cập vào https://m.facebook.com 
và vào phần tin nhắn để lấy link url)


```bash
python3 autofacebook.py test
```
Lập lịch chạy:
Sử dụng crontab và thư viện python crontab để lập lịch chạy cho script.

```bash
python3 scheduler.py
```
