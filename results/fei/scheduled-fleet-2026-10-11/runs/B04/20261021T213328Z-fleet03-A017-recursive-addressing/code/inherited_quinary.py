"""A017-six-control-affine-four-edge-v1: actual four-point affine child disagreement."""
from pathlib import Path
import json,itertools,time,hashlib,argparse
R=Path(__file__).resolve().parents[1]
def walsh(g):
 w=g.copy();h=1
 while h<len(w):
  for j in range(0,len(w),2*h):
   for k in range(j,j+h):a,b=w[k],w[k+h];w[k],w[k+h]=a+b,a-b
  h*=2
 return w
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');z=ap.parse_args();start=time.perf_counter();bad=count=0;digest=hashlib.sha256();first=None;best=None
 it=itertools.product([-2,-1,0,1,2],repeat=7)
 if z.pilot:it=itertools.islice(it,125)
 for tail in it:
  H=[2]+list(tail);A=[t-2 for t in walsh(H)];P=Q=1
  for a in A:
   t=a*a;P*=(t+4)**(t+4);Q*=4**4
   if t:Q*=t**t
  ok=P<=(Q<<128)
  if not ok:
   bad+=1
   if first is None:
    # a(t,z) has2+H(z) positive values in each four-vertex t slice.
    child=[1 if (x&3)<2+H[x>>2] else -1 for x in range(32)]
    g=[(-child[x>>1] if (x&1 and (x>>3)==0) else child[x>>1]) for x in range(64)]
    W=walsh(g);pairsP=pairsQ=1;mass=0
    for s in range(0,64,2):
     a,b=W[s]//4,W[s+1]//4;t,u=a*a,b*b;mass+=u
     if t+u:pairsP*=(t+u)**(t+u)
     if t:pairsQ*=t**t
     if u:pairsQ*=u**u
    assert (P,Q)==(pairsP,pairsQ) and mass==32
    first=dict(projected_H=H,actual_six_control_truth=g,integer_certificate=dict(P=str(P),Q_times2_power128=str(Q<<128),positive_slack=str(P-(Q<<128))))
  if best is None or P*best[1]>best[0]*Q:best=(P,Q,H)
  digest.update(json.dumps([H,ok]).encode()+b'\n');count+=1
 result=dict(status='PASS',helper='A017-six-control-affine-four-edge-v1',pilot=z.pilot,quinary_cases=count,K4_bad=bad,maximum_profile=best[2],maximum_ratio_integer_form=dict(P=str(best[0]),Q=str(best[1])),first_bad_actual_Boolean=first,coverage_sha256=digest.hexdigest(),elapsed_seconds=time.perf_counter()-start)
 (R/'out'/('quinary_pilot.json' if z.pilot else 'quinary_certificate.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf8');print(json.dumps({k:v for k,v in result.items() if k not in ['maximum_ratio_integer_form','first_bad_actual_Boolean']}))
if __name__=='__main__':main()
