from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import json,sys,time

run=Path(__file__).resolve().parents[1]
start=time.perf_counter(); checks=0
pilot='--pilot' in sys.argv
def ck(v):
 global checks
 checks+=1
 assert v,checks
def table(n,k):return [2*((k>>x)&1)-1 for x in range(1<<n)]
def subsets(s):
 t=s
 while True:
  yield t
  if not t:break
  t=(t-1)&s
def vp(p,s):
 v=F(1)
 for i,q in enumerate(p):
  if s>>i&1:v*=4*q*(1-q)
 return v
def data(tab,p):
 n=len(p); active=sum(1<<i for i,q in enumerate(p) if 0<q<1)
 poly=list(map(F,tab))
 for i in range(n):
  for s in range(1<<n):
   if s>>i&1:poly[s]-=poly[s^(1<<i)]
 c={}
 for s in subsets(active):
  z=F(0)
  for a in range(1<<n):
   if a&s!=s:continue
   v=poly[a]
   for i,q in enumerate(p):
    if (a^s)>>i&1:v*=q
   z+=v
  c[s]=z/F(2**s.bit_count())
 P={s:vp(p,s)*v*v for s,v in c.items()};ck(sum(P.values())==1)
 # Independent centered-moment reconstruction, without polynomial coefficients.
 for s in c:
  z=F(0)
  for x,f in enumerate(tab):
   v=F(f)
   for i,q in enumerate(p):
    v*=q if x>>i&1 else 1-q
    if s>>i&1:v*=(F((x>>i)&1)-q)/(2*q*(1-q))
   z+=v
  ck(z==c[s])
 j={};W={}
 for s,z in c.items():
  if not s or not z:continue
  ck(abs(z)<=1); u=abs(z);jj=0
  while u<=F(1,2):u*=2;jj+=1
  j[s]=jj;W[s]=vp(p,s)/F(4**jj)
 V=1-P[0];Z=sum(W.values(),F(0));Q={s:F(0) for s in P};Q[0]=P[0]
 if V:
  for s in W:Q[s]=V*W[s]/Z
 ck(sum(Q.values())==1)
 I=sum(s.bit_count()*v for s,v in P.items())
 return dict(p=p,c=c,P=P,j=j,W=W,V=V,Z=Z,Q=Q,I=I,D=I-V,J=sum(P[s]*v for s,v in j.items()))

@lru_cache(None)
def factors(n):
 d={};p=2
 while p*p<=n:
  while n%p==0:d[p]=d.get(p,0)+1;n//=p
  p=3 if p==2 else p+2
 if n>1:d[n]=d.get(n,0)+1
 return tuple(d.items())
def logs(terms):
 d={}
 for w,q in terms:
  q=F(q)
  if not w:continue
  assert q>0
  for sign,n in [(1,q.numerator),(-1,q.denominator)]:
   for p,k in factors(n):d[p]=d.get(p,F(0))+sign*w*k
 return {p:v for p,v in d.items() if v}
def plus(a,b):
 d=a.copy()
 for p,v in b.items():d[p]=d.get(p,F(0))+v
 return {p:v for p,v in d.items() if v}
def times(w,a):return {p:w*v for p,v in a.items() if w*v}
def kl(d,q=None):
 q=d['Q'] if q is None else q
 return logs((z,z/q[s]) for s,z in d['P'].items() if z)
def ent(d):return logs((z,1/d['c'][s]**2) for s,z in d['P'].items() if s and z)
def bern(s,t):return logs([(s,s/t),(1-s,(1-s)/(1-t))])

# The prefix is A045's own stage9 arithmetic, not any source checker's code.
rawdata=data
@lru_cache(None)
def dcache(tab,p):
 d=rawdata(tab,p);P=d['P'];c=d['c'];j=d['j']
 d['R']=sum((s.bit_count()-2)*v for s,v in P.items() if s.bit_count()>=3)
 d['M']=sum(v for s,v in P.items() if s.bit_count()>=2)
 d['J1']=sum(P[s]*v for s,v in j.items() if s.bit_count()==1)
 d['Jh']=sum(P[s]*v for s,v in j.items() if s.bit_count()>=2)
 d['E1']=logs((v,1/c[s]**2) for s,v in P.items() if v and s.bit_count()==1)
 d['L1']=logs((P[s],1/(F(4**jj)*c[s]**2)) for s,jj in j.items() if s.bit_count()==1)
 d['Lh']=logs((P[s],1/(F(4**jj)*c[s]**2)) for s,jj in j.items() if s.bit_count()>=2)
 d['Zh']=sum(v for s,v in d['W'].items() if s.bit_count()>=2)
 d['Q']={s:v if s.bit_count()<=1 else d['M']*d['W'].get(s,0)/d['Zh'] if d['Zh'] else F(0) for s,v in P.items()}
 d['nh']=logs([(d['M'],d['Zh']/d['M'])]) if d['M'] else {}
 d['SJ']=2*d['D']-d['R']-d['J1']
 ck(d['SJ']>=0);ck(d['M']==d['D']-d['R']);ck(sum(d['Q'].values())==1)
 for i,q in enumerate(p):
  s=1<<i
  if s not in j:continue
  inf=sum(v for a,v in P.items() if a&s)
  ck(P[s]*j[s]<=inf-P[s])
 ck(kl(d)==plus(d['nh'],times(-1,d['Lh'])))
 return d
def D(tab,p):return dcache(tuple(tab),tuple(map(F,p)))
def rat(v):return {0:F(v)} if v else {}
def lg4(v):return logs([(v,F(4))])
def lsum(items):
 z={}
 for v in items:z=plus(z,v)
 return z
def zero_node(tab,p):
 d=D(tab,p)
 return {'tab':list(tab),'p':tuple(p),'d':d,'Qtree':d['Q'],'T':F(0),'V':{},'C1':F(0),'Ch':F(0),'Rtree':F(0),'SJtree':F(0),'Stree':{},'E1src':{},'J1src':F(0),'L1src':{},'Jhsrc':F(0),'Lhsrc':{},'nsrc':{},'Ktree':{}}
def literal(p):return zero_node([-1,1],(p,))

singleton_carry_witness=None
def node(mask,children):
 global singleton_carry_witness
 ps=tuple(q for ch in children for q in ch['p']);sizes=[len(ch['p']) for ch in children]
 offsets=[];n=0
 for s in sizes:offsets.append(n);n+=s
 tab=[];gate=table(len(children),mask)
 for x in range(1<<n):
  a=0
  for i,ch in enumerate(children):
   y=(x>>offsets[i])&((1<<sizes[i])-1)
   a|=int(ch['tab'][y]==1)<<i
  tab.append(gate[a])
 d=D(tab,ps);pg=tuple((1+ch['d']['c'][0])/2 for ch in children);g=D(gate,pg)
 weights=[];bs=[];tout=F(0);tin=F(0);vv={};c1=F(0);chi=F(0);Q={}
 for i,ch in enumerate(children):
  cd=ch['d'];w=cd['V'];sg=g['P'].get(1<<i,F(0));inf=sum(v for a,v in g['P'].items() if a>>i&1)
  aa=inf/w if w else F(0);bb=(inf-sg)/w if w else F(0);weights.append(aa);bs.append(bb)
  tout+=(sg/w)*cd['M']*g['j'].get(1<<i,0) if w else 0
  tin+=bb*cd['J1'];vv=plus(vv,times(bb,cd['L1']))
  if sg and cd['M']:
   u2=F(4**g['j'][1<<i])*g['c'][1<<i]**2
   vv=plus(vv,logs([(sg*cd['M']/w,1/u2)]))
 for s,pp in d['P'].items():
  ts=[(s>>o)&((1<<n0)-1) for o,n0 in zip(offsets,sizes)]
  a=sum(int(t!=0)<<i for i,t in enumerate(ts));pred=g['P'].get(a,F(0));q=g['Q'].get(a,F(0));coef=g['c'].get(a,F(0));js=g['j'].get(a,0)
  for ch,t in zip(children,ts):
   if not t:continue
   cd=ch['d']
   if not cd['V']:pred=q=coef=F(0);break
   pred*=cd['P'].get(t,F(0))/cd['V'];q*=ch['Qtree'].get(t,F(0))/cd['V'];coef*=cd['c'].get(t,F(0));js+=cd['j'].get(t,0)
  ck(pred==pp);ck(coef==d['c'][s]);Q[s]=q
  if s.bit_count()<=1:ck(q==pp)
  if not pp or not s:continue
  carry=d['j'][s]-js;ck(carry>=0)
  if s.bit_count()==1:c1+=pp*carry
  else:chi+=pp*carry
  if carry and s.bit_count()==1 and singleton_carry_witness is None:
   singleton_carry_witness={'outer_mask':mask,'physical_biases':list(map(str,ps)),'label':s,'mass':str(pp),'actual_j':d['j'][s],'summed_local_j':js,'carry':carry,'root_truth_table':tab}
 ck(sum(Q.values())==1)
 ck(d['D']==g['D']+sum(w*ch['d']['D'] for w,ch in zip(weights,children)))
 locT=tout+tin
 ck(d['Jh']==g['Jh']+sum(w*ch['d']['Jh'] for w,ch in zip(weights,children))+chi+locT)
 # One-boundary source theorem, rational after dividing by ln4.
 refund=g['R']+sum((aa-bb)*ch['d']['D']+aa*ch['d']['R'] for aa,bb,ch in zip(weights,bs,children))
 ck(locT<=d['D']-refund/2)
 ck(plus(lg4(locT),plus(vv,d['E1']))==plus(g['E1'],lsum(times(w,ch['d']['E1']) for w,ch in zip(weights,children))))
 z={'tab':tab,'p':ps,'d':d,'Qtree':Q}
 for key,local in [('T',locT),('C1',c1),('Ch',chi),('Rtree',g['R']),('SJtree',g['SJ']),('J1src',g['J1']),('Jhsrc',g['Jh'])]:z[key]=local+sum(w*ch[key] for w,ch in zip(weights,children))
 for key,local in [('V',vv),('Stree',plus(rat(4*g['D']-2*g['R']),times(-1,g['E1']))),('E1src',g['E1']),('L1src',g['L1']),('Lhsrc',g['Lh']),('nsrc',g['nh']),('Ktree',kl(g))]:z[key]=plus(local,lsum(times(w,ch[key]) for w,ch in zip(weights,children)))
 # All-depth original singleton entropy owner (A044).
 ck(lsum([lg4(z['T']),z['V'],d['E1'],z['Stree']])==rat(4*d['D']-2*z['Rtree']))
 ck(plus(lg4(z['Ch']),d['Lh'])==plus(z['Lhsrc'],z['V']))
 ck(d['Jh']==z['Jhsrc']+z['Ch']+z['T'])
 ck(kl(d,Q)==z['Ktree'])
 ck(plus(kl(d),times(-1,z['Ktree']))==lsum([lg4(z['Ch']),times(-1,z['V']),d['nh'],times(-1,z['nsrc'])]))
 # New sharp scale source and singleton-carry owner. No carry erased.
 ck(z['T']+d['J1']+z['SJtree']==2*d['D']-z['Rtree']+z['C1'])
 ck(lsum([lg4(z['C1']),d['L1'],z['V']])==z['L1src'])
 if z['C1']==0:ck(z['T']<=2*d['D']-z['Rtree']-d['J1'])
 return z

laws=[(F(1,2),)*4,(F(1,3),F(2,5),F(3,4),F(1,4))]
cases=list(product(range(16),[0,8,6,14],[0,8,6,14],laws))
if pilot:cases=cases[:8]+[(g,h,k,laws[1]) for g,h,k in [(8,8,8),(6,8,14),(14,14,6),(1,6,8)]]
for g,h,k,p in cases:
 left=node(h,[literal(p[0]),literal(p[1])]);right=node(k,[literal(p[2]),literal(p[3])]);node(g,[left,right])
chaincases=list(product(range(16),laws))
if pilot:chaincases=chaincases[:2]
for g,p in chaincases:
 base=node(8,[literal(p[0]),literal(p[1])]);mid=node(6,[base,literal(p[2])]);node(g,[mid,literal(p[3])])

# Structural tower moments; not a truth-table enumeration on 3^8 inputs.
towers=[]
for depth in range(1,9):
 inf=F(3,2)**depth;de=inf-1;j1=depth*F(3,4)**depth
 T=F(3,2)*de-j1;rt=de/2;sj=F(0)
 ck(T+j1+sj==2*de-rt);ck(T<=2*de-rt-j1)
 if depth==4:ck(T-de==F(49,64))
 towers.append({'depth':depth,'Delta':str(de),'J1_over_ln4':str(j1),'T_over_ln4':str(T),'singleton_carry':'0','Rtree':str(rt),'new_scale_residual_over_ln4':str(sj)})

# Sharp local scale source: fair AND2; all singleton mass is genuine.
fairand=D([-1,-1,-1,1],(F(1,2),F(1,2)));ck(fairand['SJ']==0);ck(fairand['J1']==2*fairand['D'])
# Same wire versus invented independent outputs; physical versus spectral restriction.
ck((2*F(1,3)-1)**2==F(1,9));ck((2*F(1,3)**2-1)**2==F(49,81))
ck(fairand['P'][0]/(fairand['P'][0]+fairand['P'][2])==F(1,2));ck(D([-1,-1],(F(1,2),))['P'][0]==1)
for p in [(F(0),F(1,3)),(F(1),F(1,3))]:
 z=node(8,[literal(p[0]),literal(p[1])]);ck(z['d']['D']==0)
ck(singleton_carry_witness is not None)
elapsed=time.perf_counter()-start
res={'status':'PASS','pilot':pilot,'two_child_cases':len(cases),'depth3_chain_cases':len(chaincases),'compressed_towers':8,'assertions':checks,'runtime_seconds':elapsed,'spectral_arithmetic':'Fraction Mobius independently checked against centered moments','logarithmic_equalities':'canonical rational prime-log vectors; no numeric log signs','sharp_local_scale_source':'fair AND2: J1=ln4*(2Delta-R)','first_singleton_carry_witness':singleton_carry_witness,'full_fei':'OPEN'}
(run/'out'/('PILOT.json' if pilot else 'CHECKS.json')).write_text(json.dumps(res,indent=2)+'\n',encoding='utf-8',newline='')
(run/'out'/('PILOT_TOWERS.json' if pilot else 'TOWERS.json')).write_text(json.dumps(towers,indent=2)+'\n',encoding='utf-8',newline='')
print(json.dumps(res));assert elapsed<(55 if pilot else 180)
