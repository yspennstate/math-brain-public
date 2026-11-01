# F0011 — maximal-rank symmetric-Hadamard cores are self-spectral principal Walsh sets

Date: 2026-09-19 UTC  
Slot: `R7-06`  
Canonical target: `F0011` / Van H. Vu, *Recent progress in combinatorial random matrix theory*, Conjecture 9.4  
Methods executed in this ordinary post-STUCK2 recovery run: **B1 / B27 / B20**  
Status: **PARTIAL / restricted structural theorem; source conjecture remains OPEN under bounded current checks**.

## 1. Starting point inherited from STUCK2

Work on the cleanest remaining two-eigenvalue subfamily isolated by the preceding R7-06 recovery. Let

\[
n=4t^2,\qquad t\ \text{even},\qquad v=n-1=2m+1,\qquad m=2t^2-1.
\]

Thus `m` is odd. After diagonal switching and an overall sign, a symmetric Hadamard matrix of order `n` may be written

\[
\widetilde H=
\begin{pmatrix}
1&\mathbf 1^T\\
\mathbf 1&B
\end{pmatrix},
\qquad B=J-2N,
\]

where `N` is a symmetric binary `v x v` matrix. The exact Hadamard equations are

\[
\boxed{
N\mathbf1=(m+1)\mathbf1,
\qquad
N^2=\frac{m+1}{2}(I+J)=t^2(I+J).
}
\tag{1}
\]

The final-recovery core considered here is the maximal binary-rank stratum

\[
\boxed{\operatorname{rank}_{\mathbb F_2}N=m.}
\tag{2}
\]

Because `t` is even, (1) gives, over `F_2`,

\[
N^2=0,
\qquad N\mathbf1=0.
\tag{3}
\]

STUCK2 encoded such a first shadow as `N=X S X^T`, with `S` invertible symmetric, and obtained the exact middle-shell condition `S D(P) subset L_P`. The first result below shows that on this odd-dimensional maximal-rank stratum the matrix `S` is gauge: it can always be absorbed into the choice of basis of `im N`. This changes the category from a coupled `(P,S)` count to a self-spectral-set count in a Walsh group.

## 2. Factorization lemma

### Lemma 2.1 — unique symmetric form on a chosen image basis

Let `N in Sym_v(F_2)` satisfy `N^2=0` and `rank N=m`. Let

\[
U=\operatorname{im}N
\]

and let `X in F_2^{v x m}` have full column rank with column space `U`. Then there is a unique invertible symmetric matrix `S in Sym_m(F_2)` such that

\[
\boxed{N=XSX^T.}
\tag{4}
\]

#### Proof

Since `N` is symmetric,

\[
\ker N=(\operatorname{im}N)^\perp=U^\perp.
\]

Since the columns of `X` span `U`,

\[
\ker X^T=U^\perp=\ker N.
\tag{5}
\]

Also `im N subseteq im X`, so there is an `m x v` matrix `A` with `N=XA`. Because `X` is injective as a map `F_2^m -> F_2^v`,

\[
\ker A=\ker N=\ker X^T.
\]

Both `A` and `X^T` have rank `m`, hence they have the same row space. Therefore

\[
A=SX^T
\]

for a unique `S in GL_m(F_2)`. This gives (4). Taking transposes gives

\[
XSX^T=XS^TX^T.
\]

Choose a left inverse `L` of `X`; then multiplication by `L` on the left and `L^T` on the right yields `S=S^T`. Uniqueness follows from the same multiplication. ∎

## 3. Odd-dimensional symmetric forms: the `S` coordinate is gauge

### Lemma 3.1 — every nonsingular symmetric odd-dimensional binary form is Euclidean

If `m` is odd and `S in Sym_m(F_2)` is invertible, then there exists `T in GL_m(F_2)` with

\[
\boxed{S=TT^T.}
\tag{6}
\]

#### Proof

Let `B(x,y)=x^T S y`. In characteristic two,

\[
\ell(x):=B(x,x)
\]

is linear. Because an alternating bilinear form has even rank, a nonsingular form in odd dimension cannot be alternating, so `ell` is nonzero. Nondegeneracy gives a unique vector `omega` such that

\[
\ell(x)=B(x,\omega)\qquad\text{for every }x.
\tag{7}
\]

We first prove `B(omega,omega)=1`. If it were zero, then `omega in omega^perp`; moreover (7) shows that the restriction of `B` to `omega^perp` is alternating. The radical of this restricted form is

\[
\omega^\perp\cap(\omega^\perp)^\perp
=\omega^\perp\cap\langle\omega\rangle
=\langle\omega\rangle.
\]

Hence its rank would be

\[
(m-1)-1=m-2,
\]

which is odd, impossible for an alternating form. Thus `B(omega,omega)=1`.

It follows that `omega notin omega^perp`, and the restriction to the even-dimensional space `omega^perp` is a nondegenerate alternating form. Therefore

\[
B\cong\langle1\rangle\perp H^{(m-1)/2},
\]

where `H=[[0,1],[1,0]]` is the hyperbolic plane. Finally

\[
\langle1\rangle\perp H\cong I_3:
\]

if `e,f` is a hyperbolic basis orthogonal to a norm-one vector `omega`, then

\[
\omega+e,\quad \omega+f,\quad \omega+e+f
\]

are three independent, pairwise orthogonal norm-one vectors. Iterating gives `B cong I_m`. Thus for some `P in GL_m(F_2)`,

\[
P^T S P=I,
\]

and hence `S=P^{-T}P^{-1}`. Taking `T=P^{-T}` gives (6). ∎

### Corollary 3.2 — Euclidean factorization

Under Lemma 2.1, after replacing `X` by `XT`, one may assume

\[
\boxed{N=XX^T.}
\tag{8}
\]

This does **not** reduce the number of original matrices; it only chooses an adapted coordinate system on `im N`.

## 4. B1 / CHANGE THE CATEGORY: exact equivalence with a self-spectral Walsh set

Write the rows of the Euclidean factor `X` as

\[
p_1,\ldots,p_v\in\mathbb F_2^m.
\]

Because `N` is a binary matrix and every exact row of `N` has weight `m+1`, no `p_i` is zero. If `p_i=p_j` for `i ne j`, then rows `i,j` of `N=XX^T` are equal. Their support intersection would then have size `m+1`, whereas (1) says every off-diagonal intersection is exactly `(m+1)/2`; contradiction. Thus the `p_i` are nonzero and pairwise distinct. They span `F_2^m` because `X` has full column rank.

Define

\[
\boxed{Q:=\{0,p_1,\ldots,p_v\}\subset\mathbb F_2^m.}
\tag{9}
\]

Then

\[
|Q|=v+1=2m+2=n.
\]

For `x,y in Q`, let

\[
W_Q(x,y)=(-1)^{x\cdot y}.
\tag{10}
\]

### Theorem 4.1 — self-spectral principal-Walsh normal form

On the even-`t`, maximal-rank branch (1)–(2), the normalized symmetric Hadamard matrix is exactly

\[
\boxed{\widetilde H=W_Q=\bigl((-1)^{x\cdot y}\bigr)_{x,y\in Q}.}
\tag{11}
\]

Conversely, let `m=2t^2-1` with `t` even. If `Q subset F_2^m` has

\[
0\in Q,\qquad |Q|=2m+2,
\]

spans `F_2^m`, and its principal Walsh matrix `W_Q` is Hadamard, then after ordering `Q={0,p_1,...,p_v}` the binary matrix

\[
N_{ij}=p_i\cdot p_j
\tag{12}
\]

has rank `m` over `F_2` and satisfies the full exact integer system (1). Thus it reconstructs a normalized symmetric-Hadamard core in this branch.

#### Proof

For the forward direction, (8) gives

\[
N_{ij}=p_i\cdot p_j\pmod2.
\]

Since `N_{ij}` itself is `0` or `1`,

\[
B_{ij}=1-2N_{ij}=(-1)^{p_i\cdot p_j}.
\]

The first row and column of `widetilde H` are all `+1`, which are exactly the characters involving the zero vector. This proves (11).

For the converse, form `X` with rows `p_i`. Spanning makes `X` full column rank. Put `N=XX^T` over `F_2` and identify each entry with its binary representative. Since `X` is injective,

\[
XX^T z=0\iff X^Tz=0,
\]

so `rank N=rank X^T=m`.

Now use the Hadamard orthogonality of `W_Q`. Orthogonality of the row indexed by `0` with the row indexed by `p_i` gives

\[
1+\sum_{j=1}^v(-1)^{N_{ij}}=0.
\]

Since `v=2m+1`, this says row `i` of `N` has exactly `m+1` ones. For `i ne j`, orthogonality of rows `p_i,p_j` gives Hamming distance `m+1` between the corresponding binary rows of `N`. Two weight-`m+1` binary rows at distance `m+1` intersect in exactly `(m+1)/2` positions. Therefore

\[
(N^2)_{ii}=m+1,
\qquad
(N^2)_{ij}=\frac{m+1}{2}\quad(i\ne j),
\]

which is exactly (1). ∎

In the language of finite harmonic analysis, `Q` is a **self-spectral set**: it is a spectral set whose spectrum can be chosen to be the same set `Q` under the standard pairing on `F_2^m`. Equivalently, `W_Q` is a principal real-Hadamard submatrix of the full Walsh matrix of order `2^m`.

The broad Hadamard/spectral-set correspondence is classical; this report makes no novelty claim for that correspondence. The point for F0011 is that the previously coupled `(P,S)` blocker is now losslessly gauge-normalized to one subset `Q` with a self-principal Fourier constraint.

## 5. The gauge fiber is exactly an orthogonal-group torsor

The Euclidean factor `X` is not unique, and this nonuniqueness must not be mistaken for distinct matrices.

### Proposition 5.1

If `X,Y in F_2^{v x m}` have full column rank and

\[
XX^T=YY^T=N,
\]

then there is a unique `T in GL_m(F_2)` with `Y=XT`, and it satisfies

\[
\boxed{TT^T=I.}
\tag{13}
\]

Conversely every such `T` preserves `N`.

#### Proof

Since `rank N=m` and `im N subseteq im X`, dimensions give `im X=im N`; likewise `im Y=im N`. Hence `Y=XT` for a unique `T in GL_m(F_2)`. Substitution yields

\[
X(TT^T-I)X^T=0.
\]

Multiplying by a left inverse of `X` and its transpose gives (13). The converse is immediate. ∎

Thus adapted self-spectral coordinates form a free torsor for

\[
O(m,2)=\{T:TT^T=I\}.
\]

For `m=2k+1`, the distinguished norm functional identifies `O(m,2)` with `Sp(2k,2)`, and the standard finite-group order is

\[
|O(m,2)|
=2^{k^2}\prod_{i=1}^k(2^{2i}-1)
=2^{(m^2-m)/2+O(1)}.
\tag{14}
\]

Therefore any future count performed in `X` or `Q` coordinates must divide out this quadratic-size gauge orbit before comparing with the original fixed-spectrum matrix count.

## 6. Fourier zero-set formulation and a maximum-clique theorem

Let

\[
f=1_Q,
\qquad
\widehat f(a)=\sum_{q\in Q}(-1)^{a\cdot q},
\qquad
Z_Q=\{a\in F_2^m:\widehat f(a)=0\}.
\tag{15}
\]

### Proposition 6.1 — exact Fourier criterion

`W_Q` is Hadamard if and only if

\[
\boxed{(Q+Q)\setminus\{0\}\subseteq Z_Q.}
\tag{16}
\]

#### Proof

Rows indexed by `x,y in Q` have inner product

\[
\sum_{q\in Q}(-1)^{x\cdot q}(-1)^{y\cdot q}
=\widehat f(x+y).
\]

For `x ne y`, `x+y ne0`; pairwise row orthogonality is therefore exactly (16). ∎

Define the translation graph

\[
\Gamma_Q=\operatorname{Cay}(F_2^m,Z_Q),
\qquad
a\sim b\iff a+b\in Z_Q.
\tag{17}
\]

### Proposition 6.2 — the self-spectral set is a maximum clique

If `Q` is self-spectral, then `Q` is a clique of `Gamma_Q` of size `n=|Q|`, and no clique is larger.

#### Proof

Equation (16) says `Q` is a clique. For any clique `C`, associate to `c in C` the vector

\[
\phi(c)=\bigl((-1)^{c\cdot q}\bigr)_{q\in Q}\in\mathbb R^{|Q|}.
\]

If `c ne d` then

\[
\langle\phi(c),\phi(d)\rangle=\widehat f(c+d)=0.
\]

Thus `C` gives `|C|` nonzero mutually orthogonal vectors in `R^{|Q|}`, so `|C|<=|Q|`. Equality is achieved by `Q`. ∎

This is the promised B1 category change: the exact core is now a **self-generated maximum clique in its own Fourier-zero Cayley graph**. Unlike the previous row-exposure formulation, the constraint is global and symmetric in all points of `Q`.

## 7. Fixed spectrum becomes one Fourier coefficient

Because the standard binary dot product satisfies

\[
q\cdot q=\mathbf1_m\cdot q,
\]

we have

\[
\boxed{
\operatorname{tr}W_Q
=\sum_{q\in Q}(-1)^{q\cdot q}
=\widehat f(\mathbf1_m).
}
\tag{18}
\]

Since `W_Q^2=nI` and `sqrt(n)=2t`, its eigenvalues are `+2t` and `-2t`; their multiplicities are determined by the trace. Therefore, on this branch, fixing the exact two-eigenvalue spectrum is equivalent to prescribing the single Fourier coefficient `hat f(1_m)` in addition to self-spectrality.

This is useful because the source-level fixed-fiber problem can now be asked entirely in finite harmonic-analysis terms.

## 8. B27 / SWAP THE QUANTIFIERS: every exact object has a half-Hadamard basis seed

The false local statement found earlier was: every row-exposure order has few completions. The swapped statement sought at STUCK2 is: every completed object has **some** useful seed.

Because `Q` spans `F_2^m`, choose any vector-space basis

\[
\mathcal B=\{b_1,\ldots,b_m\}\subseteq Q\setminus\{0\}.
\]

For `a in F_2^m`, write

\[
\chi_a(q)=(-1)^{a\cdot q},\qquad q\in Q.
\]

### Proposition 8.1 — half-Hadamard seed

The `m+1=n/2` vectors

\[
\chi_0,\chi_{b_1},\ldots,\chi_{b_m}\in\{\pm1\}^Q
\]

are pairwise orthogonal. Equivalently, the binary `n x m` evaluation array

\[
A(q,i)=b_i\cdot q
\]

is an orthogonal array `OA(n,m,2,2)`: every column is balanced, and every pair of columns contains each of the four binary patterns exactly `n/4` times.

#### Proof

For each `i`, `b_i=0+b_i` is a nonzero element of `Q+Q`, so (16) gives `hat f(b_i)=0`; hence `chi_0` is orthogonal to `chi_{b_i}`. For `i ne j`, `b_i+b_j in (Q+Q)\{0}`, so `hat f(b_i+b_j)=0`; hence `chi_{b_i}` and `chi_{b_j}` are orthogonal. Balance plus zero pair correlation gives the four equal pair-pattern counts. ∎

Let

\[
T=Q\setminus(\{0\}\cup\mathcal B).
\]

Then `|T|=m+1`. Since **all** character columns indexed by `Q` are mutually orthogonal, the vectors `{chi_t:t in T}` form an orthogonal basis for the real orthogonal complement of the seed span. Thus every exact object admits a half-dimensional orthogonal seed and an equally sized orthogonal-character completion.

The number of choices of a basis **inside one completed Q** is at most

\[
\binom{n-1}{m}m!\le n^m=2^{O(m\log m)},
\]

which is subquadratic on the logarithmic scale. This is the correct quantifier swap: one may choose a favorable basis after seeing the completed object without paying a quadratic number of *index-choice* bits.

## 9. B20 / FIND WHY THE ALGORITHM FAILS: basis normalization conserves a quadratic Gram parameter

The seed theorem alone still does not give a subquadratic encoding. The obstruction can be stated exactly.

Put the chosen ordered basis vectors into an invertible matrix `R in GL_m(F_2)` and pass to coordinates

\[
x=Rz.
\]

The standard dot product becomes

\[
x\cdot y=z^T G w,
\qquad
\boxed{G=R^TR.}
\tag{19}
\]

In these coordinates the chosen basis is the standard basis, but the principal character matrix is now

\[
(-1)^{z^T G w}
\]

rather than the standard Walsh pairing. Thus the information removed from the basis has moved into the nonsingular symmetric Gram form `G`.

By Lemma 3.1 every nonsingular symmetric `m x m` binary matrix occurs as `R^TR` when `m` is odd. Moreover,

\[
R_1^TR_1=R_2^TR_2
\]

if and only if `R_2R_1^{-1}` lies in the orthogonal group (up to the equivalent left/right convention). Therefore the set of possible Gram forms has cardinality

\[
\frac{|GL(m,2)|}{|O(m,2)|}.
\]

Using

\[
|GL(m,2)|=2^{m^2+O(1)}
\]

and (14),

\[
\boxed{
\#\{G\text{ nonsingular symmetric}\}
=2^{(m^2+m)/2+O(1)}.
}
\tag{20}
\]

Hence an arbitrary `GL_m` basis normalization still leaves about `m^2/2` binary bits in the pairing. This is the precise failure of the naive good-seed algorithm: **the seed can be normalized only by changing the bilinear form, and the family of possible forms itself has quadratic entropy.**

This does not prove that all Gram forms occur among exact F0011 cores. It proves the narrower and rigorous statement needed for route selection: basis normalization by itself is not a compression theorem; any successful use of Proposition 8.1 must exploit additional restrictions coupling the transformed set and its Gram form.

## 10. What changed mathematically

The previous STUCK2 blocker was the coupled condition

\[
S D(P)\subseteq L_P
\]

with both the image/code coordinate `P` and the symmetric-form coordinate `S` apparently carrying quadratic entropy. On the odd-dimensional maximal-rank branch, Theorem 4.1 shows that `S` is not an independent invariant. It can be gauged to the identity, leaving the exact object

\[
\boxed{
Q\subset F_2^m,\quad |Q|=2m+2,\quad 0\in Q,\quad \langle Q\rangle=F_2^m,
\quad ( (-1)^{x\cdot y})_{x,y\in Q}\text{ Hadamard}.
}
\tag{21}
\]

The original matrix is recovered from `Q` up to the orthogonal gauge and subquadratic label choices. Equivalently, `Q` is a size-`2m+2` self-spectral set and a maximum clique in the Fourier-zero Cayley graph generated by itself.

This is a cleaner exact counting target than the `(P,S)` description, but it is still a **restricted core theorem**, not Vu's asymptotic conjecture.

## 11. Literature boundary checked 2026-09-19

The following bounded current checks were used to avoid claiming a classical bridge as new:

1. Van H. Vu, arXiv:2005.02797 / *Probability Surveys* 18 (2021), Conjecture 9.4, remains the exact F0011 source target used by this slot.
2. Mihail N. Kolountzakis and Mate Matolcsi, *Complex Hadamard matrices and the Spectral Set Conjecture* (arXiv:math/0411512), explicitly develops the finite-abelian connection between spectral sets and complex Hadamard matrices. Therefore the broad spectral-set interpretation is prior art.
3. John E. Herr and Troy M. Wiegand, *Identifying Complex Hadamard Submatrices of the Fourier Matrices via Primitive Sets* (arXiv:1909.13145; LAA 2021), gives compatibility tests for Hadamard submatrices of Fourier matrices. This is adjacent to, but does not in the bounded search supply, an asymptotic count for the self-principal Walsh subsets (21).
4. Asaf Ferber, Vishesh Jain and Yufei Zhao, *On the number of Hadamard matrices via anti-concentration*, CPC 31 (2022), prove `H(n)<=2^{(1-c_H)n^2/2}` for some absolute `c_H>0`, conjecture `H(n)=2^{O(n log n)}`, and state that even `2^{o(n^2)}` would be very interesting and require new ideas. Hence their theorem does not remove the Hadamard-count obstruction inherited by F0011.
5. Shilei Fan and Mamateli Kadir, arXiv:2609.00087 (2026-08-31), construct tiles without spectra including an example in `F_2^13`; this confirms that the modern finite-`F_2` spectral/tiling landscape is nontrivial, but it neither proves nor refutes the special self-spectral count (21).

A bounded 2026-09-19 search did **not** surface a theorem proving Vu's `2^{-(1/2+o(1))n^2}` asymptotic or a theorem giving a subquadratic count for the self-principal Walsh family (21). These are search misses only; they are not certifications of global openness or novelty.

## 12. Exact gap and next route

The unresolved restricted counting problem is now:

\[
\boxed{
\#\{Q\subset F_2^m:\ Q\text{ satisfies }(21),\ \widehat{1_Q}(\mathbf1_m)=\tau\}
=2^{o(m^2)}
}
\tag{22}
\]

for each admissible fixed trace `tau`, modulo the orthogonal gauge and subquadratic relabeling factors. Proving (22) for this branch would be genuine partial movement in the fixed-spectrum entropy obstruction, but still would not close F0011 outside this branch.

The B27 basis seed exposes a half-Hadamard decomposition, but B20 shows why simply normalizing that basis fails: a quadratic Gram parameter survives. The next run should therefore attack the **self-principal** condition rather than ordinary Hadamard completion.

Proposed next nonrepeating methods:

- **B4 (prove something weaker, completely):** prove a `2^{o(m^2)}` count or structural classification for self-spectral `Q` under an additional concrete additive hypothesis such as small doubling / large additive energy, with the hypothesis stated and proved sufficient for the count.
- **B9 (randomize):** quantify the probability that a random spanning size-`2m+2` set has the quadratic family of Fourier zeros required by (16), and isolate exactly which dependence prevents a direct first-moment count.
- **B23 (do what the proposer did not expect):** try to construct a genuinely quadratic-entropy family of self-spectral `Q`; such a family would expose a serious obstruction to the desired fixed-fiber theorem and could potentially redirect the source attack toward refutation or a different dominant family.

No finite checker was created in this run because the new claims are theorem-sized algebraic reductions and are proved above on the page. No numerical fit, timeout, or negative search is being used as source resolution.
