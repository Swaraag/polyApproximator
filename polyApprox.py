# sin function for angles between 0 and pi/4 radians
# function that translates given input into a value between 0 and pi/4, which can then be multiplied/divided/negatived into the correct answer
# input is x. x % 2pi. if that value is above pi, then value is negative. if value is below pi, it is positive. then do that value modulus of pi/4 to get it into the first quadrant. Then we
# Cos function that just does sin(90-x) using the function that is mentioned right above
# Tan function that divides sin by cos
# Take x and modulus by 2pi. This will give you a value within the range of 0 and 2pi. Then, use an if statement to check whether the value is above or below pi. If it’s within 0 and pi, then the sin value will be positive. If it is between pi and 2pi, the sin value will be negative. Then, take the modulus of pi/2 so that the value is within the first quadrant. Then, if that value is between 0 and pi/4, then we can use the approxSin(x) function to find that value. If the value is between pi/4 and pi/2, take pi/2 - the value, which will get it into the range of 0 and pi/4: we know that this value’s cosine is equal to the sine of the value we want to get. Therefore, we can use the pythagorean theorem, knowing that this sin(x) = cos(90-x), and take sqrt(1-sin(90-x)), which will get us cos(90-x).


import numpy as np

pi = np.pi

x = (1000 % (2*pi))
x %= (pi/2)

# if betterX is greater than pi/4, betterXX = pi/2 - betterX. This value's cos is equal to the sin of the value we want. Find the sin of betterXX, and use pythagorean theorem (sqrt(1-sin(betterXX)), which would get cosin of that value, which is equal to the sin of the intended value)
