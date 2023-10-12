units=(float(input("Enter units:")));
def calculateBill(units):

    if (units <= 100):
	
        print( units * 0);
	
    elif (units <= 200):
	
        print((100 * 5) +	(units - 100) * 5);
	
    elif (units <= 300):
        print((100 * 5) +(100 * 5 +(units - 200) * 10));
	
    elif (units > 300):
        print((100 * 5) +(100 * 5 +(100 * 5) +(units - 300) * 10));
    else:
        print("invalid");
print((calculateBill(units)));
