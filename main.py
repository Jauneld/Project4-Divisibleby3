count = int(input("How many numbers do you need to check? "))
non = 0
yes = 0
for i in range(0,count):
    num = int(input("Enter number: "))
    divi = num % 3
    if divi == 0:
        print(str(num) + " is divisible by 3.")
        yes = yes + 1
    else:
        print(str(num) + " is not divisible by 3.")
        non = non + 1
print("You entered " + str(yes) + " number(s) that are divisible by 3.")
print("You entered " + str(non) + " number(s) that are not divisible by 3.")