from arith import *
from pathlib import Path
from functools import lru_cache
import json,time
R=Path(__file__).resolve().parents[1];t0=time.perf_counter();checks=0
def ck(b):
 global checks
 checks+=1;assert b,checks
 assert time.perf_counter()-t0<55,'runtime cap'
@lru_cache(None)
def lnsmall(x):
 u=(x-1)/(x+1);s=Q(0)
 for k in range(80):s+=2*u**(2*k+1)/Q(2*k+1)
 return s,s+2*u**161/(161*(1-u*u))
@lru_cache(None)
def lnprime(p):
 k=p.bit_length()-1;x=Q(p,1<<k);a,b=lnsmall(x);c,d=lnsmall(Q(2))
 return a+k*c,b+k*d
def positive(v):
 lo=Q(0);hi=Q(0)
 for p,c in v.items():
  a,b=lnprime(p);lo+=c*(a if c>=0 else b);hi+=c*(b if c>=0 else a)
 ck(not v or lo>0)
 # Outward dyadic rounding keeps exact receipts short; sign was tested before rounding.
 scale=1<<80
 lower=(lo.numerator*scale)//lo.denominator
 upper=-((-hi.numerator*scale)//hi.denominator)
 return [str(Q(lower,scale)),str(Q(upper,scale))]
def proj(p,inds):
 return [sum(v for x,v in enumerate(p) if sum(((x>>i)&1)<<j for j,i in enumerate(inds))==s) for s in range(1<<len(inds))]
rows=[]
for r in [1,2]:
 n=3*r;N=1<<n
 truth=[(-1)**sum(((x>>(3*b))&7)==0 for b in range(r)) for x in range(N)]
 # Independent direct-character Fourier calculation.
 coeffs=[Q(sum(truth[x]*(-1)**((x&s).bit_count()) for x in range(N)),N) for s in range(N)]
 p=[x*x for x in coeffs];ck(p==law(truth));ck(sum(p)==1)
 tc=add((n,H([Q(3,4),Q(1,4)])),(-1,H(p)))
 ck(tc=={2:Q(2*r),3:-Q(9*r,8)})
 for kind in ['marginal','two-positive','three-positive','exact']:
  if kind=='exact':
   M=1<<r;w=[Q(1,M)]*M;comps=[]
   for z in range(M):
    qz=[]
    for x in range(N):
     val=Q(1)
     for b in range(r):val*=Q(1,8) if z>>b&1 else int(((x>>(3*b))&7)==0)
     qz.append(val)
    comps.append(qz)
  else:
   M={'marginal':1,'two-positive':2,'three-positive':3}[kind]
   w=[Q(z+1,M*(M+1)//2) for z in range(M)];comps=[]
   for z in range(M):
    us=[Q(1,4) if M==1 else Q(1+(i+z)%3,4) for i in range(n)]
    comps.append([__import__('functools').reduce(lambda a,b:a*b,[(u if x>>i&1 else 1-u) for i,u in enumerate(us)],Q(1)) for x in range(N)])
  q=[sum(w[z]*comps[z][x] for z in range(M)) for x in range(N)]
  ck(sum(q)==1);ck(all(x>0 for x in q))
  if kind=='exact':ck(q==p)
  joint=[[p[x]*w[z]*comps[z][x]/q[x] for x in range(N)] for z in range(M)]
  vz=[sum(row) for row in joint];ck(sum(vz)==1)
  cond=[[v/vz[z] for v in joint[z]] for z in range(M)]
  icond=add((1,H(p)),*[(-vz[z],H(cond[z])) for z in range(M)])
  bitmi=[];localtc={};res={}
  for i in range(n):bitmi.append(add((1,H(proj(p,[i]))),*[(-vz[z],H(proj(cond[z],[i]))) for z in range(M)]))
  for z in range(M):
   localtc=add((1,localtc),(-vz[z],H(cond[z])),*[(vz[z],H(proj(cond[z],[i]))) for i in range(n)])
   res=add((1,res),*[(vz[z],D(proj(cond[z],[i]),proj(comps[z],[i]))) for i in range(n)])
  ck(localtc==add((1,tc),(1,icond),*[(-1,x) for x in bitmi]))
  ck(D(p,q)==add((1,localtc),(1,D(vz,w)),(1,res)))
  contraction=add((2,icond),*[(-1,x) for x in bitmi]);guard=positive(contraction)
  tradeoff=add((1,D(p,q)),(1,icond),(-1,tc));tradeguard=positive(tradeoff)
  cardinal=add((1,D(p,q)),(1,logq(Q(M))),(-1,tc));cardguard=positive(cardinal)
  ck(tradeoff==add((1,contraction),(1,D(vz,w)),(1,res)))
  rows.append({'blocks':r,'kind':kind,'M':M,'weights':w,'KL':D(p,q),'posterior_information':icond,'posterior_entropy':H(vz),'bit_MI':bitmi,'contraction_residual':contraction,'contraction_natural_log_interval':guard,'tradeoff_residual':tradeoff,'tradeoff_natural_log_interval':tradeguard,'cardinality_natural_log_interval':cardguard,'posterior_joint':joint})
  if r==1:
   h=[(-1)**(x&7).bit_count()*truth[x>>3] for x in range(8*N)]
   for sig in [-1,1]:
    parent=wrap(h,sig);pp=law(parent);ck(set(parent)=={-1,1})
    childce={};targets=[]
    for outcome in [0,1]:
     hc=restrict(h,0,outcome);child=restrict(parent,4,outcome);pc=law(child)
     Rc=[Q(0)]*(4*N)
     for s,v in enumerate(q):Rc[4*s+3]=v
     target=reference(hc,Rc,sig);ck(sum(target)==1)
     childce=add((1,childce),(Q(1,2),CE(pc,target)));targets.append(target)
     ck(pc==marginal(pp,4));ck(CE(pc,target)==add((1,H(pc)),(beta,D(p,q))))
    fullbill=add((1,erasure(pp,4)),(1,childce),(-1,H(pp)))
    ck(fullbill==add((beta,D(p,q))));ck(influence(pp,4)==beta)
    ck(erasure(pp,4)=={})
# Independent A079 duplicated-core reconstruction: direct characters, all4 truth tables on1bit
# and the 2bit bent defect, including constants. Six product-mixture fixtures per core.
diagonal=[]
for truth in [[1,1],[-1,-1],[1,-1],[-1,1],[-1,1,1,1]]:
 N=len(truth);n=N.bit_length()-1
 # Physical sign multiplication corresponds to XOR of input bit labels.
 duplicate=[truth[x^y] for y in range(N) for x in range(N)]
 dp=law(duplicate);p=law(truth)
 expected=[p[x] if x==y else Q(0) for y in range(N) for x in range(N)]
 ck(dp==expected)
 for M in [1,2,3]:
  w=[Q(1,M)]*M;ac=[];bc=[]
  for z in range(M):
   aa=[Q(1+(x+z)%3) for x in range(N)];bb=[Q(1+(2*x+z)%4) for x in range(N)]
   ac.append([v/sum(aa) for v in aa]);bc.append([v/sum(bb) for v in bb])
  qdiag=[sum(w[z]*ac[z][x]*bc[z][x] for z in range(M)) for x in range(N)]
  joint=[[p[x]*w[z]*ac[z][x]*bc[z][x]/qdiag[x] for x in range(N)] for z in range(M)]
  vz=[sum(row) for row in joint];cond=[[v/vz[z] for v in joint[z]] for z in range(M)]
  lhs=add((1,CE(p,qdiag)),(-1,H(p)))
  rhs=add((1,D(vz,w)),*[(vz[z],H(cond[z])) for z in range(M)],*[(vz[z],D(cond[z],ac[z])) for z in range(M)],*[(vz[z],D(cond[z],bc[z])) for z in range(M)])
  ck(lhs==rhs)
  I=add((1,H(p)),*[(-vz[z],H(cond[z])) for z in range(M)])
  ck(add((1,lhs),(1,I),(-1,H(p)))==add((1,D(vz,w)),*[(vz[z],D(cond[z],ac[z])) for z in range(M)],*[(vz[z],D(cond[z],bc[z])) for z in range(M)]))
  diagonal.append({'truth':truth,'M':M,'KL':lhs,'posterior_information':I})
out={'PASS':True,'checks':checks,'seconds':time.perf_counter()-t0,'posterior_cases':len(rows),'A079_diagonal_cases':len(diagonal),'A079_reconstruction':diagonal,'decompositions':rows,'formal_status':'NOT_CLAIMED','arithmetic':'Fractions, prime-log coefficient identities and 80-term rational atanh intervals; no float sign decisions'}
(R/'out/independent.json').write_text(json.dumps(enc(out),indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ['decompositions','A079_reconstruction']}))
