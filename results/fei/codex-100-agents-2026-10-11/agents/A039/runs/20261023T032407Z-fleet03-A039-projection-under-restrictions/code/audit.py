"""Independent literal-Walsh / exact prime-log reconstruction. No checker import."""
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import json,time

START=time.monotonic();N=0;R=Path(__file__).resolve().parents[1]
def verify(a,msg):
    global N
    N+=1
    assert a,msg
    assert time.monotonic()-START<55,'audit frozen runtime guard'
def walsh(values):
    n=len(values)
    return [Q(sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(values)),n) for s in range(n)]
def prob(values):return [a*a for a in walsh(values)]
def residual(i,j):return (i&((1<<j)-1))|((i>>(j+1))<<j)
def fold(values,j):
    out=[Q(0)]*(len(values)//2)
    for i,a in enumerate(values):out[residual(i,j)]+=a
    return out
def child(values,j,y):return [v for i,v in enumerate(values) if (i>>j)&1==y]
def pointlaw(w,beta):
    vals=[-1]+[1]*((1<<w)-1);p=prob(vals)
    if w==1:return p
    out=list(p)
    for i in range(1,len(p)):out[i]=beta*p[i]
    out[-1]+=(1-beta)*(1-p[0])
    return out
def product(a,b):return [x*y for y in b for x in a]
def outer(values,data):
    p=prob(values)
    return [p[i] if i<2 else data[i//2]/4 for i in range(len(p))]
@lru_cache(None)
def factor_integer(k):
    assert k>0
    out={};d=2
    while d*d<=k:
        while k%d==0:out[d]=out.get(d,0)+1;k//=d
        d=3 if d==2 else d+2
    if k>1:out[k]=out.get(k,0)+1
    return out
def addlog(out,x,c):
    for sign,k in [(1,x.numerator),(-1,x.denominator)]:
        for p,e in factor_integer(k).items():out[p]=out.get(p,Q(0))+c*sign*e
def kl(p,q):
    out={}
    for a,b in zip(p,q):
        if a:addlog(out,a/b,a)
    return {p:c for p,c in out.items() if c}
def combine(terms):
    out={}
    for scalar,expr in terms:
        for p,c in expr.items():out[p]=out.get(p,Q(0))+scalar*c
    return {p:c for p,c in out.items() if c}
results=[]
for w in [2,3,4]:
  for epsilon in [-1,1]:
    for sign in [-1,1]:
      # Queried factor first, one width-two spectator; x is frequency bit0.
      vals=[]
      for x in range(1<<(w+3)):
          v=-1 if ((x>>1)&((1<<w)-1))==0 else 1
          u=-1 if (x>>(w+1))==0 else 1
          vals.append(epsilon if x&1==0 else sign*v*u)
      p=prob(vals);pv=pointlaw(w,Q(1));pu=pointlaw(2,Q(1))
      qv=pointlaw(w,Q(5,6));qu=pointlaw(2,Q(5,6))
      ref=outer(vals,product(qv,qu));j=1;pp=fold(p,j);rr=fold(ref,j)
      lv=[qv[i]/pv[i] for i in range(len(pv))]
      B=[a*lv[(i>>1)&((1<<w)-1)] for i,a in enumerate(p)]
      bb=fold(B,j);outs=[];direct=[];newprice=[];fullterms=[]
      verify(sum(B)==1,'normalized isolated-factor reference')
      for y in [0,1]:
          cv=child(vals,j,y);cp=prob(cv)
          kernel=[a/(2*b) if b else Q(1,2) for a,b in zip(cp,pp)]
          raw=[a*b for a,b in zip(rr,kernel)];rho=sum(raw);outs.append(rho)
          old=[a/rho for a in raw]
          if y==1:
              fp=[Q(1)]+[Q(0)]*((1<<(w-1))-1);fq=fp
          else:fp=pointlaw(w-1,Q(1));fq=pointlaw(w-1,Q(4,5))
          new=outer(cv,product(fq,qu))
          direct.extend([(Q(1,2),kl(cp,new)),(-Q(1,2),kl(cp,old))])
          newprice.append((Q(1,4),kl(fp,fq)))
          verify(sum(old)==1 and sum(new)==1,'complete inherited and fresh laws normalized')
          verify(rho>=Q(5,12),'outcome lower bound')
      directexpr=combine(direct)
      rhsexpr=combine(newprice+[(-Q(1),kl(pp,bb)),(Q(1),kl([Q(1,2)]*2,outs))])
      verify(directexpr==rhsexpr,'exact PRIME-LOG equality: full reset = factor/2 - erasedKL + outcomeKL')
      results.append({'w':w,'epsilon':epsilon,'core_sign':sign,'outcomes':list(map(str,outs)),'identity_prime_log_terms':{str(p):str(c) for p,c in directexpr.items()},'nonfair':outs[0]!=Q(1,2)})
out={'status':'PASS','independent_of_checker':True,'method':'literal Walsh sums, posterior matrix construction, exact rational coefficients of independently factored prime logarithms','checks':N,'cases':len(results),'nonfair_cases':sum(r['nonfair'] for r in results),'runtime_seconds':time.monotonic()-START,'results':results,'review_status':'Separate author implementation; NOT external independent acceptance.'}
(R/'out/AUDIT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='results'}))
