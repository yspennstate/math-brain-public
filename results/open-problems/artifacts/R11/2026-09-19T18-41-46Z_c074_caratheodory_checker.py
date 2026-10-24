from fractions import Fraction as F
from itertools import combinations
from math import comb

assertions = 0

def check(cond, msg=''):
    global assertions
    assertions += 1
    if not cond:
        raise AssertionError(msg)

def H(n):
    return sum((F(1,k) for k in range(1,n+1)), F(0,1))

def unordered_splits(V):
    V = tuple(sorted(V))
    a0 = V[0]
    out=[]
    for r in range(1,len(V)):
        for A in combinations(V,r):
            A=set(A)
            if a0 not in A:
                continue
            B=set(V)-A
            if B:
                out.append((tuple(sorted(A)),tuple(sorted(B))))
    return out

def D(K):
    return (3**K - 2**(K+1) + 1)//2

# Coordinate-count identity.
for K in range(2,11):
    explicit = 0
    for m in range(2,K+1):
        explicit += comb(K,m)*(2**(m-1)-1)
    check(explicit == D(K), (K, explicit, D(K)))

# One total order realizes exactly k-1 nontrivial unordered threshold splits.
for k in range(2,13):
    order=tuple(range(k))
    splits=set()
    for r in range(1,k):
        A=frozenset(order[:r]); B=frozenset(order[r:])
        canon=tuple(sorted((tuple(sorted(A)),tuple(sorted(B)))))
        splits.add(canon)
    check(len(splits)==k-1, (k,len(splits)))

# For every bounded support size L<=50 there is a fixed k violating coverage.
for L in range(1,51):
    found=False
    for k in range(2,30):
        if 2**(k-1)-1 > L*(k-1):
            found=True
            break
    check(found, L)


def powperm(x,p,d):
    return pow(x,d,p)

def v_translation(t, A, B, p=5, d=3):
    # Per-translation contribution v_t, so uniform full-orbit rate is (1/p) sum_t v_t.
    total=F(0,1)
    A=tuple(A); B=tuple(B)
    vals={ell:powperm((t+ell)%p,p,d) for ell in set(A)|set(B)}
    for u in range(1,p):
        ind1 = all(vals[a] < u for a in A) and all(vals[b] >= u for b in B)
        ind2 = all(vals[b] < u for b in B) and all(vals[a] >= u for a in A)
        if ind1 or ind2:
            total += F(p, 2*u*(p-u))
    return total

def all_coords(K):
    coords=[]
    base=range(K)
    for m in range(2,K+1):
        for V in combinations(base,m):
            coords.extend(unordered_splits(V))
    return coords

p=5; d=3; K=3
coords=all_coords(K)
check(len(coords)==D(K), len(coords))
T=(0,1,3,4)
lams=(F(4,15),F(1,3),F(4,15),F(2,15))
check(sum(lams,F(0,1))==1)
for lam in lams:
    check(lam>0)

# x^3 is a permutation mod 5 and every active translation is injective on four labels.
vals=[powperm(x,p,d) for x in range(p)]
check(len(set(vals))==p)
for t in T:
    out=[powperm((t+ell)%p,p,d) for ell in range(4)]
    check(len(set(out))==4, (t,out))

# Exact Caratheodory compression on every split coordinate through K=3.
expected_pair=F(1,1)
expected_triple=F(1,2)
for A,B in coords:
    full=sum((v_translation(t,A,B,p,d) for t in range(p)),F(0,1))/p
    comp=sum((lam*v_translation(t,A,B,p,d) for t,lam in zip(T,lams)),F(0,1))
    check(full==comp, (A,B,full,comp))
    if len(A)+len(B)==2:
        check(full==expected_pair,(A,B,full))
    elif len(A)+len(B)==3:
        check(full==expected_triple,(A,B,full))

# Proposal-rate normalization for compressed model.
proposal=sum((lam*sum((F(p,2*u*(p-u)) for u in range(1,p)),F(0,1)) for lam in lams),F(0,1))
check(proposal==H(p-1),(proposal,H(p-1)))

# Full N=4 root witness.
N=4
singles=[]
for a in range(N):
    A=(a,); B=tuple(x for x in range(N) if x!=a)
    q=sum((lam*v_translation(t,A,B,p,d) for t,lam in zip(T,lams)),F(0,1))
    singles.append(q)

balanced=[]
# canonical representatives: A contains 0, |A|=2
for b in range(1,N):
    A=(0,b); B=tuple(x for x in range(N) if x not in A)
    q=sum((lam*v_translation(t,A,B,p,d) for t,lam in zip(T,lams)),F(0,1))
    balanced.append(q)

exp_s=[F(7,18),F(13,36),F(5,18),F(5,24)]
exp_b=[F(2,9),F(5,36),F(1,9)]
check(singles==exp_s,(singles,exp_s))
check(balanced==exp_b,(balanced,exp_b))
# Source CTCS rates at N=4: B(1,3)=1/3, B(2,2)=1/6.
for q in singles:
    check(q != F(1,3))
for q in balanced:
    check(q != F(1,6))
check(len(set(singles))>1)
check(len(set(balanced))>1)

# Frozen-equivalence ratio invariant differs from source (source all ratios 1 in each size class).
check(max(singles)/min(singles) != 1)
check(max(balanced)/min(balanced) != 1)

print('C074_CARATHEODORY_SPARSITY_EXACT_CHECK')
print(f'assertions={assertions}')
print('params=N4_p5_d3_K3')
print('support=',T)
print('weights=',','.join(str(x) for x in lams))
print('compressed_K3_matches_full_orbit=YES')
print('proposal_rate=',proposal)
print('source_proposal_rate_H4=',H(4))
print('root_1v3=',','.join(str(x) for x in singles))
print('root_2v2=',','.join(str(x) for x in balanced))
print('D3=',D(3))
print('ALL_EXACT_CHECKS_PASS')
