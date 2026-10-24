# F0011 — inverse ternary core, dense low-rank defect, and Euclidean Gram collapse

Date: 2026-09-20 UTC  
Role: C05 / R7-06, registry native ID `6aabe827777c8191a43330b4a87d481d`  
Canonical target: F0011 / Van H. Vu, *Recent progress in combinatorial random matrix theory*, Conjecture 9.4  
Status: **PROVED PARTIAL** toward the source conjecture, pending later independent review

## 1. Source target and inherited shell

Vu's Conjecture 9.4 concerns the symmetric Rademacher matrix `M_n^sym`, with independent fair signs on and above the diagonal:

\[
\Pr\bigl(\operatorname{Spec}(M_n^{\rm sym})\subset\mathbb Z\bigr)
=2^{-(1/2+o(1))n^2}.
\]

Equivalently, the total number of labelled symmetric sign matrices with integral spectrum should be `2^{o(n^2)}`. The source quantifier is the total integral-spectrum event, not a fixed spectrum. The current C05 line is a restricted bridge through the centered two-eigenvalue family `H^2=NI`.

The immediately inherited result is the `|r-lambda|=4`, one-parity, low-rank sign-Gram shell. Write

\[
CC^T=(r-4\varepsilon)I+4\varepsilon BB^T,
\qquad \varepsilon\in\{+1,-1\},
\]

where the rows are partitioned into `q` nonempty blocks, the matching column Gram has the same block-size multiset, and we are interested in the entropy-dangerous regime

\[
q=o(r),\qquad q>4.
\]

Let `F` and `E` be the anchor-difference bases of the row and column blockwise zero-sum lattices. Put

\[
d=r-q,
\qquad
G_{\mathcal G}=F^TF,
\qquad
G_{\mathcal H}=E^TE.
\]

Each metric is a direct sum of blocks `I+J`. The preceding run proved that there is an injective ternary core

\[
CE=2FT,
\qquad
T\in\{-1,0,1\}^{d\times d},
\]

satisfying

\[
T^TG_{\mathcal G}T=sG_{\mathcal H},
\qquad
s=\frac r4-\varepsilon.
\tag{1.1}
\]

The missing theorem was to use the sign-reconstruction constraint, rather than count arbitrary metric similarities.

## 2. New theorem I — a reverse ternary core and a scaled inverse pair

Apply the same contrast-basis construction to `C^T`. Since `C^T` maps the row zero-sum residual space into the column zero-sum residual space, there is a unique matrix `S` with

\[
C^TF=2ES.
\tag{2.1}
\]

Each column of `C^TF/2` is a half-difference of two sign rows, hence has entries in `{-1,0,1}`. A vector in the column zero-sum space has contrast coordinates equal to its non-anchor entries. Therefore

\[
\boxed{S\in\{-1,0,1\}^{d\times d}.}
\tag{2.2}
\]

Now use `C^TC E=(r-4\varepsilon)E` and (2.1):

\[
C^T(CE)=C^T(2FT)=4EST=(r-4\varepsilon)E.
\]

Since `E` has full column rank,

\[
\boxed{ST=sI_d.}
\tag{2.3}
\]

Similarly `CC^TF=(r-4\varepsilon)F` gives

\[
\boxed{TS=sI_d.}
\tag{2.4}
\]

Thus the sign-reconstructible metric core is not an arbitrary ternary similarity: its scaled inverse is ternary as well,

\[
\boxed{S=sT^{-1}\in\{-1,0,1\}^{d\times d}.}
\tag{2.5}
\]

In particular `s` is an integer. Hence the nontrivial `q=o(r)` one-parity shell forces

\[
\boxed{r\equiv0\pmod4.}
\tag{2.6}
\]

The adjoint identity is also exact. From `CE=2FT` and `C^TF=2ES`,

\[
\boxed{T^TG_{\mathcal G}=G_{\mathcal H}S.}
\tag{2.7}
\]

Equation (1.1) follows again by multiplying (2.7) by `T` and using `ST=sI`.

## 3. New theorem II — the inverse defect is rank `<=2q`

Choose one anchor `g_i` in every row block and one anchor `h_j` in every column block. For a non-anchor row `g` in row block `i` and a non-anchor column `h` in column block `j`, the two contrast cores have the concrete entries

\[
T_{g,h}=\frac{C_{g,h}-C_{g,h_j}}2,
\qquad
S_{h,g}=\frac{C_{g,h}-C_{g_i,h}}2.
\tag{3.1}
\]

Therefore

\[
D:=T-S^T
\]

has entries

\[
D_{g,h}=\frac{C_{g_i,h}-C_{g,h_j}}2\in\{-1,0,1\}.
\tag{3.2}
\]

The first term in (3.2) is constant down each non-anchor row group, so its matrix has rank at most `q`. The second is constant across each non-anchor column group, so its matrix has rank at most `q`. Hence

\[
\boxed{D\in\{-1,0,1\}^{d\times d},\qquad \operatorname{rank}D\le2q.}
\tag{3.3}
\]

Since `S^T=T-D`, the scaled-inverse relation gives

\[
T(T^T-D^T)=sI,
\qquad
(T^T-D^T)T=sI.
\]

Consequently

\[
\boxed{\operatorname{rank}(TT^T-sI)\le2q,}
\qquad
\boxed{\operatorname{rank}(T^TT-sI)\le2q.}
\tag{3.4}
\]

Thus `T` has singular value `sqrt(s)` with multiplicity at least

\[
\boxed{d-2q=r-3q=(1-o(1))r.}
\tag{3.5}
\]

This is an ordinary Euclidean rigidity statement, not merely a similarity with respect to the `I+J` metrics.

## 4. New theorem III — midpoint normal form

Set

\[
X=\frac{T+S^T}{2}=T-\frac D2.
\tag{4.1}
\]

Because `TT^T-TD^T=sI` is symmetric, `TD^T=DT^T`. Completing the square gives

\[
\boxed{XX^T=sI+\frac14DD^T.}
\tag{4.2}
\]

Similarly, from `T^TT-D^TT=sI`,

\[
\boxed{X^TX=sI+\frac14D^TD.}
\tag{4.3}
\]

The entry alphabet of `X` is sign-reconstruction-sensitive:

* if `D_ij=0`, then `T_ij=S_ji` and `X_ij` lies in `{-1,0,1}`;
* if `|D_ij|=1`, the local four-sign identity forces exactly one of `T_ij,S_ji` to be nonzero, so

\[
\boxed{|D_{ij}|=1\Longrightarrow X_{ij}\in\{-1/2,+1/2\}.}
\tag{4.4}
\]

Thus every root is encoded by a low-rank ternary defect `D` plus a mixed ternary/half-sign matrix `X` whose row and column Grams are both fixed low-rank perturbations of `sI`.

This is stronger than saying that `T` is close to a weighing matrix in spectral rank: the two sides of the scaled inverse are centered around the same `X`.

## 5. New theorem IV — exact ordinary Gram factorization and subquadratic Gram-skeleton entropy

Let `L_{\mathcal G}` be the `q x d` block-incidence matrix on the row contrast coordinates: the `i`th row is `1` on the non-anchor coordinates of row block `i` and `0` elsewhere. Define `L_{\mathcal H}` analogously. Then

\[
G_{\mathcal G}=I+L_{\mathcal G}^TL_{\mathcal G},
\qquad
G_{\mathcal H}=I+L_{\mathcal H}^TL_{\mathcal H}.
\tag{5.1}
\]

Put

\[
Q=L_{\mathcal G}T.
\tag{5.2}
\]

For a column `t` of `T`, `Ft` is a half-difference of two sign columns. The sum of the contrast coordinates in one row block is minus the anchor coordinate of that half-difference, so it lies in `{-1,0,1}`. Therefore

\[
\boxed{Q\in\{-1,0,1\}^{q\times d}.}
\tag{5.3}
\]

Expanding (1.1) using (5.1) gives

\[
T^TT+Q^TQ=sI+sL_{\mathcal H}^TL_{\mathcal H},
\]

hence

\[
\boxed{
T^TT=sI+sL_{\mathcal H}^TL_{\mathcal H}-Q^TQ.
}
\tag{5.4}
\]

In particular the entire ordinary column Gram of `T` is determined by the column partition and the `q x d` ternary signature matrix `Q`.

For columns `j,k`, (5.4) reads explicitly

\[
\|t_j\|_0=2s-\|Q_j\|_2^2,
\tag{5.5}
\]

\[
t_j\cdot t_k=
\begin{cases}
 s-Q_j\cdot Q_k,&j,k\text{ in the same column block},\\
 -Q_j\cdot Q_k,&j,k\text{ in distinct column blocks}.
\end{cases}
\tag{5.6}
\]

Thus

\[
\boxed{2s-q\le\|t_j\|_0\le2s.}
\tag{5.7}
\]

For a fixed partition there are at most `3^(qd)` possible ordinary Gram matrices (5.4). Including the labelled `q`-block partition costs at most `q^r`, and all anchor/switching data are at most exponential in `O(qr+r)`. Therefore, in the inherited `q=o(r)` regime,

\[
\boxed{
\#\{\text{possible ordinary Gram skeletons }T^TT\}
=2^{o(r^2)}.
}
\tag{5.8}
\]

Applying the same argument to `S` gives a ternary `P=L_{\mathcal H}S` and

\[
S^TS=sI+sL_{\mathcal G}^TL_{\mathcal G}-P^TP.
\tag{5.9}
\]

Since `T=sS^{-1}`, (5.9) also determines `TT^T`. Consequently **both** ordinary row- and column-Gram skeletons of `T` range over only `2^{o(r^2)}` possibilities.

This is a genuine entropy improvement at the skeleton level. The remaining difficulty is now entirely a common two-sided ternary root fiber with a giant flat singular plateau.

## 6. New theorem V — the low-rank defect is necessarily dense

Taking traces in (5.4) and using `tr(L_{\mathcal H}^TL_{\mathcal H})=d` gives

\[
\|T\|_F^2=2sd-\|Q\|_F^2.
\tag{6.1}
\]

Similarly

\[
\|S\|_F^2=2sd-\|P\|_F^2.
\tag{6.2}
\]

On the other hand, from `T=X+D/2`, `S^T=X-D/2`, and (4.2),

\[
\|T\|_F^2+\|S\|_F^2
=2sd+\|D\|_F^2.
\tag{6.3}
\]

Combining (6.1)--(6.3) yields the exact identity

\[
\boxed{
\|D\|_F^2
=2sd-\|Q\|_F^2-\|P\|_F^2.
}
\tag{6.4}
\]

Because `D` is ternary, `||D||_F^2` is exactly the number of nonzero entries. Since `P,Q` are `q x d` ternary matrices,

\[
\boxed{
2d(s-q)\le |\operatorname{supp}D|\le2sd.
}
\tag{6.5}
\]

In the entropy-dangerous regime `q=o(r)`, `d=r-q` and `s=r/4+O(1)`, so

\[
\boxed{
\frac{|\operatorname{supp}D|}{d^2}=\frac12+o(1).
}
\tag{6.6}
\]

Thus the rank-`o(r)` defect is **not sparse in entries**. It occupies asymptotically half of the core. Any intermediate reduction that attempts to delete only `o(r^2)` exceptional cells in order to obtain a genuine weighing matrix is therefore false for this sign-reconstructible core. The correct small object is algebraic rank / anchor complexity, not support size.

Despite being dense, the family of such defects has subquadratic entropy. A rank-`k` ternary `d x d` matrix is determined by `k` independent rows and, after choosing `k` pivot coordinates, each remaining ternary row has at most `3^k` possibilities. Hence

\[
\#\{D\in\{-1,0,1\}^{d\times d}:\operatorname{rank}D\le2q\}
\le 2^{O(qd+q\log d)}=2^{o(r^2)}.
\tag{6.7}
\]

So the defect itself is not the quadratic-entropy reservoir either.

## 7. New theorem VI — flat cofactors and Smith constraints

From the metric determinant identity and the matching block-size multisets,

\[
|\det T|=s^{d/2}.
\tag{7.1}
\]

Together with `T^{-1}=S/s`, this gives

\[
\boxed{
\operatorname{adj}(T)=\pm s^{d/2-1}S.
}
\tag{7.2}
\]

(When `d` is odd, the conclusions below force `s` to be a square, so the displayed quantity is still integral.) Therefore every cofactor of `T` belongs to the three-point set

\[
\boxed{
\{0,\ +s^{d/2-1},\ -s^{d/2-1}\}.
}
\tag{7.3}
\]

Let the Smith invariants of `T` be `alpha_1|...|alpha_d`. Since `sT^{-1}` is integral,

\[
\boxed{\alpha_i\mid s\quad\text{for every }i,}
\tag{7.4}
\]

while (7.1) gives

\[
\prod_i\alpha_i=s^{d/2}.
\tag{7.5}
\]

If `p^e || s` and `v_i=v_p(alpha_i)`, then `0<=v_i<=e` and

\[
\sum_i v_i=\frac{de}{2}.
\tag{7.6}
\]

Hence

\[
\boxed{\operatorname{rank}_{\mathbb F_p}(T)\le\lfloor d/2\rfloor.}
\tag{7.7}
\]

If `e=1`, necessarily `d` is even and exactly half the Smith invariants are divisible by `p`, so

\[
\boxed{p\parallel s\Longrightarrow \operatorname{rank}_{\mathbb F_p}(T)=d/2.}
\tag{7.8}
\]

If `d` is odd, (7.6) forces every prime exponent of `s` to be even:

\[
\boxed{d\text{ odd}\Longrightarrow s\text{ is a perfect square}.}
\tag{7.9}
\]

These are exact arithmetic certificates for any candidate root and require no invertibility assumption on the original cross block `C`; `T` itself is invertible because of (2.3)--(2.4).

## 8. What changed and what remains

The preceding run reduced the difficult sign-root fiber to a ternary metric-isometry problem. This run shows that a sign-reconstructible core has substantially more structure:

1. its scaled inverse is ternary (`TS=ST=sI`);
2. it differs from the transpose of that inverse by a ternary matrix `D` of rank at most `2q`;
3. its ordinary row and column Grams differ from `sI` in rank at most `2q`;
4. those ordinary Gram skeletons already have only `2^{o(r^2)}` entropy;
5. the low-rank defect `D` itself also has only `2^{o(r^2)}` entropy, but is necessarily dense on asymptotically half the cells;
6. the remaining fiber has a giant exact singular-value plateau and flat cofactor / Smith constraints.

Therefore the next missing theorem is no longer an arbitrary metric-similarity count. It is a **two-sided ternary root-fiber theorem** for matrices with

\[
T^TT=sI+sL^TL-Q^TQ,
\qquad
TT^T=sI+\text{rank-}O(q)\text{ defect},
\qquad
sT^{-1}\in\{-1,0,1\}^{d\times d},
\]

where `q=o(r)`, `d=r-q`, `s=r/4+O(1)`, and the inverse defect `T-(sT^{-1})^T` is a dense rank-`O(q)` cut matrix inherited from anchors.

A direct reduction to an exact weighing matrix by deleting a few bad entries is ruled out by (6.6). The next useful attacks are instead:

* classify low-rank cut matrices `D` together with the mixed-alphabet midpoint equation (4.2)--(4.4), seeking a contracting block recursion; or
* use the flat cofactor / Smith constraints to obtain anti-concentration inside a fixed ordinary two-sided Gram fiber.

The bounded-rank `q<=4` branch still contains Hadamard and D-optimal/weighing-matrix hardness and is not discarded. Higher shells, indefinite defects, and the passage from this two-eigenvalue family to general integral spectra remain open.

## 9. Literature boundary checked 20 September 2026

A bounded current search did not surface a resolution of Vu's exact Conjecture 9.4; this remains negative search evidence only, not an openness or novelty certificate.

Classical weighing matrices are ternary matrices `W` satisfying `WW^T=wI`; Hadamard matrices are the special case `w=n`. Existing weighing-matrix literature contains extensive existence and finite classification work, including group-developed families, but the present bounded search did not identify a general `2^{o(n^2)}` enumeration theorem at density `w/n` near `1/4`. The current result is therefore stated only as a project reduction/structural theorem, not as a claim that weighing-matrix enumeration is new.

Relevant background includes Arasu--Hollon, *Group Developed Weighing Matrices* (Australasian J. Combin. 55 (2013), 205--233) and the inherited Ferber--Jain--Zhao Hadamard anti-concentration boundary.
