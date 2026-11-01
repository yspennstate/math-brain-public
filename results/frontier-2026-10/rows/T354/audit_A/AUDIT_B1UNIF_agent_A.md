# Audit 2 of NOTE "Uniform in beta1" (agent_B/NOTE.md, 20 Oct 09:5x)

Audit 1 is agent C's audit_C/AUDIT_UNIFORM_B1_agent_C.md (10:02). The two were written at the same time and
independently, by different routes. Audit 1 checks the transposition identity with random non-comonotone weights, at n 5-7, eps 0 and 1,
and the exact root at beta1 up to 0.9999 on the three-valued b. This audit checks e2 itself against d S, without going through the
identity, and it runs a negative control with S = 0. Both reach CONFIRMED on steps 1-4, and they make the same two hand points: the
convex-combination argument for psi's range, and sum_q X_q = 0 with the unseen slots included. Audit 1's remark that the step-3
expectation is O(d^2) when a is flat over an epoch fits the d dependence seen here.

agent A, 20 Oct 2026 10:0x. Scope: eps >= 0, a_i = 1, beta1 in [0, 1), the claim |e2| <= C d^2 K_rr(beta1) with C free of n
and beta1, hence x*/x0 = 1 + O(d) uniformly in n and beta1 when B3 != 0.

Verdict: CONFIRMED. Steps 1-4 check by hand. An exact enumeration written for this audit (no code shared with
uniform_b1/transposition_check.py) gives |e2|/(d S) between 0.004 and 2.04 over beta1 0 to 0.9999, with the ratio settling as d
shrinks. A non-comonotone w with S = 0 leaves e2 of order d^2, so comonotonicity carries the step, as the NOTE says. This closes the
question my momentum audit left open (AUDIT_MOMENTUM, section D: "a proof of O(d) uniform in beta1 would need e2 bounded by C d^2 K_rr").

## Steps by hand

1. Both weight sequences are nonnegative and nonincreasing in the lag inside an epoch. The current epoch's unseen slots carry 0 in both,
   and 0 is the smallest value of each, so comonotonicity survives them.
2. sum_q b_pi(q) is the sum of the multiset, which is 0, so sum_q X_q = 0 and sum_q w_q X_q = (1/2n) sum_{q,r} (w_q - w_r)(X_q - X_r).
   For the swap, put pi' = pi o (q r). It has the same law, b_pi'(q) = b_pi(r), and eta(pi') = eta(pi) - (a_q - a_r) DZ. Hence
   X_q - X_r = E[b_pi(q) (F(eta) - F(eta - (a_q - a_r) DZ))]. Averaging this with the same expression written from r replaces
   b_pi(q) by Db/2 and gives the stated 1/(4n). The integral over t is symmetric under the swap: eta - t D -> eta - (1 - t) D.
   The intermediate point is a convex combination of the v of pi and the v of pi', so y stays in [gamma/V, max g^2/V], where psi is smooth.
3. F'(0) = 0 and F'' = psi'', bounded on that range. So |E[Db DZ F'(xi)]| <= |p2| |E[Db DZ xi]| + C E xi^2, with |Db DZ| bounded.
   E[Db DZ eta] splits three ways:
   - The other epochs are independent of epoch e and have mean 0, so they drop.
   - The q and r slots give a_q, a_r <= d/V times bounded moments.
   - The rest uses E[Z_pi(s) | pi(q), pi(r)] = -(Z_pi(q) + Z_pi(r))/(n - 2), exact because sum Z = 0. Times sum_s a_s <= (n - 2) d/V,
     this is at most d/V in absolute value, uniformly in n.
   The shift term is at most (d/V) E DZ^2. E eta^2 = O(d) uniformly in n is the verified UNIFORM step. So the expectation is O(d),
   with constants free of n, beta1, q and r. Nothing here needs |x| = O(d) beyond what the root bracket already gives (AUDIT_UNIFORM, item E).
4. Comonotonicity makes every (w_q - w_r)(a_q - a_r) >= 0, which turns the bound on each pair into |T_e| <= (C d/4) S_e. With F' = 1 and
   q != r, E[Db DZ] = 2 E[bZ] - 2 E[b_i Z_j] = 2 E[bZ] (1 + 1/(n - 1)) = (2n/(n - 1)) E[bZ]. So the first-order term is
   (n/(2(n - 1))) E[bZ] sum_e S_e. Matching it to the lag sum gives sum_e S_e = 2 (n - 1) d K_rr/(n V) <= 2 d K_rr/V, and
   |e2| <= C' d^2 K_rr. A by-product: K_rr >= 0 for every beta1 and beta2. The e1 terms (x E[psi]) involve v only, so they carry no beta1.

## Exact enumeration (b1unif/)

b1unif_enum.py sets up two independent epochs and enumerates all n!^2 orders. It uses b = (4, -1, -1, -1, -1) at n = 5 and
(3, 1, -1, -1, -1, -1) at n = 6, x = 0 and psi = y^(-1/2), with a_q = (d/V) beta2^lag and w_q = (1 - beta1) beta1^lag. It computes
e2 = E[(w.b) F(eta)] directly, with no transposition identity, and compares it with d S. The table below gives e2/(d S) at d = 0.002
(full grid, d 0.05/0.01/0.002 and beta2 0.8/0.95: b1unif_enum_run1.txt):

| b, beta2 | beta1 0 | 0.5 | 0.9 | 0.99 | 0.999 | 0.9999 |
|---|---|---|---|---|---|---|
| n 5, 0.8 | 2.036 | 1.149 | 0.524 | 0.408 | 0.398 | 0.396 |
| n 5, 0.95 | 0.525 | 0.250 | 0.065 | 0.034 | 0.031 | 0.031 |
| n 6, 0.8 | 0.761 | 0.461 | 0.217 | 0.169 | 0.164 | 0.164 |
| n 6, 0.95 | 0.203 | 0.106 | 0.028 | 0.015 | 0.013 | 0.013 |

Over beta1 0 to 0.9999, e2 and S each fall by about eight orders of magnitude while their ratio converges. That is the
"(1 - beta1)^2 for both" the NOTE reports, seen on a different model. Each epoch also obeys the bound separately: T0/(d S0) and T1/(d S1)
stay within [-0.07, 2.04]. From d 0.01 to 0.002 the ratio moves by under 15 pct on every row; the d 0.05 column is further off on the small ratios
(0.0085 against 0.034). So e2 = O(d S), not O(S).

Negative control (b1unif_control.py, b1unif_control_run1.txt). Take w = (1 - beta1) beta1^lag + t (one-hot at the middle lag), with t
chosen so that the signed S is exactly 0. This w is not comonotone with a. e2 is then -1.12e-4 at d 0.01 and -4.50e-6 at d 0.002
(n 5, beta2 0.8, beta1 0.5), a ratio of 25 = 5^2. So e2 is order d^2 while S = 0. The bound in terms of S fails without comonotonicity,
which is exactly the property the NOTE's step 1 supplies.

## What this does not cover

The enumeration is at n = 5 and 6 only. The n-uniformity rests on step 3's conditioning argument, which is exact, and on the verified
E eta^2 = O(d). It agrees with the exact-solver table at n up to 400 (AUDIT_MOMENTUM, section D): (x*/x0 - 1)/d stays within 1.15 at
every beta1 to 0.999. The constant C is not computed. The ratio column above suggests it is of order 1 on these models.

Files: b1unif/b1unif_enum.py, b1unif_enum_run1.txt, b1unif_control.py, b1unif_control_run1.txt.
