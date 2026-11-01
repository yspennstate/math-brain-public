import itertools, json, math, sys, time
from fractions import Fraction as F
from pathlib import Path

RUN=Path(__file__).resolve().parents[1]
START=time.monotonic(); checks=0; B=24; DEN=1<<B
def ck(v):
 global checks
 assert v
 checks+=1
 if checks%200==0 and time.monotonic()-START>55: raise RuntimeError('frozen runtime limit')
def theta(s,r):
 if r<=s:return DEN,DEN
 target=s**6*DEN**5; factor=r**6
 lo,hi=0,DEN
 while hi-lo>1:
  mid=(lo+hi)//2
  if mid**5*factor<=target:lo=mid
  else:hi=mid
 ck(lo**5*factor<=target<=hi**5*factor)
 return lo,hi
def es(vals,s):
 a=[1]+[0]*s
 for v in vals:
  for j in range(s,0,-1):a[j]+=a[j-1]*v
 return a[s]
def mask(xs):return sum(1<<x for x in xs)
def fwht(a):
 a=a[:];step=1
 while step<len(a):
  for st in range(0,len(a),2*step):
   for i in range(st,st+step):u,v=a[i],a[i+step];a[i],a[i+step]=u+v,u-v
  step*=2
 return a
def one(k):
 m=2*k;n=2*m;W=m;size=1<<n;N=math.comb(m,k)**2
 pi=F(1,1<<W);activity=pi/N;D=(1+activity)**N-1
 ck(pi<=D<=2*pi)
 gates=[tuple(x)+tuple(y) for x in itertools.combinations(range(m),k) for y in itertools.combinations(range(m,n),k)]
 tw={s:[theta(s,r) for r in range(1,W+1)] for s in range(1,W+1)}
 zs={s:(es([x[0] for x in tw[s]],s),es([x[1] for x in tw[s]],s)) for s in tw}
 for s,(lo,hi) in zs.items():ck(hi<=18**s*DEN**s)
 sumslo=[0]*size;sumshi=[0]*size;counts=[0]*size;events=0
 for g in gates:
  for loc in range(1,1<<W):
   s=loc.bit_count();inds=[i for i in range(W) if loc>>i&1];a=mask(g[i] for i in inds)
   sumslo[a]+=math.prod(tw[s][i][0] for i in inds)
   sumshi[a]+=math.prod(tw[s][i][1] for i in inds)
   counts[a]+=1;events+=1
 truth=[2*int((x&((1<<m)-1)).bit_count()>=k and (x>>m).bit_count()>=k)-1 for x in range(size)]
 walsh=fwht(truth);p=[F(z*z,size*size) for z in walsh]
 ck(sum(p)==1)
 I=sum(p[a]*a.bit_count() for a in range(size))
 pivotal=F(sum(truth[x]!=truth[x^(1<<i)] for x in range(size) for i in range(n)),size)
 ak=F(math.comb(m,k),1<<m);q=(1+ak)/2
 ck(I==pivotal==2*q*m*ak);ck(I>=1)
 if k<=2:
  for a in range(size):ck(walsh[a]==sum(truth[x]*(-1 if (a&x).bit_count()%2 else 1) for x in range(size)))
 g0=tuple(range(k))+tuple(range(m,m+k));g1=tuple(range(k,m))+tuple(range(m+k,n))
 def visit(g,a):
  inds=[i for i,j in enumerate(g) if a>>j&1];s=len(inds);ck(s>0)
  return F(math.prod(tw[s][i][0] for i in inds),2*s*(s+1)*zs[s][1]),F(math.prod(tw[s][i][1] for i in inds),2*s*(s+1)*zs[s][0])
 total_upper=F(0);good=bad=0;badmass=F(0);orbits={}
 for a in range(1,size):
  s=(a&((1<<m)-1)).bit_count();t=(a>>m).bit_count();d=s+t
  orbit=(s,t)
  if orbit in orbits:ck(p[a]==orbits[orbit])
  else:orbits[orbit]=p[a]
  if s<=k and t<=k:
   good+=1;ck(counts[a]==math.comb(m-s,k-s)*math.comb(m-t,k-t))
   lower=activity/D*F(sumslo[a],2*d*(d+1)*zs[d][1])
   upper=activity/D*F(sumshi[a],2*d*(d+1)*zs[d][0])
   # Rational weakening e<3 of the analytic good-event lower bound.
   ck(lower**5 >= F(d,W)**(6*d)/((4*d*(d+1)*108**d)**5))
  else:
   bad+=1;badmass+=p[a];ck(counts[a]==0 and d>=k+1)
   l0,u0=visit(g0,a);l1,u1=visit(g1,a)
   lower=activity**2/D*l0*l1;upper=activity**2/D*u0*u1
   ck(l0>=F(1,1<<(4*W)) and l1>=F(1,1<<(4*W)))
   ck(lower>=F(1,1<<(1+13*m)))
  ck(0<lower<=upper<=1);total_upper+=upper
 ck(total_upper<=1);ck(badmass*(k+1)<=I)
 # Raw independent Bernoulli product recovers the conditioned root event law.
 rootp=activity/(1+activity);normalizer=1-(1-rootp)**N
 ck(rootp*(1-rootp)**(N-1)/normalizer==activity/D)
 ck(rootp**2*(1-rootp)**(N-2)/normalizer==activity**2/D)
 return dict(k=k,n=n,N=N,good_outputs=good,bad_outputs=bad,one_root_events=events,influence=str(I),bad_spectral_mass=str(badmass),checks=checks,elapsed_seconds=time.monotonic()-START)
def review():
 import hashlib
 src=RUN.parents[2]/'A007/runs/20261023T010805Z-fleet03-A007-root-normalization'
 claims=json.loads((src/'CLAIMS.json').read_text(encoding='utf-8'))
 for c in claims:ck(hashlib.sha256(c['exact_statement'].encode()).hexdigest()==c['statement_sha256'])
 vectors=0
 for n in (1,2,3):
  for xs in itertools.product((F(1,8),F(1,2),F(2)),repeat=n):
   A=sum(xs);D=math.prod(1+x for x in xs)-1;vectors+=1
   for i in range(n):
    E=math.prod(1+xs[j] for j in range(n) if j!=i)
    ck(0<=A*E-D<=A*D)
    ck(xs[i]*E/D-xs[i]/A==xs[i]*(A*E-D)/(A*D))
 truth=[2*int((x>>1&1) and ((x&1) or (x>>2&1)))-1 for x in range(8)]
 ck(F(sum(t==1 for t in truth),8)==F(3,8))
 ck(F(sum(truth[x]!=truth[x^(1<<i)] for x in range(8) for i in range(3)),8)==F(5,4))
 implicants=[]
 for face in itertools.product((-1,0,1),repeat=3):
  points=[x for x in range(8) if all(v==-1 or (x>>i&1)==v for i,v in enumerate(face))]
  if all(truth[x]==1 for x in points):implicants.append(face)
 primes=[f for f in implicants if not any(all(g[i]==-1 or g[i]==f[i] for i in range(3)) and sum(v!=-1 for v in g)<sum(v!=-1 for v in f) for g in implicants)]
 ck(set(primes)=={(1,1,-1),(-1,1,1)})
 for j in range(1,65):
  d=F(1,1<<j);x=(d/8,d*d/8);y=(d**3/8,d*d/8);L=sum(x)-sum(y)
  ck(sum(y)/sum(x)==d);ck((d+d*d)/2<=F(3,8));ck(0<L)
  # Exact deficit bound using A007's independently checked |multi-root remainder|<=L.
  lower=F(3,4)*j*(1-d)/(1+d)-F(9,8)*L
  ck(lower>F(3,4)*j-1)
 return {'vectors':vectors,'retuning_parameters':64,'prime_faces':27,'checks':checks,'reviewed_claim_hashes':[c['statement_sha256'] for c in claims]}
if __name__=='__main__':
 mode=sys.argv[1] if len(sys.argv)>1 else 'pilot'
 if mode=='review':result=review()
 else:
  result=[]
  for k in ([1,2] if mode=='pilot' else [1,2,3]):
   result.append(one(k));(RUN/'out'/f'{mode}.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 result={'mode':mode,'results':result,'total_checks':checks,'elapsed_seconds':time.monotonic()-START,'status':'PASS'}
 (RUN/'out'/f'{mode}.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
