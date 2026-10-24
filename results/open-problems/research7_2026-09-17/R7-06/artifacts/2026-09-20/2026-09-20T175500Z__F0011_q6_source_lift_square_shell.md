# F0011 — q=6 source-lift rigidity: one giant anchor block and a square-order arithmetic shell

Date: 2026-09-20 UTC  
Role: C05 / R7-06 `Random Matrix Spectral Entropy`  
Canonical target: F0011 / Van H. Vu, *Recent progress in combinatorial random matrix theory*, Conjecture 9.4  
Status: **PROVED PARTIAL** toward the outside source, pending later independent review

## 1. Exact source target and inherited point

Vu's Conjecture 9.4 concerns the symmetric Rademacher matrix `M_n^sym`, with the entries on and above the diagonal independent fair signs and symmetry below the diagonal:

\[
\Pr\!\bigl(\operatorname{Spec}(M_n^{\rm sym})\subset\mathbb Z\bigr)
=2^{-(1/2+o(1))n^2}.
\]

Equivalently, the total number of labelled symmetric sign matrices with integral spectrum should be `2^{o(n^2)}`. The source quantifier is the total integral-spectrum event, not a fixed-spectrum event. The earlier F0011 line observed that only `2^{O(n)}` integral spectra are arithmetically possible, so a **uniform** `2^{o(n^2)}` bound for every fixed spectrum would suffice after summing spectra; that inherited observation is not a source statement and is not reproved here.

The active C05 bridge is the centered two-eigenvalue family. In the positive semidefinite `|r-lambda|=4` shell with `q>4`, every sign root `C in {+/-1}^{r x r}` has row and column block-Gram forms

\[
CC^T=(r-4)I+4BB^T,
\qquad
C^TC=(r-4)I+4B'B'^T,
\]

where `B,B'` are membership matrices of `q` row and column blocks, and the row/column block-size multisets agree. For a block of size `a`, the exceptional Gram eigenvalue is

\[
\mu_a=r+4(a-1).
\]

The latest own result proved that the unique zero-minority rank-two contrast branch is

\[
q=6,
\qquad
\varepsilon=+1,
\]

and that its **normalized contrast-core relaxation** is Hadamard-entropy equivalent, up to `2^{O(r log r)}` normalization, to Hadamard matrices of order `r-4`. That equivalence deliberately discarded the original six anchor rows and six anchor columns. The missing theorem was to pull the source-specific anchor/lift equations back through the normalized core.

This note does that. The outcome is a strong source-specific arithmetic restriction: an actually liftable q=6 zero-minority core can occur only when

\[
\boxed{r=12u^2+4}
\]

for an integer `u>=1`; moreover one row block and one column block are forced to have size `6u^2`, the other five sizes are all even, and the smallest candidate `u=1` is impossible.

No small-order census is used.

---

## 2. q=6 zero-minority support bookkeeping

Write

\[
s:=\frac r4-1,
\qquad
r=4s+4,
\qquad
d=r-6=4s-2=2m,
\qquad
m=2s-1.
\]

Choose one row anchor `g_i` in each of the six row blocks `G_i` and one column anchor `h_j` in each of the six column blocks `H_j`. On the `d x d` non-anchor grid define the inherited discrepancy masks

\[
U_{g,h}:=C_{g_i,h},
\qquad
V_{g,h}:=C_{g,h_j},
\]

and binary supports

\[
X_{g,h}:=1_{\{C_{g,h}\ne V_{g,h}\}},
\qquad
Y_{g,h}:=1_{\{C_{g,h}\ne U_{g,h}\}}.
\]

The exact anchor identity from the preceding binary-support reduction is

\[
Y=X\oplus E,
\qquad
E_{g,h}=1_{\{U_{g,h}\ne V_{g,h}\}}.
\]

In the q=6 zero-minority rank-two branch, after merely labelling the two defect-support halves, `E` is the complete bipartite two-half mask

\[
E=
\begin{pmatrix}
0&J_m\\
J_m&0
\end{pmatrix}.
\]

Call the two non-anchor row halves `R_+,R_-` and the two non-anchor column halves `C_-,C_+`, so `E=1` exactly on `R_+ x C_+` and `R_- x C_-`.

The inherited quotient values are

\[
\beta=s,
\qquad
\gamma=s-1,
\qquad
|\alpha|=s,
\]

and zero minority means the two diagonal ternary blocks have support degree exactly `s`. Therefore the support matrix `X=|T|` has exact row and column weights

\[
\begin{array}{c|cc}
& R_+ & R_-\\ \hline
|X\text{-row}|&2s&2s-1
\end{array}
\]

and

\[
\begin{array}{c|cc}
& C_- & C_+\\ \hline
|X\text{-column}|&2s-1&2s.
\end{array}
\]

Because `Y=X xor E`, the `Y` row weights are swapped:

\[
|Y\text{-row}|=
\begin{cases}
2s-1,&g\in R_+,\\
2s,&g\in R_-.
\end{cases}
\]

These are support statements only; they survive every signed normalization used to put the rank-two defect into complete-bipartite form.

---

## 3. New theorem I — the six anchor coordinates have an exact 1/0 discrepancy pattern

Two distinct rows in the same original row block have Gram inner product `4`. Since the rows are signs of length `r=4s+4`, their Hamming distance is

\[
\frac{r-4}{2}=2s.
\]

For a non-anchor row `g in G_i`, the support of `Y` records precisely the disagreements between row `g` and its row anchor `g_i` on the **non-anchor columns**. Hence the number of disagreements on the six anchor columns is

\[
2s-|Y_g|.
\]

Thus

\[
\boxed{
\begin{array}{ll}
g\in R_+:&\text{row }g\text{ differs from its row anchor on exactly one of the six column anchors},\\
g\in R_-:&\text{row }g\text{ agrees with its row anchor on all six column anchors}.
\end{array}}
\tag{3.1}
\]

The column Gram has the same block form, so the identical argument on columns uses the support of `X`. A non-anchor column and its column anchor also have Hamming distance `2s`. Therefore

\[
\boxed{
\begin{array}{ll}
h\in C_-:&\text{column }h\text{ differs from its column anchor on exactly one of the six row anchors},\\
h\in C_+:&\text{column }h\text{ agrees with its column anchor on all six row anchors}.
\end{array}}
\tag{3.2}
\]

This is the first source-specific constraint absent from the relaxed Hadamard core.

---

## 4. New theorem II — complete-bipartite defect support forces one giant row block and one giant column block

Let

\[
a_{ij}:=C_{g_i,h_j}\in\{\pm1\}
\]

be the `6 x 6` anchor-anchor sign table.

For a non-anchor row `g in G_i`, define

\[
\rho_g(j):=1_{\{C_{g,h_j}\ne a_{ij}\}}.
\]

For a non-anchor column `h in H_j`, define

\[
\sigma_h(i):=1_{\{C_{g_i,h}\ne a_{ij}\}}.
\]

Then, because `U_{g,h}` and `V_{g,h}` are compared to the same anchor-anchor sign `a_{ij}`,

\[
\boxed{E_{g,h}=\rho_g(j)\oplus\sigma_h(i).}
\tag{4.1}
\]

By (3.1), every `g in R_+` has exactly one `j` with `rho_g(j)=1`, while every `g in R_-` has `rho_g=0`. By (3.2), every `h in C_-` has exactly one `i` with `sigma_h(i)=1`, while every `h in C_+` has `sigma_h=0`.

Now use the complete-bipartite support of `E`.

### Top-right rectangle

For `g in R_+` and `h in C_+`, equation (4.1) reduces to

\[
1=E_{g,h}=\rho_g(j),
\]

where `j` is the original column-block label of `h`. Since `rho_g` has exactly one `1`, **all columns of `C_+` belong to one and the same original column block**. Call it `H_{j_*}`. The same equation then forces every `g in R_+` to use `j_*` as its unique anchor-column discrepancy.

### Bottom-left rectangle

For `g in R_-` and `h in C_-`, equation (4.1) reduces to

\[
1=E_{g,h}=\sigma_h(i),
\]

where `i` is the original row-block label of `g`. Since `sigma_h` has exactly one `1`, **all rows of `R_-` belong to one and the same original row block**. Call it `G_{i_*}`. Every `h in C_-` uses `i_*` as its unique anchor-row discrepancy.

### Top-left rectangle

For `g in R_+`, `h in C_-`, we have `E_{g,h}=0`, so

\[
1_{\{j=j_*\}}=1_{\{i=i_*\}}.
\tag{4.2}
\]

Since both halves are nonempty, (4.2) gives only two possibilities:

1. all rows in `R_+` also lie in `G_{i_*}` and all columns in `C_-` also lie in `H_{j_*}`; or
2. no row in `R_+` lies in `G_{i_*}` and no column in `C_-` lies in `H_{j_*}`.

The first possibility is impossible in the inherited q>4 shell for `r>12`. It would give row-block sizes

\[
\{2m+1,1,1,1,1,1\},
\]

which contains distinct odd block sizes. The two-sided quotient theorem already proved that if two distinct block sizes occur in this shell, then **every** occurring block size is even.

Therefore only possibility 2 remains. Hence

\[
\boxed{|G_{i_*}|=|H_{j_*}|=m+1=2s.}
\tag{4.3}
\]

Moreover the other five row blocks partition `R_+` together with their five anchors, and the other five column blocks partition `C_-` together with their five anchors. Thus their sizes each sum to

\[
2s+4.
\tag{4.4}
\]

Since not all six blocks can have size `2s`, distinct sizes occur. The same quotient parity theorem therefore implies that **all six row block sizes and all six column block sizes are even**.

The size `2s` is unique: if a second block also had size `2s`, the remaining four positive even block sizes would have to sum to `4`, impossible. Therefore

\[
\boxed{
2s\text{ occurs with multiplicity exactly one in both the row and column size multisets.}
}
\tag{4.5}
\]

This is a much stronger lift condition than Hadamard completion alone.

---

## 5. New theorem III — multiplicity-one quotient forces a square shell

For a block of size `a`, the two-sided quotient theorem gives an integral size-class quotient matrix `M_a` satisfying

\[
M_a^TM_a=M_aM_a^T=\mu_a I,
\qquad
\mu_a=r+4(a-1).
\]

By (4.5), the size class `a=2s` has multiplicity one. Thus `M_{2s}` is a `1 x 1` integer matrix, say `[t]`, and

\[
t^2=\mu_{2s}.
\]

But

\[
\mu_{2s}
=r+4(2s-1)
=(4s+4)+(8s-4)
=12s.
\]

Therefore

\[
\boxed{12s=t^2.}
\tag{5.1}
\]

Since `12 | t^2`, one has `6 | t`; write `t=6u`. Then

\[
\boxed{s=3u^2.}
\tag{5.2}
\]

Consequently every actually liftable q=6 zero-minority source root satisfies

\[
\boxed{
r=4s+4=12u^2+4,}
\tag{5.3}
\]

and its Hadamard completion from the preceding run has order

\[
\boxed{N=r-4=12u^2.}
\tag{5.4}
\]

The distinguished row and column blocks have size

\[
\boxed{2s=6u^2.}
\tag{5.5}
\]

Thus the Hadamard-hard normalized core does **not** lift at arbitrary Hadamard orders. Source compatibility restricts it to the sparse square-order subsequence `12u^2`, and simultaneously forces a unique block containing exactly half of the `N=12u^2` Hadamard-completion scale.

This does not yet count the liftable Hadamards at the admissible orders, so it is not an entropy closure.

---

## 6. Remaining five block sizes and an additional quotient obstruction

Write the other five block sizes as

\[
2c_1,\ldots,2c_5,
\qquad
c_i\ge1.
\]

From (4.4) and `s=3u^2`,

\[
\boxed{c_1+\cdots+c_5=s+2=3u^2+2.}
\tag{6.1}
\]

The row and column multisets of these five sizes agree.

If a value `c` occurs with odd multiplicity `ell` among the five, then the corresponding quotient block has

\[
M_{2c}^TM_{2c}=4(s+2c)I_\ell.
\]

Taking determinants, the odd exponent forces `s+2c` to be a square. Hence every odd-multiplicity residual size class obeys

\[
\boxed{3u^2+2c=v^2}
\tag{6.2}
\]

for an integer `v`. Since the total residual multiplicity is five, at least one residual size class has odd multiplicity, so at least one equation (6.2) must hold.

A crude but sometimes useful local norm obstruction is also automatic. Because the entries of `M_{2c}` are even and have absolute value at most `2c`, writing `M_{2c}=2Q_c` gives

\[
Q_c^TQ_c=(s+2c)I_\ell,
\qquad
|Q_c(i,j)|\le c.
\]

Thus

\[
\boxed{s+2c\le \ell c^2.}
\tag{6.3}
\]

These are finite-dimensional arithmetic tests on the five-block residue profile, obtained before any Hadamard enumeration.

---

## 7. Exact exclusion of the first arithmetic candidate

The first square-shell candidate is `u=1`. Then

\[
s=3,
\qquad
r=16,
\qquad
N=r-4=12,
\]

and the distinguished block has size `6`. Equation (6.1) gives

\[
c_1+\cdots+c_5=5,
\]

so necessarily

\[
c_1=\cdots=c_5=1.
\]

Thus the five residual blocks all have size `2`, and their size-class quotient is a `5 x 5` integer matrix satisfying

\[
M_2^TM_2=20I_5,
\qquad
M_2(i,j)\in\{-2,0,2\}.
\]

Write `M_2=2Q`. Then

\[
Q^TQ=5I_5,
\qquad
Q\in\{-1,0,1\}^{5\times5}.
\]

Every column has squared norm `5`, so every entry in every column is nonzero. Hence `Q` is a `5 x 5` sign matrix. But the inner product of two sign vectors of odd length five is odd and can never equal zero, contradicting `Q^TQ=5I`.

Therefore

\[
\boxed{u=1\text{ is impossible}.}
\tag{7.1}
\]

So the first possible source-liftable q=6 zero-minority order, if any exists at all, must have `u>=2`, i.e.

\[
r\ge52,
\qquad
N=r-4\ge48.
\]

This is an exact theorem, not a census.

---

## 8. Relation to the previous Hadamard-entropy obstruction

The preceding run proved that the relaxed q=6 core family has the same leading entropy as all Hadamard matrices of order `N=r-4`. That result is still correct for the relaxation.

The new source-specific theorem shows that actual F0011 lifts occupy a much thinner part of that relaxed family:

* the order must be `N=12u^2`;
* the original six row blocks and six column blocks contain unique distinguished blocks of size `N/2=6u^2`;
* the remaining five block sizes are even and satisfy (6.1)--(6.3);
* the first arithmetic candidate `N=12` is impossible.

This does **not** yet prove a subquadratic count at the admissible orders `12u^2`: the family of Hadamard matrices of those orders may still be quadratically large, and the present theorem has not yet quantified how many satisfy the marked six-anchor lift equations.

What has changed is the bottleneck. The correct next bounded-q problem is no longer an arbitrary Hadamard count. It is:

> count Hadamard completions of order `12u^2` that admit the six-anchor lift with one forced `6u^2` block and a five-block even residual quotient satisfying the square/norm constraints above.

That is strictly more source-specific than the core-only relaxation.

The singular/corank endpoint remains untouched by this argument: no inversion of the original sign cross-block `C` is used here. The theorem concerns the positive q=6 shell reached through the singular-safe contrast formalism.

---

## 9. Current literature boundary, checked 20 September 2026

A bounded fresh search did not surface a resolution of Vu's exact Conjecture 9.4. This is negative-search evidence only, not an openness certificate.

Ferber--Jain--Zhao remains the relevant general square-Hadamard counting boundary: their anti-concentration method gives a strict constant quadratic improvement, not `H(N)=2^{o(N^2)}`. Damek Davis's 31 March 2026 theorem counts rectangular partial Hadamards in the cubic regime, relevant to the growing-q child classes but not to this fixed-q marked-lift problem. Valtonen's September 2026 classification of symmetric Hadamard matrices is finite-order (through order 32) and does not supply the needed asymptotic entropy theorem.

No external novelty claim is made for the elementary determinant-square or quotient arguments in isolation. The project result is their forced combination with the exact q=6 anchor-discrepancy geometry of the F0011 source lift.

---

## 10. Obligation delta and next attack

New proved partial statements in this run:

* exact `1/0` anchor-coordinate discrepancy counts on the four q=6 contrast halves;
* complete-bipartite defect support forces all `R_-` rows into one original row block and all `C_+` columns into one original column block;
* the same-half equations and the inherited parity theorem force those blocks to have exact size `2s` and to be unique;
* multiplicity one in the integer quotient forces `12s` to be a square, hence `s=3u^2`, `r=12u^2+4`, and Hadamard completion order `N=12u^2`;
* the remaining five block sizes are even, sum as in (6.1), and every odd-multiplicity residual size class obeys a square condition;
* the first candidate `u=1` is impossible by a `5 x 5` quotient parity contradiction.

Still open:

* count the marked six-anchor liftable Hadamards at `N=12u^2`, `u>=2`;
* growing-q cross-class gluing entropy;
* bounded `q<=4` Hadamard/D-optimal leaves;
* higher semidefinite shells and indefinite defects;
* the full centered two-eigenvalue count;
* Vu's total integral-spectrum conjecture.

### Next concrete attack

For `u>=2`, expose the unique distinguished `6u^2 x 6u^2` row/column block and its `1 x 1` quotient value `+/-6u`. Pull this regular block through the canonical Hadamard completion of order `12u^2`. The target is an explicit marked-Hadamard condition (regular half-set / constant-sum submatrix) strong enough to admit anti-concentration or a contracting design recursion. In parallel, use the fixed dimension at most five of every residual quotient block to enumerate **symbolically**, not by small-n census, the allowed multiplicity patterns and norm forms from (6.2)--(6.3).

Frozen full-source finite metric remains

\[
\boxed{N_{\rm exact}:9\to9.}
\]

No small-order census was run.