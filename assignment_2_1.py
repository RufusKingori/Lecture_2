#This program adds 2 to a and assigns the results to b
#Multiplies b times 4 and assigns the results to a
#Divides a by 3.14 and assigns the results to c
#Subtracts 8 from b and assigns the results to a

def main():
    a = int()
    b = int()
    c = int()

    b = 2 + a
    print("b:", b)
    a = b * 4
    print("a:", a)
    c = 3.14 / a
    print("c:", c)
    a = b - 8
    print("a:", a)
main()


