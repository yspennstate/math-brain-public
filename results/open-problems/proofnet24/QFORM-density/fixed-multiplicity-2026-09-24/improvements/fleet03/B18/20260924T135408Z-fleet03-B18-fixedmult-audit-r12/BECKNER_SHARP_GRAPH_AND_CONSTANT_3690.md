# fleet03/B18 r12 — Beckner sharp Hausdorff–Young transfer, stronger graph determinant, and 3690 constant

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T135408Z-fleet03-B18-fixedmult-audit-r12`  
Pinned manuscript source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned manuscript SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`

## Status

The 17-eigenvalue bounded-density theorem remains PASS in this B18 audit lineage. This run gives a new same-scope quantitative improvement, but **does not lower the multiplicity threshold below 17**. The full three-eigenvalue conjecture remains OPEN / NOT PROVED / NOT DISPROVED, and full-target continuity remains OPEN.

The new source transfer is the sharp Babenko–Beckner Hausdorff–Young inequality. It improves the scalar Fourier-power input used by the manuscript's graph Brascamp–Lieb proof and, after propagating constants through the quarter-power/pivot chain, sharpens the same-scope theorem constant from this slot's prior `3810` to `3690`.

## 1. Primary-source theorem and exact Fourier convention

Beckner, *Inequalities in Fourier Analysis*, Ann. of Math. 102 (1975), 159–182, proves the sharp Hausdorff–Young inequality. In the normalization

\[
\mathcal F_0 f(\xi)=\int_{\mathbb R}e^{-2\pi i x\xi}f(x)\,dx,
\]

if `1<=r<=2`, `q=r/(r-1)>=2`, then

\[
\|\mathcal F_0 f\|_q
\le
\left(\frac{r^{1/r}}{q^{1/q}}\right)^{1/2}\|f\|_r.
\tag{1.1}
\]

For the manuscript convention

\[
\widehat f(t)=\int e^{itx}f(x)\,dx,
\]

we have `||fhat||_q=(2 pi)^(1/q)||F_0f||_q`.

If `f` is a probability density satisfying `0<=f<=1`, then `||f||_r<=1` for every `r>=1`. Therefore for every `q>=2`, with `r=q/(q-1)`, Beckner gives the exact bound

\[
\boxed{
\int_{\mathbb R}|\widehat f(t)|^qdt
\le
2\pi\,q^{-1/2}
\left(\frac q{q-1}\right)^{(q-1)/2}.}
\tag{1.2}
\]

This uses no moment, centering, iid, smoothness, support or log-concavity assumption. It is valid for the arbitrary rough cap-one scalar densities in the manuscript.

## 2. Exact row-factor estimate for the graph Brascamp–Lieb proof

Use the manuscript's fourth-power decoupling for

\[
Z=F(X_I)+2X_I^TMX_J+G(X_J),
\]

where `I,J` are disjoint banks of original independent cap-one coordinates and `F,G` are arbitrary measurable real phases. With `a=2t`, `D=X_J-X'_J`, and the manuscript notation

\[
H=\alpha I+a^2M^TM,
\qquad
c_j=\alpha e_j^TH^{-1}e_j,
\qquad
d_i=a^2m_i^TH^{-1}m_i,
\]

we have `0<=c_j,d_i<=1` and

\[
\theta:=\sum_i d_i=\sum_j(1-c_j).
\]

For `0<d<=1`, put `q=2/d`. Equation (1.2) yields

\[
\int|\widehat f|^{2/d}
\le
2\pi\sqrt{d/2}
\left(\frac2{2-d}\right)^{(2-d)/(2d)}.
\tag{2.1}
\]

Hence the row factor appearing after geometric Brascamp–Lieb is bounded by

\[
 d^{-d/2}\left(\int|\widehat f|^{2/d}\right)^d
\le
(2\pi)^d 2^{-d/2}
\left(\frac2{2-d}\right)^{(2-d)/2}.
\tag{2.2}
\]

Define

\[
\psi(d)
=-\frac d2\log2
+\frac{2-d}{2}\log\frac2{2-d}.
\]

Then `psi(0)=0`,

\[
\psi'(0)=\frac{1-\log2}{2}=:c,
\qquad
\psi''(d)=-\frac1{2(2-d)}<0.
\]

By concavity,

\[
\psi(d)\le cd
\qquad (0\le d\le1).
\tag{2.3}
\]

Therefore the product of all row factors is at most

\[
(2\pi e^c)^\theta.
\tag{2.4}
\]

The manuscript's column entropy estimate is unchanged:

\[
\prod_j c_j^{-c_j/2}\le e^{\theta/2}.
\tag{2.5}
\]

After extracting `det(H)^(-1/2)` and the alpha powers, the complete nondeterminant factor is

\[
\left(
\frac{2\pi e^{c+1/2}}{\sqrt\alpha}
\right)^\theta.
\]

Since

\[
c+\frac12=1-\frac12\log2,
\qquad
e^{c+1/2}=\frac e{\sqrt2},
\]

choose

\[
\alpha=2\pi^2e^2.
\]

The entropy factor then cancels exactly.

## 3. New determinant theorem

The preceding computation gives

\[
|\phi_Z(t)|^4
\le
\det\left(I+\frac{4t^2}{2\pi^2e^2}M^TM\right)^{-1/2}.
\]

Thus

\[
\boxed{
|\phi_Z(t)|
\le
\det\left(I+\frac{2t^2}{\pi^2e^2}M^TM\right)^{-1/8}.}
\tag{3.1}
\]

Call this `QFORM-BECKNER-SHARP-GRAPH-v1`.

Comparison at identical hypotheses:

- pinned manuscript coefficient: `1/(pi^2 e^2)`;
- prior B18 Rudelson–Vershynin transfer: `1/(2 pi^2 e)`;
- present Beckner transfer: `2/(pi^2 e^2)`.

Numerically `2/e^2 > 1/(2e)`, so (3.1) strictly strengthens the prior B18 determinant estimate as well as the manuscript estimate.

No independence after a rotation is used: the only independence is in the original-coordinate banks before deterministic linear maps, exactly as in the manuscript's decoupling proof.

## 4. Crossing-volume consequences

Let

\[
Z_k(M)=\sum_{|S|=|T|=k}\det(M[S,T])^2.
\]

Cauchy–Binet and (3.1) give

\[
|\phi_Z(t)|
\le
\min\left\{1,
\left(\frac{u_k}{|t|}\right)^{k/4}\right\},
\qquad
u_k=\frac{\pi e}{\sqrt2}\,Z_k(M)^{-1/(2k)}.
\tag{4.1}
\]

Thus for `k=5`, the manuscript's power-envelope lemma gives

\[
\boxed{
\|p_Z\|_\infty
\le
\frac{5e}{\sqrt2}\,Z_5(M)^{-1/10}.}
\tag{4.2}
\]

For `k=3`, its half-Riesz estimate becomes

\[
\boxed{
\sup_a\mathbb E|Z-a|^{-1/2}
\le
12\sqrt{\frac{e}{2\sqrt2}}\,Z_3(M)^{-1/12}.}
\tag{4.3}
\]

On the manuscript's random-cut witness, `Z_3(M)^(-1/6)<=160`; therefore

\[
12\sqrt{\frac{80e}{\sqrt2}}<150.
\tag{4.4}
\]

A rational verification of the last strict inequality is obtained from `e<11/4` and `sqrt(2)>140/99` (the latter because `140^2<2*99^2`): after squaring, the left side is bounded by

\[
\frac{11520(11/4)}{140/99}
=\frac{156816}{7}<22500=150^2.
\]

For the order-five random-cut witness, `Z_5(M)^(-1/10)<=160`, so the no-pivot density is below

\[
\frac{800e}{\sqrt2}<1600.
\tag{4.5}
\]

These sharpen constants only; they do not change the structural threshold.

## 5. Sharper quarter-power concentration

If `R=X^TAX+b^TX+c` and `||A||=L`, the manuscript's random sign cut produces a cross block `M` with `||M||>=L/4`. Retaining one singular factor in (3.1) gives

\[
|\phi_R(t)|
\le
2^{3/8}(\pi e)^{1/4}(L|t|)^{-1/4}.
\tag{5.1}
\]

Run the manuscript's Gaussian smoothing argument. The factor `e^v v^{-1/8}` is minimized at `v=1/8`; using

\[
\int_{\mathbb R}e^{-u t^2}|t|^{-1/4}dt
=u^{-3/8}\Gamma(3/8)
\]

gives

\[
\boxed{
\Pr\{|R-a|<\rho\}
\le
\min\{1,C_B(\rho/L)^{1/4}\},}
\tag{5.2}
\]

where

\[
\boxed{
C_B=\sqrt2\,e^{3/8}\pi^{-1/4}\Gamma(3/8).}
\tag{5.3}
\]

This is strictly smaller than the prior B18 Rudelson–Vershynin constant.

For a coarse fully explicit bound sufficient below, `C_B<4`. One elementary route is:

1. `Gamma(3/8)<5/2`. For completeness, on `[0,1]`, `e^{-t}<=1-t+t^2/2`, giving `1348/627`. On `[1,infinity)`, integration by parts gives
   `I_1=e^{-1}-(5/8)int_1^infinity t^{-13/8}e^{-t}dt`; restricting the subtracted integral to `[1,2]`, using `2^{-13/8}>3/10`, `e^{-1}>4/11`, `e^{-2}<7/50`, and `e^{-1}<3/8`, yields a tail small enough that the total is `<5/2`.
2. The prefactor `P=sqrt2 e^{3/8} pi^{-1/4}` is `<8/5`: indeed `P^4=4e^{3/2}/pi`, while `e<11/4`, `sqrt(e)<5/3`, `pi>3` give `P^4<55/9<(8/5)^4`.

Hence `C_B<4`.

Since `log 4<7/5`, the manuscript's layer-cake calculation gives, for `L>=1`,

\[
\boxed{
\sup_a\mathbb E\log_+\frac1{|R-a|}
<4+4\cdot\frac75=\frac{48}{5}.}
\tag{5.4}
\]

## 6. Propagation through the `s_9` half-potential compiler

Keep the manuscript's `eta=1/100` and all original hypotheses.

### No pivot

Equation (4.4) gives full half-potential `<150`.

### Scalar pivot

The manuscript's exact scalar-square kernel gives

\[
H(Q):=\sup_a\mathbb E\bigl[|Q-a|^{-1/2};|Q-a|\le1\bigr]
\le
\eta^{-1/2}(8+3L_0),
\]

where `L_0` is the translated logarithmic-potential constant. By (5.4),

\[
H(Q)<10\left(8+3\frac{48}{5}\right)=368.
\tag{6.1}
\]

### Definite pair

The manuscript gives `<40 pi<368`.

### Indefinite pair

Here the relevant conditional bound is

\[
D^{-1/2}\{32+4\log(16\sqrt D)\},
\qquad D\ge\eta=10^{-2},
\]

because `16 sqrt(D)>1` throughout this range. Put `x=sqrt(D)>=1/10`. Then

\[
f(x)=\frac{32+4\log(16x)}x,
\quad
f'(x)=\frac{-28-4\log(16x)}{x^2}<0.
\]

Thus the maximum is at `x=1/10`:

\[
f(x)\le10\{32+4\log(8/5)\}<340,
\tag{6.2}
\]

where `log(8/5)<1/2` follows from `e>8/3>(8/5)^2`.

Therefore every pivot/no-pivot branch under `s_9(A)>=1` has truncated half-potential `<368`. Adding the contribution from `|Q-a|>1`, which is at most one, yields

\[
\boxed{
 s_9(A)\ge1
 \Longrightarrow
 \sup_a\mathbb E|Q-a|^{-1/2}<369.}
\tag{6.3}
\]

## 7. Same-scope 17-eigenvalue theorem with constant 3690

Run the pinned manuscript's normalized `s_17(A)>=1` case split without changing any structural argument.

- no pivot: by (4.5), density `<1600`;
- scalar pivot: the Schur complement retains at least nine singular directions and the scalar square profile costs `eta^{-1/2}=10`, so (6.3) gives density `<3690`;
- definite pair: `<10 pi`;
- indefinite pair: the manuscript's logarithmic receiver remains far below `3690`.

Scaling `Y=KX`, `A'=A/K^2`, `b'=b/K`, followed by division by `s`, is exactly the manuscript scaling. Hence

\[
\boxed{
 s_{17}(A)\ge s>0
 \quad\Longrightarrow\quad
 \|p_{X^TAX+b^TX+c}\|_\infty
 <3690\,\frac{K^2}{s}.}
\tag{7.1}
\]

Call this `QFORM-FIXED17-BECKNER-CONSTANT-3690-v1`.

All original theorem quantifiers are retained: arbitrary dimension, arbitrary real symmetric `A`, all signatures and remaining spectrum, arbitrary affine `b,c`, and independent rough non-identical coordinates with densities bounded by `K`.

Continuity is not newly asserted in pivot branches.

## 8. Threshold reduction attempt: why Beckner does not by itself prove `s_13` L-infinity

The structural manuscript argument under `s_13(A)>=1` supplies an order-four crossing volume. Equation (4.1) then gives the endpoint envelope

\[
|\phi(t)|\lesssim |t|^{-1}.
\]

The Beckner source improves its constant but not its exponent. Therefore absolute Fourier inversion still has a logarithmically divergent majorant. This source transfer alone does **not** prove an unconditional 13-eigenvalue bounded-density theorem.

The prior B18 leverage-gapped fractional determinant still closes every order-four witness with a fixed row-leverage gap. The genuine surviving analytic case is a physical row with leverage tending to one. The sharp algebraic examples already present in the package show that simply changing `rank R<=3r` to `2r`, or retuning `eta/kappa`, cannot remove the `m>=4r+1` structural threshold.

Thus this run lowers the theorem constant but **not** its multiplicity. A true `17 -> 13` L-infinity improvement still needs an endpoint order-four receiver, a heavy-row physical hub/curved-fiber argument retaining same-bank phases, or a product-preserving repartition theorem that forces a leverage gap.

## 9. Application of the designated fleet04/B18 result to an actual inequality

The latest consumed fleet04/B18 r6 theorem proves that for its two-sided-anchor packet, if `c_1,c_2` are the top two singular values of `P_r C`, then

\[
\|p_Q\|_\infty\le\frac{2\sqrt{2\pi}}{\sqrt{c_1c_2}}.
\tag{9.1}
\]

Apply it to the literal owner-target family

\[
Q_{\varepsilon,\lambda}
=2X_1Y_1+2\varepsilon X_2Y_2+\lambda W^2,
\qquad0<\varepsilon<1,\ \lambda\ge1.
\]

Its coefficient matrix has eigenvalues

\[
\{1,-1,\varepsilon,-\varepsilon,\lambda\},
\]

so it has exactly three eigenvalues of modulus at least one. Here `r=0`, `C=diag(1,epsilon)`, hence `c_1=1`, `c_2=epsilon` and the partner theorem gives

\[
\boxed{
\|p_Q\|_\infty\le\frac{2\sqrt{2\pi}}{\sqrt\varepsilon}.}
\tag{9.2}
\]

At `epsilon=1/2`, this is `4 sqrt(pi)`. This concrete application is only a supporting control family; it is not used to claim the fixed-17 theorem or full-three-eigenvalue theorem.

## 10. Primary-source/prior-art status

The source match in this run is Beckner's sharp Hausdorff–Young theorem; it exactly covers the scalar Fourier step after the cap-one density observation `||f||_r<=1`.

Other previously checked primary sources retain their earlier scope:

- Rudelson–Vershynin gives the sharp bounded-density normalized linear-sum theorem and remains valid, but Beckner is stronger for the scalar Fourier-power constant needed by this graph proof.
- Livshyts–Paouris–Pivovarov gives sharp product marginal density caps; it does not solve arbitrary same-bank quadratic phases by itself.
- Banks–Garza Vargas–Kulkarni–Srivastava gives bilinear-affine density results, but does not directly cover `F(X_I)+2X_I^TMX_J+G(X_J)` with arbitrary same-bank phases.
- Herry–Malicet–Poly requires substantially smoother/iid input structure and does not match the arbitrary rough/non-iid theorem.

No exact published theorem was found in the checked primary sources that solves the unrestricted three-eigenvalue conjecture with all owner quantifiers.

## 11. Audit verdict and next obligation

- pinned 17-eigenvalue theorem: **PASS in this B18 audit lineage**;
- same-scope constant: **improved from 3810 to 3690**;
- unconditional 13-eigenvalue L-infinity theorem: **OPEN**;
- full three-eigenvalue L-infinity conjecture: **OPEN**;
- full-target continuity: **OPEN**.

The next mathematical obligation is the same heavy-leverage order-four endpoint, now with the sharp scalar Hausdorff–Young constant fully paid. Further constant tuning cannot lower the multiplicity threshold by itself.
