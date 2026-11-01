from pathlib import Path
import numpy as np,json,math
# Referee check of the Fourier ODE and the sign bound, using a genuine
# C1 piecewise quadratic sector function u=r^2 cos^2(pi*theta/alpha).
rows=[]
for deg in [135,150,162]:
 alpha=math.radians(deg);theta=(np.arange(200000)+0.5)*alpha/200000-alpha/2
 f=np.cos(math.pi*theta/alpha)**2
 g=2+(2-2*math.pi**2/alpha**2)*np.cos(2*math.pi*theta/alpha)
 projection=float(np.sum(g*np.cos(2*theta))*alpha/len(theta))
 a=float(g.min());b=float(g.max());kappa=a-b*(1-math.sin(alpha))
 assert abs(projection)<1e-8 and kappa<0
 rows.append(dict(angle=deg,manufactured_density_min=a,manufactured_density_max=b,projection=projection,lower_projection_bound=kappa))
for H in range(-1,101):
 k=H+3;alpha=math.pi-math.pi/(2*k)
 kap=(H+2)-(H+3)*(1-math.sin(alpha))
 assert kap>0
 rows.append(dict(H=H,regular_polygon_angle=alpha,contradiction_margin=kap))
Path('experiments/corner_checks.json').write_text(json.dumps(rows,indent=2),encoding='utf8')
print('Fourier sign and ODE checked with manufactured wedge functions; contradiction margin positive for H=-1 through 100.')
