# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
a = int(age)
hasil = 90 - a
hari = 365*hasil
minggu = 52*hasil
bulan = 12*hasil
hasil_akhir = f"You have {hari} days, {minggu} weeks, and {bulan} months left."
print(hasil_akhir)