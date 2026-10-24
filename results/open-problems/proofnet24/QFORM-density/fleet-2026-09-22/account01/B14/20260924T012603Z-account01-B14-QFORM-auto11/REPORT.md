# account01/B14 — singular-kernel leakage localization by a random linear receiver

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T012603Z-account01-B14-QFORM-auto11`  
Assignment: translations and localization.  
Status: `SUPPORTING_THEOREM_PROVED / STRICT_TARGET_BRANCH_PROVED / FULL_QFORM_OPEN`.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 0. Scope and sources

The live target is the arbitrary-product-law quadratic-form conjecture: independent real coordinates with densities at most one, symmetric coefficient matrix with at least three eigenvalues of modulus at least one, and no support, moment, centering, definiteness or rotation assumptions.

Live corrections used: no uniform pointwise quadratic Fourier decay; rotations do not preserve product independence; bounded-diameter/fixed-fragment localization cannot be assumed; a good principal minor is not forced by the bare third singular-value condition; projection and diagonal estimates are supporting inputs only.

Completed designated-partner source actually applied below:

- account02/B14, run `20260922T181403Z-account02-B14-QFORM-r17`, canonical report at `yspennstate/math-open-problems@04e83634ca19b2a891726f12ea1767c44fbf76a0`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260922T181403Z-account02-B14-QFORM-r17/REPORT.md`.

Its Theorem A says that if a finite measure `mu` on the line has mass `m` and density cap `D`, then for `0<alpha<1`, uniformly in `t`,

\[
\int |x-t|^{-\alpha}\,d\mu(x)
\le \frac{2^\alpha}{1-\alpha}D^\alpha m^{1-\alpha}.
\tag{0.1}
\]

The standard Ball--Rogozin one-dimensional projection estimate already source-pinned in the QFORM fleet is used only as a supporting control: for independent cap-one coordinates `Y_j`,

\[
\left\|p_{c^TY}\right\|_\infty\le \frac{\sqrt2}{\|c\|_2}.
\tag{0.2}
\]

## 1. Translation-uniform hyperbolic Lp core

Let `U,V` be independent probability variables with densities at most one, let `a != 0`, and let `u_0,v_0` be arbitrary real shifts. For every `p>1`,

\[
\boxed{
\left\|p_{2a(U-u_0)(V-v_0)}\right\|_p
\le p |a|^{-1+1/p}.
}
\tag{1.1}
\]

Proof. Put `alpha=1-1/p`. Conditional on `U=x`, scaling the cap-one density of `V` gives

\[
\|p_{2a(x-u_0)(V-v_0)}\|_p
\le (2|a||x-u_0|)^{-\alpha}.
\]

Minkowski and the bathtub estimate give

\[
\|p\|_p
\le (2|a|)^{-\alpha}\,E|U-u_0|^{-\alpha}
\le (2|a|)^{-\alpha}\frac{2^\alpha}{1-\alpha}
=p|a|^{-\alpha}.
\]

No support radius, moment or location enters.

## 2. Random-linear-receiver localization theorem

Let `U,V,Z,Y` be mutually independent groups, with `U,V,Z` having densities at most one. Let `nu` be a finite positive subprobability law for `Y`, of mass `m`. Suppose a scalar statistic `beta(Y)` has, under `nu`, an unnormalized density cap `D`. Let `A(Y),B(Y),R(Y)` be arbitrary measurable real functions. For `a != 0` define

\[
Q=2aUV+A(Y)U+B(Y)V+2\beta(Y)Z+R(Y).
\tag{2.1}
\]

Then for every `p>1`,

\[
\boxed{
\|p_Q^{(\nu)}\|_\infty
\le
\frac{p^2}{p-1}
|a|^{-1+1/p}
D^{1/p}m^{1-1/p}.
}
\tag{2.2}
\]

Here `p_Q^(nu)` is the unnormalized output density contributed by the `Y` subprobability `nu`.

Proof. Fix `Y=y`. Completing the hyperbolic product,

\[
2aUV+A(y)U+B(y)V
=2a\left(U+\frac{B(y)}{2a}\right)
\left(V+\frac{A(y)}{2a}\right)
-\frac{A(y)B(y)}{2a}.
\]

By (1.1), its conditional density has `L^p` norm at most `p|a|^{-1+1/p}`, uniformly in the possibly enormous shifts. Let `q=p/(p-1)`. Conditional on `Y=y`,

\[
\|p_{2\beta(y)Z}\|_q
\le (2|\beta(y)|)^{-1/p},
\]

because a cap-one probability density has `L^q` norm at most one. Young's inequality therefore gives

\[
\|p_{Q\mid Y=y}\|_\infty
\le p|a|^{-1+1/p}(2|\beta(y)|)^{-1/p}.
\]

Integrating in `nu` and applying the completed account02/B14 Riesz bound (0.1) with `alpha=1/p` gives

\[
\begin{aligned}
\|p_Q^{(\nu)}\|_\infty
&\le p|a|^{-1+1/p}2^{-1/p}
\int |\beta(y)|^{-1/p}d\nu(y)\\
&\le p|a|^{-1+1/p}2^{-1/p}
\frac{2^{1/p}}{1-1/p}D^{1/p}m^{1-1/p},
\end{aligned}
\]

which is (2.2).

### Fragment ledger

If `nu=sum_j nu_j`, with masses `m_j` and unnormalized scalar-density caps `D_j`, then

\[
\boxed{
\|p_Q^{(\nu)}\|_\infty
\le \frac{p^2}{p-1}|a|^{-1+1/p}
\sum_jD_j^{1/p}m_j^{1-1/p}.
}
\tag{2.3}
\]

By Holder,

\[
\sum_jD_j^{1/p}m_j^{1-1/p}
\le (\sum_jD_j)^{1/p}(\sum_jm_j)^{1-1/p}.
\tag{2.4}
\]

Hence if the unnormalized fragment caps retain their masses, `D_j<=L m_j`, the full sum costs exactly the same `L^(1/p)` as the unsplit law. In particular, arbitrary distant/countably many outside fragments are zero-tax. Normalizing active fragments before applying the estimate is not justified and can reintroduce the known fragmentation loss.

## 3. Product-bank specialization

Let now `Y=(Y_1,...,Y_m)` have independent cap-one probability densities and let

\[
\beta(Y)=c^TY+t,
\qquad c\ne0,
\]

where the translation `t` is arbitrary. By the source-pinned projection control (0.2), `beta(Y)` has density cap

\[
D\le \frac{\sqrt2}{\|c\|_2},
\]

uniformly in `t`. Theorem (2.2) therefore becomes

\[
\boxed{
\|p_Q\|_\infty
\le C_p\,|a|^{-1+1/p}\|c\|_2^{-1/p},
\qquad
C_p:=\frac{p^2}{p-1}2^{1/(2p)}.
}
\tag{3.1}
\]

At `p=2`,

\[
\boxed{
\|p_Q\|_\infty
\le 2^{9/4}|a|^{-1/2}\|c\|_2^{-1/2}
=4.7568284600\ldots |a|^{-1/2}\|c\|_2^{-1/2}.
}
\tag{3.2}
\]

For the normalized threshold branch `|a|>=1`, `||c||_2>=1`, optimizing `C_p` over `p>1` gives

\[
p_*=\frac{4+\log2+\sqrt{(4+\log2)^2-8\log2}}4
=2.1881899005\ldots,
\tag{3.3}
\]

and

\[
\boxed{
C_*:=C_{p_*}=4.7213840044\ldots .
}
\tag{3.4}
\]

This improves the simple `p=2` constant while preserving all translation/support robustness.

## 4. Singular-Schur interpretation: kernel leakage can be paid probabilistically

Consider the singular three-coordinate active block

\[
B_0=
\begin{pmatrix}
0&a&0\\
a&0&0\\
0&0&0
\end{pmatrix}
\]

on coordinates `(U,V,Z)`. Its kernel is exactly the `Z` direction. Couple an independent original-coordinate bank `Y` through

\[
C=
\begin{pmatrix}
r^T\\s^T\\c^T
\end{pmatrix}.
\]

The range components `r,s` are absorbed exactly into `Y`-dependent translations of `U,V`; the only genuinely non-Schur-absorbable term is the kernel leakage `2Z c^TY`. Theorem (3.1) shows that this leakage is not fatal: it is controlled by the anti-concentration of the untouched product bank `c^TY`.

Concretely, for arbitrary symmetric `H`, arbitrary affine terms, and independent cap-one coordinates,

\[
\begin{aligned}
Q={}&2aUV+2U r^TY+2V s^TY+2Z(c^TY+t)\\
&+Y^THY+\ell_UU+\ell_VV+\ell_Y^TY+\eta,
\end{aligned}
\tag{4.1}
\]

one has exactly (3.1), with no dependence on `r,s,H,t,ell,eta`, support geometry, translations or moments.

Thus the previous exact singular-Schur localization criterion `P_{ker B}C=0` admits a quantitative extension: nonzero kernel leakage can be allowed when its scalar coefficient has a whole-law density cap. What must remain whole is the random coefficient law; paying normalized fragments before aggregation is the unsafe operation.

## 5. Genuine three-large-eigenvalue family

For a clean exact-target application take `r=s=0`; then the active original-coordinate principal block is

\[
A_*=
\begin{pmatrix}0&a\\a&0\end{pmatrix}
\oplus
\begin{pmatrix}0&c^T\\c&H\end{pmatrix}.
\tag{5.1}
\]

The first block contributes eigenvalues `+|a|,-|a|`. The second symmetric block `S` satisfies

\[
\|S\|_{op}\ge \|Se_Z\|_2=\|c\|_2,
\]

so it has an eigenvalue of modulus at least `||c||_2`. Therefore if

\[
|a|\ge1,\qquad \|c\|_2\ge1,
\tag{5.2}
\]

`A_*` has at least three eigenvalues of modulus at least one.

Now embed `A_*` as a principal block of an arbitrarily large symmetric matrix, with completely arbitrary outside block and arbitrary active--outside couplings. Condition on the outside original coordinates. Those couplings produce only affine terms in `(U,V,Z,Y)`: the `U,V` terms are absorbed into the translation-uniform hyperbolic core, the `Z` term merely translates `c^TY`, and the `Y` terms enter the arbitrary remainder. Hence the conditional estimate is uniform in the outside value and integrates without loss. Cauchy interlacing preserves the three threshold eigenvalues in the ambient matrix.

Consequently the entire ambient family satisfies

\[
\boxed{
\|p_{X^TAX}\|_\infty\le C_*=4.7213840044\ldots .
}
\tag{5.3}
\]

This is a strict target-valid indefinite/off-diagonal family. It remains uniform for diffuse receivers, e.g.

\[
c=m^{-1/2}(1,\ldots,1),
\]

where every individual coupling tends to zero while `||c||_2=1`.

## 6. Localization consequence

The useful localization statement from this run is therefore:

> Arbitrary shifts, remote fragments, unbounded supports and moment-free tails cost zero whenever they enter through (i) affine shifts of the hyperbolic core, (ii) translations of the scalar kernel-leakage coefficient, or (iii) arbitrary remainder terms after conditioning. The only analytic currency is the whole-law scalar density cap of the kernel-leakage coefficient. With a mass-weighted unnormalized cap ledger, even countable fragment decompositions preserve the same constant.

This is materially stronger than the purely algebraic singular-Schur zero-leakage condition and uses the completed account02/B14 Riesz theorem at the actual receiver inequality.

## 7. What remains open

This does **not** prove the unrestricted conjecture. The unpaid structural step is to show that bare `s_3(A)>=1` forces, before active-fragment normalization, either a quantitatively nondegenerate hyperbolic core plus a product-bank kernel leakage as above, or one of the fleet's other completed whole-active exits. In particular, a general matrix need not contain the direct-sum block (5.1), and the source-pinned projection inequality is only a supporting anti-concentration input, not the full QFORM theorem.

No uniform pointwise quadratic Fourier estimate, rotated independence, bounded support, moment bound, or principal-minor extraction from `s_3(A)>=1` is assumed.
