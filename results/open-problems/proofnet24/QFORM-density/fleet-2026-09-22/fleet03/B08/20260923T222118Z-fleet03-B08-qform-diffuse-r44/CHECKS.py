import itertools, math
import numpy as np

C0 = 3 * 2**(5/6)
c = 27/256
mu_gate = c/(2+3*c)
Cdiff = C0*c**(-1/6)
assert abs(mu_gate - 27/593) < 1e-15
assert abs(Cdiff - (2**(13/6))*math.sqrt(3)) < 1e-12
assert abs(3*2**(5/6)*2**(2/3) - 6*math.sqrt(2)) < 1e-12

# Exact projected common-plane cancellation on seeded random matrices.
rng = np.random.default_rng(20260923222118)
max_cancel = 0.0
for _ in range(500):
    m1,m2 = 8,7
    M1 = rng.normal(size=(2,m1)); M2 = rng.normal(size=(2,m2))
    K = np.sort(rng.choice(m1,size=4,replace=False))
    Kc = np.array([i for i in range(m1) if i not in set(K)])
    MK = M1[:,K]
    if np.linalg.matrix_rank(MK) < 2: continue
    P = MK.T @ np.linalg.inv(MK@MK.T) @ MK
    R = rng.normal(size=(2,2)); R=(R+R.T)/2
    S1 = rng.normal(size=(m1,m1)); S1=(S1+S1.T)/2
    cross = np.vstack([M1[:,Kc].T@R@MK + S1[np.ix_(Kc,K)], M2.T@R@MK])
    lhs = cross@(np.eye(len(K))-P)
    rhs = np.vstack([S1[np.ix_(Kc,K)]@(np.eye(len(K))-P), np.zeros((m2,len(K)))])
    max_cancel=max(max_cancel,float(np.max(np.abs(lhs-rhs))))
assert max_cancel < 1e-10

# Exact expectation identity used in the random-cut proof, checked by enumeration.
def cut_expectation(M,q,p=0.75):
    m=M.shape[1]; W=np.vstack([M,q[None,:]])
    exact=0.0
    for mask in range(1<<m):
        K=[i for i in range(m) if (mask>>i)&1]
        prob=p**len(K)*(1-p)**(m-len(K))
        det=0.0 if len(K)<3 else max(0.0,float(np.linalg.det(W[:,K]@W[:,K].T)))
        Kc=[i for i in range(m) if i not in K]
        exact += prob*det*float(np.sum(q[Kc]**2))
    cb=0.0
    for I in itertools.combinations(range(m),3):
        d=float(np.linalg.det(W[:,I]))
        cb += d*d*(1-float(np.sum(q[list(I)]**2)))
    return exact,p**3*(1-p)*cb

rng=np.random.default_rng(20260923)
max_expect=0.0
for _ in range(30):
    M=rng.normal(size=(2,7)); q=rng.normal(size=7); q/=np.linalg.norm(q)
    a,b=cut_expectation(M,q)
    max_expect=max(max_expect,abs(a-b))
assert max_expect < 1e-10

# Sylvester-Hadamard exact-match stress family cuts, m=8,16,32.
def chars(d):
    xs=np.array(list(itertools.product([0,1],repeat=d)),dtype=int)
    return np.array([(-1)**((xs@a)%2)/math.sqrt(len(xs)) for a in xs])

stress=[]
for d in (3,4,5):
    H=chars(d); m=2**d; a,b,qidx=1,2,3
    forbidden={0,a^b,a^qidx,b^qidx}
    h=next(z for z in range(1,m) if z not in forbidden)
    r1,r2,q=H[a],H[b],H[qidx]
    sign=H[h]*math.sqrt(m); K=sign>0; I=~K
    MK=np.stack([r1[K],r2[K]])
    G=MK@MK.T
    area=math.sqrt(float(np.linalg.det(G)))
    inner=np.max(np.abs(MK@q[K]))
    F=float(np.linalg.norm(q[I])*np.linalg.norm(q[K]))
    alpha=float(np.max(q[I]**2*np.linalg.norm(q[K])**2/F**2))
    assert np.max(np.abs(G-0.5*np.eye(2))) < 1e-12
    assert inner < 1e-12
    assert abs(area-0.5)<1e-12 and abs(F-0.5)<1e-12
    assert abs(alpha-2/m)<1e-12
    stress.append((m,area,F,alpha))

print('QFORM_B08_R44_CHECK_PASS')
print('C0_grouped=',repr(C0))
print('c_random_cut=',repr(c))
print('mu_gate=',repr(mu_gate),' exact=27/593')
print('Cdiff=',repr(Cdiff))
print('stress_constant_6sqrt2=',repr(6*math.sqrt(2)))
print('max_commonplane_projection_error=',repr(max_cancel))
print('max_random_cut_expectation_error=',repr(max_expect))
for row in stress: print('stress',row)
