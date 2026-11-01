import numpy as np
rng=np.random.default_rng(31337)
def mmpp_c2(Q,lam):
    m=len(lam); D=np.diag(lam)
    # stationary pi of Q
    A=np.vstack([Q.T, np.ones(m)])
    b=np.zeros(m+1); b[-1]=1
    pi,*_=np.linalg.lstsq(A,b,rcond=None)
    D0=Q-D
    M=np.linalg.inv(-D0)
    th=pi@D; s=th.sum()
    if s<=0: return None,None
    th=th/s
    one=np.ones(m)
    m1=th@M@one
    m2=2*(th@M@M@one)
    if m1<=0: return None,None
    c2=m2/(m1*m1)-1
    return c2, 1.0/(pi@lam)   # second value: mean interarrival should equal 1/(pi.lambda)
def rand_Q(m,rng,cyclic=False,skew=0.0):
    if cyclic:
        Q=np.zeros((m,m))
        for i in range(m):
            Q[i,(i+1)%m]=rng.exponential()*(1+skew)
            Q[i,(i-1)%m]+=rng.exponential()*max(1e-9,1-skew)
    else:
        Q=rng.exponential(size=(m,m))
    np.fill_diagonal(Q,0)
    np.fill_diagonal(Q,-Q.sum(1))
    return Q
print("Validation: does the phase-type mean equal 1/(pi.lambda)?")
for m in [2,3,4]:
    Q=rand_Q(m,rng); lam=rng.exponential(size=m)*3
    c2,chk=mmpp_c2(Q,lam)
    M=np.linalg.inv(-(Q-np.diag(lam)))
    Aa=np.vstack([Q.T,np.ones(m)]); bb=np.zeros(m+1); bb[-1]=1
    pi,*_=np.linalg.lstsq(Aa,bb,rcond=None)
    th=pi@np.diag(lam); th=th/th.sum()
    print(f"  m={m}: E[T]={th@M@np.ones(m):.8f}  1/(pi.lam)={chk:.8f}  c^2={c2:.6f}")
print()
print("Search for c^2 < 1 (a counterexample to the folklore conjecture):")
worst=1e9; wp=None; n=0; below=0
for m in [2,3,4,5,6,8]:
    wm=1e9
    for trial in range(40000):
        cyc = trial%3==0
        Q=rand_Q(m,rng,cyclic=cyc,skew=rng.random()*1.9)
        lam=np.exp(rng.normal(size=m)*rng.choice([0.5,2.0,4.0]))
        out=mmpp_c2(Q,lam)
        if out[0] is None: continue
        c2=out[0]; n+=1
        if c2<wm: wm=c2
        if c2<worst: worst=c2; wp=(m,Q.copy(),lam.copy())
        if c2<1-1e-9: below+=1
    print(f"  m={m}: min c^2 over 40000 random MMPPs = {wm:.8f}")
print(f"\n  total sampled {n}; instances with c^2 < 1: {below}; global min c^2 = {worst:.8f}")
