"""Independent exact witness: integer FWHT, edge enumeration, log-power signs."""
from pathlib import Path
from fractions import Fraction as Q
from math import lcm
import json,time
run=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def ck(v):
    global checks
    checks+=1;assert v
def spectrum(v):
    a=list(v);h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for k in range(j,j+h):x,y=a[k],a[k+h];a[k]=x+y;a[k+h]=x-y
        h*=2
    return tuple(Q(x*x,len(v)**2) for x in a)
def E(*terms):
    out={}
    for a in terms:
        for x,c in a.items():out[x]=out.get(x,Q(0))+c
    return {x:c for x,c in out.items() if c and x!=1}
def M(a,c):return E({x:v*c for x,v in a.items()})
def bits(x):return {Q(2):Q(x)}
def ce(p,q):return E(*[{x:-v} for v,x in zip(p,q) if v])
def H(p):return ce(p,p)
def certificate(a):
    den=lcm(*(c.denominator for c in a.values())) if a else 1
    prod=Q(1)
    for x,c in a.items():prod*=x**int(c*den)
    return prod,den
def nonneg(a):return certificate(a)[0]>=1
def positive(a):return certificate(a)[0]>1
def equal(a,b):return certificate(E(a,M(b,-1)))[0]==1
def edge(v,i):return Q(sum(v[k]!=v[k^(1<<i)] for k in range(len(v))),len(v))
def restrict(v,i,s):return tuple(x for k,x in enumerate(v) if k>>i&1==s)
def project(q,i):
    return tuple(q[(k&((1<<i)-1))+((k>>i)<<(i+1))]+q[(k&((1<<i)-1))+((k>>i)<<(i+1))+(1<<i)] for k in range(len(q)//2))

F=(1,)+(-1,)*7;f0=restrict(F,0,0);f1=restrict(F,0,1)
ck(f0==(1,-1,-1,-1));ck(f1==(-1,)*4)
p=spectrum(F);p0=spectrum(f0);p1=spectrum(f1)
ck(p==(Q(9,16),)+(Q(1,16),)*7)
ck(p0==(Q(1,4),)*4);ck(p1==(Q(1),Q(0),Q(0),Q(0)))
q0=(Q(1,10),Q(2,5),Q(1,10),Q(2,5));q1=p1
ck(all((x>0)==(y>0) for pp,qq in [(p0,q0),(p1,q1)] for x,y in zip(pp,qq)))
Ibar=sum(edge(v,i) for v in [f0,f1] for i in [0,1])/2
e=edge(F,0);R=2*e;A=4*Ibar;tau=Ibar/4
ck(Ibar==Q(1,2));ck(e==Q(1,4));ck(R==Q(1,2));ck(A==2);ck(tau==Q(1,8))
ck(sum(edge(F,i) for i in range(3))==Q(3,4))
openingCE=M(E(ce(p0,q0),ce(p1,q1)),Q(1,2))
ck(equal(openingCE,{Q(5):Q(1,2)}))
initialH=E(H(p),bits(-1));Lzero=nonneg(E(bits(5*e),M(initialH,-1)))
ck(Lzero)
U=E(bits(A-tau),M(openingCE,-1))
admission=E(U,bits(-Q(3,2)*R+e/4));ck(nonneg(admission))
S=E(U,bits(-R));ck(nonneg(S));ck(positive(E(bits(Q(1,4)),M(S,-1))))

children=[restrict(v,1,s) for v in [f0,f1] for s in [0,1]]
pcs=[spectrum(v) for v in children]
qbs=[project(q0,1),project(q1,1)]
ck(qbs==[(Q(1,5),Q(4,5)),(Q(1),Q(0))])
terminalCE=M(E(*[ce(pp,qbs[k//2]) for k,pp in enumerate(pcs)]),Q(1,4))
nextH=E(M(E(H(p0),H(p1)),Q(1,2)),M(E(*[H(pp) for pp in pcs]),-Q(1,4)))
ck(equal(nextH,bits(1)))
nextC=E(openingCE,M(terminalCE,-1));ck(equal(nextC,bits(Q(1,2))))
ck(equal(E(nextH,M(nextC,-1)),bits(Q(1,2))))
required=Q(1,2)-Q(1,4);ck(required==Q(1,4))
# All first-query unused slack is allowed; STILL no nonnegative final source.
whole=E(initialH,nextH,terminalCE,bits(tau))
gap=E(whole,bits(-A-4*e));ck(positive(gap))
closed={Q(20000,19683):Q(1,8)};ck(equal(gap,closed))
ck(20000>19683);ck(5**8<2**19);ck(5**4>2**9);ck(3**9>2**14)

# Empty/nonempty calibration changes no conditional nonempty shape here.
calibrated=[(pp[0],1-pp[0]) for pp in pcs]
ck(all(sum(qq)==1 for qq in calibrated))
calCE=M(E(*[ce(pp,qq) for pp,qq in zip(pcs,calibrated)]),Q(1,4))
ck(equal(calCE,bits(0)))
calwhole=E(initialH,nextH,calCE,bits(tau))
ck(nonneg(E(bits(A+4*e),M(calwhole,-1))))

def show(a):
    prod,den=certificate(a)
    return {'log_terms':{str(x):str(c) for x,c in a.items()},'power_ratio':str(prod),'power_denominator':den,'sign':(prod>1)-(prod<1)}
out={'status':'PASS','exact_assertions':checks,'seconds':time.perf_counter()-start,'truth_table':F,'q0':list(map(str,q0)),'q1':list(map(str,q1)),'A':str(A),'tau':str(tau),'e':str(e),'R':str(R),'L':0,'opening_admission_margin':show(admission),'S':show(S),'next_JS_minus_conditionalKL':'1/2','next_reserve_release':'1/4','next_required_from_old_S':'1/4','whole_ledger_excess':show(gap),'closed_excess':'log2(20000/19683)/8 > 0','calibration_CE':show(calCE),'calibrated_residual':show(E(bits(A+4*e),M(calwhole,-1))),'scope':'refutes admission-only guarantee for prescribed next seed query under LITERAL full-reference projection; neither v2 nor FEI nor calibrated/nonempty-profile policies are refuted'}
(run/'out/WITNESS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:v for k,v in out.items() if k in ['status','exact_assertions','seconds','closed_excess','scope']}))
