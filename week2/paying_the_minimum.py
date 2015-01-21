# Test 1
balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
# Output should be:
# Month: 1
# Minimum monthly payment: 168.52
# Remaining balance: 4111.89
# ...
# Month: 12
# Minimum monthly payment: 129.0
# Remaining balance: 3147.67
# Total paid: 1775.55
# Remaining balance: 3147.67

monthlyInterestRate = annualInterestRate / 12.0
totalPaid = 0
for month in range(1, 13):
    print "Month:", month
    monthlyPayment = monthlyPaymentRate * balance
    unpaidBalance = balance - monthlyPayment
    balance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
    print "Minimum monthly payment:", round(monthlyPayment, 2)
    print "Remaining balance:", round(balance, 2)
    totalPaid += monthlyPayment
print "Total paid:", round(totalPaid, 2)
print "Remaining balance:", round(balance, 2)
