def getBezout(x,y):
    (s1, t1, r1, s2, t2, r2) = ( 0, 1, y, 1, 0, x )
    while (r1 != 0):
        q = r2 // r1
        (r2, r1) = (r1, r2 - q * r1)
        (s2, s1) = (s1, s2 - q * s1)
        (t2, t1) = (t1, t2 - q * t1)
   
    # r2 = gcd(x,y) but we don't need this!
   
    return ((s2, t2))

positions = ( 17, 19, 7, 13, 5, 3, 11 )
current = ( 5, 8, 1, 7, 1, 0, 0  )


# Create the system of linear equations of the form t = a(i) mod n(i)

equations = []

for i in range(len(positions)):
    equations.append(((-1-i-current[i]) % positions[i], positions[i]))

while (len(equations) > 1):
    eq1 = equations.pop()
    eq2 = equations.pop()
    m = getBezout(eq1[1], eq2[1])
    a = eq1[0]*m[1]*eq2[1] + eq2[0]*m[0]*eq1[1]
 
    equations.append((a, eq1[1]*eq2[1]))

print(a % equations[0][1])