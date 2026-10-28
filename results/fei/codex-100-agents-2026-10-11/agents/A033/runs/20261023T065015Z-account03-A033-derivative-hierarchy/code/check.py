from fractions import Fraction as Q
from pathlib import Path
from math import comb
import json,time,hashlib
ROOT=Path(__file__).resolve().parents[1];START=time.monotonic();checks=0
def ck(v):
 global checks
 checks+=1
 if not v:raise AssertionError(checks)
 if time.monotonic()-START>55:raise TimeoutError('frozen 55s cap')
def fw(tt):
 w=list(tt);step=1
 while step<len(w):
  for k in range(0,len(w),2*step):
   for j in range(k,k+step):a,b=w[j],w[j+step];w[j],w[j+step]=a+b,a-b
  step*=2
 return w
def direct(tt):return [sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(tt)) for s in range(len(tt))]
def ins(v,j,b):return (v&((1<<j)-1))|((v>>j)<<(j+1))|(b<<j)
def edge(tt,j):return Q(sum(tt[x]!=tt[x^(1<<j)] for x in range(len(tt))),len(tt))
def prob(tt):return tuple(Q(v*v,len(tt)**2) for v in fw(tt))
def maj(m):return tuple(1 if x.bit_count()<=m else -1 for x in range(1<<(2*m+1)))
for m in (1,2,3,4):
 g=maj(m);ck(sum(g)==0)
 for j in range(2*m+1):ck(edge(g,j)==Q(comb(2*m,m),4**m))
for m in list(range(257))+[8192,32768]:
 a=Q(comb(2*m,m),4**m);ck(a*a*(3*m+1)<=1)
 ck((3*m+1)*(2*m+2)**2-(3*m+4)*(2*m+1)**2==m)
def mul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c
l=mul([1,3],mul([2,2],[2,2]));r=mul([4,3],mul([1,2],[1,2]));ck([x-y for x,y in zip(l,r)]==[0,1,0,0])
rates=[]
for K,m in ((2,8192),(4,32768),(17,524288),(100,16777216)):
 ck(4096*K*K<3*m+1)
 rates.append({'K':K,'m':m,'core_bits':2*m+1,'exact_sufficient_guard':f'{4096*K*K} < {3*m+1}','strength':'1/64','strict_reset_lower_bound':'beta/64','strict_K_influence_upper_bound':'beta/64'})
# Direct characters reconstruct the full physical seed, independently of block injection code.
g=maj(1);N=9
h=tuple(g[sum(((x>>(3*j)&7).bit_count()%2)<<j for j in range(3))] for x in range(1<<N))
wh=direct(h);ck(wh==fw(h));ph=tuple(Q(w*w,len(h)**2) for w in wh)
ck(all(not ph[s] or all((s>>(3*j)&7) in (0,7) for j in range(3)) for s in range(len(h))))
a=(1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1);b=tuple(1-x*x for x in a)
aa=tuple(Q(x,16) for x in direct(a));bb=tuple(Q(x,16) for x in direct(b));beta=sum(x*x for x in bb)
ck(beta==Q(3,8))
C=sum(x*x*y*y for x,y in zip(aa,bb));D=sum(x*y**3 for x,y in zip(aa,bb));E=sum(y**4 for y in bb)
ck((C,D,E,C-D*D/E)==(Q(3,512),Q(3,256),Q(21,512),Q(9,3584)))
terminals=[]
for sig in (1,-1):
 tt=tuple(a[u]+sig*b[u]*h[x] for x in range(len(h)) for u in range(16));p=prob(tt)
 ck(all(abs(v)==1 for v in tt));ck(edge(tt,4)==beta*Q(1,2))
 pm=tuple(p[ins(v,4,0)]+p[ins(v,4,1)] for v in range(len(tt)//2))
 ck(all(not(p[ins(v,4,0)] and p[ins(v,4,1)]) for v in range(len(pm))))
 for outcome in (0,1):
  child=tuple(tt[ins(v,4,outcome)] for v in range(len(tt)//2));pc=prob(child)
  ck(pc==pm)
  # Remaining physical seed bit0 is in a two-bit block; singleton1 is OFF image.
  target=1
  ck(all(pc[u+16*target]==0 for u in range(16)))
  q=list(pc)
  for T in range(1,len(pc)//16):
   for u in range(16):q[u+16*T]=Q(63,64)*pc[u+16*T]+(Q(1,64)*bb[u]**2 if T==target else 0)
  ck(sum(q)==1);ck(q[:16]==list(pc[:16]));ck(sum(pc[16:])==beta)
  ck(all(not p0 or q0==p0*Q(63,64) for p0,q0 in zip(pc[16:],q[16:])))
  ck(all(not p0 or q0>0 for p0,q0 in zip(pc,q)))
  # Exact support/floor certificates force CE(new)-CE(old)=beta*log2(64/63).
  terminals.append({'tag_sign':sig,'physical_outcome':outcome,'tail_mass':str(beta),'reset_log_ratio':'64/63','current_refund':'0','actual_influence':str(beta/2),'full_new_reference_sha256':hashlib.sha256('|'.join(map(str,q)).encode()).hexdigest()})
# Positive control at completion: point defect core with two-bit blocks.
core=(-1,1,1,1);lift=tuple(core[((x&3).bit_count()%2)|(((x>>2&3).bit_count()%2)<<1)] for x in range(16))
parent=tuple(lift[ins(v,0,0)] for v in range(8));pa=prob(parent)
children=[tuple(parent[ins(v,0,o)] for v in range(4)) for o in (0,1)]
def dyadH(p):
 total=Q(0)
 for v in p:
  if v:
   ck(v.numerator&(v.numerator-1)==0 and v.denominator&(v.denominator-1)==0)
   total+=v*(v.denominator.bit_length()-v.numerator.bit_length())
 return total
mh=tuple(pa[ins(v,0,0)]+pa[ins(v,0,1)] for v in range(4))
Hp=dyadH(pa);Hm=dyadH(mh);Hc=sum(dyadH(prob(tt)) for tt in children)/2
ck((Hp,Hm,Hc)==(2,1,0))
# The polynomial guard is universal; this independent finite Gamma computation is source review evidence only.
out={'status':'PASS','helper':'A033-majority-local-rate-v1','exact_assertions':checks,'runtime_seconds':time.monotonic()-START,'majority_truth_tables':4,'central_binomial_parameters':259,'rate_certificates':rates,'full_terminal_count':4,'terminals':terminals,'completion_boundary':{'H_parent':str(Hp),'H_marginal':str(Hm),'mean_H_children':str(Hc),'conditional_erasure':'1','JS':'1'},'A096_Gram':{'C':str(C),'D':str(D),'E':str(E),'Gamma':str(C-D*D/E)},'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/'out').mkdir(exist_ok=True)
(ROOT/'out/validation.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ('terminals','rate_certificates')}))
