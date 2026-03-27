# cheking status and asking 
if P>=90 and Attendance>=80 and M1>=90 and M2 >=90 and M3>=90 and M4>=90:
    print("Grade:A [Excellent]. \n You are elible for reward.\n Status:Pass")
elif P>=75 and Attendance>=80 and M1>=75  and M2>=75 and M3>=75 and M4>=75:
    print("Grade:B[Very Good]. \n you are eligible for reward. \n Status:Pass ")
elif  P>=60 and Attendance>=80 and M1>=60  and M2>=60 and M3>=60 and M4>=60:
    print("Grade:C[Good]. \n you are eligible for reward. \n Status:Pass")
elif  P>40 and Attendance>=80 and M1>=40  and M2>=40 and M3>=40 and M4>=40:
    print("Grade:D[Standard]. \n you are eligible for reward. \n Status:Pass")
else:
    print("Grade F[NEED IMPROVEMENT!!!].\n you are Not eligible for reward. \n Status:Fail")