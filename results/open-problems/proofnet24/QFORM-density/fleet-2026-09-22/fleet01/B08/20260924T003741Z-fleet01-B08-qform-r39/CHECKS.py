import numpy as np

rng=np.random.default_rng(390024)
N=2000
max_mix=0.0
max_scalar=0.0
max_constraint=0.0
bad=0
for _ in range(N):
    m=int(rng.integers(4,25))
    Z=rng.normal(size=(m,2))
    U,_=np.linalg.qr(Z, mode='reduced')
    A=rng.normal(size=(2,2))
    R=(A+A.T)/2
    d=rng.normal(size=m)
    D=np.diag(d)
    G=-(U@R + D@U)
    S=U.T@G
    F=G@U.T + U@G.T - U@S@U.T
    E=U@R@U.T + D + F
    cerr=np.linalg.norm(E@U,'fro')/(1+np.linalg.norm(E,'fro'))
    max_constraint=max(max_constraint,cerr)
    vals,O=np.linalg.eigh(R)
    Ut=U@O
    Delta=abs(vals[1]-vals[0])
    x=Ut[:,0]
    y=Ut[:,1]
    ell=x*x+y*y
    mix=(Delta**2)*np.sum((x*x*y*y)/ell)
    den=np.linalg.norm(F,'fro')**2
    if den>1e-14:
        max_mix=max(max_mix,mix/den)
    r=0.5*(vals[0]+vals[1])
    lhs=np.sum(ell*(d+r)**2)
    rhs=2*den+Delta**2
    if rhs>1e-14:
        max_scalar=max(max_scalar,lhs/rhs)
    if mix>den+1e-9 or lhs>rhs+1e-9:
        bad+=1
print(f'trials={N}')
print(f'max_constraint_relative={max_constraint:.16e}')
print(f'max_mix_ratio={max_mix:.16f}')
print(f'max_scalar_ratio={max_scalar:.16f}')
print(f'violations={bad}')
print('QFORM_B08_R39_RIGIDITY_CHECK_PASS')
