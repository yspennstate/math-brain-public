from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import math,time,json,sys
RUN=Path(__file__).resolve().parents[1]; START=time.monotonic(); assertions=0
def ck(v):
 global assertions
 assertions+=1
 assert v
 assert time.monotonic()-START<45
def plus(a,b):return a[0]+b[0],a[1]+b[1]
def minus(a,b):return a[0]-b[1],a[1]-b[0]
def mul(a,c):return (a[0]*c,a[1]*c) if c>=0 else (a[1]*c,a[0]*c)
@lru_cache(None)
def log(q):
 q=F(q);assert q>0;k=0
 while q>=2:q/=2;k+=1
 while q<1:q*=2;k-=1
 def series(v):
  z=(v-1)/(v+1);lo=2*sum((z**(2*i+1)/F(2*i+1) for i in range(18)),F(0))
  return lo,lo+2*z**37/(37*(1-z*z))
 lo,hi=series(q);a,b=series(F(2));lo,hi=(lo+k*a,hi+k*b) if k>=0 else (lo+k*b,hi+k*a)
 grid=1<<96
 return F(math.floor(lo*grid),grid),F(math.ceil(hi*grid),grid)
def log2(q):
 a,b=log(q);c,d=log(F(2));return (a/d,b/c) if a>=0 else ((a/c,b/d) if b<=0 else (a/c,b/c))
def ce(p,q):
 out=(F(0),F(0))
 for a,b in zip(p,q):
  if a:out=plus(out,mul(log2(b),-a))
 return out
@lru_cache(None)
def factors(n):
 out={};d=2
 while d*d<=n:
  while n%d==0:out[d]=out.get(d,0)+1;n//=d
  d+=1
 if n>1:out[n]=out.get(n,0)+1
 return out
def form(p,q):
 out={}
 for a,b in zip(p,q):
  if a:
   for number,sgn in [(b.numerator,-1),(b.denominator,1)]:
    for d,e in factors(number).items():out[d]=out.get(d,F(0))+sgn*a*e
 return {d:e for d,e in out.items() if e}
def fadd(a,b,c=1):
 out=dict(a)
 for d,e in b.items():out[d]=out.get(d,F(0))+c*e
 return {d:e for d,e in out.items() if e}
def coeff(v):
 a=list(v);step=1
 while step<len(a):
  for k in range(0,len(a),2*step):
   for i in range(k,k+step):a[i],a[i+step]=a[i]+a[i+step],a[i]-a[i+step]
  step*=2
 return [F(x,len(v)) for x in a]
def spectrum(v):return [x*x for x in coeff(v)]
def ins(t,j,s):return (t&((1<<j)-1))|((t>>j)<<(j+1))|(s<<j)
def child(v,j,s):return [v[ins(t,j,s)] for t in range(len(v)//2)]
def marginal(p,j):return [p[ins(t,j,0)]+p[ins(t,j,1)] for t in range(len(p)//2)]
def pivot(v,j):return F(sum(v[t]!=v[t^(1<<j)] for t in range(len(v))),len(v))
CTL=[1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1]; A=coeff(CTL);B=coeff([1-x*x for x in CTL]);beta=sum(b*b for b in B)
def core(z,L):
 y=[-1 if ((z>>(j*L))&((1<<L)-1)).bit_count()%2 else 1 for j in range(3)]
 return -1 if y[0]==y[1]==y[2] else 1
def wrap(p,m,sign):return [(A[u]+sign*m*B[u])**2 if t==0 else B[u]**2*p[t] for t in range(len(p)) for u in range(16)]
def floor_census():
 count=0;best=[]
 for z in range(8,17):
  for x in range(1,18-z):
   y=18-z-x;ck(y>0);count+=1
   ck(6*x*y*z<=6*5*5*8)
   if 6*x*y*z==6*5*5*8:best.append([6,x,y,z])
 ck(count==45 and best==[[6,5,5,8]])
 return count
def review(L,sign):
 v=[CTL[t&15]+sign*(1-CTL[t&15]**2)*core(t>>4,L) for t in range(1<<(4+3*L))]
 p=spectrum(v);n=4+3*L
 ck(set(v)=={-1,1} and sum(p)==1 and sum(x>0 for x in p)<=64)
 infl=[pivot(v,j) for j in range(n)];expected=[F(5 if sign==1 else 7,16)]*2+[F(1,2)]*2
 ck(infl[:4]==expected);ck(all(a==F(3,16) for a in infl[4:]));ck(sum(infl)==(F(13 if sign==1 else 15,8)+F(9*L,16)))
 ck(F(35,4)<=4*sum(infl));c0=ce(p,p);ck(c0[1]<6)
 q0=p;nodes=[(v,p,q0,0,F(1))];terminals=0;transitions=0;after=0;minmargin=F(100)
 delta=mul(log2(F(27,25)),F(3,32));df={3:F(9,32),5:F(-3,16)}
 while nodes:
  v,p,q,d,reach=nodes.pop();ck(p==q)
  if d<L:
   j=4;ck(all(not (p[ins(t,j,0)] and p[ins(t,j,1)]) for t in range(len(p)//2)))
   qb=marginal(q,j)
   for s in [0,1]:
    cv=child(v,j,s);cp=spectrum(cv);ck(cp==qb);transitions+=1
    nodes.append((cv,cp,qb,d+1,reach/2))
  else:
   terminals+=1;sv=[sign*v[1|(z<<4)] for z in range(1<<(2*L))];sp=spectrum(sv);sm=sum(sv)/len(sv)
   # sm is exactly1/2; cast explicitly to rational before all reference arithmetic.
   sm=F(sum(sv),len(sv));ck(sm==F(1,2));ck(wrap(sp,sm,sign)==p)
   block=(1<<L)-1;labels=[0,block,block<<L,(1<<(2*L))-1]
   ck([sp[t] for t in labels]==[F(1,4)]*4 and sum(sp)==1)
   fresh=[F(0)]*len(sp)
   for t,mass in zip(labels,[F(1,4),F(5,24),F(5,24),F(1,3)]):fresh[t]=mass
   qn=wrap(fresh,sm,sign);ck(sum(qn)==1)
   ck(fadd(form(p,qn),form(p,q),-1)==df)
   margin=F(35,4)-F(1,4)-ce(p,qn)[1];ck(margin>F(77,32));minmargin=min(minmargin,margin)
   # One genuine query of the remaining second block, using installed qn.
   j=4;qb=marginal(qn,j);avg=(F(0),F(0));er=(F(0),F(0));occ=(F(0),F(0))
   for t in range(len(p)//2):
    pp=[p[ins(t,j,s)] for s in [0,1]];qq=[qn[ins(t,j,s)] for s in [0,1]];mass=sum(pp)
    if mass:
     pp=[a/mass for a in pp];qq=[a/sum(qq) for a in qq]
     er=plus(er,mul(ce(pp,pp),mass));occ=plus(occ,mul(minus(ce(pp,qq),ce(pp,pp)),mass))
   for s in [0,1]:
    cp=spectrum(child(v,j,s));avg=plus(avg,mul(ce(cp,qb),F(1,2)));after+=1
   increment=minus(plus(er,avg),ce(p,qn));identity=plus(increment,occ);ck(identity[0]<=0<=identity[1])
   ck(occ[1]>=0);ck(increment[1]<=0 or identity[0]<=0<=identity[1])
 ck(terminals==2**L and transitions==2*(2**L-1))
 return {'L':L,'sign':sign,'vertices':1<<n,'terminal_count':terminals,'prefix_child_transitions':transitions,'post_conversion_children':after,'margin_lower_rational':str(minmargin),'cost_form':{str(k):str(v) for k,v in df.items()}}
def geometric():
 # A real unequal-depth isospectral tree on the L=2 encoded seed.
 v=[core(z,2) for z in range(64)];p=spectrum(v);omega=[i for i,a in enumerate(p) if a]
 leaves=[]
 for first in [0,1]:
  cv=child(v,0,first);cp=spectrum(cv);mapping={t:((t>>1)) for t in omega};ck(cp==marginal(p,0))
  if first==0:leaves.append((cp,mapping,F(1,2),[3,3,1,1]))
  else:
   for second in [0,1]:
    p2=spectrum(child(cv,0,second));mp={t:(u>>1) for t,u in mapping.items()};ck(p2==marginal(cp,0));leaves.append((p2,mp,F(1,4),[1,1,3,3]))
 bills=[]
 for ghost in [False,True]:
  meanform={};avg=(F(0),F(0))
  for pl,mp,w,weights in leaves:
   q=[F(0)]*len(pl)
   for root,a in zip(omega,weights):q[mp[root]]=F(a,8)*(F(7,8) if ghost else 1)
   if ghost:q[next(t for t in range(len(pl)) if not pl[t])]=F(1,8)
   ck(sum(q)==1);avg=plus(avg,mul(ce(pl,q),w));meanform=fadd(meanform,form(pl,q),w)
  delta=fadd(meanform,form(p,p),-1);want={2:F(1),3:F(-1,2)}
  if ghost:want=fadd(want,{2:F(3),7:F(-1)})
  ck(delta==want)
  inc=minus(avg,ce(p,p));ck(inc[0]>0)
  bills.append({'ghost':ghost,'exact_delta_log2_form':{str(k):str(v) for k,v in delta.items()},'Rstar':'P','Z':'7*sqrt(3)/16' if ghost else 'sqrt(3)/2'})
 return {'leaf_weights':['1/2','1/4','1/4'],'witnesses':bills}
pilot='--pilot' in sys.argv; widths=[1] if pilot else [2,3]
count=floor_census();rows=[review(L,s) for L in widths for s in [-1,1]];geom=geometric()
result={'verdict':'PASS','mode':'pilot' if pilot else 'main','assertions':assertions,'rows':rows,'floor_candidates':count,'geometric':geom,'elapsed_seconds':time.monotonic()-START,'arithmetic':'integer FWHT, physical pivots, exact Fraction prime-log forms, outward18-term atanh on2^-96 grid','formal_verification':'NOT_CLAIMED'}
(RUN/'out'/('PILOT.json' if pilot else 'VALIDATION.json')).write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps({k:result[k] for k in ['verdict','mode','assertions','elapsed_seconds']}))
