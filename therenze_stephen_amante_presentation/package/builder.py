
class Builder:

    def box(self, size):
        y = 0
        while y < size:
            x = 0
            while x < size:
                print("*", end=" ")
                x += 1
            print()
            y += 1

    def triangle(self, size):
        y = 0
        while y < size:
            x = 0
            while x <= y:
                print("*", end=" ")
                x += 1
            print()
            y += 1

    
    def frame(self, size):
        y = 0
        while y < size:
            x = 0
            while x < size:
                if y == 0 or y == size - 1 or x == 0 or x == size - 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
                x += 1
            print()
            y += 1


    def diamond(self, size):
        y = 0
        while y < size:

            print(" " * (size - y), end="")
            # Print the stars
            print("* " * (y + 1))
            y += 1

        y = size - 2
        while y >= 0:

            print(" " * (size - y), end="")
            # Print the stars
            print("* " * (y + 1))
            y -= 1