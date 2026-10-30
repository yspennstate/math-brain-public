from discover import fw,R
from fractions import Fraction as Q
import json,time,hashlib
checks=0
def ck(b):
 global checks
 checks+=1
 assert b,checks
def mul(a,b,l,poly):
 c=0
 while b:
  if b&1:c^=a
  b>>=1;a<<=1
  if a>>l:a^=poly
 return c
def logs(x):
 ans={}
 for value,sgn in [(x.numerator,1),(x.denominator,-1)]:
  k=2
  while k*k<=value:
   while value%k==0:ans[k]=ans.get(k,0)+sgn;value//=k
   k+=1
  if value>1:ans[value]=ans.get(value,0)+sgn
 return {p:Q(c) for p,c in ans.items() if c}
def add(*terms):
 ans={}
 for a,fac in terms:
  for p,c in a.items():ans[p]=ans.get(p,Q(0))+fac*c
 return {p:c for p,c in ans.items() if c}
def entropy(p):return add(*[(logs(x),-x) for x in p if x])
def stats(table):
 N=len(table);n=N.bit_length()-1;w=fw(table);p=[Q(t*t,N*N) for t in w]
 ck(sum(p)==1)
 ds=[]
 for i in range(n):
  d=sum((p[s] for s in range(N) if s>>i&1),Q(0));edges=Q(sum(table[s]!=table[s^(1<<i)] for s in range(N)),N)
  ck(d==edges);ds.append(d)
 return w,p,ds,entropy(p)
def execute(l,poly):
 start=time.perf_counter();q=1<<l;N=1<<(3*l);n=3*l+2
 ck(all(mul(a,b,l,poly)!=0 for a in range(1,q) for b in range(1,q)))
 core=[]
 for s in range(N):
  a=s&(q-1);b=(s>>l)&(q-1);x=s>>(2*l)
  core.append((-1 if a&1 else 1)*(-1 if x==mul(a,b,l,poly) else 1))
 wh,ph,dh,Hh=stats(core);ck(wh[0]==0)
 c=1-Q(2,q);M=(q-1)*q*q;t=Q(4,q**4)
 special=(c*c if c else None);nonzero=[v for v in ph if v]
 ck(len(nonzero)==M+(1 if c else 0));ck(sum(v==t for v in nonzero)==M if l>1 else all(v==t for v in nonzero))
 if c:ck(nonzero.count(c*c)==1);ck(c*c+M*t==1)
 G=[];H=[]
 for s in range(1<<n):
  u=s.bit_count()&1;v=(s>>1)&1;bent=-1 if u*v else 1
  G.append(bent);H.append(bent*core[s>>2])
 wg,pg,dg,Hg=stats(G);wv,pv,dv,Hv=stats(H)
 ck(all(d==Q(1,2) for d in dg+dv));ck(Hg=={2:Q(2)});ck(Hv==add((Hh,1),({2:Q(2)},1)));ck(all(not(a and b) for a,b in zip(pg,pv)))
 parent=[(G[s>>1] if s&1==0 else H[s>>1]) for s in range(1<<(n+1))]
 wp,pp,dp,Hp=stats(parent);ck(all(d==Q(1,2) for d in dp))
 pe=[pp[2*s]+pp[2*s+1] for s in range(1<<n)]
 for s in range(1<<n):ck(pp[2*s]==pp[2*s+1]);ck(pe[s]==(pg[s]+pv[s])/2)
 ck(Hp==add((Hh,Q(1,2)),({2:Q(4)},1)))
 ck(add((Hp,1),(Hg,Q(-1,2)),(Hv,Q(-1,2)))=={2:Q(2)})
 r=Q(0);reference_only=0
 for s in range(1<<n):
  if pe[s]:k=pg[s]/(2*pe[s]);ck(k in [0,1])
  else:k=Q(1,2);reference_only+=1
  r+=k/Q(1<<n)
 ck(0<r<1);ck(1-r>0)
 ag=Q(sum(bool(x) for x in pg),1<<n);ah=Q(sum(bool(x) for x in pv),1<<n);eps=Q(reference_only,1<<n)
 ck(ag+ah+eps==1);ck(r==ag+eps/2)
 if l>=2:
  ck(ag==Q(1,q**3));ck(ah==1-Q(1,q)+Q(1,q**3));ck(eps==Q(1,q)-Q(2,q**3));ck(r==Q(1,2*q));ck(4*r*(1-r)<Q(2,q));ck(r<=Q(1,8))
  # Actual entropy dictionaries preserve both full terminal H and TC.
  Kp=add(({2:Q(n+1)},1),(Hp,-1));Kmean=add(({2:Q(n)},1),(Hg,Q(-1,2)),(Hv,Q(-1,2)))
  ck(add((Kmean,1),(Kp,-1))=={2:Q(1)})
  O=add((logs(4*r*(1-r)),Q(-1,2)));D=add((O,1),(Kmean,1),(Kp,-1));ck(D==add((O,1),({2:Q(1)},1)))
  ck(Q(l+2,2)<Q(Q(9*l,2)+2,4));ck(Q(4)+Q(3*l,2)<Q(3*l+3))
 else:ck(r!=Q(1,2*q));ck(c==0)
 return dict(l=l,polynomial=poly,dimension_parent=n+1,source_core_support=len(nonzero),r_G=str(r),reference_only_atoms=reference_only,influences='all1/2',core_H={str(p):str(v) for p,v in Hh.items()},parent_H={str(p):str(v) for p,v in Hp.items()},child_H=[{str(p):str(v) for p,v in H.items()} for H in [Hg,Hv]],truth_table_sha256=hashlib.sha256(bytes(x+1 for x in parent)).hexdigest(),seconds=time.perf_counter()-start,boundary_excluded=l==1)
start=time.perf_counter();rows=[execute(l,p) for l,p in [(1,3),(2,7),(3,11)]]
out=dict(status='PASS',checks=checks,seconds=time.perf_counter()-start,rows=rows,arithmetic='integer Walsh, Fraction, exact prime-log identities and rational sign comparisons; no floating entropy signs')
ck(out['seconds']<55)
(R/'out'/'FAMILY_CERTIFICATE.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
