from functools import lru_cache
from itertools import product
from fractions import Fraction
from math import comb
from pathlib import Path
import json, time

t0 = time.perf_counter()

@lru_cache(None)
def matchings(n):
    if n == 0:
        return ((),)
    result = [tuple((a+1,b+1) for a,b in p) for p in matchings(n-1)]
    for j in range(1,n):
        for interior in matchings(j-1):
            for exterior in matchings(n-j-1):
                result.append(((0,j),) + tuple((a+1,b+1) for a,b in interior) + tuple((a+j+1,b+j+1) for a,b in exterior))
    return tuple(result)

def noncrossing(pairs):
    endpoints = [i for p in pairs for i in p]
    if len(set(endpoints)) != len(endpoints):
        return False
    return not any(a<c<b<d or c<a<d<b for a,b in pairs for c,d in pairs)

surgery_count = 0
cases = dict(together=0, both_unpaired=0, one_external=0, two_external=0)
for n in range(2,13):
    for pairs in matchings(n):
        assert noncrossing(pairs)
        count_by_k = None
        for i in range(n-1):
            j = i+1
            partners = dict([entry for a,b in pairs for entry in ((a,b),(b,a))])
            p,q = partners.get(i),partners.get(j)
            out = [ab for ab in pairs if i not in ab and j not in ab]
            if p == j:
                cases['together'] += 1
            elif p is None and q is None:
                cases['both_unpaired'] += 1
            elif p is None or q is None:
                cases['one_external'] += 1
            else:
                cases['two_external'] += 1
                out.append(tuple(sorted((p,q))))
            assert noncrossing(out), (n,pairs,i,out)
            assert (n-2)-2*len(out) <= n-2*len(pairs)
            surgery_count += 1
    for k in range(n+1):
        actual = sum(n-2*len(p) == k for p in matchings(n))
        expected = 0 if (n-k)%2 else comb(n,k)*comb(n-k,(n-k)//2)//((n-k)//2+1)
        assert actual == expected, (n,k,actual,expected)

def reduce_word(w):
    stack = []
    for x in w:
        if stack and stack[-1] == (x ^ 1):
            stack.pop()
        else:
            stack.append(x)
    return tuple(stack)

@lru_cache(None)
def norm(w):
    if not w:
        return 0
    best = 1+norm(w[1:])
    for j in range(1,len(w)):
        if w[j] == (w[0]^1):
            best = min(best,norm(w[1:j])+norm(w[j+1:]))
    return best

def inverse(w):
    return tuple(x^1 for x in reversed(w))

def deletion_oracle(w):
    best = len(w)
    for mask in range(1<<len(w)):
        kept = tuple(w[i] for i in range(len(w)) if mask & (1<<i))
        if not reduce_word(kept):
            best = min(best,len(w)-len(kept))
    return best

word_count = oracle_count = pair_count = 0
for n in range(9):
    for w in product(range(4), repeat=n):
        value = norm(w)
        assert value == norm(reduce_word(w)) == norm(inverse(w))
        assert (value == 0) == (reduce_word(w) == ())
        if n <= 6:
            assert value == deletion_oracle(w), w
            oracle_count += 1
        word_count += 1

short = [w for n in range(4) for w in product(range(4), repeat=n)]
for u in short:
    for w in short:
        assert norm(u+w) <= norm(u)+norm(w)
        assert norm(u+w+inverse(u)) == norm(w)
        pair_count += 1

bound_checks = []
for n in range(1,201):
    exact_union = sum((Fraction(comb(n,k)*comb(n-k,(n-k)//2), ((n-k)//2+1)*64**((n-k)//2)) for k in range(n//4+1) if (n-k)%2==0), Fraction(0))
    coarse_union = sum((Fraction(comb(n,k),16**((n-k)//2)) for k in range(n//4+1) if (n-k)%2==0), Fraction(0))
    assert exact_union <= coarse_union
    assert coarse_union**2 <= Fraction(1,2**n), n
    if n in (1,2,4,8,16,32,64,100,200):
        bound_checks.append({'n': n, 'catalan_union': float(exact_union), 'coarse_union': float(coarse_union), 'claimed_bound': 2**(-n/2)})

report = {'surgery_instances': surgery_count, 'surgery_cases': cases, 'matching_count_lengths': '2..12', 'words': word_count, 'independent_deletion_oracle_words': oracle_count, 'word_pairs': pair_count, 'exact_rational_probability_checks': 200, 'selected_bounds': bound_checks, 'seconds': time.perf_counter()-t0, 'all_passed': True}
Path(__file__).with_name('independent_checks.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
