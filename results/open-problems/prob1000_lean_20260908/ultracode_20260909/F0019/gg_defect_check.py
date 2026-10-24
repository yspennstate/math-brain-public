# F0019: check the exact formula  d/dbeta E[OV_n] = 2 beta n E< R12^2 + 3 R12 R34 - 4 R13 R23 >
# (Gaussian environment, replicas under mu_n^{(x)4}), by exact two-time marginals in d=1 at small n.
# Also re-check p_n' = beta(1 - E OV_n) at beta=2 with more samples, and a small d=2 monotonicity test.
import numpy as np, time, json
rng = np.random.default_rng(7)

def forward_backward(omega, beta):
    n = omega.shape[0]-1; L = omega.shape[1]
    F = np.zeros(L); F[n] = 1.0; Fs=[F.copy()]; logZ=0.0
    for k in range(1,n+1):
        pred = np.zeros(L); pred[1:] += F[:-1]; pred[:-1] += F[1:]; pred*=0.5
        F = pred*np.exp(beta*omega[k]); s=F.sum(); logZ+=np.log(s); F/=s; Fs.append(F.copy())
    B = np.ones(L); Bs=[None]*(n+1); Bs[n]=B.copy()
    for k in range(n,0,-1):
        g = np.exp(beta*omega[k])*B
        Bn = np.zeros(L); Bn[1:]+=g[:-1]; Bn[:-1]+=g[1:]; Bn*=0.5
        B = Bn/Bn.max(); Bs[k-1]=B.copy()
    return Fs, Bs, logZ

def two_time(omega, beta):
    """Returns marg[k] (L,) and joint[k][l] (L,L) for 1<=k<l<=n under mu_n."""
    n = omega.shape[0]-1; L = omega.shape[1]
    Fs, Bs, logZ = forward_backward(omega, beta)
    marg = {}
    for k in range(1,n+1):
        m = Fs[k]*Bs[k]; marg[k] = m/m.sum()
    joint = {}
    for k in range(1,n):
        # propagate from each x at time k: P[x, y] unnormalised weight of paths (k,x)->(l,y)
        P = np.eye(L)
        for l in range(k+1,n+1):
            Pn = np.zeros_like(P); Pn[:,1:]+=P[:,:-1]; Pn[:,:-1]+=P[:,1:]; Pn*=0.5
            P = Pn*np.exp(beta*omega[l])[None,:]
            P /= max(P.max(),1e-300)
            J = Fs[k][:,None]*P*Bs[l][None,:]
            J /= J.sum()
            joint[(k,l)] = J
    return marg, joint, logZ

def replica_functionals(omega, beta):
    n = omega.shape[0]-1
    marg, joint, logZ = two_time(omega, beta)
    R12 = sum(np.sum(marg[k]**2) for k in marg)/n
    S12sq = 0.0; S1323 = 0.0
    for k in range(1,n+1):
        # diagonal k=l terms: R12^2 term: sum_x mu_k(x)^2 ; R13R23: sum_x mu_k(x)^3
        S12sq += np.sum(marg[k]**2); S1323 += np.sum(marg[k]**3)
    for (k,l),J in joint.items():
        S12sq += 2*np.sum(J**2)
        S1323 += 2*np.sum(marg[k][:,None]*marg[l][None,:]*J)
    R12sq = S12sq/n**2; R1323 = S1323/n**2; R12R34 = R12**2
    return R12, R12sq, R1323, R12R34, logZ

t0=time.time()
n=12; L=2*n+1; M=400; h=0.02
out={}
for beta in [0.5,1.0,2.0]:
    lhs=0.0; rhs=0.0
    for _ in range(M):
        w = rng.standard_normal((n+1,L))
        R12,R12sq,R1323,R12R34,_ = replica_functionals(w,beta)
        rhs += 2*beta*n*(R12sq + 3*R12R34 - 4*R1323)
        # finite difference of OV_n(beta) on the same environment
        Rp = replica_functionals(w,beta+h)[0]; Rm = replica_functionals(w,beta-h)[0]
        lhs += (Rp-Rm)/(2*h)
    out[beta]=(lhs/M, rhs/M)
    print(f"n={n} beta={beta}: FD d/dbeta E OV_n = {lhs/M:.4f}   2 beta n E<R12^2+3R12R34-4R13R23> = {rhs/M:.4f}")
print("elapsed", round(time.time()-t0,1))

# re-check identity at beta=2, n=100, M=800, h=0.01
def layers_ov(omega,beta):
    Fs,Bs,logZ = forward_backward(omega,beta); n=omega.shape[0]-1
    ov=0.0
    for k in range(1,n+1):
        m=Fs[k]*Bs[k]; m/=m.sum(); ov+=np.sum(m**2)
    return ov/n, logZ
n=60; M=300; h=0.01; beta=2.0; d=0.0; ov=0.0
for _ in range(M):
    w=rng.standard_normal((n+1,2*n+1))
    _,lp=layers_ov(w,beta+h); _,lm=layers_ov(w,beta-h); o,_=layers_ov(w,beta)
    d+=(lp-lm)/(2*h)/n; ov+=o
print(f"identity recheck beta=2 n=100 M=800: FD p_n'={d/M:.4f}  beta(1-E OV_n)={beta*(1-ov/M):.4f}")
out['identity_beta2']=(d/M, beta*(1-ov/M))

# d=2 mean-overlap monotonicity, n=24, M=60
def ov_d2(omega,beta):
    n=omega.shape[0]-1; L=omega.shape[1]
    F=np.zeros((L,L)); F[n,n]=1.0; Fs=[F.copy()]
    def nb(A):
        P=np.zeros_like(A); P[1:,:]+=A[:-1,:]; P[:-1,:]+=A[1:,:]; P[:,1:]+=A[:,:-1]; P[:,:-1]+=A[:,1:]; return P*0.25
    for k in range(1,n+1):
        F=nb(F)*np.exp(beta*omega[k]); F/=F.sum(); Fs.append(F.copy())
    B=np.ones((L,L)); ov=0.0
    for k in range(n,0,-1):
        m=Fs[k]*B; m/=m.sum(); ov+=np.sum(m**2)
        B=nb(np.exp(beta*omega[k])*B); B/=B.max()
    return ov/n
n=16; L=2*n+1; M=30; betas=[0.25,0.5,0.75,1.0,1.5,2.0,3.0]
mean=np.zeros(len(betas)); viol=0
for _ in range(M):
    w=rng.standard_normal((n+1,L,L))
    v=np.array([ov_d2(w,b) for b in betas]); mean+=v
    if (np.diff(v)<-1e-12).any(): viol+=1
mean/=M
print("d=2 n=24 M=60 mean OV_n(beta):", dict(zip(betas,np.round(mean,4).tolist())), "pathwise violations:", viol)
out['d2']={'betas':betas,'mean':mean.tolist(),'viol':viol,'M':M}
json.dump(out,open('gg_defect_results.json','w',encoding='utf-8'),indent=1,default=str)
print("total elapsed", round(time.time()-t0,1))
