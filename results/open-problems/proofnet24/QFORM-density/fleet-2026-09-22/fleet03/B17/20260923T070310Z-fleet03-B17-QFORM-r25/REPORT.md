SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B17, 2026-09-23T07:03:10Z.
attacking: nonzero-mean Gaussian and translated rotated-bank witnesses; determine whether affine CLT structure can exceed the 3 sqrt(2) obstruction.

# Affine Gaussian ceiling: nonzero means cannot beat `3 sqrt(2)`

## Status and scope

This report proves a sharp supporting theorem for **all Gaussian quadratic forms with arbitrary mean** under a covariance floor, then gives an exact translated version of the completed rotated cap-one partner witness. It closes the affine/nonzero-mean Gaussian-surrogate loophole left by the preceding centered-Gaussian theorem.

It does **not** prove the full arbitrary-input QFORM conjecture. The universal density upper bound for arbitrary independent cap-one inputs remains open, and the requested full-target continuity conclusion remains open.


The centered Gaussian theorem used below is worker-owned prior result
`yspennstate/math-open-problems@9ccec4009fa3289188c7bd7344b299cab3be56ce`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B17/20260923T060210Z-fleet03-B17-QFORM-r24/REPORT.md`.

The designated completed partner result actually applied below is
`fleet04/B17`, `yspennstate/math-open-problems@2156b76156ad5956c214a881fcfd6d977d6f3b9f`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B17/20260922T211900Z-fleet04-B17-QFORM-r3/REPORT.md`.

---

## 1. Main theorem: arbitrary Gaussian mean does not increase the sharp ceiling

### Theorem 1 (sharp affine-Gaussian QFORM ceiling)

Let
\[
G\sim N(\mu,\Sigma)\quad\text{in }\mathbb R^n,
\qquad \Sigma\succeq \sigma^2 I_n,
\qquad \sigma>0.
\]
Let `A=A^T` have at least three eigenvalues of absolute value at least `1`, equivalently `s_3(A)>=1`. Then
\[
Q_G=G^T A G
\]
has a bounded continuous density and
\[
\boxed{
\|p_{Q_G}\|_\infty\le {1\over 2\sqrt2\,\sigma^2}.
}
\]
The constant is sharp. Equality is attained in rank three by
\[
\mu=0,\qquad \Sigma=\sigma^2I_3,
\qquad A=\operatorname{diag}(1,1,-1),
\]
up to orthogonal conjugacy and global sign reversal.

At the density-one variance floor `sigma^2=1/12`,
\[
\boxed{\|p_{Q_G}\|_\infty\le3\sqrt2.}
\]

### Proof

Write
\[
G=\mu+\Sigma^{1/2}Z,\qquad Z\sim N(0,I_n),
\]
and put
\[
B=\Sigma^{1/2}A\Sigma^{1/2},
\qquad m=\Sigma^{-1/2}\mu.
\]
As in the centered theorem,
\[
s_3(B)\ge\sigma^2s_3(A)\ge\sigma^2.
\]
Choose an orthogonal `O` with
\[
OBO^T=\operatorname{diag}(\beta_1,\ldots,\beta_n).
\]
Since `W=OZ` is again a vector of independent standard normals and `a=Om`,
\[
Q_G\stackrel d=\sum_{j=1}^n\beta_j(W_j+a_j)^2.
\]
At least three coefficients `beta_j` have magnitude at least `sigma^2`; select any such three and denote their contribution by `T_a`.

For one coordinate,
\[
(W+a)^2\sim\chi^2_1(a^2).
\]
The noncentral chi-square law has the exact Poisson mixture
\[
\chi^2_1(a^2)\mid N=k\sim\chi^2_{1+2k},
\qquad N\sim\operatorname{Poisson}(a^2/2).
\]
By central chi-square additivity,
\[
\chi^2_{1+2k}\stackrel d=\chi^2_1+\chi^2_{2k}
\]
with the two terms independent. Therefore, conditional on the three Poisson counts `K=(k_1,k_2,k_3)`,
\[
T_a\stackrel d=T_0+R_K,
\]
where
\[
T_0=\beta_1Z_1^2+\beta_2Z_2^2+\beta_3Z_3^2
\]
is the centered strong triple and `R_K` is independent of `T_0`. Hence
\[
p_{T_a}
=\sum_K w_K\,(p_{T_0}*\nu_K),
\]
where `w_K` are the Poisson product weights and `nu_K` are probability laws. Young's inequality gives
\[
\|p_{T_a}\|_\infty
\le\|p_{T_0}\|_\infty.
\]
The centered theorem proved in the preceding B17 run gives
\[
\|p_{T_0}\|_\infty
\le {1\over2\sqrt2\,\sigma^2}
\]
for every sign pattern, with the stronger same-sign estimate
`1/(sqrt(2 pi e) sigma^2)`.

All remaining coordinates contribute a random variable independent of the selected triple. Convolution with that residual law cannot increase the density supremum, proving the displayed bound for the full form.

For continuity, the centered three-mode density is in `C_0(R)` by the preceding theorem. Each conditional density `p_{T_0}*nu_K` is therefore also in `C_0(R)` with common sup bound. The Poisson mixture converges uniformly because its tail total mass tends to zero, so `p_{T_a}` lies in `C_0(R)`. Convolution with the independent residual probability law preserves `C_0(R)`. Thus the full Gaussian quadratic form has a bounded continuous density.

Sharpness is the centered isotropic `(2,1)` example already identified in the preceding run. `square`

---

## 2. Density-one consequence: even affine matching-Gaussian surrogates are capped by `3 sqrt(2)`

If a probability density satisfies `0<=f<=1` and has finite variance, the sharp bathtub argument gives
\[
\operatorname{Var}(X)\ge {1\over12}.
\]
Hence for independent cap-one inputs with finite second moments, their matching Gaussian
\[
G\sim N(\mathbb EX,\operatorname{diag}(\operatorname{Var}X_i))
\]
has covariance at least `I/12`. Theorem 1 therefore yields
\[
\boxed{
\|p_{G^TAG}\|_\infty\le3\sqrt2
}
\]
for every symmetric `A` with three eigenvalues of magnitude at least one.

This is stronger than the previous centered-surrogate statement: **nonzero means cannot raise the Gaussian endpoint above `3 sqrt(2)` either.** Thus any source-valid witness above the current lower-bound obstruction must exploit genuinely non-Gaussian finite-scale structure, not merely affine CLT structure.

---

## 3. Exact quantitative cone-tip penalty for a nonzero Gaussian mean

For the sharp isotropic signature, let
\[
Q_h=(h_1+\sqrt v Z_1)^2+(h_2+\sqrt v Z_2)^2-(h_3+\sqrt v Z_3)^2,
\qquad v>0.
\]
Put
\[
\delta_+={h_1^2+h_2^2\over v},
\qquad \delta_-={h_3^2\over v},
\qquad \Delta={\|h\|^2\over v}.
\]
Then, writing the positive noncentral chi-square as `chi^2_2(delta_+)` and the negative one as `chi^2_1(delta_-)`, the Poisson mixture gives
\[
p_{Q_h}(0)
={1\over v}\sum_{k,l\ge0}w_{k,l}d_{k,l}(0),
\]
where
\[
d_{k,l}(0)=
{\Gamma(k+l+1/2)\over
2^{k+l+3/2}k!\,\Gamma(l+1/2)}.
\]
Since `d_{0,0}(0)=1/(2 sqrt(2))`, define
\[
r_{k,l}={d_{k,l}(0)\over d_{0,0}(0)}
={\Gamma(k+l+1/2)\over2^{k+l}k!\Gamma(l+1/2)}.
\]
Then
\[
r_{0,0}=1,
\qquad
\sup_{(k,l)\ne(0,0)}r_{k,l}={1\over2}.
\]
For `l=0,k>=1`, the maximum is already below `1/2`. For `l>=1`, `r_{k,l}/sqrt(2)` is the pmf of a negative-binomial random variable with shape `l+1/2` and success probability `1/2`; decomposing that law as the convolution of the `3/2`-shape law with another probability law shows its maximal atom is at most `2^{-3/2}`, giving `r_{k,l}<=1/2`. Equality occurs at `(k,l)=(0,1)`.

The probability of the zero Poisson pair is `exp(-Delta/2)`. Therefore
\[
\boxed{
{p_{Q_h}(0)\over p_{Q_0}(0)}
\le {1+e^{-\Delta/2}\over2}.
}
\]
Equivalently,
\[
\boxed{
p_{Q_h}(0)
\le{1\over2\sqrt2\,v}
{1+e^{-\|h\|^2/(2v)}\over2}.}
\]
At the density-one variance floor `v=1/12`,
\[
\boxed{
p_{Q_h}(0)
\le3\sqrt2\,{1+e^{-6\|h\|^2}\over2}.}
\]
Thus every fixed nonzero active mean gives a strict quantitative loss at the cone tip.

In fact the **full** density supremum is also strictly below the centered maximum for nonzero `h` in this exact rank-three isotropic model. The centered density has a unique maximizer at zero: on the positive side this follows from the exact exponential factor of the `chi^2_2` density, and on the negative side from strict monotonicity of the `chi^2_1` density. Every nonzero Poisson component is a convolution of that centered density with a nondegenerate continuous law, so its sup is strictly smaller. The countable Poisson mixture belongs to `C_0` and has pointwise value strictly below the centered maximum; hence it attains a strictly smaller global maximum.

---

## 4. Exact genuinely rotated translated cap-one stress family

Apply the completed `fleet04/B17` construction. Let
\[
J=\operatorname{diag}(1,1,-1),
\qquad
O={1\over7}\begin{pmatrix}
6&-2&-3\\
-2&3&-6\\
-3&-6&-2
\end{pmatrix},
\]
let `v_j=Oe_j`, repeat the physical row `v_j/sqrt(m)` for `k=1,...,m`, and set
\[
A_m=R_mJR_m^T.
\]
Then the exact nonzero spectrum of `A_m` is `{1,1,-1}` and the bank-level matrix is
\[
B=O^TJO={1\over49}\begin{pmatrix}
31&-36&-12\\
-36&-23&-24\\
-12&-24&41
\end{pmatrix},
\]
with every entry nonzero.

Fix any `h in R^3`, put `b=O^Th`, and replace the centered partner inputs by the shifted cap-one laws
\[
X_{jk}^{(m,h)}\sim\operatorname{Unif}
\left[-{1\over2}+{b_j\over\sqrt m},
       {1\over2}+{b_j\over\sqrt m}\right],
\]
independently over `j,k`. Every finite input density is still exactly one on a set of length one. The normalized bank variables are
\[
Y_{mj}=b_j+{1\over\sqrt m}\sum_{k=1}^mU_{jk},
\]
so
\[
Q_m^{(h)}=Y_m^TBY_m=(OY_m)^TJ(OY_m).
\]
The translated version of the partner's weighted local Edgeworth expansion is literal translation of its one-dimensional bank density. Inserting it into the same rank-three coarea parametrization gives, for fixed `h`,
\[
p_{Q_m^{(h)}}(0)\longrightarrow p_{Q_h}(0),
\]
where
\[
Q_h=(h_1+\sqrt{1/12}Z_1)^2
+(h_2+\sqrt{1/12}Z_2)^2
-(h_3+\sqrt{1/12}Z_3)^2.
\]
Consequently
\[
\boxed{
\limsup_{m\to\infty}p_{Q_m^{(h)}}(0)
\le3\sqrt2\,{1+e^{-6\|h\|^2}\over2}.
}
\]
For every fixed nonzero `h`, this is strictly below `3 sqrt(2)`. Thus a fixed mesoscopic translation of the three diffuse rotated banks cannot improve the sharp lower-bound mechanism; it damages the cone-tip peak.

For `h=0`, the partner proves the stronger finite expansion
\[
\boxed{
p_{Q_m^{(0)}}(0)
=3\sqrt2\left(1-{5295\over21952m}+O(m^{-2})\right),}
\]
so the centered exact cap-one rotated family still saturates the affine-Gaussian ceiling.

This is the required application of a completed partner result to an actual inequality: partner saturation gives the lower endpoint `C_universal>=3 sqrt(2)`, while Theorem 1 proves that the **entire arbitrary-mean Gaussian surrogate class** cannot exceed the same number.

---

## 5. Sharp-witness consequences

1. **Affine Gaussian endpoints are exhausted.** Covariance anisotropy, arbitrary Gaussian means, and arbitrary extra independent Gaussian quadratic modes cannot beat `3 sqrt(2)` once the covariance floor `Sigma>=I/12` is respected.

2. **The known obstruction is genuinely centered.** In the exact isotropic rank-three sharp model, every nonzero active Gaussian mean strictly lowers the global density maximum; at zero there is the explicit factor `(1+exp(-6||h||^2))/2`.

3. **Translated diffuse cap-one banks do not produce a stronger lower bound.** The exact rotated partner matrices remain source-valid under `O(m^{-1/2})` physical interval translations, but every fixed nonzero limiting bank mean loses cone-tip density.

4. **What remains for B17.** A witness above `3 sqrt(2)`, if one exists, must exploit a genuinely non-Gaussian finite-scale or multiscale mechanism: e.g. fragmented laws whose local limit is not governed solely by mean/covariance, mesoscopic rows that survive outside a Gaussian block, or a compound-Poisson/multiscale shared-coordinate structure. The next B17 mechanism should target such a non-Gaussian construction rather than another Gaussian surrogate.

---

## 6. Scope of continuity

Theorem 1 proves a bounded continuous density for the complete affine-Gaussian class. The finite translated partner family also has continuous density for the same `m>=3` scope as the partner's local Edgeworth/coarea proof. **The full arbitrary-input QFORM continuity conclusion remains open.**

Status: supporting theorem proved; full QFORM OPEN / NOT PROVED. Repository transport is genuine, but no authenticated native brain receiver-use event occurred in this run, so status remains `WITHOUT_VERIFIED_BRAIN`.
