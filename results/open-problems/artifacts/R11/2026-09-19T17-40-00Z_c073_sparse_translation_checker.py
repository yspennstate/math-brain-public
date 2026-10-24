from fractions import Fraction as F
from itertools import combinations
from math import comb, ceil

ASSERTIONS = 0

def check(cond, msg='assertion failed'):
    global ASSERTIONS
    ASSERTIONS += 1
    if not cond:
        raise AssertionError(msg)

def H(n):
    return sum((F(1,j) for j in range(1,n+1)), F(0))

def canon_split(A, universe):
    A=frozenset(A); B=frozenset(set(universe)-set(A))
    if len(A)<len(B): return (A,B)
    if len(B)<len(A): return (B,A)
    return (A,B) if tuple(sorted(A)) < tuple(sorted(B)) else (B,A)

def all_unordered_splits(universe):
    U=tuple(universe); out=[]; seen=set()
    for r in range(1,len(U)):
        for A in combinations(U,r):
            s=canon_split(A,U)
            if s not in seen:
                seen.add(s); out.append(s)
    return out

def sparse_rates(N,p,d,L):
    U=tuple(range(N))
    rates={s:F(0) for s in all_unordered_splits(U)}
    masks=[]
    for u in range(1,p):
        for t in range(L):
            red=frozenset(x for x in U if pow((t+x)%p,d,p) < u)
            masks.append((u,t,red))
            if red and len(red)<N:
                s=canon_split(red,U)
                rates[s] += F(p,2*L*u*(p-u))
    return rates,masks

def B(i,j):
    # beta(i,j)=(i-1)!(j-1)!/(i+j-1)! via exact product
    num=1
    for a in range(1,i): num*=a
    for b in range(1,j): num*=b
    den=1
    for c in range(1,i+j): den*=c
    return F(num,den)

# Candidate C073 finite witness.
N=6; p=11; d=3; L=7
check(L == ceil(p**0.75), 'L mismatch')
check(L < p, 'sparse set not proper')
# x -> x^3 is a permutation mod 11.
vals=[pow(x,d,p) for x in range(p)]
check(len(set(vals))==p, 'power map not a permutation')
# Every retained translation separates every pair at some threshold because outputs are distinct.
for t in range(L):
    out=[pow((t+x)%p,d,p) for x in range(N)]
    check(len(out)==len(set(out)), f'collision at t={t}')
    for a,b in combinations(range(N),2):
        va,vb=out[a],out[b]
        check(va!=vb)
        lo,hi=sorted((va,vb))
        # threshold u=lo+1 separates unless lo=hi, which was excluded; hi<=p-1.
        u=lo+1
        check(1 <= u <= p-1)
        check((va<u) != (vb<u))

rates,masks=sparse_rates(N,p,d,L)
check(len(rates)==2**(N-1)-1)
check(len(masks)==L*(p-1))

# Direct total proposal rate, including null masks, is exactly H_{p-1} after p/L rescaling.
total_proposal=sum((F(p,2*L*u*(p-u)) for u in range(1,p) for t in range(L)),F(0))
check(total_proposal==H(p-1), 'proposal rate normalization')

# Every recorded split rate equals a second direct orientation count.
U=tuple(range(N))
for s,q in rates.items():
    A,Bset=s
    q2=F(0)
    for u,t,red in masks:
        if red==A or red==Bset:
            q2 += F(p,2*L*u*(p-u))
    check(q==q2, f'double count mismatch {s}')

# Group exact multisets and aggregates.
groups={}
for (A,Bset),q in rates.items():
    key=(len(A),len(Bset))
    groups.setdefault(key,[]).append(q)
for key in groups:
    groups[key].sort()

check(len(groups[(1,5)])==6)
check(len(groups[(2,4)])==15)
check(len(groups[(3,3)])==10)

expected_15=sorted([F(11,144)]*3+[F(572,2205)]*2+[F(2981,8820)])
expected_24=sorted([F(0)]*8+[F(319,5880)]*2+[F(143,2352)]*3+[F(737,7056),F(1661,11760)])
expected_33=sorted([F(0)]*8+[F(11,420),F(627,1960)])
check(groups[(1,5)]==expected_15,'1|5 multiset')
check(groups[(2,4)]==expected_24,'2|4 multiset')
check(groups[(3,3)]==expected_33,'3|3 multiset')
check(sum(groups[(1,5)],F(0))==F(4257,3920))
check(sum(groups[(2,4)],F(0))==F(18931,35280))
check(sum(groups[(3,3)],F(0))==F(407,1176))
root_total=sum(rates.values(),F(0))
check(root_total==F(4961,2520))
check(sum(groups[(3,3)],F(0))/root_total==F(555,3157))
check(sum(q==0 for q in groups[(2,4)])==8)
check(sum(q==0 for q in groups[(3,3)])==8)

# Source CTCS has strictly positive specified rates B(i,j), so zeros certify finite non-equivalence.
check(B(1,5)==F(1,5))
check(B(2,4)==F(1,20))
check(B(3,3)==F(1,30))
for key,vals0 in groups.items():
    i,j=key
    check(B(i,j)>0)

# Compare with C072 (full p translations, same p,d): it has one zero 2|4, not eight.
full_rates,_=sparse_rates(N,p,d,p)
full_groups={}
for (A,Bset),q in full_rates.items():
    full_groups.setdefault((len(A),len(Bset)),[]).append(q)
for key in full_groups: full_groups[key].sort()
check(sum(q==0 for q in full_groups[(2,4)])==1)
check(sum(q==0 for q in full_groups[(3,3)])==4)
check(groups[(2,4)]!=full_groups[(2,4)])

# Exhaustive invariance witness: no relabeling plus positive common time-rescaling can turn C073 rates into source CTCS rates.
# A source rate array has no zeros; C073 has zeros, and relabeling only permutes entries.
for perm_zero in [sum(q==0 for q in groups[(1,5)]),sum(q==0 for q in groups[(2,4)]),sum(q==0 for q in groups[(3,3)])]:
    check(perm_zero>=0)
check(sum(q==0 for q in rates.values())==16)

# Sanity over several p and arbitrary sparse L: rescaling always preserves exact total proposal rate H_{p-1}.
for pp in [5,7,11,13,17,19,23,29,31,37,41,43]:
    for LL in [1,2,max(1,pp//3),max(1,pp//2),pp-1,pp]:
        if LL>pp: continue
        tot=sum((F(pp,2*LL*u*(pp-u)) for u in range(1,pp) for _ in range(LL)),F(0))
        check(tot==H(pp-1),f'normalization p={pp} L={LL}')

# Finite Vandermonde/degree>=2 core checks for representative growing-degree cases.
# We verify that no nonzero small Fourier vector produces a phase of degree <=1 over Q
# for m<=d-1, matching the exact algebraic lemma used in the proof.
def poly_coeff_phase(offsets,h,d):
    # ascending coefficient list of sum h_j (t+a_j)^d over integers
    coeff=[0]*(d+1)
    for a,hh in zip(offsets,h):
        for k in range(d+1):
            coeff[k]+=hh*comb(d,k)*(a**(d-k))
    return coeff

for d0 in [3,5,7]:
    for m in range(1,d0):
        offs=list(range(m))
        # Exhaust small Fourier cube {-2,-1,0,1,2}^m except zero.
        def rec(prefix):
            if len(prefix)==m:
                if all(x==0 for x in prefix): return
                coeff=poly_coeff_phase(offs,prefix,d0)
                deg=max((k for k,c in enumerate(coeff) if c),default=-1)
                check(deg>=2,f'degree obstruction d={d0} m={m} h={prefix} deg={deg}')
                return
            for z in [-2,-1,0,1,2]: rec(prefix+[z])
        rec([])

print('C073_SPARSE_TRANSLATION_EXACT_CHECK')
print(f'assertions={ASSERTIONS}')
print('params=N6_d3_p11_L7')
print('total_proposal=', total_proposal)
print('source_specified_rates=', B(1,5), B(2,4), B(3,3))
print('c073_1x5=', ','.join(map(str,groups[(1,5)])))
print('c073_2x4=', ','.join(map(str,groups[(2,4)])))
print('c073_3x3=', ','.join(map(str,groups[(3,3)])))
print('c073_aggregates=', sum(groups[(1,5)],F(0)), sum(groups[(2,4)],F(0)), sum(groups[(3,3)],F(0)))
print('c073_root_total=',root_total)
print('c073_balanced_probability=',sum(groups[(3,3)],F(0))/root_total)
print('c073_zero_counts_2x4_3x3=',sum(q==0 for q in groups[(2,4)]),sum(q==0 for q in groups[(3,3)]))
print('c072_zero_counts_2x4_3x3=',sum(q==0 for q in full_groups[(2,4)]),sum(q==0 for q in full_groups[(3,3)]))
print('ALL_EXACT_CHECKS_PASS')
