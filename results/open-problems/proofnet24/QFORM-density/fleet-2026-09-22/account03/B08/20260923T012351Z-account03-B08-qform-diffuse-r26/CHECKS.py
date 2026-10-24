from fractions import Fraction
import math
import numpy as np

rng=np.random.default_rng(20260923)

# q=1 anchored determinant identity
for _ in range(200):
    b,ro1,ro2,ka1,ka2,d11,d12,d21,d22=rng.normal(size=9)
    M=np.array([[b,ro1,ro2],[ka1,d11,d12],[ka2,d21,d22]])
    C=d11*d22-d12*d21
    rhs=(b*C-ro1*ka1*d22+ro1*ka2*d12
         +ro2*ka1*d21-ro2*ka2*d11)
    assert abs(np.linalg.det(M)-rhs) < 1e-9

# q=2 two-shared determinant identity
for _ in range(200):
    a,b,x,u,v,p,q,z=rng.normal(size=8)
    M=np.array([[a,x,u],[x,b,v],[p,q,z]])
    d=a*b-x*x
    rhs=d*z-a*q*v-b*p*u+x*p*v+x*q*u
    assert abs(np.linalg.det(M)-rhs) < 1e-9

# q=3 principal determinant identity
for _ in range(200):
    a,b,c,x,y,z=rng.normal(size=6)
    M=np.array([[a,x,y],[x,b,z],[y,z,c]])
    rhs=a*b*c+2*x*y*z-a*z*z-b*y*y-c*x*x
    assert abs(np.linalg.det(M)-rhs) < 1e-9

p1=Fraction(4,9375)
p2=Fraction(1,384)
p3=Fraction(2,27)
assert p1/4 == Fraction(1,9375)
assert p1/64 == Fraction(1,150000)
assert p1/256 == Fraction(1,600000)
assert p2/25 == Fraction(1,9600)
assert p3/25 == Fraction(2,675)

q0_constant=6*48**(1/3)
coherent_triangle_factor=(math.sqrt(2/675)/2)**(1/3)
coherent_triangle_constant=2*(3+math.log(8))/coherent_triangle_factor

print('q0_exact_rank3_constant=',repr(q0_constant))
print('coherent_triangle_scale=',repr(coherent_triangle_factor))
print('coherent_triangle_constant=',repr(coherent_triangle_constant))
print('QFORM_B08_R26_CHECK_PASS')
