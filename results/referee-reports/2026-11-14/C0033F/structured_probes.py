"""Deep structured probes, with analytic error certificates from C0033E."""
import json,time,resource,math
from pathlib import Path
import mpmath as mp
from stable_core import evaluate,strings
from general_collar import block,kernel,limit
from mixed_limit import limiting,q_weak

def main():
 start=time.monotonic();out=dict(rows=[],general_rows=[],certificates=[])
 for L in (20,80,200,500,1000,3000):
  mp.mp.dps=120+math.ceil(2*L/math.log(10));h=mp.exp(-L);a=mp.mpf('.5');e=h**6
  q=q_weak(a,h,e);ev=evaluate(q);m0=limiting(a,h);nu=a*(1-a)*h*(1-h);err=mp.mpf('4e13')*e**2/nu**8
  assert abs(ev['margin']-m0)<mp.mpf('1e-65')
  b0=h*(1-h);b1=mp.mpf('.5')-b0
  atoms=[b0/2-2*h*e**2,b0/2+2*h*e**2,b1/2+(2*h-1)*e**2,b1/2+(1-2*h)*e**2,b1/2+(2*h-1)*e**2,b1/2+(1-2*h)*e**2,b0/2+2*(1-h)*e**2,b0/2-2*(1-h)*e**2]
  lam=-mp.log(min(atoms));assert abs(lam-ev['logscale'])<mp.mpf('1e-65')
  row=strings(dict(L=L,precision=mp.mp.dps,margin=ev['margin'],Lambda=lam,product=lam*ev['margin'],m0=m0,analytic_margin_error_bound=err,product_error_bound=lam*err),90);out['rows'].append(row)
  Path('data/structured_probes.json').write_text(json.dumps(out,indent=2)+'\n');print('balanced',L,row['product'],flush=True)
 for angle in ('.1','.3','.7'):
  for L in (20,80,200,500):
   mp.mp.dps=120+math.ceil(3*L/math.log(10));h=mp.exp(-L);theta=mp.mpf(angle);C=block(h,h,theta);v=mp.matrix([mp.cos(theta),mp.sin(theta)]);a=mp.mpf('.5');x=h**12
   q=kernel(a,C,v,x);ev=evaluate(q);m0=limit(C,v)
   out['general_rows'].append(strings(dict(angle=angle,L=L,precision=mp.mp.dps,margin=ev['margin'],Lambda=ev['logscale'],product=ev['margin']*ev['logscale'],m0=m0,error=ev['margin']-m0),75))
 # A rigorous interval enclosure of the analytic E remainder at an exact rational
 # h=10^-1000, e=h^6. No rounded floating kernel is substituted.
 iv=mp.iv;iv.dps=2400;h=iv.mpf(1)/iv.mpf(10)**1000;e=h**6;b0=h*(1-h);b1=iv.mpf('.5')-b0;K=2*iv.log(b1/b0)
 f=1/b0-1/(2*b1);g=1/(2*b1);v=1/b0-3
 m0=(f*f-(g-K)**2)/(f*f-g*g+f*K*(v+1/v)+K*K)
 nu=b0/4;err=iv.mpf('4e13')*e**2/nu**8;pm=b0/2-2*(1-h)*e**2;lam=-iv.log(pm)
 margin=m0+iv.mpf([-1,1])*err;product=margin*lam
 from interval_core import bounds
 out['certificates'].append(dict(h='10^-1000',e='10^-6000',a='1/2',method='C0033E (5) plus exact atom table; interval evaluation of m0 and remainder',interval_precision=iv.dps,margin=bounds(margin,60),product=bounds(product,60)))
 out.update(seconds=time.monotonic()-start,peak_rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/2**20)
 Path('data/structured_probes.json').write_text(json.dumps(out,indent=2)+'\n');print('complete',out['seconds'],flush=True)
if __name__=='__main__':main()
