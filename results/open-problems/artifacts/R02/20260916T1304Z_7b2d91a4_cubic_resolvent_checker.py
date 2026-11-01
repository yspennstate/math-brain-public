from fractions import Fraction
import sympy as sp

print('R02 KLS cubic-resolvent exact checker')

a,b,c = sp.symbols('a b c', positive=True)
U = a*b*c + (c*(a-b)**2 + a*(b-c)**2 + b*(c-a)**2)/6
G = sp.expand((a**3+b**3+c**3)/3 - U)
Schur = sp.expand(a**3+b**3+c**3+3*a*b*c - (a*a*b+a*a*c+b*b*a+b*b*c+c*c*a+c*c*b))
AMGM = sp.expand(a**3+b**3+c**3-3*a*b*c)
assert sp.simplify(6*G - (Schur + AMGM)) == 0
print('symbolic decomposition 6*(avg_cubes-U)=Schur3+AMGM3: PASS')

def family(m):
    assert m >= 2 and isinstance(m, int)
    N = 8*(m**3-m)//3
    assert 3*N == 8*(m**3-m)
    hsum = Fraction(m**3-m,1) + N*(Fraction(1,8)-Fraction(1,2))
    s1 = Fraction(m,1) + N*Fraction(1,2)
    s3 = Fraction(m**3,1) + N*Fraction(1,8)
    assert hsum == 0
    assert s1 == s3
    n=1+N
    assert s3 <= n
    D=4*s3
    return n, Fraction(m,1), s3, D

print('m n qmax sum_q3 D/n')
for m in [2,3,5,10,20,50]:
    n,qmax,s3,D=family(m)
    print(m,n,qmax,s3,D/Fraction(n,1))
for m in range(2,1000):
    n,qmax,s3,D=family(m)
    assert qmax==m
    assert D <= 4*n
n,qmax,s3,D=family(50)
assert qmax==50 and D/Fraction(n,1)<3
print('exact product-family edge obstruction: PASS')
print('all checks PASS')
