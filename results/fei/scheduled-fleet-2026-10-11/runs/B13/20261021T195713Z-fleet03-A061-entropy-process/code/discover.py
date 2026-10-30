import math,json,time
from pathlib import Path

R=Path(__file__).resolve().parents[1]
def fw(a):
 a=list(a);h=1
 while h<len(a):
  for k in range(0,len(a),2*h):
   for j in range(k,k+h):a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
  h*=2
 return a
def ent(p):return -sum(x*math.log2(x) for x in p if x)
def hb(x):return ent([x,1-x])
def stats(a):
 n=(len(a)-1).bit_length();N=len(a);p=[x*x/(N*N) for x in fw(a)]
 d=[sum(x for s,x in enumerate(p) if s>>i&1) for i in range(n)]
 return p,d,sum(hb(x) for x in d)-ent(p)
def child(a,i,b):return [a[(s&((1<<i)-1))|((s>>i)<<(i+1))|(b<<i)] for s in range(len(a)//2)]
def check(a,i):
 p,d,K=stats(a);n=len(d);cs=[stats(child(a,i,b)) for b in [0,1]]
 pe=[p[(s&((1<<i)-1))|((s>>i)<<(i+1))]+p[(s&((1<<i)-1))|((s>>i)<<(i+1))|(1<<i)] for s in range(len(a)//2)]
 ids=[j for j in range(n) if j!=i];Q=[math.prod(d[j] if s>>k&1 else 1-d[j] for k,j in enumerate(ids)) for s in range(len(pe))]
 rr=[sum(Q[s]*(cs[b][0][s]/(2*pe[s]) if pe[s] else .5) for s in range(len(pe))) for b in [0,1]]
 O=-.5*math.log2(4*rr[0]*rr[1]);D=O+(cs[0][2]+cs[1][2])/2-K
 J=ent(pe)-(ent(cs[0][0])+ent(cs[1][0]))/2
 return dict(D=D,O=O,J=J,gap=D-J,d=d[i],r=rr,K=K)
def main():
 import sys
 domain=[int(x) for x in sys.argv[1:]] or [1,2,3]
 start=time.perf_counter();count=0;best=(-1,None);maxratio=(-1,None);records=[]
 for n in domain:
  for mask in range(1<<(1<<n)):
   a=[1 if mask>>s&1 else -1 for s in range(1<<n)]
   for i in range(n):
    v=check(a,i);count+=1;v.update(n=n,mask=mask,i=i)
    if v['gap']>best[0]:best=(v['gap'],v)
    if v['d'] and v['D']/v['d']>maxratio[0]:maxratio=(v['D']/v['d'],v)
    if v['gap']>1e-9 and len(records)<10:records.append(v)
   if time.perf_counter()-start>55:raise RuntimeError('frozen runtime exceeded')
 out=dict(count=count,seconds=time.perf_counter()-start,max_gap=best[1],max_D_per_d=maxratio,first_failures=records,arithmetic='FLOAT DISCOVERY ONLY')
 (R/'out').mkdir(exist_ok=True);(R/'out'/('DISCOVERY_'+''.join(map(str,domain))+'.json')).write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
if __name__=='__main__':main()
