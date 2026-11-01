# Status

Date: 2026-06-01

## What is complete

- Literature bank created at
  `~\Downloads\probability_rmt_open_problem_bank`.
- Projection-density/small-ball references for the non-Gaussian route were
  added on 2026-05-31: arXiv:1402.4492, arXiv:1507.07949, arXiv:1503.09190.
- Main phase-retrieval/RMT manuscript exists in
  `~\phase_retrieval_omega\paper`.
- Lean project exists in
  `~\phase_retrieval_omega\lean\omega_comb`.
- Current Lean file verifies the binomial row-count bound and fixed-apex
  overlap expectation/probability identities, including central-binomial
  polynomial-over-exponential bounds for the redundancy-two `D=1` and `D=2`
  high-overlap terms, their combined bad-overlap mass, and the finite
  redundancy-two `E[1/D] <= 3/(n+1)` estimate. It also verifies the abstract
  weighted-excess estimate `E[1+C/D] <= 1+3C/(n+1)` for `C >= 0` and the
  second-moment envelope with a crude high-overlap constant `H`.
- A new Lean module `OmegaComb.DeterministicWidth` formalizes the selected-row
  Gram matrix, proves it symmetric, and proves its quadratic form equals the
  selected sum of squared row projections. It also defines the finite family of
  `k`-row subsets, the minimum selected energy over those subsets, proves the
  minimum is attained, and connects that minimum to selected-row Gram quadratic
  forms.
- The deterministic-width Lean module now also has a generic subset-weight
  minimum object, an attainment theorem for that generic minimum, and exact
  specialization lemmas identifying selected row energy with the generic
  subset-weight formulation.
- The same module now proves a certificate-form order-statistic identity:
  any `k`-subset whose weights are all no larger than the weights outside the
  subset realizes the exact finite minimum over all `k`-subsets. This has also
  been specialized to selected row-projection energies.
- For canonical `Fin n` index sets, the module now constructs the sorted
  prefix with `Tuple.sort` and proves that the finite minimum over all
  `k`-subsets equals the sum of the first `k` sorted weights.
- For `Fin n` row-indexed rational matrices, the sorted-prefix theorem is now
  specialized to squared row projections: the finite minimum over all selected
  `k`-row energies equals the sum of the first `k` sorted squared row
  projections.
- A row-Gram lower-bound bridge is formalized: if every selected `k`-row Gram
  quadratic form lower-bounds `c * ||z||^2`, then the finite min energy, and
  for `Fin n` rows the sorted `k`-smallest squared-projection sum, obeys the
  same lower bound.
- A matrix-level eigenvalue proxy is also formalized: if every selected row
  Gram matrix satisfies `forall z, c * ||z||^2 <= z^T G z`, then the same
  deterministic lower bounds follow.
- A new Plucker dominance-graph diagnostic tested a proposed signed-relation
  proof mechanism. It showed that dominant-product propagation through
  near-tight Plucker relations stays fragmented, even under relaxed graph
  rules. This rules out a naive giant-reachability proof route and points next
  to incidence-sum or packet arguments around Plucker coordinates/circuits.
- A coordinate-incidence Plucker diagnostic was added next. It shows that
  after aggregating signed relation packets by individual determinant
  coordinate, the graph becomes globally connected and has a giant strongly
  connected core for `m=5,6`; large Plucker coordinates are disproportionately
  dominant and small ones disproportionately supply opposite packets.
- A dyadic Plucker incidence diagnostic now bins determinants by relative size.
  It shows the top determinant level carries most Cauchy-Binet weight and has
  positive dominant/opposite packet role, while roughly one third of all
  coordinate-level opposite flow goes from top-level dominant coordinates to
  lower levels in quick optimized `m=5,6` runs.
- The sign-free `K5` star-ratio relaxation for the `Gr(3,5)`/dual `Gr(2,5)`
  model is now solved exactly: arbitrary nonnegative edge weights satisfy
  `min_d min_j w_dj/sum_{k != d,j} w_dk <= 1/3`, with equality only for
  uniform edge weights. This isolates the remaining real-Plucker difficulty:
  improving the bound to `(4-sqrt(5))/11` requires signed Ptolemy/Grassmann-
  Plucker structure.
- The real `Gr(2,5)` star-ratio theorem is now solved exactly. For every
  real `5 x 2` Parseval frame, squared Plucker weights satisfy
  `min_i min_j w_ij/sum_{k != i,j} w_ik <= (4-sqrt(5))/11`, with equality at
  the dual regular pentagon. The proof uses projective gaps, leverage sums,
  and a Jensen lemma.
- The rank-two theorem is now solved for every `Gr(2,n)`, `n >= 3`. For every
  real `n x 2` Parseval frame, squared Plucker weights satisfy
  `min_i min_{j != i} w_ij/sum_{k != i,j} w_ik <= alpha_n/(1-alpha_n)`, where
  `alpha_n=(2/n)sin^2(pi/n)`. Equality is attained by the uniform leverage
  regular projective `n`-gon. The `n=5` case recovers `(4-sqrt(5))/11`.
- The analytic bounded-density local-CLT inputs for P1 are now complete at
  the deterministic lemma level. The one-slab lower density follows from
  RV-scale delocalization. The two-dimensional pair local CLT no longer needs
  the temporary `phi_X in L^1` assumption: bounded density gives `phi_X in
  L^2`, and a four-factor Cauchy-Binet/Cauchy-Schwarz far-tail estimate closes
  the Fourier proof.
- For the exact subexponential-law problem, the fixed-apex count now has a
  solved first-two-moment reduction at the first-moment threshold: if
  `L_m p(t_m)=lambda`, then `E Z_{t_m}=lambda` and
  `E[Z_{t_m}(Z_{t_m}-1)]/lambda^2 = 1+O(1/m)` up to an exponentially small
  high-overlap correction. The full Poisson/Chen-Stein theorem remains open.
- The first-moment constants for the P2 distance-count proxies are now
  explicit: the fixed-apex threshold is
  `2 sqrt(2) pi lambda sqrt(m) 4^{-m}(1+O(1/m))`, while the all-apex
  distance-incidence threshold is
  `sqrt(2) pi lambda 4^{-m}/sqrt(m)(1+O(1/m))`. This identifies the natural
  all-apex subexponential scale and isolates the remaining swap-dependence
  obstruction.
- The P1 delocalization target has been corrected. A literal all-subsets
  RV-scale delocalization event is too strong for a union-bound route: a fixed
  Gaussian null normal is Haar and has only polynomial failure probability at
  threshold `A sqrt(log m/m)`, while the fixed-apex family has
  `binom(2m-2,m-1)=exp((log 4+o(1))m)` members. The right target is a
  typical-good-family theorem plus a correlation-average estimate.
- The P1 good-family target has now been reduced by exchangeability to
  random-subset estimates. A single-submatrix estimate
  `P(||u_{S_*}||_inf > A sqrt(log m/m)) -> 0` implies that the empirical
  fraction of bad fixed-apex null normals is `o_P(1)`. Similarly, empirical
  truncated correlation-kernel averages are controlled by the expectation for
  an independent uniformly random pair `(S_*,T_*)`.
- For bounded-density subgaussian entries, the single-submatrix P1
  delocalization input is now covered by the Nguyen--Vu normal-vector theorem:
  `P(||u||_inf > A sqrt(log m/m)) -> 0` for sufficiently large fixed `A`.
  Thus the subgaussian P1 route is reduced to the random-pair side.
- A D-stratified random-pair diagnostic now samples null-normal pairs
  conditioned on `D=m-|S cap T|` and compares
  `(1-rho^2)^(-1/2)` with the exact Gaussian benchmark
  `Gamma(D/2) Gamma((D-2)/2) / Gamma((D-1)/2)^2`.  The ordinary `D>=3`
  buckets track the Gaussian `1+O(1/D)` behavior for Gaussian, uniform,
  Laplace, and logistic entries up to `m=24`; the singular `D=2` bucket is
  confirmed as a separate high-overlap/projection-density error.
- The D-stratified kernel target has been reduced further to a moment/tail
  form.  For `X=rho^2` and `K=(1-X)^(-1/2)`,
  `E[K|D] <= 1 + B_theta E[X|D] + E[K 1_{X>theta}|D]`.  The diagnostic now
  reports `D*E_good[rho^2|D]` and high-correlation tail fractions; quick runs
  show `D*E_good[rho^2|D]` stays at the Gaussian scale while near-parallel
  tails concentrate at small `D`.
- The same overlap-stratified diagnostic now tracks a higher angular moment
  ladder.  For Gaussian
  residual Haar lines,
  `E rho^(2q)=prod_{j=0}^{q-1}(2j+1)/(D+2j)`, so the expected scaled
  benchmarks are `D E rho^2 ~ 1`, `D^2 E rho^4 ~ 3`,
  and `D^3 E rho^6 ~ 15`.  Focused `m=24` runs show Gaussian, uniform,
  Laplace, and logistic entries following the same scaled-moment profile for
  ordinary `D>=6` buckets, refining the target to moment bounds plus a final
  no-near-parallel edge estimate.
- The conditional residual-line coordinate reduction has been verified
  directly: for `S=A union B`, `T=A union C`, an orthonormal basis `Q_A` of
  `ker(A)` identifies the original null-normal angle with the angle between
  null lines of `(B Q_A)` and `(C Q_A)` in `R^D`, to numerical roundoff.
- The P1 random-pair target has been reduced one layer further to a conditional
  residual covariance statement.  Given shared rows `A` with
  `dim span(A)^perp=D`, the two private null normals are independent residual
  null lines in that complement.  If `M_A=E[v v^T | A]`, then
  `E[(v dot w)^2 | A]=trace(M_A^2)`.  A new diagnostic estimates
  `D trace(M_A^2)` with the self-pair bias removed; for `m=24` and
  `D=3,6,12,24`, Gaussian, uniform, Laplace, and logistic rows all stayed
  essentially at the Haar target `1`.
- A residual near-parallel tail probe now compares conditional residual null
  lines against a Haar-line baseline in the same `D`.  At `m=24`, tails and
  kernel-edge masses for thresholds `0.90,0.95,0.99` track Haar for Gaussian,
  uniform, Laplace, and logistic entries at the tested sampling budget.  The
  remaining proof target is a conditional anti-alignment/cap bound.
- The near-parallel edge now has exact Haar beta-law benchmarks.  For
  `Y=1-rho^2`, Haar residual lines have
  `Y ~ Beta((D-1)/2,1/2)`, giving explicit formulas for both
  `P(Y<=eps)` and `E[Y^(-1/2)1_{Y<=eps}]`.  A diagnostic comparing Gaussian,
  uniform, Laplace, and logistic residual lines to these formulas remains
  Haar-scale at the observable eps levels.
- The dyadic diagnostic now also tracks partner exposure. For strict
  isolated-dominant packets, the top-cut boundary-normalized lower exposure
  requirement is `1.203x` and `1.185x` the high-level dominant partner exposure
  for `m=5` and `m=6`; actual downward partner exposure is about `2.2x`.
  Relation-level pressure is also visible: median top-cut `rel_need/dom` is
  `1.434` for `m=5` and `1.505` for `m=6` in strict isolated packets.
  Template classification shows the leading pressure comes mostly from
  3-term top-top dominant packets: the top eight strict-isolated templates
  cover about `36.8%` of top-cut downward need for `m=5` and `24.2%` for
  `m=6`. This makes the deterministic Plucker bottleneck a concrete
  median/average partner-capacity inequality, starting with a Ptolemy-like
  local template.
- A new Lean module `OmegaComb.PluckerTemplate` verifies the scalar core of
  that local template: if `x,y >= L >= 0` and the lower-endpoint weighted
  opposite mass covers `x*y`, then `L*(x+y) <= 2*weighted`. The Lean build
  succeeds with `8252` jobs.
- A top-top coverage diagnostic now measures that exact coverage hypothesis.
  In strict isolated top-cut packets, coverage fraction is `0.696` for `m=5`
  but `0.458` for `m=6`; the uncovered `(0,1)` and `(0,2)` signatures are now
  the concrete incidence obstruction.
- A product-level graph for uncovered top-top packets was tested. It is
  fragmented: in quick strict `m=5,6` runs, largest weak component is only `3`
  and zero uncovered mass reaches covered top-top sources. So the next proof
  mechanism must aggregate uncovered high-high opposite products at coordinate
  or circuit level, not by product-node paths.
- A lower-star versus upper-circuit Plucker incidence diagnostic was added.
  It shows that rank-two contraction lower-star imbalance is strongly aligned
  with the upper co-star/circuit imbalance needed for the deterministic
  Balan-Wang route (`corr(log lower_best, log upper_best)` about `0.98` to
  `1.00` in `m=3..6` optimized examples). The rank-two condition is a broad
  filter rather than a proof: at `m=6`, `43.5%` of coordinates satisfy the
  lower-star bound but only `17.4%` of those are within `10C` of the best
  upper-circuit witness.
- The lower-star target has been reframed as a minimum-support codeword
  imbalance problem for real `[2m-1,m,m]` MDS-like subspaces. A longer
  `m<=6` profile gives `A(Q)^(1/m)=0.576,0.443,0.336,0.266`, while quick
  supplementary `m=6` examples show the same null-star/upper-circuit alignment
  at a more extreme short-ascent point (`A=1.865e-5`, `C=2.012e-5`,
  `corr(log lower, log upper)=0.988`). This sharpens the deterministic target
  to an extremal minimum-support-codeword residual-coordinate theorem.
- A direct lower-star optimizer was added for the actual reduced extremal
  problem `sup_Q A(Q)`, rather than measuring `A(Q)` only on `K_m`-optimized
  examples. It now supports optional `K_m` warm starts. The best direct bases
  are currently `A^(1/m)=0.5759,0.4800,0.3514,0.2765` for `m=3,4,5,6`; the
  warm-started `m=6` value is `A=4.4685e-4`, improving the earlier
  `K_m`-profile lower-star value. At `m=4`, direct optimization finds a larger
  lower-star value than the `K_m`-optimized profile, so future deterministic
  diagnostics should optimize `A(Q)` directly and preserve warm-started best
  frames.
- The first saved `m=6` direct lower-star candidate has been structurally
  inspected.  It is nearly equal-leverage (`spread ~= 1.083`), has
  `A=4.4685e-4`, `K=1.2716e-4`, and upper-circuit value
  `C=3.3625e-4` (`C/A=0.752`).  The best deletion star has residual
  probabilities `4.47e-4,1.37e-2,0.200,0.207,0.242,0.336`, suggesting the
  extremal lower-star obstruction is a structured minimum-support-codeword
  imbalance rather than a tiny-leverage artifact.
- A near-parallel residual-line tail diagnostic now targets the singular edge
  of the P1 pair kernel. It compares `P(1-rho^2<=eps)` and the truncated
  singular contribution against exact Haar incomplete-beta benchmarks. In a
  focused `m=24`, `D=3,4,6,8` run, bounded-density residual-line tails tracked
  the Haar scale at visible event probabilities; sparse high-D/small-eps rows
  are sample-size limited. This isolates the next proof step: convert
  near-parallel residual null lines into a small-singular-value or determinant
  event for a coupled projected residual matrix.
- The near-parallel edge now has a deterministic slab reduction. If residual
  null lines `v,w` satisfy `1-<v,w>^2 <= eps`, then every private row `c_j`
  of one residual block lies in the slab
  `|<c_j,v>| <= sqrt(2 eps)||c_j||`. After row-norm truncation this becomes
  `D-1` independent one-dimensional slab events, equivalently a packet of
  nearly singular augmented residual matrices. This gives the correct
  `eps^((D-1)/2)` exponent and a useful localization device, but the constants
  still need determinant-aware sharpening.
- The slab-constant audit quantifies that loss: in an iid Gaussian
  residual-coordinate model, the rowwise slab event exceeded the true Haar cap
  event by factors about `3.6,10.1,60.6,394.5` for `D=3,4,6,8` at
  `eps=0.25`.  This points back to determinant-aware least-squares geometry
  for Haar-comparable constants.
- A tail-to-kernel calculus lemma now closes the bookkeeping for that edge:
  if `P(Y<=eps) <= A eps^alpha` with `alpha>1/2`, then
  `E[Y^(-1/2)1_{Y<=eps0}] <= A*(2alpha)/(2alpha-1)*eps0^(alpha-1/2)`.
  With the slab exponent `alpha=(D-1)/2`, the ordinary `D>=3` near-parallel
  kernel contribution is finite and controlled by the slab/projection-density
  bound; `D=2` stays in the separate high-overlap fallback.
- The residual cap event has also been reduced to a least-squares small-ball
  problem. After rotating the first residual line to `e_1`, write the second
  residual matrix as `[a|B]`; then the second null line is
  `(1,-B^{-1}a)/sqrt(1+||B^{-1}a||^2)`. In the Gaussian case
  `B^{-1}a` has the exact multidimensional Cauchy law, giving
  `P(||B^{-1}a||<=r)=I_{r^2/(1+r^2)}((D-1)/2,1/2) ~ c_D r^(D-1)`.
  The non-Gaussian edge theorem is now precisely a robust version of this
  least-squares small-ball estimate.
- The least-squares route now has a clean sufficient density lemma: if the
  rotated first column `a` has conditional density at most `L_B` given the
  square block `B`, then
  `P(||B^{-1}a||<=r|B) <= L_B vol(B_2^d)|det B|r^d`.  Under row-norm
  truncation this gives the Haar-scale cap exponent `eps^((D-1)/2)`, and the
  existing tail-to-kernel lemma converts it to the ordinary `D>=3` singular
  kernel-edge bound.  The remaining analytic input is therefore a conditional
  density bound for `a|B` after the non-Gaussian projection/rotation.
- The same least-squares route now has an exact determinant-tilted density
  formulation.  If `g_U(s,b)` is the one-row density in the rotated residual
  frame `U=[p|W]`, then `z=-B^{-1}a` has density
  `h_U(z)=int |det B| prod_i g_U(-<b_i,z>,b_i)dB`.  A local bound on `h_U`
  gives the cap tail directly, and the Gaussian case evaluates to the exact
  Cauchy density.  This sharpens the remaining non-Gaussian input to a
  projected-density plus determinant-moment estimate, avoiding a separate
  pointwise lower bound for the marginal law of `XW`.
- The determinant-tilted density has now been factored into a sliced one-row
  density and a determinant moment:
  `h_U(z)=J_U(z)^d E_{nu_{U,z}}|det(b_1,...,b_d)|`, where `J_U(z)` is the
  density at zero of `<X,p+Wz>`.  This isolates the remaining hard input:
  after the existing local-CLT machinery controls `J_U`, prove a
  Haar-comparable bound on the volume-normalized sliced determinant moment.
  A Gaussian constant audit confirms the exact factorization and shows that
  Hadamard row-norm products overcount by factors `18.47`, `135.82`, and
  `1001.41` already at `D=8,12,16`.
- A least-squares density probe now estimates the averaged small-ball density
  of `z=-B^{-1}a` near zero.  In a focused `m=24` run, probability ratios
  against the exact Gaussian Cauchy small-ball law stayed order one for
  Gaussian, uniform, Laplace, and logistic rows at observable radii; for
  example at `D=4,r=0.75` the ratios were `0.944,0.961,1.025,0.909`, and at
  `D=6,r=1.0` they were `0.988,0.923,1.070,1.088`.
- A sliced determinant coefficient probe now targets the refined coefficient
  directly by kernel-slicing fresh rows on `<X,p>=0` and estimating
  `vol(B_2^d)J_U(0)^d E_{nu_{U,0}}|det|`.  In a focused `m=24` run, mean
  ratios to the Gaussian/Haar coefficient stayed on scale for
  Gaussian/uniform/Laplace/logistic entries.  For `D=3,4,6,8`, the respective
  ratios were Gaussian `0.954,0.912,0.870,0.847`, uniform
  `0.960,0.973,0.864,0.817`, Laplace `0.898,0.895,0.893,0.783`, and logistic
  `0.937,0.881,0.895,0.856`.
- The sliced determinant moment has a sharper sufficient bound via
  `E det(b_1,...,b_d)^2=d! det E[bb^T]`.  Thus
  `h_U(z) <= J_U(z)^d sqrt(d! det M_U(z))`.  In the Gaussian normalization this
  loses only `~d^(1/4)` relative to the exact Cauchy coefficient, so the P1
  cap edge is now reduced to a conditional local CLT for `J_U(z)` plus a
  sliced covariance-volume estimate for `det M_U(z)`.
- The covariance-volume estimate has been reduced to a trace criterion:
  `det M <= (tr M/d)^d`.  Thus it suffices to prove a quadratic-weighted local
  CLT for
  `T_U(z)=int ||b||^2 g_U(-<b,z>,b)db = J_U(z) tr M_U(z)`, with target
  `T_U(z) <= phi_z(0)(tr Sigma_z+O(log D))` on good residual frames.  The
  sliced determinant probe now reports trace/logdet diagnostics, and a small
  smoke run kept trace-per-dimension means close to one for Gaussian, uniform,
  Laplace, and logistic rows.
## Solved-results list with novelty/publishability flags

1. Gaussian real phase-retrieval stability scale and Dyson-index
   square-submatrix generalization.
   Novelty: project-original. Publishability: manuscript-level result; already
   packaged in `phase_retrieval_omega/paper`.

2. Fixed-apex overlap combinatorics and Lean-supported expectation identities.
   Novelty: project-original supporting machinery. Publishability: supporting
   lemma inside the manuscript/proof infrastructure, not standalone.

3. Deterministic row-Gram/order-statistic bridge in Lean.
   Novelty: project-original formalization of the reduction. Publishability:
   useful as verified infrastructure; not a standalone mathematical result.

4. Sign-free `K5` star-ratio relaxation.
   Novelty: project-new barrier lemma. Publishability: supporting/barrier
   proposition; useful inside a deterministic Plucker note.

5. Exact real `Gr(2,5)` star-ratio theorem.
   Novelty: apparently project-new, with adjacent literature on positive
   `Gr(2,n)` Plucker ratios. Publishability: publishable as a compact base-case
   theorem in the deterministic Balan-Wang/Plucker-imbalance writeup.

6. Exact real rank-two `Gr(2,n)` star-ratio theorem.
   Novelty: apparently project-new after a quick literature smoke check;
   final external novelty claim still needs a dedicated citation pass.
   Publishability: stronger than the `n=5` base case and suitable as a
   proposition in the deterministic Balan-Wang/Plucker-imbalance note.

7. Bounded-density one- and two-dimensional local CLT inputs for P1.
   Novelty: project-new analytic reduction. Publishability: supporting
   proposition for the non-Gaussian universality route; depends on the remaining
   random-matrix delocalization/correlation inputs for the full theorem.

8. P1 averaged-delocalization fixed-apex criterion.
   Novelty: correction/refinement of the route. Publishability: useful as a
   proof-strategy proposition that prevents aiming at an unnecessarily strong
   and union-bound-inaccessible event.

9. P1 random-subset exchangeability reduction.
   Novelty: proof-strategy reduction. Publishability: supporting proposition
   for the non-Gaussian universality route; reduces the good-family part to a
   standard single-matrix delocalization estimate and a random-pair kernel
   estimate.

10. P1 single-normal delocalization and D-stratified random-pair target.
   Novelty: proof-strategy reduction and diagnostic support. Publishability:
   supporting proposition/experiment for the non-Gaussian universality route;
   for subgaussian entries the single-normal part is covered by Nguyen--Vu, and
   the remaining theorem is the D-stratified random-pair estimate.

11. Top-top Plucker template scalar Lean lemma.
   Novelty: verified local algebra for the dyadic partner-capacity route.
   Publishability: proof infrastructure, not standalone.

12. Fixed-apex Poisson first-two-moment reduction for the exact subexponential
   law.
   Novelty: project-new moment reduction. Publishability: supporting
   proposition for the Gaussian subexponential-law route; the full Poisson
   theorem remains open.

13. Subexponential distance-threshold constants.
   Novelty: project bookkeeping, but it sharpens the exact-scale target.
   Publishability: supporting calculation for the P2 subexponential-law route.

## Current proof frontier

The best next target is the non-Gaussian bounded-density universal upper bound.
The proof skeleton is:

1. Fix one apex row and count hyperplanes from `(m-1)` other rows.
2. Use typical-good-family null-normal delocalization to get enough one-slab
   lower bounds at exponentially small scales.
3. Use a two-dimensional local CLT and projection-density bounds for pair
   estimates.
4. Use the fixed-apex overlap identity to close the second moment.

The missing hard inputs are:

- for the bounded-density subgaussian route, the single-submatrix
  null-normal delocalization input is now covered by Nguyen--Vu plus the
  exchangeability reduction; extending beyond subgaussian tails may need a
  truncation/localization argument;
- random-pair non-Gaussian correlation-average/high-correlation control,
  now sharpened to a D-stratified target:
  `E[(1-rho_ST^2)^(-1/2) | D] <= 1+C/D+eta_m(D)` for `D>=3`, with `D<=2`
  handled by the high-overlap/projection-density fallback.  A sufficient
  proof route is now isolated: prove a Gaussian-scale moment hierarchy
  `E[rho_ST^(2q) | D]=O_q(D^{-q})` and a matching no-near-parallel tail
  estimate.

## Next concrete Lean target

Move back to the analytic proof, using the verified row-Gram/order-statistic
bridge as a stable deterministic lemma. For the deterministic Plucker route,
the next concrete target is a dyadic coordinate-level incidence lemma: under
local circuit balance, signed Plucker packets from high determinant levels
should force too much opposite-packet mass in lower levels unless a circuit
ratio is exponentially small. The remaining bottleneck is proving the
incidence theorem suggested by the new exposure/template diagnostic: many
top-top isolated packets must have lower-endpoint coverage, and local circuit
balance must stop cancellation from hiding in uncovered packets. The next
subtarget is to project uncovered top-top targets to Plucker coordinates or
circuits and prove an incidence imbalance there.
The base `Gr(2,5)` case is closed. The next deterministic Plucker target is
to identify a higher-rank replacement for the projective gap/leverage Jensen
argument, or prove the sharper lower-star/null-vector statement that some
deletion star has an exponentially small residual coordinate and then transfer
it to circuits using `C(Q) <= (m-1) A(Q)`.
For P1, the next analytic/random-matrix target is the D-stratified
fixed-apex random-pair correlation theorem for overlapping non-Gaussian null
normals, split into a quadratic angular decorrelation estimate and a
high-correlation/no-near-parallel tail estimate.  A sharper route is now to
condition on the shared row span, prove covariance/tensor isotropy of the
projected residual null-line law (`D trace(M_A^2)=O(1)` and higher tensor
analogues), then prove a Haar-comparable conditional anti-alignment/cap bound
for the near-one edge, benchmarked by the exact beta law of
`Y=1-rho^2`.  The edge now has two deterministic bridges: the slab reduction
to `D-1` one-dimensional projection-density events, and the determinant-aware
least-squares identity `Y=||B^{-1}a||^2/(1+||B^{-1}a||^2)`.  The slab constant
audit shows that rowwise slabs alone overcount in `D`, so the remaining
analytic work is to combine good-family delocalization, projected density
bounds, row-norm truncation, the `J_U(z)` scalar-density estimate, and a
quadratic-weighted local CLT controlling the sliced covariance trace behind
the determinant-tilted density of `z=-B^{-1}a`.  The `J_U(z)` scalar density
factor is now reduced to a frame-leverage/local-CLT event for
`q_z=(p+Wz)/sqrt(1+||z||^2)`, namely
`max_i(|p_i|+r||W_i||_2)/sqrt(1+r^2) <= A sqrt(log m/m)` on `||z||<=r`.
For growing `D`, this forces an explicit `r sqrt(D)` limitation unless a
stronger scalar-density estimate replaces the RV-scale local CLT.  The
single-normal delocalization input is already available for the bounded-density
subgaussian route.
- A radius-window diagnostic now quantifies this scalar-density limitation.
  At `m=24` with the restrictive constant `A=2`, mean local-CLT radii shrink
  as `D` grows: Gaussian gives `3.48,3.44,3.42,1.19,0.65` for
  `D=3,4,6,8,12`, while Laplace gives `3.70,3.02,1.87,0.83,0.52`.  With
  `A=3` or `A=4`, all tested laws and `D<=12` reached the search cap `r=4`.
  Thus the RV local CLT is adequate for fixed/moderate `D` with a large enough
  delocalization constant, while genuinely large-`D` cap bookkeeping still
  needs either `r sqrt(D)` control or a stronger scalar-density input.
- A nonzero-`z` sliced covariance probe now tests the other half of the
  determinant route on the actual cap-radius range.  At `m=24`, the mean
  Cauchy-Schwarz coefficient ratios against the exact Gaussian Cauchy density
  stayed modest at `r=0.5` and `r=1.0`: for `D=3`, Gaussian/uniform/Laplace/
  logistic were about `1.35/1.40`, `1.33/1.36`, `1.35/1.43`, `1.39/1.39`;
  for `D=8`, they were about `1.63/1.84`, `1.47/1.59`, `1.57/1.72`,
  `1.63/1.80`.  The logarithmic geometry ratio
  `d log(J_U/phi_z)+1/2 log(det M_U/det Sigma_z)` stayed near zero, supporting
  the target that this term should be `O(log D)` rather than linear in `D`.
- The same nonzero-`z` probe now reports the trace-level object needed for the
  weaker quadratic-weighted local CLT.  The weighted trace ratio
  `T_U/T_G=(J_U tr M_U)/(phi_z tr Sigma_z)` stayed close to one at `m=24`:
  at `r=0.5`/`r=1.0`, Gaussian was `0.974/0.993` for `D=3` and
  `0.982/0.998` for `D=8`, with uniform/logistic similar and Laplace still
  below one (`0.956/0.977` for `D=3`, `0.952/0.959` for `D=8`).  This supports
  the reduced proof target: scalar local CLT for `J_U(z)` plus
  quadratic-weighted local CLT for `T_U(z)`, followed by AM-GM for `det M_U`.
- The quadratic trace target is now reduced to weighted two-dimensional local
  CLTs.  With `q_z=(p+Wz)/sqrt(1+||z||^2)` and `W=[w_k]`,
  `T_U(z)=sqrt(1+||z||^2)^(-1) sum_k H(q_z,w_k)`, where
  `H(q,w)=int y^2 f_{(<X,q>,<X,w>)}(0,y)dy`.  The Gaussian summands are
  `phi(0)(1-<q_z,w_k>^2)`, so a weighted pair local CLT with total
  `O(log D)` error gives the sliced trace criterion and ties the cap-edge
  input back to the existing two-dimensional local-CLT framework.
- The remaining weighted pair tail has a clean sufficient condition.  Splitting
  `H(q,w)` at `|y|<=L`, compact pair-local-CLT error costs `(2/3)L^3 eps_L`.
  For the tail, if
  `u=(q-<q,w>w)/sqrt(1-<q,w>^2)` and
  `sup_{y,t} f_{<X,u>|<X,w>=y}(t)<=K_cond`, then
  `H_tail <= K_cond(1-<q,w>^2)^(-1/2)
  E[<X,w>^2 1_{|<X,w>|>L}]`, which is exponentially small for subgaussian
  entries.  This isolates the next analytic input as a conditional
  projection-density bound on the slice, not a full conditional local CLT.
- The AM-GM bookkeeping has been sharpened: because
  `log(J_U/phi_z)+1/2 log((tr M_U/d)/det(Sigma_z)^(1/d))`
  equals
  `1/2 log(J_U/phi_z)+1/2 log(T_U/(phi_z d det(Sigma_z)^(1/d)))`, the cap
  upper bound needs only upper estimates for `J_U` and `T_U`; it does not need
  a separate lower bound on `J_U`.  The growing-`D` target is therefore
  `gamma_D+tau_D=O(log D/D)` for these two upper errors, plus the averaged
  weighted pair-slice tail bound.
- A weighted pair-spread radius diagnostic shows why the trace proof should be
  averaged rather than worst-case over all columns.  At `m=24,A=3`, the scalar
  `q_z` radius window capped at `r=4`, but the conservative whitened pair
  windows for `(<X,q_z>,<X,w_k>)` were only about `0.67,0.55,0.49,0.35,0.28`
  for Gaussian `D=3,4,6,8,12`, with similar values for the other tested laws.
  Even at `A=4`, the Gaussian pair windows were `1.07,0.93,0.83,0.67,0.59`.
  This makes a uniform all-pair local-CLT condition too conservative for the
  full scalar cap window and points to summed/averaged pair-slice estimates.
- An averaged weighted-pair tail probe now measures the exact summed tail term.
  At `m=24,r=1,L=3`, the normalized tail ratios were only a few percent:
  Gaussian `0.014/0.025` for `D=3/8`, uniform `0.011/0.013`, Laplace
  `0.022/0.045`, and logistic `0.021/0.029`; at `L=2.5` the range was roughly
  `0.05--0.11`.  The total weighted trace ratio remained near one.  This
  supports replacing the too-strong worst-slice conditional-density supremum by
  a direct integrated/summed tail estimate.
- The conditional-density tail input has been sharpened.  A global bound on
  `f_{<X,u>|<X,w>=y}` is too strong because bounded joint density for
  `(<X,w>,<X,u>)` gives no lower bound on the marginal density in far slices.
  On bounded windows, however, the existing scalar and pair local CLTs already
  give the needed conditional bound under RV-scale pair delocalization.  The
  remaining P1 tail target is now an averaged far-slice estimate for the
  summed weighted trace, not a full conditional local CLT.
- A new weighted pair-slice tail probe estimates this far-slice term directly.
  In a focused `m=24` run, full weighted slices remained near the Gaussian
  calibration.  At `D=8,r=1,L=2`, Gaussian/uniform/Laplace/logistic full-slice
  ratios were `0.976,0.977,0.966,0.962`; `|Y|>2` tail fractions were
  `0.231,0.224,0.255,0.244`; and `|Y|>3` far fractions were
  `0.027,0.014,0.046,0.030`.  The bounded-window tail is benign; the proof
  should target an absolute or summed far-slice decay bound.
- The matching trace-level tail probe now aggregates over residual columns
  before normalization.  At `m=24,D=8,r=1,L=2`, the summed trace ratios were
  again `0.976,0.977,0.966,0.962`, with `|Y|>2` tail fractions
  `0.234,0.226,0.258,0.246` and `|Y|>3` far fractions
  `0.0278,0.0146,0.0471,0.0302`.  This is the quantity appearing in the
  proof target and confirms that the remaining estimate is a summed far-slice
  bound.
- The weighted trace now has a precise cutoff budget.  For
  `H_k(z)=int y^2 f_k(0,y)dy`, summed compact one-sided pair-density error
  `Delta_L`, and exact averaged tail `A_L`, the inequality
  `sum_k H_k(z) <= phi(0)sum_k(1-c_k^2)+(2/3)L^3 Delta_L+A_L` reduces the
  growing-`D` target to `L_D^3 Delta_L_D+A_L_D <= C log D`.  Taking
  `L_D=sqrt(A log D)` is the natural scale: since `tr Sigma_z asymp d`, this
  is a normalized `O(log D/d)` budget and Gaussian tails are below it for
  `A>2`.  The tail-probe script also accepts the earlier documented `--levels`
  flag as an alias for `--tail-cutoffs`.
- A trace-level cutoff-schedule probe at `m=32,r=1,D=8,12,16` supports this
  scale.  It aggregates over residual columns before normalizing.  At `L=3.5`,
  averaged tail fractions were Gaussian `0.004,0.006,0.006`, uniform
  `0.004,0.003,0.002`, Laplace `0.015,0.017,0.020`, and logistic
  `0.007,0.009,0.012`.  Since `sqrt(4 log D)` is `2.88,3.15,3.33` on this
  grid, the `A=4` schedule lies between the `L=3.0` and `L=3.5` rows; heavier
  tails need a larger constant but still show modest summed tail mass.
- The averaged tail has a sharper proof route: rewrite
  `A_L(z)` as `J_q(0) E[sum_k <X,w_k>^2 1_{|<X,w_k>|>L} | <X,q_z>=0]`.
  Exponential tilting in a residual direction preserves product structure and
  reduces slice subgaussian tails to a scalar tilted-density bound for
  `<X,q_z>` at zero.  In the subgaussian entry class, if that tilted scalar
  density is uniformly bounded, then `A_L <= C d(1+L^2)exp(-cL^2)`, which fits
  the `C log D` budget at `L_D^2=A log D`.  The next analytic sublemma is now
  a tilted scalar local CLT upper bound.
- The far-slice target now has an exponential-moment reduction.  Writing
  `B=XW`, `S=<X,q_z>`, and conditioning on `S=0`,
  `A_L(z)=J_q E[sum_k B_k^2 1_{|B_k|>L} | S=0]`.  Thus
  `A_L(z)<=e^{-eta L^2} E_eta(z)`, where `E_eta` is the summed
  `y^2 e^{eta y^2}` pair-slice moment.  Gaussian calibration gives
  `E_eta^G<=phi(0)(1-2eta)^(-3/2)tr Sigma_z` for `eta<1/2`, explaining the
  `A>2` Gaussian cutoff.  The non-Gaussian target is now a law-dependent
  sliced exponential second-moment bound, which yields
  `A_L_D<=C log D` for `L_D^2` slightly larger than `eta^{-1}log D`.
- Scope correction: that quadratic exponential-moment target is for the
  bounded-density subgaussian route.  Laplace/logistic entries have only
  exponential tails, so `E exp(eta <X,w>^2)=infinity` for nonzero linear
  forms.  The general Orlicz schedule is: if the sliced
  `y^2 exp(eta |y|^alpha)` moment is controlled, then
  `L_D~(log D)^(1/alpha)` suffices.  Thus subgaussian laws use
  `sqrt(log D)`, exponential-tailed laws use `log D` unless truncated, and
  finite-moment laws need polynomial cutoffs or a truncation step.
- The tilted-mgf route has been reduced to a tilted scalar local-CLT sublemma.
  After tilting by `theta<X,w_k>`, the coordinate laws remain independent with
  parameters `a_i=theta w_{k,i}`.  If these tilted laws have uniform variance,
  third-moment, and bounded-density/Fourier-integrability control, then the
  existing scalar Fourier local CLT gives a uniform bound on the density of
  `<X,q_z>` at zero under the tilted product law.  The required leverage window
  is `L_D max_i |w_{k,i}|<=a_0`; for subgaussian `L_D~sqrt(log D)` and typical
  residual frames this is `sqrt(D log D log m/m)<<1`.
- The tilted leverage window has been sharpened from row-norm to entrywise
  form.  A new probe measures `L_D max_{i,k}|W_{i,k}|` and compares it with
  `L_D||W||_{2->infty}`.  At `m=64,alpha=2,A=4,r=1`, Gaussian entry tilts for
  `D=8,16,32` were `1.168,1.653,2.681` versus row-norm tilts
  `1.489,2.160,3.093`; logistic rows were `1.151,1.656,2.748` versus
  `1.522,2.195,3.123`.  Thus the tilted tail step should use the Haar-scale
  entrywise condition `sqrt(log D log(mD)/m)<<1`; the row-norm limitation
  remains only for the scalar `q_z` density/radius window.
- The tilted scalar-density route has been reconciled with the Orlicz
  reductions.  It is a proof mechanism, not a separate target:
  tilted scalar density bound gives slice tails, slice tails give sliced
  Orlicz/exponential moments, and those moments give the averaged far-tail
  cutoff bound.
- A tilted scalar-density probe now tests that mechanism directly.  At
  `m=32,theta=1,r=1`, mean tilted-density ratios versus the Gaussian tilted
  calibration for `D=8/16` were Gaussian `0.982/0.964`, uniform
  `0.970/0.978`, Laplace `0.981/0.965`, and logistic `0.975/0.968`, with
  `p90` ratios at most about `1.03`.  At `theta=2`, importance-sampling
  effective sample sizes dropped and some Laplace columns exited the finite-mgf
  strip, confirming that the proof must track `|theta|max_i|w_i|<=c_law` and
  split constants by entry-law class.
- The tilted-density probe now also reports the local-CLT leverage columns.
  In the stable `theta=1,r=1,m=32` rows, mean `q_scaled` for `D=8/16` was
  Gaussian `1.390/1.327`, uniform `1.250/1.214`, Laplace `1.369/1.342`, and
  logistic `1.194/1.228`; mean `w_entry_scaled` was Gaussian `1.104/1.236`,
  uniform `1.014/1.225`, Laplace `1.093/1.338`, and logistic `1.085/1.232`.
  Mean actual coordinate tilts were all below `0.59`, so the successful
  tilted-density rows are inside the intended local-CLT window.
- The tilted-density probe now uses the correct non-Gaussian local-CLT
  calibration: the tilted triangular-array Gaussian with exact coordinate
  means and variances.  At `theta=2,r=1`, ratios against this calibration for
  `D=8/16` were Gaussian `0.995/0.944`, uniform `0.964/0.975`, Laplace
  `1.096/1.006`, and logistic `0.998/0.968`.  This separates a calibration
  artifact from the real remaining issues: low tilted-kernel effective sample
  size and finite-mgf strip constraints.
- The tilted leverage diagnostic now reports threshold success fractions for
  both the actual entrywise tilt `L_D max_{i,k}|W_ik|` and the row-norm
  fallback `L_D||W||_{2->infty}`, and skips the full-residual boundary `D=m`.
  In the focused `m=64,128`, `alpha=2`, `A=4`, `r=1` grid, the entrywise
  condition is strictly more useful: at `m=64,D=16`, logistic-threshold
  entry success was Gaussian `0.90`, uniform `0.90`, Laplace `0.70`,
  logistic `1.00`, while row-norm success was zero; at `m=128,D=32`, entry
  success was Gaussian `0.90`, uniform `1.00`, Laplace `0.70`, logistic
  `0.60`, again with row-norm success zero.  For `alpha=1,A=4`, every row had
  entry success zero even at `pi/sqrt(3)`, so exponential-tail cutoffs need
  larger `m`, smaller constants, or truncation before this tilted local-CLT
  window can be used.
- An hourly Downloads report is now installed.  The script
  `phase_retrieval_omega/codex_runtime/write_hourly_download_report.ps1`
  writes `~\Downloads\phase_retrieval_omega_hourly_report.md`.
  The Windows Scheduled Task `PhaseRetrievalOmegaHourlyReport` has one trigger
  with `<Interval>PT1H</Interval>`, first automatic run
  `2026-06-01T03:51:34+03:00`, and `MultipleInstancesPolicy=IgnoreNew`.
  The report explicitly says which problems are solved and which frontiers
  remain open.
- The Haar benchmark for the tilted entrywise condition is now proved in
  `notes/p1_haar_entrywise_tilt_window_2026_06_01.md`.  For a Haar tangent
  completion `W in R^{m x d}`,
  `max_{i,k}|W_ik| <= sqrt(2(log(2md)+s)/(m-2))` with probability at least
  `1-exp(-s)`.  Hence the tilted tail step has scale
  `L_D sqrt(log(mD)/m)`: for subgaussian cutoffs,
  `sqrt(log D log(mD)/m)<<1`, and for exponential-tail Orlicz cutoffs,
  `(log D)^2 log(mD)/m<<1` after squaring.  This is a Gaussian/Haar
  coordinate benchmark, not the full non-Gaussian angular-universality theorem.
  The determinant and sliced-trace formulas are tangent-rotation invariant, so
  the proof can choose a Haar tangent completion for the tail step; the scalar
  `q_z` radius window still requires row-norm control.
- The tilted scalar-density route now directly yields the weighted far-tail
  budget.  The new note
  `notes/p1_tilted_density_tail_budget_2026_06_01.md` proves: if
  `J_{q,w,theta}(0)<=C_J` and `M_w(theta)<=exp(K theta^2)` for
  `|theta|<=theta_*`, then
  `A_L(z)<=C d(1+L^2)exp(-cL^2)` for `L<=4K theta_*`.  Thus
  `L_D^2=A log D` gives `A_L_D(z)<=C log D` once `A` is large enough and the
  coordinate-tilt window contains the optimizer `theta=L_D/(4K)`.  The
  remaining weighted-trace input is now the compact averaged local-CLT budget
  `L_D^3 Delta_L_D(z)<=C log D`.  The same argument with a finite mgf strip
  gives the `L_D~log D` schedule for exponential-tail laws.
- The compact weighted-trace term is now reduced to a quantitative pair
  local-CLT rate in `notes/p1_compact_pair_clt_budget_2026_06_01.md`.
  Deterministically, an orthonormal pair with row norms at most `delta` has
  the directional spread needed by the bounded-density pair local CLT: every
  direction has at least `1/(2 delta^2)` coordinates of size at least
  `1/sqrt(2m)`.  Thus the good-frame bound
  `delta~sqrt(log(mD)/m)` gives spread `kappa~1/log(mD)`.  For the cap-window
  pairs `(q_z,w_k)`, whitening is stable on `||z||<=r` because
  `1-<q_z,w_k>^2>=1/(1+r^2)`, and the row bound is controlled by
  `||q_z||_infty+||w_k||_infty`.  The remaining compact budget is
  `eps_m(L_D,r,B)<=C log D/(d L_D^3)`, where `eps_m` is the pair local-CLT
  error on `|x|,|y|<=C_r L_D`; for `L_D=sqrt(A log D)` this is roughly
  `C/(D sqrt(log D))`.
- A compact-budget diagnostic was added:
  `numerics/p1_compact_pair_clt_budget_probe.py` and
  `notes/p1_compact_pair_clt_budget_probe_2026_06_01.md`.  It estimates the
  exact one-sided compact quantity `Delta_L` by a two-dimensional kernel
  line-density estimator and reports `L^3 Delta_L/log D`.  In the focused
  `m=24,32`, `D=8,12,16`, `r=1`, `L=sqrt(4 log D)` grid, Gaussian rows give
  the estimator floor because their true compact error is zero:
  `0.341,0.491,0.891` at `m=24` and `0.295,0.652,0.658` at `m=32`.  Logistic
  rows stayed near this floor, uniform rows were moderately higher, and
  Laplace rows were highest (`0.779,1.787,3.123` at `m=24` and
  `0.457,1.088,2.097` at `m=32`).  This gives a scale check for the remaining
  compact local-CLT estimate; it is not a proof of the rate.
- The bounded-density compact pair local-CLT now has an explicit quantitative
  Fourier ledger in `notes/p1_quantitative_pair_clt_fourier_budget_2026_06_01.md`.
  The crude worst-pair bound is
  `eps_m <= C delta + C kappa^(-1)exp(-c kappa T^2) +
  C m q_eta^(kappa m) + C exp(-T^2/4)`, under `delta T^3<<1`.  With
  `delta~sqrt(log(mD)/m)` and `kappa~1/log(mD)`, the middle/far/Gaussian-tail
  terms fit the compact budget after choosing
  `T^2~log(mD)log(D sqrt(log D))`.  The near-zone term closes the compact
  budget in the partial regime `D^2 log D log(mD)<<m` plus a polylogarithmic
  smallness condition.  The bottleneck is now explicit: improve the worst-pair
  `O(delta)` near-zone term, or prove an averaged one-sided `Delta_L` estimate
  directly.
