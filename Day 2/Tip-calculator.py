print("Welcome to the tip calculator!")
harga = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
orang = int(input("How many people to split the bill?"))

tip_persen = tip / 100
jumlah_tip = harga * tip_persen
jumlah_harga = harga + jumlah_tip
harga_per_orang = jumlah_harga / people
hasil_akhir = round(harga_per_orang, 2)


# FAQ: How to round to 2 decimal places?

# Find the answer in the Q&A here: https://www.udemy.com/course/100-days-of-code/learn/lecture/17965132#questions/13315048


print(f"Each person should pay: ${hasil_akhir}")