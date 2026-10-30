SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B15, 2026-09-22T22:19:24Z.

attacking: an exact positive Maxwell/tent multiscale representation of density height, so the remaining universal estimate can be stated as a compactly supported averaged small-ball inequality without pointwise Fourier decay or reciprocal-minor inversion.

# fleet03/B15 r20 — exact tent-kernel / Maxwell small-ball normal form

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Worker:** `fleet03/B15`  
**Run:** `20260922T221924Z-fleet03-B15-qform-r20`  
**Status:** `ESSENTIAL_STEP_APPLIED / TARGET_EQUIVALENT_POSITIVE_REGULARIZATION`  
**Full universal QFORM:** **OPEN / NOT PROVED**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and why this run changes mechanism

The target remains: for every dimension, every product law with independent one-dimensional probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove one finite universal constant `C` for the density of `Q=X^TAX`, or give a valid counterexample.

This run does not use any of the corrected false interfaces: no law-uniform one-dimensional van-der-Corput decay, no arbitrary-joint rank-three coarea estimate, no positive conditional projection-density moment, no independence after spectral rotation, and no fiber-supremum estimate. It changes mechanism from the previous B15 absolute-Fourier-tail regularity argument to an exact **positive compact-kernel / averaged-small-ball** formulation.

The new result is not the missing universal inequality. It gives a no-loss target-level interface for that inequality and identifies precisely why a worst conditional density cap must not be taken before averaging.

## 2. Assigned partner result actually applied

Completed partner `fleet04/B15`:

- repository/commit: `yspennstate/math-open-problems@ad7e5daa036cc8330b1432285ad40fec611d37dd`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B15/20260922T211430Z-fleet04-B15-heat-regularity-r4/REPORT.md`.

For the Gaussian kernel

\[
\gamma_\varepsilon(u)=\frac{1}{\sqrt{2\pi}\,\varepsilon}
\exp\!\left(-\frac{u^2}{2\varepsilon^2}\right),
\]

that theorem proves for **every** Borel probability measure `mu` on `R`

\[
\boxed{
\sup_{\varepsilon>0,\,y\in\mathbb R}
(\mu*\gamma_\varepsilon)(y)
=\|p_\mu\|_\infty,
}
\tag{2.1}
\]

with value `+infinity` when no bounded density exists. Thus the central QFORM height problem already has an exact positive heat formulation.

This report proves a second exact formulation with a compactly supported tent kernel and then applies (2.1) to identify the two target constants with **zero loss**.

## 3. General positive-kernel layer-cake theorem

Let `K:R-> [0,infinity)` be an even probability density, nonincreasing and absolutely continuous on `(0,infinity)`, with `K(r)->0` as `r->infinity`. Set

\[
K_\varepsilon(u)=\varepsilon^{-1}K(u/\varepsilon).
\]

For a probability measure `mu`, define the centered small-ball ratio

\[
m_y(r)=\frac{\mu([y-r,y+r])}{2r},\qquad r>0.
\]

### Theorem 3.1 — exact scale mixture

For every `epsilon>0` and `y`,

\[
\boxed{
(\mu*K_\varepsilon)(y)
=\int_0^\infty m_y(r)\,\nu_\varepsilon(dr),
\qquad
\nu_\varepsilon(dr)=-2rK_\varepsilon'(r)\,dr.
}
\tag{3.1}
\]

Moreover `nu_epsilon` is a probability measure on `(0,infinity)`.

### Proof

For `s>=0`, absolute continuity and monotonicity give

\[
K_\varepsilon(s)=\int_s^\infty -K_\varepsilon'(r)\,dr.
\]

Tonelli therefore yields

\[
\begin{aligned}
(\mu*K_\varepsilon)(y)
&=\int K_\varepsilon(|x-y|)\,d\mu(x)\\
&=\int_0^\infty -K_\varepsilon'(r)
\mu([y-r,y+r])\,dr\\
&=\int_0^\infty m_y(r)[-2rK_\varepsilon'(r)]\,dr.
\end{aligned}
\]

Since an integrable monotone `K` satisfies `rK(r)->0`, integration by parts gives

\[
\int_0^\infty -2rK_\varepsilon'(r)\,dr
=2\int_0^\infty K_\varepsilon(r)\,dr=1.
\]

This proves (3.1). `square`

### Theorem 3.2 — exact height characterization

For this scaled approximate identity,

\[
\boxed{
\sup_{\varepsilon>0,\,y\in\mathbb R}
(\mu*K_\varepsilon)(y)=\|p_\mu\|_\infty,
}
\tag{3.2}
\]

again with `+infinity` if `mu` has no bounded density.

If `mu=p dx` and `||p||_infinity<=C`, convolution contraction gives the upper bound immediately. Conversely, suppose every convolution is at most `C`. For every nonnegative `varphi in C_c(R)`,

\[
\int \varphi(y)(\mu*K_\varepsilon)(y)\,dy
\le C\int\varphi(y)\,dy.
\]

As `epsilon->0`, `K_epsilon` is an approximate identity and the left side converges to `int varphi dmu`. Hence `mu<=C dx`, so `mu=p dx` with `p<=C` a.e. Taking the least `C` proves (3.2).

Thus every kernel in this class is an exact positive density-height probe; the kernel changes the scale averaging but not the sharp supremal height.

## 4. Gaussian heat is exactly a Maxwell average of small-ball ratios

For the partner Gaussian kernel,

\[
-2r\gamma_\varepsilon'(r)
=\sqrt{\frac2\pi}\frac{r^2}{\varepsilon^3}
\exp\!\left(-\frac{r^2}{2\varepsilon^2}\right).
\]

This is the density of `epsilon R`, where `R` has the chi distribution with three degrees of freedom (the Maxwell distribution). Therefore (3.1) specializes to

\[
\boxed{
(\mu*\gamma_\varepsilon)(y)
=\mathbb E_{R\sim\chi_3}
\,m_y(\varepsilon R).
}
\tag{4.1}
\]

Combining (4.1) with the completed fleet04/B15 theorem gives the exact identity

\[
\boxed{
\|p_\mu\|_\infty
=\sup_{\varepsilon>0,y}
\mathbb E_{R\sim\chi_3}
\frac{\mu([y-\varepsilon R,y+\varepsilon R])}{2\varepsilon R}.
}
\tag{4.2}
\]

This is an exact multiscale small-ball interpretation of the partner heat normal form; no Fourier decay assumption is involved.

## 5. Compact tent kernel: an exact averaged-small-ball target

Define

\[
\tau(u)=(1-|u|)_+,
\qquad
\tau_\varepsilon(u)=\varepsilon^{-1}
\left(1-\frac{|u|}{\varepsilon}\right)_+.
\]

It is an even probability density and, on `0<r<epsilon`,
`-tau_epsilon'(r)=epsilon^{-2}`. Thus Theorem 3.1 gives

\[
(\mu*\tau_\varepsilon)(y)
=\int_0^\varepsilon m_y(r)\frac{2r}{\varepsilon^2}\,dr.
\tag{5.1}
\]

Equivalently, directly by layer cake,

\[
\boxed{
T_\varepsilon(\mu;y):=(\mu*\tau_\varepsilon)(y)
=\frac1{\varepsilon^2}
\mathbb E(\varepsilon-|Z-y|)_+
=\frac1{\varepsilon^2}
\int_0^\varepsilon
\Pr\{|Z-y|\le r\}\,dr,
}
\tag{5.2}
\]

where `Z~mu`.

Theorem 3.2 now gives

\[
\boxed{
\|p_\mu\|_\infty
=
\sup_{\varepsilon>0,y}
\frac1{\varepsilon^2}
\mathbb E(\varepsilon-|Z-y|)_+.
}
\tag{5.3}
\]

Therefore the full QFORM conjecture is **exactly equivalent**, with the same constant `C`, to the single positive inequality

\[
\boxed{
\mathbb E\bigl(\varepsilon-|X^TAX-y|\bigr)_+
\le C\varepsilon^2
}
\tag{5.4}
\]

for every admissible product input, every admissible `A`, every center `y`, and every `epsilon>0`.

Equivalently,

\[
\boxed{
\int_0^\varepsilon
\Pr\{|X^TAX-y|\le r\}\,dr
\le C\varepsilon^2.
}
\tag{5.5}
\]

This is an **averaged** linear small-ball inequality. It is neither weaker nor stronger than the desired density bound: after taking all scales, it is exactly equivalent.

## 6. Safe Fourier representation: compact support in real space, `sinc^2` damping in frequency

With the Fourier convention `hat h(t)=int e^{itu}h(u)du`,

\[
\widehat{\tau_\varepsilon}(t)
=\left(\frac{\sin(\varepsilon t/2)}{\varepsilon t/2}\right)^2.
\tag{6.1}
\]

Consequently, for every probability law `mu`,

\[
\boxed{
T_\varepsilon(\mu;y)
=\frac1{2\pi}\int_{\mathbb R}
 e^{-ity}\widehat\mu(t)
\left(\frac{\sin(\varepsilon t/2)}{\varepsilon t/2}\right)^2dt.
}
\tag{6.2}
\]

The integral is absolutely convergent solely because `|hat mu(t)|<=1` and `sinc^2` is integrable. It does **not** assert `hat mu in L^1`, and it does not use the refuted law-uniform pointwise quadratic-phase decay claim.

Thus (5.4) has two simultaneously valid forms:

- a positive, compactly supported real-space loss that sees only `|Q-y|<=epsilon`;
- an automatically absolutely convergent Fourier integral retaining oscillatory information about the product law.

## 7. Actual no-loss application of fleet04/B15

The partner theorem (2.1) and the new tent theorem (5.3) imply, for every probability law,

\[
\boxed{
\sup_{\varepsilon,y}T_\varepsilon(\mu;y)
=
\sup_{\delta,y}(\mu*\gamma_\delta)(y)
=
\|p_\mu\|_\infty.
}
\tag{7.1}
\]

This is a genuine quantitative transfer, not a citation-only use of the partner result. In particular:

- if a QFORM branch proves the fleet04 Gaussian heat inequality `(mu_Q*gamma_delta)(y)<=C` at every heat scale and center, then the **same constant** gives `T_epsilon(mu_Q;y)<=C` at every tent scale and center;
- conversely, a proof of (5.4) with constant `C` implies the Gaussian heat bound with the **same constant** by (5.3), density boundedness, and convolution contraction.

Hence the Gaussian and tent programmes have exactly the same sharp universal constant. One may choose whichever keeps the product structure visible longer.

## 8. Why this does not revive the false conditional-cap route

The compact averaged-small-ball functional reveals an exact obstruction to an otherwise tempting proof.

Suppose that after conditioning on a sigma-field `G`, one has only a random conditional density cap `L=L(G)` for `Q|G`. Then

\[
\Pr(|Q-y|\le r\mid G)\le\min(1,2Lr).
\]

Substitution into (5.2) gives

\[
T_\varepsilon(Q;y)
\le \mathbb E\,\Theta_\varepsilon(L),
\tag{8.1}
\]

where

\[
\Theta_\varepsilon(L)=
\begin{cases}
L,&2L\varepsilon\le1,\\[3pt]
\displaystyle
\frac1\varepsilon-
\frac{1}{4L\varepsilon^2},&2L\varepsilon>1.
\end{cases}
\tag{8.2}
\]

For every finite `L`, `Theta_epsilon(L)` increases to `L` as `epsilon downarrow0`. Therefore monotone convergence gives

\[
\boxed{
\sup_{\varepsilon>0}\mathbb E\Theta_\varepsilon(L)
=\mathbb E L,
}
\tag{8.3}
\]

with the right side possibly infinite.

So **tent smoothing cannot repair a proof after one has already replaced a conditional output by its worst conditional density cap**. If that cap is nonintegrable, the all-scale tent supremum faithfully recovers the same divergence. This is consistent with the live counterexamples to universal worst-conditional-cap / positive conditional-moment arguments.

The replacement obligation is precise: on a grouped-bank or scalar-conditioning branch, estimate the conditional positive quantity

\[
\mathbb E[(\varepsilon-|Q-y|)_+\mid G]
\]

directly, while the original-coordinate product/shift geometry is still present, **before** taking a conditional `L^infinity` norm or paying a reciprocal small minor.

## 9. Essential boundedness versus continuity

The exact tent inequality (5.4), uniformly over all scales, proves **essential boundedness** and absolute continuity by Theorem 3.2. It does **not**, by itself, imply that the resulting `L^infinity` density has a continuous representative. This separation is important.

A separate completed fleet02/B15 report,
`yspennstate/math-open-problems@9b8bb7e84811978a2c46c7bb5ec50f2570dbc056`, gives a fixed-matrix `C_0` theorem for rank `>=3` product targets with matrix-dependent height constants. Thus the current archive contains a target-wide qualitative continuity proof, while the shared top-level `CLAIMS.json` has not yet been promoted from `OPEN` for the continuity claim. This report does not use that qualitative continuity statement to infer the missing universal height.

For a fixed instance already known to have `p in C_0`, the tent approximate identity satisfies

\[
\|p*\tau_\varepsilon-p\|_\infty\to0,
\qquad
\sup_y T_\varepsilon(\mu;y)\to\max p
\quad(\varepsilon\downarrow0).
\tag{9.1}
\]

Unlike the Gaussian heat semigroup, no monotonicity in `epsilon` is claimed for the tent maxima.

## 10. First unpaid implication after this run

The full problem is still the universal constant. In the new exact normal form, the first unpaid implication is:

> **Prove one universal `C` such that**
> `E(epsilon-|X^TAX-y|)_+ <= C epsilon^2`
> for all admissible `A`, all cap-one product laws, all centers and all scales, while aggregating original-coordinate product structure before conditional suprema or reciprocal local-minor costs.

This formulation is useful on the difficult near-degenerate grouped-bank branch because it tolerates scale-dependent small-ball estimates and only asks for their triangular average. But Section 8 proves that merely inserting a random conditional density cap cannot close the problem; the averaging must occur before that lossy step.

Natural next application: feed the live grouped-bank/ridge or decoupling estimates directly into (5.2) or (6.2), preserving their product provenance, and test whether the integration over radii/frequencies cancels the near-degeneracy costs that defeat one-minor arguments.

## 11. Status ledger

- Full dimension- and matrix-independent density constant: **OPEN**.
- New target-level equivalence: **PROVED** — universal QFORM height equals the universal tent functional (5.4)/(5.5).
- Assigned fleet04/B15 partner result: **APPLIED WITH ZERO CONSTANT LOSS** through (7.1).
- Gaussian heat interpretation as a Maxwell average of centered small-ball ratios: **PROVED**.
- Conditional worst-cap shortcut: **quantitatively shown insufficient** via (8.1)-(8.3) whenever its expected cap diverges.
- Essential boundedness and continuity remain separate conclusions; this report proves the former from a uniform tent bound, not the latter from boundedness alone.
- No scheduler, notification, email/Drive, public-release, workflow, paid-model/API/Codex, or cross-account mutation was performed.
