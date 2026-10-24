import math,pathlib,json,numpy as np
out=[]
for c in [0.01,0.1,0.5,1.0,2.0,10.0]:
 p=min(2.,(1+math.sqrt(1+8*c))/2);k=p*(p-1)/2
 assert 1<p<=2 and k<=c+1e-12
 nodes,ws=np.polynomial.legendre.leggauss(256);u=(nodes+1)/2;integral=np.dot(ws/2,u*(1-u)**(p-1));val=p*integral
 out.append(f'c={c:g}, p={p:.12g}, power-generator budget k={k:.12g}, p*integral={val:.12g}, exact=1/(p+1)={1/(p+1):.12g}, error={abs(val-1/(p+1)):.3g}')
 for x in np.linspace(0,2*math.pi,101):
  for eps in [1e-6,0.01,1.0]:
   lhs=2*p*(p-1)*math.sin(x/2)**2*(x+eps)**(p-2)
   assert lhs<=k*x**p+1e-10
out.append('Regularized diffusion bound: all grid checks passed; not a substitute for the written inequality.')
p=(1+math.sqrt(5))/2;L=2*math.pi;nodes,ws=np.polynomial.legendre.leggauss(64)
for s in [0.05,0.2,0.5,1.0]:
 xx=s*(nodes+1)/2;w=s*ws/2;dif=xx[:,None]-xx[None,:];K=np.sinc(dif/(2*np.pi))/(2*np.pi);B=np.sqrt(w[:,None])*K*np.sqrt(w[None,:]);sgn,ld=np.linalg.slogdet(np.eye(64)-B);G=sgn*np.exp(ld)
 remainder=G-1+s/L;bound=(s/L)**(p+1)/(p+1);fake=math.exp(-s/L)-1+s/L
 assert -1e-13<=remainder<=bound+1e-13
 out.append(f'beta=2, s={s:g}: external determinant remainder={remainder:.12g}, proved bound={bound:.12g}, exponential remainder={fake:.12g}')
assert math.exp(-0.05/L)-1+0.05/L > (0.05/L)**(p+1)/(p+1)
out.append('Exponential candidate violates the generator-derived bound at s=0.05.')
pathlib.Path('new_moment_checks.txt').write_text('\n'.join(out)+'\n',encoding='utf8');print('\n'.join(out))
claims=[
 {'problem_id':'D0047','claim':'For every beta>0 and s>=0, 0<=G_beta(s)-1+s/(2pi)<=((s/(2pi))^(p+1))/(p+1), p=min(2,(1+sqrt(1+2beta))/2).','status':'proved','proof_location':'ATTEMPT.md Section 13','remaining_gap':'This is a weak small-gap remainder bound, not the sharp coefficient or a Painleve derivation.','checks':'Stopped discounted Ito formula with epsilon regularization; concavity; explicit beta integral; new_moment_checks.txt.'},
 {'problem_id':'D0047','claim':'The carousel SDE implies a vanishing Peano quadratic gap remainder for every beta>0, excluding the exponential sigma-PV branch directly from probabilistic data.','status':'proved','proof_location':'ATTEMPT.md Section 14','remaining_gap':'No classical second derivative is inferred solely from the asymptotic bound; physical sigma-PV remains unproved.','checks':'p>1 in Section 13 and Taylor expansion of the exponential.'},
 {'problem_id':'D0047','claim':'For nonzero a, formal sigma-PV solutions with Sigma=-ar+O(r^2) have exactly two sectors: b=0 gives the linear series, and b=-a^2 gives a uniquely recursively determined formal nonlinear series. Thus there is at most one analytic PV gap germ with the physical slope and zero quadratic gap coefficient.','status':'proved','proof_location':'ATTEMPT.md Section 15','remaining_gap':'Convergence/existence of an analytic nonlinear germ and physical carousel selection are not proved.','checks':'First-difference coefficient proof for all orders; check_new_series.py verifies orders 3 through 10; SelectionAlgebra.lean checks finite algebra if new_lean_check.txt has exit 0.'}
]
with pathlib.Path('CLAIMS.jsonl').open('a',encoding='utf8') as f:
 for claim in claims:f.write(json.dumps(claim,ensure_ascii=False)+'\n')
