from itertools import product
weights=set()
rows=[]
# Canonical representatives for quadratic forms q:F2^7->F2 with alternating polar rank 2s.
# q0 has Arf 0 on the symplectic quotient; q1 toggles Arf by x0+x1 for s>=1.
# A nonzero radical-linear term (when the radical is nontrivial) makes q balanced.
for s in range(4):
    r=7-2*s
    reps=[]
    reps.append(("arf0", lambda x,s=s: sum(x[2*j]*x[2*j+1] for j in range(s)) & 1))
    if s>=1:
        reps.append(("arf1", lambda x,s=s: (sum(x[2*j]*x[2*j+1] for j in range(s)) + x[0] + x[1]) & 1))
    if r>=1:
        reps.append(("radlinear", lambda x,s=s: (sum(x[2*j]*x[2*j+1] for j in range(s)) + x[2*s]) & 1))
    for name,q in reps:
        w=sum(q(x) for x in product((0,1), repeat=7))
        weights.add(w)
        rows.append((s,r,name,w))
for row in rows:
    print(*row)
print('weights=',','.join(map(str,sorted(weights))))
assert weights=={0,32,48,56,64,72,80,96}
print('P03-C7-QUADRATIC-MOD8-WEIGHT-SELF-CHECK=PASS')
