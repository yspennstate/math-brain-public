import itertools, math
import numpy as np

rng=np.random.default_rng(20260923)

# 1. Exact 3x3 inverse identity, numerical regression.
max_inv_err=0.0
for _ in range(2000):
    a=rng.normal(); beta=rng.normal()
    E=10.0**rng.uniform(-2,2)
    lam=(1 if rng.random()<0.5 else -1)*10.0**rng.uniform(-2,2)
    C=np.array([[a,beta,math.sqrt(E)],[beta,lam,0.0],[math.sqrt(E),0.0,0.0]])
    I=np.array([[0.0,0.0,1/math.sqrt(E)],
                [0.0,1/lam,-beta/(math.sqrt(E)*lam)],
                [1/math.sqrt(E),-beta/(math.sqrt(E)*lam),(-a*lam+beta*beta)/(E*lam)]])
    max_inv_err=max(max_inv_err,float(np.max(np.abs(C@I-np.eye(3)))))

# 2. Diffuse pair law.
min_disjoint=1.0; max_pair_sum_err=0.0; diffuse_count=0
for m in range(4,31):
    for _ in range(200):
        Q,_=np.linalg.qr(rng.normal(size=(m,2)))
        z,q=Q[:,0],Q[:,1]
        ell=z*z+q*q
        if float(np.max(ell))>0.5+1e-12:
            continue
        p=np.array([(z[i]*q[j]-z[j]*q[i])**2 for i,j in itertools.combinations(range(m),2)])
        disjoint=1.0-float(np.sum(ell*ell))+float(np.sum(p*p))
        min_disjoint=min(min_disjoint,disjoint)
        max_pair_sum_err=max(max_pair_sum_err,abs(float(np.sum(p))-1.0))
        diffuse_count+=1

# 3. Leaf and pair Schur identities.
max_leaf_err=0.0; max_schur_err=0.0
for _ in range(4000):
    m=int(rng.integers(3,12))
    Q,_=np.linalg.qr(rng.normal(size=(m,2)))
    z,q=Q[:,0],Q[:,1]
    E=10.0**rng.uniform(-1,2)
    lam=(1 if rng.random()<0.5 else -1)*10.0**rng.uniform(-1,2)
    a=rng.normal()*10.0**rng.uniform(-1,1); beta=rng.normal()*10.0**rng.uniform(-1,1)
    b=beta*z+math.sqrt(E)*q
    A=np.zeros((m+1,m+1)); A[0,0]=a; A[0,1:]=b; A[1:,0]=b; A[1:,1:]=lam*np.outer(z,z)
    inds=np.where(np.abs(z)>1e-8)[0]
    if not len(inds): continue
    i=int(rng.choice(inds)); mask=np.arange(m)!=i
    w=b[mask]-(b[i]/z[i])*z[mask]
    H=sum((b[i]*z[j]-b[j]*z[i])**2 for j in range(m) if j!=i)
    max_leaf_err=max(max_leaf_err,abs(float(w@w)-H/z[i]**2)/(1+H/z[i]**2))
    B=A[np.ix_([0,i+1],[0,i+1])]; d=float(np.linalg.det(B))
    if abs(d)>1e-8:
        rest=[j+1 for j in range(m) if j!=i]
        Cross=A[np.ix_([0,i+1],rest)]
        S=A[np.ix_(rest,rest)]-Cross.T@np.linalg.inv(B)@Cross
        v=b[i]*z[mask]-z[i]*b[mask]
        S2=-(lam/d)*np.outer(v,v)
        max_schur_err=max(max_schur_err,float(np.max(np.abs(S-S2)))/(1+float(np.max(np.abs(S2)))))

# 4. Constants.
eps=1/16
r0=math.sqrt(3/8)-math.sqrt(17/128)
kappa0=r0-1/8
pair_currency_lower=kappa0/2
C_diffuse=3*2**(4/3)*100**(1/6)
C_hub_leaf=128*eps**(-1/4)
C_pair=8*math.sqrt(5)*pair_currency_lower**(-1/4)

print(f'max_inverse_identity_error={max_inv_err:.3e}')
print(f'diffuse_samples={diffuse_count}')
print(f'min_sampled_disjoint_probability={min_disjoint:.12f}')
print(f'max_pair_law_normalization_error={max_pair_sum_err:.3e}')
print(f'max_leaf_identity_relative_error={max_leaf_err:.3e}')
print(f'max_pair_schur_relative_error={max_schur_err:.3e}')
print(f'epsilon={eps:.12f}')
print(f'r0={r0:.12f}')
print(f'kappa0={kappa0:.12f}')
print(f'pair_currency_lower={pair_currency_lower:.12f}')
print(f'C_diffuse={C_diffuse:.12f}')
print(f'C_hub_leaf={C_hub_leaf:.12f}')
print(f'C_pair={C_pair:.12f}')
assert min_disjoint>0.01
assert kappa0>0.1
assert C_diffuse<17
assert C_hub_leaf==256
assert C_pair<40
assert max_inv_err<1e-9 and max_leaf_err<1e-10 and max_schur_err<1e-10
print('STATUS=PASS')
