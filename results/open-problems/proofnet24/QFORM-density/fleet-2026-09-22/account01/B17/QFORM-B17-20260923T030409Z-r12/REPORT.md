# QFORM B17 — exact null-pair plus square theorem

Run: `QFORM-B17-20260923T030409Z-r12`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: `NEW_SUPPORTING_THEOREM`; full QFORM remains **OPEN / NOT PROVED**. Full-target continuity remains separately open.  
Execution context: scheduled automation; `WITHOUT_VERIFIED_BRAIN`.

Fresh pre-write source: `yspennstate/math-research-brain` main observed through commit `82fae37e4028645a13616a93075a54da0897c0da`; OWNER CONTROL revision `2026-09-22.15`; control README blob `fca13a89d221115332ce5e60d49554ee0e213efa`; fresh correction inbox blob `c7000cf3822ae4935a2faf43b89ac92ea65ac0fe`. The proof below uses none of the refuted arbitrary-joint coarea, post-rotation independence, uniform pointwise oscillatory decay, conditional-cap, fiber-supremum, fixed-fragment-count, one-minor, or universal-cross-cut interfaces.

## 1. New theorem

### QFORM-NULLPAIR-SQUARE-GLOBAL-4-v1

Let `X,Y,Z` be independent real random variables with probability densities `f_X,f_Y,f_Z` satisfying

\[
0\le f_X,f_Y,f_Z\le 1.
\]

Let `a,b` be nonzero reals and set

\[
Q=2aXY+bZ^2.
\]

Then `Q` has a continuous density and

\[
\boxed{\|p_Q\|_\infty\le \frac{4}{\sqrt{|ab|}}.}
\tag{1}
\]

In particular, if `|a|>=1` and `|b|>=1`, then

\[
\boxed{\|p_Q\|_\infty\le4<3\sqrt2.}
\tag{2}
\]

The matrix

\[
A_{a,b}=\begin{pmatrix}0&a&0\\a&0&0\\0&0&b\end{pmatrix}
\]

has eigenvalues `{a,-a,b}`. Thus (2) is an exact original-coordinate, genuinely non-diagonal target family with three eigenvalues of magnitude at least one and **arbitrary** independent cap-one input laws. No Gaussian limit, moment hypothesis, centering, support connectedness, or rearrangement of the source law is assumed.

The same bound survives arbitrary affine terms:

\[
2aXY+bZ^2+\alpha X+\beta Y+\gamma Z+c,
\]

because independent translations complete the bilinear and square terms. Consequently, if an ambient quadratic form has a physical principal block exactly `A_{a,b}`, then after conditioning on every outside **original coordinate**, all outside couplings enter only as affine terms and the full ambient form obeys the same bound (1), uniformly in the conditioning.

---

## 2. Square-density envelope

By reflecting the output if necessary, it is enough to take `b>0`. Let

\[
W=bZ^2.
\]

For `w>0`, `W` has density

\[
k_b(w)
=\frac{f_Z(\sqrt{w/b})+f_Z(-\sqrt{w/b})}{2\sqrt{bw}}
\le \frac1{\sqrt{bw}}.
\tag{3}
\]

This is the only use of the cap on the third input. Notice that (3) is source-valid in the original physical coordinate; no rotated-coordinate density claim is made.

---

## 3. First bathtub: the `X` coordinate

Fix `y\ne0`. Conditional on `Y=y`, the variable

\[
Q_y=2ayX+W
\]

has density

\[
p_y(s)=\int_{\mathbb R} f_X(x)k_b(s-2ayx)\,dx.
\tag{4}
\]

Using (3),

\[
p_y(s)
\le \frac1{\sqrt b}
\int f_X(x)(s-2ayx)_+^{-1/2}\,dx.
\tag{5}
\]

Assume first `ay>0` and write `c=s/(2ay)`. Then

\[
(s-2ayx)_+^{-1/2}
=(2|ay|)^{-1/2}(c-x)_+^{-1/2}.
\]

Among all `0<=f<=1` with integral one, the integral against the decreasing kernel `u^{-1/2}` is maximized by filling the unit interval immediately adjacent to its singular boundary. Equivalently, by layer cake / the one-dimensional bathtub principle,

\[
\int f_X(x)(c-x)_+^{-1/2}\,dx
\le \int_0^1u^{-1/2}\,du=2.
\tag{6}
\]

The same argument applies for `ay<0` after reflection. Hence, uniformly in `s`,

\[
\boxed{
p_y(s)\le \frac{\sqrt2}{\sqrt{|ab|}}|y|^{-1/2}.
}
\tag{7}
\]

---

## 4. Second bathtub: the `Y` coordinate

Average (7) against `f_Y`. Since `Y` has a density, the exceptional point `y=0` has probability zero. We obtain

\[
p_Q(s)
\le \frac{\sqrt2}{\sqrt{|ab|}}
\int_{\mathbb R}f_Y(y)|y|^{-1/2}\,dy.
\tag{8}
\]

Again by the bathtub principle, among all probability densities bounded by one the last integral is maximized by the centered interval of length one:

\[
\int f_Y(y)|y|^{-1/2}\,dy
\le \int_{-1/2}^{1/2}|y|^{-1/2}\,dy
=2\sqrt2.
\tag{9}
\]

Combining (8) and (9) gives exactly

\[
\|p_Q\|_\infty\le \frac4{\sqrt{|ab|}},
\]

proving (1). For `|a|,|b|>=1`, `4<3\sqrt2` follows after squaring from `16<18`.

This is a global-output estimate; no special output level is selected.

---

## 5. Density existence and continuity in this branch

For every fixed `y\ne0`, the law of `2ayX` has an `L^1` density and `W=bZ^2` has the `L^1` density (3). Their convolution `p_y` is therefore continuous. The domination (7) is independent of `s`, and

\[
\int f_Y(y)|y|^{-1/2}dy\le2\sqrt2<\infty.
\]

Thus dominated convergence in `y` shows that

\[
p_Q(s)=\int f_Y(y)p_y(s)dy
\]

is a continuous representative of the density. This proves continuity only for this exact null-pair branch. The full QFORM continuity question remains open.

---

## 6. Affine and ambient conditioning extension

For arbitrary real `alpha,beta,gamma,c`, set

\[
X'=X+\frac{\beta}{2a},\qquad
Y'=Y+\frac{\alpha}{2a},\qquad
Z'=Z+\frac{\gamma}{2b}.
\]

Then

\[
2aXY+bZ^2+\alpha X+\beta Y+\gamma Z+c
=2aX'Y'+b(Z')^2+c-\frac{\alpha\beta}{2a}-\frac{\gamma^2}{4b}.
\tag{10}
\]

Translations preserve independence and the density cap. Therefore (1) applies verbatim.

Now let an arbitrary larger symmetric matrix contain a physical principal block on three original coordinates equal to `A_{a,b}`. Conditional on all remaining original coordinates, the quadratic form in those three independent coordinates is exactly (10), with condition-dependent affine coefficients and an additive constant. The conditional density is bounded by `4/sqrt(|ab|)` uniformly in the outside coordinates. Averaging the conditional densities proves the same global ambient bound. This extension retains original-coordinate product provenance throughout.

---

## 7. Exact rotated stress interpretation

Let

\[
J=\operatorname{diag}(1,1,-1),\qquad
w_+=\frac{e_1+e_3}{\sqrt2},\qquad
w_-=\frac{e_1-e_3}{\sqrt2}.
\]

Then

\[
w_+^TJw_+=w_-^TJw_-=0,\qquad
w_+^TJw_-=1,
\]

while `w_+,w_-,e_2` are Euclidean orthonormal. Taking these three vectors as the physical-to-spectral rows gives

\[
R^TR=I_3,
\qquad
RJR^T=
\begin{pmatrix}0&1&0\\1&0&0\\0&0&1\end{pmatrix},
\]

and hence the exact physical form

\[
X_{\rm phys}^TRJR^TX_{\rm phys}=2XY+Z^2.
\tag{11}
\]

Thus two complementary **J-lightlike macroscopic physical rows** cannot create a peak above four, even when all three physical laws are arbitrary cap-one densities. This is stronger than the previous one-heavy lightlike Gaussian-completion theorem: it is finite-dimensional, fully arbitrary-law in this exact rotated architecture, and global in the output.

---

## 8. Designated account02/B17 result actually applied

The completed designated-partner theorem was read from

`yspennstate/math-open-problems@06aea167c49a7d7574f1c2f518c756f22413371a`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/B17-20260923T014533Z-r14-multiscale/REPORT.md`.

It proves for an arbitrary cap-one `X` and independent `G_+,G_-~N(0,1/12)` that

\[
\left\|p_{X^2+G_+^2-G_-^2}\right\|_\infty
\le C_{\rm maj}
:=\frac6\pi\left(\frac52+\log\frac43-\gamma\right)
=4.2216798636\ldots
<3\sqrt2.
\tag{12}
\]

Apply (12) to the aligned-majority one-heavy branch and apply the new theorem (2) to the complementary-null two-heavy branch. For their union of exact stress mechanisms,

\[
\boxed{
\sup_{Q\in\mathcal C_{\rm maj}\cup\mathcal C_{\rm null}}
\|p_Q\|_\infty
\le \max\{C_{\rm maj},4\}
=C_{\rm maj}
<3\sqrt2.
}
\tag{13}
\]

Thus the partner result is used at an actual inequality, and together the two results exclude both a macroscopic row aligned with a majority-sign eigenvector (under its Gaussian-completion scope) and a pair of complementary macroscopic null rows (under the fully arbitrary-law exact scope here) as mechanisms for exceeding the known `3 sqrt(2)` lower obstruction.

Equation (13) is a mechanism classification, not a proof of the unrestricted conjecture.

---

## 9. What remains unpaid

The known target-level lower obstruction remains

\[
C_{\rm univ}\ge3\sqrt2.
\]

The new theorem rules out a broad and genuinely rotated source-valid witness family strictly below that scale. Any witness above `3 sqrt(2)`, if one exists, must avoid this exact null-pair structure. Remaining plausible stress mechanisms include several non-null non-collinear macroscopic rows, shared-coordinate heavy rows with a fully coupled third direction, finite/mesoscopic non-Gaussian interactions not reducible to an isolated null pair, or higher spectral-rank coupling.

Nothing here proves the full arbitrary-matrix QFORM theorem, and no status promotion beyond `NEW_SUPPORTING_THEOREM` is warranted.

## 10. Deterministic checks

Sibling `verify_nullpair.py` checks the spectral identity and constants. `CHECKS.txt` records the executed output. These checks are consistency certificates, not substitutes for the analytic proof above.
