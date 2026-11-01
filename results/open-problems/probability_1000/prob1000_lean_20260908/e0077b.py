import numpy as np
rng=np.random.default_rng(4242)
def pieces(Q,lam):
    m=len(lam); D=np.diag(lam)
    A=np.vstack([Q.T,np.ones(m)]); b=np.zeros(m+1); b[-1]=1
    pi,*_=np.linalg.lstsq(A,b,rcond=None)
    M=np.linalg.inv(D-Q)          # A = (D-Q)^{-1}
    one=np.ones(m)
    h=M@one                       # mean time to next arrival from each state
    th=pi@D; th=th/th.sum()
    m1=th@M@one; m2=2*(th@M@M@one)
    c2=m2/(m1*m1)-1
    cov=float(pi@(lam*h) - (pi@lam)*(pi@h))
    return c2,cov,float(pi@(lam*h)),pi,h,lam
def rand_Q(m,rng,cyclic=False,skew=0.0):
    if cyclic:
        Q=np.zeros((m,m))
        for i in range(m):
            Q[i,(i+1)%m]=rng.exponential()*(1+skew); Q[i,(i-1)%m]+=rng.exponential()*max(1e-9,1-skew)
    else:
        Q=rng.exponential(size=(m,m))
    np.fill_diagonal(Q,0); np.fill_diagonal(Q,-Q.sum(1)); return Q
print("Claim: pi.(lam*h) == 1 exactly, and  c^2 >= 1  <=>  Cov_pi(lam,h) <= 0.")
maxid=0; worstcov=-1e9; n=0; sign_mismatch=0
for m in [2,3,4,5,6,8,12]:
    for trial in range(20000):
        Q=rand_Q(m,rng,cyclic=(trial%3==0),skew=rng.random()*1.9)
        lam=np.exp(rng.normal(size=m)*rng.choice([0.5,2.0,4.0]))
        try: c2,cov,ident,pi,h,l=pieces(Q,lam)
        except Exception: continue
        n+=1
        maxid=max(maxid,abs(ident-1.0))
        if cov>worstcov: worstcov=cov
        if (c2>=1-1e-9) != (cov<=1e-12): sign_mismatch+=1
print(f"  sampled {n}")
print(f"  max |pi.(lam*h) - 1| = {maxid:.3e}   (the identity pi D h = 1)")
print(f"  largest Cov_pi(lam,h) seen = {worstcov:+.6e}   (must be <= 0 for the conjecture)")
print(f"  cases where sign(c^2-1) disagrees with sign(-Cov): {sign_mismatch}")
