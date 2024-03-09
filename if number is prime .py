# Author : Doha yasser saeed
# Check if number is prime or not
repeat = '1'
while repeat == '1' :
    print("==================\n===Prime Or Not===\n==================")
    num = input("Enter the number :")
    while not num.isdigit() :
        num = input("pls enter another number :")

    num = int(num)
    factors=[]
    i = 1
    while i <= num :
        if num % i == 0 :
            factors.append(i)
        i += 1

    if len(factors) == 2 :
        print("It's a prime number ")
    else:
        print("Not a prime")

    repeat = input("1-repeat again..\n2-Exiting..\n")
    while repeat != '1' and repeat != '2' :
        repeat = input("Enter a valid choice")
    if repeat == '2':
        print("Thanks for using my program ")
        exit()

repeat = '1'
