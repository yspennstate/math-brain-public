"""Standalone exact actual-reference checker, v1. Run with python -X utf8 -B."""
import argparse
import functools
import hashlib
import itertools
import json
from fractions import Fraction as F
from pathlib import Path
import time

ASSERTIONS = 0
TRANSACTIONS = 0
ZERO_ROWS = 0

def check(test, label):
    global ASSERTIONS
    ASSERTIONS += 1
    if not test:
        raise AssertionError(label)

def logtwo(x):
    x = F(x)
    check(x > 0, 'positive log argument')
    a, b = x.numerator, x.denominator
    check(a & (a-1) == 0 and b & (b-1) == 0, 'exact power-of-two ratio')
    return a.bit_length() - b.bit_length()

def kl(p, Q):
    return sum((a * logtwo(a/b) for a, b in zip(p, Q) if a), F(0))

def entropy(p):
    return -sum((a * logtwo(a) for a in p if a), F(0))

def rank(rows):
    basis = {}
    for row in rows:
        while row:
            j = row.bit_length()-1
            if j in basis:
                row ^= basis[j]
            else:
                basis[j] = row
                break
    return len(basis)

def insert(t, i, bit):
    low = (1 << i)-1
    return (t & low) | ((t & ~low) << 1) | (bit << i)

def restrict(tab, i, bit):
    return tuple(tab[insert(t, i, bit)] for t in range(len(tab)//2))

@functools.lru_cache(None)
def info(tab):
    n = len(tab).bit_length()-1
    N = len(tab)
    walsh = list(tab)
    h = 1
    while h < N:
        for k in range(0, N, 2*h):
            for j in range(k, k+h):
                a,b = walsh[j],walsh[j+h]
                walsh[j],walsh[j+h] = a+b,a-b
        h *= 2
    p = tuple(F(a*a, N*N) for a in walsh)
    d = tuple(sum((p[t] for t in range(N) if t >> i & 1), F(0)) for i in range(n))
    Q = tuple(__import__('math').prod(d[i] if t >> i & 1 else 1-d[i] for i in range(n)) for t in range(N))
    bits = tuple((1-a)//2 for a in tab)
    ell = [bits[0] ^ bits[1 << i] for i in range(n)]
    rows = [sum((bits[0] ^ bits[1 << i] ^ bits[1 << j] ^ bits[(1 << i) | (1 << j)]) << j
                for j in range(n) if j != i) for i in range(n)]
    r = rank(rows)
    m = sum(bool(a) for a in rows)
    check(r % 2 == 0, 'alternating even rank')
    check(sum(p) == sum(Q) == 1, 'normalized law and actual product')
    check(all(a == F(1,1 << r) for a in p if a), 'flat actual quadratic spectrum')
    check(entropy(p) == r and kl(p,Q) == m-r, 'rank entropy and TC')
    for i in range(n):
        edge = F(sum(tab[t] != tab[t ^ (1 << i)] for t in range(N)),N)
        check(edge == d[i] == (F(1,2) if rows[i] else ell[i]), 'physical/spectral influence')
    return {'p':p,'Q':Q,'d':d,'rows':rows,'r':r,'m':m,'K':F(m-r),'I':sum(d,F(0))}

@functools.lru_cache(None)
def transaction(tab, i):
    global TRANSACTIONS, ZERO_ROWS
    TRANSACTIONS += 1
    old = info(tab)
    tabs = [restrict(tab,i,b) for b in (0,1)]
    children = [info(t) for t in tabs]
    q = tuple(old['p'][insert(t,i,0)] + old['p'][insert(t,i,1)] for t in range(len(tab)//2))
    Qbar = tuple(old['Q'][insert(t,i,0)] + old['Q'][insert(t,i,1)] for t in range(len(tab)//2))
    check(all(q[t] == (children[0]['p'][t]+children[1]['p'][t])/2 for t in range(len(q))), 'physical mean equals erasure')
    predicted_K = []
    pi = []
    for child in children:
        unnormalized = tuple(Qbar[t] * (child['p'][t]/(2*q[t]) if q[t] else F(1,2)) for t in range(len(q)))
        ZERO_ROWS += sum(q[t] == 0 and Qbar[t] > 0 for t in range(len(q)))
        mass = sum(unnormalized,F(0))
        check(mass == F(1,2), 'actual reference outcome fair including zero-source rows')
        ref = tuple(a/mass for a in unnormalized)
        check(sum(ref) == 1, 'actual child normalization')
        predicted_K.append(kl(child['p'],ref))
        pi.append(mass)
    E = old['K'] - kl(q,Qbar)
    O = kl((F(1,2),F(1,2)),pi)
    sigma = sum((child['K']-kb for child,kb in zip(children,predicted_K)),F(0))/2
    check(old['K'] == E+O+sum(predicted_K,F(0))/2, 'complete reference chain rule')
    check(O == 0, 'no outcome allowance omitted')
    if old['rows'][i]:
        s = (old['r']-children[0]['r'])//2
        k = old['m']-1-children[0]['m']
        check(s in (0,1) and k >= 0, 'rank deletion alternatives')
        check(E == 1-s and sigma == s-k, 'actual reset formula')
    else:
        check(E == sigma == 0, 'isolated deterministic coordinate')
    check(children[0]['r'] == children[1]['r'] and children[0]['m'] == children[1]['m'], 'both physical branches retained')
    return tuple(tabs), E, O, sigma

@functools.lru_cache(None)
def gross(tab):
    n = len(tab).bit_length()-1
    values = [F(0)]
    for i in range(n):
        children,E,O,sigma = transaction(tab,i)
        values.append(max(F(0),sigma) + sum((gross(t) for t in children),F(0))/2)
    ans = max(values)
    r = info(tab)['r']
    check(ans <= max(0,r//2-1), 'all adaptive stopping policies gross-rank bound')
    return ans

@functools.lru_cache(None)
def pending(tab):
    """Extra reserve if E may remain available; used only as an additional diagnostic."""
    n = len(tab).bit_length()-1
    values = [F(0)]
    for i in range(n):
        children,E,O,sigma = transaction(tab,i)
        values.append(sigma-E+sum((pending(t) for t in children),F(0))/2)
    ans = max(values)
    check(ans <= gross(tab), 'available erasure refunds cannot increase reserve')
    return ans

def make(n, edges, linear, c):
    return tuple(1-2*((c+(linear & x).bit_count()+sum(((x>>i)&1)*((x>>j)&1) for i,j in edges))%2) for x in range(1 << n))

def exhaustive(maxn):
    count = 0
    results = []
    for n in range(maxn+1):
        pairs = list(itertools.combinations(range(n),2))
        for mask in range(1 << len(pairs)):
            edges = [e for j,e in enumerate(pairs) if mask >> j & 1]
            for ell in range(1 << n):
                for c in (0,1):
                    tab = make(n,edges,ell,c)
                    z = info(tab)
                    g,b = gross(tab),pending(tab)
                    check(z['K']+F(z['r'],2) <= 2*z['I'], 'single original 2I source and owner admission')
                    check(z['m']+F(z['r'],2) <= 3*z['I'], 'full terminal accounting capacity')
                    if z['r']:
                        check(F(z['r'],2)-g-F(1,4) >= F(3,4), 'old quarter and residual at every cut')
                    count += 1
        results.append({'n':n,'cumulative_cases':count})
    return count,results

def sharp(k):
    m = k+2
    n = 2*k+2
    edges = [(0,j) for j in range(1,m)] + [(m+j-2,j) for j in range(2,m)]
    root = make(n,edges,0,0)
    z = info(root)
    check(z['r'] == n and z['K'] == 0 and z['I'] == k+1, 'sharp bent product root')
    states = [(root,F(0))]
    for depth in range(k):
        nxt = []
        for tab,bill in states:
            # Controllers occupy the final consecutive coordinates. Delete first remaining.
            children,E,O,sigma = transaction(tab,m)
            check((E,O,sigma) == (0,0,1), 'sharp controller query has no refund')
            nxt.extend((t,bill+sigma) for t in children)
        states = nxt
    for tab,bill in states:
        end = info(tab)
        check(end['r'] == 2 and end['m'] == m and end['K'] == bill == k, 'sharp full terminal cost on every outcome')
        check(F(z['r'],2)-bill == 1, 'rank reserve sharp with full history')
    return {'k':k,'n':n,'terminal_branches':len(states),'necessary_extra_units':k,'original_I':k+1,'terminal_H':2,'terminal_K':k}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pilot',action='store_true')
    parser.add_argument('--out',required=True)
    args = parser.parse_args()
    started = time.monotonic()
    count,domain = exhaustive(3 if args.pilot else 4)
    sharp_results = [] if args.pilot else [sharp(k) for k in range(1,5)]
    result = {'status':'PASS','mode':'pilot' if args.pilot else 'main','cases':count,'domain':domain,
              'transactions_including_sharp':TRANSACTIONS,'assertions':ASSERTIONS,'positive_reference_only_rows_retained':ZERO_ROWS,
              'sharp':sharp_results,'elapsed_seconds':round(time.monotonic()-started,3),
              'arithmetic':'exact integers, Fraction, exact dyadic logarithms; no floating point in checks',
              'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(args.out).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))

if __name__ == '__main__':
    main()
