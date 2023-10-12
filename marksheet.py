name=str(input("Enter Name="))
standard=float(input("Enter Class="))
section=str(input("Enter Section="))


hindi=float(input("Enter marks of Hindi="))
english=float(input("Enter marks of English="))
maths=float(input("Enter marks of Maths="))
science=float(input("Enter marks of Science="))
sst=float(input("Enter marks of Social Science="))



total=hindi+english+maths+science+sst
avg=int(total/5)



print('Student Name: ',name)
print('Student Class: ',standard)
print('Student Section: ',section)
print('Total marks obtain out of 500: ',total)
print('Average: ',avg)
print('Percentage: ',avg,'%')
				
if(avg>=90):
				 print(name,"got Grade A and Outstanding")
elif(avg>=80 & avg<90):
			 	print(name,"got Grade B and Excellent")
elif(avg>=70 & avg<80):
	 			print(name,"got Grade C and Very Good")
elif(avg>=60 & avg<70):
		 		print(name,"got Grade D and Good")
elif(avg>=50 & avg<60):
		 		print(name,"got Grade E and Average")
else:
 				print(name,"got Grade F and Student is Fail")
	 			
				
				
