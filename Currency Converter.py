print("Currency Converter")
print("1. Rupees to Dollars")
print("2. Dollars to Rupees")
print("3. Euros to Dollars")
print("4. Dollars to Euros")
choice = int(input("Enter your choice: "))

def rtd():
    rupees = float(input("Enter Rupees: "))
    conversion = rupees*85.53
    print(conversion)

def dtr():
    dollars = float(input("Enter Dollars: "))
    conversion = dollars*0.012
    print(conversion)

def etr():
    euros = float(input("Enter Euros: "))
    conversion = euros*1.10
    print(conversion)

def rte():
    dollars = float(input("Enter Dollars: "))
    conversion = dollars*0.91
    print(conversion)

if choice == 1:
    rtd()
elif choice == 2:
    dtr()
elif choice == 3:
    etr()
elif choice == 4:
    rte()    