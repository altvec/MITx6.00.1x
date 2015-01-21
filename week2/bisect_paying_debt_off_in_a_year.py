# Test case 1
balance = 320000
annualInterestRate = 0.2
# Output should be:
# Lowest Payment: 29157.09


def calculate(balance, monthlyPayment):
    monthlyInterestRate = annualInterestRate / 12.0
    for month in range(1, 13):
        unpaidBalance = balance - monthlyPayment
        balance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
    return balance


lowerPayment = balance / 12
upperPayment = (balance * (1 + annualInterestRate / 12) ** 12) / 12.0
payment = (lowerPayment + upperPayment) / 2

while True:
    result = calculate(balance, payment)
    if abs(result - 0.01) < 0.1:
        print "Lowest Payment: " + str(round(payment, 2))
        break
    else:
        if result < 0:
            upperPayment = payment
        elif result > 0:
            lowerPayment = payment
        payment = round((lowerPayment + upperPayment) / 2, 2)
