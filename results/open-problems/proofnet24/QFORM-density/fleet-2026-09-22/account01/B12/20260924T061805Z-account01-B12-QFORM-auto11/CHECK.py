import itertools, math
import numpy as np

rng=np.random.default_rng(20260924)

def e_k(B,k):
    s=np.linalg.svd(B,compute_uv=False)
    vals=s*s
    return sum(np.prod(vals[list(I)]) for I in itertools.combinations(range(len(vals)),k))

def rankk_formula(B,a,b,k):
    U,s,Vt=np.linalg.svd(B,full_matrices=True)
    sig=s[:k]
    Uk=U[:,:k]; Vk=Vt[:k,:].T
    alpha=Uk.T@a; beta=Vk.T@b
    aperp=a-Uk@alpha; bperp=b-Vk@beta
    tau=float(np.sum(alpha*beta/sig))
    R=(tau*tau
       +np.linalg.norm(aperp)**2*np.sum((beta/sig)**2)
       +np.linalg.norm(bperp)**2*np.sum((alpha/sig)**2)
       +np.linalg.norm(aperp)**2*np.linalg.norm(bperp)**2*np.sum(1/sig**2))
    Z0=float(np.prod(sig**2))
    return Z0,tau,float(R)

max_rel=0.0
min_gap=1e100
for trial in range(2000):
    p,q,k=8,9,5
    U0,_=np.linalg.qr(rng.normal(size=(p,k)))
    V0,_=np.linalg.qr(rng.normal(size=(q,k)))
    sig=np.exp(rng.normal(size=k))
    B=U0[:,:k]@np.diag(sig)@V0[:,:k].T
    a=rng.normal(size=p); b=rng.normal(size=q)
    Z0,tau,R=rankk_formula(B,a,b,k)
    min_gap=min(min_gap,R-tau*tau)
    for theta in (rng.normal()*5,-13.0,0.125):
        lhs=e_k(B+theta*np.outer(a,b),k)
        rhs=Z0*(1+2*theta*tau+theta*theta*R)
        max_rel=max(max_rel,abs(lhs-rhs)/(1+abs(lhs)))

c=3.0
J=np.array([[0.,1.],[-1.,0.]])
J4=np.block([[J,np.zeros((2,2))],[np.zeros((2,2)),J]])
K=np.zeros((9,9)); K[:4,:4]=-np.eye(4); K[4:8,4:8]=c*J4
Bc=2*(np.eye(9)+K.T)
a=np.zeros(9); a[0]=1
b=np.zeros(9); b[4]=1
base_s=np.linalg.svd(Bc,compute_uv=False)
min_s5=1e100
for lam in (-1e6,-100.,-2.,0.,3.,1e6):
    Bt=Bc+(lam/2)*np.outer(a,b)
    s=np.linalg.svd(Bt,compute_uv=False)
    min_s5=min(min_s5,s[4])

print(f'max_relative_formula_error={max_rel:.6e}')
print(f'min_observed_R_minus_tau2={min_gap:.6e}')
print(f'partner_family_baseline_s5={base_s[4]:.12f}')
print(f'partner_family_min_s5_over_test_lambdas={min_s5:.12f}')
print(f'density_bound_h_delta_1over64={5*math.sqrt(2*math.e)/(2-1/32):.12f}')
