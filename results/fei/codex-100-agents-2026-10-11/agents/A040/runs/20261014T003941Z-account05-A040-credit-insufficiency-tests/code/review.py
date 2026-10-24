"""Independent physical-cube review. No author executable is imported."""
from fractions import Fraction as F
from pathlib import Path
from functools import lru_cache
import json, time, sys, hashlib
ROOT=Path(__file__).resolve().parents[1]
START=time.monotonic(); CHECKS=0
def check(ok):
 global CHECKS
 assert ok
 CHECKS+=1
def add(*terms):
 z={}
 for a,v in terms:
  for p,c in v.items():z[p]=z.get(p,F(0))+a*c
 return {p:c for p,c in z.items() if c}
@lru_cache(None)
def fac(n):
 z={};p=2
 while p*p<=n:
  while n%p==0:z[p]=z.get(p,0)+1;n//=p
  p=3 if p==2 else p+2
 if n>1:z[n]=z.get(n,0)+1
 return z
@lru_cache(None)
def lv(x):
 x=F(x);return add((1,fac(x.numerator)),(-1,fac(x.denominator)))
@lru_cache(None)
def ent_atom(p):return add((-p,lv(p))) if p else {}
def ent(P):return add(*[(1,ent_atom(p)) for p in P if p])
@lru_cache(None)
def h(d):return ent([d,1-d])
@lru_cache(None)
def log_bounds(p):
 p=F(p);shift=p.numerator.bit_length()-p.denominator.bit_length();v=p/F(2)**shift
 if v<1:v*=2;shift-=1
 def ln(x):
  t=(x-1)/(x+1);m=24
  low=2*sum((t**(2*j+1)/F(2*j+1) for j in range(m)),F(0))
  return low,low+2*t**(2*m+1)/((2*m+1)*(1-t*t))
 a,b=ln(v);c,d=ln(F(2));return shift+a/d,shift+b/c
def bounds(v):
 lo=hi=F(0)
 for p,c in v.items():
  a,b=log_bounds(p);lo+=c*(a if c>0 else b);hi+=c*(b if c>0 else a)
 return lo,hi
def packed(v):
 lo,hi=bounds(v);grid=10**25
 return {'prime_log_vector':{str(p):str(c) for p,c in sorted(v.items())},'lower':str(F(lo.numerator*grid//lo.denominator,grid)),'upper':str(F(-((-hi.numerator*grid)//hi.denominator),grid))}
def fwht(v):
 a=list(v);stride=1
 while stride<len(a):
  for base in range(0,len(a),2*stride):
   for j in range(base,base+stride):x,y=a[j],a[j+stride];a[j],a[j+stride]=x+y,x-y
  stride*=2
 return tuple(a)
def halves(v,i):
 return tuple(v[x] for x in range(len(v)) if not(x>>i&1)),tuple(v[x|(1<<i)] for x in range(len(v)) if not(x>>i&1))
def infs(v):
 N=len(v)
 return tuple(F(sum(v[x]!=v[x|(1<<i)] for x in range(N) if not(x>>i&1)),N//2) for i in range(N.bit_length()-1))
@lru_cache(None)
def spectrum(v):
 N=len(v);W=fwht(v);P=tuple(F(w*w,N*N) for w in W);d=infs(v)
 check(sum(P)==1)
 check(d==tuple(sum((p for s,p in enumerate(P) if s>>i&1),F(0)) for i in range(len(d))))
 H=ent(P);TC=add(*[(1,h(x)) for x in d],(-1,H))
 return P,d,H,TC,W
def core(kind,k):
 if kind=='dictator':return (1,-1)
 vals=[]
 for x in range(1<<(k+(2 if kind=='selector' else 1))):
  data=x&((1<<k)-1);b=(-1)**sum((data>>(2*j)&1)*(data>>(2*j+1)&1) for j in range(k//2))
  if kind=='selector' and (x>>k&1) and data==0:b=-b
  z=x>>(k+(1 if kind=='selector' else 0))&1
  vals.append((-1)**z*b)
 return tuple(vals)
def build(L,R,T,g):
 n=1+L+R+T;out=[];A=[]
 for c in range(1<<n):
  X=c&1;W=((c>>1)&((1<<L)-1))==((1<<L)-1)
  U=((c>>(1+L))&((1<<R)-1))==((1<<R)-1)
  V=((c>>(1+L+R))&((1<<T)-1))==((1<<T)-1)
  A.append(int((X and (U or V)) or (W and U and V)))
 for v in range((1<<n)*len(g)):out.append(g[v>>n] if A[v&((1<<n)-1)] else 1)
 return tuple(out),tuple(A),n
def signed_influence_indicator(A):return sum(infs(tuple(1-2*a for a in A)))/2
def odd_faces(v):
 N=len(v);total=0
 for i in range(N.bit_length()-1):
  for j in range(i):
   mask=(1<<i)|(1<<j)
   total+=sum(v[x]*v[x|(1<<i)]*v[x|(1<<j)]*v[x|mask]<0 for x in range(N) if x&mask==0)
 return F(2*total,N)
def run_case(L,R,T,kind,k):
 spectrum.cache_clear();g=core(kind,k);v,A,n=build(L,R,T,g);P,ds,H,TC,_=spectrum(v);_,gd,gH,_,_=spectrum(g)
 check(sum(g)==0);Ig=sum(gd);p=F(1,2**L);q=F(1,2**R);r=F(1,2**T)
 beta=q+r-q*r;eta=p*q*r;pi=(beta+eta)/2;e=beta-eta;dX=e/2
 rem=((L+R+T)*eta+R*q*(1-r)+T*r*(1-q))/2
 check(F(sum(A),len(A))==pi);check(signed_influence_indicator(A)==dX+rem)
 check(ds[0]==dX);check(sum(ds[:n])==dX+rem);check(sum(ds[n:])==pi*Ig)
 check(sum(ds)==dX+rem+pi*Ig)
 A0,A1=halves(A,0);D=tuple(a1-a0 for a0,a1 in zip(A0,A1))
 check(set(D)<={0,1});check(F(sum(D),len(D))==e)
 # This directly checks disjoint physical boundaries, not inclusion-exclusion.
 for j in range(n-1):
  for x in range(len(A0)):
   if not(x>>j&1):check(not(A0[x]!=A0[x|(1<<j)] and A1[x]!=A1[x|(1<<j)]))
 check(signed_influence_indicator(D)==2*rem)
 sums={s:{} for s in ['B','posterior','JS','Gamma','minor']};removed=F(0);face=F(0);badface=F(0);terminalI=F(0);terminalH={};terminalTC={};terminalprob=F(0);terminalface=F(0);nodes=[]
 # Prove a tight lower bound; using a coarse 1.4 would demand an unrelated
 # stronger finite inequality when minority packets are very small.
 t=F(1,3);ln2lo=2*sum((t**(2*j+1)/F(2*j+1) for j in range(24)),F(0))
 ln2hi=ln2lo+2*t**49/(49*(1-t*t));c_lower=1/ln2hi
 def walk(v,labels,weight,depth):
  nonlocal removed,face,badface,terminalI,terminalH,terminalTC,terminalprob,terminalface
  P,ds,H,TC,W=spectrum(v)
  chosen=next((j for j in range(n) if j in labels and ds[labels.index(j)]),None)
  if chosen is None:
   terminalI+=weight*sum(ds);terminalH=add((1,terminalH),(weight,H));terminalTC=add((1,terminalTC),(weight,TC));terminalface+=weight*odd_faces(v)
   if len(set(v))>1:terminalprob+=weight
   return
  i=labels.index(chosen);v0,v1=halves(v,i);p0,d0,H0,TC0,W0=spectrum(v0);p1,d1,H1,TC1,W1=spectrum(v1)
  packet=tuple(P[s]+P[s|(1<<i)] for s in range(len(P)) if not(s>>i&1));HP=ent(packet)
  B=add((1,H),(-1,HP));J=add((1,h(ds[i])),(-1,B));JS=add((1,HP),(-F(1,2),H0),(-F(1,2),H1))
  Gamma=add(*[(1,h((a+b)/2)) for a,b in zip(d0,d1)],*[(-F(1,2),h(a)) for a in d0+d1])
  mu=F(0);minor={};N=len(v0)
  for a,b,Q in zip(W0,W1,packet):
   m=F((abs(a)-abs(b))**2,4*N*N);mu+=m
   if m:minor=add((1,minor),(m,lv(Q/m)))
  check(mu<=ds[i]);check(bounds(add((1,B),(-1,minor)))[0]>=0 or B==minor)
  if mu:
   check(bounds(add((1,B),(-1,minor)))[1]<=c_lower*mu)
   check(bounds(JS)[1]<=2*c_lower*mu)
   check(bounds(add((1,H),(-F(1,2),H0),(-F(1,2),H1),(-1,minor)))[1]<=3*c_lower*mu)
  else:check(not JS and B==minor)
  check(not add((1,TC),(-1,J),(1,JS),(-1,Gamma),(-F(1,2),TC0),(-F(1,2),TC1)))
  check(sum(ds)==ds[i]+(sum(d0)+sum(d1))/2)
  prod=tuple(a*b for a,b in zip(v0,v1));cost=sum(infs(prod))/2
  sign=add((1,B),(-4*ds[i],{2:F(1)}));lo,hi=bounds(sign)
  check(not sign or lo>0 or hi<0);bad=lo>0
  if depth:check(not bad)
  if not depth:check(cost==rem+e*Ig/2)
  check(cost<=sum(ds)-ds[i] if not depth else True)
  for s,z in [('B',B),('posterior',J),('JS',JS),('Gamma',Gamma),('minor',minor)]:sums[s]=add((1,sums[s]),(weight,z))
  removed+=weight*ds[i];face+=weight*cost
  if bad:badface+=weight*cost
  nodes.append({'original_coordinate':chosen,'depth':depth,'weight':str(weight),'d':str(ds[i]),'face':str(cost),'bad':bad,'B_minus_4d':packed(sign),'posterior':packed(J)})
  nextlabels=labels[:i]+labels[i+1:]
  walk(v0,nextlabels,weight/2,depth+1);walk(v1,nextlabels,weight/2,depth+1)
 walk(v,tuple(range(len(ds))),F(1),0)
 check(removed==dX+rem);check(terminalI==pi*Ig);check(terminalprob==pi);check(not add((1,terminalH),(-pi,gH)))
 check(not add((1,H),(-1,sums['B']),(-1,sums['JS']),(-1,terminalH)))
 check(not add((1,sums['posterior']),(1,sums['Gamma']),(1,terminalTC),(-1,TC),(-1,sums['JS'])))
 check(badface in [F(0),rem+e*Ig/2]);check(badface<=sum(ds)-dX)
 check(face+terminalface==odd_faces(v))
 # The exact slack of the terminal-core one-unit reserve is eta*I(g).
 check(pi*Ig-e*Ig/2==eta*Ig)
 control0=infs(tuple(1-2*a for a in A0));control1=infs(tuple(1-2*a for a in A1));controlD=infs(tuple(1-2*a for a in D))
 for j in range(n-1):
  before=(control0[j]+control1[j])/4
  charged=controlD[j]/2
  check(charged==2*before)
 return {'L':L,'R':R,'T':T,'kind':kind,'k':k,'dimension':len(ds),'pi':str(pi),'I':str(sum(ds)),'control_I':str(removed),'terminal_I':str(terminalI),'terminal_entropy':packed(terminalH),'root_entropy':packed(H),'root_face':str(rem+e*Ig/2),'Q_bad':str(badface),'unused_terminal_reserve':str(eta*Ig),'posterior_sum':packed(sums['posterior']),'root_posterior':nodes[0]['posterior'],'nodes':nodes}
def main():
 pilot='pilot' in sys.argv;cases=[(L,R,T,'dictator',0) for L in [1,2,3] for R in [1,2,3] for T in [1,2,3]]
 cases += [(L,R,T,'bent',k) for L in [1,2] for R in [1,2] for T in [1,2] for k in [2,4]]
 cases += [(L,R,T,'selector',4) for L in [1,2] for R in [1,2] for T in [1,2]]
 if pilot:cases=cases[:1]
 rows=[];target=ROOT/'out'/('PILOT.json' if pilot else 'RESULTS.json');prior_checks=0
 if not pilot and 'resume' in sys.argv and target.exists():
  old=json.loads(target.read_text(encoding='utf-8'));rows=old['cases'];prior_checks=old['checks']
  check([tuple(z[s] for s in ['L','R','T','kind','k']) for z in rows]==cases[:len(rows)])
 for case in cases[len(rows):]:
  if time.monotonic()-START>=45:
   target.write_text(json.dumps({'status':'CHECKPOINT','checks':prior_checks+CHECKS,'root_count':len(rows),'runtime_seconds_this_batch':time.monotonic()-START,'cases':rows},indent=2),encoding='utf-8')
   print(json.dumps({'status':'CHECKPOINT','checks':prior_checks+CHECKS,'roots':len(rows),'runtime_seconds_this_batch':time.monotonic()-START}));return
  rows.append(run_case(*case));target.write_text(json.dumps({'status':'RUNNING','checks':prior_checks+CHECKS,'cases':rows},indent=2),encoding='utf-8')
 if not pilot:
  # Homogeneity certificate: balanced cores have identical root control B,J.
  groups={}
  for row in rows:
   key=tuple(row[s] for s in ['L','R','T']);p=row['root_posterior']['prime_log_vector']
   if key in groups:check(p==groups[key])
   else:groups[key]=p
  # Scalar constants proved by explicit series and rational estimates.
  lnlo,lnhi=(lambda t:(2*sum((t**(2*j+1)/F(2*j+1) for j in range(24)),F(0)),2*sum((t**(2*j+1)/F(2*j+1) for j in range(24)),F(0))+2*t**49/(49*(1-t*t))))(F(1,3))
  check(1/lnhi>F(7,5));check(1/lnlo<F(81,56));check(1+F(81,56)+2*F(81,56)/F(8,3)<4)
  check(5+2*F(81,56)<8);check(5+3*F(81,56)<10)
  check(rows[0]['root_posterior']['lower']!='0')
 target.write_text(json.dumps({'status':'PASS','checks':prior_checks+CHECKS,'root_count':len(rows),'runtime_seconds_final_batch':time.monotonic()-START,'cases':rows},indent=2),encoding='utf-8')
 print(json.dumps({'status':'PASS','checks':prior_checks+CHECKS,'roots':len(rows),'runtime_seconds_final_batch':time.monotonic()-START}))
if __name__=='__main__':main()
