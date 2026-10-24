import numpy as np,json,math
from pathlib import Path
out=[]
for n in [401,801]:
 t=np.linspace(0,10,n);x=t[:,None];y=t[None,:]
 for eps,b in [(0.,0.),(.3,0.),(.3,.5),(.3,1.)]:
  V=lambda z:z*z/2+eps*(1-np.cos(z))
  D=lambda z:z+eps*np.sin(z)
  w=np.exp(-V(x)-V(x-y)-V(y-b))
  integ=lambda f:np.trapezoid(np.trapezoid(f,t,axis=1),t,axis=0)
  Z=integ(w)
  row={'grid':n,'epsilon':eps,'boundary':b,'mean_x':float(integ(x*w)/Z),'mean_y':float(integ(y*w)/Z)}
  if b==0:row['euler_energy']=float(integ((x*D(x)+(x-y)*D(x-y)+y*D(y))*w)/Z)
  out.append(row)
rho=.5;sigma=math.sqrt(2/3);p=.25+math.asin(rho)/(2*math.pi)
exact=sigma*(1+rho)/(2*math.sqrt(2*math.pi)*p)
res={'model':'triangle 0--x--y--0; nonnegative x,y; H=V(x)+V(x-y)+V(y-b)','extent':10,'curvature_epsilon03':[.7,1.3],'gaussian_exact_mean':exact,'results':out}
Path('numerical_checks.json').write_text(json.dumps(res,indent=2),encoding='utf8')
print(json.dumps(res,indent=2))
