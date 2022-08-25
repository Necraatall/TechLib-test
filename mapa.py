# Python3 program to implement printing map of city for the travelling salesmen
def add_vectors():
    print("Please type first_coordinate_y for position of Pharmacy in interval 1..16 and press ENTER: ")
    first_coordinate_y = int(input())

    print("Please type first_coordinate_x for position of Pharmacy in interval 1..16 and press ENTER: ")
    first_coordinate_x = int(input())

    print("Please type second_coordinate_y for position of Food Shop in interval 1..16 and press ENTER: ")
    second_coordinate_y = int(input())

    print("Please type second_coordinate_x for position of Food Shop in interval 1..16 and press ENTER: ")
    second_coordinate_x = int(input())    

    if first_coordinate_x > 16: 
        print("Please type correct first_coordinate_x for position of Pharmacy in interval 1..16 and press ENTER: ")
        first_coordinate_x = int(input())
    if first_coordinate_y > 16: 
        print("Please type correct first_coordinate_y for position of Pharmacy in interval 1..16 and press ENTER: ")
        first_coordinate_y = int(input())
    if second_coordinate_x > 16: 
        print("Please type correct second_coordinate_x for position of Food Shop in interval 1..16 and press ENTER: ")
        second_coordinate_x = int(input())
    if second_coordinate_y > 16: 
        print("Please type correct second_coordinate_y for position of Food Shop in interval 1..16 and press ENTER: ")
        second_coordinate_y = int(input())    

    return first_coordinate_x, first_coordinate_y, second_coordinate_x, second_coordinate_y

VECTORS = add_vectors()
VECTORS = [VECTORS[0], VECTORS[1], VECTORS[2], VECTORS[3]]

# Prints on the shell output the map of city with the points to travel
def make_field():
    for n in range(1, 17, 1):
        for k in range(1, 17, 1):        
            road = "--"
            if (n == VECTORS[0] and k is VECTORS[1]) or (n == VECTORS[2] and k is VECTORS[3]):
                point = "X"
            else: point = "+"
        
            print(f"{point}{road}", end="")

        print("+")
        if n != 16:
            print("|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |")


# Driver Code
if __name__ == "__main__":
    make_field()
