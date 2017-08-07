#8
# start   end
# 1       2
# 3       4
# 0       6
# 5       7
# 8       9
# 5       9
# 9       12
# 14      18
n = input("nhap so phan tu: ")
a = []
b = []
for i in range(n):
    s = input("start: ")
    e = input("end  : ")
    a.append(s)
    b.append(e)
print "input: \n",a,"\n",b
#sap xep end time theo thu tu tang dan
for i in range(0, n):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
            b[i], b[j] = b[j], b[i]

print "input after sort by end time: \n", a,"\n", b
print "output: "
print a[0],"    ", b[0]
t = 0
for i in range(n):
    if a[i] > b[t]:
        t = i
        print a[i], "    ", b[t]


