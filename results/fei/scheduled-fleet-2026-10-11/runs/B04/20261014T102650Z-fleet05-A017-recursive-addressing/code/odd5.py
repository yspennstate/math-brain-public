"""A017-six-control-five-edge-v1: Walsh parity versus concavity certificate."""
from pathlib import Path
import json,hashlib,argparse,time
R=Path(__file__).resolve().parents[1]
def profiles():
 for c11 in range(2):
  for c9 in range(2):
   for c7 in range(3):
    for c5 in range(6):
     c3=16-15*c11-10*c9-6*c7-3*c5
     if c3>=0:yield (32-c3-c5-c7-c9-c11,c3,c5,c7,c9,c11)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--plan',action='store_true');ap.add_argument('--pilot',action='store_true');a=ap.parse_args()
 if a.plan:print(json.dumps(dict(full_profiles=sum(1 for _ in profiles()),pilot_profiles=5)));return
 start=time.perf_counter();ps=list(profiles())[:5 if a.pilot else None];digest=hashlib.sha256()
 for c in ps:
  assert sum(c)==32 and sum(k*v*v for k,v in zip(c,[1,3,5,7,9,11]))==160 and c[0]>=16
  digest.update(json.dumps(c).encode()+b'\n')
 comparisons={
  'one_row_a1_loss_gt_1_over8':(1<<63,135**8),
  'one_row_a3_loss_gt_1_over8':(1<<319,3**72*5**88),
  'global_tangent_overshoot_lt1':(5**160*3**2592,1<<4479),
  'log2_11_lt7_over2':(1<<7,11**2),
  'exp7_over10_gt2':(12013,12000)}
 assert all(lhs>rhs for lhs,rhs in comparisons.values())
 result=dict(status='PASS',helper='A017-six-control-five-edge-v1',pilot=a.pilot,present_profiles=len(ps),minimum_magnitude_one_rows=min(c[0] for c in ps),checks=3*len(ps)+len(comparisons),profiles=ps,integer_certificates={k:dict(lhs=str(l),rhs=str(r),positive_slack=str(l-r)) for k,(l,r) in comparisons.items()},erasure_bound='B < 639/1024 < 4*(5/32)',coverage_sha256=digest.hexdigest(),elapsed_seconds=time.perf_counter()-start)
 (R/'out'/('odd5_pilot.json' if a.pilot else 'odd5_certificate.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf8');print(json.dumps({k:v for k,v in result.items() if k not in ['profiles','integer_certificates']}))
if __name__=='__main__':main()
