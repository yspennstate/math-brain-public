#!/usr/bin/env python3
from itertools import permutations

def compose(p,q):
    # p∘q on {0,...,n-1}
    return tuple(p[q[i]] for i in range(len(p)))

def inv(p):
    out=[0]*len(p)
    for i,j in enumerate(p):
        out[j]=i
    return tuple(out)

def generate(gens, n):
    e=tuple(range(n))
    G={e}
    frontier=[e]
    gens2=list(gens)+[inv(g) for g in gens]
    while frontier:
        a=frontier.pop()
        for g in gens2:
            b=compose(a,g)
            if b not in G:
                G.add(b); frontier.append(b)
    return G

def parity(p):
    invs=0
    for i in range(len(p)):
        for j in range(i+1,len(p)):
            invs += p[i] > p[j]
    return invs % 2

def commutator(a,b):
    return compose(compose(compose(a,b),inv(a)),inv(b))

# S3
a3=set(permutations(range(3)))
e3=(0,1,2)
trans=(1,0,2)      # (12)
H=generate([trans],3)
assert len(a3)==6 and len(H)==2
conjH=set()
for g in a3:
    conj=frozenset(compose(compose(g,h),inv(g)) for h in H)
    conjH.add(conj)
assert len(conjH)==3
assert any(compose(compose(g,trans),inv(g)) not in H for g in a3)

# left cosets H r
unseen=set(a3); cosets=[]
while unseen:
    r=next(iter(unseen))
    C={compose(h,r) for h in H}
    cosets.append(C); unseen-=C
assert len(cosets)==3 and all(len(C)==2 for C in cosets)

# quotient adjacency if S3\{e} is included in Cayley generator set
adj=[[0]*3 for _ in range(3)]
for i,C in enumerate(cosets):
    for j,D in enumerate(cosets):
        if i==j: continue
        found=False
        for r in C:
            for t in D:
                s=compose(inv(r),t)
                if s != e3: # then s ∈ S3\{1}
                    found=True
                    break
            if found: break
        adj[i][j]=int(found)
assert adj == [[0,1,1],[1,0,1],[1,1,0]]

# derived subgroup of S3
comms3=[commutator(a,b) for a in a3 for b in a3]
D3=generate(comms3,3)
assert len(D3)==3
assert len(a3)//len(D3)==2

# A5
all5=set(permutations(range(5)))
A5={p for p in all5 if parity(p)==0}
assert len(A5)==60
comms5=[commutator(a,b) for a in A5 for b in A5]
D5=generate(comms5,5)
assert len(D5)==60

# A5 has trivial abelianization, S3 has C2 abelianization.
# Therefore (S3 * A5)^ab = C2, so no C3 quotient can exist.
assert len(a3)//len(D3)==2
assert len(A5)//len(D5)==1

print("P19 independent D0072 finite-core audit")
print(f"|S3|={len(a3)} |H|={len(H)} index={len(cosets)} conjugates(H)={len(conjH)}")
print("quotient adjacency:")
for row in adj:
    print(" ".join(map(str,row)))
print(f"|[S3,S3]|={len(D3)} |S3^ab|={len(a3)//len(D3)}")
print(f"|A5|={len(A5)} |[A5,A5]|={len(D5)} |A5^ab|={len(A5)//len(D5)}")
print("finite implication: no C3 quotient of (S3*A5) via abelianization")
print("P19-AUDIT-P20-D0072-ENDTOEND-23 FINITE_CORE_PASS")
