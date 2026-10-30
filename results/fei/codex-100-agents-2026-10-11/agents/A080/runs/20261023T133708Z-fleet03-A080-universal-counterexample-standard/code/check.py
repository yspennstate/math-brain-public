"""Frozen <=4-bit author certificate; exact rational prime-log arithmetic only."""
import argparse
import functools
import itertools
import json
import math
import time
from fractions import Fraction as Q
from pathlib import Path

START = time.monotonic()
ROOT = Path(__file__).resolve().parents[1]
COUNT = 0
MAX_BITS = 0

def check(ok, message):
    global COUNT
    COUNT += 1
    if not ok:
        raise AssertionError(message)
    if time.monotonic() - START > 55:
        raise RuntimeError('Frozen 55-second cap reached')

def form(items=()):
    d = {}
    for p, c in items:
        d[p] = d.get(p, Q(0)) + c
    return tuple(sorted((p, c) for p, c in d.items() if c))

def add(*args):
    return form(itertools.chain.from_iterable(args))

def scale(a, c):
    return form((p, x*c) for p, x in a)

def sub(a, b):
    return add(a, scale(b, -1))

def const(c):
    return form(((2, Q(c)),))

@functools.lru_cache(None)
def sign(a):
    global MAX_BITS
    if not a:
        return 0
    den = math.lcm(*(c.denominator for _, c in a))
    positive = negative = 1
    for p, c in a:
        e = c.numerator * (den // c.denominator)
        if e > 0:
            positive *= p**e
        else:
            negative *= p**(-e)
    MAX_BITS = max(MAX_BITS, positive.bit_length(), negative.bit_length())
    return (positive > negative) - (positive < negative)

def maximum(*args):
    best = ()
    for a in args:
        if sign(sub(a, best)) > 0:
            best = a
    return best

def factors(x):
    p = 2
    while p*p <= x:
        e = 0
        while x % p == 0:
            x //= p
            e += 1
        if e:
            yield p, e
        p += 1
    if x > 1:
        yield x, 1

def dim(f):
    return len(f).bit_length()-1

def restrict(f, i, b):
    return tuple(f[x] for x in range(len(f)) if (x >> i) & 1 == b)

@functools.lru_cache(None)
def data(f):
    n, N = dim(f), len(f)
    w = list(f)
    h = 1
    while h < N:
        for s in range(0, N, 2*h):
            for j in range(s, s+h):
                a, b = w[j], w[j+h]
                w[j], w[j+h] = a+b, a-b
        h *= 2
    check(sum(x*x for x in w) == N*N, 'Parseval')
    entropy = const(2*n)
    for x in w:
        if x:
            entropy = add(entropy, form((p, -2*Q(x*x, N*N)*e) for p,e in factors(abs(x))))
    influence = sum((Q(sum(f[x] != f[x ^ (1 << i)] for x in range(N)), N) for i in range(n)), Q(0))
    check(influence == sum((Q(x*x, N*N)*s.bit_count() for s,x in enumerate(w)), Q(0)), 'edge/Walsh influence')
    return entropy, influence

@functools.lru_cache(None)
def hull(f, K):
    H, I = data(f)
    choices = [(), sub(H, const(K*I))]
    for i in range(dim(f)):
        choices.append(scale(add(hull(restrict(f,i,0),K), hull(restrict(f,i,1),K)), Q(1,2)))
    return maximum(*choices)

@functools.lru_cache(None)
def policy(f, K):
    """Terminal truth table and reach; every terminal signed deficit >=0."""
    H, I = data(f)
    d, r = sub(H, const(K*I)), hull(f,K)
    if sign(d) >= 0 and d == r:
        return ((Q(1), f),)
    for i in range(dim(f)):
        a, b = restrict(f,i,0), restrict(f,i,1)
        if scale(add(hull(a,K), hull(b,K)), Q(1,2)) == r:
            return tuple((p/2, g) for child in (a,b) for p,g in policy(child,K))
    raise AssertionError('No attaining policy query')

def policy_tree(f, K):
    H,I=data(f)
    d,r=sub(H,const(K*I)),hull(f,K)
    if sign(d)>=0 and d==r:
        return {'stop':True}
    for i in range(dim(f)):
        children=[restrict(f,i,b) for b in (0,1)]
        if scale(add(*(hull(g,K) for g in children)),Q(1,2))==r:
            return {'query':i,'children':[policy_tree(g,K) for g in children]}
    raise AssertionError('No tree certificate')

def product(f,g):
    return tuple(x*y for y in g for x in f)

def compose(B,f,g):
    return tuple(B[(x == 1) + 2*(y == 1)] for y in g for x in f)

def pivot(B, core, other):
    return Q(sum(B[(z == 1)*2] != B[1+(z == 1)*2] for z in other),len(other)) if core == 0 else Q(sum(B[z == 1] != B[2+(z == 1)] for z in other),len(other))

def serial(a):
    return [[p,str(c)] for p,c in a]

def main(pilot):
    functions = list(itertools.product((-1,1), repeat=4))
    rates = tuple(map(Q, ('0','1/2','1','3/2','2','4')))
    pairs = list(itertools.product(functions, repeat=2))
    if pilot:
        pairs, rates = pairs[:4], (Q(1),)
    tensor_rows = []
    policy_rows = []
    for f in functions:
        for K in rates:
            leaves = policy(f,K)
            check(sum((p for p,_ in leaves),Q(0)) == 1, 'policy total reach')
            value = ()
            for reach, leaf in leaves:
                H,I = data(leaf)
                d = sub(H,const(K*I))
                check(sign(d)>=0, 'completed leaf signed deficit')
                value = add(value,scale(d,reach))
            check(value == hull(f,K), 'policy attains hull')
            policy_rows.append({'f':list(f),'K':str(K),'value':serial(value),'tree':policy_tree(f,K),'leaves':[{'reach':str(p),'f':list(g)} for p,g in leaves]})
    for f,g in pairs:
        F = product(f,g)
        H,I = data(F)
        check(H == add(data(f)[0],data(g)[0]), 'product entropy')
        check(I == data(f)[1]+data(g)[1], 'product physical influence')
        for K in rates:
            r = hull(F,K)
            check(r == add(hull(f,K),hull(g,K)), 'EXACT tensorization')
            joint = ()
            for p,a in policy(f,K):
                for q,b in policy(g,K):
                    Ha,Ia = data(product(a,b))
                    d = sub(Ha,const(K*Ia))
                    check(sign(d)>=0,'joint policy terminal sign')
                    joint = add(joint,scale(d,p*q))
            check(joint==r,'literal joint policy lower witness')
            tensor_rows.append({'f':list(f),'g':list(g),'K':str(K),'hull':serial(r)})
        for K,L in zip(rates,rates[1:]):
            delta = sub(hull(F,K), hull(F,L))
            check(sign(delta)>=0,'rate monotonicity')
            check(sign(sub(const((L-K)*I),delta))>=0,'rate Lipschitz')
    point = (-1,1,1,1)
    bank_cases = list(itertools.product(functions,functions))
    if pilot:
        bank_cases = bank_cases[:4]
    bank_rows = []
    for B,f in bank_cases:
        g = point
        F = compose(B,f,g)
        H,I = data(F)
        q0,q1 = pivot(B,0,g),pivot(B,1,f)
        check(I == q0*data(f)[1]+q1*data(g)[1],'composition physical influence')
        C = sub(H,add(scale(data(f)[0],q0),scale(data(g)[0],q1)))
        for K in map(Q,('0','1','2','4')):
            A = add(C,const(6*I),scale(hull(f,K),q0),scale(hull(g,K),q1))
            D = add(scale(sub(data(f)[0],hull(f,K)),q0),scale(sub(data(g)[0],hull(g,K)),q1))
            check(A == sub(add(H,const(6*I)),D),'bank exact rewriting')
            check(sign(sub(A,add(H,const((6-K)*I))))>=0,'bank lower bound')
            check(sign(sub(add(H,const(6*I)),A))>=0,'bank upper bound')
            check(sign(A)>=0,'source rational-six bank nonnegative')
            bank_rows.append({'outer':list(B),'first':list(f),'K':str(K),'H':serial(H),'I':str(I),'A':serial(A)})
    for K in rates:
        check(hull(point,K)==const(max(Q(0),2-K)),'point exact hull')
        coarse = add(const(6),hull(point,K))
        fine = const(8)
        if K<=2:
            check(coarse==const(8-K) and sub(fine,coarse)==const(K),'sharp bank interval')
    dual_rows=[{'f':list(f),'K':str(K),'value':serial(hull(f,K))} for n in range(3) for f in itertools.product((-1,1),repeat=2**n) for K in rates]
    elapsed = time.monotonic()-START
    summary = {'status':'PASS','pilot':pilot,'tensor_rows':len(tensor_rows),'bank_rows':len(bank_rows),'completed_core_policies':len(policy_rows),'exact_predicates':COUNT,'hull_cached_states':hull.cache_info().currsize,'truth_tables_cached':data.cache_info().currsize,'max_integer_comparison_bits':MAX_BITS,'elapsed_seconds':elapsed,'arithmetic':'Fraction and integer-power comparison; no floating mathematical verdict','independent_review':'PENDING'}
    tag = 'pilot' if pilot else 'main'
    (ROOT/'out'/f'{tag}_certificates.json').write_text(json.dumps({'dual':dual_rows,'policies':policy_rows,'tensor':tensor_rows,'bank':bank_rows},indent=2)+'\n',encoding='utf-8')
    (ROOT/'out'/f'{tag}_summary.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(summary),flush=True)

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--pilot',action='store_true')
    main(parser.parse_args().pilot)
