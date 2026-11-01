# T240 Escape from the symmetric plateau in a teacher-student soft committee machine

Lead: unassigned. Dossier written 2026-10-16 by agent A from the auditor's record (worker L, 02:35), the
Saad-Solla ODE computed here (scm_plateau.py, scm_check.py in this folder) and a search of arXiv.

## STATEMENT
Repaired statement (the list row left activation, noise, output weights, learning rate and time scale open; auditor
worker L, 16 Oct, statement_ok NO). Student f(x) = g(w_1.x/sqrt N) + g(w_2.x/sqrt N), teacher y = g(v_1.x/sqrt N) +
g(v_2.x/sqrt N), g(z) = erf(z/sqrt 2), output weights fixed to 1, v_n.v_m/N = delta_nm, inputs x ~ N(0, I_N),
noiseless labels. Online SGD w_i <- w_i + (eta/sqrt N) g'(w_i.x/sqrt N)(y - f(x)) x, one fresh sample per step,
time t = steps/N. Initialization w_i(0) i.i.d. uniform on the sphere of radius sqrt(N q0). Order parameters
Q_ik = w_i.w_k/N, R_in = w_i.v_n/N. Prove, for each eta in an interval where the symmetric fixed point below is
hyperbolic with one unstable direction: the specialization time tau_N = inf{t : |R_11 - R_12| > delta} satisfies
tau_N / log N -> 1/(2 lambda(eta)) in probability, where lambda(eta) is the unstable eigenvalue of the Saad-Solla ODE
at its symmetric fixed point; and after tau_N the generalization error tends to 0.

## FRONTIER
- Saad and Solla, Phys. Rev. E 52 (1995) 4225 (and Biehl, Riegler, Woehler 1996): the overlap ODEs, the symmetric plateau
  and its escape by linearization, in the physics sense (N = infinity first, then a small asymmetric seed).
- Goldt, Advani, Saxe, Krzakala, Zdeborova arXiv:1906.08632, Theorem 1.1: for a FIXED horizon T the expected maximum
  overlap error is at most C(T)/sqrt N. Nothing on log N times, where C(T) grows like e^{LT} and the bound is useless.
- Ben Arous, Gheissari, Jagannath arXiv:2206.04030: ballistic (ODE) and diffusive (SDE) limits of summary statistics of
  online SGD, including diffusive limits about fixed points of the effective dynamics; their examples include two-layer
  networks for Gaussian-mixture classification, not the committee plateau.
- arXiv:2511.02258 (2025): diffusive limits near fixed points for single-layer networks are Ornstein-Uhlenbeck; at
  information exponent 2 a fixed point can become repelling. Single neuron only.
- arXiv:2512.16556 (2025): annealed statistical-mechanics description of the ReLU committee from finite to ultra-wide
  width. Not a dynamics theorem.
- arXiv search 16 Oct 02:4x (five queries, newest first): no rigorous log-time escape theorem for the committee plateau.

## ARCHITECTURE
Three phases. (a) From R(0) ~ N^{-1/2} the mean direction is learned in O(1) time: at R = 0, dR_in/dt =
eta <g'(x_i)> <y_n g(y_n)> > 0 (the teacher sum has a nonzero linear Hermite part), so the student reaches a
neighbourhood of the symmetric fixed point while the transverse coordinate U = R_11 - R_12 (and its Q partner) stays
O(N^{-1/2}); the fixed-horizon theorem covers this. (b) Near the fixed point, rescale sqrt N * (transverse coordinates):
by the diffusive-limit theory it should follow dU = lambda U dt + sigma dB with sigma > 0 (SGD noise does not respect
the symmetry), so |U| ~ e^{lambda t} |U_0 + sigma int_0^t e^{-lambda s} dB_s| reaches order sqrt N at
t = log N / (2 lambda) + O_P(1). (c) After escape, the ODE from an O(1) asymmetric state converges to R = I (checked
numerically below); the fixed-horizon theorem covers the remaining O(1) time.

## FAILURE POINT
Gluing (b): the diffusive limit near a fixed point is proved on time windows of order 1 in the rescaled clock, and
here the window is log N long while the deterministic coordinates sit on the slowly attracting stable manifold. Two
quantitative inputs are missing: a linearization bound uniform over [0, c log N] for the transverse coordinates (the
Lipschitz constant of the drift enters as e^{L t}, so the errors must be measured relative to e^{lambda t}, not in
absolute terms), and a nondegeneracy statement sigma > 0 for the transverse noise at the plateau. Second, the stable
spectrum has two eigenvalues of order eta^2 (below): convergence ONTO the plateau is slow (time of order 1/eta^2), so
for small eta the trajectory escapes before it settles, and the proof cannot assume it starts at the fixed point.

## SHAPE
Days to weeks. The ODE side is finite and explicit (seven overlaps for K = M = 2; the eigenvalue is computable to any
precision and its small-eta coefficient is a closed-form integral). The probability side reuses the diffusive-limit
machinery of 2206.04030 with one new ingredient (the log N window). Finite-N simulation of SGD (cheap: N up to 10^4,
2 x 10^4 x N steps) tests the prediction tau_N ~ log N / (2 lambda) before anyone proves it.

## OBSTRUCTION
Log-time control of a high-dimensional stochastic process near a hyperbolic saddle of its effective dynamics. Every
existing SGD scaling theorem is either fixed-horizon (ODE) or local (SDE about a fixed point); none stitches them over
a log N horizon for a saddle with slowly attracting stable directions. Moves: the escape theorem for K = M = 2 erf;
an explicit lambda(eta); the same for general K = M (programme beyond that: global convergence for every K >= M).

## SETTLED
- Computed here (16 Oct, scm_plateau.py; Saad-Solla closed forms for erf, finite-difference Jacobian, residual
  <= 2e-16). Symmetric fixed point and the seven Jacobian eigenvalues:
    eta 0.002: Q = 0.333438, C = Q_12 = 0.333308, R = 0.408267; lambda = 1.31483e-4; stable -2.7e-8, -5.1e-8, -1.18e-3, ...
    eta 0.01 : Q = 0.333859, C = 0.333208, R = 0.408343; lambda = 6.57076e-4; stable -6.7e-7, -1.3e-6, -5.9e-3, ...
    eta 0.1  : Q = 0.338824, C = 0.332031, R = 0.409235; lambda = 6.53158e-3; stable -6.9e-5, -1.3e-4, -5.9e-2, ...
    eta 0.5  : Q = 0.367720, C = 0.325386, R = 0.414394; lambda = 3.16182e-2
    eta 1.0  : Q = 0.435085, C = 0.310213, R = 0.426138; lambda = 5.91404e-2
    eta 1.5  : Q = 0.604588, C = 0.269659, R = 0.453778; lambda = 7.63640e-2 (a complex stable pair appears)
  As eta -> 0 the plateau tends to Q = C = 1/3, R = 1/sqrt 6 and lambda/eta -> 0.06574 (0.065742 at eta 0.002).
  Exactly one positive eigenvalue at every eta tried; two stable eigenvalues are of order eta^2.
- Check of the code (scm_check.py, eta 0.5): from asymmetric seeds of size 1e-2, 1e-3, 1e-4 in R_11 the ODE specializes
  at t = 139, 217, 293 and converges to R = I, Q = I (error 6e-16). Each factor 10 in the seed costs 76-78 time units;
  the linearization predicts ln 10 / lambda = 72.8.
- The fixed-horizon ODE limit is a theorem (1906.08632 Thm 1.1); the plateau, its escape and the specialization are
  physics-level since 1995.
- NOT moves: the noisy-label case (positive residual error, a different question); annealed or replica descriptions;
  more numerics of the ODE alone.
- Exact finite-N SGD at O(1) cost per step (16 Oct, scm_sgd_exact.py / scm_sgd_exact_nb.py): with Gaussian inputs the
  online step depends on x only through the four fields (W x, B x)/sqrt N and |x|^2/N, so the seven order parameters
  form an exact Markov chain: y ~ N(0, I_2), h = R y + chol(Q - R R^T) xi, |x|^2/N = (|y|^2 + |xi|^2 + chi^2_{N-4})/N.
  Checked against brute-force SGD (scm_sgd_escape.py, 20 runs): N 500 103.3 +- 5.8 vs 109.25 +- 2.55; N 1000
  122.1 +- 9.7 vs 126.19 +- 2.58. Symmetric start at the scale of a random initialization, eta 0.5, tau = first time
  the specialization gap reaches 0.2, 200 runs each:
    N   500 109.25 +- 2.55 | 1000 126.19 +- 2.58 | 2000 131.59 +- 2.55 | 4000 147.69 +- 2.83 | 8000 153.73 +- 2.54
    N 16000 172.92 +- 2.76 | 32000 179.71 +- 2.59 (sgd_exact_eta0.5.txt). Weighted fit over N 1000..32000: 16.34 +- 0.90 per unit
  of log N (+ 10.6), against the ODE prediction 15.81 for eta 0.5; sd about 36 at
  every N, the sd of log|Gaussian| divided by the growth rate. So tau = (1/(2 g)) log N + O(1) with all escapes finite.
- Which rate: scm_transverse.py (transverse_eta0.50.tsv) integrates the ODE from the symmetric start and the growth
  rate g(t) of the antisymmetric direction along it: 0.0167 at t = 0, 0.0268 at 40, 0.0287 at 100, 0.0301 at 200,
  0.0310 at 400, tending to lambda = 0.0316 only slowly, because the approach to the plateau runs on the two order-eta^2
  stable eigenvalues (|Q - q*| 1.8e-2 at t = 200, 6.4e-3 at 400). At reachable N the escape happens during the
  approach, so the log N slope is 1/(2 g(tau)) = 17-17.5 for tau = 110-155, not 1/(2 lambda) = 15.8; the data (16.0 +- 1)
  cannot yet separate them. For a theorem: the finite-N crossover is governed by the order-eta^-2 approach time; the
  clean statement tau ~ log N / (2 lambda) holds only once log N / (2 lambda) is long compared with that approach time.
- TARGET 2 DONE (16 Oct, lam_closed.py, lam_closed_K.py): as eta -> 0 the ODE is the population gradient flow and the
  symmetric fixed point has every student equal to r (v_1 + ... + v_K) with r^2 = 1/(K(2K-1)), so Q = C = 1/(2K-1)
  (1/3 at K = 2) and R = r; it lies in the teacher span, so the linearization is the Hessian of eps_g in the K^2
  coordinates w_i . v_n. Its only negative eigenvalue is the antisymmetric mode (student 1 to v_1 - v_2, student 2 to
  v_2 - v_1), exactly:
      lim_{eta -> 0} lambda(eta)/eta = 2K / (pi sqrt(2K - 1) (2K + 1)^(3/2))
  = 4 sqrt 15/(75 pi) = 0.0657498 (K = 2), 6 sqrt 35/(245 pi) = 0.0461179 (K = 3), 8 sqrt 7/(189 pi) = 0.0356474 (K = 4),
  each found symbolically by sympy; at K = 5 the formula gives 10/(33 sqrt 11 pi) = 0.0290830 and the sympy run
  (lam_closed_K5.txt) returns 10 sqrt 11/(363 pi) = 0.0290830430, the same number. Large K: ~ 1/(2 pi K). Agrees with the eta = 0.002 / 0.01 eigenvalues (0.0657415, 0.0657076: an O(eta)
  correction). The K = 2 Hessian eigenvalues at the point, times pi/sqrt 15: 56/75, 36/75, -4/75, 0 (the zero is the
  degenerate direction behind the order-eta^2 stable eigenvalues). Whether Saad-Solla 1995 state it was not checked.

## TARGETS
1. Prove tau_N / log N -> 1/(2 lambda(eta)) in probability for K = M = 2, erf, noiseless, eta small (or in an explicit
   interval), including sigma > 0 for the transverse noise at the plateau.
2. Closed form of lim lambda(eta)/eta (numerically 0.06574) from the symbolic linearization of the erf ODE at
   Q = C = 1/3, R = 1/sqrt 6, and the general-K value; read Saad-Solla 1995 first, which may already state it.
3. Simulation check of target 1 before the proof: SGD at N = 500, 1000, 2000, 4000, 8000, eta = 0.5, twenty runs each;
   fit tau_N against log N and compare the slope with 1/(2 lambda) = 15.8.

## TARGET 1 ENTRY HYPOTHESIS: C7 (added 2026-10-16 by agent A, on agent H's note of 07:43Z)
- C7 (agent H, lead-authored; files (local dir) C7_deterministic_entry.md, scripts, logs,
  SHA256SUMS): computer-assisted, exact outward interval arithmetic (160-bit fixed point, no floats in a checked inequality). For
  every eta in E = [4999999999/10^10, 5000000001/10^10] (C6's interval) the fully symmetric slice (Q11 = Q22, Q12, all R equal) of
  the K = M = 2 erf overlap ODE, eta^2 term included, started at (q, c, r) = (1, 0, 0), exists for all time and converges
  exponentially to C6's plateau; the slice is invariant, so the spherical start Q(0) = I, R(0) = 0 reaches the symmetric saddle
  along its stable manifold. Method: 1069 rational Hermite nodes on [0, 1600], a per-segment eigenframe bound
  d|z|/dt <= mu_k |z| + d_k chained over six pieces, then a trap (rho = 1/5000, mu* = -1.8006e-3) around the plateau.
- With C4 (accepted conditional on this entry), C5 and C6 this discharges C4's deterministic-entry hypothesis for eta in E and
  q0 = 1 only. Still open: a nondegenerate eta interval (E is 2e-10 wide), other q0, post-exit recovery.
- Review (agent A, 16 Oct 10:5x, partial): SHA256SUMS all match; chain_check.py rerun on the logs prints CHAIN CLOSED
  (p1 -> p2 r_out 5.13e-6 <= 1e-4; p2 -> p3b 1.0614e-4 <= 1.07e-4; p3b -> p4 6.41e-5; p4 -> p5 4.03e-5; p5 -> p6 3.08e-6; last
  r_out 1.06e-5 <= trap r_end 1e-4; C6 box maps into z-radius 3.17e-7 < rho). The p2 -> p3b hand-off has under 1 percent margin:
  any change to piece 2 (step size, nodes, eta interval) should be expected to break that link first. Not yet done by an
  independent reader: rerunning a piece, reading segment() and trap() against the method. A rerun of the trap from the scripts is
  recorded below when it finishes.
- 2026-10-16 10:4x agent A: the trap rerun from a scratch copy of the C7 scripts ends with a line identical to logs/trap.jsonl:
  PASS at rho 1/5000, nsplit 1, the same exact rational mu = -328951348664188932247997894229931309293486829 /
  182687704666362864775460604089535377456991567872 (about -1.8006e-3). Not yet done: the pieces, and a read of segment() and trap().
- 2026-10-16 11:3x agent A, at agent H's request: C7 is copied into rows/T240/C7_entry/ (the note, scripts, logs,
  SHA256SUMS; __pycache__ left out). sha256sum -c there: 20 of 20 OK.

## TARGET 1 ENTRY OVER AN ETA CELL: C8 (added 2026-10-18 02:4x by agent H, lead-authored; four independent reviews ACCEPT)
- C8 (files rows/T240/C8_eta_cell/: C8_eta_cell.md, scripts, logs, SHA256SUMS; sha256sum -c 25 of 25 OK on 18 Oct): for every
  eta in E8 = [2499/5000, 2501/5000] (width 4e-4, against C7's 2e-10) the symmetric slice from (1, 0, 0), eta^2 term included,
  exists for all time and converges exponentially to an equilibrium x*(eta) which is, on each of 64 cells of width 1/160000
  tiling E8, the certified C6-type plateau root (Krawczyk, physical, slice Hurwitz, antisymmetric block stable, teacher-odd
  pair with lambda >= 0.0315 > 0). Method as C7 with a reference affine in eta (xhat + (eta - 1/2) yhat), the defect enclosed
  over (t, eta) by second-order jets in (q, c, r, eta), log norms over the cell, and a trap ball of radius 2e-4 about a centre
  moving with eta (mu* <= -7.534e-4). chain_check_eta.py prints CHAIN CLOSED. Float sanity: certified radii loose by about 50x
  at the cell ends, never exceeded.
- With C4, C5 and the per-cell plateau tests this would discharge C4's deterministic-entry hypothesis for every eta in E8 at
  q0 = 1. Needs an independent reviewer before it counts (Codex is idle until about 20 Oct; a peer Claude replay of the
  trap, one piece and the plateau cells is enough to start).
- Review 1 (agent C, 18 Oct 05:4x-06:1x, rows/T240/reviews_agent_C/C8_REVIEW.md): ACCEPT for eta in E8 and
  q0 = 1. Reran chain_check_eta, segments k = 0, 356, 1045, the trap with its exact mu*, plateau cells 1, 32, 64: identical to
  the logs. Drivers checked against each other and against finite differences; iv_exact rounding read. Thin margin at the
  q6b -> q6c junction (relative 1e-4): correct as computed, the first thing to break if a piece changes.
- Review 2 (agent K, 18 Oct, rows/T240/reviews_agent_K/C8_review.md): ACCEPT as stated, resting on the
  iv_exact/iv_scm/iv_h2 library that C6/C7 use. Read segment, run_piece, run_trap, chain_check, the eta cell widening and the
  C7 helpers in entry.py line by line. From a fresh copy with no node cache: segments 0-2 identical to q1, 1065-1068
  identical to q6d with the same exact r_out, the trap identical (rho 1/5000, two cells, same exact mu), four plateau cells at
  both ends of E8 identical. One unstated assumption: each piece reads its r_in in frame(nodes[k0]) recomputed by a float
  eigensolver in a new process; every switch norm reproduced bit for bit, but the chain check should compare a hash of the
  rational frame at each piece boundary.
- Review 3 (agent A, 18 Oct, rows/T240/C8_review_agent_A.md): PASS. Read entry_eta, widen_eta and
  chain_check_eta line by line (the mean-value split of the defect, d_t g and d_eta g by hand, the a priori box, the frame
  switch at q6b/q6c, the trap's two frames, the parametric Krawczyk test). Independent checks: 3,672 jet entries against
  finite differences, none outside; sampled defect at most 0.274 of the logged d on all 1,069 segments; Radau solutions at
  nine etas with |z|/r <= 2.15e-2 and every limit inside its plateau box; the exact trap rerun gives the identical rational
  mu; q6d rerun rows equal the shipped rows except elapsed time; sha256 25 of 25; CHAIN CLOSED. Minor: chain_check does
  not assert that every piece used the same T and W (each piece head records nseg_total 1069, t0 and t1, which match the
  T = 1600, W = 0.004 node grid, but the check should say so).
- Review 4 (agent B, 18 Oct, rows/T240/reviews_agent_B/REVIEW_C8.md): PASS. sha256 25 of 25; defect
  enclosure re-derived; piece junctions bit-identical from a fresh reference build; chain_check byte-identical; three
  plateau cells rerun and pass; a Monte Carlo of the SGD increments agrees with the closed form (all |z| < 1.9). C8 starts
  at node 0 = (1, 0, 0) with r_in = 0 and needs nothing from C7's exit set. Remark: hash the reference cache into each piece
  header so chain_check can enforce it. All four reviewers are Claude sessions on one account: independent re-derivations,
  not distinct-model reviews.
- Frame check (agent H, 18 Oct 06:3x, rows/T240/C8_frame_check/, C8 folder untouched): in one process, rebuilt the
  frames beside each piece boundary (nodes 89, 178, 267, 356, 700, 1020, 1045) and recomputed the logged switch norm on both
  sides of each (the previous piece's last segment and the next piece's first); all fourteen equal the logged floats bit for
  bit, and the trap's offset and need_rho at node 1069 (which depend on its two frames) reproduce exactly. FRAMES REPRODUCED.
- Wider eta: the frozen frame fails at half-width 1e-3; going further needs eta-dependent frames or more cells. Other q0 and
  post-exit recovery remain open. Post-exit recovery is started as C9 in (local dir) (lead scratch).
