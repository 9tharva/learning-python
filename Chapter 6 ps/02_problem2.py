marks1 = int(input("Enter marsk1: "))
marks2 = int(input("Enter marsk2: "))
marks3 = int(input("Enter marsk3: "))

#Check total percentage
total_percentage = (100*(marks1 + marks2 + marks3))/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33 ):
    print("you are passed", total_percentage)

else:
    print("yoy failed, try again next year:", total_percentage)


