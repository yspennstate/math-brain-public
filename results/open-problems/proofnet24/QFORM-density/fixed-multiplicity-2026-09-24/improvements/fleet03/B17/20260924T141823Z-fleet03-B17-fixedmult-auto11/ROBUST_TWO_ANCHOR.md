# fleet03/B17 — robust two-anchor extraction at the multiplicity-eight collar

Run: `20260924T141823Z-fleet03-B17-fixedmult-auto11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned baseline: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.  
Status: **PROVED SUPPORTING REDUCTION + SHARPENED EXACT-ZERO RECEIVER; multiplicity eight remains open.**

This note starts from the proved fleet03/B04 terminal-collar theorem for the no-pivot `s_8(A)>=1` chamber. It removes the previously stated aggregate-to-local obstruction: the two-sided collar actually forces one literal pair of original coordinates to have a dimension-free rank-two outside cross map. It then sharpens the exact-zero two-anchor receiver and closes that exact-zero subcase with a continuous density. Finally it combines the same anchor extraction with the order-two Schur half-potential mechanism to show that, for an invertible anchor, the moving logarithmic singularity is uniformly paid without selecting a tiny local minor. The only remaining local determinant singularity in that route is the nonlogarithmic pair term.

No Gaussian, moment, support, log-concavity, post-rotation independence, or law-uniform pointwise quadratic-phase decay assumption is used.

## 1. Input from the proved `s_8` terminal collar

Use the baseline parameters

\[
\eta=10^{-2},\qquad \kappa=80^{-2},\qquad
\varepsilon_*={3\sqrt2\over80}.
\]

The fleet03/B04 theorem says that in the no-`eta`-pivot chamber with `s_8(A)>=1`, either `V_3(A)>=kappa^3` (already paid by the third-volume density receiver), or else

\[
V_2(A)\ge\kappa^2
\]

and there is a determinant-squared family of **good** ordered disjoint two-set seeds `B=A[S,T]` carrying at least half of `V_2(A)`. To each good seed one may assign a disjoint two-set `H=H(B)` such that

\[
|\det A[S,H]\,\det A[H,T]|
\ge \delta_* |\det A[S,T]|,
\tag{1.1}
\]

where

\[
\delta_*
={97\over100}-{297\sqrt2+3\sqrt{202}\over4000}
=0.8543351401911337\ldots .
\tag{1.2}
\]

The same good-seed construction gives, on the seed complement, two diagonal interpolation defects of modulus at least `1-epsilon_*`, while the off-diagonal interpolation error has operator norm at most `epsilon_*`.

## 2. New robust-anchor extraction

For every two-set `H`, define

\[
D_H:=\sum_{\substack{U\subset[n]\setminus H\\|U|=2}}
       \det A[H,U]^2.
\tag{2.1}
\]

If `C_H=A[H,H^c]`, Cauchy--Binet gives

\[
D_H=\det(C_HC_H^T).
\tag{2.2}
\]

Also, by the definition of the disjoint order-two volume,

\[
\sum_H D_H=V_2(A).
\tag{2.3}
\]

For each `H`, let

\[
w_H:=\sum_{\substack{B=(S,T)\ {m good}\\H(B)=H}}
       \det A[S,T]^2.
\tag{2.4}
\]

Since good seeds carry at least half the determinant-squared sampling mass,

\[
\sum_H w_H\ge {1\over2}V_2(A)={1\over2}\sum_H D_H.
\tag{2.5}
\]

Hence there exists at least one literal two-set `H_*` for which

\[
w_{H_*}\ge {1\over2}D_{H_*}.
\tag{2.6}
\]

For this same `H_*`, square (1.1) and sum over its assigned good seeds. The resulting terms are a subset of

\[
\Xi_{H_*}:=
\sum_{\substack{S,T\subset H_*^c,\ |S|=|T|=2\\S\cap T=\varnothing}}
\det A[H_*,S]^2\det A[H_*,T]^2.
\]

Thus

\[
\delta_*^2 w_{H_*}\le\Xi_{H_*}.
\tag{2.7}
\]

On the other hand, dropping the restriction `S cap T=emptyset` only enlarges the nonnegative sum, so

\[
\Xi_{H_*}\le
\left(\sum_{S\subset H_*^c,|S|=2}\det A[H_*,S]^2\right)^2
=D_{H_*}^2.
\tag{2.8}
\]

Combining (2.6)--(2.8) gives

\[
\boxed{
D_{H_*}=\det(C_{H_*}C_{H_*}^T)
\ge {\delta_*^2\over2}
=0.3649442658827020\ldots
}
\tag{2.9}
\]

and simultaneously

\[
\boxed{
 w_{H_*}\ge {\delta_*^2\over4}
=0.1824721329413510\ldots .
}
\tag{2.10}
\]

This is the main structural improvement. The `s_8` terminal collar is **not** merely an aggregate `Xi_2/Omega_1` packet: it contains one actual pair of original coordinates whose outside `2 x (n-2)` cross map has row rank two and singular-value product at least

\[
\sqrt{D_{H_*}}\ge {\delta_*\over\sqrt2}
=0.6041061710351104\ldots .
\tag{2.11}
\]

Because the ambient branch has no `eta`-pivot, its physical self-block

\[
K_*:=A[H_*,H_*]
\]

still satisfies `|A_hh|<eta` on both diagonal entries and `|det K_*|<eta`. Thus multiplicity eight has been reduced to a **single robust-cross / small-self-curvature two-anchor chamber**, with no dimension-dependent aggregate-to-local loss.

### Why (2.9) was not automatic from a single local collar

A lower bound on one product `|det A[H,S] det A[H,T]|` is not forced dimension-independently. The point is instead to normalize the assigned good-seed mass by the identity `sum_H D_H=V_2`. Equation (2.5) supplies an `H` with `w_H/D_H>=1/2`, and only then does the two-sided collar force `D_H` itself to be order one. This avoids paying the reciprocal of a tiny individual minor.

## 3. Sharpened exact-zero two-anchor affine receiver

The following improves the front constant in the previously completed exact-zero receiver and is self-contained from the baseline product-projection lemma.

### Theorem `QFORM-EXACT-ZERO-TWO-ANCHOR-SHARPENED-v1`

Let `H={h_1,h_2}` be two literal original coordinates, let all original coordinates be independent with densities bounded by one, and write

\[
Q=X^TAX+b^TX+c.
\]

Assume

\[
A[H,H]=0,
\qquad C=A[H,H^c],
\qquad D_H:=\det(CC^T)>0.
\]

Then `Q` has a bounded **continuous** density and

\[
\boxed{
\|p_Q\|_\infty
\le \sqrt{2\pi e}\,D_H^{-1/4}.
}
\tag{3.1}
\]

The numerical front constant is

\[
\sqrt{2\pi e}=4.132731354122493\ldots,
\]

improving the previous `e sqrt(2 pi)=6.813722...` by the exact factor `sqrt(e)`.

#### Proof

Put `Y=X_{H^c}`. Since the anchor block is zero,

\[
Q=R(Y)+2X_H\cdot L(Y),
\qquad L(Y)=CY+b_H/2,
\tag{3.2}
\]

where `R` is an arbitrary quadratic-affine function of `Y`.

Condition on `Y`. If `l=L(Y)`, then the density of

\[
2(l_1X_{h_1}+l_2X_{h_2})
\]

is bounded by

\[
{1\over2\max(|l_1|,|l_2|)}
\le {1\over\sqrt2\,|l|}.
\tag{3.3}
\]

Indeed, choose the larger coefficient; its scaled one-dimensional density has the first cap, and convolution with the other independent coordinate cannot increase an `L^infinity` norm.

Let `G=CC^T` and `U=G^{-1/2}C`. Then `UU^T=I_2`. The baseline two-dimensional product-projection lemma gives `UY` a density bounded by `e`. Since

\[
L=G^{1/2}(UY)+b_H/2,
\]

`L` has a two-dimensional density bounded by

\[
M={e\over\sqrt{\det G}}={e\over\sqrt{D_H}}.
\tag{3.4}
\]

For any two-dimensional probability density bounded by `M`, layer cake (equivalently the bathtub principle for the decreasing radial kernel) gives

\[
\mathbb E|L|^{-1}
\le\int_0^\infty\min\{1,\pi M/t^2\}\,dt
=2\sqrt{\pi M}.
\tag{3.5}
\]

Average the conditional density domination (3.3):

\[
\|p_Q\|_\infty
\le {1\over\sqrt2}\mathbb E|L|^{-1}
\le \sqrt{2\pi M}
\le\sqrt{2\pi e}\,D_H^{-1/4}.
\]

For continuity, the exceptional sets `L_1=0` or `L_2=0` have probability zero because `L` has a two-dimensional density. Otherwise the conditional output density in (3.2) is the convolution of two scaled `L^1` densities, hence is continuous. The integrable majorant `(sqrt2 |L|)^{-1}` from (3.3)--(3.5) permits dominated convergence after the random shift `R(Y)`. Thus the averaged density is continuous. QED.

### Exact-zero `s_8` terminal corollary

If the robust pair `H_*` from Section 2 happens to satisfy `A[H_*,H_*]=0`, then (2.9) and (3.1) give

\[
\boxed{
\|p_Q\|_\infty
\le \sqrt{2\pi e}\left({\delta_*^2\over2}\right)^{-1/4}
<5.318.
}
\tag{3.6}
\]

This is a continuous-density conclusion for that exact-zero endpoint.

## 4. The same robust pair pays the aggregate/local part of the nonzero Schur logarithm

This section records a useful consequence when `K_*=A[H_*,H_*]` is invertible. It does **not** finish the near-singular pair endpoint.

Let

\[
D:=|\det K_*|>0,
\qquad
\gamma_*:=1-2\varepsilon_*
=1-{3\sqrt2\over40}
=0.8939339828220179\ldots .
\tag{4.1}
\]

For every good seed `B=A[S,T]` assigned to `H_*`, the good-seed completion has

\[
K_*-A[H_*,T]B^{-1}A[S,H_*]
\]

with both diagonal defect magnitudes at least `1-epsilon_*` and off-diagonal defect magnitude at most `epsilon_*`. Therefore its determinant has modulus at least `gamma_*`. The block determinant identity gives

\[
|\det A[S\cup H_*,T\cup H_*]|
\ge\gamma_*|\det B|.
\tag{4.2}
\]

Pivoting instead on the invertible principal pair `K_*`, with Schur complement `S_*`, gives

\[
\det A[S\cup H_*,T\cup H_*]
=\det K_*\,\det S_*[S,T].
\]

Hence

\[
|\det S_*[S,T]|
\ge {\gamma_*\over D}|\det B|.
\tag{4.3}
\]

Summing (4.3)^2 over the assigned seeds and using (2.10),

\[
V_2(S_*)
\ge {\gamma_*^2\over D^2}w_{H_*}
\ge {\gamma_*^2\delta_*^2\over4D^2}.
\tag{4.4}
\]

The fair physical coordinate cut therefore has some order-two crossing with

\[
E_2\ge {1\over16}V_2(S_*)
\ge {\gamma_*^2\delta_*^2\over64D^2}.
\tag{4.5}
\]

Apply the completed marginal-free order-two half-potential receiver with

\[
C_2=8\sqrt e\,2^{-1/8}=12.095072570796\ldots .
\]

The Schur critical value `R_*` satisfies

\[
\boxed{
\sup_a\mathbb E|R_*-a|^{-1/2}
\le 2^{3/4}C_2(\gamma_*\delta_*)^{-1/4}D^{1/4}.
}
\tag{4.6}
\]

Thus the half-potential gains exactly the quarter power of the small pair determinant needed to neutralize the logarithmic hyperbolic singularity. Combining the baseline hyperbolic envelope

\[
p_Q(z)\le D^{-1/2}
\left[6+\mathbb E\log_+{16\sqrt D\over|z-R_*|}\right]
\]

with the elementary potential-to-log estimate

\[
\mathbb E\log_+{16\sqrt D\over|z-R_*|}
\le8D^{1/4}\sup_a\mathbb E|R_*-a|^{-1/2}
\]

gives

\[
\boxed{
 p_Q(z)
\le 6D^{-1/2}+174.076
}
\tag{4.7}
\]

for almost every `z` (the displayed decimal rounds upward from `174.0754526...`).

The structural point is stronger than the constant: **neither the moving logarithmic critical value nor aggregate-to-local dilution remains an obstruction for this selected robust pair.** The sole determinant-singular term left by this route is the nonlogarithmic `6D^{-1/2}` term.

## 5. Precise remaining multiplicity-eight endpoint

Combining Sections 2--4 with the existing `V_3` branch gives the following reduction.

In the only unpaid no-pivot `s_8(A)>=1` chamber, there is a literal two-coordinate pair `H_*` satisfying

\[
\det(A[H_*,H_*^c]A[H_*,H_*^c]^T)
\ge0.3649442658\ldots,
\tag{5.1}
\]

while its principal self-block obeys the no-pivot bounds

\[
|A_{hh}|<10^{-2},\qquad |\det A[H_*,H_*]|<10^{-2}.
\tag{5.2}
\]

Moreover the same pair carries good-seed mass `w_H>=0.1824721329...`. If its self-block is exactly zero, the density is continuously bounded by `<5.318`. If the self-block is invertible, the logarithmic Schur singularity is already uniformly paid; only the nonlogarithmic determinant tail in (4.7) can still diverge as `det K_* ->0`. Singular nonzero rank-one self-blocks belong to the same remaining near-singular endpoint.

Therefore a multiplicity-eight proof no longer needs to solve a dimension-diffuse `Xi_2` selection problem. It needs a **uniform near-singular two-anchor receiver** for a pair with the fixed robust cross determinant (5.1), or an equivalent argument that removes/interpolates the nonlogarithmic `D^{-1/2}` term through `D=0` while retaining arbitrary rough product inputs and arbitrary complement curvature.

This note does not claim multiplicity eight, and it does not change the status of the unrestricted three-eigenvalue conjecture.
