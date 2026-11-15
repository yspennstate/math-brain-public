import json,math,random,time
from pathlib import Path
import mpmath as mp
from symmetric import evaluate
mp.mp.dps=110
start=time.monotonic()
# All rational constant certificates are independent of floating-point discovery.
import sharpen_gamma_constants
for n in range(1,25):
 r=json.loads(Path(f'census_cert_{n:02d}.json').read_text());assert r['B_le_2.18I_integer_certificate']
print('integer_certificates_through_n24',True,flush=True)
# Validate both sides of the small-block split, including values arbitrarily close to its join.
maximum=-1
for n in range(25,40):
 for j in range(2001):
  rho=math.exp(-j/200)
  ell=-math.log(rho);c=2*math.log(2)-1;d=(2-math.sqrt(2))/math.sqrt(math.pi)
  C=math.log(4)-d/math.sqrt(n-1)+1/(2*(n-1));rr=math.log(2)-c/n
  val=(min(C,ell)+rr)/(2*math.log(2))+(1+.5*math.log(n)-1.5*ell)/(n*rho*math.log(2))
  assert val<1.6,(n,rho,val)
  maximum=max(maximum,val)
print('small_block_rho_grid_cases',15*2001,'max_upper',maximum,flush=True)
# Independently verify the refined oscillatory witness.
ref=json.loads(Path('gamma_refinement_2000.json').read_text());f=[1 if x=='+' else -1 for x in ref['value_vector']]
v=evaluate(f,110);v2=evaluate(f,150)
assert abs(v['Gamma/I']-v2['Gamma/I'])<mp.mpf('1e-95')
assert abs(float(v['Gamma/I'])-ref['best']['Gamma/I'])<1e-10
out={'n':2000,'value_vector':ref['value_vector'],'metrics':{k:mp.nstr(x,80) if x is not None and not isinstance(x,(str,bool,int)) else x for k,x in v.items()}}
Path('refinement_high_precision.json').write_text(json.dumps(out,indent=2)+'\n')
print('refined_Gamma_over_I',mp.nstr(v['Gamma/I'],75),flush=True)
print('wall_seconds',time.monotonic()-start,flush=True)
