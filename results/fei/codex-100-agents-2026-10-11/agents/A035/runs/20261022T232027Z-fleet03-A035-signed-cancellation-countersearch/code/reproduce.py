from pathlib import Path
from fractions import Fraction as F
from collections import Counter,defaultdict
from functools import lru_cache
import json,time
R=Path(__file__).resolve().parents[1];START=time.perf_counter();checks=0
def ck(v):
 global checks
 assert v;checks+=1
def unitln(x):
 z=(x-1)/(x+1);v=z;lo=F(0)
 for j in range(24):lo+=2*v/(2*j+1);v*=z*z
 return lo,lo+2*v/(49*(1-z*z))
LN2=unitln(F(2))
def outward(iv):
 scale=1<<120
 return F(iv[0].numerator*scale//iv[0].denominator,scale),F(-((-iv[1].numerator*scale)//iv[1].denominator),scale)
@lru_cache(None)
def log(q):
 n=q.numerator;d=q.denominator;shift=n.bit_length()-d.bit_length();z=q/F(2)**shift
 if z<1:z*=2;shift-=1
 lo,hi=unitln(z);return F(shift)+lo/LN2[1],F(shift)+hi/LN2[0]
def logs(terms):
 lo=hi=F(0)
 for q,c in terms.items():
  if not c:continue
  a,b=log(q)
  if c<0:a,b=b,a
  lo+=a*c;hi+=b*c
 return outward((lo,hi))
def add(*iv):return outward((sum(v[0] for v in iv),sum(v[1] for v in iv)))
def scale(iv,c):return outward((iv[0]*c,iv[1]*c) if c>=0 else (iv[1]*c,iv[0]*c))
def sub(a,b):return add(a,scale(b,-1))
def avg(v):return scale(add(*v),F(1,len(v)))
def ent(a):return logs(Counter({q:-q*c for q,c in Counter(x*x for x in a if x).items()}))
def row(a,i):
 M=defaultdict(F);B=defaultdict(F);energy=F(0)
 for s in range(len(a)):
  if s&(1<<i):continue
  u=a[s]**2;v=a[s|(1<<i)]**2;r=u+v;energy+=v
  if v:M[r/v]+=v;B[r/v]+=v
  if u:B[r/u]+=u
 return energy,logs(M),logs(B)
def ce_fair(a,i):
 t=defaultdict(F);norm=F(0)
 for s,v in enumerate(a):
  q=(a[s&~(1<<i)]**2+a[s|(1<<i)]**2)/2;norm+=q
  if v:ck(q>0);t[q]-=v*v
 ck(norm==1);return logs(t)
def table(L):
 n=2*L+4;out=[]
 for y in range(1<<n):
  x,a,b,c=[(y>>j)&1 for j in range(4)];u=(y>>4)&((1<<L)-1);v=y>>(4+L)
  out.append(-1 if (x==a==c==0) or (u==0 and a==b==0) or (v==0 and b==c==0) else 1)
 return out,list(range(n))
def restrict(t,labels,orig,value):
 i=labels.index(orig);lo=(1<<i)-1
 return [t[(x&lo)|((x&~lo)<<1)|(value<<i)] for x in range(len(t)//2)],labels[:i]+labels[i+1:]
def characters(t):
 N=len(t);a=[F(sum(v*(-1)**((x&s).bit_count()%2) for x,v in enumerate(t)),N) for s in range(N)]
 ck(sum(v*v for v in a)==1);return a
main={r['L']:r for r in json.loads((R/'out/validation.json').read_text(encoding='utf-8'))['cases']}
results=[]
for L in (1,2,3):
 t,labels=table(L);A=characters(t);M=add(*(row(A,i)[1] for i in labels));Bx=row(A,0)[2]
 Ipriv=sum(row(A,i)[0] for i in [0]+list(range(4,len(labels))))
 ck(Ipriv==F(main[L]['I_private']))
 oldCE=[];Bb=[];newCE=[];Hs=[];newH=[];Ba=[]
 for s in (0,1):
  p,lp=restrict(t,labels,0,s);P=characters(p);Hs.append(ent(P));Bb.append(row(P,lp.index(2))[2]);oldCE.append(ce_fair(P,lp.index(2)))
  for b in (0,1):
   v,lv=restrict(p,lp,2,b);V=characters(v);newCE.append(ce_fair(V,lv.index(1)));newH.append(ent(V));Ba.append(row(V,lv.index(1))[2])
   if s==b==1:ck(set(v)=={1});ck(newCE[-1]==(F(1),F(1)))
 oldbill=add(M,Bx,avg(oldCE));newbill=add(M,Bx,avg(Bb),avg(newCE));spare=sub((17*Ipriv,)*2,newbill)
 ck(spare[0]>F(1,32))
 for field,iv in [('M_old',M),('old_full_bill',oldbill),('new_full_bill',newbill),('new_spare',spare)]:
  target=[F(x) for x in main[L][field]];ck(iv[0]<=target[1] and target[0]<=iv[1])
 if L==1:
  for U in range(len(A)):ck(sum(A[s]*A[s^U] for s in range(len(A)))==(1 if U==0 else 0))
 results.append(dict(L=L,root_dimension=len(labels),old_bill=[str(x) for x in oldbill],new_bill=[str(x) for x in newbill],spare=[str(x) for x in spare]))
 ck(time.perf_counter()-START<60)
out=dict(checks=checks,runtime_seconds=time.perf_counter()-START,method='direct Boolean truth tables and all normalized character sums; separate24-term rational logarithms',cases=results)
(R/'out/reproduction.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k!='cases'}))
