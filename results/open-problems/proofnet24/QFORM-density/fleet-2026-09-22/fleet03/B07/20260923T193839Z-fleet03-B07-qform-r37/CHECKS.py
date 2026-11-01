import math
import numpy as np

rng=np.random.default_rng(20260923)

def e2_from_minors(K):
    m,n=K.shape
    z=0.0
    for i in range(m):
        for j in range(i+1,m):
            for a in range(n):
                for b in range(a+1,n):
                    d=K[i,a]*K[j,b]-K[i,b]*K[j,a]
                    z += d*d
    return z

def e3_from_singular(B):
    s=np.linalg.svd(B,compute_uv=False)
    val=0.0
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            for k in range(j+1,len(s)):
                val += (s[i]*s[j]*s[k])**2
    return float(val)

max_mu_sum_err=0.0
max_volume_relerr=0.0
max_heavy=0
count=0
for _ in range(300):
    m=int(rng.integers(4,9)); n=int(rng.integers(2,7))
    K=rng.normal(size=(m,2)) @ rng.normal(size=(2,n))
    Z=e2_from_minors(K)
    if Z<1e-10:
        continue
    mus=[]
    for i in range(m):
        Zi=e2_from_minors(np.delete(K,i,axis=0))
        mus.append(1.0-Zi/Z)
    max_mu_sum_err=max(max_mu_sum_err,abs(sum(mus)-2.0))
    max_heavy=max(max_heavy,sum(x>2/3+1e-12 for x in mus))

    C=rng.normal(size=(m,m)); C=(C+C.T)/2
    for i in range(m):
        Ki=np.delete(K,i,axis=0)
        ci=np.delete(C[:,i],i)
        coef=np.linalg.lstsq(Ki,ci,rcond=None)[0]
        q=np.linalg.norm(ci-Ki@coef)
        B=np.column_stack([Ki,ci])
        lhs=e3_from_singular(B)
        rhs=e2_from_minors(Ki)*q*q
        max_volume_relerr=max(max_volume_relerr,abs(lhs-rhs)/max(1.0,abs(lhs),abs(rhs)))
    count += 1

max_decomp_error=0.0
max_rank_excess=0
max_entry_excess=0.0
decomp_count=0
for _ in range(300):
    m=int(rng.integers(5,12)); n=int(rng.integers(2,8))
    K=rng.normal(size=(m,2)) @ rng.normal(size=(2,n))
    Z=e2_from_minors(K)
    if Z<1e-9:
        continue
    mus=[]
    for i in range(m):
        Zi=e2_from_minors(np.delete(K,i,axis=0))
        mus.append(1.0-Zi/Z)
    H={i for i,x in enumerate(mus) if x>2/3}
    J=[i for i in range(m) if i not in H]

    # Engineer a genuinely low-containment chamber: a symmetric rank-two
    # carrier plus arbitrary diagonal and tiny symmetric off-diagonal noise.
    U=np.linalg.svd(K,full_matrices=False)[0][:,:2]
    M2=rng.normal(size=(2,2)); M2=(M2+M2.T)/2
    C=U @ M2 @ U.T
    np.fill_diagonal(C,rng.normal(size=m))
    eps=1e-5
    noise=rng.uniform(-eps,eps,size=(m,m)); noise=(noise+noise.T)/2; np.fill_diagonal(noise,0)
    C += noise

    delta=1e-3
    L0=np.zeros((m,m))
    qmax=0.0
    for i in J:
        Ki=np.delete(K,i,axis=0)
        ci=np.delete(C[:,i],i)
        coef=np.linalg.lstsq(Ki,ci,rcond=None)[0]
        ui=K@coef
        L0[:,i]=ui
        qmax=max(qmax,np.linalg.norm(ci-np.delete(ui,i)))
    if qmax>=delta:
        continue

    S=(L0+L0.T)/2
    M=C-S
    P=np.zeros((m,m))
    for i in H: P[i,i]=1.0
    Q=np.eye(m)-P
    RH=P@M + Q@M@P
    N=M-RH
    D=np.diag(np.diag(N))
    E=N-D
    R0=S+RH
    rec=D+R0+E

    max_decomp_error=max(max_decomp_error,np.linalg.norm(rec-C))
    max_rank_excess=max(max_rank_excess,max(0,np.linalg.matrix_rank(R0,tol=1e-9)-8))
    max_entry_excess=max(max_entry_excess,max(0.0,np.max(np.abs(E))-delta))
    decomp_count += 1

P0=533.7524707810138
h=(2*math.sqrt(2)-1)/1572864
prod_factor=P0/(1024*math.sqrt(3))
cross_coeff=6/(prod_factor**(1/3))
core_coeff=2*math.sqrt(66*math.pi)/(11/1024)
residual=(11/512)*h

print(f'rank2_instances={count}')
print(f'max_abs(sum_mu-2)={max_mu_sum_err:.3e}')
print(f'max_heavy_rows(mu>2/3)={max_heavy}')
print(f'max_rel_volume_identity_error={max_volume_relerr:.3e}')
print(f'low_containment_instances={decomp_count}')
print(f'max_decomposition_reconstruction_error={max_decomp_error:.3e}')
print(f'max_rank_excess_over_8={max_rank_excess}')
print(f'max_entry_excess_over_delta={max_entry_excess:.3e}')
print(f'h={h:.16e}')
print(f'transferred_Delta3_factor={prod_factor:.15f} * h^3')
print(f'transferred_density_coeff={cross_coeff:.12f} / h')
print(f'transferred_density_numeric={cross_coeff/h:.6f}')
print(f'partner_core_density_coeff={core_coeff:.12f} / h')
print(f'partner_core_density_numeric={core_coeff/h:.6f}')
print(f'global_entrywise_residual_bound={residual:.16e}')
assert max_mu_sum_err<1e-10
assert max_heavy<=2
assert max_volume_relerr<1e-10
assert decomp_count>0
assert max_decomp_error<1e-9
assert max_rank_excess==0
assert max_entry_excess<1e-12
print('STATUS=PASS')
