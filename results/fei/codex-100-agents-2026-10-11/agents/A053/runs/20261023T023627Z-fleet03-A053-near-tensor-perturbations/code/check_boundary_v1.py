from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,time,hashlib
import arithmetic as a
RUN=Path(__file__).resolve().parents[1]; start=time.perf_counter(); checks=0

def check(v):
 global checks
 checks+=1
 assert v, checks
 if time.perf_counter()-start>55: raise RuntimeError('55-second frozen guard')
def save(n,v): (RUN/'out'/n).write_text(json.dumps(v,indent=2)+'\n',encoding='utf-8')
def profile(r,N,kind='h',edit=True):
 m=2*r;t=F(1,2**r);d=t*t;z=F(2,2**N) if edit else F(0);cp=(2**m+2**r)//2;cm=(2**m-2**r)//2
 if kind=='h': return [(t-d-z,cp),(-t-d-z,cm),(d-z,2**m),(-z,2**N-2**(m+1))]
 if kind=='gp': return [(t-2*d,cp),(-t-2*d,cm)]
 return [(t-z,cp),(-t-z,cm),(-z,2**N-2**m)]
def hist(p):
 c=Counter()
 for v,k in p:
  if k and v:c[v*v]+=k
 return c
def H(p):
 check(sum(v*v*k for v,k in p)==1)
 lo=hi=F(0)
 for v,k in p:
  if v and k:
   l,u=a.log2(v*v);lo-=k*v*v*u;hi-=k*v*v*l
 return lo,hi
def sub(x,y): return x[0]-y[1],x[1]-y[0]
def plus(x,y):return x[0]+y[0],x[1]+y[1]
def scale(x,c):return x[0]*c,x[1]*c
def bank(L,Q):return L[0]-9*Q,L[1]-9*Q

def actual(r):
 m=2*r;n=3*(m+1);N=1<<n;p=F(1,N)
 def g(y): return -1 if sum(((y>>(2*j))&1)*((y>>(2*j+1))&1) for j in range(r))%2 else 1
 seed=[]
 for x in range(N):
  y=sum((((x>>(3*j))&7).bit_count()%2)<<j for j in range(m+1));v=g(y&((1<<m)-1))
  if y>>m and (y&((1<<m)-1))==0:v=-v
  seed.append(v)
 edited=seed.copy();edited[0]*=-1
 sf=a.fwht(seed);ef=a.fwht(edited)
 check(all(v in (-1,1) for v in edited));check(sum(v<0 for v in seed)%2==0);check(sum(v<0 for v in edited)%2==1)
 support=[s for s,v in enumerate(sf) if v]
 for i,s in enumerate(support):
  for u in support[:i]:check((s^u).bit_count()>=3)
 for s,(v,w) in enumerate(zip(sf,ef)):
  check(w==v-2);check(w!=0)
  iscode=all(((s>>(3*j))&7) in (0,7) for j in range(m+1))
  if not iscode:check(v==0)
  else:
   label=sum((1 if ((s>>(3*j))&7)==7 else 0)<<j for j in range(m+1));data=label&((1<<m)-1)
   sigma=-1 if sum(((data>>(2*j))&1)*((data>>(2*j+1))&1) for j in range(r))%2 else 1
   predicted=F(1,2**m) if label>>m else F(sigma,2**r)-F(1,2**m)
   check(F(v,N)==predicted)
 for s in (range(N) if r==1 else [0,1,2,3,7,8,31,63,127,255,511,1023,4095,8191,16383,32767]):
  check(ef[s]==sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(edited)))
 check(Counter(F(v*v,N*N) for v in ef if v)==hist(profile(r,n)))
 inf=a.infs(edited);d=F(1,2**m)
 check(inf==[F(1,2)+d+2*p]*(3*m)+[d-2*p]*3)
 check(sum(inf)==F(3*m,2)+3*(m+1)*d+6*(m-1)*p)
 prefix=[];leaves=[];mask=(1<<(3*m))-1
 for b in range(4):
  leaf=[edited[(x&mask)|(b<<(3*m))|((x>>(3*m))<<(3*m+2))] for x in range(1<<(n-2))]
  w=a.fwht(leaf);cnt=Counter(F(v*v,len(leaf)**2) for v in w if v)
  check(cnt==hist(profile(r,n-2,edit=(b==0))))
  prefix.append(H([(F(v,len(leaf)),c) for v,c in Counter(w).items()]))
 for b in range(8):
  leaf=edited[b<<(3*m):(b+1)<<(3*m)];w=a.fwht(leaf);cnt=Counter(F(v*v,len(leaf)**2) for v in w if v)
  typ='gp' if b.bit_count()%2 else 'g'
  check(cnt==hist(profile(r,3*m,kind=typ,edit=(b==0))))
  leaves.append(H([(F(v,len(leaf)),c) for v,c in Counter(w).items()]))
 return {'r':r,'n':n,'truth_sha256':hashlib.sha256(bytes(v==1 for v in edited)).hexdigest(),'full_spectrum_and_all_terminals':'PASS','direct_Walsh_labels':N if r==1 else 16}

physical=[actual(r) for r in [1,2]]; save('PHYSICAL_CHECK.json',physical)
rows=[]
for r in range(1,17):
 m=2*r;n=3*(m+1);p=F(1,2**n);d=F(1,2**m)
 root=H(profile(r,n));h=H(profile(r,m+1,edit=False));mid=H(profile(r,n-2));gp=H(profile(r,m,kind='gp'));ge=H(profile(r,3*m,kind='g'))
 L2=sub(root,scale(plus(mid,scale(h,3)),F(1,4)))
 L3=sub(root,scale(plus(ge,plus((F(3*m),F(3*m)),scale(gp,4))),F(1,8)))
 B2=bank(L2,2*d-4*p);B3=bank(L3,3*d-6*p)
 check(B2[1]<-p/2)
 if r>=7:
  check(90*r+37<8*2**r);check(L3[0]>(2*r-3)*d)
 if r==16:check(B3[0]>2*d)
 rows.append({'r':r,'n':n,'B2_over_p_upper':str(B2[1]/p),'B3_over_d_lower':str(B3[0]/d),'L3_over_d_lower':str(L3[0]/d),'B2_negative':True,'B3_positive_certified':B3[0]>0})
save('COMPRESSED_CERTIFICATES.json',rows)
save('EXACT_CHECK.json',{'status':'PASS','assertions':checks,'physical_r':[1,2],'compressed_r':list(range(1,17)),'r16_n99_same_K9_bank_gt_2d':True,'runtime_seconds':time.perf_counter()-start,'arithmetic':'integer Walsh and physical edges, exact Fraction and rational logarithm intervals; no floating sign tests'})
print((RUN/'out/EXACT_CHECK.json').read_text(encoding='utf-8'))
