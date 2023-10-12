month_no = input("Input the no of Month: ")

if month_no== "1":
	print("January 31 days")
elif month_no in ("April", "June", "September", "November"):
	print("No. of days: 30 days")
elif month_no in ("2"):
	print("February 28/29 days")
elif month_no in ("3"):
	print("March 31 days")
elif month_no in ("4"):
	print("April 30 days")
elif month_no in ("5"):
	print("May 31 days")
elif month_no in ("6"):
	print("June 30 days")
elif month_no in ("7"):
	print("July 31 days")
elif month_no in ("8"):
	print("August 31 days")
elif month_no in ("9"):
	print("September 30 days")
elif month_no in ("10"):
	print("October 31 days")
elif month_no in ("11"):
	print("November 30 days")
elif month_no in ("12"):
	print("December 31 days")
else:
	print("Wrong month name") 
