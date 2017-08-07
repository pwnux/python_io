# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
import os

# Bài toán tính học phí của một kì học khi người dùng nhập các mã học phần các môn học
# mà người đó sẽ học trong kì
# Chương trình lấy dữ liệu các học phần và số tín chỉ học phí từ trang sis
# Chương trình nhắc người dùng các mã học phần và in ra màn hình số tiền của các môn học đó
# Chương trình được dùng mỗi đầu kì học khi đăng kí tín chỉ, cần tính ngay học phí để điều chỉnh
# lượng môn học cho phù hợp và biết trước học phí để chuẩn bị cho phù hợp

# Các hướng mở rộng của bài toán
# Viết chương trình lấy dữ liệu thời khóa biểu các môn học
# Đề xuất các thời khóa biểu cho người dùng đỡ mất công sắp xếp thủ công


if __name__ == "__main__":

    driver = webdriver.Firefox()
    driver.get("http://sis.hust.edu.vn/ModuleProgram/CourseLists.aspx")

    dic = {}
    try:
        for pageNum in range(1,200):
            tblMain = driver.find_element_by_id("MainContent_gvCoursesGrid_DXMainTable")
            divPageBottom = driver.find_element_by_id("MainContent_gvCoursesGrid_DXPagerBottom")
            listBtn = divPageBottom.find_elements_by_tag_name("b")
            btnNext = []
            for b in listBtn:
                if b.get_attribute("onclick") == "aspxGVPagerOnClick('MainContent_gvCoursesGrid','PBN');":
                    btnNext = b
                    break
            tr_list = tblMain.find_elements_by_tag_name("tr")
            for tr_elm in tr_list:
                lst = []
                for td_elm in tr_elm.find_elements_by_tag_name("td"):
                    if("dxgv" == td_elm.get_attribute("class")):
                        lst.append(td_elm.get_attribute("innerHTML"))
                if len(lst) > 4:
                        # print(lst)
                    id = lst[0]
                    cost = lst[4]
                    print(id, cost)
                    dic.update({id: cost})
            btnNext.click()
    except:
        print("abc")

    print "dic= ", dic
    print "len = ", len(dic)

HOC_PHI_MOT_TIN_CHI = 185

print("Nhap vao cac ma mon hoc ki toi: ")
lstMaHP = raw_input()
lstMaHP = lstMaHP.split(",")
print(lstMaHP)
totalCost = 0
for maHP in lstMaHP:
    totalCost += float(dic.get(maHP,0))

totalCost *= HOC_PHI_MOT_TIN_CHI
print("Hoc phi cua ban la: " + str(totalCost) + " nghin")
