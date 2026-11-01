from itertools import product

# Variables 0,1,2,3. Literal sign +1 means x_i, -1 means not x_i.
F = [
    ((0,-1),(1,-1),(3,-1)),
    ((0,+1),(2,-1),(3,-1)),
    ((1,+1),(2,-1),(3,-1)),
    ((1,-1),(2,-1),(3,+1)),
]
n=4
sigma=(1,1,0,0)
y=1
leaves=(2,3)

def lit_true(v,s,a):
    return (a[v]==1) if s==1 else (a[v]==0)

def sat(a):
    return all(any(lit_true(v,s,a) for v,s in C) for C in F)

def flip(a, S):
    b=list(a)
    for v in S:
        b[v]^=1
    return tuple(b)

def critical(v,a):
    out=[]
    for j,C in enumerate(F):
        tr=[u for u,s in C if lit_true(u,s,a)]
        if tr==[v]:
            out.append(j)
    return out

SAT=[a for a in product((0,1),repeat=n) if sat(a)]
SATset=set(SAT)

def neigh(a):
    for v in range(n):
        b=flip(a,(v,))
        if b in SATset:
            yield b

# component of sigma
seen={sigma}; stack=[sigma]
while stack:
    a=stack.pop()
    for b in neigh(a):
        if b not in seen:
            seen.add(b); stack.append(b)

assert sat(sigma)
assert max(sum(a) for a in seen)==sum(sigma)==2
assert critical(y,sigma)==[]
for x in leaves:
    cx=critical(x,sigma)
    assert len(cx)==1
    C=F[cx[0]]
    assert any(v==y and s==-1 for v,s in C)
    assert sat(flip(sigma,(y,x)))
assert sat(flip(sigma,(y,)))
assert not sat(flip(sigma,(y,2,3)))

# Exact flip-set clause identity for every satisfying base assignment and every S.
def endpoint_clause_identity(a,S,C):
    S=set(S)
    T={v for v,s in C if lit_true(v,s,a)}
    FF={v for v,s in C if not lit_true(v,s,a)}
    lhs=any(lit_true(v,s,flip(a,S)) for v,s in C)
    rhs=(not T.issubset(S)) or bool(FF.intersection(S))
    return lhs==rhs

for a in SAT:
    for mask in range(1<<n):
        S=[v for v in range(n) if (mask>>v)&1]
        for C in F:
            assert endpoint_clause_identity(a,S,C)

print("counterexample_formula_clauses =", len(F))
print("satisfying_assignments =", len(SAT))
print("sigma_component_size =", len(seen))
print("sigma_component_max_weight =", max(sum(a) for a in seen))
print("sigma =", sigma)
print("critical_sets =", {v:critical(v,sigma) for v in range(n)})
print("single_y_flip_sat =", sat(flip(sigma,(y,))))
print("individual_rescues_sat =", [sat(flip(sigma,(y,x))) for x in leaves])
print("two_leaf_augmentation_sat =", sat(flip(sigma,(y,2,3))))
print("flip_set_clause_identity_checks =", len(SAT)*(1<<n)*len(F))
print("ALL_EXACT_CHECKS_PASS = True")
