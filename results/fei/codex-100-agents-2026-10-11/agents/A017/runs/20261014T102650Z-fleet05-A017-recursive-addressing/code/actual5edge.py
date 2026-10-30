"""A017-actual-six-control-five-edge-v1: direct Boolean controls for odd lattice lemma."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import importlib.util,json,argparse,time,hashlib
R=Path(__file__).resolve().parents[1]
p=R.parent/'20261011T234546Z-fleet05-A017-recursive-addressing/code/check.py'
s=importlib.util.spec_from_file_location('u',p);U=importlib.util.module_from_spec(s);s.loader.exec_module(U)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');z=ap.parse_args();start=time.perf_counter();cases=checks=0;digest=hashlib.sha256();minones=32
 for code in U.graph_codes(5)[:1 if z.pilot else 4]:
  for ell in range(2 if z.pilot else 32):
   _,edges,_=U.parameters(5,code);a=U.signs(5,ell,edges)
   for shift in range(2 if z.pilot else 32):
    E={x^shift for x in [0,1,2,3,4]};b=[-v if x in E else v for x,v in enumerate(a)]
    g=[b[x>>1] if x&1 else a[x>>1] for x in range(64)]
    W=U.fwht(g);assert all(t%2==0 and (t//2)%2 for t in W);checks+=1;w=[t//2 for t in W]
    masses=[sum(w[s]**2 for s in range(64) if s>>i&1) for i in range(6)]
    assert masses==[sum(g[x]!=g[x^(1<<i)] for x in range(64))*16 for i in range(6)] and masses[0]==160;checks+=1
    ones=sum(abs(w[s])==1 for s in range(1,64,2));assert ones>=16;checks+=1;minones=min(minones,ones)
    P=Q=1
    for s in range(0,64,2):
     t,u=w[s]**2,w[s+1]**2;P*=(t+u)**(t+u);Q*=t**t*u**u
    assert P<(Q<<639);checks+=1
    digest.update(json.dumps([code,ell,shift,masses,ones]).encode()+b'\n');cases+=1
 result=dict(status='PASS',helper='A017-actual-six-control-five-edge-v1',pilot=z.pilot,cases=cases,assertions=checks,minimum_observed_magnitude_one_rows=minones,erasure_certificate='P < Q*2^639, hence B < 639/1024',coverage_sha256=digest.hexdigest(),elapsed_seconds=time.perf_counter()-start)
 (R/'out'/('actual5edge_pilot.json' if z.pilot else 'actual5edge_certificate.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf8');print(json.dumps(result))
if __name__=='__main__':main()
