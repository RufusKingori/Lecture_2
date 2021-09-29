#This program computes a given integer power of a given number using a for loop
#The user enters the base number and the exponent
#After each iteration, the exponent is increased by 1,
# and the result is multiplied by the base exponent number of times.

def main():
    base = int(input("Enter the base number:"))
    exponent = int(input("Enter the exponent:"))


    for exponent in range (exponent+1):
        result= base ** exponent

    print("The answer is:",result)
main()

