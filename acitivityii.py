Name = str(input("Enter Your Name:"))
M1 = float(input("Enter Your Module1 marks"))
M2 = float(input("Enter Your Module2 marks"))
M3 = float(input("Enter Your Module3 marks"))
M4 = float(input("Enter Your Module4 marks"))
Attendance = float(input("enter your attendance:"))
# print output for name and attandance
print("Name:",Name)
print(f"Attendence:{Attendance}%")
#processs find percentage
T= (M1+M2+M3+M4)
P= (T/400)*100
#printing percantage
print("Percentage:%.2f" %(P),"%")