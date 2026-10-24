from fractions import Fraction as F
import pathlib,json
out=[]
for d in [4,5]:
 L=F(d,2*(d-1));U=L+F(1,100);q0=1-1/(L*(d-2))
 K=q0**d/(2*(2*d*(1+U)+1));delta=L*K/2;lam=L+delta
 tau=1/(2*d*(1+U));B=2*L/lam-2+2*K
 assert q0>0 and 0<delta<F(1,100) and B>=K>0
 out.append({'d':d,'L':str(L),'U':str(U),'q_lower':str(q0),'isolation_lower_K':str(K),'delta':str(delta),'threshold_lower_bound':str(lam),'threshold_lower_bound_decimal':float(lam),'time_window_tau':str(tau),'branching_excess_lower_positive':str(B)})
pathlib.Path('second_threshold_bounds.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
