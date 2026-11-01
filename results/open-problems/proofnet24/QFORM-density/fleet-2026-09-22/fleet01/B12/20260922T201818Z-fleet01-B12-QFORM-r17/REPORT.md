# fleet01/B12 QFORM r17 — exact low-rank spectral-addition transport through physical Schur chains

Status: **PROVED_SUPPORTING_THEOREM / FULL TARGET OPEN**.

Target retained: for independent real coordinates with densities bounded by one and a symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal density bound for the quadratic form. This report proves a conditional stability theorem for arbitrary-rank spectral additions; it does not close the universal three-eigenvalue reduction.

## Source pins and corrections used



Completed dependencies actually used:

1. `fleet02/B12`, `QFORM lossless extra-eigenvalue peeling`, canonical `yspennstate/math-open-problems@4b8eb43e9d001d41de6190b587fefe8fdea2006b`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B12/20260922T185427Z-fleet02-B12-QFORM-r11/REPORT.md`. Used at the exact density recurrence
   \[
   M_{j-1}\le 2\sqrt{M_j/|a_j|},\qquad
   2\sqrt{M/\eta}\le \max\{M,4/\eta\}.
   \]
2. `fleet02/B12`, exact one-spike Möbius stress family, canonical `yspennstate/math-open-problems@5295a978b9e3336cc823f0e631bde093c30a8a4d`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B12/20260922T1953Z-fleet02-B12-qform-r16/REPORT.md`. The rank-one specialization of the new matrix update below reproduces its Möbius denominator exactly; its complementary-three-coordinate estimate is used as the explicit certificate switch at a pivot pole.
3. Regularized physical-cross determinant theorem, canonical `yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`, path `proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`. Five physical cross singular values at least `sigma` imply a continuous terminal density bounded by `5e/(2 sigma)`, with arbitrary self blocks and outside couplings.

## 1. Exact low-rank Schur transport identity

Let
\[
B=\begin{pmatrix}\alpha&b^T\\ b&D\end{pmatrix},\qquad \alpha\ne0,
\]
and let an arbitrary symmetric rank-at-most-`k` perturbation be represented as
\[
E=UCU^T,\qquad
U=\begin{pmatrix}u\\V\end{pmatrix},
\]
where `u` is one row and `C=C^T` is `k x k`. Put
\[
A=B+E,
\qquad
a=\alpha+uCu^T.
\]
Assume also `a!=0`. Define
\[
W:=V-\frac{b u}{\alpha},
\qquad
C':=C-\frac{Cu^T uC}{a}.
\]
Then the two physical scalar Schur complements satisfy the exact identity
\[
\boxed{
\operatorname{Sc}(A)=\operatorname{Sc}(B)+W C' W^T.
}
\tag{1}
\]
In particular,
\[
\boxed{
\operatorname{rank}\bigl(\operatorname{Sc}(A)-\operatorname{Sc}(B)\bigr)\le k.
}
\tag{2}
\]

### Proof

Expand the difference:
\[
\begin{aligned}
\operatorname{Sc}(A)-\operatorname{Sc}(B)
&=VCV^T-
\frac{(b+VCu^T)(b+VCu^T)^T}{a}
+\frac{bb^T}{\alpha}.
\end{aligned}
\]
The update matrix obeys
\[
C'u^T=\frac{\alpha}{a}Cu^T,
\qquad
u:=uC'u^T=\frac{\alpha}{a}uCu^T.
\]
Expanding `W C' W^T` therefore gives
\[
VCV^T-\frac{VCu^T uCV^T}{a}
-\frac{VCu^T b^T+b uCV^T}{a}
+\frac{uCu^T}{\alpha a}bb^T,
\]
and the last coefficient is exactly
\[
\frac1\alpha-\frac1a
=\frac{uCu^T}{\alpha a}.
\]
This is the preceding Schur-complement difference, proving (1), and (2) follows immediately.

If `C` is invertible, then the update has the equivalent inverse form
\[
\boxed{(C')^{-1}=C^{-1}+\alpha^{-1}u^Tu}
\tag{3}
\]
and hence the determinant transport law
\[
\boxed{\det C'=\det C\,\frac{\alpha}{a}.}
\tag{4}
\]
Indeed (3) is the Sherman--Morrison formula, and (4) follows from the matrix determinant lemma.

### Rank-one specialization and partner Möbius law

For `k=1`, write `C=(c)`. Then
\[
\boxed{c'=\frac{c\alpha}{\alpha+c u^2}.}
\tag{5}
\]
This is the exact scalar Möbius transport observed independently by `fleet02/B12`.

Apply (5) to its family
\[
B=2\sigma I_4,
\qquad
E=(\tau-2\sigma)vv^T,
\qquad
v=(\sqrt q,\sqrt{1-q},0,0).
\]
The physical pivot is
\[
a=2\sigma(1-q)+\tau q.
\]
Formula (1) gives the first residual eigenvalue
\[
2\sigma+\frac{2\sigma(\tau-2\sigma)(1-q)}{a}
=\frac{2\sigma\tau}{a},
\]
with the other two residual eigenvalues exactly `2 sigma`, reproducing the partner's exact formula.

The same partner result proves the complementary physical block on coordinates `{2,3,4}` has two eigenvalues exactly `2 sigma` for every `tau`; the completed physical-three-coordinate theorem therefore yields the actual inequality
\[
\boxed{\|p_{X^TAX}\|_\infty\le C_*/2
=12.091519144980758\ldots}
\tag{6}
\]
for all real `tau`, including the true Möbius pole `a=0`. Thus a valid proof must switch certificates before division by a collapsing pivot; (6) is an explicit successful switch, not merely a citation.

## 2. Iteration: arbitrary low-rank additions never increase their rank budget

Let `B^(0)` be any real symmetric matrix and `E^(0)` any symmetric matrix of rank at most `k`; put
\[
A^{(0)}=B^{(0)}+E^{(0)}.
\]
Fix distinct original coordinates `i_1,...,i_m`. Recursively form the physical scalar Schur complements
\[
B^{(j+1)}=\operatorname{Sc}_{i_{j+1}}(B^{(j)}),
\qquad
A^{(j+1)}=\operatorname{Sc}_{i_{j+1}}(A^{(j)}),
\]
assuming at each stage that both the base pivot and actual pivot are nonzero.

Applying (1) inductively gives
\[
\boxed{
A^{(j)}=B^{(j)}+E^{(j)},\qquad \operatorname{rank}E^{(j)}\le k
\quad(0\le j\le m).
}
\tag{7}
\]
Thus arbitrary added eigenvalues of either sign and arbitrary magnitude remain a `k`-dimensional perturbation budget after an arbitrarily long physical Schur chain; no operator-norm factor is generated.

When the coefficient matrix in a factorization of `E^(0)` is invertible, (4) iterates to
\[
\boxed{
\det C_m=\det C_0\prod_{j=0}^{m-1}\frac{\alpha_j}{a_j}.
}
\tag{8}
\]
This identity isolates the only possible blow-up: physical-pivot cancellation. There is no hidden dependence on the off-diagonal shear rows.

## 3. Rank-budgeted cross-certificate stability

Let `I,J` be disjoint physical coordinate sets in the terminal residual. Put
\[
T_0=B^{(m)}[I,J],\qquad T=A^{(m)}[I,J].
\]
By (7),
\[
\operatorname{rank}(T-T_0)\le k.
\]
For rectangular singular values, the rank-`k` perturbation inequality gives
\[
\boxed{s_r(T)\ge s_{r+k}(T_0)}
\tag{9}
\]
for every admissible `r`. Therefore if
\[
s_{k+5}(T_0)\ge\sigma>0,
\tag{10}
\]
then the actual terminal cross block `T` has at least five singular values at least `sigma`, completely independently of the sizes and signs of the `k` added eigenvalues.

The regularized determinant theorem now gives the terminal bound
\[
\boxed{M_m:=\|p_{Q_m}\|_\infty\le\frac{5e}{2\sigma}.}
\tag{11}
\]
No assumption is made on the terminal self blocks, on outside couplings, or on any further small spectral directions.

## 4. Lifting the terminal certificate through the actual chain

Let `a_j` denote the actual scalar pivot at the `j`th physical elimination and suppose
\[
|a_j|\ge\delta\sigma\qquad(0\le j<m)
\tag{12}
\]
for one `delta>0`. By the completed `fleet02/B12` dependence-safe square recurrence,
\[
M_j\le2\sqrt{M_{j+1}/|a_j|}.
\]
Writing `B_j=\sigma M_j`, (12) gives
\[
B_j\le2\sqrt{B_{j+1}/\delta}.
\]
Since
\[
2\sqrt{B/\delta}\le\max\{B,4/\delta\},
\]
iteration of the recurrence and (11) yield the dimension-free stability estimate
\[
\boxed{
\|p_{X^TA^{(0)}X}\|_\infty
\le
\frac1\sigma\max\left\{\frac{5e}{2},\frac4\delta\right\}.
}
\tag{13}
\]
The constant is independent of the number `m` of Schur steps, of the perturbation rank `k`, and of the magnitudes and signs of all nonzero eigenvalues of `E^(0)`; `k` is paid only by requiring `k` additional robust cross singular directions in the base terminal certificate.

A leverage-enhanced variant replaces `5` by `3`: if `s_{k+3}(T_0)>=sigma` and the *actual* terminal cross-range leverage meets the completed `q=1` regularized-determinant hypothesis, then
\[
M_m\le\frac{3e}{\sqrt2\,\sigma},
\]
so (13) becomes
\[
\boxed{
\|p_Q\|_\infty
\le
\frac1\sigma\max\left\{\frac{3e}{\sqrt2},\frac4\delta\right\}.
}
\tag{14}
\]
The leverage condition is explicitly on the final actual cross block and is not asserted to survive arbitrary perturbation.

## 5. What this does and does not solve

This theorem gives a product-preserving stability mechanism for adding arbitrary low-rank spectral material of either sign, including arbitrarily small and arbitrarily large eigenvalues. It is stronger than a small-operator-norm perturbation argument: the perturbation norm never appears. The price is purely geometric: one needs a base terminal cross packet with `k+5` robust directions and a chain of noncollapsing actual physical pivots.

The partner Möbius family shows that a lower bound on a fixed chosen pivot cannot be inferred from the perturbation magnitude alone: a new eigenvalue can tend to zero or infinity while the pivot tends to zero. Certificate switching such as (6), or aggregate-before-inversion geometry, is therefore genuinely necessary.

The full three-large-eigenvalue conjecture remains open because its bare hypothesis does not imply the existence of a base packet with `k+5` cross directions, nor a noncollapsing pivot chain. This report therefore removes a substantial *additional-eigenvalue stability* debt once such a packet is present; it does not provide the still-missing exhaustive product-preserving structural reduction from only `s_3(A)>=1`.

Regularity: (11) yields a continuous terminal density, but the square-lifting argument above is used only for an `L^infty` estimate. Continuity of the fully lifted law is not asserted here.

## 6. Deterministic corroboration

A local finite checker tested 1,800 random symmetric base/low-rank-update instances for (1)--(4), rank preservation, and the cross singular-value inequality (9). Maximum operator-norm residual in (1) was `1.66e-14`; maximum determinant-identity residual was `3.19e-12`; there were zero rank or singular-value violations. These finite checks corroborate algebra only and are not a proof certificate.
