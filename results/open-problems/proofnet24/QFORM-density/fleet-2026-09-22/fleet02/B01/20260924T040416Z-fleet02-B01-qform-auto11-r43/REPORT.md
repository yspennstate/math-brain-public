SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B01, 2026-09-24T04:04:16Z.
attacking: the heavy-star endpoint by pairing one literal star edge with the remaining independent star tail and spending their joint L2 frequency gain through half-Riesz.

# fleet02/B01 — heavy-star edge/tail half-Riesz compiler

Programme: `QFORM-DENSITY-3EIG-20260922`.

Status: **NEW SUPPORTING THEOREM / ESSENTIAL STEP APPLIED / FULL QFORM OPEN**.

All variables below are literal original-coordinate variables. No independence after rotation is used. No Gaussianity, moments, support regularity, log-concavity, compactness, connectedness or identical-law assumption is introduced. The phase-aligned fragmented-support counterexample to law-uniform scalar quadratic-phase decay remains in force.

## 1. Input from the preceding finite-leak reduction

The preceding fleet02/B01 run reduced the exact-`W_2`, diagonal-plus-rank-two finite-leak endpoint to three local normal forms. One of them is a residual diagonal-plus-star after a literal outer scalar completion

\[
Q=a(X_0+h)^2+R,\qquad a\ne0,
\]

where, for an original hub `H` and original leaves, the quadratic part of `R` is diagonal except for the hub-to-leaf star. The earlier mixed-Fresnel theorem paid this star only when every normalized slope leverage was at most `1/2`. The first unpaid case was therefore a star with one heavy physical leaf.

The theorem below removes that leverage gate whenever the heavy edge and the remaining tail are both nonzero.

## 2. Theorem `QFORM-STAR-EDGE-TAIL-HALFRIESZ-v1`

Let `H,U,Y_1,...,Y_m` be independent original coordinates, each with a probability density bounded by one. Let

\[
\begin{aligned}
R={}&dH^2+eU^2+2\beta HU
 +\sum_{i=1}^m\bigl(d_iY_i^2+2c_iHY_i\bigr)\\
&+\ell_HH+\ell_UU+\sum_i\ell_iY_i+q_0,
\end{aligned}
\tag{2.1}
\]

where `beta != 0`. Put

\[
C=\left(\sum_i c_i^2\right)^{1/2}.
\]

If `C>0`, then

\[
\boxed{
H_{1/2}(R):=\sup_s\mathbb E|R-s|^{-1/2}
\le 2^{21/8}(|\beta|C)^{-1/4}.
}
\tag{2.2}
\]

Consequently, if a further independent original coordinate admits the exact scalar completion

\[
Q=a(X_0+h(H,U,Y))^2+R,
\qquad a\ne0,
\tag{2.3}
\]

then the law of `Q` has a density satisfying

\[
\boxed{
\|p_Q\|_\infty
\le 2^{21/8}|a|^{-1/2}(|\beta|C)^{-1/4}.
}
\tag{2.4}
\]

There is no leverage condition on the tail vector `c`, and arbitrary diagonal quadratic twists and affine terms are retained.

### Proof

Fix `t != 0` and condition only through the literal hub variable `H=h`. Split the conditional characteristic function into the singled-out heavy edge and the remaining tail:

\[
F_t(h)=\mathbb E_U
 e^{it(eU^2+2\beta hU+\ell_UU)},
\tag{2.5}
\]

\[
G_t(h)=\prod_i\mathbb E_{Y_i}
 e^{it(d_iY_i^2+2c_i hY_i+\ell_iY_i)}.
\tag{2.6}
\]

The hub-only terms have modulus one. Since `f_H<=1`,

\[
|\phi_R(t)|
\le\int_{\mathbb R}|F_t(h)G_t(h)|\,dh
\le\|F_t\|_2\|G_t\|_2.
\tag{2.7}
\]

For `g_U(u)=f_U(u)e^{it(eu^2+\ell_Uu)}`, (2.5) is the Fourier transform of `g_U` evaluated at `2\beta th`. Plancherel and `\int f_U^2<=1` give

\[
\boxed{
\|F_t\|_2^2\le\frac{\pi}{|\beta t|}.
}
\tag{2.8}
\]

For the tail put `alpha_i=c_i^2/C^2` on the nonzero `c_i`; then `sum alpha_i=1`. Hölder, followed by the pinned cap-one Fourier `L^p` lemma with `p_i=2/alpha_i>=2`, gives

\[
\begin{aligned}
\|G_t\|_2^2
&=\int\prod_i |G_{i,t}(h)|^2\,dh\\
&\le\prod_i
\left(\int|G_{i,t}(h)|^{2/\alpha_i}\,dh\right)^{\alpha_i}\\
&\le\prod_i
\left[
 \frac1{2|tc_i|}\frac{4\pi}{\sqrt{2/\alpha_i}}
\right]^{\alpha_i}\\
&=\boxed{\frac{\sqrt2\,\pi}{|t|C}}.
\end{aligned}
\tag{2.9}
\]

Here the diagonal phases `d_iY_i^2` are harmless unimodular twists, exactly as in the pinned Fourier report. Combining (2.7)--(2.9),

\[
\boxed{
|\phi_R(t)|
\le
\min\left\{1,
2^{1/4}\pi (|\beta|C)^{-1/2}|t|^{-1}
\right\}.
}
\tag{2.10}
\]

This is the needed averaged-frequency replacement: the critical `1/|t|` comes from two independent physical slope resources jointly and is not a scalar stationary-phase assertion.

Now apply the proved fractional-potential interface from the required `20260922T211500Z` Fourier report:

\[
H_{1/2}(R)
\le(2\pi)^{-1/2}
\int_{\mathbb R}|t|^{-1/2}|\phi_R(t)|\,dt.
\tag{2.11}
\]

For every `K>0`,

\[
\int_{\mathbb R}|t|^{-1/2}\min(1,K/|t|)\,dt=8\sqrt K.
\tag{2.12}
\]

Taking `K=2^{1/4}\pi(|\beta|C)^{-1/2}` in (2.11) gives exactly

\[
H_{1/2}(R)
\le2^{21/8}(|\beta|C)^{-1/4},
\]

which is (2.2). The same pinned report's exact square peel

\[
\|p_Q\|_\infty\le|a|^{-1/2}H_{1/2}(R)
\]

gives (2.4). `square`

## 3. Full-target stress family: the previous leverage gate fails, the new theorem pays

Take independent cap-one variables `(X_0,H,U,V)` and

\[
Q_*=X_0^2+2H\left(U+\frac12V\right).
\tag{3.1}
\]

Its coefficient matrix has spectrum

\[
\left\{-\frac{\sqrt5}{2},\ 0,\ 1,\ \frac{\sqrt5}{2}\right\},
\tag{3.2}
\]

so it has exactly three eigenvalues of modulus at least one. The star slope vector is `(1,1/2)`, whose heavy-coordinate leverage is

\[
\frac{1}{1+1/4}=\frac45>\frac12.
\]

Thus the preceding diffuse-star mixed-Fresnel theorem is unavailable. In Theorem 2 take

\[
a=1,\qquad \beta=1,\qquad C=\frac12.
\]

Then

\[
\boxed{
\|p_{Q_*}\|_\infty
\le2^{23/8}
=7.3360323456\ldots .
}
\tag{3.3}
\]

This is a genuine full-target family and the estimate is uniform over every admissible product law.

The required volume mechanisms are genuinely blind here. Every original-coordinate cross block of the star plus the independent outer diagonal has rank at most one, hence on every cut

\[
e_3(M^TM)=e_5(M^TM)=0.
\tag{3.4}
\]

Therefore D, D' and D5 have exactly zero currency on (3.1), whereas the pinned `L^p` Fourier lemma plus fractional-potential/square-peel interface gives (3.3).

## 4. Newest fleet03/B01 theorem: actual application and actual obstruction

The newest designated-partner result consumed in this run is fleet03/B01 `QFORM-TWO-HUB-ONE-SIDED-ENTANGLED-LR-v1`. At `r=2`, for two original hubs with row-rank-two slope matrix `B`, an arbitrary same-bank measurable phase, and a one-sided-entangled hyperbolic residual edge `2cUV`, it proves

\[
\|p_Q\|_\infty
<3.572\,\det(BB^T)^{-1/6}|c|^{-1/3}.
\tag{4.1}
\]

Its checked six-coordinate example has spectrum approximately

\[
\{-1.53209,-1,-0.347296,1,1,1.87939\},
\]

so it is target-valid, and (4.1) gives `||p_Q||_infinity<3.572` for every cap-one product input law. Thus the partner theorem is an actual paid full-target packet, not merely a cited summary.

It does not by itself close the support-two isotropic finite-leak arrowhead from the preceding fleet02/B01 normal form: that arrowhead has only one aggregate two-hub slope direction, so its `2 x m` slope matrix has row rank one and

\[
\det(BB^T)=0.
\tag{4.2}
\]

This is the concrete obstruction to routing that survivor through (4.1).

## 5. What is newly removed, and the next exact gap

For a support-one star with total slope vector `b`, if no coordinate carries more than half of `||b||^2`, the previous theorem pays it by mixed Fresnel. If one coordinate is heavy and the tail vector is nonzero, Theorem 2 now pays it through the product

\[
|b_{\rm heavy}|\,\|b_{\rm tail}\|_2.
\]

So the qualitative `leverage>1/2` obstruction is gone. The surviving endpoint is quantitatively sharper:

**`QFORM-FINITELEAK-ALMOST-SINGLEEDGE-OR-RANK1-ARROWHEAD-v1`.** Route the cases in which the star is genuinely almost a single physical edge (the heavy-edge/tail product tends to zero, including zero tail), together with the diagonal-plus-global-rank-one plus one-edge form and the support-two two-hub arrowhead whose hub-to-leaf slope has row rank one. The receiver must remain product-preserving and must not pay a reciprocal coefficient that is allowed to vanish.

The phase-aligned-density refutation remains untouched: no law-uniform pointwise positive-power bound for `E exp(itX^2)` is asserted or used.

Full unrestricted QFORM remains OPEN. Continuity is not claimed by Theorem 2 beyond what follows from any separately invoked density theorem.
