# account03/B14 — translation-uniform zero-diagonal triple closure

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T173618Z-account03-B14-QFORM-r15`  
**Assignment:** translations and localization  
**Startup control:** `yspennstate/math-research-brain@fd93875d01be9ddf7534ea5402828bf422c19eb0`; refreshed before publication to `3c8e4fe6942ee985c3aa07f9f9f8c801f30fb56b`  
**Owner control at refresh:** `2026-09-22.9`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** supporting target-level theorem; full QFORM remains OPEN.

## 1. Result

This run proves a translation-uniform density bound for an exact physical branch that is missed by scalar-pivot arguments: a nonsingular three-coordinate principal block with zero physical diagonal.

### Theorem A (pure off-diagonal physical triple)

Let `X,Y,Z` be independent real random variables with probability densities bounded by one. Let

\[
B=\begin{pmatrix}
0&a&b\\
a&0&c\\
b&c&0
\end{pmatrix},\qquad abc\ne0,
\]

and let

\[
Q_3=(X,Y,Z)B(X,Y,Z)^T+d_1X+d_2Y+d_3Z+d_0.
\]

Then `Q_3` has an essentially bounded density and

\[
\boxed{
\|p_{Q_3}\|_\infty
\le C_{\rm off}\,|\det B|^{-1/3},
\qquad
C_{\rm off}=21\,2^{1/3}e^{-2/3}<13.585.
}
\]

The estimate is uniform in the affine coefficients `d_i`, in translations of the input laws, in fragment number/separation, and in support diameter. No moment, compact-support, connected-support, log-concavity or smoothness hypothesis is used.

### Corollary B (conditional active-triple branch in arbitrary dimension)

Let `A` be any real symmetric `n x n` matrix. Suppose there is an original-coordinate triple `I={i,j,k}` such that the principal block `B=A_{I,I}` has zero diagonal and `det B != 0`. For independent cap-one coordinates `X_1,...,X_n`, conditioning on the outside coordinates produces

\[
Q\mid X_{I^c}=z=x_I^TBx_I+\ell(z)^Tx_I+c(z).
\]

Therefore, uniformly in `z`,

\[
\boxed{
\|p_{Q\mid X_{I^c}=z}\|_\infty
\le C_{\rm off}|\det B|^{-1/3}
}
\]

and hence

\[
\boxed{
\|p_Q\|_\infty
\le C_{\rm off}|\det B|^{-1/3}.
}
\]

In particular, if `|det B|>=1`, this branch is closed with `||p_Q||_infty < 13.585` even when the full matrix has arbitrary additional eigenvalues, arbitrary outside quadratic coefficients, and arbitrary cross couplings.

This does **not** assert that the three-large-eigenvalue hypothesis always supplies such a physical triple. That structural implication remains unpaid.

## 2. Translation removal is exact

Because `det B=2abc !=0`, the block is invertible. For an arbitrary affine vector `d=(d_1,d_2,d_3)^T`, let

\[
h=\frac12 B^{-1}d.
\]

Writing `x=y-h` gives

\[
x^TBx+d^Tx=y^TBy-\frac14d^TB^{-1}d.
\]

Thus affine terms only translate the output level after a coordinatewise translation of the three inputs. Coordinatewise translations preserve independence and the cap `f_i<=1`. Consequently it suffices to prove Theorem A for

\[
Q_0=2aXY+2bXZ+2cYZ.
\]

The same observation is what makes Corollary B uniform in the outside realization `z`: the induced vector `ell(z)` is removed separately on every deterministic outside fiber, without any moment or support bound.

## 3. Product-density envelope

The first lemma is elementary but is the main analytic input.

### Lemma 1

Let `U,V` be independent with probability densities bounded by one. Then `P=UV` has a density satisfying, for `s != 0`,

\[
p_P(s)\le H(|s|),
\]

where

\[
H(r)=
\begin{cases}
2+2\log(1/r),&0<r\le1,\\
2r^{-1/2},&r\ge1.
\end{cases}
\]

If instead `||f_U||_infty<=M` and `||f_V||_infty<=N`, then

\[
\boxed{p_{UV}(s)\le MN\,H(MN|s|).}
\]

#### Proof

For cap-one densities,

\[
p_P(s)=\int_{\mathbb R}f_U(u)f_V(s/u)\frac{du}{|u|}.
\]

If `0<|s|<=1`, split into `|u|<|s|`, `|s|<=|u|<=1`, and `|u|>1`. In the first region substitute `v=s/u`; because `|v|>1`, that piece is at most `1`. The middle piece is at most

\[
\int_{|s|\le|u|\le1}\frac{du}{|u|}=2\log(1/|s|),
\]

and the last piece is at most `1`. Hence the first branch of `H`.

If `|s|>=1`, split at `|u|=sqrt{|s|}`. On the large-`u` part use `1/|u|<=|s|^{-1/2}` and `int f_U=1`; on the small-`u` part substitute `v=s/u` and use `1/|v|<=|s|^{-1/2}`. This gives `2|s|^{-1/2}`.

For general caps set `U'=MU`, `V'=NV`. The transformed densities are cap one and `U'V'=MN UV`, giving the scaled formula.

## 4. One-dimensional logarithmic trace bound

We need to average the logarithmic product singularity against the third physical coordinate.

### Lemma 2

For every `L>=1`, every real `s`, and every probability density `f<=1`,

\[
\boxed{
\int_{\mathbb R} f(x)H\!\left(L|x^2-s|\right)\,dx
\le
\frac{14(1+\log\sqrt L)}{\sqrt L}.
}
\]

#### Proof

Put `m=sqrt L>=1`, change variables `y=mx`, and define `w(y)=f(y/m)`. Then `0<=w<=1` and `int w=m`. It is enough to control

\[
F_\sigma(y)=H(|y^2-\sigma|)
\]

uniformly in `sigma`.

For every `R>0`,

\[
\big|\{y:|y^2-\sigma|<R\}\big|\le2\sqrt{2R}.
\]

Indeed, for `sigma>=0` the set is the difference of two symmetric square-root intervals, and the worst case occurs at the transition `sigma=R`; for `sigma<0` the estimate is easier.

Hence the superlevel measure `mu(u)=|{F_sigma>u}|` satisfies

\[
\mu(u)\le\frac{4\sqrt2}{u},\qquad0<u\le2,
\]

and

\[
\mu(u)\le2\sqrt2\exp(-(u-2)/4),\qquad u>2.
\]

Layer cake and `0<=w<=1`, `int w=m`, give

\[
\int wF_\sigma
\le\int_0^\infty\min\{m,\mu(u)\}\,du.
\]

For `1<=m<=2sqrt2`, the right side is at most `2m+8sqrt2`, which is at most `14(1+log m)`. For `m>=2sqrt2`, split at `u_0=4sqrt2/m`; the low-level part is at most

\[
4\sqrt2\left[1+\log\frac{m}{2\sqrt2}\right],
\]

and the high-level exponential tail contributes at most `8sqrt2`. Their sum is again at most `14(1+log m)`. Divide by `m`.

## 5. Proof of Theorem A

Relabel the variables so that

\[
|c|=\min\{|a|,|b|,|c|\}.
\]

Thus

\[
r:=\frac{|ab|}{c^2}\ge1.
\]

Fix `X=x` and define

\[
U=bx+cY,
\qquad
W=2Z+\frac{2a}{c}x.
\]

Conditional on `X=x`, `U` and `W` are independent. Their density caps are respectively `1/|c|` and `1/2`. The quadratic form factors as

\[
Q_0
=U W-\frac{2ab}{c}x^2.
\]

By Lemma 1, with `k=1/(2|c|)`, the conditional density satisfies

\[
p_{Q_0\mid X=x}(t)
\le
k\,H\!\left(k\left|t+\frac{2ab}{c}x^2\right|\right).
\]

Since

\[
k\left|\frac{2ab}{c}\right|=\frac{|ab|}{c^2}=r,
\]

averaging in `x` and applying Lemma 2 gives

\[
\|p_{Q_0}\|_\infty
\le
\frac{1}{2|c|}\cdot
\frac{14(1+\tfrac12\log r)}{\sqrt r}
=
7\frac{1+\tfrac12\log r}{\sqrt{|ab|}}.
\]

Let

\[
P=|abc|.
\]

Because `r=|ab|/c^2`, we have `P=|c|^3r` and therefore

\[
\frac1{\sqrt{|ab|}}=P^{-1/3}r^{-1/6}.
\]

The elementary one-variable function

\[
g(r)=\left(1+\frac12\log r\right)r^{-1/6},\qquad r\ge1,
\]

has its maximum at `log r=4`, where

\[
g_{\max}=3e^{-2/3}.
\]

Thus

\[
\|p_{Q_0}\|_\infty
\le21e^{-2/3}P^{-1/3}.
\]

Finally, `det B=2abc`, so

\[
\|p_{Q_0}\|_\infty
\le21\,2^{1/3}e^{-2/3}|\det B|^{-1/3}.
\]

The affine reduction in Section 2 completes Theorem A.

## 6. Proof of Corollary B

Condition on all coordinates outside `I`. Since the original coordinates are independent, the three active conditional marginals remain the original cap-one laws. The outside realization only produces a deterministic affine vector and additive constant in the active variables. Theorem A is uniform over both, hence for almost every outside realization `z`,

\[
\Pr\{Q\in J\mid X_{I^c}=z\}
\le C_{\rm off}|\det B|^{-1/3}|J|.
\]

Integrating `z` gives the same small-ball inequality for the full form. Therefore the output law is absolutely continuous with essential density bound `C_off |det B|^{-1/3}`.

## 7. Partner result actually applied

The completed partner theorem used is account04/B14:

- repository/commit: `yspennstate/math-open-problems@430065de1a8e478dc6156f6b489aa46a63681c09`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260922T171953Z-account04-B14-QFORM-r2/REPORT.md`.

It proves exact cap-preserving compact completion and

\[
C_{\rm all}=C_{\rm compact}=C_{\rm finite\ interval\ unions}
\]

for quadratic small-ball constants, with no support-diameter or fragment-count loss.

Applied to the present branch: one may first establish the displayed `C_off |det B|^{-1/3}` inequality on compact finite-fragment indicator products; because the constant derived above is independent of every support location, separation, diameter and fragment count, account04/B14 transfers the *same* constant to arbitrary unbounded cap-one product laws. The direct calculation above in fact already works for arbitrary cap-one densities, so the partner theorem provides an independent exact localization transfer rather than an additional assumption.

## 8. Relation to the live full-QFORM proof

This is a concrete closure of part of the zero-physical-pivot geometry. Scalar-Schur arguments require a nonzero physical diagonal and can lose a factor as that pivot tends to zero. The theorem here instead exploits the three off-diagonal couplings jointly; the determinant is the only matrix scale that survives.

It is stronger than merely applying the rank-exactly-three target theorem to a three-variable form because Corollary B is a conditional **principal-block** statement inside an arbitrary higher-rank ambient matrix and only asks for a determinant lower bound on that zero-diagonal block, not that each eigenvalue of the block separately have modulus at least one.

The unpaid structural implication is now precise:

> Under the full hypothesis that `A` has at least three eigenvalues of modulus at least one, either produce a target-valid branch already covered by the current ridge/rank-two machinery, or force an original-coordinate triple whose near-zero diagonal and off-diagonal determinant can be quantitatively reduced to the theorem above without a dimension-dependent loss.

The exact zero-diagonal branch is solved; a **near-zero diagonal stability theorem** remains open.

## 9. Continuity

This report proves existence of an essentially bounded density in its stated branch. It does **not** prove that density has a continuous representative for arbitrary measurable cap-one input densities. Continuity remains a separate target.

## 10. Corrections respected

No pointwise van-der-Corput decay, post-rotation independence, Gaussian/log-concave/moment hypothesis, bounded support diameter, fixed fragment count, or projection-density-to-indefinite-trace shortcut is used. No numerical histogram is used as proof. Full QFORM remains OPEN.
