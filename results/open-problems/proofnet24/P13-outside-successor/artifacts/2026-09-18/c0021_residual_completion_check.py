from fractions import Fraction
from functools import lru_cache

PLUS, MINUS, U = '+', '-', 'u'

def norm(children):
    p=sum(c==PLUS for c in children); m=sum(c==MINUS for c in children)
    if p>=2: return PLUS
    if m>=2: return MINUS
    return tuple(sorted(children,key=repr))

@lru_cache(None)
def full(k):
    return U if k==0 else norm((full(k-1),)*3)

@lru_cache(None)
def queries(t):
    if t==U: return ((PLUS,MINUS),)
    if t in (PLUS,MINUS): return ()
    out=set()
    for i,c in enumerate(t):
        if i and t[i]==t[i-1]: continue
        for cp,cm in queries(c):
            out.add((norm(t[:i]+(cp,)+t[i+1:]),norm(t[:i]+(cm,)+t[i+1:])))
    return tuple(sorted(out,key=repr))

@lru_cache(None)
def V(t):
    if t in (PLUS,MINUS): return Fraction(0)
    return min(Fraction(1)+(V(a)+V(b))/2 for a,b in queries(t))

def root_norm(st): return tuple(sorted(st,key=repr))
def root_done(st): return sum(c==PLUS for c in st)>=2 or sum(c==MINUS for c in st)>=2

@lru_cache(None)
def root_moves(st):
    out=set()
    for i,c in enumerate(st):
        if c in (PLUS,MINUS): continue
        if i and st[i]==st[i-1]: continue
        for cp,cm in queries(c):
            a=root_norm(st[:i]+(cp,)+st[i+1:])
            b=root_norm(st[:i]+(cm,)+st[i+1:])
            out.add((a,b))
    return tuple(sorted(out,key=repr))

@lru_cache(None)
def W(st):
    if root_done(st): return Fraction(0)
    return min(Fraction(1)+(W(a)+W(b))/2 for a,b in root_moves(st))

@lru_cache(None)
def residual_range(st):
    if root_done(st):
        r=sum((V(c) for c in st if c not in (PLUS,MINUS)),Fraction(0))
        return r,r
    target=W(st)
    candidates=[]
    for a,b in root_moves(st):
        if Fraction(1)+(W(a)+W(b))/2==target:
            amin,amax=residual_range(a); bmin,bmax=residual_range(b)
            candidates.append(((amin+bmin)/2,(amax+bmax)/2))
    return min(x for x,y in candidates), max(y for x,y in candidates)

print('C0021 residual-completion exact self-check')
for h in range(0,3):
    init=root_norm((full(h),)*3)
    cost=W(init)
    assert cost==V(full(h+1))
    rmin,rmax=residual_range(init)
    Dh=V(full(h))
    lbmin=3*Dh-rmax
    lbmax=3*Dh-rmin
    print(f'h={h}: D_h={Dh}; D_(h+1)={cost}; residual among cost-optimal policies=[{rmin},{rmax}]')
    print(f'      residual/D_h range=[{rmin/Dh},{rmax/Dh}]; accounting lower-bound range=[{lbmin},{lbmax}]')
print('ALL_EXACT_CHECKS_PASS')
