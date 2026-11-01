from fractions import Fraction as F
from math import comb
from pathlib import Path
from functools import lru_cache
import json,time,argparse
R=Path(__file__).resolve().parents[1]; start=time.monotonic(); checks=0
def ck(b):
 global checks
 assert b
 checks+=1
def transform(vals,p):
 a=list(map(F,vals));n=len(p)
 for i,q in enumerate(p):
  z=1<<i
  for base in range(0,len(a),2*z):
   for j in range(z):
    l,h=a[base+j],a[base+j+z]
    a[base+j]=(1-q)*l+q*h;a[base+j+z]=h-l
 mass=[];v=[]
 for s,x in enumerate(a):
  factor=F(1)
  for i,q in enumerate(p):
   if s>>i&1:factor*=q*(1-q)
  mass.append(x*x*factor);v.append(factor*4**s.bit_count())
 return a,mass,v
def delta(m):return sum((s.bit_count()-1)*p for s,p in enumerate(m) if s)
def binom(n,k):return comb(n,k) if 0<=k<=n else 0
@lru_cache(maxsize=10000)
def ln(x):
 x=F(x);k=0
 while x>=2:x/=2;k+=1
 while x<1:x*=2;k-=1
 def part(y):
  z=(y-1)/(y+1);a=2*sum((z**(2*j+1)/F(2*j+1) for j in range(24)),F(0))
  return a,a+2*z**49/(49*(1-z*z))
 a,b=part(x);l,u=part(F(2))
 return (a+k*l,b+k*u) if k>=0 else (a+k*u,b+k*l)
def outward(interval):
 a,b=interval;z=1<<80
 return [str(F((a*z).__floor__(),z)),str(F((b*z).__ceil__(),z))]
def entropy(m,v,pred=lambda s:bool(s)):
 a=b=F(0)
 for s,p in enumerate(m):
  if p and pred(s):
   l,u=ln(v[s]/p);a+=p*l;b+=p*u
 return a,b
pilot=argparse.ArgumentParser();pilot.add_argument('--pilot',action='store_true');args=pilot.parse_args()
rmax=3 if args.pilot else 12
rows=[]
for r in range(1,rmax+1):
 n=4*r+1;k0=(n+1)//2; coeff=[]
 for k in range(n+1):
  numerator=sum(sum((-1)**(k-l)*binom(k,l)*binom(n-k,j-l) for l in range(k+1)) for j in range(k0,n+1))
  # Constant sign -1 contributes only at empty set.
  c=F(2*numerator,2**n)-(1 if k==0 else 0);coeff.append(c)
 ck(coeff[0]==0);ck(sum(comb(n,k)*c*c for k,c in enumerate(coeff))==1)
 ck(abs(coeff[2*r+1])==F(comb(2*r,r),2**(4*r)))
 influence=sum(k*comb(n,k)*c*c for k,c in enumerate(coeff))
 ck(influence==F(n*comb(n-1,(n-1)//2),2**(n-1)))
 l1=sum(comb(n,k)*abs(c) for k,c in enumerate(coeff));source=l1/4;rootD=influence/2
 lower=F(2**(2*r),2*(4*r+1)*(2*r+1)**2)
 ck(source/rootD>=lower)
 eglo=eghi=mlo=mhi=F(0)
 for k,c in enumerate(coeff):
  if k and c:
   p=c*c; multiplicity=comb(n,k);l,u=ln(1/p)
   eglo+=multiplicity*p*l;eghi+=multiplicity*p*u
   pm=p/4;l,u=ln(1/pm);mlo+=multiplicity*pm*l;mhi+=multiplicity*pm*u
   ck(F(1,1)/pm==4/p) # exact log-factor identity
 ln4=ln(F(4));ck(mlo<=(eghi+ln4[1])/4 and (eglo+ln4[0])/4<=mhi)
 # The analytic identity is proved in COFACTOR_REFERENCE.md; intervals corroborate.
 if r<=2:
  weights=[n+1,n+1]+[1]*n;t=n+1+k0;dimension=n+2
  vals=[2*int(sum(w for i,w in enumerate(weights) if x>>i&1)>=t)-1 for x in range(1<<dimension)]
  _,mass,v=transform(vals,[F(1,2)]*dimension)
  ck(sum(mass)==1);ck(delta(mass)==rootD)
  M=sum(p for s,p in enumerate(mass) if s&3 and s>>2)
  dm=sum((s.bit_count()-1)*p for s,p in enumerate(mass) if s&3 and s>>2)
  ck(M==F(1,4));ck(dm==(influence+1)/4)
  for s,p in enumerate(mass):
   a=s&3;z=s>>2
   if z:ck(p==(coeff[z.bit_count()]**2/4 if a in (0,3) else 0))
 rows.append({'r':r,'n_B':n,'w':n+1,'threshold':n+1+k0,'I_majority':str(influence),'root_Delta':str(rootD),'L1_majority':str(l1),'B_abs_over_Delta':str(source/rootD),'proved_lower_bound':str(lower),'E_mixed_over_Delta_mixed_nats_interval':outward((4*mlo/(influence+1),4*mhi/(influence+1)))})
 if time.monotonic()-start>60:raise RuntimeError('pilot/main cap')

# Actual biased physical-cofactor profiles, without a conditional spectral law.
profiles_checked=0;thresholds=0
for h,b in ((2,2),(3,3)):
 if args.pilot and h==3:continue
 for w in (F(1,2),F(2),F(4)):
  for qb in ([F(1,2)]*b,[F(1,4) if i%2==0 else F(3,4) for i in range(b)]):
   for j in range(1,int(2*(w*h+b))+1):
    t=F(j,2);process=[]
    for a in range(h+1):
     vals=[2*int(w*a+x.bit_count()>=t)-1 for x in range(1<<b)]
     c,_,_=transform(vals,qb);process.append([z/F(2)**s.bit_count() for s,z in enumerate(c)])
    for T in range(1,1<<b):
     sequence=[F(0)]+[z[T] for z in process]+[F(0)]
     variation=sum(abs(a-bb) for a,bb in zip(sequence,sequence[1:]));ck(variation<=2)
     ck(sum(abs(process[a+1][T]-process[a][T])/2 for a in range(h))<=1)
     profiles_checked+=1
    thresholds+=1

# Independent source-bound A045 reconstruction on the explicit admission fixtures.
def law(vals,p):
 _,mass,_=transform(vals,p);ck(sum(mass)==1);return tuple(mass)
catalog1={law([1 if mask>>x&1 else -1 for x in range(2)],[F(1,4)]) for mask in range(4)}
catalog2={law([1 if mask>>x&1 else -1 for x in range(4)],[F(1,2)]*2) for mask in range(16)}
ck((F(0),F(1)) not in catalog1)
ck((F(0),F(1,3),F(1,3),F(1,3)) not in catalog2)
ck((F(0),F(1,2),F(0),F(1,2)) not in catalog2)
fixtures=[]
for label,n,h,p,vals in [
 ('biased-OR2',2,1,[F(1,4)]*2,[2*int(x!=0)-1 for x in range(4)]),
 ('fair-AND4',4,2,[F(1,2)]*4,[2*int(x==15)-1 for x in range(16)]),
 ('coupled-phase4',4,2,[F(1,2)]*4,[(2*(x&1)-1)*(2*((x>>2)&1)-1)*(-1)**(((x>>1)&1)*((x>>3)&1)) for x in range(16)]),
 ('unequal-KL5',5,2,[F(1,4)]*5,[2*int(2*(x&3).bit_count()+(x>>2).bit_count()>=3)-1 for x in range(32)])]:
 coefficients,mass,v=transform(vals,p);a={};b={};M=dm=F(0)
 for s,z in enumerate(mass):
  U=s&((1<<h)-1);T=s>>h
  if U and T:
   a[U]=a.get(U,F(0))+z;b[T]=b.get(T,F(0))+z;M+=z;dm+=(s.bit_count()-1)*z
 ck(M>0);ck(dm>=M)
 ck(sum((U.bit_count()+T.bit_count()-1)*aa*bb/(M*M) for U,aa in a.items() for T,bb in b.items())==dm/M)
 tc0=tc1=kl0=kl1=F(0)
 for s,z in enumerate(mass):
  U=s&((1<<h)-1);T=s>>h
  if U and T and z:
   d=s.bit_count()-1;lik=z*M/(a[U]*b[T]);ck((d*z/dm)/(d*a[U]*b[T]/(M*dm))==lik)
   l,u=ln(lik);tc0+=z/M*l;tc1+=z/M*u;kl0+=d*z/dm*l;kl1+=d*z/dm*u
 if label=='unequal-KL5':ck(kl1-tc0<0)
 if label=='biased-OR2':ck(M==F(9,64));ck(tuple(a.get(U,0)/M for U in range(2))==(0,1))
 if label=='fair-AND4':ck(M==F(9,64));ck(all(aa/M==F(1,3) for aa in a.values()));ck(all(aa*bb/(M*M)==F(1,9) for aa in a.values() for bb in b.values()))
 if label=='coupled-phase4':
  ck(M==1);ck(all(z in (0,F(1,4)) for z in mass));ck(tc0==tc1==0)
  ck(all(z==a.get(s&3,0)*b.get(s>>2,0) for s,z in enumerate(mass)))
  C=lambda U,T:coefficients[U|(T<<2)]/F(2)**(U.bit_count()+T.bit_count())
  ck(C(1,1)*C(3,3)-C(1,3)*C(3,1)!=0)
 fixtures.append({'label':label,'M':str(M),'Delta_mixed':str(dm),'TC_spec_interval':outward((tc0,tc1)),'degree_KL_minus_TC_interval':outward((kl0-tc1,kl1-tc0))})
out={'helper':'A041-stage4-v1.1','pilot':args.pilot,'assertions':checks,'cofactor_family_cases':len(rows),'truth_table_family_reconstructions':2,'threshold_cases':thresholds,'coefficient_profiles':profiles_checked,'Boolean_catalog_tables':20,'admission_fixtures':fixtures,'cofactor_obstruction_certificates':rows,'runtime_seconds':time.monotonic()-start}
(R/('out/PILOT.json' if args.pilot else 'out/EXACT_CHECKS.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ('admission_fixtures','cofactor_obstruction_certificates')},indent=2))
