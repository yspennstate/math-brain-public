#!/usr/bin/env python3
"""Exact finite checker for the tensor-product MUB counterexample route in C^6=C^2 tensor C^3."""
import itertools
import sympy as sp

I=sp.I
sqrt=sp.sqrt
omega=-sp.Rational(1,2)+I*sqrt(3)/2

def sqabs(z):
    return sp.simplify(sp.expand_complex(z*sp.conjugate(z)))

def is_unitary(M):
    return sp.simplify(M.conjugate().T*M-sp.eye(M.rows)) == sp.zeros(M.rows)

def mub(A,B):
    d=A.rows
    C=sp.simplify(A.conjugate().T*B)
    return all(sp.simplify(sqabs(C[i,j])-sp.Rational(1,d))==0 for i in range(d) for j in range(d))

Q2=[
    sp.eye(2),
    sp.Matrix([[1,1],[1,-1]])/sqrt(2),
    sp.Matrix([[1,1],[I,-I]])/sqrt(2),
]
Q3=[sp.eye(3)]
for a in range(3):
    M=sp.zeros(3)
    for x in range(3):
        for b in range(3):
            M[x,b]=omega**((a*x*x+b*x)%3)/sqrt(3)
    Q3.append(sp.simplify(M))

assert all(is_unitary(M) for M in Q2)
assert all(is_unitary(M) for M in Q3)
assert all(mub(Q2[i],Q2[j]) for i,j in itertools.combinations(range(3),2))
assert all(mub(Q3[i],Q3[j]) for i,j in itertools.combinations(range(4),2))

labels=[(a,b) for a in range(3) for b in range(4)]
assert len(labels)==12

def product_mub(x,y):
    return x[0]!=y[0] and x[1]!=y[1]

edge_set={(i,j) for i,j in itertools.combinations(range(12),2) if product_mub(labels[i],labels[j])}
assert len(edge_set)==36

max_size=0
max_cliques=[]
for r in range(1,13):
    found=[]
    for comb in itertools.combinations(range(12),r):
        if all((min(i,j),max(i,j)) in edge_set for i,j in itertools.combinations(comb,2)):
            found.append(comb)
    if found:
        max_size=r
        max_cliques=found
    else:
        break
assert max_size==3
assert len(max_cliques)==24

# Exact full-pair residual for product bases.  If both local labels differ, the
# tensor product is MUB and the block residual is zero.  If only the qubit
# label agrees, the 36 squared overlaps are 18 copies of 1/3 and 18 zeros,
# giving block residual 1.  If only the qutrit label agrees, they are 12
# copies of 1/2 and 24 zeros, giving block residual 2.
def pair_residual(x,y):
    same2=(x[0]==y[0])
    same3=(x[1]==y[1])
    assert not (same2 and same3)
    if not same2 and not same3:
        return sp.Integer(0)
    if same2:
        return sp.Integer(18)*(sp.Rational(1,3)-sp.Rational(1,6))**2 + sp.Integer(18)*(sp.Rational(0)-sp.Rational(1,6))**2
    return sp.Integer(12)*(sp.Rational(1,2)-sp.Rational(1,6))**2 + sp.Integer(24)*(sp.Rational(0)-sp.Rational(1,6))**2

assert pair_residual((0,0),(0,1))==1
assert pair_residual((0,0),(1,0))==2
assert pair_residual((0,0),(1,1))==0

best_total=None
best_seven=[]
seven_count=0
for comb in itertools.combinations(range(12),7):
    seven_count += 1
    total=sum(pair_residual(labels[i],labels[j]) for i,j in itertools.combinations(comb,2))
    total=sp.simplify(total)
    if best_total is None or total<best_total:
        best_total=total
        best_seven=[comb]
    elif total==best_total:
        best_seven.append(comb)

assert seven_count==792
assert best_total==11
assert len(best_seven)==144
best_normalized=sp.Rational(best_total,21*36)
assert best_normalized==sp.Rational(11,756)

print('C29 exact tensor-product MUB checker: PASS')
print('ambient dimension: 6 = 2*3')
print('local complete MUB counts: 3 in C^2, 4 in C^3')
print('product bases checked:',len(labels))
print('exact MUB edges:',len(edge_set))
print('maximum pairwise-MUB product-basis clique size:',max_size)
print('number of maximum cliques:',len(max_cliques))
print('7-subsets exhaustively checked:',seven_count)
print('minimum unnormalized full-pair residual over product-family 7-tuples:',best_total)
print('minimum normalized residual over product-family 7-tuples:',best_normalized)
print('number of residual-minimizing 7-tuples:',len(best_seven))
print('first five maximum cliques (local labels):')
for c in max_cliques[:5]:
    print(' ',[labels[i] for i in c])
print('CONCLUSION: no seven-MUB counterexample exists inside the complete 12-basis tensor-product family.')
