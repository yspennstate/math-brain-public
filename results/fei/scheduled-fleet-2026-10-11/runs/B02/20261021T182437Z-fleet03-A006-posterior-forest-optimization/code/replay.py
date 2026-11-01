"""Independent exact certificate consumer: no optimizer or author helper imports."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations,product
from math import prod,comb,factorial
import json,time
B=Path(__file__).resolve().parents[1]
A010=B.parents[2]/'A010/runs/20261021T161852Z-fleet03-A010-universal-residual-falsifier'
start=time.monotonic();checks=0
def ck(p):
 global checks
 checks+=1
 assert p,checks
def makecuts(E,n,lift):
 out={};m=len(E)
 def ins(d):
  key=tuple(sorted((t,v) for t,v in d.items() if v))
  out.setdefault(key,None)
 for i in range(m):
  for j in range(i+1,m):
   if not any(v in E[j] for v in E[i]):continue
   for U in range(1<<m) if lift else [0]:
    if U&(1<<i|1<<j):continue
    for t in map(F,['0','1/4','1/2','1','2','4']):
     ins({U|1<<i:-t*t,U|1<<j:F(-1),U|1<<i|1<<j:4*(t+1)**2})
 if lift:
  for U in range(1,1<<m):
   for v in range(n):
    ii=[j for j in range(m) if v in E[j] and not U&(1<<j)]
    if ii:ins({U:F(-1),**{U|1<<j:F(4) for j in ii}})
 return [dict(k) for k in out]
def upper(h,u,cuts,receipt):
 s=dict(h);theta=F(receipt['theta'])
 for j,yy in receipt['multipliers']:
  y=F(yy);ck(y>=0)
  for t,z in cuts[j].items():s[t]-=y*z
 val=theta+sum(u[t]*max(s[t]-theta,0) for t in s)
 ck(str(val)==receipt['value'])
 for t in h:ck(theta+max(s[t]-theta,0)+sum(F(y)*cuts[j].get(t,0) for j,y in receipt['multipliers'])>=h[t])
 return val
d=json.loads((B/'out/CHECK.json').read_text(encoding='utf-8'))
source=json.loads((A010/'out/CHECK.json').read_text(encoding='utf-8'))
for row,src in zip(d['rows'],source['rows']):
 E=row['edges'];n=row['n'];m=len(E);h={int(t):F(z) for t,z in row['h'].items()};u={int(t):F(z) for t,z in row['caps'].items()}
 ck(h=={int(t):F(z) for t,z in src['h'].items()})
 for t,data in src['root_caps'].items():
  J=[E[i] for i in range(m) if int(t)>>i&1];L=F(data['L']);z=list(map(F,data['primal']));y=list(map(F,data['dual']));k=len(J)
  ck(all(x>=0 for x in z+y))
  ck(all(sum(z[i] for i,e in enumerate(J) if v in e)<=1 for v in range(n)))
  ck(all(y[a]+y[b]>=1 for a,b in J));ck(sum(y)==sum(z)==L)
  ck(u[int(t)]==1/((1+4*k/L)**k-(4*k/L)**k))
 oldcaps={int(t):min(F(1),F(4)**(1-int(t).bit_count())*F(data['L'])**(int(t).bit_count()-1)/int(t).bit_count()**int(t).bit_count()) for t,data in src['root_caps'].items()}
 left=F(1);oldvalue=F(0)
 for t in sorted(h,key=h.get,reverse=True):
  z=min(left,oldcaps[t]);oldvalue+=z*h[t];left-=z
  if not left:break
 ck(left==0 and oldvalue-F(row['v'])==F(src['old_gap']))
 values=[]
 for key,lift in [('cap',None),('pair',False),('lifted',True)]:
  cuts=[] if lift is None else makecuts(E,n,lift)
  c=row['certificates'][key];ck(len(cuts)==c['cut_count'])
  values.append(upper(h,u,cuts,c))
 ck(min(values)==F(row['certificates']['lifted']['best_value']))
 ck(F(row['best_bit_gap_over_I'])==2*(min(values)-F(row['v']))/F(row['I']))
# Positive multiplicative law satisfying all old caps/cones but breaking whole row.
E=[(0,1),(0,2),(0,3),(4,5)];lam=[F(2,5)]*3+[F(1,2)]
D=prod(1+x/4 for x in lam)-1;ck(D==F(3979,8000));bad_D=D
p={t:prod(lam[i]/4 for i in range(4) if t>>i&1)/D for t in range(1,16)}
ck(sum(p.values())==1)
for t in p:
 J=[E[i] for i in range(4) if t>>i&1];k=len(J)
 # Vertex-cover prices and a matching attain this L exactly on these star+edge subsets.
 L=F(bool(t&7)+bool(t&8));u=1/((1+4*k/L)**k-(4*k/L)**k)
 yy=[F(0)]*6;zz=[F(0)]*len(J)
 if t&7:
  yy[0]=1;zz[next(j for j,e in enumerate(J) if 0 in e)]=1
 if t&8:yy[4]=1;zz[J.index((4,5))]=1
 ck(sum(yy)==sum(zz)==L and all(yy[a]+yy[b]>=1 for a,b in J))
 ck(all(sum(zz[j] for j,e in enumerate(J) if v in e)<=1 for v in range(6)))
 ck(p[t]<=u)
for a in makecuts(E,6,False):ck(sum(z*p[t] for t,z in a.items())<=0)
for U in range(16):
 for i,j in combinations(range(3),2):
  if U&(1<<i|1<<j):continue
  a,b,c=p[U|1<<i],p[U|1<<j],p[U|1<<i|1<<j]
  ck(a*b-4*c*(a+b)>=0)
violation=4*sum(p[8|1<<i] for i in range(3))-p[8]
ck(violation==F(200,3979)>0)
# Empty-anchor normalization is not allowed; a single conditioned gate has p1=1.
ck(4*F(1)>1)
# Boundary pair cones and exact two-gate reconstruction, including zero determinant.
for i in range(1,16):
 for j in range(1,17-i):
  x,y=F(i,16),F(j,16);den=(1+x/4)*(1+y/4)-1
  a,b,c=x/(4*den),y/(4*den),x*y/(16*den)
  ck(4*c/b==x and 4*c/a==y)
  ck(a*b-4*c*(a+b)==c*(1-x-y)/den)
  ck((a-4*c)*(b-4*c)-16*c*c>=0)
q,r,s=F(2,3),F(5,18),F(1,18)
ck(q*r-4*s*(q+r)==F(-2,81));ck(q/4+r-9*s==F(-1,18))
# Whole A010 finite star extension: replay every exact primal/dual value and cap.
for src in source['stars']:
 m=src['m'];D=(1+F(1,4*m))**m-1;delta=F(1,4**m);ph=(1-F(1,2**m))**2
 aa=lambda k:F(factorial(k-1),3*8**k*k*(k+1))
 bb=lambda k:F(factorial(k),16*8**k*(k+1)*(k+2))
 h={}
 for k in range(1,m+1):
  h[k]=delta*D*(4*m)**k*(1+aa(k)/(aa(k)+bb(k)*F(m-k,m)))
  h[k]+=4*D*ph if k==1 else k*delta*D*4**k*m**(k-1)*bb(k-1)/(aa(k-1)+bb(k-1)*F(m-k+1,m))
 u={k:F(comb(m,k),((1+12*F(k,3))**k-(12*F(k,3))**k)) for k in h}
 c=src['new_lp'];theta=F(c['threshold']);pp={int(t):F(z) for t,z in c['primal'].items()}
 ck(sum(pp.values())==1 and all(0<=pp.get(k,0)<=u[k] for k in h))
 primal=sum(h[k]*pp.get(k,0) for k in h);dual=theta+sum(u[k]*max(h[k]-theta,0) for k in h)
 ck(primal==dual==F(c['value']));ck(primal-(1-delta)==F(src['new_gap']))
 ck(F(src['new_gap'])<F(src['old_gap'])<F(src['I'])/6)
out={'status':'PASS','graphs_replayed':len(d['rows']),'star_certificates_replayed':len(source['stars']),'assertions':checks,'separating_law':{'lambda':list(map(str,lam)),'D':str(bad_D),'whole_row_violation':str(violation),'all_15_caps':True,'every_conditional_pair_PSD':True},'seconds':time.monotonic()-start}
(B/'out/REPLAY.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
