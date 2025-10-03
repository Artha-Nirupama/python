import random 
students = {
   "Artha": {"age":21, "marks":{"math":85, "science":90}},
   "Nimal": {"age":22, "marks":{"math":75, "science":95}},
   "Sahan": {"age":20, "marks":{"math":65, "science":70}}
}
for x in students:
    mark = random(50,100)
    students[x].append("marks":"english":mark)