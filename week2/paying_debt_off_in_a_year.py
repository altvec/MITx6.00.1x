# Test case 1
balance = 3329
annualInterestRate = 0.2
# Output should be:
# Lowest Payment: 310


def calculate(balance, monthlyPayment):
    monthlyInterestRate = annualInterestRate / 12.0
    for month in range(1, 13):
        unpaidBalance = balance - monthlyPayment
        balance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
    return balance

payment = 10

while calculate(balance, payment) > 0:
    payment += 10

print "Lowest Payment: %d" % payment
