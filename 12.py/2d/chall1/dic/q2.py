student = {
   "Artha": {"age":21, "marks":100},
   "Nimal": {"age":22, "marks":90},
   "Sahan": {"age":20, "marks":75}
}
mark = [student[y]["marks"] for y in student]
for x in student:
    if student[x]["marks"] == max(mark):
        print(x)