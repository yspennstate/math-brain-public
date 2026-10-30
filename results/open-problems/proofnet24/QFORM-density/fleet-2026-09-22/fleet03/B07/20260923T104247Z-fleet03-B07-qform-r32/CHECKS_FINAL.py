import itertools, math
import numpy as np

rng=np.random.default_rng(320260923)
NCASES=2000
counts=[0,0,0]
min_lift_ratio=float('inf')
min_h3_ratio=float('inf')

def anchored_w(M):
    nr,nc=M.shape
    s=0.0
    for rs in itertools.combinations(range(1,nr),2):
        rows=(0,)+rs
        for cs in itertools.combinations(range(1,nc),2):
            cols=(0,)+cs
            s += float(np.linalg.det(M[np.ix_(rows,cols)]))**2
    return s

def anchored_z(M):
    b=M[0,0]; r=M[0,1:]; c=M[1:,0]; B=M[1:,1:]
    K=b*B-np.outer(c,r)
    return float(np.sum(K*K)), np.linalg.norm(r)*np.linalg.norm(c), K

for _ in range(NCASES):
    nr=int(rng.integers(3,7)); nc=int(rng.integers(3,7))
    M=rng.normal(size=(nr,nc))
    Z,P,K=anchored_z(M)
    svals=np.linalg.svd(M,compute_uv=False)
    T2=float(np.sum(svals[2:]**2))
    W=anchored_w(M)
    if Z*T2>1e-12:
        min_lift_ratio=min(min_lift_ratio,W/(0.5*T2*Z))
    assert W+1e-7 >=0.5*T2*Z
    if P<1e-12:
        continue
    if np.linalg.norm(K)<P/3:
        counts[0]+=1
        b=M[0,0]
        assert abs(b)>1e-12
        M0=np.outer(np.r_[b,M[1:,0]],np.r_[1.0,M[0,1:]/b])
        assert np.linalg.norm(M-M0) <0.5*np.linalg.norm(M)+1e-8
    elif T2<P/9:
        counts[1]+=1
        assert math.sqrt(T2)<np.linalg.norm(M)/3+1e-8
    else:
        counts[2]+=1
        ratio=W/(P**3/162)
        min_h3_ratio=min(min_h3_ratio,ratio)
        assert W+1e-8>=P**3/162

h=(2*math.sqrt(2)-1)/1572864
beta=math.sqrt(63)/16
assert abs(beta**2/9-7/256)<1e-15
assert abs(beta/12-math.sqrt(7)/64)<1e-15
assert abs(beta**3/162-7*math.sqrt(7)/24576)<1e-15
vol_factor=(9*math.sqrt(3)*math.e/2)*(162**(1/6))*beta**(-0.5)
terminal_factor=(81/16)*math.sqrt(math.pi)*math.sqrt(162)*beta**(-1.5)

print('cases',NCASES)
print('branch_counts_R1_R2_H3',counts)
print('min_W_over_half_T2Z',repr(min_lift_ratio))
print('min_W_over_P3_over_162_in_H3_branch',repr(min_h3_ratio))
print('h',repr(h))
print('beta',repr(beta))
print('partner_E2_constant',repr(beta**2/9))
print('partner_matching_product_constant',repr(beta/12))
print('partner_H3_constant',repr(beta**3/162))
print('volume_factor_times_h_inverse',repr(vol_factor))
print('volume_absolute_bound',repr(vol_factor/h))
print('terminal_core_factor_times_h_inverse',repr(terminal_factor))
print('terminal_core_absolute_bound',repr(terminal_factor/h))
print('STATUS=PASS')