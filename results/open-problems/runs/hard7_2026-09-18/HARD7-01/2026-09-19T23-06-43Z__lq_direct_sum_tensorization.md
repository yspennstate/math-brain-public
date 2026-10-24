Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. No movement in the frozen source metric `B_cart: infinity -> infinity`. Methods tried: B6 / B14 / B30.**

# HARD7-01 — BLYZ run 2: mixed-norm direct-sum tensorization beyond Cartesian products

**Status:** `PARTIAL / SOURCE OPEN`. The unrestricted Böröczky–Lutwak–Yang–Zhang log-Brunn–Minkowski conjecture is not solved here. This run proves a new restricted-class theorem on the page and deliberately does **not** relabel its secondary parameter range as movement of the already-saturated frozen metric.

## 1. Continuity, ownership, exclusions, and source refresh

I resumed the exact current target and newest checkpoint rather than restarting:

`runs/hard7_2026-09-18/HARD7-01/2026-09-19T22-04-44Z__handoff_mi_admission_logbm_tensorization.md`.

The active exclusive claim remains

`operations/claims/LOG-BRUNN-MINKOWSKI-SYMMETRIC.md`,

owned by HARD7-01. A fresh repository search found no conflicting canonical owner. The neighboring `GZ-DIMBM-EVEN-LOGCONCAVE` and `B-WEAK-EVEN-LOGCONCAVE` claims are distinct sources and are explicitly handed off/released; the newest R7-02 delta report independently records `LOG-BRUNN-MINKOWSKI-SYMMETRIC` as newly claimed by HARD7-01 rather than available to its shard. The posted/settled exclusions in `POSTED.md`, campaign `INDEX.md`/`RANKING.md`, root `RESULTS.md`, root `QUEUE.md`, and the intake/alias search were reconciled before continuing.

Exact primary source remains:

K. J. Böröczky, E. Lutwak, D. Yang, G. Zhang, **The log-Brunn–Minkowski inequality**, *Advances in Mathematics* 231 (2012), 1974–1997, Problem 1.1, equation (1.4), DOI `10.1016/j.aim.2012.07.015`.

For origin-symmetric convex bodies `K,L subset R^n` and `lambda in [0,1]`, with the logarithmic Wulff combination

\[
(1-\lambda)\cdot K+_0\lambda\cdot L
=\bigcap_{u\in S^{n-1}}\{x:\langle x,u\rangle\le h_K(u)^{1-\lambda}h_L(u)^\lambda\},
\]

the source asks whether

\[
V_n((1-\lambda)\cdot K+_0\lambda\cdot L)
\ge V_n(K)^{1-\lambda}V_n(L)^\lambda
\tag{LBM}
\]

holds in every dimension. BLYZ prove the full planar case and the planar companion `0<p<1` family.

A fresh bounded literature check on 2026-09-19/20 UTC used the BLYZ source plus:

- A. V. Kolesnikov and E. Milman, *Local L^p-Brunn-Minkowski Inequalities for p<1*, Memoirs AMS 277 (2022), no. 1360, DOI `10.1090/MEMO/1360`;
- C. Saroglou, *More on logarithmic sums of convex bodies*, Mathematika 62 (2016), 818–841, DOI `10.1112/S0025579316000061`;
- E. Milman, *Centro-affine differential geometry and the log-Minkowski problem*, JEMS 27 (2025), 709–772, DOI `10.4171/JEMS/1386`;
- XiaoRui Lu, *Logarithmic Brunn–Minkowski Inequality under n−2 Reflection Symmetries*, arXiv:2608.20730, submitted 21 August 2026.

No unrestricted all-dimensional resolution was found in this bounded search. This is negative search evidence only, not a worldwide openness/novelty certificate.

One planned route from the previous checkpoint was **not** pursued as if new: Kolesnikov–Milman already prove local log-BM near the cube (and near specified `ell_q` balls in their regime), so “small relative shear of the cube” is not a clean novelty target. I pivoted instead to an exact global block geometry that is not Cartesian.

## 2. Frozen metric: no movement

The admission metric is

`B_cart = largest number of 1D/2D Cartesian blocks for which the exact source inequality is track-certified for every common-GL image of the corresponding product pair.`

The preceding run proved Cartesian tensorization for every finite number of blocks, hence

\[
\boxed{B_{\rm cart}:\infty\longrightarrow\infty.}
\]

So this run is **no movement** in the frozen metric. The unrestricted source-dimensional baseline also remains

\[
2\longrightarrow2.
\]

The theorem below enlarges the geometry of the certified restricted class, but I do not substitute that secondary parameter for the frozen metric.

## 3. B6 — deform the solved Cartesian point through block Banach sums

The previous theorem corresponds to a Cartesian product, whose support function adds block supports. To leave the product manifold while retaining an exact support calculus, fix an orthogonal decomposition

\[
E=E_1\oplus\cdots\oplus E_m,\qquad d_j=\dim E_j,\qquad n=\sum_j d_j,
\]

and a parameter `q in [1,infinity]`. Let `r` be its Hölder-conjugate exponent,

\[
\frac1q+\frac1r=1,
\]

with `q=1,r=infinity` and `q=infinity,r=1` in the endpoint conventions.

For origin-symmetric convex bodies `K_j subset E_j`, define the block `ell_r` gauge sum

\[
\mathcal S_q(K_1,\ldots,K_m)
:=\left\{x=(x_j):
\left(\sum_j\|x_j\|_{K_j}^{\,r}\right)^{1/r}\le1\right\},
\tag{3.1}
\]

with the obvious maximum interpretation when `r=infinity`. By duality of `ell_r` and `ell_q`,

\[
h_{\mathcal S_q(K_1,\ldots,K_m)}(u)
=\left(\sum_j h_{K_j}(u_j)^q\right)^{1/q}.
\tag{3.2}
\]

At `q=1` this is exactly the previous Cartesian product. At `q=infinity` it is the `ell_1` gauge join. Thus `q` gives an exact deformation away from the solved Cartesian geometry.

The counterexample boundary is immediate and useful. For `q<1`, the candidate support aggregator is generally not subadditive: for two scalar blocks,

\[
H(e_1+e_2)=2^{1/q}>2=H(e_1)+H(e_2),
\]

so it need not be a support function at all. Hence `q>=1` is a structural convexity boundary, not an arbitrary proof restriction.

## 4. Mixed-power-mean inequality: the exact gluing engine

Write

\[
\alpha=1-\lambda,\qquad\beta=\lambda,
\]

and define the scalar power mean

\[
M_0(a,b)=a^\alpha b^\beta,
\qquad
M_p(a,b)=(\alpha a^p+\beta b^p)^{1/p}\quad(p>0).
\]

### Lemma 4.1
For nonnegative vectors `a=(a_j), b=(b_j)`, every `q in [1,infinity]`, and every `p in [0,q]`,

\[
\boxed{
\|\big(M_p(a_j,b_j)\big)_j\|_q
\le M_p(\|a\|_q,\|b\|_q).
}
\tag{4.1}
\]

#### Proof
For `p=0` and finite `q`, Hölder gives

\[
\sum_j a_j^{\alpha q}b_j^{\beta q}
\le
\left(\sum_j a_j^q\right)^\alpha
\left(\sum_j b_j^q\right)^\beta,
\]

and taking the `q`th root yields (4.1). The `q=infinity` endpoint is the elementary maximum inequality.

For `p>0`, put `s=q/p>=1`, `A_j=a_j^p`, `B_j=b_j^p`. Then Minkowski in `ell_s` gives

\[
\begin{aligned}
\|\big(M_p(a_j,b_j)\big)_j\|_q^p
&=\|\alpha A+\beta B\|_s\\
&\le\alpha\|A\|_s+\beta\|B\|_s\\
&=\alpha\|a\|_q^p+\beta\|b\|_q^p,
\end{aligned}
\]

which is exactly (4.1) after taking the `p`th root. The `q=infinity` endpoint follows from the same maximum argument. QED.

The condition `p<=q` is sharp for this route. With `alpha=beta=1/2`, `a=(1,0)` and `b=(0,1)`,

\[
\|\big(M_p(a_j,b_j)\big)\|_q=2^{1/q-1/p},
\qquad
M_p(\|a\|_q,\|b\|_q)=1.
\]

Thus the required inequality reverses when `p>q`. In the BLYZ hard range `0<=p<=1` and our convex range `q>=1`, the safe condition `p<=q` is automatic.

## 5. B30 — localize by blocks, then glue exactly

### Theorem 5.1 — `ell_q`-support direct-sum tensorization

Fix `lambda in [0,1]`, `q in [1,infinity]`, and `p in [0,q]`. Let

\[
K=\mathcal S_q(K_1,\ldots,K_m),\qquad
L=\mathcal S_q(L_1,\ldots,L_m),
\]

with every `K_j,L_j` origin-symmetric convex bodies in the same block `E_j`. Let

\[
C_j=(1-\lambda)\cdot K_j+_p\lambda\cdot L_j
\]

be the block Wulff `L_p` combinations and

\[
C=(1-\lambda)\cdot K+_p\lambda\cdot L
\]

the global Wulff combination. Then

\[
\boxed{
\mathcal S_q(C_1,\ldots,C_m)\subseteq C.
}
\tag{5.1}
\]

#### Proof
For `u=(u_j)`, put

\[
a_j=h_{K_j}(u_j),\qquad b_j=h_{L_j}(u_j).
\]

By the Wulff definition,

\[
h_{C_j}(u_j)\le M_p(a_j,b_j).
\]

Using (3.2), monotonicity of the `ell_q` norm, and Lemma 4.1,

\[
\begin{aligned}
h_{\mathcal S_q(C_1,\ldots,C_m)}(u)
&=\|\big(h_{C_j}(u_j)\big)_j\|_q\\
&\le\|\big(M_p(a_j,b_j)\big)_j\|_q\\
&\le M_p(\|a\|_q,\|b\|_q)\\
&=M_p(h_K(u),h_L(u)).
\end{aligned}
\]

The final expression is the defining support cap for `C`; hence (5.1). QED.

This is a support-containment statement independent of any volume theorem on the blocks.

## 6. B14 — the acting group and the exact shape-independent volume factor

The block sum has an exact volume formula. For finite `r`, block gauge polar integration gives

\[
\boxed{
V_n(\mathcal S_q(K_1,\ldots,K_m))
=c_{r,\mathbf d}\prod_{j=1}^m V_{d_j}(K_j),
}
\tag{6.1}
\]

where

\[
c_{r,\mathbf d}
=\frac{\prod_{j=1}^m\Gamma(1+d_j/r)}{\Gamma(1+n/r)}.
\tag{6.2}
\]

For `r=infinity` the constant is `1`, recovering Cartesian volume multiplication.

For completeness, (6.1) follows by writing `t_j=\|x_j\|_{K_j}`. The radial shell measure in block `j` is

\[
d_jV(K_j)t_j^{d_j-1}\,dt_j.
\]

After `y_j=t_j^r`, the integral over `sum y_j<=1` is the Dirichlet simplex integral, yielding exactly (6.2). Crucially, `c_{r,d}` depends only on the block dimensions and `r`, not on the shapes.

Therefore, if every block pair obeys the BLYZ `p`-volume inequality

\[
V(C_j)\ge V(K_j)^\alpha V(L_j)^\beta,
\tag{6.3}
\]

then Theorem 5.1 and (6.1) give

\[
\begin{aligned}
V(C)
&\ge c_{r,\mathbf d}\prod_jV(C_j)\\
&\ge c_{r,\mathbf d}\prod_jV(K_j)^\alpha V(L_j)^\beta\\
&=V(K)^\alpha V(L)^\beta,
\end{aligned}
\tag{6.4}
\]

because `alpha+beta=1`, so the same shape-independent constant appears with total exponent one on the right.

This proves:

### Corollary 6.1 — exact BLYZ family on arbitrary block `ell_r` sums

For every `q in [1,infinity]` and every `p in [0,1]`, the BLYZ `L_p` volume inequality tensorizes from the blocks through `mathcal S_q`. Since BLYZ prove the needed factor theorem for every origin-symmetric one- or two-dimensional block, their full `0<=p<=1` family holds in arbitrary total dimension for every pair

\[
K=\mathcal S_q(K_1,\ldots,K_m),\qquad
L=\mathcal S_q(L_1,\ldots,L_m)
\]

with common block decomposition and all block dimensions `1` or `2`.

The theorem is invariant under a common global `T in GL(n)`: the Wulff operation is `GL(n)`-equivariant and volume scales by `|det T|`. Block-preserving `GL(E_j)` changes are already absorbed into the arbitrary factor bodies. This group quotient is why the orthogonal model loses no generality for the stated common-GL class.

At `q=1` Corollary 6.1 recovers the preceding Cartesian tensorization. Intermediate `q` and `q=infinity` give genuinely non-Cartesian block geometries.

## 7. Current-literature overlap guard

This theorem is **not** presented as a verified-priority result.

- Kolesnikov–Milman already cover local log-BM near the cube and several `ell_q` balls, so the discarded local-shear idea is not claimed.
- Saroglou proves major unconditional classes and reductions, but arbitrary planar factor bodies in the block construction need not be unconditional in a common coordinate basis.
- Lu proves the log-BM inequality for bodies with `n-2` orthogonal hyperplane reflection symmetries. In dimension three, a `2+1` block sum automatically has the one required block-hyperplane reflection, so that three-dimensional subfamily overlaps Lu's 2026 theorem and earns no novelty claim here.
- In a `2+2` split in dimension four, arbitrary origin-symmetric planar factors need not have line-reflection symmetries; block sign changes are codimension-two central inversions rather than hyperplane reflections. Thus the exact overlap with Lu/Saroglou is not automatic in higher-dimensional arbitrary-block cases.

Targeted searches for `log-Brunn-Minkowski direct sum`, `Firey direct sum`, `block tensorization`, and neighboring formulations did not locate this exact arbitrary-`q`, arbitrary-planar-block transfer statement. **That bounded negative search does not establish novelty. Priority remains `UNVERIFIED / may be elementary folklore`.** The on-page proof is the only claim made here.

## 8. What the three methods actually did

- **B6 — deform to a solvable point:** instead of a relative shear already entangled with known local theorems, deform the exact Cartesian product (`q=1`) through the entire Banach-sum family `q in [1,infinity]`. This exposed a mixed-power-mean inequality and produced a global exact restricted theorem.
- **B14 — find the group acting:** quotient common `GL(n)` and blockwise coordinate changes. The key invariant is the shape-independent Dirichlet volume constant `c_{r,d}`, which cancels exactly in the log-concavity exponent.
- **B30 — one scale/direction at a time:** localize the Wulff support caps to blocks and glue them with Hölder/Minkowski. The exact failure at `p>q` and the nonconvex boundary at `q<1` identify where this mechanism stops.

This is substantive progress in certified geometry, but it does not move the frozen metric and does not solve the source.

## 9. Verification discipline

There is no finite exhaustive claim in this run. The new result is an analytic theorem with the full proof on the page. Under the 90/10 rule I did **not** manufacture an `artifacts/` checker merely to create a receipt. No simulation is used as proof.

A private algebra/numerical sanity check of the mixed-norm inequality was used during derivation, but it is not evidence for the theorem and is not promoted to the repository. The proof above is exact.

This is the **first unchanged run** for `B_cart` on the new BLYZ target after its admission jump `1 -> infinity`; Section I is not yet triggered.

## 10. Model / scheduler / permission truth

Actual model exposed to this run: **GPT-5.6 Sol**. Reasoning-effort telemetry is not exposed, so the actual reasoning level is **UNVERIFIED**. The prompt requests GPT-6/maximum; I do not claim that request was enforced.

The currently exposed native scheduler-management schema still offers only task title, prompt, schedule/relative start, timing mode, and enabled state. It exposes **no model-family selector, no reasoning-effort selector, no authenticated applied-model/effort receipt, and no guaranteed run duration**. Enforcing GPT-6/maximum would require a product/workspace/API/admin surface that actually exposes and attests those fields; this worker cannot synthesize such a selector from prompt text.

The historical `You cannot modify this task` response on a P26 scheduler ID is an authorization/context boundary. Repository policy records that P26 was later updated from a different authorized context. The valid workaround is the owning/admin-authorized context or platform support, not bypassing permissions or creating a duplicate schedule. No scheduler mutation was attempted here.

## 11. Ledger delta and next checkpoint

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
  unchanged_runs_on_current_target: 1
  unrestricted_source_dimension_before: 2
  unrestricted_source_dimension_after: 2

  methods: [B6, B14, B30]
  theorem: lq_support_direct_sum_tensorization
  theorem_parameter_range: q_in_[1,infinity], p_in_[0,q]
  source_corollary_range: q_in_[1,infinity], p_in_[0,1]
  boundary_obstruction: p_gt_q_breaks_mixed_norm_gluing; q_lt_1_not_support_convex
  common_GL_extension: true
  finite_checker_needed: false
  priority_status: UNVERIFIED_MAY_BE_FOLKLORE

  literature_pivot: cube_local_shear_not_claimed_due_Kolesnikov_Milman_2022
  n3_overlap_guard: Lu_2026_n_minus_2_reflections

  next_methods: [B4, B18, B24]
  next_route: characterize_equality_and_strictness_of_mixed_norm_tensorization_then_test_first_2_plus_2_off_block_perturbation
  closure_audit_requested: false
  scheduler_changed: false
  email_or_drive_used: false
```

The next run must resume this exact BLYZ target. Use a different triple, proposed **B4 / B18 / B24**. The concrete goal is to characterize when both inequalities in the support gluing and the block volume step are equal, then use that rigidity to test the first genuinely off-block perturbation in a `2+2` four-dimensional configuration, where the automatic three-dimensional reflection-symmetry shortcut no longer applies.