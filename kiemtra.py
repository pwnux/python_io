dic = {
    "big":"lon",
    "learn":"hoc"
}
def timkiem():
    search= raw_input("Nhap tu tim kiem: ")
    if search not in dic:
        print "khong tim thay tu: "
    else:
        print search+" co nghia la: "+ dic[search]


def themtu():
    word = raw_input("Nhap tu: ")
    mean = raw_input("Nhap nghia: ")
    dic[word]=mean
    print "tu "+ word +" da duoc them vao tu dien ";

def xoatu():
    delword= raw_input("Nhap tu can xoa")
    if delword in dic:
        del [delword]
    else:
        print "Tu chua ton tai: "
def xemtatca():
    for x in dic:
        print  x +"-->"+ dic[x]


def menu():
        print "1.tim kiem"
        print "2.Them tu:"
        print "3.Xoa tu:"
        print "4.xem tat ca cac tu:"
        print "0.thoat "

def dictionary():

    menu()
    choice = input("Nhap lua chon cua ban: ")
    while choice != 0:
        if choice==1:
            timkiem()
        if choice==2:
            themtu()
        if choice==3:
            xoatu()
        if choice==4:
            xemtatca()
        if choice==0:
            break
        choice = input("Nhap lua chon cua ban: ")
dictionary()

