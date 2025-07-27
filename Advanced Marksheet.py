name= input ("Enter Name:")
rollno= int (input ("Enter Roll No:"))
standard= int (input ("Enter Class:"))
gender= input ("Enter Gender:")
english= int (input ("Enter English Marks:"))
maths= int (input ("Enter Maths Marks:"))
physics= int (input ("Enter Physics Marks:"))
urdu= int (input ("Enter Urdu Marks:"))
pst= int (input ("Enter Pst Marks:"))
chemsitry= int (input ("Enter Chemistry Marks:"))
obtained_marks= english + maths + physics + urdu + pst + chemsitry
percentage= obtained_marks/550*100

print ("\033[1;31;40m--------------MARKSHEET--------------")
print ("\033[1;37;40mYour Name is:" + name)
print ("\033[1;37;40mYour Roll No is:" + str(rollno))
print ("\033[1;37;40mYour Class is:" + str(standard))
print ("\033[1;37;40mYour Gender is:" + gender)
print ("\033[1;37;40mTotal Marks Are: 550")
print ("\033[1;37;40mObtained Marks Are:"+ str(obtained_marks))
print ("\033[1;37;40mYour Percentage is:"+ str(percentage))

if (percentage>=80):
    print ("Grade: A-1")
    print ("Remarks: Excellent")
elif (percentage>=70):
    print ("Grade: A")    
    print ("Remarks: Good")
elif (percentage>=60):
    print ("Grade: B") 
    print ("Remarks: Fair but Need some Improvement")
elif (percentage>=50):
    print ("Grade: C") 
    print ("Remarks:  Improve")
elif (percentage>=40):
    print ("Grade: D") 
    print ("Remarks: Poor, Work Hard")
elif (percentage>=33):
    print ("Grade: E") 
    print ("Remarks: Keep Studying and Try Again")
else:
    print ("Grade: F")
    print ("Remarks: Get Better")

a = 0
subjects_name = ""

if (english < 33):
    a += 1
    subjects_name += "English, "

if (maths < 33):
    a += 1
    subjects_name += "Maths, "

if (physics < 33):
    a += 1
    subjects_name += "Physics, "

if (urdu < 33):
    a += 1
    subjects_name += "Urdu, "

if (pst < 33):
    a += 1
    subjects_name += "PST, "

if (chemsitry < 33):
    a += 1
    subjects_name += "Chemistry, "

if a > 0:
     print("Failed Subject Counts:" + str(a))
     print("Failed Subject Names:\n" + subjects_name)