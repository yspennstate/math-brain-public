from pathlib import Path
from fractions import Fraction as Q
import json,time,sys
ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT.parent/'20261012T010436Z-fleet05-A018-shared-data-collision-law/code/check_lead.py'
ns={'__file__':str(OLD),'__name__':'arithmetic_only'}
exec(compile(OLD.read_text(encoding='utf8').split("\nresult={'helper_version'")[0],str(OLD),'exec'),ns)
start=time.perf_counter();checks=0
def ck(x):
 global checks
 checks+=1;assert x;assert time.perf_counter()-start<60
def W(v):
 if len(v)==1:return v[:]
 k=len(v)//2;a=W(v[:k]);b=W(v[k:])
 return [x+y for x,y in zip(a,b)]+[x-y for x,y in zip(a,b)]
def H(v):
 w=W(v);N=len(v)
 return ns['ent']([Q(x*x,N*N) for x in w])
rows=[]
fixtures=[(4,[8,14])] if '--pilot' in sys.argv else [(4,[mask]) for mask in range(16)]+[(4,[8,14]),(6,[8,14])]
for m,masks in fixtures:
 a=len(masks);n=2+a*m;L=1<<n;delta=Q(1,1<<m)
 def value(i):
  b=i&3;result=1
  for j,mask in enumerate(masks):
   t=(i>>(2+j*m))&((1<<m)-1)
   parity=sum(((t>>k)&1)*((t>>(k+1))&1) for k in range(0,m,2))%2
   c=1-2*parity
   result*=c-2*int(t==0)*((mask>>b)&1)
  return result
 v=[value(i) for i in range(L)];w=W(v);ck(w==ns['fw'](v))
 I=Q(0);d=Q(0)
 for bit in range(n):
  physical=Q(sum(v[i]!=v[i^(1<<bit)] for i in range(L)),L)
  spectral=Q(sum(x*x for s,x in enumerate(w) if s&(1<<bit)),L*L)
  ck(physical==spectral);I+=physical
  if bit<2:d+=physical
 J=a*Q(m,2)+2*m*delta*sum(Q(mask.bit_count(),4) for mask in masks)
 ck(I==J+d)
 E=Q(sum(x*x for s,x in enumerate(w) if s&3==3),L*L)
 Tpriv=2*sum(Q(x*x,L*L)*(s>>2).bit_count()*(s&3).bit_count() for s,x in enumerate(w))
 T=Tpriv+2*E
 ck(Tpriv<=2*J and 2*E<=d and T<=2*I)
 owner=Q(0)
 for bit in (0,1):
  other=1-bit
  for history in (0,1):
   b=history<<other;bp=b|(1<<bit)
   changed=[int(((mask>>b)^(mask>>bp))&1) for mask in masks]
   for j,mask in enumerate(masks):
    Jed=Q(m,2)+m*delta*(((mask>>b)&1)+((mask>>bp)&1))
    kap=m*delta*changed[j]/2
    q=(1-2*delta)**(sum(changed)-changed[j])
    t=(1-q)*Jed/2+q*kap
    ck(t<=Jed/2);owner+=t/2
 ck(Tpriv==2*owner)
 leaves=[[value((t<<2)|b) for t in range(1<<(a*m))] for b in range(4)]
 HR=H(v);Havg=ns['add'](*[(Q(1,4),H(leaf)) for leaf in leaves])
 R=[sum(Q(w[(t<<2)|b]**2,L*L) for b in range(4)) for t in range(1<<(a*m))]
 ck(all(x>0 for x in R));ck(sum(R)==1)
 B=ns['add']((1,HR),(-1,ns['ent'](R)))
 CE=ns['add']((a*m,{2:1}),(1,B))
 ck(ns['grid'](B)[0]>=0 or B=={})
 ck(ns['grid'](ns['add']((2,{2:1}),(-1,B)))[0]>=0)
 ck(ns['grid'](ns['add']((3*I,{2:1}),(-1,CE)))[0]>=0)
 ck(ns['grid']({2:4*I-a*m-T},constant=-3*d)[0]>=0)
 ck(ns['grid'](ns['add']((1,HR),(-1,Havg),(-1,B)))[0]>=0)
 ck(ns['grid'](ns['add']((a*m+T,{2:1}),(-1,CE)),constant=3*d)[0]>=0)
 normalization=sum(Q(1,1<<(a*m))*sum(Q(w[(t<<2)|b]**2,L*L)/R[t] for b in range(4)) for t in range(1<<(a*m)))
 ck(normalization==1)
 rows.append({'m':m,'masks':masks,'I':str(I),'J':str(J),'d':str(d),'E_zw':str(E),'T':str(T),'T_private':str(Tpriv),'reference_normalization':'1','status':'PASS'})
 (ROOT/'out/REVIEW_PARTIAL.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf8')
out={'status':'PASS','cases':rows,'checks':checks,'elapsed_seconds':time.perf_counter()-start,'independence':'Own recursive Walsh and actual edges, no A016 implementation imported; prior A018 rational log definitions only'}
(ROOT/'out'/('REVIEW_PILOT.json' if '--pilot' in sys.argv else 'TWO_PIVOT_REVIEW.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:out[k] for k in ('status','checks','elapsed_seconds')}))
