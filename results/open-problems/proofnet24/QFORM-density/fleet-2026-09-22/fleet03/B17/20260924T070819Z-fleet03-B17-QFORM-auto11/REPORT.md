# fleet03/B17 — Gaussian translation mixture rigidity and quantitative noncentral loss

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T070819Z-fleet03-B17-QFORM-auto11`  
Status: `NEW SUPPORTING THEOREM / PARTNER RESULT APPLIED / FULL TARGET OPEN`.

The unrestricted quadratic-form bounded-density conjecture remains OPEN. This report does **not** impose Gaussianity on the original target. It proves a no-go theorem for Gaussian/CLT witness mechanisms and applies a completed source-valid `fleet04/B17` witness to an explicit quantitative comparison.

No post-rotation independence for the original product law is used. No arbitrary-joint coarea theorem, conditional projection cap, pointwise law-uniform van der Corput bound, Monte Carlo histogram, compact-support reduction, or interval extremality claim is used.

## 1. Main theorem: arbitrary Gaussian translation cannot increase the density norm

### Theorem 1 (`QFORM-GAUSSIAN-TRANSLATION-MIXTURE-RIGIDITY-v1`)

Let `Z=(Z_1,...,Z_r)` have independent `N(0,1)` coordinates, let

\[
D=\operatorname{diag}(\lambda_1,\ldots,\lambda_r),
\qquad \delta\in\mathbb R^r,
\]

and define

\[
Q_\delta=\sum_{j=1}^r\lambda_j(Z_j+\delta_j)^2,
\qquad
Q_0=\sum_{j=1}^r\lambda_jZ_j^2.
\]

Assume `Q_0` has a bounded density `p_0`. Then `Q_delta` has a bounded density `p_delta` and

\[
\boxed{\|p_\delta\|_\infty\le \|p_0\|_\infty.}
\tag{1.1}
\]

More strongly, `p_delta` is a convex mixture of convolutions of `p_0` with probability measures.

### Proof

For each coordinate, the standard Poisson-mixture representation of a noncentral chi-square law gives

\[
(Z_j+\delta_j)^2\mid K_j=k
\ \stackrel d=\ \chi^2_{1+2k},
\qquad
K_j\sim\operatorname{Poisson}(\delta_j^2/2),
\]

with the `K_j` independent. Also

\[
\chi^2_{1+2k}\stackrel d=\chi^2_1+\chi^2_{2k},
\]

where the two terms on the right can be taken independent (and `chi^2_0=0`). Hence conditional on `K=(K_1,...,K_r)=k`,

\[
Q_\delta\stackrel d=Q_0+W_k,
\qquad
W_k=\sum_j\lambda_j\chi^2_{2k_j},
\]

with `Q_0` and `W_k` independent. Therefore

\[
p_\delta=\sum_{k\in\mathbb N^r}w_k\,(p_0*\mu_k),
\qquad w_k\ge0,\quad \sum_kw_k=1,
\]

where `mu_k` is the law of `W_k`. Young's probability-convolution inequality gives

\[
\|p_0*\mu_k\|_\infty\le\|p_0\|_\infty
\]

for every `k`, and averaging proves (1.1). `square`

### Coordinate-free Gaussian corollary

Let `X~N(m,Sigma)` with `Sigma` positive definite and let `A` be real symmetric. Put

\[
M=\Sigma^{1/2}A\Sigma^{1/2}.
\]

After whitening and orthogonally diagonalizing `M`, the linear term caused by `m` lies in `range(M)` because

\[
\Sigma^{1/2}Am=M\Sigma^{-1/2}m.
\]

Thus one can complete squares only in the nonzero spectral coordinates; null coordinates acquire no linear term. Up to an irrelevant deterministic output translation, `X^TAX` has exactly the form in Theorem 1. Consequently

\[
\boxed{
\|p_{X^TAX}\|_\infty
\le
\|p_{Z^TMZ}\|_\infty,
}
\tag{1.2}
\]

whenever the centered comparator on the right has a bounded density. In words: **for a fixed Gaussian covariance and fixed quadratic form, arbitrary noncentrality cannot make the output-density supremum larger than in the centered Gaussian case.**

This removes *all* fixed-mean Gaussian rank-three overshoot mechanisms at once, not merely translation along the minority-sign axis.

## 2. Quantitative strict loss for the `(1,1,-c)` chamber

Let

\[
G_j\sim N(\mu_j,s)\quad(j=1,2,3)
\]

independently, let `c>=1`, and set

\[
Q=G_1^2+G_2^2-cG_3^2,
\qquad
D=\frac{\mu_1^2+\mu_2^2+\mu_3^2}{s}.
\]

The centered comparator has global density norm

\[
C_0(c,s)=\frac1{2s\sqrt{1+c}}.
\tag{2.1}
\]

Indeed `G_1^2+G_2^2` is exponential with scale `2s`, `cG_3^2` has a decreasing density, and the difference convolution is maximized at zero; the elementary gamma integral gives (2.1).

The Poisson variables can be aggregated into

\[
K_+=K_1+K_2,
\qquad K_-=K_3.
\]

Their joint zero-event has exact probability

\[
\mathbb P(K_+=K_-=0)=e^{-D/2}.
\tag{2.2}
\]

If `K_+>=1`, then the positive part has a `Gamma(1+K_+,2s)` density. Since

\[
\operatorname{Gamma}(1+K_+,2s)
\stackrel d=
\operatorname{Gamma}(2,2s)+\operatorname{Gamma}(K_+-1,2s),
\]

convolution shows that its density cap is at most the shape-two cap

\[
\frac1{2es}.
\tag{2.3}
\]

If `K_+=0` and `K_->=1`, the magnitude of the negative part has a `Gamma(K_-+1/2,2cs)` density. Likewise it is a convolution of `Gamma(3/2,2cs)` with a probability law, so its density cap is at most

\[
\frac{e^{-1/2}}{\sqrt{2\pi}\,c s}
\le
\frac{e^{-1/2}}{\sqrt{2\pi}\,s}.
\tag{2.4}
\]

Since

\[
\frac1{2e}<\frac{e^{-1/2}}{\sqrt{2\pi}},
\]

every nonzero Poisson component has density norm at most

\[
C_1(s)=\frac{e^{-1/2}}{\sqrt{2\pi}\,s}.
\tag{2.5}
\]

Combining the zero component (2.1) with all nonzero components yields the explicit strict-loss envelope

\[
\boxed{
\|p_Q\|_\infty
\le
e^{-D/2}\frac1{2s\sqrt{1+c}}
+(1-e^{-D/2})\frac{e^{-1/2}}{\sqrt{2\pi}\,s}.
}
\tag{2.6}
\]

Equation (1.1) is still the sharper statement when the second constant exceeds `C_0`; equation (2.6) is useful near the sharp chamber `c≈1` because `C_1<C_0` there.

At the minimum-variance diffuse scale `s=1/12`, uniformly for every `c>=1`,

\[
C_1=\frac{12e^{-1/2}}{\sqrt{2\pi}}
=2.903648694229720\ldots .
\tag{2.7}
\]

For `D>=1/4`, using `C_0(c,1/12)<=3sqrt(2)`,

\[
\boxed{
\|p_Q\|_\infty
\le
3\sqrt2\,e^{-1/8}
+\frac{12e^{-1/2}}{\sqrt{2\pi}}(1-e^{-1/8})
=4.085304980540336\ldots .
}
\tag{2.8}
\]

## 3. Rigorous comparison with the completed partner `fleet04/B17` witness

The completed designated-partner theorem actually used here is

`QFORM-MACROFRAGMENTED-STRICTSLACK-DENSE-WITNESS-v1`,

source:

- repository `yspennstate/math-open-problems`;
- commit `4be63022324b82f254f1d7a4353a3e883f08d10a`;
- path `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B17/20260924T011922Z-fleet04-B17-QFORM-r6/REPORT.md`.

It constructs source-valid independent cap-one fragmented laws and exact entrywise-dense matrices with

\[
\operatorname{spec}_{\ne0}A_m=\{1,1,-(1+1/m)\}
\]

such that, at `theta=1/100`,

\[
\boxed{
\liminf_{m\to\infty}\|p_{Q_m}^{\rm partner}\|_\infty
\ge3\sqrt2\,e^{-3/100}
=4.117251705266084\ldots .
}
\tag{3.1}
\]

Now compare this to *every* noncentral Gaussian in the same `(1,1,-c_m)` spectral chamber at variance `s=1/12` with standardized noncentrality `D>=1/4`. Equation (2.8) gives

\[
\boxed{
\sup_{m\ge1}\sup_{D\ge1/4}
\|p_Q^{\rm Gaussian}(m,D)\|_\infty
\le4.085304980540336\ldots
<4.117251705266084\ldots
\le C_*.
}
\tag{3.2}
\]

Here `C_*` denotes any valid universal target constant. This is an actual inequality using the completed partner result, not merely a citation.

The strict comparison can be certified without floating-point arithmetic. Divide (2.8) by `3sqrt(2)` and set

\[
r=\frac{2e^{-1/2}}{\sqrt\pi}.
\]

Elementary bounds give

\[
r<\frac{69}{100},
\qquad
e^{-1/8}<\frac{883}{1000}.
\]

For the first: `e^{1/2}>41/25` from the first four positive terms of its Taylor series, while `sqrt(pi)>177/100`; hence `e^{1/2}sqrt(pi)>7257/2500>200/69`. For the second: `e^{1/8}>1+1/8+1/128=145/128>1000/883`. Therefore

\[
\frac{\text{left side of (2.8)}}{3\sqrt2}
<\frac{69}{100}+\frac{31}{100}\frac{883}{1000}
=0.96373.
\]

On the other hand

\[
e^{-3/100}>1-\frac3{100}=0.97.
\]

Thus the strict inequality in (3.2) is certified symbolically.

Interpretation: the partner's fragmented product witness retains more concentration than **any fixed noncentral Gaussian comparator with Mahalanobis squared displacement at least `1/4`**, despite having the same strict spectral chamber. Therefore a putative witness above `3sqrt(2)` cannot be explained by a fixed-mean Gaussian/CLT displacement mechanism.

## 4. Consequences for sharp-witness search

1. **Arbitrary Gaussian mean is harmless for the density norm.** The centered Gaussian is always worst among Gaussian translations at fixed covariance and quadratic form.
2. **The earlier minority-axis result was not special.** Off-axis and fully coupled mean shifts are covered by the same Poisson-mixture argument after whitening and spectral rotation.
3. **Quantitative noncentrality loses a definite amount near the sharp chamber.** At variance `1/12`, standardized displacement `D>=1/4` forces the explicit ceiling `4.08530498...`, below the partner's exact source-valid lower certificate `4.11725170...`.
4. Therefore the remaining witness frontier is a genuinely surviving non-Gaussian component, negative two-sheet structure not representable as fixed Gaussian noncentrality, several macroscopic shared rows, or interacting additional spectrum.

This does **not** prove the universal upper bound and does not show that `3sqrt(2)` is the sharp universal constant.

## 5. Continuity status

For the Gaussian class above, the centered rank-three comparator has a continuous density and every conditional Poisson component is a convolution with a probability law, so the noncentral Gaussian output also has a continuous density. This is a statement only about this Gaussian comparison class.

**Full-target continuity remains OPEN.**

## 6. Source/correction status

Control source read before the run: `yspennstate/math-research-brain@7c60b94f729b89142196f07dd26608c25f454723`; fresh prepublication main was later re-resolved and corrections refreshed. Required live corrections consumed include the failures of law-uniform pointwise quadratic-phase decay, unrestricted-joint coarea, conditional projection-cap moments, naive fiber-sup integration, post-rotation independence, and fixed fragment-count reductions. None is used here.

Execution status: `WITHOUT_VERIFIED_BRAIN`. Repository retrieval is genuine; no authenticated native learned-memory receiver-use event occurred.

**Full QFORM: OPEN / NOT PROVED / NOT DISPROVED.**
