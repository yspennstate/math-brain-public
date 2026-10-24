from fractions import Fraction as F

# I0130 exact-rational self-check for the B8 symbolic-breakpoint run.
# This does NOT replace the written continuum proof. It checks the arithmetic
# in the exact theorem G_3^{delta=1/10}(D=2)=729/4000.

delta = F(1, 10)
alpha = 1 - delta
beta = 1 + delta
assert alpha + beta == 2

# Preserved exact continuous two-step Bellman formula.
D0 = alpha * beta / 2
A = alpha * alpha / 2
D1 = 2 * alpha - alpha * alpha / 2
cut = 2 * alpha
assert D0 == F(99, 200)
assert A == F(81, 200)
assert D1 == F(279, 200)
assert cut == F(9, 5)

# At D=2 write x=2-C, where C=beta*a+alpha*b.  On the G2 plateau
# the unconstrained branch-balance point is a*=A/(alpha+beta)=A/2.
astar = A / 2
xstar = beta * (1 - astar)
V = alpha * astar
assert astar == F(81, 400)
assert xstar == F(3509, 4000)
assert V == F(729, 4000)
assert D0 < xstar < D1

# On the first G2 piece the balance point is infeasible; at the smallest
# feasible a the low branch equals alpha-beta=-1/5.
assert alpha - beta == F(-1, 5)
assert F(-1, 5) < V

# On the plateau below xstar the constrained optimum is x + A - beta,
# increasing to exactly V at xstar.
assert xstar + A - beta == V

# On the third G2 piece, g(x)<=A and the balance point is feasible.
# It suffices to verify feasibility at the worst endpoint x=2*alpha:
# beta*(2*alpha-x) <= 2*(2-x), with slack 4*delta.
x = cut
assert 2 * (2 - x) - beta * (2 * alpha - x) == 4 * delta
assert 4 * delta > 0

# Explicit attaining action: choose x=1 (hence C=1) inside the plateau.
x = F(1, 1)
a = astar
b = (1 - beta * a) / alpha
assert b == F(3109, 3600)
assert 0 <= a <= 1 and 0 <= b <= 1
C = beta * a + alpha * b
assert C == 1
assert D0 <= x <= D1
H = alpha * a
L = -beta * a + A
assert H == L == V

print("I0130_SYMBOLIC_G3_SELFCHECK_PASS")
print("delta=1/10")
print("alpha=9/10")
print("G2_breakpoints=99/200,279/200,9/5")
print("G2_plateau=81/200")
print("plateau_balance_a=81/400")
print("plateau_feasibility_threshold_x=3509/4000")
print("attaining_action_a=81/400")
print("attaining_action_b=3109/3600")
print("attaining_C=1")
print("G3_at_D2=729/4000")
