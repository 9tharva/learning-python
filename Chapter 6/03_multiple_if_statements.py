a = int(input("Enter your age: "))

#if statement 1

if(a%2 == 0):
    print("a is even")

#end of if statement 1

#if statement 2

if(a>=18):
    print("You are above the age of 18")

elif(a<0):
    print("you are entering invalid age")

else:
    print("You are below the age of consent")

#end of if statement 2

print("end of program")