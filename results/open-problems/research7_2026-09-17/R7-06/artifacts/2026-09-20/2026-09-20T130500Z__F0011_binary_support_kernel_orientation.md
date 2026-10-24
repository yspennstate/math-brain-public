# F0011 — binary support reduction for the kernel-orientation fiber

Date: 2026-09-20 UTC  
Role: C05 / R7-06 `Random Matrix Spectral Entropy`  
Canonical target: F0011 / Van H. Vu, *Recent progress in combinatorial random matrix theory*, Conjecture 9.4  
Status: **PROVED PARTIAL** toward the outside source, pending later independent review

## 1. Source target and inherited point

Vu's Conjecture 9.4 concerns the symmetric Rademacher matrix `M_n^sym`, with independent fair signs on and above the diagonal:

\[
\Pr\bigl(\operatorname{Spec}(M_n^{\rm sym})\subset\mathbb Z\bigr)
=2^{-(1/2+o(1))n^2}.
\]

Equivalently, the total number of labelled symmetric sign matrices with integral spectrum should be `2^{o(n^2)}`. The source quantifier is the total integral-spectrum event, not a fixed spectrum.

The current C05 line remains the centered fixed two-eigenvalue bridge. In the entropy-dangerous one-parity `|r-lambda|=4` shell from the preceding runs, write

\[
CC^T=(r-4\varepsilon)I+4\varepsilon BB^T,
\qquad \varepsilon\in\{+1,-1\},
\]

with `q=o(r)`, `q>4`, row and column partitions into `q` blocks, and `d=r-q`. The anchor-difference compression gives

\[
CE=2FT,\qquad C^TF=2ES,
\]

with

\[
T,S\in\{-1,0,1\}^{d\times d},
\qquad TS=ST=sI_d,
\qquad s=\frac r4-\varepsilon>0.
\]

The latest inherited theorem defines

\[
D:=T-S^T
\]

and proves

\[
\operatorname{rank}_{\mathbb R}D=k\le 2q=o(r),
\]

while `D` is nevertheless dense, with support density `1/2+o(1)`. It also proves the exact Riccati relation

\[
(T^TT)D^TD=(T^TT-sI)^2
\]

and localizes all remaining quadratic real freedom to the scaled isometry

\[
T/\sqrt{s}:\ker D\to\ker D^T.
\]

The purpose of this note is to remove a further source of apparent entropy: **the ternary signs themselves**. The kernel-orientation fiber admits an exact binary-support formulation with only subquadratic anchor overhead.

---

## 2. Exact cellwise anchor formulas

Fix one anchor `g_i` in every row block `G_i` and one anchor `h_j` in every column block `H_j`. Core row indices are the non-anchor `g`, and core column indices are the non-anchor `h`.

For `g in G_i\setminus{g_i}` and `h in H_j\setminus{h_j}`, the inherited contrast formulas are

\[
T_{g,h}=\frac{C_{g,h}-C_{g,h_j}}2,
\tag{2.1}
\]

\[
S_{h,g}=\frac{C_{g,h}-C_{g_i,h}}2,
\tag{2.2}
\]

and therefore

\[
D_{g,h}=T_{g,h}-S_{h,g}
=\frac{C_{g_i,h}-C_{g,h_j}}2.
\tag{2.3}
\]

Define two sign masks on the `d x d` contrast grid:

\[
U_{g,h}:=C_{g_i,h},
\qquad
V_{g,h}:=C_{g,h_j}.
\tag{2.4}
\]

Thus `U` is constant down each row-partition class and `V` is constant across each column-partition class, in the appropriate expanded sense, and

\[
\boxed{D=(U-V)/2.}
\tag{2.5}
\]

In particular, if

\[
E_{g,h}:=\mathbf 1_{\{D_{g,h}\ne0\}}
=\mathbf 1_{\{U_{g,h}\ne V_{g,h}\}},
\tag{2.6}
\]

then `E` is exactly the reduction of `D` modulo `2` after identifying `-1` and `+1` with `1`.

Because `D` is an integer matrix,

\[
\boxed{
\operatorname{rank}_{\mathbb F_2}E
\le \operatorname{rank}_{\mathbb Q}D
=k\le2q.
}
\tag{2.7}
\]

The rank inequality follows because a nonzero minor over `F_2` is a nonzero integer minor and hence is nonzero over `Q`.

---

## 3. New theorem I — the ternary pair is actually a signed binary-support pair

Define binary matrices

\[
X_{g,h}:=\mathbf1_{\{C_{g,h}\ne V_{g,h}\}},
\qquad
Y_{g,h}:=\mathbf1_{\{C_{g,h}\ne U_{g,h}\}}.
\tag{3.1}
\]

From (2.1), if `C_{g,h}=V_{g,h}` then `T_{g,h}=0`; if `C_{g,h}=-V_{g,h}` then `T_{g,h}=-V_{g,h}`. Therefore

\[
\boxed{T=-V\odot X.}
\tag{3.2}
\]

Likewise

\[
\boxed{S^T=-U\odot Y.}
\tag{3.3}
\]

Here `odot` is the entrywise product.

Since `U` and `V` are signs, changing the comparison sign from `V` to `U` toggles exactly on the cells where `U\ne V`. Hence, entrywise over `{0,1}`,

\[
\boxed{Y=X\oplus E.}
\tag{3.4}
\]

This proves an exact local dichotomy:

* if `D_{g,h}=0`, then `T_{g,h}=S_{h,g}` and both are simultaneously zero or the same sign;
* if `D_{g,h}\ne0`, then exactly one of `T_{g,h}`, `S_{h,g}` is nonzero.

Equivalently, on the defect support the two inverse cores split the cell between them, while off the defect support they coincide.

Most importantly, **once the anchor masks `U,V` are fixed, the binary support matrix `X` determines both `T` and `S` uniquely**.

---

## 4. New theorem II — exact signed binary biorthogonality

Insert (3.2)--(3.4) into `TS=sI`. Since

\[
S=-(U\odot Y)^T,
\]

the two minus signs cancel and give

\[
\boxed{
(V\odot X)(U\odot(X\oplus E))^T=sI_d.
}
\tag{4.1}
\]

The reverse equation `ST=sI` is

\[
\boxed{
(U\odot(X\oplus E))^T(V\odot X)=sI_d.
}
\tag{4.2}
\]

Thus the fixed two-sided ternary Gram fiber is exactly an **anchor-signed binary incidence problem**. No ternary sign choice remains after `U,V` are recorded.

This is stronger than the preceding Gram-skeleton reduction: the remaining unknown is one binary matrix `X`, not a pair of ternary matrices.

---

## 5. New theorem III — an exact `s`-regular common-support core

Define the common-support matrix

\[
A:=X\odot(1-E).
\tag{5.1}
\]

Take the `g`th diagonal entry of (4.1). On a cell with `E_{g,h}=1`, exactly one of `X_{g,h}` and `(X\oplus E)_{g,h}` equals `1`, so that cell contributes zero. On a cell with `E_{g,h}=0`, we have `U_{g,h}=V_{g,h}` and the contribution is exactly `X_{g,h}`. Therefore

\[
\boxed{
\sum_h A_{g,h}=s
\quad\text{for every row }g.
}
\tag{5.2}
\]

The diagonal of (4.2) gives the column version:

\[
\boxed{
\sum_g A_{g,h}=s
\quad\text{for every column }h.
}
\tag{5.3}
\]

Hence

\[
\boxed{
A\text{ is the incidence matrix of an }s\text{-regular bipartite graph on }d+d\text{ vertices}.
}
\tag{5.4}
\]

By the 1-factorization theorem for regular bipartite graphs,

\[
\boxed{
A=P_1+\cdots+P_s
}
\tag{5.5}
\]

for pairwise edge-disjoint permutation matrices `P_1,...,P_s`.

So the zero pattern of the low-rank dense defect `D` necessarily contains `s` edge-disjoint perfect matchings on which `T` and `S^T` agree and are nonzero.

Because `s=r/4+O(1)` and `d=r-q=(1-o(1))r`, this is a linear-size matching packing, not a small exceptional feature.

### Matching normalization

Choosing one of these perfect matchings and permuting the contrast columns along it makes every matched cell diagonal. Since each matched cell lies in `E=0`, after this column permutation

\[
\boxed{D_{ii}=0\quad\text{for every }i.}
\tag{5.6}
\]

The matching choice and the column permutation cost at most

\[
d!\,s=2^{O(d\log d)}=2^{o(r^2)}
\]

possibilities. Thus, at source entropy scale, every feasible kernel-orientation defect may be studied in a **zero-diagonal normal form** without excluding the singular/corank endpoint.

This normalization is useful for the next structural attack on low-rank dense ternary defects.

---

## 6. New theorem IV — subquadratic anchor overhead and a binary entropy equivalence

The two expanded anchor masks are determined by the actual anchor rows and anchor columns of `C`:

* `q` row anchors record at most `qr` signs;
* `q` column anchors record at most `qr` signs.

The labelled row and column partitions cost at most `q^{2r}` possibilities, and anchor choices inside the blocks cost at most `r^{2q}`. Therefore all partition, anchor and sign-mask data together use at most

\[
2^{O(qr+r\log q+q\log r)}
=2^{o(r^2)}
\tag{6.1}
\]

possibilities because `q=o(r)`.

For fixed such data, `X` reconstructs the entire non-anchor interior of `C` from

\[
C_{g,h}=V_{g,h}(1-2X_{g,h}),
\tag{6.2}
\]

while the anchor rows and columns were already recorded.

Consequently, if `N_bin(r,q)` denotes the maximum number of binary matrices `X` satisfying the exact signed biorthogonality system (4.1)--(4.2) for admissible anchor data, then the number of sign roots in this inherited shell obeys

\[
\boxed{
N_{\rm shell}(r,q)
\le
2^{O(qr+r\log r)}\,N_{\rm bin}(r,q).
}
\tag{6.3}
\]

In particular,

\[
\boxed{
N_{\rm bin}(r,q)=2^{o(r^2)}
\Longrightarrow
N_{\rm shell}(r,q)=2^{o(r^2)}.
}
\tag{6.4}
\]

This is an entropy-scale equivalence up to subquadratic overhead. The missing theorem is therefore no longer a ternary sign-root theorem; it is a **binary support-orientation theorem** with a low-rank defect mask and an `s`-regular common core.

---

## 7. New theorem V — finite-field shadow of the kernel orientation

Reduce (4.1) modulo `2`. All sign masks disappear, so with `E` and `X` viewed over `F_2`,

\[
\boxed{
X(X+E)^T=(s\bmod2)I.
}
\tag{7.1}
\]

Similarly

\[
\boxed{
(X+E)^TX=(s\bmod2)I.
}
\tag{7.2}
\]

Together with (2.7), this gives a low-rank finite-field defect theorem.

### Odd `s`

If `s` is odd, then `X` and `X+E` are invertible over `F_2`, and

\[
\boxed{
X+E=X^{-T},
\qquad
E=X+X^{-T},
\qquad
\operatorname{rank}_{\mathbb F_2}E\le k\le2q.
}
\tag{7.3}
\]

Thus the binary support itself is an inverse-transpose pair with a rank-`o(r)` defect.

For every `z in ker(E)`,

\[
Xz=X^{-T}z,
\]

and therefore

\[
X^TXz=z.
\]

Moreover `X(ker E)=ker E^T`. Hence the same large exact plateau seen over the reals has a finite-field shadow:

\[
\boxed{
X:\ker E\longrightarrow\ker E^T
\text{ is an isometry for the standard }F_2\text{ bilinear form}.
}
\tag{7.4}
\]

This also shows why a purely mod-2 argument is unlikely by itself to close the shell: it retains a large orthogonal-orientation sector. The integer signed equations and the regular common-support constraint (5.4) carry information not visible modulo `2`.

### Even `s`

If `s` is even, then

\[
X(X+E)^T=0,
\qquad
(X+E)^TX=0.
\tag{7.5}
\]

Thus the row spaces of `X` and `X+E` are orthogonal and

\[
\operatorname{rank}_{\mathbb F_2}X
+
\operatorname{rank}_{\mathbb F_2}(X+E)
\le d.
\tag{7.6}
\]

Their rank difference is at most `rank(E)<=k`.

If in addition `v_2(s)=1`, the inherited Smith-invariant identity gives exactly `d/2` odd invariant factors for both `T` and `S`; since reduction modulo `2` forgets only signs,

\[
\boxed{
\operatorname{rank}_{\mathbb F_2}X
=
\operatorname{rank}_{\mathbb F_2}(X+E)
=d/2,
}
\tag{7.7}
\]

and hence their row spaces are exact orthogonal complements. This is a binary dual-code normal form for that arithmetic subcase.

---

## 8. What changed and what remains open

The previous run localized all quadratic real freedom to the plateau isometry `ker D -> ker D^T`, but the object was still presented as a ternary inverse pair. The present theorem removes the sign ambiguity completely:

\[
\boxed{
\text{shell root}
\rightsquigarrow
\text{subquadratic anchor data}
+
\text{one binary matrix }X.
}
\]

The binary matrix is not arbitrary. It must satisfy simultaneously:

1. the exact signed biorthogonality equations (4.1)--(4.2);
2. a defect mask `E` with `rank_{F_2}E<=2q=o(r)`;
3. an `s`-regular common-support graph `A=X\odot(1-E)`;
4. a perfect-matching normalization in which the defect has zero diagonal;
5. the finite-field inverse-transpose / dual-code identities in Section 7.

This is a genuine structural reduction at the `2^{o(r^2)}` entropy scale. It does **not** yet count the admissible binary supports, so it does not close the centered two-eigenvalue family and certainly does not close Vu's total integral-spectrum conjecture.

The strongest next attack is now one of the following.

* **Integer support entropy:** count binary `X` satisfying (4.1) with an `s`-factor inside `1-E`, exploiting that `E` has low rank but dense support.
* **Zero-diagonal defect recursion:** after the matching normalization, classify dense rank-`o(r)` ternary `D` with zero diagonal and show that entropy-near-extremal support orientations force a contracting group-divisible / weighing-matrix recursion.
* **Arithmetic-code interaction:** in the odd-`s` branch combine `E=X+X^{-T}` over `F_2` with the integer row/column equations; in the `v_2(s)=1` branch exploit the exact dual-code pair together with the `s`-regular common support. Pure finite-field counting alone should not be expected to suffice.

The bounded-rank `q<=4` Hadamard/D-optimal branch, higher shells, indefinite defects, and the final passage from the centered two-eigenvalue slice to all integral spectra remain open.

---

## 9. Current literature boundary

A bounded fresh check on 20 September 2026 did not surface a resolution of Vu's exact Conjecture 9.4; this is negative search evidence only, not an openness or novelty certificate.

Ferber--Jain--Zhao, *On the number of Hadamard matrices via anti-concentration*, Combinatorics, Probability and Computing 31 (2022), 455--477, remains the relevant general enumeration boundary: it proves a constant quadratic improvement for Hadamard counting but explicitly notes that a `2^{o(n^2)}` bound would require new ideas.

The block-structured Gram / group-divisible-design connection is classical; see H. Tamura, *D-optimal designs and group divisible designs*, Journal of Combinatorial Designs 14 (2006), 451--462. Balancedly splittable Hadamard constructions of Kharaghani--Suda are also relevant to the possibility that a future extremal binary-support branch recurses through structured design nodes. These references do not supply the missing binary-support entropy theorem above.

---

## 10. Frozen full-source metric

No finite census was run in this iteration. The full-source metric remains

\[
\boxed{N_{\rm exact}:9\to9.}
\]
