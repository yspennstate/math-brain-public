from fractions import Fraction
from functools import lru_cache
from collections import deque

PLUS, MINUS, U = '+', '-', 'u'

def norm(children):
    p = sum(c == PLUS for c in children)
    m = sum(c == MINUS for c in children)
    if p >= 2: return PLUS
    if m >= 2: return MINUS
    return tuple(sorted(children, key=repr))

@lru_cache(None)
def full(k):
    return U if k == 0 else norm((full(k-1),)*3)

@lru_cache(None)
def queries(t):
    if t == U: return ((PLUS, MINUS),)
    if t in (PLUS, MINUS): return ()
    out = set()
    for i,c in enumerate(t):
        if i and t[i] == t[i-1]:
            continue
        for cp,cm in queries(c):
            out.add((norm(t[:i]+(cp,)+t[i+1:]),
                     norm(t[:i]+(cm,)+t[i+1:])))
    return tuple(sorted(out, key=repr))

@lru_cache(None)
def V(t):
    if t in (PLUS, MINUS): return Fraction(0)
    return min(Fraction(1) + (V(a)+V(b))/2 for a,b in queries(t))

@lru_cache(None)
def q(t):
    if t == PLUS: return Fraction(1)
    if t == MINUS: return Fraction(0)
    if t == U: return Fraction(1,2)
    a,b,c = (q(x) for x in t)
    return a*b + a*c + b*c - 2*a*b*c

def median_leaf_path(t):
    path=[]
    while t != U:
        assert t not in (PLUS,MINUS)
        qs=[q(c) for c in t]
        med=sorted(qs)[1]
        cand=[i for i,c in enumerate(t) if c not in (PLUS,MINUS) and qs[i]==med]
        assert cand, (t,qs)
        i=cand[0]
        path.append(i)
        t=t[i]
    return tuple(path)

def query_at_path(t,path):
    if not path:
        assert t == U
        return PLUS, MINUS
    i=path[0]
    cp,cm=query_at_path(t[i],path[1:])
    return (norm(t[:i]+(cp,)+t[i+1:]),
            norm(t[:i]+(cm,)+t[i+1:]))

def qvalue(t,path):
    a,b=query_at_path(t,path)
    return Fraction(1)+(V(a)+V(b))/2

def all_leaf_paths(t,prefix=()):
    if t == U:
        yield prefix
    elif t not in (PLUS,MINUS):
        for i,c in enumerate(t):
            if c not in (PLUS,MINUS):
                yield from all_leaf_paths(c,prefix+(i,))

# Follow the recursive median-posterior rule for three + outcomes from the full depth-3 tree.
t=full(3)
for bit in '+++':
    p=median_leaf_path(t)
    a,b=query_at_path(t,p)
    t=a if bit=='+' else b

post=tuple(q(c) for c in t)
assert post == (Fraction(3,4), Fraction(5,8), Fraction(1,2)), post
median_path=median_leaf_path(t)
assert median_path == (1,1,0), median_path
median_Q=qvalue(t,median_path)

vals=[(qvalue(t,p),p) for p in all_leaf_paths(t)]
opt_Q=min(v for v,p in vals)
opt_paths=sorted(p for v,p in vals if v==opt_Q)
assert opt_paths == [(1,0,1),(1,0,2)], opt_paths
assert median_Q == Fraction(3031947,262144), median_Q
assert opt_Q == Fraction(3028131,262144), opt_Q
assert median_Q-opt_Q == Fraction(477,32768)
assert V(t)==opt_Q

D1=V(full(1)); D2=V(full(2)); D3=V(full(3))
assert D1==Fraction(5,2)
assert D2==Fraction(393,64)
assert D3==Fraction(15796051,1048576)

print('C0021 exact self-check')
print('D1 =',D1)
print('D2 =',D2)
print('D3 =',D3)
print('witness transcript = +++ under recursive median-posterior rule')
print('root-child posteriors =', ', '.join(str(x) for x in post))
print('median-rule next leaf path =', median_path)
print('median-rule Bellman Q =',median_Q)
print('optimal next leaf paths =', opt_paths)
print('optimal Bellman Q =',opt_Q)
print('strict gap =',median_Q-opt_Q)
print('ALL_EXACT_CHECKS_PASS')
