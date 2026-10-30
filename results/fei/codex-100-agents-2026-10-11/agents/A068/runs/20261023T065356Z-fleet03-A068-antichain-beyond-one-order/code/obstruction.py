"""Exact certificates for an inherited-source, nonempty-profile obstruction."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json,time
HERE=Path(__file__).resolve().parent.parent
START=time.monotonic();CHECKS=0
def check(x,label):
 global CHECKS
 CHECKS+=1
 if not x:raise AssertionError(label)
def influence(truth):
 n=(len(truth)-1).bit_length()
 return [F(sum(truth[x]!=truth[x^(1<<j)] for x in range(len(truth))),len(truth)) for j in range(n)]
def direct_walsh(truth):
 # Independent of the previous stages' fast Walsh implementation.
 return [F(sum(value*(-1 if (x&s).bit_count()%2 else 1) for x,value in enumerate(truth)),len(truth)) for s in range(len(truth))]
def formula(k,physical):
 L=1<<k;rho=F(1,L);M=L-1;N=2*M;eps=F(1,1<<L)
 main=F(1,2);heavy=F(1,2)-eps;small=eps/N
 check(main+heavy+N*small==1,'original reference normalized')
 check(main>0 and heavy>=F(1,4) and small>0,'full exact support no ghost')
 # log(1/heavy)<=2, log N<k+1 and -log eps=L imply
 # rootCE strictly below this rational envelope.
 restmass=N*rho*rho
 envelope=(1-rho)**2+2*rho*rho+restmass*(L+k+1)
 Iroot=1+(k-1)*rho
 check(k+1<=L,'all-dimensional logarithm envelope premise')
 check(envelope<5<=5*Iroot,'root complete cost strictly below5I')
 t=F(1,2)-small # inherited nonempty source mass after x exposure
 check(t>=F(1,4),'nonempty inherited normalizer bounded below')
 qheavy=(heavy+small)/t;qsmall=2*small/t
 check(qheavy+(M-1)*qsmall==1,'same original nonempty conditional law')
 check(qheavy<=1,'heavy contribution to KL at least-log(M)/M')
 check(F(1,M)/qsmall>=F(1<<max(0,L-2)),'each other actual/source likelihood ratio at least2^(L-2)')
 v=4*rho*(1-rho)
 dlower=F((M-1)*(L-2)-k,M)
 childlower=v*dlower
 Ichild=2*k*rho
 frontierlower=childlower/2
 deficit25=frontierlower-25*Ichild/2
 if k>=3:
  check(2*k<=L,'linear k at most half exponential L')
  check(dlower>=F(L,2),'genuine nonempty KL at least2^(k-1)')
  check(childlower>=2*(1-rho)>=F(7,4),'calibrated full cost bounded below while influence vanishes')
 if k==8:check(deficit25==F(9727,8192),'explicit one-query full-bank deficit certificate')
 if physical:
  # Physical spin is (-1)^bit: bit0 represents +1, consistently with Walsh.
  truth=[1 if ((z&1)==0 or (z>>1)==0) else -1 for z in range(2*L)]
  coeff=direct_walsh(truth)
  for s,c in enumerate(coeff):
   predicted=1-rho if s==1 else (-rho if s&1 else rho)
   check(c==predicted,'physical Walsh formula')
  inf=influence(truth)
  check(inf==[1-rho]+[rho]*k,'all coordinates relevant physical influence')
  check(sum(inf)==Iroot,'root influence formula')
  Q=[small]*(2*L);Q[1]=main;Q[2]=heavy
  check(sum(Q)==1 and all(Q),'full inherited source')
  marginal=[Q[2*s]+Q[2*s+1] for s in range(L)]
  check(marginal[0]==F(1,2)+small,'literal frequency marginal vacuum')
  check(marginal[1]==heavy+small,'literal marginal heavy nonempty atom')
  check(all(marginal[s]==2*small for s in range(2,L)),'remaining inherited nonempty atoms')
  child=truth[1::2]
  chat=direct_walsh(child)
  check(chat==[2*rho-1]+[2*rho]*(L-1),'actual negative child AND spectrum')
  check(sum(influence(child))==Ichild,'actual negative child influence')
  check(truth[::2]==[1]*L,'positive child truly constant')
  vac=(1-2*rho)**2
  calibrated=[vac]+[(1-vac)*q/t for q in marginal[1:]]
  check(sum(calibrated)==1,'optimal vacuum-only calibrated reference normalized')
  check(calibrated[0]==chat[0]**2,'actual empty mass matched')
  check(calibrated[1]/v==qheavy,'nonempty heavy profile survives calibration')
  check(all(z/v==qsmall for z in calibrated[2:]),'nonempty small profile survives calibration')
 return {'k':k,'physical':physical,'root_I':str(Iroot),'root_CE_upper_strict':str(envelope),'child_I':str(Ichild),'conditional_nonempty_KL_lower':str(dlower),'child_full_CE_lower':str(childlower),'frontier_full_CE_lower':str(frontierlower),'frontier_minus_rate25_lower':str(deficit25),'positive_rate25_deficit_certified':deficit25>0}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');args=ap.parse_args()
 rows=[];result={'status':'RUNNING','pilot':args.pilot}
 try:
  for k in range(1,(4 if args.pilot else 16)+1):
   rows.append(formula(k,k<=8))
   if time.monotonic()-START>45:raise RuntimeError('frozen runtime exhausted')
  result.update(status='PASS',rows=rows,formula_cases=len(rows),physical_cases=sum(row['physical'] for row in rows))
 except Exception as exc:
  result.update(status='FAIL',error=repr(exc),rows=rows);raise
 finally:
  result.update(assertions=CHECKS,seconds=time.monotonic()-START,helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
  dest=HERE/'out';dest.mkdir(exist_ok=True)
  (dest/('obstruction_pilot.json' if args.pilot else 'obstruction.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
  print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
if __name__=='__main__':main()
