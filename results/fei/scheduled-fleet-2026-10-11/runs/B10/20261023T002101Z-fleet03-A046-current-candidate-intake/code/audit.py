from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import json,time
RUN=Path(__file__).resolve().parents[1];START=time.perf_counter();COUNT=0
def ck(p):
 global COUNT
 assert p
 COUNT+=1
 assert time.perf_counter()-START<55
def iv(v):return tuple(map(Q,v))
def add(a,b):return a[0]+b[0],a[1]+b[1]
def scale(a,c):return (a[0]*c,a[1]*c) if c>=0 else (a[1]*c,a[0]*c)
def sub(a,b):return add(a,scale(b,-1))
def lnu(x):
 z=(x-1)/(x+1);v=z;s=Q(0)
 for k in range(40):s+=v/(2*k+1);v*=z*z
 return 2*s,2*s+2*v/(81*(1-z*z))
ln2=lnu(Q(2))
@lru_cache(None)
def log(x):
 k=x.numerator.bit_length()-x.denominator.bit_length();y=x/Q(2)**k
 if y<1:y*=2;k-=1
 a,b=lnu(y);return a/ln2[1]+k,b/ln2[0]+k
def kl(p,q):
 out=(Q(0),Q(0))
 for s,v in p.items():
  v=Q(v)
  if v:ck(Q(q.get(s,0))>0);out=add(out,scale(sub(log(v),log(Q(q[s]))),v))
 return out
def entropy(p):
 out=(Q(0),Q(0))
 for v in p.values():
  v=Q(v)
  if v:out=add(out,scale(log(v),-v))
 return out
def eqoverlap(a,b):ck(max(a[0],b[0])<=min(a[1],b[1]))
def lawcheck(p):ck(all(Q(v)>=0 for v in p.values()));ck(sum(map(Q,p.values()))==1)
def prescribed_factor_product(m,r,path,tilt):
 out={0:Q(1)}
 for j in range(m):
  block=list(range(3+j*r,3+(j+1)*r));live=[i for i in block if str(i) not in path]
  if any(path.get(str(i))==0 for i in block) or not live:f={0:Q(1)}
  elif len(live)==1:f={1<<live[0]:Q(1)}
  else:
   d=Q(1,1<<len(live));v=4*d*(1-d);f={0:(1-2*d)**2};full=sum(1<<i for i in live)
   for a in range(1,1<<len(live)):
    mask=sum(1<<live[k] for k in range(len(live)) if a>>k&1)
    f[mask]=(1-tilt)*4*d*d+(v*tilt if mask==full else 0)
  out={s|t:a*b for s,a in out.items() for t,b in f.items()}
 return out
roots=set();positive=0;least=None
paths=sorted((RUN/'out').glob('m*r*_*.json'));ck(len(paths)==27)
for path in paths:
 d=json.loads(path.read_text(encoding='utf-8'));m=d['m'];r=d['r'];delta=Q(1,1<<r)
 p,q=d['root_P'],d['root_Q'];lawcheck(p);lawcheck(q)
 qcore=prescribed_factor_product(m,r,{},Q(1,8))
 expected={int(s):Q(w) for s,w in p.items() if int(s)<8}
 for s,w in qcore.items():
  if s:
   for c in (0,1,4,5):expected[s|c]=w/16
 ck({int(s):Q(w) for s,w in q.items()}==expected)
 A=kl(p,q);H=entropy(p);eqoverlap(A,iv(d['root_KL']));eqoverlap(H,iv(d['root_H']))
 if (m,r) not in roots:
  roots.add((m,r));N=1<<(3+m*r)
  t=[]
  for x in range(N):
   h=(-1)**sum(all(x>>(3+j*r+k)&1 for k in range(r)) for j in range(m))
   t.append(1-2*(x>>1&1) if not x&1 else h if x&4 else 1)
  for s in range(N):
   a=sum(t[x]*(-1 if (s&x).bit_count()%2 else 1) for x in range(N))
   ck(Q(p.get(str(s),0))==Q(a*a,N*N))
  physical=sum(Q(sum(t[x]!=t[x^(1<<i)] for x in range(N)),N) for i in range(3+m*r))
  ck(physical==Q(d['root_I']))
 sig=(Q(0),Q(0));fresh=(Q(0),Q(0))
 for row in d['exercised_resets']:
  for name in ['P','old_Q','new_Q']:lawcheck(row[name])
  old=kl(row['P'],row['old_Q']);new=kl(row['P'],row['new_Q']);w=Q(row['w'])
  qg=prescribed_factor_product(m,r,row['data_path'],Q(1,7))
  if row['controller']=='x':desired=qg
  else:
   desired={int(s):Q(w) for s,w in row['P'].items() if int(s)<8}
   for s,mass in qg.items():
    if s:desired[s]=mass/4;desired[s|1]=mass/4
  ck({int(s):Q(w) for s,w in row['new_Q'].items()}==desired)
  eqoverlap(old,iv(row['old_K']));eqoverlap(new,iv(row['new_K']))
  inc=sub(new,old);eqoverlap(inc,iv(row['sigma']));sig=add(sig,scale(inc,w));fresh=add(fresh,scale(new,w))
  if inc[0]>0:positive+=1
 eqoverlap(sig,iv(d['signed_reset_total']));eqoverlap(fresh,iv(d['actual_fresh_KL']))
 ck(Q(d['conditional_variance_expectation'])<=Q(d['original_variance_sum']))
 cap=scale(log(Q(7,6)),Q(d['original_variance_sum'])/4)
 ck(fresh[1]<cap[0]);ck(cap[1]<m*delta/4)
 Hf=(Q(0),Q(0));Kf=(Q(0),Q(0));If=Q(0);reach=Q(0)
 for row in d['final_rows']:
  lawcheck(row['P']);lawcheck(row['Q']);w=Q(row['w']);reach+=w
  Hf=add(Hf,scale(entropy(row['P']),w));Kf=add(Kf,scale(kl(row['P'],row['Q']),w));If+=w*Q(row['I'])
 ck(reach==1)
 S=sub((4*If,4*If),Hf);I=Q(d['root_I'])
 edge=sub(sub(H,Hf),(4*(I-If),)*2);net=add(add(A,edge),sig)
 positivepart=max(Q(0),net[0]),max(Q(0),net[1])
 paid=sub(sub(S,positivepart),(Q(1,4),)*2)
 ck(paid[0]>Q(7,10));eqoverlap(paid,iv(d['after_old_booking']))
 eqoverlap(add(A,sig),add(iv(d['old_source_releases']),Kf))
 least=paid[0] if least is None else min(least,paid[0])
ck(positive==56);ck(7**4<2*6**4)
out={'status':'PASS','reference_recipe_reconstructed':True,'helper_version':'audit-v2-recipe-weight-fixed','checks':COUNT,'cases':len(paths),'independent_direct_character_roots':len(roots),'positive_reset_nodes':positive,'lowest_certified_finite_margin':str(least),'runtime_seconds':time.perf_counter()-START,'arithmetic':'independent40-term logs/direct character root/physical edges/persisted full probability laws','not_certified_by_this_audit':'unbounded quantifiers or source-level analytic proof; those are PROOF.md and external review pending'}
(RUN/'out/AUDIT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:out[k] for k in ['status','checks','cases','positive_reset_nodes','runtime_seconds']}))
