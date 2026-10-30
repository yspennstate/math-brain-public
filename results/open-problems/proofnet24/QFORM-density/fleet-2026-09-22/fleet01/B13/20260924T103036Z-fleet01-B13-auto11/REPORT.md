SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B13, 2026-09-24T10:30:36Z.
attacking: exact product-set shell geometry, selective sign pruning, and an original-coordinate difference-gradient receiver; applying fleet02/B13 r12's affine-defect theorem to an actual slab inequality.

# fleet01/B13 — shell-sign pruning and difference-gradient geometry

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T103036Z-fleet01-B13-auto11`  
Role: extremal product laws  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW SUPPORTING LEMMAS / ESSENTIAL STEP APPLIED / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**.

Fresh control was read on `math-research-brain/main`; the current owner control revision is `2026-09-22.15`, superseding the historical `.5` while retaining the same QFORM-only target. The live correction inbox was consumed: no post-rotation independence, no uniform pointwise one-dimensional quadratic oscillatory decay, no arbitrary-joint coarea shortcut, no projection-density-only closure, no bounded-diameter or fixed-fragment-count extremality.

The exact cap-one-to-product-indicator purification from the immediately preceding fleet01/B13 run is retained: every individual slab witness transfers with zero loss to measurable unit product sets, for the same matrix and the same interval. No interval or centered-uniform extremality is assumed below.

## 1. Partner result used at its exact proved scope

The newest completed designated partner is fleet02/B13 r12, source-pinned as

`yspennstate/math-open-problems@89c5263400fd23e149295699eaff0811d6219828`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B13/20260924T100717Z-fleet02-B13-QFORM-r12/REPORT.md`.

Its theorem `QFORM-SLAB-MASS-TRIMMED-AFFINE-DEFECT-v1` says the following. Write

\[
A=M+F,
\]

assume every affine `M`-form has density at most `C_M`, let `J` have length `ell`, and let

\[
p=\Pr\{X^TAX\in J\}=\rho\ell.
\]

For arbitrary physical coordinate sets `G_i` with

\[
\eta:=\sum_i\Pr\{X_i\notin G_i\}\le p/2,
\]

define

\[
\Delta_{\rm aff}(F;G)
=
\inf_{a,c}\operatorname*{ess\,sup}_{x\in\prod_iG_i}
|x^TFx-a^Tx-c|.
\]

Then

\[
p-\eta\le C_M(\ell+2\Delta_{\rm aff}(F;G)),
\]

and, for `rho>=4 C_M`,

\[
\boxed{\Delta_{\rm aff}(F;G)\ge {p\over8C_M}.}
\tag{1.1}
\]

In the current exact-rank-two rough endpoint,

\[
A=D_C+\lambda_1vv^T+E_{\rm sep}+\lambda_2ww^T,
\qquad |C|\le4,
\tag{1.2}
\]

where

\[
M=D_C+\lambda_1vv^T,
\qquad
F=E_{\rm sep}+\lambda_2ww^T,
\]

\[
\|E_{\rm sep}\|_{op}\le {C_D\over\rho},
\qquad C_D=2\sqrt{30\pi}=19.41625912555699\ldots,
\tag{1.3}
\]

\[
\rho|\lambda_2|\le\sqrt H,
\qquad H=\sqrt{1536e^2},
\qquad \sqrt H=10.321552950446426\ldots,
\tag{1.4}
\]

and

\[
C_M=500e\cdot5(8+\log5)
=65302.90114768759\ldots.
\tag{1.5}
\]

The partner consequence, for every retained product family with deletion budget at most `p/2`, is

\[
\boxed{
C_D\sum_{i\notin C}\kappa(G_i)
+\rho|\lambda_2|\,\kappa_w(G)
\ge {\rho p\over8C_M},
}
\tag{1.6}
\]

where

\[
\kappa(S)=\inf_{\alpha,\beta}\operatorname*{ess\,sup}_{x\in S}|x^2-\alpha x-\beta|
\tag{1.7}
\]

and `kappa_w` is the analogous Chebyshev defect of `(w^Tx)^2` on the retained product set.

Everything below applies this theorem to explicit retained sets; it does not replace the rough tail by a small random perturbation.

## 2. Exact quadratic-shell identity

### Theorem 2.1 — `QFORM-QUADRATIC-SHELL-IDENTITY-v1`

For every measurable finite-measure `S subset R`, allowing the value `+infinity`,

\[
\boxed{
\kappa(S)
=
{1\over2}\inf_{m\in\mathbb R}
\left[
\operatorname*{ess\,sup}_{x\in S}(x-m)^2
-
\operatorname*{ess\,inf}_{x\in S}(x-m)^2
\right].
}
\tag{2.1}
\]

**Proof.** Write `m=alpha/2`. Then

\[
x^2-\alpha x-\beta=(x-m)^2-c
\]

for a freely chosen constant `c`. For fixed `m`, the best uniform constant approximation to the scalar function `(x-m)^2` is the midpoint of its essential range, and its error is exactly half the range. Taking the infimum over `m` gives (2.1). QED.

Thus `kappa` is exactly the thickness of the thinnest quadratic shell around some physical center; it is not a convex-hull diameter.

For

\[
H(m,r,\delta)=\{x: |(x-m)^2-r^2|\le\delta\},
\tag{2.2}
\]

one has the sharp one-dimensional volume estimate

\[
\boxed{|H(m,r,\delta)|\le2\sqrt{2\delta}.}
\tag{2.3}
\]

Indeed, if `r^2>=delta`, its length is

\[
2\bigl(\sqrt{r^2+\delta}-\sqrt{r^2-\delta}\bigr)
\le2\sqrt{2\delta},
\]

with maximum at `r^2=delta`; if `r^2<delta`, the shell is one interval of length `2sqrt(r^2+delta)<=2sqrt(2delta)`.

Consequently every measurable `S` of measure `s` satisfies the universal sharp lower bound

\[
\boxed{\kappa(S)\ge{s^2\over8}.}
\tag{2.4}
\]

For an interval of length `s`, equality holds. This is a theorem about the defect functional only; it does **not** assert that intervals are extremal for QFORM.

If `E` is a unit-measure set and

\[
\kappa_E^{\rm tr}(\eta)
:=
\inf_{G\subset E:\ |E\setminus G|\le\eta}\kappa(G),
\tag{2.5}
\]

then (2.1) is equivalent, at the level of the infimum, to

\[
\kappa_E^{\rm tr}(\eta)
=
\inf\{\delta:\exists m,r,\ |E\cap H(m,r,\delta)|\ge1-\eta\},
\tag{2.6}
\]

and (2.4) gives

\[
\boxed{\kappa_E^{\rm tr}(\eta)\ge{(1-\eta)^2\over8}.}
\tag{2.7}
\]

## 3. Selective shell-sign pruning

The defect lower bound (1.6) still allows remote two-sided shells. The next theorem separates genuine local width from the binary sign ambiguity of such shells.

For each original-coordinate unit set `E_i`, choose arbitrary parameters `m_i,r_i,delta_i` and retain

\[
S_i
=E_i\cap\{|(x-m_i)^2-r_i^2|\le\delta_i\}.
\tag{3.1}
\]

Let

\[
\varepsilon_i=1-|S_i|.
\tag{3.2}
\]

Split the shell into the two physical branches

\[
S_i^\pm=S_i\cap\{\pm(x-m_i)\ge0\},
\qquad
b_i=\min(|S_i^+|,|S_i^-|),
\tag{3.3}
\]

and let `sigma_i` denote a dominant sign. Put

\[
a_i=\sqrt{(r_i^2-\delta_i)_+},
\qquad
B_i=\sqrt{r_i^2+\delta_i},
\qquad
h_i={B_i-a_i\over2}.
\tag{3.4}
\]

A dominant branch lies in an ordinary interval of half-width `h_i`; therefore

\[
\kappa(S_i^{\sigma_i})\le{h_i^2\over2},
\qquad
\kappa(S_i)\le\delta_i.
\tag{3.5}
\]

### Theorem 3.1 — `QFORM-SELECTIVE-SHELL-SIGN-PRUNING-v1`

Let `I` be any subset of physical coordinates. Retain the dominant shell branch on `I`, and retain both branches off `I`:

\[
G_i=S_i^{\sigma_i}\quad(i\in I),
\qquad
G_i=S_i\quad(i\notin I).
\tag{3.6}
\]

If

\[
\boxed{
\sum_i\varepsilon_i+\sum_{i\in I}b_i\le{p\over2},
}
\tag{3.7}
\]

then, in the partner's rough normal form and for `rho>=4C_M`, define

\[
R_I
=
\sum_{i\in I}|w_i|h_i
+
\sum_{i\notin I}|w_i|B_i.
\tag{3.8}
\]

One has

\[
\boxed{
C_D\!\left[
\sum_{\substack{i\notin C\\ i\notin I}}\delta_i
+{1\over2}\sum_{\substack{i\notin C\\ i\in I}}h_i^2
\right]
+{\rho|\lambda_2|\over2}R_I^2
\ge {\rho p\over8C_M}.
}
\tag{3.9}
\]

**Proof.** Equation (3.7) is exactly the deletion-budget hypothesis needed for the partner theorem. The coordinatewise diagonal defects obey (3.5). For the rank-one carrier, choose as center for a pruned coordinate the midpoint of its dominant shell interval and as center for an unpruned coordinate `m_i`. Then every `x in prod_i G_i` satisfies

\[
|w^Tx-y_0|\le R_I
\]

for a deterministic `y_0`. The function `y^2` on an interval of half-width `R_I` has affine Chebyshev error at most `R_I^2/2`, so

\[
\kappa_w(G)\le{R_I^2\over2}.
\]

Insert these upper bounds into the partner's lower bound (1.6). QED.

Using (1.4), (3.9) also yields the source-explicit inequality

\[
C_D\!\left[
\sum_{\substack{i\notin C\\ i\notin I}}\delta_i
+{1\over2}\sum_{\substack{i\notin C\\ i\in I}}h_i^2
\right]
+{\sqrt H\over2}R_I^2
\ge {\rho p\over8C_M}.
\tag{3.10}
\]

This is the actual partner application required by the assignment.

## 4. The two-sided sign-bank dichotomy

Take `I` to be all coordinates. If

\[
\sum_i\varepsilon_i+\sum_i b_i\le{p\over2},
\tag{4.1}
\]

then (3.9), after multiplying by two, gives

\[
\boxed{
C_D\sum_{i\notin C}h_i^2
+ho|\lambda_2|\left(\sum_i|w_i|h_i\right)^2
\ge {\rho p\over4C_M}.
}
\tag{4.2}
\]

Using `rho|lambda_2|<=sqrt H`,

\[
\boxed{
C_D\sum_{i\notin C}h_i^2
+\sqrt H\left(\sum_i|w_i|h_i\right)^2
\ge {\rho p\over4C_M}.
}
\tag{4.3}
\]

Numerically,

\[
8C_MC_D=10143504.402673082\ldots,
\qquad
8C_M\sqrt H=5392218.816109009\ldots .
\tag{4.4}
\]

Therefore at least one of

\[
\boxed{
\sum_{i\notin C}h_i^2
\ge {\rho p\over10143504.402673082\ldots}
}
\tag{4.5}
\]

or

\[
\boxed{
\left(\sum_i|w_i|h_i\right)^2
\ge {\rho p\over5392218.816109009\ldots}
}
\tag{4.6}
\]

must hold.

Equivalently, if the shell miss satisfies

\[
\sum_i\varepsilon_i\le{p\over4}
\tag{4.7}
\]

and both tangent-width payments (4.5)--(4.6) fail, then necessarily

\[
\boxed{\sum_i b_i>{p\over4}.}
\tag{4.8}
\]

This is `QFORM-TWOSIDED-SIGN-BANK-v1`: thin remote shells can evade the ordinary tangent-width receiver only by retaining a fixed amount of genuinely two-sided marginal branch mass.

When `delta_i<=r_i^2`,

\[
h_i
=
{\delta_i\over
\sqrt{r_i^2+\delta_i}+\sqrt{r_i^2-\delta_i}},
\tag{4.9}
\]

so for a very remote thin shell `r_i>>sqrt(delta_i)`, one has

\[
h_i\sim{\delta_i\over2r_i}.
\tag{4.10}
\]

Thus empty distance from the origin is not being charged: after a sign branch is selected, remoteness makes the true tangent width **smaller**. The only remaining currency is actual two-sided sign mass. This is precisely compatible with the live correction forbidding bounded-diameter or fixed-fragment-count reductions.

## 5. Direct geometric sublevel-set inequality from differences

The next theorem is independent of the rough normal form and applies to every product-indicator witness.

Let

\[
E=\prod_{i=1}^nE_i,
\qquad |E_i|=1,
\qquad q(x)=x^TAx,
\]

and

\[
S=\{x\in E:q(x)\in J\},
\qquad p=|S|,
\qquad \ell=|J|.
\tag{5.1}
\]

Define the one-dimensional autocorrelations

\[
m_i(t)=|E_i\cap(E_i+t)|,
\tag{5.2}
\]

and

\[
M(u)=\prod_i m_i(u_i).
\tag{5.3}
\]

Each `m_i` is bounded by one and integrates to one, so `M` is the probability density of the independent difference vector `U=X-X'` for independent uniform points `X,X'` in `E`.

For `u in R^n`, put

\[
\Gamma_A(u)
=
\max_i |(Au)_i|\,m_i(u_i).
\tag{5.4}
\]

### Theorem 5.1 — `QFORM-PRODUCTSET-DIFFERENCE-GRADIENT-v1`

With the convention that `ell/0=+infinity`, one has

\[
\boxed{
p^2
\le
\int_{\mathbb R^n}
M(u)\min\left\{1,{\ell\over\Gamma_A(u)}\right\}\,du.
}
\tag{5.5}
\]

**Proof.** Let

\[
h(u)=|S\cap(S+u)|.
\]

Fubini gives

\[
\int h(u)\,du=|S|^2=p^2.
\tag{5.6}
\]

Fix `u`. If `x` belongs to `S cap (S+u)`, then both `x` and `x-u` are in the slab, and the exact polarization identity gives

\[
|q(x)-q(x-u)|
=
|2(Au)^Tx-u^TAu|
\le\ell.
\tag{5.7}
\]

Hence `(Au)^Tx` is restricted to an interval of length `ell/2`; for a deliberately looser constant we may use length `ell`. Also

\[
x_i\in E_i\cap(E_i+u_i),
\]

whose measure is `m_i(u_i)`. Fiber in coordinate `i`. If `(Au)_i\ne0`, the allowed `x_i` interval has length at most `ell/|(Au)_i|`, so

\[
h(u)
\le
M(u)\min\left\{1,{\ell\over |(Au)_i|m_i(u_i)}\right\}.
\tag{5.8}
\]

Taking the best coordinate gives (5.5), and integrating uses (5.6). No random-coordinate rotation or conditional-independence assertion occurs. QED.

As a quantitative corollary, for every `T>0`,

\[
p^2
\le
\Pr_M\{\Gamma_A(U)\le T\}+{\ell\over T}.
\tag{5.9}
\]

Choosing

\[
T={2\ell\over p^2}={2\over\rho p}
\tag{5.10}
\]

gives

\[
\boxed{
\Pr_M\left\{\Gamma_A(U)\le{2\over\rho p}\right\}
\ge {p^2\over2}.
}
\tag{5.11}
\]

Thus a high-ratio product-set slab forces a positive amount of the **ambient independent difference law** onto vectors for which every original-coordinate gradient component is small after weighting by the corresponding self-overlap `m_i(U_i)`. This is a genuine product-geometric restriction, not a support-radius statement.

## 6. What the new pair of results says

The partner affine-defect theorem plus selective sign pruning gives a clean endpoint dichotomy:

* either the retained shells have enough one-sided tangent width to pay (4.5) or (4.6), or
* the product geometry contains aggregate two-sided sign mass exceeding `p/4`.

Independently, every product-set slab obeys the difference-gradient inequality (5.5)--(5.11). The latter keeps the original coordinate product provenance: before any slab conditioning, the difference coordinates are independent and have densities `m_i<=1`.

The exact two-sided-shell limit makes the remaining mechanism transparent. If a coordinate is concentrated near `m_i plus/minus r_i`, subtracting physical affine terms turns a rank-one square into a Rademacher-type cross interaction among the independent branch signs. The present run proves the branch-mass alternative rigorously but does **not** yet prove the dimension-free smoothing estimate for that sign chaos.

## 7. First unpaid implication

The first unpaid implication is now

`QFORM-SHELL-SIGN-BANK-TO-DIFFERENCE-GRADIENT-RECEIVER-v1`:

> In the current rough normal form, convert the forced aggregate two-sided branch mass in (4.8), together with the original-coordinate independent-difference constraint (5.5), into a universal slab payment while retaining the complete `E_sep` phase and the secondary rank-one carrier. Equivalently, prove a dimension-free small-ball/oscillatory bound for the resulting physical sign bank, or construct a genuine source-valid cap-one counterexample satisfying both the affine-defect lower bound and the difference-gradient restriction.

No such closure is claimed here. Full unrestricted QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. Continuity remains a separate stronger goal.

## 8. Numerical constants and scope audit

`4 C_M = 261211.60459075036...`.

`8 C_M C_D = 10143504.402673082...`.

`8 C_M sqrt(H) = 5392218.816109009...`.

All identities and inequalities above are original-coordinate statements. No input moment assumption, compact support, log-concavity, connected support, bounded diameter, fixed fragment count, centered law, identical law, or interval extremality is imposed. The only branch-specific assumptions are exactly those of the source-pinned fleet02/B13 r12 theorem in Sections 1, 3, and 4. Section 5 is unconditional for arbitrary unit product sets and arbitrary symmetric `A`.

Model self-report: `GPT-5.6 Sol`. Configured thinking level: `UNKNOWN_NOT_EXPOSED`. Provider reasoning-token and provider thinking-time counters: `null / not exposed`.
