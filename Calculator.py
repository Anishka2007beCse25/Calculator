import math
print("---Simple Calculator---")
print("operations available:")
print("1 for (+)")
print("2 for (-)")
print("3 for (*)")
print("4 for (/)")
print("5 for(^)")
print("6 for math.sin(x)")
print("7 for math.cos(x)")
print("8 for math.tan(x)")
print("9 for math.sqrt(number)")
print("10 for inverse sin (arcsin)")
print("11 for inverse cos (arccos)")
print("12 for inverse tan (arctan)")
print("13 for logarithm base 10 (log)")
print("14 for natural logarithm (ln)")
print("15 for antilog (base 10)")
print("16 for antilog(natural base e)")
print("17 for Show PI(3.14)")
print("18 for show e")

choice = input("\nEnteryour choice (1-18): ")

if choice == "1":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result =", a + b)

elif choice == "2":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result =", a - b)

elif choice == "3":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result =", a * b)

elif choice == "4":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if b != 0:
        print("Result =", a / b)
    else:
        print("Error: Division by zero!")

elif choice == "5":
    a = float(input("Enter base number: "))
    b = float(input("Enter exponent: "))
    print("Result =", a ** b) # Use ** for exponentiation

elif choice == "6":
    a = float(input("Enter angle in degrees: "))
    print(f"sin({a}) =", math.sin(math.radians(a))) # Use f-string for better printing

elif choice == "7":
    a = float(input("Enter angle in degrees: "))
    print(f"cos({a}) =", math.cos(math.radians(a))) # Use f-string for better printing

elif choice == "8":
    a = float(input("Enter angle in degrees: "))
    print(f"tan({a}) =", math.tan(math.radians(a))) # Use f-string for better printing

elif choice == "9":
    a = float(input("Enter number: "))
    if a >= 0:
        print(f"sqrt({a}) =", math.sqrt(a)) # Use f-string for better printing
    else:
        print("Error: Square root of negative number is undefined!")

elif choice == "10":
    a = float(input("Enter value between -1 and 1: "))
    if -1 <= a <= 1:
        print(f"arcsin({a}) =", math.degrees(math.asin(a))) # Use math.asin for arcsin, convert to degrees
    else:
        print("Error: Input for arcsin must be between -1 and 1!")

elif choice == "11":
    a = float(input("Enter value between -1 and 1: "))
    if -1 <= a <= 1:
        print(f"arccos({a}) =", math.degrees(math.acos(a))) # Use math.acos for arccos, convert to degrees
    else:
        print("Error: Input for arccos must be between -1 and 1!")

elif choice == "12":
    a = float(input("Enter number: "))
    print(f"arctan({a}) =", math.degrees(math.atan(a))) # Use math.atan for arctan, convert to degrees

elif choice == "13":
    num = float(input("Enter positive number: "))
    if num > 0:
        print(f"log10({num}) =", math.log10(num))
    else:
        print("Error: Log undefined for non-positive numbers!")

elif choice == "14":
    num = float(input("Enter positive number: "))
    if num > 0:
        print(f"ln({num}) =", math.log(num)) # math.log is natural logarithm
    else:
        print("Error: ln undefined for non-positive numbers!")

elif choice == "15":
    num = float(input("Enter number: "))
    print(f"10^({num}) =", 10 ** num) # Antilog base 10 is 10 raised to the power

elif choice == "16":
   num = float(input("Enter number: "))
   print(f"e^({num}) =", math.exp(num)) # Antilog natural base e is math.exp()

elif choice == "17":
    print("PI =", math.pi) # print math.pi directly

elif choice == "18":
    print("e =", math.e) # print math.e directly

else:
    print("Invalid choice! Please select from 1-18.")
    