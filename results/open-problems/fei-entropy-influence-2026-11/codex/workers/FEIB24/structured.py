import json,math,itertools,hashlib,os,resource,time
from pathlib import Path
import numpy as np
from analysis import evaluate,table_from_hex,wht,phi,minterms
start=time.time();rows=[];best={};rng=np.random.default_rng(241111)
Path('witnesses').mkdir(exist_ok=True)
def save(tag,f,extra=None):
 s=evaluate(f);s['tag']=tag
 if extra:s.update(extra)
 rows.append(s)
 n=s['n']
 if n not in best or s['minratio']>best[n]['minratio']:
  fn='witnesses/structured_n%d.npz'%n;np.savez_compressed(fn,f=np.asarray(f,dtype=np.int8));best[n]=dict(s,witness=fn)
 print(tag,'n',n,'min',round(s['minratio'],10),'HI',round(s['HI'],10),'EI',round(s['EI'],10),flush=True)
 return s

def hidden(k,m=1):
 n=k*m+1;N=1<<n;ix=np.arange(N);ys=[]
 for j in range(k):
  wt=np.zeros(N,dtype=np.uint8)
  for t in range(m):wt+=(ix>>(j*m+t)&1).astype(np.uint8)
  ys.append(wt>m//2)
 maj=sum(y.astype(np.uint8) for y in ys)>k//2
 ge=np.ones(N,dtype=bool)
 for j in range(k//2):ge&=ys[j]
 return np.where(maj|((ix>>(n-1)&1==1)&ge),1,-1)

def compose(outer,inner):
 k=len(outer).bit_length()-1;m=len(inner).bit_length()-1;n=k*m
 ix=np.arange(1<<n);o=np.zeros(len(ix),dtype=np.int32)
 for j in range(k):o|=(inner[(ix>>(j*m))&((1<<m)-1)]>0).astype(np.int32)<<j
 return outer[o]

def threshold(n,t):
 return np.array([1 if x.bit_count()>=t else -1 for x in range(1<<n)],dtype=np.int8)

def dnf(n,terms):
 ix=np.arange(1<<n);v=np.zeros(len(ix),dtype=bool)
 for t in terms:v|=(ix&t)==t
 return np.where(v,1,-1)

for r in map(json.loads,open('hill_records.jsonl')):
 n=r['n'];f=dnf(n,r['minterms']);s=evaluate(f)
 assert abs(s['minratio']-r['minratio'])<2e-12
 if n not in best or s['minratio']>best[n]['minratio']:
  np.savez_compressed(f'witnesses/hill_n{n}.npz',f=f.astype(np.int8))
  best[n]=dict(s,minterms=r['minterms'],witness=f'witnesses/hill_n{n}.npz')
json.dump(best,open('hill_audit.json','w'),indent=2)
# Genuine separate samples at n=7, a specified distribution over monotone DNFs.
for t in range(2000):
 n=7;width=int(rng.integers(2,6));count=int(rng.integers(1,19));terms=[]
 for j in range(count):terms.append(sum(1<<int(i) for i in rng.choice(n,width,replace=False)))
 f=dnf(n,terms);s=evaluate(f)
 if t==0:samplebest=dict(s,minterms=terms,draw=t)
 if s['minratio']>samplebest['minratio']:samplebest=dict(s,minterms=terms,draw=t)
json.dump(dict(seed=241111,draws=2000,distribution='width uniform in 2..5, term count uniform in 1..18; terms iid uniform fixed-width subsets',best=samplebest),open('sample7.json','w'),indent=2)
for k in range(1,20,2):save(f'hidden_{k}',hidden(k),dict(k=k,m=1,delta=2.**-k))
for k,m in [(3,3),(3,5),(5,3)]:save(f'hidden_{k}_maj{m}',hidden(k,m),dict(k=k,m=m,delta=2.**-k))
for b in range(2,8):
 for m in range(2,8):
  if b*m>20:continue
  for t in sorted(set([1,(b+1)//2,b])):
   for q in sorted(set([1,m])):
    save(f'thr{b}_{t}_thr{m}_{q}',compose(threshold(b,t),threshold(m,q)),dict(b=b,m=m,t=t,q=q))
# Outer six-variable census extremizers composed with balanced majority on disjoint blocks.
cs=json.load(open('census_summary.json'))
for key in ['minratio','EI','HI']:
 f=table_from_hex(cs['6'][key]['truth_hex'],6)
 save(f'census6_{key}_maj3',compose(f,threshold(3,2)))
# A reproducible local previously saved 18-variable seed: independently re-evaluate and verify monotonicity.
for name in ['n18_balanced','n18_AI']:
 f=np.load('../FEIB03/witnesses/'+name+'.npz')['f'].astype(np.int64)
 # Earlier worker uses the opposite output sign. Orient monotonically before audit.
 if f[0]>f[-1]:f=-f
 s=save('inherited_'+name,f,dict(source='../FEIB03/witnesses/'+name+'.npz',source_sha256=hashlib.sha256(Path('../FEIB03/witnesses/'+name+'.npz').read_bytes()).hexdigest()))
 np.savez_compressed('witnesses/'+name+'.npz',f=f.astype(np.int8))
for n in [7,10,12,14,16,18,20]:
 for t in range(12):
  width=int(rng.integers(2,min(n,7)));count=int(rng.integers(2,3*n+1));terms=[]
  for j in range(count):terms.append(sum(1<<int(i) for i in rng.choice(n,width,replace=False)))
  save(f'random_dnf_{n}_{t}',dnf(n,terms),dict(minterms=terms))
json.dump(rows,open('structured.json','w'),indent=2)
json.dump(best,open('search_best.json','w'),indent=2)
json.dump(dict(elapsed_seconds=time.time()-start,peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,nice=os.getpriority(os.PRIO_PROCESS,0),threads=1,rows=len(rows)),open('structured_resources.json','w'),indent=2)
