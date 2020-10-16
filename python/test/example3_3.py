score = input("Enter Score: ")
sc = float(score)
if 1.0>=sc>=0.9:
    grade = "A"
elif 0.9>=sc>0.8:
    grade = "B"
elif 0.8>=sc>0.7:
    grade = "C"
elif 0.7>=sc>0.6:
    grade = "D"
elif 0.6>=sc>0.0:
    grade = "F"
else:
    grade= "error"
print(grade)