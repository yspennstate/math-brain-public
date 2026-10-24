SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B17, 2026-09-23T11:02:44Z.
attacking: multiscale three-bank stress with one vanishing-leverage mesoscopic row per bank; derive the exact first density deficit and test whether several shared mesoscopic rows can overshoot 3sqrt2.

# QFORM B17 — vanishing-leverage mesoscopic rows cannot improve the `3 sqrt(2)` diffuse obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T110244Z-account03-B17-QFORM-auto11`  
Assignment: sharp constant and witnesses  
Status: **NEW SUPPORTING SHARP-WITNESS THEOREM; FULL QFORM OPEN / NOT PROVED**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. The result

Let
\[
B_u=I_3-2uu^T,\qquad u\in S^2,
\]
so `spec(B_u)={1,1,-1}`.  For each `m`, choose three numbers
`0<=ell_{j,m}<1` with
\[
\max_j\ell_{j,m}\longrightarrow0.
\tag{1.1}
\]
For each bank `j`, take one distinguished physical coordinate of weight
`sqrt(ell_{j,m})` and `m` diffuse physical coordinates of weight
`sqrt((1-ell_{j,m})/m)`.  Put independent `Unif[-1/2,1/2]` variables on every
physical coordinate.  If `C_m` is the resulting `3 x (3m+3)` synthesis matrix
and
\[
A_m=C_m^TB_uC_m,
\tag{1.2}
\]
then
\[
C_mC_m^T=I_3,
\qquad
\boxed{\operatorname{spec}_{\ne0}(A_m)=\{1,1,-1\}}
\tag{1.3}
\]
for every finite `m`.

Set
\[
D_{j,m}:=\ell_{j,m}^2+{(1-\ell_{j,m})^2\over m},
\qquad
S_m:=\sum_{j=1}^3D_{j,m}.
\tag{1.4}
\]
Then the output has a continuous density for all sufficiently large `m`, and
uniformly for `u in S^2`,
\[
\boxed{
\|p_{X^TA_mX}\|_\infty
=3\sqrt2\left[
1-\sum_{j=1}^3 c_j(u)D_{j,m}+o(S_m)
\right],
}
\tag{1.5}
\]
where, with `x_j=u_j^2`,
\[
\boxed{
c_j(u)={57+6x_j-39x_j^2\over640}.}
\tag{1.6}
\]
Every coefficient is strictly positive, quantitatively
\[
\boxed{c_j(u)\ge {3\over80},}
\tag{1.7}
\]
and
\[
\boxed{
\sum_{j=1}^3c_j(u)
={177-39\sum_j u_j^4\over640}
\ge {69\over320}.}
\tag{1.8}
\]
Consequently every such vanishing-leverage mesoscopic perturbation approaches
the Gaussian obstruction **from below**.  In particular, several physical
rows may be much heavier than the `1/m` diffuse rows while their leverage still
vanishes, but they cannot create a first-order overshoot of `3 sqrt(2)` in this
exact product-provenance family.

This is stronger than a fixed `ell` perturbation: (1.5) allows arbitrary
relative scales among the three `ell_{j,m}` as long as each tends to zero.

## 2. Exact finite source-valid frame

Let `e_1,e_2,e_3` be the bank axes.  The columns of `C_m` belonging to bank
`j` are
\[
\sqrt{\ell_{j,m}}e_j,
\qquad
\underbrace{
\sqrt{(1-\ell_{j,m})/m}e_j,\ldots,
\sqrt{(1-\ell_{j,m})/m}e_j}_{m\text{ copies}}.
\tag{2.1}
\]
Therefore bank `j` contributes exactly
\[
\ell_{j,m}e_je_j^T+(1-\ell_{j,m})e_je_j^T=e_je_j^T
\]
to `C_mC_m^T`, proving (1.3).  No post-rotation independence is asserted.
All independence is in the original physical coordinates.

Writing `U_{j0},U_{jk}` for the physical uniforms and
\[
S_{j,m}=m^{-1/2}\sum_{k=1}^mU_{jk},
\]
the three bank variables are independent and equal to
\[
Y_{j,m}
=\sqrt{\ell_{j,m}}U_{j0}
 +\sqrt{1-\ell_{j,m}}S_{j,m}.
\tag{2.2}
\]
The quadratic output is exactly
\[
Q_m=Y_m^TB_uY_m.
\tag{2.3}
\]
Every finite member therefore satisfies the owner's original density-cap and
spectral hypotheses.

## 3. The bank local limit with a multiscale fourth-cumulant parameter

Put `sigma^2=1/12` and standardize one physical uniform by
`W=sqrt(12) U`.  Its characteristic function is
\[
\widehat f_W(t)=\operatorname{sinc}(\sqrt3\,t).
\]
For one bank define `Z_{j,m}=Y_{j,m}/sigma`.  Its exact characteristic
function is
\[
\Psi_{j,m}(t)
=
\operatorname{sinc}(\sqrt{3\ell_{j,m}}\,t)
\left[
\operatorname{sinc}\!\left(
\sqrt{ {3(1-\ell_{j,m})\over m}}\,t
\right)
\right]^m.
\tag{3.1}
\]
Using
\[
\log\operatorname{sinc}z
=-{z^2\over6}-{z^4\over180}-{z^6\over2835}+O(z^8),
\tag{3.2}
\]
one gets
\[
\log\Psi_{j,m}(t)
=-{t^2\over2}
-{D_{j,m}t^4\over20}
-{E_{j,m}t^6\over105}
+O(F_{j,m}t^8),
\tag{3.3}
\]
where
\[
E_{j,m}=\ell_{j,m}^3+{(1-\ell_{j,m})^3\over m^2}.
\tag{3.4}
\]
The key point is
\[
{E_{j,m}\over D_{j,m}}\longrightarrow0,
\tag{3.5}
\]
because `ell_{j,m}->0`; equivalently the largest squared coefficient in the
bank tends to zero.  Thus the fourth cumulant is the first non-Gaussian term
at every vanishing-leverage scale.

The weighted Fourier tail argument in the completed designated-partner report
`account04/B17`,

`yspennstate/math-open-problems@2156b76156ad5956c214a881fcfd6d977d6f3b9f`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B17/20260922T211900Z-account04-B17-QFORM-r3/REPORT.md`,

applies after replacing the equal-bank scale by
`sqrt((1-ell_{j,m})/m)`: eventually `1-ell_{j,m}>=1/2`, while the extra
`sinc(sqrt(3 ell)t)` factor has modulus at most one.  Hence the partner's
central Gaussian domination and outer Fourier-tail estimates remain uniform.
Applying the same finite number of Fourier derivatives gives
\[
\boxed{
g_{j,m}(y)
=\gamma_\sigma(y)
\left[1-{D_{j,m}\over20}H_4(y/\sigma)\right]
+o(D_{j,m})(1+|y|)^{-8}.}
\tag{3.6}
\]
This is the exact place where the completed partner analysis is used, not
merely cited.

Multiplying the three independent bank densities gives
\[
\rho_m(y)
=\gamma_\sigma^{(3)}(y)
\left[1-{1\over20}\sum_{j=1}^3D_{j,m}H_4(y_j/\sigma)\right]
+o(S_m)(1+|y|)^{-8}.
\tag{3.7}
\]
Cross-products of fourth-cumulant terms are `O(S_m^2)=o(S_m)`.

## 4. Uniform propagation through the indefinite quadratic pushforward

Let `T_u` denote pushforward by `q_u(y)=y^TB_uy`.  Since `B_u` is orthogonally
conjugate to `diag(1,1,-1)`, cylindrical coordinates give for the radial
majorant `w(y)=(1+|y|)^{-8}`
\[
\sup_{u\in S^2}\sup_s T_uw(s)
\le
\pi\int_{\mathbb R}(1+|z|)^{-8}dz
={2\pi\over7}.
\tag{4.1}
\]
Therefore (3.7) may be pushed through `q_u` uniformly in the output level and
orientation:
\[
p_{m,u}(s)
=p_0(s)-{1\over20}\sum_{j=1}^3D_{j,m}J_{u,j}(s)+o(S_m),
\tag{4.2}
\]
where
\[
J_{u,j}
=T_u\!\left[\gamma_\sigma^{(3)}H_4(y_j/\sigma)\right].
\tag{4.3}
\]
The functions `J_{u,j}(s)` are jointly continuous in `(u,s)`; the same radial
integrable majorant proves this by dominated convergence.

At the Gaussian endpoint, orientation disappears and
\[
Q_0\stackrel d=G_1^2+G_2^2-G_3^2,
\qquad G_j\sim N(0,1/12).
\tag{4.4}
\]
Its density has unique global maximum at zero and
\[
\boxed{p_0(0)=3\sqrt2.}
\tag{4.5}
\]
For `s>=0`, explicitly `p_0(s)=3sqrt(2)e^{-6s}`; on the negative side strict
monotonicity of the `chi^2_1` density inside the convolution gives
`p_0(s)<p_0(0)`.

Uniform convergence in (4.2) forces every maximizing output level to tend to
zero.  Evaluating (4.2) at a maximizer for the upper bound and at zero for the
lower bound shows that the first correction to the **global** supremum is the
cone-tip correction.  Thus it remains only to compute `J_{u,j}(0)`.

## 5. Exact cone moment and positivity

Choose an orthogonal spectral basis whose minority-sign axis is `u` and write
`x_j=u_j^2`.  On either nappe of the isotropic cone, a spectral direction is
`w=(cos theta,sin theta,epsilon)`, `epsilon=+-1`.  Let `a_j` be its `j`th
original-coordinate component.  Angular averaging gives
\[
\mathbb E a_j^2={1+x_j\over2},
\tag{5.1}
\]
\[
\mathbb E a_j^4
={3\over8}(1-x_j)^2+3x_j(1-x_j)+x_j^2.
\tag{5.2}
\]
Under the normalized Gaussian cone measure, if `r/sigma=q`, then
\[
\mathbb E q^2={1\over2},
\qquad
\mathbb E q^4={3\over4}.
\tag{5.3}
\]
Since `H_4(z)=z^4-6z^2+3`, (5.1)--(5.3) yield
\[
{J_{u,j}(0)\over p_0(0)}
={57+6x_j-39x_j^2\over32}.
\tag{5.4}
\]
Multiplying by `1/20` gives (1.6).

The quadratic `57+6x-39x^2` is concave on `[0,1]`; its endpoint values are
`57` and `24`.  Hence (1.7).  Summing and using
`sum x_j=1`, `sum x_j^2<=1` gives (1.8).  Substitution in (4.2) proves (1.5).

A useful uniform corollary is
\[
\boxed{
\|p_{Q_m}\|_\infty
\le3\sqrt2\left[
1-\left({3\over80}+o(1)\right)S_m
\right].}
\tag{5.5}
\]
Thus the diffuse Gaussian endpoint is a strict local maximum against this
entire three-parameter mesoscopic deformation.

## 6. Critical `m^{-1/2}` leverage and exact application to the partner witness

The transition scale is especially transparent when
\[
\ell_{j,m}={\alpha_j\over\sqrt m},
\qquad \alpha_j\ge0\text{ fixed}.
\tag{6.1}
\]
Then
\[
D_{j,m}
={1+\alpha_j^2\over m}
-{2\alpha_j\over m^{3/2}}
+O(m^{-2}),
\tag{6.2}
\]
and therefore
\[
\boxed{
\|p_{Q_m}\|_\infty
=3\sqrt2\left[
1-{1\over m}\sum_{j=1}^3c_j(u)(1+\alpha_j^2)
+o(m^{-1})
\right].}
\tag{6.3}
\]

Now take exactly the designated partner's rational rotation
\[
O={1\over7}
\begin{pmatrix}
6&-2&-3\\
-2&3&-6\\
-3&-6&-2
\end{pmatrix},
\qquad
B=O^T\operatorname{diag}(1,1,-1)O
={1\over49}
\begin{pmatrix}
31&-36&-12\\
-36&-23&-24\\
-12&-24&41
\end{pmatrix}.
\tag{6.4}
\]
Its minority-axis squared coordinates are
\[
(x_1,x_2,x_3)=\left({9\over49},{36\over49},{4\over49}\right).
\tag{6.5}
\]
Formula (1.6) gives
\[
(c_1,c_2,c_3)
=\left(
{17043\over192080},
{96897\over1536640},
{137409\over1536640}
\right),
\tag{6.6}
\]
and, exactly,
\[
\boxed{
\sum_jc_j={5295\over21952}.}
\tag{6.7}
\]
This reproduces the completed account04/B17 coefficient
\[
p_{Q_m}^{\rm partner}(0)
=3\sqrt2\left(1-{5295\over21952m}+O(m^{-2})\right)
\tag{6.8}
\]
from a different calculation and now places it inside the mesoscopic family.
Combining (6.3), (6.7), and the pointwise lower bound (1.7) yields the actual
partner-comparison inequality
\[
\boxed{
\sum_jc_j(1+\alpha_j^2)
\ge {5295\over21952}+{3\over80}\sum_j\alpha_j^2.}
\tag{6.9}
\]
Hence every nonzero critical mesoscopic perturbation has a strictly **larger**
first density deficit than the partner's pure diffuse witness.  For equal
`alpha_j=alpha`,
\[
\boxed{
\|p_{Q_m}\|_\infty
=3\sqrt2\left[
1-(1+\alpha^2){5295\over21952m}+o(m^{-1})
\right].}
\tag{6.10}
\]
For `alpha=1` the coefficient is exactly `5295/10976`, twice the partner
coefficient.

The partner theorem also supplies the source-valid lower obstruction
\[
\boxed{C_{\rm universal}\ge3\sqrt2,}
\tag{6.11}
\]
because its finite inputs are independent cap-one uniforms and its finite
matrices already have exact nonzero spectrum `{1,1,-1}`.

## 7. Scaling interpretation

For equal leverage `ell_m` in all three banks:

- if `ell_m=o(m^{-1/2})`, then `D_{j,m}=m^{-1}+o(m^{-1})`; the special rows are
  invisible at first order and one recovers the partner diffuse correction;
- if `ell_m=alpha m^{-1/2}`, (6.10) is the exact critical crossover;
- if `m^{-1/2}<<ell_m->0`, then `D_{j,m}~ell_m^2`, so the negative gap from
  `3sqrt2` is much larger than the diffuse `1/m` gap.

Thus a finite number of vanishing-leverage mesoscopic rows does not offer a
route above `3sqrt2`; within this source-valid architecture the most dangerous
configuration is the most diffuse one.

## 8. Continuity and exact scope

For large `m` every bank density in (2.2) is continuous and compactly
supported.  The cylindrical representation of the nondegenerate rank-three
quadratic pushforward, together with dominated convergence at the cone tip,
gives a continuous output density for this family.  This is a **family-level**
continuity statement only.  Full-target continuity remains open.

The theorem does **not** prove the unrestricted conjecture.  It assumes the
exact three-bank rank-three architecture, centered unit-interval physical
inputs, and one distinguished row plus an equal diffuse remainder in each
bank.  It does, however, exclude the next natural sharp-witness mechanism:
several shared mesoscopic physical rows whose leverage vanishes more slowly
than the diffuse bank leverage.

The next nonredundant B17 stress should therefore let the non-Gaussian
finite-leverage component survive at order one, or break the orthogonal
three-bank architecture so that mesoscopic rows couple non-collinearly before
the quadratic map.

## 9. Correction discipline

This proof uses no law-uniform pointwise van-der-Corput estimate, no
post-rotation independence, no arbitrary-joint coarea inequality, no
conditional projection-density moment, no bounded-support reduction, and no
histogram extremality claim.  The only coarea step is an exact computation for
the explicit rank-three family with full product provenance retained before
the spectral rotation.

Full QFORM remains **OPEN / NOT PROVED**.  The universal lower obstruction
remains `3sqrt2`; this run constrains a multiscale witness route rather than
claiming the universal upper theorem.
