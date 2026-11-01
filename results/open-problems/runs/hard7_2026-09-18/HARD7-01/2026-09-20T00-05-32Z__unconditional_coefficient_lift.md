Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. No movement in the frozen source metric `B_cart: infinity -> infinity`. Methods tried: B4 / B18 / B24.**

# HARD7-01 — BLYZ run 3: exact coefficient-body scalarization, a broad common-factor class, and a strict off-block neighborhood

**Status:** `PARTIAL / SOURCE OPEN`.

The unrestricted Böröczky–Lutwak–Yang–Zhang log-Brunn–Minkowski conjecture is not solved here. This run does three things that are source-relevant but do not alter the already saturated admission metric:

1. it finds an exact category change which reduces a high-dimensional common-factor class to a weighted unconditional coefficient problem;
2. it proves the weighted coefficient inequality from first principles by multiplicative Prékopa–Leindler, yielding a much broader exact class than the previous one-parameter `ell_q` block family;
3. it proves strictness for non-uniform block dilations when `1<q<infinity` and then gives an explicit robustness inequality that produces genuinely cross-block perturbations.

No simulation is used as proof. There is no finite exhaustive claim, so no checker was manufactured merely for a receipt.

## 1. Continuity, ownership, source, and current-status refresh

I resumed the newest checkpoint

`runs/hard7_2026-09-18/HARD7-01/2026-09-19T23-06-43Z__lq_direct_sum_tensorization.md`

rather than restarting. The exclusive canonical claim remains

`operations/claims/LOG-BRUNN-MINKOWSKI-SYMMETRIC.md`

owned by HARD7-01. The newest neighboring R7-02 delta still records this claim as owned by HARD7-01 and does not duplicate it. I reread the controlling HARD7/new-methods files, `POSTED.md`, campaign `INDEX.md`/`RANKING.md`, the active claim, and the newest relevant neighboring report; the repository-wide alias search shows no competing owner for this exact source.

Primary source remains:

K. J. Böröczky, E. Lutwak, D. Yang, G. Zhang, **The log-Brunn–Minkowski inequality**, *Adv. Math.* 231 (2012), 1974–1997, Problem 1.1, equation (1.4), DOI `10.1016/j.aim.2012.07.015`.

For origin-symmetric convex bodies `K,L subset R^n` and `lambda in [0,1]`, writing `alpha=1-lambda`, `beta=lambda`, and

`K_lambda = intersection_u {x : <x,u> <= h_K(u)^alpha h_L(u)^beta}`,

the source asks whether

`V(K_lambda) >= V(K)^alpha V(L)^beta`

holds in every dimension.

Fresh bounded literature checks on 2026-09-20 UTC included the BLYZ source; Saroglou, *More on logarithmic sums of convex bodies* (Mathematika 2016 / arXiv:1409.4346); Kolesnikov–Milman, *Local L^p-Brunn-Minkowski Inequalities for p<1* (Memoirs AMS 2022); Rotem, *The log-Brunn-Minkowski inequality for complex bodies* (arXiv:1412.5321); Xi, *The Reverse-log-Brunn-Minkowski inequality* (arXiv:2307.04266); Milman, *Centro-affine differential geometry and the log-Minkowski problem* (JEMS 2025); and Lu, *Logarithmic Brunn–Minkowski Inequality under n-2 Reflection Symmetries* (arXiv:2608.20730, 21 August 2026). I found no unrestricted all-dimensional resolution. This is bounded negative search evidence only, not a worldwide novelty certificate.

The literature overlap guard matters here. Saroglou covers ordinary unconditional pairs; Rotem covers complex bodies; Lu covers `n-2` orthogonal hyperplane reflections. The class below allows arbitrary symmetric factor bodies inside blocks and therefore need not be unconditional in ambient coordinates, complex, or hyperplane-reflection invariant. I did not locate the exact coefficient-lift theorem in the bounded search, but its priority remains **UNVERIFIED / possible folklore**.

## 2. Frozen metric and run count

The admission metric is still

`B_cart = largest number of 1D/2D Cartesian blocks for which the source inequality is track-certified for every common-GL image of the corresponding product pair.`

Run 1 on this BLYZ target proved all finite block counts, hence

`B_cart = infinity`.

Therefore this run records honestly

`B_cart: infinity -> infinity`.

The unrestricted full-source dimensional baseline remains

`2 -> 2`.

This is the **second consecutive unchanged run** on the current BLYZ target. Section I is not yet triggered; a third unchanged run must be a stuck/obstruction run unless the source metric genuinely moves.

## 3. B24 first: the naive strictness route is false at the Cartesian endpoint

The preceding checkpoint proposed using strict Hölder slack in the mixed support inequality to force strict log-BM volume. That inference is false in general.

Take a Cartesian product

`K = K_1 x ... x K_m`

and independently dilate the factors,

`L = c_1 K_1 x ... x c_m K_m`, `c_j>0`.

Let `D = c_1^beta K_1 x ... x c_m^beta K_m`. The previous Hölder argument gives `D subset K_lambda`. But for a direction supported entirely in block `j`, the Wulff cap is exactly

`h_K(u)^alpha h_L(u)^beta = c_j^beta h_{K_j}(u)`.

Hence every `x in K_lambda` must satisfy `x_j in c_j^beta K_j` for every `j`, so `K_lambda subset D`. Thus

`K_lambda = D`

and

`V(K_lambda)=V(K)^alpha V(L)^beta`

even when the `c_j` are all different. Mixed directions have strict Hölder slack, but those relaxed halfspaces are redundant. This is exactly the geometric phenomenon behind the expected “dilated direct summands” equality pattern discussed in the modern literature. It kills the proposed support-slack-implies-volume-slack argument at `q=1`.

That negative result changed the route rather than generating another lemma on the same mechanism.

## 4. B18 — change category: exact unconditional coefficient lifting

Fix an orthogonal direct sum

`E = E_1 direct_sum ... direct_sum E_m`, `d_j=dim(E_j)`, `n=sum d_j`,

and origin-symmetric convex bodies `K_j subset E_j`. Write

`p_j(x_j)=||x_j||_{K_j}`.

For a 1-unconditional convex body `A subset R^m`, define its block lift

`A[K_1,...,K_m] = {x=(x_j) : (p_1(x_1),...,p_m(x_m)) in A}`,

where unconditionality makes membership depend only on absolute coordinate values.

### Lemma 4.1 — exact support scalarization

For `u=(u_j)` and `s_j=h_{K_j}(u_j)`, one has

`h_{A[K_1,...,K_m]}(u) = h_A(s_1,...,s_m)`.

#### Proof
If `x` belongs to the lift and `t_j=p_j(x_j)`, then

`<x,u> <= sum_j t_j h_{K_j}(u_j) <= h_A(s)`.

Conversely choose `t in A_+` maximizing `t dot s`. For each `j` choose `y_j in K_j` attaining `h_{K_j}(u_j)` and set `x_j=t_j y_j`. Then `x` belongs to the lift and attains `t dot s=h_A(s)`. QED.

### Theorem 4.2 — the Wulff operation commutes exactly with common-factor lifting

Let `A,B subset R^m` be 1-unconditional convex bodies, and put

`K=A[K_1,...,K_m]`, `L=B[K_1,...,K_m]`.

Let

`C=(1-lambda) dot A +_0 lambda dot B`

be the `m`-dimensional logarithmic Wulff combination. Then the full `n`-dimensional Wulff combination satisfies the exact identity

`(1-lambda) dot K +_0 lambda dot L = C[K_1,...,K_m]`.        (4.1)

#### Proof: first inclusion
By Lemma 4.1,

`h_{C[K]}(u)=h_C(s) <= h_A(s)^alpha h_B(s)^beta = h_K(u)^alpha h_L(u)^beta`.

Thus `C[K]` obeys every global Wulff halfspace and is contained in the global combination.

#### Proof: reverse inclusion
Let `x=(x_j)` lie in the global Wulff body and set `t_j=p_j(x_j)`. To prove `t in C`, by unconditionality it is enough to test coefficient directions `a=(a_j)>=0`.

For each nonzero `x_j`, Hahn–Banach for the norm `p_j` gives a norming functional `v_j` with

`h_{K_j}(v_j)=1`, `<x_j,v_j>=t_j`.

Set `u_j=a_j v_j`. Then Lemma 4.1 gives

`h_K(u)=h_A(a)`, `h_L(u)=h_B(a)`,

while

`<x,u>=sum_j a_j t_j`.

The global Wulff constraint yields

`sum_j a_j t_j <= h_A(a)^alpha h_B(a)^beta`

for every `a>=0`, which is precisely the Wulff membership test `t in C`. Therefore `x in C[K]`. QED.

This is an exact reduction, not a support lower bound.

## 5. The volume also scalarizes exactly

Define the monomial measure on the positive orthant

`d mu_d(t) = product_j t_j^(d_j-1) dt`,

and

`kappa_K = product_j d_j V_{d_j}(K_j)`.

### Lemma 5.1
For every unconditional coefficient body `A`,

`V_n(A[K_1,...,K_m]) = kappa_K * mu_d(A_+)`.        (5.1)

#### Proof
For each block, the pushforward of Lebesgue measure under `x_j -> p_j(x_j)` has distribution function

`V({p_j<=t}) = t^(d_j) V(K_j)`

and hence radial density

`d_j V(K_j) t^(d_j-1) dt`.

Taking the product over blocks and integrating over `A_+` gives (5.1). QED.

Combining Theorem 4.2 and Lemma 5.1, the original `n`-dimensional source inequality for this common-factor class is **equivalent** to

`mu_d(C_+) >= mu_d(A_+)^alpha mu_d(B_+)^beta`.        (5.2)

The factor geometry has disappeared completely; only the coefficient problem remains.

## 6. B4 — prove the coefficient theorem completely

### Theorem 6.1 — weighted unconditional log-BM for the monomial measure

Let `A,B subset R^m` be 1-unconditional convex bodies, `d_j>0`, and `C=(1-lambda) dot A +_0 lambda dot B`. Then

`mu_d(C_+) >= mu_d(A_+)^alpha mu_d(B_+)^beta`.        (6.1)

Consequently, for arbitrary origin-symmetric factor bodies `K_j`,

`V_n((1-lambda) dot A[K_j] +_0 lambda dot B[K_j])`

`>= V_n(A[K_j])^alpha V_n(B[K_j])^beta`.        (6.2)

#### Proof
For `x in A_+`, `y in B_+`, define the coordinatewise geometric interpolation

`z_j=x_j^alpha y_j^beta`.

For any `u>=0`, Hölder gives

`u dot z = sum_j (u_j x_j)^alpha (u_j y_j)^beta`

`<= (u dot x)^alpha (u dot y)^beta`

`<= h_A(u)^alpha h_B(u)^beta`.

For arbitrary signs use unconditionality, replacing `u` by `|u|`. Therefore every such `z` lies in `C_+`.

Now take logarithmic coordinates `x_j=e^{X_j}`. Up to null coordinate hyperplanes,

`mu_d(A_+) = integral_{log A_+} exp(d dot X) dX`,

and similarly for `B,C`. The pointwise inclusion just proved says

`alpha log(A_+) + beta log(B_+) subset log(C_+)`.

Set

`f(X)=1_{log A_+}(X) exp(d dot X)`,

`g(Y)=1_{log B_+}(Y) exp(d dot Y)`,

`h(Z)=1_{log C_+}(Z) exp(d dot Z)`.

Whenever `Z=alpha X+beta Y`, the inclusion and linearity of `d dot Z` give

`h(Z) >= f(X)^alpha g(Y)^beta`.

Prékopa–Leindler therefore yields (6.1). Equation (6.2) follows from the exact scalarization and cancellation of `kappa_K` because `alpha+beta=1`. QED.

### What this adds over the previous run

The previous run handled one common coefficient norm `ell_r` while allowing the factor bodies to differ block by block. Theorem 6.1 moves in a different direction: the factors are common, but the two coefficient bodies `A,B` may be **arbitrary 1-unconditional convex bodies**, with no common `ell_r` structure and no perturbative smallness assumption. The total ambient dimension and every block dimension are arbitrary.

In particular, taking two arbitrary centrally symmetric planar factor bodies in a `2+2` split already gives four-dimensional examples that need not be ambient-coordinate unconditional or possess Lu's two orthogonal hyperplane reflections.

## 7. B24 — exact strictness boundary for the old `ell_q` family

The coefficient language also settles the strictness question cleanly.

Let `1<q<infinity`, `r=q/(q-1)`, `A=B_r^m`, and

`B=diag(c_1,...,c_m) A`, `c_j>0`.

Let `D=diag(c_1^beta,...,c_m^beta)A`. Coordinatewise geometric interpolation gives `D subset C`, where `C=A+_0 B`.

The support functions are

`h_D(u) = (sum_j c_j^(beta q)|u_j|^q)^(1/q)`,

while the Wulff cap is

`G(u) = (sum_j |u_j|^q)^(alpha/q) (sum_j c_j^q |u_j|^q)^(beta/q)`.

Hölder gives `h_D<=G`, with equality for a direction `u` precisely when the `c_j` are constant on the nonzero support of `u`.

### Proposition 7.1
If `lambda in (0,1)`, `1<q<infinity`, and the `c_j` are not all equal, then

`D` is a **proper** subset of `C`, and hence the lifted log-BM inequality is strict for every choice of common factor bodies.

#### Proof
Choose `u_0` with every coordinate positive. Since the `c_j` are not all equal,

`G(u_0)>h_D(u_0)`.

Because `r>1`, `D` is strictly convex and `h_D` is differentiable away from zero; let `x_0` be the unique support point of `D` in direction `u_0`.

Suppose `x_0` were on the boundary of `C`. Then some supporting Wulff inequality would be active there: for some unit `v`,

`x_0 dot v = G(v)`.

But always

`x_0 dot v <= h_D(v) <= G(v)`.

Thus equality forces simultaneously `x_0 dot v=h_D(v)` and `h_D(v)=G(v)`. The first equality says `v` belongs to the normal cone of `D` at `x_0`; uniqueness of the normal gives `v` on the ray of `u_0`. On that ray the second equality is impossible because `G(u_0)>h_D(u_0)`. Therefore no Wulff constraint is active at `x_0`.

By continuity on the unit sphere, `min_v (G(v)-x_0 dot v)>0`, so a full neighborhood of `x_0` lies in `C`. Hence `D` is properly contained in `C`.

Moreover `x_0` lies in the positive orthant. The monomial density is strictly positive there, so

`mu_d(C_+)>mu_d(D_+)`.

But `mu_d(D_+)=mu_d(A_+)^alpha mu_d(B_+)^beta` by diagonal scaling. Thus the weighted coefficient inequality, and therefore the lifted source inequality, is strict. QED.

For two unequal coefficients `c_i != c_k`, one explicit mixed-direction cap gap is

`Delta_ik = 2^(alpha/q) (c_i^q+c_k^q)^(beta/q) - (c_i^(beta q)+c_k^(beta q))^(1/q) > 0`.

This is an auxiliary exact defect; it is **not** substituted for the frozen source metric.

At the Cartesian endpoint `q=1`, Proposition 7.1 fails exactly as it should: independent block dilations are equality cases because the relaxed mixed constraints are redundant. Thus the run identifies a sharp mechanism boundary: `q=1` permits direct-summand equality, while `1<q<infinity` makes nonuniform block dilation strict.

## 8. A quantitative robustness lemma gives genuinely cross-block pairs

Strictness can now be converted into an actual off-block neighborhood without invoking simulation or a local spectral theorem.

### Lemma 8.1 — multiplicative support-distortion robustness

Let `K,L_0 subset R^n` be origin-symmetric convex bodies and suppose their log-BM ratio at `lambda in (0,1)` is

`R_0 = V(K_lambda(L_0)) / [V(K)^alpha V(L_0)^beta] > 1`.

Let `T` be invertible and assume

`e^(-eps) L_0 subset T L_0 subset e^(eps) L_0`.        (8.1)

Then

`V(K_lambda(TL_0)) / [V(K)^alpha V(TL_0)^beta] >= R_0 e^(-2 beta n eps)`.        (8.2)

Hence the source inequality remains valid whenever

`eps <= log(R_0)/(2 beta n)`.        (8.3)

#### Proof
From (8.1),

`e^(-eps) h_{L_0} <= h_{TL_0} <= e^(eps) h_{L_0}`.

Therefore the logarithmic Wulff caps differ by factors `e^(+- beta eps)`, and monotonicity/homogeneity of the Wulff construction gives

`e^(-beta eps) K_lambda(L_0) subset K_lambda(TL_0)`.

Thus its volume is at least `e^(-beta n eps)` times the base Wulff volume. Also (8.1) and volume monotonicity give

`V(TL_0) <= e^(n eps)V(L_0)`.

Dividing yields (8.2), and (8.3) is immediate. QED.

Apply Lemma 8.1 to Proposition 7.1 in a `2+2` four-dimensional split with `c_1!=c_2`. Since `R_0>1`, every sufficiently small nonzero linear map `T` mixing the two blocks and satisfying (8.1) produces a pair `(K,TL_0)` that is **not** in the exact common block-lift class yet still satisfies the source inequality. Such cross-block maps exist arbitrarily close to the identity. The allowed distortion is explicit in terms of the exact base ratio `R_0`; this run does not pretend to have a closed-form numerical lower bound for `R_0-1`.

This is the first genuinely off-block consequence of the new route. It remains a restricted open neighborhood, not global four-dimensional closure.

## 9. What the three methods actually did

- **B4 — prove something weaker, completely:** instead of another attempt at the unrestricted source, prove the exact common-factor lifting theorem and weighted coefficient inequality with full on-page proofs.
- **B18 — say it in another language:** replace high-dimensional convex bodies by 1-unconditional coefficient bodies with monomial weight. The Wulff operation and volume both commute with the lift, so the reduction is exact rather than heuristic.
- **B24 — find the extremal/equality object:** the Cartesian coefficient cube exposes why mixed-support slack can be completely redundant; finite-`r` coefficient balls then show the strict regime, and the strict base pair seeds an off-block robustness neighborhood.

All three routes materially differ from the preceding B6/B14/B30 run.

## 10. Verification and current limitations

Every new theorem above is analytic and proved on the page. No finite enumeration or numerical search is asserted, so no exact-arithmetic artifact is required this run.

The main remaining source gap is unchanged: arbitrary origin-symmetric `K,L` in dimension `3` and higher need not admit a common-factor unconditional coefficient representation, nor lie in the perturbative neighborhood generated above. The coefficient reduction does not address pairs whose angular block factors differ in an uncontrolled way.

The strongest concrete next question is now quantitative and lower-dimensional: for `m=2`, `d=(2,2)`, `r=2`, and a fixed nonuniform dilation ratio `c_2/c_1`, obtain an explicit lower bound for the coefficient-volume ratio `R_0-1`. That would turn (8.3) into a numerical cross-block radius rather than an existence radius.

## 11. Runtime / scheduler capability truth

The actual model exposed to this run is **GPT-5.6 Sol**. Reasoning-effort telemetry is not exposed, so the actual reasoning level is **UNVERIFIED**. GPT-6/maximum is only requested in prompt text; I do not claim it ran.

The exposed scheduler-management interface still has no model-family selector and no reasoning-effort selector. Enforcing GPT-6/maximum would require a product/workspace/API/admin surface that actually exposes and authenticates those fields. The historical `You cannot modify this task` response on P26 is an authorization/context boundary; the legitimate workaround is the owning/admin-authorized context or platform support, not a duplicate task or permission bypass. No scheduler mutation was attempted in this run.

## 12. Ledger delta and next checkpoint

```yaml
ledger_delta:
  worker: HARD7-01
  runtime_model: GPT-5.6 Sol
  reasoning_level: UNVERIFIED
  requested_model: GPT-6
  requested_reasoning: maximum

  active_target: LOG-BRUNN-MINKOWSKI-SYMMETRIC
  source: BLYZ_2012_Problem_1_1
  status: PARTIAL_SOURCE_OPEN
  metric: B_cart
  before: infinity
  after: infinity
  movement: no_movement
  unchanged_runs_on_current_target: 2
  unrestricted_source_dimension_before: 2
  unrestricted_source_dimension_after: 2

  methods: [B4, B18, B24]
  new_exact_reduction: unconditional_coefficient_common_factor_lift
  coefficient_measure: product_t_j^(d_j-1)_dt
  coefficient_theorem: weighted_unconditional_logBM_via_multiplicative_PreKopa
  strictness: finite_r_nonuniform_block_dilations_strict
  cartesian_boundary: q_eq_1_independent_block_dilations_are_equality
  off_block_robustness: R(T) >= R0*exp(-2*beta*n*eps)
  priority_status: UNVERIFIED_MAY_BE_FOLKLORE
  finite_checker_needed: false

  next_methods: [B7, B13, B29]
  next_route: explicit_two_coefficient_volume_defect_for_r2_d22_then_numerical_free_cross_block_radius
  section_I_trigger_if_next_metric_unchanged: true
  closure_audit_requested: false
  scheduler_changed: false
  email_or_drive_used: false
```

Next run must stay on the exact BLYZ target. If `B_cart` remains unchanged, Section I is triggered and the report must explicitly inventory the obstruction before choosing the recovery route. The proposed fresh triple is **B7 / B13 / B29**, aimed at solving the two-coefficient Wulff body exactly enough to lower-bound `R_0-1` rather than adding another qualitative class theorem.
