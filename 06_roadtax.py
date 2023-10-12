cp=float(input("Enter the cost price:"));
if cp>100000:
    tr=0.15;
elif cp>50000:
    tr=0.10;
else:
    tr=0.05;
roadtax=(cp*tr);
print(f"Road tax to be paid: Rs {roadtax:.2f}")
