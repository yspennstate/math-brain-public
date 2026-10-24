# F0011 — exact Hadamard entropy equivalence of the q=6 zero-minority contrast core

Date: 2026-09-20 UTC  
Role: C05 / R7-06 `Random Matrix Spectral Entropy`  
Canonical target: F0011 / Van H. Vu, *Recent progress in combinatorial random matrix theory*, Conjecture 9.4  
Status: **PROVED PARTIAL** toward the outside source, pending later independent review. This is a theorem about the normalized contrast-core relaxation, not a proof that every core lifts to an original F0011 sign-Gram root.

## 1. Source target and inherited bottleneck

Vu's Conjecture 9.4 asks for the total integral-spectrum probability for the symmetric Rademacher ensemble,

\[
\Pr\bigl(\operatorname{Spec}(M_n^{\rm sym})\subset\mathbb Z\bigr)
=2^{-(1/2+o(1))n^2}.
\]

The active C05 line is a restricted centered two-eigenvalue bridge. The latest own theorem reduced the entropy-dangerous rank-two support in the semidefinite `|r-lambda|=4`, `q=o(r)`, `q>4` shell to a two-class ternary inverse core. It proved that the unique zero-minority branch is

\[
\varepsilon=+1,\qquad q=6,
\]

and injects, after two-column completion, into Hadamard matrices of order `r-4`.

The missing strategic question was whether that Hadamard appearance is merely a convenient upper-bound device, or whether the normalized core equation itself already contains the full Hadamard enumeration problem. The answer is the latter.

Throughout this note put

\[
2m=r-q=r-6,\qquad N:=2m+2=r-4,
\qquad s:=\frac{m+1}{2}.
\]

Since `4|r`, `m` is odd and `4|N`.

In the zero-minority branch, after the inherited signed/permutation normalization, the ternary core has no negative entries and therefore is a binary matrix

\[
T=X=\begin{pmatrix}A&B\\C&F\end{pmatrix}
\in\{0,1\}^{2m\times2m}.
\]

After possibly swapping the two halves, the quotient parameters are

\[
\beta=s,\qquad \gamma=s-1,\qquad \alpha=s.
\]

Thus the exact row Gram matrix is

\[
XX^T
=sI_{2m}+
\begin{pmatrix}
sJ_m&sJ_m\\
sJ_m&(s-1)J_m
\end{pmatrix},
\tag{1.1}
\]

and the exact column Gram matrix is

\[
X^TX
=sI_{2m}+
\begin{pmatrix}
(s-1)J_m&sJ_m\\
sJ_m&sJ_m
\end{pmatrix}.
\tag{1.2}
\]

Equivalently, in block notation every row of `A,B,F` has sum `s`, every row of `C` has sum `s-1`, and the transposed statement holds with the two column halves interchanged in the same way.

Let `C_m` denote the set of binary matrices satisfying this normalized q=6 zero-minority core system.

## 2. New theorem A — every normalized core completes *canonically* to a Hadamard matrix

For `X in C_m`, define

\[
K_0:=J_{2m}-2X\in\{\pm1\}^{2m\times2m}.
\]

Order the core rows as `R_+,R_-`, each of size `m`, and the core columns as `C_-,C_+`, each of size `m`, according to the block structure in (1.1)--(1.2).

Adjoin two new rows `a,b` and two new columns `c,d`. Define the `N x N` sign matrix `K(X)` by

* row `a` is all `+1`;
* row `b` has signs `(+1,-1,-1_{C_-},+1_{C_+})` on `(c,d,C_-,C_+)`;
* a row in `R_+` has entries `(+1,+1,K_0(i,*))`;
* a row in `R_-` has entries `(+1,-1,K_0(i,*))`.

Then

\[
\boxed{K(X)K(X)^T=NI_N.}
\tag{2.1}
\]

Hence `K(X)` is a Hadamard matrix of order `N=r-4`.

### Proof

From (1.1), distinct top rows of `X` have intersection `s`, distinct bottom rows have intersection `s-1`, and a top/bottom pair has intersection `s`. Their respective row weights are `m+1` and `m`. Therefore distinct rows of `K_0=J-2X` have inner products

\[
-2\quad\text{within }R_+,
\qquad
-2\quad\text{within }R_-,
\qquad
0\quad\text{across }R_+\times R_-.
\tag{2.2}
\]

The appended `(c,d)` tails have inner products `+2,+2,0` in the same three cases, so all distinct core rows become orthogonal.

The row sums of `K_0` are `-2` on `R_+` and `0` on `R_-`; therefore the new all-ones row `a` is orthogonal to every core row after the tails are restored.

For a top row, both block row sums of `K_0` equal

\[
m-2s=-1.
\]

Thus its inner product with row `b` on the old coordinates is `-(-1)+(-1)=0`, while the two new coordinates contribute `1-1=0`.

For a bottom row, the `C_-` block has row sum

\[
m-2(s-1)=1,
\]

while the `C_+` block has row sum `m-2s=-1`. Hence its old-coordinate inner product with `b` is `-1-1=-2`, and the new coordinates contribute `1+1=2`.

Finally `a` and `b` are orthogonal because row `b` has equally many `+1` and `-1` entries. All rows have norm squared `N`, proving (2.1).

The map `X -> K(X)` is injective because deleting `a,b,c,d` and applying `X=(J-K_0)/2` recovers `X` exactly. Consequently

\[
\boxed{|C_m|\le H(N),}
\tag{2.3}
\]

where `H(N)` is the number of labelled Hadamard matrices of order `N`.

## 3. New theorem B — every Hadamard matrix punctures back to a normalized q=6 core after standard switching/permutation

Conversely, let `K` be an arbitrary labelled Hadamard matrix of order `N=2m+2>2`.

Choose a row `a` and column `c` and switch rows and columns so that row `a` and column `c` are all `+1`. Choose any other row `b`. Since `b` is orthogonal to `a`, it contains `N/2` negative entries; choose a column `d` with

\[
K_{b,d}=-1.
\]

After the normalization, the `2 x 2` corner on rows `(a,b)` and columns `(c,d)` is

\[
\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
\tag{3.1}
\]

Delete rows `a,b` and columns `c,d`. Among the remaining rows, exactly `m` have `K_{i,d}=+1` and exactly `m` have `K_{i,d}=-1`; call these `R_+,R_-`. Among the remaining columns, exactly `m` have `K_{b,j}=-1` and exactly `m` have `K_{b,j}=+1`; call these `C_-,C_+`. Permute rows and columns so these classes are consecutive.

Let `K_0` be the resulting `2m x 2m` punctured matrix and define

\[
\boxed{X=(J_{2m}-K_0)/2.}
\tag{3.2}
\]

Then

\[
\boxed{X\in C_m.}
\tag{3.3}
\]

### Proof of the block degrees

Take `i in R_+`. Orthogonality of row `i` with `a` says the full row sum is zero. Removing columns `c,d`, whose entries are both `+1`, leaves punctured row sum `-2`. Orthogonality with row `b` says

\[
\sum_{C_-}K_{ij}=\sum_{C_+}K_{ij}.
\]

Hence both block sums are `-1`, so both blocks contain exactly

\[
(m+1)/2=s
\]

negative entries. Therefore the corresponding rows of `A,B` both have sum `s`.

Take `i in R_-`. Removing `c,d` removes `+1,-1`, so the punctured row sum is zero. Orthogonality with `b` gives

\[
\sum_{C_-}K_{ij}-\sum_{C_+}K_{ij}=2.
\]

Thus the two block sums are `+1,-1`, so the negative counts are `s-1,s`. Therefore rows of `C,F` have sums `s-1,s`.

The same argument applied to columns gives the transposed block degrees required by (1.2).

### Proof of the Gram equations

For two remaining rows with the same `d`-sign, the contribution of deleted columns `(c,d)` to their full Hadamard inner product is `2`; therefore their punctured inner product is `-2`. For rows with opposite `d`-sign the deleted contribution is zero, so their punctured inner product is zero.

Using `K_0=J-2X` and the just-proved row weights converts these three inner products exactly into the intersection numbers `s,s-1,s` in (1.1). The column argument is identical and gives (1.2). Thus `X in C_m`.

So every Hadamard equivalence orbit contains at least one canonical completion coming from `C_m`.

## 4. New theorem C — the relaxed q=6 core and Hadamard enumeration have the same quadratic entropy

The signed row/column permutation group has size at most

\[
2^{2N}(N!)^2=2^{O(N\log N)}.
\]

By Theorem B, every labelled Hadamard matrix can be moved by such an operation to a representative in the image of `C_m`. Therefore

\[
\boxed{
\frac{H(N)}{2^{2N}(N!)^2}
\le |C_m|
\le H(N).
}
\tag{4.1}
\]

Equivalently,

\[
\boxed{
\log_2 |C_m|
=\log_2 H(N)+O(N\log N)
}
\tag{4.2}
\]

in the entropy-scale sense that the two logarithms differ by at most `O(N log N)`.

This is the main strategic conclusion of the run:

> **The normalized q=6 zero-minority contrast-core problem is not merely bounded above by Hadamard enumeration. It is Hadamard enumeration up to subquadratic normalization entropy.**

Thus a theorem using only the normalized inverse-core equations cannot prove a `2^{o(r^2)}` bound for this branch without, at the same entropy scale, proving the open square-Hadamard bound

\[
H(N)=2^{o(N^2)}.
\]

The previous one-way completion therefore cannot be the end of the bounded-defect attack.

## 5. What this does and does not prove for F0011

This theorem is an explicit obstruction to an over-broad intermediate reduction, not a counterexample to Vu's conjecture.

The set `C_m` is the **normalized contrast-core relaxation**. The proof above does **not** show that every `X in C_m` extends through the source-specific anchor rows/columns to an original sign-Gram root in the F0011 shell. Hence (4.1) is not asserted as a lower bound for the actual F0011 root count.

What it proves is that any next entropy theorem must exploit information discarded by the relaxed core system — specifically, the original anchor/lift compatibility, higher-shell coupling, symmetry of the surrounding two-eigenvalue root, or a genuinely new Hadamard-counting theorem. Re-running a core-only `TS=ST=sI` count cannot bypass the Hadamard barrier.

This also clarifies the growing-`q` strategy. The punctured partial-Hadamard class contraction from the previous run remains useful when `q -> infinity`, but a bounded-`q` recursive leaf must be treated as a genuine design atom rather than assumed to have subquadratic entropy for free.

## 6. Singular/corank endpoint

Nothing in the argument inverts the original sign cross-block from which the contrast core was derived. The singular/corank endpoint therefore remains part of the inherited C05 framework. The only inversion used earlier is the contrast-core inverse identity `TS=sI`, which is already valid before this q=6 specialization.

## 7. Remaining gap and next attack

The immediate missing theorem is now more precise.

* **Growing q:** exploit the `Theta(q)` refined row and column anchor classes simultaneously to bound their cross-class gluing entropy. The square dimensions of the partial-Hadamard children already contract to `o(m^2)`.
* **Bounded q:** do not attempt a core-only entropy bound. Instead use the source-specific anchor/lift compatibility to decide which Hadamard/design cores actually extend to full sign-Gram roots. The first concrete target is the q=6 canonical core above: characterize the extra anchor equations on the completed Hadamard `K(X)` and prove either a strict entropy loss inside Hadamard space or an explicit large liftable family.

The bounded-rank `q<=4` Hadamard/D-optimal branch, higher semidefinite shells, indefinite defects, full centered two-eigenvalue count, and Vu's total integral-spectrum conjecture remain open.
