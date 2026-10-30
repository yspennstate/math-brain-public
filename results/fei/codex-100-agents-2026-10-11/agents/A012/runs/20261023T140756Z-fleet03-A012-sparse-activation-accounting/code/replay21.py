from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time
R=Path(__file__).resolve().parents[1];BASE=R.parents[1];T=time.perf_counter();checks=0
def ck(v):
 global checks
 assert v,checks;checks+=1
 assert time.perf_counter()-T<50
A=json.loads((R/'out/FULL.json').read_text(encoding='utf-8'));ck(A['status']=='PAID')
target=json.loads((BASE/'runs/20261023T053904Z-fleet03-A012-sparse-activation-accounting/out/NEXT_TARGET.json').read_text(encoding='utf-8'))
truth=[]
for x in range(64):
 s=x&7;u=(x>>3)&1;v=(x>>4)&1;z=x>>5;c=-1 if s==0 else 1
 g=c*(-1 if s==0 and u==0 else 1);h=c*(-1 if s==1 and v==0 else 1);truth.append(g if z==0 else h)
ck(truth==target['F']);Q=list(map(F,target['root_Q']))
def spectral(v):return [F(sum(v[x]*(-1)**((x&m).bit_count()%2) for x in range(len(v)))**2,len(v)**2) for m in range(len(v))]
ck(spectral(truth)==Q)
@lru_cache(None)
def raw(s):
 free=[j for j,a in enumerate(s) if a==-1];v=[truth[x] for x in range(64) if all(a==-1 or ((x>>j)&1)==a for j,a in enumerate(s))];p=spectral(v);q=[F(0)]*len(p)
 for t,x in enumerate(Q):q[sum(((t>>j)&1)<<k for k,j in enumerate(free))]+=x
 ck(sum(p)==sum(q)==1)
 inf=sum((x*m.bit_count() for m,x in enumerate(p)),F(0));mask=sum(1<<k for k,j in enumerate(free) if j<3);shared=sum((x*(m&mask).bit_count() for m,x in enumerate(p)),F(0))
 return p,q,inf,shared,free
@lru_cache(maxsize=20000)
def log2(q):
 if q==1:return F(0),F(0)
 N=4096;n=q.numerator**N;d=q.denominator**N;k=n.bit_length()-d.bit_length()
 def ge(k):return n>=(d<<k) if k>=0 else (n<<(-k))>=d
 if not ge(k):k-=1
 ck(ge(k) and not ge(k+1));return F(k,N),F(k+1,N)
def bitlogsum(p,q):
 l=h=F(0)
 for x,y in zip(p,q):
  if x:ck(y>0);a,b=log2(x/y);l+=x*a;h+=x*b
 return l,h
z=F(1,3);N=20;elllo=sum((2*z**(2*j+1)/F(2*j+1) for j in range(N)),F(0));ellhi=elllo+2*z**(2*N+1)/F(2*N+1)/(1-z*z)
def klnats(p,q):
 l,h=bitlogsum(p,q);return l*(elllo if l>=0 else ellhi),h*(ellhi if h>=0 else elllo)
records={}
for x in A['DP_super_solution'].values():records[(tuple(x['state']),None if x['anchor'] is None else tuple(x['anchor']))]=F(x['upper_potential_nats'])
transactions={}
for x in A['transactions'].values():
 s=tuple(x['anchor']);p,q,_,_,_=raw(s);r0=(p[0]+q[0])/2;beta=(1-r0)/(1-q[0]);r=[r0]+[beta*y for y in q[1:]]
 ck(beta==F(x['beta']));ck(r==list(map(F,x['R_at_transaction'])));ck(sum(r)==1)
 hi=klnats(r,q)[1];cup=F(x['conversion_nats'][1]);ck(hi<=cup);transactions[s]=(beta,cup)
def step(s,j,b):
 v=list(s);v[j]=b;return tuple(v)
def bound(s,anchor):
 if anchor is None and s[0]!=-1 and s[1]!=-1 and s[2]==-1:return transactions[s][1]+records[(s,s)]
 return records[(s,anchor)]
for (s,anchor),w in records.items():
 p,q,inf,shared,free=raw(s)
 if anchor is not None:
  beta=transactions[anchor][0];q=[1-beta*(1-q[0])]+[beta*y for y in q[1:]]
 ck(sum(q)==1 and min(q)>=0);ck(klnats(p,q)[1]<=w)
 for k,j in enumerate(free):
  d0=step(s,j,0);d1=step(s,j,1);ck(w>=(bound(d0,anchor)+bound(d1,anchor))/2)
  e=sum((x for m,x in enumerate(p) if (m>>k)&1),F(0));i0=raw(d0);i1=raw(d1)
  ck(inf==e+(i0[2]+i1[2])/2)
  ck(shared==(i0[3]+i1[3])/2+(e if j<3 else 0))
root=(-1,)*6;w=bound(root,None)
# H(root) in bits from independent integer-log intervals, not author prime logs.
hl=hh=F(0)
for x in Q:
 if x:a,b=log2(1/x);hl+=x*a;hh+=x*b
Klo=4+2/ellhi;Khi=4+2/elllo;bhi=F(5,4)/elllo;blo=F(5,4)/ellhi
stocklo=Klo*F(7,8)-bhi-hh;stockhi=Khi*F(7,8)-blo-hl
marginlo=stocklo-w/elllo;marginhi=stockhi-F(A['worst_terminal_KL_plus_all_fees_nats'][0])/ellhi
ck(marginlo>0);delta=F((marginlo*1024).__floor__()-1,1024);ck(delta>0 and marginlo>delta)
# All prescribed U terminals are rebuilt from current full references.
for x in A['prescribed_U_full_terminals']:
 s=tuple(x['physical_state']);anchor=tuple(x['anchor']);p,q,inf,_,_=raw(s);beta=transactions[anchor][0];q=[1-beta*(1-q[0])]+[beta*y for y in q[1:]]
 ck(p==list(map(F,x['P'])) and q==list(map(F,x['Q_current'])) and inf==F(x['I']))
def enc(v):
 if isinstance(v,F):return str(v)
 if isinstance(v,dict):return {str(k):enc(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [enc(x) for x in v]
 return v
out={'status':'PASS','assertions':checks,'seconds':time.perf_counter()-T,'certificate_states_checked':len(records),'transactions_checked':len(transactions),'raw_states_recomputed':raw.cache_info().currsize,'all_policy_margin_bits_interval':[marginlo,marginhi],'uniform_margin_delta_bits':delta,'original_source_spare_bits':[stocklo,stockhi],'root_full_KL_plus_fees_upper_nats':w,'physical_influence_owner_identities':'checked for every saved physical edge','not_independent_agent_acceptance':True}
(R/'out/REPLAY.json').write_bytes((json.dumps(enc(out),indent=2)+'\n').encode('utf-8'))
print(json.dumps({**{k:v for k,v in out.items() if k not in ('all_policy_margin_bits_interval','original_source_spare_bits','root_full_KL_plus_fees_upper_nats','uniform_margin_delta_bits')},'all_policy_margin_bits_interval':[float(marginlo),float(marginhi)],'uniform_margin_delta_bits':str(delta)}))
