import itertools, math
import numpy as np

rng=np.random.default_rng(20260923)
max_cb=0.0
max_pair=0.0
min_wedge_ratio=float('inf')

for _ in range(1000):
    m=int(rng.integers(4,10))
    C=rng.normal(size=(m,3))
    G=C.T@C
    if np.linalg.det(G)<1e-12:
        continue
    P=C@np.linalg.inv(G)@C.T
    detG=float(np.linalg.det(G))
    triples=list(itertools.combinations(range(m),3))
    weights={S: float(np.linalg.det(C[list(S),:])**2) for S in triples}
    total=sum(weights.values())
    max_cb=max(max_cb,abs(total-detG)/(1+abs(detG)))
    for i in range(m):
        Zi=sum(v for S,v in weights.items() if i in S)
        max_cb=max(max_cb,abs(Zi-P[i,i]*detG)/(1+abs(detG)))
        for k in range(i+1,m):
            Zik=sum(v for S,v in weights.items() if i in S and k in S)
            pair=P[i,i]*P[k,k]-P[i,k]**2
            max_pair=max(max_pair,abs(Zik-pair*detG)/(1+abs(detG)))
    U,s,Vt=np.linalg.svd(C,full_matrices=False)
    for _j in range(3):
        i,k=map(int,rng.choice(m,size=2,replace=False))
        e2=0.0
        for cols in itertools.combinations(range(3),2):
            e2+=float(np.linalg.det(C[[i,k]][:,list(cols)])**2)
        pair=P[i,i]*P[k,k]-P[i,k]**2
        denom=(s[1]*s[2])**2*pair
        if denom>1e-12:
            min_wedge_ratio=min(min_wedge_ratio,e2/denom)

cross_L16=48*math.sqrt(2)
joined_R1R2=48*math.sqrt(2)/(3**(1/3))
early=25*math.e*math.sqrt(5/6)*2**(-0.1)
early_L16=16*early
l3=3**(2/3)*2**(1/3)*5**(1/6)
l3_L16=l3*16**(2/3)
partner=(2**(4/3)+1)*math.sqrt(3)*2**(1/4)

print(f'cross_rank3_L16={cross_L16:.15f}')
print(f'joined_R1R2_constant={joined_R1R2:.15f}')
print(f'checkpoint_diffuse_gamma={early:.15f}')
print(f'checkpoint_diffuse_L16={early_L16:.15f}')
print(f'checkpoint_L3_gamma={l3:.15f}')
print(f'checkpoint_L3_L16={l3_L16:.15f}')
print(f'partner_constant={partner:.15f}')
print(f'max_cauchy_binet_leverage_error={max_cb:.3e}')
print(f'max_pair_DPP_error={max_pair:.3e}')
print(f'min_wedge_ratio={min_wedge_ratio:.12f}')
assert cross_L16 < 68
assert joined_R1R2 < 47.067
assert partner < 7.251
assert max_cb < 1e-10
assert max_pair < 1e-10
assert min_wedge_ratio >= 1-1e-10
print('QFORM_B08_R41_CHECK_PASS')
