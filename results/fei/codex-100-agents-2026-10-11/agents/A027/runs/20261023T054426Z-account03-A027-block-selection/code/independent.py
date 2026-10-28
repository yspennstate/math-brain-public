"""Fixed D4 witness: direct characters, separate 32-term rational logarithms."""
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import json,time
RUN=Path(__file__).resolve().parents[1];START=time.monotonic();N=0;C=Q(21,4)
def ck(v):
    global N
    assert v
    N+=1
    assert time.monotonic()-START<60
def plus(*pairs):
    z={}
    for c,e in pairs:
        for k,v in e.items():z[k]=z.get(k,Q(0))+c*v
    return {k:v for k,v in z.items() if v}
def fac(n):
    z={};p=2
    while p*p<=n:
        while n%p==0:z[p]=z.get(p,0)+1;n//=p
        p+=1
    if n>1:z[n]=z.get(n,0)+1
    return z
def log(q):return plus((1,fac(q.numerator)),(-1,fac(q.denominator)))
def eta(q):return plus((-q,log(q))) if q else {}
def E(z):return eta(z*z)
def H(f):
    mass=Q(0);z={}
    for a in range(len(f)):
        v=Q(sum(x*(-1 if (j&a).bit_count()%2 else 1) for j,x in enumerate(f)),len(f))
        mass+=v*v;z=plus((1,z),(1,E(v)))
    ck(mass==1);return z
def I(f):return Q(sum(f[j]!=f[j^(1<<i)] for j in range(len(f)) for i in range(len(f).bit_length()-1)),len(f))
def A(d):return plus((4*d*(1-d),eta(Q(1,4))),(2*d*(1-d),{2:Q(1)}),(1,E(d)),(1,E(1-d)),(Q(-1,2),E(1-2*d)))
def Ap(t):return plus((4*(1-2*t),eta(Q(1,4))),(2*(1-2*t),{2:Q(1)}),(-4*t,log(t)),(4*(1-t),log(1-t)),(-4*(1-2*t),log(1-2*t)))
t=Q(1,16)
def T(d):return plus((1,A(t)),(d-t,Ap(t)))
def U(d):return plus((1,A(d)),(-1,T(d)))
def ln(q):
    y=(q-1)/(q+1);v=sum((2*y**(2*j+1)/(2*j+1) for j in range(32)),Q(0))
    return v,v+2*y**65/(65*(1-y*y))
LN2=ln(Q(2))
@lru_cache(None)
def lb(n):
    q=Q(n);k=0
    while q>=2:q/=2;k+=1
    lo,hi=ln(q);return k+lo/LN2[1],k+hi/LN2[0]
def bounds(e):
    lo=hi=Q(0)
    for k,c in e.items():
        a,b=lb(k);lo+=c*(a if c>0 else b);hi+=c*(b if c>0 else a)
    return lo,hi
def num(q):return {2:Q(q)} if q else {}
def enc(e):return {'prime_log':{str(k):str(v) for k,v in e.items()},'interval':[str(v) for v in bounds(e)]}
u=(-1,)+(1,)*15;F=u+(1,)*16;rows=[]
for depth in range(5):
    # Query low core bits. Include every actual leaf, including constant siblings.
    EH=EU=EC={};EI=Q(0);coreH={};coreI=Q(0)
    for a in range(1<<depth):
        v=tuple(u[a+(j<<depth)] for j in range(1<<(4-depth)));f=v+(1,)*len(v);d=Q(v.count(-1),len(v));w=Q(1,1<<depth)
        S=plus((1,num(C*I(f))),(-1,H(f)));Sc=plus((1,num(C*I(v))),(-1,H(v)))
        reserve=plus((1,num(C*d)),(-1,T(d)))
        ck(plus((1,S),(1,U(d)))==plus((Q(1,2),Sc),(1,reserve)))
        ck(bounds(reserve)[0]>=0);ck(bounds(Sc)[0]>=0)
        if bounds(U(d))[1]<0:ck(bounds(plus((1,S),(1,U(d))))[0]>0)
        EH=plus((1,EH),(w,H(f)));EU=plus((1,EU),(w,U(d)));EI+=w*I(f)
        EC=plus((1,EC),(w,S),(w,U(d)));coreH=plus((1,coreH),(w,H(v)));coreI+=w*I(v)
    error=plus((1,H(F)),(-1,EH),(Q(-1,2),H(u)),(Q(1,2),coreH))
    ck(error==plus((-1,EU)))
    q=I(F)-EI;ck(q==Q(1,2)*(I(u)-coreI))
    rootS=plus((1,num(C*I(F))),(-1,H(F)))
    cd=plus((1,num(C*(I(u)-coreI))),(-1,H(u)),(1,coreH))
    ck(rootS==plus((Q(1,2),cd),(1,EC)))
    rows.append({'depth':depth,'leaves':1<<depth,'error':enc(error),'combined_terminals':enc(EC)})
guard=plus((1,num(C)),(1,U(Q(1))))
ck(bounds(U(Q(1)))[1]<0);ck(bounds(guard)[0]>0)
main=json.loads((RUN/'out/validation.json').read_text(encoding='utf-8'))
ck(enc(guard)['prime_log']==main['point4_paid_reserve']['prime_log'])
ck(bounds(plus((-1,EU)))[0]>0)
out={'status':'PASS','assertions':N,'elapsed_seconds':time.monotonic()-START,'method':'direct characters and independent rational logarithms; D4 r1, all five prefix frontiers','point4_paid_reserve':enc(guard),'frontiers':rows}
(RUN/'out/independent.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if not isinstance(v,(dict,list))}))
