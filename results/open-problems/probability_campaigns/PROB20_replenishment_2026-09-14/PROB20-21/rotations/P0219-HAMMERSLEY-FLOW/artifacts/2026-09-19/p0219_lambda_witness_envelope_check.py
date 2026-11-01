#!/usr/bin/env python3
"""
P0219 exact self-check for the lambda-envelope of the preserved four-defect
routing-tax witness. Integer arithmetic only.

For every vertex set A in the n=4 directed grid, compute the affine score
    S_lambda(A) = C_f(A) - B(A) - lambda O_b(A) = a - lambda b.
For the preserved closed set C={0,2,11,12}, verify that every affine line lies
below 3-lambda on [0,1], that (a,b)=(3,1) occurs, and that at lambda=1 the
best value is 2. Hence G(lambda)=3-lambda for 0<=lambda<=1, with a monotone
(score-slope 0) optimizer tying only at lambda=1.
"""
def vertices(n):
    return [(x,y) for x in range(n) for y in range(n)]

def edges(n):
    E=[]
    for x in range(n):
        for y in range(n):
            if x+1<n:
                E.append(((x,y),(x+1,y)))
            if y+1<n:
                E.append(((x,y),(x,y+1)))
    return E

n=4
V=vertices(n)
E=edges(n)
vix={v:i for i,v in enumerate(V)}
C={0,2,11,12}

lines=set()
witness_As=[]
for amask in range(1<<len(V)):
    inside=[bool((amask>>i)&1) for i in range(len(V))]
    cf=0
    back=0
    open_back=0
    for ei,(u,v) in enumerate(E):
        iu,iv=vix[u],vix[v]
        if inside[iu] and not inside[iv] and ei in C:
            cf += 1
        if not inside[iu] and inside[iv]:
            back += 1
            if ei not in C:
                open_back += 1
    a=cf-back
    b=open_back
    lines.add((a,b))
    if (a,b)==(3,1):
        witness_As.append(amask)

assert witness_As, "missing (3,1) witness line"

# A linear inequality on [0,1] is certified by its two endpoints.
for a,b in lines:
    assert a <= 3, (a,b,"lambda=0 violation")
    assert a-b <= 2, (a,b,"lambda=1 violation")

best0=max(a for a,b in lines)
best1=max(a-b for a,b in lines)
assert best0==3
assert best1==2

slope0_lines=sorted((a,b) for a,b in lines if a==best0)
slope1_lines=sorted((a,b) for a,b in lines if a-b==best1)
assert (3,1) in slope0_lines
assert (3,1) in slope1_lines
assert any(b==0 for a,b in slope1_lines)

print("P0219_LAMBDA_WITNESS_ENVELOPE_EXACT")
print("N", n)
print("CLOSED_EDGE_INDICES", sorted(C))
print("DISTINCT_AFFINE_LINES", len(lines))
print("BEST_AT_LAMBDA_0", best0)
print("BEST_AT_LAMBDA_1", best1)
print("ACTIVE_AT_LAMBDA_0", slope0_lines)
print("ACTIVE_AT_LAMBDA_1", slope1_lines)
print("CERTIFIED_ENVELOPE", "G(lambda)=3-lambda for all 0<=lambda<=1")
print("OPEN_BACKSTEP_SLOPE_AE", 1)
print("INTEGRAL_OPEN_BACKSTEPS", 1)
print("OVERALL_PASS")
