a = int(input("Enter your age: "))

#if elif else ladder

if(a>18):
    print("you are above the age of consent")
    print("Good for you")

elif(a<0):
    print("You are entering invalid age")

elif(a==0):
    print("you are entering invalid age")

else:
    print("You are below the age of consent")

print("end of program")