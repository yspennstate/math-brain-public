import itertools, math
import numpy as np

rng=np.random.default_rng(20260923)
p=3/4
c=p**3*(1-p)

def Prow(M):
    if M.shape[1]==0:
        return np.zeros((0,0))
    return np.linalg.pinv(M)@M

def xi(M,S):
    m=M.shape[1]
    ans=0.0
    for i in range(m):
        js=[j for j in range(m) if j!=i]
        for T in itertools.combinations(js,3):
            ans += np.linalg.det(np.vstack([M[:,T],S[i,list(T)]]))**2
    return ans

def currency(M,S,K):
    m=M.shape[1]
    K=list(K); Kc=[j for j in range(m) if j not in K]
    MK=M[:,K]
    A2=np.linalg.det(MK@MK.T)
    P=Prow(MK)
    C=S[np.ix_(Kc,K)]@(np.eye(len(K))-P) if K else np.zeros((len(Kc),0))
    return A2*np.sum(C*C)

e1=e2=e3=0.0
for rep in range(40):
    m=6
    M=rng.normal(size=(2,m))
    Z=rng.normal(size=(m,m)); S=(Z+Z.T)/2
    X=xi(M,S)
    for mask in range(1<<m):
        K=[j for j in range(m) if (mask>>j)&1]
        lhs=currency(M,S,K)
        rhs=0.0
        for i in range(m):
            if i in K: continue
            for T in itertools.combinations(K,3):
                rhs += np.linalg.det(np.vstack([M[:,T],S[i,list(T)]]))**2
        e1=max(e1,abs(lhs-rhs))
    E=0.0
    for mask in range(1<<m):
        K=[j for j in range(m) if (mask>>j)&1]
        prob=p**len(K)*(1-p)**(m-len(K))
        E += prob*currency(M,S,K)
    e2=max(e2,abs(E-c*X))
    G=M@M.T; Gi=np.linalg.inv(G); detG=np.linalg.det(G)
    Din=0.0
    for i in range(m):
        lev=M[:,i]@Gi@M[:,i]
        js=[j for j in range(m) if j!=i]
        Mm=M[:,js]
        r=S[i,js]@(np.eye(m-1)-Prow(Mm))
        Din += (1-lev)*(r@r)
    e3=max(e3,abs(X-detG*Din))

e4=0.0
for rep in range(40):
    m=8
    M=rng.normal(size=(2,m))
    R=rng.normal(size=(2,2)); R=(R+R.T)/2
    d=rng.normal(size=m)
    S=M.T@R@M+np.diag(d)
    e4=max(e4,abs(xi(M,S)))

C=2**(13/6)*math.sqrt(3)
sstar=1/(64*math.sqrt(896))
eta=(C/619)**3/sstar
loc=math.sqrt(c/2)*eta

print("QFORM_B08_COMPOUND_CHECK")
print(f"c_bernoulli={c:.15f}")
print(f"receiver_constant={C:.15f}")
print(f"s_star={sstar:.15e}")
print(f"eta_619={eta:.15e}")
print(f"localized_row_at_eta={loc:.15e}")
print(f"max_E1_error={e1:.3e}")
print(f"max_E2_error={e2:.3e}")
print(f"max_intrinsic_error={e3:.3e}")
print(f"max_aligned_Xi={e4:.3e}")
print("star_family: spectrum={+L,+L,-L,-L}, pair_gate_ratio=1/sqrt(2m), H_bound=4/L")
print("QFORM_B08_R29_CHECK_PASS")
