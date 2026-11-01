# F0012 recovery 2 — exact cube-zero counting and the low-second-rank half-exponent theorem

Target: Vu Conjecture 9.5 recovery after the source-level refutation.  
Restricted recovery object: sign matrices `A in {+1,-1}^{n x n}` satisfying `A^3=0`.  
Methods used: **B6 deform to a solved point / B20 isolate why the algorithm fails / B27 swap quantifiers**.

The source conjecture is already refuted by the earlier R7-07 block-shear family. The purpose here is to attack the corrected candidate exponent `1/2` inside the nilpotent fiber. The previous run proved the full `A^2=0` stratum has cardinality at most `2^{n^2/2+O(n)}`. This note deforms that proof to `A^3=0` and obtains a complete half-exponent theorem whenever `rank(A^2)` is sublinear on the `n/log n` scale.

## 1. Setup

For integers `0 <= s <= r <= n`, define

\[
\mathcal N_3(n;r,s)
=
\{A\in\{\pm1\}^{n\times n}:A^3=0,\ \operatorname{rank}A=r,\ \operatorname{rank}A^2=s\}.
\]

For any member of this set, the kernel increments are

\[
b_1=n-r,\qquad b_2=r-s,\qquad b_3=s.
\]

They are nonincreasing, so necessarily

\[
s\le r/2,\qquad r-s\le n-r,
\qquad\text{hence}\qquad r\le\frac{n+s}{2}.
\tag{1}
\]

The second inequality also follows directly from
`im(A) cap ker(A)` having dimension `r-s` and lying in `ker(A)`.

We repeatedly use the elementary affine-hypercube lemma:

> If `L` is an affine subspace of `R^N` of affine dimension `d`, then
> \[
> |L\cap\{\pm1\}^N|\le 2^d.
> \]

Indeed, select `d` coordinate functionals whose restrictions are a basis of the dual of the direction space; projection to those coordinates is injective on `L`.

## 2. B6 — exact deformation of the square-zero reveal

### Theorem 2.1 (rank-refined cube-zero count)

For every feasible `n,r,s`,

\[
\boxed{
|\mathcal N_3(n;r,s)|
\le
\binom nr^2\binom rs^2
(n+1)^{2rs-s^2}
2^{\,2nr-2r^2+rs}.
}
\tag{2}
\]

For `s=0`, this reduces exactly to the preceding square-zero estimate

\[
|\mathcal N_3(n;r,0)|
\le
\binom nr^2 2^{2r(n-r)}.
\tag{3}
\]

Thus (2) is a literal deformation of the solved `A^2=0` counting argument, not a different unrelated bound.

### Proof

Fix `A in mathcal N_3(n;r,s)`.
Choose row and column index sets `I,J subset [n]`, each of size `r`, such that

\[
B=A_{I,J}
\]

is nonsingular. There are at most `binom(n,r)^2` choices. Put

\[
R=A_{I,*}\in\{\pm1\}^{r\times n},
\qquad
C=A_{*,J}\in\{\pm1\}^{n\times r}.
\]

Then `R` and `C` have rank `r`, `C_{I,*}=B`, and the exact CUR identity gives

\[
A=C B^{-1}R.
\tag{4}
\]

There are at most `2^{rn}` possibilities for `R`; after `R` and `J` are fixed, `B=R_{*,J}` is fixed as well.

Define the middle product

\[
G=RC=(A^2)_{I,J}\in\mathbf Z^{r\times r}
\tag{5}
\]

and

\[
T=B^{-1}G.
\tag{6}
\]

Using (4),

\[
A^2=C B^{-1}G B^{-1}R=C T B^{-1}R,
\tag{7}
\]

so left multiplication by the full-column-rank matrix `C` and right multiplication by the full-row-rank matrix `B^{-1}R` preserve rank. Hence

\[
\operatorname{rank}G
=
\operatorname{rank}T
=
\operatorname{rank}A^2
=s.
\tag{8}
\]

Likewise,

\[
A^3
=C(B^{-1}G)^2B^{-1}R
=C T^2 B^{-1}R.
\tag{9}
\]

Again the outer factors have full rank, so

\[
A^3=0
\quad\Longleftrightarrow\quad
T^2=0.
\tag{10}
\]

This is the exact middle-matrix reduction.

### 2.1 The cube-zero condition forces a large projection of `ker R`

Let `pi_I:R^n -> R^I` denote coordinate projection and set

\[
q=\dim \pi_I(\ker R).
\tag{11}
\]

Since `T^2=0` and `rank T=s`,

\[
\dim\ker T=r-s.
\tag{12}
\]

For every `v in ker T`,

\[
R(Cv)=Gv=BTv=0,
\]

so `Cv in ker R`. But on the coordinates `I`,

\[
\pi_I(Cv)=C_{I,*}v=Bv.
\tag{13}
\]

Because `B` is invertible, `B(ker T)` has dimension `r-s`. Therefore

\[
\boxed{q\ge r-s.}
\tag{14}
\]

This is the exact replacement for the square-zero fact `q=r`.

### 2.2 Counting `C` once `R` and `G` are fixed

Fix `R` and a possible `G`. For the `j`th selected basis column `c_j` of `C`, both

\[
(c_j)_I=B_{*,j}
\qquad\text{and}\qquad
R c_j=G_{*,j}
\tag{15}
\]

are fixed.

If `c_j,c'_j` are two real solutions, their difference `h` lies in

\[
V_R=\{h\in\ker R:h_I=0\}.
\tag{16}
\]

Now `dim ker R=n-r`, and the kernel of `pi_I|_{ker R}` is exactly `V_R`, so by rank-nullity

\[
\dim V_R=(n-r)-q
\le n-r-(r-s)
=n-2r+s.
\tag{17}
\]

Thus the affine solution space for each sign column has dimension at most `n-2r+s`, and the affine-hypercube lemma gives at most

\[
2^{n-2r+s}
\]

choices per column. The `r` columns are constrained separately once `G` is fixed, hence

\[
\#\{C:C_I=B,\ RC=G,\ C\in\{\pm1\}^{n\times r}\}
\le
2^{r(n-2r+s)}.
\tag{18}
\]

Notice that feasibility itself implies `n-2r+s>=0`, in agreement with (1).

### 2.3 Counting the possible integer middle matrices `G`

Every entry of `G=RC` is a sum of `n` signs, so it belongs to

\[
\{-n,-n+2,\dots,n-2,n\},
\]

a set of exactly `n+1` integers.

A rank-`s` `r x r` matrix is determined by any nonsingular `s x s` minor together with the corresponding `s` full rows and `s` full columns. More precisely, choose `P,Q subset[r]` of size `s` with `G_{P,Q}` invertible. Then

\[
G=G_{*,Q}(G_{P,Q})^{-1}G_{P,*}.
\tag{19}
\]

The union of the exposed row and column entries has cardinality

\[
sr+rs-s^2=2rs-s^2.
\]

Therefore

\[
\#\{G:\operatorname{rank}G=s,\ G_{ab}\in\{-n,-n+2,\ldots,n\}\}
\le
\binom rs^2 (n+1)^{2rs-s^2}.
\tag{20}
\]

We have deliberately ignored the additional equation `T^2=0` in (20), so this remains an upper bound.

Combining the choices of `(I,J)`, `R`, `G`, and then `C`, and using (4) to reconstruct `A` uniquely, gives

\[
\begin{aligned}
|\mathcal N_3(n;r,s)|
&\le
\binom nr^2
2^{rn}
\binom rs^2(n+1)^{2rs-s^2}
2^{r(n-2r+s)}\\
&=
\binom nr^2\binom rs^2
(n+1)^{2rs-s^2}
2^{2nr-2r^2+rs},
\end{aligned}
\]

which is (2). QED.

## 3. B27 — swap the quantifiers and solve a uniform mesoscopic regime

The point of (2) is not a fixed `(r,s)` estimate. It becomes useful after swapping the order of attack: instead of trying every three-step Jordan profile separately, first prove the half exponent uniformly over every profile with sufficiently small second rank.

### Theorem 3.1 (uniform low-second-rank half exponent)

Let `s_n` be any integer sequence satisfying

\[
s_n\log n=o(n).
\tag{21}
\]

Then

\[
\boxed{
\#\{A\in\{\pm1\}^{n\times n}:A^3=0,\ \operatorname{rank}A^2\le s_n\}
\le
2^{n^2/2+o(n^2)}.
}
\tag{22}
\]

In particular,

\[
\boxed{
\#\{A:A^3=0,\ \operatorname{rank}A^2\le n/(\log n)^2\}
\le
2^{n^2/2+O(n^2/\log n)}.
}
\tag{23}
\]

### Proof

For fixed `s`, the binary exponent in (2) is

\[
h(r,s)=2nr-2r^2+rs.
\tag{24}
\]

Complete the square:

\[
\boxed{
h(r,s)
=-2\left(r-\frac n2-\frac s4\right)^2
+\frac{n^2}{2}+\frac{ns}{2}+\frac{s^2}{8}.
}
\tag{25}
\]

Therefore, uniformly in `r`,

\[
h(r,s)\le
\frac{n^2}{2}+\frac{ns}{2}+\frac{s^2}{8}.
\tag{26}
\]

The integer-middle-matrix term contributes

\[
(2rs-s^2)\log_2(n+1)
\le 2ns\log_2(n+1).
\tag{27}
\]

The binomial factors contribute only `O(n)` bits, and summing over at most `n^2` pairs `(r,s)` costs only `O(log n)` additional bits.

If `s<=s_n` and `s_n log n=o(n)`, then both `ns=o(n^2)` and `ns log n=o(n^2)`. Equations (26)-(27) therefore give

\[
\log_2 \#\{A:A^3=0,\operatorname{rank}A^2\le s_n\}
\le
\frac{n^2}{2}+o(n^2),
\]

proving (22). Taking `s_n=n/(log n)^2` gives the explicit error in (23). QED.

### Consequences

1. The entire square-zero stratum `s=0` is recovered.
2. Every fixed second rank `s=O(1)` has the corrected half exponent.
3. More generally every `s=o(n/log n)` is controlled uniformly.
4. Hence any cube-zero family capable of violating the candidate `1/2` exponent must satisfy
   \[
   \operatorname{rank}(A^2)\not=o(n/\log n).
   \]
   In particular the unresolved obstruction has genuinely mesoscopic/macroscopic second rank.

This is a real restriction on a potential counterfamily; it is not a source-level improvement of `u_GI` because the full nilpotent fiber, and even the full `A^3=0` fiber, still contains the unresolved range `rank(A^2) >> n/log n`.

## 4. B20 — exact point where the reveal algorithm fails

The deformation proof identifies the obstruction quantitatively.

For `A^2=0`, the middle matrix is `G=0`. No middle-state entropy is paid, and the basis-column fibers have dimension `n-2r`.

For `A^3=0`, the same reveal leaves a rank-`s` integer matrix

\[
G=(A^2)_{I,J}=RC,
\]

with entries in an alphabet of size `n+1`. Once `G` is fixed, the affine fibers are still small enough: the new binary cost relative to `s=0` is only `rs`. The obstruction is the naive enumeration

\[
\boxed{
\log_2 \#G
\le
(2rs-s^2)\log_2(n+1)+O(n),
}
\tag{28}
\]

which is harmless when `s log n=o(n)` but becomes `Theta(n^2 log n)` when `s=Theta(n)`.

This `log n` loss is not intrinsic algebraic dimension: the rank-`s` determinantal variety has only `2rs-s^2` continuous degrees of freedom. It appears because every degree of freedom was encoded by one integer in an interval of length `Theta(n)`. A successful extension to linear `s` therefore needs a **binary-entropy bound for attainable middle matrices `G=RC`**, exploiting both that `R,C` are sign matrices and that

\[
(B^{-1}G)^2=0,
\tag{29}
\]

rather than enumerating arbitrary bounded integer rank-`s` matrices.

That is the exact algorithmic failure, and it is sharper than the previous statement that `A^3=0` merely introduces an “intermediate map.” The missing ingredient is now a quantitative compression theorem for the attainable middle product.

## 5. Relation to the full F0012 recovery

The original source event is

\[
E_n=\{\operatorname{Spec}(M_n)\subset\mathbf Z[i]\}.
\]

Earlier R7-07 work already refuted Vu's proposed exponent `1` by constructing `2^{n^2/2+O(n)}` exceptional sign matrices, so the fixed source metric remains

\[
0\le u_{GI}\le\frac12.
\]

This note does **not** improve that interval. It advances the selected post-STUCK1 nilpotent-fiber recovery by proving the candidate half exponent for a uniform, growing family of nilpotency-index-three profiles.

The full recovery target

\[
N_0(n)=\#\{A\in\{\pm1\}^{n\times n}:\chi_A(x)=x^n\}
\le2^{n^2/2+o(n^2)}
\]

remains open in this work. Even the complete `A^3=0` count remains open in the linear-second-rank range.

## 6. Next attack suggested by the obstruction

The next nonrepeating methods should target (28) directly rather than add another Jordan-profile lemma:

- **B11 (dualize):** Fourier-expand the distribution of the middle product `G=RC` and seek a rank-sensitive entropy/anti-concentration bound that counts attainable `G` without paying `log n` per scalar entry.
- **B28 (typical instead of all):** split row bases `R` into anti-concentrated typical bases and structured exceptional bases; prove the typical class already has middle-product entropy `2^{O(rs)}`.
- **B24 (extremal object):** classify row spaces `H` for which many sign vectors lie in fibers of `R`; exact equality in the subspace-hypercube bound forces coordinate-duplication structure, suggesting a stability theorem for near-extremizers.

The desired bridge is a statement of the schematic form

\[
\#\{G=RC:\ C\in\{\pm1\}^{n\times r},\ \operatorname{rank}G=s,\ (B^{-1}G)^2=0\}
\le 2^{O(rs)+o(n^2)},
\]

uniformly in the relevant row bases `R`. Proving such a bound with a sufficiently small constant would remove the only `log n` loss in Theorem 2.1 and reach the genuinely linear-`s` regime.

## 7. Status

- Source-level Vu Conjecture 9.5: **REFUTED** by earlier R7-07 work.
- Frozen source metric `u_GI`: **NO MOVEMENT**, still `[0,1/2]`.
- Post-STUCK1 recovery target: **PARTIAL**.
- New proved result: rank-refined exact count (2), including the uniform theorem (22)-(23).
- No claim that the full nilpotent fiber or the corrected exponent `u_GI=1/2` is proved.
- Novelty of these restricted counting lemmas: **UNVERIFIED**; bounded literature searches did not surface a direct prior count for nilpotent `{+1,-1}` matrices, which is negative evidence only.
