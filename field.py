# print("using start, stop, and step arguments in Python range() function")
# print("Printing All odd numbers between 1 and 16 using range()")


def add_vectors():
    print("Please type First_coordinate_y in interval 1..16 and press ENTER: ")
    first_coordinate_y = int(input())

    print("Please type first_coordinate_x in interval 1..16 and press ENTER: ")
    first_coordinate_x = int(input())

    print("Please type second_coordinate_y in interval 1..16 and press ENTER: ")
    second_coordinate_y = int(input())

    print("Please type second_coordinate_x in interval 1..16 and press ENTER: ")
    second_coordinate_x = int(input())    

    if first_coordinate_x > 16: 
        print("Please type correct first_coordinate_x in interval 1..16 and press ENTER: ")
        first_coordinate_x = int(input())
    if first_coordinate_y > 16: 
        print("Please type correct First_coordinate_y in interval 1..16 and press ENTER: ")
        first_coordinate_y = int(input())
    if second_coordinate_x > 16: 
        print("Please type correct second_coordinate_x in interval 1..16 and press ENTER: ")
        second_coordinate_x = int(input())
    if second_coordinate_y > 16: 
        print("Please type correct second_coordinate_y in interval 1..16 and press ENTER: ")
        second_coordinate_y = int(input())    

    return first_coordinate_x, first_coordinate_y, second_coordinate_x, second_coordinate_y

VECTORS = add_vectors()
VECTORS = [VECTORS[0], VECTORS[1]]
print(type(VECTORS[0]), type(VECTORS[1]), type(VECTORS[2]), type(VECTORS[3]))

def make_field():
    for n in range(1, 17, 1):
        for k in range(1, 17, 1):        
            road = "--"
            if n == VECTORS[0] and k is VECTORS[1]:
                point = "O"
            else:
                point = "+"
            print(f"{point}{road}", end="")
        print("+")
        if n != 16:
            print("|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |")


