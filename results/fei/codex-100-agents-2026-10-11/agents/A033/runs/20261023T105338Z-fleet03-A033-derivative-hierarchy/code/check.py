from pathlib import Path
from fractions import Fraction as F
from itertools import product
from functools import lru_cache
import json,time,hashlib,sys
ROOT=Path(__file__).resolve().parents[1]
START=time.monotonic();checks=0;transactions=0;terminals=0;iso=0;positive=0
PILOT='--pilot' in sys.argv
PANEL='--panel' in sys.argv
def ck(v):
 global checks
 checks+=1
 if not v:raise AssertionError(checks)
 if time.monotonic()-START>55:raise TimeoutError('frozen55s cap')
def char(tt):
 return tuple(F(sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(tt)),len(tt)) for s in range(len(tt)))
def ins(v,j,b):return (v&((1<<j)-1))|((v>>j)<<(j+1))|(b<<j)
def restrict(tt,j,o):return tuple(tt[ins(x,j,o)] for x in range(len(tt)//2))
def law(tt):return tuple(v*v for v in char(tt))
def l2(a,b):return sum((x-y)**2 for x,y in zip(a,b))
def parts(xs):
 if not xs:yield ();return
 for p in parts(xs[1:]):
  yield ((xs[0],),)+p
  for i in range(len(p)):yield p[:i]+((xs[0],)+p[i],)+p[i+1:]
a=(1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1)
b=tuple(1-v*v for v in a);A=char(a);B=char(b)
beta=sum(v*v for v in B);C=sum(v*v*w*w for v,w in zip(A,B));D=sum(v*w**3 for v,w in zip(A,B));E=sum(v**4 for v in B);Gamma=C-D*D/E
ck((beta,C,D,E,Gamma)==(F(3,8),F(3,512),F(3,256),F(21,512),F(9,3584)))
digest=hashlib.sha256();witness=None
for n in range(1,3 if PILOT else 4):
 N=1<<n;H=N//2
 domain=list(product((-1,1),repeat=N))
 if PANEL and n==3:
  first=domain[:32]
  wit=tuple(((-1 if (s&3)==0 else 1)*(-1 if s&4 else 1)) for s in range(8))
  parity=tuple(-1 if s.bit_count()%2 else 1 for s in range(8))
  domain=sorted(set(first+[tuple(-z for z in tt) for tt in first]+[wit,tuple(-z for z in wit),parity,tuple(-z for z in parity)]))
 for values in domain:
  hat=char(values);P=tuple(v*v for v in hat);m=hat[0];d=hat[1]
  u=hat[::2];v=hat[1::2];uv=tuple(x*y for x,y in zip(u,v))
  ck(sum(P)==1 and sum(uv)==0)
  hp=[restrict(values,0,o) for o in (0,1)];hh=[char(t) for t in hp];pp=[tuple(z*z for z in h) for h in hh]
  ck(all(hh[o]==tuple(x+(1 if o==0 else -1)*y for x,y in zip(u,v)) for o in (0,1)))
  bins=tuple(z for z in (tuple(t for t in range(1,H) if uv[t]>=0),tuple(t for t in range(1,H) if uv[t]<0)) if z)
  opt=sum(sum(uv[t] for t in w)**2 for w in bins)
  for partition in parts(tuple(range(1,H))):ck(sum(sum(uv[t] for t in w)**2 for w in partition)<=opt)
  if d==0:ck(opt==sum(abs(uv[t]) for t in range(1,H))**2/2)
  for sig in (1,-1):
   tt=tuple(a[c]+sig*b[c]*values[s] for s in range(N) for c in range(16))
   # Full actual wrapper laws reconstructed from truth, not from the claimed reference formula.
   par=law(tt);child=[law(restrict(tt,4,o)) for o in (0,1)]
   pm=tuple(par[ins(z,4,0)]+par[ins(z,4,1)] for z in range(len(par)//2))
   ck(tuple((x+y)/2 for x,y in zip(*child))==pm)
   ck(all(par[16*t+c]==((A[c]+sig*m*B[c])**2 if t==0 else B[c]**2*P[t]) for t in range(N) for c in range(16)))
   for ref in ('actual','uniform'):
    R=P if ref=='actual' else (m*m,)+tuple((1-m*m)/F(N-1) for _ in range(N-1))
    Q=tuple((A[c]+sig*m*B[c])**2 if t==0 else B[c]**2*R[t] for t in range(N) for c in range(16))
    qm=tuple(Q[ins(z,4,0)]+Q[ins(z,4,1)] for z in range(len(Q)//2))
    rb=tuple(R[2*t]+R[2*t+1] for t in range(H))
    ck(sum(Q)==sum(qm)==1 and all(not p or q>0 for p,q in zip(par,Q)))
    # Conditional occupancy chain is certified exactly by its underlying joint/marginal disintegration.
    for z,pz in enumerate(pm):
     if pz:
      ck(qm[z]>0)
      ck(sum(par[ins(z,4,o)]/pz for o in (0,1))==1)
      ck(sum(Q[ins(z,4,o)]/qm[z] for o in (0,1))==1)
    for partition in ((tuple(range(1,H)),) if H>1 else (),bins):
     cs=tuple(sum(uv[t] for t in w) for w in partition)
     x=Gamma*d*d+E*sum(c*c for c in cs)
     ck(x>=0)
     coarse=lambda z:tuple(z[c] for c in range(16))+tuple(sum(z[16*t+c] for t in w) for c in range(16) for w in partition)
     qco=coarse(qm);pco=[coarse(p) for p in child]
     z=tuple((x0-x1)/2 for x0,x1 in zip(*pco))
     formula=tuple(2*d*B[c]*(sig*A[c]+m*B[c]) for c in range(16))+tuple(2*B[c]**2*c0 for c in range(16) for c0 in cs)
     ck(z==formula)
     ck(sum(zz*zz for zz in z)>=4*x)
     pavg=tuple((x0+x1)/2 for x0,x1 in zip(*pco))
     ck((l2(pco[0],qco)+l2(pco[1],qco))/2==l2(pavg,qco)+sum(zz*zz for zz in z))
     for o in (0,1):
      pc=child[o];mch=hh[o][0];rc=[F(0)]*H;rc[0]=mch*mch
      for w in partition:
       mass=sum(pp[o][t] for t in w);den=sum(rb[t] for t in w)
       ck(not mass or den>0)
       for t in w:rc[t]=mass*rb[t]/den if mass else F(0)
      qc=tuple((A[c]+sig*mch*B[c])**2 if t==0 else B[c]**2*rc[t] for t in range(H) for c in range(16))
      ck(sum(rc)==sum(qc)==1 and all(not p or q>0 for p,q in zip(pc,qc)))
      ck(coarse(qc)==pco[o])
      # Check every calibration multiplier; these equalities certify the exact log-sum CE refund.
      blocks=[(c,) for c in range(16)]+[tuple(16*t+c for t in w) for c in range(16) for w in partition]
      for block in blocks:
       tr=sum(pc[z0] for z0 in block);old=sum(qm[z0] for z0 in block)
       ck(all(qc[z0]==(qm[z0]*tr/old if tr else 0) for z0 in block))
      tail=beta*(1-mch*mch);eps=x/(tail+x) if tail*x else F(0)
      qnew=tuple(qc[c] if t==0 else (1-eps)*qc[16*t+c]+eps*B[c]**2*(1-mch*mch)/F(H-1) for t in range(H) for c in range(16))
      ck(sum(qnew)==1 and qnew[:16]==qc[:16])
      ck(all(not p or q>0 for p,q in zip(pc,qnew)))
      ck(all(qnew[z0]>=(1-eps)*qc[z0] for z0 in range(16,len(qnew))))
      ck(sum(pc[16:])==tail)
      if eps:ck(1-eps==tail/(tail+x))
      if ref=='actual' and d==0 and not any(uv):ck(pc==qm and qc==pc)
      digest.update('|'.join(map(str,qnew)).encode('utf-8'));terminals+=1
     transactions+=1
     if x:positive+=1
     else:iso+=1
     if n==3 and values==tuple(((-1 if (s&3)==0 else 1)*(-1 if s&4 else 1)) for s in range(8)) and partition==bins:
      ck((m,d,x)==(0,0,F(21,4096)));ck(x/(beta+x)==F(7,519));witness={'x':str(x),'epsilon':str(x/(beta+x)),'both_children_retained':True}
out={'status':'PASS','helper':'A033-independent-A097-v1.1','pilot':PILOT,'panel':PANEL,'seed_queries':transactions//8,'transactions':transactions,'full_terminal_references':terminals,'positive_energy_transactions':positive,'zero_energy_transactions':iso,'exact_assertions':checks,'runtime_seconds':time.monotonic()-START,'terminal_digest':digest.hexdigest(),'witness':witness,'arithmetic':'integer direct characters and Fraction; analytic CE/refund inequalities reconstructed in REVIEW_A097.md','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/'out').mkdir(exist_ok=True)
(ROOT/'out'/('pilot.json' if PILOT else 'validation.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
