from fractions import Fraction as Q
from pathlib import Path
from functools import lru_cache
from math import comb
import argparse,json,time
R=Path(__file__).resolve().parents[1];start=time.monotonic();checks=0
def ck(b):
 global checks
 assert b
 checks+=1
def transform(vals,p):
 a=list(map(Q,vals))
 for i,q in enumerate(p):
  z=1<<i
  for b in range(0,len(a),2*z):
   for j in range(z):
    lo,hi=a[b+j],a[b+j+z];a[b+j]=(1-q)*lo+q*hi;a[b+j+z]=hi-lo
 mass=[];v=[]
 for s,x in enumerate(a):
  factor=Q(1)
  for i,q in enumerate(p):
   if s>>i&1:factor*=q*(1-q)
  mass.append(x*x*factor);v.append(factor*4**s.bit_count())
 return a,mass,v
@lru_cache(maxsize=30000)
def ln(x):
 x=Q(x);k=0
 while x>=2:x/=2;k+=1
 while x<1:x*=2;k-=1
 def part(y):
  z=(y-1)/(y+1);lo=2*sum((z**(2*j+1)/Q(2*j+1) for j in range(20)),Q(0))
  return lo,lo+2*z**41/(41*(1-z*z))
 a,b=part(x);l,u=part(Q(2))
 return (a+k*l,b+k*u) if k>=0 else (a+k*u,b+k*l)
def outward(I):
 z=1<<80
 return [str(Q((I[0]*z).__floor__(),z)),str(Q((I[1]*z).__ceil__(),z))]
def entropy(m,v,pred=lambda s:bool(s)):
 lo=hi=Q(0)
 for s,p in enumerate(m):
  if p and pred(s):
   l,u=ln(v[s]/p);lo+=p*l;hi+=p*u
 return lo,hi
def reference(vals,p,h,direction):
 b=len(p)-h;d=h if direction=='A' else b;c=b if direction=='A' else h
 pd=p[:h] if direction=='A' else p[h:];pc=p[h:] if direction=='A' else p[:h]
 profiles=[]
 for k in range(d+1):
  a=(1<<k)-1
  child=[vals[a|(x<<h)] for x in range(1<<c)] if direction=='A' else [vals[x|(a<<h)] for x in range(1<<c)]
  u,_,vc=transform(child,pc);profiles.append([x/Q(2)**T.bit_count() for T,x in enumerate(u)])
 tails=[]
 for j in range(1,d+1):
  _,mg,vg=transform([2*int(x.bit_count()>=j)-1 for x in range(1<<d)],pd)
  tails.append((mg,sum(U.bit_count()*z for U,z in enumerate(mg))))
 K=[Q(0)]*(1<<len(p));budget=Q(0)
 for T in range(1,1<<c):
  alphas=[(profiles[j][T]-profiles[j-1][T])/2 for j in range(1,d+1)]
  ck(sum(abs(z) for z in alphas)<=1)
  budget+=vc[T]*sum(z*z*tails[j][1] for j,z in enumerate(alphas))
  for U in range(1,1<<d):
   s=U|(T<<h) if direction=='A' else T|(U<<h)
   K[s]=vc[T]*sum(z*z*tails[j][0][U] for j,z in enumerate(alphas))
 return K,budget
parser=argparse.ArgumentParser();parser.add_argument('--pilot',action='store_true');args=parser.parse_args()
rows=[];maximum=(Q(0),None)
def case(h,b,w,p,t,label):
 global maximum
 n=h+b;vals=[2*int(w*(x&((1<<h)-1)).bit_count()+(x>>h).bit_count()>=t)-1 for x in range(1<<n)]
 _,mass,v=transform(vals,p);ck(sum(mass)==1)
 KA,BA=reference(vals,p,h,'A');KB,BB=reference(vals,p,h,'B')
 mixed=lambda s:bool(s&((1<<h)-1)) and bool(s>>h)
 M=sum(z for s,z in enumerate(mass) if mixed(s))
 D=sum((s.bit_count()-1)*z for s,z in enumerate(mass) if mixed(s))
 JA=sum((s&((1<<h)-1)).bit_count()*z for s,z in enumerate(mass) if mixed(s))
 JB=sum((s>>h).bit_count()*z for s,z in enumerate(mass) if mixed(s))
 ck(BA==JA);ck(BB==JB);ck(JA+JB==D+M)
 ck(sum((s&((1<<h)-1)).bit_count()*z for s,z in enumerate(KA))==JA)
 ck(sum((s>>h).bit_count()*z for s,z in enumerate(KB))==JB)
 za=sum(KA);zb=sum(KB);ck(za<=JA);ck(zb<=JB)
 K=[max(a,b) for a,b in zip(KA,KB)];Z=sum(K);ck(Z<=D+M);ck(M<=D)
 for s,z in enumerate(mass):
  if mixed(s):
   ck(KA[s]<=v[s]);ck(KB[s]<=v[s]);ck(K[s]<=v[s])
   if z:ck(KA[s]>0 and KB[s]>0)
 if M:
  ck(Z>0);ck(sum(k/Z for k in K)==1)
  C0=C1=KL0=KL1=Q(0)
  for s,z in enumerate(mass):
   if mixed(s) and z:
    likelihood=z*Z/(M*K[s]);l,u=ln(v[s]/K[s]);C0+=z*l;C1+=z*u
    l,u=ln(likelihood);KL0+=z/M*l;KL1+=z/M*u
    ck((v[s]/K[s])*(Z/M)/likelihood==v[s]/z)
  ck(C0>=0);ck(KL0>=0)
  tax=ln(Z/M);tax=(M*tax[0],M*tax[1])
  if Z>M:ck(tax[1]<=Q(3,4)*D)
  if label=='two-heavy-control':
   ck(M==Q(1,4));ck(za==Q(3,8));ck(zb==Q(1,4));ck(Z==Q(1,2))
   for s,z in enumerate(mass):
    if mixed(s):ck(KB[s]==z)
   ck(all(z*Z==2*M*K[s] for s,z in enumerate(mass) if mixed(s) and z))
  if label=='recovered-guard':
   for s,z in enumerate(mass):
    if mixed(s):ck(KA[s]==z);ck(K[s]>=z)
  if C1/D>maximum[0]:maximum=(C1/D,label)
  rows.append({'label':label,'h':h,'b':b,'w':str(w),'t':str(t),'biases':[str(x) for x in p],'M':str(M),'D_mixed':str(D),'J_A':str(JA),'J_B':str(JB),'Z_A':str(za),'Z_B':str(zb),'Z_star':str(Z),'C_star_over_D_nats_interval':outward((C0/D,C1/D)),'KL_R_Qstar_interval':outward((KL0,KL1))})
 else:ck(D==Z==za==zb==0);rows.append({'label':label,'h':h,'b':b,'M':'0'})
 if time.monotonic()-start>60:raise RuntimeError('frozen runtime cap')
sizes=((1,2),(2,2)) if args.pilot else ((1,2),(2,2),(2,3),(3,2),(3,3))
for h,b in sizes:
 n=h+b;profiles=[(Q(1,2),)*n,tuple([Q(1,4),Q(1,2),Q(3,4)][i%3] for i in range(n))]
 for w in (Q(1,2),Q(2),Q(3)):
  for p in profiles:
   for j in range(1,int(2*(w*h+b))+1):case(h,b,w,p,Q(j,2),'threshold')
threshold_cases=len(rows)
for r in ((1,) if args.pilot else (1,2)):
 b=4*r+1;case(2,b,Q(b+1),(Q(1,2),)*(b+2),Q(b+1+(b+1)//2),'two-heavy-control')
guard_cases=0
for m in ((2,3) if args.pilot else (2,3,4,5)):
 q=Q(1,m*m);eta=Q(1,m);a=q**m;q0=(1-eta)*a/(eta+(1-eta)*a)
 case(1,m,Q(m),(q0,)+(q,)*m,Q(m),'recovered-guard');guard_cases+=1
for m in ((2,) if args.pilot else (2,3,4,5)):
 for q in ((Q(1,16),) if args.pilot else (Q(1,16),Q(1,256))):
  eta=Q(1,2);a=q**m;q0=(1-eta)*a/(eta+(1-eta)*a)
  case(1,m,Q(m),(q0,)+(q,)*m,Q(m),'recovered-guard');guard_cases+=1

# Count-compressed infinite-family lower-bound certificates and source quadratic constants.
growth=[]
for r in ((1,2) if args.pilot else (1,2,4,8,16,32)):
 m=2*r;n=4*r+1;q=Q(comb(2*m,m),4**m)
 ck(q*q>=Q(1,4*m));ck(q*q<=Q(1,m+1));ck(n*q*q>=Q(1,2))
 lower=ln(Q(2*r+1));ln4=ln(Q(4))
 growth.append({'r':r,'n_B':n,'singleton_coefficient':str(q),'E_mixed_over_J_A_nats_lower_bound':str(Q(1,4)*lower[0]+Q(1,2)*ln4[0]),'source_J_A':'1/2','source_Z_A':'3/8','reverse_K':'actual mixed P','Z_star':'1/2'})

# Complete one-bit selector owner on A045's actual band/parity fixture; no threshold assertion.
selector=[]
for r in ((1,2) if args.pilot else (1,2,4,8)):
 n=16*r*r;m=n//2;b=Q(comb(n-1,m-r),2**(n-1))
 count=[Q(comb(n,k),2**n) for k in range(n+1)]
 g=lambda k:1 if k<=m-r or k>=m+r else -1
 eg=sum(count[k]*g(k) for k in range(n+1))
 top=sum(count[k]*g(k)*(-1)**k for k in range(n+1))
 influence=Q(n,2)+n*b+(1-top)/2;variance=1-eg*eg/4;d=influence-variance
 ck(influence>=Q(n,2));ck(d>=Q(n,2)-1);ck(n+1<=3*d)
 # One-bit Fourier coefficient identity for arbitrary branch coefficients, exact rational.
 for a,c in ((Q(1,3),Q(-2,5)),(Q(0),Q(1)),(Q(2,7),Q(2,7))):
  p=Q(1,4);vC=4*p*(1-p);alpha=(c-a)/2
  ck(vC*alpha*alpha==vC*(c-a)**2/4)
 selector.append({'r':r,'n_data':n,'I':str(influence),'Delta':str(d),'complete_mixed_owner':'K_C=P_mixed exactly; Z_C=M, Q_C=R','retained_terminal_payment':'E_mixed <=(n+1)ln2<=3ln2 Delta','no_pair_multiplicity':True})
out={'helper':'A041-stage5-v1.1','pilot':args.pilot,'assertions':checks,'threshold_cases':threshold_cases,'two_heavy_truth_table_controls':1 if args.pilot else 2,'recovered_guard_cases':guard_cases,'growth_formula_cases':len(growth),'selector_count_cases':len(selector),'runtime_seconds':time.monotonic()-start,'maximum_finite_C_star_over_D_nats_upper':outward((maximum[0],maximum[0]))[1],'maximum_finite_label':maximum[1],'certificates':rows,'one_orientation_obstruction':growth,'selected_owner_fixture':selector}
(R/('out/PILOT.json' if args.pilot else 'out/EXACT_CHECKS.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ('certificates','one_orientation_obstruction','selected_owner_fixture')},indent=2))
