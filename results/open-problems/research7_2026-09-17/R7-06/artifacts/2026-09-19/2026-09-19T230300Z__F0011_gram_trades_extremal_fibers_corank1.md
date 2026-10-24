# F0011 — exact Gram-support reconstruction, minimum frame-trade volume, extremal small fibers, and the corank-one boundary

Date: 2026-09-19 UTC  
Target: F0011 / Van H. Vu, Conjecture 9.4 (integral spectrum of a symmetric Rademacher matrix)  
Status of all results below: **PARTIAL** toward the source conjecture.  
Methods: **B19 / B24 / B30**.  
Novelty: not asserted. In particular, correlation/cut-polytope language, Hadamard switching, entry-trades, and integer Gram-root algorithms have substantial prior literature. The term “frame trade” below is only descriptive and is not asserted to coincide with the established entry-trade notion.

## 1. Setting inherited from the preceding run

On the two-eigenvalue symmetric-Hadamard boundary, split

\[
H=\begin{pmatrix}P&C\\ C^T&D\end{pmatrix}=H^T,
\qquad H^2=s^2I_{2r}.
\]

Then

\[
P^2+CC^T=s^2I,\qquad PC+CD=0,\qquad C^TC+D^2=s^2I.
\tag{1.1}
\]

For a fixed first half set

\[
K_P=s^2I-P^2=CC^T.
\tag{1.2}
\]

The preceding run proved that when the correlation vertices given by the columns of one invertible sign root form a simplicial face, all sign Gram roots are obtained by column signs and permutations. Here we remove the simplicial hypothesis at the price of replacing “one root” by an exact finite support system, and then isolate the precise ambiguity object.

---

## 2. B19 — MAKE IT AN ALGORITHM: exact support reconstruction for every positive-definite sign Gram matrix

Let

\[
\mathcal V_r=\{[x]:x\in\{\pm1\}^r,\ [x]=\{x,-x\}\}
\]

be the `2^{r-1}` sign classes, and put

\[
A_{[x]}=xx^T.
\]

This is well defined on sign classes. For a positive-definite integer matrix `K` which admits an `r x r` sign root, define

\[
\mathcal B(K)=
\left\{
S\subset\mathcal V_r:\ |S|=r,
\quad \sum_{v\in S}A_v=K
\right\}.
\tag{2.1}
\]

### Theorem 2.1 — exact root/support correspondence

If `K>0`, then the set of sign matrices `C in {+-1}^{r x r}` satisfying

\[
CC^T=K
\]

is obtained exactly as follows:

1. choose `S in \mathcal B(K)`;
2. choose one of the two sign representatives of each of its `r` sign classes;
3. order the resulting `r` columns arbitrarily.

Consequently

\[
\boxed{
R(K):=\#\{C\in\{\pm1\}^{r\times r}:CC^T=K\}
=2^r r!\,|\mathcal B(K)|.
}
\tag{2.2}
\]

#### Proof

Let `C=[c_1 ... c_r]` satisfy `CC^T=K>0`. Since `K` is positive definite, `C` is invertible. Hence no two columns of `C` can agree up to sign. Their sign classes therefore form an `r`-element subset

\[
S_C=\{[c_1],\ldots,[c_r]\}\subset\mathcal V_r.
\]

Moreover

\[
K=CC^T=\sum_{j=1}^r c_jc_j^T
=\sum_{v\in S_C}A_v,
\]

so `S_C in \mathcal B(K)`.

Conversely, take `S in \mathcal B(K)`, choose representatives `c_v` and order them as the columns of `C`. Then

\[
CC^T=\sum_{v\in S}A_v=K.
\]

Because `K>0`, this `C` is automatically invertible. There are independently `2^r` representative-sign choices and `r!` orderings. Since distinct classes cannot be identified by these choices, all `2^r r!` matrices are distinct. Summing over disjoint supports gives (2.2). ∎

### Corollary 2.2 — exact reconstruction algorithm

An exact, exhaustive Gram-root procedure is therefore:

- enumerate the canonical representatives `x` with first coordinate `+1`;
- solve the exact binary linear system

\[
\sum_{v\in\mathcal V_r}z_v A_v=K,
\qquad
z_v\in\{0,1\},
\qquad
\sum_v z_v=r;
\tag{2.3}
\]

- expand every support solution by signed column permutation.

There is no numerical eigenvalue tolerance in this reconstruction. If `F(K)` denotes the minimal face of the sign-correlation polytope containing `K/r`, then every support in `\mathcal B(K)` lies inside `F(K)`: a face containing a point contains every term of any strictly positive convex representation of that point. Thus exact facial inequalities can prune (2.3), but failure of simpliciality is no longer a failure of correctness.

This makes the preceding facial certificate an acceleration/rigidity certificate rather than a completeness requirement.

---

## 3. The ambiguity object: balanced frame trades

Take two distinct supports `S,T in \mathcal B(K)`. Cancel their common classes and put

\[
A=S\setminus T,
\qquad
B=T\setminus S.
\]

Then `|A|=|B|=:t`, `A cap B=emptyset`, and

\[
\boxed{
\sum_{a\in A}aa^T=
\sum_{b\in B}bb^T.
}
\tag{3.1}
\]

Call such a pair a **balanced frame trade of volume `t`**. This is only local terminology for (3.1). The established Hadamard-trade literature modifies entries of a Hadamard matrix; no identity of notions is asserted here.

Because `A` and `B` are subsets of basis supports, both corresponding column matrices

\[
U=[a_1\cdots a_t],\qquad
V=[b_1\cdots b_t]
\]

have full column rank. Equation (3.1) says

\[
UU^T=VV^T.
\tag{3.2}
\]

### Proposition 3.1 — every support ambiguity is a partial cube isometry

There exists an orthogonal matrix `Q in O(t)` such that

\[
\boxed{V=UQ.}
\tag{3.3}
\]

For a nontrivial trade, `Q` is not a signed permutation matrix.

#### Proof

For every matrix `M`, `range(MM^T)=range(M)`. Thus (3.2) gives `range(U)=range(V)`. Since both have full column rank `t`, write `V=UQ` with `Q` invertible. Substitution gives

\[
U(I-QQ^T)U^T=0.
\]

Applying a left inverse of `U` on the left and its transpose on the right yields `QQ^T=I`, hence `Q in O(t)`. If `Q` were a signed permutation, the columns of `V` would agree up to sign and order with the columns of `U`, contrary to `A cap B=emptyset`. ∎

So non-simplicial Gram ambiguity is equivalent to finding a nonmonomial orthogonal map which sends a finite spanning set of cube rows to cube rows.

Any nonzero integer support difference also contains an inclusion-minimal signed affine dependence among correlation vertices, i.e. a circuit of the correlation configuration. Thus the exact root-fiber problem can be organized by circuits/trades in the minimal face instead of by unconstrained orthogonal matrices.

---

## 4. A sharp local obstruction: the minimum nontrivial frame-trade volume is four

### Theorem 4.1

For basis-supported balanced frame trades as above,

\[
\boxed{t\ge4,}
\tag{4.1}
\]

and volume `4` actually occurs.

#### Proof: `t=1`

Equality of one rank-one correlation matrix gives `aa^T=bb^T`, hence `b=+-a`, the same sign class. This contradicts disjointness.

#### Proof: `t=2`

Choose two linearly independent rows of `U`; call the resulting `2 x 2` sign matrix `U_0`. The same rows of `V` form `V_0`, and

\[
U_0U_0^T=V_0V_0^T.
\]

Two independent sign vectors in dimension two are orthogonal, so both row Gram matrices equal `2I`. Hence

\[
Q=U_0^{-1}V_0=\frac12U_0^TV_0.
\]

Every entry of `U_0^TV_0` is an even integer, so `Q` is an integral orthogonal matrix. Every integral orthogonal matrix is a signed permutation. Proposition 3.1 then makes the trade trivial, contradiction.

#### Proof: `t=3`

Choose three independent rows and call the square sign submatrices `U_0,V_0`. They have the same row Gram matrix.

Multiply columns of each matrix independently by signs so that its first row becomes `(1,1,1)`; this preserves the row Gram matrix. If needed, multiply rows two and three of **both** matrices by the same signs so their inner products with the first row are `+1`. Because the matrices are invertible, neither lower row equals the first, so each lower row now has exactly one minus sign. The two minus positions must be distinct; otherwise the two lower rows coincide. Therefore their mutual inner product is `-1`.

Thus in each matrix the two lower rows are exactly two distinct members of

\[
(-1,1,1),\quad(1,-1,1),\quad(1,1,-1).
\]

A permutation of the three columns carries the normalized `U_0` to the normalized `V_0`. Undoing the column sign normalizations shows `V_0=U_0\Pi\Delta`; hence the global `Q=U_0^{-1}V_0` is a signed permutation, again contradicting nontriviality.

#### Construction at `t=4`

Take

\[
U=\begin{pmatrix}
1&1&1&1\\
-1&-1&1&1\\
-1&1&-1&1\\
-1&1&1&-1
\end{pmatrix},
\qquad
V=\begin{pmatrix}
1&1&1&1\\
-1&-1&1&1\\
-1&1&-1&1\\
1&-1&-1&1
\end{pmatrix}.
\tag{4.2}
\]

Direct multiplication gives

\[
UU^T=VV^T=4I.
\]

The sign classes of the columns of `U` are

\[
+---,\quad +-++,\quad ++-+,\quad +++-,
\]

while those of `V` are

\[
+--+,\quad +-+-,\quad ++--,\quad ++++,
\]

so the supports are disjoint. Moreover

\[
U^{-1}V
=\frac12
\begin{pmatrix}
1&1&1&-1\\
1&1&-1&1\\
1&-1&1&1\\
-1&1&1&1
\end{pmatrix},
\tag{4.3}
\]

which is orthogonal and nonmonomial. Hence a nontrivial volume-four trade exists. ∎

This theorem says that the first failure of the simplicial/root-unique regime is a genuinely four-column phenomenon; pair and triple replacement mechanisms cannot create new Gram roots.

---

## 5. B24 — FIND THE EXTREMAL OBJECT: exact maximum support fibers through `r=6`

The exact checker

`2026-09-19T230000Z__F0011_gram_fiber_census.py`

enumerates every `r`-subset of the `2^{r-1}` canonical sign classes for `2<=r<=6`. It keys the frame sum by all off-diagonal entries (the diagonal is identically `r`), counts every support fiber exactly, and uses Bareiss elimination to verify a positive-definite witness at the global maximum. No floating point arithmetic is used.

The resulting exact maxima are

| r | sign classes | r-subsets | distinct Gram sums | global max `|B(K)|` | positive-definite max witness? |
|---:|---:|---:|---:|---:|---|
| 2 | 2 | 1 | 1 | 1 | yes, det 4 |
| 3 | 4 | 4 | 4 | 1 | yes, det 16 |
| 4 | 8 | 70 | 69 | 2 | yes, `K=4I`, det 256 |
| 5 | 16 | 4,368 | 4,208 | 2 | yes, det 1,024 |
| 6 | 32 | 906,192 | 834,960 | **6** | yes, det 16,384 |

For `r=6`, one maximizing positive-definite Gram matrix is

\[
K_6=
\begin{pmatrix}
6&0&-2&0&-2&0\\
0&6&0&2&0&2\\
-2&0&6&0&-2&0\\
0&2&0&6&0&-2\\
-2&0&-2&0&6&0\\
0&2&0&-2&0&6
\end{pmatrix},
\qquad
\det K_6=16384.
\tag{5.1}
\]

Because the enumeration's global maximum is over **all** support sums, including singular ones, and (5.1) attains that maximum with positive determinant, the same number `6` is exactly the maximum over positive-definite sign Gram matrices.

Combining with Theorem 2.1, the exact maximum number of ordered signed Gram roots for `r=2,...,6` is

\[
\boxed{
8,\ 48,\ 768,\ 7680,\ 276480.
}
\tag{5.2}
\]

### Consequence for the extremal hypothesis

The naive conjecture “every positive-definite sign Gram root is unique up to signed permutation” is false already at `r=4`, and multiplicity rises to six supports by `r=6`. Also `K=rI` is **not** established as the universal extremizer: it is the unique max-support Gram sum at `r=4`, but the `r=6` displayed maximizer is not diagonal. Thus a future asymptotic extremal theorem must control nonorthogonal Gram points, not only Hadamard `K=rI` fibers.

This finite census is an exact milestone about the B24 extremal object. It is **not** movement of the source-level frozen metric `N_exact`, which remains tied to complete integral-spectrum classification by matrix order.

---

## 6. B30 — ONE SCALE AT A TIME: exact structure of the corank-one cross block

Assume now

\[
\operatorname{corank}C=1.
\]

### Proposition 6.1 — dephased binary normal form

By independent diagonal sign switches on the two halves of `H`, one may dephase `C` so that its first row and first column are all `+1`. Then uniquely

\[
C=
\begin{pmatrix}
1&\mathbf1^T\\
\mathbf1&J-2A
\end{pmatrix}
\tag{6.1}
\]

for an `(r-1) x (r-1)` binary matrix `A`. Subtracting the first row from every lower row gives

\[
\boxed{
\operatorname{rank}C=1+\operatorname{rank}A,
\qquad
\operatorname{corank}C=\operatorname{corank}A.
}
\tag{6.2}
\]

Therefore the corank-one branch is exactly the binary rank condition

\[
\operatorname{rank}A=r-2.
\tag{6.3}
\]

If `Az=0`, then

\[
v=(-\mathbf1^Tz,z)
\tag{6.4}
\]

spans `ker C`; every vector in `ker C` is of this form. Similarly, if `A^Tw=0`, then

\[
u=(-\mathbf1^Tw,w)
\tag{6.5}
\]

spans `ker C^T`. In particular

\[
\boxed{\mathbf1^Tv=\mathbf1^Tu=0.}
\tag{6.6}
\]

Since `A` is integral of rank `r-2`, primitive integer choices of `u,v` exist. Thus after dephasing, the two endpoint modes from the preceding run are balanced rational/integer directions, not arbitrary real eigenlines.

#### Proof

Dephasing is standard diagonal sign switching. Subtracting the first row of (6.1) from lower row `i` replaces it by `(0,-2A_i)`, proving (6.2). Solving `C(a,z)^T=0` gives first equation `a+1^Tz=0`; substituting this into the lower equations leaves exactly `Az=0`. The left-kernel calculation is the transpose. ∎

### Proposition 6.2 — fixing one side leaves at most two sign choices on the other

Fix a corank-one `C`. If `P,P'` are symmetric solutions of

\[
PC+CD=0
\]

for the same `D`, then

\[
P-P'=\alpha uu^T
\tag{6.7}
\]

for a scalar `alpha` and a generator `u` of `ker C^T`. Therefore a fixed pair `(C,D)` has at most two sign-matrix choices for `P`. Symmetrically, a fixed pair `(C,P)` has at most two sign-matrix choices for `D`.

#### Proof

`(P-P')C=0`. Since `range(C)=(ker C^T)^perp=u^perp`, the symmetric operator `P-P'` annihilates `u^perp`. Its range is therefore contained in `span(u)`, so it has the form `alpha uu^T`. A nonconstant affine line in a real vector space meets a `{+-1}` cube in at most two points: any coordinate in which the direction is nonzero permits at most two scalar values. The transpose argument gives the statement for `D`. ∎

This unconditional lemma shows that large corank-one completion fibers cannot come from varying only one diagonal half while holding the other half and cross block fixed.

---

## 7. Generic corank-one rigidity from distinct nonzero singular values

Let the nonzero singular values of a corank-one sign matrix `C` be

\[
\sigma_1,\ldots,\sigma_{r-1}.
\]

### Theorem 7.1 — fixed `C` has only `2^{O(r)}` generic completions

Assume the nonzero singular values are pairwise distinct. Then for fixed `C` and fixed `s`, the number of real symmetric pairs `(P,D)` satisfying (1.1) is at most

\[
\boxed{2^{r+1}.}
\tag{7.1}
\]

If in addition the multiplicity of `+s` in the full `2r x 2r` two-eigenvalue spectrum is fixed, the number is at most

\[
\boxed{2^r.}
\tag{7.2}
\]

The same bounds therefore hold a fortiori for sign completions.

#### Proof

Put

\[
A_L=s^2I-CC^T=P^2.
\tag{7.3}
\]

The eigenvalue of `A_L` on `ker C^T` is `s^2`; on the remaining singular directions they are

\[
s^2-\sigma_i^2.
\]

Since every `sigma_i>0` and the nonzero singular values are pairwise distinct, these `r` eigenvalues are all distinct. Thus `A_L` has simple spectrum.

Every symmetric square root `P` of `A_L` commutes with `A_L` because

\[
PA_L=P^3=A_LP.
\]

A commuting symmetric matrix is diagonal in the one-dimensional eigenspaces of `A_L`. On each positive eigenvalue there are two square-root signs; on a zero eigenvalue there is only zero. Hence there are at most `2^r` possible real symmetric `P`.

Let `E=ker C^T` and `F=ker C`. The endpoint decomposition from the preceding run gives an invertible restriction

\[
C_0:F^\perp\to E^\perp.
\]

For a selected `P`, equation `PC+CD=0` forces uniquely on `F^perp`

\[
D_0=-C_0^{-1}P_0C_0.
\tag{7.4}
\]

On the one-dimensional `F`, equation `D^2=s^2I-C^TC` forces `D` to act by either `+s` or `-s`. Thus there are at most two `D` for each `P`, proving (7.1).

Now fix the full two-eigenvalue spectrum, and let `a` be the multiplicity of `+s`. On the invertible cores, (7.4) makes the traces cancel. Write the endpoint eigenvalues as `epsilon s` for `P|_E` and `delta s` for `D|_F`, with `epsilon,delta in {+-1}`. Then

\[
\operatorname{tr}H=s(\epsilon+\delta)=s(2a-2r).
\tag{7.5}
\]

For a chosen `P`, `epsilon` is fixed, and (7.5) determines `delta` uniquely if a completion exists. Therefore at most one `D` remains per `P`, proving (7.2). ∎

### Corollary 7.2 — exact location of possible quadratic entropy at corank one

Any corank-one completion family with quadratic entropy in `r` must lie inside the discriminant-degenerate locus where `C` has a repeated nonzero singular value.

So after the preceding run reduced singularity to endpoint modes, the present run reduces the **generic** one-endpoint-mode case to exponential rather than quadratic ambiguity. The unresolved corank-one obstruction is now the repeated-singular-value subfamily together with its sign constraints.

---

## 8. Relation to prior literature checked on 2026-09-19 UTC / 2026-09-20 local time

1. **Goldberger–Strassler (2022), “A practical algorithm for completing half-Hadamard matrices using LLL”, J. Algebraic Combinatorics 55, 217–244, DOI 10.1007/s10801-021-01077-z.** Their work directly studies half-Hadamard completion and integer Gram square roots `XX^T=G`; its practical completion guarantee depends on an unproved LLL-performance conjecture. The exact support reconstruction above is a different finite formulation and no priority/novelty claim is made.
2. **Ó Catháin–Wanless (2015), “Trades in complex Hadamard matrices”.** Their “trade” is a set of matrix entries changed to obtain another Hadamard matrix. They prove a real Hadamard entry-trade has at least `n` entries and study rectangular trades. The frame-support replacement (3.1) is not asserted to be the same object.
3. **Crnković–Egan–Švob (2026), “A universal theory of switching for combinatorial objects, and applications to complex Hadamard matrices”, J. Algebraic Combinatorics 63, article 64, published 5 June 2026, DOI 10.1007/s10801-026-01548-1.** This develops a broad switching framework and resolves an open problem about complex-Hadamard trade size. It is adjacent prior art that makes novelty claims about the descriptive “frame trade” especially inappropriate without a dedicated comparison.
4. **Ferber–Jain–Zhao (2021), “On the number of Hadamard matrices via anti-concentration”, Combinatorics, Probability and Computing.** This remains relevant to the orthogonal Gram point `K=rI`; controlling all positive-definite Gram fibers uniformly is at least as delicate as controlling structured Hadamard fibers.
5. **Alexander Van Werde (arXiv:2608.12410, submitted 11 August 2026), “Finding all cospectral mates over a number field”.** The complete finite algorithm is in the nonzero-discriminant/simple-spectrum regime. The repeated-spectrum symmetric-Hadamard boundary here lies outside that clean regime.

A bounded fresh search did not surface a paper proving Vu’s full Conjecture 9.4 asymptotic. That is only negative search evidence, not an openness or novelty certificate.

---

## 9. What moved mathematically and what did not

The source-level frozen metric is unchanged:

\[
\boxed{N_{\rm exact}:9\to9.}
\]

The run nevertheless produces three substantive reductions:

- **B19:** every positive-definite sign-Gram fiber is an exact 0–1 support fiber, and every ambiguity is generated by balanced frame trades / correlation circuits; nontrivial volume begins exactly at four.
- **B24:** the exact extremal support-fiber multiplicities through `r=6` are `1,1,2,2,6`; a nonorthogonal positive-definite `r=6` Gram matrix attains the global maximum.
- **B30:** the corank-one cross block has a dephased rank-`r-2` binary core with balanced integer endpoint modes, and if its nonzero singular values are distinct then fixed-spectrum completion multiplicity for fixed `C` is at most `2^r`.

The remaining source obstruction is still asymptotic. In the invertible branch it is the growth of non-simplicial positive-definite sign-Gram support fibers. In the first singular branch it is now localized to repeated-nonzero-singular-value cross blocks. Neither is controlled here by `2^{o(r^2)}` uniformly.
