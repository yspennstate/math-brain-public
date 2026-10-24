SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B17, 2026-09-23T08:42:05Z.
attacking: a genuinely dense four-coordinate rank-three Hadamard stress; determine its full output-density maximum exactly, then compare it to the sharp diffuse mechanism using the designated account02/B17 theorem.

# QFORM B17 — exact global density of the dense four-coordinate Hadamard stress

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T084205Z-account01-B17-QFORM-auto11`  
Status: **NEW SUPPORTING SHARP-WITNESS THEOREM; FULL QFORM OPEN / NOT PROVED**  
Execution: `WITHOUT_VERIFIED_BRAIN`. Full-target continuity remains a separate target.

## 1. The exact target family

Let

\[
O=\frac12\begin{pmatrix}
1&1&1&1\\
1&-1&1&-1\\
1&1&-1&-1\\
1&-1&-1&1
\end{pmatrix},\qquad
J_0=\operatorname{diag}(1,1,-1,0),
\]

and

\[
A=OJ_0O^T
=\frac14\begin{pmatrix}
1&-1&3&1\\
-1&1&1&3\\
3&1&1&-1\\
1&3&-1&1
\end{pmatrix}.
\tag{1.1}
\]

`O` is orthogonal, so

\[
\boxed{\operatorname{spec}(A)=\{1,1,-1,0\}.}
\tag{1.2}
\]

All sixteen entries of `A` are nonzero. Hence this is an exact finite, genuinely shared-coordinate, nonseparable target matrix with exactly three eigenvalues of modulus one.

Let `X_1,...,X_4` be independent `Unif[-1/2,1/2]`. Their physical densities are exactly one on their supports. Put

\[
Q=X^TAX.
\]

### Theorem `QFORM-HADAMARD4-GLOBAL-MODE-v1`

`Q` has a bounded continuous density with

\[
\boxed{
\|p_Q\|_\infty=p_Q(0)=8(\sqrt2-1)=3.313708498984\ldots .
}
\tag{1.3}
\]

Moreover `p_Q(t)` is nonincreasing for `t>=0`, while `p_Q(-t)` is nonincreasing for `t>=0`. Thus zero is a global mode from both sides.

In particular

\[
\boxed{\pi<8(\sqrt2-1)<3\sqrt2.}
\tag{1.4}
\]

So this is a finite exact rotated example whose density is already strictly larger than the sharp diagonal constant `pi`, but it still lies strictly below the known diffuse obstruction `3 sqrt(2)`.

## 2. Exact product-provenance projection density

Write spectral/null coordinates

\[
(y_1,y_2,y_3,z)^T=O^TX.
\]

Then

\[
Q=y_1^2+y_2^2-y_3^2.
\tag{2.1}
\]

For fixed `y=(y_1,y_2,y_3)`, the physical cube constraints are four length-two intervals for the null coordinate `z`. Their centers are

\[
\begin{aligned}
b_1&=-(y_1+y_2+y_3),\\
b_2&= y_1-y_2+y_3,\\
b_3&= y_1+y_2-y_3,\\
b_4&=-y_1+y_2+y_3.
\end{aligned}
\tag{2.2}
\]

The fiber length is therefore

\[
\ell(y)=\bigl(2-(\max_i b_i-\min_i b_i)\bigr)_+.
\tag{2.3}
\]

The six pairwise differences in (2.2) are twice the quantities `y_i+y_j` or `y_i-y_j`. Hence

\[
\max_i b_i-\min_i b_i
=2\max_{i<j}\max\{|y_i+y_j|,|y_i-y_j|\}
=2(M_1(y)+M_2(y)),
\tag{2.4}
\]

where `M_1>=M_2>=M_3` are the ordered absolute coordinate magnitudes. Consequently the exact three-dimensional marginal density inherited from the original product cube is

\[
\boxed{
\rho(y)=2\bigl(1-M_1(y)-M_2(y)\bigr)_+.
}
\tag{2.5}
\]

This identity is useful in its own right: it retains the precise product provenance rather than replacing the projection by an arbitrary joint density.

## 3. Exact cone-tip value

On the cone `y_1^2+y_2^2-y_3^2=0`, parameterize each nappe by

\[
y=r(\cos\theta,\sin\theta,\sigma),\qquad r\ge0,\quad \sigma\in\{\pm1\}.
\tag{3.1}
\]

For the Lorentz quadratic form,

\[
\frac{dS}{|\nabla Q|}=\frac12\,dr\,d\theta
\tag{3.2}
\]

on each nappe. On the positive nappe the four null-fiber centers are `r b_j(theta)` with

\[
(b_1,b_2,b_3,b_4)=(-c-s-1,-c+s+1,c-s+1,c+s-1),
\]

where `c=cos theta`, `s=sin theta`. Their range is

\[
D(\theta)=2\bigl(1+\max\{|\cos\theta|,|\sin\theta|\}\bigr).
\tag{3.3}
\]

Indeed the candidates `2(1+|c|)` and `2(1+|s|)` dominate `2|c+s|` and `2|c-s|`. The fiber length along that ray is

\[
L(r,\theta)=(2-rD(\theta))_+,
\]

so

\[
\int_0^\infty L(r,\theta)dr=\frac2{D(\theta)}.
\tag{3.4}
\]

The negative nappe gives the same integral. Therefore

\[
p_Q(0)=2\int_0^{2\pi}\frac{d\theta}{D(\theta)}.
\tag{3.5}
\]

By eightfold symmetry, and `max(cos theta,sin theta)=cos theta` on `[0,pi/4]`,

\[
\begin{aligned}
p_Q(0)
&=8\int_0^{\pi/4}\frac{d\theta}{1+\cos\theta}\\
&=8\tan(\pi/8)
=8(\sqrt2-1).
\end{aligned}
\tag{3.6}
\]

The same value is obtained as the symmetric small-ball derivative `lim_{eps downarrow0} P(|Q|<=eps)/(2eps)`.

## 4. The entire two-sheet side is monotone away from the tip

Let `tau>=0` and consider level `Q=-tau`. By sign symmetry and swapping `|y_1|,|y_2|`, write

\[
a=|y_1|\ge b=|y_2|\ge0,
\qquad
c_\tau=\sqrt{a^2+b^2+\tau}.
\]

Since `c_tau>=a`, the two largest coordinate magnitudes are `c_tau` and `a`. Integrating the delta function in `y_3` gives both roots `+-c_tau`, with total Jacobian factor `1/c_tau`. Using (2.5),

\[
\boxed{
p_Q(-\tau)=16\int_0^\infty\int_0^a
\frac{(1-a-c_\tau)_+}{c_\tau}\,db\,da.
}
\tag{4.1}
\]

For fixed `(a,b)`, the function

\[
c\mapsto \frac{(1-a-c)_+}{c}
=\left(\frac{1-a}{c}-1\right)_+
\]

is nonincreasing. Since `c_tau` increases with `tau`, (4.1) implies

\[
\boxed{p_Q(-\tau)\le p_Q(0)\qquad(\tau\ge0).}
\tag{4.2}
\]

This pays the genuinely difficult two-sheet side for this dense shared-coordinate stress by exact product geometry, not by an arbitrary-joint coarea estimate.

## 5. The one-sheet side is also monotone away from zero

Let `t>=0`. Use polar coordinates in the positive spectral plane:

\[
y_1=r\cos\theta,\quad y_2=r\sin\theta,
\qquad r=\sqrt{u^2+t},\quad u=|y_3|.
\]

Integrating the delta function in `r` gives factor `1/2`. Restrict by symmetry to `0<=theta<=pi/4`, where `c=cos theta>=s=sin theta>=0`. The two largest absolute coordinates have sum

\[
r c+\max\{r s,u\}.
\]

Hence (2.5) yields the exact formula

\[
\boxed{
p_Q(t)=16\int_0^{\pi/4}\int_0^\infty
\left(1-c\sqrt{u^2+t}
-\max\{s\sqrt{u^2+t},u\}\right)_+du\,d\theta.
}
\tag{5.1}
\]

For fixed `(u,theta)`, every `t`-dependent term subtracted inside the positive part is nondecreasing in `t`. Therefore

\[
\boxed{p_Q(t)\le p_Q(0)\qquad(t\ge0).}
\tag{5.2}
\]

Equations (4.2) and (5.2), together with (3.6), prove the global assertion (1.3). Dominated convergence in (4.1) and (5.1) also gives continuity at zero; away from zero the same formulas give a continuous representative directly.

## 6. Exact comparisons

The upper comparison in (1.4) is

\[
3\sqrt2-8(\sqrt2-1)=8-5\sqrt2>0
\]

because `sqrt(2)<8/5`. For the lower comparison, the classical `pi<22/7` and

\[
8(\sqrt2-1)>\frac{22}{7}
\iff \sqrt2>\frac{39}{28},
\]

while

\[
2-\left(\frac{39}{28}\right)^2=\frac{47}{784}>0.
\]

Thus the strict inequalities require no floating-point inference.

## 7. Newest-Claude result applied to an actual inequality

The required newest-Claude package `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`, proves for exact rank-three signature `(+,+,-)` the ruled one-sheet estimate

\[
p_Q(s)\le\pi\sqrt2,\qquad s\ge0,
\tag{7.1}
\]

for arbitrary product inputs, with no leverage condition. Applying it to the actual matrix (1.1) immediately certifies its entire positive side. Formula (5.1) then sharpens the same applied inequality in this stress family to

\[
\boxed{
sup_{s\ge0}p_Q(s)=8(\sqrt2-1)<\pi\sqrt2.
}
\tag{7.2}
\]

The new contribution is therefore concentrated where the general Claude theorem remains weakest: exact control of this dense family's two-sheet side and the global mode.

## 8. Designated account02/B17 result applied to an actual comparison

The current completed designated partner result is

`math-open-problems@fefb4cf4f0af17c810341152311c3822c78d5b7f`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/20260923T082513Z-account02-B17-QFORM-r12/UNIFORM_EXTENSION.md`.

Specialize it to the canonical strong core `B=diag(1,1,-1)`. If `P_m` is the three-bank averaging frame and every physical input is an arbitrary independent translation of a unit interval, then for one deterministic `Delta_m->0`,

\[
\boxed{
\sup_{\text{allowed translations}}
\|p_{X^TP_mBP_m^TX}\|_\infty
\le3\sqrt2+\Delta_m.
}
\tag{8.1}
\]

For centered translations the same partner theorem gives convergence of the density supremum to `3sqrt(2)`. Applying (8.1) to this concrete canonical comparator and comparing with (1.3) gives

\[
\boxed{
\|p_Q\|_\infty=8(\sqrt2-1)
<3\sqrt2
=\lim_{m\to\infty}\|p_{X^TP_mBP_m^TX}\|_\infty.
}
\tag{8.2}
\]

Thus the all-heavy, maximally shared finite Hadamard geometry is strictly less dangerous than the genuinely diffuse sharp mechanism, while the partner theorem simultaneously rules out arbitrary unit-smoothed fragmentation/translation as an asymptotic escape in the comparator. This is an equation-level use of the designated partner result, not a copied citation.

The partner's subsequent same-run comparison `math-open-problems@03a790a998540092501eafef53300a132070115e` further records that replacing two diffuse banks by arbitrary opposite-sign cap-one heavy laws creates a strict cone-tip gap below `3sqrt(2)`. Combined with (1.3), the still-unpaid sharp-witness directions are therefore off-center asymmetric fragmentation, shrinking smoothing scales, growing/nonperiodic shared-coordinate geometry, or coupled full-spectrum tails—not this symmetric four-coordinate core.

## 9. Correction discipline and remaining scope

This proof uses none of the live refuted interfaces: no independence after spectral rotation, no arbitrary-joint coarea estimate, no positive moment of worst conditional projection density, no fixed-fragment extremality assertion, no uniformly good minor assumption, and no law-uniform pointwise stationary-phase decay. The orthogonal transform is used only to compute the exact marginal induced by the original product cube, namely (2.5).

The theorem is a source-valid sharp-witness result, not the full QFORM theorem. The certified universal lower obstruction remains `C_univ>=3sqrt(2)` from the diffuse sequence, which is larger than the finite value here. What (1.3) adds is an exact global dense finite witness above `pi`, together with a complete no-escape proof for its two-sheet and one-sheet outputs.
