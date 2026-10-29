# T354 scalar model: Adam's limit point under a vanishing step (agent B, 20 Oct 2026)

Model: f_i(x) = a_i x^2/2 + b_i x, i = 1..n, sum b_i = 0, so f = mean f_i has its minimum at 0. Adam in the PyTorch form (EMAs m, v,
bias correction, eps outside the root) with random reshuffling (RR) or with-replacement sampling (iid) and a step that goes to
zero. The iterate then moves on a slower clock than the moving averages and follows xdot = -D(x), where D(x) is the stationary
mean of m_k/(sqrt(v_k) + eps) at frozen x. The limit point x* solves D(x*) = 0, and |f'(x*)| = abar |x*| is the residual.

Result (first order in the fluctuation of v, eps = 0). Write g_i = a_i x + b_i, V = mean g^2, C = mean g^3 - f'(x) V. Then

    D(x) = V^(-1/2) [ f'(x) - (1 - beta2) K C / (2V) ] + higher order,
    x*  = (1 - beta2) K m3 / (2 abar V0) (1 + O(1 - beta2)),   m3 = mean b^3, V0 = mean b^2,

with K = E[m_k dv_k] / ((1 - beta2) C). Under iid sampling K = (1 - beta1)/(1 - beta1 beta2) (the lag sum (1-beta1)(1-beta2) C sum_i (beta1 beta2)^i), which is 1 at beta1 = 0 and about 1/2 at beta1 = beta2; corrected by agent A's audit (rows/T354/audit_A, sim K 0.524 +/- 0.010 at beta1 = beta2 = 0.99 against 0.5025) - the first text said K = 1 for every beta1, and its iid checks were all at beta1 = 0. Under RR, lags i (for m) and j (for v) contribute
C when i = j, -C/(n-1) when they are different positions of the same epoch, and 0 across epochs (independent permutations), so
K = (1/n) sum_p sum_i (1-beta1) beta1^i [beta2^i - (S_e(i) - beta2^i)/(n-1)], S_e = sum of beta2^j over the epoch of lag i
(kfactor.py). At beta1 = 0: K = 1 - (1/(n(n-1))) sum_p sum_{j=1..p} beta2^j, which is 1/2 as n(1-beta2) -> 0 and tends to 1 (the
iid value) as n(1-beta2) -> infinity. With momentum and n(1-beta2) small, K = (1/n) sum_p (1 - p/(n-1))(1 - beta1^(p+1)), which
goes to 0 as 1/(1-beta1) >> n and to 1/2 as n >> 1/(1-beta1).

So, in this model, the residual is linear in 1 - beta2, its coefficient is the third moment of the per-example gradients at the
optimum over their second moment, and reshuffling halves it when the v-window is longer than an epoch. It does not depend on
n(1 - beta2) except through K, which stays in [1/2, 1] at beta1 = 0. It is zero when the b_i are symmetric (D(0) = 0 by symmetry).
It does not vanish with the step size at fixed beta2: a lower bound of the residual in the scalar class is
|f'(x*)| >= (1 - beta2) |m3| / (4 V0) (1 - o(1)) for RR at beta1 = 0.

Checks (n = 10, b = (9, -1, ..., -1), a = 1, so m3/V0 = 8): frozen-x drift by simulation over 2000-4000 chains of random
permutations, bisection for x* (adam_scalar_drift.py, sweep.py -> sweep_n10.jsonl, kfactor.py output in kfactor_check.txt).
RR beta1 0: sim / first order = 0.998, 0.982, 0.916, 0.840, 0.485 at beta2 = 0.999, 0.99, 0.95, 0.9, 0.5. RR beta1 0.9: 0.994,
0.887 (2000 chains; rechecked at 8000 chains, seeds 1 and 2: 1.023, 1.012), 1.002, 1.046, 0.925. iid is Monte Carlo noisy (the epoch average of g is not exact): 1.09, 1.03, 0.99 at
beta1 0. First-order prediction at beta2 0.999 RR beta1 0: 0.002008, simulated 0.002005.

End-to-end Adam (PyTorch update with bias correction, eta_k = 0.05/sqrt(k), 2e6 steps, start 0.5, adam_run.py), mean iterate over
the second half against the frozen-x x*: 0.0020047 vs 0.0020048 (beta2 0.999, beta1 0), 0.23178 vs 0.23187 (0.9, 0), 0.032744 vs
0.032662 (0.95, 0.9) - the slow-clock reduction holds, bias correction included.

Vector case (20 Oct 00:5x, vec_drift.py, vec_drift_runs.jsonl). f_i(x) = x'Hx/2 + b_i'x in R^d with coordinatewise Adam. The
lag covariance argument runs coordinate by coordinate: m_k and v_k are built from g_k alone, so the first-order drift is
D_k = V_k^{-1/2} [d_k f - (1 - beta2) K C_k/(2 V_k)] with C_k the third central moment of g_k, and D(x*) = 0 gives
H x* = (1 - beta2) K c, c_k = E[b_k^3]/(2 E[b_k^2]). Only each coordinate's own third moment enters; cross moments such as
E[b_2 b_1^2] do not. Test: d = 2, H = [[1, .5], [.5, 2]], n = 10, b_1 = (9, -1 x 9), b_2 = (-4, -4, 2, 1 x 6, 0) (c = (4, -1.357);
the two coordinates are strongly dependent, E[b_2 b_1^2] = -32 against E[b_2^3] = -11.4, so a cross-moment law would miss by about
a factor 3 on coordinate 2). Frozen-x drift at three points with common random numbers, linear solve, one refinement, residual drift
on a fresh seed. Simulated over predicted x*, per coordinate:
  RR  b1 0    b2 0.999  K 0.502  0.9989 0.9995
  RR  b1 0    b2 0.99   K 0.518  0.9885 0.9923
  RR  b1 0    b2 0.95   K 0.583  0.9464 0.9658
  RR  b1 0.9  b2 0.99   K 0.155  1.0016 0.9907
  RR  b1 0.9  b2 0.999  K 0.152  0.9953 0.9912
  iid b1 0    b2 0.99   K 1      1.0195 1.0107  (50,000 chains; residual drift 2 pct of D(0))
  iid b1 0.99 b2 0.99   K 0.5025 1.0536 1.0475  (50,000 chains; residual 5 pct; K = 1 would give about 0.52 - the audit's iid
                                                 correction confirmed on a second model)
The departures at beta2 0.95 are the same second-order terms as in the scalar runs.

Prior work (read 20 Oct 00:4x). Dereich, Do, Jentzen and von Wurstemberger, "Adam symmetry theorem" (arXiv 2511.06675 v2,
22 Jun 2026), prove for iid data and quadratic loss |theta - x|^2 with two-point x that Adam with vanishing steps reaches the
minimizer if and only if the data are symmetric (Thm 1.1), and for strongly convex problems an upper bound
c0 M^{-1}(1 - beta2) + c sqrt(gamma_n) on the error with existential constants (Thm 1.2); their simulations (Sec. 5.2.2, 5.3.2,
two-point and skew normal data) suggest the rates 1 in 1/M and in 1 - beta2 are sharp. Their limit theorem (Thm 3.2, from
Dereich, Jentzen and Kassing, arXiv 2511.04622) says a convergent Adam run sits at a zero of the Adam vector field, the stationary
mean of m/(eps + sqrt(v)) at frozen theta - the same D used here. So the frozen-drift reduction, the symmetry criterion and the
order (1 - beta2)/M are theirs. What is not in either paper: the leading constant, x* = (1 - beta2) K m3 / (2 abar V0), and any
treatment of reshuffling. The constant agrees with their rate: an iid mini-batch of size M has m3/M^2 and V0/M, so
x* = (1 - beta2) K m3 / (2 abar V0 M) with K = (1 - beta1)/(1 - beta1 beta2), which attains their M^{-1}(1 - beta2) order exactly and so confirms that it is sharp.
The reshuffling factor K (1/2 when n(1 - beta2) is small, beta1 = 0) has no counterpart there (iid only). Also searched:
2208.09632 (Zhang et al., neighbourhood of size O(variance) once beta2 is large; no constant), 2208.09900 (Wang et al., RR Adam
under (L0,L1) smoothness; rates, no limit point), Reddi et al. 1904.09237 (non-convergence by construction).

Rigorous remainder, iid sampling, any beta1, eps = 0 (20 Oct 01:3x, remainder_iid.py, remainder_iid_runs.txt, iid_condmean.py).
Assume m = min_i g_i(x)^2 > 0 near the optimum. For momentum lag i write the stationary v_k = V t_i + d beta2^i Z_{k-i}
(d = 1 - beta2, Z = g^2 - V), where t_i is independent of g_{k-i}, E t_i = 1, t_i >= m/V and Var t_i <= d Var(g^2)/((1+beta2)V^2).
Taylor expansion of y^(-1/2) in the lag-i term, with independence, gives exactly
    sqrt(V) D(x) = f'(x) P0 - (d K C/(2V)) P1 + R,   K = (1 - beta1)/(1 - beta1 beta2),
where P0 >= 1 and P1 >= 1 by Jensen (y^(-1/2) convex, its derivative concave), P0 - 1 and P1 - 1 are O(d) through Var t_i, and
|R| <= (1-beta1)/(1-beta1 beta2^2) d^2 E[|g| Z^2]/(2V^2) sup_i E phi''(t_i - d) = O(d^2). The explicit upper bounds use the
divided-difference remainders, which are monotone in t, split at a level t0 with Bernstein's lower-tail bound for the perpetuity
(summands bounded below by -d(V - m)/V). So every zero satisfies abar x* P0 = d K C P1/(2V) - R, i.e.
x* = d K m3/(2 abar V0) (1 + O(d)) with computable constants. This re-derives the audit's iid K by a second route (the lag weights
(1 - beta1)(beta1 beta2)^i appear directly). On the test model the enclosure of x*/x0 for zeros in [0, 3 x0] (the range scanned), sign change verified and the bracket
checked on a 4000-point grid:
  beta2 0.9999 [0.9994, 1.0014]   0.999 [0.9935, 1.0169]   0.995 [0.9504, 1.1444]   0.99 [0.7548, 1.6140]   (beta1 0)
  beta2 0.999, beta1 0.9 [0.9936, 1.0169]; beta1 0.99 [0.9939, 1.0164]
A low-noise check at beta1 0 (iid_condmean.py: the average over the n samples is taken exactly for each sampled v, so only the
fluctuation of v is Monte Carlo) gives x*/x0 = 1.0009, 1.0046, 1.0105 (1.0102 on a second seed) at beta2 0.999, 0.995, 0.99, inside
every enclosure; the second-order correction is about +1.0 d. The earlier iid figure 1.09 at beta2 0.999 was sampling noise.
Not covered: reshuffling (lags within an epoch are dependent, so t_i is no longer independent of g_{k-i}), eps > 0, data with some
g_i(x*) = 0 (then m = 0 and the bound is void; mini-batch means can vanish).

Rigorous remainder, reshuffling, beta1 = 0, eps = 0 (20 Oct 01:4x, remainder_rr.py, remainder_rr_runs.txt). Under RR the deviation of
v_k/V from 1 is bounded deterministically: the current epoch's partial sum is at most beta2^p Smax + (1 - beta2^p) sum|Z_i|
(Smax = sum of the positive Z_i), and each earlier full epoch, a permutation of all Z_i with sum 0, contributes at most
beta2^s (1 - beta2^(n-1))/2 sum|Z_i|, so |v_k/V - 1| <= eps_p = O(d) uniformly. Expanding y^(-1/2) to second order with a
deterministic cubic remainder (5/16) eps^3 (1 - eps)^(-7/2):
    sqrt(V) D = f' - d K C/(2V) + (3/8)(Q2 + X) + R3,   |R3| = O(d^3),
where K is the RR factor of kfactor.py (exact), Q2 collects the second-order terms with both lags in the current epoch (exact, from
the without-replacement moments of (g_a, Z_b, Z_c)), and X = f' times the squared earlier-epoch part, 0 <= X/f' <= eps_full^2. On the
test model the enclosure of x*/x0 is [0.99982, 0.99992] at beta2 0.9999, [0.99348, 1.00391] at 0.999, [0.831, 1.155] at 0.995. The
second-order centre at beta2 0.999 is 0.99869; the frozen-x simulation (sweep_n10.jsonl) gives 0.99870. Since eps grows like
n d (Smax/V + sum|Z|/V), the expansion is useful only while n(1 - beta2) is small, the regime where K is near 1/2. Not covered: RR with
momentum, eps > 0, n(1 - beta2) of order 1.

Rigorous remainder, reshuffling with momentum, eps = 0 (20 Oct 01:5x, remainder_rr_mom.py). The bound |v_k/V - 1| <= eps_p is
unchanged, and m_k is a convex combination of past gradients, so the cubic remainder costs at most G (5/16) eps^3 (1 - eps)^(-7/2).
The first-order term is d K C/V with K = kfactor.K_rr(n, beta1, beta2); the second-order term sums the lag-i moments of
(g_{k-i}, Z_b, Z_c) with weights (1 - beta1) beta1^i, epoch by epoch, truncated at a lag L of many epochs with a crude tail bound.
At beta1 = 0 it reproduces remainder_rr.py ([0.99341, 1.00391] at beta2 0.999). Enclosures of x*/x0: beta1 0.9, beta2 0.9999
[0.99982, 1.00015]; beta1 0.9, beta2 0.999 [0.98257, 1.01701], which contains the simulated 0.99364 (sweep_n10.jsonl, 0.00060328);
beta1 0.5, beta2 0.999 [0.99276, 1.00550]. At beta1 0.9, beta2 0.99 the remainder is not small (eps reaches 1 in the bound) and
the enclosure is empty of content, as expected outside the small n(1 - beta2) regime.

eps > 0 (20 Oct 02:1x, eps_sweep.py, eps_sweep.jsonl, eps_seed_check.py). With s = sqrt(V), 1/(s sqrt(1+u) + eps) =
1/(s+eps) - (s/2) u/(s+eps)^2 + O(u^2), so the correlation term is damped by s/(s+eps) relative to f' and
    x*(eps) = x*(0) s/(s+eps)   to first order, for any sampling scheme and any beta1.
On the test model s = 3. At beta2 0.99, eps 0, 1, 3, 10, RR and iid, beta1 0 and 0.9, every case fits x*(eps) = X 3/(3+eps) + delta
with residual under 0.2 per cent of X. delta is the common-random-number offset of the frozen-x simulation (all eps share one seed;
the noise in the chain mean of m does not shrink with eps while x* does): at RR beta1 0.9 seeds 0, 1, 2 give delta -7.0e-4, 2e-5,
1.3e-4 and X 0.006221, 0.006194, 0.006200, against the first-order 0.04 K_rr(10, 0.9, 0.99) = 0.006213. RR beta1 0 needs no offset
(ratios 0.7512, 0.5016, 0.2320 against 0.75, 0.5, 0.2308). iid beta1 0: X 0.04019 against the exact 0.04039 (laplace_exact.py).
So eps rescales the residual by sqrt(V)/(sqrt(V)+eps) and changes nothing else at this order; the rigorous remainder bounds above
carry over with phi(y) = 1/(s sqrt(y) + eps), whose derivatives are dominated by the eps = 0 ones, but that has not been written out.

Rigorous remainder, reshuffling, beta1 = 0, eps >= 0 (20 Oct 02:2x, remainder_rr_eps.py, remainder_rr_eps_runs.txt). Replace
y^(-1/2) by psi(y) = (s+eps)/(s sqrt(y)+eps): psi'(1) = -r/2, psi''(1) = r/4 + r^2/2 with r = s/(s+eps), and the third derivative
is largest in size at y = 1 - e (every term of (1/q)''' has one sign and grows as y falls), which gives a closed cubic remainder;
at eps = 0 it is (15/8)(1-e)^(-7/2), the old one. Enclosures of x*/(x0 r): beta2 0.999, eps 0/1/3/10: [0.99348, 1.00391],
[0.99512, 1.00263], [0.99648, 1.00163], [0.99763, 1.00085]; beta2 0.99: [0.130, 1.872], [0.404, 1.581], [0.609, 1.373],
[0.763, 1.221]. The eps = 0 row reproduces remainder_rr.py; the simulated values at beta2 0.99 (0.986, 0.989, 0.991, 0.993) are
inside. eps tightens the bound because it damps the denominator's response to v.

Audit 2 of the iid remainder lemma (agent A, 20 Oct, audit_A/AUDIT_REMAINDER_agent_A.md): algebra checked by
hand; exact x*/x0 by a Laplace-transform route with no Monte Carlo lies inside all eight enclosures (e.g. 1.009790 at 0.99/0,
1.023949 at 0.99/0.99). Audit 3, independent (agent C, audit_C/AUDIT_IID_REMAINDER_agent_C.md, 20 Oct
03:2x): CONFIRMED line by line (the t_i >= m/V bound, Jensen for P0 and P1, the divided differences, the Bernstein tail), and
exact x*/x0 by a cumulant route inside all eight enclosures; its one remark, that the bracket covers zeros in [0, 3 x0], is
now in the text. Two independent audits: the iid remainder lemma (beta1 any, eps = 0) counts as verified. The RR lemma with no momentum and eps = 0 has one audit (agent A, audit_A/AUDIT_RR_agent_A.md,
20 Oct 03:1x: the |v/V - 1| bound, the 5/16 remainder, Q2 and the sign of X checked by hand; exact x*/x0 with no Taylor step,
0.993690, 0.998725, 0.999872 at beta2 0.995, 0.999, 0.9999, each inside its enclosure; the second-order centre misses by about
-33 d^2). The RR lemmas with momentum and with eps > 0 have one numerical audit (agent C,
audit_C/AUDIT_RR_MOM_EPS_agent_C.md, 20 Oct 03:2x: an independent exact RR route, epoch factorization with an
erfcx kernel, puts all 10 non-vacuous roots inside their enclosures, e.g. 0.9875, 0.9891, 0.9907, 0.9925 at beta2 0.99; the
enclosure algebra was tested, not re-derived; its addendum of 20 Oct 03:4x re-derives that algebra: the momentum pairing brute-forced
over all permutation pairs to 9.6e-15, the truncation tail conservative, the X bracket using e_p, psi' and psi'' and the monotone
|psi'''| checked). The beta1 = 0, eps = 0 RR lemma has a second independent audit (agent C,
audit_C/AUDIT_RR_B1ZERO_agent_C.md, 20 Oct 03:39: every line re-derived, the moment identities brute-forced over all
720 permutations at n = 6 to 1.2e-16, the exact roots inside all three enclosures) and so counts as verified. The momentum and eps > 0
RR versions have a second audit (agent A, audit_A/AUDIT_RR_MOM_EPS_agent_A.md, 20 Oct 04:0x, push 7ba97458): an
exact route with no Taylor step (rr_exact_mom_eps.py: the erfcx Laplace kernel for eps, one epoch's slot pinned for momentum,
reproducing rr_exact.py at beta1 = 0, eps = 0, its reduction checked against direct RR Monte Carlo at frozen x), putting all twelve
roots inside their enclosures, the tightest 0.999984 in [0.99982, 1.00015] at beta1 0.9, beta2 0.9999. With two independent audits
the RR lemmas with momentum and with eps > 0 count as verified.

Status (20 Oct 04:1x): under iid sampling with eps = 0 the first-order law x* = d K m3/(2 abar V0)(1 + O(d)) is proved by the remainder lemma, which has two independent audits (agent A, agent C), and so counts as verified; under reshuffling all three lemmas (beta1 = 0 with eps = 0, momentum, eps > 0) have two independent audits each (agent A, agent C) and count as verified, so the reshuffled law x* = d K_rr m3/(2 abar V0)(1 + O(d)) is verified too. Open: the RR next-order term (below, candidate) and its momentum version (vector case done above;
contracted against the preconditioned Hessian inverse).

## The next-order term, iid sampling, eps = 0 (20 Oct 2026 02:4x)

Keeping every O(d^2) term of sqrt(V) D(x) (d = 1 - beta2; x* is O(d), so x (y-1)^2 counts at this order) gives, with B_k = E b^k,
Z = b^2 - B2, S = Var(b^2), K = (1-b1)/(1-b1 b2) and K2 = (1-b1)/(1-b1 b2^2),

    E[m (y-1)]   = d K (2 x B2 + B3)/V                                (exact)
    E[m (y-1)^2] = d x S/(2 B2^2) + d^2 K2 E[b Z^2]/B2^2 + O(d^3)
    E[m (y-1)^3] = (3/2) d^2 K B3 S/B2^3 + O(d^3)                     (one index with g, the other two paired)

and the quartic and higher terms are O(d^3). Solving x = (dK/2)(2x B2 + B3)/B2 - (3/8)E2 + (5/16)E3:

    x*/x0 = 1 + d [ K + (3/4) ( S/B2^2 - (K2/K) E[b Z^2]/(B2 B3) ) ] + O(d^2).

For a two-valued b, Z = (b_1 + b_2) b, both ratios equal (b_1+b_2)^2/B2, and the bracket is K + (3/4)((b_1+b_2)^2/B2)(1 - K2/K);
at beta1 = 0 it is exactly 1. On the test model (b_1 + b_2 = 8, B2 = 9) with r = d/(1-b1) held fixed as d -> 0 the bracket tends to
1/(1+r) + (16/3) r/(1+2r): 1.3535 at r = 0.1 and 2.2778 at r = 1; for small r it is 1 + (13/3) b1 r. Check against the exact
Laplace-transform solver of agent A (audit_A/laplace_exact.py, 200 nodes; next_order_exact_runs.txt and
next_order_pred.txt), as (x*/x0 - 1)/d, exact against predicted:

    r = 0.1:  d 0.004 1.3475 / 1.3404,  d 0.002 1.3510 / 1.3470,  d 0.001 1.352 / 1.3502,  d 0.0005 1.352 / 1.3519
    r = 1:    d 0.01  2.3949 / 2.2625,  d 0.004 2.3238 / 2.2717,  d 0.002 2.3005 / 2.2747
    b1 = 0:   d 0.01  0.979 / 1,  d 0.005 0.991 / 1,  d 0.001 0.998 / 1,  d 0.0001 1.000 / 1

The gap shrinks linearly in d in every family (about 13 d at r = 1, 1.8 d at r = 0.1), as an O(d^2) remainder should. The 3.5 fitted
in the second audit is this bracket's slope seen at r = 0.1, where the r^2 terms already matter. Derivation by hand, numerical check
by an independent exact route. Audits: agent A (audit_A/AUDIT_NEXTORDER_agent_A.md, 20 Oct 02:5x: the three
moments and the solve re-derived by hand, the three-valued constants and gaps recomputed; it confirms the coefficient, not a
remainder bound, and uses E b = 0) and agent C (audit_C/AUDIT_NEXT_ORDER_agent_C.md, 03:0x: re-derived with
sympy, and an exact x* with no Laplace kernel, from a Taylor series of the step in Y to order 14 with exact moments of Y lag by
lag; all 13 rows agree to the printed digit). Two independent audits: the eps = 0 coefficient counts as verified.

Three-valued check (20 Oct 02:5x). On the test model the two ratios in the bracket cancel at beta1 = 0, so the model cannot tell
the S/B2^2 term from the E[b Z^2] term. b = (6, 2, -1 x 8) (mean 0, B2 4.8, B3 21.6) separates them: the predicted bracket is
0.4045 at beta1 = 0. Exact (laplace_exact_bvec.py, the second audit's solver with b as an argument, 300 nodes,
next_order_bvec3_exact.txt) against predicted (next_order_bvec.py), as (x*/x0 - 1)/d:

    b1 = 0:   d 0.01 0.3557 / 0.4045,  0.005 0.3809,  0.002 0.3952,  0.001 0.3999; Richardson on the last two 0.4046
    r = 0.1:  d 0.004 0.6374 / 0.6493,  0.002 0.6482 / 0.6541,  0.001 0.6536 / 0.6564

The gaps are 4.7 d and 3 d, linear in d, so the limit is the formula's in both families.

## The next-order term with eps > 0 (20 Oct 2026 03:0x)

m/(sqrt(v) + eps) = (m/(s+eps)) psi(y) with psi(y) = (s+eps)/(s sqrt(y) + eps), s = sqrt(V). The bookkeeping of the eps = 0 section
goes through with psi's derivatives at 1, p1 = -r/2, p2 = s(eps+3s)/(4(eps+s)^2), p3 = -3s(eps^2+4 eps s+5s^2)/(8(eps+s)^3),
r = s/(s+eps), in place of -1/2, 3/4, -15/8:

    x*/x0 = 1 + d [ r K - (p2/4) S/B2^2 - (p2/r)(K2/K) E[b Z^2]/(B2 B3) - (p3/(2r)) S/B2^2 ] + O(d^2),   x0 = r d K B3/(2 B2).

At beta1 = 0 the bracket is 1, 0.306, -0.167, -0.427 at eps 0, 1, 3, 10 on the test model, and 0.405, -0.132, -0.403, -0.507 on
b = (6, 2, -1 x 8): eps turns the correction negative, so x0 r overstates the limit point slightly once eps is comparable to sqrt(V).

Exact check (next_order_eps.py). 1/(sqrt(v) + eps) = int_0^inf k(u) e^(-uv) du with k(u) = (pi u)^(-1/2)[1 - eps sqrt(pi u)
erfcx(eps sqrt(u))] (from 1/(a+eps) = int e^(-t(a+eps)) dt and the subordinator identity e^(-t sqrt(v)) = int t/(2 sqrt(pi))
u^(-3/2) e^(-t^2/(4u)) e^(-uv) du); quadrature reproduces 1/(sqrt(v)+eps) to 1e-11 (next_order_eps_kernel_check.txt). Under iid
sampling e^(-uv) factorizes over lags, so the second audit's exact solver carries over with its weight multiplied by the bracket of
k; at eps = 0 it reproduces that solver's 1.000998 and 1.001352. Exact against predicted, (x*/x0 - 1)/d (next_order_eps_runs.txt):

    test model   eps 1  b1 0     d 0.002 0.2966  d 0.001 0.3011   predicted 0.3056   (Richardson 0.3056)
                 eps 1  r 0.1    0.5976  0.6027                   0.6021 / 0.6049
                 eps 3  b1 0     -0.1750 -0.1708                  -0.1667
                 eps 3  r 0.1    0.0737  0.0790                   0.0795 / 0.0819
                 eps 10 b1 0     -0.4320 -0.4293                  -0.4267
                 eps 10 r 0.1    -0.2389 -0.2350                  -0.2348 / -0.2330
    three-valued eps 3  b1 0     -0.4090 -0.4061                  -0.4032
                 eps 3  r 0.1    -0.2375 -0.2334                  -0.2326 / -0.2310

(with momentum the predicted value moves with d at fixed r; the two printed are at d 0.002 and 0.001). Every gap halves when d
halves. Audit 1: agent C (AUDIT_NEXT_ORDER_agent_C.md, 20 Oct 03:0x), CONFIRMED: p1-p3 by sympy, k(u) checked
analytically, exact x* by the kernel-free Taylor route matching every row. Audit 2: agent A (audit_A/AUDIT_NEXTORDER_EPS_agent_A.md, 20 Oct 03:2x, push 37df8873), CONFIRMED:
p1-p3 and the solve by hand, the kernel re-derived, its own exact route (trapezoid in log u, eps_exact_logu.py) matching all 12
rows to 3e-9. Two independent audits: the eps > 0 coefficient counts as verified. Not covered by either: the next order under reshuffling, a rigorous eps > 0 iid remainder, the vector case.

## The next-order term, random reshuffling, beta1 = 0, eps = 0 (20 Oct 2026 04:0x, verified: two audits, see the momentum section)

With g_i = x + b_i (mean b = 0), B_k = E b^k, Z = b^2 - B2, T = E[b Z^2], K = K_rr(n, 0, beta2) and x0 = d K B3/(2 B2), at
fixed n as d = 1 - beta2 -> 0,

    x*/x0 = 1 + d (K - T/(8 K B2 B3)) + O(d^2) = 1 + d (1/2 - T/(4 B2 B3)) + O(d^2).

Derivation, from the reshuffling remainder lemma: 0 = x - (d K/2) C/V + (3/8) Q2 + (3/8) X + E[g r] with C = 2 x B2 + B3 and
V = x^2 + B2. Since x = O(d), C/V = B3/B2 + 2x + O(d^2), X = O(x d^2) and E[g r] = O(d^3). In Q2 set x = 0 and beta = 1
(s1 = s2 = p), at a cost of O(d^3). Because sum_b Z_b = 0, M0l = Mjj = -T/(n-1) and Mjl = 2T/((n-1)(n-2)). The averages
over p are (n-1)/2 for p and (n-1)(n-2)/3 for p(p-1), so the bracket averages to T (1 - 3/2 + 2/3) = T/6. That leaves
x (1 - d K) = d K B3/(2 B2) - (3/8) d^2 T/(6 B2^2). Under iid sampling the same bracket is T, not T/6, and the long lag sum
adds the S = Var(b^2) term of the iid formula. Under reshuffling each earlier epoch sums Z to zero, so there is no S term at
this order.

Checks (next_order_rr.py, next_order_rr_runs.txt):

- The bracket identity, brute-forced over all permutations at n = 5, 6, 7 with random b, agrees with T/6 to 5e-16.
- Against exact roots from agent A's Laplace route (audit_A/rr_exact.py, no Taylor step), on the test model
  b = (9, -1 x 9), where B2 = 9, B3 = 72, T = 4608 and the limit coefficient is -23/18 = -1.277778:

| beta2  | (x*/x0 - 1)/d, exact | gap to the K-form, over d |
|--------|----------------------|---------------------------|
| 0.9999 | -1.27745             | -5.08                     |
| 0.9995 | -1.27615             | -5.07                     |
| 0.999  | -1.27453             | -5.07                     |
| 0.998  | -1.27133             | -5.05                     |
| 0.995  | -1.26199             | -5.00                     |

- The gap is flat in d, so what remains is O(d^2). Extrapolating the exact column linearly to d = 0 gives -1.27777, against
  -1.277778.

Scope: beta1 = 0, eps = 0, a_i = 1, and the regime where n d is small (K - 1/2 is about d (n+1)/6). Momentum: next section.

## The next-order term, random reshuffling with momentum, eps = 0 (20 Oct 2026 04:1x, verified: two audits)

Same notation, K = K_rr(n, beta1, beta2), x0 = d K B3/(2 B2). At fixed n and beta1, as d -> 0,

    x*/x0 = 1 + d (K - (3/4) T H/(K B2 B3)) + O(d^2),   H = (1/n) sum_{p=0}^{n-1} (1 - beta1^(p+1)) h(p),
    h(p) = 1 - 3p/(n-1) + 2p(p-1)/((n-1)(n-2)),   K -> K0 = (1/n) sum_p (1 - beta1^(p+1)) (1 - p/(n-1)).

At beta1 = 0, H = 1/6 and K0 = 1/2, which is the section above. Derivation, from the momentum remainder lemma: as before
0 = x - (d K/2) C/V + (3/8) Q + O(d^3), since the part with both Z lags in an epoch other than g's is f' = x times O(d^2). In Q take
x = 0 and beta2 = 1. A momentum lag in a full earlier epoch then has bracket c^2 [M00 + 2(n-1) M0l + (n-1) Mjj + (n-1)(n-2) Mjl]
= c^2 T (1 - 2 - 1 + 2) = 0, because that epoch sums Z to zero. A lag i <= p in the current epoch has bracket c^2 T h(p), the same
for every i, and the momentum weights of those lags sum to 1 - beta1^(p+1). So Q = (d/B2)^2 T H.

Checks (next_order_rr_mom.py, next_order_rr_mom_runs.txt), test model B2 = 9, B3 = 72, T = 4608, n = 10:

- Q from the lemma's own lag sum at x = 0 divided by (d/B2)^2 T is H (1 + O(d)): ratios 1.0012 and 1.0027 at beta2 0.9999 for
  beta1 0.5 and 0.9.
- Against exact roots from agent A's route (audit_A/rr_exact_mom_eps.py, no Taylor step):

| beta1 | limit coefficient | (x*/x0 - 1)/d exact at beta2 0.9999 / 0.9995 / 0.999 / 0.998 | gap to the K-form, over d |
|-------|-------------------|----------------------------------------------------------------|---------------------------|
| 0.3   | -1.044874         | - / -1.04283 / -1.04081 / -                                    | -2.90                     |
| 0.5   | -0.814764         | -0.81426 / -0.81229 / -0.80984 / -0.80495                      | -0.66 to -0.71            |
| 0.9   | -0.156625         | -0.15586 / -0.15282 / -0.14901 / -0.14138                      | 6.19 to 6.24              |

- The gap is flat in d at each beta1, so what remains is O(d^2). Extrapolating the exact column linearly from beta2 0.9999 and
  0.9995 to d = 0 gives -0.81475 (beta1 0.5) and -0.15662 (beta1 0.9), against -0.814764 and -0.156625.

At beta1 0.3 the exact roots at beta2 0.9995 and 0.999 extrapolate to -1.04485 (agent A).

Audit 1: agent A (audit_A/AUDIT_NEXTORDER_RR_MOM_agent_A.md, 20 Oct, push cf490b48), CONFIRMED: H
re-derived by hand from the three-slot permutation moments, and by exact enumeration at n = 6 over current-epoch and earlier-epoch
permutations, E/T = H to 12 digits at beta1 0, 0.5, 0.7, 0.9. Audit 2: agent C
(audit_C/AUDIT_RR_NEXT_ORDER_agent_C.md, push 63be44e7), CONFIRMED for every beta1 >= 0: M0l, Mjj, Mjl, the zero
bracket of a full earlier epoch, h(p) and K0 re-derived by hand, and an independent exact solver with two special samples
(rr_exact_two_special.py) on a second model, b = (6, 2, -1 x 8), where the limits -0.880787, -0.541022, -0.087858 at beta1 0, 0.5,
0.9 are reproduced by extrapolation to 4e-6 with gaps flat in d. On that model an S term would be (3/4) S/B2^2 = 3.55 and none
appears. With two audits, this term and its beta1 = 0 case count as verified.

Scope: eps = 0, a_i = 1, n d small. The O(d^2) term grows with beta1 (6.2 d at beta1 0.9 against -0.7 d at 0.5), so at
beta1 = 0.9 and beta2 = 0.99 the formula is off by about 0.06 in the coefficient. eps > 0: next section.

## The next-order term, random reshuffling with momentum and eps > 0 (20 Oct 2026 04:2x; verified: audit 1 agent A, audit 2 agent C AUDIT_RR_NEXT_ORDER_EPS, see the 05:2x section)

With s = sqrt(B2), r = s/(s + eps), p2 = s(eps + 3s)/(4(eps + s)^2) (the second derivative at 1 of
psi(y) = (s + eps)/(s sqrt(y) + eps), as in the eps section for iid sampling), H and K as in the section above, and
x0 = r d K B3/(2 B2):

    x*/x0 = 1 + d (r K - p2 T H/(r K B2 B3)) + O(d^2).

Derivation: the eps lemma under reshuffling gives 0 = x - (r/2) d K C/V + (p2/2) Q + O(d^3) with the same Q = (d/B2)^2 T H as at
eps = 0. r and p2 depend on x only through V = x^2 + B2, so only at O(d^2). Under iid sampling the S = Var(b^2) terms come from
E[(y-1)^2] = O(d) over the long lag window; under reshuffling E[(y-1)^2] is O(d^2), because each earlier epoch sums Z to zero, and
they drop out as they do at eps = 0. eps = 0 gives r = 1, p2 = 3/4 and the momentum formula above.

Check (next_order_rr_eps.py, next_order_rr_eps_runs.txt): 18 exact roots from audit_A/rr_exact_mom_eps.py at beta1 0, 0.5,
0.9, eps 1 and 10, beta2 0.9999, 0.9995, 0.999. At each (beta1, eps) the gap between the exact (x*/x0 - 1)/d and the formula,
divided by d, is flat in d: about -4.9 (beta1 0, eps 1), -3.4 (0, 10), -1.4 (0.5, 1 and 10), 4.1 (0.9, 1), 1.5 (0.9, 10). So what
remains is O(d^2). The rows at beta2 0.9999 wobble by up to 0.2 in that ratio, which is the solver's precision divided by d^2.
Example: beta1 0.9, eps 10, the exact values -0.11487 / -0.11406 / -0.11301 against the formula -0.11505 / -0.11482 / -0.11454.

Audit 1: agent A (audit_A/AUDIT_NEXTORDER_RR_EPS_agent_A.md, push 8cbf6228), CONFIRMED: psi'(1) = -r/2
and psi''(1) = p2 by hand and by finite differences; exact roots at points not run here, eps 3: beta1 0.3 extrapolates to
-0.773107 against the limit -0.773113, beta1 0.7 to -0.393312 against -0.393316. A second audit is needed.

Scope: a_i = 1, n d small, scalar. With this section every case of the scalar law has its next-order term: iid and reshuffling,
with and without momentum, eps = 0 and eps > 0.

## Prior work (literature check, 20 Oct 03:4x; not exhaustive)
The frozen-x field whose zero is x* here is the "Adam vector field" of Dereich, Jentzen and Kassing (arXiv 2511.04622, Def. 1.3):
fixed beta1, beta2, vanishing step, the iterates track its flow and a convergent limit is one of its zeros. They state that its zeros
can differ from the critical points but give no formula or example; their Lemma 4.3 shows that, under noise whose third moment
vanishes at the critical set, zeros near that set are critical points, which is consistent with x* being driven by m3. Zhang, Chen,
Shi, Sun and Luo (arXiv 2208.09632, Thm 3.1) bound the neighbourhood reached under reshuffling by a multiple of the gradient
variance D0 and do not locate the limit. Malladi et al. (arXiv 2205.10287) work in the SDE scaling (1 - beta2) ~ eta^2, a different
regime, and assume a bounded third moment. Heilman and Mohanty (arXiv 2607.03519) concern regret. None of these states
x* = (1 - beta2) K m3/(2 abar V0) or its next-order term; a search of the stochastic-approximation literature on Adam with fixed
beta2 (Barakat-Bianchi 1810.02263 take 1 - beta proportional to the step) found nothing closer.

## Random reshuffling, unequal curvatures, eps = 0, any beta1: next-order term (20 Oct 05:1x; verified by two audits, see the 05:5x status below)

Take g_i = a_i x + b_i with mean b = 0 and abar = E a. The RR lemma goes through unchanged, because it uses only the
gradient values. Two things move: f' = abar x, and the slope of C/V at x = 0, where C = E[g Z] = E g^3 - abar x V. The
quadratic term Q is taken at x = 0, where a drops out, so it is the same (d/B2)^2 T H. With
c1 = (3 E[a b^2] - abar B2)/B2 - 2 B3 E[a b]/B2^2 (c1 = 2 when a = 1):

    x0 = d K B3 / (2 abar B2),     x*/x0 = 1 + d ( K c1/(2 abar) - (3/4) T H/(K B2 B3) ) + O(d^2).

Check (next_order_rr_a.py, next_order_rr_a_runs.txt): exact roots from audit_A/rr_exact_mom_eps.py, changing
only g_s = a_s x + 9 and g_o = a_o x - 1. Pairs (a_s, a_o) = (3, 1), (1, 2), (0.5, 1.5), (4, 0.5), giving c1 = 4, 3, 2, 4.5,
with beta1 0/0.5/0.9 and beta2 0.9999/0.9995/0.999. At every pair and beta1, gap/d is flat in d (for example (3,1) beta1 0:
-5.77, -5.81, -5.81; (4,0.5) beta1 0.5: -1.30, -1.35, -1.34), so the O(d) coefficient is exact and the remainder is O(d^2).
At (4, 0.5), beta1 0.9 the coefficient changes sign (beta2 0.9999: exact +0.0935, predicted +0.0928; gap/d 6.21, 6.18, 6.20), and the formula follows it. 36 rows, all flat.

## RR next-order term with eps > 0: VERIFIED (20 Oct 05:2x)

Second audit: agent C, rows/T354/audit_C/AUDIT_RR_NEXT_ORDER_EPS_agent_C.md (push 5ab4bd84). It derives
psi'(1) = -r/2 and psi''(1) = p2 by hand and recomputes exact roots on a different model, b = (6, 2, -1 x 8), at eps 1 and 10 and
beta1 0/0.5/0.9. All six limits match to 2e-6, gap/d is flat, and the iid S term is ruled out. With agent A's
8cbf6228 that is two independent audits. Every scalar next-order term is now verified, apart from the a_i case above (candidate).

Unequal-curvature term, first audit (20 Oct 05:2x): agent A, rows/T354/audit_A/AUDIT_RR_CURV_agent_A.md.
By hand, h sums to zero over each epoch, so a enters the linear term only through C and the mean of m; the x-parts of Q are
O(d^3). Exact check on three other models (n 5, b (4, -1 x 4), a (2,1) and (0.5,2); n 6, b (-5, 1 x 5), a (1.5,0.5), negative
skew), beta1 0/0.5/0.9: gap/d is flat to 0.01 in all 9 rows. Not covered: eps > 0, three-valued b. One audit; a second is wanted.

## Random reshuffling, unequal curvatures, eps > 0: next-order term (20 Oct 05:4x; verified by two audits, see 06:04 below)

With eps > 0 and unequal a_i the stationary V depends on x through E[a b], so r = s/(s + eps), s = sqrt(V), has a slope at
x = 0 that the a = 1 case did not need (there E[a b] = E b = 0). Writing r1 = eps E[a b]/(s (s + eps)^2), s = sqrt(B2):

    x0 = r d K B3 / (2 abar B2),
    x*/x0 = 1 + d ( K (r c1 + r1 B3/B2)/(2 abar) - p2 T H/(r K B2 B3) ) + O(d^2),

with p2 = s(eps + 3s)/(4 (eps + s)^2) and c1 as in the eps = 0 section. At eps = 0, r = 1 and r1 = 0 and this is the eps = 0
formula; at a = 1 it is the verified eps > 0 formula.

Check (next_order_rr_a_eps.py, next_order_rr_a_eps_runs.txt): exact roots as before, pairs (3, 1) and (4, 0.5), eps 1 and 10,
beta1 0 and 0.9, beta2 0.9999/0.9995/0.999, 24 rows. gap/d is flat in d in every group (for example (3,1) eps 1 beta1 0: -5.53,
-5.59, -5.59; (4,0.5) eps 10 beta1 0.9: 1.75, 1.52, 1.52), so the O(d) coefficient is exact. The same formula without r1 is off
by 0.04 to 0.15 in every row, not in proportion to d, so the r slope is needed. At (4, 0.5), eps 1, beta1 0.9 the coefficient is
positive (+0.091 exact, +0.091 predicted). The beta2 0.9999 rows sit a little off the other two (-5.53 against -5.59), as they did
in the verified a = 1 eps > 0 rows (-4.91 against -4.97); x*/x0 is printed to 9 decimals, so at d = 1e-4 gap/d
is only good to about 0.1. Not yet covered: three-valued b, beta1 0.5. agent C's running a_i audit (audit_C/
rra_runs.txt) also prints this formula's prediction ("withr1") on b = (6, 2, -1 x 8); that is their check, not yet written up.

Unequal curvatures, status (20 Oct 05:5x): agent C's audit (audit_C/AUDIT_RR_CURVATURE_agent_C.md, push
a9724714) re-derives c1, r1 and the Q term by hand and computes exact roots on b = (6, 2, -1 x 8) with three curvature vectors, eps
0 and 1, beta1 0 and 0.9: gap/d is flat and the three-point intercept is at most 3e-6 in all twelve families; without r1 the eps 1
rows are off by up to 0.12. With agent A's audit, the eps = 0 unequal-curvature term is VERIFIED (two audits). The eps > 0
unequal-curvature term had one audit at this point; its second (agent A, 06:04) is below. Not covered by either: beta1 0.5, a_i varying within the bulk.

Vector case, shared Hessian, exact reduction. With g_i = H x + b_i the drift of coordinate j depends on x only through (H x)_j, so
D_j(x) = D_scalar,j((H x)_j) and H x* = u*, u*_j the scalar limit for coordinate j's noise b_{.j}, to every order in d and for every
beta1 and eps. Every verified a = 1 scalar term therefore holds coordinate by coordinate after one linear solve.

Unequal curvatures with eps > 0: VERIFIED (06:04). Second audit: agent A, audit_A/AUDIT_RR_CURV_EPS_agent_A.md
(push 96b239d0): r1 re-derived as dr/dx at 0; exact roots in twelve families on two-valued b (n 5 and 6, B3 and E[ab] of both
signs), eps 1, 3 and 10, beta1 0, 0.5 and 0.9, beta2 0.9995/0.999/0.998; gap/d flat (spread at most 0.012); without r1 off by
0.006-0.037, not in proportion to d. With agent C's audit (a9724714, three-valued b) that is two independent audits. Every
scalar next-order term under reshuffling, a_i and eps included, is now verified. Not covered by any audit: a_i varying within the bulk.

Vector case, per-sample Hessians H_i: VERIFIED (candidate 20 Oct 06:1x, two audits by 07:0x). g_i(x) = H_i x + b_i in R^d, coordinatewise Adam, E b = 0. At
frozen x coordinate j's moments are built from g_{.j} alone, so its drift is the scalar drift at the values g_{ij}(x) = (H_i x)_j +
b_ij; the coupling enters through x only. Expanding the scalar next-order terms with a_i replaced by the row (H_i)_{j.} gives, per
coordinate j (s_j = sqrt(B2_j), r_j = s_j/(s_j + eps), p2_j = s_j(eps + 3 s_j)/(4 (eps + s_j)^2), m_j = B3_j/B2_j),

    (Hbar x)_j - (d K/2) [ r_j m_j + r_j (M x)_j + m_j (R x)_j ] + (p2_j/2) d^2 T_j H(beta1)/B2_j^2 = 0,
    M_jk = (3 E[b_j^2 H_jk] - Hbar_jk B2_j)/B2_j - 2 B3_j E[b_j H_jk]/B2_j^2      (c1 as a matrix),
    R_jk = eps E[b_j H_jk]/(s_j (s_j + eps)^2)                                       (r1 as a matrix),

a linear system for x* to O(d^2). For a shared H (H_i = H) M and R reduce to the scalar c1 and r1 times H, and this is the exact
shared-H reduction above. With a_i scalar and d = 1 it is the verified unequal-curvature term.

Check (vec_hi_rr.py, vec_hi_batch.sh, vec_hi_out/, vec_hi_rr_runs.txt): n = 10, one special sample and nine others, two coordinates,
so each coordinate is two-valued and audit_A/rr_exact_mom_eps.py gives its exact scalar drift; the exact 2-d root by chord
Newton (residual under 1e-16). Two models with non-commuting H_s, H_o (A: [[3,1],[1,2]] vs [[1,.3],[.3,1.5]]; B: [[.5,-.8],[-.8,3]]
vs [[1.5,.2],[.2,.8]], a negative coupling), (beta1, eps) in {(0,0), (0.9,0), (0,1), (0.9,1), (0.5,1)}, beta2 0.9995/0.999/0.998, 30 rows.
Statistic G_j = (x*_j - pred_j)/(x0_j d^2): flat in d means the O(d) relative term is exact. It is flat in every family, for
example A beta1 0 eps 0: [-4.918 -4.468], [-4.912 -4.461], [-4.899 -4.446]; B beta1 0.9 eps 1: [4.081 3.232], [4.094 3.245]; B beta1 0
eps 1: [-4.509 -5.282], [-4.501 -5.276], [-4.481 -5.260] (beta2 0.9995, 0.999, 0.998 in each list; the small drift is linear in d,
the O(d^3) term). The control with M = R = 0 ("noM") doubles each time d halves (A beta1 0 eps 0:
382.8, 768.5, 1539.9), so the coupling through H_i is needed and is right. Not covered: three or more coordinates, b with more than
two values per coordinate, a_i-type spread within the bulk. Wanted: two independent audits.
Audit 1 (20 Oct 06:5x): CONFIRMED by agent C, audit_C/AUDIT_VEC_HI_agent_C.md (push 15327545). They re-derived
M and R by hand and ran 30 exact roots on their own model: 3 coordinates, three-valued b per coordinate with B3 of both signs, and three
non-commuting H. G is flat, and noM doubles.
Audit 2 (20 Oct 06:4x): CONFIRMED by agent A, audit_A/AUDIT_VEC_HI_agent_A.md (push 1dcf02ed). By hand
the same M and R; own code (vec_three_valued.py), n = 6, three coordinates, two special samples so three values per coordinate,
non-commuting H, B3 of both signs; G flat across beta2 0.998/0.999/0.9995 at (beta1, eps) = (0,0), (0.5,1), (0.9,3).

## Every n: the reshuffling factor in closed form, and the law uniform in n(1 - beta2) (20 Oct 06:5x; the large-n rows verified by two audits, see below)

Everything above assumes n d small (d = 1 - beta2). With n = 50,000 and beta2 = 0.999, n d = 50, so the practical regime is the
other one. The leading law x* = d K_rr B3/(2 B2) never needed n d small: E[m (y-1)] = d K_rr C/V is exact at first order for every
n. What needed it was the remainder bound. Two pieces here.

K_rr in closed form (kclosed.py; it matches kfactor.K_rr's lag sum to 1.4e-11 over n 2..200, beta1 0/0.5/0.9, beta2 0.9..0.999).
With g = beta1 beta2 and G(z) = z (1 - z^n)/(1 - z),

    K_rr = n/(n-1) (1-beta1)/(1-g) - [ n - G(beta1) - G(beta2) + G(g) + g (1-beta1^n)(1-beta2^n)/(1-g) ] / (n (n-1) (1-beta2)).

At beta1 = 0 this is K_rr = 1 - beta2 [n d - (1 - beta2^n)] / (n (n-1) d^2): 1/2 + (n+1) d/6 + ... for small n d, and
1 - beta2/((n-1) d) + O(1/(n d)^2) for large n d, against the iid value 1. So reshuffling halves the residual when the v-window
is longer than an epoch and stops helping when the window is shorter: at n d = 5 it saves 16%, at n d = 50 about 2%.

Exact roots at large n (rr_exact_m2.py; rr_exact_m.py is the slow reference). The noise distribution is held fixed while n grows:
a tenth of the samples have b = 9 and the rest b = -1 (B2 = 9, B3 = 72 for every n divisible by 10). Each epoch's special slots are a
uniform random subset, so E e^(-u v) factorizes over epochs and each factor is a normalized elementary-symmetric mean, computed
by a stable recursion. An earlier epoch's factor is one universal function of u A beta2^lag, tabulated once. The solver gives
audit_A/rr_exact_mom_eps.py's n = 10 root to 12 digits, and the slow reference's root at n = 20, m = 2 likewise. beta1 = 0,
eps = 0, (x*/x0 - 1)/d with x0 = d K_rr B3/(2 B2):

    n d    d = 0.01          d = 0.005         d = 0.002
    0.1    -1.247 (n 10)     -1.225 (n 20)     -1.211 (n 50)
    0.5    -0.960 (n 50)     -0.932 (n 100)    -0.915 (n 250)
    1      -0.649 (n 100)    -0.618 (n 200)    -0.600 (n 500)
    2      -0.217 (n 200)    -0.188 (n 400)    -0.170 (n 1000)
    5      +0.333 (n 500)    +0.358 (n 1000)   +0.372 (n 2500)
    10                       (d = 0.005: +0.6416, n 2000, audit 1)
    20     +0.751 (n 1000, d = 0.02)   +0.792 (n 2000, d = 0.01)   +0.8086 (n 4000, d = 0.005, audit 1)
    50     +0.866 (n 2500, d = 0.02; d = 0.04 and 0.01 running)

At fixed n d the column settles as d falls, by an amount proportional to d. So x*/x0 = 1 + d c(n d) + O(d^2), where c is a bounded
function of n d alone. It rises from about -1.20 at n d = 0.1 (the verified small-n d coefficient on this model, -1.278, is its
n d -> 0 limit) and through zero near n d = 3. As n d -> infinity it should tend to +1, the verified iid coefficient at beta1 = 0
for two-valued b. Extrapolating linearly in d from the two smallest d gives c(5) = 0.381, c(10) = 0.662 and c(20) = 0.825 (agent C's audit; Richardson 0.823 at n d 20), so (1 - c) n d = 3.10, 3.38, 3.50. c tends to 1 like a/(n d), the same order as K_rr's own approach to 1, but a is still rising and is not pinned down; the n d = 50 row tests it. The relative error of the leading law is under 1.3 d at every n. With the iid K = 1 in place of K_rr, the
n d = 5 rows would be 19% off, against 0.2%.

eps = 1 at large n d (rr_exact_m2.py with eps 1, rrm_out/*eps1*.txt; x0 = r d K_rr B3/(2 B2), r = 3/4):

    n d    d = 0.01          d = 0.005         linear to d = 0    eps = 0, same extrapolation
    0.1                      -1.074 (n 20)                        (n d -> 0 limit -1.106 by the verified eps formula)
    1      -0.708 (n 100)    -0.686 (n 200)    -0.664             -0.59
    5      -0.105 (n 500)    -0.080 (n 1000)   -0.055             +0.38
    10     +0.060 (n 1000)

As n d grows the coefficient should tend to the verified iid value at eps = 1, 0.306 (against 1 at eps = 0). The distance to that
limit is 0.62, 0.61 and 0.58 times the eps = 0 distance at n d -> 0, 1 and 5, so eps mostly rescales the approach. It crosses zero
near n d = 7 instead of 3. With eps comparable to sqrt(V), x0 slightly overstates the limit point for every n d up to about 7.

Momentum at large n d (rr_exact_m3.py, rrm3_out/; eps = 0; x0 = d K_rr(beta1) B3/(2 B2) with K_rr's closed form at that beta1).
rr_exact_m3.py reproduces the n = 10 exact momentum roots to 10 digits and rr_exact_m2.py's rows at beta1 = 0.

    n d   beta1   d = 0.01          d = 0.005         linear to d = 0
    1     0       -0.649 (n 100)    -0.618 (n 200)    -0.587   (d = 0.002, n 500: -0.600)
    1     0.5     -0.545            -0.565            -0.585
    1     0.9     +0.052            -0.206            -0.464
    5     0       +0.333 (n 500)    +0.358 (n 1000)   +0.383
    5     0.5     +0.385            +0.384            +0.382
    5     0.9     +0.735            +0.572            +0.409

At beta1 = 0.5 the limit equals the beta1 = 0 limit to 0.002 at both n d. The momentum shift (beta1 row minus beta1 0 row, same d)
halves when d halves: 0.104, 0.053 (n d 1) and 0.052, 0.026 (n d 5) at beta1 0.5; 0.70, 0.41 and 0.40, 0.21 at beta1 0.9. So the
whole beta1 dependence beyond K_rr sits at order d^2 in x*/x0, with a coefficient that grows roughly like beta1/(1 - beta1) (shift/d
about 10 and 5 at beta1 0.5, about 75 and 41 at beta1 0.9, for n d 1 and 5): x*/x0 = 1 + d c(n d) + d^2 e(n d, beta1) + ..., with the
same c(n d) as at beta1 = 0. At beta1 0.9 the two-point extrapolation is not yet in its linear range (d/(1 - beta1) is 0.1 at d 0.01).
Test at n d 1, d 0.002 (n 500), with the prediction written before the result: -0.58 at beta1 0.5, and at beta1 0.9 between -0.45
(shift exactly proportional to d) and -0.36 (the two-point fit's 0.12 intercept is real). Result: -0.578 and -0.416 (beta1 0: -0.600).
The beta1 0.9 shift is 0.70, 0.41, 0.184 at d 0.01, 0.005, 0.002, so shift/d = 70, 82, 92: it vanishes with d, with a coefficient
near 100 = 11 beta1/(1 - beta1). The quadratic fit through the three d gives c(1) = -0.588, -0.588, -0.579 at beta1 0, 0.5, 0.9. So
c(n d) does not depend on beta1; momentum enters x*/x0 at order d^2 beta1/(1 - beta1), and only through K_rr at order d.

Audit 1 of the large-n rows: agent C (audit_C/AUDIT_LARGE_N_agent_C.md, pushes a852b8ea, e0fdfd4e), CONFIRMED: K_rr's closed form against the lag sum (1.4e-11) and Monte Carlo, and every cell of the table reproduced to its printed digit by an independent solver (rrm_indep.py). It corrected the rate: the first text read c(20) = 0.83 off the d = 0.02 root, outside the linear range, and stated 3.2/(n d). Audit 2: agent A, audit_A/AUDIT_RRM_agent_A.md (08:3x), CONFIRMED by Monte Carlo of the reshuffled stream itself, independent of the recursion both solvers share: every row within its error bar.

The remainder, uniform in n (20 Oct 07:3x; verified at eps = 0 and at eps > 0 by two audits each, the eps > 0 second one audit_A/AUDIT_EPSUNIF_agent_A.md; beta1 = 0, eps >= 0, a_i = 1). Fix the multiset b_1..b_n (mean 0) and
|x| <= rho < min |b_i|, so every g_i^2 >= gamma := (min |b_i| - rho)^2 > 0. Write V = E g^2, Z_i = g_i^2 - V (sum Z = 0),
eta = y - 1. The constants below depend on gamma/V, max |b|, max |Z|, and the population moments s2 = E Z^2, m4 = E Z^4, and never on n.

1. Since d sum_j beta2^j = 1, v is a convex combination of the g_i^2, so y lies in [gamma/V, max g^2/V]. On that interval
   psi(y) = (s + eps)/(s sqrt(y) + eps) equals its cubic Taylor polynomial at 1 up to |R| <= C eta^4.
2. Split eta = eta_c + eta_f. eta_c = (d/V) sum_{j=0..p} beta2^j Z at the slots of the current epoch up to position p; eta_f is the
   sum of one term eta_e per earlier epoch. The eta_e are independent of one another and of the current epoch, and each has mean 0.
3. Permutation moments (perm_moment4.py, exact in n, brute force at n = 5, 6). For S = sum_q a_q z_pi(q) with sum a = sum z = 0,
   A_k = sum a^k, P_k = sum z^k:
       E S^2 = A2 P2/(n-1),     E S^3 = n A3 P3/((n-1)(n-2)),
       E S^4 = [A2^2 (3 P2^2 (n^2-3n+3) - 3 P4 n(n-1)) + A4 (P4 n^2 (n+1) - 3 P2^2 n(n-1))] / (n (n-1)(n-2)(n-3)),
   so E S^4 <= 14 (s2^2 A2^2 + m4 A4) for n >= 4. Uncentred weights w cost nothing: sum z = 0 lets w be replaced by w - mean(w),
   with sum (w - mean)^2 <= sum w^2 and sum (w - mean)^4 <= 16 sum w^4. For the current epoch, A2 <= min(p+1, 1/d) and
   A4 <= A2. For the earlier epochs, the A2 sum to at most 1/(1 - beta2^2) <= 1/d.
4. Hence E eta^2 <= C d and E eta^4 <= C d^2. For eta_f, independence gives E eta_f^4 <= 3 (E eta_f^2)^2 + sum_e E eta_e^4.
5. The terms of sqrt(V)(s + eps) D / (s + eps), averaged over the position p:
   - E[g eta] = d K_rr (2 x B2 + B3)/V, exactly, from E[Z_pi(i) | pi(p)] = -Z_pi(p)/(n-1).
   - E[g eta^2] = x E eta^2 + E[b eta_c^2]: cross terms with eta_f vanish by independence, and E b = 0 at a uniform position.
     Expanding (Z_k + W)^2 by distinct-index sums, |E[b eta_c^2]| <= 8 |E[b Z^2]| (d/V)^2. The three pieces are bounded by 1, 2
     and 4 times |E[b Z^2]|, because each lag beyond the first costs 1/(n-1) and there are at most n - 1 lags.
   - E[g eta^3] = x E eta^3 + E[b eta_c^3] + 3 E[b eta_c] E eta_f^2. The last term is O(d) O(d). For the middle term, condition on
     pi(p): W = M + W0 with |M| <= max|Z| and W0 a centred permutation sum over the other n - 1 values. E[W0^3] = O(sum w^3) =
     O(1/d) by the E S^3 formula, so E[b (Z_k + W)^3] = O(1/d) and E[b eta_c^3] = O(d^2).
   - E[g R] <= C E eta^4 = O(d^2).
So D(x) sqrt(V) = x - (d K_rr/2)(2 x B2 + B3)/V + x e1(x) + e2(x), with |e1| <= C d and |e2| <= C d^2 for all |x| <= rho and
all n >= 4; e1 collects the x E eta^k terms ((3/8) x E eta^2 is of order x d), e2 the b terms and E[g R]. At a zero the bracket
x (1 - d K_rr B2/V + e1) = d K_rr B3/(2V) - e2 has 1 - O(d) in front, so |x*| <= C d, x* e1 = O(d^2), and
x*(1 - d K_rr B2/V) = d K_rr B3/(2V) + O(d^2): x* = x0 (1 + O(d)) uniformly in n. A zero exists by the sign change at x0 +- C' d^2.
With eps > 0 the same steps run with psi's Taylor coefficients p1, p2/2, p3/6 (p1, p2, p3 the derivatives above) in place of
-1/2, 3/8, -5/16. Audit 1 of the eps > 0 version: agent C (audit_C/AUDIT_EPS_agent_C.md), conclusion confirmed. In the E[b eta_c^3] step,
E[(c + W0)^3] = c^3 + 3 c E W0^2 + E W0^3 and both W0 moments are O(1/d). E[b eta_c^2] is exactly c_n(beta2) E[b Z^2] (d/V)^2 with
c_n = avg_p [1 - (2 sum_j beta2^j + sum_j beta2^(2j))/(n-1) + 2 sum_{j != l} beta2^(j+l)/((n-1)(n-2))], j, l in 1..p, |c_n| <= 6.
Audit 1: agent C (audit_C/AUDIT_UNIFORM_agent_C.md, push a1c56d60), conclusion confirmed; the exact solver at
x = 0.1, n d = 1 gives E2 = 0.365 x d + 2.46 d^2, against (3/8) E eta^2/d = 0.371-0.376 computed from the permutation formula. This is the
large-n version of the reshuffling lemma; the deterministic bound in remainder_rr.py grows with n d. Momentum: see the next paragraph. Audit 2: agent A (audit_A/AUDIT_UNIFORM_agent_A.md, push
75953314), confirmed, with the same correction to E2. Two audits at eps = 0: verified. The eps > 0 version has not been re-derived by either.


Momentum, uniform in n (20 Oct 07:5x; verified at fixed beta1 by two audits: agent A, audit_A/AUDIT_MOMENTUM_agent_A.md, the proof step by step, with two corrections now in the text; agent C, audit_C/AUDIT_MOMENTUM2_agent_C.md (push 33c36e9c), numerical, an independent momentum solver on a three-valued b; eps >= 0, a_i = 1, any fixed beta1 in [0, 1)). The numerator is
m_k = sum_{i>=0} w_i g_{k-i} with w_i = (1 - beta1) beta1^i, a convex combination, and the denominator is unchanged, so
D_m(x) = sum_i w_i E[g_{k-i} psi(y_k)] / (s + eps) and the remainder argument above runs lag by lag with the same constants.
For a fixed lag i, write g_{k-i} = x + b_sigma, sigma the slot at that lag. Its marginal is uniform, so E b_sigma = 0.
- Lag inside the current epoch (i <= p). sigma is one of eta_c's slots, with weight beta2^i <= 1 in eta_c. Conditioning on pi(sigma)
  gives eta_c = (d/V)(beta2^i Z_sigma + M + W0) with |M| <= max |Z| and W0 a centred permutation sum over n - 1 values, as in the
  beta1 = 0 step. E[b_sigma eta_c^2] = O(d^2) and E[b_sigma eta_c^3] = O(d^2) follow verbatim, and eta_f is independent of b_sigma.
- Lag in an earlier epoch e. sigma is a slot of eta_e only. eta_c, and every eta_f' with f' != e, are independent of (b_sigma, eta_e)
  and have mean 0, so E[b_sigma eta^2] = E[b_sigma eta_e^2], E[b_sigma eta^3] = E[b_sigma eta_e^3] + 3 E[b_sigma eta_e] E(eta - eta_e)^2,
  and the same conditioning on pi(sigma) inside epoch e gives O(d^2) for each. The bound on eta_e's weight sum alone gives only O(d); the
  step needs the beta1 = 0 cancellation: E[W0^2 | sigma] depends on the value at sigma only through a 1/(n - 1) term and E b = 0 removes
  the rest, so |E[b_sigma eta_e^2]| <= 6 |E b Z^2| (d/V)^2 for weights in [0, 1] (audit 1; largest ratio 0.49 over 180 enumerated
  draws at n = 5, 6, 7). The cubic term is fine with the crude bound, (d/V)^3 O(1/d) = O(d^2).
- The first-order terms sum to sum_i w_i E[g_{k-i} eta] = d K_rr(beta1) (2 x B2 + B3)/V, which is the lag sum K_rr was defined by, and
  the x E eta^k terms are the same as at beta1 = 0 because sum w_i = 1.
So D_m(x) sqrt(V) = x - (d K_rr(beta1)/2)(2 x B2 + B3)/V + x e1 + e2, with |e1| <= C d, |e2| <= C d^2, C independent of n and of beta1,
and x* = x0(beta1) (1 + O(d / K_rr(beta1))) uniformly in n: e2 is O(d^2) in absolute terms while x0 = O(d K_rr), so the relative
error carries 1/K_rr (agent A, 20 Oct 08:1x). For fixed beta1 < 1 this is O(d) uniformly in n as long as inf_n K_rr(n, beta1) > 0;
audit 1 finds inf_n K_rr at n = 2, about (1 - beta1)/2 (n -> infinity: (1 - beta1)/(1 - beta1 beta2)), so x*/x0 = 1 + O(d/(1 - beta1))
uniformly in n. It is not shown uniform as beta1 -> 1, where K_rr -> 0 (0.0137 at beta1 0.999, n 100, d 0.01), although the exact solver still keeps
(x*/x0 - 1)/d bounded there (1.15 at 0.999; 0.99 at d 0.05, beta1 0.999, where d/K_rr = 17.6), so e2 seems to shrink with K_rr. A proof
uniform in beta1 would need |e2| <= C d x0; open. This is consistent with the rows above: the beta1 dependence of x*/x0 beyond K_rr is
O(d^2) at fixed beta1, with a d^2 coefficient growing like beta1/(1 - beta1).

Uniform in beta1 (20 Oct 09:5x; VERIFIED, two audits: agent A audit_A/AUDIT_B1UNIF_agent_A.md and agent C
audit_C/AUDIT_UNIFORM_B1_agent_C.md, both CONFIRMED; eps >= 0, a_i = 1, every beta1 in [0, 1); uniform_b1/transposition_check.py).
The claim: |e2| <= C d^2 K_rr(beta1) = C' d x0(beta1), with C free of n and beta1, so x*/x0 = 1 + O(d) uniformly in n and beta1 when B3 != 0.
1. The b part of the numerator is m - x = sum_e sum_{q in e} w_q b_pi_e(q), one sum per epoch (the current epoch's unseen slots carry
   w = 0), with w_q = (1 - beta1) beta1^lag(q). eta = sum_e sum_q a_q Z_pi_e(q) with a_q = (d/V) beta2^lag(q) (0 on unseen slots).
   In each epoch w and a are both nonincreasing in the lag: they are comonotone, so (w_q - w_r)(a_q - a_r) >= 0 for every pair.
2. e2 is the sum over epochs of T_e = E[(sum_q w_q b_pi(q)) F(eta)], F(eta) = psi(1 + eta) - 1 - p1 eta (everything in psi past first
   order, the Taylor remainder included, so E[g R] needs no separate step). Since sum_q E[b_pi(q) F] = 0, the sum is
   (1/2n) sum_{q,r} (w_q - w_r)(X_q - X_r) with X_q = E[b_pi(q) F]. Swapping pi(q) and pi(r) preserves the law and changes eta by
   -(a_q - a_r)(Z_pi(q) - Z_pi(r)), so
       T_e = (1/4n) sum_{q,r} (w_q - w_r)(a_q - a_r) E[ Db DZ  int_0^1 F'(eta - t (a_q - a_r) DZ) dt ],
   Db = b_pi(q) - b_pi(r), DZ = Z_pi(q) - Z_pi(r). This is exact: the enumeration over all orders at n = 5, 6 matches it to 1e-9 or better.
3. The expectation is O(d), uniformly in q, r, n and beta1. F'(xi) = psi''(1) xi + O(xi^2), and y stays in [gamma/V, max g^2/V], where
   psi is smooth. xi = eta - t (a_q - a_r) DZ with |a_q - a_r| <= d/V. E[Db DZ eta]: the other epochs are independent with mean 0 and
   drop out; inside the epoch, a_q Z_pi(q) and a_r Z_pi(r) are O(d), and given pi(q), pi(r) the other slots average to
   -(Z_pi(q) + Z_pi(r))/(n - 2) with total weight at most (n - 2) d/V. So E[Db DZ eta] = O(d), and E xi^2 <= 2 E eta^2 + O(d^2) = O(d).
4. Hence |T_e| <= C d S_e, S_e = (1/n) sum_{q,r} (w_q - w_r)(a_q - a_r) >= 0. The first-order term is the same identity with F' = 1:
   E[Db DZ] = (2n/(n - 1)) E[bZ] for q != r, so sum_e E[(w.b)_e eta] = (n/(2(n - 1))) E[bZ] sum_e S_e, E[bZ] = 2 x B2 + B3. That is the
   lag sum d K_rr(beta1)(2 x B2 + B3)/V, so d K_rr/V = (n/(2(n - 1))) sum_e S_e: K_rr >= 0 for every beta1, and
   |e2| <= C d sum_e S_e <= C'' d . d K_rr. The relative error is O(d) with no 1/K_rr. The x E[psi] terms (e1) do not involve beta1.
The step at beta1 = 0 that used the 1/(n - 1) cancellation is the case w = (1, 0, 0, ...) of this one. Check (uniform_b1/run_eps0.txt,
run_eps1.txt): T/(d S) at d 0.1, 0.01, 0.001 and beta1 0 to 0.9999 on three b's stays in [-0.65, 0.38] and converges as beta1 -> 1 while T
and S each fall like (1 - beta1)^2; for example -0.2143 at every beta1 >= 0.99, d 0.001. This also explains audit 2's table: (x*/x0 - 1)/d
levels off near 1.1 as beta1 -> 1 instead of growing like 1/K_rr.
Exact solver near beta1 = 1 (rr_exact_m3.py, n 20, beta2 .95, eps 0; prediction written first in uniform_b1/PREDICTION.txt):
(x*/x0 - 1)/d = 0.99287 at beta1 .9999 (K 2.83e-4), against 0.988 at .998 and 0.991 at .999 (K 2.85e-3). A 1/K_rr law would have multiplied it by ten from .999.
Further out (rr_exact_m3b.py, 20 Oct 10:4x: same solver, the epoch loop stops once every c is under the tilt grid, where the tail
is exact; it reproduces the .9999 root to 6e-11): 0.99308 at beta1 .99999 (K 2.83e-5) and 0.99304 at .999999 (K 2.83e-6). K_rr
falls a hundredfold from .9999 and the coefficient moves in the fourth digit. Files uniform_b1/m3_n20_b1_0.99999.txt, _0.999999.txt.
At eps = 1 the same picture holds on the exact root (agent C, 03da30a3, audit_C/AUDIT_UNIFORM_B1_agent_C.md section
"eps = 1 at beta1 -> 1", r3meu_out/): b (6, 2, -1), n d = 1, (x*/(r x0) - 1)/d between 0.30 and 0.46 for beta1 .99 to .9999 while K_rr
falls a hundredfold; the .9999 row still rises with falling d (0.426, 0.448, 0.457; Richardson order 1 gives 0.466).

c(n d) in closed form (20 Oct 08:0x; verified by two audits: agent C, audit_C/AUDIT_CCLOSED_agent_C.md (push 8b1be7ec), numerical, on a three-valued b with r1 != r2; agent A, audit_A/AUDIT_CCLOSED_agent_A.md (push fe6952e4), k, Q, cb and avg[k Q] re-derived by hand from the permutation moments, the exact slot sums converging to the integrands at rate 1/n, the cubic term by Monte Carlo; beta1 = 0, eps = 0, a_i = 1; c_closed.py, c_closed_sym.py). At x = O(d)
keep the O(d^2) terms of sqrt(V) D = E[g (1 - eta/2 + (3/8) eta^2 - (5/16) eta^3)] + O(d^3):
    x [1 - d K B2/V + (3/8) E eta^2] - d K B3/(2V) + (3/8) E[b eta^2] - (5/16) E[b eta^3],
so c = K - (3/8) E eta^2/d + (2 B2/(d^2 K B3)) [ (5/16) E[b eta^3] - (3/8) E[b eta^2] ]. In the limit n -> infinity at fixed s = n d,
with theta = p d uniform on [0, s), lag weights e^(-tau), the current epoch on tau in [0, theta] and same-epoch covariance -z2/(n-1):
    k(theta) = 1 - (1 - e^-theta)/s                        K = avg k = 1 - 1/s + (1 - e^-s)/s^2
    E eta^2 = d r1 Q(theta),  Q = 1/2 - (1 - e^-theta)^2/s - e^(-2 theta) tanh(s/2)/s
    E[b eta^2] = (d/V)^2 E[bZ^2] cb,  cb = avg [1 - 2(1 - e^-theta)/s - (1 - e^(-2 theta))/(2s) + 2(1 - e^-theta)^2/s^2]
                (the large-n limit of agent C's exact c_n(beta2))
    E[b eta^3] = 3 d^2 (B3/V) r1 avg[k Q]   (3 E[b eta_c] times the variance of the rest of eta, where conditioning on the current
                slot makes E[b eta_c] = (d/V) k(theta) E[bZ] through the cross term 3 E[b M W0^2]; E[b W0^3] and the remaining
                conditioning terms are O(1) against O(1/d) and drop)
with r1 = z2/V^2 = (B4 - B2^2)/B2^2 and r2 = E[bZ^2]/(B2 B3). Hence
    c(s) = K - (3/8) r1 avg Q - (3/4) r2 cb/K + (15/8) r1 avg[k Q]/K   (elementary closed forms printed by c_closed_sym.py).
Checks. c(0+) = 1/2 - r2/4 = -1.278 on the 9/-1 model, the verified small-n d coefficient. c(infinity) = 1 + (3/4)(r1 - r2), the
verified iid coefficient (1 here, since r1 = r2 = 64/9 for two-valued b). In between, against the extrapolated exact rows:
    s       0.1      0.5      1        2        5        10       20       50
    c(s)   -1.201   -0.903   -0.588   -0.159   +0.381   +0.660   +0.823   +0.928
    rows   -1.20    -0.90    -0.588   -0.16    +0.381   +0.662   +0.823   +0.925
(n d 50: 0.7515, 0.8661, 0.9024 at d 0.04, 0.02, 0.01, n 1250, 2500, 5000, second-order Richardson 0.925; the d 0.01 root was
predicted at about 0.90 before it ran.)
And (1 - c) s -> 1 + 3 r1/8 = 3.667 (two-valued b), which is why the measured 3.10, 3.38, 3.50 kept rising: 1 from K, 3 r1/8 from
the variance terms. With r1 != r2, c tends to 1 + (3/4)(r1 - r2) instead, and it is (c(inf) - c(s)) s that tends to a constant in r1, r2.
Audit 1 checked the general form on a three-valued b: c(1e-4) = -0.88074 against 1/2 - r2/4 = -0.88079, c(1e4) = 0.40433 against
1 + (3/4)(r1 - r2) = 0.40451, and the exact rows to 1e-4 at n d 0.2, 1 and 2. At n d 5 the quadratic extrapolation (n to 1000) gives
+0.0766 against +0.0765; at n d 10 the linear one from two points gives +0.2311 against +0.2269, the overshoot the n d 5 curvature predicts. The same c holds at every fixed beta1: the momentum rows above on 9/-1, and on the three-valued b agent C's
audit_C/AUDIT_MOMENTUM2_agent_C.md (push 33c36e9c): at beta1 0.5, c = -0.4771 at n d 1 and -0.2267 at n d 2 against
-0.4775 and -0.2268; at beta1 0.9, n d 1, the order-4 Richardson value -0.4773 with the n 800 row (agent C, 98b3f9b0; order 3 gave -0.474).
eps > 0 in closed form (20 Oct 09:1x; verified by two audits: agent C, audit_C/AUDIT_CEPS_agent_C.md, at n d 1
on the three-valued b; agent A, audit_A/AUDIT_CEPS_agent_A.md, twelve Monte Carlo rows on 9/-1 and 6/2/-1; c_closed_eps.py; beta1 = 0, a_i = 1). The eta moments do not depend
on eps, and psi(y) = (sq + eps)/(sq sqrt(y) + eps), sq = sqrt(B2), has Taylor coefficients p1 = -r/2, p2/2 and p3/6 at 1 (r, p2, p3 as
in the eps section) in place of -1/2, 3/8 and -5/16. The same solve gives, with x0 = r d K B3/(2 B2),
    c(s) = r K - (p2/2) r1 avg Q - p2 r2 cb/(r K) - p3 r1 avg[k Q]/(r K).
At eps = 0 this is the formula above. Its limits are c(0+) = r/2 - p2 r2/(3 r), which is the verified reshuffling eps formula at n d -> 0
(-1.1065 on 9/-1 at eps 1), and c(inf) = r - p2 r1/4 - p2 r2/r - p3 r1/(2 r), which is the verified iid eps bracket (0.3056 there).
Against exact roots, eps 1, with each prediction written before its run (rrm_out/PREDICTIONS_eps1.txt, r3e_out/PREDICTION.txt):
    9/-1 (rr_exact_m2.py)         n d 1:  -0.708, -0.686 at d .01, .005; linear -0.664; closed form -0.6646
                                  n d 5:  -0.105, -0.080; linear -0.055; closed form -0.0568
                                  n d 10: +0.0602, +0.0854 (n 1000, 2000; predicted 0.084); linear +0.1106; closed form +0.1091
                                  n d 20: +0.1553 at d .01 (n 2000; predicted 0.15); closed form +0.2041, the usual slope of about -5 d
    b (6, 2, -1), w (.1, .1, .8)  n d 1:  -0.563923, -0.551533, -0.545295 at d .01, .005, .0025 (n 100, 200, 400); second-order
          (rrm3v_eps.py)                  Richardson -0.53903; closed form -0.5390; the eps = 0 value -0.4775 is excluded
                                  n d 5:  -0.298632, -0.281463 at d .01, .005 (n 500, 1000); linear -0.26429; closed form -0.2645
                                  n d 10: -0.238326 at d .01 (n 1000); closed form -0.2004 (gap 3.8 d, as at n d 5)
rrm3v_eps.py is agent C's three-valued solver with the s-weight multiplied by 1 - eps sqrt(pi) s erfcx(eps s), the eps kernel
of rr_exact_m2.py after u = s^2; with b = (9, -1, -1) it gives rr_exact_m2.py's eps 1 root at n 100, beta2 .99 (-0.707679) to the digit.
Audit 1 (agent C) used its own evaluator (p2, p3 by sympy) and its momentum solver rrm3m.py with the eps kernel, checked
against rrm_eps.py: at n d 1 on b (6, 2, -1), eps 1, the rows extrapolate to -0.5390, -0.5388 and -0.5368 at beta1 0, 0.5 and 0.9
(the last of order 3, slow as at eps 0) against the formula's -0.539035. At n d 2 its rows give -0.4086 at beta1 0 and 0.5 against -0.408672. So c does not depend on beta1 at eps 1 either.
So eps rescales the whole curve rather than only its ends. On 9/-1 at eps 1, c crosses zero near n d 6 (n d 3 at eps 0).

eps > 0 with momentum on the three-valued b (20 Oct 10:3x, from agent C's exact roots audit_C/r3me_out, rrm3m.py with EPS=1;
Richardson re-done here): c(1) -0.5390 / -0.5388 / -0.5368 at beta1 0 / .5 / .9 and c(2) -0.4086 / -0.4086 at beta1 0 / .5, against
the closed form -0.539035 and -0.408672. So the eps > 0 c does not depend on beta1 on a b with r1 != r2 either. Not run: beta1 .9 at n d 2.

Both eps > 0 results now have their second audits and count as verified. The closed form: agent A, AUDIT_CEPS, 11:1x,
CONFIRMED, twelve Monte Carlo rows (n 100 to 1000, 9/-1 and 6/2/-1) agree with the exact roots; extrapolated linearly to d = 0 the
Monte Carlo gives -0.543 +- 0.003 at n d 1 and -0.257 +- 0.007 at n d 5 on 6/2/-1, against -0.5390 and -0.2645. The remainder bound:
AUDIT_EPSUNIF, 11:0x, CONFIRMED, six Monte Carlo rows from n 10 to 500 at eps 1 and 3 within 1.6 se of the exact roots. Nothing in
the scalar law is left at one audit.
