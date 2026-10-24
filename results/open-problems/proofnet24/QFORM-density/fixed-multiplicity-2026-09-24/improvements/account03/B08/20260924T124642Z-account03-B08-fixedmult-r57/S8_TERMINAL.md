# account03/B08 r57 — exact terminal structure below the nine-eigenvalue threshold

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T124642Z-account03-B08-fixedmult-r57`  
Baseline: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Status: **new proved supporting theorem; no eight-eigenvalue density theorem claimed**.

The sibling audit proves the nine-eigenvalue theorem in one independent review. This note identifies exactly what the current interpolation mechanism leaves if one tries to replace `s_9(A)>=1` by `s_8(A)>=1`.

Throughout
\[
 \eta=1/100,\qquad \kappa=1/80^2.
\]

## Theorem — `QFORM-S8-TERMINAL-R2-SATURATION-v1`

Let `A=A^T` have no `eta`-pivot and satisfy
\[
 s_8(A)\ge1.
\]
Assume the order-three crossing-volume conclusion fails at the manuscript scale:
\[
 V_3(A)<\kappa^3.
\]
Then all of the following hold.

### 1. The unique bad sampled ratio is `r=2`

The manuscript's proof works unchanged for every sampled ratio `r<=1`, since `8>=4r+1`. Hence
\[
 V_1(A)\ge\kappa,\qquad V_2(A)\ge\kappa^2,
\]
and therefore
\[
 0<V_2(A),\qquad \frac{V_3(A)}{V_2(A)}<\kappa.
\tag{1}
\]
Thus the only obstruction to the `k=3` spectral-to-volume argument at multiplicity eight is the terminal order-two seed.

### 2. Canonical order-two completion

Apply the audited volume-sampling lemma at `r=2`. There are disjoint two-sets `S,T`, with `B=A[S,T]` invertible and `L=[n]\\(S union T)`, for which
\[
 A=D+R+E,
\]
where `D` is diagonal and vanishes on `S union T`, `E` has zero diagonal, and
\[
 \|E\|_F\le3\sqrt\kappa=\frac3{80},
 \qquad \operatorname{rank}R\le6,
 \qquad R_{L,L}=P_{L,L},
 \qquad \operatorname{rank}R_{L,L}\le2,
\tag{2}
\]
with
\[
 P=A_{\cdot,T}B^{-1}A_{S,\cdot}.
\]
Put
\[
 c_0:=\frac17+\frac3{80}=\frac{101}{560}.
\tag{3}
\]
The no-pivot entry bound and (2) give, for distinct `i,j in L`,
\[
 |R_{ij}|=|A_{ij}-E_{ij}|<c_0.
\tag{4}
\]

### 3. Exactly two diagonal directions carry the terminal mass

Perturbation by `E` gives
\[
 s_8(D+R)\ge1-\frac3{80}=\frac{77}{80}.
\]
Since `rank R<=6`, the rank perturbation lemma implies
\[
 \boxed{s_2(D)\ge\frac{77}{80}.}
\tag{5}
\]

On the other hand define
\[
 \beta:=\eta+2c_0
 =\frac1{100}+2\left(\frac17+\frac3{80}\right)
 =\frac{519}{1400}.
\tag{6}
\]
There cannot be three indices in `L` with `|D_ii|>beta`. Indeed, on such a three-set `H_3`,
\[
 |R_{ii}|=|A_{ii}-D_{ii}|>\beta-\eta=2c_0,
\]
while by (4) each row has two off-diagonal entries of modulus `<c_0`. Hence `R[H_3,H_3]` is strictly row-diagonally dominant and has rank three, contradicting `rank R_{L,L}<=2`. Therefore
\[
 \boxed{s_3(D)\le\frac{519}{1400}.}
\tag{7}
\]
Equations (5)-(7) show that the terminal chamber contains exactly two large diagonal coordinates at the `77/80` level and cannot contain a third one above `519/1400`.

### 4. The full rank-six correction is quantitatively saturated

Use the standard singular-value inequality
\[
 s_{i+j-1}(X+Y)\le s_i(X)+s_j(Y).
\]
With `(i,j)=(3,6)`, (7) gives
\[
 \frac{77}{80}
 \le s_8(D+R)
 \le s_3(D)+s_6(R),
\]
so
\[
 \boxed{
 s_6(R)\ge
 \frac{77}{80}-\frac{519}{1400}
 =\frac{1657}{2800}
 =0.5917857142\ldots .}
\tag{8}
\]
Thus all six allowed singular directions of the global correction are genuinely present at a fixed scale.

### 5. A physical two-coordinate heavy block is uniformly invertible in the interpolant

Choose the two-set `H subset L` on which
\[
 |D_{ii}|\ge\frac{77}{80}.
\]
Because `R_{L,L}=P_{L,L}`, for `i in H`,
\[
 |P_{ii}|=|R_{ii}|
 \ge\frac{77}{80}-\frac1{100}
 =\frac{381}{400},
\tag{9}
\]
and for the two off-diagonal positions of this `2x2` block,
\[
 |P_{ij}|<c_0=\frac{101}{560}.
\tag{10}
\]
Consequently
\[
 |\det P_{H,H}|
 \ge\left(\frac{381}{400}\right)^2-\left(\frac{101}{560}\right)^2
 =\frac{857233}{980000}
 >0.8747275.
\tag{11}
\]
In particular `P[H,H]` is not merely rank two; it is uniformly far from singular.

Since
\[
 P_{H,H}=A_{H,T}B^{-1}A_{S,H},
\]
(11) gives the exact original-coordinate determinant chain
\[
 \boxed{
 |\det A[H,T]|\,|\det A[S,H]|
 \ge\frac{857233}{980000}\,|\det A[S,T]|.}
\tag{12}
\]
Here `S,H,T` are three pairwise disjoint physical two-banks.

### 6. Every nominal rank-two piece of the correction is necessary

Let `Q=R-P`, and write exactly as in the audited nonsymmetric support decomposition
\[
 R=P+Q_T+Q_S,
\qquad Q_T=\Pi_TQ,
\qquad Q_S=(I-\Pi_T)Q\Pi_S.
\tag{13}
\]
Each of `P,Q_T,Q_S` has rank at most two.

Fix one piece `C` among these three and replace it by a best rank-one approximation. The sum of that approximation and the other two exact rank-two pieces has rank at most five and approximates `R` with operator error `s_2(C)`. By the best-rank approximation formula,
\[
 s_6(R)\le s_2(C).
\]
Combining with (8),
\[
 \boxed{
 \min\{s_2(P),s_2(Q_T),s_2(Q_S)\}
 \ge\frac{1657}{2800}.}
\tag{14}
\]
Thus the terminal `s_8` state saturates all three rank-two channels simultaneously.

## 7. Designated account04/B08 theorem applied to the same `s_8` survivor

Use `QFORM-PHYSICAL-DELETION-CHILD-WINDOW-v1` from
`yspennstate/math-open-problems@a5e66e2944c89857a41d5e18c283d53a4307be76`, path
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B08/20260923T212412Z-account04-B08-QFORM-r2/REPORT.md`.

For every original coordinate deletion, write the child principal matrix as `C_i`. Embedding `C_i` back into the parent dimension changes `A` by rank at most two, hence
\[
 s_5(A)\le s_3(C_i).
\]
Since `s_8(A)>=1`, in particular `s_5(A)>=1`, so
\[
 s_3(C_i)\ge1
\tag{15}
\]
for **every** physical deletion `i`.

Therefore, if for even one child the spectral projection onto `|lambda(C_i)|>=1/64` satisfies
\[
 \max_j(P_{C_i}(1/64))_{jj}\le\frac1{32},
\]
the partner theorem applies at `m=1` and gives
\[
 \boxed{\|p_{X^TAX}\|_\infty<64,\qquad p\in C_0.}
\tag{16}
\]
It retains the parent scalar, all cross terms, all signs, and the full complementary spectrum by conditioning only the deleted original coordinate.

Thus any unpaid normalized `s_8` terminal survivor must satisfy the strong localization condition
\[
 \boxed{
 \forall i\ \exists j\ne i:\quad
 (P_{C_i}(1/64))_{jj}>1/32.}
\tag{17}
\]
After scaling, (16) is `<64 K^2/s` whenever the corresponding normalized window condition holds.

## 8. What this proves and what remains

This theorem does not prove the eight-eigenvalue density theorem. It shows that the first unresolved no-pivot `s_8` state is highly rigid:

- only the `r=2` sampled ratio can fail;
- exactly two diagonal directions carry the missing spectral mass;
- the rank-six correction has all six singular directions at scale at least `1657/2800`;
- each of its three rank-two support pieces is individually saturated;
- three disjoint physical two-banks satisfy the determinant chain (12);
- every physical deletion must have a localized `1/64` child spectral window unless the full density is already `<64`.

A valid `9 -> 8` proof must consume this simultaneous rank-two-saturation/localized-child state, or replace the present order-three interpolation route. The full three-eigenvalue conjecture and global continuity statement remain OPEN.
