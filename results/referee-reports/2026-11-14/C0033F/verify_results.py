"""Doubled-precision reconstruction and exact rational interval point audits."""
import json,time,resource,math
from pathlib import Path
from fractions import Fraction as F
import mpmath as mp
from mp_core import evaluate as original,coordinates,strings
from stable_core import evaluate as stable
from search_faces import make as face_make
from optimize_global import make as global_make
import interval_core as ic

def significant_bounds(z,digits=70):
 ans=[]
 for n,t in enumerate(z._mpi_):
  q=ic.endpoint(t)
  if not q:ans.append('0');continue
  exponent=int(mp.floor(mp.log10(abs(mp.mpf(q.numerator)/q.denominator))))
  power=exponent-digits+1;unit=F(10)**power;val=q/unit
  integer=val.numerator//val.denominator if n==0 else -((-val.numerator)//val.denominator)
  ans.append(str(integer)+'e'+str(power))
 return ans

def exact_strict(coords):
 a,b,c,xr,xi,yr,yi,zr,zi=coords
 def minors(a,b,c,xr,xi,yr,yi,zr,zi):
  return [a,a*b-xr*xr-xi*xi,a*b*c-a*(zr*zr+zi*zi)-b*(yr*yr+yi*yi)-c*(xr*xr+xi*xi)+2*((xr*zr-xi*zi)*yr+(xr*zi+xi*zr)*yi)]
 assert all(z>0 for z in minors(*coords))
 comp=[1-a,1-b,1-c,-xr,-xi,-yr,-yi,-zr,-zi]
 assert all(z>0 for z in minors(*comp))
 return True

def certify(q,name,dps):
 # The exact decimal-coordinate kernel is the certified object.
 coords=[F(mp.nstr(z,dps+20)) for z in coordinates(q)];exact_strict(coords)
 path=Path('data')/(name+'_rational.json');path.write_text(json.dumps(dict(coordinates=list(map(str,coords)),meaning='exact rational coordinates; coordinate order as mp_core.py'),indent=2)+'\n')
 attempts=[];ic.bounds=significant_bounds
 precision=2*dps+200
 for retry in range(4):
  ic.iv.dps=precision
  try:
   cert=ic.full_certificate([ic.rat(str(z)) for z in coords]);cert.update(name=name,input_path=str(path),precision=precision,retries=attempts,exact_strict=True);return cert
  except (ArithmeticError,ZeroDivisionError,ValueError) as err:attempts.append(dict(precision=precision,error=str(err)));precision*=2
 raise ArithmeticError(('failed point certificate',name,attempts))

def main():
 start=time.monotonic();out=dict(replay=[],certificates=[],maximum_original_stable_discrepancy=mp.mpf(0),maximum_replay_discrepancy=mp.mpf(0),maximum_scaled_hessian_identity_error=mp.mpf(0))
 face=json.load(open('data/face_search.json'));opt=json.load(open('data/global_optimization.json'))
 for name,g in face['groups'].items():
  row=g['minimum_product'];mp.mp.dps=2*row['precision'];q=face_make(row['descriptor']);a=original(q,True);b=stable(q);delta=abs(a['margin']-b['margin']);replay=abs(a['margin']-mp.mpf(row['margin']));assert delta<mp.mpf('1e-65') and replay<mp.mpf('1e-65')
  nh=a['negative_hessian'];R=a['R'];d=mp.re(mp.det(R));rhs=a['J']-d*a['z']*a['z'].T
  scale=[mp.sqrt(abs(nh[i,i])) for i in range(9)];err=max(abs(nh[i,j]-rhs[i,j])/(scale[i]*scale[j]) for i in range(9) for j in range(9))
  assert err<mp.mpf('1e-65')
  out['maximum_original_stable_discrepancy']=max(out['maximum_original_stable_discrepancy'],delta);out['maximum_replay_discrepancy']=max(out['maximum_replay_discrepancy'],replay);out['maximum_scaled_hessian_identity_error']=max(out['maximum_scaled_hessian_identity_error'],err)
  out['replay'].append(strings(dict(name=name,precision=mp.mp.dps,margin=a['margin'],product=a['margin']*a['logscale'],replay_error=replay,original_stable_discrepancy=delta,hessian_identity_error=err),80))
 for run in opt['runs']:
  row=run['best'];mp.mp.dps=2*row['precision'];q,_=global_make(row['params']);ev=original(q,True);error=abs(ev['margin']-mp.mpf(row['margin']));assert error<mp.mpf('1e-65')
  out['replay'].append(strings(dict(name='global_'+str(run['L']),precision=mp.mp.dps,margin=ev['margin'],product=ev['margin']*ev['logscale'],replay_error=error),80))
 row=opt['best'];mp.mp.dps=row['precision']+80;q,_=global_make(row['params']);out['certificates'].append(certify(q,'global_best',row['precision']+40))
 # An exact, unequal, complex collar example; e=10^-50 is inside the proved collar.
 from general_collar import kernel,parameters,limit
 mp.mp.dps=600;a=mp.mpf(3)/1000;C=mp.matrix([[mp.mpf(1)/5,-mp.mpf(17)/100],[-mp.mpf(17)/100,mp.mpf(7)/10]])
 v=mp.matrix([mp.mpf(3)/5,mp.mpf(12)/25+mp.j*mp.mpf(16)/25]);x=mp.mpf(10)**-100;par=parameters(a,C);assert x<par['collar_x'];q=kernel(a,C,v,x)
 out['certificates'].append(certify(q,'general_complex_collar',500))
 # Independent deep balanced probe: original ambient solve at enough precision
 # to resolve its unscaled R, versus stable diagonal scaling and inherited m0.
 from mixed_limit import q_weak,limiting
 L=500;mp.mp.dps=3500;h=mp.exp(-L);q=q_weak(mp.mpf('.5'),h,h**6);ev=original(q);st=stable(q);m0=limiting(mp.mpf('.5'),h)
 assert abs(ev['margin']-st['margin'])<mp.mpf('1e-70') and abs(ev['margin']-m0)<mp.mpf('1e-70')
 out['deep_original_check']=strings(dict(L=L,precision=3500,margin=ev['margin'],stable_discrepancy=ev['margin']-st['margin'],m0_discrepancy=ev['margin']-m0),90)
 out.update(seconds=time.monotonic()-start,peak_rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/2**20)
 Path('data/verification.json').write_text(json.dumps(strings(out,90),indent=2)+'\n');print('verified',len(out['replay']),'certificates',len(out['certificates']),out['seconds'],flush=True)
if __name__=='__main__':main()
