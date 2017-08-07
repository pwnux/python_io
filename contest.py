# compute the average of score
def classtify(average):
    if average <4.0:
        return "F"
    elif average <5.0:
        return "D"
    elif average <5.5:
        return "D+"
    elif average <6.6:
        return "C"
    elif average <7.0:
        return "C+"
    elif average<8.0:
        return "B"
    elif average <8.5:
        return "B+"
    elif average <9.5:
        return "A"
    else:
        return "A+"

lst_score = []
print "Input \"end\" to finish"
while True:
    sub = raw_input("Input the subject name:")
    if sub.lower() == "end":
        break
    try:
        factor = input("Input the factor:")
        mid_term  = input("Input the mid score:")
        end_term = input("Input the end score:")
    except NameError:
        print "Wrong input!!"
        continue
    for each in (factor,mid_term,end_term):
        if each < 0 or each >10 or not isinstance(each,int):
            print "Wrong input!!"
            continue
    lst_score.append((sub,factor,mid_term,end_term))
    print "----------------"

print "\n"
sum_average = 0
sum_factor = 0
print "subject--factor--mid score--end score--average--classification"
if len(lst_score) == 0:
    print "------------"
else:
    for each in range(0,len(lst_score)):
        average = float(0.3*lst_score[each][2]+0.7*lst_score[each][3])
        sum_average = sum_average+average*lst_score[each][1]
        sum_factor = sum_factor + lst_score[each][1]
        print "{0}--{1}--{2}--{3}--{4}--{5}".format(lst_score[each][0],lst_score[each][1],lst_score[each][2],lst_score[each][3],average,classtify(average))
    print "\n"
    print "------------"
    print "Average:{0}".format(sum_average/sum_factor)


