import math
import numpy as np

rng=np.random.default_rng(20260924049)

tau=2**-16
b0=1/(64*math.sqrt(2))
theta=tau/(b0-tau)
f0=2**-12
R0=1/64
kappa0=1/64
eps0=f0+theta*(R0+f0)
eta0=eps0*(1+5/kappa0)
lev=(eta0/(1/2))**2

print('tau',tau)
print('b0',b0)
print('theta0',theta)
print('epsilon0',eps0)
print('eta0',eta0)
print('half_scale_leverage',lev)
assert lev < 1/32

# Lemma 2.1: actual top-two deleted row space versus the fixed rank-two deleted row space.
viol=0
max_ratio=0.0
count=0
for _ in range(10000):
    m=int(rng.integers(4,20)); n=int(rng.integers(4,20))
    U,_=np.linalg.qr(rng.normal(size=(m,2)))
    V,_=np.linalg.qr(rng.normal(size=(n,2)))
    s2=float(rng.uniform(1/64,0.1)); s1=float(rng.uniform(s2,0.3))
    ell=np.sum(V**2,axis=1)
    choices=np.where(ell<=0.5)[0]
    if len(choices)==0:
        continue
    j=int(rng.choice(choices)); keep=[k for k in range(n) if k!=j]
    A0=U@np.diag([s1,s2])@V[keep,:].T
    F=rng.normal(size=A0.shape)
    F*=float(rng.uniform(0,tau))/np.linalg.svd(F,compute_uv=False)[0]
    M=A0+F
    Q0,_=np.linalg.qr(V[keep,:])
    _,sv,Vh=np.linalg.svd(M,full_matrices=False)
    W=Vh[:2,:].T
    Pperp=np.eye(len(keep))-Q0@Q0.T
    lhs=np.linalg.svd(Pperp@W,compute_uv=False)[0]
    b=np.linalg.svd(A0,compute_uv=False)[1]
    fn=np.linalg.svd(F,compute_uv=False)[0]
    rhs=fn/(b-fn)
    if lhs>rhs+1e-10:
        viol+=1
    if rhs>0:
        max_ratio=max(max_ratio,lhs/rhs)
    count+=1
print('subspace_cases',count,'violations',viol,'max_lhs_over_bound',max_ratio)
assert viol==0

# Lemma 3.1: two-anchor common-plane rigidity.
viol=0
max_ratio=0.0
for _ in range(10000):
    m=int(rng.integers(4,24))
    V,_=np.linalg.qr(rng.normal(size=(m,2)))
    dets=[]
    for a in range(m):
        for b in range(a+1,m):
            dets.append((abs(np.linalg.det(np.stack([V[a],V[b]]))),a,b))
    kappa,a,b=max(dets)
    B0=rng.normal(size=(2,2)); B0=(B0+B0.T)/2
    q=rng.normal(size=m)
    E=rng.normal(size=(m,m)); E=(E+E.T)/2; np.fill_diagonal(E,0)
    E*=rng.uniform(1e-7,2e-3)/max(np.linalg.norm(E,axis=0).max(),1e-30)
    D=V@B0@V.T+np.diag(q)+E
    noise=rng.normal(size=(m,2))*rng.uniform(0,3e-4)
    C=np.array([B0@V[j]+noise[j] for j in range(m)])
    eps=0.0
    for j in range(m):
        pred=V@C[j]
        mask=np.arange(m)!=j
        eps=max(eps,np.linalg.norm((D[:,j]-pred)[mask]))
    M=np.column_stack([V[a],V[b]])
    Cout=np.column_stack([C[a],C[b]])
    T=Cout@np.linalg.inv(M)
    B=(T+T.T)/2
    Res=D-V@B@V.T
    Res=Res-np.diag(np.diag(Res))
    lhs=np.linalg.norm(Res,axis=0).max()
    rhs=eps*(1+5/kappa)
    if lhs>rhs+1e-10:
        viol+=1
    if rhs>0:
        max_ratio=max(max_ratio,lhs/rhs)
print('rigidity_cases',10000,'violations',viol,'max_lhs_over_bound',max_ratio)
assert viol==0

# Lemma 4.1 near-sharp rank-one spectral leverage stress.
viol=0
max_ratio=0.0
for _ in range(1000):
    m=int(rng.integers(40,1000))
    lam=eta0*math.sqrt(m)*float(rng.uniform(.5,1))
    u=np.ones(m)/math.sqrt(m)*math.sqrt(lam)
    E=np.outer(u,u)
    vals,vec=np.linalg.eigh(E)
    idx=np.where(np.abs(vals)>=0.5)[0]
    lhs=0.0 if len(idx)==0 else float(np.max(np.diag(vec[:,idx]@vec[:,idx].T)))
    row=float(np.linalg.norm(E,axis=1).max())
    rhs=(row/0.5)**2
    if lhs>rhs+1e-8:
        viol+=1
    if rhs>0:
        max_ratio=max(max_ratio,lhs/rhs)
print('spectral_leverage_cases',1000,'violations',viol,'max_lhs_over_bound',max_ratio)
assert viol==0

partner=34*math.sqrt(math.log(math.e*2**32))
pair=27.2653244653667*(1/64)**(-1/10)*(2**-12)**(-2/5)
print('partner_D_2^-32_bound',partner)
print('fresh_pair_gate_bound',pair)
print('QFORM_B19_R49_COMMONPLANE_CHECK_PASS')
