def val():
    val1=int(input("Enter value 1:"))
    val2=int(input("Enter value 2:"))
    return val1,val2
a=True
while a:
    inp = int(input(
        "Enter 1 for addition\n2 for substraction\n3 for multiplication\n4 for division\nEnter any else key to exit from the loop\n"))
    match inp:
        case 1:
            val1,val2=val()
            print(f"The Addition of {val1} and {val2} is {val1+val2}\n")
        case 2:
            val1, val2 = val()
            print(f"The substraction of {val1} and {val2} is {val1 - val2}\n")
        case 3:
            val1, val2 = val()
            print(f"The multiplication of {val1} and {val2} is {val1*val2}\n")
        case 4:
            val1, val2 = val()
            print(f"The divison of {val1} and {val2} is {val1 / val2}")
            print(f"The divison of {val2} and {val1} is {val2 / val1}\n")
        case _:
              a=False
              print("Exiting from the loop")



