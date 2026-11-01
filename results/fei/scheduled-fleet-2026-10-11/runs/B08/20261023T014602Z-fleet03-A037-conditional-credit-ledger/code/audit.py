"""Independent literal-character transform and exact prime-log identities."""
from fractions import Fraction as R
from pathlib import Path
import json,time

start=time.monotonic();checks=0
def ck(v):
    global checks
    checks+=1
    assert v,checks
    assert time.monotonic()-start<55
def merge(a,b,scale=R(1)):
    c=dict(a)
    for p,x in b.items():c[p]=c.get(p,R(0))+scale*x
    return {p:x for p,x in c.items() if x}
def logvec(q):
    result={}
    for number,sign in [(q.numerator,1),(q.denominator,-1)]:
        p=2
        while p*p<=number:
            while number%p==0:
                result[p]=result.get(p,0)+sign;number//=p
            p+=1
        if number>1:result[number]=result.get(number,0)+sign
    return {p:R(x) for p,x in result.items() if x}
def entropy(p):
    v={}
    for x in p:
        if x:v=merge(v,logvec(x),-x)
    return v
def divergence(p,q):
    v={}
    for x,y in zip(p,q):
        if x:v=merge(v,logvec(x/y),x)
    return v
def spectrum(tab):
    return [R(sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(tab))**2,len(tab)**2) for s in range(len(tab))]
def marg(p):
    return [sum(x for s,x in enumerate(p) if s>>j&1) for j in range((len(p)-1).bit_length())]
def product(ds):
    out=[]
    for s in range(1<<len(ds)):
        q=R(1)
        for j,d in enumerate(ds):q*=d if s>>j&1 else 1-d
        out.append(q)
    return out
def tc(p):return divergence(p,product(marg(p)))
def ph(m):
    d=R(2,2**m)
    return entropy([(1-d)**2]+[d*d]*(2**m-1))
def hb(d):return entropy([d,1-d])
def ln_iv(q):
    e=0
    while q>=2:q/=2;e+=1
    while q<1:q*=2;e-=1
    def series(x):
        z=(x-1)/(x+1);lo=sum((2*z**(2*j+1)/R(2*j+1) for j in range(60)),R(0))
        return lo,lo+2*z**121/(121*(1-z*z))
    a,b=series(q);l,u=series(R(2))
    if e>=0:return a+e*l,b+e*u
    return a+e*u,b+e*l
def bounds(v):
    l,u=ln_iv(R(2));a=b=R(0)
    for p,c in v.items():
        x,y=ln_iv(R(p));lo,hi=x/u,y/l
        a+=c*(lo if c>=0 else hi);b+=c*(hi if c>=0 else lo)
    return a,b

def point(w):return spectrum([-1]+[1]*(2**w-1))
def ref(p,beta):
 q=[p[0]]+[beta*x for x in p[1:]]
 if len(q)>2:q[-1]+=(1-beta)*(1-p[0])
 else:q=list(p)
 return q
def tensor(p,q):return [x*y for y in q for x in p]

rows=[]
for w in range(2,6):
 for s in [2,3]:
  p=point(w);v=point(s);q=ref(p,R(5,6));z=ref(v,R(5,6))
  P=tensor(p,v);Q=tensor(q,z)
  children=[tensor(point(w-1),v),tensor([R(1)]+[R(0)]*(2**(w-1)-1),v)]
  small=[point(w-1),[R(1)]+[R(0)]*(2**(w-1)-1)]
  pe=[P[2*j]+P[2*j+1] for j in range(len(P)//2)]
  qe=[Q[2*j]+Q[2*j+1] for j in range(len(Q)//2)]
  pes=[p[2*j]+p[2*j+1] for j in range(len(p)//2)]
  qes=[q[2*j]+q[2*j+1] for j in range(len(q)//2)]
  direct={};factor={};outcomes=[]
  for y,py in enumerate(children):
   k=[x/(2*a) for x,a in zip(py,pe)]
   oy=sum(a*b for a,b in zip(qe,k));outcomes.append(oy)
   inherited=[a*b/oy for a,b in zip(qe,k)]
   ks=[x/(2*a) for x,a in zip(small[y],pes)]
   os=sum(a*b for a,b in zip(qes,ks))
   oldfactor=[a*b/os for a,b in zip(qes,ks)]
   freshfactor=ref(small[y],R(4,5)) if w-1>=2 and y==0 else list(small[y])
   fresh=tensor(freshfactor,z)
   ck(oy==os);ck(inherited==tensor(oldfactor,z));ck(sum(fresh)==1)
   direct=merge(direct,merge(divergence(py,fresh),divergence(py,inherited),-1),R(1,2))
   factor=merge(factor,merge(divergence(small[y],freshfactor),divergence(small[y],oldfactor),-1),R(1,2))
  ck(direct==factor)
  lo,hi=bounds(direct);cap=bounds(logvec(R(5,4)))[0]/2
  ck(hi<cap)
  if w==3:ck(lo>0)
  rows.append({'width':w,'spectator_width':s,'exact_factor_cancellation':True,'second_reset_interval':[str(lo),str(hi)],'positive':lo>0})

ck(5**3<2*4**3)
out={'status':'PASS','checks':checks,'runtime_seconds':time.monotonic()-start,'cases':rows,'independence':'literal Walsh sums, Fraction atomwise posterior products, exact prime-log cancellation; imports no main checker or interval helper'}
root=Path(__file__).resolve().parent.parent
(root/'out/AUDIT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ['status','checks','runtime_seconds']}))

