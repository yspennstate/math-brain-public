import numpy as np, itertools, math
rng=np.random.default_rng(20260924064126)
dstar=0.10429071727552326290
pstar=1.19876993884320
eps=2**-16
z0=pstar*pstar/3
tau=2**-30
cN=dstar/math.sqrt(2)-eps
r=eps**2/cN**2
eta=math.sqrt(2)*eps/cN
q2=32*tau/z0
D2=64*tau/z0+2*eta**2
D0=math.sqrt(D2)
gamma=1/64-27*D0
partner=2*math.sqrt(6*math.pi*27)/gamma
density=10.5501688311648*tau**(-1/6)

def H2(G):
    tr=np.trace(G)
    e2=0.5*(tr*tr-np.trace(G@G))
    return G@G-tr*G+e2*np.eye(G.shape[0])

def e3_cross(C):
    m,n=C.shape
    out=0.0
    if m<3 or n<3:
        return 0.0
    for I in itertools.combinations(range(m),3):
        for J in itertools.combinations(range(n),3):
            out += np.linalg.det(C[np.ix_(I,J)])**2
    return out

max_id=0.0
min_ratio=1e300
for trial in range(120):
    n=10
    B=rng.integers(-4,5,size=(n,n)).astype(float)
    A=(B+B.T)/2
    T=list(range(4))
    S=list(range(4,10))
    pairs=[(4,5),(6,7),(8,9)]
    totalF=0.0
    for K in pairs:
        cols=[j for j in S if j not in K]
        N=A[np.ix_(T,cols)]
        R=A[np.ix_(list(K),cols)]
        F=float(np.trace(R@H2(N.T@N)@R.T))
        direct=0.0
        for rr in K:
            for I in itertools.combinations(T,2):
                for J in itertools.combinations(cols,3):
                    direct += np.linalg.det(A[np.ix_(list(I)+[rr],list(J))])**2
        max_id=max(max_id,abs(F-direct)/(1+abs(direct)))
        totalF += F
    vals=[]
    for bits in itertools.product([0,1],repeat=3):
        moved=set()
        for bit,K in zip(bits,pairs):
            if bit:
                moved.update(K)
        L=T+sorted(moved)
        Rcols=[j for j in S if j not in moved]
        vals.append(e3_cross(A[np.ix_(L,Rcols)]))
    avg=sum(vals)/len(vals)
    if totalF>1e-12:
        min_ratio=min(min_ratio,avg/(totalF/16))
assert max_id<1e-10
assert min_ratio>=1-1e-10

max_alpha=0.0
max_angle=0.0
max_heavy_pairs=0
for trial in range(300):
    m,n=8,20
    U,_=np.linalg.qr(rng.normal(size=(m,2)))
    V,_=np.linalg.qr(rng.normal(size=(n,2)))
    s1=10**rng.uniform(0,4)
    s2=max(dstar*1.2,10**rng.uniform(-0.2,0.5))
    L=U@np.diag([s1,s2])@V.T
    E=rng.normal(size=(m,n))
    E=E/np.linalg.norm(E,'fro')*(eps*rng.uniform(0.05,0.8))
    M=L+E
    Ug,sg,Vtg=np.linalg.svd(M,full_matrices=False)
    Lg=(Ug[:,:2]*sg[:2])@Vtg[:2,:]
    Eg=M-Lg
    if sg[1]<=dstar or np.linalg.norm(Eg,'fro')>=eps:
        continue
    Vg=Vtg[:2,:].T
    ells=[]
    for a in range(0,n,2):
        K=[a,a+1]
        ell=np.linalg.norm(Vg[K,:],'fro')**2
        ells.append(ell)
        if ell>0.5:
            continue
        cols=[j for j in range(n) if j not in K]
        N=M[:,cols]
        Un,sn,Vtn=np.linalg.svd(N,full_matrices=False)
        x=sn*sn
        Z=sum(x[i]*x[j] for i in range(len(x)) for j in range(i+1,len(x)))
        if len(x)>2:
            alpha=max(xx*(x.sum()-xx)/Z for xx in x[2:])
            max_alpha=max(max_alpha,alpha)
        Vminus=Vg[cols,:]
        Q,_=np.linalg.qr(Vminus)
        P=Vtn[:2,:].T
        ang=np.linalg.norm((np.eye(len(cols))-Q@Q.T)@P,'fro')
        max_angle=max(max_angle,ang)
    max_heavy_pairs=max(max_heavy_pairs,sum(x>0.5 for x in ells))
assert max_heavy_pairs<=3
assert max_alpha < 0.5
assert max_angle <= eta*(1+1e-6)

print('PAIR_PACKET_MAX_RELERR=%.3e'%max_id)
print('RANDOM_CUT_MIN_RATIO=%.12f'%min_ratio)
print('MAX_LEVERAGE_HEAVY_PAIRS=%d'%max_heavy_pairs)
print('TAIL_ALPHA_ANALYTIC_BOUND=%.15e'%(2*r+r*r))
print('MAX_OBSERVED_TAIL_ALPHA=%.15e'%max_alpha)
print('COMMON_PLANE_ETA=%.15e'%eta)
print('MAX_OBSERVED_PLANE_DISTANCE=%.15e'%max_angle)
print('QSUM2_UNPAID_BOUND=%.15e'%q2)
print('QSUM_UNPAID_BOUND=%.15e'%math.sqrt(q2))
print('D0_ESTAR_LE_1=%.15e'%D0)
print('PARTNER_GAMMA=%.15e'%gamma)
print('PARTNER_DENSITY_BOUND=%.12f'%partner)
print('E3_DENSITY_BOUND=%.12f'%density)
print('STATUS=PASS')
