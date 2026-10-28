SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B17, 2026-09-23T11:30:26Z.
attacking: vanishing-intensity remote fragments at the critical sqrt(m) scale; test whether a first-order non-Gaussian perturbation can overshoot 3 sqrt(2).

# Rare-fragment first variation is strictly unfavorable at the sharp rotated witness

Programme: QFORM-DENSITY-3EIG-20260922
Worker: account03/B17
Run: 20260923T113026Z-account03-B17-QFORM-auto11
Classification: SUPPORTING_ANALYTIC_WITNESS_CONSTRAINT
Full conjecture: OPEN / NOT PROVED
Full-target continuity: OPEN
Execution: WITHOUT_VERIFIED_BRAIN

## 1. Statement

Use the completed account04/B17 rational three-bank frame

\[
O={1\over7}\begin{pmatrix}6&-2&-3\\-2&3&-6\\-3&-6&-2\end{pmatrix},\qquad
J=\operatorname{diag}(1,1,-1),
\]

and let the row attached to bank `j` be `O e_j/sqrt(m)`, repeated `m` times. Then `R_m^T R_m=I_3`, hence

\[
A_m=R_m J R_m^T
\]

has exact nonzero spectrum `{1,1,-1}` for every `m`. In bank coordinates

\[
B=O^TJO={1\over49}\begin{pmatrix}
31&-36&-12\\
-36&-23&-24\\
-12&-24&41
\end{pmatrix}.
\]

Fix constants `c_j>=0` and nonzero real `a_j`. Put

\[
\varepsilon_{j,m}={c_j\over m^2}.
\]

For all sufficiently large `m`, choose the independent physical input density in bank `j` to be

\[
f_{j,m}(x)=
(1-\varepsilon_{j,m})\mathbf 1_{[-1/2,1/2]}(x)
+
\mathbf 1_{[a_j\sqrt m-\varepsilon_{j,m}/2,\,a_j\sqrt m+\varepsilon_{j,m}/2]}(x).
\]

The two intervals are then disjoint. Therefore `f_{j,m}` is an exact probability density and `0<=f_{j,m}<=1`. Its support is disconnected and its diameter is of order `sqrt(m)`; no compact-diameter, connected-support, Gaussian or log-concavity hypothesis is being added.

Let `Q_m=X^T A_m X`. Define

\[
P_*=3\sqrt2,\qquad a_0={5295\over21952}.
\]

Then the cone-tip density obeys the first-variation inequality

\[
\boxed{
\liminf_{m\to\infty}
 m\left(1-{p_{Q_m}(0)\over P_*}\right)
\ge
 a_0+{1\over2}\sum_{j=1}^3 c_j\bigl(1-e^{-6a_j^2}\bigr).
}
\]

In particular every genuine remote fragment (`c_j>0`, `a_j!=0`) makes the first-order deficit from `3 sqrt(2)` strictly larger. Thus a vanishing-intensity fragment of mass `c_j/m^2` placed at the critical physical distance `a_j sqrt(m)` cannot turn the completed rotated witness into an order-`1/m` overshoot above `3 sqrt(2)`.

For the symmetric choice `c_j=a_j=1`,

\[
a_0+{3\over2}(1-e^{-6})
=1.7374899621140092\ldots,
\]

compared with the unfragmented partner deficit `a_0=0.24120809037900875...`.

This theorem concerns the value at the cone tip. It does not prove that the global finite-`m` mode remains at zero, and therefore does not prove a global `3 sqrt(2)` upper bound for this fragmented family.

## 2. Exact mixture decomposition

Each physical law is exactly the mixture

- with probability `1-epsilon_{j,m}`, a centered unit uniform;
- with probability `epsilon_{j,m}`, a uniform on the remote interval of length `epsilon_{j,m}`.

Let `N_j` be the number of remote selections among the `m` variables of bank `j`. Then

\[
N_j\sim\operatorname{Bin}(m,c_j/m^2)
\]

independently across the three banks. Put `C=c_1+c_2+c_3`. The exact binomial expansions give

\[
\Pr(N_1=N_2=N_3=0)=1-{C\over m}+O(m^{-2}),
\]

and, for the event `E_j` of exactly one remote selection in bank `j` and none in the other two banks,

\[
\Pr(E_j)={c_j\over m}+O(m^{-2}).
\]

The probability of two through six total remote selections is `O(m^{-2})`. Counts at least seven have probability `O(m^{-7})`.

## 3. Zero-remote component: apply the completed partner result

Conditioned on zero remote selections, all `3m` physical variables are exactly centered unit uniforms. This is precisely the completed account04/B17 source-valid witness. Their weighted local Edgeworth/coarea calculation proves

\[
\boxed{
p_{0,m}(0)=P_*\left(1-{a_0\over m}+O(m^{-2})\right).}
\]

Source actually applied:
`yspennstate/math-open-problems@2156b76156ad5956c214a881fcfd6d977d6f3b9f`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B17/20260922T211900Z-account04-B17-QFORM-r3/REPORT.md`.

This is the required completed-partner input to an actual inequality in the present run.

## 4. One-remote component and the affine-Gaussian penalty

Condition on `E_j`. The normalized bank vector has the form

\[
Y_m=a_j e_j+G_m^{(j)}+\eta_m e_j,
\]

where `G_m^{(j)}` is formed from `m-1` centered uniforms in bank `j` and `m` centered uniforms in the other two banks, all normalized by `sqrt(m)`, while the residual remote-interval noise satisfies `|eta_m|<=epsilon_{j,m}/(2sqrt(m))=O(m^{-5/2})`.

The standard weighted local CLT/Edgeworth argument used in the partner proof therefore gives local convergence of the bank density to

\[
N(a_j e_j,I_3/12).
\]

Since

\[
Q_m=Y_m^T B Y_m=(O Y_m)^T J(OY_m),
\]

the limiting spectral mean is

\[
h_j=O(a_j e_j),\qquad \|h_j\|=|a_j|.
\]

Let `q_j` denote the limiting zero density of this noncentral Gaussian quadratic form. The previously proved sharp affine-Gaussian cone-tip estimate gives

\[
\boxed{
{q_j\over P_*}
\le {1+e^{-6a_j^2}\over2}.
}
\]

Hence every nonzero critical-scale remote shift has a strictly smaller cone-tip density than the centered Gaussian endpoint.

The affine-Gaussian source is worker-owned prior work:
`yspennstate/math-open-problems@dcf8885d5153370cacfa246ad1e29fb06d971769`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B17/20260923T070310Z-account03-B17-QFORM-r25/REPORT.md`.

## 5. Remainder from two or more remote selections

For any fixed total remote count `r<=6`, every bank still contains `m-O(1)` centered unit uniforms. The normalized bank densities therefore have a uniform `L^infinity` bound for all large `m` (convolution plus the standard local CLT bound). Since `B` is a fixed invertible `3x3` matrix, the already-established original-coordinate rank-three/localized theorem gives a finite uniform bound on the conditional quadratic output density. Thus the total contribution of `2<=r<=6` is `O(m^{-2})`.

For `r>=7`, use a crude polynomial bound. A normalized sum containing at least one centered uniform has density at most `sqrt(m)` by convolution. If all summands in a bank are remote uniforms, a single normalized remote variable has density at most `sqrt(m)/epsilon_{j,m}=O(m^{5/2})`, and convolution cannot increase that cap. Hence every conditioned bank density is at most `O(m^{5/2})`. Scaling the fixed three-dimensional invertible quadratic-form bound gives an `O(m^5)` conditional output-density bound. Multiplying by `Pr(r>=7)=O(m^{-7})` yields `O(m^{-2})`.

Therefore the complete `r>=2` contribution to `p_{Q_m}(0)` is `O(m^{-2})`.

## 6. Assemble the first variation

The exact mixture identity gives

\[
p_{Q_m}(0)
=\Pr(N=0)p_{0,m}(0)
+\sum_{j=1}^3\Pr(E_j)p_{1,j,m}(0)
+O(m^{-2}),
\]

where `p_{1,j,m}(0)->q_j`. Substituting the expansions from Sections 2--4,

\[
{p_{Q_m}(0)\over P_*}
=1-{1\over m}
\left[a_0+\sum_{j=1}^3c_j\left(1-{q_j\over P_*}\right)\right]
+o(m^{-1}).
\]

Using the noncentral bound,

\[
1-{q_j\over P_*}
\ge {1-e^{-6a_j^2}\over2},
\]

which proves

\[
\liminf_{m\to\infty}
 m\left(1-{p_{Q_m}(0)\over3\sqrt2}\right)
\ge {5295\over21952}
+{1\over2}\sum_jc_j(1-e^{-6a_j^2}).
\]

## 7. Interpretation for the sharp-constant search

The previous fragmented-family run excluded the finite-activity regime `epsilon_m=lambda/m`, whose limit is a Gaussian core plus compound-Poisson shift. The present theorem covers the subtler `epsilon_m=c/m^2` regime: the Gaussian limit is unchanged, but rare remote fragments survive exactly at the same `1/m` scale as the partner's Edgeworth correction. Their first variation has the wrong sign for producing a stronger lower bound.

So two nearby multiscale escape routes are now excluded at the cone tip:

1. finite-activity critical fragments (`mass ~1/m` at distance `sqrt(m)`) cannot raise the limiting ceiling above `3 sqrt(2)`;
2. vanishing-activity critical fragments (`mass ~1/m^2` at distance `sqrt(m)`) cannot reverse the first finite-size correction.

A stronger witness, if it exists, must use a different mechanism: for example an off-tip mode, a scale between these two regimes with nontrivial dependence on the frame, several correlated mesoscopic shared rows, or a non-CLT triangular array not reducible to an independent random shift of the minimum-variance Gaussian core.

No refuted arbitrary-joint coarea estimate, post-rotation independence claim, conditional projection-cap moment, pointwise van-der-Corput decay, fiber-supremum principle, or Monte Carlo histogram is used.

## 8. Scope and continuity

Every finite input law above is source-valid under the exact target assumptions. The theorem establishes the displayed cone-tip asymptotic and associated lower-bound constraint. It does not establish the unrestricted QFORM upper bound. No new full-family continuity theorem is claimed here; full-target continuity remains open.

