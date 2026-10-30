"""Independent carrier audit: direct characters/edges; no source helper imports."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import sys,time,json
sys.dont_write_bytecode=True
import arithmetic as iv
ROOT=Path(__file__).resolve().parents[1]
COUNT=0;QUERIES=0;NODES=0
def ck(x,label=''):
 global COUNT
 COUNT+=1
 if not x:raise AssertionError(label)
def lin(*terms):
 d={}
 for c,e in terms:
  for k,v in e.items():d[k]=d.get(k,F())+c*v
 return {k:v for k,v in d.items() if v}
def const(x):return {2:F(x)} if x else {}
@lru_cache(None)
def factor(n):
 d={};p=2
 while p*p<=n:
  while n%p==0:d[p]=d.get(p,0)+1;n//=p
  p=3 if p==2 else p+2
 if n>1:d[n]=d.get(n,0)+1
 return d
def log(x):
 x=F(x);ck(x>0,'log positive')
 return lin((1,{p:F(v) for p,v in factor(x.numerator).items()}),(-1,{p:F(v) for p,v in factor(x.denominator).items()}))
def box(e):return iv.add(*(iv.scale(iv.lg(p),v) for p,v in e.items()))
def eq(a,b,label):ck(not lin((1,a),(-1,b)),label)
def ge(e,label):ck(not e or box(e)[0]>=0,label)
def gt(e,label):ck(bool(e) and box(e)[0]>0,label)
def maximum(a,b):
 d=lin((1,a),(-1,b))
 if not d:return a
 lo,hi=box(d);ck(lo>0 or hi<0,'max exact sign resolved')
 return a if lo>0 else b
def pos(e):return maximum({},e)
def ent(p):return lin(*[(-x,log(x)) for x in p if x])
def kl(p,r):
 ck(len(p)==len(r) and sum(p)==sum(r)==1,'KL normalized')
 ck(all(not a or b>0 for a,b in zip(p,r)),'source support')
 return lin(*[(a,log(a/b)) for a,b in zip(p,r) if a])
def child(t,i,b):return tuple(v for x,v in enumerate(t) if (x>>i)&1==b)
@lru_cache(None)
def stats(t):
 n=len(t).bit_length()-1;w=iv.walsh(t)
 p=tuple(F(v*v,len(t)**2) for v in w);ck(sum(p)==1,'direct Parseval')
 ds=tuple(F(sum(v!=t[x^(1<<i)] for x,v in enumerate(t)),len(t)) for i in range(n))
 for i,d in enumerate(ds):ck(d==sum((v for s,v in enumerate(p) if (s>>i)&1),F()),'direct edges vs coefficients')
 H=ent(p);M=lin(*[(1,ent((d,1-d))) for d in ds]);TC=lin((1,M),(-1,H));ge(TC,'TC nonnegative')
 return p,ds,H,M,TC
def move(t,i,R):
 p,ds,H,M,TC=stats(t);cs=[child(t,i,b) for b in [0,1]];ps=[stats(c)[0] for c in cs]
 pairs=[(s,s|(1<<i)) for s in range(len(t)) if not (s>>i)&1]
 pe=[p[a]+p[b] for a,b in pairs];re=[R[a]+R[b] for a,b in pairs]
 U=[[],[]];z=F()
 for s,(a,b) in enumerate(zip(pe,re)):
  ks=[ps[v][s]/(2*a) if a else F(1,2) for v in [0,1]];ck(sum(ks)==1,'fair zero extension')
  if not a:z+=b
  for v in [0,1]:U[v].append(b*ks[v])
 reach=[sum(v) for v in U];ck(sum(reach)==1 and min(reach)>0,'positive reference prediction')
 rr=[tuple(x/reach[b] for x in U[b]) for b in [0,1]]
 K=kl(p,R);Kc=[kl(ps[b],rr[b]) for b in [0,1]]
 O=lin((F(-1,2),log(4*reach[0]*reach[1])));E=lin((1,K),(-1,kl(pe,re)))
 eq(K,lin((1,E),(1,O),(F(1,2),Kc[0]),(F(1,2),Kc[1])),'exact prime-log chain')
 ge(E,'erasure credit');ge(O,'outcome cost')
 for j,d in enumerate(ds):
  if j!=i:ck(d==(stats(cs[0])[1][j-(j>i)]+stats(cs[1])[1][j-(j>i)])/2,'physical influence conservation')
 ge(lin((1,M),(F(-1,2),stats(cs[0])[3]),(F(-1,2),stats(cs[1])[3])),'same marginal envelope decreases in mean')
 return cs,rr,reach,O,E,Kc,z
def book(t,R,depth):
 global QUERIES,NODES
 NODES+=1;p,ds,H,M,TC=stats(t);K=kl(p,R)
 Bs=[pos(lin((1,TC),(-1,K))) for _ in range(depth+1)]
 for i in range(len(ds)) if depth else []:
  QUERIES+=1;c,r,pr,O,E,Kc,z=move(t,i,R)
  bs=[book(c[b],r[b],depth-1) for b in [0,1]]
  for d in range(1,depth+1):Bs[d]=maximum(Bs[d],lin((F(1,2),bs[0][d-1]),(F(1,2),bs[1][d-1]),(-1,E)))
 for d,B in enumerate(Bs):
  ge(lin((1,M),(-1,B)),'B bounded by inherited M')
  ge(lin((1,K),(1,B),(-1,TC)),'terminal retained')
  if d:ge(lin((1,B),(-1,Bs[d-1])),'nested bookings')
 return Bs
def lift(R,L):return tuple(R[(s>>2)^(L if s&1 else 0)]/4 for s in range(4*len(R)))
def carrier(g,L,c=0):
 return tuple(g[z>>2]*(-1 if (((z&1)^((z>>1)&1)^((L&(z>>2)).bit_count()%2)^c)&((z>>1)&1)) else 1) for z in range(4*len(g)))
def checkhist(g,R,L,c,depth):
 t=carrier(g,L,c);Q=lift(R,L);ck(stats(t)[0]==lift(stats(g)[0],L),'actual carrier spectral law')
 eq(kl(stats(t)[0],Q),kl(stats(g)[0],R),'lift KL')
 v=move(t,1,Q);ck(v[2]==[F(1,2),F(1,2)],'fair carrier including reference-only pairs');eq(v[3],{},'carrier O zero')
 for term in v[0]:
  eq(stats(term)[2],stats(g)[2],'both terminal H');eq(stats(term)[4],stats(g)[4],'both terminal TC')
 if depth:
  for i in range(len(g).bit_length()-1):
   a=move(g,i,R);b=move(t,i+2,Q)
   ck(a[2]==b[2],'predictions commute');eq(a[3],b[3],'outcome cost commutes');eq(a[4],b[4],'erasure commutes')
   nL=(L&((1<<i)-1))|((L>>(i+1))<<i)
   for v in [0,1]:
    ck(b[1][v]==lift(a[1][v],nL),'normalized reference lift commutes')
    ck(b[0][v]==carrier(a[0][v],nL,c^(v*((L>>i)&1))),'physical affine phase update')
    checkhist(a[0][v],a[1][v],nL,c^(v*((L>>i)&1)),depth-1)
def generic(pilot):
 cases=0
 for mask in ([0,7] if pilot else range(16)):
  g=tuple(1 if (mask>>i)&1 else -1 for i in range(4))
  refs=[tuple([F(1,4)]*4),tuple(F(x,11) for x in [1,2,3,5])]
  if not pilot:refs.append(stats(g)[0])
  for R in refs:
   book(g,R,2)
   for L in ([3] if pilot else range(4)):
    for c in ([0] if pilot else [0,1]):checkhist(g,R,L,c,2);cases+=1
 return {'fixtures':cases,'arbitrary_references':['uniform','nonmatching(1,2,3,5)/11']+([] if pilot else ['actual spectrum']),'histories_per_fixture':13,'reference_only_rows':'included'}
def mult(a,b,l):
 ans=0;poly={1:3,2:7,3:11}[l]
 while b:
  if b&1:ans^=a
  b>>=1;a<<=1
  if a>>l:a^=poly
 return ans
def core(l):
 q=1<<l
 return tuple((-1 if z&1 else 1)*(-1 if (z>>(2*l))==mult(z&(q-1),(z>>l)&(q-1),l) else 1) for z in range(q**3))
def references(h):
 p=stats(h)[0];N=len(h)
 wh=tuple(F(0) if s==0 else F(1) if p[s] else F(1,2) for s in range(N));wg=tuple(1-v for v in wh)
 rh=sum(wh)/N;rg=sum(wg)/N
 return tuple(v/(N*rh) for v in wh),tuple(v/(N*rg) for v in wg),rg
def field(pilot):
 rows=[]
 for l in ([2] if pilot else [2,3]):
  h=core(l);p,ds,H,M,TC=stats(h);R,RG,rg=references(h);q=1<<l;m=3*l
  ck(p[0]==0 and rg==F(1,2*q),'field original root predictions')
  a=F(2,q)-F(2,q*q);b=F(2,q)
  for j,d in enumerate(ds):ck(d==(1-a if j==0 else a if j<2*l else b),'all physical field marginals')
  eq(M,lin((2*l,ent((a,1-a))),(l,ent((b,1-b)))),'field M formula')
  S=lin((1,const(2*m+2)),(F(-1,2),H));cap=F(3) if l==2 else F(39*l,32)
  B=book(h,R,1 if pilot else 2);W=[lin((F(1,2),v)) for v in B]
  ge(lin((1,const(cap)),(F(-1,2),M)),'all-history rational cap')
  gt(lin((F(13,48),S),(-1,const(cap))),'strict original owner13/48')
  gt(lin((F(3,4),S),(-1,const(cap)),(F(-23,48),S)),'old quarter retained')
  if not pilot:
   expected=lin((1,const(F(47,32))),(F(-3,8),log(7))) if l==2 else {}
   eq(W[2],expected,'exact optional-stop depth-two booking')
   gt(lin((F(1,25),S),(-1,W[2])),'depthtwo original owner bound')
   gt(lin((F(1,50),S),(-1,W[2]),(1,W[1])),'second topup bound')
  rows.append({'l':l,'M':M,'Sbar':S,'W':W,'cap':cap})
 ck(3**12>2**19 and 288<299,'all-width integer guard')
 # The excluded l1 family is not incorrectly admitted by the q>=4 support formula.
 ck(references(core(1))[2]==F(5,16),'excluded l1 exact boundary')
 return {'rows':rows,'queries':QUERIES,'nodes':NODES}
def physical(pilot):
 h=core(2);G=carrier((1,)*64,63);H=carrier(h,63)
 t=tuple((H if z&1 else G)[z>>1] for z in range(512));Q=tuple([F(1,512)]*512)
 c,R,pr,O,E,Kc,z=move(t,0,Q);ck(c==[G,H] and pr==[F(1,8),F(7,8)],'full physical selector')
 RH,RG,rg=references(h);ck(R==[lift(RG,63),lift(RH,63)],'full actual inherited references')
 eq(E,{},'root erasure zero')
 S=lin((1,const(4*sum(stats(G)[1]))),(F(-1,2),stats(G)[2]),(F(-1,2),stats(H)[2]));eq(S,const(F(23,2)),'actual original S')
 old=pos(lin((1,stats(h)[4]),(-1,Kc[1])))
 dat=move(H,2,R[1]);co=move(h,0,RH)
 ck(dat[1]==[lift(v,31) for v in co[1]],'first ordinary reference commutes')
 eq(dat[4],{},'actual first-data erasure credit zero')
 bs=[];terminalH=[];terminalTC=[];carrierrefs=[]
 for b in [0,1]:
  car=move(dat[0][b],1,dat[1][b]);ck(car[2]==[F(1,2)]*2,'actual interposed carrier fair')
  eq(car[3],{},'actual carrier O0');carrierrefs.append(car[6])
  for term in car[0]:terminalH.append(stats(term)[2]);terminalTC.append(stats(term)[4])
  bs.append(pos(lin((1,stats(car[0][0])[4]),(-1,dat[5][b]))))
 new=pos(lin((F(1,2),bs[0]),(F(1,2),bs[1]),(-1,dat[4])))
 delta=lin((1,new),(-1,old));formula=lin((1,const(F(-9,2))),(F(3,8),log(3)),(F(15,8),log(5)))
 eq(delta,formula,'independent exact booking increase')
 gt(lin((1,delta),(-1,const(F(11,25)))),'positive interposed-query shortfall')
 Kroot=kl(stats(t)[0],Q)
 debt=lin((F(1,2),Kc[0]),*[(F(1,8),e) for e in terminalTC],(1,O),(F(1,2),dat[3]),(-1,Kroot),(F(-1,2),old))
 eq(debt,lin((F(1,2),delta)),'full asymmetric stopped cut with G KL retained')
 HH=lin((F(1,2),stats(G)[2]),*[(F(1,8),e) for e in terminalH]);eq(HH,const(F(11,4)),'full stopped terminal entropy')
 gt(lin((F(1,50),S),(F(-1,2),new)),'one total new booking below S/50')
 support=sum(1 for x in stats(t)[0] if x)/F(512)
 ck(support==F(25,32),'other-module reference mass on source support')
 product_prediction=support*pr[0]+(1-support)*F(1,2)
 ck(product_prediction==F(53,256) and product_prediction!=pr[0],'global fair-extension transport does not tensorize')
 second=[]
 if not pilot:
  for b in [0,1]:
   full=move(dat[0][b],5,dat[1][b]);cc=move(co[0][b],3,co[1][b])
   ck(full[1]==[lift(v,15) for v in cc[1]],'second proper data reference lift')
   for d in [0,1]:
    car=move(full[0][d],1,full[1][d]);ck(car[2]==[F(1,2)]*2,'second-query carrier pairing')
    for term in car[0]:
     eq(stats(term)[2],stats(cc[0][d])[2],'both second-query full H');eq(stats(term)[4],stats(cc[0][d])[4],'both second-query full TC')
    second.append({'history':[b,d],'H':stats(cc[0][d])[2],'TC':stats(cc[0][d])[4],'K':full[5][d],'reference_only':car[6]})
 return {'Sbar':S,'old_H_booking':old,'new_H_booking':new,'delta':delta,'stopped_debt':debt,'terminal_H':HH,'carrier_reference_only':carrierrefs,'two_module_prediction':product_prediction,'second_data_terminals':second}
def serial(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {str(k):serial(v) for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [serial(v) for v in x]
 return x
if __name__=='__main__':
 start=time.perf_counter();mode=sys.argv[1];pilot='--pilot' in sys.argv
 try:
  out={'generic':generic,'field':field,'physical':physical}[mode](pilot)
  ck(time.perf_counter()-start<55,'frozen runtime cap')
  out.update(status='PASS',assertions=COUNT,interval_helper_assertions=iv.NTEST,seconds=time.perf_counter()-start,helper='a087-carrier-referee-v1')
  path=ROOT/'out'/(mode.upper()+('_PILOT' if pilot else '')+'.json');path.write_text(json.dumps(serial(out),indent=2)+'\n',encoding='utf-8',newline='\n')
  print(json.dumps({k:v for k,v in serial(out).items() if k in ['status','assertions','seconds','fixtures','queries','nodes','helper']}))
 except Exception as e:
  (ROOT/'out'/(mode.upper()+'_FAILURE.json')).write_text(json.dumps({'status':'FAILED','exception':repr(e),'assertions':COUNT,'seconds':time.perf_counter()-start},indent=2),encoding='utf-8',newline='\n')
  raise
