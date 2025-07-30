print(" Calculator")
a=int(input("enter the number a:"))
b=int(input("enter the number b:"))
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulus")
choice=input(" enter the choice")
if choice == '1':
    c=a+b
    print("Addition",c)
elif choice == '2':
     print("Choose Subtraction Type")
     print("1.a-b")
     print("2.b-a")
     sub_choice=input("enter your choice")
     if sub_choice == '1':
        c = a - b
        print("Subtraction (a-b)",c)
     elif sub_choice == '2':
            c = b - a
            print("Subtraction (b-a)",c)
     else:
                print("invalid")

elif choice == '3':
    c=a*b
    print("Multiplication",c)
elif choice == '4':
    print("Choose division Type")
    print("1.a/b")
    print("2.b/a")
    sub_choice=input("enter your choice")
    if sub_choice == '1':
        if b != 0:
            c = a / b
            print("Division (a/b)",c)
        else:
            print("error Try again !")
    elif sub_choice == '2':
        if a != 0:
            c = b / a
            print("Division (a/b)",c)
        else:
            print("error Try again ")
elif choice == '5':
    c=a%b
    print("Modulus",c)
else:
    print("CHOICE IS WRONG TRY AGAIN")
