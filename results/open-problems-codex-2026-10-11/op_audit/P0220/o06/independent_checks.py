from pathlib import Path
import math, itertools, bisect, json, random
from fractions import Fraction as F
import mpmath as mp
mp.mp.dps=70
N=7

# All independent probabilities use chronological patience sorting of permutations.
# No RSK, transposition, dimension formula, or claimant implementation is used.
hist={}
atoms={}
for n in range(N+1):
    h={}
    for perm in itertools.permutations(range(1,n+1)):
        tops=[]; widths=[0]
        for x in perm:
            j=bisect.bisect_left(tops,x)
            if j==len(tops): tops.append(x)
            else: tops[j]=x
            widths.append(len(tops))
        w=tuple(widths); h[w]=h.get(w,0)+1
        if n>=3 and len(tops)>=3 and tops[2]==n:
            key=(tops[1],n); atoms[key]=atoms.get(key,0)+1
    hist[n]=h

def scalar(u,a,b):
    start=max(0,b-a)
    return mp.fsum(u**n/(mp.factorial(n)*mp.factorial(a+n-b)) for n in range(start,180))

def determinant(obs):
    by={}
    for t,k in obs:
        if t>0: by[t]=min(by.get(t,k),k)
    if not by: return mp.mpf(1)
    ts=sorted(by); ks=[min(by[t] for t in ts[a:]) for a in range(len(ts))]
    T=mp.mpf(str(ts[-1])); d=ks[-1]-1
    if not d: return mp.exp(-T)
    markers=[(mp.mpf(str(t)),x) for t,k in zip(ts[:-1],ks[:-1]) for x in range(d-k+1)]
    q=len(markers); M=mp.matrix(d+q)
    def p(u,y,x): return u**(y-x)/mp.factorial(y-x) if y>=x else mp.mpf(0)
    for i in range(d):
        for j in range(d): M[i,j]=scalar(T,i,j)
        for a,(s,x) in enumerate(markers): M[i,d+a]=p(s,x,i)
    for a,(s,x) in enumerate(markers):
        for j in range(d): M[d+a,j]=-scalar(T-s,x,j)
        for b,(t,y) in enumerate(markers): M[d+a,d+b]=-p(t-s,y,x) if s<t else 0
    return mp.exp(-T)*mp.det(M)

def comps(n,r):
    if r==1:
        yield (n,); return
    for a in range(n+1):
        for rest in comps(n-a,r-1): yield (a,)+rest

def exact_truncated(obs):
    # Deliberately do not use suffix minima; retain every original constraint.
    ts=sorted(set(t for t,k in obs if t>0)); r=len(ts)
    if not ts: return mp.mpf(1),mp.mpf(0)
    ds=[F(str(ts[0]))]+[F(str(ts[i]))-F(str(ts[i-1])) for i in range(1,r)]
    total=F(0)
    for n in range(N+1):
        for counts in comps(n,r):
            cut=list(itertools.accumulate(counts))
            good=sum(v for w,v in hist[n].items() if all(w[cut[ts.index(t)]]<k for t,k in obs if t>0))
            weight=F(good,math.factorial(n))
            for dt,c in zip(ds,counts): weight*=dt**c/math.factorial(c)
            total+=weight
    T=mp.mpf(str(ts[-1])); val=mp.exp(-T)*mp.mpf(total.numerator)/total.denominator
    tail=1-mp.exp(-T)*mp.fsum(T**n/mp.factorial(n) for n in range(N+1))
    return val,tail

cases=[[],[(0,4)],[(.1,1)],[(.3,2)],[(.7,3)],[(.5,5)],
       [(.1,1),(.3,2),(.6,3)],[(.1,2),(.4,3),(.7,4)],
       [(.1,4),(.4,2),(.6,5)],[(.2,4),(.2,2),(.5,3)],
       [(.6,2),(.2,4),(.4,3)],[(.1,1),(.3,2),(.5,3),(.7,4),(.9,5)],
       [(.2,5),(.4,5),(.6,5)],[(.2,2),(.4,2),(.6,2)]]
random.seed(22006)
for _ in range(20):
    cases.append([(random.choice([.1,.2,.3,.4,.5,.6]),random.randint(1,6)) for _ in range(random.randint(1,5))])
records=[]
for obs in cases:
    pred=determinant(obs); low,tail=exact_truncated(obs)
    ok=low-mp.mpf('1e-55')<=pred<=low+tail+mp.mpf('1e-55')
    assert ok,(obs,pred,low,tail)
    records.append({'observations':obs,'determinant':str(pred),'independent_lower':str(low),'Poisson_tail':str(tail),'passes':ok})

# Derive triple coefficients independently from the stated closed density.
import sympy as sp
from sympy.polys.matrices import DomainMatrix
v=sp.symbols('v')
exact_records=[]
for obs in [cases[i] for i in [3,4,6,7,8,9,10,11,12,13]]:
    by={}
    for t,k in obs:
        if t>0: by[F(str(t))]=min(by.get(F(str(t)),k),k)
    ts=sorted(by); ks=[min(by[t] for t in ts[a:]) for a in range(len(ts))]
    T=ts[-1]; d=ks[-1]-1
    markers=[(t,x) for t,k in zip(ts[:-1],ks[:-1]) for x in range(d-k+1)]
    def rat(t): return sp.Rational(t.numerator,t.denominator)
    def es(t,a,b): return sum((rat(t)*v)**n/sp.Integer(math.factorial(n)*math.factorial(a+n-b)) for n in range(max(0,b-a),N+1))
    def ps(t,y,x): return (rat(t)*v)**(y-x)/sp.Integer(math.factorial(y-x)) if y>=x else 0
    if d:
        matrix=sp.zeros(d+len(markers))
        for i in range(d):
            for j in range(d):matrix[i,j]=es(T,i,j)
            for aa,(s,x) in enumerate(markers):matrix[i,d+aa]=ps(s,x,i)
        for aa,(s,x) in enumerate(markers):
            for j in range(d):matrix[d+aa,j]=-es(T-s,x,j)
            for bb,(t,y) in enumerate(markers):matrix[d+aa,d+bb]=-ps(t-s,y,x) if s<t else 0
        polydet=DomainMatrix.from_Matrix(matrix).convert_to(sp.QQ.poly_ring(v)).det().as_expr()
        polynomial=sp.Poly(polydet,v)
    else: polynomial=sp.Poly(1,v)
    ds=[ts[0]]+[ts[i]-ts[i-1] for i in range(1,len(ts))]
    exact_coeff=[]
    for n in range(N+1):
        expected=F(0)
        for counts in comps(n,len(ts)):
            cut=list(itertools.accumulate(counts))
            good=sum(cnt for w,cnt in hist[n].items() if all(w[cut[ts.index(F(str(t)))]]<k for t,k in obs if t>0))
            weight=F(good,math.factorial(n))
            for dt,c in zip(ds,counts):weight*=dt**c/math.factorial(c)
            expected+=weight
        actual=polynomial.coeff_monomial(v**n)
        assert actual==rat(expected),(obs,n,actual,expected)
        exact_coeff.append(str(actual))
    exact_records.append({'observations':obs,'matrix_size':d+len(markers),'coefficients_degree_0_to_7':exact_coeff})
    print('Exact determinant coefficients pass:',obs,flush=True)
g,h=sp.symbols('g h')
def L(j,v): return sum(v**n/sp.Integer(math.factorial(n)*math.factorial(n+j)) for n in range(5))
C=sp.Poly(sp.expand(L(1,g+h)*(L(1,h)-L(2,h))+(L(3,g+h)-L(2,g+h))*L(0,h)),g,h)
coeffs=[]
for r in range(5):
    for s in range(5-r):
        b=r+2; c=r+s+3
        expected=sp.Rational(atoms.get((b,c),0),math.factorial(c)*math.factorial(r)*math.factorial(s))
        actual=C.coeff_monomial(g**r*h**s)
        assert actual==expected,(r,s,actual,expected)
        coeffs.append([r,s,str(actual)])

# Symbolic differentiation, with independent formal derivative implementation.
a,b=sp.symbols('a b')
la=[sp.Function('L'+str(j))(a) for j in range(5)]
lb=[sp.Function('L'+str(j))(b) for j in range(5)]
P=la[0]*lb[0]-b*la[1]*lb[1]
def deriv(expr,v):
    out=sp.diff(expr,v)
    arr=la if v==a else lb
    return out.xreplace({sp.Derivative(arr[j],v):arr[j+1] for j in range(4)})
pab=deriv(deriv(P,a),b)
brace=sp.expand(pab-deriv(pab,a)-deriv(pab,b))
target=la[1]*(lb[1]-lb[2])+(la[3]-la[2])*lb[0]
diff=sp.expand(brace-target)
# use L_j=b L_(j+2)+(j+1)L_(j+1), as follows from factorial coefficients.
diff=sp.expand(diff.subs(lb[0],lb[1]+b*lb[2]).subs(lb[1],2*lb[2]+b*lb[3]))
assert diff==0,diff
mixed=F(1,6)*F(11,120)-F(1,8)**2
assert mixed==F(-1,2880)
assert mixed/F(1,6)**2==F(-1,80)
rg=(F(1,8)*F(1,2)-F(1,6)*F(1,3))/F(1,2)**2
assert rg==F(1,36)
Path('independent_checks.json').write_text(json.dumps({'survival_cases':records,'exact_survival_coefficients':exact_records,'triple_coefficients':coeffs,'symbolic_density_derivative':True,'mixed_log_derivative':str(mixed/F(1,6)**2),'conditional_derivative':str(rg)},indent=2),encoding='utf-8')
print(f'PASS: {len(records)} survival cases using all permutations through size {N}; 15 exact triple coefficients; symbolic triple differentiation; exact dependence witnesses.')
