alter=int(input("Alter:"))
note=float(input("Abschlussnote:"))
if alter>=20 and alter<=50 and note>=80 and note<=100:
  print("einstellen.")
else:
  print("ablehnen.")