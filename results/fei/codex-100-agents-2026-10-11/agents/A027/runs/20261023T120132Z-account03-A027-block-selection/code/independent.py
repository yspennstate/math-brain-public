from fractions import Fraction as Q
from pathlib import Path
from functools import lru_cache
import json,time
R=Path(__file__).resolve().parents[1];START=time.monotonic();N=0;C=Q(21,4)
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
def lg(q):return plus((1,fac(q.numerator)),(-1,fac(q.denominator)))
def eta(q):return plus((-q,lg(q))) if q else {}
@lru_cache(None)
def hat(f):return tuple(Q(sum(v*(-1 if (a&j).bit_count()%2 else 1) for j,v in enumerate(f)),len(f)) for a in range(len(f)))
def P(f):return tuple(v*v for v in hat(f))
def H(f):return plus(*[(1,eta(z)) for z in P(f)])
def I(f):return Q(sum(f[j]!=f[j^(1<<i)] for j in range(len(f)) for i in range(len(f).bit_length()-1)),len(f))
def restrict(f,i,b):
    n=len(f).bit_length()-1
    return tuple(f[(j&((1<<i)-1))+(b<<i)+((j>>i)<<(i+1))] for j in range(1<<(n-1)))
def activate(v,a):return tuple(v[j] if x==-1 else 1 for x in a for j in range(len(v)))
def D(p,q):return plus(*[(z,lg(z/r)) for z,r in zip(p,q) if z])
def ln(q):
    y=(q-1)/(q+1);v=sum((2*y**(2*j+1)/(2*j+1) for j in range(32)),Q(0))
    return v,v+2*y**65/(65*(1-y*y))
LN2=ln(Q(2))
@lru_cache(None)
def lb(k):
    x=Q(k);a=0
    while x>=2:x/=2;a+=1
    lo,hi=ln(x);return a+lo/LN2[1],a+hi/LN2[0]
def bounds(e):
    lo=hi=Q(0)
    for k,c in e.items():
        a,b=lb(k);lo+=c*(a if c>0 else b);hi+=c*(b if c>0 else a)
    return lo,hi
def enc(e):return {'prime_log':{str(k):str(v) for k,v in e.items()},'interval':[str(v) for v in bounds(e)]}
def num(q):return {2:Q(q)} if q else {}
u=(-1,)+(1,)*15;a=tuple(-1 if j.bit_count()>=2 else 1 for j in range(8));f=activate(u,a)
v=(-1,)+(1,)*7;childa=[restrict(a,0,b) for b in (0,1)];children=[activate(v,z) for z in childa]
ck(I(f)==Q(11,32));ck(I(f)==Q(1,16)+Q(1,32)+sum(I(z)/4 for z in children))
for b in (0,1):ck(children[b]==restrict(restrict(f,0,0),3,b))
selected=children[1];p=P(selected);theta=Q(1,8)
def E(z):return eta(z*z)
def G(ac,d):
    pr=Q(ac.count(-1),len(ac));V=4*pr*(1-pr);hp=plus((1,H(ac)),(-1,E(hat(ac)[0])))
    return plus((d,hp),(4*d*(1-d),eta(pr*pr)),(2*d*(1-d)*V,num(1)),(V,E(d)),(1,E(1-2*pr*d)),(-pr,E(1-2*d)))
def GP(ac,t):
    pr=Q(ac.count(-1),len(ac));V=4*pr*(1-pr);hp=plus((1,H(ac)),(-1,E(hat(ac)[0])))
    return plus((1,hp),(4*(1-2*t),eta(pr*pr)),(2*(1-2*t)*V,num(1)),(-4*V*t,lg(t)),(8*pr*(1-2*pr*t),lg(1-2*pr*t)),(-8*pr*(1-2*t),lg(1-2*t)))
tt=Q(1,16);dd=Q(1,8);ac=childa[1]
refund=plus((1,G(ac,dd)),(-1,G(ac,tt)),(-(dd-tt),GP(ac,tt)))
selectedbank=plus((Q(1,4),num(C*I(selected))),(Q(-1,4),H(selected)),(Q(1,4),refund))
coremargin=plus((1,num(C*Q(1,16))),(Q(-1,2),H(u)),(Q(1,4),H(v)))
ck(bounds(plus((1,coremargin),(-1,num(Q(1,64)))))[0]>0)
ck(bounds(plus((1,selectedbank),(-1,num(Q(1,64)))))[0]>0)
q=tuple(z if not(j>>3) else z*(1-theta+3*theta*((j>>3)==1)) for j,z in enumerate(p))
ck(sum(q)==1);ck(sum(z for j,z in enumerate(p) if j>>3)==Q(3,32))
cost=plus((Q(1,4),D(p,q)));closed=plus((Q(-1,128),lg(Q(5,4))),(Q(-1,64),lg(Q(7,8))))
ck(cost==closed);ck(bounds(plus((1,num(Q(9,1792))),(-1,cost)))[0]>0)
ck(bounds(plus((1,selectedbank),(-1,cost),(-1,num(Q(19,1792)))))[0]>0)
ck(bounds(plus((1,num(C*I(f)-Q(1,64))),(-1,H(f)),(-1,cost)))[0]>0)

def step(f,q,i):
    p=P(f);children=[restrict(f,i,b) for b in (0,1)];raw=[[],[]];n=len(f).bit_length()-1
    for k in range(1<<(n-1)):
        j=(k&((1<<i)-1))+((k>>i)<<(i+1));jj=j+(1<<i);mass=p[j]+p[jj];rm=q[j]+q[jj]
        for b in (0,1):
            physical=P(children[b])[k]/2
            prob=physical/mass if mass else Q(1,2)
            raw[b].append(rm*prob)
            ck(mass*prob==physical)
    zs=[sum(z) for z in raw];ck(sum(zs)==1)
    refs=[tuple(z/zs[b] for z in raw[b]) for b in (0,1)]
    before=D(p,q);after=plus((Q(1,2),D(P(children[0]),refs[0])),(Q(1,2),D(P(children[1]),refs[1])))
    gap=plus((1,before),(-1,after));ck(not gap or bounds(gap)[0]>=0)
    return children,refs,zs,gap
ch,refs,zs,gap=step(selected,q,0);expected={};normalizers=[list(map(str,zs))]
for w,rho in zip(ch,refs):
    cs,rs,zs,g=step(w,rho,2)
    normalizers.append(list(map(str,zs)))
    for v,r in zip(cs,rs):expected=plus((1,expected),(Q(1,4),D(P(v),r)))
ck(bounds(plus((1,D(p,q)),(-1,expected)))[0]>=0)
main=json.loads((R/'out/validation.json').read_text(encoding='utf-8'))
ck(enc(cost)['prime_log']==main['costs'][-1]['weighted_actual_reset']['prime_log'])
ck(enc(selectedbank)['prime_log']==main['selected_full_signed_account']['prime_log'])
out={'status':'PASS','assertions':N,'elapsed_seconds':time.monotonic()-START,'method':'independent direct characters and physical likelihood kernels;32-term rational logs; first changed reference through DATA then CONTROL','actual_cost':enc(cost),'root_surplus_after_old_and_cost':enc(plus((1,num(C*I(f)-Q(1,64))),(-1,H(f)),(-1,cost))),'reference_normalizers':normalizers}
(R/'out/independent.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if not isinstance(v,(list,dict))}))
