students = {
   "Artha": {"age":21, "marks":{"math":85, "science":90}},
   "Nimal": {"age":22, "marks":{"math":75, "science":95}},
   "Sahan": {"age":20, "marks":{"math":65, "science":70}}
}
scienceMarks = [students[x]["marks"]["science"] for x in students]
print(scienceMarks)
answer = [x for x in students if students[x]["marks"]["science"]== max(scienceMarks)]
print(f"The highest science marks has:{answer} and it is {max(scienceMarks)}🥳")
