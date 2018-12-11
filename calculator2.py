x = int(raw_input("Enter the value for x: "))
print x

y = int(raw_input("Enter the value for y: "))
print y

operation = raw_input("Choose math operation (+, -, *, /: ")
print operation

if operation == "+":
    print "osszeadas"
    print x + y
elif operation == "-":
    print "kivonas"
    print x - y
elif operation == "*":
    print "szorzas"
    print x * y
elif operation == "/":
    print "osztas"
    print x / y
else:
    print "You did not provide the correct math operation."