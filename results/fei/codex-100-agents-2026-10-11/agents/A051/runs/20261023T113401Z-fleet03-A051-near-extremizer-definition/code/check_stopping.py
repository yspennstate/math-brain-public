from pathlib import Path
from fractions import Fraction as F
import sys,time,json,hashlib
import exact_utils as x
R=Path(__file__).resolve().parents[1];START=time.monotonic();PILOT='--pilot' in sys.argv;C=0
def ck(z):
 global C
 C+=1;assert z,C
 if time.monotonic()-START>55:raise RuntimeError('55s frozen cap')
def hb(u):
 a=u.numerator;b=u.denominator
 r={p:F(e) for p,e in x.factor(b).items()}
 for z in [a,b-a]:
  if z:r=x.plus(r,{p:-F(z*e,b) for p,e in x.factor(z).items()})
 return r
def canonical(f,ref,ids):
 n=len(f).bit_length()-1;s=x.stats(f);rows=[];span={0}
 for v in sorted(range(1,1<<n),key=lambda v:(s['m'][v],v)):
  if v not in span:rows.append(v);span|={z^v for z in tuple(span)}
 b=sum((s['w'][v]>F(1,2))<<j for j,v in enumerate(rows))
 out=[];rr=[];ii=[]
 for y in range(1<<n):
  z=0
  for j,v in enumerate(rows):
   if y>>j&1:z^=v
  sg=-1 if x.par(b&y) else 1
  out.append(f[z]*sg);rr.append(ref[z]*sg);ii.append(ids[z])
 ck(tuple(out)==s['canonical']);return tuple(out),tuple(rr),tuple(ii)
def tree(f,ref,mode):
 root=f;Z=tuple(a!=b for a,b in zip(f,ref));nodes=[];leaves=[]
 def rec(g,c,ids,dep,reach):
  n=len(g).bit_length()-1;s=x.stats(g);q=F(sum(a!=b for a,b in zip(g,c)),len(g))
  ck(q==F(sum(Z[j] for j in ids),len(ids)))
  if n==0 or (mode==1 and len(set(g))==1) or (mode==2 and dep>=1):
   leaves.append((reach,dep,q,s));return
  i=n-1 if mode==1 else (min(range(n),key=lambda j:(s['p'][j],j)) if mode==3 else 0)
  ck(min(s['p'][i],1-s['p'][i])<=min(2*q,F(1,2)))
  cs=[];rho=F(0)
  for b in [0,1]:
   pos=[z for z in range(len(g)) if (z>>i)&1==b]
   gg=tuple(g[z] for z in pos);cc=tuple(c[z] for z in pos);jj=tuple(ids[z] for z in pos)
   old=x.stats(gg)
   if mode==1 or mode==2 or (mode==3 and b):gg,cc,jj=canonical(gg,cc,jj)
   new=x.stats(gg);ck(new['I']<=old['I'] and new['H']==old['H'])
   rho+=(old['I']-new['I'])/2;cs.append((gg,cc,jj))
  ck(sum((F(sum(a!=b for a,b in zip(gg,cc)),len(gg)) for gg,cc,_ in cs),F(0))/2==q)
  L=x.sub(s['H'],x.plus(*(x.scale(F(1,2),x.stats(gg)['H']) for gg,_,_ in cs)))
  nodes.append((reach,q,L,s['p'][i]+rho))
  for gg,cc,jj in cs:rec(gg,cc,jj,dep+1,reach/2)
 rec(f,ref,tuple(range(len(f))),0,F(1))
 d=sum((w for w,_,_,_ in nodes),F(0));a=sum((w*q for w,q,_,_ in nodes),F(0))
 ck(d==sum((w*dep for w,dep,_,_ in leaves),F(0)))
 ck(a==sum((w*q*dep for w,dep,q,_ in leaves),F(0)))
 ck(sum((w for w,_,_,_ in leaves),F(0))==1)
 leafH=x.plus(*(x.scale(w,s['H']) for w,_,_,s in leaves))
 L=x.sub(x.stats(f)['H'],leafH)
 ck(L==x.plus(*(x.scale(w,ell) for w,_,ell,_ in nodes)))
 spend=sum((w*q for w,_,_,q in nodes),F(0));leafI=sum((w*s['I'] for w,_,_,s in leaves),F(0))
 ck(x.stats(f)['I']==spend+leafI)
 if d:
  u=min(2*a/d,F(1,2));b=hb(u);blo,bhi=x.interval(b);lo,hi=x.interval(L)
  # Lower enclosure of proven upper budget used to certify every replay.
  ck(hi<=d*(blo+2*u/x.LN2[1]))
  for K in [0,1,2,4]:
   D=x.sub(x.stats(f)['H'],x.const(K*x.stats(f)['I']))
   LD=x.sub(leafH,x.const(K*leafI))
   ck(x.interval(x.sub(D,LD))[1]<=d*(blo+2*u/x.LN2[1]))
 else:ck(not L and a==0)
 return len(nodes),len(leaves)
roots=[x.table(n,t) for n in range(3 if PILOT else 4) for t in range(1<<(1<<n))]
policies=nodes=leaves=0
for f in roots:
 s=x.stats(f);z=max(range(len(f)),key=lambda j:abs(s['a'][j]));sg=1 if s['a'][z]>=0 else -1
 best=tuple(sg*(-1 if x.par(z&y) else 1) for y in range(len(f)))
 for ref in [best,(1,)*len(f)]:
  for mode in range(4):
   nn,ll=tree(f,ref,mode);policies+=1;nodes+=nn;leaves+=ll
result={'status':'PASS','pilot':PILOT,'root_tables':len(roots),'complete_policies':policies,'internal_nodes':nodes,'complete_leaves':leaves,'assertions':C+x.COUNT,'own_assertions':C,'utility_assertions':x.COUNT,'runtime_seconds':time.monotonic()-START,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'utility_sha256':hashlib.sha256(Path(x.__file__).read_bytes()).hexdigest(),'arithmetic':'integer Walsh, exact physical error events and ancestry labels, Fraction, prime-log entropy and rational32-term atanh enclosures','scope':'four fixed policy rules/two references, not an exhaustive policy census; theorem is analytic'}
(R/'out'/('PILOT.json' if PILOT else 'CHECK.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
