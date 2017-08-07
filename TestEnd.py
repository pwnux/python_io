if __name__ == "__main__":
    SumLai = 0
    Moneymongmuon = 0
    Moneyht = raw_input("Nhap so tien hien co: ")
    check = True
    while check:
        Moneymongmuon = raw_input("Nhap so tien mong muon: ")
        if Moneymongmuon>Moneyht:
            check = False
        else:
            print "Nhap lai so tien mong muon, phai lon hon"
    Laixuat = raw_input("Nhap lai xuat: ")
    thang = 0
    while Moneyht<Moneymongmuon:

        tmp = Moneyht
        temp = int(float(Moneyht)*float(Laixuat))
        Moneyht = int(int(Moneyht) + int(int(temp)/100))
        SumLai = int(SumLai) + int(Moneyht) - int(tmp)
        thang += 1
    print "Tong lai la: " + str(SumLai)
    print "Tong so tien la: " +str(int(Moneyht)+int(SumLai))
    print "So thang la: "+str(thang)