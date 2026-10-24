import numpy as np, math
rng=np.random.default_rng(0)
max_id=max_sumerr=max_violation=0.0
max_heavy=0
for trial in range(500):
    m=int(rng.integers(4,9)); n=int(rng.integers(3,8))
    K=rng.normal(size=(m,n)); G=K@K.T
    tr=float(np.trace(G)); Z=(tr*tr-float(np.trace(G@G)))/2
    if Z<1e-12: continue
    mus=[]
    for i in range(m):
        Ki=np.delete(K,i,axis=0); Gi=Ki@Ki.T
        tri=float(np.trace(Gi)); Zi=(tri*tri-float(np.trace(Gi@Gi)))/2
        mus.append(1-Zi/Z)
        c=rng.normal(size=m-1)
        Bi=np.column_stack([Ki,c]); GB=Bi@Bi.T
        trb=float(np.trace(GB))
        e3b=(trb**3-3*trb*float(np.trace(GB@GB))+2*float(np.trace(GB@GB@GB)))/6
        e3i=(tri**3-3*tri*float(np.trace(Gi@Gi))+2*float(np.trace(Gi@Gi@Gi)))/6
        H2=Gi@Gi-tri*Gi+Zi*np.eye(m-1)
        rhs=e3i+float(c@H2@c)
        max_id=max(max_id,abs(e3b-rhs)/(1+abs(e3b)))
        vals,U=np.linalg.eigh(Gi)
        alpha=vals*(tri-vals)/Zi if Zi>1e-12 else np.zeros_like(vals)
        heavy=alpha>2/3+1e-12
        max_heavy=max(max_heavy,int(heavy.sum()))
        P=U[:,heavy]@U[:,heavy].T if heavy.any() else np.zeros_like(Gi)
        q=np.linalg.norm((np.eye(m-1)-P)@c)
        max_violation=max(max_violation,max(0.0,(Zi/3)*q*q-float(c@H2@c)))
    max_sumerr=max(max_sumerr,abs(sum(mus)-2))
Z0=854675.100194511
e3coeff=Z0/(9*1024**2)
C3=10.5501688311648
dens=C3*e3coeff**(-1/6)
minor_count=math.ceil(e3coeff*262144/27)
print('max_newton_relative_error=',max_id)
print('max_physical_marginal_sum_error=',max_sumerr)
print('max_spectral_heavy_count=',max_heavy)
print('max_loewner_scalar_violation=',max_violation)
print('e3_coefficient=',e3coeff)
print('density_coefficient_times_h^-1=',dens)
print('min_nonzero_3x3_minors=',minor_count)
print('STATUS=PASS')
