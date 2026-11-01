import json,math,pathlib,time
from fractions import Fraction as Q
from decimal import Decimal,getcontext
import numpy as np
import networkx as nx
from scipy.stats import norm
start=time.time();getcontext().prec=40
q=Q(8,9);r=3;d=4
f=lambda x:3*x*x-2*x*x*x
h=lambda x:q*(4*x**3-3*x**4)
x1=q*f(q);h1=h(q);h2=h(x1)
A2=3*q*q-2*q**3;A3=q**3;mass2=3*q*q*(1-q)
sigma1=h1*(1-h1)+4*(q*q*A2*A2-h1*h1)+12*q**3*(1-q)*mass2**2
z=Decimal(5)/36;a=Decimal(4)/3;b=Decimal(16)/9;rec_upper=Decimal(1152)/569;alpha=Decimal(36)/5
rec=[]
for t in range(100001):
 assert 1/(alpha+rec_upper*t)-Decimal('1e-32')<=z<=1/(alpha+a*t)+Decimal('1e-32')
 if t in [0,1,4,16,64,256,1024,10000,100000]:rec.append(dict(t=t,z=float(z),t_z=float(t*z),drift=float(a*z*z+b*z*z*z)))
 z=z-a*z*z-b*z*z*z
# Exact local mean after TWO rounds: enumerate only exceptional overlapping two-hop neighbourhoods.
def local_h2(adj,v):
 ns=adj[v];vs=sorted({v,*ns,*[u for w in ns for u in adj[w]]})
 if len(vs)==17:return h2,False
 ind={u:i for i,u in enumerate(vs)};L=len(vs);masks=np.arange(1<<L,dtype=np.uint32)
 occupied_root=((masks>>ind[v])&1).astype(bool);count=np.zeros(len(masks),dtype=np.uint8)
 for w in ns:
  own=((masks>>ind[w])&1).astype(bool)
  deg=sum(((masks>>ind[u])&1).astype(np.uint8) for u in adj[w])
  count+=own&(deg>=3)
 valid=occupied_root&(count>=3)
 pc=np.zeros(len(masks),dtype=np.uint8)
 for j in range(L):pc+=((masks>>j)&1).astype(np.uint8)
 hist=np.bincount(pc[valid],minlength=L+1)
 prob=Q(sum(int(hist[j])*8**j for j in range(L+1)),9**L)
 return prob,True
rng=np.random.default_rng(89012);rows=[]
for n in [64,256,1024]:
 for j in range(6):
  G=nx.random_regular_graph(4,n,seed=89012+1000*n+j);adj=[sorted(G[v]) for v in range(n)];arr=np.array(adj,dtype=np.int32)
  mu2=Q(0);bad=0
  for v in range(n):
   hv,badv=local_h2(adj,v);mu2+=hv;bad+=badv
  h1samples=[];h2samples=[]
  for _ in range(8):
   initial=rng.random((256,n))<float(q)
   step1=initial&(initial[:,arr].sum(axis=2)>=3)
   step2=step1&(step1[:,arr].sum(axis=2)>=3)
   h1samples.extend(step1.sum(axis=1).tolist());h2samples.extend(step2.sum(axis=1).tolist())
  h1samples=np.array(h1samples);Z=(h1samples-n*float(h1))/math.sqrt(n)
  rows.append(dict(n=n,graph=j,overlap_roots=bad,exact_mean_h1=float(n*h1),exact_mean_h2=float(mu2),exact_mean_h2_error=float(mu2-n*h2),sample_mean_h1=float(np.mean(h1samples)),sample_variance_h1_over_n=float(np.var(h1samples,ddof=1)/n),predicted_sigma1_squared=float(sigma1),cdf_h1_zero=float(np.mean(Z<=0)),cdf_h1_one_sigma=float(np.mean(Z<=math.sqrt(float(sigma1)))),sample_mean_h2=float(np.mean(h2samples)),samples=2048))
 out=dict(q=str(q),h1=str(h1),h2=str(h2),sigma1_squared=str(sigma1),recursion=rec,graphs=rows,elapsed=time.time()-start)
 pathlib.Path('second_experiments.json').write_text(json.dumps(out,indent=2),encoding='utf8')
 print('completed n',n,'mean_h2_errors',[round(x['exact_mean_h2_error'],6) for x in rows if x['n']==n],flush=True)
print('recursion',rec)
print('sigma1',sigma1,float(sigma1),'elapsed',time.time()-start)
