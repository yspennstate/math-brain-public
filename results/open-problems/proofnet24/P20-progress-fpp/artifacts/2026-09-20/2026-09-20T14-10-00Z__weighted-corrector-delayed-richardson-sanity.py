from fractions import Fraction
import sympy as sp

# 1) Exact uniform-profile boundary-chain variance/reset calculation.
W = 48
M = W + 1
# Adjacent output-boundary link costs Z_l are Gamma(2,1): E Z=2, Var Z=2.
coeffs = [Fraction(M-2-2*l, M) for l in range(M-1)]
mean_D = sum(c*2 for c in coeffs)
var_D = sum(c*c*2 for c in coeffs)
expected_var = Fraction(2*W*(W-1), 3*(W+1))
assert mean_D == 0
assert var_D == expected_var
# E max(H_left,H_right) <= W + 1/2 sqrt(var_D)
C_uniform = sp.Integer(W) + sp.sqrt(sp.Rational(W*(W-1), 6*(W+1)))
assert sp.simplify(C_uniform - (sp.Integer(48) + 2*sp.sqrt(94)/7)) == 0

# 2) Exact branch threshold for pure uniform corrector eta=1, kappa=0, L=4.
L = 4
lam = sp.Rational(3002823, 1250000)  # 4 * 0.6005646
avg_threshold = sp.Integer(2*L) + C_uniform - lam
single_zero_r = sp.simplify(avg_threshold * sp.Rational(M, M-1))
span_only_r = sp.Integer(2*L + 2*W) - lam  # kappa=1
assert single_zero_r < span_only_r

# 3) Samplewise endpoint-max property on a finite chain with exact rational link costs.
# H_k = average chain distance from k to all j; it decreases then increases, so max is endpoint.
Z = [Fraction(3,2), Fraction(5,4), Fraction(7,3), Fraction(11,6)]
Msmall = 5
H = []
for k in range(Msmall):
    tot = Fraction(0)
    for j in range(Msmall):
        if j < k:
            tot += sum(Z[j:k])
        elif j > k:
            tot += sum(Z[k:j])
    H.append(tot/Fraction(Msmall))
assert max(H) == max(H[0], H[-1])

# 4) Delayed Richardson reward identity on two-source/one-output star.
# s0 active at 0, s1 activates at a, each has an independent Exp(1) edge to output o.
# T_o = min(E0, a + E1), hence E T_o = 1 - exp(-a)/2.
a = sp.symbols('a', positive=True)
closed = 1 - sp.exp(-a)/2
# First-event recursion: reward before activation E[min(E0,a)] + survival*postactivation mean 1/2.
rec = (1-sp.exp(-a)) + sp.exp(-a)*sp.Rational(1,2)
assert sp.simplify(closed-rec) == 0

# 5) Undelayed weighted-output reward identity on a two-output star.
# One source, outputs o1,o2 with iid Exp(1) edges. first=min(E1,E2), last=max(E1,E2).
# With kappa=1/4 and uniform alpha total eta=1/2 (alpha_j=1/4 each),
# Q=(1-kappa-eta)t_first + kappa t_last + sum alpha_j F_j.
kappa = sp.Rational(1,4)
eta = sp.Rational(1,2)
E_first = sp.Rational(1,2)
E_last = sp.Rational(3,2)
E_sumF_weighted = sp.Rational(1,4)*1 + sp.Rational(1,4)*1
Q = (1-kappa-eta)*E_first + kappa*E_last + E_sumF_weighted
assert Q == sp.Integer(1)

print('P20-T10-WEIGHTED-CORRECTOR-DELAYED-RICHARDSON-SANITY: ALL_EXACT_CHECKS_PASS')
print('uniform_reset_bound_C49 =', sp.sstr(C_uniform), '=', sp.N(C_uniform, 18))
print('avg_profile_threshold =', sp.sstr(avg_threshold), '=', sp.N(avg_threshold, 18))
print('single_zero_other_coords_threshold =', sp.sstr(single_zero_r), '=', sp.N(single_zero_r, 18))
print('previous_span_only_threshold =', sp.sstr(span_only_r), '=', sp.N(span_only_r, 18))
print('exact_delayed_star_mean =', sp.sstr(closed))
print('exact_two_output_weighted_Q =', Q)
