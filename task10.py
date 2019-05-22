class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area_rect(self):
        area = self.length*self.width
        print("The area of rectangle: ", area)
        

length = float(input("Enter the length of the rectangle "))
width = float(input("Enter the width of the rectangle "))
r = Rectangle(length, width)
r. area_rect()



