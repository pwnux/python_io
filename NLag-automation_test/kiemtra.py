# encoding=utf8

# [{'name': 'don_gia'}]
# [{'name': 'gia_tri_sd'}]
def thanh_tien(str_month, dict_don_gia, list_gia_tri_sd):
    result = {}     # {'name': 'thanh_tien', }
    for i in range(len(list_gia_tri_sd)):
        key = list_gia_tri_sd[i].keys()[0]
        temp = list_gia_tri_sd[i][key] * dict_don_gia[key]
        result[key] = temp

    s = {}
    s[str_month] = result
    return s    # {'month': {'name': 'thanh_tien', } }

# {'name': 'thanh_tien'}
def chenh_lech(dict_thanh_tien_thang_x, dict_thanh_tien_thang_y):
    month_x = dict_thanh_tien_thang_x.keys()[0]
    month_y = dict_thanh_tien_thang_y.keys()[0]

    list_key_x = dict_thanh_tien_thang_x[month_x].keys()
    list_key_y = dict_thanh_tien_thang_y[month_y].keys()

    tong_chenh_lech = 0

    for i in list_key_x:
        if i in list_key_y:
            temp = dict_thanh_tien_thang_x[month_x][i] - dict_thanh_tien_thang_y[month_y][i]
            if temp > 0:
                print i + " Âm " + str(temp) + " so với tháng trước"
                tong_chenh_lech -= temp
            else:
                print i + " Dương " + str(0 - temp) + " so với tháng trước"
                tong_chenh_lech -= temp
        else:
            print i + " Âm " + str(dict_thanh_tien_thang_x[month_x][i]) + " so với tháng trước"
            tong_chenh_lech -= dict_thanh_tien_thang_x[month_x][i]
    for i in list_key_y:
        if i not in list_key_x:
            print i + " Dương " + str(dict_thanh_tien_thang_y[month_y][i]) + " so với tháng trước"
            tong_chenh_lech += dict_thanh_tien_thang_y[month_y][i]

    print "Tổng chi tháng " + str(month_x) + " " + str(tong_chenh_lech) + " so với tháng " + str(month_y)


if __name__ == "__main__":
    dict1 = {'dien': 5, 'nuoc': 17, 'net': 2, 'name4': 31}
    list1 = [{'dien': 56}, {'nuoc': 90}, {'name4': 50}]
    list2 = [{'dien': 58}, {'nuoc': 88}, {'net': 100}]

    # print thanh_tien(1, dict1, list1)
    chenh_lech(thanh_tien(1, dict1, list1), thanh_tien(2, dict1, list2))
