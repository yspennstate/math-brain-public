Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. No source-metric movement: `D_B=2 -> D_B=2`. Methods tried: B13 / B9 / B10.**

# HARD7-01 run 17 — gradient shares and the full globally-even spectral gap on the `l_q^2` cone

Status: **PARTIAL / source OPEN / STUCK1 recovery continuation**.

## 1. Continuity, ownership, required reads, and current-source sentinel

This run continues the exact admitted HARD7-01 target from

`runs/hard7_2026-09-18/HARD7-01/2026-09-19T12-05-39Z__weakB_first_eigenspace_split_cone.md`.

The active create-only claim remains

`operations/claims/B-WEAK-EVEN-LOGCONCAVE.md`,

owner **HARD7-01**, status `CLAIMED / source OPEN / research PARTIAL only`. No claim file was overwritten and no equivalent owner was found in the bounded repository alias search.

At run start I reread/reconciled the HARD7 control, the new-methods policy and owner directive, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the current claim, the newest own checkpoint, and the newest visible neighboring R02 report (`runs/R02/20260919T1208Z_successor_gate_kressner_owned_p0157_reassigned_3_6_11_3f7c9a12.md`). The neighboring track is unrelated. Indexed repository searches for `(B)-conjecture`, weak `(B)`, log-concavity of dilates and the canonical claim recovered no competing owner. As in earlier runs, I do not falsely claim that a bounded connector rendered every byte of the roughly 780-row append-only intake corpus; the relevant current ledgers and indexed alias surface were checked.

The exact source target remains:

> For every integer `n>=1`, every even log-concave probability measure `mu` on `R^n`, and every origin-symmetric convex body `K`, prove that `t -> mu(e^t K)` is log-concave on `R`.

The frozen source metric is

`D_B = largest d for which this exact statement is proved for all admissible (mu,K) in every dimension n<=d`.

Saroglou's planar theorem still gives the verified baseline, hence

\[
\boxed{D_B:2\longrightarrow2.}
\]

### Current-literature check, 2026-09-19

I reran bounded searches for the full weak `(B)` statement and recent `(B)` work. The checked sources still separate the open full conjecture from solved subclasses:

- Cordero-Erausquin--Rotem, *Improved log-concavity for rotationally invariant measures of symmetric convex sets*, Ann. Probab. 51 (2023), arXiv:2111.05110, proves the rotationally invariant class, not all even log-concave measures.
- Armeniakos--Ulivelli, arXiv:2602.23350 (submitted 2026-02-26), proves that a strengthened dimensional Brunn--Minkowski condition implies `(B)` and recovers hereditarily convex measures, not the full source statement.
- Putterman, arXiv:2608.08472 (submitted 2026-08-09), concerns sharp stability for the Gaussian `(B)` theorem and its Gaussian strong/functional extensions, not a resolution for all even log-concave measures.
- The original Cordero-Erausquin--Fradelizi--Maurey `(B)` paper proves the Gaussian theorem and already treats/comments on the coordinatewise unconditional setting. Marsiglietti, arXiv:1411.2538 / Pacific J. Math. 277 (2015), explicitly records the unconditional `(B)` case and related `L^p` inequalities. Therefore **I do not present an unconditional special case as new**.
- For the Dirichlet/Wright--Fisher spectral input, the sharp Poincare inequality and full spectrum are standard; see Miclo--Feng--Wang, arXiv:1504.02829. The ground-state transform used below is likewise standard machinery. No novelty claim is made for that mechanism.

I found no full all-dimensional even-log-concave resolution in this bounded current search. This is bounded negative evidence only, not an exhaustive novelty certificate.

## 2. Inherited exact obstruction

For a common-degree positively `2`-homogeneous split

\[
H=\phi+\psi,
\]
run 12 derived the exact cone-measure covariance identity

\[
\operatorname{Cov}(\phi(X),\psi(X))
=\frac n2\left[m(1-m)-\left(\frac n2+1\right)\operatorname{Var}_{\nu_H}(U)\right],
\tag{2.1}
\]
where `X` has density proportional to `e^{-H}`, `S_H={H=1}`, `nu_H` is cone probability,

\[
U=\phi|_{S_H},\qquad m=\mathbb E_{\nu_H}U.
\]

Thus this local/common-degree correlation inequality follows from

\[
\boxed{
\frac{\operatorname{Var}(U)}{m(1-m)}\le\frac{2}{n+2}.
}
\tag{2.2}
\]

Runs 14--16 specialized to

\[
H_q(x)=\left(\sum_{i=1}^n|x_i|^q\right)^{2/q},\qquad q>2,
\tag{2.3}
\]
and found the exact sign-invariant Hessian-metric gap

\[
\lambda_{\rm unc}(n,q)=\frac{nq}{2(q-1)}.
\tag{2.4}
\]

For `n=3,q=4`, the first Dirichlet mode has gap `2`, below the naive desired `3`. Run 16 nevertheless proved that when the split itself lies purely in that first eigenspace, convex complementarity forces the much stronger sharp ratio `2/35`. The remaining checkpoint was to understand arbitrary nonlinear splits, in particular whether a large first projection could coexist with higher modes.

This run removes that projection obstruction on the entire smooth `l_q^2` slice, without assuming that the two summands are coordinatewise unconditional.

## 3. B13 — FIND WHAT ONLY INCREASES: coordinate convexity forces gradient shares into `[0,1]`

Assume throughout this theorem that `n>=2`, `q>2`, and

\[
H_q=\phi+\psi
\tag{3.1}
\]
with `phi,psi` convex, positively `2`-homogeneous and `C^2` on `R^n\setminus\{0\}`. Global evenness may also be imposed, as it is in the source functional setting; the coordinate argument below actually needs only the stated convex split and homogeneity.

Let

\[
A=\nabla^2H_q,\qquad B=\nabla^2\phi.
\]
Then

\[
0\preceq B\preceq A.
\tag{3.2}
\]

Fix an index `i` and a nonzero point on the coordinate face `x_i=0`. Since `q>2`,

\[
A_{ii}=0
\qquad\text{on }\{x_i=0\}\setminus\{0\}.
\tag{3.3}
\]

Both `B` and `A-B=Hess psi` are positive semidefinite, hence (3.3) forces

\[
B_{ii}=0.
\]
For a positive semidefinite matrix, `|B_ij|^2<=B_ii B_jj`, so the entire `i`th row vanishes there:

\[
B_{ij}=0\qquad\forall j.
\tag{3.4}
\]

Therefore the normal derivative

\[
a_i(y):=\partial_i\phi(0,y)
\]
is constant on each connected component of the punctured coordinate face. But `grad phi` is positively `1`-homogeneous, so along every positive ray in that component

\[
a_i(ty)=t a_i(y).
\]
A quantity that is both constant along the ray and multiplied by `t` must vanish. Hence

\[
\boxed{\partial_i\phi=0=\partial_i\psi\quad\text{on }x_i=0,\ x\ne0.}
\tag{3.5}
\]

Now freeze all other coordinates and view `phi` and `psi` as convex functions of the single coordinate `x_i`. Their derivatives vanish at `0`, so their derivatives are nonnegative for `x_i>0` and nonpositive for `x_i<0`. Since their sum is `H_q`, at every interior point `x_i!=0` the ratio

\[
h_i(x):=\frac{\partial_i\phi(x)}{\partial_iH_q(x)}
\tag{3.6}
\]
satisfies

\[
\boxed{0\le h_i(x)\le1.}
\tag{3.7}
\]

This is the monotone quantity the earlier ambient spectral argument was missing: not the Hessian eigenvalue by itself, but the **fraction of each coordinate radial derivative allocated to one convex summand**.

On

\[
S_q=\left\{x:\sum_i|x_i|^q=1\right\},
\]
put

\[
w_i=|x_i|^q,
\qquad U=\phi|_{S_q}.
\]
Since

\[
\partial_iH_q=2\operatorname{sgn}(x_i)|x_i|^{q-1}
\quad\text{on }S_q,
\]
Euler's identity gives

\[
2U=x\cdot\nabla\phi
=2\sum_iw_i h_i,
\]
so

\[
\boxed{U=\sum_iw_i h_i.}
\tag{3.8}
\]

In particular `0<=U<=1` follows directly from the gradient shares.

**Outcome B13.** The degeneracy that previously looked like a liability is useful: on each coordinate face it pins the normal derivative of both complementary summands to zero, and convexity then traps every coordinate derivative share in `[0,1]`.

## 4. B9 — RANDOMIZE: the exact Hessian energy is a conditional variance

Let

\[
u_i=\operatorname{sgn}(x_i)|x_i|^{q-1},
\qquad
D=2(q-1)\operatorname{diag}(|x_i|^{q-2}).
\]
On `S_q`,

\[
A=D+2(2-q)uu^T.
\tag{4.1}
\]

The degree-zero extension `U=phi/H_q` satisfies `x dot grad U=0`. Moreover, from (3.6),

\[
\partial_iU
=\partial_i\phi-U\partial_iH_q
=2u_i(h_i-U).
\tag{4.2}
\]

Since

\[
D^{-1}u=\frac{x}{2(q-1)},
\]
the rank-one Sherman--Morrison correction in `(grad U)^T A^{-1}(grad U)` vanishes exactly because `x dot grad U=0`. Therefore the inverse-Hessian carré du champ is

\[
\boxed{
\Gamma_{H_q}(U)
=\frac{2}{q-1}\sum_iw_i(h_i-U)^2.
}
\tag{4.3}
\]

Now, conditional on `x`, introduce a random coordinate `I` with

\[
\mathbb P(I=i\mid x)=w_i.
\tag{4.4}
\]
Then (3.8) says

\[
\mathbb E[h_I\mid x]=U,
\]
and (4.3) becomes the exact probabilistic identity

\[
\boxed{
\Gamma_{H_q}(U)
=\frac{2}{q-1}\operatorname{Var}(h_I\mid x).
}
\tag{4.5}
\]

**Outcome B9.** The nonlinear inverse-Hessian energy is not merely bounded by a quadratic form; it is exactly the conditional variance of one bounded random gradient share.

## 5. B10 — DERANDOMIZE: Bernoulli endpoints give the sharp pointwise energy cap

Because `0<=h_I<=1` and its conditional mean is `U`,

\[
\mathbb E[h_I^2\mid x]\le\mathbb E[h_I\mid x]=U.
\]
Hence

\[
\operatorname{Var}(h_I\mid x)\le U(1-U),
\]
and (4.5) yields the strengthened pointwise inequality

\[
\boxed{
\Gamma_{H_q}(U)
\le\frac{2}{q-1}U(1-U).
}
\tag{5.1}
\]

The coefficient is the extremal bounded-variable variance coefficient; equality in this local step requires the gradient shares to be Bernoulli endpoints under the weights `w_i`.

This improves the generic run-14 estimate

\[
\Gamma_H(U)\le2U(1-U)
\]
by the factor `1/(q-1)`. It uses the special `l_q^2` face degeneracy but **does not assume `phi` or `psi` is coordinatewise unconditional**.

The remaining issue is that run 15 proved the spectral gap only in the sign-invariant quotient. The next subsection closes that gap as well.

## 6. Full globally-even Hessian spectral gap by sign characters

Cone measure on `S_q` decomposes into independent uniform signs and

\[
W=(w_1,\ldots,w_n)\sim\operatorname{Dirichlet}(\alpha,\ldots,\alpha),
\qquad\alpha=1/q.
\tag{6.1}
\]

Inside every open orthant, for a degree-zero function `f`, the same calculation as run 15 gives

\[
\Gamma_{H_q}(f)
=\frac{q^2}{2(q-1)}\Gamma_0(f),
\tag{6.2}
\]
where

\[
\Gamma_0(g)
=\sum_iw_i g_i^2-\left(\sum_iw_i g_i\right)^2
\tag{6.3}
\]
is the standard Wright--Fisher form.

Let

\[
L g
=\sum_{i,j}w_i(\delta_{ij}-w_j)\partial_{ij}g
+\sum_i(\alpha-n\alpha w_i)\partial_i g
\tag{6.4}
\]
be its symmetric generator under the Dirichlet law.

Decompose a globally even `f` into Fourier characters of the coordinate-sign cube:

\[
f(\varepsilon,w)=
\sum_{S\subseteq[n]}\chi_S(\varepsilon)g_S(w),
\qquad
\chi_S(\varepsilon)=\prod_{i\in S}\varepsilon_i.
\tag{6.5}
\]

Global evenness `f(-x)=f(x)` kills every odd-cardinality `S`. If `i in S`, continuity across the face `w_i=0` forces the trace of `g_S` on that face to vanish. Variance and the Dirichlet form split orthogonally over the sign characters.

For a nonempty sign sector `S`, write `s=|S|` and

\[
\beta=1-\alpha=\frac{q-1}{q},
\qquad
h_S(w)=\prod_{i\in S}w_i^\beta.
\tag{6.6}
\]

A direct substitution into (6.4) cancels every inverse-power term because

\[
\beta(\beta+\alpha-1)=0,
\]
and gives

\[
\boxed{
-Lh_S=\rho_s h_S,
\qquad
\rho_s=rac{s(q-1)}{q^2}
\big[n-1+(q-1)(s-1)\big].
}
\tag{6.7}
\]

The standard ground-state identity, valid first for smooth functions with the indicated zero traces and then by closure, is

\[
\mathcal E_0(g,g)-\rho_s\int g^2d\pi
=
\int h_S^2\Gamma_0(g/h_S)d\pi
\ge0.
\tag{6.8}
\]

Thus after multiplying by the metric factor in (6.2), the bottom of the `S` sector is at least (and the ground state realizes)

\[
\boxed{
\lambda_s
=\frac{s}{2}\big[n-1+(q-1)(s-1)\big].
}
\tag{6.9}
\]

For the sign-invariant sector `S=emptyset`, the standard sharp Dirichlet gap is `n/q`, hence the Hessian-metric gap is exactly the inherited

\[
\lambda_0=\frac{nq}{2(q-1)}.
\tag{6.10}
\]

For a globally even but sign-noninvariant sector one has `s>=2`. Formula (6.9) is increasing in `s`, so its minimum is

\[
\lambda_2=n+q-2.
\]
Moreover

\[
\lambda_2-\lambda_0
=
\frac{(q-2)(n+2q-2)}{2(q-1)}>0.
\tag{6.11}
\]

Therefore the previously computed sign-invariant gap is in fact the **full globally-even gap**:

\[
\boxed{
\lambda_{\rm even}(H_q)=\frac{nq}{2(q-1)}.
}
\tag{6.12}
\]

This sign-sector extension is a ground-state/Dirichlet-form calculation, not a novelty claim about Wright--Fisher spectral theory.

## 7. Main restricted theorem: arbitrary smooth convex complementary splits of `H_q`

Let

\[
V:=\operatorname{Var}_{\nu_q}(U),
\qquad M:=m(1-m).
\]

Poincare with (6.12) and the pointwise bound (5.1) give

\[
\frac{nq}{2(q-1)}V
\le
\mathbb E\Gamma_{H_q}(U)
\le
\frac{2}{q-1}\mathbb E[U(1-U)]
=\frac{2}{q-1}(M-V).
\]

Solving exactly,

\[
\boxed{
\frac{V}{M}\le\frac{4}{nq+4}.
}
\tag{7.1}
\]

But

\[
\frac{2}{n+2}-\frac{4}{nq+4}
=
\frac{2n(q-2)}{(n+2)(nq+4)}>0
\qquad(q>2),
\tag{7.2}
\]
so (2.2) follows strictly. Combining with the covariance identity (2.1),

\[
\boxed{
\operatorname{Cov}(\phi(X),\psi(X))
\ge
\frac{n^2(q-2)}{2(nq+4)}\,m(1-m)
\ge0.
}
\tag{7.3}
\]

### Theorem 7.1 — precise scope

For `n>=2,q>2`, let

\[
H_q(x)=\left(\sum_i|x_i|^q\right)^{2/q}.
\]
If `phi,psi` are `C^2` on `R^n\setminus{0}`, convex, positively `2`-homogeneous, globally even functions satisfying `phi+psi=H_q`, then the exact common-degree covariance in (2.1) is nonnegative, with the quantitative lower bound (7.3).

No coordinatewise unconditionality of `phi` or `psi` is assumed. I do **not** extend the statement here to nonsmooth summands: an approximation argument preserving the complementary split and the exact boundary structure would have to be written separately.

### First unresolved calibration `n=3,q=4`

Equation (7.1) gives

\[
\boxed{
\frac{\operatorname{Var}(U)}{m(1-m)}\le\frac14.
}
\tag{7.4}
\]

The source-slice target is `2/5`, so the new certified slack is

\[
\frac25-\frac14=\boxed{\frac3{20}}.
\tag{7.5}
\]

The previous sufficient projection target was `19/55`; now automatically

\[
\|\Pi_1(U-m)\|_2^2
\le V
\le\frac14M
<\frac{19}{55}M,
\]
with exact extra slack

\[
\frac{19}{55}-\frac14=\boxed{\frac{21}{220}}.
\tag{7.6}
\]

Thus the run-16 projection obstruction is gone on the whole smooth globally-even `q=4` complementary-split slice, not merely on its first eigenspace.

## 8. What this does and does not solve

This is a genuine strengthening of the repository's recovery theorem: run 16 controlled only source-realizable **pure first-eigenspace** splits; the present argument controls arbitrary smooth globally-even convex complementary splits summing to `H_q`, including sign-dependent and nonlinear angular modes.

It still does **not** move `D_B`. The full weak `(B)` conjecture permits arbitrary even log-concave potentials/bodies and is not reduced to a single fixed `l_q^2` total potential. In particular, under the functional/dilation interpolation the total potential generally leaves the exact `H_q` family away from the calibration point. I therefore label this result **PARTIAL**, not PROVED or REFUTED.

The coordinatewise unconditional `(B)` subclass itself is old (Cordero-Erausquin--Fradelizi--Maurey; see also Marsiglietti). The new repository statement above deliberately avoids claiming that old subclass as a discovery: its point is the non-coordinatewise-unconditional complementary-split local theorem and the mechanism that makes the deficient spectral sector harmless. A dedicated prior-art search for this exact local formulation would still be required before any novelty claim or paper use.

The nearest next mathematical target is now broader and cleaner: replace the exact `l_q^2` face degeneracy by a quantitative condition on a general 2-homogeneous even `H` that guarantees bounded gradient shares and a matching full-even Hessian-metric gap. If such a condition can be deformed from `H_q` to a large class without losing the inequality, it would move beyond this calibration family.

## 9. Exact self-check and idea-before-code compliance

Before writing checker code, I archived the route itself at

`artifacts/hard7_2026-09-18/HARD7-01/2026-09-19T13-01-43Z__gradient_share_full_even_idea.md`

creation commit

`a25f139fde81e9bb13c396b4c5037f386d2fd532`.

That idea file was read back at its creation commit before any checker was added.

The exact symbolic checker is

`artifacts/hard7_2026-09-18/HARD7-01/2026-09-19T13-01-43Z__gradient_share_full_even_check.py`

creation commit

`d7e3faa0db4950cce86cf49e62b83e853f97122f`.

Its executed stdout is archived at

`artifacts/hard7_2026-09-18/HARD7-01/2026-09-19T13-01-43Z__gradient_share_full_even_check.out`

creation commit

`9b93ec2b1ac2fd245d55e0f08d64d7b440440ca3`.

The output ends

`ALL_EXACT_CHECKS_PASS = True`.

It checks the sign-sector ground-state cancellation, `rho_s`, the metric-scaled sector eigenvalue, the exact sign-invariant gap, the strict separation of the first allowed even sign sector, the gradient-share/Poincare variance ratio `4/(nq+4)`, its exact slack from the required `2/(n+2)`, the covariance margin, and all `n=3,q=4` rational calibrations. This is a **self-check**, not an independent audit; the theorem-sized justification is the on-page proof above.

Both checker and output were read back successfully at their returned creation commits before this report was written.

## 10. Method outcomes and lifecycle

- **B13 / FIND WHAT ONLY INCREASES:** the zero normal-curvature faces of `H_q`, combined with complementary convexity, force both summands' normal derivatives to start at zero; each coordinate gradient share therefore stays in `[0,1]`.
- **B9 / RANDOMIZE:** choosing a coordinate with probability `w_i` converts the exact Hessian energy to `2/(q-1)` times a conditional variance.
- **B10 / DERANDOMIZE:** the worst `[0,1]` conditional law is Bernoulli; the remaining sign dependence is dispatched exactly by the sign-character ground states.

These methods were unused on the current weak-`(B)` target and differ from the preceding run's B12/B16/B25.

The frozen source metric again has no movement, but the **remaining obligation moved materially**: the previous `n=3,q=4` arbitrary-split first-projection question is now settled inside the entire smooth `H_q` complementary-split family. The next obstruction is deformation away from the exact `l_q^2` total potential, rather than control of the deficient first Dirichlet mode. I therefore do not escalate to a new Section-I stuck report in this invocation.

## 11. Scheduler/model capability truth

The currently exposed automation interface still offers task prompt/title, schedule/timing and enabled-state controls, but no binding model-family selector, no reasoning-effort selector and no guaranteed execution duration. `GPT-6 / maximum` therefore remains prompt-requested only. The runtime actually identifying this run is **GPT-5.6 Sol**; reasoning level is **UNVERIFIED**.

The repository's current `RESULTS.md` records that one earlier context returned `You cannot modify this task` for P26, while a later authorized context successfully updated P26. The non-bypass remedy for any such refusal is to use the owning/authorized account or workspace, obtain a legitimate ownership/permission transfer, or use platform support. Creating a duplicate schedule or editing repository text does not change native task authorization. HARD7-01 attempted no scheduler mutation in this run.

No Gmail, Drive, public posting, other-track edit, shared-root rewrite, force-push or schedule creation/modification was performed.

## 12. Status and next checkpoint

**Status: PARTIAL. Full weak `(B)` remains OPEN in the checked literature.**

Durable quantitative theorem in the recovery slice:

\[
\boxed{
\frac{\operatorname{Var}_{\nu_q}(\phi/H_q)}{m(1-m)}
\le\frac{4}{nq+4}
<\frac{2}{n+2}
\quad(n\ge2,q>2)
}
\]

for smooth globally-even convex complementary `2`-homogeneous splits `H_q=phi+psi`, with no coordinatewise-unconditional assumption on the summands.

For `n=3,q=4`, the bound is `1/4`, versus required `2/5`, and the covariance lower-bound coefficient is `9/16`.

Next checkpoint: identify a deformation-stable replacement for the two special ingredients used here — zero coordinate-face curvature that yields bounded gradient shares, and a full-even Hessian-metric gap whose worst sector is the quotient mode — and test whether it persists for a non-`l_q` 2-homogeneous total potential. Do not return to the now-settled first-projection subproblem.

No source closure, source refutation, paper, independent audit, or novelty certificate is claimed.

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
  methods: [B13, B9, B10]
  idea_commit: a25f139fde81e9bb13c396b4c5037f386d2fd532
  exact_checker_commit: d7e3faa0db4950cce86cf49e62b83e853f97122f
  exact_output_commit: 9b93ec2b1ac2fd245d55e0f08d64d7b440440ca3
  new_checkpoint:
    full_even_hessian_gap_lq: "n*q/(2*(q-1))"
    gradient_share_energy_cap: "Gamma <= 2/(q-1) U(1-U)"
    arbitrary_smooth_split_variance_ratio: "Var(U)/(m(1-m)) <= 4/(n*q+4)"
    n3_q4_ratio: "1/4"
    n3_q4_target_slack: "3/20"
    n3_q4_covariance_margin_coefficient: "9/16"
  remaining_obligation: "deform the gradient-share plus full-even-gap mechanism beyond the exact l_q^2 total potential, or find a source-valid obstruction"
  shared_RESULTS_edit: false
```
