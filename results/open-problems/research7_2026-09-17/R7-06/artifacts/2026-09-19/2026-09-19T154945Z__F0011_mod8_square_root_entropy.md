# F0011 — a 2-adic square-root reduction and a quadratic entropy bound for the symmetric-Hadamard core

Date: 2026-09-19 UTC  
Slot: `R7-06`  
Target: Van H. Vu, *Recent progress in combinatorial random matrix theory*, Conjecture 9.4.  
Methods: **B30 / B11 / B15**.  
Status: **PARTIAL**. This note proves a restricted structural/counting theorem for the two-eigenvalue symmetric-Hadamard core. It does **not** prove Vu's conjecture and it does not claim novelty.

## 1. Why this is the post-STUCK1 recovery test

The STUCK1 report isolated the exact source-level bottleneck as fixed-spectrum entropy and selected one recovery action: port the mod-4/rank-duality/rational-canonical architecture from Caden Young's 2026 normal-sign-matrix theorem to the spectral problem, with a fail-fast test on the simplest two-eigenvalue branch

\[
H=H^T\in\{\pm1\}^{n\times n},\qquad H^2=nI.
\]

For square `n`, this branch has integral eigenvalues `\pm\sqrt n` and therefore lies inside F0011. The calculation below is useful even when `n` is not a square, because it isolates exactly what the first 2-adic lift can and cannot see.

Throughout, `J=11^T` and

\[
A:=\frac{J-H}{2}\in\operatorname{Sym}_n(\{0,1\}).
\]

Thus `H=J-2A`.

## 2. B30: the first nontrivial 2-adic lift

Let

\[
r:=A1\in\mathbb Z^n
\]

be the vector of integer row sums of `A`. Since `A` is symmetric,

\[
JA=1r^T,\qquad AJ=r1^T,\qquad J^2=nJ.
\]

Expanding `H^2=nI` gives the exact identity

\[
nJ-2(1r^T+r1^T)+4A^2=nI,
\]

or equivalently

\[
\boxed{
2A^2=1r^T+r1^T+\frac n2(I-J).
}
\tag{2.1}
\]

A nontrivial Hadamard order is divisible by four, so write

\[
n=4q.
\]

Reducing (2.1) modulo two shows

\[
1(r\bmod2)^T+(r\bmod2)1^T=0.
\]

Hence every row sum has the same parity. Write that common parity as `p\in\mathbb F_2`. There is therefore a uniquely determined vector `u\in\mathbb F_2^n` such that

\[
r\equiv p1+2u\pmod4.
\]

Now reduce (2.1), after the exact division by two already displayed there, modulo two. One obtains

\[
A^2
=
1u^T+u1^T+(p+q)J+qI
\qquad\text{in }\mathbb F_2^{n\times n}.
\tag{2.2}
\]

Define

\[
\varepsilon:=q\bmod2,
\qquad
C:=A+\varepsilon I\in\operatorname{Sym}_n(\mathbb F_2).
\]

Because the cross term in `(A+\varepsilon I)^2` vanishes in characteristic two,

\[
\boxed{
C^2=R_{p,u}:=1u^T+u1^T+(p+q)J.
}
\tag{2.3}
\]

The right-hand side has rank at most two. Thus the first genuinely nontrivial spectral 2-adic lift does not become a large linear system as in Young's normality problem; instead it becomes a **symmetric square-root problem of a rank-at-most-two matrix over `\mathbb F_2`**.

The coarse type `(p,u)` has at most `2^{n+1}` possibilities, hence only `2^{O(n)}` entropy.

A useful exact strengthening is already present over the integers. Rearranging the original identity gives

\[
\boxed{
A^2=\frac n4 I+
\left(\frac12(1r^T+r1^T)-\frac n4J\right).
}
\tag{2.4}
\]

For a fixed full row-sum vector `r`, the matrix `A^2` is therefore fixed and differs from the scalar matrix `(n/4)I` by rank at most two. The number of possible full row-sum vectors is at most `(n+1)^n=2^{O(n\log n)}`. Thus even an **exact**, not merely modular, coarse type exists with subquadratic entropy.

## 3. B11: dualize the square-root equation through its image space

The key counting lemma is purely finite-field linear algebra.

### Lemma 3.1 — symmetric square roots of bounded-rank matrices

Fix `s\ge0`. Uniformly over all `R\in\mathbb F_2^{n\times n}` with `rank(R)\le s`, the number of symmetric matrices

\[
C\in\operatorname{Sym}_n(\mathbb F_2),\qquad C^2=R,
\]

is at most

\[
\boxed{2^{n^2/4+O_s(n)}}.
\tag{3.1}
\]

#### Proof

Let `C` be such a solution and put

\[
U:=\operatorname{im}C,\qquad r:=\dim U.
\]

Choose an `n\times r` full-column-rank matrix `X` whose columns form a basis of `U`. Choose an `n\times r` matrix `V` of preimages satisfying

\[
CV=X.
\]

Then

\[
X^TX
=V^TC^TCV
=V^TC^2V
=V^TRV.
\]

Therefore

\[
\boxed{\operatorname{rank}(X^TX)\le s.}
\tag{3.2}
\]

So the standard dot product restricted to `U` has rank at most `s`. This is the dual geometric object replacing Young's rank-dual linear system: the image of a square root must be an **almost totally isotropic subspace**.

We first count possible `r`-dimensional subspaces `U` satisfying (3.2). For an ordered basis matrix `X`, the Gram matrix

\[
K:=X^TX
\]

is symmetric of rank at most `s`. The number of possible `r\times r` matrices of rank at most `s` is at most `2^{O_s(r)}`; this crude bound is enough.

Fix one such `K`. Choose the columns `x_1,\dots,x_r` of `X` sequentially. Once `x_1,\dots,x_{i-1}` are linearly independent, the conditions

\[
x_j^Tx_i=K_{ji},\qquad 1\le j<i,
\]

are `i-1` independent linear conditions on `x_i`, because the standard dot product on `\mathbb F_2^n` is nondegenerate and the vectors `x_1,\dots,x_{i-1}` are independent. Ignoring the additional diagonal condition `x_i^Tx_i=K_{ii}` can only enlarge the count. Hence

\[
\#\{X:X^TX=K,\ \operatorname{rank}X=r\}
\le
\prod_{i=1}^r2^{n-(i-1)}
=2^{nr-r(r-1)/2}.
\]

Every `r`-dimensional subspace has exactly `|GL_r(\mathbb F_2)|=2^{r^2+O(1)}` ordered bases. Therefore the number of possible image subspaces is at most

\[
2^{nr-r(r-1)/2-r^2+O_s(r)}.
\tag{3.3}
\]

Now fix one such `U` and basis matrix `X`. Any symmetric matrix `C` with image contained in `U` annihilates `U^\perp`: if `v\in U^\perp`, then for every `w`,

\[
w^TCv=(Cw)^Tv=0,
\]

so `Cv=0`. Consequently `C` factors through `X^T`, and there is an `r\times r` matrix `S` with

\[
C=XSX^T.
\]

Symmetry of `C` and full column rank of `X` imply `S=S^T`. Hence for a fixed `U` there are at most

\[
2^{r(r+1)/2}
\]

possible symmetric `C`.

Multiplying this with (3.3) gives

\[
\#\{C:\dim\operatorname{im}C=r,\ C^2=R\}
\le
2^{r(n-r)+O_s(n)}.
\]

Since `r(n-r)\le n^2/4`, summing over `0\le r\le n` changes only the `O_s(n)` term. This proves (3.1). `\square`

### Corollary 3.2 — a quadratic-exponent bound for symmetric Hadamards

Let `SH(n)` denote the number of labeled symmetric real Hadamard matrices of order `n`. Then

\[
\boxed{
SH(n)\le 2^{n^2/4+O(n)}.
}
\tag{3.4}
\]

Indeed, every such `H` produces a type `(p,u)` and a symmetric binary matrix `C` satisfying (2.3), where `rank(R_{p,u})\le2`. There are only `2^{n+1}` types. Lemma 3.1 with `s=2`, followed by the injective recovery

\[
C\mapsto A=C+\varepsilon I\mapsto H=J-2A,
\]

gives (3.4).

The same upper bound holds, a fortiori, for the subset with any one fixed trace/eigenvalue-multiplicity pattern. In the F0011 square-order two-eigenvalue branch this yields a genuine fixed-integral-spectrum quadratic entropy saving, but **not** the required subquadratic entropy.

## 4. B15: break symmetry by conditioning on spectral row-sum type

The full row-sum vector

\[
r=A1
\]

is a legal coarse type with only `2^{O(n\log n)}` possibilities. Conditional on `r`, equation (2.4) fixes the entire square `A^2`:

\[
A^2=B(r):=
\frac n4 I+
\frac12(1r^T+r1^T)-\frac n4J.
\tag{4.1}
\]

Thus the symmetric-Hadamard counting problem can be written exactly as

\[
\sum_r
\#\{A\in\operatorname{Sym}_n(\{0,1\}):A1=r,\ A^2=B(r)\}.
\tag{4.2}
\]

This is the spectral analogue of conditioning on a coarse type before reducing modulo two: the universal congruence `H\equiv J\pmod2` no longer erases everything. The first 2-adic shadow of a fixed `r` is precisely the bounded-rank square-root equation (2.3).

However, the first lift still has **quadratic** ambient entropy. For example, when `n=2m`, the fixed subspace

\[
U_0:=\{(x,x):x\in\mathbb F_2^m\}
\]

is totally isotropic for the standard dot product. With

\[
X=\begin{pmatrix}I_m\\I_m\end{pmatrix},
\qquad X^TX=0,
\]

every symmetric `m\times m` binary matrix `S` gives

\[
C=XSX^T,
\qquad C^2=XS(X^TX)SX^T=0.
\]

The map `S\mapsto C` is injective, so even the bare type `C^2=0` has at least

\[
2^{m(m+1)/2}=2^{n^2/8+O(n)}
\]

symmetric solutions. Therefore **no argument using only the first mod-4/mod-8 equation `C^2=R_{p,u}` can prove a `2^{o(n^2)}` bound**. Additional arithmetic information from the exact lift (4.1), a higher 2-adic layer, or a genuinely global design/spectral constraint is necessary.

This is the fail-fast conclusion requested by STUCK1: the Young-style first linearization has been replaced by a valid bounded-rank square-root constraint and yields a nontrivial `1/4`-exponent upper bound for the symmetric-Hadamard core, but the first lift alone provably leaves `2^{\Omega(n^2)}` ambient solutions.

## 5. Relation to the full F0011 source problem

Earlier R7-06 work reduced Vu's conjecture to the uniform fixed-spectrum entropy statement

\[
\max_\lambda K_n(\lambda)=2^{o(n^2)},
\]

where `K_n(\lambda)` counts diagonally colored two-graph isomorphism classes in one integral spectral fiber. The present theorem does **not** establish that bound. It proves only that, on the simplest symmetric-Hadamard fixed-spectrum core, a subquadratic-size 2-adic type exists and the first modular square-root constraint cuts the naive symmetric-sign entropy from about `n^2/2` bits to at most `n^2/4+O(n)` bits.

The remaining gap is still quadratic. The exact object left after conditioning is a binary symmetric square root of the scalar-plus-rank-two matrix `B(r)` in (4.1). Any continuation of the 2-adic recovery route must use information beyond the first square-root shadow.

## 6. Literature/scope notes, checked 2026-09-19

- Caden Young, *Sharp Exponential Asymptotics for Normal Sign Matrices*, arXiv:2607.15294 (2026-07-01), proves the sharp normal-sign exponent using mod-4 linearization, rank duality, and finite-field rational-canonical/centralizer counting. The present calculation tests whether that architecture has a spectral analogue; it does not claim Young's mechanism as new.
- Ferber–Jain–Zhao, *On the number of Hadamard matrices via anti-concentration*, Combinatorics, Probability and Computing 31 (2022), gives a nontrivial constant quadratic-exponent improvement for general Hadamard matrices and conjectures `H(n)=2^{O(n\log n)}`. The bound here is only for **symmetric** Hadamards and is not claimed to improve the best known literature.
- The 2-rank of graphical/symmetric Hadamard-derived objects is classical and has an established design/strongly-regular-graph literature. The present note therefore makes no novelty claim from the finite-field rank formulation.
- A bounded current search did not locate a paper proving Vu's Conjecture 9.4 or a source-equivalent `2^{o(n^2)}` fixed-spectrum entropy theorem. This is negative evidence only, not an openness or novelty certificate.

## 7. Exact outcome of the three methods

**B30:** successful restricted theorem. The first nontrivial 2-adic lift is the rank-at-most-two square-root equation (2.3), with only `2^{O(n)}` coarse types.

**B11:** successful restricted counting theorem. Dualizing through `U=im(C)` converts `C^2=R` into an almost-isotropic-subspace condition and yields `2^{n^2/4+O(n)}` symmetric solutions for fixed bounded-rank `R`.

**B15:** successful diagnosis, not source closure. Conditioning on the exact row-sum vector fixes `A^2` as a scalar-plus-rank-two matrix, but the first modular shadow alone still admits `2^{\Omega(n^2)}` solutions. The missing ingredient is a second layer of arithmetic/global rigidity.

The frozen F0011 metric `N_exact` is unaffected by these asymptotic structural results and remains `8`.