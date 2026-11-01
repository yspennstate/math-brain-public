# F0011 — normalized Hadamard-design core and the exact entropy barrier of its first binary shadow

Date: 2026-09-19 UTC  
Slot: `R7-06`  
Target: Van H. Vu, *Recent progress in combinatorial random matrix theory*, Conjecture 9.4 (integral spectrum)  
Methods executed: **B6 / B24 / B25**  
Status: **restricted theorem / obstruction only; F0011 remains PARTIAL / OPEN**.

## 1. Purpose

The preceding STUCK1 recovery reduced the two-eigenvalue symmetric-Hadamard branch to a binary symmetric square-root equation and proved the upper bound `2^{n^2/4+O(n)}` for its first 2-adic relaxation. This note asks whether conditioning on the exact row-sum type, or counting the same binary square roots through their image spaces, can remove that residual quadratic entropy.

The answer at the first binary layer is **no, sharply**. After canonical diagonal-switch normalization, the apparently variable row-sum type collapses to the classical Hadamard-design point. Its parity shadow is a square-zero symmetric operator annihilating the all-one vector. That relaxation itself has `2^{(1/4+o(1))v^2}` points. Thus the `1/4` exponent from the previous run is not an artifact of a loose upper bound: it is the true entropy scale of the first modular shadow.

No novelty is claimed for the classical Hadamard-design correspondence or for finite-field enumeration of symmetric nilpotent matrices. In particular, Brouwer--Gow--Sheekey, *Counting Symmetric Nilpotent Matrices*, Electronic Journal of Combinatorics 21(2) (2014), P2.4, gives a much broader exact enumeration framework for symmetric/self-adjoint nilpotents. The contribution here is the source-specific reduction and the resulting fail-fast obstruction for the F0011 recovery route.

## 2. B6 — diagonal switching sends every symmetric-Hadamard orbit to a fixed design type

Let

\[
H=H^T\in\{\pm1\}^{n\times n},\qquad H^2=nI_n.
\]

Fix vertex `1`, put `d=H_{11}`, and define the diagonal sign matrix `D` by

\[
D_{11}=1,\qquad D_{ii}=dH_{1i}\quad(i>1).
\]

Then

\[
\widetilde H:=dDHD
\]

is again symmetric, satisfies `\widetilde H^2=nI`, and has first row and first column identically `+1`. Indeed, for `i>1`,

\[
\widetilde H_{1i}=dH_{1i}(dH_{1i})=1,
\qquad
\widetilde H_{11}=dH_{11}=1.
\]

Write

\[
\widetilde H=
\begin{pmatrix}
1&\mathbf 1^T\\
\mathbf 1&B
\end{pmatrix},
\qquad B=B^T\in\{\pm1\}^{(n-1)\times(n-1)}.
\]

Expanding `\widetilde H^2=nI` gives the two exact core identities

\[
\boxed{B\mathbf1=-\mathbf1,\qquad B^2=nI-J.}
\tag{2.1}
\]

Now define

\[
G:=\frac{J+B}{2}\in\{0,1\}^{v\times v},\qquad v=n-1.
\]

Since `J\mathbf1=v\mathbf1` and `B\mathbf1=-\mathbf1`,

\[
\boxed{G\mathbf1=\frac{n-2}{2}\mathbf1.}
\tag{2.2}
\]

Also, using `J^2=vJ`, `JB=BJ=-J`, and (2.1),

\[
4G^2
=J^2+JB+BJ+B^2
=nI+(n-4)J,
\]
so

\[
\boxed{G^2=\frac n4I+\frac{n-4}{4}J.}
\tag{2.3}
\]

Thus `G` is the symmetric incidence matrix of a Hadamard 2-design with

\[
(v,k,\lambda)=
\left(n-1,\frac{n-2}{2},\frac{n-4}{4}\right).
\]

Conversely, a symmetric binary matrix satisfying (2.2)--(2.3) reconstructs `B=2G-J`, for which

\[
B\mathbf1=-\mathbf1,
\qquad
B^2=nI-J,
\]
and hence reconstructs a normalized symmetric Hadamard matrix `\widetilde H`.

This correspondence is classical. The point for F0011 is that **after diagonal switching the full row-sum vector is no longer a large type space on this branch**: it has collapsed to one constant design parameter. Therefore the proposed B6 deformation does not reveal a hidden family of row-sum extremizers; it lands exactly on the standard Hadamard-design core.

### Square-order specialization forced by integral spectrum

On the two-eigenvalue branch the eigenvalues are `\pm\sqrt n`. Integral spectrum therefore forces `n` to be a square. For nontrivial Hadamard order, write

\[
n=4t^2.
\]

Then

\[
\boxed{
v=4t^2-1,\qquad
G\mathbf1=(2t^2-1)\mathbf1,\qquad
G^2=t^2I+(t^2-1)J.
}
\tag{2.4}
\]

The remaining exact counting problem on this core is consequently the number of symmetric `{0,1}` incidence matrices satisfying (2.4), possibly with a fixed trace/eigenvalue multiplicity if one stays inside one exact spectral fiber.

## 3. B24 — the first binary shadow has a universal square-zero normal form

Reduce (2.4) modulo two. Since `v=4t^2-1` is odd and `2t^2-1` is odd,

\[
G\mathbf1=\mathbf1\qquad(\bmod 2).
\tag{3.1}
\]

There are two parity cases.

* If `t` is odd, then `G^2=I` over `\mathbb F_2`. Set
  \[
  N=G+I.
  \]
  Then `N=N^T`, `N^2=0`, and `N\mathbf1=0`.

* If `t` is even, then `G^2=J` over `\mathbb F_2`. Set
  \[
  N=G+J.
  \]
  Here `GJ=JG=J` by (3.1), and `J^2=vJ=J`; hence again
  \[
  N=N^T,\qquad N^2=0,\qquad N\mathbf1=0.
  \]

For fixed parity of `t`, the map `G\mapsto N` is an affine bijection onto its image. Therefore every normalized square-order symmetric-Hadamard design lies inside the relaxation

\[
\boxed{
\mathcal N_v:=
\{N\in\operatorname{Sym}_v(\mathbb F_2):N^2=0,\ N\mathbf1=0\},
\qquad v\text{ odd}.
}
\tag{3.2}
\]

The B24 extremal question is now exact: how large is `\mathcal N_v`, and which ranks carry its entropy?

## 4. B25 — exact rank decomposition by isotropic image spaces

Write

\[
v=2m+1,
\qquad
V=\mathbb F_2^v,
\qquad
e=\mathbf1,
\qquad
W=e^\perp.
\]

Because `v` is odd,

\[
e\cdot e=1.
\]

Hence `V=\langle e\rangle\perp W`. For every `x\in W`,

\[
x\cdot x=\sum_i x_i=e\cdot x=0,
\]
so the restriction of the standard dot product to `W` is alternating. It is nondegenerate because

\[
W^\perp=\langle e\rangle
\quad\text{and}\quad
e\notin W.
\]

Thus `W` is a `2m`-dimensional symplectic vector space.

Take `N\in\mathcal N_v` and put `U=\operatorname{im}N`. Since `Ne=0` and `N=N^T`,

\[
e\cdot Nx=(Ne)\cdot x=0,
\]
so `U\subseteq W`. Symmetry also gives

\[
\ker N=U^\perp.
\]

The equation `N^2=0` is exactly

\[
U\subseteq\ker N=U^\perp,
\]
so `U` is totally isotropic in the symplectic space `W`. In particular,

\[
\operatorname{rank}N=\dim U\le m.
\tag{4.1}
\]

### Exact fiber over a fixed isotropic image

Let `U\subset W` be an `r`-dimensional totally isotropic subspace and let `X` be a `v\times r` matrix whose columns form a basis of `U`. Then `X^TX=0` and `X^Te=0`.

Every symmetric map with image exactly `U`, square zero, and annihilating `e` has a unique representation

\[
\boxed{N=XSX^T}
\tag{4.2}
\]

with `S` an invertible symmetric `r\times r` matrix over `\mathbb F_2`.

Proof: if `\operatorname{im}N=U` and `N=N^T`, then `N` annihilates `U^\perp=\ker X^T`, so it factors uniquely through the surjection `X^T:V\to\mathbb F_2^r`; because `X` is injective there is a unique matrix `S` with `N=XSX^T`. Transposing (4.2) forces `S=S^T`, and `\operatorname{rank}N=r` forces `S` invertible. Conversely, for symmetric invertible `S`,

\[
N^2=XS(X^TX)SX^T=0,
\qquad
Ne=XSX^Te=0,
\]
and `\operatorname{im}N=U`.

Let `h_r` denote the number of invertible symmetric `r\times r` matrices over `\mathbb F_2`. Let `I(m,r)` denote the number of `r`-dimensional totally isotropic subspaces of a `2m`-dimensional symplectic space over `\mathbb F_2`. The preceding argument gives the exact rank decomposition

\[
\boxed{
|\mathcal N_{2m+1}|=
\sum_{r=0}^{m} I(m,r)h_r.
}
\tag{4.3}
\]

The isotropic-subspace factor has the elementary product formula

\[
\boxed{
I(m,r)=
\prod_{i=0}^{r-1}
\frac{2^{2m-2i}-1}{2^{r-i}-1}.
}
\tag{4.4}
\]

Indeed, after choosing an isotropic independent `i`-tuple, the next vector has `2^{2m-i}-2^i` possibilities in the current orthogonal complement but outside the current span. Multiplying over `i=0,...,r-1` and dividing by the number `|GL_r(2)|=\prod_{i=0}^{r-1}(2^r-2^i)` of ordered bases yields (4.4).

From (4.4), uniformly for `0\le r\le m`,

\[
\log_2 I(m,r)
=2mr-\frac32r^2+\frac12r+O(1).
\tag{4.5}
\]

The error is bounded because the products of factors `(1-2^{-j})` and `(1-2^{-2j})` stay between positive absolute constants and one.

Using only the trivial bound

\[
h_r\le 2^{r(r+1)/2},
\]
(4.3)--(4.5) give

\[
I(m,r)h_r
\le
2^{r(2m+1-r)+O(1)}.
\tag{4.6}
\]

Since `r\le m`, the quadratic exponent is maximized at `r=m` and equals

\[
m(m+1)=\frac{v^2-1}{4}.
\]
Summing the `m+1` rank layers gives

\[
\boxed{
|\mathcal N_v|
\le 2^{(v^2-1)/4+O(\log v)}.
}
\tag{4.7}
\]

### Matching lower exponent

For `r=m`, the isotropic spaces are Lagrangians. Formula (4.4) becomes

\[
I(m,m)=\prod_{j=1}^{m}(2^j+1)
=2^{m(m+1)/2+O(1)}.
\tag{4.8}
\]

There are at least `2^{m(m-1)/2-O(m)}` invertible symmetric `m\times m` matrices: if `m` is even, use all nondegenerate alternating forms (which are symmetric in characteristic two); if `m` is odd, take `1\oplus A` with `A` a nondegenerate alternating form on `m-1` coordinates. The usual `GL/Sp` orbit count gives the displayed exponent. Therefore the rank-`m` term in (4.3) alone gives

\[
|\mathcal N_v|
\ge
2^{m^2-O(m)}
=2^{(v^2-1)/4-O(v)}.
\tag{4.9}
\]

Combining (4.7) and (4.9),

\[
\boxed{
|\mathcal N_v|
=2^{v^2/4+O(v)}.
}
\tag{4.10}
\]

If one inserts the classical exact count of nonsingular symmetric binary matrices, then `h_m` is a positive constant fraction (up to the parity-dependent exact product) of all `2^{m(m+1)/2}` symmetric matrices, and (4.10) sharpens to

\[
|\mathcal N_{2m+1}|=\Theta(2^{m(m+1)})
=\Theta(2^{(v^2-1)/4}).
\tag{4.11}
\]

I do not use (4.11) for any novelty claim. Brouwer--Gow--Sheekey (2014) determine much broader counts for symmetric/self-adjoint nilpotent matrices and explicitly discuss rank/exponent refinements.

## 5. What B24 identifies as the extremal modular object

The exponent in (4.6) is `r(v-r)`, increasing throughout `0\le r\le m`. Hence the first binary relaxation is entropy-dominated by **maximal-rank square-zero maps**:

\[
\operatorname{rank}N=m,
\qquad
\operatorname{im}N=\ker N\cap W
\]
with `\operatorname{im}N` a Lagrangian subspace of `W`.

Equivalently, a typical entropy-maximizing modular certificate consists of

1. a Lagrangian `U\subset W`, and
2. a nonsingular symmetric bilinear form `S` on the `m` coordinates of `U`,

through `N=XSX^T`.

This is the concrete extremal object requested by B24. It also makes B25 literal: the same relaxation is counted once by the matrix entries and again by `(U,S)`.

## 6. Consequence for the F0011 recovery route

The previous run's `2^{n^2/4+O(n)}` upper bound for the first 2-adic symmetric-Hadamard shadow is now seen to be asymptotically saturated by the relaxation itself. Therefore **the first parity square-zero equation cannot, by itself, supply a subquadratic entropy theorem**.

Any continuation must use information discarded by the map `G\mapsto N`, for example a genuine higher 2-adic lift or the exact integer design equations

\[
G\mathbf1=(2t^2-1)\mathbf1,
\qquad
G^2=t^2I+(t^2-1)J,
\tag{6.1}
\]
not merely their parity consequences. In probabilistic language, one must show that the exact Hadamard-design points form an exponentially tiny subset of an ambient square-zero variety which itself has the full `1/4` quadratic entropy exponent.

This does not settle even the symmetric-Hadamard counting subproblem, much less Vu's full fixed-spectrum entropy problem. It is a route-killing obstruction plus a cleaner normal form.

## 7. Prior-art / literature scope checked 2026-09-19

- Van H. Vu, arXiv:2005.02797 / *Probability Surveys* 18 (2021), Conjecture 9.4, remains the source target.
- Caden Young, arXiv:2607.15294 (submitted 2026-07-01), proves sharp normal-sign-matrix asymptotics through mod-4 linearization, rank duality and finite-field centralizer counting; this was the methodological template for STUCK1.
- The normalized-Hadamard to symmetric `2-(4u-1,2u-1,u-1)` design correspondence is classical and reversible; it is not new here.
- A. E. Brouwer, R. Gow, J. Sheekey, *Counting Symmetric Nilpotent Matrices*, EJC 21(2) (2014), P2.4, determines the number of symmetric/self-adjoint nilpotent matrices over finite fields and discusses refinements by rank and nilpotency exponent. This is strong prior art for the finite-field counting side; no novelty is asserted for (4.3)--(4.11) as an isolated enumeration statement.
- A bounded current search on 2026-09-19 did not surface a proof of Vu's Conjecture 9.4. That search miss is negative evidence only, not an openness or novelty certificate.

## 8. Protocol state

Frozen source metric remains

`N_exact = 8`.

This note does not claim finite-census movement. It is the second ordinary post-STUCK1 research run if the accompanying immutable report records `8 -> 8`. HARD recovery count remains `1/2`.