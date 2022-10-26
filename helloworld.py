import sys
def factorial(num):
    if(num==0):
        return 1
    else:
        return num * factorial(num-1)
if __name__ == "__main__":
    print(f"Given arguments through command line are:", sys.argv)
    lst = [int(i) for i in sys.argv[1:]]
    for num in lst:
        result = factorial(num)
        print(f"The factorial of {num} is {result}")

