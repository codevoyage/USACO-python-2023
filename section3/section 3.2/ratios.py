"""
ID: shikha11
LANG: PYTHON3
TASK: ratios
"""
import math

fin = open('ratios.in', 'r')
fout = open('ratios.out', 'w')


# Function to find the LCM of two numbers
def lcm(x, y):
    return abs(x * y) // math.gcd(x, y)


goal = list(map(int, fin.readline().strip().split()))
mixtures = []
for _ in range(3):
    mixtures.append(list(map(int, fin.readline().strip().split())))

# Solve the system of equations using Cramer's rule
a11, a12, a13 = mixtures[0]
a21, a22, a23 = mixtures[1]
a31, a32, a33 = mixtures[2]
b1, b2, b3 = goal

D = a11 * (a22 * a33 - a23 * a32) - a12 * (a21 * a33 - a23 * a31) + a13 * (a21 * a32 - a22 * a31)

D1 = b1 * (a22 * a33 - a23 * a32) - b2 * (a21 * a33 - a23 * a31) + b3 * (a21 * a32 - a22 * a31)
D2 = a11 * (b2 * a33 - b3 * a32) - a12 * (b1 * a33 - b3 * a31) + a13 * (b1 * a32 - b2 * a31)
D3 = a11 * (a22 * b3 - a23 * b2) - a12 * (a21 * b3 - a23 * b1) + a13 * (a21 * b2 - a22 * b1)

# Check if D is zero, indicating no solution
if D == 0:
    fout.write("NONE\n")
else:
    # Calculate the common factor
    common_factor = math.gcd(D, math.gcd(D1, math.gcd(D2, D3)))

    # Divide all values by the common factor
    D //= common_factor
    D1 //= common_factor
    D2 //= common_factor
    D3 //= common_factor

    # Check if any of the values are negative
    if D*D1*D2*D3 < 0:
        fout.write("NONE\n")
    else:
        fout.write(f"{abs(D1)} {abs(D2)} {abs(D3)} {abs(D)}\n")

fin.close()
fout.close()


