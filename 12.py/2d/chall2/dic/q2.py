students = {
   "Artha": {"age":21, "marks":85},
   "Nimal": {"age":22, "marks":90},
   "Sahan": {"age":20, "marks":75}
}    
        
for x in students:
    if students[x]["marks"]>=90:
        grades = "A"
    elif students[x]["marks"]>75:
        grades = "B"
    else:
        grades = "C"
    students[x].update({"Grade":grades})
print(students)