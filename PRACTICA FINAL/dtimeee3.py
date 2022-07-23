import datetime

date1 = datetime.datetime(20,11,11)
date2 = datetime.datetime(2028,11,11)

if date1 == date2:
    print("Nacieron el mismo dia")
elif date2 < date1:
    print("El niño 1 es menor que el niño 2")

else:

    print("No nacieron el mismo dia")

