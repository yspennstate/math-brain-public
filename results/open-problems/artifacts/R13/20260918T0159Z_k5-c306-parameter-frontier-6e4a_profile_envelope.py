from fractions import Fraction
from math import ceil, sqrt, pi
M=[0,5,16,29,48,61,80,101,128,133,144,157,176,189,208,229,256]
c=Fraction(153,500)
old=Fraction(303,1000)

def parts(total,q,minv=1):
    out=[]
    def rec(rem,k,lo,a):
        if k==0:
            if rem==0: out.append(tuple(a))
            return
        for x in range(lo, rem//k+1): rec(rem-x,k-1,x,a+[x])
    rec(total,q,minv,[]); return out

def energy(p):
    z=Fraction(0)
    for k in p: z += Fraction(k*k,M[k])
    return z

q4=[p for p in parts(16,4) if energy(p)<5*c]
q5=[p for p in parts(16,5) if energy(p)<5*c]
q6min=min((energy(p),p) for q in range(6,17) for p in parts(16,q))
assert q6min==(Fraction(49,30),(1,1,1,1,4,8))
assert q6min[0]-5*c==Fraction(31,300)
assert 3*c<1
assert len(q4)==34
assert len(q5)==11

def bound(n,cc):
    if n==1:return 1.0
    if n==2:return sqrt(2)
    if n==3:return (sqrt(11)+sqrt(2))/3
    if n==4:return sqrt(3)
    if 5<=n<=85:return min(sqrt(3*n/4),sqrt(ceil(n/5)/float(cc)))
    return 3*sqrt(2*pi)
imp=[n for n in range(1,200) if bound(n,c)<bound(n,old)-1e-12]
assert imp==[5,9,10,14,15,18,19,20,22,23,24,25]+list(range(27,86))
assert len(imp)==71
# Crossover checks without relying on decimal pi: 333/106 < pi < 22/7.
assert Fraction(17,1)/c < 18*Fraction(333,106)
assert Fraction(18,1)/c > 18*Fraction(22,7)
print('c=',c,'K5_upper=sqrt(500/153)=',sqrt(500/153))
print('q4_profiles=',len(q4),q4)
print('q5_profiles=',len(q5),q5)
print('q>=6_min=',q6min,'gap=',q6min[0]-5*c)
print('improved_dimensions_count=',len(imp))
print('improved_dimensions=',imp)
print('crossover=finite through n=85; universal from n=86')
print('R13_K5_C306_PROFILE_ENVELOPE_EXACT_PASS')
