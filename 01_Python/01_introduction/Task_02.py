import math

#Circle Area Funcion
def circle_area (radius = 0):
    circle_area = 2 * math.pi * (radius ** 2)
    return circle_area

while True:
    radius = float(input(' Please enter a postive circle radius: '))
    if radius >= 0:
        break

print('Circle area = ', circle_area(radius))
        
                