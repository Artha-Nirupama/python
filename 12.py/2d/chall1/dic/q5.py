students = {
   "Artha": {"age":21, "marks":85},
   "Nimal": {"age":22, "marks":90},
   "Sahan": {"age":20, "marks":75}
}
tupl = [tuple(f"{y}:{students[y]}") for y in students]
print(tupl)