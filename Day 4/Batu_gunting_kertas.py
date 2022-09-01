import random

batu = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

kertas = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

gunting = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

gambar = [batu, kertas, gunting]

milih = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(gambar[milih])

acak = random.randint(0, 2)
print("Computer chose:")
print(gambar[acak])

if milih >= 3 or milih < 0: 
  print("You typed an invalid number, you lose!") 
elif milih == 0 and acak == 2:
  print("You win!")
elif acak == 0 and milih == 2:
  print("You lose")
elif acak > milih:
  print("You lose")
elif milih > acak:
  print("You win!")
elif acak == milih:
  print("It's a draw")