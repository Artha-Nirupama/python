students = {
   "Artha": {"age":21, "marks":{"math":85, "science":90}},
   "Nimal": {"age":22, "marks":{"math":75, "science":95}},
   "Sahan": {"age":20, "marks":{"math":65, "science":70}}
}
markslist = {y:students[y]["marks"] for y in students}
print(markslist)
avarageList = [(markslist[x]["math"],markslist[x]["science"])for x in markslist]
print(avarageList)
avge = [sum(x)/2 for x in avarageList]
outList = []
cout = 0
for x in markslist:
    outList.append(f"{x} : {avge[cout]}")
    cout +=1
print(outList)