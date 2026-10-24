Runtime model family exposed to this session: **GPT-5.6 Sol**. Applied reasoning-effort metadata is **UNVERIFIED**; no GPT-6 / maximum-effort receipt is exposed or claimed.

# P20 T10 — reference-profile subeigenvector variational certificate for Exp(1) diagonal FPP

Date: 2026-09-20 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Controlling directive: `operations/PROGRESS20_2026-09-20.md`.  
Canonical parent: `operations/claims/PROB10-10.md`.  
Model: nearest-neighbor **undirected** FPP on `Z^2` with iid physical-edge weights `Exp(1)`.  
Status: **PARTIAL / OPEN** for the source problem. The theorem arguments below are **CANDIDATE_PROVED pending later independent review**. No completed certification, publication, novelty, or priority claim is made.

## 1. Source-facing accounting and exact source

The exact parent remains Auffinger--Damron--Hanson, *50 years of first passage percolation*, arXiv:1511.03262, Question 4 in §2.5.1:

> Show that if `F` is a continuous distribution then the limit shape is strictly convex.

Section 2.8 discusses strict convexity as conjectural. The present repository claim freezes the iid `Exp(1)`, undirected nearest-neighbor `Z^2` specialization.

Let `mu` be the deterministic time-constant norm and

`Delta_12 := 2 mu(e1)-mu(1,1) >= 0`.

The retained rigorous lower certificate is

`mu(e1) >= b := 3002823/10000000 = 0.3002823`.

Therefore the first axis/diagonal checkpoint would follow from

`mu(1,1) < 2b = 3002823/5000000 = 0.6005646`.

Original-problem metric:

- **before:** largest proved `c_*` with `Delta_12 >= c_*` is `0`;
- **after:** `c_*=0`.

Thus this run does **not** prove the axis/diagonal defect and certainly does not close full strict convexity.

A bounded fresh literature check on 20 September 2026 again found no unconditional theorem settling this exact ordinary iid Exp(1), undirected nearest-neighbor model. The known boundaries remain the ones already preserved by the canonical claim: Lalley's strict-convexity theorem is conditional; Dembin--Elboim--Peled's quantitative coalescence theorem assumes substantial extreme-point information about the limit shape; Jacquet's unrestricted-versus-directed comparison is a different inequality. Directed integrable models and sampled numerical curvature are not imported as evidence for this target.

## 2. Continuity, failures, and why this run changes the object

I read only the essential current dependencies:

1. `operations/PROGRESS20_2026-09-20.md` and the LIVE20 P20/P04 T10 pairing;
2. `operations/claims/PROB10-10.md`;
3. P20's immediately preceding report `proofnet24/P20-progress-fpp/runs/2026-09-20/2026-09-20T15-38-56Z__ancestor-fixed-point-bellman.md`;
4. the current canonical source-domination/pruning report `runs/prob10_2026-09-20/PROB10-10/20260920T1448Z__source-domination-pruning.md`;
5. P04's latest report found on master, `proofnet24/P04-progress-curvature/runs/2026-09-20/2026-09-20T15-45-27Z__adaptive-margin-new-wedge1356756.md`;
6. R08's source-facing stuck report and retained failure history;
7. the displaced cyclic-interval proof only for the short preservation handoff in §11.

The binding failures remain preserved:

- shared bypasses invalidate multiplication of nominally independent local surgery gains;
- exact finite triangle equality occurs on positive-probability cylinders, so pointwise finite strictness is false;
- fixed-corner exact square blocks through the historical tested sizes did not reach the diagonal threshold;
- first-moment SAW/Chernoff counting has a diagonal obstruction from the exponentially numerous monotone E/N paths;
- reflected strict-triangle cones are compatible with the exact `l1` diamond and therefore do not move `Delta_12`;
- the true-geodesic Busemann/Jacquet route can collapse under the flat-face hypothesis to near-co-calibration, leaving a global rigidity obstruction;
- sampled carry estimates below `0.6005646` are screens, not proofs.

The previous P20 run replaced continuous-profile verification by a flat-reference ancestor kernel `(q,K)`. Its exact theorem is sound enough to motivate the present attack, but a source-relevant certificate still seemed to require computing both first-hit expectations and a finite-dimensional ancestor stationary vector. This run removes the ancestor-kernel computation altogether: a single deterministic **reference profile** and finitely many expected output labels are enough.

## 3. Fresh-band min-plus operator

Fix a finite diagonal band of longitudinal length `L` and transverse half-width parameter `W`, with the same finite offset set

`D={1,...,M}`

on its input and output antidiagonal boundaries. For a realized fresh band environment `omega`, let

`d_omega(i,j)`

be the restricted passage metric from input offset `i` to output offset `j`. For any finite vector `y in R^M`, define

`F_omega(y)_j := min_i {y_i+d_omega(i,j)}`,

`g_omega(y) := min_j F_omega(y)_j`,

`Phi_omega(y) := F_omega(y)-g_omega(y) 1`.

Let the deterministic expected min-plus operator be

`T(y) := E F_omega(y)`.

Translation covariance is exact:

`F_omega(y+c1)=F_omega(y)+c1`, hence `T(y+c1)=T(y)+c1`.

For later evaluation we may therefore normalize any reference profile by subtracting its minimum, so it becomes a vector of nonnegative deterministic source-activation delays.

## 4. P20-FPP-REFERENCE-SUBEIGENVECTOR-48 — CANDIDATE_PROVED

### Theorem

For a deterministic reference profile `z`, define

`Lambda(z) := max_j { T(z)_j-z_j }`.                              (4.1)

Then the exact asynchronous fresh-band carry satisfies

`mu(1,1) <= Lambda(z)/L`.                                        (4.2)

Consequently

`Delta_12 >= 0.6005646-Lambda(z)/L`.                             (4.3)

In particular, a rigorous finite-band certificate

`T(z)_j <= z_j+lambda` for every output `j`,                     (4.4)

with

`lambda < 0.6005646 L`,                                         (4.5)

proves `Delta_12>0`.

The certificate needs **no** continuous profile cover, no profile projection, and no explicit ancestor kernel.

### Proof

Fix `z`. For each output coordinate `j`, select measurably a minimizing input at the reference profile:

`I_j^z(omega) in argmin_i {z_i+d_omega(i,j)}`.                   (4.6)

Continuity of the edge law gives uniqueness almost surely, although an arbitrary measurable tie rule is sufficient.

Define the column-stochastic reference-ancestor kernel

`K^z_ij := P(I_j^z=i)`.                                          (4.7)

Because each column sums to one, the probability simplex is invariant under `K^z`, so there exists a probability vector `alpha` satisfying

`K^z alpha=alpha`.                                               (4.8)

For an arbitrary finite incoming profile `y`, the reference minimizer is an admissible competitor in the definition of `F_omega(y)_j`. Pathwise,

`F_omega(y)_j`
` <= y_{I_j^z}+d_omega(I_j^z,j)`
` = F_omega(z)_j + (y-z)_{I_j^z}`.                              (4.9)

Multiply by `alpha_j`, sum in `j`, and take expectation. Using (4.8),

`E[alpha dot F_omega(y)]`
` <= alpha dot T(z) + (K^z alpha) dot (y-z)`
` = alpha dot y + alpha dot (T(z)-z)`
` <= alpha dot y + Lambda(z)`.                                  (4.10)

Since `sum_j alpha_j=1`,

`g_omega(y)+alpha dot Phi_omega(y)=alpha dot F_omega(y)`.        (4.11)

Thus the linear projective corrector `h(y)=alpha dot y` satisfies the global Bellman inequality

`E[g_omega(y)+h(Phi_omega(y))]-h(y) <= Lambda(z)`                (4.12)

for **every** finite incoming profile `y`.

Now concatenate iid fresh length-`L` bands using the already-established exact asynchronous carry. Let `M_k` be the accumulated minimum and `Y_k` the normalized boundary profile after block `k`. Starting after the first connected band, condition on the past and telescope (4.12):

`E[M_N+h(Y_N)]`
` <= E[M_1+h(Y_1)] +(N-1)Lambda(z)`.                             (4.13)

Because `Y_N>=0` coordinatewise and `alpha` is a probability vector, `h(Y_N)>=0`. The standard fresh terminal staircase from the minimizing output offset back to the central offset uses at most `W` fresh edges, hence has expected cost at most `W`. The first-band term is finite. Therefore

`E T(0,(NL,NL))`
` <= (N-1)Lambda(z)+E[M_1+h(Y_1)]+W`.                            (4.14)

Divide by `NL` and let `N->infinity`; ordinary `L^1` convergence of passage times to the time constant gives (4.2). Equation (4.3) uses `2mu(e1)>=0.6005646`. QED.

### Rigorous interval version

Suppose a finite-state evaluator returns one-sided bounds

`T(z)_j <= Tbar_j`                                               (4.15)

for all `j`. Then it is enough to set

`lambdabar := max_j(Tbar_j-z_j)`.                               (4.16)

The conclusion is

`mu(1,1) <= lambdabar/L`,                                       (4.17)

and a strict rational check `lambdabar < 0.6005646 L` closes the axis/diagonal checkpoint. No approximation of `K^z` enters the error ledger.

## 5. Explicit finite-to-infinite error

The transfer above can be made completely quantitative. Let `m_{L,W}` be the number of physical edges in one finite band. Starting from the zero profile, every output is reachable by a path lying in the connected band and the passage cost of such a path is at most the sum of all block-edge weights. Hence

`M_1+h(Y_1)=alpha dot F_omega(0)`
` <= max_j F_omega(0)_j`
` <= sum_{e in E_band} tau_e`,                                  (5.1)

so

`E[M_1+h(Y_1)] <= m_{L,W}`.                                     (5.2)

Therefore, for every `N>=2`,

`E T(0,(NL,NL))`
` <= (N-1)Lambda(z)+m_{L,W}+W`,                                 (5.3)

and in particular

`E T(0,(NL,NL))/(NL)`
` <= Lambda(z)/L +(m_{L,W}+W)/(NL)`.                            (5.4)

Thus the only block-to-infinite-volume loss in this certificate is an explicit `O(1/N)` interface term. This is the form intended for P04 coordination.

## 6. P20-FPP-MEAN-MINPLUS-COLLATZ-WIELANDT-49 — CANDIDATE_PROVED

The preceding theorem is not merely a one-off bound: there is an optimal deterministic reference profile for the expected block operator.

### Proposition

The expected min-plus map `T:R^M->R^M` has an additive eigenpair

`T(z_*)=z_*+lambda_* 1`.                                        (6.1)

Moreover

`lambda_* = inf_{z in R^M} max_j {T(z)_j-z_j}`.                 (6.2)

Consequently

`mu(1,1) <= lambda_*/L`.                                        (6.3)

### Proof

For every realization, `F_omega` is coordinatewise monotone, additively homogeneous, and 1-Lipschitz in `||.||_infinity`; expectation preserves these properties. Along the finite output boundary, the passage-time difference between any two output labels is bounded by the passage cost of the fixed output-boundary chain joining them. Its expected total cost is at most `2W`. Therefore

`span T(y) <= E span F_omega(y) <= 2W`                           (6.4)

for every `y`.

Fix one coordinate `j0` and the compact convex set

`C={z in R^M : z_{j0}=0, span(z)<=2W}`.                          (6.5)

Define

`G(z)=T(z)-T(z)_{j0} 1`.                                        (6.6)

By (6.4), `G(C) subset C`; continuity of `T` makes `G` continuous. Brouwer's fixed-point theorem supplies `z_* in C` with `G(z_*)=z_*`. Setting `lambda_*=T(z_*)_{j0}` proves (6.1).

For arbitrary `z`, set

`Lambda=max_j(T(z)_j-z_j)`.                                     (6.7)

Then `T(z)<=z+Lambda 1`. Monotonicity and additive homogeneity imply inductively

`T^n(z)<=z+n Lambda 1`.                                         (6.8)

Choose `c` so that `z_*<=z+c1`. Then

`z_*+n lambda_*1`
` =T^n(z_*)`
` <=T^n(z+c1)`
` =T^n(z)+c1`
` <=z+(nLambda+c)1`.                                            (6.9)

Divide coordinatewise by `n` and let `n->infinity`; `lambda_*<=Lambda`. Since `Lambda(z_*)=lambda_*`, equality (6.2) follows. Finally apply Theorem 48 at `z_*`. QED.

### Interpretation

This produces the explicit finite-dimensional variational upper bound

`mu(1,1)`
` <= (1/L) inf_z max_j [ E min_i {z_i+d_omega(i,j)} - z_j ].     (6.10)

It is a nonlinear Perron--Frobenius / min-plus subeigenvector mechanism. The original random profile process need never be discretized: only the expected block operator is sampled/evaluated during the search, and a final proof uses rigorous one-sided expectations at one deterministic reference profile.

## 7. Demonstrated exact finite gain on the smallest nontrivial band

I implemented a rigorous finite sanity/certificate for the `L=1, W=2` diagonal band (8 vertices, 8 physical edges). The code uses exact Python `Fraction` arithmetic for the finite continuous-time Richardson recursion. For deterministic delayed source activation it evaluates the augmented backward equation by an 80-term exact Taylor polynomial and bounds the omitted tail by an explicit rational infinity-norm geometric majorant.

Reference profile:

`z=(57/100,0,57/100)`.                                          (7.1)

The executed enclosure is

`T_outer(z) = 1.6818230921197506...` with Taylor tail `<1.21e-53`,

`T_center(z)= 1.1130108523220166...` with Taylor tail `<7.08e-57`.

Therefore

`Lambda(z) < 1113011/1000000 = 1.113011`.                       (7.2)

The preceding **flat-reference ancestor** theorem on this identical `L=1,W=2` block had the exact value

`lambda_flat=43/36=1.1944444444...`.                            (7.3)

Thus the present nonflat reference profile rigorously improves that one-band Bellman constant by at least

`43/36 - 1113011/1000000`
` = 732901/9000000`
` = 0.081433444444444...`.                                      (7.4)

This is about a `6.8%` reduction in the certified block constant. It is a **demonstrated mechanism gain**, not source-level curvature: `1.113011` is still far above the source threshold `0.6005646` at `L=1`.

Essential executed artifacts:

- `proofnet24/P20-progress-fpp/artifacts/2026-09-20/2026-09-20T16-10-13Z__reference-subeigenvector-exact.py`, creation commit `e7b9c1eb102eb577f40261985f7cb5236528e317`;
- `proofnet24/P20-progress-fpp/artifacts/2026-09-20/2026-09-20T16-10-13Z__reference-subeigenvector-exact.out`, creation commit `6974622dd52a5911db73402263262edeab021467`.

The archived output ends

`P20-REFERENCE-SUBEIGENVECTOR-EXACT-SANITY: ALL_EXACT_CHECKS_PASS`.

The computation is only a finite theorem check and a comparison of rigorous Bellman constants. It is not sampled numerical curvature and is not used to claim `Delta_12>0`.

## 8. P04 / canonical-owner handoff

P04's current reflected-cone improvement remains a genuine restricted-direction theorem but, as already corrected in this track, it is compatible with an `l1` diamond and therefore does not move the source-facing `Delta_12`. Its useful infrastructure here is the dependence-controlled fresh-block architecture and finite-to-infinite accounting.

Theorem 48 changes P04's source-facing finite task substantially. One no longer needs to certify all incoming profiles, or even compute an ancestor kernel. It is enough to do the following for one candidate deterministic profile `z`:

1. normalize `min z=0`;
2. for each output coordinate `j`, rigorously upper-bound the finite multi-source passage expectation
   `T(z)_j=E min_i{z_i+d_omega(i,j)}`;
3. check the finite list of inequalities
   `Tbar_j-z_j < 0.6005646 L`;
4. invoke (5.4) for the controlled finite-to-infinite transfer.

The canonical source-domination theorem can be inserted before step 2: delayed sources that are dominated by nearby earlier sources may be deleted with its explicit Gamma positive-part error. Edge deletion is also one-sided for an upper passage-time certificate. Thus a source-relevant rigorous computation may combine:

- a screened approximate eigenprofile only to **choose** `z`;
- deterministic source pruning with explicit error;
- P04-style physical-edge finite blocks;
- rigorous Richardson/Dijkstra expectation intervals for the remaining sources;
- the single scalar final check `max_j(Tbar_j-z_j)<0.6005646 L`.

No empirical screen is itself admitted into the proof.

## 9. Residual obstruction and honest failure report

The conceptual Bellman/profile obstruction has been reduced, not eliminated. At source-relevant widths and lengths, exact subset-state Richardson recursion still grows exponentially. This run does **not** contain a rigorous `L,W,z` satisfying the source threshold.

The remaining bottleneck is now finite and sharply stated:

`Find L,W,z and rigorous Tbar(z) such that`

`max_j [Tbar_j(z)-z_j] < 0.6005646 L`.                           (9.1)

Compared with the preceding run, the required rigorous data have dropped from an entire pair `(q,K)` plus a stationary/fixed-point error to only `M` scalar output expectations at one profile. Compared with the earlier box/net Bellman routes, the uncountable profile state has disappeared completely.

A brute-force width-48 subset recursion is not a viable next step by itself. The next attack is a frontier/pathwidth-compressed delayed-Richardson evaluator, one output coordinate at a time, with canonical source-domination pruning and one-sided interval arithmetic. A nonrigorous value iteration may propose a near-eigenprofile `z`, but every final coordinate bound must be rigorous. If that still fails twice at source-relevant widths, the preserved true-geodesic residual/Jacquet route is the materially different fallback rather than another larger brute-force subset enumeration.

## 10. Original-problem versus mechanism ledger

**Original problem:**

- `Delta_12` certified lower constant before: `c_*=0`;
- after: `c_*=0`;
- full ADH strict convexity: **OPEN** in this track.

**Demonstrated mechanism gain:**

- before: flat-reference global Bellman certificate required finite `(q,K)` and a stationary vector or approximate fixed-point residual;
- after: one deterministic reference profile with `M` rigorous scalar expectations suffices;
- new variational characterization: `lambda_*=inf_z max_j(T_j(z)-z_j)` for the expected finite-band min-plus operator;
- exact `L=1,W=2` demonstration lowers the preceding flat-reference Bellman constant from `43/36` to `<1113011/1000000`, a certified gain of at least `732901/9000000`;
- finite-to-infinite error is explicitly bounded by `(m_{L,W}+W)/(NL)`.

**ledger_delta:**

`P20 T10 | source c_* 0 -> 0 | NEW CANDIDATE_PROVED P20-FPP-REFERENCE-SUBEIGENVECTOR-48 + P20-FPP-MEAN-MINPLUS-COLLATZ-WIELANDT-49 | exact tiny-band Bellman constant 43/36 -> <1113011/1000000 | continuous-profile/K-kernel certification replaced by one-profile coordinatewise expectation certificate | source still OPEN | next: frontier-compressed rigorous T(z) evaluator + pruning`.

## 11. Short cyclic-interval handoff

The displaced P20 cyclic-interval proof remains preserved and is not reopened. The source-literal candidate

`P20-FOKAM-BITJOKA-CI241-SEMICIRCLE-MAJORITY-01`

remains intact. P26's genuinely independent full-proof/source-quantifier audit remains

`PASS_FULL_MATHEMATICAL_PROOF / SOURCE_LITERAL_CONJECTURE_2_41 / SOURCE_QUANTIFIERS_PASS / OWNER_FINITE_SANITY_READ / PENDING_SECOND_DISTINCT_AUDIT / PRIOR_ART_UNVERIFIED`.

The recovered gate remains `1/2`; no completed certification is implied. This run spent no research effort waiting for the missing audit.

## 12. Next attack

1. Use ordinary floating/value iteration only as a **proposal generator** for a normalized approximate additive eigenprofile of `T` at a block size already showing source-facing numerical room.
2. Freeze that rationalized `z` before certification.
3. Apply source-domination pruning to remove high-delay sources with a rigorous Gamma-tail budget.
4. Evaluate each remaining `T(z)_j` by a frontier/pathwidth Richardson recursion with outward-rounded rational or interval arithmetic.
5. Check (9.1) directly. If successful, combine with (5.4) and the retained axis lower bound to obtain an explicit positive `Delta_12`; if unsuccessful, record the certified miss rather than extrapolating sampled curvature.

No historical or peer file is overwritten by this report.

END OF P20 FPP RUN REPORT
