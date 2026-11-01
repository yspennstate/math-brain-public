from pathlib import Path
import sys,time,json
from arithmetic import Q,h2,sub,scale,dump
from audit import influence,restrict,mu
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'out'
start=time.monotonic();checks=0
def ck(ok,msg):
 global checks
 checks+=1
 if not ok:raise AssertionError(msg)
 if time.monotonic()-start>55:raise RuntimeError('frozen55 second limit')
def P(t):return 2*(1-t*t)
def C(t):return sub(scale(2,h2((1+t)/2)),scale(Q(1,2),h2(t*t)))
def main():
 pilot='--pilot' in sys.argv;count=16 if pilot else 256;means=range(0,257,16) if pilot else range(257)
 rows=0;zero=0
 for mask in range(count):
  g=[1-2*((mask>>x)&1) for x in range(8)];m=mu(g);p=P(m)
  ck(p<=2*influence(g),'all physical influence price via Poincare')
  if m not in (-1,0,1):ck(C(m)[1]<p,'strict correction majorant on actual core')
  else:ck({Q(-1):0,Q(0):2,Q(1):0}[m]==p,'exact equality at symmetric endpoints')
  for j in range(3):
   mm=[mu(restrict(g,j,b)) for b in range(2)]
   drop=p-(P(mm[0])+P(mm[1]))/2
   ck(drop==(mm[0]-mm[1])**2/2,'exact variance-envelope physical drift')
   ck(drop>=0,'coherence under arbitrary core query');rows+=1;zero+=int(drop==0)
  ck(p>=0,'y query kills correction envelope on both full outcomes');rows+=1
 tested=0
 for j in means:
  t=Q(j,128)-1;tested+=1
  if t not in (-1,0,1):ck(C(t)[1]<P(t),'positive dyadic majorant gap')
 result={'status':'PASS','pilot':pilot,'actual_three_bit_cores':count,'physical_query_pairs':rows,'zero_core_drift_rows':zero,'dyadic_means':tested,'checked_assertions':checks,'runtime_seconds':time.monotonic()-start,'universal_scope':'Analytic PROOF.md section6, every Boolean core dimension. Finite grid is corroboration only.','universal_envelope':'2Var(g), while y free;0 after y fixed','ordinary_full_FEI':'OPEN'}
 dump(OUT/('VARIANCE_PILOT.json' if pilot else 'VARIANCE_ENVELOPE.json'),result);print(json.dumps(result,indent=2))
if __name__=='__main__':main()
