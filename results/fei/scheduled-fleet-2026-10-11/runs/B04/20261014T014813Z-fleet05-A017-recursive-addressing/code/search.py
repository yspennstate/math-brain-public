"""A017-three-edit-v1; exact frozen D=4 polar-pivot census."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import importlib.util,json,time,itertools,hashlib,argparse
from fractions import Fraction as F
R=Path(__file__).resolve().parents[1]
old=R.parent/'20261011T234546Z-fleet05-A017-recursive-addressing/code/check.py'
sp=importlib.util.spec_from_file_location('exact',old);U=importlib.util.module_from_spec(sp);sp.loader.exec_module(U)
checks=0;cache={};bcache={};digest=hashlib.sha256()
def req(x,msg=''):
 global checks
 checks+=1
 if not x:raise AssertionError((checks,msg))
def data(bits):
 if bits not in cache:
  g=[1-2*((bits>>x)&1) for x in range(16)];w=U.fwht(g)
  edge=[sum(g[x]!=g[x^(1<<i)] for x in range(16)) for i in range(4)]
  req(edge==[sum(a*a for s,a in enumerate(w) if s>>i&1)//16 for i in range(4)],'physical and spectral influence')
  cache[bits]=(tuple(w),tuple(edge))
 return cache[bits]
def B(bits,i):
 key=(bits,i)
 if key not in bcache:bcache[key]=U.erasure({0:data(bits)[0]},4,i)
 return bcache[key]
def main():
 start=time.perf_counter();ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');a=ap.parse_args()
 codes=[g|l for g in U.graph_codes(4) for l in range(16)] if a.pilot else range(1024)
 roots=polar=bad=critical=0;witness=[]
 for code in codes:
  l,edges,Q=U.parameters(4,code);base=U.signs(4,l,edges);bb=sum((x<0)<<j for j,x in enumerate(base));bw=U.fwht(base)
  for u,v in itertools.combinations(range(1,16),2):
   bits=bb^1^(1<<u)^(1<<v);ws,inf=data(bits)
   for s,w in enumerate(ws):req(w==bw[s]-2*sum(base[x]*(-1)**U.parity(s&x) for x in [0,u,v]),'signed three-edit amplitude')
   roots+=1
   for i in range(4):
    if not Q[i]:continue
    polar+=1
    if inf[i]>=4:continue
    req(inf[i]==2,'odd edge-count minimum at D4');critical+=1
    entropy=B(bits,i);margin=U.LF().add(entropy).add(U.LF(F(inf[i],4)),-1)
    lo,hi=margin.interval();req(lo>0 or hi<=0,'exact sign resolved')
    if lo>0:
     bad+=1
     if len(witness)<12:
      C=F(sum(2*s.bit_count()*w*w for s,w in enumerate(ws) if s>>i&1),256)
      witness.append(dict(qcode=code,linear=l,edges=edges,edits=[0,u,v],truth_negative_bits=bits,coordinate=i,influence=str(F(inf[i],16)),erasure=entropy.json(),K4_excess=margin.json(),boundary=str(C),walsh=list(ws)))
   digest.update(f'{code},{u},{v},{bits}\n'.encode())
 out=dict(status='PASS',helper='A017-three-edit-v1',pilot=a.pilot,roots=roots,polar_coordinates=polar,critical_influence_eighth=critical,K4_bad_polar_coordinates=bad,unique_truth_tables=len(cache),assertions=checks,utility_assertions=U.CHECKS,elapsed_seconds=time.perf_counter()-start,coverage_sha256=digest.hexdigest(),witnesses=witness)
 (R/'out'/('pilot.json' if a.pilot else 'census.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf8');print(json.dumps({k:v for k,v in out.items() if k!='witnesses'}))
if __name__=='__main__':main()
