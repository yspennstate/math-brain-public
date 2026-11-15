# The Fourier entropy-influence constant of read-once formulas (working note, 2026-09-21)

Status: the reduction below is a complete proof; the constant is established numerically (a computer-assisted
rigorous version is the open task). Notation follows Hod (2017): true = -1, Pr[f] = Pr[f = true], h = binary
entropy in bits, V_p = 4p(1-p), H = spectral entropy, I = total influence, I+ = I/V, H+ = (H - h(V))/V.

## 1. Composition through a two-input gate

Let a, b be Boolean functions on disjoint variable sets with Pr[a] = p, Pr[b] = q, and g = AND(a, b). By the
composition lemma (O'Donnell-Tan 2013, Prop. 3.2; Hod 2017, Lemma 3.1) with the biased Fourier transform of AND at
the biases 1-2p, 1-2q,

    I(g) = It_a I+(a) + It_b I+(b),      H(g) = It_a H+(a) + It_b H+(b) + Ht_AND(p, q),

where for the AND gate (a direct computation, checked against the general biased transform and against brute force
on formulas with up to 17 variables, error 2e-15)

    It_a = q V_p,   It_b = p V_q,   w_empty = (1 - 2pq)^2,   w_ab = w_empty + It_a + It_b - 1,
    Ht_AND(p, q) = phi(w_empty) + phi(It_a - w_ab) + phi(It_b - w_ab) + phi(w_ab),   phi(w) = w log2(1/w).

Since It_a I+(a) = q I(a) and It_b I+(b) = p I(b): I(AND(a,b)) = q I(a) + p I(b). OR(a, b) is the negation of
AND(not a, not b); negation of a function or of its inputs changes neither H nor I, so OR(a,b) has the H and I of
AND(a', b') with Pr[a'] = 1-p, Pr[b'] = 1-q.

## 2. The reduction to a one-variable inequality

Proposition. Let C > 0 and let Gamma: (0,1) -> [0, inf) satisfy Gamma(p) = Gamma(1-p) and, for all p, q in (0,1),

    (A)   Gamma(pq) <= q (Gamma(p) + h(V_p)) + p (Gamma(q) + h(V_q)) - Ht_AND(p, q).

If Gamma(1/2) <= C, then every read-once formula f over AND, OR, NOT (fan-in two; larger fan-in is a composition)
on independent uniform bits satisfies

    H(f) <= C I(f) - Gamma(Pr[f])  <=  C I(f).

Proof. Induction on the formula. A variable: H = 0, I = 1, Pr = 1/2, and 0 <= C - Gamma(1/2). NOT preserves H, I
and maps p to 1-p; Gamma is symmetric. For g = AND(a, b) with the hypothesis H(a) <= C I(a) - Gamma(p) and
H(b) <= C I(b) - Gamma(q):

    H(g) = q V_p H+(a) + p V_q H+(b) + Ht_AND
         <= q (C I(a) - Gamma(p) - h(V_p)) + p (C I(b) - Gamma(q) - h(V_q)) + Ht_AND
         = C I(g) - [ q (Gamma(p) + h(V_p)) + p (Gamma(q) + h(V_q)) - Ht_AND(p,q) ]
         <= C I(g) - Gamma(pq)                                  by (A), and Pr[g] = pq.

OR follows from AND on the negated inputs and the symmetry of Gamma. Gamma >= 0 gives the last inequality. QED.

Remarks. (i) The constant C does not enter (A); it only enters through Gamma(1/2) <= C, so the read-once FEI
constant C_RO satisfies C_RO <= inf { Gamma(1/2) : Gamma admissible, >= 0, symmetric }. (ii) Conversely the
extremal slack Sigma*(p) = inf { C I(f) - H(f) : f read-once, Pr[f] = p } is admissible whenever the inequality
is imposed only at realised (dyadic) measures, and it dominates every admissible Gamma with Gamma(1/2) <= C by the
proposition; so on realised measures the largest admissible function under the cap is Sigma* itself, and the
smallest cap with Sigma* >= 0 is exactly C_RO. Imposing (A) for all real p, q is a relaxation in the safe direction.

## 3. Lower bound (Hod 2017)

Hod's construction F_{m+1} = (F_m AND F_{m+1})^dual, iterated from a single variable, is read-once and has
lim H/I = beta(1/2) = S(1/2) = 6.4547837..., where S(z) = sum_{j>=0} h(q_j) q_1...q_j / (1-q_j) with q_0 = z,
q_{j+1} = 1/(1+q_j), equivalently S(z) = h(z)/(1-z) + S(1/(1+z))/(1+z). Our evaluator reproduces 6.4547837 from
the recursion (fei_recsys.py) and by brute force on the materialised finite functions (verify_record.py).
For any read-once seed f with (p, I, H) the same construction gives lim H/I = (H - h(V_p) + V_p S(p))/I, hence the
extremal slack obeys Sigma*(p) >= V_p S(p) - h(V_p) =: Gamma_H(p) whenever C_RO = beta(1/2).

## 4. Numerics

Value iteration Gamma <- min(Gamma, T Gamma) from the cap (Gamma(1/2) = C, 60 elsewhere) on an N-point grid,
with T the right-hand side of (A) minimised over factorisations and symmetrised (fei_readonce_gamma.py):

    N = 600:  smallest C with Gamma >= 0 everywhere = 6.454794   (Hod's lower bound 6.4547837)
    N = 1500, 3000: running (2026-09-21 04:0x)

Consistency: the 2,352 formulas on the frontier of a Pareto DP over all read-once formulas (fei_readonce_dp2.py,
each record re-evaluated exactly from its tree) satisfy H <= C I - Gamma_num(Pr f) up to 0.0045 at the one
dyadic point that is not a grid point; the DP's best ratio climbs 2.0, 3.40, 3.89, 4.40, 4.72, 5.07, 5.28, 5.51,
5.64, 5.79, 5.88, 5.98, ... 6.30 (sweep 22) and has not passed beta(1/2); exhaustive and annealed searches over
self-similar recursive systems (one to three symbols, gates of two and three inputs) reach exactly 6.4547837 from
many distinct systems and nothing above it. Gamma_H is not admissible (min violation 0.00075 near p = q = 0.908;
its symmetrisation 0.013), and the lexicographic slack C I(l_p) - H(l_p) fails by 0.10 near p = q = 0.665, so the
extremal potential is the fixed point rather than either closed form.

Conjecture (numerically established). C_RO = beta(1/2) = 6.4547837..., with Hod's construction extremal.

## 5. Towards a proof

Rigorous certificate = an explicit admissible symmetric Gamma >= 0 with Gamma(1/2) = beta(1/2) + epsilon. Plan:
(a) interval-arithmetic value iteration on a geometric grid (cell-wise lower bounds of the right-hand side, Gamma
piecewise constant) on [p0, 1-p0]; (b) an analytic argument on (0, p0], where along AND_n the slack
C I - H = (2n(C-4) + O(1))/2^n tends to zero and (A) is tight to first order; in the + normalisation
G = (Gamma + h(V))/V the AND-chain slack grows like ((C-4)/2) log2(1/p) against the required log2(1/(4p)), so
there is room. (c) Whether a closed form exists for the fixed point is open; it equals the AND_n slack at dyadic
p = 2^-n and exceeds Gamma_H by up to 0.27 near p = 0.06.

## 6. Two extensions and the shape of the proof (2026-09-21 04:5x)

Three-input gates. The induction closes for a k-input gate G exactly when
Gamma(p_out) <= sum_i It_i(G; p) (Gamma(p_i) + h(V_i)) / V_i - Ht_G(p) for all input measures. With Gamma the
AND/OR fixed point (N = 600), all 218 nondegenerate 3-input gates satisfy this on a 33^3 grid of measures in
[0.02, 0.98]: the smallest value is -0.00002, attained only by gates that reduce to a two-input gate on a fresh
variable (fei_gate3_check.py). So the sharp constant is the same for read-once formulas over every gate of fan-in
at most three, and (numerically) Hod's two-input construction is extremal in that larger class too.

The edge. On a hybrid grid (geometric tails of 24 points per octave down to 2^-14, uniform middle at 1/2000;
fei_readonce_gamma_geo.py, C = 6.4548) the fixed point equals the AND_k slack at every dyadic p = 2^-k and
Gamma(p)/p - 2(C-4) log2(1/p) tends to 8 - 8/ln 4 = 2.229 with a bounded log-periodic correction between 2.2 and 3
at non-dyadic small p. The constraint (A) is tight to first order along AND chains (both the p log(1/p) and the
constant term cancel exactly), so a rigorous verification cannot rely on absolute margins near zero.

Margin device for a rigorous certificate. Adding c min(p, 1-p) to an admissible Gamma raises every AND
constraint's right-hand side by 2c pq while raising its left-hand side by c pq, a margin of c pq that scales with
the measures; the price is Gamma(1/2) + c/2, i.e. a theorem constant beta(1/2) + c/2. So a computer-assisted proof
of C_RO <= 6.4558 needs: (a) interval bounds of (A) for Gamma_hat = Gamma_num + c min(p,1-p) on a geometric grid
with relative error below c; (b) an analytic lemma for measures below the grid, where Gamma_hat may be taken as the
explicit AND-chain form p (2(C-4) log2(1/p) + b) with b slightly above 2.229 and the remainder terms are O(p^2 q)
and O(p q^2), against the available margin c pq.

## 7. The computer-assisted certificate (2026-09-21 05:0x-06:3x)

Normalisation. Divide (A) by pq and write G(p) = Gamma(p)/p, L(z) = log2(1/z), Psi(z) = phi((1-2z)^2)/z. Expanding the
four AND weights w_empty = (1-2pq)^2, w_ab = 4pq(1-p)(1-q), w_a = 4pq^2(1-p), w_b = 4p^2q(1-q) and the two binary
entropies h(V_p) = phi(4p(1-p)) + phi((1-2p)^2), every log2(1-p) and log2(1-q) term cancels and (A) becomes

    (A')   Phi(p,q) := G(p) + G(q) - G(pq) - E(p,q) >= 0,
           E(p,q) = 8p(1-q) L(p) + 8q(1-p) L(q) + 8(1-p)(1-q) + Psi(pq) - Psi(p) - Psi(q)

(identity checked to 40 digits at random points). As p, q -> 0, E -> 8 - 4/ln2 = b* = 2.22922, the AND-chain constant
of section 6; Psi(z) = (4/ln2)(1-2z)^2 ell(2z) with ell(u) = -ln(1-u)/u is the cancellation-free form for small z.

The certificate. On the small side p = 2^-x, x >= 1, take nodes x_j (step 2^-11 in p on [1/32, 1/2], then M nodes per
octave down to 2^-K; every dyadic is a node), values G_j from the value iteration of section 4 run in this exact
representation (Gamma/p linear in x between nodes, cancellation-free E; fei_cert_vi.py: at C0 = 6.4548, M = 24, K = 40
it converges in 120 iterations, and G(2^-k) reproduces the AND-chain slack at every k with G(2^-k)/... - 2(C0-4)k =
2.229220 at k = 30 and 40). Beyond x = K the tail is linear with slope sigma_t = (G_J - b*)/K, so that
G(x) + G(y) - G(x+y) = b* exactly when x, y > K. The certified potential is

    Gamma_hat(p) = p G_num(x) + c p (1-p),    Gamma_hat(1-p) = Gamma_hat(p),    Gamma_hat(1/2) = C0 + c/4,

whose extra term gives (A') the uniform slack c(1-p)(1-q) at every point where G_num itself satisfies it.  The theorem
constant is C0 + c/4.

Verification (fei_cert.py, fei_cert23.py). Interval arithmetic in numpy float64 with outward rounding after every
operation (nextafter), transcendental functions padded by 8 ulps; the primitives were checked against 90-digit mpmath
on 9,000 random cells (0 containment failures).  The square (0,1)^2 is covered by
  region 1  p, q <= 1/2: cells in (x, y), Phi bounded below with G over an interval by its node range (sparse table)
            and E by its natural extension; failing cells split in four (adaptive);
  region 2  p <= 1/2 < q, v = 1-q = 2^-y': Phi/v written with the mean-value enclosures
            [G(x) - G(x + L(1-v))]/v = -(ell(v)/ln2) G'(xi) and [Psi(p(1-v)) - Psi(p)]/v = -p Psi'(zeta);
  region 3  p, q > 1/2, u = 1-p <= v = 1-q, w = u+v-uv: Phi/u with [Lambda(v) - Lambda(w)]/u = -(1-v) Lambda'(xi)
            for Lambda(z) = Gamma_hat(z)/(1-z), and the split at w = 1/2 (pq = 1/2) handled with the accurate
            forms m = 1-2v = -expm1((1-y') ln2), L(pq) - 1 = [u ell(u) - log1p(m)]/ln2;
  tails     p < 2^-K: (T1) both small: Phi = b* + c(1-p)(1-q) - E and E - b* <= (16K+19) 2^-K, proved from
            (1-2z)^2 ell(2z) in [1 - 3z, 1 - 3z + (4/3) z^2]; (T2) q in [2^-K, 1/2]: the one-variable condition
            G_num(y) - sigma_t y - e(q) + c(1-2^-K)(1-q) >= 8(1-q)K 2^-K + (12/ln2) 2^-K with e(q) = 8qy + 8(1-q) - Psi(q)
            the p -> 0 limit of E, using E(p,q) - e(q) <= p[8(1-q)x + 12/ln2]; (T3) q > 1/2: the analogous
            one-variable condition in y'; and three constant-only lemmas for u or v below 2^-K in regions 2 and 3.
The derivative enclosures (Psi', Psit' = -Psi'(1-.), ell' by series with a geometric tail bound, Lambda') were
checked against high-precision numerical derivatives.

Results so far (candidate M = 24, K = 40, C0 = 6.4548): with c = 0.05 the four lemmas, (T2) (depth 3) and (T3)
(depth 0) pass; region 1 passed at depth 4 on an earlier candidate; regions 1-3 are running.  A floating-point scan
of the interpolant without margin puts its worst violation at -6.1e-3 (in units of (1-p)(1-q)), on the line q = 1/2
at p = 2^-4.85, i.e. midway between the dyadic nodes where the linear interpolation of the log-periodic term is worst;
so this candidate certifies about C0 + 0.002, and the M = 96 candidate (16 times smaller interpolation error) is
running.  Every certified constant is an upper bound on C_RO; Hod's construction gives C_RO >= 6.4547837.

## 8. Theorem (computer-assisted), 2026-09-21 06:5x

    For every read-once formula f over AND, OR, NOT on independent uniform bits,   H(f) <= 6.4673 I(f).

Certificate: the potential of section 7 with C0 = 6.4548, M = 24, K = 40, c = 0.05 (constant C0 + c/4 = 6.4673).
All six parts verified on this machine with fei_cert23.py (interval arithmetic as described; the region checks are
adaptive with directional splitting, the tails analytic):
    lemmas (T1, regions 2 and 3 beyond the grid)  OK, margins +0.05, +120, +7.9, +7.1
    T2 (p below the grid, q <= 1/2)               OK at depth 3 (2,738 cells, min lower bound +0.020)
    T3 (p below the grid, q > 1/2)                OK at depth 0 (1,800 cells, min +0.017)
    region 1 (p, q <= 1/2)                        OK at depth 4 (1.62M cells at depth 0, 17.6M at depth 2, 1.1M at depth 4; 314 s)
    region 2 (p <= 1/2 < q)                       OK at depth 17 (3.2M cells at depth 0; 1,544 s)
    region 3 (p, q > 1/2)                         OK at depth 22 (1.66M cells at depth 0, incl. 20 extra octaves; 84 s)
Assumptions: IEEE double arithmetic with correctly rounded +, -, *, /; numpy log2, log1p, exp2 accurate to within
8 ulp (the primitives were checked against 90-digit arithmetic on 9,000 random cells).  Hod's lower bound is
6.4547837, so the read-once constant lies in [6.45478, 6.4673]; the previously published bound was 10.

The tight set, where the verification had to refine: the fresh-variable line q = 1/2 and its dyadic relatives
q = 2^-k (region 1), the strip p -> 1/2- with q -> 1 (region 2) and its mirror p -> 1 with q = 1/2 (region 3), and
the arc pq = 1/2 with p, q near 0.71 where the cap at 1/2 is active (region 3).  A bound that divides an interval
width by a small parameter (v in region 2, u in region 3) has to be refined along that axis alone; splitting both
axes doubles the failing count per level.

Sharper constants: the M = 24 candidate certifies down to about c = 0.008 (its interpolation error on the q = 1/2
line, 6.1e-3 in units of (1-p)(1-q), is the floor); a run at c = 0.01 (constant 6.4573) is in progress, and the
M = 96 candidate (16 times smaller interpolation error) should certify about 6.4552.

## 9. Theorem sharpened, 2026-09-21 08:1x

    For every read-once formula f over AND, OR, NOT on independent uniform bits,   H(f) <= 6.4573 I(f).

Same candidate as section 8 (C0 = 6.4548, M = 24, K = 40) with the margin c = 0.01 (constant C0 + c/4 = 6.4573).
The six parts ran as separate processes under run_cert_all.py (logs search_logs/cert_h24_c001_*.out, summary
cert_h24_c001_SUMMARY.json with all_ok true):
    lemmas (T1, regions 2 and 3 beyond the grid)  OK: T1 margin +0.010; region 2 beyond the grid +120.5;
                                                  region 3 beyond the grid +7.98 (max Lambda' = 199 for u < 2^-60); both deep +7.08
    T2 (p below the grid, q <= 1/2)               OK at depth 5 (1,800 cells at depth 0, 72 at depth 5; min lower bound +2.6e-3)
    T3 (p below the grid, q > 1/2)                OK at depth 2 (1,800 cells at depth 0; min +1.7e-3)
    region 1 (p, q <= 1/2)                        OK at depth 13 (1.62M cells at depth 0, 32.7M at depth 8, the widest level;
                                                  2 cells still failing at depth 12, none at depth 13; 951 s)
    region 2 (p <= 1/2 < q)                       OK at depth 22 (3.24M cells at depth 0, 19.7M at depth 8; min +9.6e-4; 4,978 s)
    region 3 (p, q > 1/2)                         OK, deepest level 28 (1.66M initial cells, 23.3M evaluated in memory-bounded
                                                  batches of 2M; 280 s)
Assumptions as in section 8.  Hence 6.4547837 <= C_RO <= 6.4573.

What limits the next step.  Two things, and both are in the numerics rather than the mathematics.
(i) The margin c has to cover the candidate's violation of (A) between its nodes: 6.1e-3 (units of (1-p)(1-q)) for
M = 24, 2.2e-3 for M = 96 (scan_cmin.py; the M = 96 residual sits in the uniform 2^-11 part of the grid next to
p = 1/2, not in the octave part), so M = 96 alone reaches about 6.4554 and a finer grid near 1/2 about 6.4551.
(ii) The region-1 enclosure bounds G(x) + G(y) - G(x+y) from three separate ranges, so its width is about 20h for
a cell of side h whatever the margin; below c = 0.01 the refinement has to go so deep that the cell count explodes
(the c = 0.003 run held 150M live cells and 15 GB when it was stopped; the driver is memory-bounded now, but the
time would be days).  The cure is an enclosure that keeps the cancellation: G is piecewise linear in x, so on a
cell inside one linear piece the exact minimum of G(x) + G(y) - G(x+y) is at a corner, and E can be enclosed by a
mean-value form of width O(h) with a small constant.  With that and the M = 96 candidate the same machinery should
certify about 6.4554, and with a finer near-1/2 grid about 6.4551.  Numerically the constant is 6.4547837 = beta(1/2).

## 10. The region-1 enclosure that keeps the cancellation (2026-09-21 14:2x)

Section 9 named the cure and it works.  fei_cert_r1x.py bounds Phi on a cell X x Y from below by the larger of two
enclosures, each rigorous in the same outward-rounded float64 arithmetic as before.

(a) The piecewise-linear part P = G_num(x) + G_num(y) - G_num(x+y) is linear on every piece of the subdivision of
    the cell by the lines x + y = node (the x and y sides of a node cell, and of its bisections, lie in one segment
    each), so its minimum is at a vertex of that subdivision: a corner, or a point where such a line meets an edge.
    Those vertices are evaluated with one-ulp interval coordinates, which gives the minimum exactly to rounding
    (against a dense grid: the bound is never above the grid minimum and within 3e-13 of it).
(b) The margin term c(1-p)(1-q) is monotone in each variable, so its minimum is at a corner.
(c) E is enclosed by the smaller of its interval evaluation and the mean-value form E(centre) + rx max|dE/dx| +
    ry max|dE/dy|, with dE/dx = p[8(1-q)(1 - x ln2) + 8qy ln2 + 8(1-q) ln2 - Psi'(pq) q ln2 + Psi'(p) ln2].
(d) The centred form Phi(centre) - rx max|dPhi/dx| - ry max|dPhi/dy|, where dPhi/dx = G_num'(x) - G_num'(x+y)
    + c ln2 p(1-q) - dE/dx with the slope of x's segment (exact) and the range of slopes of the segments met by
    x + y; Phi is Lipschitz, so the mean-value inequality holds with the essential supremum of the derivative.
    This form is second order in the cell width where Phi is flat, which is exactly where the old bound was tight.

Cross-check (crosscheck_r1x.py, cert_vi_h24k40.npz, c = 0.01, 251 random cells of widths h to h/32, 1,993 points at
40 digits): the bound never exceeds the true value; the slack between the sampled minimum and the bound has
median 7.7e-6 and maximum 1.8e-2, against a median of 0.10 and a maximum of 0.41 for the decoupled bound on the
same cells.  With the margin set to c = -0.2 (a way for the check to fail) every one of the 247 cells whose sampled
Phi is negative is flagged and none is bounded above its true value; that control also caught a real error, the
corner minimum of the margin term had been taken at (x0, y0), which is right only for c > 0.

Runs (BelowNormal, one core each):
    region 1, M = 24, c = 0.01     VERIFIED in 557 s: 1.62M node cells, 1.70M cells evaluated, deepest level 6
                                   (the decoupled bound needed 32.7M cells at its widest level and 951 s)
    region 1, M = 96, c = 0.003    VERIFIED in 2,066 s: 9.33M node cells, 9.50M cells evaluated, deepest level 9 (the decoupled bound had 108M cells still failing at depth 9 after 2,846 s when it was stopped)
    region 3, M = 96, c = 0.003    running at the time of writing with the section-9 bound (deepest level 27, 68M cells evaluated after 1,722 s)
    region 2, M = 96, c = 0.003    running at the time of writing with the section-9 bound (started 14:16)
With region 1 no longer the bottleneck, the constant at c = 0.003 is 6.45555 once regions 2 and 3 confirm at that margin (their lemmas, T2 and T3 already passed at c = 0.003 on the M = 96 candidate, cert_h96_c0003_SUMMARY.json); the next step is a candidate with a finer grid next to p = 1/2, where the M = 96 residual of 2.2e-3 sits, to bring c below 0.001.
