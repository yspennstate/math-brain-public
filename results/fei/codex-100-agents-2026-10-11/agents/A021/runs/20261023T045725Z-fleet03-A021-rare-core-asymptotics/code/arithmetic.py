"""Exact complete-reference certificates; no outside helper import or write."""
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import json,time,sys,hashlib
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'out'; OUT.mkdir(exist_ok=True)
count=0
def ck(x,where):
 global count
 count+=1
 assert x,(count,where)
def save(name,x): (OUT/name).write_text(json.dumps(x,indent=2,default=str)+'\n',encoding='utf-8',newline='')
@lru_cache(None)
def factors(n):
 out={}; p=2
 while p*p<=n:
  while n%p==0: out[p]=out.get(p,0)+1; n//=p
  p+=1
 if n>1: out[n]=out.get(n,0)+1
 return out
def plus(*terms):
 d={}
 for a in terms:
  for p,c in a.items(): d[p]=d.get(p,Q(0))+c
 return {p:c for p,c in d.items() if c}
def mul(a,c): return {p:v*c for p,v in a.items() if v*c}
def const(c): return {2:Q(c)} if c else {}
def lg(x):
 x=Q(x); d={p:Q(v) for p,v in factors(x.numerator).items()}
 return plus(d,{p:-Q(v) for p,v in factors(x.denominator).items()})
@lru_cache(None)
def log_interval(p):
 q=Q(p); k=q.numerator.bit_length()-1; y=q/Q(2)**k
 def ln(y):
  z=(y-1)/(y+1); term=z; s=Q(0)
  for j in range(40): s+=2*term/(2*j+1); term*=z*z
  return s,s+2*term/(81*(1-z*z))
 a,b=ln(y); c,d=ln(Q(2))
 return k+a/d,k+b/c
def bounds(a):
 lo=hi=Q(0)
 for p,c in a.items():
  l,h=log_interval(p)
  if c<0: l,h=h,l
  lo+=c*l; hi+=c*h
 return lo,hi
def ge(a,x=0): return not a and x<=0 or bounds(a)[0]>=x
def fwht(f):
 a=list(f); h=1
 while h<len(a):
  for j in range(0,len(a),2*h):
   for i in range(j,j+h): u,v=a[i],a[i+h]; a[i]=u+v; a[i+h]=u-v
  h*=2
 return a
def spectrum(f):
 n=len(f); return [Q(a*a,n*n) for a in fwht(f)]
def entropy(P): return plus(*(mul(lg(1/p),p) for p in P if p))
def ce(P,ref):
 terms=[]
 for p,r in zip(P,ref):
  if p:
   ck(r>0,'reference support'); terms.append(mul(lg(1/r),p))
 return plus(*terms)
def inf(f,i): return Q(sum(f[j]!=f[j^(1<<i)] for j in range(len(f))),len(f))
def restrict(f,i,b): return [v for j,v in enumerate(f) if j>>i&1==b]
def g(x): return -1 if x==0 else 1
CONTROLS=((0,0,0,0),(1,1,1,1),(0,1,0,1),(0,0,1,1),(0,0,0,1),(0,1,1,1))
def run(pilot=False):
 start=time.perf_counter(); rows=[]; t=2; k=6; N=64; delta=Q(1,N)
 L3=lg(3); L13=lg(13); G=plus(mul(L13,Q(1,2)),mul(L3,-Q(9,8)))
 for v in (range(4) if pilot else range(64)):
  for ac,A in enumerate(CONTROLS):
   alpha=Q(sum(A),4); a=[1-2*z for z in A]; Pa=spectrum(a); L=mul(entropy(Pa),delta)
   R=[1-4*delta*alpha*(1-alpha)]+[delta*p for p in Pa[1:]]
   ck(sum(R)==1,'root controller normalized')
   f=[g(x&7)*g(x>>3)*(-1 if x==v and A[z] else 1) for z in range(4) for x in range(N)]
   P=spectrum(f); Qdata=[Q(9 if s&7==0 else 1,16)*Q(9 if s>>3==0 else 1,16) for s in range(N)]
   ref=[Qdata[s]*R[z] for z in range(4) for s in range(N)]
   C0=ce(P,ref); H0=entropy(P); D0=plus(C0,mul(H0,-1)); Id=sum((inf(f,i) for i in range(k)),Q(0))
   ck(ge(D0),'root KL nonnegative')
   ck(ge(plus(const(4*Id),L,mul(C0,-1)),Q(179*t,576)),'sharpened original source')
   # Independent direct controller marginal check, including empty atom.
   ck([sum(P[z*N:(z+1)*N]) for z in range(4)]==R,'root R from actual spectrum')
   for i in (0,1,2):
    fs=[restrict(f,i,b) for b in (0,1)]; Ps=[spectrum(ff) for ff in fs]
    refs=[]; Cs=[]; Hs=[]; Ds=[]
    for b in (0,1):
     qb=[Q(1,4) if b==0 else Q(13 if s&3==0 else 1,16) for s in range(32)]
     qb=[q*Q(9 if s>>2==0 else 1,16) for s,q in enumerate(qb)]
     ck(sum(qb)==1,'child Q normalized')
     refs.append([qb[s]*R[z] for z in range(4) for s in range(32)])
     Cs.append(ce(Ps[b],refs[b])); Hs.append(entropy(Ps[b])); Ds.append(plus(Cs[-1],mul(Hs[-1],-1)))
     ck(ge(Ds[-1]),'full child KL nonnegative')
    C1=mul(plus(*Cs),Q(1,2)); drop=plus(C0,mul(C1,-1)); d=inf(f,i)
    vi=v&7; sigma=g(vi)*g(vi^(1<<i))
    if vi==0: w=mul(L3,-7)
    elif not (vi>>i&1): w=mul(L3,5)
    else: w=plus(mul(L3,5),mul(L13,-3))
    expected=plus(const(1),G,mul(w,delta*alpha))
    ck(drop==expected,'exact prescribed conversion')
    ck(d==Q(1,4)+2*delta*alpha*sigma,'actual physical query')
    loss=plus(const(4*d),mul(drop,-1))
    ck(bounds(loss)[1]<Q(1,8),'reference capacity loss')
    Ichild=sum((sum((inf(ff,j) for j in range(k-1)),Q(0)) for ff in fs),Q(0))/2
    ck(Ichild==Id-d,'data influence telescope')
    U=Q(t,64); B0=plus(const(4*Id-U),L,mul(C0,-1)); B1=plus(const(4*Ichild-U),L,mul(C1,-1))
    ck(B1==plus(B0,mul(loss,-1)),'SAME original bank transfer')
    ck(ge(B1,Q(11*t,64)),'old U and original t64 retained')
    Hchild=mul(plus(*Hs),Q(1,2)); Dactual=plus(H0,mul(Hchild,-1)); Dchild=mul(plus(*Ds),Q(1,2))
    ck(Dactual==plus(drop,Dchild,mul(D0,-1)),'actual entropy versus reference decrement')
    ck(plus(B1,Dchild,const(4*d),mul(Dactual,-1))==plus(B0,D0),'full signed history identity')
    mr=[(sum(Ps[0][z*32:(z+1)*32])+sum(Ps[1][z*32:(z+1)*32]))/2 for z in range(4)]
    ck(mr==R,'unchanged controller reference mass')
    if all(A) and v>>i&1:
     off=sum((p for z in range(4) for s,p in enumerate(Ps[1][z*32:(z+1)*32]) if s&3),Q(0))
     ck(off==6*delta>0,'canonical zero reference is invalid')
    rows.append({'v':v,'control':ac,'query':i,'d':str(d),'capacity_loss_bounds':list(map(str,bounds(loss))),'child_bank_lower':str(bounds(B1)[0])})
  if time.perf_counter()-start>59: raise RuntimeError('frozen60-second cap')
  save('PILOT.json' if pilot else 'DIRECT.json',{'status':'RUNNING','cases':len(rows),'assertions':count})
 scalar=[]
 for tt in range(2,41):
  for vv in range(8):
   for alpha in (Q(0),Q(1,2),Q(1)):
    delta=Q(1,8**tt); sigma=g(vv)*g(vv^1)
    w=mul(L3,-7) if vv==0 else mul(L3,5) if vv%2==0 else plus(mul(L3,5),mul(L13,-3))
    loss=plus(mul(G,-1),mul(plus(const(8*sigma),mul(w,-1)),delta*alpha))
    ck(bounds(loss)[1]<Q(1,8),'scalar conversion')
    if tt>=3: ck(bounds(loss)[1]<0,'t>=3 release')
    ck(Q(tt,4)-Q(tt,64)-Q(1,8)>=Q(11*tt,64),'scalar preserved reserve')
    scalar.append({'t':tt,'local_vertex':vv,'alpha':str(alpha)})
 # Integer certificates for every logarithm bound actually used.
 for ok in [3**9>2**14,3**5<2**8,3**12>2**19,3**80<2**127,13**10>2**37,13**24<2**89]: ck(ok,'integer logarithm certificate')
 save('SCALAR.json',{'status':'PASS','cases':len(scalar),'integer_log_certificates':6})
 obj={'status':'PASS','cases':len(rows),'scalar_cases':len(scalar),'assertions':count,'seconds':time.perf_counter()-start,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'rows':rows}
 save('PILOT.json' if pilot else 'DIRECT.json',obj)
 print(json.dumps({k:v for k,v in obj.items() if k not in ('rows','helper_sha256')}))
if __name__=='__main__': run('--pilot' in sys.argv)
