from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,importlib.util,json,time
HERE=Path(__file__).resolve().parent.parent
s=importlib.util.spec_from_file_location('obstruction',HERE/'code'/'obstruction.py');o=importlib.util.module_from_spec(s);s.loader.exec_module(o)
old=HERE.parent/'20261022T211502Z-fleet03-A068-antichain-beyond-one-order'/'code'/'verify.py'
assert hashlib.sha256(old.read_bytes()).hexdigest()=='af436c9eaac4e0f2617d170517f163636ef03d669d83b7e93ca41ee3f0fde5d0'
s=importlib.util.spec_from_file_location('arithmetic',old);a=importlib.util.module_from_spec(s);s.loader.exec_module(a)
def rank(rows,k):
 rows=list(rows);r=0
 for j in range(k):
  p=next((z for z in range(r,k) if rows[z]>>j&1),None)
  if p is None:continue
  rows[r],rows[p]=rows[p],rows[r]
  for z in range(r+1,k):
   if rows[z]>>j&1:rows[z]^=rows[r]
  r+=1
 return r
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');args=ap.parse_args()
 start=time.monotonic();candidates=admitted=0;rows=[]
 for k in range(1,(2 if args.pilot else 8)+1):
  L=1<<k;rho=F(1,L);N=2*(L-1);eps=F(1,1<<L)
  q=[F(1,2)+eps/N,F(1,2)-eps+eps/N]+[2*eps/N]*(L-2)
  expected=[q[0]]+[(1-q[0])/(L-1)]*(L-1)
  if k<=3:
   total=[F(0)]*L;count=0
   for code in range(1<<(k*k)):
    candidates+=1;matrix=[(code>>(k*j))&(L-1) for j in range(k)]
    if rank(matrix,k)!=k:continue
    count+=1;admitted+=1;images=[]
    for z in range(L):
     image=sum(((row&z).bit_count()%2)<<j for j,row in enumerate(matrix));images.append(image)
     a.check((z==0)==(image==0),'actual AND point-defect function invariant')
     total[image]+=q[z]
    a.check(len(set(images))==L,'source frequency map is a permutation')
   average=[v/count for v in total]
   a.check(average==expected,'literal ORIGINAL source GL average exact')
  child=[(1-2*rho)**2]+[4*rho*rho]*(L-1)
  calibrated=[child[0]]+[(1-child[0])*v/(1-expected[0]) for v in expected[1:]]
  a.check(calibrated==child,'orbit return and vacuum calibration equals actual spectrum')
  physical=[1]+[-1]*(L-1)
  a.check([v*v for v in o.direct_walsh(physical)]==child,'independent physical child Walsh')
  I=sum(o.influence(physical));a.check(I==2*k*rho,'physical child influence')
  H=a.entropy(child)
  a.nonnegative(a.combine((1,{2:4*I}),(-1,H)),'orbit source full cost <=4I')
  # The positive child is constant and has zero full terminal bill.
  a.nonnegative(a.combine((1,{2:5*I/2-I/2}),(F(-1,2),H)),'SAME root rate5 leaves >=old remaining influence')
  rows.append({'k':k,'new_full_reference':'exact AND spectrum via original-source GL averaging and vacuum calibration','both_child_average_I':str(I/2),'same_rate5_remainder_lower':str(I/2)})
  if time.monotonic()-start>30:raise RuntimeError('frozen runtime exhausted')
 result={'status':'PASS','pilot':args.pilot,'child_cases':len(rows),'matrix_candidates':candidates,'invertible_matrices':admitted,'assertions':a.CHECKS,'certified_log_signs':len(a.SIGN_CACHE),'seconds':time.monotonic()-start,'rows':rows,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
 path=HERE/'out'/('orbit_pilot.json' if args.pilot else 'orbit.json');path.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
if __name__=='__main__':main()
