# MOC4 account03/B09 — exact SO(6) refutation of coefficientwise odd-twist completeness

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex-normal `4 x 4` Marcus-de Oliveira determinant hull  
**Worker:** account03/B09  
**Assignment:** exploit the special complementary `2 x 2` minors in dimension four and apply the result to the shared determinant-support problem  
**Named partner:** account04/B07  
**Candidate:** `MOC4-CYCLE-SEPARATOR-NOGO-v1`  
**Outcome:** `CANDIDATE_REFUTED`. A natural coefficientwise strengthening of the current odd-twist route is false on a genuine exterior-square unitary orbit. The parent MOC4 statement remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact inherited step and the implication attacked

The target is

\[
\det(A+B)\in\operatorname{conv}\left\{
\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4
\right\}
\]

for every complex normal `4 x 4` pair, including singular and repeated spectra.

The required named other-account result consumed substantively is **account04/B07**, run `20260922T021038Z-account04-B07-MOC4-r13`, `MOC4-ODD-WEYL-ORIENTATION-v1`. In the real exterior-square model it writes `O=Lambda^2 U in SO(6)` in `2 x 2` blocks and sets

\[
t_{ij}=q^+_{ij}+q^-_{ij}=\tfrac12\|B_{ij}\|_F^2,
\qquad
y_{ij}=q^+_{ij}-q^-_{ij}=\det B_{ij}.
\]

For every odd signed perfect matching it proves the nonlinear overlap inequality

\[
\sum_i\sqrt{q^{\epsilon_i}_{i,\rho(i)}}\le2.
\]

My preceding B09 run strengthened the linear part of that orientation information to the sixteen exact checkerboard constraints

\[
\sum_{i,j}q^{r_i c_j}_{ij}\le2,
\qquad
\Bigl(\prod_i r_i\Bigr)\Bigl(\prod_jc_j\Bigr)=-1.
\tag{OT}
\]

Those constraints exactly closed the difficult structured datum on which the unrestricted 48-colour matching relaxation overshoots the genuine 24-endpoint support.

The live question is weaker than coefficientwise convexity: only **structured spectral support directions** `(K,X)` have to satisfy

\[
\sum_{ij}\left(K_{ij}y_{ij}+\frac12X_{ij}t_{ij}\right)
\le \max_{24\text{ even signed endpoints}}(\cdots).
\tag{S}
\]

A tempting route would prove the stronger statement that every genuine `(t,y)` satisfying the unitary constraints lies in the convex hull of the 24 even signed matching endpoints, perhaps using `(OT)`. This run directly tests and refutes that strengthening on an actual `SO(6)` point, not on arbitrary bistochastic data.

This is a material mechanism change from the preceding rank-defect/LP-dual run: the present argument derives an exact parity-hull separator and evaluates it on a closed-form true exterior-square orbit point.

## 2. A 48-member family of valid inequalities for the even endpoint hull

Let `pi in S_3`, let `s=(s_1,s_2,s_3) in {+1,-1}^3` have odd parity `s_1s_2s_3=-1`, and let `tau in {+1,-1}`. With indices read modulo three, define

\[
\Phi_{\pi,s,\tau}(t,y)
:=3\sum_{i=1}^3 s_i y_{i,\pi(i)}
+\tau\left[
\sum_i t_{i,\pi(i-1)}-\sum_i t_{i,\pi(i+1)}
\right].
\tag{1}
\]

### Lemma — cycle-cut inequality

Every one of the 24 genuine even signed matching endpoints satisfies

\[
\boxed{\Phi_{\pi,s,\tau}(t,y)\le3.}
\tag{2}
\]

Hence `(2)` holds on their convex hull. There are `6*4*2=48` distinct inequalities of this form.

### Proof

Relabel columns by `pi`; it is enough to consider `pi=id`. An even signed endpoint consists of a permutation `rho in S_3` and signs `epsilon_i` on its three occupied entries with `epsilon_1epsilon_2epsilon_3=+1`.

If `rho=id`, the cycle term in `(1)` vanishes and

\[
\Phi=3\sum_i s_i\epsilon_i.
\]

Because `(s_1\epsilon_1)(s_2\epsilon_2)(s_3\epsilon_3)=-1`, the sum of the three signs is at most one, so `Phi<=3`.

If `rho` is a transposition, it has one fixed point. The two nonfixed occupied entries contribute once with opposite signs to the two directed-cycle sums, so the cycle difference is zero. Only the fixed diagonal entry contributes, giving `Phi=+/-3`.

If `rho` is a 3-cycle, no diagonal term contributes and all three occupied entries lie in exactly one of the two directed 3-cycles, giving `Phi=+/-3`. Thus `(2)` holds in every case. QED.

The companion verifier checks all 48 inequalities against all 24 endpoints exactly with `Fraction`; this is not a floating-point hull inference.

## 3. A closed-form genuine SO(6) point outside that hull

Consider the two rational planar rotations

\[
(c_1,s_1)=(7/25,24/25),\qquad
(c_2,s_2)=(20/29,21/29)
\]

and let

\[
O=G_{4,6}(c_2,s_2)G_{2,6}(c_1,s_1).
\tag{3}
\]

Explicitly,

\[
O=\begin{pmatrix}
1&0&0&0&0&0\\
0&7/25&0&0&0&-24/25\\
0&0&1&0&0&0\\
0&-504/725&0&20/29&0&-147/725\\
0&0&0&0&1&0\\
0&96/145&0&21/29&0&28/145
\end{pmatrix}.
\tag{4}
\]

Exact arithmetic gives `O^T O=I` and `det O=1`, hence `O in SO(6)`. Under the standard real form of `Lambda^2 C^4`, the representation `SU(4)=Spin(6) -> SO(6)` is onto, so `(4)` is a genuine exterior-square unitary-orbit point rather than an arbitrary transport array.

Partitioning `(4)` into three-by-three `2 x 2` blocks gives

\[
t=\begin{pmatrix}
337/625&0&288/625\\
127008/525625&1241/1682&21609/1051250\\
4608/21025&441/1682&21809/42050
\end{pmatrix},
\tag{5}
\]

and

\[
y=\operatorname{diag}(7/25,20/29,28/145).
\tag{6}
\]

All `q^+=(t+y)/2` and `q^-=(t-y)/2` are nonnegative, and every row and column of `t` sums exactly to one.

Take `pi=id`, `s=(+,+,-)`, `tau=+1`. Then `(1)` becomes

\[
3(y_{11}+y_{22}-y_{33})
+(t_{13}+t_{21}+t_{32})
-(t_{12}+t_{23}+t_{31})\le3.
\tag{7}
\]

For `(5)-(6)`, exact evaluation yields

\[
\Phi=\frac{1605549}{525625}
=3+\frac{28674}{525625}>3.
\tag{8}
\]

Therefore this **genuine** `SO(6)` / exterior-square unitary point is outside the convex hull of the 24 even signed matching endpoints.

## 4. The previous sixteen odd-twist cuts still pass

The point `(5)-(6)` does not evade the previous B09 compatibility theorem. For all sixteen checkerboard odd twists `(OT)`, exact enumeration gives

\[
\max_{(r,c)}\sum_{ij}q^{r_ic_j}_{ij}
=\frac{1369}{725}<2.
\tag{9}
\]

Thus row/column conservation plus all sixteen valid odd-twist mass inequalities do **not** imply coefficientwise membership in the even endpoint hull, even after restricting to genuine `SO(6)` data. The missing information is more delicate than orientation-component mass alone.

This also explains why the prior hard structured datum being certified by `(OT)` cannot be promoted into a universal positive common-lift theorem: that success was support-direction-specific.

## 5. What this does and does not prove

This is **not a counterexample to MOC4**. Inequality `(7)` is an explicit separating functional for the coefficientwise parity hull, but I have not shown that its coefficient pair

\[
K_{\rm cyc}=3\operatorname{diag}(1,1,-1),
\qquad
X_{\rm cyc}=2\begin{pmatrix}
0&-1&1\\1&0&-1\\-1&1&0
\end{pmatrix}
\tag{10}
\]

arises from actual spectra `(a,b)` and a support direction `eta`. MOC4 only requires `(S)` for that structured spectral image, not for every real `(K,X)`.

Accordingly the exact route refuted here is:

> **`MOC4-ODD-TWIST-COMPLETE-LIFT-v1` (FALSE):** genuine exterior-square unitary compatibility plus the sixteen odd-twist mass cuts force `(t,y)` into the convex hull of the 24 `S_4` endpoints.

The sharpened first missing implication is now necessarily **support-specific**:

> **`MOC4-STRUCTURED-DUAL-CONE-v1`:** characterize the spectral coefficient image `(K(a,b,eta),X(a,b,eta))` well enough to prove that no separator of a genuine `SO(6)` point from the even endpoint hull can lie in that image, equivalently prove `(S)` directly for all structured pairs.

A useful next attack is to substitute the exact exterior-power formulas

\[
X_{\alpha\beta}=\Re\bigl(\eta A^+_\alpha B^+_\beta\bigr),
\qquad
K=(HWH^T)_{1^\perp}+\tfrac12Y,
\]

with

\[
Y_{\alpha\beta}=\Re\bigl(\eta A^-_\alpha B^-_\beta\bigr),
\quad
W_{ij}=\Re\bigl(\eta(a_{i^c}b_j+a_i b_{j^c})\bigr),
\]

into a separating normal such as `(10)`, rather than adding more transport-only cuts. That is the first place where the special spectral algebra, rather than generic `SO(6)` geometry, must now pay the residual.

## 6. Exact verification

`verify_cycle_separator.py` uses only standard-library `fractions.Fraction`. It verifies:

1. exact orthogonality and determinant `+1` of `(4)`;
2. exact block formulas `(5)-(6)`, nonnegativity, and row/column conservation;
3. all sixteen old odd-twist inequalities, with maximum `1369/725`;
4. all 48 cycle-cut inequalities on all 24 even signed endpoints, with endpoint maximum exactly `3`;
5. the witness value `1605549/525625` and excess `28674/525625`.

Observed exact output is saved in `VERIFICATION.txt`.

**Status:** `CANDIDATE_REFUTED`. Full MOC4 remains open. No arbitrary bistochastic surrogate, benchmark gold, held-out answer, credential, email/Drive material, paid model/API/Codex, remote workflow, or public release was used.
