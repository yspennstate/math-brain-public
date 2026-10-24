# account02/B16 — source n=18 coherent-bias test reduced to two exact candidate secants

**Classification:** `ESSENTIAL_STEP_APPLIED / EXACT_FINITE_BIAS_SCALAR_REDUCTION / FULL_FEI_OPEN`.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED.**

## 0. Later-owner precedence and scope

Fresh owner control revision `2026-09-22.2` supersedes the older Campaign-C half-band wording and directs all FEI workers to the equivalent all-gate inequality. I therefore did not reopen the retired positive-current route. The live candidate inherited from the current chain is
\[
C_*=6.5218512,\qquad
\Gamma_*(p)=\Gamma_0(p)+a_*p(1-p),\qquad
a_*=0.2682048,\qquad \Gamma_0(1/2)=C_0=6.4548.
\]
The universal obligation remains `LIMIT-PRIME-GATE-LIFT-v1`: prove the gate defect is nonnegative for every composition-prime Boolean gate and every interior product bias, or produce a genuine prime/bias counterexample.

The latest **completed** account02/B18 lead consumed before this run is
`account02/B18/20260922T051105Z-random-depth-barycenter/REPORT.md`, which gives the exact currency-weighted random-depth cocycle and shows that local margin requests may exceed the center while only their signed Poincare-currency average matters. A newer B18 invocation has only a start record at `20260922T070547Z-n18-first-cell-cusp-resolution`; it targets the unavailable current candidate's near-half values. To avoid duplication, this B16 run does **not** reconstruct or guess those candidate bytes. It instead eliminates the entire source-side Fourier/entropy remainder and reduces B18's candidate-side job to two secant values.

## 1. Last three B16 substantive reports

The last three completed substantive B16 mechanisms were:

1. `20260922T040442Z-fixedT-character-recoding`: fixed exceptional support, arbitrary host grouping/orientation, symbolic uniform-bias closure.
2. `20260922T045212Z-recmaj-collision-architecture-obstruction`: a materially different occurrence/collision mechanism; recursive majority shows collision entropy alone is unpayable without the negative architecture KL credit.
3. `20260922T045841Z-source-bias-log-curvature`: the exact n=18 source gate has a unique negative biased zero-mode-birth direction; coherently biasing all nine core variables yields
\[
D_\Gamma(u)=D_\Gamma(0)-{67383\over8192}u^2\log_2(1/u^2)+O_\Gamma(u^2).
\]
At `u=1/5000` the leading decrement exceeds the certified central stable-candidate defect by
`2.3822767131526423e-6`, but the finite `O(u^2)` remainder was unpaid because the current f4 candidate bytes were unavailable.

**FULL-PROBLEM CHANGE: NONE.** Full FEI is still open.  
**MECHANISM CHANGE: YES.** This run replaces the asymptotic `O(u^2)` placeholder by an exact finite source identity and a two-secant candidate criterion. It does not introduce another gate family or another positive kernel.

## 2. Named OTHER-account theorem consumed and applied

I consumed account04/B14
`20260922T051345Z-balanced-transposition-barrier/REPORT.md`.
For this same balanced composition-prime n=18 source gate it proves, with exact interval arithmetic, that every single balanced truth-table transposition strictly decreases the danger functional at `C_*=6.5218512`; in particular all one-pair gate mutations are repelled while the coherent product-bias direction from the preceding B16 report remains live.

This is used, not merely cited: it removes local gate mutation as the competing source-valid falsification mechanism and makes the present finite product-bias calculation the nonoverlapping local threat. Nothing below changes the truth table.

## 3. Exact ten-transform entropy reduction

Let `x in {0,1}^9` be the nine core bits and `y in {0,1}^9` the nine host bits. The inherited source reconstruction has nine disjoint exceptional core pairs
\[
P_1=(78,79),\ P_2=(113,121),\ P_3=(228,484),\ P_4=(170,186),\ P_5=(149,151),
\]
\[
P_6=(338,466),\ P_7=(284,316),\ P_8=(291,295),\ P_9=(393,457).
\]
Writing the signed base-core function as `f_0(x) in {+1,-1}`, every exceptional cell has `f_0=+1`, and the complete source gate is exactly
\[
F(x,y)=f_0(x)-2\sum_{j=1}^9 1_{P_j}(x)y_j.
\tag{3.1}
\]
The committed reconstruction reproduces source truth-table SHA-256
`f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`.

Bias every core coordinate by the same `p=1/2+u` and keep every host unbiased. In the host Fourier basis, (3.1) has **only host degree 0 or 1**. Precisely,
\[
g_0(x)=f_0(x)-\sum_j1_{P_j}(x),\qquad g_j(x)=-1_{P_j}(x),
\tag{3.2}
\]
and, for every core frequency `S`,
\[
\widehat F_p(S,\varnothing)=\widehat g_{0,p}(S),\qquad
\widehat F_p(S,\{j\})=\widehat g_{j,p}(S),
\tag{3.3}
\]
with all host degree at least two coefficients zero. Here
\[
\widehat h_p(S)=\sum_x h(x)\mu_p(x)
\prod_{i\in S}{x_i-p\over\sqrt{p(1-p)}}.
\tag{3.4}
\]
Therefore the full 18-bit biased spectral entropy is **exactly** the finite 10-by-512 sum
\[
\boxed{
\widetilde H_F(u)=
\sum_{S\subseteq[9]}\phi(\widehat g_{0,p}(S)^2)
+\sum_{j=1}^9\sum_{S\subseteq[9]}\phi(\widehat g_{j,p}(S)^2),
\quad \phi(w)=-w\log_2w.
}
\tag{3.5}
\]
This is a structural equality, not a numerical approximation. It removes the apparent 18-dimensional entropy computation from the finite gate test.

## 4. Exact finite defect identity at u=1/5000

For the coherent core bias, the exact source polynomials from the preceding B16 report are
\[
p_{out}(u)=\frac12+\frac{513}{256}u-\frac{105}{16}u^3+\frac{99}{8}u^5-9u^7+u^9,
\]
\[
d_c(u)=\frac{513}{256}-\frac{315}{16}u^2+\frac{495}{8}u^4-63u^6+9u^8,
\qquad d_h(u)=9(1/4-u^2)^4.
\]
Put
\[
\delta(u)=p_{out}(u)-\frac12,
\]
and, using symmetry of `Gamma_*`, define the exact potential increment
\[
\Delta P_*(u)=
 d_c(u)\Gamma_*(1/2-u)+d_h(u)C_*
 -\Gamma_*(1/2-\delta(u))-\frac{133}{128}C_*.
\tag{4.1}
\]
Then no asymptotic remainder remains:
\[
\boxed{
D_*(u)=D_*(0)+\Delta P_*(u)
+d_c(u)h_2(1-4u^2)-[\widetilde H_F(u)-\widetilde H_F(0)].
}
\tag{4.2}
\]
Equation (3.5) makes every non-candidate term in (4.2) source-exact.

At
\[
u={1\over5000},
\]
the high-precision checker gives, stably at 80 and 120 decimal digits,
\[
\widetilde H_F(0)=6.77660530900597808251979022189188231478723503802017\ldots,
\]
\[
\widetilde H_F(u)=6.77661493183901009867244551897405101830997135503807\ldots,
\]
\[
\delta=0.000400781197500003959999884800000512,
\]
\[
d_c h_2(1-4u^2)=7.70080659758327873325972079227816\times10^{-6}.
\]
The central defect recovered from the same finite sum is
\[
D_*(0)=5.70349402191748020977810811768521\times10^{-6},
\]
matching the previously certified central interval.

Consequently the stable candidate is **falsified by this already-proved composition-prime gate at this single bias point if and only if**
\[
\boxed{
\Delta P_*(1/5000)
< -3.78146758748460628774074674125985\times10^{-6}.
}
\tag{4.3}
\]
This is the weakest sufficient full finite-net bound for this point because (4.2) is an equality: no source entropy, terminal term, influence term, or logarithmic remainder is left unpaid.

For continuity with the previous singular calculation, if
\[
L(u)={67383\over8192}u^2\log_2(1/u^2),
\]
then the entire **source-side regular remainder** is now explicit:
\[
R_{src}(u):=d_c h_2(1-4u^2)-[\widetilde H_F(u)-\widetilde H_F(0)]+L(u),
\]
with
\[
\boxed{R_{src}(1/5000)=6.16374430063724862040583136253103\times10^{-6}.}
\tag{4.4}
\]
Thus the old `O_Gamma(u^2)` has been localized completely to the candidate potential secants.

## 5. Current candidate reduced to two base-potential secants

Write
\[
\Gamma_*(z)=\Gamma_0(z)+a_*z(1-z),\qquad a_*=0.2682048,
\]
with `Gamma_0(1/2)=C_0=6.4548`. The quadratic part of (4.1) is exact and equals
\[
\Delta P_{quad}=-3.27291991387873254912239397903190\times10^{-8}.
\tag{5.1}
\]
Hence (4.3) is equivalent to
\[
\Delta P_0< -3.74873838834581896224952280146953\times10^{-6}.
\tag{5.2}
\]
Define only two scalar secants of the unavailable base candidate,
\[
q(t):={C_0-\Gamma_0(1/2-t)\over t},\qquad t>0.
\tag{5.3}
\]
A direct rearrangement gives
\[
\Delta P_0=
\delta q(\delta)-d_cu q(u)
+\left[d_c+d_h-1-{133\over128}\right]C_0.
\tag{5.4}
\]
At `u=1/5000`, put
\[
\rho={d_cu\over\delta}
=0.99999973801170111030557084364597253353309912384669\ldots,
\]
\[
\tau=0.0036919120632476182006947434430134091303925959472723\ldots.
\]
Then the finite candidate decision is the single scalar comparison
\[
\boxed{
D_{\Gamma_*}(F;p(1/5000))<0
\iff
q(\delta)-\rho q(1/5000)<\tau.
}
\tag{5.5}
\]
Safety at this point is the reverse weak inequality. This is the smallest honest source-bound handoff I can derive without the actual current f4 bytes: **two candidate secants and one threshold**. No candidate value has been guessed from the older h96 file.

This scope is deliberately complementary to the current account02/B18 start, which is attempting to resolve the near-half candidate cell itself.

## 6. Checker and status

`CHECKER.py` reconstructs the source hash, proves the host-degree reduction by construction, performs the ten core transforms, verifies total Fourier mass one, and recomputes all constants at both 80 and 120 decimal digits; the first 50 significant digits of every decision constant agree. `CHECK_OUTPUT.txt` reports `STATUS PASS`.

The high-precision decimal evaluation is a decisive computational cross-check, not an interval-arithmetic proof of the displayed decimal truncations. The theorem-sized content is the exact algebraic reduction (3.1)--(5.5); one can retain the finite sums in (3.5) if certified enclosures of the decimal constants are required.

## 7. Before/after universal gap

**Before:** the source prime gate had a rigorous negative logarithmic curvature and a finite point `u=1/5000` where the leading singular decrement exceeded the central slack, but the whole `O(u^2)` finite remainder was unresolved.

**After:** every source-dependent finite remainder is explicit and the exact stable-candidate decision at that point is reduced to (5.5). The remaining datum is only the current base candidate's two near-half secants `q(1/5000)` and `q(delta)`.

**Exact remaining universal gap:** even a negative result in (5.5) would refute only the present fixed potential, not FEI; a positive result would close only this specific source/bias point. Full FEI still requires a valid symmetric finite-cap potential satisfying the all-gate inequality for every composition-prime gate and every interior bias, or another equivalent universal proof. No novelty or publication-priority claim is made.
