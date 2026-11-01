"""Independent source-level reconstruction, exact upper-set/GU certificate."""
from pathlib import Path
import json,time,sys
from functools import lru_cache
from fractions import Fraction as F
R=Path(__file__).resolve().parents[1]; HOME=R.parents[1]
old=HOME/'runs/20261023T113614Z-fleet03-A061-entropy-process/code'
for src,dst in [('arith.py','arith.py'),('independent_oracle.py','oracle.py')]:
 (R/'code'/dst).write_bytes((old/src).read_bytes())
import arith as A
import oracle as D
N=0; COUNTS={}; WITNESS=None
def ck(b,s):
 global N
 N+=1
 if not b:raise AssertionError(s)
def add(*x):return A.plus(*x)
def nn(x,s):ck(not x or A.interval(x)[0]>=0,s)
def sector(g,h):return tuple((g[x>>2] if not (x>>1&1) else h[x>>2]*(-1 if x&1 else 1)) for x in range(4*len(g)))
def ref(w,rs):return tuple(w[x&1]*rs[x&1][x>>2]/2 for x in range(4*len(rs[0])))
def walk(g,h,w,rs,t,Q):
 global WITNESS
 COUNTS['pivot_states']+=1
 ck(t==sector(g,h) and Q==ref(w,rs),'FULL sector representation including zero-source atoms')
 p0,p1=D.stats(g)[0],D.stats(h)[0]
 p,ds,H,M,TC=D.stats(t)
 ck(p==tuple([p0[x>>2]/4 if not(x&1) else p1[x>>2]/4 for x in range(len(t))]),'actual direct spectrum sector identity')
 masses=[sum((rs[b][s] for s,a in enumerate([p0,p1][b]) if a),F()) for b in [0,1]]
 pred=[F(1,2)+(w[0]*masses[0]-w[1]*masses[1])/2];pred.append(1-pred[0])
 cs,qs,r,E,O,ks=D.transport(t,Q,1)
 ck(r==pred and not E,'actual protected-pivot prediction and ZERO erasure')
 debit=[]; losses=[]
 for b,core in enumerate([g,h]):
  Db=D.kl([p0,p1][b],rs[b]);Tb=D.stats(core)[4];L=add((1,Db),(-1,Tb));losses.append(L)
  ck(ks[b]==add((1,Db),(1,A.log(r[b]/w[b]))),'actual child KL with ALL reference-only mass')
  ck(D.stats(cs[b])[2]==D.stats(core)[2] and D.stats(cs[b])[4]==Tb,'FULL child H and TC')
  J=add((1,A.log(w[b]/r[b])),(-1,L));ck(J==add((1,Tb),(-1,ks[b])),'exact signed debit')
  debit.append(A.positive(J));COUNTS['reset_children']+=1
  ck(D.kl(D.stats(cs[b])[0],D.product(D.stats(cs[b])[1]))==Tb,'actual normalized product reset')
  if L and A.interval(L)[1]<0 and WITNESS is None:WITNESS={'g':list(g),'h':list(h),'w':list(map(str,w)),'L':A.value(L),'J':A.value(J),'remaining_core_bits':len(g).bit_length()-1}
 B=add((F(1,2),debit[0]),(F(1,2),debit[1]))
 bound=add((1,A.const(F(1,2))),(F(1,2),A.positive(add((-1,losses[0])))),(F(1,2),A.positive(add((-1,losses[1])))))
 nn(add((1,bound),(-1,B)),'sharp eligibility bound')
 K=D.kl(p,Q);ck(not add((1,K),(-1,O),(F(-1,2),ks[0]),(F(-1,2),ks[1])),'pivot KL boundary')
 G=B
 for j in range(len(g).bit_length()-1):
  tg,rg,pg,eg,og,kg=D.transport(g,rs[0],j);th,rh,ph,eh,oh,kh=D.transport(h,rs[1],j)
  ts,Qs,rr,ee,oo,kk=D.transport(t,Q,j+2);COUNTS['ordinary_queries']+=1;childG=[]
  for b in [0,1]:
   rb=w[0]*pg[b]+w[1]*ph[b];ck(rr[b]==rb,'actual mixture prediction')
   wb=(w[0]*pg[b]/rb,w[1]*ph[b]/rb)
   childG.append(walk(tg[b],th[b],wb,(rg[b],rh[b]),ts[b],Qs[b]))
  candidate=add((F(1,2),childG[0]),(F(1,2),childG[1]),(-1,ee));G=A.maximum(G,candidate)
  nn(add((1,K),(1,G),(-1,oo),(F(1,2),add((-1,kk[0]),(-1,childG[0]))),(F(1,2),add((-1,kk[1]),(-1,childG[1])))),'every ordinary drift pays actual O')
 return G
def arms(g,h):
 p0,d0,*_=D.stats(g);p1,d1,*_=D.stats(h);size=len(g)
 common=D.product(tuple((a+b)/2 for a,b in zip(d0,d1)))
 yield (F(1,2),F(1,2)),(common,common),'actual_original_product'
 denom=size*(size+1)//2
 yield (F(1,3),F(2,3)),(tuple(F(s+1,denom) for s in range(size)),tuple(F(size-s,denom) for s in range(size))),'nonproduct_unequal_sectors'
 yield (F(2,5),F(3,5)),(tuple((3*p+F(1,size))/4 for p in p0),tuple((p+F(2,size))/3 for p in p1)),'source_mixed_correlated'
 yield (F(3,4),F(1,4)),(D.product((F(1,3),)*(size.bit_length()-1)),D.product((F(2,3),)*(size.bit_length()-1))),'different_products'
def pairs(pilot):
 for n in ([0,1] if pilot else [0,1,2]):
  tables=[tuple(-1 if code>>(x-1)&1 else 1 for x in range(1,1<<n)) for code in range(1<<((1<<n)-1))]
  tables=[(1,)+t for t in tables]
  if n==2 and '--full-original-domain' not in sys.argv:
   constant=(1,)*4;point=(1,-1,-1,-1);parity=(1,-1,-1,1);bent=(1,1,1,-1)
   for g,h in [(point,point),(point,constant),(point,parity),(bent,parity)]:yield g,h
  else:
   for g in tables:
    for h in tables:yield g,h
 if not pilot:
  point=(1,)+(-1,)*7 # sign-normalized point; same squared spectrum as negative-at0.
  maj=tuple(1 if x.bit_count()<=1 else -1 for x in range(8))
  star=tuple(-1 if (x&1)*(((x>>1)&1)^((x>>2)&1)) else 1 for x in range(8))
  for g,h in [(point,point),(point,(1,)*8),(point,maj),(star,maj)]:yield g,h
@lru_cache(None)
def upper(t):
 p=D.stats(t)[0];n=len(t).bit_length()-1
 pi=[sum((p[z] for z in range(len(p)) if z&s==s),F()) for s in range(len(p))]
 return add(*[(p[s],A.log(pi[s]/p[s])) for s in range(len(p)) if p[s]])
def point_check(maxm):
 out=[]
 for m in range(1,maxm+1):
  t=(-1,)+(1,)*((1<<m)-1);d=F(1,1<<(m-1));U=upper(t);I=sum(D.stats(t)[1])
  formula=add((-2*(1-d)**2,A.log(1-d))) if d<1 else {}
  formula=add((1,formula),(1,A.const(m*d-m*d*d)))
  ck(U==formula and I==m*d,'actual upper-set U and influence formula including vacuum')
  G={}
  for j in range(m):G=add((1,G),(1,U),(F(-1,2),upper(D.child(t,j,0))),(F(-1,2),upper(D.child(t,j,1))))
  nn(add((1,A.const(F(19,8)*I)),(-1,G)),'actual GU residual19/8 all physical directions')
  out.append({'m':m,'I':str(I),'U':A.value(U),'G':A.value(G)})
 return out
def run(pilot):
 global COUNTS,N,WITNESS
 COUNTS={'pairs':0,'reference_entries':0,'pivot_states':0,'reset_children':0,'ordinary_queries':0};N=0;WITNESS=None
 beforeD,beforeA=D.N,A.COUNT;start=time.perf_counter()
 for g,h in pairs(pilot):
  COUNTS['pairs']+=1
  for w,rs,label in arms(g,h):
   COUNTS['reference_entries']+=1
   for b in [0,1]:ck(sum(rs[b])==1,'sector reference normalized')
   walk(g,h,w,rs,sector(g,h),ref(w,rs))
 points=point_check(3 if pilot else 8)
 ck(COUNTS['pivot_states']==(52 if pilot else 4644 if '--full-original-domain' in sys.argv else 1524),'exact frozen ordered-prefix coverage')
 if not pilot:ck(WITNESS is not None,'negative eligibility term actually exercised')
 elapsed=time.perf_counter()-start;ck(elapsed<(55 if pilot else 120),'frozen compute runtime')
 out={'status':'PASS','stage':'pilot' if pilot else 'main','counts':COUNTS,'author_predicates':N,'independent_transport_predicates':D.N-beforeD,'auxiliary_scalar_predicates':A.COUNT-beforeA,'seconds':elapsed,'negative_eligibility_witness':WITNESS,'point_GU':points,'all_m_bridge':'PROOF.md sections1--3 analytic; no finite extrapolation'}
 (R/'out'/('PILOT.json' if pilot else 'MAIN.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
 print(json.dumps({k:out[k] for k in ['status','stage','counts','author_predicates','independent_transport_predicates','auxiliary_scalar_predicates','seconds']}),flush=True)
 return elapsed
if __name__=='__main__':
 run(True)
 if '--pilot-only' not in sys.argv:run(False)
