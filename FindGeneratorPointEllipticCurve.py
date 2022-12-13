# This function calculates the y-coordinate of a point on the curve
# with the given x-coordinate, using the formula y^2 = x^3+ax+b (mod p)
def calculate_y_coordinate(x, a, b, p):
  return (x**3 + a * x + b) % p

# This function calculates the generator point for the given elliptic curve
# y^2 = x^3+ax+b (mod p)
def calculate_generator_point(a, b, p):
  for x in range(p):
    # Calculate the y-coordinate for this x
    y = calculate_y_coordinate(x, a, b, p)
    # If the point (x,y) is on the curve, return it as the generator point
    if (y**2) % p == (x**3 + a * x + b) % p:
      return (x, y)

# In my example I had to calculate the generator point for the curve y^2 = x^3+6x+9 (mod 8011)
a = 6
b = 9
p = 8011
generator_point = calculate_generator_point(a, b, p)
print(generator_point)
