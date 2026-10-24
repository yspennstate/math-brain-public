Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated binding model/effort selector or runtime telemetry is exposed.

# F0011 — two-sided equitable quotient and ternary-core reduction for the `|delta|=4` shell

Date: 2026-09-20 UTC  
Role: C05 / R7-06, registry native ID `6aabe827777c8191a43330b4a87d481d`  
Canonical target: F0011 / Van H. Vu, *Recent progress in combinatorial random matrix theory*, Conjecture 9.4  
Status: **PROVED PARTIAL** toward the source conjecture, pending later independent review. This is not a source-level solution and no external novelty claim is made.

## 1. Source target and exact inherited point

Vu's Conjecture 9.4 asks, for the symmetric Rademacher matrix `M_n^sym` with independent fair signs on and above the diagonal,

\[
\Pr\bigl(\operatorname{Spec}(M_n^{\rm sym})\subset\mathbb Z\bigr)
=2^{-(1/2+o(1))n^2}.
\]

Equivalently, the total number of labelled symmetric sign matrices with integral spectrum should be `2^{o(n^2)}`. The source statement is a total-spectrum event, not a fixed-spectrum statement.

The active restricted family remains

\[
H=H^T\in\{\pm1\}^{N\times N},\qquad H^2=NI,
\]

with `N=2r` and a balanced cut

\[
H=\begin{pmatrix}P&C\\C^T&D\end{pmatrix}.
\]

The latest own report before this note is

`research7_2026-09-17/R7-06/runs/2026-09-20/2026-09-20T090800Z__report.md`.

That report proves, in the entropy-dangerous low-rank branch,

\[
K:=CC^T=\lambda I+R,
\qquad q:=\operatorname{rank}R=o(r),
\qquad |\lambda-r|\le \frac{rq}{r-q},
\]

and for the semidefinite arithmetic shell `|delta|=4`, where

\[
\delta:=r-\lambda=4\varepsilon,\qquad \varepsilon\in\{+1,-1\},
\]

it proves the following exact alternative after switching and permutation:

* either the defect has a two-parity core of rank at most four;
* or it has one parity class and
  \[
  R=4\varepsilon BB^T,
  \]
  where `B` is the membership matrix of a set partition of `[r]` into `q` nonempty groups.

Therefore every shell point with `q>4` is automatically in the one-parity branch. The purpose of this note is to pass from the **row Gram skeleton** to a **two-sided root-fiber decomposition** and then compress every sign root to a ternary generalized-orthogonality core. This is the missing bridge attacked in this run.

Throughout Sections 2–8 assume `r>12`, `q>4`, and

\[
CC^T=(r-4\varepsilon)I+4\varepsilon BB^T,
\tag{1.1}
\]

where `C` is an `r x r` sign matrix, `B` is the membership matrix of a partition

\[
\mathcal G=\{G_1,\ldots,G_q\},\qquad |G_i|=a_i,\qquad \sum_i a_i=r,
\]

and `epsilon=+1` is the positive-semidefinite shell while `epsilon=-1` is the negative-semidefinite shell. Put

\[
\lambda:=r-4\varepsilon>0.
\tag{1.2}
\]

The negative branch is allowed to be singular in its exceptional block-constant directions; no invertibility of `C` is assumed.

---

## 2. The column Gram is forced into the same shell

Set

\[
K_L:=CC^T,\qquad K_R:=C^TC.
\]

Both have diagonal `r`, and because they are square Gram matrices they have exactly the same eigenvalues with multiplicity. From (1.1),

\[
K_L-\lambda I=4\varepsilon BB^T
\]

is semidefinite of sign `epsilon`, rank `q`, and constant diagonal `4 epsilon`. Therefore

\[
R_R:=K_R-\lambda I
\]

has the same nonzero eigenvalues, the same rank `q`, the same sign of semidefiniteness, and the same constant diagonal `4 epsilon`.

The previous `|delta|=4` shell theorem applies to `R_R` as well. Since `q>4`, its two-parity alternative is impossible. Hence, after an independent column switching and permutation, there is a column partition

\[
\mathcal H=\{H_1,\ldots,H_q\}
\]

with membership matrix `B'` such that

\[
\boxed{
C^TC=(r-4\varepsilon)I+4\varepsilon B'B'^T.
}
\tag{2.1}
\]

This is the first new step: **a one-sided block Gram root automatically has a two-sided block Gram structure** once `q>4`.

### Matching of block-size multisets

For a row block of size `a`, the corresponding exceptional eigenvalue of `K_L` is

\[
\mu_a:=\lambda+4\varepsilon a
=r+4\varepsilon(a-1).
\tag{2.2}
\]

The map `a -> mu_a` is injective. The exceptional eigenvalues of `K_R` have the same form with the column-block sizes. Equality of the spectra therefore gives

\[
\boxed{
\{|G_1|,\ldots,|G_q|\}_{\rm multi}
=
\{|H_1|,\ldots,|H_q|\}_{\rm multi}.
}
\tag{2.3}
\]

Thus row and column partitions have the same block-size multiset, including at the singular endpoint `mu_a=0` of the negative shell.

---

## 3. Spectral intertwining makes the partition equitable

Let `m_a` denote the number of row groups of size `a`; by (2.3) this is also the number of column groups of size `a`.

Let `U` be the `r x q` matrix whose column associated to `G` is

\[
u_G:=|G|^{-1/2}\mathbf 1_G,
\]

and define `V` analogously for the column partition. Then

\[
U^TU=V^TV=I_q.
\]

The Gram matrices are

\[
K_L
=\lambda(I-UU^T)+U\,\operatorname{diag}(\mu_{a_i})\,U^T,
\tag{3.1}
\]

\[
K_R
=\lambda(I-VV^T)+V\,\operatorname{diag}(\mu_{b_j})\,V^T.
\tag{3.2}
\]

The identity

\[
(CC^T)C=C(C^TC)
\tag{3.3}
\]

shows that `C` carries each eigenspace of `K_R` into the equal-eigenvalue eigenspace of `K_L`. Since the exceptional eigenvalue `mu_a` determines the block size `a`, `C` sends the column block-constant space of size class `a` into the row block-constant space of the same size class.

Define the quotient matrix

\[
M:=U^TCV.
\tag{3.4}
\]

After ordering groups by size, `M` is block diagonal:

\[
\boxed{M=\bigoplus_a M_a,\qquad M_a\in\mathbb R^{m_a\times m_a}.}
\tag{3.5}
\]

Moreover

\[
\boxed{
M_a^TM_a=M_aM_a^T=\mu_a I_{m_a}.
}
\tag{3.6}
\]

When `mu_a=0`, this simply says `M_a=0`; no inverse is taken.

### Integer quotient theorem

The entries of `M_a` are actually integers. If `G` and `H` are row and column groups of the same size `a`, then

\[
M_{G,H}
=\frac1a\sum_{x\in G}\sum_{y\in H} C_{xy}.
\]

But `Cv_H` is constant on the row group `G`, with value `M_{G,H}/sqrt(a)`. On the other hand its entry at `x in G` is

\[
\frac1{\sqrt a}\sum_{y\in H}C_{xy}.
\]

Therefore every row of the `a x a` block `C[G,H]` has the same sum and

\[
\boxed{
\sum_{y\in H}C_{xy}=M_{G,H}
\quad\text{for every }x\in G.
}
\tag{3.7}
\]

By transposition every column of that block has the same sum as well. Hence

\[
\boxed{
M_a\in\mathbb Z^{m_a\times m_a},\qquad
|M_{G,H}|\le a,\qquad
M_{G,H}\equiv a\pmod2.
}
\tag{3.8}
\]

Thus every equal-size block pair is biregular with an integer row/column sum, while different size classes are spectrally decoupled.

### Unequal block sizes are exactly balanced

If `|G|=a`, `|H|=b`, and `a ne b`, then `Cv_H` belongs to the row eigenspace `mu_b`, which has no support on the block-constant direction of `G`. Hence every row of `C[G,H]` has sum zero. By the transpose argument every column has sum zero:

\[
\boxed{
a\ne b
\Longrightarrow
C[G,H]\mathbf1=0,
\qquad
\mathbf1^TC[G,H]=0.
}
\tag{3.9}
\]

A sign vector of odd length cannot have sum zero. Therefore:

\[
\boxed{
\text{if two distinct block sizes occur, then every occurring block size is even.}
}
\tag{3.10}
\]

Equivalently, if any block size is odd, **all blocks have that same size**. This is a new arithmetic rigidity of the root itself, not merely of the Gram skeleton.

---

## 4. Subquadratic entropy of all quotient data when `q=o(r)`

The row/column signed partitions themselves use only `2^{o(r^2)}` possibilities:

\[
\#\{\text{labelled partitions into }q\text{ groups plus switchings}\}
\le q^{2r}2^{2r}
=2^{O(r\log q+r)}
=2^{o(r^2)}.
\tag{4.1}
\]

For a fixed size profile, the crude entrywise bound (3.8) gives

\[
\log_2\#\{M\}
\le
\sum_a m_a^2\log_2(2a+1).
\tag{4.2}
\]

Since `m_a<=q`,

\[
\sum_a m_a^2\log_2(2a+1)
\le
q\sum_a m_a\log_2(2a+1).
\]

The function `log(2x+1)` is concave, and

\[
\frac1q\sum_a m_a a=\frac rq.
\]

Hence Jensen gives

\[
\boxed{
\log_2\#\{M\}
\le
q^2\log_2\left(\frac{2r}{q}+1\right).
}
\tag{4.3}
\]

If `q=o(r)`, write `q=epsilon_r r` with `epsilon_r ->0`. Then

\[
q^2\log\left(\frac rq+1\right)
=r^2\epsilon_r^2\log(1/\epsilon_r+1)
=o(r^2).
\]

Therefore:

\[
\boxed{
q=o(r)
\Longrightarrow
\text{all signed partitions and all quotient matrices together have }2^{o(r^2)}\text{ possibilities.}
}
\tag{4.4}
\]

This moves the entropy question from the quotient to the residual operator.

---

## 5. Exact quotient-residual decomposition

Put

\[
Z:=C-UMV^T.
\tag{5.1}
\]

Because `CV=UM` and, by transposition, `U^TC=MV^T`,

\[
\boxed{ZV=0,\qquad U^TZ=0.}
\tag{5.2}
\]

Thus `Z` has zero sum on every column partition block in each row and zero sum on every row partition block in each column.

Using (3.1), (3.2), and (3.6),

\[
\boxed{
ZZ^T=\lambda(I-UU^T),
\qquad
Z^TZ=\lambda(I-VV^T).
}
\tag{5.3}
\]

So after removing only the `q` block-constant modes, the remaining `(r-q)`-dimensional part is an exact scaled isometry, with scale `sqrt(lambda)`. This holds equally in the singular negative shell because possible zero singular values occur only in the quotient `M`; the residual scale `lambda=r+4` is strictly positive.

The blockwise residual entries satisfy

\[
Z_{xy}=C_{xy}-\frac{M_{G,H}}a
\]

when `x in G`, `y in H`, and `|G|=|H|=a`, while `Z_{xy}=C_{xy}` for unequal sizes. The point of the next section is to replace this rational residual by an **integer ternary core**.

---

## 6. Difference-lattice compression produces a ternary core

For a row block `G={g_0,g_1,...,g_{a-1}}`, choose one anchor `g_0` and let

\[
F_G=
\begin{pmatrix}
 e_{g_1}-e_{g_0}&\cdots&e_{g_{a-1}}-e_{g_0}
\end{pmatrix}
\in\mathbb Z^{r\times(a-1)}.
\]

Let `F` be the block direct sum of these column bases over all row groups. Define `E` analogously for the column groups. Then `F` and `E` have `d:=r-q` columns and span the integer lattices of vectors having zero coordinate sum in every group.

Their Gram matrices are block diagonal:

\[
G_{\mathcal G}:=F^TF
=\bigoplus_{G\in\mathcal G}(I_{|G|-1}+J_{|G|-1}),
\tag{6.1}
\]

\[
G_{\mathcal H}:=E^TE
=\bigoplus_{H\in\mathcal H}(I_{|H|-1}+J_{|H|-1}).
\tag{6.2}
\]

Because `C` maps the column zero-sum lattice into the row zero-sum lattice, there is a unique integer matrix `A in Z^{d x d}` such that

\[
CF=\text{(not dimensionally defined); instead, with the column basis }E,
\qquad
\boxed{CE=FA.}
\tag{6.3}
\]

The coordinates are exceptionally simple. A column of `CE` is the difference of two sign columns of `C`, so its entries lie in `{ -2,0,2 }`. In the basis `F`, the coefficient of `e_g-e_{g_0}` is simply the non-anchor coordinate of that difference vector. Hence

\[
\boxed{A\in\{-2,0,2\}^{d\times d}.}
\tag{6.4}
\]

Write

\[
A=2T,
\qquad
\boxed{T\in\{-1,0,1\}^{d\times d}.}
\tag{6.5}
\]

This `T` is the **ternary core**.

Now use `E^TC^TCE=lambda E^TE`, because `E` lies in `V^perp`, and substitute `CE=2FT`:

\[
4T^T(F^TF)T=\lambda(E^TE).
\]

Since `lambda` is divisible by four in this shell, put

\[
s:=\frac\lambda4=\frac r4-\varepsilon\in\mathbb Z_{>0}.
\tag{6.6}
\]

Then

\[
\boxed{
T^T G_{\mathcal G}T=sG_{\mathcal H}.
}
\tag{6.7}
\]

Since the two block-size multisets agree, both metric matrices have the same determinant. In particular `T` is invertible and

\[
\boxed{
|\det T|=s^{d/2}.
}
\tag{6.8}
\]

Consequently, if `d=r-q` is odd, then

\[
\boxed{s=r/4-\varepsilon\text{ must be a perfect square}.}
\tag{6.9}
\]

Because `r` is even, `d` is odd exactly when `q` is odd. Thus, away from the sparse arithmetic subsequence on which `r/4-epsilon` is a square, **every one-parity `|delta|=4` root with `q>4` has even defect rank**.

This is a new arithmetic obstruction that comes from the root fiber, not from the row Gram determinant alone.

### Injectivity of the compression

For fixed signed row/column partitions and quotient `M`, the pair of subspaces

\[
\operatorname{span}(V)\oplus\operatorname{span}(E)=\mathbb R^r
\]

is a direct sum. The action of `C` on the first summand is fixed by

\[
CV=UM,
\]

and the action on the second is fixed by

\[
CE=2FT.
\]

Therefore `C` is uniquely determined by `(partitions, switchings, M, T)`. Hence the map from sign roots to ternary cores is injective once the subquadratic outer data are fixed.

We have proved:

### Theorem 6.1 — two-sided quotient / ternary-core reduction

Let `C in {+-1}^{r x r}` lie in the semidefinite `|delta|=4` shell of the inherited F0011 low-rank branch, with `q=rank R>4`. After row/column switchings and labelled partitions into `q` groups, there exist:

1. matching row and column block-size multisets;
2. integer quotient matrices `M_a` satisfying `M_aM_a^T=mu_a I` and the parity/size bounds (3.8);
3. a ternary matrix
   \[
   T\in\{-1,0,1\}^{(r-q)\times(r-q)}
   \]
   satisfying the exact generalized-orthogonality equation
   \[
   T^TG_{\mathcal G}T=(r/4-\varepsilon)G_{\mathcal H};
   \]
4. exact reconstruction of `C` from this data.

If moreover `q=o(r)`, all data except the ternary core have total entropy `o(r^2)`.

This theorem includes the negative-shell singular endpoint.

---

## 7. Additional local arithmetic consequences

### 7.1 Odd block sizes cannot mix

Equation (3.9) proves that if more than one block size occurs then all sizes are even. Thus a one-parity shell with an odd group size must be **uniform**:

\[
\boxed{
\exists a\text{ odd with }m_a>0
\Longrightarrow
m_b=0\quad\forall b\ne a.
}
\tag{7.1}
\]

In particular, singleton groups cannot coexist with any larger group. In the inherited regime `q=o(r)`, the all-singleton possibility `q=r` is excluded for large `r`.

### 7.2 Quotient determinant constraints by multiplicity class

From

\[
M_aM_a^T=\mu_a I_{m_a}
\]

we get

\[
\det(M_a)^2=\mu_a^{m_a}.
\]

Therefore

\[
\boxed{
m_a\text{ odd}\Longrightarrow \mu_a=r+4\varepsilon(a-1)\text{ is a perfect square}.}
\tag{7.2}
\]

For `m_a=2`, `mu_a` must be representable by the norm form of a `2 x 2` integer orthogonal matrix; after signed row/column changes this reduces to a sum-of-two-squares condition. These restrictions are useful for pruning admissible quotient profiles but are not used in the entropy bound (4.4).

### 7.3 A fixed-alphabet hard core

The preceding report left the root multiplicity of a fixed block Gram matrix as an unstructured Hadamard/D-optimal-type obstacle. The new theorem shows that, once `q>4`, every such root is controlled by a **fixed three-letter alphabet** core satisfying an exact metric-isometry equation. The remaining hard object is therefore not an arbitrary sign root of a block Gram matrix but

\[
\boxed{
T\in\{-1,0,1\}^{d\times d},
\qquad
T^TG_{\mathcal G}T=sG_{\mathcal H},
\qquad d=r-q,
}
\tag{7.3}
\]

with `s=r/4-epsilon`, matching `A`-type block metrics, and the extra reconstruction constraint that the induced `C` has all entries in `{+-1}`.

This is a genuine root-fiber reduction: partitions and quotient data are already `2^{o(r^2)}` when `q=o(r)`, so any remaining quadratic entropy must live inside these ternary metric-isometries.

---

## 8. What this rules out and what remains

The proposed intermediate picture “the `|delta|=4` root fiber is controlled merely by its row Gram block partition” is incomplete. The root automatically creates a **second, spectrally matched column partition**, an equitable integer quotient, and a large ternary residual isometry. Thus the correct recursive object is two-sided.

This also explains why another row-Gram census would not address the source conjecture: after the row skeleton is fixed, a dimension `r-q=(1-o(1))r` ternary metric-isometry core remains.

What is now proved for the `|delta|=4`, `q>4`, `q=o(r)` branch:

* `[PROVED PARTIAL]` row block Gram forces a matching column block Gram;
* `[PROVED PARTIAL]` row/column block-size multisets agree exactly;
* `[PROVED PARTIAL]` unequal-size blocks are exactly row/column balanced, forcing all distinct occurring sizes to be even;
* `[PROVED PARTIAL]` equal-size quotient matrices are integral orthogonal matrices `M_aM_a^T=mu_a I`;
* `[PROVED PARTIAL]` all partition and quotient data have `2^{o(r^2)}` entropy;
* `[PROVED PARTIAL]` every sign root compresses injectively to a ternary `(r-q) x (r-q)` matrix satisfying (7.3);
* `[PROVED PARTIAL]` if `q` is odd then `r/4-epsilon` must be a square;
* `[OPEN]` prove `2^{o(r^2)}` many admissible ternary cores, or exhibit a quadratic-entropy counterfamily;
* `[OPEN]` handle the bounded-rank `q<=4` classical Hadamard / D-optimal / two-cloud fibers by a compatible recursion rather than pretending they are absent;
* `[OPEN]` higher shells, indefinite defects, and general integral spectra remain outside this theorem.

The strongest next attack is now to count (7.3). Two concrete routes are exposed:

1. exploit the direct-sum root-lattice metrics `G_G=I+J` and the ternary alphabet to obtain a combinatorial-dimension deficit unless `T` itself decomposes into smaller metric-Hadamard blocks;
2. classify the equality/near-equality cases of the determinant identity (6.8) inside ternary matrices and seek a strict contraction in the sum of squared block dimensions.

Either route works directly on the root fiber rather than on another Gram skeleton.

---

## 9. Literature boundary checked in this run

A bounded current search on 20 September 2026 did not surface a resolution of Vu's exact Conjecture 9.4 or a general subquadratic enumeration theorem for Hadamard matrices. This is negative search evidence only.

Relevant published boundaries remain:

* A. Ferber, V. Jain, Y. Zhao, *On the number of Hadamard matrices via anti-concentration*, Combinatorics, Probability and Computing 31 (2022), 455–477, DOI `10.1017/S0963548321000377`. They prove the first constant-factor quadratic improvement over the Odlyzko exponent and explicitly identify `2^{o(n^2)}` Hadamard enumeration as requiring new ideas.
* H. Tamura, *D-optimal designs and group divisible designs*, Journal of Combinatorial Designs 14 (2006), 451–462, DOI `10.1002/jcd.20103`, studies square matrices with block-structured Gram matrices and their relation to group-divisible designs. The present note does not claim that the general design-theoretic setting is new; the project contribution here is the exact two-sided spectral/ternary reduction for the inherited F0011 shell.

No public posting or external novelty claim is made.