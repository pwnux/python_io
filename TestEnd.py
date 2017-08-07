if __name__ == "__main__":
    SumLai = 0
    Moneymongmuon = 0
    Moneyht = input("Nhap so tien hien co: ")
    check = True
    while check:
        Moneymongmuon = input("Nhap so tien mong muon: ")
        if Moneymongmuon>Moneyht:
            check = False
        else:
            print "Nhap lai so tien mong muon, phai lon hon"
    Laixuat = input("Nhap lai xuat: ")
    thang = 0
    while Moneyht<Moneymongmuon:
        tmp = Moneyht
        temp = Moneyht*float(Laixuat)
        Moneyht = int(Moneyht) + (Moneyht*float(Laixuat))/100
        SumLai = SumLai + Moneyht - tmp
        thang += 1
    print "Tong lai la: " + str(SumLai)
    print "Tong so tien la: " +str(Moneyht+SumLai)
    print "So thang la: "+str(thang) +"thang"
