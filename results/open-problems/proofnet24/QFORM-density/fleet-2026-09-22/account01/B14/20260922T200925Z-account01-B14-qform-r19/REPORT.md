# account01/B14 — rainbow exterior-bank localization and coupled three-bank compression

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T200925Z-account01-B14-qform-r19`  
**Assignment:** translations and localization  
**Status:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_LOCALIZATION_THEOREM`; full QFORM remains OPEN.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Scope and source pins

Fresh protected control was read at `yspennstate/math-research-brain@7eed8549df05d1ce2eced35e1df8550b9aaaad27`, with OWNER CONTROL revision `2026-09-22.15`; a pre-write refresh at `899e2f789827509e84bada90cf8053467b641d16` still keeps QFORM as the exclusive target and contains no later stop.

This run substantively consumes the completed assigned-partner theorem:

- account02/B14, run `20260922T193635Z-account02-B14-QFORM-r19`;
- canonical report `yspennstate/math-open-problems@85c9fd52d16444290a9672ee48f233d492b20b56`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260922T193635Z-account02-B14-QFORM-r19/REPORT.md`.

Its exact inputs used below are

\[
\sum_{|I|=|J|=3}\det(A_{I,J})^2
=\|\wedge^3A\|_{HS}^2
=e_3(s_1(A)^2,\ldots,s_n(A)^2),
\tag{0.1}
\]

hence the target hypothesis implies the left side is at least one, and the exact diffuse family

\[
A_m=[1]\oplus J_m/m\oplus(-J_m/m)
\tag{0.2}
\]

has global exterior mass one while every bounded physical active set captures a vanishing fraction and every nonzero physical principal triple has determinant `m^{-2}`.

A second completed source used is account03/B14, `QFORM-PRINCIPAL-TRIPLE-DETERMINANT-LOCALIZATION-v1`, canonical commit `89e6481f4f7ed7d49a77cfcb989ee93572d5d5cd`. For three independent cap-one scalar variables and any nonsingular symmetric coefficient matrix `B`, arbitrary affine perturbations allowed,

\[
\|p_q\|_\infty\le32\sqrt{10}\,|\det B|^{-1/3}.
\tag{0.3}
\]

Finally I use the standard Ball--Rogozin one-dimensional projection bound already source-pinned in the QFORM fleet: if `u` is Euclidean unit and the underlying original coordinates are independent with densities at most one, then `u^TX` has density at most `sqrt(2)`.

No arbitrary-joint coarea statement, conditional positive-density moment, rotation-induced independence, pointwise quadratic Fourier decay, bounded support diameter, or bounded fragment-count reduction is used.

## 1. A product-preserving three-bank localization of the full third exterior mass

For a partition `Pi=(B_1,B_2,B_3)` of the ORIGINAL coordinate indices into three color classes, call a triple `I` **rainbow** when it contains exactly one coordinate from each `B_a`. Define the rainbow third-compound mass

\[
\mathcal R_\Pi(A)
:=\sum_{\substack{|I|=|J|=3\\I,J\text{ rainbow}}}
\det(A_{I,J})^2.
\tag{1.1}
\]

Also let

\[
M_r(A):=\sum_{\substack{|I|=|J|=3\\|I\cap J|=r}}
\det(A_{I,J})^2,
\qquad r=0,1,2,3.
\tag{1.2}
\]

### Theorem 1 — `QFORM-RAINBOW-EXTERIOR-BANK-LOCALIZATION-v1`

For every real matrix `A`, there exists a partition `Pi=(B_1,B_2,B_3)` of the original coordinates such that

\[
\boxed{
\mathcal R_\Pi(A)
\ge \frac4{81}\,\|\wedge^3A\|_{HS}^2.
}
\tag{1.3}
\]

More precisely, under iid uniform three-coloring,

\[
\boxed{
\mathbb E_\Pi\mathcal R_\Pi(A)
=\frac4{81}(M_0+M_1)+\frac2{27}M_2+\frac29M_3.
}
\tag{1.4}
\]

Hence every QFORM target matrix, having at least three singular values at least one, admits an original-coordinate three-bank partition satisfying

\[
\boxed{\mathcal R_\Pi(A)\ge4/81.}
\tag{1.5}
\]

#### Proof

Fix `I,J`, each of size three, and color every coordinate independently uniformly in `{1,2,3}`. The contribution `det(A_{I,J})^2` survives exactly when both `I` and `J` are rainbow.

If `r=|I cap J|`, the joint probabilities are elementary finite counts:

- `r=0`: `36/3^6=4/81`;
- `r=1`: `12/3^5=4/81`;
- `r=2`: `6/3^4=2/27`;
- `r=3`: `6/3^3=2/9`.

Summing these probabilities against the squared minors gives (1.4), which is at least `(4/81) sum_r M_r`. By (0.1) this is `(4/81)||wedge^3A||_HS^2`. Therefore some deterministic coloring attains at least the expectation, proving (1.3). Under the target hypothesis, (0.1) is at least one, giving (1.5). `QED`

### Interpretation

This is a genuine product-preserving matrix localization: the three banks are disjoint sets of original independent coordinates, so random variables constructed from different banks remain independent. Unlike bounded active-set localization, no coordinate is discarded and no mixed curvature is turned into affine data. The theorem converts the bare spectral hypothesis into a quantitative bank statement before any reciprocal determinant is paid.

The partner obstruction shows why this order matters: on `A_m`, no `O(1)` active set sees a fixed fraction of the exterior mass, whereas the natural three-bank partition retains all of it.

## 2. Exact coupled three-bank compression theorem

The previous run solved diagonal rank-one banks. Here the bank-level quadratic coefficient is allowed to be a fully coupled nonsingular `3 x 3` matrix.

Let the original coordinates be split as

\[
S=I_1\sqcup I_2\sqcup I_3,
\qquad T=S^c.
\]

For each `a=1,2,3`, let `u_a` be a Euclidean unit vector supported on `I_a`, and put `U=[u_1,u_2,u_3]`. The disjoint supports make the columns orthonormal. Assume the physical blocks satisfy

\[
A_{S,S}=UMU^T,
\qquad
A_{S,T}=UK
\tag{2.1}
\]

for some symmetric nonsingular `3 x 3` matrix `M` and arbitrary matrix `K`; the outside block `A_{T,T}` is arbitrary.

Write

\[
Y_a=u_a^TX_{I_a}.
\tag{2.2}
\]

Because the three banks are disjoint, `Y_1,Y_2,Y_3` are independent. Let `H_a=||p_{Y_a}||_infinity`; Ball--Rogozin gives `H_a<=sqrt(2)`, and if `I_a` is a singleton with coefficient magnitude one then `H_a<=1`.

### Theorem 2 — `QFORM-COUPLED-THREE-BANK-COMPRESSION-v1`

Under (2.1), for arbitrary independent original-coordinate densities bounded by one,

\[
\boxed{
\|p_{X^TAX}\|_\infty
\le
32\sqrt{10}\,(H_1H_2H_3)^{2/3}|\det M|^{-1/3}.
}
\tag{2.3}
\]

In particular,

\[
\boxed{
\|p_{X^TAX}\|_\infty
\le64\sqrt{10}\,|\det M|^{-1/3},
}
\tag{2.4}
\]

and if `M` itself has three eigenvalues of modulus at least one,

\[
\boxed{\|p_{X^TAX}\|_\infty\le64\sqrt{10}.}
\tag{2.5}
\]

No support, moment, centering, compactness, connectedness, fragment-count or support-location hypothesis is used. Arbitrary outside dimension, arbitrary outside quadratic form and arbitrary range-aligned cross coupling `UK` are allowed.

#### Proof

Condition on the outside coordinates `X_T=z`. Equation (2.1) gives exactly

\[
Q\mid X_T=z
=Y^TMY+2(Kz)^TY+c(z).
\tag{2.6}
\]

The three scalar variables `Y_a` remain independent. Define `Z_a=H_aY_a`; then each `Z_a` has density at most one. With `D=diag(H_1,H_2,H_3)`, (2.6) becomes

\[
Z^T(D^{-1}MD^{-1})Z+\text{affine}+c(z).
\tag{2.7}
\]

The determinant of the quadratic coefficient is

\[
\det(D^{-1}MD^{-1})
=\frac{\det M}{(H_1H_2H_3)^2}.
\tag{2.8}
\]

Apply the completed three-variable determinant theorem (0.3), uniformly in the affine vector and in `z`:

\[
\|p_{Q\mid X_T=z}\|_\infty
\le32\sqrt{10}\,(H_1H_2H_3)^{2/3}|\det M|^{-1/3}.
\tag{2.9}
\]

Average over `z` to obtain (2.3). The bounds (2.4)--(2.5) follow from `H_a<=sqrt(2)` and `|det M|>=1`. `QED`

### Why this is genuinely stronger than the previous bank theorem

The prior B14 branch required the bank coefficient matrix to be diagonal, so the bank-level quadratic was a sum of independent squares. Theorem 2 permits arbitrary couplings `M_ab Y_aY_b`. Thus diagonalizing `M` is never used and no false independence after rotation occurs.

## 3. Applying the assigned partner result to a genuinely nonseparable diffuse target family

The partner's family (0.2) is the special case `M=diag(1,1,-1)`. The same mechanism has a fully coupled extension.

Let

\[
u_0=e_0,
\qquad
u_+=m^{-1/2}(1,\ldots,1)\text{ on the positive bank},
\qquad
u_-=m^{-1/2}(1,\ldots,1)\text{ on the negative bank},
\]

and put `U_m=[u_0,u_+,u_-]`. For any symmetric nonsingular `3 x 3` matrix `M`, define

\[
A_m(M)=U_m M U_m^T.
\tag{3.1}
\]

Because `U_m^TU_m=I_3`, the three nonzero eigenvalues of `A_m(M)` are exactly the eigenvalues of `M`.

For every row triple `I` and column triple `J` consisting of the singleton, one positive-bank coordinate and one negative-bank coordinate,

\[
\det A_m(M)_{I,J}=\frac{\det M}{m^2},
\tag{3.2}
\]

and all other third mixed minors vanish. Consequently

\[
\boxed{\|\wedge^3A_m(M)\|_{HS}^2=|\det M|^2.}
\tag{3.3}
\]

For an active set containing the singleton and `p,q` coordinates from the two diffuse banks,

\[
\boxed{
\mathcal E_3(S)=|\det M|^2\frac{p^2q^2}{m^4}.
}
\tag{3.4}
\]

Thus the account02/B14 bounded-active-set obstruction persists unchanged, up to the factor `|det M|^2`, for arbitrary coupled bank matrices `M`: any fixed-cardinality active set still loses all exterior mass as `m to infinity`, and every usable physical principal triple has determinant magnitude `|det M|/m^2`.

Now choose the explicit nonseparable bank matrix

\[
M_*=
\begin{pmatrix}
3/2&1/2&0\\
1/2&3/2&0\\
0&0&-1
\end{pmatrix}.
\tag{3.5}
\]

Its eigenvalues are exactly `{2,1,-1}` and `|det M_*|=2`, so every `A_m(M_*)` lies in the exact QFORM target class. The best local physical-triple determinant theorem has cost

\[
32\sqrt{10}\,(2/m^2)^{-1/3}
=32\sqrt{10}\,2^{-1/3}m^{2/3},
\tag{3.6}
\]

which diverges.

By contrast, grouping the three full original-coordinate banks gives independent scalar variables `Y_0,Y_+,Y_-`. Here `H_0<=1` and `H_+,H_-<=sqrt(2)`, so Theorem 2 yields

\[
\begin{aligned}
\|p_{X^TA_m(M_*)X}\|_\infty
&\le32\sqrt{10}\,(1\cdot\sqrt2\cdot\sqrt2)^{2/3}2^{-1/3}\\
&=\boxed{32\sqrt{10}\,2^{1/3}}\\
&<127.50,
\end{aligned}
\tag{3.7}
\]

uniformly in `m` and in every cap-one product input law.

This is an actual inequality application of the partner's exterior-mass obstruction: the local determinant certificate diverges like `m^{2/3}`, while product-preserving bank aggregation pays the same nonseparable target family with a fixed constant.

The natural partition `{singleton},{positive bank},{negative bank}` retains the full rainbow mass

\[
\mathcal R_\Pi(A_m(M_*))=|\det M_*|^2=4,
\tag{3.8}
\]

so the rainbow theorem is exact rather than lossy on the canonical obstruction.

## 4. Translation and arbitrary-support robustness

Both theorems above are completely insensitive to arbitrary deterministic shifts of the input supports. Coordinatewise translations preserve independence and the cap-one condition. In Theorem 2 every outside realization enters only through the affine term `2(Kz)^TY`, which is already covered uniformly by the determinant theorem. Thus arbitrarily distant fragments and unbounded supports incur no additional constant.

The exact finite-fragment extreme-product localization from the previous B14 run may therefore be applied before or after the three-bank partition without changing the small-ball constant. No bounded support diameter or uniform fragment count is introduced.

## 5. What is still unpaid

The full conjecture is not proved. The remaining structural implication is now sharper:

> Starting only from `||wedge^3 A||_HS^2>=1`, use the rainbow partition from Theorem 1 to convert the quantitative rainbow mass `R_Pi(A)>=4/81` into either (i) a coupled three-bank compression of the form (2.1) with dimension-free determinant budget, or (ii) one of the existing diffuse/ridge/full-matrix smoothing branches, without first selecting and reciprocating one tiny physical minor.

The obstacle is that a large rainbow **Hilbert--Schmidt** third-compound mass need not concentrate on one rank-three bank factorization. A full proof needs an aggregate-before-inversion inequality at the bank level. Theorem 1 supplies the product-respecting bank partition on which such an inequality may be sought.

## 6. Classification

`ESSENTIAL_STEP_APPLIED / SUPPORTING_LOCALIZATION_THEOREM / FULL_QFORM_OPEN`.

No claim of a universal full proof is made. The new advances are:

1. a deterministic three-bank original-coordinate localization retaining at least `4/81` of the total third exterior-volume mass;
2. a translation-uniform theorem for fully coupled rank-three disjoint-bank compressions;
3. a concrete nonseparable diffuse target family where every local determinant certificate diverges but the grouped theorem gives a fixed bound.
