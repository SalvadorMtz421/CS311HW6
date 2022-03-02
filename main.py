# Salvador Martinez CS311 Homework 6

#============== Number 2
price = 109.99*5
tax = .12*(109.99*5)
print(price+tax)

#=============== Number 3
examScore = float(input("Enter your Exam Score: "))
if examScore >= 90:
    print("Your Grade is an A.")

if examScore >= 80 and examScore <= 89:
    print("Your Grade is an B.")

if examScore >= 70 and examScore <= 79:
    print("Your Grade is an C.")

if examScore >= 60 and examScore <= 69:
    print("Your Grade is an D.")

if examScore < 60:
    print("Your Grade is an F.")

#============ Number 4

def tipCalculator():
    billTotal = float(input("Please enter your Bill Total: "))
    tipPercentage = float(input("Please enter your Tip in % format: "))
    tipInDecimal = tipPercentage * 0.01
    print("Your Tip is: $", round(billTotal * tipInDecimal, 2))

tipCalculator()

#============ Number 5

list = [2,4,6,8,10,12,14]
for x in list:
    print(x*5)

#============== Number 6

def isGreaterThan(array, arraySize, n) :
    for x in range(arraySize+1):
        if x > n:
            print(x)
            continue

myArray = [1,2,3,4,5]
n = 2
isGreaterThan(myArray,len(myArray),n)

