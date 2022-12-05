x=input("Enter any Date in the form of DD/MM/YYYY= ")
y=input("Enter any Date in the form of DD/MM/YYYY= ")
d1=list(map(int,x.split('/')))
d2=list(map(int,y.split('/')))
leap=[]
nleap=[]
if 1 <= d1[0] <= 31 and 1 <= d1[1] <= 12 and d2[2]:
    if 1 <= d2[0] <= 31 and 1 <= d2[1] <= 12:
        for i in range(d1[-1],d2[-1]):
            if ((i%4 == 0) and (i%100 != 0)) or (i%400 == 0):
                leap.append(i)
            else:
                nleap.append(i)
                print("leap years are= ",leap)
                print("non leap years are=",nleap)
                print("---------------------------")
                print("Choose any one option from given below")
                print("For Print 1st Date you enter early Press 1")
                print("For Print 2nd Date you enter early Press 2")
                print("For Print Leap year List  Press 3")
                print("For Print Non Leap Year List Press 4")
                n= int(input("Choose any one option and type here: "))
                if n==1:
                    print("First Date Enter By you",x)
                elif n==2:
                    print("Second Date Enter By you: ",y)
                elif n==3:
                    print("List of all Leap Years are: ",leap)
                elif n==4:
                    print("List of all Non Leap Years are: ",nleap)
    else:
        print("You are Entring a Wrong Date Please Enter a Valid Date")
else:
    print("You are Entring a Wrong Date, Please Enter a Valid Date")
