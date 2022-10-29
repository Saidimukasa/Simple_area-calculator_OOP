# Finding the Area of circle,retrangle and triangle using the class
class Area:
    def __init__(self,radius,length,breadth,base,height):
     self.radius=radius
     self.length=length
     self.breadth=breadth
     self.base=base
     self.height=height
    def area_circle(self):
        area_of_circle= 3.14*self.radius*self.radius
        return area_of_circle
    def area_rectangle(self):
        area_of_rectangle=self.length*self.breadth
        return area_of_rectangle
    def area_triangle(self):
        area_of_triangle=0.5*self.base*self.height
        return area_of_triangle
    
    def __str__(self):
        return "Area of circle is {} Area of rectangle is {} Area of triangle is {}".format(self.area_circle(),self.area_rectangle(),self.area_triangle())
    
area_of_shapes=Area(5,10,20,30,40)
print(area_of_shapes)
       
     
     
     
     
     