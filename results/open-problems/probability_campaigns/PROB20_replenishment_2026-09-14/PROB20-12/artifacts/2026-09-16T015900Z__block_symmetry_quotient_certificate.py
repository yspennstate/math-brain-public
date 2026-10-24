from fractions import Fraction as F
from itertools import product, combinations
from collections import defaultdict

# Exact rational diagnostic for the block-symmetry quotient-lifting theorem.
# Six sites in three two-point exchangeability blocks.
blocks=[(0,1),(2,3),(4,5)]

# Rational orthogonal quotient matrix: rows=blocks, cols=colors.
Q=[[F(1,3),F(2,3),F(2,3)],
   [F(2,3),F(1,3),F(-2,3)],
   [F(2,3),F(-2,3),F(1,3)]]

for i in range(3):
  for j in range(3):
    s=sum(Q[b][i]*Q[b][j] for b in range(3))
    assert s==(1 if i==j else 0)

# H_i = owner zero-sum line in B_i plus quotient constant line U_i.
# We use an unnormalised rational basis. Its Gram matrix is 2 I, so a
# two-site basis probability is det(M_X)^2 / det(M M^T) = det(M_X)^2/4.
bases=[]
for i in range(3):
    v=[F(0) for _ in range(6)]
    a,b=blocks[i]
    v[a]=1
    v[b]=-1
    w=[]
    for bb in range(3):
        w += [Q[bb][i],Q[bb][i]]
    assert sum(x*x for x in v)==2
    assert sum(x*x for x in w)==2
    assert sum(x*y for x,y in zip(v,w))==0
    bases.append((v,w))

def det2_prob(i,S):
    v,w=bases[i]
    a,b=sorted(S)
    d=v[a]*w[b]-v[b]*w[a]
    return d*d/F(4)

# Quotient rank-one DPP coupling. The squared quotient matrix is
# (1/9)*[[1,4,4],[4,1,4],[4,4,1]].
# Identity has weight 1/9 and the two 3-cycles weight 4/9 each.
assignments=[
    ((0,1,2),F(1,9)),
    ((1,2,0),F(4,9)),
    ((2,0,1),F(4,9)),
]

joint=defaultdict(F)
for q,wt in assignments:
  for zbits in product([0,1], repeat=3):
    p=wt*F(1,8)
    X=[set() for _ in range(3)]
    for bb,B in enumerate(blocks):
      owner=bb
      qc=q[bb]
      z=B[zbits[bb]]
      if qc==owner:
        X[owner].update(B)
      else:
        X[owner].update(set(B)-{z})
        X[qc].add(z)
    assert set().union(*X)==set(range(6))
    assert sum(len(x) for x in X)==6
    joint[tuple(tuple(sorted(x)) for x in X)]+=p

assert sum(joint.values())==1

# Compare every color marginal exactly against the direct determinant formula.
margs=[defaultdict(F) for _ in range(3)]
for xs,p in joint.items():
  for i in range(3):
    margs[i][xs[i]]+=p

for i in range(3):
  direct={S:det2_prob(i,S) for S in combinations(range(6),2)}
  direct={S:p for S,p in direct.items() if p}
  assert dict(margs[i])==direct

# The union of colors 1 and 2 is the complement of color 0.
# Verify the union marginal pointwise using the projection-DPP dual law.
un=defaultdict(F)
for xs,p in joint.items():
    un[tuple(sorted(set(xs[1])|set(xs[2])))]+=p
for T,p in un.items():
  comp=tuple(sorted(set(range(6))-set(T)))
  assert p==det2_prob(0,comp)

print('joint_atoms',len(joint))
print('marginal_support_sizes',[len(m) for m in margs])
print('all_exact_checks_passed')
