from fractions import Fraction
import sympy as sp
from itertools import product

# ---------- exact cavity formulas ----------
r=sp.symbols('r', positive=True)
p=1-sp.exp(-r)
mean=1-sp.exp(-r)
second=2-2*(r+1)*sp.exp(-r)
q=sp.simplify(second-mean**2)
assert sp.simplify(q-(1-2*r*sp.exp(-r)-sp.exp(-2*r)))==0
pser=sp.series(p,r,0,6)
qser=sp.series(q,r,0,7)
ratser=sp.series(sp.simplify(q/p),r,0,5)
assert sp.limit(q/p,r,0,dir='+')==0
assert sp.expand(qser.removeO()).coeff(r,3)==sp.Rational(1,3)

# ---------- exact Bernoulli cube Doob / ANOVA ----------
states=list(product([0,1], repeat=3))
vals=[Fraction(x) for x in [0,1,3,4,7,9,10,15]]
f=dict(zip(states,vals))

def avg(seq):
    seq=list(seq); return sum(seq,Fraction(0))/len(seq)
mu=avg(f.values())
var=avg((v-mu)**2 for v in f.values())

# conditional expectation E[f | first k bits]
def cond_first(k, prefix):
    return avg(f[x] for x in states if x[:k]==prefix)

doob=[]
prev={( ):mu}
for k in range(1,4):
    current={pref:cond_first(k,pref) for pref in product([0,1], repeat=k)}
    sq=Fraction(0)
    for x in states:
        dk=current[x[:k]] - (prev[x[:k-1]] if k>1 else mu)
        sq += dk*dk/Fraction(8)
    doob.append(sq)
    prev=current
assert sum(doob,Fraction(0))==var

# ANOVA via E[f|X_S] Mobius recursion
subsets=[tuple(i for i in range(3) if mask>>i &1) for mask in range(8)]
components={}
for S in subsets:
    comp={}
    assignments=list(product([0,1], repeat=len(S)))
    for a in assignments:
        ef=avg(f[x] for x in states if tuple(x[i] for i in S)==a)
        val=ef
        for T in subsets:
            if len(T)>=len(S) or not set(T).issubset(S):
                continue
            if T in components:
                ta=tuple(a[S.index(i)] for i in T)
                val-=components[T][ta]
        comp[a]=val
    components[S]=comp

norms={}
for S,comp in components.items():
    if not S:
        norms[S]=Fraction(0)
        continue
    norms[S]=avg(v*v for v in comp.values())
assert sum(norms[S] for S in subsets if S)==var

# exact refresh covariance at survival a=1/2
a=Fraction(1,2)
# centered f
fc={x:f[x]-mu for x in states}
cov=Fraction(0)
for x in states:
    px=Fraction(1,8)
    for y in states:
        trans=Fraction(1)
        for i in range(3):
            trans *= (a if y[i]==x[i] else Fraction(0)) + (1-a)*Fraction(1,2)
        cov += px*trans*fc[x]*fc[y]
rhs=sum((a**len(S))*norms[S] for S in subsets if S)
assert cov==rhs

# integrated coefficients 2 k int exp(-2kt) = 1
for k in (1,2,3):
    t=sp.symbols('t', nonnegative=True)
    assert sp.integrate(2*k*sp.exp(-2*k*t),(t,0,sp.oo))==1

print('PASS')
print('p(r)=', p)
print('E[min(X,r)]=', mean)
print('E[min(X,r)^2]=', second)
print('q(r)=Var(min(X,r))=', q)
print('p series:', pser)
print('q series:', qser)
print('q/p series:', ratser)
print('lim_{r->0+} q/p =', sp.limit(q/p,r,0,dir='+'))
print('cube variance =', var)
print('Doob increments squared =', doob)
print('ANOVA norms =', {str(S):norms[S] for S in subsets if S})
print('refresh covariance a=1/2 =', cov)
print('ANOVA refresh RHS =', rhs)
