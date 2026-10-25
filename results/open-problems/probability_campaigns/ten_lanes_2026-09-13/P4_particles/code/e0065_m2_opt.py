# E0065 control: lambda_2 = sup over non-regular QSO on S^1 of min_{i,j,k} P_{ij,k}
# f(x) = A x^2 + 2B x(1-x) + C(1-x)^2 ; entries {A,1-A,B,1-B,C,1-C}
from fractions import Fraction as Fr
import math, itertools, random

def f(A,B,C,x): return A*x*x + 2*B*x*(1-x) + C*(1-x)**2
def fp(A,B,C,x): return 2*A*x + 2*B*(1-2*x) - 2*C*(1-x)

def fixed_point(A,B,C):
    # solve a x^2 + (b-1) x + C = 0 with a=A-2B+C, b=2B-2C ; unique root in (0,1)
    a = A-2*B+C; b = 2*B-2*C-1.0; c = C
    if abs(a) < 1e-14:
        return -c/b
    disc = b*b-4*a*c
    if disc < 0: return None
    s = math.sqrt(disc)
    for r in ((-b+s)/(2*a), (-b-s)/(2*a)):
        if -1e-12 <= r <= 1+1e-12: return r
    return None

def mn(A,B,C): return min(A,1-A,B,1-B,C,1-C)

best=(-1,None)
random.seed(7)
# coarse grid then local refine: maximize mn subject to f'(p) <= -1
N=220
for i in range(N+1):
    A=i/N
    for j in range(N+1):
        B=j/N
        for k in range(N+1):
            C=k/N
            m=mn(A,B,C)
            if m<=best[0]: continue
            p=fixed_point(A,B,C)
            if p is None: continue
            if fp(A,B,C,p) <= -1.0:
                best=(m,(A,B,C,p))
print("grid best:",best)

# local refine by random search around best
A0,B0,C0,_=best[1]
cur=best
for scale in (0.02,0.005,0.001,2e-4,5e-5,1e-5):
    for _ in range(400000):
        A=min(1,max(0,cur[1][0]+random.uniform(-scale,scale)))
        B=min(1,max(0,cur[1][1]+random.uniform(-scale,scale)))
        C=min(1,max(0,cur[1][2]+random.uniform(-scale,scale)))
        m=mn(A,B,C)
        if m<=cur[0]: continue
        p=fixed_point(A,B,C)
        if p is None: continue
        if fp(A,B,C,p) <= -1.0:
            cur=(m,(A,B,C,p))
print("refined:",cur)
print("(3-sqrt7)/2 =",(3-math.sqrt(7))/2)
