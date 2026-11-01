#!/usr/bin/env python3
"""Independent exact verifier for P04 Target-3 ten-window rational certificate.

Uses exact SymPy rationals throughout.  It verifies:
- numerator bidegree (50,20);
- 681 nonzero power-basis monomials;
- positivity on the full rational phase rectangle by tensor Bernstein
  coefficients after midpoint subdivision only in the x-coordinate;
- 18 terminal rectangles, max depth 17;
- the exact minimum terminal Bernstein coefficient archived by P23.
"""
import sympy as sp
from math import comb
from collections import Counter

r,x,u,v = sp.symbols("r x u v")
c10 = sp.Rational(3882594969529,12500000000000)
r0 = sp.Rational(273,62)
r1 = sp.Rational(35501,8062)
x0 = sp.Rational(8062,35501)
x1 = sp.Rational(1)

def g(y):
    return y/(1+y)**2

def phi(y):
    return (r-1)*y/((1+y)**2*(1+r*y)**2)

E10 = g(x/r**4) + sum(phi(r**j*x) for j in range(-4,5))
rat = sp.cancel(E10-c10)
num, den = sp.fraction(rat)
P = sp.Poly(num,r,x,domain=sp.QQ)

assert (P.degree(r),P.degree(x)) == (50,20)
assert len(P.terms()) == 681
assert sp.factor(den) == 12500000000000*(r+x)**2*(r**2+x)**2*(r**3+x)**2*(r**4+x)**2*(x+1)**2*(r*x+1)**2*(r**2*x+1)**2*(r**3*x+1)**2*(r**4*x+1)**2*(r**5*x+1)**2

mapped = sp.Poly(sp.expand(num.subs({
    r:r0+(r1-r0)*u,
    x:x0+(x1-x0)*v
})),u,v,domain=sp.QQ)
n,m = mapped.degree(u), mapped.degree(v)
power = mapped.as_dict()

B = [[sp.Rational(0) for _ in range(m+1)] for _ in range(n+1)]
for i in range(n+1):
    for j in range(m+1):
        s = sp.Rational(0)
        for a in range(i+1):
            for b in range(j+1):
                c = power.get((a,b),sp.Rational(0))
                if c:
                    s += c*sp.Rational(comb(i,a),comb(n,a))*sp.Rational(comb(j,b),comb(m,b))
        B[i][j] = s

def positive(B):
    return all(z>0 for row in B for z in row)

def split_v(B):
    nr = len(B)-1
    mv = len(B[0])-1
    L = [[None]*(mv+1) for _ in range(nr+1)]
    R = [[None]*(mv+1) for _ in range(nr+1)]
    for i,row in enumerate(B):
        levels = [list(row)]
        for _ in range(mv):
            prev = levels[-1]
            levels.append([(prev[j]+prev[j+1])/2 for j in range(len(prev)-1)])
        for k in range(mv+1):
            L[i][k] = levels[k][0]
            R[i][mv-k] = levels[k][-1]
    return L,R

stack=[(B,0,sp.Rational(0),sp.Rational(1))]
leaves=[]
while stack:
    Bb,depth,a,b = stack.pop()
    if positive(Bb):
        leaves.append((depth,a,b,Bb))
        continue
    assert depth < 30
    L,R = split_v(Bb)
    mid=(a+b)/2
    stack.append((R,depth+1,mid,b))
    stack.append((L,depth+1,a,mid))

hist = Counter(depth for depth,_,_,_ in leaves)
mincoef = min(z for _,_,_,Bb in leaves for row in Bb for z in row)

expected_num = int("786400128480726547992413082343997216402987021774739212160171251218345518749939156964037034180935407031588802618149415534081308973415552564120847930076696141126931311191425105616868436561375853459321732081438909868018077549008316631655522639103272417951248525314937093314008108217552729977479820267592921893544456506101472044860466913493920945201445468474380546880261")
expected_den = int("146194183912793161898432677498835630551088292562697847404552302907811541542299773479051008291372894285470858296107878996477581919667871927024269098502844124213668625187131858865138678439757668759930317479702162010194926227796979140446511678846019439812198880918236988641878601617148147037907265936130249959165937022798215569317191808450560")

assert len(leaves) == 18
assert max(hist) == 17
assert hist == Counter({d:1 for d in range(1,17)}) + Counter({17:2})
assert mincoef == sp.Rational(expected_num,expected_den)
assert mincoef > 0

print("bidegree:",(P.degree(r),P.degree(x)))
print("power_terms:",len(P.terms()))
print("terminal_rectangles:",len(leaves))
print("max_depth:",max(hist))
print("depth_histogram:",dict(sorted(hist.items())))
print("min_positive_bernstein:",mincoef)
print("CERTIFICATE_OK")
