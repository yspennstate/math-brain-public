from pathlib import Path
import numpy as np, sympy as sp, json,time
root=Path(__file__).resolve().parent
start=time.time(); rng=np.random.default_rng(190019)
x,y,alpha=sp.symbols('x y alpha',real=True)
A=sp.Matrix([[-1,-1],[1,-1]]);a=sp.Matrix([1,0]);v=sp.Matrix([x,y])
symbolic={'affine_determinant':str(sp.det(sp.Matrix.hstack(A*v,A*(v-a)))), 'Aa':str(A*a), 'A2a':str(A*A*a), 'rank_determinant':str(sp.det(sp.Matrix.hstack(A*a,A*A*a)))}
def eA(t):
 return np.exp(-t)*np.array([[np.cos(t),-np.sin(t)],[np.sin(t),np.cos(t)]])
def end(x0,s1,s2,T=1):
 return eA(T)@x0+(eA(T-s2)-eA(T-s1))@np.array([1.,0.])
b=np.array([-1.,1.]);maxerr=0.;mindet=1.
for j in range(300):
 s1=rng.uniform(.02,.7);s2=rng.uniform(s1+.02,.98);xx=rng.normal(size=2);h=1e-6
 num=np.column_stack([(end(xx,s1+h,s2)-end(xx,s1-h,s2))/(2*h),(end(xx,s1,s2+h)-end(xx,s1,s2-h))/(2*h)])
 exact=np.column_stack([eA(1-s1)@b,-eA(1-s2)@b])
 maxerr=max(maxerr,float(np.max(abs(num-exact))));mindet=min(mindet,float(abs(np.linalg.det(exact))))
assert maxerr<1e-8 and mindet>0
# Sample the stationary convolution by backward alternating exponential holds.
# Two-state stationary chains are reversible, so reverse-time rates equal forward rates.
N=30000; rates=np.array([.5,3.]);pi=np.array([3/3.5,.5/3.5]);states=(rng.random(N)>pi[0]).astype(int)
initial=states.copy();u=np.zeros(N);X=np.zeros((N,2));cutoff=30.;iterations=0
while np.any(u<cutoff):
 ids=np.flatnonzero(u<cutoff);left=u[ids];right=np.minimum(cutoff,left+rng.exponential(1/rates[states[ids]]));active=states[ids]==1
 z=ids[active];l=left[active];r=right[active]
 X[z,0]+=np.exp(-l)*np.cos(l)-np.exp(-r)*np.cos(r)
 X[z,1]+=np.exp(-l)*np.sin(l)-np.exp(-r)*np.sin(r)
 u[ids]=right;states[ids]=1-states[ids];iterations+=1
rad=np.linalg.norm(X,axis=1);balls=[]
for r in [.2,.1,.05,.02,.01]:
 measured=float(np.mean((initial==0)&(rad<r)))
 lower=float(pi[0]*(r/2)**rates[0]);balls.append({'radius':r,'empirical_mode0_ball_mass':measured,'proved_lower_bound_using_R_2':lower})
# Annulus exponent, including the exact Lp endpoint, checked symbolically.
L,P=sp.symbols('L P',positive=True);expr=2*(P-1)-L*P
endpoint=sp.simplify(expr.subs(P,2/(2-L)));assert endpoint==0
result={'symbolic':symbolic,'jacobian_cases':300,'jacobian_max_absolute_error':maxerr,'jacobian_min_abs_determinant':mindet,'stationary_samples':N,'lambda0':.5,'lambda1':3.,'truncation_cutoff':cutoff,'deterministic_truncation_error_bound':float(2**.5*np.exp(-cutoff)),'simulation_iterations':iterations,'ball_mass_comparison':balls,'endpoint_exponent':str(endpoint),'elapsed_seconds':time.time()-start,'interpretation':'Symbolic identities and numerical checks agree; Monte Carlo is diagnostic, not proof.'}
(root/'numerics.json').write_text(json.dumps(result,indent=2),encoding='utf8');print(json.dumps(result,indent=2))
