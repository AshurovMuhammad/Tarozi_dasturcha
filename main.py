pol = input("Agar siz erkak kishi bo'lsangiz E xarfini kiriting, Ayol kishi bo'lsangiz A xarfini kiriting!!!\n>>> ")
roat = int(input("Bo'yingiz uzunligini kiriting\n>>> "))

if pol=="E":
    r = int(((roat*4/2.54)-128)*0.453)
elif pol=="A":
    r =int(((roat*3.5/2.54)-108)*0.453)

print(f"Sizning o'rtacha vazningiz\n>>>  {str(r)}")


