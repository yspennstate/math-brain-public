# account02/B19 r26 — N3 aggregate-vs-single-gradient synthesis

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Universal proof assembly / SYNTHESIS  
Status: **ESSENTIAL_STEP_APPLIED + CANDIDATE_REFUTED / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source-pinned proof graph consumed

Fresh brain control at invocation was `yspennstate/math-research-brain@6c140e5c9cb524e3f339087af8bd0a41675aaa06`, OWNER CONTROL revision `2026-09-22.15`, QFORM-only. The owner proof-first and Claude-latest requests were read. The current synthesis reduction remains the no-pivot class `N3(tau)`: after the already-paid scalar/pair branches one may restrict to matrices satisfying

`|A_ii| < tau`,  `|A_ii A_jj - A_ij^2| < tau` for every `i != j`,

while retaining at least three eigenvalues of modulus at least one. The full conjecture is still open because this class has not been exhausted.

The required newest-Claude package was read at the exact source pin

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`, including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. In particular I use Theorem H below at equation level. Theorem D/D' and D5 remain valid paid exits; arbitrary-joint 3D coarea remains refuted.

The newest completed designated-partner handoff available at the fresh control state is account03/B19 r24, canonical mathematics

`yspennstate/math-open-problems@2c88af5e0ac6a4faf8d923a621c7d7006d544ffe`.

Its theorem `QFORM-TWO-PHYSICAL-GRADIENT-2OVER3-SMALLBALL-v1` gives, for two original physical coordinates and a disjoint product bank with two-row cross-area

`Delta_2 = sqrt(det(M M^T)) > 0`,

`sup_z P(|R-z| <= eps) <= 12 (2 Delta_2)^(-1/3) eps^(2/3)`

and hence

`sup_z E |R-z|^(-1/2) < 21.687 Delta_2^(-1/4)`.

A further compatible completed analytic result is account02/B14's `QFORM-TOP-d-CROSS-AVERAGING-v1`, source-visible at

`yspennstate/math-open-problems@2734623e95f9fafea5354620290ee75ad835b7df`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260922T220604Z-account02-B14-QFORM-r21/REPORT.md`.

For a zero-self physical block

`Q(U,V)=2 U^T C V + R(V) + affine`,

it proves

`||p_Q||_inf <= e sqrt(pi) / sqrt(s_1(C) s_2(C))`.              (1.1)

All coordinates remain original independent coordinates; no rotated independence is used.

## 2. A complete target-level closure: every pure bipartite target

### Proposition 2.1 — `QFORM-PURE-BIPARTITE-TARGET-PAID-v1`

Let

`A = [[0,C],[C^T,0]]`

in an original-coordinate partition. If `A` has at least three eigenvalues of modulus at least one, then for every independent cap-one input vector,

`||p_(X^T A X)||_inf <= e sqrt(pi) < 4.819`.                    (2.1)

### Proof

The nonzero spectrum of the symmetric bipartite matrix is exactly

`{+s_j(C), -s_j(C) : s_j(C)>0}`.

The heavy eigenvalues therefore occur in opposite-sign pairs. Having at least three eigenvalues of modulus at least one forces at least two singular values of `C` to satisfy

`s_1(C) >= s_2(C) >= 1`.

Writing the original product vector as `(U,V)`, the quadratic form is exactly `2 U^T C V`. Apply (1.1):

`||p_Q||_inf <= e sqrt(pi) [s_1(C)s_2(C)]^(-1/2) <= e sqrt(pi)`.

This is essential boundedness; no separate continuity claim is made. QED.

This pays an infinite-dimensional-looking N3 obstruction class at target level, rather than choosing one tiny physical minor.

## 3. Refutation of universal single-second-gradient extraction inside N3

A tempting completion of the designated partner route would assert that every N3 target exposes two original physical coordinates whose cross gradients have a universally positive area. That assertion is false even in the pure bipartite subclass just paid above.

Fix `m>=2`. Split the right coordinates into three groups `G_1,G_2,G_3`, each of size `m`, and let `g_1,g_2,g_3 in R^(3m)` be the disjoint unit vectors which equal `m^(-1/2)` on their own group and zero elsewhere. On the left take one hub row `h`, `m` rows `p_k`, and `m` rows `q_k`, and define the `(1+2m) x (3m)` matrix `C_m` by

`r_h = g_1`,

`r_(p_k) = m^(-1/2) g_2`,

`r_(q_k) = m^(-1/2) g_3`.

Let

`A_m = [[0,C_m],[C_m^T,0]]`.                                    (3.1)

Then

`C_m^T C_m = g_1 g_1^T + g_2 g_2^T + g_3 g_3^T`,

so `C_m` has singular values exactly `(1,1,1)` and

`spec(A_m) = {+1,+1,+1,-1,-1,-1,0,...,0}`.                    (3.2)

Thus every `A_m` satisfies the owner target.

All diagonal entries vanish. Every physical two-coordinate principal block is either zero (same side) or

`[[0,c],[c,0]]`

with `|c|<=m^(-1/2)`, hence

`|det A_m[{i,j}]| <= 1/m`.                                     (3.3)

Therefore, for every fixed `tau>0`, all sufficiently large `m` lie in `N3(tau)`.

Now take any two original physical coordinates and any disjoint bank of remaining coordinates. Let `Delta_2` be the designated partner's two-row cross-area. Adding columns can only increase each singular value of a two-row matrix, so it suffices to use all remaining coordinates. Directly from the row/column geometry above:

- two left rows have area at most `m^(-1/2)` (hub versus one transverse row is the maximum);
- two right rows have area at most `m^(-1)`;
- one left and one right active coordinate have cross-gradient supports on opposite sides, with norm product at most `m^(-1/2)`.

Consequently

`sup_(all physical pairs/banks) Delta_2 <= m^(-1/2) -> 0`.       (3.4)

This proves:

### Refutation 3.1 — `QFORM-N3-SINGLE-SECOND-GRADIENT-EXTRACTION-FALSE-v1`

There is no universal `c_0>0` such that every N3 target matrix admits a designated-partner two-physical-gradient receiver with `Delta_2>=c_0`.

At equation level, applying account03/B19 r24 to any physical pair in (3.1) gives only a half-Riesz certificate whose displayed right-hand side is at least

`21.687 m^(1/8)`                                                   (3.5)

at the best possible pair scale. Thus the theorem is valid but a single-pair application cannot certify a uniform target bound on this family. This does **not** refute r24; it refutes only the attempted global structural extraction into its local receiver.

## 4. Required newest-Claude theorem applied to the same obstruction

The family (3.1) is not a QFORM counterexample. Besides Proposition 2.1, it is paid directly by newest-Claude Theorem H, and this application explains the missing aggregate geometry.

Use the single hub as `H={h}` and put every other coordinate in `I`; take `J=empty`. On `I`, set

`P=m^(-1/2) sum_k e_(p_k)`, `B=m^(-1/2) sum_j e_(G_2,j)`,

`Q=m^(-1/2) sum_k e_(q_k)`, `D=m^(-1/2) sum_j e_(G_3,j)`.

The internal block has the exact rank-four spectral decomposition

`A_II = v_1 v_1^T - v_2 v_2^T + v_3 v_3^T - v_4 v_4^T`,

where

`v_1=(P+B)/sqrt(2)`, `v_2=(P-B)/sqrt(2)`,

`v_3=(Q+D)/sqrt(2)`, `v_4=(Q-D)/sqrt(2)`.

The hub-column restricted to `I` is the unit vector

`a=m^(-1/2) sum_j e_(G_1,j)`,

which is orthogonal to all four `v_k`. Therefore the augmented Theorem-H Gram matrix is exactly

`G_tilde = I_5`.                                                  (4.1)

Every physical coordinate in `I` has augmented leverage exactly `1/m`, so for `m>=2` the required leverage bound `<=1/2` holds.

Theorem H with `|H|=1`, `r=4`, all `|lambda_k|=1`, and `det G_tilde=1` gives

`|phi_Q(t)| <= 32 pi^3 |t|^(-3)`.                               (4.2)

Using `|phi|<=1` and Fourier inversion,

`||p_Q||_inf
 <= (2pi)^(-1) int_R min(1,32 pi^3 |t|^(-3)) dt
 = (3/(2pi)) (32 pi^3)^(1/3)
 = (3/2) 32^(1/3)
 = 4.7622031559...`.                                              (4.3)

This is the requested equation-level application of a completed result from the exact `e5f71d...` package. It also diagnoses why a local two-gradient route is structurally incomplete: the uniform smoothing currency is spread over an exact rank-four light block plus one diffuse hub, while each individual second physical gradient tends to zero.

## 5. Full proof graph after this run

The source-pinned conditional graph is now:

1. Owner scalar/pair completion reduces the full target to `N3(tau)` after already-paid physical pivot/definite-pair/indefinite-pair exits.
2. Newest-Claude F/H/D/D'/D5 pay diffuse Fresnel, exact hub, rank-three cross-volume, and rank-five cross-volume branches under their stated hypotheses.
3. Current volume-stability and other source-pinned ridge/aggregate routes pay robust high-cross-rank perturbative branches without deleting small coefficients at the law level.
4. account03/B19 r24 pays a genuine two-physical-gradient `2/3` small-ball / half-Riesz receiver and its scalar/pair splices when a quantitative local area plus a third smoothing source exists.
5. account01/B01 closes the analytic aggregate `E2` half-Riesz obstruction once a scalar square peel is legitimately available.
6. Proposition 2.1 above closes **all pure bipartite target matrices**, including strict-N3 families with no quantitative local second gradient.

What remains is therefore not pure bipartite geometry and not a universal local second-gradient extraction.

## 6. First unpaid implication, with quantifiers

The first synthesis gate is now the curved aggregate third-source problem:

### `QFORM-N3-CURVED-AGGREGATE-THIRD-SOURCE-v1`

Prove that there exist universal constants `tau_0>0` and `C<infinity` such that for every dimension `n`, every real symmetric `A` satisfying

- at least three eigenvalues of `A` have modulus at least one;
- `|A_ii|<tau_0` for every `i`;
- `|A_ii A_jj-A_ij^2|<tau_0` for every `i!=j`;

and every independent real product law with one-dimensional densities bounded by one, the density of `X^T A X` is at most `C`, **under the additional negative hypotheses that none of the already source-proved scalar/pair, F/H, D/D'/D5, volume-stability/ridge, pure-bipartite top-two-cross, or quantitative r24 local-two-gradient-plus-third-source exits applies**.

Equivalently, one needs a product-safe way to fuse an **aggregate rank-two cross bank** with the unavoidable third spectral source when nonzero within-bank curvature prevents the zero-self conditioning used in (1.1). The family (3.1) proves that this fusion cannot first select one physical second-gradient row at fixed scale. The live correction set also forbids deleting the within-bank curvature merely because its coefficients are small: no law-uniform coefficient-perturbation principle is available for unrestricted fragmented supports.

A quantitatively useful replacement would suffice: for example, show that every survivor either admits an exact Theorem-H low-rank-plus-diagonal light representation at fixed augmented determinant, or an aggregate two-row/second-compound currency that can be combined with a third source **before** selecting a physical minor.

## 7. Scope

This run proves a target-level pure-bipartite closure and a strict-N3 structural no-go for universal single-second-gradient extraction. It does **not** prove full QFORM and supplies no end-to-end review, let alone the required two independent reviews. All arbitrary-support, no-moment, no-log-concavity and original-coordinate independence restrictions are preserved.
