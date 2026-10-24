# QFORM B17: one heavy null row plus two diffuse banks

Run: `20260923T050530Z-account03-B17-QFORM-r23`  
Status: `NEW_SUPPORTING_THEOREM`; full QFORM OPEN; full-target continuity OPEN; `WITHOUT_VERIFIED_BRAIN`.

## Target and purpose

The owner target is the universal bounded-density conjecture for independent real coordinates with densities at most one and a real symmetric matrix having at least three eigenvalues of absolute value at least one.  This report does **not** prove the full conjecture.  It closes a sharp-witness mechanism that remained open in the preceding B17 work: one genuinely heavy physical coordinate placed on an isotropic (null) spectral direction, coupled to two diffuse banks.

The main result is exact in the Gaussian-completion limit and keeps the heavy physical law completely arbitrary under the cap `f<=1`.  Arbitrary fragmentation, disconnected support and translation are therefore included.

Throughout
\[
\sigma^2=\frac1{12}.
\]

## Theorem A: exact cap-one extremizer in the null-row Gaussian completion

Let `X` be any real random variable with probability density `f` satisfying `0<=f<=1`.  Let `B,C` be independent `N(0,sigma^2)` variables, independent of `X`, and set
\[
Q=2XB+C^2.
\]
Then `Q` has a bounded continuous density.  Moreover
\[
\boxed{
 p_Q(0)\le C_{\rm null}
 :=p_{\,2UB+C^2}(0),\qquad U\sim {\rm Unif}[-1/2,1/2],
}
\]
where `U,B,C` are independent.  The centered unit interval is the unique a.e. maximizer of the zero-density functional among cap-one laws.  Finally
\[
\boxed{C_{\rm null}<3\sqrt2.}
\]
A numerical quadrature used only as a diagnostic gives
\[
C_{\rm null}=3.62066702814959078157\ldots,
\qquad 3\sqrt2-C_{\rm null}=0.6219736589696945\ldots.
\]
Thus arbitrary fragmentation of the heavy coordinate cannot reach the known `3sqrt(2)` obstruction in this architecture.

### Proof

The characteristic function factors as
\[
\phi_Q(t)
=(1-2i\sigma^2t)^{-1/2}\,
\mathbb E\exp(-2\sigma^2t^2X^2).
\tag{1}
\]
For `s>0`, the kernel `x -> exp(-s x^2)` is even and strictly decreasing in `|x|`.  The bathtub principle for `0<=f<=1`, `int f=1` gives
\[
\mathbb E e^{-sX^2}
\le I(s):=\int_{-1/2}^{1/2}e^{-sx^2}\,dx.
\tag{2}
\]
In particular `I(s)<=sqrt(pi/s)`, so (1) is `O(|t|^{-3/2})` at infinity.  Hence `phi_Q in L^1`, Fourier inversion supplies a bounded continuous density, and
\[
p_Q(0)
=\frac1\pi\int_0^\infty
\Re(1-it/6)^{-1/2}\,
\mathbb E e^{-t^2X^2/6}\,dt.
\tag{3}
\]
The real factor in (3) is strictly positive.  Applying (2) pointwise in `t` proves the extremal assertion and gives
\[
C_{\rm null}
=\frac1\pi\int_0^\infty
\Re(1-it/6)^{-1/2}
\left(\int_{-1/2}^{1/2}e^{-t^2x^2/6}\,dx\right)dt.
\tag{4}
\]
The uniqueness of the bathtub optimizer for every positive frequency gives uniqueness a.e. of the centered interval law for the integrated functional.

It remains to compare (4) with the isotropic Gaussian obstruction.  For every `s>0`,
\[
I(s)<\left(1+\frac{s}{6}\right)^{-1/2}.
\tag{5}
\]
Indeed, put `z=sqrt(s)/2`.  Inequality (5) is equivalent to
\[
\operatorname{erf}(z)
<\frac{2z}{\sqrt\pi\sqrt{1+2z^2/3}}.
\]
Both sides vanish at zero, while the derivative of the right side minus the left side equals
\[
\frac2{\sqrt\pi}
\left[(1+2z^2/3)^{-3/2}-e^{-z^2}\right]\ge0,
\]
because
\[
\frac32\log(1+2z^2/3)\le z^2
\]
by `log(1+u)<=u`; strictness holds for `z>0`.

The right side of (5) is exactly `E exp(-sG^2)` for `G~N(0,1/12)`.  Therefore (3)-(5) imply
\[
C_{\rm null}<p_{2G_1G_2+G_3^2}(0).
\]
With the orthogonal change
\[
U=(G_1+G_2)/\sqrt2,\qquad V=(G_1-G_2)/\sqrt2,
\]
one has `2G_1G_2+G_3^2=U^2+G_3^2-V^2`.  The three variables are iid `N(0,sigma^2)`, so direct convolution gives
\[
p_{U^2+G_3^2-V^2}(0)=\frac1{2\sqrt2\sigma^2}=3\sqrt2.
\]
This proves the theorem.

## Exact source-valid finite rotated family

Let
\[
a=\frac{e_1+e_3}{\sqrt2},\qquad
b=\frac{e_1-e_3}{\sqrt2},\qquad
c=e_2,
\]
so `{a,b,c}` is an orthonormal basis and, for `J=diag(1,1,-1)`,
\[
y^TJy=2y_a y_b+y_c^2.
\]
For every integer `m>=3`, form the `(2m+1) x 3` matrix `R_m` with rows
\[
a,\qquad \underbrace{b/\sqrt m,\ldots,b/\sqrt m}_{m\text{ rows}},
\qquad \underbrace{c/\sqrt m,\ldots,c/\sqrt m}_{m\text{ rows}}.
\]
Then
\[
R_m^TR_m=aa^T+bb^T+cc^T=I_3.
\]
Consequently
\[
A_m=R_mJR_m^T
\]
has exact nonzero spectrum
\[
\boxed{\{1,1,-1\}}.
\]
Take all `2m+1` physical coordinates independent `Unif[-1/2,1/2]`.  Writing
\[
B_m=m^{-1/2}\sum_{k=1}^mU_k,
\qquad
C_m=m^{-1/2}\sum_{k=1}^mV_k,
\]
the exact physical quadratic form is
\[
\boxed{Q_m=2X_0B_m+C_m^2.}
\tag{6}
\]
The first physical row is genuinely isotropic for the quadratic signature (`a^TJa=0`) but couples to the entire `b` bank.  This is therefore a rotated, nonseparable exact target family, not a diagonal control.

For the centered interval heavy law used in (6), if `g_m` denotes the density of either normalized bank, integrating first in `X_0` gives the exact zero-density identity
\[
\boxed{
p_{Q_m}(0)
=\iint_{\mathbb R^2}
 g_m(b)g_m(c)\,
 \frac{\mathbf 1_{\{c^2\le |b|\}}}{2|b|}\,db\,dc.
}
\tag{7}
\]
The apparent `1/|b|` singularity is integrable because the allowed `c` interval has length `O(sqrt(|b|))` near the origin.

## Designated partner result applied to an actual inequality

The completed `account04/B17` result at

`yspennstate/math-open-problems@2156b76156ad5956c214a881fcfd6d977d6f3b9f`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B17/20260922T211900Z-account04-B17-QFORM-r3/REPORT.md`

proves the weighted local Edgeworth expansion for the same normalized uniform bank:
\[
g_m(y)=\gamma_\sigma(y)
\left[1-\frac1{20m}H_4(y/\sigma)\right]
+O(m^{-2})(1+|y|)^{-8}.
\tag{8}
\]
Apply (8) to both factors in the **actual identity (7)**.  Because the kernel in (7) is integrable against every polynomially weighted Gaussian majorant, termwise integration is justified and gives
\[
\boxed{
p_{Q_m}(0)
=C_{\rm null}-\frac{I_{\rm null}}{20m}+O(m^{-2}),
}
\tag{9}
\]
where the finite, completely explicit coefficient is
\[
I_{\rm null}
=\iint
\frac{\mathbf 1_{\{c^2\le |b|\}}}{2|b|}
\gamma_\sigma(b)\gamma_\sigma(c)
\left[H_4(b/\sigma)+H_4(c/\sigma)\right]db\,dc.
\tag{10}
\]
Thus the finite exact cap-one rotated family converges locally at zero to the cap-one extremal null-row limit.  This is stronger than weak convergence and is a direct application of the designated partner theorem to a concrete density formula.

A high-precision diagnostic evaluation gives
\[
I_{\rm null}=11.6540810558260528\ldots,
\qquad I_{\rm null}/20=0.5827040527913026\ldots.
\]
The proof of (9) does not rely on these decimal evaluations.

For `m>=3`, the partner's bank regularity together with the integral representation obtained from (6) also yields continuity of this witness density.  This is only a witness-family continuity statement; the owner's full continuity conclusion remains open.

## Consequence for the sharp-constant search

The designated partner family proves the universal lower bound
\[
C_*\ge3\sqrt2.
\]
The theorem above shows that the entire one-heavy-null-row Gaussian-completion architecture satisfies
\[
\sup_{0\le f\le1,\,\int f=1}p_{2XB+C^2}(0)
=C_{\rm null}<3\sqrt2\le C_*.
\]
Hence no fragmentation or translation of the single heavy coordinate can sharpen the universal lower bound inside this architecture.  A witness above `3sqrt(2)` must use a different mechanism: at least two mesoscopic/heavy directions, several non-collinear mesoscopic rows, or a genuinely multiscale three-bank geometry.

## Scope / nonclaims

* No Gaussian assumption is made on the original finite target family; every physical finite input is a cap-one uniform law.
* The arbitrary cap-one law appears only in the rigorous Gaussian-completion theorem, used to exclude fragmentation of the one-heavy null row.
* No post-rotation independence is asserted.
* No claim is made that zero is the global density maximizer for arbitrary target forms.
* The full universal upper bound and the full continuity statement remain open.
* Repository transport was used; no authenticated native brain receiver-use event occurred, so status remains `WITHOUT_VERIFIED_BRAIN`.
