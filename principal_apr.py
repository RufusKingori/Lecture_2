#this program computes the value of an investment
#in this case carried 10 years into the future

def main():
    print("This program calculates the future value of a 10 year investment.")

    Principal = int(input("Enter the principal amount:"))
    Annual_Percentage_Rate = float(input("Enter the APR:"))

    for i in range(10):
        Principal = Principal * (1 + Annual_Percentage_Rate)

    print("The future value of the principal is:", Principal)

main()