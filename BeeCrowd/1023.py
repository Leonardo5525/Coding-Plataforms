a,b,c = input().split()
a = float(a)
b = float(b)
c = float(c)

delta = b**2 - 4*a*c

r1 = (-1*(b) + delta**0.5)/2*a
r2 = (-1*(b) - delta**0.5)/2*a

print(r1)
print(r2)