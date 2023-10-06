import math

num1 = 12
num2 = 18

gcd = math.gcd(num1, num2)
lcm = num1 * num2 // gcd

print(f"GCD: {gcd}")
print(f"LCM: {lcm}")
