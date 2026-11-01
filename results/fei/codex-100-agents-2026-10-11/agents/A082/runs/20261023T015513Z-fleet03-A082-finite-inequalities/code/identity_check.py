from pathlib import Path
import sys,json,time
import exact as E
from exact import F
ROOT=Path(__file__).resolve().parents[1]
def main():
 start=time.perf_counter();pilot='--pilot' in sys.argv;algebra=physical=negative_coefficient=0
 grid=[F(k,4) for k in range(5)]
 for a in range(9):
  for b in range(9-a):
   for c in range(9-a-b):
    R=tuple(F(x,8) for x in (a,b,c,8-a-b-c))
    for p in grid:
     if R[0]==1 and p!=1:continue
     C=E.calibrate(R,p)
     for j in (0,1):
      O=E.marginal(R,j);V=E.marginal(C,j)
      for q in grid:
       if q<1 and (p==1 or O[0]==1 or V[0]==1):continue
       E.ck(E.calibrate(V,q)==E.calibrate(O,q));algebra+=1
       if p<1 and p<R[0]:negative_coefficient+=1
 for code in range(16 if pilot else 256):
  f=tuple(-1 if code>>x&1 else 1 for x in range(8));P=E.spectrum(f)
  for R in E.references(P):
   for j in range(3):
    O=E.marginal(R,j)
    for v in (0,1):
     g=E.child(f,j,v);C=E.calibrate(O,E.spectrum(g)[0])
     for k in range(2):
      U=E.marginal(O,k);V=E.marginal(C,k)
      for w in (0,1):
       gg=E.child(g,k,w);q=E.spectrum(gg)[0]
       E.ck(E.calibrate(U,q)==E.calibrate(V,q));physical+=1
  if time.perf_counter()-start>60:raise RuntimeError('identity frozen60second cap')
 # Real negative arm: omit final calibration and equality fails.
 R=(F(1,4),)*4;p=F(1,2);q=F(1,4)
 O=E.marginal(R,0);V=E.marginal(E.calibrate(R,p),0)
 E.ck(V!=E.calibrate(O,q));E.ck(E.calibrate(V,q)==E.calibrate(O,q))
 control=dict(original=list(map(str,R)),first_calibrated_marginal=list(map(str,V)),direct_final_calibrated=list(map(str,E.calibrate(O,q))),conclusion='final calibration is essential; the omitted-final-calibration negative arm fails equality')
 out=dict(status='PASS',pilot=pilot,algebraic_admissible_cases=algebra,physical_two_query_histories=physical,alpha_greater_than_one_cases=negative_coefficient,assertions=E.ASSERTIONS,negative_control=control,elapsed_seconds=time.perf_counter()-start)
 (ROOT/('out/IDENTITY_PILOT.json' if pilot else 'out/IDENTITY_CHECK.json')).write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k!='negative_control'}))
if __name__=='__main__':main()
