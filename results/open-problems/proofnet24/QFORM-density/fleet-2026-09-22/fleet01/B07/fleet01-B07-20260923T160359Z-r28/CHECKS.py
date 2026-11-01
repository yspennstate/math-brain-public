import itertools, math, numpy as np

rng=np.random.default_rng(20260923)
h=0.75
rho0=2.25-math.sqrt(5)
viol=0
cases=0
macro_cases=0
min_macro_ratio=1.0

def e2(s):
    lam=s*s
    return sum(lam[i]*lam[j] for i in range(len(lam)) for j in range(i+1,len(lam)))

for m,n in [(4,4),(5,6),(8,7)]:
    rows=list(itertools.combinations(range(m),2))
    cols=list(itertools.combinations(range(n),2))
    for _ in range(400):
        M=rng.normal(size=(m,n))
        U,s,Vt=np.linalg.svd(M,full_matrices=False)
        Om=e2(s)
        P=(s[0]*s[1])**2
        delta=Om-P
        E=np.sum(s*s)
        T2=np.sum(s[2:]**2)
        assert delta <= E*T2 + 1e-9*max(1.0,Om)
        D=np.array([[np.linalg.det(M[np.ix_(R,C)]) for C in cols] for R in rows])
        M2=(U[:,:2]*s[:2])@Vt[:2,:]
        D0=np.array([[np.linalg.det(M2[np.ix_(R,C)]) for C in cols] for R in rows])
        W=D*D/Om
        W0=D0*D0/P
        tv=0.5*np.abs(W-W0).sum()
        rho=delta/Om
        assert tv <= math.sqrt(rho)+rho/2+1e-9
        cases+=1

for _ in range(1000):
    m=n=5
    A=np.eye(m,2)+0.03*rng.normal(size=(m,2))
    U,_=np.linalg.qr(A)
    B=np.eye(n,2)+0.03*rng.normal(size=(n,2))
    V,_=np.linalg.qr(B)
    Qu,_=np.linalg.qr(np.column_stack([U,rng.normal(size=(m,m-2))]))
    Qv,_=np.linalg.qr(np.column_stack([V,rng.normal(size=(n,n-2))]))
    s=np.array([2.0,1.2,0.01,0.008,0.004])
    M=Qu@np.diag(s)@Qv.T
    Us,ss,Vts=np.linalg.svd(M,full_matrices=False)
    Om=e2(ss)
    P=(ss[0]*ss[1])**2
    rho=(Om-P)/Om
    levU=np.sum(Us[:,:2]**2,axis=1)
    levV=np.sum(Vts[:2,:]**2,axis=0)
    ir=np.where(levU>=h)[0]
    jc=np.where(levV>=h)[0]
    if rho<=rho0 and len(ir)>=2 and len(jc)>=2:
        R=tuple(ir[:2]); C=tuple(jc[:2])
        ratio=np.linalg.det(M[np.ix_(R,C)])**2/Om
        min_macro_ratio=min(min_macro_ratio,ratio)
        assert ratio >= 1/8-1e-9
        macro_cases+=1

print('generic_cases=',cases)
print('targeted_macro_cases=',macro_cases)
print('violations=',viol)
print('min_targeted_macro_ratio=',min_macro_ratio)
print('rho0=',rho0)
print('STATUS=PASS')
