# prime number

num = int(input("Enter a number: "))

# Prime numbers are greater than 1
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a Prime number")
            break
    else:
        print(num, "is a Prime number")
else:
    print(num, "is not a Prime number")

    

# Even Odd

number = int(input("Enter a number: "))

# Check even or odd
if number % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")

