def main():
    height = int(input("Height: "))
    drawing_pyramid(height)




def drawing_pyramid(height):
    i = 0
    while i != height:
        i += 1
        print('#' * i, end = "\n")


main()

