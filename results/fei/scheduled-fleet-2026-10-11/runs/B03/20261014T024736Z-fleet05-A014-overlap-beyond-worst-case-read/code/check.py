from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import argparse,itertools,json,time
R=Path(__file__).resolve().parents[1]
start=time.monotonic(); assertions=0
parser=argparse.ArgumentParser();parser.add_argument('--pilot',action='store_true');args=parser.parse_args()
budget=60 if args.pilot else 300
def ck(x):
 global assertions
 assertions+=1
 assert x
 if time.monotonic()-start>budget: raise TimeoutError('Frozen budget')
def walsh(a):
 a=list(a);h=1
 while h<len(a):
  for i in range(0,len(a),2*h):
   for j in range(i,i+h):
    u,v=a[j],a[j+h];a[j],a[j+h]=u+v,u-v
  h*=2
 return a
@lru_cache(None)
def factors(n):
 out={}; p=2
 while p*p<=n:
  while n%p==0:out[p]=out.get(p,0)+1;n//=p
  p+=1
 if n>1:out[n]=out.get(n,0)+1
 return out
def add(*terms):
 out={}
 for scale,v in terms:
  for prime,c in v.items():out[prime]=out.get(prime,F(0))+scale*c
 return {p:c for p,c in out.items() if c}
@lru_cache(None)
def H(probs):
 out={}
 for p in probs:
  if p:
   for prime,e in factors(p.denominator).items():out[prime]=out.get(prime,F(0))+p*e
   for prime,e in factors(p.numerator).items():out[prime]=out.get(prime,F(0))-p*e
 return {prime:c for prime,c in out.items() if c}
def entropy(probs):return H(tuple(probs))
def binary(p):return entropy([p,1-p])
@lru_cache(None)
def log_vector(q):
 return add((1,{p:F(e) for p,e in factors(q.numerator).items()}),(-1,{p:F(e) for p,e in factors(q.denominator).items()}))
def CE(P,Q):
 return add(*[(-p,log_vector(q)) for p,q in zip(P,Q) if p])
def influence(values):
 n=(len(values)).bit_length()-1
 return sum((F(sum(values[x]!=values[x^(1<<j)] for x in range(len(values))),len(values)) for j in range(n)),F(0))
def component(mask):
 v=[int(mask&(1<<i)!=0) for i in range(4)]
 a=F(sum(v),4); hats=walsh(v)
 P=[F(t*t,16*a) for t in hats] if a else [F(0)]*4
 fv=[1-2*t for t in v]
 return v,a,hats,P,entropy(P),entropy([F(t*t,16) for t in walsh(fv)]),influence(fv)
components={mask:component(mask) for mask in range(16)}
pairs=[(u,v) for u in range(16) for v in range(16) if v&u==v]
ck(len(pairs)==81)
cases=[(pair,pair) for pair in pairs] if args.pilot else list(itertools.product(pairs,pairs))
stats={'cases':0,'nonzero_blockers':0,'zero_blockers':0,'positive_private_monotone_cases':0,'nontrivial_shared_bit':0}
samples=[]
def decreasing(mask):return all(not (mask&(1<<i)) or mask&(1<<j) for i in range(4) for j in range(4) if j&i==j)
for hp,kp in cases:
 hs=[components[t] for t in hp];ks=[components[t] for t in kp]
 As=[hs[i][1]*ks[i][1] for i in range(2)];s=sum(As)/2
 C=[hs[x&1][0][(x>>1)&3]*ks[x&1][0][(x>>3)&3] for x in range(32)]
 ck(F(sum(C),32)==s)
 f=[1-2*t for t in C];fhat=walsh(f)
 I=sum((F(A.bit_count()*t*t,1024) for A,t in enumerate(fhat)),F(0))
 Ix=As[0]-As[1]
 private=sum((ks[i][1]*hs[i][6]/2+hs[i][1]*ks[i][6]/2 for i in range(2)),F(0))
 ck(I==private+Ix); ck(I==influence(f))
 stats['cases']+=1
 if all(decreasing(t) for t in hp+kp):stats['positive_private_monotone_cases']+=1
 if Ix:stats['nontrivial_shared_bit']+=1
 if not s:
  stats['zero_blockers']+=1;ck(all(t==1 for t in f));continue
 stats['nonzero_blockers']+=1
 lam=[As[i]/(2*s) for i in range(2)]
 coeff=[[F(hs[i][2][Y]*ks[i][2][Z],16) for Y in range(4) for Z in range(4)] for i in range(2)]
 row=[];L={};J={};joint=[]
 for t in range(16):
  a,b=coeff[0][t],coeff[1][t];den=a*a+b*b
  rt=den/(2*s);row.append(rt)
  q0=(a+b)**2/(4*s);q1=(a-b)**2/(4*s);joint.extend([q0,q1])
  ck(q0+q1==rt)
  if den:
   L=add((1,L),(rt,binary(b*b/den)))
   J=add((1,J),(rt,binary((a-b)**2/(2*den))))
 ck(sum(row)==1);ck(sum(joint)==1)
 PC=[F(t*t,1024*s) for t in walsh(C)]
 ck(sorted(PC)==sorted(joint));ck(PC[0]==s)
 ck(joint==[PC[2*Y+8*Z+xi] for Y in range(4) for Z in range(4) for xi in range(2)])
 HC=entropy(PC)
 terminal=add(*[(lam[i],add((1,hs[i][4]),(1,ks[i][4]))) for i in range(2)])
 ck(HC==add((1,terminal),(1,binary(lam[1])),(-1,L),(1,J)))
 ck(sum(joint[1::2])==Ix/(4*s))
 v=4*s*(1-s)
 HF=entropy([F(t*t,1024) for t in fhat])
 ck(HF==add((1,binary(v)),(4*s,HC),(-4*s,binary(s))))
 B=add(*[(ks[i][1]/2,hs[i][5]) for i in range(2)],*[(hs[i][1]/2,ks[i][5]) for i in range(2)])
 D=add((1,binary(v)),(4*s,add((1,binary(lam[1])),(-1,L),(1,J))),(-4*s,binary(s)),
       *[(-ks[i][1]/2,binary(4*hs[i][1]*(1-hs[i][1]))) for i in range(2)],
       *[(-hs[i][1]/2,binary(4*ks[i][1]*(1-ks[i][1]))) for i in range(2)],
       *[(2*As[i],add((1,binary(hs[i][1])),(1,binary(ks[i][1])))) for i in range(2)])
 ck(HF==add((1,B),(1,D)))
 # Full-support reference from exact component spectra, uniform separator bit.
 Q=[rt/2 for rt in row for bit in range(2)]
 ck(sum(Q)==1)
 ck(all(not actual or reference>0 for actual,reference in zip(joint,Q)))
 for ref in (Q,[F(1,32)]*32):
  refrow=[ref[2*t]+ref[2*t+1] for t in range(16)]
  CEC=CE(joint,ref)
  ck(CEC==add((1,CE(row,refrow)),(1,{2:F(1)})))
  ck(add((1,CEC),(-1,HC))==add((1,CE(row,refrow)),(-1,entropy(row)),(1,{2:F(1)}),(-1,J)))
  if s==1:continue
  qe=ref[0]
  Qf=[1-v]+[v*q/(1-qe) for q in ref[1:]]
  Pf=[F(fhat[2*Y+8*Z+xi]**2,1024) for Y in range(4) for Z in range(4) for xi in range(2)]
  ck(sum(Qf)==1);ck(all(not p or q>0 for p,q in zip(Pf,Qf)))
  CEf=CE(Pf,Qf)
  ck(CEf==add((1,binary(v)),(4*s,CEC),(4*s*s,log_vector(qe)),(4*s*(1-s),log_vector(1-qe))))
  Pnon=[p/(1-s) for p in joint[1:]];Qnon=[q/(1-qe) for q in ref[1:]]
  ck(add((1,CEf),(-1,HF))==add((v,CE(Pnon,Qnon)),(-v,entropy(Pnon))))
 if len(samples)<12 and Ix and I:
  samples.append({'h_masks':hp,'k_masks':kp,'s':str(s),'I':str(I),'I_shared':str(Ix),'D_prime_log_coefficients':{str(p):str(c) for p,c in D.items()}})
 if stats['cases']%100==0:
  (R/'out/checkpoint.json').write_text(json.dumps({'stats':stats,'assertions':assertions,'elapsed_seconds':time.monotonic()-start},indent=2)+'\n')
out={'helper':'A014-shared-blocker-v1.2','mode':'pilot' if args.pilot else 'full','stats':stats,'assertions':assertions,'elapsed_seconds':time.monotonic()-start,'entropy_arithmetic':'Rational linear combinations of log2(prime); equality of every coefficient','samples':samples}
(R/('out/pilot.json' if args.pilot else 'out/check.json')).write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='samples'}))
