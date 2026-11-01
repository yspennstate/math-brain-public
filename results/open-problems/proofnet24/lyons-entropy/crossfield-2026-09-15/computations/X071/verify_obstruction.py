"""Exact rational/logarithmic proof that all-pivot gradient work can be adverse."""
import json
from pathlib import Path
import sympy as s

OUT=Path(__file__).resolve().parent
K=s.Matrix([[30779,21025,38699],[21025,34717,29177],[38699,29177,49504]])/100000
A=s.Matrix([[0,17,-1],[17,0,-11],[-1,-11,0]])/20

def logq(x):
    x=s.Rational(x)
    return sum(e*s.log(p) for p,e in s.factorint(x.p).items())-sum(e*s.log(p) for p,e in s.factorint(x.q).items())

def gradient(J):
    G=s.zeros(2)
    for m in range(4):
        M=J-s.diag(*[1-((m>>j)&1) for j in range(2)])
        sg=(-1)**(2-m.bit_count())
        p=sg*M.det()
        assert p>0
        G-=logq(p)*sg*M.adjugate()
    return G

def near_log(x,N=24):
    z=(x-1)/(x+1)
    assert 0<=z<=s.Rational(1,3)
    lo=2*sum(z**(2*j+1)/s.Integer(2*j+1) for j in range(N))
    hi=lo+2*z**(2*N+1)/(s.Integer(2*N+1)*(1-z*z))
    return lo,hi

L2=near_log(s.Integer(2))
def log_interval(x):
    x=s.Rational(x);n=0
    while x>=2:x/=2;n+=1
    while x<1:x*=2;n-=1
    lo,hi=near_log(x)
    if n>=0:return lo+n*L2[0],hi+n*L2[1]
    return lo+n*L2[1],hi+n*L2[0]

def expression_interval(expr):
    expr=s.expand(expr)
    logs=expr.atoms(s.log)
    lo=hi=expr.xreplace({g:s.Integer(0) for g in logs})
    for g in logs:
        c=expr.coeff(g)
        assert c.is_Rational
        l,h=log_interval(g.args[0])
        if c>=0:lo+=c*l;hi+=c*h
        else:lo+=c*h;hi+=c*l
    return lo,hi

principal=[]
for J in (K,s.eye(3)-K):
    vals=[s.factor(J[:j,:j].det()) for j in (1,2,3)]
    assert all(z>0 for z in vals)
    principal.append([str(z) for z in vals])

V=s.Integer(0)
for k in range(3):
    rr=[j for j in range(3) if j!=k]
    a=K[k,k];v=K.extract(rr,[k]);w=A.extract(rr,[k]);R=K.extract(rr,rr)
    J1=R-v*v.T/a;J0=R+v*v.T/(1-a)
    G=gradient(J1)-gradient(J0)
    V+=(w.T*G*w)[0]
lo,hi=expression_interval(V)
assert s.Rational(-71,1000)<lo<hi<s.Rational(-7,100)
result={
    'status':'PASS',
    'certified_interval':['-71/1000','-7/100'],
    'gradient_work_display':str(s.N(V,35)),
    'principal_minors':principal,
    'log_bound':'24-term atanh series after reduction to [1,2); geometric rational tail',
    'scope':'Counterexample only to nonnegativity of summed conditional gradient work; not to entropy concavity.'
}
(OUT/'obstruction.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
