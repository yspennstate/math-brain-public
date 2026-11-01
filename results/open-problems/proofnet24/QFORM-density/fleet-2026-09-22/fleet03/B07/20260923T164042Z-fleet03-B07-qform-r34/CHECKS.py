import random, math

SEED=3407
rng=random.Random(SEED)

def e2_minor_exact(K):
    m=len(K); n=len(K[0]); out=0
    for i in range(m):
        for k in range(i+1,m):
            for j in range(n):
                for l in range(j+1,n):
                    d=K[i][j]*K[k][l]-K[i][l]*K[k][j]
                    out += d*d
    return out

def e2_gram_exact(K):
    m=len(K); n=len(K[0])
    G=[[sum(K[i][j]*K[k][j] for j in range(n)) for k in range(m)] for i in range(m)]
    tr=sum(G[i][i] for i in range(m))
    tr2=sum(G[i][k]*G[k][i] for i in range(m) for k in range(m))
    return (tr*tr-tr2)//2

count=0
for m in range(2,7):
    for n in range(2,7):
        for _ in range(25):
            K=[[rng.randint(-4,4) for _ in range(n)] for __ in range(m)]
            assert e2_minor_exact(K)==e2_gram_exact(K)
            count+=1

h=(2*math.sqrt(2)-1)/1572864
sigma_h=243.24294332152962
tau=1/64
entry_h=1/8
zeta=tau+entry_h/sigma_h
assert zeta < 1/32
assert 11*(1/16+zeta) < 15/16

e2_h4=sigma_h**4/4096
minor_count=math.floor(e2_h4*1024)+1
grid_norm_h=7*sigma_h/64
grid_entries=math.floor((grid_norm_h/entry_h)**2)+1
row_norm_h=15*sigma_h/64
row_entries=math.floor((row_norm_h/entry_h)**2)+1

def greedy_banks(weights,target,k):
    pos=0; banks=[]
    for _ in range(k):
        mass=0.0; inds=[]
        while pos<len(weights) and mass<target:
            mass += weights[pos]
            inds.append(pos)
            pos += 1
        if mass+1e-15<target:
            return None
        banks.append((inds,mass))
    return banks

gb_tests=0
for _ in range(500):
    n=256
    for attempt in range(1000):
        w=[rng.random() for _ in range(n)]
        s=sum(w); w=[x/s for x in w]
        if max(w)<=zeta:
            break
    else:
        raise RuntimeError('failed to generate capped vector')
    banks=greedy_banks(w,1/16,12)
    assert banks is not None
    assert all(m>=1/16-1e-14 for _,m in banks)
    assert all(m<1/16+zeta+1e-14 for _,m in banks)
    gb_tests+=1

print(f'SEED={SEED}')
print(f'exact_E2_identity_tests={count} PASS')
print(f'zeta={zeta:.15f}')
print(f'one_over_32={1/32:.15f}')
print(f'eleven_bank_consumption_upper={11*(1/16+zeta):.15f}')
print(f'fifteen_over_16={15/16:.15f}')
print(f'greedy_twelve_bank_tests={gb_tests} PASS')
print(f'partner_scale_sigma_over_h={sigma_h:.15f}')
print(f'E2_floor_over_h4={e2_h4:.12f}')
print(f'nonzero_2x2_minor_count_floor={minor_count}')
print(f'grid_or_hub_block_norm_over_h={grid_norm_h:.12f}')
print(f'grid_or_hub_nonzero_entry_count_floor={grid_entries}')
print(f'full_row_bank_norm_over_h={row_norm_h:.12f}')
print(f'full_row_bank_nonzero_entry_count_floor={row_entries}')
print('STATUS=PASS')
