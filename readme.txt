- Vấn đề: trong 1 cpu, tại 1 thời điểm chỉ có 1 tiến trình được thực hiện, 1 tiến trình có start time và end time, cho n tiến trình, thời gian bắt đầu được viết trong mảng a, thời gian kết thúc trong mảng b, bài toán ở đây là lấy ra thứ tự tiến trình sao cho không bị xung đột
- Giải quyết: sắp xếp 2 mảng theo thời gian bắt đầu, sau đó lấy các tiến trình sau cho thời gian bắt đầu của tiến trình sau không xung đột với thời gian làm việc của tiến trình trước
n = 8
a = [1, 3, 0, 5, 8, 5, 9 , 14]    //start time
b = [2, 4, 6, 7, 9, 9, 12, 18]    //end time

sorted 
a = [0, 1, 3, 5, 5, 8, 9 , 14] 
b = [6, 2, 4, 7, 9, 9, 12, 18]

output
out =   [0, 8, 14]
        [6, 9, 18]
- Mở rộng ra giải quyết vấn đề đi xoạc (tính trên 1 em đào), mỗi anh có 1 thời gian bắt đầu và kết thúc khác nhau khác nhau, sắp xếp sau cho các anh ko va chạm với nhau (xung đột) just for fun :))
- Giải quyết vấn đề ô tô ra và vào bốc rỡ hàng của 1 kho hàng, lên kế hoạch để các ô tô có thể ra vào mà ko va chạm nhau hoặc bị tắc đường do đường nhỏ
- đây là ý tưởng của em, bài này dựa trên thuật toán tham lam, ko biết em code đúng ko, có gì anh cmt lại giúp em, tks anh 
