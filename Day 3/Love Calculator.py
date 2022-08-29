# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
nama = name1 + name2
nama_setara = nama.lower()
t = nama.count("t")
r = nama.count("r")
u = nama.count("u")
e = nama.count("e")
true = t + r + u + e

l = nama.count("l")
o = nama.count("o")
v = nama.count("v")
e = nama.count("e")
love = l + o + v + e

hasil = int(str(true) + str(love))

if hasil < 10 or hasil > 90:
    print(f"Your score is {hasil}, you go together like coke and mentos.")
elif hasil >=40 and hasil <= 50:
    print(f"Your score is {hasil}, you are alright together.")
else :
    print(f"Your score is {hasil}.")