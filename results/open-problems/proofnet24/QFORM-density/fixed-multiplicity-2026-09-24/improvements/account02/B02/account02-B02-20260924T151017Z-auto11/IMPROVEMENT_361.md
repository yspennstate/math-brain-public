# account02/B02 auto11 — nine directions with constant 361

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

Status: **PROVED CANDIDATE IMPROVEMENT / NOT YET TWO-REVIEW VALIDATED.** This retunes the independently reviewed nine-eigenvalue `400` manuscript after repairing its harmless negative-tail coordinate notation. It proves the same multiplicity-nine theorem with the sharper constant `<361`. It does not prove multiplicity eight or the unrestricted three-eigenvalue conjecture.

## Theorem

Let `X=(X_1,...,X_n)` have independent real coordinate densities bounded by `K`, let `A=A^T`, and let `b,c` be arbitrary. If

\[
s_9(A)\ge s>0,
\]

then `Q=X^TAX+b^TX+c` has an essentially bounded density and

\[
\boxed{\ \|p_Q\|_\infty<361\,K^2/s.\ }
\]

The complete analytic receiver and pivot lemmas are those proved in the pinned standalone nine-direction source `paper.tex`, source commit `eeb752c8943536541b34b42b8bf48e924f4d3d2f`, blob `19fb119877426b640b2c0dae19ec2f78a399fe11`, SHA-256 `bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3`, independently reviewed in this run. The only change below is a rational retuning of the three structural parameters together with sharper elementary constant bookkeeping.

## 1. Analytic constants retained from the reviewed proof

For every literal physical cross block `M`, arbitrary same-bank and outside quadratic/affine phases retained,

\[
\|p_Q\|_\infty\le C_3 Z_3(M)^{-1/6},
\qquad
C_3=3\sqrt2\,e(9/2)^{1/6},
\tag{1}
\]

and

\[
\sup_a E|Q-a|^{-1/2}\le C_2 Z_2(M)^{-1/8},
\qquad
C_2=8\sqrt e\,2^{-1/8}.
\tag{2}
\]

A useful rational certificate for (1) is

\[
C_3<\frac{232551}{15680}.
\tag{3}
\]

Indeed `sqrt2<99/70`, `e<87/32`, and `(9/2)^(1/6)<9/7`. The first and third inequalities follow by squaring/sixth powers (`9801>9800` and `2*9^5>7^6`); for `e<87/32`, the exponential series through degree four plus the geometric tail bound gives `e<65/24+1/100<87/32`. Likewise

\[
C_2<13,
\tag{4}
\]

because `C_2^2=64e2^{-1/4}<64(11/4)(6/7)=1056/7<169`.

For the scalar logarithmic branch define

\[
J_0=\pi+4\log2,
\qquad L_0=4+4\log5.
\]

Use the elementary rational bounds

\[
\pi<\frac{22}{7},\qquad
\log2<\frac{347}{500},\qquad
\log5<\frac{161}{100}.
\tag{5}
\]

The logarithm bounds are certified by positive Taylor sums:

\[
\sum_{j=0}^4\frac{(347/500)^j}{j!}
=\frac{3000289173281}{1500000000000}>2,
\]

and

\[
\sum_{j=0}^7\frac{(161/100)^j}{j!}
=\frac{40011628664174467}{8000000000000000}>5.
\]

Consequently

\[
J_0+2L_0<\frac{23449}{875}=26.798857\ldots,
\tag{6}
\]

and

\[
6+\log16+L_0<\frac{2402}{125}=19.216.
\tag{7}
\]

The reviewed full pair half-potential remains

\[
\sup_a E|Q-a|^{-1/2}<16D^{-1/4}
\tag{8}
\]

for a physical two-coordinate quadratic block with determinant modulus `D>0`.

## 2. Retuned structural parameters

Normalize `K=s=1` and set

\[
d=\frac{47}{625},\qquad
p=\frac{57}{20000},\qquad
h=\frac{411}{5000},\qquad
\kappa=h^2.
\tag{9}
\]

A scalar pivot means `|A_ii|>=d`; a pair pivot means a principal two-coordinate determinant has modulus at least `p`.

If no pivot exists, then

\[
|A_{ii}|<d,
\qquad
|A_{ij}|^2<p+d^2=\frac{106313}{12500000}.
\]

Since

\[
\frac{106313}{12500000}
<\left(\frac{923}{10000}\right)^2
\]

(the difference is `57/4000000`), we may write

\[
|A_{ij}|<q:=\frac{923}{10000}.
\tag{10}
\]

### Spectral-to-volume proposition for `k<=3`

If `A` has no pivot and `s_{4k-3}(A)>=1`, `1<=k<=3`, then

\[
V_k(A)\ge\kappa^k.
\tag{11}
\]

The proof is the reviewed interpolation/completion proof with the new constants. If `V_k<kappa^k`, select `0<=r<=k-1<=2` with `V_{r+1}<kappa V_r`. At `r=0`, `||A||<d+h<1`. For `r=1,2`, completion gives `A=D+R+E`, `rank R<=3r`, `rank R[L,L]<=r`, zero-diagonal `E`, and `||E||_F<(r+1)h`. Rank subtraction forces `r+1` diagonal entries of `D` on `L` of modulus at least `1-(r+1)h`. On those coordinates strict row diagonal dominance follows from

\[
1-d-q-4h>0\quad(r=1),
\qquad
1-d-2q-9h>0\quad(r=2).
\]

With (9)--(10) these margins are explicitly

\[
\frac{5037}{10000}>0,
\qquad
\frac1{2500}>0.
\tag{12}
\]

Thus `R[L,L]` would have rank at least `r+1`, a contradiction. This proves (11).

A fair physical coordinate cut gives

\[
Z_3(M)^{-1/6}\le\frac2h=\frac{10000}{411},
\tag{13}
\]

and, at order two,

\[
Z_2(M)^{-1/8}\le\sqrt{\frac2h}.
\tag{14}
\]

## 3. Nine-direction branch bounds

Assume `s_9(A)>=1`.

### No pivot

By (3), (11), (13), and the order-three receiver,

\[
\|p_Q\|_\infty
<\frac{232551}{15680}\frac{10000}{411}
=\frac{9689625}{26852}
<361,
\tag{15}
\]

since `361*26852-9689625=3947>0`.

### Scalar pivot

The Schur complement retains at least eight unit-scale spectral directions, hence at least five. Apply the reviewed five-direction full-half-potential trichotomy.

If its Schur remainder has no pivot, (2), (4), and (14) give after the outer square profile

\[
C_2\sqrt{\frac{2}{dh}}<13\cdot18=234<361,
\tag{16}
\]

because `2/(dh)=6250000/19317<324`.

If the Schur remainder has a pair pivot, (8) gives

\[
16p^{-1/4}d^{-1/2}<16\cdot\frac92\cdot\frac{15}{4}=270<361.
\tag{17}
\]

Here `p^{-1/4}<9/2` because `57/20000>(2/9)^4`, and `d^{-1/2}<15/4` because `47/625>16/225`.

If the Schur remainder has a scalar pivot, the reviewed scalar convolution/logarithmic argument gives the outer density bound

\[
d^{-1/2}+\frac{J_0+2L_0}{d}.
\]

Using (6) and `d^{-1/2}<15/4`,

\[
\|p_Q\|_\infty
<\frac{15}{4}+\frac{23449}{875}\frac{625}{47}
=\frac{473915}{1316}
<361,
\tag{18}
\]

with slack `1161/1316`.

### Definite pair pivot

The direct two-dimensional Jacobian estimate gives

\[
\|p_Q\|_\infty\le\pi p^{-1/2}
<\frac{22}{7}\frac{75}{4}<59<361,
\tag{19}
\]

where `p^{-1/2}<75/4` because `20000/57<5625/16` (`320000<320625`).

### Indefinite pair pivot

The pair Schur complement retains at least seven unit-scale spectral directions, so the quarter-power logarithmic estimate applies to its critical value. The reviewed averaging calculation yields

\[
\|p_Q\|_\infty
\le p^{-1/2}(6+\log16+L_0)+\frac1e.
\]

Using (7), `p^{-1/2}<75/4`, and `1/e<1/2`,

\[
\|p_Q\|_\infty
<\frac{75}{4}\frac{2402}{125}+\frac12
=\frac{1804}{5}=360.8<361.
\tag{20}
\]

All normalized cases are therefore strictly below 361.

## 4. Scaling

For arbitrary `K,s`, let `Y=KX` and

\[
\widetilde Q=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c.
\]

Then the coordinates of `Y` have density cap one, `s_9(A/s)>=1`, and `Q=(s/K^2)\widetilde Q`. One-dimensional density scaling gives

\[
\boxed{\|p_Q\|_\infty<361K^2/s.}
\]

## 5. Endpoint obstruction and status

The B02 exact-law tests still rule out a shortcut through scalar Fourier exponents or an order-two density endpoint. The cap-one Gaussian has exactly `int |fhat|^q=2*pi/sqrt(q)`, so the Fourier-power exponent is sharp. For independent `Unif[-1/2,1/2]`, `X^2` has density `s^-1/2` on `(0,1/4)`, and `X_1^2-X_2^2` has infinite density at zero. Therefore the unresolved eight-direction branch must spend the new overlap/shared-coordinate structure, not merely sharpen `E_2` constants.

The `<361` retuning has only this one complete review and is **not** release-validated. The independently reviewed `400` candidate remains the stronger-validation checkpoint from this run; the earlier immutable `<536` note is superseded numerically but preserved. Multiplicity eight and unrestricted three-eigenvalue QFORM remain open.
