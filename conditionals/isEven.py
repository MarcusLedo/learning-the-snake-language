def main():
    x = int(input("What is x?\n"));
    if isEven(x):
        print(f"{x} is even");
    else:
        print(f"{x} is odd");


def isEven(n):
    if n % 2 == 0:
        return True;
    else:
        return False;

main();