SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B15, 2026-09-24T07:00:11Z.
attacking: dimension-free majority-sheet regularity versus diffuse leverage; sharpen submass stability and independently audit the ruled rough-input bridge.

# Rigor check — leverage-sensitive ruled stability and rough passage

Full QFORM status: OPEN. All coordinates below are original independent coordinates until the deterministic spectral geometry is introduced. No independence after rotation is used.

## 1. Source-pinned ruled formula and the anisotropic submass lemma

Take orthonormal `r_1,r_2,r_3 in R^n`, positive curvatures `lambda_1,lambda_2,mu`, and

\[
q(X)=\lambda_1\langle r_1,X\rangle^2+\lambda_2\langle r_2,X\rangle^2-\mu\langle r_3,X\rangle^2.
\]

Let `R` be the `n x 3` matrix with columns `r_k`, let `rho_j` be its j-th row, and set

\[
a_j=|\rho_j|^2,\qquad 0\le a_j\le1,\qquad \sum_j a_j=3.
\]

The completed ruled theorem in
`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`
uses the standard-cone ruling after the scaling
`z=(sqrt(lambda_1)y_1,sqrt(lambda_2)y_2,sqrt(mu)y_3)`.
Write

\[
v_\theta=
\left(-{\sin\theta\over\sqrt{\lambda_1}},
{\cos\theta\over\sqrt{\lambda_2}},
{1\over\sqrt\mu}\right)
\]

for the ruling direction in the unscaled spectral y-coordinates. The exact majority-sheet coefficient is

\[
C_+(\lambda_1,\lambda_2,\mu)
=(\lambda_1\lambda_2\mu)^{-1/2}
\int_0^{2\pi}{d\theta\over |v_\theta|}.
\tag{R1}
\]

When all three curvatures are at least one, `C_+<=pi sqrt(2)`.

Now replace the j-th original-coordinate probability factor by a subdensity `g`, with
`0<=g<=1` and `int g=m<=1`, keeping every other factor a cap-one probability density. Let `nu_{j,m}^+` be the output submeasure restricted to `q>=0`.

For fixed theta, let `U_theta` be an orthonormal 2-frame spanning `v_theta^perp`. Removing coordinate j changes the two-dimensional frame Gram matrix from the identity to

\[
I_2-(U_\theta\rho_j)(U_\theta\rho_j)^T,
\]

whose determinant is

\[
d_j(\theta)=1-|U_\theta\rho_j|^2.
\tag{R2}
\]

Two bounds hold for the two-dimensional trace density `h_theta` seen by the ruling line:

\[
h_\theta\le2,
\qquad
h_\theta\le {2m\over\sqrt{d_j(\theta)}}.
\tag{R3}
\]

The first follows by completing `g` to a cap-one probability density and using the same two-dimensional product-projection theorem as the ruled source. For the second, condition on the selected coordinate. The remaining product probability projects through the 2-frame with Gram determinant `d_j(theta)`, so its density is at most `2/sqrt(d_j(theta))`; integrate against `g`, whose mass is m. Hence

\[
h_\theta\le2\min\left(1,{m\over\sqrt{d_j(\theta)}}\right).
\tag{R4}
\]

Because orthogonal projection cannot increase norm,

\[
d_j(\theta)=1-|U_\theta\rho_j|^2\ge1-|\rho_j|^2=1-a_j.
\tag{R5}
\]

The standard-cone parametrisation has coarea factor `1/2`; its t-parameter is not arclength, and the arclength speed after undoing the spectral scaling is `|v_theta|`. Thus (R4)-(R5) inserted into the exact source formula give the new anisotropic estimate

\[
\boxed{
H(\nu_{j,m}^+)
\le
C_+(\lambda_1,\lambda_2,\mu)
\min\left(1,{m\over\sqrt{1-a_j}}\right)
}
\tag{R6}
\]

whenever `a_j<1`. In particular, under `lambda_1,lambda_2,mu>=1`,

\[
H(\nu_{j,m}^+)\le
\pi\sqrt2\,{m\over\sqrt{1-a_j}}.
\tag{R7}
\]

This is an essential-height statement; no continuity is involved.

## 2. Diffuse-frame Lipschitz stability

Let `f=(f_i)` and `g=(g_i)` be two cap-one product probability laws and

\[
\delta_j=\|f_j-g_j\|_1,
\qquad
\Delta=\sum_j\delta_j.
\]

Telescope in the original coordinates. For the j-th signed factor, the positive and negative parts of `f_j-g_j` are cap-one subdensities of the same mass `delta_j/2`. Applying (R6) to both signs gives

\[
\|T_j^+\|_\infty
\le
{C_+\delta_j\over\sqrt{1-a_j}}.
\tag{R8}
\]

Therefore, if every row leverage satisfies `a_j<=1/2`,

\[
\boxed{
\|r_f^+-r_g^+\|_\infty
\le \sqrt2 C_+\Delta
\le2\pi\Delta.
}
\tag{R9}
\]

This is dimension-free and anisotropic: the three curvatures may be arbitrary numbers at least one.

## 3. All-leverage isotropic stability

For the isotropic signature `(1,1,-1)`, the preceding account02/B15 result
`math-open-problems@45779cb1dca5f453ac620431b380ad015a052e70`
proved the complementary orientation-uniform submass estimate

\[
H(\nu_{j,m}^+)\le20\sqrt2\sqrt m.
\tag{R10}
\]

Combining (R6) with (R10), the j-th signed telescoping term obeys

\[
\|T_j^+\|_\infty
\le
\min\left(40\sqrt{\delta_j},
{\sqrt2\pi\delta_j\over\sqrt{1-a_j}}
\right).
\tag{R11}
\]

Let `H={j:a_j>3/4}`. Since `sum a_j=3`, `|H|<=3`. On the complement, the second term in (R11) is at most `2 sqrt(2) pi delta_j`; on H use the first term and Cauchy-Schwarz. This gives

\[
\boxed{
\|r_f^+-r_g^+\|_\infty
\le
2\sqrt2\pi\Delta+40\sqrt{3\Delta}.
}
\tag{R12}
\]

For `Delta<=1`, one may record the pure Holder form

\[
\|r_f^+-r_g^+\|_\infty
\le(2\sqrt2\pi+40\sqrt3)\sqrt\Delta<79\sqrt\Delta.
\tag{R13}
\]

Thus, on the isotropic ruled majority sheet, all square-root instability is confined to at most three high-leverage original coordinates. If the frame is diffuse (`max a_j<=1/2`), the stronger Lipschitz estimate (R9) holds.

## 4. Rough-input passage is zero-loss

For arbitrary rough cap-one factors choose a nonnegative probability approximate identity and mollify in the original coordinates. Then

\[
0\le f_i^{(\eta)}\le1,
\qquad
\int f_i^{(\eta)}=1,
\qquad
\|f_i^{(\eta)}-f_i\|_1\to0,
\]

and for every finite collection

\[
\left\|\prod_i f_i^{(\eta)}-\prod_i f_i\right\|_1
\le\sum_i\|f_i^{(\eta)}-f_i\|_1\to0.
\tag{R14}
\]

For a fixed positive-sheet event G, restriction by `1_G` and deterministic pushforward by q both contract total variation. Consequently a smooth interval estimate with constant C passes directly to the rough positive submeasure with the same C. In particular (R6), (R9), and (R12) hold for arbitrary measurable cap-one marginals. No convergence of pointwise density representatives is required to pay height.

For the ambient ruled bridge, condition on every coordinate outside an invertible original-coordinate active block B. Then

\[
Q_w(x)=x^TBx+2d(w)^Tx+c_0(w)
=(x+B^{-1}d(w))^TB(x+B^{-1}d(w))+c(w).
\tag{R15}
\]

Thus the later source correction requiring the affine term to lie in the quadratic range is automatic in this scope. The completion is a translation in the original independent coordinates. Translation preserves the cap and the product `L1` error in (R14). The conditional majority interval bound therefore survives rough approximation with exactly the source coefficient, and averaging w finishes the ambient statement. No spectral-coordinate independence and no output continuity are used.

## 5. A genuine exact-target obstruction to single-triple payment

For integer `m>=2`, split `3m` independent cap-one coordinates into three disjoint banks and set

\[
Y_k={1\over\sqrt m}\sum_{j=1}^m X_{k,j},
\qquad
Q_m=Y_1^2+Y_2^2-Y_3^2.
\tag{R16}
\]

The matrix of `Q_m` has spectrum `{1,1,-1,0,...,0}` and every row leverage is `1/m<=1/2`. Hence the source-pinned ruled theorem gives

\[
\Pr(Q_m\in I,Q_m\ge0)\le\pi\sqrt2\,|I|,
\tag{R17}
\]

and (R9) gives, for two product input laws,

\[
\|r_f^+-r_g^+\|_\infty\le2\pi\sum_{k,j}\|f_{k,j}-g_{k,j}\|_1.
\tag{R18}
\]

The full output is also uniformly paid in this family. Each `Y_k` has density cap at most `sqrt(2)` by the one-dimensional product-projection theorem. Therefore the density of `Y_k^2` is at most `sqrt(2)/sqrt(s)` for `s>0`, and the beta convolution gives

\[
\|p_{Y_1^2+Y_2^2}\|_\infty\le2\pi.
\]

Convolution with the independent probability law of `-Y_3^2` cannot increase `L^infty`, so

\[
\boxed{\|p_{Q_m}\|_\infty\le2\pi\quad\text{for every }m.}
\tag{R19}
\]

On the other hand, every invertible physical `3x3` principal block of the matrix in (R16) chooses one coordinate from each bank and equals `diag(1/m,1/m,-1/m)` up to ordering. Thus its best physical-triple scale is exactly `1/m`. The latest designated partner account03/B15 theorem (`math-open-problems@40b108ab5984542e26b8c8ff2cd059e13446bea8`) would give only

\[
\|p_{Q_m}\|_\infty<153m
\]

through a single physical triple, while (R19) stays at `2 pi` and (R17) stays at `pi sqrt(2)`.

This is not a counterexample to QFORM. It is a source-valid obstruction to any global proof interface that first selects one physical triple and reciprocates its conditioning before aggregating a diffuse bank.

## 6. Essential boundedness versus continuity

All inequalities above are interval/essential-height estimates first. For smooth compactly controlled inputs, the ruled integral gives a continuous positive-sheet density; (R9) or (R12) then permits uniform approximation and a canonical `C_0` representative in the stated chambers. This is downstream regularity only. The universal heights (R6), (R9), (R12), (R17), and (R19) do not use continuity.
