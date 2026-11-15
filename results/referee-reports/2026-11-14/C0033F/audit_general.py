"""Independent algebraic/numerical checks of the general-collar theorem."""
import json,random,time,resource
from pathlib import Path
import mpmath as mp
from general_collar import *
from mp_core import evaluate,strings,tr,coordinates

def main():
 mp.mp.dps=120;start=time.monotonic();rng=random.Random(33605)
 out=dict(seed=33605,random_cases=0,maximum_T_identity_error=mp.mpf(0),maximum_F_identity_error=mp.mpf(0),minimum_lower_bound_gap=mp.inf,maximum_w_over_bound=0,fixed_checks=[],uniform_collar_checks=[])
 for i in range(500):
  a=mp.mpf(str(rng.uniform(.01,.99)));e0=mp.mpf(str(rng.uniform(.001,.49)));e1=mp.mpf(str(rng.uniform(.001,.49)));angle=mp.mpf(str(rng.uniform(.01,1.56)))
  C=block(e0,e1,angle);beta=mp.mpf(str(rng.uniform(0,1.57)));phi=mp.mpf(str(rng.uniform(-3.14,3.14)));v=mp.matrix([mp.cos(beta),mp.sin(beta)*mp.exp(mp.j*phi)])
  d=limit(C,v,True);W=mp.zeros(2);W2=mp.zeros(2)
  for s in range(4):
   M=C-mp.diag([int(not(s&1)),int(not(s&2))]);Mi=M**-1;k=mp.re((v.H*Mi*v)[0]);W+=d['pi'][s]*k*Mi;W2+=d['pi'][s]*Mi*v*v.H*Mi
  adjW=mp.matrix([[W[1,1],-W[0,1]],[-W[1,0],W[0,0]]])
  out['maximum_T_identity_error']=max(out['maximum_T_identity_error'],mp.norm(adjW-d['T']))
  out['maximum_F_identity_error']=max(out['maximum_F_identity_error'],mp.norm(W-W2))
  gap=d['m0']-1/(2*d['K']+3);assert gap>0
  out['minimum_lower_bound_gap']=min(out['minimum_lower_bound_gap'],gap)
  out['maximum_w_over_bound']=max(out['maximum_w_over_bound'],d['w']/(2*(d['K']+1)))
  par=parameters(a,C);assert min(mp.eigsy(W.apply(mp.re))[0])>=par['omega']
  out['random_cases']+=1
 # Fixed unequal complex connections, unbalanced block, isolated weight near endpoints.
 C=mp.matrix([[mp.mpf('.2'),mp.mpf('-.17')],[mp.mpf('-.17'),mp.mpf('.7')]])
 v=mp.matrix([mp.mpf(3)/5,mp.mpf(12)/25+mp.j*mp.mpf(16)/25]);m0=limit(C,v)
 for a in map(mp.mpf,['.00001','.31','.999999']):
  for exponent in (12,24,48):
   x=mp.mpf(10)**(-exponent);ev=evaluate(kernel(a,C,v,x));out['fixed_checks'].append(strings(dict(a=a,x=x,margin=ev['margin'],m0=m0,error=ev['margin']-m0,error_over_x=(ev['margin']-m0)/x),60))
 for case,(a,C,v) in enumerate([
  (mp.mpf('.003'),C,v),
  (mp.mpf('.999'),block(mp.mpf('1e-8'),mp.mpf('.2'),mp.mpf('.29')),mp.matrix([1,0])),
  (mp.mpf('.2'),block(mp.mpf('1e-8'),mp.mpf('1e-12'),mp.mpf('.27')),mp.matrix([mp.mpf(3)/5,mp.mpf(12)/25+mp.j*mp.mpf(16)/25])),
 ]):
  par=parameters(a,C);j=int(mp.ceil(-mp.log10(par['collar_x'])/2))+2;x=mp.mpf(10)**(-2*j)
  mp.mp.dps=max(300,12*j)
  ev=evaluate(kernel(a,C,v,x));m0=limit(C,v);err=abs(ev['margin']-m0);bound=mp.mpf('1e30')*x/par['mu']**15
  assert err<=bound and ev['margin']>=1/(8*ev['logscale']+6)
  out['uniform_collar_checks'].append(strings(dict(case=case,a=a,C=[[C[i,j] for j in range(2)] for i in range(2)],v=list(v),connection_exponent=j,x=x,precision=mp.mp.dps,parameters=par,margin=ev['margin'],m0=m0,error=err,error_bound=bound),90))
 out.update(seconds=time.monotonic()-start,peak_rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/2**20)
 Path('data/general_audit.json').write_text(json.dumps(strings(out,90),indent=2)+'\n');print(json.dumps(strings(out,20),indent=2))
if __name__=='__main__':main()
