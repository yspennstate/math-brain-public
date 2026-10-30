# MOC4 fleet03/B09 r12 — global odd-twist mass inequalities and an exact structured support certificate

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex-normal `4 x 4` Marcus-de Oliveira determinant hull  
**Worker:** fleet03/B09  
**Assignment:** exploit the special complementary `2 x 2` minors in dimension four and apply the result to the lead's determinant-support expression  
**Outcome:** `ESSENTIAL_STEP_APPLIED` — a new family of 16 exact unitary-compatibility inequalities is proved from the full `SO(6)`/Bogoliubov structure and, by an exact rational dual certificate, closes the difficult structured coefficient datum on which the 48-state orientation-forgetting relaxation fails by `3789337/2560000`. Full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Current inherited state and partner result actually used

The fresh owner control supersedes the old benchmark role and assigns fleet03/B09 to MOC4. The target is

\[
\det(A+B)\in\operatorname{conv}\left\{\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4\right\}
\]

for all complex normal `4 x 4` pairs, including singular and repeated spectra.

The named other-account partner consumed directly is **fleet04/B07**, run `20260922T021038Z-fleet04-B07-MOC4-r13`, `MOC4-ODD-WEYL-ORIENTATION-v1`. Its exact result writes the real exterior-square image `O=Lambda^2 U in SO(6)` in `2 x 2` blocks and then as Bogoliubov coefficients

\[
z\mapsto m_{ij}z+n_{ij}\bar z,
\qquad q^+_{ij}=|m_{ij}|^2,
\qquad q^-_{ij}=|n_{ij}|^2.
\]

For every odd signed perfect matching it proves

\[
\sum_i\sqrt{q^{\epsilon_i}_{i,\rho(i)}}\le2.
\]

It also exhibits an actual structured MOC4 coefficient pair for which the unrestricted 48-colour matching relaxation has

\[
M_{\rm odd}=20773731/5120000,
\qquad
M_{\rm even}=13195057/5120000,
\]

so the forbidden odd endpoint exceeds every genuine `S_4` endpoint by

\[
3789337/2560000>0.
\]

The partner leaves exactly an orientation-aware weighted-suppression implication. This run attacks that implication using the **full complex-linear part of an odd coordinate twist**, not only the three entries of one matching.

## 2. Exact two-colour support form

For the structured coefficient pair `(K,X)` supplied by the exterior-power reduction, the nonconstant support objective is

\[
Q_{K,X}(O)=\sum_{i,j=1}^3
\left[(K_{ij}+X_{ij}/2)q^+_{ij}+(-K_{ij}+X_{ij}/2)q^-_{ij}\right].
\tag{1}
\]

Orthogonality gives

\[
\sum_j(q^+_{ij}+q^-_{ij})=1,
\qquad
\sum_i(q^+_{ij}+q^-_{ij})=1.
\tag{2}
\]

The 24 even signed permutation arrays are exactly the genuine `S_4` endpoint images. The 24 odd signed arrays are orientation reversing and cannot be used as target endpoints.

## 3. New theorem: global odd-twist mass is at most two

For signs `r=(r_1,r_2,r_3)` and `c=(c_1,c_2,c_3)` in `{+1,-1}^3`, define the checkerboard channel choice

\[
s_{ij}=r_i c_j.
\]

There are 16 distinct such sign matrices with

\[
\left(\prod_i r_i\right)\left(\prod_j c_j\right)=-1.
\tag{3}
\]

### Theorem — `MOC4-ODD-TWIST-MASS-v1`

For every genuine `O in SO(6)` arising from `Lambda^2 U`, and every `(r,c)` satisfying `(3)`,

\[
\boxed{
\sum_{i,j=1}^3 q^{\,r_i c_j}_{ij}\le2.
}
\tag{4}
\]

Here `q^{+1}=q^+` and `q^{-1}=q^-`.

### Proof

Identify the three real complementary-pair planes with `C^3`, so the real orthogonal map has the unique form

\[
T(z)=Mz+N\bar z.
\tag{5}
\]

Conjugate output coordinate `i` when `r_i=-1` and input coordinate `j` when `c_j=-1`. Call the resulting real orthogonal map `T'`. Coordinatewise conjugation on one complex coordinate has real determinant `-1`, hence by `(3)`

\[
\det_{\mathbb R}T'=-1.
\tag{6}
\]

Let `M'` be the complex-linear part of `T'`. Directly from whether zero, one, or two of the corresponding input/output coordinates were conjugated,

\[
|M'_{ij}|^2=q^{\,r_i c_j}_{ij}.
\tag{7}
\]

We claim `M'` is singular. Suppose instead that `M'` is invertible. Real orthogonality in Bogoliubov form gives

\[
M'M'^*+N'N'^*=I,
\qquad
M'N'^T+N'M'^T=0.
\tag{8}
\]

Put `Z=M'^{-1}N'`. The second identity in `(8)` yields `Z^T=-Z`. The first gives

\[
M'(I+ZZ^*)M'^*=I.
\tag{9}
\]

Thus `V=M'(I+ZZ^*)^{1/2}` is unitary. For `0<=t<=1`, set

\[
M_t=V(I+t^2ZZ^*)^{-1/2},
\qquad
N_t=M_t(tZ).
\tag{10}
\]

Equations `(8)` hold with `(M',N')` replaced by `(M_t,N_t)`, so `(10)` is a continuous path of real orthogonal maps. At `t=0` it is the unitary map `z -> Vz`, hence orientation preserving; at `t=1` it is `T'`. This contradicts `(6)`. Therefore

\[
\operatorname{rank}M'\le2.
\tag{11}
\]

The first equation in `(8)` also implies `M'M'^*<=I`, so every singular value of `M'` is at most one. Hence

\[
\sum_{ij}|M'_{ij}|^2=\|M'\|_F^2\le2.
\]

Using `(7)` proves `(4)`. QED.

### Why this is stronger than the matching-mass corollary

For an odd signed matching `(rho,epsilon)`, choose `c_j=epsilon_{rho^{-1}(j)}` and `r=(+,+,+)`. Then `(4)` bounds **all nine entries in those three column channels** by two, not merely the three selected matching entries. The partner's nonlinear square-root inequality remains independently useful; `(4)` supplies a different global compatibility constraint coming from the full complex-linear block of an orientation-reversing twist.

## 4. A finite exact LP certificate for any fixed structured support direction

Let

\[
a^+_{ij}=K_{ij}+X_{ij}/2,
\qquad
a^-_{ij}=-K_{ij}+X_{ij}/2.
\tag{12}
\]

Every genuine unitary-generated `q` satisfies nonnegativity, `(2)`, and all 16 inequalities `(4)`. Therefore, for any row potentials `alpha_i`, column potentials `beta_j`, and nonnegative multipliers `lambda_t` assigned to the 16 odd twists, if

\[
a^s_{ij}
\le
\alpha_i+\beta_j+
\sum_{t:\,s_t(i,j)=s}\lambda_t
\quad\text{for every }(i,j,s),
\tag{13}
\]

then

\[
\boxed{
Q_{K,X}(O)
\le
\sum_i\alpha_i+
\sum_j\beta_j+
2\sum_t\lambda_t.
}
\tag{14}
\]

This is a source-valid outer certificate: `(4)` was proved for actual `SO(6)` exterior-square data before any linear relaxation was taken. No arbitrary bistochastic array is substituted for a unitary.

## 5. Exact application to the partner's hard structured datum

Use the exact structured coefficient matrices from the fleet01/B07 generic true-unitary datum also used by fleet04/B07:

\[
K=\begin{pmatrix}
245983/5120000&5030591/5120000&-39077/1024000\\
-5113569/5120000&56671/5120000&19643/1024000\\
-8539/1024000&-35819/1024000&5009153/5120000
\end{pmatrix},
\tag{15}
\]

\[
X=\begin{pmatrix}
-3609633/1280000&111173/51200&2385071/1280000\\
-917133/1280000&1431961/1280000&525623/256000\\
-1352967/1280000&1061147/1280000&948017/1280000
\end{pmatrix}.
\tag{16}
\]

As noted above, the full 48-state orientation-forgetting relaxation overshoots the genuine support by `3789337/2560000`.

Nevertheless `(13)` has the following **exact rational certificate**. Use row potentials

\[
\alpha=
(2302707,1268991,-871389)/5120000,
\tag{17}
\]

and column potentials

\[
\beta=(-720783/640000,\;39007/640000,\;0).
\tag{18}
\]

Only four odd-twist multipliers are nonzero:

\[
\begin{array}{c|c|c}
(r,c)&\lambda\\ \hline
((+,+,+),(-,+,+))&2042727/2560000\\
((+,+,-),(-,+,-))&133141/256000\\
((+,-,+),(+,+,+))&514151/2560000\\
((+,-,-),(-,+,+))&98951/2560000.
\end{array}
\tag{19}
\]

Each row of `(19)` satisfies `(3)`. Direct Fraction arithmetic verifies all 18 inequalities `(13)`. Nine are tight; among the nine positive dual slacks the smallest is

\[
347/16000>0.
\tag{20}
\]

Finally the dual objective is exactly

\[
\sum_i\alpha_i+\sum_j\beta_j+2\sum_t\lambda_t
=\frac{13195057}{5120000}
=M_{\rm even}.
\tag{21}
\]

Therefore every genuine `SO(6)` exterior-square image satisfies

\[
\boxed{
Q_{K,X}(O)\le M_{\rm even}
=13195057/5120000
}
\tag{22}
\]

for this difficult generic structured datum. Thus the new unitary-compatibility inequalities recover the correct 24-endpoint support bound **even though the naive 48-state coloured matching bound fails by about `1.48021`**.

This is an actual application to the shared determinant-support expression, not a free transportation example.

## 6. Exact verification

`verify_odd_twist_mass_certificate.py` checks with standard-library `fractions.Fraction` only:

1. the exact 24 even and 24 odd coloured endpoint maxima for `(15)-(16)`;
2. parity validity and nonnegativity of all four active odd-twist multipliers;
3. all 18 dual inequalities `(13)` exactly;
4. the minimum strictly positive slack `347/16000`;
5. equality of the dual objective with `13195057/5120000`.

No floating-point assertion is used in the certificate.

## 7. What remains

This run does **not** claim full MOC4. The remaining first implication has now been sharpened to a finite structured-coefficient question:

> For every spectral/support coefficient pair `(K,X)` that actually arises from `(a,b,eta)`, do the row/column constraints together with the 16 valid odd-twist mass inequalities `(4)` already have support equal to the 24 even Weyl endpoints? If not, identify the residual structured coefficient cone and combine `(4)` with the partner's stronger square-root odd-overlap inequality or the remaining phase equations in `(8)`.

The exact generic datum that defeated the previous parity-slack and 48-state relaxations is now closed by `(4)`, so this mechanism materially advances the live weighted-suppression problem.
