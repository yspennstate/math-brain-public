# account01/B09 r12 — low-leverage closure for the robust two-anchor `s_8` endpoint

Run: `20260924T144758Z-account01-B09-FIXMULT-auto11-r12`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned baseline manuscript: `7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

Status: **PROVED SUPPORTING REDUCTION / `s_8` STILL OPEN.**

This note starts from the robust two-anchor endpoint proved in account03/B17 commit `0408c579bcda638e72c010ff99892a22b9049796`. In the only unpaid no-pivot `s_8(A)>=1` branch, that result supplies a literal two-coordinate set `H`, with complement `L`, such that for

\[
C=A[H,L],\qquad G=CC^T,
\]

one has

\[
g:=\det G\ge d_0:=0.3649442658827020\ldots .
\tag{1}
\]

The principal self-block on `H` may be zero, rank one, or arbitrarily close to singular; no inverse of it is used below.

The new result closes this robust-pair endpoint whenever no physical complement coordinate has excessive leverage in the two-dimensional row space of `C`.

## Theorem `QFORM-S8-ROBUSTPAIR-LOWLEVERAGE-CLOSURE-v1`

Let `A=A^T` have no manuscript `eta`-pivot, with `eta=1/100`, and assume `s_8(A)>=1`. Suppose a literal two-set `H` satisfies (1). Put

\[
Q_C=C^T(CC^T)^{-1}C,
\qquad P=I_L-Q_C,
\qquad q_i=(Q_C)_{ii},\quad p_i=P_{ii}=1-q_i.
\]

If

\[
\boxed{q_i\le {2\over3}\quad\text{for every }i\in L,}
\tag{2}
\]

then for every vector of independent cap-one coordinate laws and every affine perturbation, the quadratic polynomial `X^TAX+b^TX+c` has a bounded continuous density, with

\[
\boxed{\|p_Q\|_\infty<23.48.}
\tag{3}
\]

Consequently, in the robust-pair terminal branch, failure of the conclusion (3) forces a literal physical coordinate with `q_i>2/3`. Since `sum_i q_i=2`, there are at most two such coordinates.

If two distinct coordinates `i,j` satisfy `q_i,q_j>2/3`, then their literal two-column cross minor already obeys

\[
\boxed{\det(C_{\{i,j\}})^2>{g\over3}\ge {d_0\over3}.}
\tag{4}
\]

Equation (4) is a localization certificate, not by itself a density theorem; an order-two crossing with arbitrary curvature on both banks is known not to suffice.

## 1. Exact anchored third-minor identity

Write `D=A[L,L]`, and let `d_i=e_i^TD` be its `i`th row. Set

\[
r_i=d_iP.
\]

Because `P` is the orthogonal projection onto the orthogonal complement of `row(C)`, `r_i` is orthogonal to both rows of `C`.

For each `i in L`, define the physical anchored third-minor energy avoiding column `i`:

\[
W_i=
\sum_{\substack{T\subset L\setminus\{i\}\\|T|=3}}
\det A[H\cup\{i\},T]^2.
\tag{5}
\]

Then

\[
\boxed{
W_i=g\bigl(p_i\|r_i\|_2^2-r_{ii}^2\bigr).
}
\tag{6}
\]

### Proof

For `T subset L`, the `3 x 3` matrix in (5) is

\[
\begin{pmatrix}C_{\cdot,T}\\ d_i|_T\end{pmatrix}.
\]

Subtracting from the last row its orthogonal projection onto `row(C)` leaves all determinants unchanged and replaces `d_i` by `r_i`. Cauchy--Binet over **all** three-subsets `T subset L` gives

\[
\sum_{|T|=3}\det\begin{pmatrix}C_{\cdot,T}\\r_i|_T\end{pmatrix}^2
=\det\begin{pmatrix}G&0\\0&\|r_i\|^2\end{pmatrix}
=g\|r_i\|^2.
\tag{7}
\]

If `r_i=0`, both sides of (6) are zero. Otherwise, the leverage of physical column `i` in the augmented three-row frame `[C;r_i]` is

\[
q_i+{r_{ii}^2\over\|r_i\|^2},
\tag{8}
\]

because its row Gram matrix is block diagonal as in (7). The Cauchy--Binet inclusion identity says that the sum of squared maximal minors containing column `i` is the total determinant in (7) times the leverage (8). Subtracting these minors from (7) proves (6). No random-variable rotation is involved.

Let

\[
W=\sum_{i\in L}W_i.
\tag{9}
\]

This is a sum of literal original-coordinate third minors with row set `H union {i}` and a disjoint three-set of columns.

## 2. A leverage-corrected diagonal completion

Under (2), `p_i>=1/3`. Define

\[
\lambda_i={r_{ii}\over p_i},\qquad
\Lambda=\operatorname{diag}(\lambda_i),
\qquad
E=(D-\Lambda)P.
\tag{10}
\]

Then `E_ii=0` for every `i`, and

\[
\boxed{
\|e_i^TE\|_2^2={W_i\over gp_i}.
}
\tag{11}
\]

Indeed, since `r_i=d_iP` lies in `range(P)`,

\[
\langle r_i,e_i^TP\rangle=r_{ii},
\qquad
\|e_i^TP\|^2=p_i.
\]

Therefore

\[
\|e_i^TE\|^2
=\left\|r_i-{r_{ii}\over p_i}e_i^TP\right\|^2
=\|r_i\|^2-{r_{ii}^2\over p_i},
\]

which is (11) by (6). Summing and using `p_i>=1/3`,

\[
\boxed{
\|E\|_F^2\le {3W\over g}.
}
\tag{12}
\]

Now extend `Lambda` by zeros on `H` and set

\[
D_0=0_H\oplus\Lambda,
\qquad
R=A-D_0-(0_H\oplus E).
\tag{13}
\]

Then

\[
R=
\begin{pmatrix}
A[H,H]&C\\
C^T&(D-\Lambda)Q_C
\end{pmatrix}.
\tag{14}
\]

Every row of `R` lies in the direct sum of the two physical `H` coordinate directions and `row(C)`. Hence

\[
\boxed{\operatorname{rank}R\le4,\qquad
\operatorname{rank}R[L,L]\le2.}
\tag{15}
\]

This is the same global-versus-restricted rank mechanism as the baseline B09 argument, but now produced from a robust physical two-anchor cross frame rather than a sampled interpolation seed.

## 3. Spectral rank perturbation forces anchored third-minor mass

Assume for contradiction that

\[
\|E\|_F\le{1\over4}.
\tag{16}
\]

Since `s_8(A)>=1`, singular-value perturbation for the possibly nonsymmetric matrix `A-(0_H\oplus E)=D_0+R` gives

\[
s_8(D_0+R)\ge{3\over4}.
\tag{17}
\]

The global rank bound `rank R<=4` therefore yields

\[
s_4(D_0)\ge{3\over4}.
\tag{18}
\]

Thus at least four diagonal entries of `Lambda` have modulus at least `3/4`; all lie in `L`. Select any three of them, indexed by `J_0 subset L`.

The no-pivot entry bound is the sharper baseline estimate

\[
|A_{ij}|<a_0:=\sqrt{\eta^2+\eta}=0.1004987562\ldots
\qquad(i\ne j).
\tag{19}
\]

Because `E` has zero diagonal, for `i in J_0`,

\[
|R_{ii}|
\ge {3\over4}-\eta
={74\over100}.
\tag{20}
\]

For distinct `i,j in J_0`,

\[
|R_{ij}|\le |A_{ij}|+|E_{ij}|
<a_0+{1\over4}.
\tag{21}
\]

Hence the sum of the two off-diagonal entries in any row is strictly less than

\[
2(a_0+1/4)=0.7009975124\ldots <0.74.
\tag{22}
\]

So `R[J_0,J_0]` is strictly row-diagonally dominant and invertible. This contradicts `rank R[L,L]<=2`. Therefore (16) is impossible and

\[
\|E\|_F>{1\over4}.
\tag{23}
\]

Combining (12) and (23) gives the quantitative physical third-minor lower bound

\[
\boxed{
W>{g\over48}.
}
\tag{24}
\]

This is the first essential implication: low physical leverage plus the eighth spectral direction forces a macroscopic bank of literal anchored third minors.

## 4. Random cut and a three-direction product-Fourier receiver

Make an independent fair physical partition `L=I sqcup J`. Each term of `W` has one distinguished coordinate `i` and a disjoint three-set `T`; the event `i in I`, `T subset J` has probability `2^{-4}=1/16`. Hence some physical cut satisfies

\[
\mathcal C
:=\sum_{\substack{i\in I,\ T\subset J\\|T|=3}}
\det A[H\cup\{i\},T]^2
\ge {W\over16}
>{g\over768}
\ge {d_0\over768}.
\tag{25}
\]

Let `M=C_{\cdot,J}` be the two hub-to-`J` rows, and project each literal `I-J` cross row of `A` orthogonally off `row(M)`. Let the residual rows form `C_res`. Cauchy--Binet and Gram--Schmidt give the exact identity

\[
\boxed{
\mathcal C=\det(MM^T)\,\|C_{res}\|_F^2.
}
\tag{26}
\]

In particular `M` has row rank two.

Apply the completed grouped product-Fourier compiler of account02/B16, commit `00043d234457291849302da1ad049b554662a513`, with the two literal coordinates in `H` retained as the hub (`k=2`) and residual order `ell=1`.

If the residual one-volume is diffuse, formula `(k,ell,d)=(2,1,3)` gives

\[
\|p_Q\|_\infty
\le C_{21}\,\mathcal C^{-1/6},
\qquad
C_{21}=3\,2^{1/6}e^{2/3}=6.55877262385\ldots .
\tag{27}
\]

If one residual physical row has more than half of the one-volume, promote that literal coordinate as a third retained hub. Its three-row cross Gram determinant is then `>mathcal C/2`; the exact-rank-three receiver gives the smaller coefficient

\[
3\sqrt e\,2^{1/6}=5.55188116380\ldots .
\tag{28}
\]

Thus (27) holds uniformly. The characteristic-function majorant has exponent `3/2>1`, so this branch has a bounded continuous density. Inserting (25) and (1),

\[
\|p_Q\|_\infty
< C_{21}(d_0/768)^{-1/6}
=23.4789328944\ldots <23.48.
\tag{29}
\]

This proves the theorem.

## 5. Exact heavy-coordinate localization

For completeness, the two-dimensional projection `Q_C` has

\[
\sum_i q_i=2.
\tag{30}
\]

Hence there are at most two coordinates with `q_i>2/3`.

There is also an exact determinantal interpretation. Define

\[
w_{ij}={\det(C_{\{i,j\}})^2\over g},\qquad i<j.
\]

Cauchy--Binet gives `sum_{i<j}w_ij=1`, and the determinantal inclusion identity gives

\[
q_i=\sum_{j\ne i}w_{ij}.
\tag{31}
\]

If two distinct coordinates satisfy `q_i,q_j>2/3`, then under the probability mass `w`,

\[
w_{ij}=\mathbb P(i\hbox{ and }j)
\ge\mathbb P(i)+\mathbb P(j)-1
=q_i+q_j-1>{1\over3}.
\]

Therefore (4) follows.

## 6. What remains for multiplicity eight

This note does **not** prove the eight-eigenvalue theorem. It removes the entire diffuse robust-pair endpoint. After combining with account03/B17, any still-unpaid robust two-anchor terminal configuration must have one or two literal complement coordinates with leverage above `2/3` in the anchor cross row space.

The two-heavy case already contains a macroscopic literal `2 x 2` anchor-to-coordinate minor by (4), but the account02/B04 counterexample at commit `122a92fbfd1f6cc6d228666fa56d9e7ffea16b65` proves that positive order-two crossing volume alone is not a density endpoint when arbitrary same-bank curvature remains on both banks. The next obligation is therefore a **high-leverage/near-coloop finite-core receiver that retains the robust-pair collar provenance**, not a generic `E_2` theorem.

All arguments above use original physical coordinates for conditioning and product structure. Orthogonal projections appear only in deterministic row-space algebra. No moments, bounded support, Gaussianity, log-concavity, post-rotation independence, or pointwise quadratic-phase decay is used.
