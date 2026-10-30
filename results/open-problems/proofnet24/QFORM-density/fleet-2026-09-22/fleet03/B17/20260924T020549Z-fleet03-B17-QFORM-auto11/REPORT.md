# fleet03/B17 — fixed 5% spectral-gap fragmented witness

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T020549Z-fleet03-B17-QFORM-auto11`  
Status: `NEW SOURCE-VALID WITNESS / PARTNER RESULT APPLIED / FULL TARGET OPEN`.

The unrestricted quadratic-form bounded-density conjecture remains OPEN. This run strengthens the current sharp-witness picture by showing that an output-density lower bound above 4 survives **simultaneously** under (i) a fixed positive margin above the spectral threshold on all three active eigenvalues, (ii) an entrywise-dense rotation, and (iii) a fixed positive asymptotic probability of using arbitrarily remote support fragments.

No Monte Carlo, moment assumption, post-rotation independence, connected-support hypothesis, arbitrary-joint coarea bound, or pointwise van-der-Corput estimate is used.

## 1. Completed sources actually used

Designated partner `fleet04/B17` completed the macroscopic fragmented-main-cell mechanism at

- `yspennstate/math-open-problems@4be63022324b82f254f1d7a4353a3e883f08d10a`,
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B17/20260924T011922Z-fleet04-B17-QFORM-r6/REPORT.md`.

Its exact positive-mixture inequality is
\[
\|p_Q\|_\infty\ge \ell_m^{3m-2}\|p_{Q_m^0}\|_\infty, \tag{1.1}
\]
when every one of the `3m` cap-one marginals has a main interval of length `ell_m`, and `Q_m^0` is the centered-unit-interval base form. This run applies (1.1) below with a genuinely different base spectrum having a fixed gap on **all three** active eigenvalues.

The centered-bank limit is supplied by the completed fleet01/B17 theorem
`QFORM-DIFFUSE-BANK-SPECTRAL-SLACK-COMPACTIFICATION-v1`:

- scientific commit `7d64d480f3b1b8f10f3ea1b169c1a6aeccbec5ea`,
- completion commit `d19c3dd3bc5e0e7a7f1c8eca725186ace671416f`,
- path `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B17/20260924T003703Z-fleet01-B17-QFORM-auto11/REPORT.md`.

Its Proposition 3.1 gives uniform density convergence of the three independent normalized uniform banks to the corresponding Gaussian quadratic-form density on every compact spectral box. The same report pins the integrable Fresnel--Brascamp--Lieb majorant that upgrades weak CLT convergence to uniform density convergence.

## 2. Exact dense matrix with a fixed 5% spectral margin

Let
\[
n=\frac{(1,2,3)}{\sqrt{14}},\qquad
H=I_3-2nn^\top
=\frac17
\begin{pmatrix}
6&-2&-3\\
-2&3&-6\\
-3&-6&-2
\end{pmatrix}.
\]
Since `H^2=I_3`, its spectrum is `{1,1,-1}`. Define
\[
B=\frac{21}{20}H
=\begin{pmatrix}
9/10&-3/10&-9/20\\
-3/10&9/20&-9/10\\
-9/20&-9/10&-3/10
\end{pmatrix}. \tag{2.1}
\]
Every entry is nonzero and
\[
\boxed{\operatorname{spec}(B)=\{21/20,21/20,-21/20\}.} \tag{2.2}
\]
Thus **all three** active eigenvalues have modulus exactly `1.05`, a fixed 5% margin above the owner's threshold.

For `m>=2`, let `R_m` be the `3m x 3` synthesis matrix with `m` rows `e_j/sqrt(m)` in bank `j`, and put
\[
A_m=R_mBR_m^\top . \tag{2.3}
\]
Because `R_m^T R_m=I_3`,
\[
\boxed{\operatorname{spec}_{\ne0}(A_m)=\{21/20,21/20,-21/20\}} \tag{2.4}
\]
for every finite `m`. Since every entry of `B` is nonzero, every entry of the physical `3m x 3m` matrix `A_m` is nonzero as well.

## 3. Centered-bank sharp limit

Let all `3m` physical variables first be independent `U_i~Unif[-1/2,1/2]`, and write
\[
Q_m^0=U^TA_mU.
\]
The three normalized bank sums converge to `G~N(0,I_3/12)`. The completed fleet01/B17 density-compactification theorem makes this convergence uniform at the output-density level. Since `B=(21/20)H` and the Gaussian law is rotationally invariant,
\[
G^TBG\ \stackrel d=\ \frac{21}{20}(G_1^2+G_2^2-G_3^2).
\]
The unit-spectrum Gaussian form has density supremum `3sqrt(2)`, so scalar output rescaling gives
\[
\boxed{
\|p_{Q_m^0}\|_\infty\longrightarrow
\frac{20}{21}\,3\sqrt2
=\frac{20\sqrt2}{7}
=4.040610178208843\ldots .} \tag{3.1}
\]
This is already a dense rotated exact-target family with a fixed 5% spectral margin and asymptotic density above 4.

## 4. Add macroscopic, arbitrarily remote fragmentation

Choose
\[
\alpha=\frac1{200},\qquad
\theta=-\frac13\log(1-\alpha)=-\frac13\log\frac{199}{200}. \tag{4.1}
\]
For each `m`, set
\[
\varepsilon_m=\frac{\theta}{m},\qquad
\ell_m=1-\frac{\theta}{m}. \tag{4.2}
\]
Choose any remote location `R_m^*>1`, allowed to tend to infinity arbitrarily fast. Every physical coordinate has the normalized cap-one density
\[
f_m(x)=
\mathbf1_{[-\ell_m/2,\ell_m/2]}(x)
+\mathbf1_{[R_m^*,R_m^*+\varepsilon_m]}(x). \tag{4.3}
\]
Thus `0<=f_m<=1` and `int f_m=ell_m+epsilon_m=1`, with two disconnected support components and unboundedly growing support diameter if desired.

Let `M_m` be the event that all `3m` coordinates select their main interval. Then
\[
\mathbb P(M_m)=\ell_m^{3m}\to e^{-3\theta}=\frac{199}{200}, \tag{4.4}
\]
so the complementary event has the fixed positive limit
\[
\boxed{\mathbb P(M_m^c)\to\frac1{200}.} \tag{4.5}
\]
This is a genuinely macroscopic product-level fragmentation probability; it does not vanish with dimension.

## 5. Apply the designated partner inequality at the actual density

Conditional on `M_m`, the physical vector is exactly `ell_m U`, hence the conditional output is `ell_m^2 Q_m^0`. The unconditional output law is a positive mixture over support-selection cells. Applying the completed fleet04/B17 inequality (1.1) gives the actual target-level estimate
\[
\boxed{
\|p_{X^TA_mX}\|_\infty
\ge \ell_m^{3m-2}\|p_{Q_m^0}\|_\infty .} \tag{5.1}
\]
Combining (3.1), (4.1), and (5.1),
\[
\begin{aligned}
\liminf_{m\to\infty}\|p_{X^TA_mX}\|_\infty
&\ge \frac{199}{200}\cdot\frac{20\sqrt2}{7}\\
&=\boxed{\frac{199\sqrt2}{70}}
=4.020407127317799\ldots . \tag{5.2}
\end{aligned}
\]
The strict inequality over 4 has an exact integer certificate:
\[
\frac{199\sqrt2}{70}>4
\iff 199\sqrt2>280
\iff 2\cdot199^2>280^2,
\]
and indeed
\[
79202>78400. \tag{5.3}
\]
So for all sufficiently large finite `m`, these exact target instances have density supremum strictly greater than 4.

The same finite-cell/Fresnel mechanism used in the partner report applies after multiplying the quadratic matrix by `21/20`; each finite member has a continuous `C_0` output density. This continuity assertion is only for this witness family, not the unrestricted theorem.

## 6. General simultaneous-gap/fragmentation frontier

The preceding construction has a useful two-parameter form. Replace `21/20` by `1+eta`, where `eta>0`, keeping the same dense Householder orientation, and choose the satellite-event limit to be any `alpha in (0,1)` by setting
\[
\theta=-\frac13\log(1-\alpha).
\]
Then every finite matrix has exact nonzero spectrum
\[
\{1+\eta,1+\eta,-(1+\eta)\}, \tag{6.1}
\]
while the same completed bank limit and partner mixture inequality give
\[
\boxed{
\liminf\|p_Q\|_\infty
\ge (1-\alpha)\frac{3\sqrt2}{1+\eta}.} \tag{6.2}
\]
Therefore this family remains above 4 precisely whenever
\[
\boxed{
\alpha<1-\frac{4(1+\eta)}{3\sqrt2}.} \tag{6.3}
\]
The right side is positive exactly for
\[
\boxed{0<\eta<\frac{3\sqrt2}{4}-1
=0.060660171779821\ldots .} \tag{6.4}
\]
Thus a proof that hopes to improve the universal constant below 4 by imposing merely a **strict** three-eigenvalue margin cannot work even if all three active eigenvalues are separated from the threshold by a fixed common amount: every common margin below about `6.066%` admits a dense fragmented exact-target sequence with an analytic lower density above 4, and one may retain a fixed positive amount of remote product mass according to (6.3).

For the concrete 5% margin, the largest satellite fraction permitted by this lower-bound mechanism is
\[
1-\frac{4(21/20)}{3\sqrt2}
=0.0100505063388\ldots, \tag{6.5}
\]
so the explicit choice `alpha=1/200=0.005` has comfortable strict room.

## 7. Scope and next implication

This is a sharp-witness constraint, not a counterexample. It does **not** improve the universal lower obstruction `C_*>=3sqrt2`, because `(eta,alpha)->(0,0)` is still needed to approach `3sqrt2`. What it adds is quantitative rigidity against two common proof simplifications:

1. fixed spectral strictness of every active eigenvalue, up to a concrete 6.066% common margin, does not force density below 4;
2. disconnected arbitrarily remote support with a fixed positive product-level satellite probability does not force density below 4.

The unrestricted QFORM theorem and full-target continuity remain OPEN. A genuinely sharper lower witness than `3sqrt2`, if it exists, must leave this scalar-scaled three-diffuse-bank Gaussianization chamber; promising mechanisms remain a surviving non-Gaussian component, multiple macroscopic shared rows, off-tip alignment, or interacting additional spectrum.
