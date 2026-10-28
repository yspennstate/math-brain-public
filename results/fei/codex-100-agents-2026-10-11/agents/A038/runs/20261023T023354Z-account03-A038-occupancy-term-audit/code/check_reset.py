import sys,json,time,hashlib
from pathlib import Path
from fractions import Fraction as F
import interval_primitives as m
R=Path(__file__).resolve().parents[1]
V=m.V
START=time.monotonic();COUNT=0
def check(b,label):
 global COUNT
 COUNT+=1
 assert b,label
 if time.monotonic()-START>55: raise RuntimeError('55 second frozen watchdog')
def overlap(a,b,label):check(a.a<=b.b and b.a<=a.b,label+' (diagnostic only)')
def encloses(a,x):return a.a<=x<=a.b
def norm(q):
 mass=sum(q,V(0));check(mass.a>0,'positive inherited outcome mass')
 return [x/mass for x in q]
def wht(t):
 a=list(t);step=1
 while step<len(a):
  for base in range(0,len(a),2*step):
   for j in range(base,base+step):
    u,v=a[j],a[j+step];a[j]=u+v;a[j+step]=u-v
  step*=2
 return [F(x,len(t)) for x in a]
def source(t):
 N=m.node(t)
 check(N['a']==wht(t),'independent butterfly vs direct Fourier transform')
 check(sum(N['p'])==1,'Parseval')
 return N
def product_q(d):
 out=[]
 for s in range(1<<len(d)):
  q=F(1)
  for j,v in enumerate(d):q*=v if s>>j&1 else 1-v
  out.append(q)
 return out
def reset(N,names):
 # Analytically classified terminal family; forced-coordinate canonical law,
 # otherwise point-defect/character/constant actual spectrum is canonical.
 p=N['p'];d=N['d']
 if p[0]==0 and F(1) in d:q=product_q(d);kind='forced-coordinate canonical'
 else:q=p[:];kind='point-defect/constant actual canonical'
 check(sum(q)==1,'new reference normalization')
 for j,v in enumerate(d):check(sum(q[s] for s in range(len(q)) if s>>j&1)==v,'new canonical inclusion moment')
 check(q[0]==p[0],'new canonical empty mass')
 for w,v in zip(p,q):check(w==0 or v>0,'new reference dominates actual source')
 if kind.startswith('point') and p[0]!=1:
  check(len(set(w for w in p[1:] if w))==1,'uniform nonempty point-defect law')
 K=m.kl(p,[V(v) for v in q]);check(K.b<=F(7,8),'prescribed reset KL bound')
 check(N['H'].b<=4*N['I'],'terminal actual H<=4I certificate')
 return K,kind
def make_root():
 t=[]
 for v in range(128):
  x,a,b=[v>>j&1 for j in range(3)]
  core=(-1 if v>>6&1 else 1)*(-1 if (v>>3)&7==0 else 1)
  t.append((-1 if a else 1) if not x else (core if b else 1))
 N=source(t);v=1-N['p'][0];r=[d/v for d in N['d']]
 check(v==F(15,16),'root variance')
 def poly(c):
  q=F(1)
  for d in r:q*=1-c*d
  return 1-c-q
 lo,hi=F(3,4),F(1)
 check(poly(lo)>0>poly(hi),'canonical positive root bracket')
 deriv=F(0)
 for j,d in enumerate(r):
  z=d
  for k,e in enumerate(r):
   if k!=j:z*=1-lo*e
  deriv+=z
 check(deriv<1,'strict derivative bracket certificate')
 for _ in range(42):
  mid=(lo+hi)/2
  if poly(mid)>0:lo=mid
  else:hi=mid
 c=V(lo,hi);q=[]
 for s in range(128):
  if s==0:q.append(V(1-v));continue
  z=V(v)/c
  for j,d in enumerate(r):z=z*(c*d if s>>j&1 else 1-c*d)
  q.append(z)
 check(encloses(sum(q,V(0)),1),'original reference normalization')
 for j,d in enumerate(N['d']):check(encloses(sum((q[s] for s in range(128) if s>>j&1),V(0)),d),'original inclusion moment')
 A=m.kl(N['p'],q);check(A.b<F(39,32),'sharper uniform source bound exercised')
 return N,q,A,c
def physical(policy,N,q,A):
 terminals=[];releases=V(0);refonly=0;nodes=0;xchecks=0
 def step(N,q,names,weight,path):
  nonlocal releases,refonly,nodes,xchecks
  nodes+=1
  if not path:
   terminals.append((N,q,names,weight));return
  label=path[0];i=names.index(label);rest=names[:i]+names[i+1:]
  pq=m.push(N,q,i);pp=m.push(N,[V(v) for v in N['p']],i)
  kids=[source(m.restrict(N['t'],i,b)) for b in range(2)]
  for b in range(2):
   for actual,w in zip(pp[b],kids[b]['p']):check(actual.a==actual.b==w/2,'actual common-channel source push')
  qn=norm(q);barp=[];barq=[]
  for s in range(len(q)):
   if s>>i&1:continue
   barp.append(N['p'][s]+N['p'][s|(1<<i)])
   barq.append(qn[s]+qn[s|(1<<i)])
   if barp[-1]==0 and barq[-1].a>0:
    refonly+=1
    check(barq[-1].a>0,'reference-only erased row retained')
  Kin=m.kl(N['p'],qn);erasure=Kin-m.kl(barp,barq)
  qm=sum(q,V(0));outmass=[sum(row,V(0))/qm for row in pq]
  O=m.kl([F(1,2)]*2,outmass)
  childK=sum((m.kl(kids[b]['p'],norm(pq[b]))*F(1,2) for b in range(2)),V(0))
  overlap(Kin,erasure+O+childK,'one-node complete KL chain')
  releases+=(erasure+O)*weight
  if label=='x':
   xchecks+=1
   avgH=(kids[0]['H']+kids[1]['H'])*F(1,2)
   avgI=(kids[0]['I']+kids[1]['I'])/2
   check(N['I']-avgI==F(1,2),'x exact influence decrement')
   overlap(N['H']-avgH,V(2),'x entropy decrement')
   overlap(4*N['I']-N['H'],4*avgI-avgH,'x surplus neutrality')
  for b in range(2):
   tail=path[1:]
   if label=='b' and b==0:tail=[]
   if policy==3 and label=='y0':tail=['x','y1' if b==0 else 'z']
   step(kids[b],pq[b],rest,weight/2,tail)
 paths=[['b','y0','x','y1'],['b','z','x','y0'],['b','x','y0','z'],['b','y0'],['b','y0','y1','x']]
 step(N,q,['x','a','b','y0','y1','y2','z'],F(1),paths[policy])
 Hf=sum((n['H']*w for n,qq,nn,w in terminals),V(0));If=sum((n['I']*w for n,qq,nn,w in terminals),F(0))
 S=4*If-Hf;Sroot=4*N['I']-N['H'];L=A+m.positive(N['H']-Hf-4*(N['I']-If))
 if policy==4:
  # x is appended immediately to the prior data frontier: total b1 weight1/2.
  # Hprefix=Hf+1 and Iprefix=If+1/4 by the exact pair identity.
  Lprefix=A+m.positive(N['H']-(Hf+1)-4*(N['I']-(If+F(1,4))))
  check(Lprefix.a==L.a and Lprefix.b==L.b,'old whole liability retained exactly, no refund')
 oldterm=V(0);B=V(0);C=V(0);rows=[];core_weight=F(0)
 for n,qq,names,w in terminals:
  oldK=m.kl(n['p'],norm(qq));oldterm+=oldK*w
  # b0 is the sole terminal still containing x. Its inherited law is kept.
  if 'x' in names:newK=V(0);kind='retained b0 inherited reference'
  else:
   newK,kind=reset(n,names);B+=newK*w;C+=m.positive(newK-oldK)*w
   # x0 leaves have actual character a; identify by its physical influence.
   if n['d'][names.index('a')]==0:core_weight+=w
  rows.append({'weight':str(w),'remaining':names,'H':n['H'].out(),'I':str(n['I']),'old_KL':oldK.out(),'new_KL':newK.out(),'reference':kind})
 check(sum(w for n,qq,nn,w in terminals)==1,'all physical terminals retained')
 check(core_weight==F(1,4),'total actual b1x1 core weight')
 overlap(A,releases+oldterm,'full original reference source telescope')
 overlap(S-L,V(min(S.a-A.b,Sroot.a-A.b),min(S.b-A.a,Sroot.b-A.a)),'same-owner min identity')
 check(S.a>=2,'final physical owner floor')
 check(B.b<=F(7,32),'all new canonical terminal KL paid')
 check(C.b<=B.b+F(1,10**17),'actual positive conversion bounded by full new KL (interval diagnostic)')
 residual=S-L-F(11,32)-B
 check(residual.a>F(7,32),'same diminished original owner after old booking and reset')
 check(refonly>0 and xchecks>0,'active x and reference-only fibers exercised')
 return {'policy':policy,'nodes':nodes,'reference_only_rows':refonly,'x_queries':xchecks,'A':A.out(),'S':S.out(),'L':L.out(),'B':B.out(),'C':C.out(),'omega':'11/32','remaining':residual.out(),'complete_old_terminal_KL':oldterm.out(),'complete_old_releases':releases.out(),'terminals':rows}
def scalar():
 rows=[]
 check(3**12>2**19,'quarter entropy bound')
 for k in range(17):
  eps=F(1,2**k)
  if k==0:p=[F(1)];I=F(0);T=V(0)
  else:
   p=[(1-2*eps)**2];I=2*k*eps
   # Avoid materializing product reference: exact entropy of explicit spectrum.
   H=-(p[0]*m.lg(p[0]) if p[0] else V(0))-(2**k-1)*4*eps**2*m.lg(4*eps**2)
   T=k*m.h(2*eps)-H
   check(H.b<=4*I,'point-defect certificate')
  if k>=3:
   E=2*eps*(k*k-F(7,2)*k+4+4*(k-1)*eps)
   En=eps*((k+1)**2-F(7,2)*(k+1)+4+2*k*eps)
   check(E<=F(7,8) and En<E,'decreasing reset envelope')
   check(T.b<E,'actual reset below envelope')
  else:check(T.a<=0<=T.b,'zero boundary reset')
  check(T.b<=F(7,8),'uniform reset price')
  rows.append({'k':k,'reset_KL':T.out()})
 for n in range(3,17):
  eps=F(1,2**n);G=2*m.h(F(1,4))+n*m.h(eps/2)
  Hlow=8*(n-1)*eps*(1-eps)
  check((G-1-Hlow/4).b<F(39,32),'sharper source envelope')
  en=F(n*(2*n+5),2**(n+2));enext=F((n+1)*(2*n+7),2**(n+3))
  check(enext<en,'root envelope monotonicity')
 return rows
if __name__=='__main__':
 N,q,A,c=make_root();policies=[4] if '--direct-only' in sys.argv else ([0] if '--pilot' in sys.argv else list(range(4)))
 sc=scalar();out=[physical(i,N,q,A) for i in policies]
 result={'status':'PASS','assertions':COUNT,'primitive_assertions':m.COUNT,'runtime_seconds':time.monotonic()-START,'canonical_root_bracket':c.out(),'source_A':A.out(),'scalar_rows':sc,'histories':out,'scope':'analytic PROOF supplies all m/history quantifiers; KL interval overlaps are diagnostics only'}
 name='DIRECT_PREFIX.json' if '--direct-only' in sys.argv else ('PILOT.json' if '--pilot' in sys.argv else 'CHECK.json')
 (R/'out'/name).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:result[k] for k in ['status','assertions','primitive_assertions','runtime_seconds']}))
