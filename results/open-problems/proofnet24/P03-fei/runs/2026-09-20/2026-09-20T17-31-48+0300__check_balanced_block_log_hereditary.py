#!/usr/bin/env python3
import math, json, random, hashlib, sys

RHO = 2.0 / math.log(2.0)
TOL = 2e-10

def fwht(values):
    a = [float(x) for x in values]
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    inv = 1.0/n
    return [x*inv for x in a]

def entropy(values):
    H = 0.0
    for c in fwht(values):
        p = c*c
        if p > 0.0:
            H -= p*math.log(p, 2)
    return H

def influences(values):
    N = len(values); n = N.bit_length()-1
    out = []
    for i in range(n):
        diff = 0
        bit = 1 << i
        for x in range(N):
            if values[x] != values[x ^ bit]:
                diff += 1
        out.append(diff/N)
    return out

def restrict_bit(values, i, b):
    N = len(values); n = N.bit_length()-1
    out = [0]*(1 << (n-1))
    lowmask = (1 << i)-1
    for y in range(len(out)):
        low = y & lowmask
        high = y >> i
        x = low | (b << i) | (high << (i+1))
        out[y] = values[x]
    return out

def Bcoord(values, i):
    c = fwht(values)
    p = [x*x for x in c]
    N = len(values); bit = 1 << i
    ans = 0.0
    for s in range(N):
        if s & bit:
            continue
        a, b = p[s], p[s|bit]
        w = a+b
        if a > 0.0 and b > 0.0:
            q = a/w
            ans += w*(-q*math.log(q,2) - (1-q)*math.log(1-q,2))
    return ans

def D_level(L):
    # valid for all Boolean functions on at most 2^L variables, L>=1
    if L <= 0:
        return 0.0
    return 2.0 + (L-1)*RHO

def K_level(L):
    # hereditary balanced-block compiler constant for at most 2^L variables
    if L <= 0:
        return 0.0
    return 2.0 + (L-2)*RHO + (RHO-1.0)*(2.0**(1-L))

def tree_R(values, L=None):
    n = len(values).bit_length()-1
    if n <= 1:
        return 0.0
    if n == 2:
        # Complete one coordinate, then the residual one-bit Boolean leaves have zero spectral entropy/allocation.
        return min(Bcoord(values,0), Bcoord(values,1))
    if L is None:
        L = math.ceil(math.log(n,2))
    if not (n <= 2**L and L >= 2):
        raise AssertionError((n,L))
    a = n//2
    A = list(range(a))
    Y = list(range(a,n))
    inf = influences(values)
    IA = sum(inf[i] for i in A)
    IY = sum(inf[i] for i in Y)
    D = D_level(L-1)
    K = K_level(L-1)
    bound_A_first = D*IA + (K+RHO)*IY
    bound_Y_first = (K+RHO)*IA + D*IY
    query = A if bound_A_first <= bound_Y_first else Y

    def query_prefix(cur, qidx):
        if not qidx:
            return tree_R(cur, L-1)
        i = qidx[0]
        root = Bcoord(cur, i)
        c0 = restrict_bit(cur, i, 0)
        c1 = restrict_bit(cur, i, 1)
        rest = [j-1 if j > i else j for j in qidx[1:]]
        return root + 0.5*(query_prefix(c0,rest) + query_prefix(c1,rest))
    return query_prefix(values, query)

def one_point(n):
    return [-1] + [1]*((1<<n)-1)

def majority_odd(n):
    assert n%2 == 1
    vals=[]
    for x in range(1<<n):
        wt=x.bit_count()
        vals.append(1 if wt <= n//2 else -1)
    return vals

def quadratic_bent(n):
    assert n%2 == 0
    vals=[]
    for x in range(1<<n):
        q=0
        for i in range(0,n,2):
            q ^= ((x>>i)&1) & ((x>>(i+1))&1)
        vals.append(-1 if q else 1)
    return vals

def check_case(values, agg):
    n=len(values).bit_length()-1
    I=sum(influences(values))
    H=entropy(values)
    if I <= TOL:
        assert H <= TOL
        return
    L=max(1, math.ceil(math.log(n,2)))
    D=D_level(L); K=K_level(L)
    R=tree_R(values,L)
    agg['cases'] += 1
    agg['max_direct_violation'] = max(agg['max_direct_violation'], H-D*I)
    agg['max_tree_violation'] = max(agg['max_tree_violation'], R-K*I)
    agg['max_R_minus_H'] = max(agg['max_R_minus_H'], R-H)
    agg['max_H_minus_2R'] = max(agg['max_H_minus_2R'], H-2*R)
    agg['max_direct_ratio'] = max(agg['max_direct_ratio'], H/I)
    agg['max_tree_ratio'] = max(agg['max_tree_ratio'], R/I)
    if H-D*I > TOL or R-K*I > TOL or R-H > TOL or H-2*R > TOL:
        raise AssertionError({'n':n,'I':I,'H':H,'R':R,'D':D,'K':K})

def main():
    # exact recurrence consistency
    recurrence=[]
    for L in range(1,12):
        if L==1:
            assert abs(D_level(L)-2.0) < 1e-14
            assert abs(K_level(L)-1.0) < 1e-14
        else:
            assert abs(D_level(L) - (D_level(L-1)+RHO)) < 1e-13
            assert abs(K_level(L) - 0.5*(D_level(L-1)+K_level(L-1)+RHO)) < 1e-13
        recurrence.append({'L':L,'D':D_level(L),'K':K_level(L)})

    exhaustive={'cases':0,'max_direct_violation':-1e100,'max_tree_violation':-1e100,
                'max_R_minus_H':-1e100,'max_H_minus_2R':-1e100,
                'max_direct_ratio':0.0,'max_tree_ratio':0.0}
    functions_total=0
    # all Boolean functions n=1..4, including global signs
    for n in range(1,5):
        N=1<<n
        for mask in range(1<<N):
            functions_total += 1
            vals=[-1 if ((mask>>x)&1) else 1 for x in range(N)]
            check_case(vals, exhaustive)

    rng=random.Random(20260920)
    random_agg={'cases':0,'max_direct_violation':-1e100,'max_tree_violation':-1e100,
                'max_R_minus_H':-1e100,'max_H_minus_2R':-1e100,
                'max_direct_ratio':0.0,'max_tree_ratio':0.0}
    random_by_n={}
    for n,samples in [(5,500),(6,350),(7,200),(8,100)]:
        local=0
        N=1<<n
        for _ in range(samples):
            vals=[1 if rng.getrandbits(1) else -1 for _ in range(N)]
            if all(v==vals[0] for v in vals):
                continue
            check_case(vals, random_agg); local += 1
        random_by_n[str(n)]=local

    named={'cases':0,'max_direct_violation':-1e100,'max_tree_violation':-1e100,
           'max_R_minus_H':-1e100,'max_H_minus_2R':-1e100,
           'max_direct_ratio':0.0,'max_tree_ratio':0.0}
    named_labels=[]
    for n in range(2,13):
        check_case(one_point(n),named); named_labels.append('one_point_%d'%n)
    for n in [3,5,7,9]:
        check_case(majority_odd(n),named); named_labels.append('majority_%d'%n)
    for n in [2,4,6,8,10]:
        check_case(quadratic_bent(n),named); named_labels.append('bent_quadratic_%d'%n)

    out={
        'status':'PASS',
        'rho_2_over_ln2':RHO,
        'theorem_constants': recurrence,
        'exhaustive': {'functions_seen':functions_total, **exhaustive},
        'random': {'samples_by_dimension':random_by_n, **random_agg},
        'named': {'labels':named_labels, **named},
        'notes': [
            'Exhaustive sweep includes all 65,812 Boolean truth tables in dimensions 1 through 4; constant functions are seen but omitted from ratio counters.',
            'tree_R constructs the balanced-block hereditary tree used in the proof, choosing between the two block-first orientations using the proved coefficient profiles.',
            'Checks R<=H<=2R validate the inherited full-tree allocation/recombination identity numerically on the constructed trees; they are not used as a proof of the new recursion.'
        ]
    }
    print(json.dumps(out, indent=2, sort_keys=True))

if __name__=='__main__':
    main()
