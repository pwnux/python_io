# python_io
for learning
Đoạn code này dùng để tính độ chính xác theo F1 Score của bài toán dự đoán nhãn cho dữ liệu đầu vào. Dữ liệu đầu vào cho code 
là chuỗi các tokens (các từ) đã được dự đoán nhãn bằng mô hình học máy SVMs. Các nhãn cho các token được đánh số từ 0 đến 14 
(trong bài toán của em có tổng cộng 15 nhãn

Công thức tính F1 score như sau:
        F1 score = 2 * precision * recall / (precision + recall)
    Trong đó:
        precision: độ chính xác, được tính bằng công thức:
                        pre = true positive / (true positive + false positive)
        recall: độ hồi tưởng, tính bằng công thức:
                        rec = true positive / (true positive + false negative)
                        
        Ở đây: true positive là số lượng nhãn mà mô hình đoán chính xác khi so sánh với nhãn do người gán
        false positive là số lưỡng nhãn mô hình đoán sai so với người gán
        false negative là số nhãn người gán đúng nhưng mô hình không đoán được 
        (link tham khảo: https://en.wikipedia.org/wiki/Precision_and_recall)
