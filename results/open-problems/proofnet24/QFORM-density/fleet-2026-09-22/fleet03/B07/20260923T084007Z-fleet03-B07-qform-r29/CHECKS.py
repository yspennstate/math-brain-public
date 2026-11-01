from fractions import Fraction
from math import sqrt, e
import random

random.seed(20260923)

def norm2(M):
    return sum(x*x for row in M for x in row)

def matrand(m,n):
    return [[random.randint(-5,5) for _ in range(n)] for _ in range(m)]

delta = Fraction(1,4)
tau = Fraction(1,16)
theta = Fraction(1,16)
c0 = 286654464
mu0 = theta**4 / c0
star_floor = delta**2 * mu0
nu = tau * (1-delta)**2 * mu0 / 8
anchor3_floor = nu / 3
Cvol = (9*sqrt(3)*e/2) * float(1/nu)**(1/6)
star_density_coeff = 4*sqrt(1/float(star_floor))

print("mu0 =", mu0)
print("star_floor =", star_floor)
print("nu =", nu)
print("anchor3_floor =", anchor3_floor)
print("volume_density_coefficient =", f"{Cvol:.12f}")
print("star_projection_density_coefficient =", f"{star_density_coeff:.12f}")

viol=0
min_ratio=1e100
for _ in range(10000):
    A=matrand(2,2); B=matrand(2,4); C=matrand(3,2); D=matrand(3,4)
    M4=norm2(A)*norm2(D)
    M5=norm2(B)*norm2(C)
    W=0
    H=[[0,0],[0,0]]
    for h in range(2):
      for l in range(2):
       s=0
       for r in range(3):
        for t in range(4):
         z=A[h][l]*D[r][t]-B[h][t]*C[r][l]
         s += z*z
       H[h][l]=s
       W += s
    rhs=(sqrt(M4)-sqrt(M5))**2
    if W+1e-9 < rhs: viol += 1
    if M4>0 and M5 < float(delta*delta)*M4:
        if not (W > float((1-delta)**2)*M4-1e-9):
            viol += 1
        if max(max(row) for row in H)+1e-9 < W/4:
            viol += 1
    if M4>0:
        min_ratio=min(min_ratio,(W**0.5 + M5**0.5)/(M4**0.5))
print("random_cases = 10000")
print("violations =",viol)
print("reverse_triangle_min_ratio =",f"{min_ratio:.12f}")
print("STATUS=PASS" if viol==0 else "STATUS=FAIL")
