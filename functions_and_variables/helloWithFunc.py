def main():
    name = input("What is your name? \n")
    hello(name)

def hello(to = "world"):
    print(f"Hello {to}!")


main()