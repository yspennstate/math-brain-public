from fractions import Fraction
from itertools import combinations
import math, random


def det3(M):
    a,b,c=M[0]; d,e,f=M[1]; g,h,i=M[2]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)


def one_check(seed, m=4, n=5):
    random.seed(seed)
    b=random.randint(-3,3)
    r=[random.randint(-3,3) for _ in range(n)]
    c=[random.randint(-3,3) for _ in range(m)]
    D=[[random.randint(-3,3) for _ in range(n)] for __ in range(m)]

    Z=E2=Omega=0
    for j,k in combinations(range(m),2):
        for p,q in combinations(range(n),2):
            det2=D[j][p]*D[k][q]-D[j][q]*D[k][p]
            G=(-r[p]*(c[j]*D[k][q]-c[k]*D[j][q])
               +r[q]*(c[j]*D[k][p]-c[k]*D[j][p]))
            det=det3([[b,r[p],r[q]],
                      [c[j],D[j][p],D[j][q]],
                      [c[k],D[k][p],D[k][q]]])
            assert det == b*det2+G
            Z += det*det
            E2 += det2*det2
            Omega += G*G

    C2=sum(x*x for x in c)
    R2=sum(x*x for x in r)
    DF2=sum(D[j][p]**2 for j in range(m) for p in range(n))
    Dr=[sum(D[j][p]*r[p] for p in range(n)) for j in range(m)]
    DTc=[sum(D[j][p]*c[j] for j in range(m)) for p in range(n)]
    cDr=sum(c[j]*Dr[j] for j in range(m))
    rhs=(C2*R2*DF2
         -C2*sum(x*x for x in Dr)
         -R2*sum(x*x for x in DTc)
         +cDr*cDr)
    assert Omega == rhs


for seed in range(25):
    one_check(seed)

assert Fraction(1, 768) / 4 == Fraction(1, 3072)
assert Fraction(1, 3072) / 4 == Fraction(1, 12288)
assert Fraction(1, 12288) / 16 == Fraction(1, 196608)
assert 196608 == 3*(2**16)
assert abs(1/math.sqrt(196608)-1/(256*math.sqrt(3))) < 1e-15

zero_endpoint=2*math.sqrt(512*math.sqrt(3))
zero_half=2**(19/4)*3**(1/8)
print('integer_identity_trials=25 PASS')
print('threshold_anchored=', Fraction(1,768))
print('threshold_transverse=', Fraction(1,3072))
print('threshold_colored=', Fraction(1,12288))
print('threshold_disjoint_factor=', Fraction(1,196608))
print('product_threshold=', 1/(256*math.sqrt(3)))
print('zero_anchor_density_endpoint=', zero_endpoint)
print('one_zero_anchor_half_riesz_endpoint=', zero_half)
print('STATUS=PASS')
