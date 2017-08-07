class lophoc():
    def __init__(self, _name, _sessions, _dayInWeek, _start, _end):
        self.name = _name
        self.sessions = _sessions
        self.dayInWeek = _dayInWeek
        self.start = _start
        self.end = _end
lop = []
print 'Luu y: cac lop nam trong khoang tu thu 2 den thu 5, gio hoc trong khoang tu 7h den 17h'
soLop = int(raw_input("Nhap so lop can tinh toan: "))

for x in range(0, soLop):
    _dayInWeek = []
    _start = []
    _end = []
    print 'Lop thu %d' %(x+1)
    _name = str(raw_input("Ten: "))
    _sessions = int(raw_input("So phien trong tuan: "))
    for y in range (0, _sessions):
        buf1 = int(raw_input("Nhap ngay hoc thu %d: " %(y+1)))
        _dayInWeek.append(buf1)
    for z in range(0, _sessions):
        buf2 = int(raw_input("Nhap gio bat dau thu %d: " %(z+1)))
        _start.append(buf2)
    for t in range(0, _sessions):
        buf3 = int(raw_input("Nhap gio ket thuc thu %d: " %(t+1)))
        _start.append(buf3)
    lopNhap = lophoc(_name, _sessions, _dayInWeek, _start, _end)
    lop.append(lopNhap)

check = 0

for i in range(0, soLop):
    for j in range(i+1, soLop):
        if lop[i]._dayInWeek == lop[j]._dayInWeek:
            if (lop[i].start <= lop[j].start <= lop[j].end) or (lop[j].start <= lop[i].start <= lop[j].end):
                print 'Ton tai lop co gio hoc trung nhau, cac lop hoc nay khong thoa man'
                check = 1
                break

print '---------------------------------------------------------------------------------------'
if check == 0:
    print 'Thoi khoa bieu: '
    for ngay in range(2, 8):
        print 'Thu %d: ' %ngay
        for l in lop:
            for i in range(0, l.sessions):
                if ngay == l.dayInWeek[i]:
                    print 'Ten mon: %s' %l.name
                    print 'Gio bat dau: %d' %l.start[i]
                    print 'Gio bat dau: %d' %l.end[i]
