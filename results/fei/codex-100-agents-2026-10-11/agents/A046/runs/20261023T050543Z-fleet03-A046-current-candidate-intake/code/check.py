from fractions import Fraction as F
from pathlib import Path
import itertools, json, sys, time
ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter(); checks=nodes=zero_rows=trees=0
def eq(a,b):
 global checks
 assert a==b,(a,b)
 checks+=1
def fourier(vals):
 n=len(vals)
 return [sum(v*(-1 if (x&t).bit_count()%2 else 1) for x,v in enumerate(vals))/F(n) for t in range(n)]
def source(vals,s):
 a=fourier(vals)
 return [(s*(t==0)+(-1 if c else 1)*a[t])**2/4 for t in range(len(a)) for c in range(2)]
def drop(t,i):return (t&((1<<i)-1))|((t>>(i+1))<<i)
def insert(t,i,b):return (t&((1<<i)-1))|(b<<i)|((t>>i)<<(i+1))
def restricted(vals,i,b):return [vals[insert(t,i,b)] for t in range(len(vals)//2)]
def fresh(vals,s):
 p=[a*a for a in fourier(vals)];q=[p[0]]+[F(6,7)*x for x in p[1:]]
 if len(p)>1:q[-1]+=F(1,7)*(1-p[0])
 P=source(vals,s)
 return [P[0],P[1]]+[q[t]/4 for t in range(1,len(p)) for c in range(2)]
def logs_add(d,w,x):
 if w and x!=1:d[x]=d.get(x,F(0))+w
def reset_logs(P,R,new):
 d={}
 for p,r,q in zip(P,R,new):
  if p:logs_add(d,p,r/q)
 return {k:v for k,v in d.items() if v}
def recurse(vals,s,R,order):
 global nodes,zero_rows
 nodes+=1
 assert time.perf_counter()-START<55,'frozen runtime exceeded'
 P=source(vals,s);p=[a*a for a in fourier(vals)]
 eq(sum(R),1);eq(sum(P),1)
 for t in range(1,len(p)):eq(R[2*t],R[2*t+1])
 new=fresh(vals,s); reduced={}
 for c in range(2):
  if P[c]:logs_add(reduced,P[c],R[c]/P[c])
 for t in range(1,len(p)):
  if p[t]:logs_add(reduced,p[t]/2,R[2*t]/new[2*t])
 eq(reset_logs(P,R,new),{k:v for k,v in reduced.items() if v})
 if not order:return
 i=order[0]
 E=[F(0)]*len(P[::2]);D=[F(0)]*len(E)
 for t in range(len(p)):
  for c in range(2):
   j=2*drop(t,i)+c; E[j]+=P[2*t+c];D[j]+=R[2*t+c]
 for b in range(2):
  child=restricted(vals,i,b);Pc=source(child,s)
  dense=[]
  for e,d,pc in zip(E,D,Pc):
   if not e:zero_rows+=1
   k=pc/(2*e) if e else F(1,2)
   dense.append(d*k)
  Z=sum(dense);assert Z>0
  dense=[x/Z for x in dense]
  cp=[a*a for a in fourier(child)]
  raw=[F(0)]*len(Pc)
  # Two vacuum masses and one shared nonempty profile; derived separately.
  for c in range(2):
   e=P[c]+p[1<<i]/4; d=R[c]+R[2*(1<<i)]
   k=Pc[c]/(2*e) if e else F(1,2)
   raw[c]=d*k
  for t in range(1,len(cp)):
   a=insert(t,i,0);aa=a|(1<<i)
   k=cp[t]/(2*(p[a]+p[aa])) if p[a]+p[aa] else F(1,2)
   rr=(4*R[2*a]+4*R[2*aa])*k
   raw[2*t]=raw[2*t+1]=rr/4
  eq(sum(raw),Z);eq([x/Z for x in raw],dense)
  recurse(child,s,dense,[j-(j>i) for j in order[1:]])
def main():
 global trees
 pilot='--pilot' in sys.argv
 for n in range(3 if pilot else 4):
  for tab in range(1<<(1<<n)):
   vals=[1 if (tab>>x)&1 else -1 for x in range(1<<n)]
   orders=list(dict.fromkeys([tuple(range(n)),tuple(reversed(range(n)))]))
   for s in (-1,1):
    for order in orders:
     trees+=1;recurse(vals,s,fresh(vals,s),list(order))
 eq(22**56<2**31*15**56,True)
 eq(14**20<2**13*9**20,True)
 eq(F(31,56)+F(14,127)>F(13,20),True)
 eq(F(2,19)>F(27,280),True)
 eq(14**8>2**5*9**8,True)
 eq(F(31,56)+F(16,255)<F(5,8),True)
 for r in range(2,8):eq(F(31,56)+F(2*r,2**r-1)>F(13,20),True)
 result={'status':'PASS','pilot':pilot,'trees':trees,'nodes':nodes,'assertions':checks,'source_zero_kernel_rows':zero_rows,'seconds':time.perf_counter()-START,'arithmetic':'exact Fraction and formal logarithm dictionaries; integer certificates','full_FEI':'OPEN'}
 (ROOT/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
 print(json.dumps(result))
if __name__=='__main__':main()
