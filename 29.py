from math import pi

def partial_volume(h, r=10):
    vol = ((4 * pi * (r**3)) /3) - ( pi * (h**2) * (3*r-h)/3)
    return vol

print(partial_volume(2))