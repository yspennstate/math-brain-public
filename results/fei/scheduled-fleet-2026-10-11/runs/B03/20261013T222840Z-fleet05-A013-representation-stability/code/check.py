from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json,time,hashlib
RUN=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def check(b):
 global checks
 checks+=1
 if time.perf_counter()-start>50:raise RuntimeError('50 second internal cutoff')
 if not b:raise AssertionError(checks)
def fwht(t):
 a=list(t);h=1
 while h<len(a):
  for j in range(0,len(a),2*h):
   for k in range(j,j+h):
    u,v=a[k],a[k+h];a[k]=u+v;a[k+h]=u-v
  h*=2
 return [F(x,len(a)) for x in a]
@lru_cache(None)
def factors(n):
 out=[];p=2
 while p*p<=n:
  e=0
  while n%p==0:n//=p;e+=1
  if e:out.append((p,e))
  p+=1
 if n>1:out.append((n,1))
 return tuple(out)
@lru_cache(None)
def lv(x):
 x=F(x);assert x>0;a={}
 for p,e in factors(x.numerator):a[p]=F(e)
 for p,e in factors(x.denominator):a[p]=a.get(p,F(0))-e
 return {p:e for p,e in a.items() if e}
def add(a,b,k=F(1)):
 a=dict(a)
 for p,v in b.items():
  a[p]=a.get(p,F(0))+k*v
  if not a[p]:del a[p]
 return a
def mul(a,k):return {p:v*k for p,v in a.items() if v*k}
def H(p):
 a={}
 for x in p:
  if x:a=add(a,lv(1/x),x)
 return a
def CE(p,q):
 a={}
 for x,y in zip(p,q):
  if x:
   check(y>0);a=add(a,lv(1/y),x)
 return a
def lniv(x):
 u=(x-1)/(x+1);lo=sum((2*u**(2*j+1)/F(2*j+1) for j in range(20)),F(0))
 return lo,lo+2*u**41/(41*(1-u*u))
lnlo,lnhi=lniv(F(2));check(lnlo>F(2,3));check(lnhi<1)
@lru_cache(None)
def logiv(x):
 x=F(x);k=0
 while x>=2:x/=2;k+=1
 while x<1:x*=2;k-=1
 lo,hi=lniv(x);return F(k)+lo/lnhi,F(k)+hi/lnlo
def iv(v):
 lo=hi=F(0)
 for p,c in v.items():
  a,b=logiv(p);lo+=c*(a if c>0 else b);hi+=c*(b if c>0 else a)
 return lo,hi
def nonneg(v):check(not v or iv(v)[0]>=0)
def refs(p):
 u=[F(1,len(p))]*len(p)
 return [p,u,[(a+b)/2 for a,b in zip(p,u)]]
def cal(p,r,shared):
 rem=1-sum(p[s] for s in shared);old=1-sum(r[s] for s in shared)
 assert not rem or old>0
 return [p[s] if s in shared else (rem*r[s]/old if rem else F(0)) for s in range(len(p))]
def influence(t,n):return [F(sum(t[x]!=t[x^(1<<j)] for x in range(len(t))),len(t)) for j in range(n)]
tables=[[1 if mask>>x&1 else -1 for x in range(4)] for mask in range(16)]
pairs=reference_cases=activation_cases=restrictions=0
boundary=[];max_b_ratio=F(0)
for shared_layout in [True,False]:
 n=4 if shared_layout else 5;zi=n-1
 shared={0,1} if shared_layout else {0}
 def embed_g(s):return s
 def embed_h(s):return (s&1)|((s>>1)<<2) if shared_layout else s<<2
 for gi,g in enumerate(tables):
  ug=fwht(g);pg=[x*x for x in ug]
  for hi,h in enumerate(tables):
   uh=fwht(h);ph=[x*x for x in uh]
   table=[]
   for x in range(1<<n):
    gx=x&3;hx=(x&1)|(((x>>2)&1)<<1) if shared_layout else (x>>2)&3
    table.append(g[gx] if not (x>>zi)&1 else h[hx])
   fhat=fwht(table);pf=[x*x for x in fhat]
   eg=[F(0)]*(1<<zi);eh=[F(0)]*(1<<zi)
   for s,a in enumerate(ug):eg[embed_g(s)]=a
   for s,a in enumerate(uh):eh[embed_h(s)]=a
   for t in range(1<<zi):
    check(fhat[t]==(eg[t]+eh[t])/2)
    check(fhat[t+(1<<zi)]==(eg[t]-eh[t])/2)
   qbar=[(a*a+b*b)/2 for a,b in zip(eg,eh)]
   erasure=add(H(pf),H(qbar),F(-1))
   delta=add(H(pf),mul(add(H(pg),H(ph)),F(1,2)),F(-1))
   js=add(H(qbar),mul(add(H(pg),H(ph)),F(1,2)),F(-1))
   d=influence(table,n)[zi]
   check(d==(1-sum(a*b for a,b in zip(eg,eh)))/2)
   check(add(erasure,js)==delta)
   nonneg(add(lv(2),erasure,F(-1)) if not d else add(mul(lv(2),4*d),erasure,F(-1)))
   if not d:check(not erasure and not delta)
   nonneg(add(mul(lv(2),7*d),delta,F(-1)))
   nonneg(js)
   check(sum(influence(table,n))==sum(influence(g,2)+influence(h,2))/2+d)
   if shared_layout:
    al=[F(g[y]+g[y+2],2) for y in [0,1]];be=[F(h[y]+h[y+2],2) for y in [0,1]]
    c=[1 if a+b>=0 else -1 for a,b in zip(al,be)]
    sy=[(2-cy*(a+b))/2 for a,b,cy in zip(al,be,c)];s=sum(sy)/2
    check(all(0<=t<=1 for t in sy));check(d>= (s*(1-s) if s<=F(1,2) else s/2))
    translated=[table[x]*c[x&1] for x in range(1<<n)];pt=[a*a for a in fwht(translated)]
    qb=[pt[t]+pt[t+(1<<zi)] for t in range(1<<zi)]
    check(add(H(pt),H(qb),F(-1))==erasure)
   for rg in refs(pg):
    rgc=cal(pg,rg,shared);check(sum(rgc)==1);nonneg(add(CE(pg,rg),CE(pg,rgc),F(-1)))
    for rh in refs(ph):
     rhc=cal(ph,rh,shared);check(sum(rhc)==1);nonneg(add(CE(ph,rh),CE(ph,rhc),F(-1)))
     q=[F(0)]*(1<<n)
     for t in range(1<<zi):
      for u in [0,1]:
       s=t|(u<<zi)
       if (t<2 if shared_layout else t==0):q[s]=pf[s]
     for t in range(4):
      if t not in shared:
       for u in [0,1]:q[embed_g(t)|(u<<zi)]=rgc[t]/4;q[embed_h(t)|(u<<zi)]=rhc[t]/4
     check(sum(q)==1)
     cg=CE(pg,rgc);ch=CE(ph,rhc);cf=CE(pf,q)
     check(cf==add(mul(add(cg,ch),F(1,2)),delta))
     check(add(cf,H(pf),F(-1))==mul(add(add(cg,H(pg),F(-1)),add(ch,H(ph),F(-1))),F(1,2)))
     vg=1-sum(pg[s] for s in shared);vh=1-sum(ph[s] for s in shared)
     sector=[pf[embed_g(t)|(u<<zi)] for t in sorted(shared) for u in [0,1]]+[vg/2,vh/2]
     chain=add(H(sector),lv(2),(vg+vh)/2)
     if vg:chain=add(chain,CE([pg[t]/vg for t in range(4) if t not in shared],[rgc[t]/vg for t in range(4) if t not in shared]),vg/2)
     if vh:chain=add(chain,CE([ph[t]/vh for t in range(4) if t not in shared],[rhc[t]/vh for t in range(4) if t not in shared]),vh/2)
     check(cf==chain);reference_cases+=1
   if shared_layout:
    gates=[]
    for v in range(4):
     if g[v]==1:gates.append({0:v&1,1:v>>1,3:0})
     if h[v]==1:gates.append({0:v&1,2:v>>1,3:1})
    check(len(gates)==sum(a==1 for a in g+h))
    for i in range(4):
     for val in [0,1]:
      rem=[j for j in range(4) if j!=i];child=[]
      retained=[{j:b for j,b in gate.items() if j!=i} for gate in gates if i not in gate or gate[i]==val]
      for x in range(8):
       xx=val<<i
       for k,j in enumerate(rem):xx|=((x>>k)&1)<<j
       child.append(table[xx])
       truth=any(all((xx>>j)&1==b for j,b in gate.items()) for gate in retained)
       check(truth==(table[xx]==1))
      nc=len(retained)
      for gate in retained:
       pi=F(1,1<<len(gate));odds=pi/nc;root=odds/(1+odds)
       check(root==pi/(nc+pi))
      if i!=3:
       zchild=rem.index(3);cc=fwht(child);pc=[a*a for a in cc]
       residual=[F(0)]*4
       for ss,w in enumerate(pc):residual[(ss&((1<<zchild)-1))|((ss>>(zchild+1))<<zchild)]+=w
       bc=add(H(pc),H(residual),F(-1));dc=influence(child,3)[zchild]
       nonneg(add(mul(lv(2),4*dc),bc,F(-1)))
      restrictions+=1
   pairs+=1
 print('mux layout complete',shared_layout,'seconds',time.perf_counter()-start,flush=True)

for g in tables:
 pg=[a*a for a in fwht(g)];mu=F(sum(g),4)
 for r in [1,2]:
  p=F(1,1<<r);ctl=(1<<r)-1
  t=[g[x>>r] if x&ctl==0 else 1 for x in range(1<<(r+2))];pf=[a*a for a in fwht(t)]
  for rg in refs(pg):
   rc=cal(pg,rg,{0});q=[]
   for ss in range(len(pf)):
    u,T=ss&ctl,ss>>r
    q.append((1-p*(1-mu))**2 if ss==0 else (p*p*(1-mu)**2 if not T else p*p*rc[T]))
   check(sum(q)==1)
   cf=CE(pf,q);cg=CE(pg,rc)
   check(add(cf,H(pf),F(-1))==mul(add(cg,H(pg),F(-1)),p))
   nonneg(add(add(mul(cg,p),lv(2),6*r*p*(1-mu)),cf,F(-1)))
   check(sum(influence(t,r+2))==p*(sum(influence(g,2))+r*(1-mu)))
   activation_cases+=1

for m in [4,6,8,10]:
 g=[]
 for x in range(1<<m):g.append((-1)**(sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(m//2))))
 h=list(g);h[0]*=-1;t=g+h
 uh=fwht(t);p=[a*a for a in uh];q=[p[x]+p[x+(1<<m)] for x in range(1<<m)]
 b=add(H(p),H(q),F(-1));d=F(1,1<<m)
 check(influence(t,m+1)[m]==d)
 for ss in range(1<<m):
  check(uh[ss+(1<<m)]**2==F(1,1<<(2*m)))
  check((uh[ss]**2+uh[ss+(1<<m)]**2)/uh[ss+(1<<m)]**2>=1<<(m-1))
 nonneg(add(b,lv(2),-(m-1)*d))
 if m>=6:nonneg(add(b,lv(2),-4*d));check(iv(add(b,lv(2),-4*d))[0]>0)
 lo,hi=iv(mul(b,1/d));grid=1<<48
 boundary.append({'m':m,'selector_influence':str(d),'erasure_over_influence_interval':[str(F(lo.numerator*grid//lo.denominator,grid)),str(F(-((-hi.numerator*grid)//hi.denominator),grid))]})
result={'helper':'A013-one-shared-bit-v1','status':'PASS','Boolean_mux_pairs':pairs,'reference_pairs':reference_cases,'activation_reference_cases':activation_cases,'physical_restrictions':restrictions,'bent_boundary_cases':boundary,'exact_assertions':checks,'elapsed_seconds':time.perf_counter()-start,'failures':0,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(RUN/'out/EXACT_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
