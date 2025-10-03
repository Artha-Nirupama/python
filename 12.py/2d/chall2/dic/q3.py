students = {
   "Artha": {"age":21, "marks":85},
   "Nimal": {"age":22, "marks":90},
   "Sahan": {"age":20, "marks":75}
}
List_Tuple = [(x,students[x]["age"],students[x]["marks"]) for x in students]
print(List_Tuple)