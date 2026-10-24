import itertools, math
import numpy as np

rng=np.random.default_rng(20260923)
NCASES=5000
rank_tube_cases=0
max_ratio=0.0
max_tail_ratio=0.0

def e2_exact(M):
    out=0
    nr,nc=M.shape
    for i,j in itertools.combinations(range(nr),2):
        for a,b in itertools.combinations(range(nc),2):
            d=int(M[i,a])*int(M[j,b])-int(M[i,b])*int(M[j,a])
            out += d*d
    return out

def e2_e3_svd(M):
    s=np.linalg.svd(M.astype(float),compute_uv=False)
    lam=s*s
    e2=sum(lam[i]*lam[j] for i in range(len(lam)) for j in range(i+1,len(lam)))
    e3=sum(lam[i]*lam[j]*lam[k]
           for i in range(len(lam))
           for j in range(i+1,len(lam))
           for k in range(j+1,len(lam)))
    t2=sum(lam[2:])
    return e2,e3,t2

for q in range(NCASES):
    nr=int(rng.integers(2,8)); nc=int(rng.integers(2,8))
    M=rng.integers(-5,6,size=(nr,nc),dtype=np.int64)
    b=float(M[0,0]); r=M[0,1:].astype(float); c=M[1:,0].astype(float)
    B=M[1:,1:].astype(float)
    P=np.linalg.norm(r)*np.linalg.norm(c)
    K=b*B-np.outer(c,r)
    K2=float(np.sum(K*K))
    E2x=e2_exact(M)
    assert K2 <= E2x+1e-9
    if E2x>0: max_ratio=max(max_ratio,K2/E2x)

    if P>1e-12 and np.linalg.norm(K)<P/3:
        rank_tube_cases += 1
        assert abs(b)>1e-12
        M0=np.outer(np.r_[b,c],np.r_[1.0,r/b])
        err=np.linalg.norm(M.astype(float)-M0)
        assert err < 0.5*np.linalg.norm(M.astype(float))+1e-10

    e2,e3,t2=e2_e3_svd(M)
    if e3>1e-10:
        max_tail_ratio=max(max_tail_ratio,t2*e2/(3*e3))
    assert t2*e2 <= 3*e3 + 1e-6*max(1.0,e3)

h=(2*math.sqrt(2)-1)/1572864
beta=math.sqrt(63)/16
assert abs(beta*beta/9-7/256)<1e-15
assert abs(beta/12-math.sqrt(7)/64)<1e-15
assert abs(beta**3/243-7*math.sqrt(7)/36864)<1e-15
vol_factor=(9*math.sqrt(3)*math.e/2)*(243**(1/6))*beta**(-0.5)

print("cases",NCASES)
print("rank_tube_cases",rank_tube_cases)
print("max_fixed_minor_energy_over_E2",repr(max_ratio))
print("max_T2E2_over_3E3",repr(max_tail_ratio))
print("h",repr(h))
print("beta",repr(beta))
print("partner_scale_E2_constant",repr(beta*beta/9))
print("partner_scale_matching_norm_product_constant",repr(beta/12))
print("partner_scale_high_tail_E3_constant",repr(beta**3/243))
print("volume_bound_factor_times_h_inverse",repr(vol_factor))
print("volume_absolute_bound",repr(vol_factor/h))
print("STATUS=PASS")