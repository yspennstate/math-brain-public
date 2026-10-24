# Pullback theorem — spend surplus terminal cross rank instead of inverting physical pivots

This strengthens REPORT.md. It removes *all actual-pivot lower bounds* when the base terminal cross packet has enough surplus rank.

## Theorem: Schur-packet pullback through an arbitrary rank-k spectral addition

Let `B` be a real symmetric matrix in original coordinates and let `K` be a physical coordinate set such that the principal block
\[
P:=B[K,K]
\]
is invertible. Write `R=K^c` and let
\[
S:=B[R,R]-B[R,K]P^{-1}B[K,R]
\]
be the physical Schur complement of the *base* matrix. Let `I,J` be disjoint subsets of `R`. Define
\[
T:=S[I,J]
\]
and
\[
h:=\operatorname{rank}\!\left(B[I,K]P^{-1}B[K,J]\right)\le |K|.
\]

Let `E` be an arbitrary symmetric matrix of rank at most `k`, with no sign or operator-norm restriction, and put `A=B+E`. Then
\[
\boxed{s_r(A[I,J])\ge s_{r+h+k}(T)}
\tag{P1}
\]
for every admissible `r`.

Consequently, if
\[
\boxed{s_{h+k+5}(T)\ge\sigma>0,}
\tag{P2}
\]
then the full quadratic form `X^TAX`, for arbitrary independent cap-one input densities, has a continuous density satisfying
\[
\boxed{\|p_{X^TAX}\|_\infty\le\frac{5e}{2\sigma}.}
\tag{P3}
\]
The constant is independent of the sizes and signs of every nonzero eigenvalue of `E`.

### Proof

From the definition of the base Schur complement,
\[
T=B[I,J]-H,
\qquad
H:=B[I,K]P^{-1}B[K,J].
\]
Thus
\[
A[I,J]=T+H+E[I,J].
\]
By construction `rank(H)=h`, while every submatrix of a rank-`k` matrix has rank at most `k`; hence
\[
\operatorname{rank}(H+E[I,J])\le h+k.
\]
For rectangular singular values, a rank-`d` perturbation obeys
\[
s_r(M+F)\ge s_{r+d}(M).
\]
Taking `M=T`, `F=H+E[I,J]`, and `d=h+k` proves (P1). Under (P2), (P1) with `r=5` gives `s_5(A[I,J])>=sigma`. The completed regularized physical-cross determinant theorem applies directly to the original matrix `A` and yields (P3), including continuity and vanishing at infinity. No Schur complement of `A` is formed, no actual pivot is divided by, and no spectral rotation is used.

## Chain version

If `K={i_1,...,i_m}` is produced by a scalar base-Schur chain with nonzero base pivots, then `P=B[K,K]` is invertible. Therefore one may pull the terminal packet directly to the original matrix. The crude universal rank cost is `h<=m`; hence
\[
s_{m+k+5}(T)\ge\sigma
\quad\Longrightarrow\quad
\|p_{X^TAX}\|_\infty\le\frac{5e}{2\sigma}.
\tag{P4}
\]
This is independent of every actual pivot of `A`, including exact pivot cancellation.

Thus there are now two complementary additional-eigenvalue mechanisms:

- few terminal cross directions + noncollapsing actual pivots: REPORT.md gives `sigma^{-1} max{5e/2,4/delta}` from only `k+5` base terminal directions;
- surplus terminal cross directions: (P4) spends at most one cross direction per eliminated base coordinate and avoids every actual pivot entirely.

The second mechanism is a rigorous aggregate-before-inversion certificate switch.

## Relation to the account02/B12 Möbius stress family

The partner family shows that one cannot infer a lower bound for a chosen actual scalar pivot from the magnitude of an added eigenvalue: the new eigenvalue may tend to zero or infinity while the pivot tends to zero. The pullback theorem explains a general escape route from that pole. If a terminal cross packet has sufficient surplus rank, do not use the unstable Möbius denominator at all; pull the packet to a physical cross block of the original matrix and apply the regularized determinant theorem directly.

In the four-dimensional partner stress family there are not enough cross directions to pay (P2), and the partner's complementary physical three-coordinate theorem instead gives the uniform bound `C_*/2`. Thus the two certificate switches cover genuinely different geometries rather than duplicating one another.

## Remaining full-target debt

The bare hypothesis `s_3(A)>=1` does not force a Schur packet with `h+k+5` robust cross directions; singleton-plus-two-bank examples already show that fixed high cross rank is not universal. Hence (P3) is a genuine stability/reduction theorem, not a proof of the full conjecture. The next structural question is whether the current ridge/grouped-bank branches plus low-rank packet pullback exhaust the matrices that fail all physical pair/triple certificates.
