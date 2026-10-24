# account01/B12 — multiplicity-eight candidate via one-exception leverage completion

Run: `20260924T152031Z-account01-B12-FIXMULT-auto11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned baseline manuscript: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

Status: **NEW COMPLETE CANDIDATE EIGHT-EIGENVALUE REPLACEMENT; NOT VALIDATED.** The proof below preserves the full arbitrary-law, arbitrary-dimension, arbitrary-sign and arbitrary-affine scope. It requires **two genuinely separate end-to-end reviews before owner-level validation**. No such reviews are invented or self-awarded here. The unrestricted three-eigenvalue conjecture remains open.

## 1. Candidate theorem

### `QFORM-FIXED-MULTIPLICITY-8-CANDIDATE-v1`

Let `X_1,...,X_n` be independent real random variables with densities bounded by `K`. Let `A=A^T` be any real symmetric matrix, let `b` be any real vector and `c` any real scalar. If

\[
s_8(A)\ge s>0,
\]

then `Q=X^TAX+b^TX+c` has an essentially bounded density satisfying

\[
\boxed{\|p_Q\|_{\infty,\mathrm{ess}}\le 6010\,{K^2\over s}.}
\tag{1.1}
\]

The new no-pivot branch below has a continuous `C_0` density. Global continuity of every pivot branch is not claimed here.

The proof is normalized to `K=s=1`; the standard baseline rescaling restores `K^2/s` at the end.

## 2. Existing reviewed inputs used

This candidate uses only already-written product-coordinate-safe components plus the new Section 4 lemma.

1. The pinned baseline manuscript, fully audited in this run.
2. The reviewed grouped product-Fourier compiler and marginal-free order-three density / order-two half-potential receivers reconstructed in `improvements/account01/B16/20260924T124038Z-r11/REPORT.md`.
3. The proved multiplicity-eight terminal collar and robust literal two-anchor extraction in `improvements/account03/B17/20260924T141823Z-account03-B17-fixedmult-auto11/ROBUST_TWO_ANCHOR.md`. In the only unpaid no-pivot `s_8>=1` chamber it supplies a literal two-set `H` with
   \[
   C=A[H,H^c],\qquad g:=\det(CC^T)\ge d_0,
   \qquad d_0={\delta_*^2\over2}=0.3649442658827020\ldots,
   \tag{2.1}
   \]
   where
   \[
   \delta_*={97\over100}-{297\sqrt2+3\sqrt{202}\over4000}.
   \]
4. The exact anchored disjoint-third-minor identity from the same physical setup, independently recorded in `improvements/account01/B09/20260924T144758Z-account01-B09-FIXMULT-auto11-r12/LOW_LEVERAGE_ROBUST_PAIR.md`. I rederive the part needed below.

No rotated random variables are introduced. Orthogonal projections below are deterministic row-space devices only.

## 3. Determinantal leverage of the robust pair

Work in the normalized no-pivot branch. Put `L=H^c`, write

\[
A=\begin{pmatrix}A[H,H]&C\\ C^T&D\end{pmatrix},
\qquad G=CC^T,
\tag{3.1}
\]

and define

\[
Q_C=C^TG^{-1}C,\qquad P=I_L-Q_C,
\qquad q_i=(Q_C)_{ii},\quad p_i=P_{ii}=1-q_i.
\tag{3.2}
\]

Since `Q_C` is a rank-two orthogonal projection,

\[
0\le q_i\le1,\qquad \sum_iq_i=2.
\tag{3.3}
\]

For distinct `i,j in L`, let

\[
w_{ij}={\det(C_{\{i,j\}})^2\over g}.
\tag{3.4}
\]

Cauchy--Binet and the determinantal inclusion identity give

\[
\sum_{i<j}w_{ij}=1,
\qquad
q_i=\sum_{j\ne i}w_{ij}.
\tag{3.5}
\]

Thus the `w_{ij}` form a probability law on two-element subsets and `q_i` is the inclusion probability of coordinate `i`.

Because the ambient state has no manuscript `eta`-pivot, with `eta=1/100`,

\[
|A_{uv}|^2<\eta^2+\eta={101\over10000}
\qquad(u\ne v).
\tag{3.6}
\]

Therefore every literal two-column minor of `C` satisfies

\[
|\det C_{\{i,j\}}|
<2(\eta^2+\eta)={101\over5000},
\tag{3.7}
\]

and hence

\[
w_{ij}
<{(101/5000)^2\over d_0}
=0.0011180885362\ldots <0.02.
\tag{3.8}
\]

This small local determinant bound has a decisive consequence.

### Lemma 3.1 — at most one high-leverage complement coordinate

There is at most one `e in L` with

\[
q_e>{51\over100}.
\tag{3.9}
\]

#### Proof

If distinct `i,j` both obeyed (3.9), then under the pair probability law `w`, inclusion--exclusion gives

\[
w_{ij}=\Pr(i\hbox{ and }j)
\ge q_i+q_j-1>{2\over100}=0.02,
\]

contradicting (3.8). QED.

This is the missing observation in the previous low-leverage closure: although one physical coordinate may be an arbitrarily strong near-coloop of the robust two-dimensional cross row space, **there cannot be two such coordinates** in the no-pivot chamber.

Choose `e` to be the unique coordinate satisfying (3.9), if it exists; if none exists, choose any `e in L` (possible because `s_8(A)>=1` implies `|L|>=6`). Put

\[
L'=L\setminus\{e\}.
\]

Then for every `i in L'`,

\[
q_i\le {51\over100},\qquad p_i\ge p_*:={49\over100}.
\tag{3.10}
\]

## 4. One-exception interpolation completion

Let `d_i=e_i^TD` be row `i` of the outside principal block and put

\[
r_i=d_iP.
\tag{4.1}
\]

For `i in L'`, define the literal disjoint anchored third-minor energy

\[
W_i=
\sum_{\substack{T\subset L\setminus\{i\}\\|T|=3}}
\det A[H\cup\{i\},T]^2.
\tag{4.2}
\]

Because `r_i` is orthogonal to both rows of `C`, Cauchy--Binet and the column-inclusion leverage identity for the three-row frame `[C;r_i]` give exactly

\[
\boxed{W_i=g\bigl(p_i\|r_i\|_2^2-r_{ii}^2\bigr).}
\tag{4.3}
\]

Set

\[
W'=\sum_{i\in L'}W_i.
\tag{4.4}
\]

### Theorem 4.1 — one-exception completion forces macroscopic disjoint third volume

Under `s_8(A)>=1`, no `eta`-pivot, and the robust-pair condition (2.1),

\[
\boxed{W'>{49\over1600}\,g.}
\tag{4.5}
\]

#### Proof

For `i in L'`, define

\[
\lambda_i={r_{ii}\over p_i},
\qquad \lambda_e=0,
\qquad
D_0=\operatorname{diag}(\lambda_i:i\in L)
\tag{4.6}
\]

and define an auxiliary, generally nonsymmetric, matrix `E` on the outside block by rows

\[
e_i^TE=(d_i-\lambda_i e_i^T)P
\quad(i\in L'),
\qquad
e_e^TE=0.
\tag{4.7}
\]

Then `E_ii=0` for every `i`, and, using `\|e_i^TP\|^2=p_i` and `\langle r_i,e_i^TP\rangle=r_{ii}`,

\[
\begin{aligned}
\|e_i^TE\|^2
&=\left\|r_i-{r_{ii}\over p_i}e_i^TP\right\|^2\\
&=\|r_i\|^2-{r_{ii}^2\over p_i}
={W_i\over gp_i}.
\end{aligned}
\tag{4.8}
\]

Hence, by (3.10),

\[
\boxed{\|E\|_F^2\le {W'\over gp_*}.}
\tag{4.9}
\]

Extend `D_0` and `E` by zeros on the two anchor coordinates and put

\[
R=A-D_0-E.
\tag{4.10}
\]

For every row indexed by `H` or by `i in L'`, the row of `R` lies in

\[
\mathbb R^H\oplus\operatorname{row}(C),
\]

a space of dimension at most four. The single exceptional row `e` is unrestricted. Therefore

\[
\boxed{\operatorname{rank}R\le5.}
\tag{4.11}
\]

More importantly, if both row and column are restricted to `L'`, the exceptional row disappears and

\[
R[L',L']=(D-D_0)(Q_C)\quad\hbox{rowwise on }L',
\]

so

\[
\boxed{\operatorname{rank}R[L',L']\le2.}
\tag{4.12}
\]

Suppose for contradiction that `\|E\|_F<=1/4`. Since operator norm is bounded by Frobenius norm,

\[
s_8(A-E)\ge {3\over4}.
\tag{4.13}
\]

But `A-E=D_0+R` and `rank R<=5`. The baseline rank-perturbation inequality therefore gives

\[
{3\over4}\le s_8(D_0+R)\le s_3(D_0).
\tag{4.14}
\]

Thus at least three diagonal entries of `D_0` have modulus at least `3/4`. The `H` entries and the exceptional `e` entry are zero, so choose a three-set `J_0 subset L'` with

\[
|\lambda_i|\ge {3\over4}\quad(i\in J_0).
\tag{4.15}
\]

For `i in J_0`, using the no-pivot bounds and `E_ii=0`,

\[
|R_{ii}|=|A_{ii}-\lambda_i|
>{3\over4}-{1\over100}={74\over100}.
\tag{4.16}
\]

For distinct `i,j in J_0`,

\[
|R_{ij}|\le |A_{ij}|+|E_{ij}|
<\sqrt{\eta^2+\eta}+{1\over4}.
\tag{4.17}
\]

Hence each off-diagonal row sum is strictly less than

\[
2\left(\sqrt{101/10000}+{1\over4}\right)
=0.7009975124\ldots <0.74.
\tag{4.18}
\]

So `R[J_0,J_0]` is strictly row-diagonally dominant and invertible. This contradicts (4.12), which bounds its rank by two. Therefore

\[
\|E\|_F>{1\over4}.
\tag{4.19}
\]

Combining (4.9) and (4.19) yields

\[
{W'\over gp_*}>{1\over16},
\]

i.e.

\[
W'>{p_*g\over16}={49g\over1600}.
\]

This proves (4.5). QED.

The key rank accounting is `5+3=8` globally but only `2<3` on the selected nonexceptional physical coordinates. The single near-coloop is absorbed into the global rank budget without saturating the restricted rank contradiction.

## 5. Product-coordinate-safe density receiver

Randomly split the literal outside coordinates `L=I\sqcup J` with independent fair coins. Every term in `W'` has one distinguished row coordinate `i` and a disjoint three-set of column coordinates `T`; the event `i in I`, `T subset J` has probability `1/16`. Therefore some physical cut obeys

\[
\mathcal C
:=\sum_{\substack{i\in I\cap L'\\T\subset J,\ |T|=3}}
\det A[H\cup\{i\},T]^2
\ge {W'\over16}
>{49g\over25600}
\ge {49d_0\over25600}.
\tag{5.1}
\]

Numerically,

\[
{49d_0\over25600}=0.000698526133916109\ldots .
\tag{5.2}
\]

Put `M=A[H,J]`. For `i in I cap L'`, project the literal row `A[i,J]` orthogonally off `row(M)` and call the residual row `c_i`. Gram--Schmidt and Cauchy--Binet give

\[
\mathcal C=\det(MM^T)\sum_{i\in I\cap L'}\|c_i\|^2.
\tag{5.3}
\]

If the residual first-volume is diffuse, the reviewed grouped compiler at `(k,ell)=(2,1)` gives

\[
\|p_Q\|_\infty
\le C_{21}\,\mathcal C^{-1/6},
\qquad
C_{21}=3\,2^{1/6}e^{2/3}=6.558772623852\ldots .
\tag{5.4}
\]

If one residual row carries more than half of the first-volume, promote that literal physical coordinate as a third hub; the reviewed exact-rank-three terminal gives a smaller constant. Thus (5.4) holds without a leverage assumption. Inserting (5.1),

\[
\boxed{
\|p_Q\|_\infty
< C_{21}\left({49d_0\over25600}\right)^{-1/6}
=22.0187232089\ldots <22.02.
}
\tag{5.5}
\]

This branch has an integrable Fourier majorant and hence a continuous `C_0` density. Every same-bank quadratic term, every affine term, and all spectrum outside the displayed crossing remain in the phase.

Therefore the robust two-anchor terminal chamber from the proved `s_8` collar is completely paid; no high-leverage/near-coloop endpoint remains.

## 6. Full normalized `s_8` assembly

We now assemble all branches for `K=s=1`.

### 6.1 No pivot

The proved `s_8` terminal-collar theorem gives two alternatives.

- If `V_3(A)>=kappa^3`, with `kappa=1/6400`, a fair physical cut gives `E_3>=4^{-3}kappa^3`; the reviewed marginal-free order-three receiver gives
  \[
  \|p_Q\|_\infty<2400.
  \tag{6.1}
  \]
- Otherwise the robust literal pair (2.1) exists, and Sections 3–5 give
  \[
  \|p_Q\|_\infty<22.02.
  \tag{6.2}
  \]

Thus every no-pivot `s_8` state is paid.

### 6.2 Scalar pivot

A scalar pivot removes one Schur direction, so from `s_8(A)>=1` the scalar Schur complement retains at least seven unit singular directions.

- If that Schur complement has a manuscript pivot, the baseline pivot half-potential proposition needs only two unit directions and gives a full half-potential at most `601` after paying the far tail.
- If it has no pivot, seven directions imply the `s_5>=1` required by the baseline `k=2` spectral-to-volume proposition. After a fair cut, the reviewed order-two receiver gives a full half-potential `<153`.

Thus the Schur half-potential is at most `601`, and the scalar square profile gives

\[
\boxed{\|p_Q\|_\infty\le6010.}
\tag{6.3}
\]

This is exactly the same argument used in the reviewed nine-direction theorem; its internal spectral requirements are strictly below the seven directions available here.

### 6.3 Pair pivots

A definite pair has the direct determinant-scale bound `<32`. An indefinite pair loses at most two Schur directions; `s_8(A)>=1` leaves at least six, hence in particular the one surviving direction needed by the audited hyperbolic/log-potential argument. Its bound remains `<251`.

Therefore all normalized branches satisfy

\[
\boxed{\|p_Q\|_{\infty,\mathrm{ess}}\le6010.}
\tag{6.4}
\]

The baseline scaling `Y=KX` and spectral normalization by `s` restore (1.1).

## 7. Review gate and exact status

This file is a **complete candidate replacement proof from multiplicity nine to multiplicity eight**. The genuinely new step is Theorem 4.1, based on the observation that no-pivot entry bounds force at most one leverage above `0.51`, after which that one coordinate can be absorbed into the global rank budget while the restricted rank remains two.

I have not found an algebraic defect in the argument in this run. Nevertheless, under the owner protocol this is **NOT YET VALIDATED**. Validation requires two separate existing-worker end-to-end reviews of the full theorem, including:

1. the leverage probability identity and the `0.51` uniqueness argument;
2. the nonsymmetric one-exception completion and both rank bounds (4.11)–(4.12);
3. the `s_8 -> s_3(D_0)` rank shift and diagonal-dominance contradiction;
4. the grouped `(2,1)` receiver application; and
5. the complete pivot/no-pivot assembly.

Until those reviews exist, repository status should be `CANDIDATE_S8_PENDING_TWO_END_TO_END_REVIEWS`, not independently validated or released.

The unrestricted three-eigenvalue conjecture remains open.
