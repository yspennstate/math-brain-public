from fractions import Fraction
from math import comb

p = Fraction(19,125)

def closure_probs(j):
    """Probabilities that a C3 bond-percolation closure from j fixed seeds has size l=1,2,3."""
    q = 1-p
    if j == 0:
        return {0: Fraction(1)}
    if j == 1:
        return {
            1: q*q,
            2: 2*p*q*q,
            3: 3*p*p - 2*p*p*p,
        }
    if j == 2:
        return {
            2: q*q,
            3: 2*p - p*p,
        }
    if j == 3:
        return {3: Fraction(1)}
    raise ValueError(j)

# P[k-1][l-1] = probability that a fixed child fibre has type l
# when its parent fibre has type k. The number j of horizontal seeds is Bin(k,p).
P = []
for k in (1,2,3):
    row = []
    for l in (1,2,3):
        total = Fraction(0)
        for j in range(1,k+1):
            seed = Fraction(comb(k,j)) * p**j * (1-p)**(k-j)
            total += seed * closure_probs(j).get(l, Fraction(0))
        row.append(total)
    P.append(row)

M = [[5*x for x in row] for row in P]  # five forward T_6 children
v = [20,39,57]
slack = []
for i,row in enumerate(M):
    slack.append(sum(row[j]*v[j] for j in range(3)) - v[i])

assert all(x > 0 for x in slack)

# Operator-side rational certificate.
# a = 3 + 2 sqrt(5) < 753/100 = z + 8/z at z=25/4.
assert 453**2 > 5*200**2
z = Fraction(25,4)
assert z + Fraction(8,1)/z == Fraction(753,100)
# Hence beta_9(a) < 25/4 and p_{2->2} > 4/25.
pu_lb = Fraction(4,25)
pc_ub = p
gap = pu_lb - pc_ub
assert gap == Fraction(1,125)

print("p0 =", p)
print("P =")
for row in P:
    print([str(x) for x in row])
print("M=5P =")
for row in M:
    print([str(x) for x in row])
print("v =", v)
print("Mv-v =", [str(x) for x in slack])
print("all_PF_slacks_positive =", all(x > 0 for x in slack))
print("sqrt5_bound: 453^2 - 5*200^2 =", 453**2 - 5*200**2)
print("z =", z, "z+8/z =", z + Fraction(8,1)/z)
print("pu_lower_strict >", pu_lb)
print("pc_upper_strict <", pc_ub)
print("gap_strict >", gap, "=", float(gap))
print("ALL_EXACT_CHECKS_PASS")
