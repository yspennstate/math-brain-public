# account03/B13 fixed-multiplicity audit r2 — hyperbolic and singular-kernel constants

Run: `20260924T123549Z-account03-B13-fixedmult-audit-r2`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned source blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned source SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Lens: B13 definite pairs, full hyperbolic envelope, exact identities and alternative derivations.

## Verdict

**PASS again for the mathematical 17-eigenvalue baseline.** I reread the complete pinned manuscript and found no new fatal defect. The projection-lemma wording repair from the preceding B13 audit remains nonfatal: after omitting rows with `b_i=0`, use `sum_{b_i>0}(1-b_i)<=d`. The repository-package mismatch (README names `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, `checks.json`, absent from the root listing inspected) remains a reproducibility gap, not a mathematical gap.

This run adds a rigorous quantitative improvement: the same proof establishes

\[
\boxed{\|p_{X^TAX+b^TX+c}\|_\infty<3110\,K^2/s}
\]

under the same hypothesis `s_17(A)>=s>0`, with all original quantifiers unchanged. No lower eigenvalue threshold is claimed.

## End-to-end dependency recheck

- **Lines 1–160 — PASS.** The theorem quantifiers, `K,s` scaling, Fourier normalization, Gaussian inversion and Riesz half-potential constants remain consistent.
- **Lines 161–320 — PASS with the already-recorded local projection wording repair.** Singular-value rank perturbation is correctly used for nonsymmetric auxiliaries; Schur spectral counting is on the original symmetric matrices; geometric Brascamp--Lieb and scalar Fourier powers retain original-coordinate product structure.
- **Lines 321–400 — PASS.** Two-copy decoupling and the regularized crossing determinant have the correct fourth-root exponent `-1/8`; `k=5` is integrable and `k=3` is used only with the half-Riesz weight.
- **Lines 401–540 — PASS, rederived below.** Scalar square, definite pair, hyperbolic pair and quarter-power concentration require no rotated-coordinate independence.
- **Lines 541–720 — PASS.** The sampled nonsymmetric interpolation has global rank at most `3r`, restricted rank at most `r`, and the `4k-3` spectral count is used in the correct direction. Random-cut multiplicity and pivot kernel arguments remain valid.
- **Lines 721–790 — PASS.** The main proof's branch counts and final scaling are unchanged. The global theorem asserts essential boundedness only; continuity is proved in the no-pivot Fourier branch, not globally.

## 1. Exact singular kernel identity and sharper envelope

The manuscript uses

\[
J(d)=\int_{-1}^1 |x|^{-1/2}|x-d|^{-1/2}\,dx.
\]

By the change `x -> -x`, `J(-d)=J(d)`, so take `d>0`.

For `0<d<=1`, splitting at `0,d` and using `x=d\sinh^2 t`, `x=d\sin^2\theta`, and `x=d\cosh^2t` gives the exact identity

\[
\boxed{
J(d)=2\operatorname{arsinh}(d^{-1/2})+\pi+2\operatorname{arcosh}(d^{-1/2}).
}
\]

For `d>=1`, the same substitutions give

\[
\boxed{
J(d)=2\operatorname{arsinh}(d^{-1/2})+2\arcsin(d^{-1/2}).
}
\]

For `z>=1`,

\[
\operatorname{arsinh}z+\operatorname{arcosh}z\le2\log(2z).
\]

Indeed, after exponentiating and putting `u=z^{-2}` this is exactly

\[
(1+\sqrt{1+u})(1+\sqrt{1-u})\le4,
\]

while `\sqrt{1+u}+\sqrt{1-u}<=2` and `\sqrt{1-u^2}<=1` prove it. Hence for `0<d<=1`,

\[
J(d)\le \pi+4\log2+2\log(1/d)<7+2\log(1/d).
\]

For `d>=1`, both inverse-hyperbolic/trigonometric terms decrease in `d`, and at `d=1` the value is `2\operatorname{arsinh}1+\pi<7`. Thus, without any case loss,

\[
\boxed{J(d)<7+2\log_+(1/|d|).}
\]

This improves the manuscript's `8+3 log_+` kernel bound.

## 2. Quarter-power concentration constant `16 -> 9/2`

In the off-diagonal branch of Lemma `quarter`, before the manuscript rounds the coefficient up to `16`, the exact Gaussian-smoothing coefficient is

\[
C_q=2^{5/8}\pi^{-1/4}e^{3/8}\Gamma(3/8).
\]

A completely elementary bound gives `C_q<9/2`.

First, on `[0,1]` the even fourth Taylor truncation is an upper bound for `e^{-x}`. On `[1,infinity)`, `x^{-5/8}<=1`. Therefore

\[
\begin{aligned}
\Gamma(3/8)
&< \frac83-\frac8{11}+\frac4{19}-\frac4{81}+\frac1{105}+e^{-1}\\
&< \frac83-\frac8{11}+\frac4{19}-\frac4{81}+\frac1{105}+\frac38\\
&=\frac{11779489}{4740120}<\frac52.
\end{aligned}
\]

Here `e>8/3` follows from the first four positive terms of its power series. Also

\[
2^{5/8}<\frac{31}{20},\qquad
\pi^{-1/4}<\frac{19}{25},\qquad
e^{3/8}<\frac32.
\]

The first follows by raising to the eighth power; the second follows from `pi>3>(25/19)^4`; and for the third, `e<11/4` follows by bounding the exponential-series tail geometrically, after which `(11/4)^3<(3/2)^8`. Consequently

\[
C_q<\frac{31}{20}\frac{19}{25}\frac32\frac52
=\frac{1767}{400}<\frac92.
\]

Thus the manuscript's concentration lemma strengthens to

\[
\boxed{
\mathbb P\{|R-a|<\rho\}
\le \min\left\{1,\frac92(\rho/L)^{1/4}\right\}.
}
\]

For `L>=1`, layer cake now gives

\[
\boxed{
\sup_a \mathbb E\log_+\frac1{|R-a|}
\le L_0^*:=4+4\log(9/2).
}
\]

No pointwise van-der-Corput estimate is used; this is the manuscript's integrated Gaussian-smoothing argument with its exact coefficient retained.

## 3. Hyperbolic pair constant retained exactly

The manuscript's hyperbolic parametrization gives on each branch, before rounding,

\[
\int_\mathbb R f_1(w_1(t))f_2(w_2(t))dt
\le \frac{15}{2}\log2+\log_+\frac{32}{\delta\Lambda}.
\]

The exact Jacobian is `1/(2 sqrt D)` and `Lambda>=2/sqrt D`, so the density envelope improves from leading constant `6` to

\[
\boxed{
 p_q(z)\le D^{-1/2}\left[
 \frac{15}{2}\log2+
 \log_+\frac{16\sqrt D}{|z-v|}
 \right].
}
\]

The coordinate used on the negative tail may differ from that used on the positive tail; both exist because `|u|=|w|=rho_0` in two dimensions. This is a clarification only, not an extra hypothesis.

## 4. Pivot half-potential improves from 600 to 310

Let `eta=1/100` as in the manuscript.

### Scalar pivot

Combining the sharper `J` envelope with `L_0^*` yields

\[
H(Q)\le 10\,[7+2L_0^*]
=10[15+8\log(9/2)]<278<310.
\]

The last elementary comparison uses `log(9/2)<8/5`, since the first four positive terms of `e^{8/5}` already exceed `9/2`.

### Definite pair

The unchanged exact estimate is

\[
H(Q)\le 40\pi<160<310.
\]

### Indefinite pair

Using the sharpened hyperbolic envelope and the manuscript's shifted log-kernel integral `<=8`,

\[
H(Q)\le D^{-1/2}\left[
 8+30\log2+4\log_+(16\sqrt D)
\right].
\]

For `D>=1/100`, write `y=sqrt D>=1/10`. The function

\[
\frac{8+30\log2+4\log(16y)}{y}
\]

is decreasing on this range because its derivative has numerator `4-[8+30log2+4log(16y)]<0`. Hence its maximum occurs at `y=1/10` and is

\[
10\,[8+30\log2+4\log(8/5)]<310.
\]

Here `log2<7/10` and `log(8/5)<1/2`, each following from short positive lower truncations of the exponential series.

Therefore Proposition `pivot-H` strengthens to

\[
\boxed{H(Q)<310.}
\]

## 5. Same 17-eigenvalue theorem with constant 3110

Under `s_9(A)>=1`, the pivot branch now has `H(Q)<310`, while the no-pivot branch still has the stronger full half-potential `<200`. Since the outside part of the full half-potential contributes at most one,

\[
\boxed{
\sup_a\mathbb E|Q-a|^{-1/2}<311.
}
\]

In the main theorem's scalar-pivot branch, `|A_ii|>=1/100` contributes a factor at most ten, so

\[
\|p_Q\|_\infty<3110.
\]

The other normalized branches stay below this: no pivot `<2400`, definite pair `<40`, and the indefinite-pair branch is much smaller (the new `L_0^*` only improves its old bound). Hence the identical proof and hypotheses establish

\[
\boxed{
\|p_{X^TAX+b^TX+c}\|_\infty<3110\,K^2/s
\qquad\text{whenever }s_{17}(A)\ge s>0.
}
\]

This is an improvement of the numerical constant only. It does not alter the manuscript's multiplicity threshold or continuity scope.

## 6. Threshold audit: why this does not prove `17 -> 13`

The interpolation mechanism at order four would require `4*4-3=13` large singular values and yields crossing-volume exponent exactly `k/4=1`. The resulting crude envelope is only `O(1/|t|)`, which is not absolutely integrable. The sharper B13 pair constants do not repair this in the no-pivot chamber because every principal two-coordinate determinant is `<eta`, so no determinant-uniform pair receiver is available there.

Thus the next genuine multiplicity improvement still needs a new order-four endpoint theorem exploiting product/quadratic structure beyond the scalar Fourier envelope, or an improved interpolation rank tradeoff. No theorem below seventeen is claimed in this run.

## Status

- 17-eigenvalue baseline: **PASS** in this independent B13 re-audit.
- New proved quantitative improvement: **3110 K^2/s** instead of `10000 K^2/s`, same hypotheses.
- Fatal mathematical defect: **none found**.
- Projection wording repair: **GAP, nonfatal and locally repairable**.
- Repository package mismatch: **GAP, reproducibility only**.
- Multiplicity below 17: **UNCHECKED/OPEN as a theorem; no reduction proved here**.
- Full three-eigenvalue conjecture: **OPEN**.
- Global continuity: **OPEN/not claimed**; no-pivot Fourier branch remains continuous.
