Do có trục trặc giữa chừng nên em đành viết tạm 1 chương trình mang tính đối phó...
Mỗi ngày ở chỗ em thực tập đều có một buổi đi bơi vào buổi trưa, mục đích chương trình là đăng lên channel 1 câu hỏi (format theo
một con bot đã dựng sẵn) dạng poll với hai đáp án có hoặc không, để hỏi xem ngày hôm đó có những ai đi bơi.
chương trình sẽ chạy vào mỗi lúc khởi động máy trong ngày, hoặc theo 1 giờ cố định, bằng crontab như sau:

1. Khởi động terminal
2. Gõ lệnh '''crontab -e'''
3. thêm dòng lệnh '''@reboot cd /location/của/file/ && python tifu.py''' để chạy lúc khởi động hoặc
''' 30 8 cd /location/của/file/ && python tifu.py''' để chạy mỗi 8h30 sáng.

Em xin hết TT^TT
