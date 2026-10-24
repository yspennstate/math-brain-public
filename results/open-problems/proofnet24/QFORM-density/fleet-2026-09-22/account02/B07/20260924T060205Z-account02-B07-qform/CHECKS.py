import itertools, math, numpy as np

rng=np.random.default_rng(20260924)
worst=0.0
for _ in range(2000):
    r=int(rng.integers(3,10))
    s=np.sort(rng.lognormal(0.0,2.0,size=r))[::-1]
    x=s*s
    z2=sum(x[i]*x[j] for i in range(r) for j in range(i+1,r))
    z3=sum(x[i]*x[j]*x[k] for i in range(r) for j in range(i+1,r) for k in range(j+1,r))
    rem=z2-x[0]*x[1]
    if rem>0:
        ratio=(x[1]*rem/2.0)/z3
        assert ratio <= 1.0+1e-12
        worst=max(worst,ratio)

# Coordinate-minor TV inequality on random 5x5 matrices.
worst_tv_excess=0.0
for _ in range(250):
    M=rng.normal(size=(5,5))
    U,s,Vt=np.linalg.svd(M,full_matrices=False)
    rows=list(itertools.combinations(range(5),2))
    cols=list(itertools.combinations(range(5),2))
    ur=np.array([np.linalg.det(U[list(R),:2]) for R in rows])
    vr=np.array([np.linalg.det(Vt.T[list(C),:2]) for C in cols])
    z=[]; a=[]
    for ir,R in enumerate(rows):
        for jc,C in enumerate(cols):
            z.append(np.linalg.det(M[np.ix_(R,C)]))
            a.append(s[0]*s[1]*ur[ir]*vr[jc])
    z=np.asarray(z); a=np.asarray(a)
    Z=float(z@z); M0=float(a@a); R=Z-M0
    w=z/math.sqrt(Z); v=a/math.sqrt(M0)
    if float(w@v)<0: v=-v
    tv=0.5*float(np.abs(w*w-v*v).sum())
    excess=tv-math.sqrt(max(0.0,R/Z))
    assert excess <= 2e-12
    worst_tv_excess=max(worst_tv_excess,excess)

d=0.10429071727552326290
p=1.19876993884320
delta=d*d*p*p/288.0
C3=3*2**(4/3)*math.e**(1/3)
print('delta_star',repr(delta))
print('marginal_free_Z3_density_bound',repr(C3*delta**(-1/6)))
print('bounded_support_actual_E2',repr((131/192)*p*p))
print('stable_pair_leading_product',repr(p/2))
print('bounded_support_leading_product',repr((7/8)*p))
print('pinned_D_regression_bound',repr(12*math.sqrt(math.e)))
print('max_compound_ratio',repr(worst))
print('max_tv_excess',repr(worst_tv_excess))
print('STATUS=PASS')
