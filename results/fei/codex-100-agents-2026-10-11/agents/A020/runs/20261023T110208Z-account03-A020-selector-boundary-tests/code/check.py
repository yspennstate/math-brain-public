from pathlib import Path
from fractions import Fraction as Q
from itertools import product
from functools import lru_cache
import sys,importlib.util,json,time,argparse
sys.dont_write_bytecode=True
R=Path(__file__).resolve().parents[1]
hp=R.parents[1]/'runs/20261022T231605Z-account03-A020-selector-boundary-tests/code/check.py'
sp=importlib.util.spec_from_file_location('logs',hp);h=importlib.util.module_from_spec(sp);sp.loader.exec_module(h)
N=0
def ck(t):
 global N
 N+=1
 assert t
def show(v):return [str(h.floorq(v[0])),str(h.ceilq(v[1]))]
def overlap(v,w):ck(v[0]<=w[1] and w[0]<=v[1])
def term(mass,code):return h.scale(h.log2(1/code),mass) if mass else h.con(0)
def add(*args):
 v=h.con(0)
 for w in args:v=h.add(v,w)
 return v
H0=h.sub(h.con(4),h.scale(h.log2(3),Q(9,8)))
C2=add(h.scale(h.log2(Q(8,5)),Q(1,4)),h.con(Q(9,4)))
@lru_cache(None)
def debit(k,m):
 p=Q(1,1<<k)*(1-Q(3,4)**m)/2;b=p/2;t=(1+b)**2/(2*(1+b*b))
 E=h.scale(h.sub(h.con(1),add(h.eta(t),h.eta(1-t))),(1+b*b)/2)
 L=add(h.scale(h.log2((9+p*p)/8),Q(1,2)),h.scale(h.log2((9+p*p)/(1+p*p)),p*p/8))
 U=add(L,E);ck(U[0]>=0 and U[1]<Q(5,8))
 return U
@lru_cache(None)
def profile(k,m,n3,n2,n1,phase):
 rho=Q(1,1<<k);mu=Q(3,4)**m;p=rho*(1-mu)/2
 nu=phase*Q(3,4)**n3*Q(1,2)**n2 if n1==0 else Q(0)
 a=rho*(1-nu)/2;r0=Q(9,16)**n3*Q(5,8)**n2*Q(3,4)**n1
 I=Q(3*n3,4)+n2+n1;cg=add(h.scale(H0,n3),h.scale(C2,n2),h.con(2*n1))
 ck(r0>=nu*nu)
 ck(cg[1]<4*I if I else cg==h.con(0))
 # Exact full-code aggregation. Nonempty surviving-seed rows are coded jointly.
 nonempty=add(h.con((1-nu*nu)*(7+2*k)),cg,h.scale(h.log2(r0),nu*nu))
 CE_nonempty=h.scale(nonempty,rho/4)
 x=rho*rho*(r0+1-2*mu)/8
 qempty=x+Q(1,2);qu=x+(1-2*p)/2
 ck(x>=0 and qempty>0 and qu>0)
 CE=add(CE_nonempty,term((1-a)**2/2,qu/16),
        term((1-rho)*a*a/rho,x/16),
        term(3*a*a/8,qempty/16),
        term((1+a*a/4)/2,qempty/16+Q(1,4)))
 # Both q signs have identical CE but unequal physical influence.
 W=[]
 for sign in [1,-1]:
  fourI=6+2*(k-1)*a+rho*I-sign*a
  w=h.sub(h.sub(h.con(fourI),CE),debit(k,m));W.append(w)
  if k>=5 and m>=4:ck(w[0]>Q(5,8))
 # General-vacuum proof certificate, with all principal overlaps preserved.
 coeff=3*r0+3-8*mu+2*nu
 if m>=4 and nu<=Q(1,2):
  ck(coeff>=Q(13,96));ck((1-2*p)/2>=(1-2*a)/8)
 # Normalization is algebraic, without deleting ghost atoms.
 ck((1-2*a)+rho*(1+1-2*nu)/2==1)
 ck((1-2*p)/2+Q(1,2)+rho*(1+1-2*mu)/4==1)
 return {'k':k,'m':m,'n3':n3,'n2':n2,'n1':n1,'phase':phase,'nu':str(nu),'R_empty':str(r0),'vacuum_domination_slack':str(coeff),'CE_seed':show(cg),'CE_full':show(CE),'old_U':show(debit(k,m)),'both_signed_reserves':[show(v) for v in W]},CE

def original(k,m):
 act=[]
 for t in range(1<<(k+3*m)):
  g=1
  for j in range(m):g*=(-1 if ((t>>(k+3*j))&7)==0 else 1)
  act.append(int((t&((1<<k)-1))==0 and g==-1))
 core=[(-1 if t&1 else 1) if act[t>>2] else (-1 if (t>>1)&1 else 1) for t in range(4*len(act))]
 ph=h.law(core);qh=[(w+int(i==1))/2 for i,w in enumerate(ph)]
 return h.full(core),h.fullref(qh)
def literal(k,m):
 f,qf=original(k,m);q0=h.marginal(qf,1);ck(sum(qf)==1)
 cache={};queries=0;clean_hist=0
 for states in product([-1,0,1],repeat=3*m):
  fixed={};active=[];phase=1;n=[0,0,0,0];cleanup=0
  for j in range(m):
   block=states[3*j:3*j+3]
   if 1 in block:
    for i,v in enumerate(block):fixed[3*j+i]=v if v!=-1 else 0;cleanup+=int(v==-1)
   else:
    free=[i for i,v in enumerate(block) if v==-1]
    if not free:phase*=-1
    else:active.append(len(free));n[len(free)]+=1
    for i,v in enumerate(block):
     if v!=-1:fixed[3*j+i]=v
  # Values on cleaned constant blocks can differ; replace by canonical first1
  # for caching only after proving both restrictions are physically equal below.
  key=(tuple((j,states[3*j:3*j+3]) for j in range(m) if 1 not in states[3*j:3*j+3]),tuple(j for j in range(m) if 1 in states[3*j:3*j+3]))
  reach=Q(1,1<<sum(v!=-1 for v in states));ck(0<reach<=1)
  clean_hist+=1<<cleanup
  if key in cache:queries+=2;continue
  scalar,ce=profile(k,m,n[3],n[2],n[1],phase)
  mu=Q(3,4)**m;rho=Q(1,1<<k);p=rho*(1-mu)/2
  for qb in [0,1]:
   v=h.restrict(f,1,qb);qr=q0
   # First apply only the physical specified history, then independently check
   # equality of both outcomes at every cleanup query.
   specified={i:z for i,z in enumerate(states) if z!=-1}
   erased=[]
   for i,z in sorted(specified.items(),reverse=True):
    bit=k+2+i;v=h.restrict(v,bit,z);qr=h.marginal(qr,bit);erased.append(i)
   for i in sorted(set(fixed)-set(specified),reverse=True):
    bit=k+2+i-sum(j<i for j in erased)
    v0=h.restrict(v,bit,0);v1=h.restrict(v,bit,1);ck(v0==v1)
    v=v0;qr=h.marginal(qr,bit);erased.append(i)
   ck(sum(qr)==1)
   # Every atom of the complete original frequency marginal is checked.
   corebits=1+k+sum(active);coreN=1<<corebits
   for z,q in enumerate(qr):
    T=z>>1;core=T%coreN;mask=T//coreN;u=core&1;pad=(core>>1)&((1<<k)-1);seed=core>>(k+1)
    rem=seed;rr=Q(1)
    for ell in active:
     freq=rem&((1<<ell)-1);rem>>=ell
     rr*=Q(1,2)+Q(1,1<<(ell+1)) if freq==0 else Q(1,1<<(ell+1))
    qc=rho*rho*(rr+(1-2*mu if seed==0 else 0))/8
    if core==1:qc+=(1-2*p)/2
    if core==0:qc+=Q(1,2)
    expect=qc/16+(Q(1,4) if T==0 else 0)
    ck(q==expect)
   pv=h.law(v);iv=h.influence(v);a=rho*(1-Q(scalar['nu']))/2
   ck(4*iv==6+2*(k-1)*a+rho*(Q(3*n[3],4)+n[2]+n[1])-(1 if qb==0 else -1)*a)
   overlap(h.ce(pv,qr),ce);queries+=1
  cache[key]=True
 return {'k':k,'m':m,'partial_assignments':3**(3*m),'q_signed_histories':queries,'canonical_cleanup_states':len(cache),'all_cleanup_outcomes_represented':clean_hist,'status':'PASS','caveat':'partial assignments overlap and are not summed as disjoint leaves; pointwise checks cover any adaptive leaf partition'}
def main(pilot):
 start=time.perf_counter();out={'status':'RUNNING','profiles':[],'literal':[]}
 ck(15**15>2**56);ck(31**31>2**152)
 ck(Q(3)-8*Q(81,256)-Q(1,3)==Q(13,96));ck(H0[1]<3);ck(C2[1]<Q(5,2))
 counts=[(0,0,0),(1,0,0),(0,0,1)] if pilot else list(product(range(3),repeat=3))+[(3,0,0),(8,0,0),(0,8,0),(0,0,8),(8,8,8)]
 file=R/'out'/('PILOT.json' if pilot else 'CHECK.json')
 for k in ([5] if pilot else [5,8]):
  for n3,n2,n1 in counts:
   for phase in [1,-1]:
    out['profiles'].append(profile(k,n3+n2+n1+4,n3,n2,n1,phase)[0]);ck(time.perf_counter()-start<60)
  file.write_text(json.dumps(out,indent=2),encoding='utf-8')
 for m in ([1] if pilot else [1,2]):
  out['literal'].append(literal(1,m));ck(time.perf_counter()-start<60)
 out.update(status='PASS',assertions=N,runtime_seconds=time.perf_counter()-start)
 file.write_text(json.dumps(out,indent=2),encoding='utf-8')
 print(json.dumps({'status':out['status'],'assertions':N,'profiles':len(out['profiles']),'literal_cases':len(out['literal']),'runtime_seconds':out['runtime_seconds']}))
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');main(ap.parse_args().pilot)
