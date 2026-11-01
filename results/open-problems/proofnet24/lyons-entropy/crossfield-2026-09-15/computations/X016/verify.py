"""Deterministic self-checks for the proved X016 rank-three identities.

No numerical result substitutes for the proofs in agents/X016.md.
"""
from itertools import combinations
from pathlib import Path
import json
import numpy as np
from probe import data, parseval, adj

I=np.eye(3)

def atoms(v,M,A):
 sets=[()]+[s for k in (1,2,3) for s in combinations(range(len(v)),k)]
 inc={():1.};dinc={():0.};ddinc={():0.}
 for s in sets[1:]:
  R=v[list(s)];C=R@M@R.conj().T;D=R@A@R.conj().T
  p=np.linalg.det(C).real
  if p<1e-23:
   inc[s]=dinc[s]=ddinc[s]=0.;continue
  B=np.linalg.solve(C,D);tr=np.trace(B).real
  inc[s]=p;dinc[s]=p*tr;ddinc[s]=p*(tr*tr-np.trace(B@B).real)
 prob={};dp={};ddp={}
 for s in sets:
  supers=[t for t in sets if set(s)<=set(t)]
  prob[s]=sum((-1)**(len(t)-len(s))*inc[t] for t in supers)
  dp[s]=sum((-1)**(len(t)-len(s))*dinc[t] for t in supers)
  ddp[s]=sum((-1)**(len(t)-len(s))*ddinc[t] for t in supers)
 retained=[s for s in sets if prob[s]>1e-20]
 fi=sum(dp[s]**2/prob[s] for s in retained)
 nh=fi+sum(ddp[s]*np.log(prob[s]) for s in retained)
 return prob,dp,ddp,fi,nh

def odds_data(v,L):
 W=np.zeros((3,3),complex);tau=0.;G=v@L@v.conj().T
 ti=np.diag(G).real
 for i,j in combinations(range(len(v)),2):
  z=np.cross(v[i],v[j]);b=np.vdot(z,z).real
  if b<1e-24:continue
  bg=np.linalg.det(G[np.ix_([i,j],[i,j])]).real
  c=np.log(ti[i]*ti[j]/bg);W+=c*np.outer(z,z.conj())
 for s in combinations(range(len(v)),3):
  r=abs(np.linalg.det(v[list(s)]))**2
  if r<1e-24:continue
  rg=np.linalg.det(G[np.ix_(s,s)]).real
  bg=[np.linalg.det(G[np.ix_(p,p)]).real for p in combinations(s,2)]
  tau+=r*np.log(np.prod(bg)/(np.prod(ti[list(s)])*rg))
 return W,tau

def defect(L):
 return 3*np.log(np.trace(L).real/3)-np.linalg.slogdet(L)[1]

def check(v,M,A,label):
 U,t,pairs,W0,tau0,*_=data(v);Q=I-M;L=M@np.linalg.inv(Q);J=np.linalg.inv(Q);H=np.linalg.inv(M)
 d0=np.linalg.det(Q).real;d3=np.linalg.det(M).real
 W,tau=odds_data(v,L);T=W+tau*M
 l,Ueig=np.linalg.eigh(M);q=1-l;a=np.diag(Ueig.conj().T@A@Ueig).real
 F1=sum(np.trace(u@J@A@J).real**2/np.trace(u@L).real for u in U)
 x=np.array([np.trace(u@A).real/t0 for u,t0 in zip(U,t)]);ht=np.trace(A).real
 fv0=sum(t*x*x);fw0=0.;rem=0.
 for i,j in combinations(range(len(v)),2):
  zz=np.cross(v[i],v[j]);bb=np.vdot(zz,zz).real
  if bb<1e-24:continue
  yy=np.vdot(zz,A@zz).real/bb;fw0+=bb*yy*yy
  rem+=.5*bb*((yy-(ht-x[i])/2)**2+(yy-(ht-x[j])/2)**2)
 fisher_remainder_error=abs(fw0-(fv0+ht*ht)/4-rem)
 assert fisher_remainder_error<2e-11
 Linv=np.linalg.inv(L)
 F2=sum(np.trace(P@H@A@H).real**2/np.trace(P@Linv).real for P,b in pairs)
 correction=-sum((l[j]-l[i])*(l[k]-l[i])/(l[i]**2*q[i]**2)*a[i]**2 for i,(j,k) in enumerate(((1,2),(0,2),(0,1))))
 p,dp,ddp,fi,nh=atoms(v,M,A)
 fi_decomp=d0*F1+d3*F2+correction
 curvature=fi-2*np.trace(T@adj(A)).real
 lev=np.linalg.eigvalsh(L);kap=lev[-1]/lev[0];m=l[-1];Dkap=3*np.log((kap+2)/3)-np.log(kap)
 upper=np.log(2*kap)+m*(np.log(9/4)+Dkap)
 var=np.trace(M@Q).real;epsilon=1-2*var*upper/3
 assert abs(fi-fi_decomp)<2e-10
 assert abs(nh-curvature)<2e-10
 assert np.linalg.eigvalsh(W-W0)[0]>=-np.log(kap)-2e-11
 assert np.linalg.eigvalsh(W-W0)[-1]<=np.log(kap)+2e-11
 assert tau-tau0>=-defect(L)-2e-11
 assert tau-tau0<=defect(Linv)+2e-11
 assert np.linalg.eigvalsh(T)[0]>=-2e-11
 assert np.linalg.eigvalsh(T)[-1]<=upper+2e-11
 mean=sum(len(s)*p0 for s,p0 in p.items());countvar=sum((len(s)-mean)**2*p0 for s,p0 in p.items());cov=sum(len(s)*dp0 for s,dp0 in dp.items())
 assert abs(countvar-var)<2e-11 and abs(cov-np.trace(A).real)<2e-11
 if np.linalg.eigvalsh(A)[0]>-1e-14 and kap<=2+1e-13:
  assert nh>=(13/2700)*fi-2e-11
  assert epsilon>=13/2700-2e-11
 return dict(label=label,M_eigenvalues=l.tolist(),odds_condition_number=kap,
   noncommutation_norm=float(np.linalg.norm(M@A-A@M)),
   fisher=fi,fisher_decomposition_error=abs(fi-fi_decomp),spectral_fisher_correction=correction,
   scalar_exterior_fisher_remainder_error=fisher_remainder_error,
   negative_hessian=nh,curvature_identity_error=abs(nh-curvature),
   cubic_distortion=tau-tau0,cubic_distortion_interval=[-defect(L),defect(Linv)],
   T_eigenvalues=np.linalg.eigvalsh(T).tolist(),T_upper_bound=upper,
   epsilon_certificate=epsilon,actual_ratio=nh/fi)

z=np.array([0,1,1j,-1+.5j,2-1j,.5+.75j]);v=parseval(np.column_stack((np.ones(6),z,z*z)))
omega=np.exp(2j*np.pi/3);F=np.array([[omega**(i*j) for j in range(3)] for i in range(3)])/np.sqrt(3)
rot=np.array([[1,1j,2],[2,1,-1j],[1,-2,1j]],complex);e,u=np.linalg.eigh(rot.conj().T@rot);rot=rot@((u/np.sqrt(e))@u.conj().T)
A=rot@np.diag([.7,1.1,1.3])@rot.conj().T
Aind=np.array([[.4,.2-.1j,.07j],[.2+.1j,-.15,.11],[-.07j,.11,.31]])
results=[check(v,F@np.diag([.4,.5,.57])@F.conj().T,A,'generic frame, nonscalar odds condition below two, noncommuting positive direction'),
 check(v,F@np.diag([.2,.5,.8])@F.conj().T,Aind,'generic frame, wide spectral range, indefinite identity check'),
 check(v,.43*I,Aind,'generic frame, scalar specialization'),
 check(v,F@np.diag([.15,.15,.22])@F.conj().T,A,'generic frame, repeated nonscalar eigenvalue'),
 check(v,F@np.diag([.73,.79,.8])@F.conj().T,A,'generic frame, upper spectral region')]
# A zero-diagonal direction in the spectral basis has no residual correction.
Aoff=F@np.array([[0,.2+.1j,.13],[.2-.1j,0,-.11j],[.13,.11j,0]])@F.conj().T
results.append(check(v,F@np.diag([.2,.5,.8])@F.conj().T,Aoff,'zero spectral diagonal direction'))
assert abs(results[-1]['spectral_fisher_correction'])<1e-25
# The rational gap proof is exact in the report; this checks its algebraic expansion.
for m in np.linspace(0,1,31):
 x=m-2/3
 lhs=1.5-(.5+m-m*m)*(1.4+m)
 rhs=1/135-x/30+(12/5+x)*x*x
 assert abs(lhs-rhs)<1e-14
 assert lhs>=13/1800-1e-14
out=Path(__file__).with_name('results.json');out.write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
