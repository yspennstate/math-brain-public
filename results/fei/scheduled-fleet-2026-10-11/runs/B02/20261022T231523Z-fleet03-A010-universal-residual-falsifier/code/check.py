from fractions import Fraction as F
from pathlib import Path
from math import comb,prod
from itertools import product
import json,time,sys
B=Path(__file__).resolve().parents[1];O=B/'out';O.mkdir(exist_ok=True)
checks=0
def ck(p):
 global checks
 checks+=1
 assert p,checks
def logbounds(x):
 x=F(x);ck(x>0);j=0
 while x<1:x*=2;j-=1
 while x>=2:x/=2;j+=1
 def ln(y):
  z=(y-1)/(y+1);lo=2*sum((z**(2*i+1)/F(2*i+1) for i in range(20)),F(0))
  return lo,lo+2*z**41/(41*(1-z*z))
 l,u=ln(x);l2,u2=ln(F(2));scale=1<<48
 low=F((j+l/u2)*scale//1,scale);hi=F(-(-(j+u/l2)*scale//1),scale)
 return low,hi
def forest(E,owned,lam):
 U=sorted(owned);adj={i:[j for j in U if i!=j and owned[i]&sum(1<<v for v in E[j])] for i in U}
 reach={i:{i,*adj[i]} for i in U}
 for v in U:
  for u in U:
   if v in reach[u]:reach[u]|=reach[v]
 comps={frozenset(j for j in U if j in reach[i] and i in reach[j]) for i in U}
 roots=sorted(min(S) for S in comps if not any(j in adj[i] for i in U if i not in S for j in S))
 ck(bool(roots));seen=set(roots);queue=roots[:];children={i:[] for i in U};visits=[]
 while queue:
  i=queue.pop(0);new=[]
  for j in adj[i]:
   if j not in seen:
    common=owned[i]&sum(1<<v for v in E[j]);v=(common&-common).bit_length()-1
    new.append((v,j));seen.add(j)
  new.sort();children[i]=new;queue.extend(j for v,j in new);visits.append(i)
 ck(seen==set(U));R=len(roots);N=len(U);num=lam**N/F(4**R)
 for i in U:
  s=owned[i].bit_count();c=len(children[i]);ck(s in (1,2))
  num/=s*(s+1)*comb(2,s)*(c+1)*(c+2)*comb(s+c-1,c)
 ck(sum(len(z) for z in children.values())==N-R)
 A=0
 for i in U:ck(not A&owned[i]);A|=owned[i]
 ck(num>=(lam/72)**A.bit_count())
 return num,{'roots':roots,'owned':{str(i):z for i,z in owned.items()},'children':{str(i):z for i,z in children.items()},'visits':visits}
def default_owned(E,A,n):
 d={}
 for v in range(n):
  if A>>v&1:
   i=next(i for i,e in enumerate(E) if v in e);d[i]=d.get(i,0)|(1<<v)
 return d
def damaged_owned(E,A,a,b):
 U=[i for i in range(a) if A>>i&1];V=[j for j in range(b) if A>>(a+j)&1]
 if not U or not V:return default_owned(E,A,a+b)
 idx={e:i for i,e in enumerate(E)};d={}
 def own(x,y,z):
  i=idx[x,a+y];d[i]=d.get(i,0)|z
 if U==[0] and V==[0]:
  own(0,1,1);own(1,0,1<<a);return d
 extras=[]
 if U==[0] and 0 in V:
  u=0;v=next(j for j in V if j);extras=[('r',0)]
 elif V==[0] and 0 in U:
  u=next(i for i in U if i);v=0;extras=[('l',0)]
 else:
  u=next((i for i in U if i),U[0]);v=next((j for j in V if j),V[0])
 own(u,v,(1<<u)|(1<<(a+v)))
 for x in U:
  if x!=u:
   if ('l',x) in extras:own(x,1,1<<x)
   else:own(x,v,1<<x)
 for y in V:
  if y!=v:
   if ('r',y) in extras:own(1,y,1<<(a+y))
   else:own(u,y,1<<(a+y))
 return d
def moments(a,b,k):
 u=F(1,2**a);v=F(1,2**b);n=a+b
 q=u+v+(k-1)*u*v
 I0=2*a*u*(1-v)+2*b*v*(1-u);IL=2*a*u*(1-v)
 I=I0+2*k*(n-4)*u*v
 R=2*v*(b-2*u*(b+k)+u*u*(b*(k+1)+2*k))
 M=2*u*v*((k+1)*(a*(1-v)+b*(1-u))-2*k*(u+v))
 return q,I0,IL,I,R,M
def physical(a,b,k,retain):
 n=a+b;E=[(i,a+j) for i in range(a) for j in range(b) if not (i==j and i<k)];lam=F(1,b)
 ck(all(sum(lam for e in E if v in e)<=1 for v in range(n)))
 f=[1 if any(x>>i&1 and x>>j&1 for i,j in E) else -1 for x in range(1<<n)]
 w=f[:];s=1
 while s<len(w):
  for z in range(0,len(w),2*s):
   for j in range(z,z+s):w[j],w[j+s]=w[j]+w[j+s],w[j]-w[j+s]
  s*=2
 P=[F(x*x,1<<(2*n)) for x in w];ck(sum(P)==1)
 q,I0,IL,I,R,M=moments(a,b,k);ck(F(f.count(-1),1<<n)==q)
 ck(F(sum(f[x]!=f[x^(1<<j)] for x in range(1<<n) for j in range(n)),1<<n)==I)
 ck(sum(A.bit_count()*p for A,p in enumerate(P))==I)
 maskL=(1<<a)-1;rr=F(0);mm=F(0);D=(1+lam/4)**len(E)-1;total=F(0);traces=[]
 for A in range(1,1<<n):
  U=A&maskL;V=A>>a;ss=U.bit_count();tt=V.bit_count();r=sum(((U>>i)^(V>>i))&1 for i in range(k));z=k-1-2*r
  coef=-2*((F(1,2**a) if not V else 0)+(F(1,2**b) if not U else 0)+F(z,2**n))
  ck(F(w[A],1<<n)==coef)
  if not U:rr+=tt*P[A]
  if U and V:mm+=(ss+tt)*P[A]
  owned=default_owned(E,A,n);num,tr=forest(E,owned,lam)
  if not V:
   num=prod(F(sum(i in e for e in E),32*b) for i in range(a) if U>>i&1)
   ck(num>=F(1,64)**ss)
  elif not U:
   num=prod(F(sum(a+j in e for e in E),32*b) for j in range(b) if V>>j&1)
   ck(num>=F(a,64*b)**tt)
  if k==1:
   dn,dt=forest(E,damaged_owned(E,A,a,b),lam)
   if U and V:ck(dn>=(lam/64)**(ss+tt))
   # The original one-edge Fourier domination includes every nonempty set.
   old=-2*((F(1,2**a) if not V else 0)+(F(1,2**b) if not U else 0)-F(1,2**n))
   ck(P[A]<=4*old*old)
  total+=num/D
  if retain:traces.append({'A':A,'numerator':str(num),'single_trace':tr})
 ck(rr==R and mm==M);ck(total<=1)
 # Source proof's two label payments, now with true moments and unchanged influence.
 lr=logbounds(F(b,a))[1];lb=logbounds(F(b))[1];l72=logbounds(F(72))[1]
 ck(R*lr<=F(50,9)*IL and M*lb<=F(9,2)*IL)
 upper=(l72+F(9,8))*I+R*lr+M*lb
 ck(upper<F(1255,72)*I and upper<18*I)
 return {'a':a,'b':b,'k':k,'I':str(I),'I_complete_graph':str(I0),'q':str(q),'R':str(R),'M':str(M),'D':str(D),'queue_output_mass':str(total),'complete_cost_upper':str(upper),'bound_over_I':str(upper/I),'truth_entries':len(f)},traces
def main():
 start=time.monotonic();pilot='--pilot' in sys.argv;rows=[];saved=[]
 pairs=[(2,2),(2,3),(3,3)] if pilot else [(a,b) for a in range(2,6) for b in range(a,6)]
 for a,b in pairs:
  for k in range(a+1):
   row,tr=physical(a,b,k,a<=3 and b<=3);rows.append(row)
   if tr:saved.append({'a':a,'b':b,'k':k,'traces':tr})
   (O/('PILOT_CHECKPOINT.json' if pilot else 'CHECKPOINT.json')).write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
   ck(time.monotonic()-start<(55 if pilot else 240))
 scalar=0
 for a in range(2,9 if pilot else 33):
  for b in range(a,9 if pilot else 33):
   u=F(1,2**a);v=F(1,2**b);ck(a*u<=F(1,2) and b*b*v<=F(9,8))
   for k in range(a+1):
    q,I0,IL,I,R,M=moments(a,b,k);ck(0<q<1 and I>=I0>0 and R>=0 and M>=0)
    ck(M<=2*u*v*(a+b)*(k+1));ck(1+u*k/(1-u)<=F(5,3));scalar+=1
 # Every count denominator, including zero children, uses this exact recurrence.
 for c in range(129):ck((c+1)**2*(c+2)<=2*6**c)
 ck(72**4<2**25)
 result={'status':'PASS','helper':'A010-growing-matching-v1','functions':len(rows),'truth_entries':sum(r['truth_entries'] for r in rows),'scalar_triples':scalar,'assertions':checks,'seconds':time.monotonic()-start,'rows':rows}
 (O/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 if not pilot:(O/'SMALL_TRACES.json').write_text(json.dumps(saved,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
if __name__=='__main__':main()
