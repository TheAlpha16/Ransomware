
def jacobi(eq1, eq2, eq3, ini_sol):
    a11, a12, a13, b01 = eq1[0], eq1[1], eq1[2], eq1[3]
    a21, a22, a23, b02 = eq2[0], eq2[1], eq2[2], eq2[3]
    a31, a32, a33, b03 = eq3[0], eq3[1], eq3[2], eq3[3]
    p, q, r = ini_sol[0], ini_sol[1], ini_sol[2]

    x = (b01 - (a12 * q) - (a13 * r)) / a11
    y = (b02 - (a21 * p) - (a23 * r)) / a22
    z = (b03 - (a31 * p) - (a32 * q)) / a33

    return [x, y, z]


Eq1 = input()
Eq2 = input()
Eq3 = input()
initial_sol = [0, 0, 0]

p1 = jacobi(Eq1, Eq2, Eq3, initial_sol)
p2 = jacobi(Eq1, Eq2, Eq3, p1)
p3 = jacobi(Eq1, Eq2, Eq3, p2)
p4 = jacobi(Eq1, Eq2, Eq3, p3)
p5 = jacobi(Eq1, Eq2, Eq3, p4)
p6 = jacobi(Eq1, Eq2, Eq3, p5)
p7 = jacobi(Eq1, Eq2, Eq3, p6)

print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print(p6)
