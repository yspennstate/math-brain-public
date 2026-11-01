from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import math,json,time,sys,itertools
ROOT=Path(__file__).resolve().parents[1];START=time.perf_counter();PILOT='--pilot' in sys.argv;checks=0
def ck(v):
 global checks
 checks+=1;assert v,checks
 assert time.perf_counter()-START<(60 if PILOT else 180)
def prod(xs):
 z=Q(1)
 for x in xs:z*=x
 return z
def transform(tab,ps):
 c=list(map(Q,tab));n=len(ps)
 for i,p in enumerate(ps):
  for s in range(1<<n):
   if s>>i&1:continue
   a,b=c[s],c[s|(1<<i)];c[s]=(1-p)*a+p*b;c[s|(1<<i)]=(b-a)/2
 vi=[4*p*(1-p) for p in ps];vs=[prod(vi[i] for i in range(n) if s>>i&1) for s in range(1<<n)];P=[a*a*b for a,b in zip(c,vs)]
 ck(sum(P)==1);return c,P,vs
def add(a,b):return a[0]+b[0],a[1]+b[1]
def scale(a,w):return (a[0]*w,a[1]*w) if w>=0 else (a[1]*w,a[0]*w)
@lru_cache(None)
def core(x):
 z=(x-1)/(x+1);term=z;lo=Q(0)
 for j in range(24):lo+=2*term/(2*j+1);term*=z*z
 return lo,lo+2*term/(49*(1-z*z))
@lru_cache(None)
def ln(x):
 assert x>0;k=0
 while x<1:x*=2;k-=1
 while x>=2:x/=2;k+=1
 iv=add(core(x),scale(core(Q(2)),k));den=10**24
 return Q(iv[0].numerator*den//iv[0].denominator,den),Q(-((-iv[1].numerator*den)//iv[1].denominator),den)
def h(x):return (Q(0),Q(0)) if not x else scale(ln(1/(x*x)),x*x)
def kap(x):
 t=abs(x)
 return (Q(0),Q(0)) if not 0<t<1 else scale(ln(1/t),2*t/(1-t))
def enc(x):return [str(x[0]),str(x[1])]
def physical_profile(tab,n,S,ps):
 sel=[i for i in range(n) if S>>i&1];other=[i for i in range(n) if not S>>i&1];mean=second=Q(0)
 for x in range(1<<len(other)):
  base=sum(((x>>j)&1)<<i for j,i in enumerate(other));wt=prod(ps[i] if x>>j&1 else 1-ps[i] for j,i in enumerate(other))
  twice=sum((-1)**(len(sel)-b.bit_count())*tab[base|sum(((b>>j)&1)<<i for j,i in enumerate(sel))] for b in range(1<<len(sel)))
  ck(twice%2==0);z=Q(twice,2);mean+=wt*z;second+=wt*z*z
 return mean,second-mean*mean
profiles=0;cases=0;degree3=0
plans=[]
for n in ([2] if PILOT else [2,3]):
 laws=[[Q(1,2)]*n,[Q(1,3),Q(2,3)] if n==2 else [Q(1,3),Q(1,2),Q(2,3)]]
 if n==2:laws.append([Q(2,3)]*n)
 for mask in range(1<<(1<<n)):
  tab=[1 if mask>>x&1 else -1 for x in range(1<<n)]
  for ps in laws:plans.append((n,mask,tab,ps))
parity=[(-1)**x.bit_count() for x in range(16)];edited=parity.copy();edited[0]*=-1
for tab in [parity,edited,[1 if 56067>>x&1 else -1 for x in range(16)]]:
 for ps in [[Q(1,2)]*4,[Q(1,3)]*4,[Q(1,4),Q(1,3),Q(1,2),Q(3,4)],[Q(3,4),Q(2,3),Q(1,3),Q(1,4)]]:plans.append((4,sum((a==1)<<x for x,a in enumerate(tab)),tab,ps))
with (ROOT/'out'/('PILOT_CASES.jsonl' if PILOT else 'CASES.jsonl')).open('w') as f:
 for n,mask,tab,ps in plans:
  c,P,vs=transform(tab,ps);Delta=sum((s.bit_count()-1)*p for s,p in enumerate(P) if s);Es=(Q(0),Q(0));packet=Q(0);pair=Q(0)
  for S in range(1,1<<n):
   k=S.bit_count();m,var=physical_profile(tab,n,S,ps);strict=sum(P[T] for T in range(1<<n) if T!=S and T&S==S)
   ck(m==2**(k-1)*c[S]);ck(var==Q(4**(k-1))*strict/vs[S])
   hm=h(m);ck(hm[1]<=2*var or m==0 or abs(m)==1)
   if 0<abs(m)<1:
    ck(var>=abs(m)*(1-abs(m)));coef=kap(m);ck(hm[1]<=scale(coef,var)[0] or var==abs(m)*(1-abs(m)))
   E=scale(h(c[S]),vs[S]);Es=add(Es,E)
   rhs=add(scale(ln(Q(4)),(k-1)*P[S]),(2*strict,2*strict));ck(E[1]<=rhs[0] or strict==0 or not P[S])
   packet+=2*strict
   if k==2:pair+=2*strict
   profiles+=1
  ck(packet==2*sum((2**s.bit_count()-2)*p for s,p in enumerate(P) if s))
  ck(pair==2*sum(math.comb(s.bit_count(),2)*p for s,p in enumerate(P) if s.bit_count()>=3))
  deg=max(s.bit_count() for s,p in enumerate(P) if p)
  if deg<=3:
   degree3+=1;bound=add((6*Delta,6*Delta),scale(ln(Q(4)),Delta));ck(Es[1]<=bound[0] or Delta==0)
  row={'n':n,'mask':mask,'ps':[str(p) for p in ps],'Delta':str(Delta),'degree':deg,'raw_pair_ledger':str(pair)};f.write(json.dumps(row)+'\n');f.flush();cases+=1
  (ROOT/'out'/('PILOT_CHECKPOINT.json' if PILOT else 'CHECKPOINT.json')).write_text(json.dumps({'cases':cases,'assertions':checks}))

admission=[]
for p in [Q(1,64),Q(1,8),Q(1,3),Q(1,2),Q(3,4),Q(63,64)]:
 tab=[1 if x==7 else -1 for x in range(8)];ps=[Q(1,2),Q(1,2),p];m,var=physical_profile(tab,3,3,ps);ck(m==p);ck(var==p*(1-p))
 admission.append({'controller_bias':str(p),'mean':str(m),'variance':str(var),'h_equals_kappa_variance':'exact log identity'})

family=[]
for r in (range(1,3) if PILOT else range(1,9)):
 n=16*r*r;m=n//2
 def g(k):return 1 if k<=m-r or k>=m+r else -1
 den=2**n;Eg=Q(sum(math.comb(n,k)*g(k) for k in range(n+1)),den)
 top=Q(sum(math.comb(n,k)*g(k)*(-1)**k for k in range(n+1)),den)
 b=Q(math.comb(n-1,m-r),2**(n-1));central=Q(math.comb(n-1,m-1),2**(n-1));c=2*(2*r-1)*b/(n-1)
 pairdirect=Q(sum(math.comb(n-2,k)*(g(k+2)-2*g(k+1)+g(k)) for k in range(n-1)),4*2**(n-2));ck(pairdirect==c)
 ck(central>=Q(1,12*r));ck(b/central>=Q(3,4));ck(Q(1,8*(n-1))<=c<=Q(2,n-1))
 # All actual complementary pair cofactors, compressed by count and selector.
 mean=second=Q(0)
 for k in range(n-1):
  wt=Q(math.comb(n-2,k),2**(n-2));zg=Q(g(k+2)-2*g(k+1)+g(k),2);zp=2*(-1)**k
  ck(zg.denominator==1);mean+=wt*(zg+zp)/2;second+=wt*(zg*zg+zp*zp)/2
 ck(mean==c);var=second-c*c;strict=var/4
 # Two full-data Fourier packets are distinct and contain every data pair strictly.
 top0=(1+top)**2/4;top1=(1-top)**2/4;ck(top0+top1==(1+top*top)/2);ck(strict>=top0+top1>=Q(1,2))
 Ig=2*n*b
 # Independent physical g edge sum and selector disagreement.
 physicalIg=Q(n)*sum(Q(math.comb(n-1,k),2**(n-1))*Q(g(k+1)-g(k),2)**2 for k in range(n));ck(Ig==physicalIg)
 selector=Q(sum(math.comb(n,k)*(g(k)!=(-1)**k) for k in range(n+1)),den);ck(selector==(1-top)/2)
 I=(Q(n)+Ig)/2+selector;V=1-(Eg/2)**2;D=I-V;ck(Q(n,2)<=I<=n+Q(1,2));ck(0<D<=n+Q(1,2))
 bill=scale(kap(c),math.comb(n,2)*strict);ratio=scale(bill,1/D);lower=scale(ln(Q(n-1,2)),Q(1,24));ck(ratio[0]>=lower[1])
 row={'r':r,'n_data':n,'pair_mean':str(c),'central_probability':str(central),'boundary_probability':str(b),'g_mean':str(Eg),'g_top_coefficient':str(top),'g_influence':str(Ig),'root_influence':str(I),'root_variance':str(V),'root_deficit':str(D),'pair_profile_variance':str(var),'strict_superset_mass_per_pair':str(strict),'top_packets_combined_mass':str(top0+top1),'mean_refunded_pair_bill':enc(bill),'bill_over_deficit':enc(ratio),'proved_divergent_lower':enc(lower),'ordinary_H_over_I_upper':str(Q(2)+Q(2,n))}
 family.append(row)
 (ROOT/'out'/('PILOT_FAMILY.json' if PILOT else 'FAMILY.json')).write_text(json.dumps(family,indent=2)+'\n')
out={'status':'PASS','pilot':PILOT,'gate_cases':cases,'integer_profiles':profiles,'degree_le_three_cases':degree3,'scalar_Boolean_admission_cases':len(admission),'selector_family_cases':len(family),'assertions':checks,'scalar_admission':admission,'runtime_seconds':time.perf_counter()-START}
(ROOT/'out'/('PILOT.json' if PILOT else 'CHECK_OUTPUT.json')).write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2));print(json.dumps({'first_n':family[0]['n_data'],'first_ratio':family[0]['bill_over_deficit'],'last_n':family[-1]['n_data'],'last_ratio':family[-1]['bill_over_deficit']}))
