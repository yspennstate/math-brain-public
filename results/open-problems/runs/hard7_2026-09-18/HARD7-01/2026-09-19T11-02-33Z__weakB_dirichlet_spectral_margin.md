Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. No source-metric movement: `D_B=2 -> D_B=2`. Methods tried: B7 / B14 / B17.**

# HARD7-01 run 15 — simplex quotient, exact Dirichlet spectral gap, and a curvature-margin theorem on the `l_q^2` cone

Status: **PARTIAL / source OPEN / STUCK1 recovery continuation**.

## 1. Continuity, source, ownership, and run-start checks

This invocation continues the exact admitted HARD7-01 target from

`runs/hard7_2026-09-18/HARD7-01/2026-09-19T10-14-16Z__weakB_extreme_split_spectral_obstruction.md`

at report commit

`7822280d842671ec4cad988e96a1292d008aabec`.

The active create-only reservation remains

`operations/claims/B-WEAK-EVEN-LOGCONCAVE.md`,

owner **HARD7-01**, status `CLAIMED / source OPEN / research PARTIAL only`. No ownership overwrite or alias minting is performed here.

I reread/reconciled the controlling HARD7 file, the new-methods policy, the owner directive, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the canonical claim, the latest own report, and the newest visible neighboring R02 state. The latter is on an unrelated successor-admission gate and does not claim weak `(B)`.

The exact source target remains:

> For every integer `n>=1`, every even log-concave probability measure `mu` on `R^n`, and every origin-symmetric convex body `K`, prove that `t -> mu(e^t K)` is log-concave on `R`.

The frozen source metric is

`D_B = largest d such that the exact weak (B)-conjecture is proved for every admissible (mu,K) in every dimension n<=d`.

The verified source baseline remains Saroglou's planar result,

\[
D_B=2.
\]

Nothing in this report proves the unrestricted three-dimensional source statement, hence

\[
\boxed{D_B:2\longrightarrow2}.
\]

This is **no source-metric movement**.

### Current-literature sentinel, 2026-09-19

A fresh bounded search again recovered Cordero-Erausquin--Rotem, *Improved log-concavity for rotationally invariant measures of symmetric convex sets* (Ann. Probab. 2023; arXiv:2111.05110), which states the general even-log-concave `(B)` conjecture and proves the rotationally invariant class; Armeniakos--Ulivelli, arXiv:2602.23350 (26 February 2026), which proves an implication from a strengthened dimensional Brunn--Minkowski statement and structured cases; and recent work on the already-proved Gaussian `(B)` theorem/stability rather than the unrestricted even-log-concave conjecture. I found no full all-dimensional resolution in this bounded search. That is negative bounded-search evidence only, not a worldwide openness or novelty certificate.

For the simplex spectral input below, I also checked the standard Dirichlet/Wright--Fisher literature. The exact spectral calculation is classical; in particular multivariate Jacobi/Wright--Fisher spectral decompositions and Dirichlet Poincare inequalities are known. Miclo--Feng--Wang, *Poincare Inequality for Dirichlet Distributions and Infinite-Dimensional Generalizations*, arXiv:1504.02829, is one such reference. I do **not** claim the Dirichlet spectral gap itself as new. The novelty of combining it with the cone-Hessian split reduction is unverified.

## 2. Checkpoint inherited from run 14

Let `phi,psi` be even convex `C^2` positively `p`-homogeneous functions of the same degree, let

\[
H=\phi+\psi,\qquad S_H=\{z:H(z)=1\},
\]

and let `nu_H` be cone probability on `S_H`. Set

\[
U(z)=\phi(z),\qquad m=\mathbb E_{\nu_H}U.
\]

For `X` with density proportional to `e^{-H(x)}`, cone polar coordinates give `X=RZ`, `R^p~Gamma(n/p,1)`, `Z~nu_H`, independently. Writing `k=n/p`, run 14 recorded the exact identity

\[
\operatorname{Cov}(\phi(X),\psi(X))
=
k\left[m(1-m)-(k+1)\operatorname{Var}_{\nu_H}(U)\right].
\tag{2.1}
\]

Thus the common-degree correlation target is exactly

\[
\operatorname{Var}_{\nu_H}(U)
\le \frac{p}{n+p}m(1-m).
\tag{2.2}
\]

For the first unresolved test slice `n=3,p=2`, this is

\[
\operatorname{Var}(U)\le \frac25m(1-m).
\tag{2.3}
\]

Run 14 also proved for `p=2` that, with `A=\nabla^2H`, `B=\nabla^2\phi`, `P=A^{-1/2}BA^{-1/2}`, and `a=A^{1/2}z`, one has

\[
|a|^2=2,\qquad U=\frac12 a^TPa,
\]

and for the tangential inverse-Hessian metric

\[
\Gamma_H(U)=|Pa-Ua|^2\le 2U(1-U).
\tag{2.4}
\]

The naive plan `lambda_even(H)>=n` was then refuted by the `l_q^2` cone. The useful unresolved question is more precise: what extra restriction on a **source-realizable convex split** repairs the deficient cone spectral gap?

This run attacks that question with a group quotient and an exact spectral constant.

## 3. B14 — FIND THE GROUP ACTING: quotient the `l_q^2` cone by coordinate signs

Fix `q>2` and

\[
H_q(x)=\left(\sum_{i=1}^n |x_i|^q\right)^{2/q},
\qquad
S_q=\left\{z:\sum_i|z_i|^q=1\right\}.
\tag{3.1}
\]

The hyperoctahedral sign subgroup `(Z/2Z)^n` acts on `S_q`. For a sign-invariant function, introduce simplex coordinates

\[
W_i=|Z_i|^q,\qquad W_i\ge0,\qquad \sum_iW_i=1.
\tag{3.2}
\]

Under cone probability `nu_q`, the standard gamma/cone-coordinate calculation gives

\[
(W_1,\ldots,W_n)\sim\operatorname{Dirichlet}(1/q,\ldots,1/q).
\tag{3.3}
\]

This quotient is important because the bad spectral mode found in run 14 is not an arbitrary angular accident: it lives in this exact sign-invariant quotient.

### Exact quotient Dirichlet form

Work on the positive orthant; the coordinate hyperplanes are cone-null and the formulas extend by approximation. Put `S=\sum_i x_i^q` and write a degree-zero sign-invariant function as

\[
f(x)=g(w_1,\ldots,w_n),\qquad w_i=\frac{x_i^q}{S}.
\]

On `S_q` one has `S=1`. If `g_i=\partial_i g` and `\bar g=\sum_iw_i g_i`, then

\[
\partial_{x_i}f=q x_i^{q-1}(g_i-\bar g).
\tag{3.4}
\]

For `u_i=x_i^{q-1}` and

\[
D=2(q-1)\operatorname{diag}(x_i^{q-2}),
\]

the Hessian of `H_q` on `S_q` is

\[
A=\nabla^2H_q
=D+2(2-q)uu^T.
\tag{3.5}
\]

Let `v=\nabla f`. Homogeneity gives `v\cdot x=0`, while

\[
D^{-1}u=\frac{x}{2(q-1)}.
\]

Therefore the rank-one Sherman--Morrison correction in `v^TA^{-1}v` vanishes. Direct substitution of (3.4) yields

\[
\boxed{
\Gamma_{H_q}(g)
=
\frac{q^2}{2(q-1)}
\left[
\sum_i w_i g_i^2-\left(\sum_iw_i g_i\right)^2
\right].
}
\tag{3.6}
\]

Thus the inverse-Hessian energy on the unconditional sector is exactly a scalar multiple of the standard Wright--Fisher carré du champ on the simplex.

**Outcome B14.** The sign quotient removes irrelevant angular degrees of freedom and turns the geometric spectral problem into an exact Dirichlet one.

## 4. B17 — LOOK FOR YOUR NUMBERS SOMEWHERE ELSE: the run-14 Rayleigh quotient is the exact Dirichlet gap

Let

\[
\alpha=1/q,\qquad \alpha_0=n/q.
\]

For the symmetric Dirichlet law in (3.3), define

\[
\Gamma_0(g)=
\sum_iw_i g_i^2-\left(\sum_iw_i g_i\right)^2.
\tag{4.1}
\]

The reversible Wright--Fisher generator with this carré du champ can be written

\[
L g
=
\sum_{i,j}w_i(\delta_{ij}-w_j)\partial_{ij}g
+
\sum_i(\alpha-\alpha_0w_i)\partial_i g.
\tag{4.2}
\]

Its sharp spectral gap is

\[
\lambda_0=\alpha_0=\frac nq.
\tag{4.3}
\]

For completeness, the degree-one centered coordinate satisfies exactly

\[
-L\left(w_1-\frac1n\right)
=
\alpha_0\left(w_1-\frac1n\right),
\]

so no larger gap is possible. Conversely, the classical multivariate Jacobi/Wright--Fisher polynomial decomposition triangularizes `-L` by total degree: the degree-`d` diagonal eigenvalue is

\[
d(d-1+\alpha_0),\qquad d=0,1,2,\ldots,
\]

with the lower-degree terms removed by orthogonalization. Polynomials are dense in `L^2` of the Dirichlet law. Hence the first nonzero eigenvalue is indeed `\alpha_0`. This is standard spectral theory, reused here rather than claimed new.

Multiplying by the factor in (3.6), the exact inverse-Hessian spectral gap **within the unconditional/sign-invariant sector** is therefore

\[
\boxed{
\lambda_{\rm unc}(n,q)
=
\frac{q^2}{2(q-1)}\frac nq
=
\frac{nq}{2(q-1)}.
}
\tag{4.4}
\]

The coordinate `W_1` used in run 14 is an equality mode, so its Rayleigh quotient was not merely a convenient upper bound: it found the exact unconditional gap.

For `n=3,q=4`,

\[
\boxed{\lambda_{\rm unc}=2.}
\tag{4.5}
\]

**Outcome B17.** The mysterious constant from the counterexample search is exactly the Wright--Fisher gap after the Hessian-metric scaling. The deficient gap is structural, not a poor choice of test function.

## 5. B7 — TAKE THE LIMIT: quantify exactly how the Gaussian gap decays

Formula (4.4) gives a complete deformation picture:

\[
\lambda_{\rm unc}(n,2)=n,
\qquad
\lambda_{\rm unc}(n,q)=\frac{nq}{2(q-1)},
\qquad
\lim_{q\to\infty}\lambda_{\rm unc}(n,q)=\frac n2.
\tag{5.1}
\]

Thus the sharp Gaussian value `n` deteriorates continuously to `n/2`; there is no hidden discontinuity at the non-Euclidean cone. This suggests that a successful theorem cannot ask the ambient cone to supply the missing spectral factor. It has to use the fact that `U` comes from a complementary pair of convex Hessians.

That observation leads to the main new restricted theorem of this run.

## 6. Curvature-margin theorem for source-realizable unconditional splits

### Theorem 6.1

Let `q>2`, let `H_q` be as in (3.1), and let

\[
H_q=\phi+\psi
\]

be an unconditional even `C^2` convex split into positively `2`-homogeneous functions. At every smooth point of `S_q`, put

\[
A=\nabla^2H_q,\qquad B=\nabla^2\phi.
\]

Assume a uniform relative curvature margin

\[
\delta A\preceq B\preceq(1-\delta)A
\qquad\text{for some }0\le\delta<\frac12.
\tag{6.1}
\]

Let `U=\phi|_{S_q}` and `m=E_{\nu_q}U`. Then

\[
\boxed{
\frac{\operatorname{Var}_{\nu_q}(U)}{m(1-m)}
\le
\frac{2}{\lambda_{\rm unc}(n,q)+2}(1-2\delta)^2.
}
\tag{6.2}
\]

Consequently, the common-degree correlation inequality (2.2) for `p=2` holds whenever

\[
\boxed{
\delta\ge
\delta_c(n,q)
:=
\frac12\left[
1-\sqrt{\frac{\lambda_{\rm unc}(n,q)+2}{n+2}}
\right].
}
\tag{6.3}
\]

#### Proof

As in run 14, define

\[
P=A^{-1/2}BA^{-1/2},\qquad a=A^{1/2}z.
\]

Euler's identity for degree two gives

\[
|a|^2=2,
\qquad
U=\frac12a^TPa.
\tag{6.4}
\]

Assumption (6.1) says every eigenvalue of `P` lies in `[\delta,1-\delta]`. Diagonalize `P`; if `\lambda_j` are its eigenvalues and

\[
\rho_j=\frac{a_j^2}{2},
\qquad
\sum_j\rho_j=1,
\]

then `U=\sum_j\rho_j\lambda_j`. The exact tangential identity from run 14 becomes

\[
\Gamma_{H_q}(U)
=|Pa-Ua|^2
=2\sum_j\rho_j(\lambda_j-U)^2.
\tag{6.5}
\]

The elementary Bhatia--Davis variance bound for a random variable supported on `[\delta,1-\delta]` gives

\[
\Gamma_{H_q}(U)
\le
2(U-\delta)(1-\delta-U).
\tag{6.6}
\]

Because the split is unconditional, `U` lies in the sign-invariant sector, so the sharp Poincare inequality from (4.4) applies:

\[
\lambda_{\rm unc}\operatorname{Var}(U)
\le
\mathbb E\Gamma_{H_q}(U).
\tag{6.7}
\]

Since (6.1) and (6.4) imply `\delta\le U\le1-\delta`, combine (6.6)-(6.7):

\[
\lambda_{\rm unc}\operatorname{Var}(U)
\le
2\mathbb E[(U-\delta)(1-\delta-U)].
\]

But

\[
\mathbb E[(U-\delta)(1-\delta-U)]
=
(m-\delta)(1-\delta-m)-\operatorname{Var}(U).
\]

Hence

\[
(\lambda_{\rm unc}+2)\operatorname{Var}(U)
\le
2(m-\delta)(1-\delta-m).
\tag{6.8}
\]

Furthermore,

\[
(m-\delta)(1-\delta-m)
=
m(1-m)-\delta(1-\delta).
\]

For `m\in[\delta,1-\delta]`, `m(1-m)\le1/4`, so

\[
\frac{(m-\delta)(1-\delta-m)}{m(1-m)}
=
1-\frac{\delta(1-\delta)}{m(1-m)}
\le
1-4\delta(1-\delta)
=(1-2\delta)^2.
\]

This proves (6.2).

For `p=2`, the target (2.2) is

\[
\frac{\operatorname{Var}(U)}{m(1-m)}\le\frac{2}{n+2}.
\]

Thus it is enough that

\[
\frac{2}{\lambda_{\rm unc}+2}(1-2\delta)^2
\le
\frac2{n+2},
\]

which is equivalent to (6.3). QED.

### Exact first unsolved calibration: `n=3,q=4`

Here `\lambda_{\rm unc}=2`, so

\[
\delta_c(3,4)
=
\frac12\left(1-\frac2{\sqrt5}\right)
=
\frac12-\frac1{\sqrt5}
\approx0.0527864.
\tag{6.9}
\]

The rational margin

\[
\delta=\frac1{16}
\]

is strictly larger than `\delta_c`, because `1/\sqrt5>7/16` is exactly equivalent after squaring positive quantities to `256>245`. Theorem 6.1 gives

\[
\frac{\operatorname{Var}(U)}{m(1-m)}
\le
\frac12\left(\frac78\right)^2
=
\boxed{\frac{49}{128}}
<
\frac25.
\tag{6.10}
\]

Substitution into (2.1), with `k=3/2`, yields the explicit strict covariance slack

\[
\boxed{
\operatorname{Cov}(\phi(X),\psi(X))
\ge
\frac{33}{512}m(1-m)>0
}
\tag{6.11}
\]

whenever `0<m<1`.

This is a genuine restricted theorem for a source-relevant homogeneous correlation slice. It is **not** the unrestricted weak `(B)` conjecture and does not move `D_B`.

## 7. What changed mathematically

Run 14 showed that first-order Hessian energy plus a universal ambient spectral-gap claim cannot work: the ambient `l_4^2` cone has an unconditional mode with Rayleigh quotient `2<3`.

This run sharpens that obstruction in two directions:

1. the quotient calculation proves that `2` is the **exact** unconditional gap, so searching for a better sign-invariant test function cannot repair it;
2. source realizability contributes a second-order quantity absent from the relaxed obstruction: a relative Hessian margin. A margin as small as `1/16` already repairs the entire missing gap in the first `n=3,q=4` case.

Therefore any counterexample to this homogeneous route on the `n=3,q=4` cone must approach the curvature boundary

\[
\lambda_{\min}(A^{-1/2}BA^{-1/2})=0
\quad\text{or}\quad
\lambda_{\max}(A^{-1/2}BA^{-1/2})=1
\]

somewhere. This is exactly consistent with run 14's extreme-split proposition: the remaining difficulty is concentrated near curvature-complementary extreme splits, not in the interior of the convex-split cone.

That is a materially narrower remaining obligation than the previous generic spectral-gap question, even though the source metric itself remains `2`.

## 8. Exact checker and scope

The finite rational core was checked by

`artifacts/hard7_2026-09-18/HARD7-01/2026-09-19T11-02-33Z__l4_dirichlet_margin_check.py`

creation commit

`1e0623f9317d0eed95b161a81f8ab325e32ab8cc`,

with archived output

`artifacts/hard7_2026-09-18/HARD7-01/2026-09-19T11-02-33Z__l4_dirichlet_margin_check.out`

creation commit

`be37012e9b8e8b80281c5e6fc9ecddddb3f2c777`.

The output ends

`ALL_EXACT_CHECKS_PASS = True`.

It checks exactly the `n=3,q=4` Dirichlet moments, the gap equality mode, the `delta=1/16` rational margin, `49/128<2/5`, the covariance coefficient `33/512`, and the integer comparison `256>245`. The general theorem is proved on the page above; the checker is not substituted for that proof.

## 9. Section-B outcomes and lifecycle

- **B14 / FIND THE GROUP ACTING:** quotienting by coordinate signs converts the cone Hessian energy exactly into a Wright--Fisher Dirichlet form.
- **B17 / LOOK FOR YOUR NUMBERS SOMEWHERE ELSE:** the prior Rayleigh quotient `nq/[2(q-1)]` is recognized and proved to be the exact unconditional Dirichlet spectral gap after geometric scaling.
- **B7 / TAKE THE LIMIT:** the gap interpolates from `n` at `q=2` to `n/2` as `q->infinity`; this exposes the exact spectral loss and leads to the compensating curvature-margin theorem.

These three method numbers are different from the preceding run's B4/B15/B27 and had not been used on the current weak-`(B)` target in the recovered run history.

The source metric has not moved, but the remaining obligation has changed: the interior relative-curvature region is now quantitatively controlled in the unconditional `l_q^2` model, and the unresolved homogeneous obstruction is pushed to the `delta=0` curvature boundary/extreme-split regime. Therefore this report does not manufacture a new stuck cycle merely from the unchanged source number. If the next runs leave that boundary obligation unchanged for the Section-I threshold, the required next stuck-recovery/rotation protocol applies.

## 10. Scheduler/model capability truth

The exposed scheduling interface still provides title, prompt, schedule/timing, enabled state, and related task controls, but no binding model-family selector, no binding reasoning-effort selector, and no guaranteed execution duration. Thus `GPT-6 / maximum` remains prompt-requested only. The actual runtime visible here is **GPT-5.6 Sol**, while reasoning effort is **UNVERIFIED**.

The historical `You cannot modify this task` response for a P26 scheduler ID remains an authorization-context issue, not something a repository write can repair. The lawful route is the owning/authorized workspace or API/admin context, an authorized ownership/permission repair/transfer, or platform support. No duplicate schedule or permission bypass is appropriate. No scheduler mutation was attempted in this run.

## 11. Status and next checkpoint

**Status: PARTIAL. Source weak `(B)` remains OPEN in the checked literature.**

Durable new checkpoint:

\[
\lambda_{\rm unc}(n,q)=\frac{nq}{2(q-1)},
\]

and for unconditional convex `2`-homogeneous splits of `H_q` satisfying `\delta A\preceq B\preceq(1-\delta)A`,

\[
\frac{\operatorname{Var}(U)}{m(1-m)}
\le
\frac{2}{\lambda_{\rm unc}+2}(1-2\delta)^2.
\]

For `n=3,q=4`, every such split with `\delta>=1/16` satisfies the common-degree target with explicit slack `33/512*m(1-m)`.

The next useful mathematical question is not another ambient-gap estimate. It is whether curvature-complementary extreme splits (`delta=0`) admit a structural reduction strong enough to prove the `2/5` cone-variance inequality, or instead produce a genuine source-valid counterexample in the homogeneous slice.

No closure, source refutation, paper, novelty certificate, or independent audit is claimed.

```yaml
ledger_delta:
  worker: HARD7-01
  canonical_claim: B-WEAK-EVEN-LOGCONCAVE
  source_status: OPEN_IN_CHECKED_LITERATURE
  status: PARTIAL
  fixed_metric:
    name: D_B
    before: 2
    after: 2
    movement: none
  methods: [B7, B14, B17]
  new_checkpoint:
    unconditional_lq_hessian_gap: "lambda_unc(n,q)=n*q/(2*(q-1))"
    curvature_margin_bound: "Var(U)/(m(1-m)) <= 2/(lambda_unc+2)*(1-2delta)^2"
    n3_q4_rational_margin: "delta=1/16 gives 49/128 < 2/5"
    n3_q4_covariance_slack: "33/512 * m(1-m)"
  code_commit: 1e0623f9317d0eed95b161a81f8ab325e32ab8cc
  output_commit: be37012e9b8e8b80281c5e6fc9ecddddb3f2c777
  remaining_obligation: "control curvature-boundary/extreme splits (delta=0) in the n=3,p=2 homogeneous route, then return to the full nonhomogeneous weak-(B) source"
```
