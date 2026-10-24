"""A017-five-control-good-coordinate-v1: exact normalized one-edge census."""
from pathlib import Path
import json,argparse,time,hashlib
R=Path(__file__).resolve().parents[1]
def walsh(g):
 w=g.copy();h=1
 while h<len(w):
  for j in range(0,len(w),2*h):
   for k in range(j,j+h):a,b=w[k],w[k+h];w[k],w[k+h]=a+b,a-b
  h*=2
 return w
def integer_good(w,i):
 P=Q=1;mass=0
 for s in range(32):
  if s>>i&1:continue
  a=w[s]**2;b=w[s|(1<<i)]**2;m=a+b
  if m:P*=m**m
  if a:Q*=a**a
  if b:Q*=b**b
  mass+=b
 return P<=(Q<<(4*mass)),P,Q,mass
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');z=ap.parse_args();start=time.perf_counter()
 count=256 if z.pilot else 32768;assertions=0;low=critical=high=0;digest=hashlib.sha256();maxbits=0
 for seed in range(count):
  a=[1]+[-1 if seed>>(x-1)&1 else 1 for x in range(1,16)]
  g=[a[x>>1] if x!=1 else -1 for x in range(32)]
  W=walsh(g);assert all(t%2==0 for t in W);w=[t//2 for t in W]
  mass=[sum(w[s]**2 for s in range(32) if s>>i&1) for i in range(5)]
  edge=[sum(g[x]!=g[x^(1<<i)] for x in range(32))*8 for i in range(5)]
  assert mass==edge and mass[0]==16 and sum(t*t for t in w)==256;assertions+=3
  i=max(range(5),key=lambda j:mass[j])
  if mass[i]<32:
   low+=1;assert mass==[16]*5 and sum(t==-1 for t in g) in [1,31];assertions+=1
  elif mass[i]==32:critical+=1
  else:high+=1
  ok,P,Q,m=integer_good(w,i);assert ok;assertions+=1;maxbits=max(maxbits,P.bit_length(),Q.bit_length()+4*m)
  digest.update(json.dumps([seed,i,mass]).encode()+b'\n')
 slacks={str(s):str((1<<(5*s-5))-s**s) for s in range(2,17)}
 assert all(int(v)>0 for v in slacks.values());assertions+=15
 result=dict(status='PASS',helper='A017-five-control-good-coordinate-v1',pilot=z.pilot,normalized_one_edge_cases=count,assertions=assertions,maximum_coordinate_classes=dict(point_defect=low,two_edge=critical,at_least_three_edges=high),chosen_K4_bad=0,max_comparison_integer_bits=maxbits,isoperimetric_cardinality_slacks=slacks,coverage_sha256=digest.hexdigest(),elapsed_seconds=time.perf_counter()-start)
 (R/'out'/('five_pilot.json' if z.pilot else 'five_certificate.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf8');print(json.dumps({k:v for k,v in result.items() if k!='isoperimetric_cardinality_slacks'}))
if __name__=='__main__':main()
