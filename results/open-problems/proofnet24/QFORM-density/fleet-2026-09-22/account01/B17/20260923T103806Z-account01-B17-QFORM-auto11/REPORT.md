SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B17, 2026-09-23T10:38:06Z.
attacking: a growing-activity, unbounded-support three-bank witness that keeps exact spectrum `{1,1,-1}` and tests whether rough fragmentation can still saturate the `3 sqrt(2)` lower obstruction.

# QFORM B17 — growing-activity unbounded-support fragmentation still saturates `3 sqrt(2)`

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T103806Z-account01-B17-QFORM-auto11`  
Assignment: Sharp constant and witnesses  
Classification: **NEW SUPPORTING SHARP-WITNESS THEOREM**  
Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**  
Full-target continuity: **separate and still open**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Result

The strongest currently source-valid lower obstruction remains

\[
C_{\rm univ}\ge 3\sqrt2.
\]

This run proves that the same obstruction can be approached by an exact finite **dense rotated** target family even when every physical input law is increasingly rough:

- the density cap is exactly at most one;
- the support has three disconnected components;
- the expected number of remote-fragment hits in each bank tends to infinity;
- the support diameter tends to infinity;
- the fourth moments tend to infinity;
- nevertheless every finite target matrix has exact nonzero spectrum `{1,1,-1}` and its cone-tip density tends to `3 sqrt(2)`.

Thus compact support, uniformly bounded fourth moment, or finite remote-fragment activity cannot be imposed in a sharpness argument without losing genuine near-extremizers.

A convenient general statement is the following.

### Theorem `QFORM-GROWING-FRAGMENT-SATURATION-v1`

Let `lambda_m>0` and `a_m>0` satisfy

\[
\lambda_m\to\infty,\qquad {\lambda_m\over m}\to0,\qquad
a_m\to0,\qquad
D_m:=a_m\sqrt{m/\lambda_m}\to\infty.
\tag{1.1}
\]

Put `epsilon_m=lambda_m/m`, `I=[-1/2,1/2]`,

\[
R_{m,\pm}=[\pm D_m-\varepsilon_m/4,\ \pm D_m+\varepsilon_m/4],
\]

and

\[
f_m(x)=(1-\varepsilon_m){\bf1}_I(x)
       +{\bf1}_{R_{m,+}}(x)+{\bf1}_{R_{m,-}}(x).
\tag{1.2}
\]

For any fixed orthogonal `O in O(3)`, let `J=diag(1,1,-1)` and make the `3m x3` frame `R_m` by repeating `(Oe_j)^T/sqrt(m)` exactly `m` times in physical bank `j`. Set

\[
A_m=R_mJR_m^T.
\tag{1.3}
\]

If the `3m` physical inputs are independent with common density `f_m`, then every `A_m` has exact nonzero spectrum `{1,1,-1}` and

\[
\boxed{p_{X^TA_mX}(0)\longrightarrow 3\sqrt2.}
\tag{1.4}
\]

If in addition

\[
a_m^4\,{m\over\lambda_m}\to\infty,
\tag{1.5}
\]

then the fourth moment of each one-coordinate law diverges.

The concrete rates used by the checker are

\[
\lambda_m=m^{1/3},\qquad a_m=m^{-1/12},\qquad
\varepsilon_m=m^{-2/3},\qquad D_m=m^{1/4},
\tag{1.6}
\]

for which `EW_m^4~m^(1/3)`.

## 2. Source-valid input checks

For large `m`, `D_m->infinity` makes the three intervals in (1.2) disjoint. Their total mass is

\[
(1-\varepsilon_m)|I|+|R_{m,+}|+|R_{m,-}|
=(1-\varepsilon_m)+{\varepsilon_m\over2}+{\varepsilon_m\over2}=1,
\]

and the density never exceeds one. It is symmetric, so its mean is zero.

The exact variance is

\[
v_m={1-\varepsilon_m\over12}
    +\varepsilon_mD_m^2+{\varepsilon_m^3\over48}
={1\over12}+a_m^2-{\lambda_m\over12m}
 +{\lambda_m^3\over48m^3}
\longrightarrow {1\over12}.
\tag{2.1}
\]

With `h=epsilon_m/4`, direct integration on the two remote intervals gives

\[
EW_m^4={1-\varepsilon_m\over80}
 +\varepsilon_mD_m^4
 +{\varepsilon_m^3D_m^2\over8}
 +{\varepsilon_m^5\over1280}.
\tag{2.2}
\]

The leading remote term is

\[
\varepsilon_mD_m^4=a_m^4{m\over\lambda_m},
\]

so (1.5) gives divergent fourth moments. For (1.6), exactly

\[
EW_m^4=m^{1/3}+{1\over80}+{1\over8m^{3/2}}
-{1\over80m^{2/3}}+{1\over1280m^{10/3}}.
\tag{2.3}
\]

The expected number of remote selections in one bank is

\[
m\varepsilon_m=\lambda_m\to\infty,
\]

while the support diameter is `2D_m+o(1)->infinity`.

## 3. Exact use of the completed account02/B17 partner result

The completed designated-partner source actually used is

`yspennstate/math-open-problems@b5377cf0235c71defa44a695048b463a9086d0b4`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/20260923T101548Z-account02-B17-QFORM-auto11b/REPORT.md`.

For precisely the symmetric three-interval shape (1.2), it proves the four-region characteristic-function bounds used below. Importantly, those estimates use the remote location only through `|cos(D_ms)|<=1`; therefore they apply to the present variable amplitude `a_m` and variable remote center `D_m`.

Let

\[
S_m={1\over\sqrt m}\sum_{k=1}^m W_{m,k},
\]

and write `h_m` for its density. The exact one-row and bank characteristic functions are

\[
\phi_m(s)=(1-\varepsilon_m)\operatorname{sinc}(s/2)
 +\varepsilon_m\operatorname{sinc}(\varepsilon_ms/4)\cos(D_ms),
\tag{3.1}
\]

\[
\psi_m(t)=\phi_m(t/\sqrt m)^m.
\tag{3.2}
\]

Applying the partner's completed estimates to this actual `phi_m` gives, eventually,

\[
|\phi_m(s)|\le e^{-s^2/60},\quad |s|\le1,
\tag{3.3}
\]

\[
|\phi_m(s)|\le q_1<1,\quad 1\le|s|\le12,
\tag{3.4}
\]

\[
|\phi_m(s)|\le {1\over3},\quad 12\le|s|\le4/\varepsilon_m,
\tag{3.5}
\]

and

\[
|\phi_m(s)|\le {6\over|s|},\quad |s|\ge4/\varepsilon_m.
\tag{3.6}
\]

Here `q_1<1` is an absolute constant. After `t=sqrt(m)s`, the three outer pieces satisfy

\[
O(\sqrt m\,q_1^m),\qquad
O(\sqrt m\,\varepsilon_m^{-1}3^{-m}),\qquad
{8\sqrt m\over\varepsilon_m(m-1)}
  \left({3\varepsilon_m\over2}\right)^m,
\]

respectively, and therefore

\[
\boxed{
\int_{|t|>\sqrt m}|\psi_m(t)|dt\to0.
}
\tag{3.7}
\]

This is the concrete completed partner result applied to an actual inequality in the present three-bank witness.

## 4. The rough bank still has a uniform local Gaussian limit

The normalized maximal row size obeys

\[
{\sup|W_m|\over\sqrt m}
\le {D_m+o(1)\over\sqrt m}
={a_m\over\sqrt{\lambda_m}}+o(m^{-1/2})\to0.
\tag{4.1}
\]

Thus the Lindeberg condition holds deterministically. Combined with (2.1), the triangular-array central limit theorem gives

\[
S_m\Rightarrow G,\qquad G\sim N(0,1/12),
\tag{4.2}
\]

so

\[
\psi_m(t)\to e^{-t^2/24}
\quad\text{for every fixed }t.
\tag{4.3}
\]

The partner bound (3.3) implies

\[
|\psi_m(t)|\le e^{-t^2/60},\qquad |t|\le\sqrt m.
\tag{4.4}
\]

Fix `R`, use dominated convergence on `[-R,R]`, then let `R->infinity` in the Gaussian envelopes on `R<|t|<=sqrt(m)`, and finally use (3.7) outside `sqrt(m)`. This gives

\[
\boxed{
\int_{\mathbb R}|\psi_m(t)-e^{-t^2/24}|dt\longrightarrow0.
}
\tag{4.5}
\]

Fourier inversion therefore yields the uniform local limit

\[
\boxed{
\delta_m:=\|h_m-\gamma_{1/\sqrt{12}}\|_\infty\to0.
}
\tag{4.6}
\]

### Required newest-Claude result applied to the same bank

The required newest-Claude source was read at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.

Its Lemma 1 proves, for every cap-one probability density `f` and every `p>=2`,

\[
\int |\widehat f(s)|^pds\le {4\pi\over\sqrt p}.
\tag{4.7}
\]

Apply (4.7) with the **actual fragmented density** `f_m` and `p=m`. By (3.2),

\[
\boxed{
\int|\psi_m(t)|dt
=\sqrt m\int|\widehat f_m(s)|^m ds\le4\pi,
\qquad \|h_m\|_\infty\le2.
}
\tag{4.8}
\]

This concrete inequality is used in the cone-tail estimate below. No law-uniform pointwise stationary-phase estimate is invoked.

The current master versions of the same Claude directory's `FOURIER_ROUTE_REPORT.md` and `COUNTEREXAMPLE_SEARCH.md` were also read. Their open-status and correction scopes are preserved.

## 5. Exact dense rotated finite target

To make the stress genuinely non-diagonal in the physical coordinates, take

\[
O={1\over7}\begin{pmatrix}
6&-2&-3\\
-2&3&-6\\
-3&-6&-2
\end{pmatrix},\qquad
J=\operatorname{diag}(1,1,-1).
\tag{5.1}
\]

Direct multiplication gives `O^TO=I` and

\[
B=O^TJO={1\over49}
\begin{pmatrix}
31&-36&-12\\
-36&-23&-24\\
-12&-24&41
\end{pmatrix}.
\tag{5.2}
\]

All nine entries of `B` are nonzero.

For the frame in (1.3),

\[
R_m^TR_m
=\sum_{j=1}^3 m{(Oe_j)(Oe_j)^T\over m}=I_3.
\tag{5.3}
\]

Consequently `A_m=R_mJR_m^T` has rank three and exact nonzero spectrum

\[
\boxed{\{1,1,-1\}.}
\tag{5.4}
\]

In bank coordinates its physical blocks are

\[
(A_m)_{jk}={B_{jk}\over m}\,\mathbf1_m\mathbf1_m^T,
\tag{5.5}
\]

so every physical matrix entry is nonzero. This is an exact dense rotated target, not a diagonal control.

Let `Y_m=(S_{1,m},S_{2,m},S_{3,m})`, with independent copies of the bank sum. Then

\[
Q_m=X^TA_mX=(OY_m)^TJ(OY_m)=Y_m^TBY_m.
\tag{5.6}
\]

## 6. Exact cone-tip formula and convergence

Let `z=Oy`. Its joint density is

\[
\rho_m(z)=\prod_{j=1}^3h_m((O^Tz)_j).
\tag{6.1}
\]

This is merely a change of variables in the density. No independence of the rotated non-Gaussian coordinates is asserted.

Let

\[
\omega_\pm(\theta)={1\over\sqrt2}(\cos\theta,\sin\theta,\pm1).
\tag{6.2}
\]

Parameterising the null cone of `q(z)=z_1^2+z_2^2-z_3^2` and dividing surface area by `|grad q|` gives the exact central-density formula

\[
\boxed{
p_{Q_m}(0)
={1\over2\sqrt2}\sum_{\pm}\int_0^{2\pi}\int_0^\infty
\rho_m(r\omega_\pm(\theta))\,dr\,d\theta.
}
\tag{6.3}
\]

For each finite `m>=2`, the bank density is continuous (it is a convolution of `L^1` densities) and compactly supported, so (6.3) is an ordinary coarea identity for this explicit product-derived density. This does not invoke the refuted arbitrary-joint coarea **bound**.

Let

\[
\rho_\infty(z)=\prod_{j=1}^3\gamma_{1/\sqrt{12}}(z_j).
\]

Because the Gaussian is isotropic,

\[
\prod_j\gamma_{1/\sqrt{12}}((O^Tz)_j)=\rho_\infty(z).
\tag{6.4}
\]

By (4.6), (4.8), and `||gamma||_infinity<2`, on every bounded ray segment

\[
|\rho_m(z)-\rho_\infty(z)|
\le3\cdot2^2\delta_m=12\delta_m.
\tag{6.5}
\]

Thus the contribution to the difference of the cone integrals from `0<=r<=R` is bounded by

\[
12\sqrt2\pi R\delta_m.
\tag{6.6}
\]

For the tail, fix a unit ray `omega` and set `v=O^Tomega`. Some `|v_j|>=1/sqrt(3)`. From (4.8),

\[
\begin{aligned}
\int_R^\infty \rho_m(r\omega)dr
&\le 2^2\int_R^\infty h_m(rv_j)dr\\
&\le4\sqrt3\,P(|S_m|\ge R/\sqrt3)\\
&\le {12\sqrt3\,v_m\over R^2}.
\end{aligned}
\tag{6.7}
\]

The limiting Gaussian has the same estimate with `v_m` replaced by `1/12`. Since (2.1) makes `v_m` uniformly bounded, (6.7) is uniform in `m`, `theta`, and the two cone sheets. First let `m->infinity` in (6.6), then `R->infinity` in (6.7). Therefore

\[
\boxed{
p_{Q_m}(0)\to p_{G_1^2+G_2^2-G_3^2}(0).
}
\tag{6.8}
\]

For iid `G_j~N(0,sigma^2)`, evaluating the same cone integral gives

\[
p_{G_1^2+G_2^2-G_3^2}(0)
={1\over2\sqrt2\,\sigma^2}.
\tag{6.9}
\]

At `sigma^2=1/12`,

\[
\boxed{
p_{Q_m}(0)\longrightarrow3\sqrt2
=4.242640687119285\ldots .
}
\tag{6.10}
\]

Since every `A_m` is an exact target matrix and every `f_m` is an admissible physical input density,

\[
\boxed{C_{\rm univ}\ge3\sqrt2.}
\tag{6.11}
\]

The numerical lower bound itself was already known; what is new here is the **rough-law saturation class** proving that the same obstruction survives growing fragmentation, diverging support, diverging fourth moments, and a dense physical rotation.

## 7. Constraint on a proposed sharp proof

Any proposed proof of a sharp upper constant `3sqrt(2)` cannot rely on first restricting near-extremizers to any of the following uniformly in dimension:

1. bounded support diameter;
2. bounded fourth moment or a fixed higher moment;
3. only finitely many remote fragment hits in a diffuse bank;
4. compact/tight one-coordinate support before aggregation.

The example does not rule out using truncation or moment bounds with an error term that is shown to vanish **after** the product-bank aggregation. It specifically shows those properties are not uniform structural features of sharp sequences.

The remaining witness frontier for values **above** `3sqrt(2)`, if any, still lies outside this class: genuinely macroscopic non-collinear/shared-coordinate heavy structures, finite/mesoscopic mechanisms that do not Gaussianise, coupled non-rank-one tails, or an off-center/two-sheet effect. No such witness is proved here.

## 8. Corrections and scope

The proof preserves the live corrections:

- no uniform law-wise pointwise `|t|^{-1/2}` stationary-phase estimate;
- no independence after spectral rotation;
- no arbitrary-joint rank-three coarea **bound**;
- no positive moment of worst conditional projection-density caps;
- no bounded-diameter or fixed-fragment-count extremality;
- no claim that a single physical minor/cross cut must be uniformly good.

The coarea identity (6.3) is used only for the explicit, continuous, product-derived finite density and is paired with the actual product-bank bound (4.8).

For this scoped family the explicit cylindrical/coarea representation gives a continuous density; this does **not** prove the separately requested full-target continuity statement.

## 9. Independent-review status and checker

No independent review of this new theorem is claimed in this run. `check.py` verifies the exact orthogonality, rotated core, spectrum, variance, fourth-moment asymptotics, remote-activity scales, and Gaussian cone-tip constant. The saved output is

`QFORM_B17_GROWING_FRAGMENT_SATURATION_CHECK_PASS`.

The checker is only an algebra certificate; the analytic proof is Sections 3-6 above.
