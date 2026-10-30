from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import json,sys,time
ROOT=Path(__file__).resolve().parents[1]
MODE=sys.argv[1]; START=time.perf_counter(); N=0
def ck(v):
 global N
 assert v, N
 N+=1
 assert time.perf_counter()-START<55
def add(*ds):
 r={}
 for d in ds:
  for p,c in d.items():r[p]=r.get(p,Q(0))+c
 return {p:c for p,c in r.items() if c}
def scale(d,c):return {p:c*v for p,v in d.items() if c*v}
@lru_cache(None)
def fac(n):
 d={};p=2
 while p*p<=n:
  while n%p==0:d[p]=d.get(p,0)+1;n//=p
  p+=1
 if n>1:d[n]=d.get(n,0)+1
 return d
def lg(q):return add(fac(q.numerator),scale(fac(q.denominator),-1))
def ent(ps):return add(*(scale(lg(p),-p) for p in ps if p))
@lru_cache(None)
def ln(p):
 k=p.bit_length()-1;r=Q(p,1<<k);z=(r-1)/(r+1)
 if p==2:z=Q(1,3);k=0
 low=2*sum((z**(2*j+1)/Q(2*j+1) for j in range(32)),Q(0))
 tail=2*z**65/(65*(1-z*z))
 if k:
  a,b=ln(2);low+=k*a;tail+=k*(b-a)
 return low,low+tail
def iv(d):
 a=b=Q(0)
 for p,c in d.items():
  l,h=ln(p);a+=c*(l if c>=0 else h);b+=c*(h if c>=0 else l)
 return a,b
def nonneg(d):ck(not d or iv(d)[0]>=0)
def enc(d):return {str(p):str(c) for p,c in d.items()}
def bits(d):
 a,b=iv(d);l,h=ln(2);v=[a/l,a/h,b/l,b/h];return [str(min(v)),str(max(v))]
def fw(f):
 return [Q(sum(f[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(len(f))),len(f)) for s in range(len(f))]
def restrict(f,i,b):
 return [f[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(len(f)//2)]
def data(f):
 a=fw(f);p=[x*x for x in a];ck(sum(p)==1)
 I=sum(s.bit_count()*x for s,x in enumerate(p));n=len(f).bit_length()-1
 ck(I==Q(sum(f[x]!=f[x^(1<<i)] for x in range(len(f)) for i in range(n)),len(f)))
 return a,ent(p),I
def main():
 roots=cuts=crit=0; selected=[];criticalC=[]
 for n in ([1,2] if MODE=='pilot' else [1,2,3]):
  for word in range(1<<(1<<n)):
   f=[-1 if word>>x&1 else 1 for x in range(1<<n)];a,H,I=data(f);roots+=1
   D=add(H,{2:-2*I});critical=n==3 and iv(D)[0]>0
   if n<=2:nonneg(scale(D,-1))
   if critical:crit+=1
   for i in range(n):
    cuts+=1; children=[data(restrict(f,i,b)) for b in (0,1)]
    L=add(H,scale(add(*(h for _,h,_ in children)),Q(-1,2)))
    Ii=Q(sum(f[x]!=f[x^(1<<i)] for x in range(len(f))),len(f))
    ck(I==Ii+sum(ic for _,_,ic in children)/2)
    B={};J={};G={};beta=C=Q(0);records=[]
    for t in range(len(a)):
     if t>>i&1:continue
     u,v=a[t],a[t|(1<<i)];q=u*u+v*v
     if not q:continue
     e=min(u*u,v*v)/q;c=4*e*(1-e);beta+=q*e;C+=q*c
     row=[u+v,u-v];z=[x*x/q for x in row]
     jr=add(*(scale(lg(x),q*x/2) for x in z if x))
     br=scale(ent([e,1-e]),q)
     B=add(B,br);J=add(J,jr);G=add(G,scale(lg(1+c),q))
     ck(sum(x**4 for x in row)/(2*q*q)-1==c)
     ck(c/4<=e<=c/2);nonneg(add({2:q*c},scale(jr,-1)))
     # kappa q e in natural log units is exactly 2 q e.
     ck(iv(jr)[1]<=2*q*e or not jr)
     records.append({'t':t,'a':str(u),'b':str(v),'q':str(q),'e':str(e),'c':str(c)})
    ck(add(B,J)==L);ck(2*beta<=C<=4*beta);ck(beta<=Ii)
    O=Ii-beta;nonneg(add(ent([beta,1-beta]),scale(B,-1)))
    nonneg(add(ent([C/2,1-C/2]),{2:C},scale(L,-1)))
    nonneg(add(G,scale(J,-1)))
    for K in (2,4,8,16):
     dk=add(H,{2:-K*I})
     S=scale(add(*(add(h,{2:-K*ic}) for _,h,ic in children)),Q(-1,2))
     reserve=add(dk,{2:K*O},S)
     ck(reserve==add(L,{2:-K*beta}))
     # Rigorous computable relaxation kappa<3; Legendre scalar bound.
     bound=lg(1+Q(2)**(3-K))
     nonneg(add(bound,scale(reserve,-1)))
     if critical and K==2:
      nonneg(S);ck(C>0)
      criticalC.append(C)
    if critical and word==1:
     selected.append({'n':n,'word':word,'coordinate':i,'C':str(C),'beta':str(beta),'orientation':str(O),'D_K2_interval':bits(D),'L':enc(L),'B':enc(B),'J':enc(J),'rows':records})
 result={'status':'PASS','helper_version':'A055-singleton-critical-reserve-v1','mode':MODE,'roots':roots,'labelled_singleton_cuts':cuts,'K2_minimal_violations':crit,'critical_singleton_cuts':len(criticalC),'critical_C_range':[str(min(criticalC)),str(max(criticalC))] if criticalC else None,'assertions':N,'runtime_seconds':time.perf_counter()-START,'arithmetic':'Fraction; integer direct character sums; prime-log expressions; 32-term atanh rational outward tails','selected':selected}
 (ROOT/'out'/f'{MODE.upper()}_CHECK.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in result.items() if k!='selected'}))
main()
