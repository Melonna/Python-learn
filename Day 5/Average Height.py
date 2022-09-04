# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_berat = 0
for height in student_heights:
    total_berat += height

jumlah_orang = 0
for student in student_heights:
    jumlah_orang += 1

rata_rata = round(total_berat / jumlah_orang)
print(rata_rata)



