"""A017-rank-two-collapse-v1: physical-coordinate exhaustive certificate."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import importlib.util,json,hashlib,time,argparse,itertools
from fractions import Fraction as F
R=Path(__file__).resolve().parents[1]
src=R.parent/'20261011T234546Z-fleet05-A017-recursive-addressing/code/check.py'
s=importlib.util.spec_from_file_location('u',src);U=importlib.util.module_from_spec(s);s.loader.exec_module(U)
checks=0
def req(v):
 global checks
 checks+=1
 if not v:raise AssertionError(checks)
def matrices():
 for graph in range(1024):
  ell,edges,Q=U.parameters(5,graph<<5)
  if U.rank(Q)==2:yield graph,edges,Q
def cases(pilot=False):
 for graph,edges,Q in list(matrices())[:3 if pilot else 155]:
  dummy=[i for i in range(5) if not Q[i]]
  cosets={tuple(U.parity(row&z) for row in Q):z for z in range(32)}
  for signature,z in sorted(cosets.items()):
   A=[w for w in range(32) if all(U.parity(Q[i]&w)==signature[i] for i in range(5))]
   for mask in range(1<<len(dummy)):
    ell=sum((1^signature[i])<<i for i in range(5) if Q[i])
    for j,i in enumerate(dummy):ell|=((mask>>j)&1)<<i
    for v in A:yield graph,edges,Q,ell,z,A,v
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');ap.add_argument('--plan',action='store_true');args=ap.parse_args()
 if args.plan:
  print(json.dumps(dict(rank_two_matrices=sum(1 for _ in matrices()),pilot_cases=sum(1 for _ in cases(True)),full_cases=sum(1 for _ in cases()))));return
 start=time.perf_counter();digest=hashlib.sha256();count=0
 for graph,edges,Q,ell,z,A,v in cases(args.pilot):
  i,j=next((i,j) for i in range(5) for j in range(i+1,5) if Q[i]>>j&1)
  a,b=Q[i],Q[j]
  req(all(((Q[k]>>m)&1)==(((a>>k&1)*(b>>m&1))^((b>>k&1)*(a>>m&1))) for k in range(5) for m in range(5)))
  req(len(A)==8)
  base=U.signs(5,ell,edges);J=[(1^U.parity(a&(x^z)))*(1^U.parity(b&(x^z))) for x in range(32)]
  req([x for x in range(32) if J[x]]==A)
  affine=[base[x]*(-1)**J[x] for x in range(32)]
  char=sum((affine[0]!=affine[1<<k])<<k for k in range(5))
  req(all(not (char>>k&1) for k in range(5) if Q[k]))
  req(all(affine[x]==affine[0]*(-1)**U.parity(char&x) for x in range(32)))
  E=set(A)-{v};g=[base[x]*(-1 if x in E else 1) for x in range(32)]
  req(all(g[x]==affine[0]*(-1)**U.parity(char&x)*(-1 if x==v else 1) for x in range(32)))
  direct=[F(sum(g[x]!=g[x^(1<<k)] for x in range(32)),32) for k in range(5)]
  req(direct==[F(15,16) if char>>k&1 else F(1,16) for k in range(5)])
  W=U.fwht(g);req(sorted(w*w for w in W)==[4]*31+[900])
  req(all(direct[k]==F(1,16) for k in range(5) if Q[k]))
  digest.update(json.dumps([graph,ell,z,v,char]).encode()+b'\n');count+=1
 result=dict(status='PASS',helper='A017-rank-two-collapse-v1',pilot=args.pilot,cases=count,assertions=checks,rank_two_matrices=155,rank_four_matrices=868,coverage_sha256=digest.hexdigest(),elapsed_seconds=time.perf_counter()-start,physical_relabeling=False,shared_data_labels_replaced=False)
 (R/'out'/('collapse_pilot.json' if args.pilot else 'collapse_certificate.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf8');print(json.dumps(result))
if __name__=='__main__':main()
