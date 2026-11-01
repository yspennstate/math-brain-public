import check as u
from fractions import Fraction as R
from itertools import product
from functools import lru_cache
from pathlib import Path
import sys,time,json,hashlib
RUN=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def ck(x):
 global checks
 checks+=1;assert x,checks
 if checks%1000==0:assert time.perf_counter()-start<55
def ln_bounds(q):
 t=(q-1)/(q+1);assert 0<=t<=R(1,3)
 lo=2*sum(t**(2*j+1)/(2*j+1) for j in range(24))
 return lo,lo+2*t**49/(49*(1-t*t))
@lru_cache(None)
def logprime(p):
 k=p.bit_length()-1;a,b=ln_bounds(R(p,1<<k));c,d=ln_bounds(R(2))
 return R(k)+a/d,R(k)+b/c
def upper(v):
 out=R(0)
 for p,e in v.items():a,b=logprime(p);out+=e*(b if e>=0 else a)
 return out
def fusion(f,s,refs):
 n=(len(f)-1).bit_length();d=n-s;h=u.transform(f);slices=[];localI=[];localp=[]
 for z in range(1<<s):
  t=[f[z|(x<<s)] for x in range(1<<d)];slices.append(t);localp.append([c*c for c in u.transform(t)]);localI.append(u.influence(t,0,d))
 nonconstant=[z for z in range(1<<s) if any(localp[z][1:])];k=len(nonconstant)
 bar=[R(0)]+[sum(refs[z][A] for z in nonconstant)/k if k else R(1,(1<<d)-1) for A in range(1,1<<d)]
 ck(sum(bar)==1)
 Q=[R(0)]*len(f)
 for mask in range(1,len(f)):
  B=mask&((1<<s)-1);A=mask>>s
  Q[mask]=bar[A]/(1<<(s+1)) if A else R(1,2*((1<<s)-1))
 ck(sum(Q)==1)
 rhs={};Gamma={};M=R(0)
 for z in nonconstant:
  p=localp[z][1:];M+=sum(p)/(1<<s)
  u.plus(rhs,u.cost(p,refs[z][1:]),R(1,1<<s))
  for A in range(1,1<<d):
   if localp[z][A]:
    ck(refs[z][A]>0 and bar[A]>=refs[z][A]/k)
    u.plus(Gamma,u.log(refs[z][A]/bar[A]),localp[z][A]/(1<<s))
 N=sum(h[B]*h[B] for B in range(1,1<<s))
 u.plus(rhs,Gamma);u.plus(rhs,{2:R(s+1)*M});u.plus(rhs,u.log(R(2*((1<<s)-1))),N)
 actual=u.cost([c*c for c in h[1:]],Q[1:]);ck(actual==rhs)
 Ix=u.influence(f,s,n);Iz=u.influence(f,0,s)
 ck(Ix==sum(localI)/(1<<s));ck(M<=Ix and N<=Iz)
 return actual,Gamma,Ix+Iz
def clause_case(anchors,widths):
 s=2;d=sum(widths);f=[]
 for xz in range(1<<(s+d)):
  z=xz&3;x=xz>>2;shift=0;value=True
  for a,w in zip(anchors,widths):value &= bool((z&a) or ((x>>shift)&((1<<w)-1)));shift+=w
  f.append(1 if value else -1)
 refs=[]
 for z in range(4):
  active=[j for j,a in enumerate(anchors) if not z&a]
  if not active:refs.append([R(0)]+[R(1,(1<<d)-1)]*((1<<d)-1));continue
  rhos=[R(1,1<<(w+1)) for w in widths];empty=R(1)
  for j in active:empty*=1-rhos[j]
  q=[R(0)]*(1<<d)
  for mask in range(1,1<<d):
   shift=0;prob=R(1)
   for j,w in enumerate(widths):
    B=(mask>>shift)&((1<<w)-1);shift+=w
    if j not in active:
     if B:prob=R(0);break
    else:prob*=rhos[j]/((1<<w)-1) if B else 1-rhos[j]
   q[mask]=prob/(1-empty)
  ck(sum(q)==1);refs.append(q)
 C,G,I=fusion(f,2,refs);ck(upper(C)<=13*I)
def negative():
 # f is independent of the core and equals the first of two data bits.
 f=[1 if (x>>1)&1 else -1 for x in range(8)]
 refs=[[R(0),R(1,10),R(9,20),R(9,20)],[R(0),R(9,10),R(1,20),R(1,20)]]
 C,G,I=fusion(f,1,refs);ck(G==u.log(R(3,5)));ck(C=={2:R(3)});ck(upper(G)<0)
def main():
 pilot='--pilot' in sys.argv;cases=0
 for word in range(8 if pilot else 256):
  f=[1 if (word>>x)&1 else -1 for x in range(8)]
  for style in [0,1]:
   refs=[[R(0)]+[R(1,3)]*3 for z in range(2)] if not style else [[R(0),R(1,6),R(2,6),R(3,6)],[R(0),R(3,6),R(2,6),R(1,6)]]
   fusion(f,1,refs);cases+=1
 families=[(a,(1,)*len(a)) for length in [1,2] for a in product([1,2,3],repeat=length)]
 families += [((1,2,3),(1,2,1)),((1,2,3),(2,1,2)),((0,1,2),(1,1,1))]
 for a,w in (families[:1] if pilot else families):clause_case(a,w);cases+=1
 negative();cases+=1;ck(cases==(18 if pilot else 528));ck(time.perf_counter()-start<55)
 result={'PASS':True,'pilot':pilot,'cases':cases,'assertions':checks,'elapsed_seconds':time.perf_counter()-start,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'negative_Gamma':'log2(3/5)','negative_fixture_complete_cost_bits':3}
 (RUN/'out'/('review_pilot.json' if pilot else 'review_full.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
if __name__=='__main__':main()
