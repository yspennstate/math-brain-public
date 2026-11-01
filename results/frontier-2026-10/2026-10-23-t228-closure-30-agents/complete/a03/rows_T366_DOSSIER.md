# T366 Catastrophic forgetting under random task orderings

Lead: unassigned. Dossier written 2026-10-16 by claude-99aebc7f from the row and the arXiv records below (abstracts read 16 Oct
09:2x, and the 16 Oct audit (status PARTLY, forgetting diagnostic)).

## STATEMENT
Repaired, following the audit: tasks X_m w = y_m, m = 1..T, JOINTLY realizable (one w* solves all), ||w*|| <= 1, max_m
||X_m|| <= 1; each step projects the iterate onto the solution set of a task drawn uniformly with replacement (the
unregularized scheme: gradient descent to convergence from the previous iterate); forgetting after k steps = E of the mean
over tasks seen so far of the squared residual of the last iterate. Determine the rate uniform over d, T and ranks between the
known Omega(1/k) and O(1/sqrt(k)). Without replacement (random permutations, epochs) is a separate question; historical loss
is not to be replaced by parameter distance.
Narrowed by the literature: with regularization the optimal O(1/k) is attained (Levinstein et al. 2506.06501), so what stays
open is the unregularized projection scheme.

## FRONTIER
- Evron, Moroshko, Ward, Srebro, Soudry arXiv:2205.09588: random ordering bound 9(d - r_avg)/k; adversarial orderings bad.
- Evron et al. arXiv:2504.04579: parameter-dependent sqrt(d - r_avg)/k and universal k^-1/4.
- Attia, Schliserman, Sherman, Koren arXiv:2507.11274: last-iterate SGD in the interpolation regime; with sigma_* = 0 and
  eta = 1/beta, O(1/sqrt(T)), improving Evron et al.'s O(T^-1/4) for realizable linear regression (population loss and
  historical forgetting, with and without replacement - per the audit); leaves the gap to Omega(1/k).
- Levinstein, Attia, Schliserman, Sherman, Koren, Soudry arXiv:2506.06501: fixed isotropic l2 regularization gives O(log k/k),
  an increasing regularization schedule gives the optimal O(1/k); both are SGD on surrogate losses.
- Xu, Ma arXiv:2604.13460: exponential decay for each fixed task law with a data-dependent coverage gap (not uniform).
- Varre, Pillaud-Vivien, Flammarion arXiv:2102.03183 (NeurIPS 2021), last iterate of constant-step noiseless least-squares SGD:
  under E|x|^2 xx' <= R H alone, step (4 R ln T)^-1 gives E R(theta_T) <= 3 R |theta*|^2 ln(T)/T, dimension-free (the log is
  open there too); O(1/T) at a fixed step only under a spectrum-dependent log-regularity condition. The step-1 projection is
  not covered (added 20 Oct by claude-5aab5938; notes claude_5aab5938/NOTES.md, last section).
- Open: the unregularized rate.

## ARCHITECTURE
The unregularized scheme is a randomized Kaczmarz / alternating-projection method on the joint solution set; with step
eta = 1/beta it is SGD on the losses (1/2)||X_m w - y_m||^2 with exact minimization, and 2507.11274's last-iterate bound for
interpolating SGD gives 1/sqrt(k). The regularized schemes move the effective step below 1/beta, which is where the 1/k
rate comes from.

## FAILURE POINT
At the full projection step the last-iterate analysis of SGD loses the averaging that gives 1/k: the last iterate of
interpolating SGD at eta = 1/beta has worst case 1/sqrt(T) in general smooth convex problems, so a 1/k bound must use the
projection structure (quadratics, projectors), not only smoothness.

## SHAPE
Days, done here as a check: two lines through the origin in R^2 at angle theta, a uniformly random line each step. Every
switch of line multiplies the iterate's norm by cos theta, the current task's residual is 0 and the other's is |w|^2 sin^2
theta, so with s = sin^2 theta the forgetting after k steps is about (s/2) E[cos^(2J) theta] = (s/2)(1 - s/2)^(k-1) (J =
number of switches, Binomial(k-1, 1/2)), up to the first step's normalization. Its sup over theta is at s/2 = 1/k and equals
(1/k)(1 - 1/k)^(k-1), about 1/(e k). So two projectors give order 1/k exactly - the known lower bound's order - and any gap
above 1/k must come from many tasks or higher rank. Weeks: whether the worst case over projector families is 1/k or k^-a with
a < 1.
Checked by Monte Carlo (16 Oct 09:2x, 4000 runs per point, 25 values of s): sup over theta of k x forgetting = 0.348,
0.365, 0.366 at k = 10, 100, 1000, against 1/e = 0.368.

## OBSTRUCTION
Many non-commuting projectors with small mutual angles. Moves: T lines (or hyperplanes) in R^d whose normals are close to one
another; the product of random projections contracts slowly along the common direction, and the forgetting is a sum over the
spectrum of E[P_{m_k} ... P_{m_1}].

## TARGETS
1. T hyperplanes in R^T with normals at pairwise angle theta (a simplex-like family): forgetting after k random projections,
   sup over theta, as a function of k and T, by simulation first (T = 3..20, k up to 10^4).
2. If the sup grows faster than 1/k in T at fixed k, look for the family that maximizes it; if not, try to prove O(1/k) for
   rank-one tasks.

### Result 2026-10-18 01:5x (claude-99aebc7f): Target 1, the simplex family (simplex_forgetting.py, simplex_forgetting_run1.txt)
T unit normals in R^T with pairwise inner product c = 1 - s, w* = 0, |w_0| = 1, a uniform random task each step, 1000 runs per
point, 31 values of s from 1e-5 to 1. The forgetting after k steps is a quadratic form in w_0 that commutes with permuting the tasks,
so its eigenspaces are the common direction and its complement (trivial and standard representations of S_T); both starting
directions are simulated and the larger is taken, which is the exact sup over unit w_0 for this family.
sup over s of k F(k):

    T     k=10   k=30   k=100  k=300  k=1000 k=3000 k=10^4
    2     0.367  0.369  0.368  0.367  0.368  0.368  0.368    (the exact two-line answer, 1/e, recovered)
    3     0.343  0.356  0.373  0.373  0.367  0.369  0.364
    5     0.299  0.376  0.360  0.379  0.363  0.366  0.354
    10    0.192  0.350  0.372  0.360  0.352  0.376  0.397
    20    0.188  0.261  0.365  0.381  0.359  0.385  0.364

The maximizing s scales as 1/k (about 1/k to 10/k), the worst angle shrinking with the horizon exactly as for two lines. Within the
Monte Carlo error (about 0.02 at 1000 runs) the constant does not grow with T or k: the simplex family is order 1/k with constant
near 1/e, so it does not separate the Omega(1/k) and O(1/sqrt(k)) bounds. At small k with T > k the sup is lower because most tasks
are unseen and the forgetting averages only over seen tasks.

### Note 2026-10-18 (claude-99aebc7f): for rank-one tasks the averaged iterate is 1/k in one line; the open part is the last iterate
Rank-one tasks with unit normals n_m, w* = 0: a step on task m maps w to w - (n_m.w) n_m, so |w_(j+1)|^2 = |w_j|^2 - (n_m.w_j)^2
exactly. Taking expectations over the uniform draw, E|w_(j+1)|^2 = E|w_j|^2 - E R(w_j) with R(w) = (1/T) sum_m (n_m.w)^2, the
residual over ALL tasks. Summing, sum_(j<k) E R(w_j) <= |w_0|^2, so the average over the first k iterates of the full-task
residual is at most |w_0|^2 / k, for every T, d and geometry (this is the randomized Kaczmarz energy identity). Two gaps separate
this from the target:
(a) last iterate: E R(w_k) need not decrease in k (E R(w_(j+1)) = E w_j' M w_j with M = (1/T) sum_m P_m A P_m, A = (1/T) sum n n',
    and M <= A fails in general), so the energy identity alone gives min_(j<k) E R(w_j) <= 1/k, not E R(w_k) <= 1/k;
(b) the seen-task average: the target averages over tasks seen so far, which differs from R only while some task is unseen
    (k below about T log T).
Higher-rank tasks: the same identity holds with (n_m.w)^2 replaced by |P_(V_m) w|^2, the squared distance to task m's solution set,
which is at least the residual |X_m w|^2 / |X_m|^2 >= |X_m w|^2 under max |X_m| <= 1, so the averaged-iterate O(1/k) carries over.
What would settle (a): a family where E R(w_k) is non-monotone with an excursion that grows with k at the worst angle, or a proof
that R(w_k) is a supermartingale up to a constant (E R(w_k) <= C min_(j<=k) E R(w_j)). The simplex data above are consistent with
the second for that family.

### Result 2026-10-18 02:1x (claude-99aebc7f): the last iterate, worst case by exact second moments (lastiter_exact.py, lastiter_exact_run1.txt)
E R(w_k) = w_0' Phi^k(A) w_0 with Phi(Y) = (1/T) sum_m P_m Y P_m and A = (1/T) sum_m n_m n_m', so the worst unit start gives
lambda_max(Phi^k(A)) exactly. A local search over unit normals (12 random starts, 150 steps each) maximizing k x lambda_max:

    d T      k = 10    k = 100   k = 1000
    3 3      0.042     0.282     0.368
    5 5      0.317     0.369     0.368
    5 20     0.070     0.354     0.369
    10 10    0.245     0.370     0.369
    10 40    0.089     0.366     0.369

At k = 1000 every (d, T) lands on 0.368-0.369 = 1/e, the same constant the averaged iterate's simplex family gave. A one-mode
picture gives the lower bound: a direction whose risk is eps and which contracts by (1 - eps) a step contributes k eps (1 - eps)^k,
maximized at (k/(k+1))^(k+1) -> 1/e. The search slightly exceeds that at k = 100 (0.370 against 0.366), so the one-mode value is
not the exact finite-k supremum; whether sup k E R(w_k) -> 1/e from above is the open part.
Also checked (inline, 18 Oct): one step can double the risk (sup E R(w_1)/R(w_0) = 2.0, reached by two nearly parallel tasks), and
sup_w E R(w_k)/R(w_0) stays at 2.0 for k = 1..100 over 3,000 random families - so the risk is not a supermartingale, and an O(1/k)
proof for the last iterate cannot go through the risk alone; it must use the energy |w_k|^2, which the identity
|w_(j+1)|^2 = |w_j|^2 - (n_m . w_j)^2 makes monotone.

### From claude-5aab5938, 2026-10-18 00:1x (their notes: claude_5aab5938/NOTES.md, pushed 5a3d8913; folded in by claude-99aebc7f)
- Literature. Derezinski-Dong, arXiv:2604.09909 (10 Apr 2026), prove a last-iterate bound for randomized Kaczmarz,
  E||Ax_t - b||^2 <= C ||A||_F^2 ||x_0 - x*||^2 / t^(3/4 + theta) with theta >= 0.001, free of the condition number, rows sampled by
  squared norm (our uniform unit rows). They state the worst-case rate as unresolved, and their majorant N_{t+1} = N_t(I - 2Q) + ||N_t|| Q
  provably cannot beat t^-(3/4 + 0.003) (their Thm 3.8). The gap is therefore Omega(1/k) against O(k^-3/4); FRONTIER should cite it.
- On the same spectra their majorant grows like t^(1/4) (8.5 at t = 1e6) while the exact map stays at 0.38; ill-conditioned and
  near-collinear multiscale families (d to 50, eigenvalues of Q to 1e-40) give max over k <= 1e8 of k G_k between 0.368 and 0.388.
- Reduction (proved). If Phi^m(Q) <= C Q for every m, then F_k(e) <= C |e|^2/(k + 1): F_k <= C F_j for j <= k, and sum_j F_j <= |e|^2.
- The hypothesis holds numerically with C = 2, sharp: 2.0000 at m = 1 (two near-parallel lines), 1.9981-1.9998 at m ~ 1e4 in the
  multiscale families. Not proved; the Lyapunov candidates 2Q - Q^2, Q + Phi(Q), Q + W and 2Q - W all fail.
- Conjecture to record: Phi^m(Q) <= 2Q for all m, hence F_k <= 2/(k + 1).
- Also from their notes: the HS spectral bound F_k <= min(1, d/2k)^(1/2)/sqrt(2k); m-step monotonicity D_{k+m} <= D_k fails for m = 1..4;
  the ratio k F_k / sum_{j<k} F_j has exact sup 2 at k = 1.

### From claude-5aab5938, 2026-10-18 01:0x (NOTES.md, last two sections; folded in by claude-99aebc7f)
- The lemma Phi^m(Q) <= C Q is proved in the plane (d = 2), with C = 1 + |z|, z = E e^{2it}: lambda_max(D_m) <= tr D_m = <1, K^{m-1}(I - K) 1>
  against a spectral measure of mass one, which also gives m G_m <= (1 - 1/m)^{m-1} -> 1/e, the planar constant seen in the
  near-collinear numerics. The same trace step gives only the folklore d/(e m) in dimension d, and that is exactly where d >= 3 fails.
- No single quadratic Lyapunov matrix certifies the lemma: the SDP's optimal constant is far above 2 already on Gaussian 3 x 4
  families, infeasible at c = 2.5 under two solvers.
- Replacing m single-row projections by one exact projection onto the span of a random m-row subset breaks the bound (ratio 902), so
  a proof has to use the one-row-at-a-time structure.
- Nested near-parallel hierarchies push the ratio to 2 at large m and never above.

### From claude-5aab5938, 2026-10-20 17:48 (claude_5aab5938/NOTES.md, 13:05-17:48): condition (B) in the cluster family is bounded in d
- (B) is E_m Q E_m <= C Q for all m (E_m = Phi^m(I)); it gives the lemma Phi^m(Q) <= 2 sqrt(C) Q and so F_k <= 2 sqrt(C)/(k + 1).
  For unit rows E_1 = I - Q, so the m = 1 quotient is lam_max((I - Q)^2) <= 1; any computed value above 1 at m = 1 is round-off.
- Family: two heavy rows plus L light rows in a regular-simplex cluster (9 parameters), in the tau -> 0 limit (limit_B.py). Exact
  S_L reduction (reduced.py): E_m = G_m (+) s_m I with G_m 3 x 3 and s_m scalar; it matches the full limit to 1e-9, and the full limit
  matches the ORIGINAL unit-row problem (d 22: tau 1e-6, 1e-7 give 1.108633, 1.109628 against 1.109638).
- Optimised values grow over d 3..42 (1.0254 to 1.1341, about 0.04 log d), but this is pre-asymptotic. At L = infinity the sup is about
  1.264 (22 starts, every optimum re-checked at 50 digits, unchanged under condition caps 1e9..1e13), reached on a boundary (light rows
  nearly orthogonal to the heavy span, a spectral gap of the averaged map closing). At a gapped optimum the finite-d values rise
  monotonically to the L = infinity value (d 42 1.020, d 1e3 1.171, d 1e6 1.2599, limit 1.2603).
- So in this family (B) holds with C about 1.264 for every d, which would give the lemma with constant about 2.25. C = 1 (hence the sharp
  2 through (B)) is false off the plane. Open: whether a richer ansatz beats 1.264, and a proof of (B) with any dimension-free C.
- A float64 run reported 231058 at one L = infinity point; it was round-off (cond(QT) 1e21 against a true smallest eigenvalue 2.4e-7;
  the 60-digit value is 1.0025).

### From claude-5aab5938, 2026-10-20 19:0x (claude_5aab5938/NOTES.md 18:5x entry): the cluster family's ceiling is (3 + sqrt 21)/6
- multi_inf.py extends the L = inf reduction to any number of clusters (U = R^n, C = R^k, each cluster its own simplex space; a heavy
  row is a cluster with d = 0). Controls in multi_selftest.txt: equal to the one-cluster code (float and 50 digits); its finite-L
  recursion equals limit_B on the explicit rows to 10 digits; B_1 = 1.
- Thirty optimiser starts over n 2-3, k 1-2, R 3-5 clusters all end at 1.26376 or below (50-digit rechecks). Extra clusters and
  extra dimensions add nothing. Every optimum has the same shape: two nearly parallel heavy rows (half-angle f) and one light cluster
  whose T-part is of order f with d ~ 1. With that T-part set to 0 the source term vanishes and B* = 1.
- In that shape B* tends to a limit as f -> 0, error about 0.5 f^2. Optimised in the limit from six starts: 1.263762615826 each time.
  Polished at f = 1e-12 with 60 digits, three optima differ from (3 + sqrt 21)/6 by -5e-25, -1.3e-24 and -6e-25, which is the 0.5 f^2
  error. So within the family sup (B) = (3 + sqrt 21)/6 = 1.2637626158..., the positive root of 3x^2 - 3x - 1, approached but not
  attained. Brute iteration at f = 6.8e-3 reaches the fixed-point value at m = 1.7e6 (iter_audit.txt).
- Consequence for the lemma: within the family Phi^m(Q) <= 2 sqrt(C) Q with 2 sqrt(C) = 2.2483. Open: derive the quadratic from the
  f -> 0 limit; test whether (3 + sqrt 21)/6 bounds (B) outside the cluster family.

### From claude-5aab5938, 2026-10-20 19:5x (claude_5aab5938/NOTES.md "limit" entry): where (3 + sqrt 21)/6 comes from
- Rescale the near-degenerate direction: G^ = D G D^-1, Q^ = D^-1 QT D^-1 with D = diag(1, f, 1). At f -> 0 two entries of G are
  neutral (G_22 and G_23, with G_23 ~ h/f). limit_sym.py (exact, sympy, at rational points) and limit_num.py (f = 1e-20, 80 digits)
  agree with focus3 to 12 digits.
- At every parameter point tested (the six optima and 800 random points) G^ has zero e1 column, and its e1 row is the Q^-optimal one.
  So B* = top singular value^2 of [[g, kappa], [0, 1]] in the Schur metric of Q^ on (e2, e3), with g = G^_22. The sampled (g, kappa)
  fill the disk (2g)^2 + kappa^2 <= 2g.
- On the circle (2g)^2 + kappa^2 = 2g the value has a single maximum, at 3g^2 + 3g - 1 = 0, where it equals 1 + g = (3 + sqrt 21)/6
  (disk_check.txt). All six optima sit at that boundary point, which is why their parameters differ and their value does not.
- Status: the quadratic follows from three measured facts (zero column, optimal e1 row, the disk). None of the three is proved yet.
  The disk is the one that carries the constant.

### From claude-5aab5938, 2026-10-20 21:0x: the f -> 0 limit is derived, not measured (two heavy rows + one light cluster)
- limit_series.py: G's two non-trivial rows as Laurent series in t (angle ~ 2t), every parameter symbolic, solved order by order.
  K = 3 fixes the neutral pair (limit_series_K3.txt / .pkl). The light cluster's v1 drops out exactly (v1_check.txt).
- The e1 column of G^ is 0 and the e1 row equals the Q^-optimal row, both symbolically (row1_check.txt). So in the limit
  B* = top singular value^2 of [[g, kappa], [0, 1]] in the Schur metric of Q^ on (e2, e3).
- Closed forms (disk_proof.txt), with W = p0 v2^2 + 4 q (1-q)(1-p0):
  g = p0 v2^2 / (2W), which lies in [0, 1/2]; s11 = 4W; sigma = p0 q (1-p0)(1-q)(2 c0 + cm v2 - v2)^2 / W;
  h + (1-g) s12/s11 = p0 q v2 (p0-1)(q-1)(2 c0 + cm v2 - v2) / W^2.
- The identity 2g - 4g^2 - kappa^2 = 0 holds for every parameter value. So every point lies ON the circle (2g)^2 + kappa^2 = 2g, not just
  inside the disk, and B* = lambda(g) = [(1+3g)(1-g) + sqrt((1-3g^2)(1+4g-3g^2))]/2. Its one critical point on (0, 1/2) is
  3g^2 + 3g - 1 = 0, value 1 + g = (3 + sqrt 21)/6. The flat optimum manifold is the level set g = (sqrt 21 - 3)/6.
  Numeric control: closed forms against the 80-digit limit code at 8 points, max difference 9.2e-10 (the 50-digit floor of gk).
- What this does not cover: that more light clusters, or more heavy rows, add nothing is measured only (multi_inf, 30 starts each);
  condition (B) outside the cluster family is untested. Next: the R-cluster version of the series argument.
- Caveat on 'derived': the series solve assumes the fixed point is a Laurent series in t starting at t^-1 (true for the unique fixed point when it is analytic in t; supported to 12 digits by the 80-digit runs, not proved). So the closed forms are rigorous modulo that expansion step.

### From claude-5aab5938, 2026-10-20 22:2x: more light clusters only lower B* (measured; the L = 2 value of 8.5 was a rounding artifact)
- With the weights summing exactly to 1, the f -> 0 limit for two heavy rows plus L light clusters (40 random points per L, f = 1e-20,
  80 digits) gives a maximum B* of 1.2619 (L = 1), 1.2558 (L = 2) and 1.2541 (L = 3). B* equals the 2x2 value exactly, and the disk
  excess (2g)^2 + kappa^2 - 2g is 0, at most -8e-5 and at most -1.2e-3 respectively.
- A transient 8.5 for L = 2 came from float weights summing to 1 - 1.7e-17. That deficit exceeds the map's spectral gap of about f^2
  once f < 4e-9. Files: claude_5aab5938/limit_multi_fix.txt, limit_multi_fixed.txt, NOTES.md (22:2x entry).
- Still open: a proof of the disk inequality for L clusters, and condition (B) outside the cluster family.

### From claude-5aab5938, 2026-10-20 22:5x: L light clusters reduce to one (claude_5aab5938/NOTES.md 22:5x entry)
- Light clusters enter the f -> 0 limit of G^ only through S = p0 sum pi v2^2 and T = p0 sum pi v2 c (agreement 6.5e-18 with the
  single equivalent cluster, L = 2..4). The extra moment R = p0 sum pi c^2 >= T^2/S enters only the Schur complement sigma and lowers kappa.
  So B* for L clusters is at most B* for one cluster, and so at most (3 + sqrt 21)/6. This is rigorous given the Laurent ansatz and the
  measured vanishing of the higher v-moments.

### From claude-5aab5938, 2026-10-20 23:4x: the light-cluster reduction is symbolic for every L (claude_5aab5938/NOTES.md 23:4x)
- With every cluster moment an independent symbol (limit_series_M.py), the limit G^ equals the single-equivalent closed form exactly
  and depends only on S and T. So B* <= (3 + sqrt 21)/6 holds for the whole cluster family given the Laurent ansatz for the fixed
  point. Still open: the ansatz, more heavy rows, (B) outside the family.

### From claude-5aab5938, 2026-10-21 00:3x: the Laurent ansatz holds (claude_5aab5938/NOTES.md 00:3x)
- g solves a linear system rational in t, so it is rational; at 8 random parameter/moment points ord det(I - L_t) = 4 and the Cramer
  numerators give pole order exactly 1, confirmed by 60-digit solves at t down to 1e-6. So B* <= (3 + sqrt 21)/6 on the cluster
  family no longer rests on the ansatz, except on a measure-zero exceptional set. Still open: K = 4 audit, more heavy rows, (B)
  outside the family.

### From claude-5aab5938, 2026-10-21 02:2x: any number of heavy rows in the pencil reduces to two (claude_5aab5938/NOTES.md 01:5x)
- With the heavy rows and the light clusters both given as arbitrary distributions (independent moment symbols), the limit G^ depends
  only on four heavy moments and the two light moments S, T (exact, K = 3 and K = 4). The two-row, one-cluster configuration with those
  moments has the same G^ and a Q^ smaller only on e3 e3'; since G^'s third row is e3', B* <= max(B*_equiv, 1). So B* <= (3 + sqrt 21)/6
  for every distribution of heavy rows in the (e1, e2) pencil and light clusters. Checked against a direct 90-digit solve (1.5e-11 on
  8 configurations of 3-5 heavy rows); pole order 1 on 6 seeded heavy configurations. Open: heavy rows outside the pencil, (B) outside
  the cluster family, the measure-zero exceptional set.

### From claude-5aab5938, 2026-10-21 03:5x: outside the pencil (B) exceeds (3 + sqrt 21)/6 (claude_5aab5938/NOTES.md 03:1x-03:5x)
- Heavy rows anywhere in U = R^3 reduce, as in the pencil, to three equal-weight atoms with matched mean and covariance of A and b affine
  in A (same G^ to O(t^2), Q^ larger only on e4 e4'; H3_moment_check.txt, 80 digits). A 12-parameter search over that family finds
  B* = 1.267891 from two independent seeds, against (3 + sqrt 21)/6 = 1.263763: heavy atoms on a line A2 = alpha + gamma A1 not through
  the origin, the light cluster with an out-of-plane component.
- Checked on the original problem with no rescaling and no reduced model: unit rows, light rows on an L = infinity simplex, the symmetric
  recursion taken to m = 2^k exactly by squaring its affine matrix at 160 digits. The ratio holds a plateau 1/t^2 << m << 1/tau^2 at
  1.26788367915 (t = 1e-8 and 1e-10), equal to the model at the same point to 12 digits; B_1 = 1 as the theorem requires.
  (orig3d_plateau.txt; the m = infinity fixed point at fixed tau reads 0.38 and is a different limit, orig3d_fixed.txt.)
- So (3 + sqrt 21)/6 is the sup of the pencil family only. The sup of (B) is at least 1.267884. Whether it is finite outside the pencil is
  open; the route to the lemma needs only some dimension-free C.

