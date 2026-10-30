from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json,time,sys
R=Path(__file__).resolve().parents[1]
def save(n,x):(R/n).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
pilot='--pilot' in sys.argv;n=2 if pilot else 3
save('out/FROZEN_'+('PILOT' if pilot else 'MAIN')+'.json',dict(helper='check.py v1',family='all labelled Boolean seeds, fixed actual 4-bit complementary controller; exact and flat-tail coherent incoming laws',domain=f'n={n}, all queries, two source references, pre-outcome sign bins',case_count=(2**(2**n))*n*2,symmetry='none',arithmetic='Fraction Fourier amplitudes and prime-factor symbolic log2; no floating signs',memory_estimate_MB=100,max_runtime_seconds=55,automatic_dimension_escalation=False))
start=time.monotonic();checks=cases=zero=positive=0
def ck(v):
 global checks
 checks+=1;assert v,checks
 assert time.monotonic()-start<55,'55 second wall cap'
def fw(t):
 return [F(sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(t)),len(t)) for s in range(len(t))]
def restrict(t,j,b):return [t[(x&((1<<j)-1))|(b<<j)|((x>>j)<<(j+1))] for x in range(len(t)//2)]
def insert(x,j,b):return (x&((1<<j)-1))|(b<<j)|((x>>j)<<(j+1))
def logs(x):
 out={}
 for v,sgn in [(x.numerator,1),(x.denominator,-1)]:
  d=2
  while d*d<=v:
   while v%d==0:out[d]=out.get(d,0)+sgn;v//=d
   d+=1
  if v>1:out[v]=out.get(v,0)+sgn
 return {k:F(v) for k,v in out.items() if v}
def add(*terms):
 out={}
 for a,d in terms:
  for p,v in d.items():out[p]=out.get(p,F(0))+a*v
 return {p:v for p,v in out.items() if v}
def ce(p,q):return add(*[(-x,logs(y)) for x,y in zip(p,q) if x])
def kl(p,q):return add((1,ce(p,q)),(-1,ce(p,p)))
def avg(a,b):return [(x+y)/2 for x,y in zip(a,b)]
def js(a,b):return add((1,ce(avg(a,b),avg(a,b))),(-F(1,2),ce(a,a)),(-F(1,2),ce(b,b)))
a=[1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1];b=[1-v*v for v in a]
A=fw(a);B=fw(b);beta=sum(x*x for x in B);E=sum(x**4 for x in B)
C=sum(x*x*y*y for x,y in zip(A,B));D=sum(x*y**3 for x,y in zip(A,B));gamma=C-D*D/E
ck((beta,E,gamma)==(F(3,8),F(21,512),F(9,3584)))
for truth in product([-1,1],repeat=2**n):
 H=fw(truth);m=H[0];P=[x*x for x in H]
 for j in range(n):
  u=[H[insert(x,j,0)] for x in range(2**(n-1))];v=[H[insert(x,j,1)] for x in range(2**(n-1))]
  ch=[[x*x for x in fw(restrict(truth,j,t))] for t in [0,1]]
  bins=[[t for t in range(1,len(u)) if (u[t]*v[t]>=0)==sgn] for sgn in [True,False]]
  c=[sum((u[t]*v[t] for t in w),F(0)) for w in bins]
  x=gamma*v[0]**2+E*sum(z*z for z in c)
  seed=[[p[0]]+[sum((p[t] for t in w),F(0)) for w in bins] for p in ch]
  pc=[]
  for p in ch:
   childmean=sum(restrict(truth,j,len(pc)))/F(len(truth)//2)
   pc.append([(aa+childmean*bb)**2 for aa,bb in zip(A,B)]+[bb*bb*sum((p[t] for t in w),F(0)) for bb in B for w in bins])
  ck(all(sum(p)==1 for p in pc))
  half=[(p-q)/2 for p,q in zip(*pc)]
  ck(sum(z*z for z in half)>=4*x)
  for flat in [False,True]:
   source=P if not flat else [P[0]]+[(1-P[0])/F(len(P)-1)]*(len(P)-1)
   rbar=[source[insert(t,j,0)]+source[insert(t,j,1)] for t in range(len(u))]
   q=[(aa+m*bb)**2+bb*bb*source[1<<j] for aa,bb in zip(A,B)]+[bb*bb*sum((rbar[t] for t in w),F(0)) for bb in B for w in bins]
   ck(sum(q)==1)
   rho=add((F(1,2),kl(pc[0],q)),(F(1,2),kl(pc[1],q)))
   ck(rho==add((1,js(*pc)),(1,kl(avg(*pc),q))))
   if v[0]==0:
    ck(js(*pc)==add((beta,js(*seed))))
    tv=sum(abs(p-q) for p,q in zip(*ch))/2
    ck(x==E*tv*tv/8)
    ck((x>0)==(ch[0]!=ch[1]))
    z=beta*tv*tv/4
    ck(z*E==x*2*beta)
    zero+=1;positive+=int(tv>0)
   cases+=1
# Exact positive witness is evaluated on the original three-bit seed, in both runs.
truth=[(-1 if z<4 else 1)*(-1 if z%4==0 else 1) for z in range(8)]
hh=fw(truth);pp=[[v*v for v in fw(restrict(truth,0,s))] for s in [0,1]]
ck(hh[0]==hh[1]==0)
tv=sum(abs(u-v) for u,v in zip(*pp))/2;ck(tv==1)
z=beta*tv*tv/4;epsilon=z/(beta+z);old=E*tv*tv/8
ck((z,epsilon,old)==(F(3,32),F(1,5),F(21,4096)))
# After bin calibration children are exact point seed spectra; mix toward the other child.
new=[[ (1-epsilon)*x+epsilon*y for x,y in zip(pp[t],pp[1-t])] for t in [0,1]]
for t in [0,1]:ck(ce(pp[t],new[t])==add((1,logs(F(5,4)))))
wrapper=[a[z&15]+b[z&15]*truth[z>>4] for z in range(128)]
actual=[t*t for t in fw(wrapper)]
for U in range(16):
 for T in range(8):ck(actual[U+16*T]==((A[U]+hh[0]*B[U])**2 if T==0 else B[U]**2*hh[T]**2))
save('out/'+('PILOT' if pilot else 'VALIDATION')+'.json',dict(status='PASS',assertions=checks,cases=cases,zero_singleton_cases=zero,positive_zero_singleton_cases=positive,seconds=time.monotonic()-start,witness=dict(beta=str(beta),old_x=str(old),new_x=str(z),old_epsilon='7/519',new_epsilon=str(epsilon),ratio=str(z/old),full_increment='(3/8)log2(5/8)',net_certificate='<=-3/(32 ln2); occupancy KL retained'),limitations='Exact tests check probability laws, Gram factors, JS decomposition and TV energy identities. KL/Pinsker signs and full analytic quantifiers are proved in DERIVATION, not inferred from tests.'))
print(json.dumps(json.loads((R/'out'/('PILOT.json' if pilot else 'VALIDATION.json')).read_text())))
