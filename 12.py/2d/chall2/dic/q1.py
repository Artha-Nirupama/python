students = {
   "Artha": {"age":21, "marks":85},
   "Nimal": {"age":22, "marks":90},
   "Sahan": {"age":20, "marks":75}
}
Aplus = [x for x in students if students[x]["marks"]>80]
print(Aplus)