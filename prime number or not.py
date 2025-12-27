num1 = int(input("Enter a number: "))

if num1 > 1:
    for i in range(2, num1):
        if num1 % i == 0:
            print("Not a prime number")
            break
    else:
        print("It is a prime number")
else:
    print("Not a prime number")