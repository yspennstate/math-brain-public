from pathlib import Path
from fractions import Fraction as F
from itertools import product
from functools import lru_cache
import json,time,sys
import prior as p
R=Path(__file__).resolve().parents[1]; start=time.perf_counter(); counts={}
pilot='--pilot' in sys.argv
def ck(v,k):
 assert v,k
 counts[k]=counts.get(k,0)+1
def cv(x):return {2:F(x)} if x else {}
def ge(v):
 if not v:return True
 return p.interval(v)[0]>=0
def L(x,y):return p.add(p.ent([x*x,y*y]),p.mul(p.ent([(x+y)**2,(x-y)**2]),-F(1,2)))
def tables(n):return [tuple(1 if m>>x&1 else -1 for x in range(1<<n)) for m in range(1<<(1<<n))]
def coeff(t):
 N=len(t)
 return tuple(F(sum(t[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(N)),N) for s in range(N))
def row(h,gs,j,i):
 full=p.compose(h,gs);q=p.qs(h,gs);g=gs[j];w=p.data(g)[0];mu=w[0];t=w[1<<i]
 other=gs[1-j];av=[];dv=[]
 for zval in other:
  z=(1 if zval==1 else 0)<<(1-j)
  hm,hp=h[z],h[z|(1<<j)]
  av.append(F(hp+hm,2));dv.append(F(hp-hm,2))
 aa,dd=coeff(tuple(av)),coeff(tuple(dv));ck(sum(x*x for x in dd)==q[j],'Parseval_D')
 special=p.add(*(L(a+mu*d,t*d) for a,d in zip(aa,dd)))
 child=[]
 for b in [0,1]:
  gg=list(gs);gg[j]=p.restrict(g,i,b);child.append(p.correction(h,gg))
 drift=p.add(p.mul(p.add(*child),F(1,2)),p.mul(p.correction(h,gs),-1))
 ck(drift==p.add(p.mul(L(mu,t),q[j]),p.mul(special,-1)),'exact_whole_row')
 ck(ge(special),'special_nonnegative')
 D=p.data(full)[3][i if j==0 else 2+i]
 ck(D==q[j]*p.data(g)[3][i],'physical_factor')
 # ln(2)*L <=2d; p.interval is outward scaled bits.
 lv=L(mu,t);hi=p.interval(lv)[1]
 ck(not lv or hi*p.LN2[1]<=2*p.data(g)[3][i]*p.Q*p.Q,'natural_row_bound')
 ck(ge(p.add(cv(3*D),p.mul(drift,-1))),'rational3_drift')
 ck(time.perf_counter()-start<55,'runtime_guard')

rates=[F(0),F(1),F(2),F(3),F(10)]
@lru_cache(None)
def rho(t,K):
 H=p.data(t)[1];I=p.data(t)[2];pay=p.add(H,cv(-K*I));v=pay if ge(pay) else {}
 for i in range(len(t).bit_length()-1):
  z=p.mul(p.add(*(rho(p.restrict(t,i,b),K) for b in [0,1])),F(1,2))
  if ge(p.add(z,p.mul(v,-1))):v=z
 return v
for n in range(3 if pilot else 4):
 for f in tables(n):
  H=p.data(f)[1];I=p.data(f)[2]
  for K in rates:
   rr=rho(f,K);ck(ge(rr),'rho_nonnegative');ck(ge(p.add(H,p.mul(rr,-1))),'rho_at_most_H')
   ck(ge(p.add(rr,p.mul(H,-1),cv(K*I))),'rho_payoff')
   for i in range(n):
    kids=[p.restrict(f,i,b) for b in [0,1]];target=[rho(g,K) for g in kids]
    # Incoming minimal stopping credit rr; supply a child floor plus constant residual.
    avg=p.mul(p.add(*target),F(1,2));res=p.add(rr,p.mul(avg,-1));ck(ge(res),'credit_feasibility')
    credits=[p.add(z,res) for z in target]
    S=p.add(cv(K*I),p.mul(H,-1));dp=p.add(S,rr)
    ds=[p.add(cv(K*p.data(g)[2]),p.mul(p.data(g)[1],-1),a) for g,a in zip(kids,credits)]
    ck(all(ge(d) for d in ds),'corrected_child_debits_nonnegative')
    e=p.add(*(p.mul(p.add(cv(K*p.data(g)[2]),p.mul(p.data(g)[1],-1)),F(1,2)) for g in kids),p.mul(S,-1))
    ck(p.mul(p.add(*ds),F(1,2))==p.add(dp,e),'signed_total_conservation')
for h,g1,g2 in product(tables(2)[:4] if pilot else tables(2),tables(2)[:4] if pilot else tables(2),tables(1)):
 for j,i in [(0,0),(0,1),(1,0)]:row(h,[g1,g2],j,i)
# Rational algebra checks: arbitrary signed old labels, negative e, zero totals.
for a0,a1,s0,s1 in product([F(-2),F(-1),F(0),F(1),F(2)],repeat=4):
 d0,d1=s0+a0,s1+a1
 if min(a0,a1,d0,d1)<0:continue
 T=(d0+d1)/2;old=F(7);new=T-old
 if T:
  ks=[d0/T,d1/T];ck(sum(ks)/2==1,'kernel_mean')
  ck(all(old*k+new*k==d for k,d in zip(ks,[d0,d1])),'signed_label_transport')
 else:ck(d0==d1==0 and old+new==0,'zero_total_signed_labels')
# Literal witness with nonnegative parent even under the false convention.
f=tuple(1 if not x&1 else (-1 if ((x>>1).bit_count()%2) else 1) for x in range(8))
ck(p.data(f)[1]==cv(2) and p.data(f)[2]==F(3,2),'gated_parity_spectrum')
ck(not rho(f,F(10)),'witness_hull_zero')
ks=[p.restrict(f,0,b) for b in [0,1]]
witness=[]
for kap in [F(9,2),F(3)]:
 U=[kap*p.data(g)[2] for g in ks];a=F(13);credit=[u+a-sum(U)/2 for u in U]
 wrong=[p.add(p.data(g)[1],cv(-10*p.data(g)[2]+c)) for g,c in zip(ks,credit)]
 right=[p.add(cv(10*p.data(g)[2]+c),p.mul(p.data(g)[1],-1)) for g,c in zip(ks,credit)]
 ck(all(not p.data(g)[1] for g in ks),'witness_rational_children')
 ck(ge(p.mul(wrong[1],-1)) and wrong[1]!= {},'wrong_sign_refuted')
 ck(all(ge(d) for d in right),'correct_sign_repaired')
 witness.append({'kappa':str(kap),'incoming':str(a),'credits':list(map(str,credit)),'wrong_debits':[str(v.get(2,0)) for v in wrong],'right_debits':[str(v.get(2,0)) for v in right]})
ck(2**74>3**9*5**25,'A075_primitive_countercontrol_integer')
result={'status':'PASS','pilot':pilot,'counts':counts,'total_checks':sum(counts.values()),'witness':witness,'runtime_seconds':time.perf_counter()-start,'proof_scope':'exact finite checks plus analytic all-dimensional reconstruction in PROOF.md; no full FEI claim'}
(R/'out'/('PILOT.json' if pilot else 'VALIDATION.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
