import math

while True:
    try:
        #get as ext first, not as number
        first = input("enter your first number( or 'q' to quit):")

       #check for 'q' before converting
        if first.lower() == 'q':
          print("bye, the calculator stopped working")
        break


        num1 = float(first)
        num2 = float(input("enter your second number"))

        result = num1 / num2
        print(f"Answer: {result}")
        break

    
    except ValueError:
        print(f"oppps, write only numbers not letters")

    except ZeroDivisionError:
        print(f"divide by numbers greater than zero")

    except Exception:
        print(f"input the right values")




print(f"Thank you for using our calculator")       
                    