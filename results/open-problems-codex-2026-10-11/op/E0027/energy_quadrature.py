from pathlib import Path
import numpy as np,json
rows=[]
for R in [10.,100.,1000.,10000.]:
 grid=np.unique(np.concatenate([np.linspace(0,8,321),np.geomspace(8,R,501)]))
 x=grid[:,None];y=grid[None,:]
 w=(np.exp(-x*x)+np.exp(-y*y))**2
 p1=np.sqrt(x)+y**1.5;p2=x**1.5+np.sqrt(y)
 def integ(v):return float(4*np.trapezoid(np.trapezoid(v,grid,axis=1),grid))
 rows.append({'R':R,'energy_X_truncated':integ(w/(1+p1)),'energy_Y_truncated':integ(w/(1+p2)),'energy_sum_truncated':integ(w/(1+p1+p2)),'nodes':len(grid)})
 assert abs(rows[-1]['energy_X_truncated']-rows[-1]['energy_Y_truncated'])<1e-7
out={'method':'Positive-quadrant product trapezoid rule; linear grid to 8 and log grid to R, multiplied by 4. No rigorous error bound. Unnormalized Fourier energy.','rows':rows,'proof':'ATTEMPT.md Section 5.1 establishes divergence/finiteness exactly; this quadrature only checks direction.'}
Path('energy_quadrature.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out,indent=2))
