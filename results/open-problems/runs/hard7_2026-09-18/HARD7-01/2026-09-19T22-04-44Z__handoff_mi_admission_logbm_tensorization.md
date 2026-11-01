Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. Rotation completed. Old source metric `D_MI: 2 -> 2` and is handed off after both Section-I recoveries; new restricted exact-source metric `B_cart: 1 -> infinity`. Methods tried on the new target: B2 / B5 / B11.**

# HARD7-01 — Section-I rotation to BLYZ log-Brunn–Minkowski and exact Cartesian tensorization

**Status:** new source **OPEN / PARTIAL**. The full log-Brunn–Minkowski conjecture is not solved here. This run proves an all-finite-block restricted theorem for the exact source inequality and identifies the first off-product obstruction for the next run.

## 1. Required continuity, lifecycle and ownership read

I resumed from the newest HARD7-01 checkpoint rather than restarting:

`runs/hard7_2026-09-18/HARD7-01/2026-09-19T21-02-00Z__stuck2_robin_moment_operator.md`.

That report had `D_MI=2` for the Artstein-Avidan–Katzin maximal-intersection uniqueness question and explicitly consumed the **second and final** allowed Section-I recovery. The source metric had remained unchanged for five current-target runs. Therefore a third recovery on that target is forbidden by the controlling hard-task lifecycle.

At run start I reread/reconciled:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- the newest own report above and the relevant neighboring admission/release/collision reports;
- repository-wide exact-name/alias searches, including the intake tree, for the new candidate.

The old maximal-intersection canonical claim has been changed from active ownership to an explicit Section-I handoff. I also repaired two stale historical HARD7-01 canonical records so that the already-handed-off weak `(B)` target is no longer shown as actively owned and the already-refuted literal Artstein-Avidan–Katzin equality clause is no longer shown as an active claim. No other worker's claim was overwritten.

The newly created exclusive claim is

`operations/claims/LOG-BRUNN-MINKOWSKI-SYMMETRIC.md`.

Repository searches for `Böröczky Lutwak Yang Zhang`, `log-Brunn-Minkowski`, `logarithmic Brunn Minkowski`, `BLYZ Problem 1.1`, and the canonical claim name found no pre-existing owner. The related dimensional Brunn–Minkowski and weak-`(B)` claims are different statements; KLS is excluded. The 2026 strong Gaussian product inequality was also rejected as a candidate because a current proof claim exists in the literature.

## 2. Exact external source and current status

Primary source:

Károly J. Böröczky, Erwin Lutwak, Deane Yang and Gaoyong Zhang, **The log-Brunn–Minkowski inequality**, *Advances in Mathematics* 231 (2012), 1974–1997, DOI `10.1016/j.aim.2012.07.015`.

The source defines, for convex bodies containing the origin in their interiors,

\[
(1-\lambda)\cdot K+_0\lambda\cdot L
=\bigcap_{u\in S^{n-1}}
\{x:\langle x,u\rangle\le h_K(u)^{1-\lambda}h_L(u)^\lambda\}.
\]

Its **Problem 1.1**, equation (1.4), asks:

\[
\boxed{
V_n((1-\lambda)\cdot K+_0\lambda\cdot L)
\ge V_n(K)^{1-\lambda}V_n(L)^\lambda
}
\tag{LBM}
\]

for every `n`, every pair of origin-symmetric convex bodies `K,L subset R^n`, and every `lambda in [0,1]`.

The same paper proves (LBM) in dimension two (Theorem 1.3). It also asks the `0<p<1` companion family in Problem 1.5 and proves that family in the plane (Theorem 1.7).

Fresh bounded current-status checks on 2026-09-19 UTC included:

1. the 2012 BLYZ source itself;
2. Christos Saroglou's work on the conjectured log-Brunn–Minkowski inequality and logarithmic sums, including unconditional classes and the implication to `(B)`;
3. Emanuel Milman, *Centro-affine differential geometry and the log-Minkowski problem*, JEMS 27 (2025), 709–772, DOI `10.4171/JEMS/1386`, which proves curvature-pinched/isomorphic regimes and interprets the conjecture spectrally;
4. XiaoRui Lu, *Logarithmic Brunn–Minkowski Inequality under n−2 Reflection Symmetries*, arXiv:2608.20730, submitted 21 August 2026, which proves a large reflection-symmetric class.

No unrestricted all-dimensional resolution was found. This is bounded negative evidence, not a worldwide novelty certificate.

A targeted search for Cartesian/product tensorization found related product-body machinery in Andrea Crasta's 2023 multiplicative Prékopa–Leindler work for unconditional sets, but no exact source for the block-tensorization statement proved below. The mechanism below is elementary enough that it may be folklore. **Priority/novelty is UNVERIFIED.** I claim only the mathematical statement and proof recorded here.

## 3. Frozen source-relevant metric

At admission I fixed

`B_cart = largest number m of blocks for which (LBM) is rigorously track-certified for every pair simultaneously representable, after one common invertible linear map, as`

\[
K=T(K_1\times\cdots\times K_m),\qquad
L=T(L_1\times\cdots\times L_m),
\]

where every factor is origin-symmetric and every block dimension is `1` or `2`.

Before this run's theorem: `B_cart=1`, from the elementary one-dimensional case and BLYZ's planar theorem.

After this run's theorem: **`B_cart=infinity`**, meaning every finite number of such blocks.

This is a restricted exact-source metric. The unrestricted source-dimensional baseline remains `2`; I do **not** infer the full `n=3` conjecture from the product theorem.

## 4. B2 — attack the negation: what must a product counterexample exploit?

The first attempt was to refute closure under Cartesian products. If closure failed, the failure would have to come from the Wulff construction: the support cap for the full product is not itself the sum of the blockwise caps.

Let

\[
\mathbb R^n=E_1\oplus\cdots\oplus E_m
\]

be an orthogonal decomposition and write

\[
K=K_1\times\cdots\times K_m,\qquad
L=L_1\times\cdots\times L_m.
\]

For `u=(u_1,...,u_m)`, support functions split exactly:

\[
h_K(u)=\sum_j h_{K_j}(u_j),\qquad
h_L(u)=\sum_j h_{L_j}(u_j).
\tag{4.1}
\]

For `alpha=1-lambda`, `beta=lambda`, put

\[
M_0(a,b)=a^\alpha b^\beta,
\]

and for `0<p\le1`,

\[
M_p(a,b)=(\alpha a^p+\beta b^p)^{1/p}.
\]

The attempted counterexample collapses because these means are **superadditive** on the positive quadrant for the entire hard range `0<=p<=1`:

\[
\sum_j M_p(a_j,b_j)
\le M_p\!\left(\sum_j a_j,\sum_j b_j\right).
\tag{4.2}
\]

For `p=0`, (4.2) is exactly Hölder:

\[
\sum_j a_j^\alpha b_j^\beta
\le \left(\sum_j a_j\right)^\alpha
   \left(\sum_j b_j\right)^\beta.
\]

For `0<p<1`, write `s=\alpha a^p+\beta b^p`. On `a,b>0`, an exact Hessian calculation gives

\[
D^2M_p(a,b)
=-\alpha\beta(1-p)s^{1/p-2}a^{p-2}b^{p-2}
\begin{pmatrix}
 b^2&-ab\\
 -ab&a^2
\end{pmatrix}\preceq0.
\tag{4.3}
\]

Thus `M_p` is concave. It is also positively one-homogeneous, and concavity plus one-homogeneity gives superadditivity. The boundary follows by continuity. At `p=1`, (4.2) is equality.

This also exposes an exact boundary of the route. For `p>1`, the sign in (4.3) reverses. Taking two pairs `(a_1,b_1)=(1,0)` and `(a_2,b_2)=(0,1)` with `alpha=beta=1/2` gives

\[
M_p(1,0)+M_p(0,1)=2^{1-1/p}>1=M_p(1,1),
\]

so the support inclusion used below reverses in this simplest test. The product mechanism is therefore aligned precisely with the difficult `p<=1` range rather than being a formal identity valid for all `p`.

A second boundary is equally important: if `K` and `L` do **not** share a common block decomposition, (4.1) does not provide the same summands on the two sides. Thus this theorem does not secretly prove the unrestricted three-dimensional problem.

## 5. B5 — add the `p` parameter: an exact tensorization theorem for the full hard family

The counterexample failure suggests proving more than the `p=0` source statement.

### Theorem 5.1 — Cartesian tensorization of BLYZ `0<=p<=1`

Fix `lambda in [0,1]` and `p in [0,1]`. Let

\[
K=\prod_{j=1}^m K_j,\qquad L=\prod_{j=1}^m L_j
\]

in an orthogonal direct sum. For each block let

\[
C_j=(1-\lambda)\cdot K_j+_p\lambda\cdot L_j
\]

be the corresponding Wulff `L_p` combination, with `p=0` interpreted logarithmically, and let

\[
C=(1-\lambda)\cdot K+_p\lambda\cdot L.
\]

Then

\[
\boxed{\prod_{j=1}^m C_j\subseteq C.}
\tag{5.1}
\]

Consequently, if every factor pair obeys the BLYZ volume inequality

\[
V(C_j)\ge V(K_j)^{1-\lambda}V(L_j)^\lambda,
\tag{5.2}
\]

then the product pair obeys the same exact inequality:

\[
\boxed{V(C)\ge V(K)^{1-\lambda}V(L)^\lambda.}
\tag{5.3}
\]

#### Proof

For `u=(u_1,...,u_m)`, abbreviate

\[
a_j=h_{K_j}(u_j),\qquad b_j=h_{L_j}(u_j).
\]

By definition of a Wulff body,

\[
h_{C_j}(u_j)\le M_p(a_j,b_j).
\]

The support of a Cartesian product is additive, so by (4.2),

\[
\begin{aligned}
h_{\prod_j C_j}(u)
 &=\sum_jh_{C_j}(u_j)\\
 &\le\sum_jM_p(a_j,b_j)\\
 &\le M_p\!\left(\sum_ja_j,\sum_jb_j\right)\\
 &=M_p(h_K(u),h_L(u)).
\end{aligned}
\tag{5.4}
\]

The final quantity is precisely the defining support cap of the global Wulff body `C`. Hence (5.4), for every direction, proves (5.1).

Volumes multiply under Cartesian products. Therefore (5.1) and the factor inequalities (5.2) give

\[
\begin{aligned}
V(C)
&\ge \prod_j V(C_j)\\
&\ge \prod_j\left[V(K_j)^{1-\lambda}V(L_j)^\lambda\right]\\
&=V(K)^{1-\lambda}V(L)^\lambda,
\end{aligned}
\]

which is (5.3). QED.

### Corollary 5.2 — arbitrarily high-dimensional exact source-valid class

BLYZ Theorems 1.3 and 1.7 prove the required factor inequalities for arbitrary origin-symmetric planar bodies for `p=0` and `0<p<1`; `p=1` is classical. In dimension one the statement is immediate for symmetric intervals. Hence Theorem 5.1 proves the full BLYZ family `0<=p<=1` for every finite Cartesian product of arbitrary one- and two-dimensional origin-symmetric factors.

In particular, the exact source Problem 1.1 holds in arbitrarily high dimension on this class. Thus

\[
\boxed{B_{\rm cart}:1\longrightarrow\infty.}
\]

This is not a finite-size experiment and not a claim about all convex bodies in those dimensions.

## 6. B11 — support/Wulff dualization and common linear images

The proof above is cleaner when read as a dual support-function statement: Cartesian products turn geometry into **addition of support functions**, while the log/Lp Wulff cap is a concave homogeneous mean. Hölder/reverse-Minkowski superadditivity is exactly the inequality needed to send a blockwise feasible support function into a globally feasible one.

There is also no coordinate-axis restriction. The Wulff operation is equivariant under a **common** invertible linear map. If `T` is invertible, then

\[
T\big((1-\lambda)\cdot K+_p\lambda\cdot L\big)
=(1-\lambda)\cdot TK+_p\lambda\cdot TL.
\tag{6.1}
\]

Indeed, for any nonzero covector `v`,

\[
h_{TK}(v)=h_K(T^Tv),\qquad h_{TL}(v)=h_L(T^Tv),
\]

and `M_p` is one-homogeneous. Transforming the defining halfspaces of the Wulff body gives (6.1). Volume is multiplied by `|det T|` on both sides of the desired inequality.

Therefore Corollary 5.2 holds for every pair simultaneously representable as

\[
K=T\left(\prod_jK_j\right),\qquad
L=T\left(\prod_jL_j\right)
\]

with one common `T`, exactly as specified in the frozen metric.

The abstract content is stronger still: **any collection of factor classes for which BLYZ is known tensorizes by direct product.** Thus future special-class theorems can be combined without redoing the global Wulff geometry.

## 7. Why this is progress but not the source solution

The unrestricted conjecture does not supply a simultaneous additive support decomposition. The theorem therefore gives a large exact family but does not move the unrestricted dimension from `2`.

The product result does, however, isolate a concrete route into dimension three. Start with

\[
K=K_2\times[-a,a],\qquad L=L_2\times[-b,b]
\]

where the inequality is now proved for arbitrary symmetric planar `K_2,L_2`. Apply a small **relative off-block shear** to one endpoint only. A common shear is vacuous by (6.1), so relative shear is the first genuinely new coupling direction.

For any product pair with a strict log-BM defect, Hausdorff/volume continuity immediately gives a nonzero neighborhood of relative shears on which the inequality remains true. Therefore the difficult local deformation problem concentrates on the equality locus of the tensorized theorem. BLYZ already classifies planar equality for `p=0` (dilates, or parallel-sided parallelograms), giving a sharply reduced set of base configurations for the first off-product second-variation calculation.

This is the most concrete next checkpoint: instead of attacking arbitrary 3D bodies, analyze relative off-block shears of the tensorized equality locus.

## 8. Prior-art guard

The targeted product search found Crasta (2023) using a multiplicative Prékopa–Leindler product-body containment for **unconditional** sets, and Saroglou's unconditional log-BM theorem. Those are close in spirit and make it especially important not to advertise Theorem 5.1 as novel without a deeper citation search. I did not find the exact arbitrary-block statement with arbitrary symmetric planar factors in the bounded search, but absence from search is not evidence of priority.

Accordingly:

- mathematical validity claimed here: **yes, by the proof on the page**;
- full source solved: **no**;
- novelty/priority of product tensorization: **UNVERIFIED / may be folklore**;
- finite simulation promoted to theorem: **no**.

## 9. 90/10 bookkeeping discipline

No finite computational claim is used in Theorem 5.1 or Corollary 5.2. The proof is analytic and exact. I therefore did **not** manufacture a checker solely to create a certificate. There is no `artifacts/` file for this run because there is no finite core requiring one.

The bookkeeping performed after the mathematics is limited to canonical-claim lifecycle repair, the new create-only reservation, this immutable report, and readback receipts.

## 10. Model / scheduler / permission truth

Actual runtime exposed to this report: **GPT-5.6 Sol**. Reasoning effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. GPT-6/maximum was requested in prompt text, but I do not claim it ran.

The exposed scheduler-management surface still provides task title, prompt, recurrence/relative start, timing mode and enabled state. It exposes **no bindable model-family selector, no reasoning-effort selector, no authenticated applied-model/effort receipt, and no guaranteed run duration**. Therefore GPT-6/maximum cannot be enforced from this scheduler surface. Changing that requires a product/workspace/API/admin surface that actually exposes and attests those fields.

The historical P26 response `You cannot modify this task` is an authorization/context boundary, not something this worker can bypass. Repository history records that P26 was later updated from another authorized context. The lawful workaround is the owning/admin-authorized context or platform support; duplicating the job or bypassing permissions is not a workaround. No scheduler mutation was attempted in this run.

## 11. Ledger delta / next run

```yaml
ledger_delta:
  worker: HARD7-01
  runtime_model: GPT-5.6 Sol
  reasoning_level: UNVERIFIED
  requested_model: GPT-6
  requested_reasoning: maximum

  predecessor_target: MAXIMAL-INTERSECTION-ELLIPSOID-UNIQUENESS
  predecessor_metric: D_MI
  predecessor_before: 2
  predecessor_after: 2
  predecessor_status: HANDOFF_SOURCE_OPEN_AFTER_TWO_SECTION_I_RECOVERIES

  active_target: LOG-BRUNN-MINKOWSKI-SYMMETRIC
  source: BLYZ_2012_Problem_1_1
  status: PARTIAL_SOURCE_OPEN
  metric: B_cart
  before: 1
  after: infinity
  unrestricted_source_dimension_before: 2
  unrestricted_source_dimension_after: 2

  methods: [B2, B5, B11]
  theorem: cartesian_tensorization_for_BLYZ_p_in_[0,1]
  common_GL_extension: true
  finite_checker_needed: false
  priority_status: UNVERIFIED_MAY_BE_FOLKLORE

  next_methods: [B6, B14, B30]
  next_route: relative_off_block_shear_of_tensorized_equality_locus
  closure_audit_requested: false
  scheduler_changed: false
  email_or_drive_used: false
```

Next run must resume this exact BLYZ claim and this checkpoint. Use a different triple, proposed **B6 / B14 / B30**: deform from the solved product class, quotient the product/equality symmetries, and localize one genuinely mixed support direction at a time. The first quantitative goal is a certified nonzero relative-shear neighborhood for a nontrivial three-dimensional equality-base subclass, without confusing that local theorem with the unrestricted conjecture.
