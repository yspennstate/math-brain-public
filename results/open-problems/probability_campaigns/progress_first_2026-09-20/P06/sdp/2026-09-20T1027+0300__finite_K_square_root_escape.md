Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but authenticated completed-run model/reasoning telemetry is unavailable, so I do not claim otherwise.**

# P06 complementary P07 iteration — deterministic square-root escape and arbitrary fixed-length finite-model iteration

Status: **P06 SOURCE KNOWN / no novelty claim for Conjecture 17. P07 OPEN / PROVED PARTIAL new mathematics; publication novelty UNVERIFIED.**

Native role preserved: `6aa7b53b0858819196d923203522c996`.  
Captured pre-write `master`: `17b3ce1e7ae4774b1eb65788bce1c511d96ffbb0`.  
Previous substantive checkpoint: `probability_campaigns/progress_first_2026-09-20/P06/sdp/2026-09-20T0930+0300__fixed_projector_second_finite_step.md`, creation commit `04add55e2718c83206ae6803afec365c84af3dae`, readback blob `2514ed33faa79181a9bacb92505700360130d27c`, with notation-only correction commit `26364c40b9ecef0c84cd9eebd32983845ef51ac2` / blob `a4177b3543983a4a099c11effd279521998f309e`.

The outside P07 source remains Bandeira--Blasiok--Dmitriev--Faure--Kireeva--Kunisky, arXiv:2502.16227, and the full-source bound remains

\[
\sqrt n\le \mathbf E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]

No full-source improvement is claimed.

The previous report proved two actual fixed-projector positive square-Newton contractions for sufficiently sharp fixed slack. This report extracts the mechanism behind that calculation and proves a stronger finite-length statement:

> **For every fixed integer `K`, there is an `epsilon_K>0` such that every fixed `0<epsilon<epsilon_K` admits `K` consecutive covariance-regularized positive square-Newton contraction steps in the actual odd-order random-circulant model, outside source-sufficient failure `o(1/sqrt(log n))`.**

The constants are allowed to depend on `K`; therefore this is not yet an infinite-iteration or exact-feasibility theorem. The new ingredient is a deterministic square-root escape lemma plus an arbitrary-fixed-degree Walsh/convolution envelope. It removes the artificial `p<20` ceiling of the previous seed and proves that no obstruction occurs at any prescribed finite iteration depth.

---

# 1. Abstract one-step normalization

Work at an arbitrary current state and whiten its covariance. Thus `X` is centered and

\[
\mathbf E X=0,\qquad \mathbf E XX^T=I.
\tag{1.1}
\]

Write the whitened target residual as

\[
r=-\nu e,\qquad \|e\|_2=1,\qquad 0<\nu<1,
\tag{1.2}
\]

so that the exact Newton score is

\[
g=\nu Z,\qquad Z=e^TX,\qquad \mathbf EZ^2=1.
\tag{1.3}
\]

Put

\[
\rho:=1-\nu^2,\qquad s:=\sqrt\rho,
\tag{1.4}
\]

and define the normalized second-score vector and longitudinal skew

\[
m_2:=\mathbf E[XZ^2],\qquad
\Gamma:=\|m_2\|_2,
\qquad
\kappa:=\mathbf EZ^3=e^Tm_2.
\tag{1.5}
\]

These agree with the invariant quantities used in the earlier reports because

\[
\tau=\mathbf E[Xg^2]=\nu^2m_2,
\qquad
{\|\tau\|_2^2\over\nu^4}=\Gamma^2.
\]

The square-canceling parameter is

\[
\alpha={1\over1+s},
\qquad
\beta=\alpha\nu={\nu\over1+s}
=\sqrt{{1-s\over1+s}}.
\tag{1.6}
\]

The pure positive square law has density

\[
q={p(1+\beta Z)^2\over1+\beta^2}
\tag{1.7}
\]

relative to the current law `p`, and its residual in the old whitened coordinates is exactly

\[
r_q={\beta\nu\over2}m_2.
\tag{1.8}
\]

Define

\[
A={\Gamma\beta\over2}.
\tag{1.9}
\]

Whenever `A<1/2`, use the same covariance-regularizing mixture as before,

\[
\eta={A\over1-A},
\qquad
\lambda=1-\eta,
\qquad
p_+=\eta p+\lambda q.
\tag{1.10}
\]

Its covariance `C_+`, still in the old whitened coordinates, obeys the exact floor

\[
C_+\succeq\eta I.
\tag{1.11}
\]

The new residual is

\[
r_+=-\eta\nu e+\lambda{\beta\nu\over2}m_2.
\tag{1.12}
\]

---

# 2. Deterministic square-root escape lemma

The crucial point is that the old residual and the square residual are asymptotically transverse. The relevant condition is not a pointwise bound on the score; it is the small longitudinal third moment `kappa`.

## Lemma 2.1 — square-root escape

Fix `C<infty`. There are constants `rho_0(C)>0` and `c(C),C'(C)>0` with the following property.

Assume

\[
0<\rho<\rho_0(C),
\qquad
\Gamma^2\le1+C\rho,
\qquad
|\kappa|\le C\rho.
\tag{2.1}
\]

Then `A<1/2`, the update (1.10) is well defined, and its new Newton decrement satisfies

\[
\boxed{
1-C'\sqrt\rho
\le \nu_+^2
\le 1-c\sqrt\rho.
}
\tag{2.2}
\]

Equivalently, with `rho_+=1-nu_+^2`,

\[
\boxed{
c\sqrt\rho\le\rho_+\le C'\sqrt\rho.}
\tag{2.3}
\]

The lower bound on `nu_+^2` in (2.2) only requires, in addition, a fixed bound `E Z^4<=M`; then `C'` may depend on `M`.

### Proof: upper decrement / lower new gap

Let

\[
t:=1-2A.
\tag{2.4}
\]

From

\[
\beta=1-s+O(s^2),\qquad
\Gamma=1+O_C(s^2),
\]

we get

\[
\boxed{t=s+O_C(s^2).}
\tag{2.5}
\]

Hence `t>0` for small enough `s`, so `A<1/2`, and

\[
\eta={1-t\over1+t}=1-2s+O_C(s^2),
\qquad
\lambda={2t\over1+t}=2s+O_C(s^2).
\tag{2.6}
\]

From (1.12), using `e^Tm_2=kappa`,

\[
{\|r_+\|_2^2\over\nu^2}
=
\eta^2+\lambda^2A^2-\eta\lambda\beta\kappa.
\tag{2.7}
\]

The covariance floor (1.11) therefore gives

\[
\nu_+^2
=r_+^TC_+^{-1}r_+
\le
\nu^2\left(
\eta+{\lambda^2A^2\over\eta}-\lambda\beta\kappa
\right).
\tag{2.8}
\]

The first two terms simplify exactly in `t`:

\[
\eta+{\lambda^2A^2\over\eta}
=
{(1-t)(1+t^2)\over1+t}
=1-2t+3t^2+O(t^3).
\tag{2.9}
\]

Since `lambda |kappa|=O_C(s^3)`, (2.5)--(2.9) yield

\[
\nu_+^2
\le
(1-s^2)(1-2s+O_C(s^2))
=
1-2s+O_C(s^2).
\tag{2.10}
\]

Thus, after shrinking `rho_0(C)` if necessary,

\[
\rho_+\ge c(C)s=c(C)\sqrt\rho.
\tag{2.11}
\]

This is the desired **square-root escape**. It is exactly the mechanism that was hidden inside the explicit `B(beta)` estimate of the preceding report.

### Proof: lower decrement / upper new gap

Assume `E Z^4<=M`. By (1.7),

\[
\mathbf E_q Z^2
={1+2\beta\kappa+\beta^2\mathbf EZ^4\over1+\beta^2}
\le C_M.
\tag{2.12}
\]

Hence the variance of `Z` under the mixture is at most

\[
e^TC_+e\le1+C_M\lambda\le1+C_M's.
\tag{2.13}
\]

Also, from (1.12),

\[
{e^Tr_+\over\nu}
=-\eta+{\lambda\beta\kappa\over2}
=-1+2s+O_{C}(s^2).
\tag{2.14}
\]

The one-dimensional variational inequality gives

\[
\nu_+^2
\ge{(e^Tr_+)^2\over e^TC_+e}
\ge1-C'_{C,M}s.
\tag{2.15}
\]

This proves (2.2)--(2.3). ∎

---

# 3. The update itself is only an `O(sqrt(rho))` polynomial perturbation

The mixed density relative to the current law is exactly

\[
{dp_+\over dp}
=1+uZ+v(Z^2-1),
\tag{3.1}
\]

where

\[
u={2\lambda\beta\over1+\beta^2},
\qquad
v={\lambda\beta^2\over1+\beta^2}.
\tag{3.2}
\]

To avoid the notation ambiguity corrected in the preceding report, (3.2)'s first coefficient is **Latin `u`**, not the decrement `nu`.

By (2.6),

\[
\boxed{u=O_C(s),\qquad v=O_C(s).}
\tag{3.3}
\]

Thus one near-boundary escape step changes the density only by order `sqrt(rho)` even though it opens a decrement gap of the same order.

Let

\[
f={m_2-\kappa e\over\|m_2-\kappa e\|},
\qquad
\mathcal S=\operatorname{span}\{e,f\}.
\tag{3.4}
\]

The new mean belongs to `S` exactly:

\[
\mathbf E_{p_+}X=ue+vm_2\in\mathcal S.
\tag{3.5}
\]

Exactly as in the previous finite second-step calculation,

\[
P_{\mathcal S^\perp}C_+e
=vP_{\mathcal S^\perp}\mathbf E[X(Z^3-Z)],
\tag{3.6}
\]

and, with `U=f^TX`,

\[
P_{\mathcal S^\perp}C_+f
=uP_{\mathcal S^\perp}\mathbf E[XUZ]
+vP_{\mathcal S^\perp}\mathbf E[XU(Z^2-1)].
\tag{3.7}
\]

Therefore any fixed bound on the three vector words in (3.6)--(3.7) gives

\[
\boxed{
\|P_{\mathcal S^\perp}C_+P_{\mathcal S}\|_{op}=O(s).
}
\tag{3.8}
\]

Because the residual (1.12) lies in `S` exactly and `C_+\succeq(1-O(s))I`, the new exact Newton vector has only `O(s)` off-plane mass. With fixed bounds on the corresponding cubic/quartic words, the same Taylor expansion used in Sections 6--7 of the preceding report yields

\[
\Gamma_+^2\le1+O(s),
\qquad
|\kappa_+|=O(s).
\tag{3.9}
\]

Together with (2.3), this has the invariant form

\[
\boxed{
\Gamma_+^2\le1+C_+\rho_+,
\qquad
|\kappa_+|\le C_+\rho_+,
}
\tag{3.10}
\]

because `rho_+` is bounded below by a constant multiple of `s`.

The important point is that (3.10) requires only a **finite list of coefficient-space moment bounds generated by the current step**. It does not require uniform hypercontractivity over the whole selected Fourier subspace.

---

# 4. Arbitrary fixed-degree collision envelope

The preceding report used a degree-limited list and therefore selected `c_n=n^{-9/20}`, which only guaranteed the convenient interpolation through fixed `p<20`. For finite but arbitrarily long iteration, that exponent should not be frozen.

## Lemma 4.1 — fixed finite word lists at arbitrary degree

Fix an integer `R` and any finite list `W_R` of normalized scalar/vector Fourier words built from:

* the symmetric mask `e_x=e_{-x}` on odd `Z_n`,
* cyclic convolutions of total Walsh degree at most `R`,
* restriction to the selected mask `D`,
* selected centering, and
* finitely many scalar contractions of such coefficient arrays.

Then there is `K(R,W_R)<infty` such that all normalized squared coefficient energies and scalar moments in `W_R` are at most `K(R,W_R)` outside probability `O_{R,W_R}(n^{-1})`.

### Proof

Every coefficient is a finite sum of Walsh characters subject to finitely many cyclic additive constraints. In a second moment, mask expectation vanishes unless each quotient class `[x]={x,-x}` occurs with even parity. Generic surviving diagrams pair the two copies up to one of finitely many sign/permutation patterns. Any non-generic identification imposes at least one additional signed affine relation and therefore removes at least one free cyclic parameter.

The degree is fixed. Hence every nonzero minor of every integer constraint matrix that can arise has absolute determinant bounded by a constant depending only on `R`. For odd composite `n`, the number of solutions contributed by a nontrivial kernel is bounded by the corresponding determinant gcd and therefore still by that same `R`-dependent constant. Thus the normalized expectations are `O_{R,W_R}(1)`.

For variances, disconnected diagrams cancel after subtracting the product of expectations. Every surviving connected diagram has at least one additional independent relation, so the normalized variance is `O_{R,W_R}(n^{-1})`. Chebyshev, followed by a union bound over the fixed finite list, proves the claim. ∎

This is the same parity/additive-collision proof architecture as the already established quadratic `Q=e*e` and cubic `e*e*e` estimates; the new point is that **nothing in that counting argument is special to degree four or eight when the requested degree is fixed before `n->infinity`.**

---

# 5. Adaptive vanishing tilt removes the old `p<20` ceiling

Fix a desired number `K` of near-boundary steps. A conservative moment budget is

\[
P_K:=8K+16.
\tag{5.1}
\]

No optimality is claimed for this value; it merely dominates every scalar moment needed after `K` quadratic reweightings and the associated squared coefficient-energy calculations.

Choose

\[
\gamma_K={1\over2P_K},
\qquad
\boxed{c_{n,K}=n^{-1/2+\gamma_K}.}
\tag{5.2}
\]

Then

\[
c_{n,K}\to0,
\qquad
c_{n,K}\sqrt n=n^{\gamma_K}\to\infty,
\qquad
c_{n,K}\sqrt{\log n}\to0.
\tag{5.3}
\]

So the singular time point is still suppressed by

\[
\exp[-\Omega(n^{\gamma_K})],
\tag{5.4}
\]

while the nonzero Gibbs law is uniformly close to the nonzero-uniform law.

If a coefficient vector has the inherited `L^2` error

\[
\rho_n=O(c_{n,K}\sqrt{\log n}),
\]

then interpolation between `L^2` and the trivial Fourier `L^infty` bound gives

\[
\|F\|_{L^p}
\le n^{1/2-1/p}\rho_n
=O\left(n^{\gamma_K-1/p}\sqrt{\log n}\right).
\tag{5.5}
\]

For every `p<=P_K`,

\[
\gamma_K-{1\over p}
\le -{1\over2P_K}<0,
\]

hence

\[
\boxed{\|F\|_{L^p}=o(1)\quad(2\le p\le P_K).}
\tag{5.6}
\]

Therefore the flat-model collision bounds from Lemma 4.1 transfer to every word required by any prescribed `K`-step symbolic expansion.

The resulting common exceptional probability is

\[
q_{n,K}
=
O_K\left({(\log n)^{1/4}\over n}\right)
+\exp[-\Omega_K(n^{\gamma_K})]
=
o\left({1\over\sqrt{\log n}}\right).
\tag{5.7}
\]

The first term includes the inherited selected quadratic-energy concentration; the finite higher-degree list contributes only `O_K(n^{-1})`.

---

# 6. Finite-K near-boundary iteration theorem

We can now iterate Lemma 2.1 without pretending that the fixed projector is resampled.

## Theorem 6.1 — arbitrary prescribed finite number of actual contractions

For every fixed integer `K>=1`, there exist constants

\[
\epsilon_K>0,
\qquad
0<c_K<C_K<\infty
\]

such that the following holds.

Fix `0<epsilon<epsilon_K`, set

\[
d=(1+\epsilon)^{-1},
\]

and use the adaptive seed (5.2). For all sufficiently large odd `n`, outside an event of probability `q_{n,K}` from (5.7), the actual fixed-projector random-circulant square-Newton scheme admits `K` consecutive covariance-regularized positive contraction steps.

Writing

\[
\rho_j=1-\nu_j^2,
\]

for the state before step `j+1`, every state that remains in the near-boundary regime satisfies

\[
\boxed{
c_K\sqrt{\rho_j}
\le\rho_{j+1}
\le C_K\sqrt{\rho_j},}
\tag{6.1}
\]

and

\[
\boxed{
\Gamma_{j+1}^2\le1+C_K\rho_{j+1},
\qquad
|\kappa_{j+1}|\le C_K\rho_{j+1}.}
\tag{6.2}
\]

### Proof

At `j=0`, the inherited vanishing-tilt theorem gives

\[
\nu_0^2=d^2+o(1),
\qquad
\Gamma_0^2=1+o(1),
\qquad
\kappa_0=o(1),
\tag{6.3}
\]

with source-sufficient failure. Since `epsilon` is fixed before `n->infinity`, (6.3) implies the hypotheses of Lemma 2.1 once `epsilon_K` is small enough.

Suppose the claim holds through state `j<K`. The density relative to the adaptive seed is the product of `j` positive quadratic score factors and `j` regularizing mixtures, hence it belongs to a finite polynomial/convolution dictionary whose degree depends only on `j`. The covariance inversions occur only in the active finite dictionary; their denominators are bounded away from zero by the regularizing floor `eta I`. Lemmas 4.1 and 5.1 therefore give all fixed coefficient-word bounds needed in (3.6)--(3.10), with common failure (5.7).

Lemma 2.1 gives (6.1). Equations (3.6)--(3.10) give (6.2). In particular, the hypotheses needed for the next application of Lemma 2.1 reproduce themselves, with constants enlarged only by an amount depending on the fixed step index. Since `K` is fixed, take the maximum of those finitely many constants and then choose `epsilon_K` small enough that every one of the `K` applications stays in its valid near-boundary neighborhood.

This completes the induction. ∎

### Quantitative interpretation

Ignoring the `K`-dependent constants, the deterministic scale is

\[
\rho_{j+1}\asymp\sqrt{\rho_j}.
\tag{6.4}
\]

Since initially

\[
\rho_0=1-d^2=2\epsilon+O(\epsilon^2),
\tag{6.5}
\]

formal iteration gives

\[
\rho_j\approx \epsilon^{\,2^{-j}}.
\tag{6.6}
\]

Thus only `O(log log(1/epsilon))` steps should be needed to reach an absolute coarse decrement gap. **Theorem 6.1 does not yet make that last statement uniform in `K`** because its collision/stability constants are allowed to depend on the prescribed finite depth. This is now the precise remaining near-boundary issue.

A concrete immediate corollary is stronger than the previous checkpoint: not only the first two, but **any prescribed finite number of actual fixed-projector positive square-Newton contractions** is rigorously available at sufficiently sharp fixed source slack.

---

# 7. What moved and what did not

## Fixed full-source bound

Unchanged:

\[
\sqrt n\le\mathbf E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]

No full P07 solution is claimed.

## New proved intermediate results

1. **Deterministic square-root escape.**  
   If `rho=1-nu^2`, `Gamma^2<=1+C rho`, and the longitudinal normalized third moment satisfies `|kappa|<=C rho`, then one covariance-regularized positive square step produces
   \[
   rho_+\asymp\sqrt{rho}.
   \]

2. **Invariant reproduction under a finite word envelope.**  
   The density perturbation has coefficients `u,v=O(sqrt(rho))`; fixed-projector covariance leakage is of that same order, and the next skew/longitudinal bounds reproduce as `Gamma_+^2<=1+O(rho_+)`, `|kappa_+|=O(rho_+)`.

3. **Arbitrary fixed-degree collision control.**  
   The Walsh/additive-counting argument extends to any finite preselected convolution degree, with `O_R(n^-1)` failure after normalization.

4. **Adaptive vanishing seed.**  
   For a prescribed finite depth `K`, the choice `c_{n,K}=n^{-1/2+1/(2P_K)}` with `P_K=8K+16` suppresses the origin while providing every fixed `L^p`, `p<=P_K`, needed by the `K`-step dictionary.

5. **Finite-K actual iteration.**  
   For every fixed `K`, sufficiently sharp fixed source slack admits `K` consecutive actual fixed-projector square-Newton contractions with failure `o(1/sqrt(log n))`.

## Still unresolved

* The constants in Theorem 6.1 are not yet uniform in `K`. Therefore it does not yet prove `O(log log(1/epsilon))` escape to an **absolute** coarse gap as `epsilon downarrow0`.
* No compact coarse-regime invariant with geometric residual decay is proved.
* Exact positive moment feasibility, and therefore the P07 source endpoint, remains open.
* The argument remains written for odd cyclic order. The even-order self-inverse frequency is still untreated.

---

# 8. Next concrete attack

The next run should quantify the degree dependence instead of adding another ad hoc step.

A useful target is an explicit bound of the form

\[
M_R\le \exp(CR\log R)
\tag{8.1}
\]

for the normalized fixed-word collision envelope through degree `R`, together with corresponding stability constants growing at most `exp(CR log R)`. Since the required step count is only `K=O(log log(1/epsilon))`, such growth would still be slow enough to test whether the square-root recursion reaches a source-independent coarse gap before the admissible near-boundary radius collapses.

If this uniform-in-depth estimate succeeds, the next target is a compact coarse region, for example

\[
\nu^2\le1-\rho_*,\qquad
\Gamma\le G_*,\qquad
|\kappa|\le K_*,
\]

on which a fixed damped positive square update contracts the decrement geometrically while preserving the same bounds. That would turn finite-K progress into exact moment feasibility.

The present result is therefore a genuine advance but remains **PROVED PARTIAL**.