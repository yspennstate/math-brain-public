from fractions import Fraction as Q
from itertools import product
from pathlib import Path
from collections import defaultdict
from functools import lru_cache
import json,time
R=Path(__file__).resolve().parents[1]; start=time.monotonic(); checks=0
def ck(x):
 global checks
 assert x
 checks+=1
def transform(values,p):
 a=list(map(Q,values)); n=len(p)
 for i,q in enumerate(p):
  step=1<<i
  for base in range(0,len(a),2*step):
   for j in range(step):
    low,high=a[base+j],a[base+j+step]
    a[base+j]=(1-q)*low+q*high; a[base+j+step]=high-low
 mass=[]; ref=[]
 for s,z in enumerate(a):
  d=Q(1)
  for i,q in enumerate(p):
   if s>>i&1:d*=q*(1-q)
  mass.append(z*z*d); ref.append(d*4**s.bit_count())
 ck(sum(mass)==sum(prob(x,p)*Q(values[x])**2 for x in range(1<<n)))
 return a,mass,ref
def prob(x,p):
 v=Q(1)
 for i,q in enumerate(p):v*=q if x>>i&1 else 1-q
 return v
def deficit(mass):return sum((s.bit_count()-1)*v for s,v in enumerate(mass) if s)
@lru_cache(maxsize=20000)
def factors(n):
 d=2; out=[]
 while d*d<=n:
  k=0
  while n%d==0:n//=d;k+=1
  if k:out.append((d,k))
  d+=1 if d==2 else 2
 if n>1:out.append((n,1))
 return out
def add(e,c,x):
 if not c:return
 ck(x>0)
 for k,v in factors(x.numerator):e[k]+=c*v
 for k,v in factors(x.denominator):e[k]-=c*v
def clean(e):return {k:v for k,v in e.items() if v}
def expression(mass,ref,predicate=lambda s:bool(s)):
 e=defaultdict(Q)
 for s,v in enumerate(mass):
  if v and predicate(s):add(e,v,ref[s]/v)
 return clean(e)
@lru_cache(maxsize=20000)
def log_bounds(x):
 x=Q(x); k=0
 while x>=2:x/=2;k+=1
 while x<1:x*=2;k-=1
 def part(t):
  z=(t-1)/(t+1); lo=2*sum((z**(2*j+1)/Q(2*j+1) for j in range(20)),Q(0))
  return lo,lo+2*z**41/(41*(1-z*z))
 a,b=part(x); l,u=part(Q(2))
 return (a+k*l,b+k*u) if k>=0 else (a+k*u,b+k*l)
def bound(e):
 a=b=Q(0)
 for k,v in e.items():
  l,u=log_bounds(k)
  a+=v*(l if v>=0 else u);b+=v*(u if v>=0 else l)
 return a,b
def diff(a,b):
 e=defaultdict(Q,a)
 for k,v in b.items():e[k]-=v
 return clean(e)
def certify_le(a,b,reserve):
 e=diff(b,a)
 if not e:ck(reserve>=0)
 else:ck(bound(e)[0]+reserve>=0)
def table(mask,n):return [1 if mask>>x&1 else -1 for x in range(1<<n)]
def essential(vals,n):return all(any(vals[x]!=vals[x^(1<<i)] for x in range(1<<n)) for i in range(n))

# Review A042 in a finite-difference basis rather than centered moment integration.
grid=[Q(1,17),Q(1,4),Q(1,2),Q(3,4),Q(16,17)]
binary=0; classification=defaultdict(int)
for mask in range(16):
 vals=table(mask,2); pos=sum(z==1 for z in vals)
 kind='corner' if pos in (1,3) else 'parity' if essential(vals,2) else 'nonessential'
 classification[kind]+=1
 for p,q in product(grid,repeat=2):
  _,mass,ref=transform(vals,[p,q]); d=deficit(mass); expected=defaultdict(Q)
  if kind=='corner':
   x=next(x for x in range(4) if vals[x]==(1 if pos==1 else -1))
   u=p if x&1 else 1-p;v=q if x&2 else 1-q
   ck(d==4*u*(1-u)*v*(1-v));add(expected,2*d,Q(2))
   add(expected,2*d*u/(1-u),1/u);add(expected,2*d*v/(1-v),1/v)
  elif kind=='parity':
   a=4*p*(1-p);b=4*q*(1-q);ck(d==a*b)
   if a!=1:add(expected,d*(1-a)/a,1/(1-a))
   if b!=1:add(expected,d*(1-b)/b,1/(1-b))
  else:ck(d==0)
  ck(expression(mass,ref)==clean(expected));binary+=1
ck(dict(classification)=={'nonessential':6,'corner':8,'parity':2})

composition=0
for outer in range(16):
 g=table(outer,2)
 if not essential(g,2):continue
 for left,right in product((8,6),repeat=2):
  children=[table(left,2),table(right,2)]
  for p in ([Q(1,3),Q(2,5),Q(3,7),Q(1,4)],[Q(1,2)]*4):
   spectra=[transform(children[i],p[2*i:2*i+2]) for i in (0,1)]
   eta=[sum(prob(x,p[2*i:2*i+2]) for x in range(4) if children[i][x]==1) for i in (0,1)]
   _,om,orr=transform(g,eta)
   full=[g[int(children[0][x&3]==1)+2*int(children[1][x>>2]==1)] for x in range(16)]
   _,fm,fr=transform(full,p); target=defaultdict(Q,expression(om,orr)); d=deficit(om)
   for i in (0,1):
    alpha=sum(v for s,v in enumerate(om) if s>>i&1)/(4*eta[i]*(1-eta[i]))
    d+=alpha*deficit(spectra[i][1])
    for k,v in expression(spectra[i][1],spectra[i][2]).items():target[k]+=alpha*v
   ck(deficit(fm)==d);ck(expression(fm,fr)==clean(target));composition+=1

# Scalar Jensen certificate; zeros and equality are handled symbolically.
scalar=0
for a,b,p in product([Q(-1),Q(-3,4),Q(-1,4),Q(0),Q(1,4),Q(3,4),Q(1)],repeat=3):
 if p not in (Q(0),Q(1,4),Q(3,4),Q(1)):continue
 # This loop's p set is specified exactly in FROZEN_SPEC.
 m=(1-p)*a+p*b;e=defaultdict(Q);f=defaultdict(Q)
 if m:add(e,m*m,1/(m*m))
 if a:add(f,(1-p)*a*a,1/(a*a))
 if b:add(f,p*b*b,1/(b*b))
 variance=(1-p)*a*a+p*b*b-m*m
 certify_le(clean(e),clean(f),3*variance);scalar+=1

rows=[]
for h,b in ((2,2),(3,2),(3,3)):
 n=h+b;profiles=[(Q(1,2),)*n,tuple([Q(1,8),Q(1,2),Q(7,8)][i%3] for i in range(n))]
 for p,w in product(profiles,(Q(1,2),Q(3,2),Q(2))):
  for j in range(1,int(2*(w*h+b))+1):
   t=Q(j,2); vals=[2*int(w*(x&((1<<h)-1)).bit_count()+(x>>h).bit_count()>=t)-1 for x in range(1<<n)]
   u,mass,ref=transform(vals,p); da=db=M=Q(0); correction=Q(0)
   for s,v in enumerate(mass):
    a=(s&((1<<h)-1)).bit_count();z=(s>>h).bit_count()
    if a:da+=(a-1)*v
    if z:db+=(z-1)*v
    if a and z:M+=v;correction+=3*(int(a>=2)+int(z>=2))*v
   ck(deficit(mass)==da+db+M);ck(correction<=6*M)
   pure=expression(mass,ref,lambda s:s.bit_count()>=2 and (s<(1<<h) or not(s&((1<<h)-1))))
   averaged=defaultdict(Q); computed=[]; variances=[]
   for remaining in ('B','A'):
    condD=Q(0); defect=Q(0); e=defaultdict(Q)
    count=h if remaining=='B' else b; qs=p[:h] if remaining=='B' else p[h:]
    for x in range(1<<count):
     child=[vals[x|(y<<h)] for y in range(1<<b)] if remaining=='B' else [vals[y|(x<<h)] for y in range(1<<h)]
     _,cm,cr=transform(child,p[h:] if remaining=='B' else p[:h]); pi=prob(x,qs)
     condD+=pi*deficit(cm)
     for k,v in expression(cm,cr,lambda s:s.bit_count()>=2).items():e[k]+=pi*v
     for s,v in enumerate(cm):
      if s.bit_count()>=2:defect+=pi*v
    pure_part=expression(mass,ref,lambda s:(s>>h).bit_count()>=2 and not(s&((1<<h)-1))) if remaining=='B' else expression(mass,ref,lambda s:s<(1<<h) and s.bit_count()>=2)
    pure_mass=sum(v for s,v in enumerate(mass) if ((s>>h).bit_count()>=2 and not(s&((1<<h)-1))) if remaining=='B') if remaining=='B' else sum(v for s,v in enumerate(mass) if s<(1<<h) and s.bit_count()>=2)
    defect-=pure_mass
    spectral_defect=sum(v for s,v in enumerate(mass) if s&((1<<h)-1) and s>>h and ((s>>h).bit_count()>=2 if remaining=='B' else (s&((1<<h)-1)).bit_count()>=2))
    ck(defect==spectral_defect);ck(condD==(db if remaining=='B' else da))
    certify_le(pure_part,clean(e),3*defect)
    for k,v in e.items():averaged[k]+=v
    computed.append(str(condD));variances.append(str(defect))
   certify_le(pure,clean(averaged),correction)
   if M:
    marginal_a=defaultdict(Q);marginal_b=defaultdict(Q)
    for s,v in enumerate(mass):
     a=s&((1<<h)-1);z=s>>h
     if a and z:marginal_a[a]+=v;marginal_b[z]+=v
    ck(sum(marginal_a.values())==sum(marginal_b.values())==M)
    ea=defaultdict(Q);eb=defaultdict(Q);tc=defaultdict(Q);mlog=defaultdict(Q)
    for a,v in marginal_a.items():
     if v:add(ea,v,ref[a]/v)
    for z,v in marginal_b.items():
     if v:add(eb,v,ref[z<<h]/v)
    for s,v in enumerate(mass):
     a=s&((1<<h)-1);z=s>>h
     if a and z and v:add(tc,v,v*M/(marginal_a[a]*marginal_b[z]))
    add(mlog,M,M);right=defaultdict(Q,ea)
    for e,sign in ((eb,1),(mlog,1),(tc,-1)):
     for k,v in e.items():right[k]+=sign*v
    ck(expression(mass,ref,lambda s:bool(s&((1<<h)-1)) and bool(s>>h))==clean(right))
    ck(sum(marginal_a[a]*marginal_b[z]/(M*M) for a in marginal_a for z in marginal_b)==1)
   rows.append({'h':h,'b':b,'w':str(w),'t':str(t),'biases':[str(q) for q in p],'Delta':str(deficit(mass)),'D_A':str(da),'D_B':str(db),'M':str(M),'variance_correction':str(correction)})
   if time.monotonic()-start>60:raise RuntimeError('frozen pilot cap')

and_rows=[]
for m in range(1,7):
 atom=Q(4)**(1-2*m);M=(2**m-1)**2*atom
 degree=atom*(2*m*2**(m-1)*(2**m-1)-(2**m-1)**2)
 ck(degree/M==Q(2*m*2**(m-1),2**m-1)-1)
 # Exact entropy is displayed as rational coefficient of ln2.
 and_rows.append({'m':m,'M':str(M),'Delta_mixed':str(degree),'E_mixed_over_M_ln2_coefficient':4*m-2,'E_mixed_over_Delta_mixed_ln2_coefficient':str(Q(4*m-2)*M/degree)})
out={'helper':'A041-stage3-v1.1','assertions':checks,'binary_cases':binary,'composition_cases':composition,'scalar_cases':scalar,'two_group_cases':len(rows),'conjunction_cases':len(and_rows),'runtime_seconds':time.monotonic()-start,'two_group_certificates':rows,'mass_only_obstruction':and_rows}
(R/'out/EXACT_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ('two_group_certificates','mass_only_obstruction')},indent=2))
