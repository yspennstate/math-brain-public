Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; GPT-6/maximum was requested in prompt text but this scheduler exposes no model/reasoning selector. Movement: `B=1 -> B=all finite block counts (∞)` in the frozen block-product metric. Methods tried: B2, B5, B11.

# HARD7-01 run 1 — admission and a tensorization theorem for dimensional Brunn–Minkowski

Status: **PARTIAL** for the full source conjecture. This report proves a source-valid higher-dimensional class theorem; it does **not** prove the full even-log-concave dimensional Brunn–Minkowski conjecture and makes no claim of publication-level novelty.

## 1. Continuity, exclusions, ownership, and source admission

I read the controlling HARD7/new-methods files, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, and searched current repository claims/reports under the relevant names and equivalent formulations. No previous HARD7-01 run was found. KLS/R02 and all posted owner Gaussian/submatrix work are excluded.

A tempting lane target, the **strong Gaussian product inequality**, was rejected as already solved: Frédéric Ouimet and Dylan Greaves, arXiv:2609.20234, state a 2026 proof for arbitrary positive exponents. I therefore did not reopen GPI.

The admitted target is the **dimensional Brunn–Minkowski conjecture for even log-concave measures**. The create-only claim is

`operations/claims/GZ-DIMBM-EVEN-LOGCONCAVE.md`

created at commit `2a6fc77279030c9794f628babc51457ced08097a` and read back at that commit before this report.

### Exact source statement tracked here

For every `n>=1`, every even log-concave probability measure `mu` on `R^n`, every nonempty centrally symmetric convex `K,L subset R^n`, and every `lambda in [0,1]`, prove

\[
 \mu((1-\lambda)K+\lambda L)^{1/n}
 \ge (1-\lambda)\mu(K)^{1/n}+\lambda\mu(L)^{1/n}.
 \tag{DBM_n}
\]

The original Gardner–Zvavitch Gaussian-only conjecture is not the unresolved object claimed here; that Gaussian case has been solved. The broader even-log-concave form above is the current target appearing in the dimensional Brunn–Minkowski program.

### Current-literature check, 2026-09-18 UTC

The bounded source/current-status search used the following primary or near-primary papers:

- G. Livshyts, *A universal bound in the dimensional Brunn-Minkowski inequality for log-concave measures*, arXiv:2107.00095: a universal positive exponent, not `1/n` in general.
- K.-W. Yang, *A uniform bound in the dimensional Brunn--Minkowski inequality for even log-concave measures*, arXiv:2607.10104, 11 July 2026: for the exact even-log-concave/symmetric-set scope, `p_n >= c/(n^2 log n)`.
- A. Eskenazis, A. Giannopoulos, N. Tziotziou, *Functional perimeter and the dimensional Brunn-Minkowski inequality for log-concave measures*, arXiv:2605.02747, 4 May 2026: another quantitative partial exponent bound.
- G. Livshyts, A. Marsiglietti, P. Nayar, A. Zvavitch, *On the Brunn-Minkowski inequality for general measures with applications to new isoperimetric-type inequalities*, arXiv:1504.04878: the exact `1/2` exponent in dimension two for symmetric log-concave measures and arbitrary symmetric convex sets, plus an unconditional higher-dimensional theorem.
- J. Hosle, A. Kolesnikov, G. Livshyts, *On the L_p-Brunn-Minkowski and dimensional Brunn-Minkowski conjectures for log-concave measures*, arXiv:2003.05282.
- D. Cordero-Erausquin, L. Rotem, arXiv:2111.05110 / Ann. Probab.: rotationally invariant log-concave measures are a solved special class.

A bounded search for `tensorization`, `product measure`, and `Gardner-Zvavitch` did not surface the theorem below in these papers. That negative search is **not** a novelty certificate. The mechanism is elementary enough that it may be folklore; record novelty as `UNVERIFIED` unless a dedicated citation audit establishes otherwise.

## 2. Frozen quantity

Let `B` be the largest block count for which `(DBM_N)` is proved for **every** product instance

\[
\mu=\bigotimes_{j=1}^B \mu_j,\qquad
K=\prod_{j=1}^B K_j,\qquad
L=\prod_{j=1}^B L_j,
\]

where each block dimension `n_j` is `1` or `2`, each `mu_j` is an arbitrary even log-concave probability measure on `R^{n_j}`, and `K_j,L_j` are arbitrary nonempty symmetric convex sets. Here `N=sum_j n_j` and the target exponent is the **source exponent** `1/N`, not a changed exponent.

Baseline before this run: `B=1`, from the known one-/two-dimensional result.

After this run: **every finite `B`**, recorded as `B=∞` for this restricted class.

This does not make the full source status PROVED: generic measures and generic bodies need not admit a common Cartesian factorization.

## 3. B2 — try to build a product counterexample

The first attack was the negation: can a high-dimensional counterexample be assembled by multiplying low-dimensional hard instances?

It cannot. In fact a more general exact tensorization law holds.

### Theorem 1 — harmonic tensorization of dimensional concavity exponents

For `j=1,...,B`, let `mu_j` be probability measures on vector spaces `E_j`. Fix classes of nonempty sets `C_j` closed under the Minkowski interpolation under consideration. Suppose there is `p_j>0` such that for every `A_j,B_j in C_j` and every `lambda in [0,1]`,

\[
\mu_j((1-\lambda)A_j+\lambda B_j)^{p_j}
\ge
(1-\lambda)\mu_j(A_j)^{p_j}
+\lambda\mu_j(B_j)^{p_j}.
\tag{1}
\]

Put

\[
\frac1p=\sum_{j=1}^B\frac1{p_j}.
\tag{2}
\]

For the product measure `mu=⊗_j mu_j` and product sets `A=Π_j A_j`, `B=Π_j B_j`,

\[
\mu((1-\lambda)A+\lambda B)^p
\ge (1-\lambda)\mu(A)^p+\lambda\mu(B)^p.
\tag{3}
\]

#### Proof

Write

\[
A_{j,\lambda}=(1-\lambda)A_j+\lambda B_j,
\qquad
f_j(\lambda)=\mu_j(A_{j,\lambda})^{p_j}.
\]

Cartesian Minkowski interpolation factorizes exactly:

\[
(1-\lambda)\prod_j A_j+\lambda\prod_j B_j
=\prod_j A_{j,\lambda}.
\tag{4}
\]

Define weights

\[
w_j=\frac{p}{p_j}.
\]

Equation (2) gives `w_j>0` and `sum_j w_j=1`. Therefore

\[
\mu\!\left(\prod_j A_{j,\lambda}\right)^p
=\prod_j \mu_j(A_{j,\lambda})^p
=\prod_j f_j(\lambda)^{w_j}.
\tag{5}
\]

The weighted geometric mean

\[
G(x_1,\ldots,x_B)=\prod_j x_j^{w_j}
\]

is concave and coordinatewise nondecreasing on `R_+^B`. By (1), coordinatewise,

\[
f_j(\lambda)\ge (1-\lambda)f_j(0)+\lambda f_j(1).
\]

Hence monotonicity of `G`, followed by concavity of `G`, yields

\[
\begin{aligned}
G(f_1(\lambda),\ldots,f_B(\lambda))
&\ge G((1-\lambda)f_1(0)+\lambda f_1(1),\ldots)\\
&\ge (1-\lambda)G(f_1(0),\ldots,f_B(0))
+\lambda G(f_1(1),\ldots,f_B(1)).
\end{aligned}
\]

Together with (5), this is exactly (3). If some mass is zero, the same conclusion follows by continuity of `G` on the closed nonnegative orthant. `□`

### Corollary 2 — arbitrary-dimensional block products of one- and two-dimensional factors satisfy the conjectured exponent

Assume every `n_j in {1,2}`; let `mu_j` be any even log-concave probability measure on `R^{n_j}` and `K_j,L_j` arbitrary nonempty symmetric convex sets. By the known `n_j<=2` dimensional Brunn–Minkowski theorem, (1) holds with

\[
p_j=1/n_j.
\]

Theorem 1 gives

\[
\frac1p=\sum_j n_j=N,
\quad\text{so}\quad p=1/N.
\]

Thus

\[
\left(\bigotimes_j\mu_j\right)
\left((1-\lambda)\prod_jK_j+\lambda\prod_jL_j\right)^{1/N}
\ge
(1-\lambda)\prod_j\mu_j(K_j)^{1/N}
+\lambda\prod_j\mu_j(L_j)^{1/N}.
\tag{6}
\]

This is exactly `(DBM_N)` for this block-product class, for arbitrary finite ambient dimension `N` obtained from `1`- and `2`-dimensional blocks. `□`

### Counterexample consequence

A counterexample to the full even-log-concave conjecture cannot be manufactured as a simultaneous Cartesian product of only one-/two-dimensional factor instances. Any product-decomposable counterexample must contain at least one factor on which the corresponding dimensional Brunn–Minkowski inequality itself fails. In particular, a three-dimensional counterexample cannot have a common `1+2` product decomposition of the measure and both bodies.

This is the useful result of the B2 attack: the natural low-dimensional product counterexample mechanism is ruled out exactly, rather than merely failing numerically.

## 4. B5 — add an exponent parameter

The proof above does more than tensorize the conjectured exponents. It gives the exact harmonic rule

\[
p_{\rm product}=\left(\sum_j p_j^{-1}\right)^{-1}.
\tag{7}
\]

Thus any future improvement to a factor exponent automatically lifts to its product class without losing anything beyond the forced harmonic dimension accounting. For equal factors `p_j=q`, `B` blocks give `p=q/B`.

This clarifies the scale: if each `n_j`-dimensional block has the conjectural exponent `1/n_j`, tensorization lands **exactly** at `1/N`, not at a weaker dimension-dependent value. Conversely, a proof architecture that treats independent blocks separately cannot beat the harmonic law without using extra cross-block structure.

This was the B5 parameter deformation attempted this run: interpolate the concavity exponent itself rather than a covariance parameter. It succeeded in producing the stronger Theorem 1.

## 5. B11 — dualize the nonlinear aggregation step

For completeness, the only nonlinear ingredient in Theorem 1 admits an elementary dual formula. For positive `x_j` and weights `w_j>0`, `sum w_j=1`,

\[
\prod_jx_j^{w_j}
=
\inf_{a_j>0:\,\prod_j a_j^{w_j}=1}
\sum_j w_j a_jx_j.
\tag{8}
\]

Indeed weighted AM–GM gives the lower bound

\[
\sum_j w_j a_jx_j\ge \prod_j(a_jx_j)^{w_j}=\prod_jx_j^{w_j}.
\]

Equality is attained by `a_j=G(x)/x_j`, since then `prod_j a_j^{w_j}=1` and every `a_jx_j=G(x)`. Formula (8) writes the weighted geometric mean as an infimum of linear functionals, making its concavity transparent.

So the tensorization theorem can be read as a primal/dual statement: factorwise concavity passes through an exact concave aggregator whose dual variables impose the single multiplicative normalization in (8). No covariance sign assumption or unconditional coordinate symmetry is used in this step.

## 6. Why this class is not merely the standard unconditional special case

The corollary allows each two-dimensional factor to be an arbitrary **centrally symmetric** log-concave measure, not an unconditional one. For example, on `R^2`, the density

\[
f(x,y)\propto \exp\!\left[-(x^2+xy+y^2)^2\right]
\]

is even and log-concave because `q(x,y)=x^2+xy+y^2` is a nonnegative convex quadratic and `q^2` is convex; it is not invariant under the independent sign flip `x -> -x`. Arbitrary products of such two-dimensional factors, with arbitrary symmetric factor bodies, are therefore covered by Corollary 2 even though the ambient instance need not be unconditional or rotationally invariant.

This observation is only used to show that the tensorized class is genuinely broader than a coordinate-unconditional toy family. It is not a novelty claim about this specific density.

## 7. What remains open

The source-wide obstruction is now clearer. The theorem handles all instances that decompose into solved low-dimensional blocks. A proof of the full conjecture must control **irreducible cross-block geometry**: either the measure, one of the bodies, or both must couple at least three directions in a way that cannot be removed by a common Cartesian factorization.

A natural next attack is therefore not another product calculation. It is to freeze `n=3` and analyze the first genuinely irreducible perturbation away from a `1+2` product instance, asking whether the `1/3`-concavity defect has a positive second variation transverse to the product manifold. This would use the B5 interpolation idea in a way that can either extend the theorem to a neighborhood or exhibit the shape of a counterexample.

No claim of closure is made. No independent audit has been requested or fabricated.

## 8. Method outcomes

- **B2 ATTACK THE NEGATION:** tried to create a high-dimensional counterexample by taking products of low-dimensional factors. **Failed constructively:** Theorem 1 proves such a mechanism cannot work when every factor satisfies its own dimensional inequality.
- **B5 ADD A PARAMETER:** promoted the source exponent to arbitrary factor exponents `p_j`. **Succeeded:** exact harmonic tensorization law (7).
- **B11 DUALIZE:** derived the variational formula (8) for the weighted geometric mean. **Succeeded:** gives a one-line dual explanation of the concavity aggregator in the proof.

## 9. ledger_delta

```yaml
track: HARD7-01
source: even-log-concave dimensional Brunn-Minkowski conjecture
claim: operations/claims/GZ-DIMBM-EVEN-LOGCONCAVE.md
claim_commit: 2a6fc77279030c9794f628babc51457ced08097a
metric: maximum low-dimensional block count B covered at source exponent for all block-product instances
metric_before: 1
metric_after: infinity  # every finite B
status_before: ADMISSION_PENDING
status_after: PARTIAL
unchanged_count_before: UNKNOWN
unchanged_count_after: 0
methods_this_run: [2, 5, 11]
remaining_obligation: prove or refute DBM_n for genuinely irreducible even log-concave instances, beginning with an n=3 cross-block perturbation
novelty: UNVERIFIED; tensorization mechanism may be folklore
closure_audits: 0
```
