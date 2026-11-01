# F0011 — good-cut mixed-energy reduction and hypercube-rich flag recursion

Status: **PROVED PARTIAL** toward Vu Conjecture 9.4, pending later independent review.  
Role: C05 / R7-06 `Random Matrix Spectral Entropy`  
Native ID: `6aabe827777c8191a43330b4a87d481d`  
Run-start master recovered earlier in this iteration: `6744ed3b560ec362b033ae20f4808a09093b8dc4`  
Fresh master before this artifact: `7f16bc305e95342ee559ef122904677994ca9306`

## 1. Outside source and inherited bottleneck

The outside target is Van H. Vu, *Recent progress in combinatorial random matrix theory*, Probability Surveys 18 (2021), Conjecture 9.4, Section 9 / PDF p. 15, arXiv:2005.02797, DOI 10.1214/20-PS346:

\[
\Pr\!\left(\operatorname{Spec}(M_n^{\rm sym})\subset\mathbb Z\right)
 = 2^{-(1/2+o(1))n^2},
\]

where the upper-triangular entries, including the diagonal, are independent fair signs and the matrix is filled symmetrically. Equivalently, the total number of labelled symmetric sign matrices with integral spectrum should be `2^{o(n^2)}`.

The current project boundary is the centered two-eigenvalue slice

\[
H=H^T\in\{\pm1\}^{2r\times 2r},\qquad H^2=2rI,\qquad \operatorname{tr}H=0.
\tag{1.1}
\]

For a balanced cut `S sqcup T=[2r]`, `|S|=|T|=r`, write

\[
H=\begin{pmatrix}P&C\\C^T&D\end{pmatrix},\qquad
K:=CC^T=2rI-P^2.
\tag{1.2}
\]

The previous report proved a uniform all-corank fixed-seed saving

\[
\log_2 \#\{(C,D)\mid P\}
 \le \left(\frac12-C_{30}+o(1)\right)r^2,
\qquad C_{30}\approx1.6118620\times10^{-5},
\tag{1.3}
\]

but also exhibited a `T=0` cut containing an arbitrary smaller Hadamard matrix. The missing issue was whether the endpoint is intrinsic to each completed matrix or merely an artifact of a bad cut, and how to turn near-saturation of the Odlyzko cube bound into a genuine recursive object.

This artifact proves two complementary structural theorems addressing exactly those points.

---

## 2. Exact balanced-cut mixed-energy average

Define the mixed energy of a balanced cut by

\[
\mathcal T(S):=\|PC\|_F^2.
\tag{2.1}
\]

From (1.2),

\[
\boxed{
\mathcal T(S)=\operatorname{tr}(K(2rI-K))
=2r^3-\operatorname{tr}(P^4).
}
\tag{2.2}
\]

Indeed `2rI-K=P^2`, so

\[
\operatorname{tr}(K(2rI-K))
=\operatorname{tr}(CC^TP^2)
=\operatorname{tr}(C^TP^2C)
=\|PC\|_F^2.
\]

We now average this quantity over all balanced cuts.

### Theorem 2.1 — exact average for an arbitrary diagonal imbalance

Let `H=H^T in {+-1}^{2r x 2r}` satisfy `H^2=2rI`, with `r>=2`, and put

\[
a:=\frac12\operatorname{tr}H.
\]

Thus `r+a` diagonal entries are `+1` and `r-a` are `-1`. If `S` is uniformly random among the `r`-subsets of `[2r]`, then

\[
\boxed{
\mathbb E_S\,\mathcal T(S)
=
\frac{r^4}{2r-1}
-
\frac{2a^2r(r-1)}{(2r-3)(2r-1)}.
}
\tag{2.3}
\]

In particular, on the centered fixed-spectrum branch `tr H=0`,

\[
\boxed{
\mathbb E_S\,\mathcal T(S)=\frac{r^4}{2r-1}.
}
\tag{2.4}
\]

#### Proof

Fix distinct indices `i,j` and condition on `i in S`, `j notin S`. Put

\[
d_i:=H_{ii},\qquad d_j:=H_{jj},\qquad
b_k:=H_{ik}H_{kj}.
\]

Because distinct rows `i,j` of `H` are orthogonal,

\[
\sum_{k=1}^{2r} b_k=0.
\tag{2.5}
\]

Moreover

\[
b_i=d_iH_{ij},\qquad b_j=d_jH_{ij}.
\tag{2.6}
\]

Conditional on the cross event, `S\setminus\{i\}` is a uniformly random `(r-1)`-subset of the remaining `2r-2` coordinates, exactly half of them, and

\[
(PC)_{ij}=b_i+\sum_{k\in S\setminus\{i\}}b_k.
\tag{2.7}
\]

Let `M=2r-2`. For a sample of size `M/2` without replacement from a `+-1` population of size `M` and total sum `B`, the sample-sum variance is

\[
\frac{M^2}{4(M-1)}\left(1-\frac{B^2}{M^2}\right).
\tag{2.8}
\]

If `d_i=d_j`, then `b_i=b_j`, the remaining population has total `B=-2b_i`, and (2.7) has mean zero. Hence

\[
\mathbb E\big[(PC)_{ij}^2\mid i\in S,j\notin S,d_i=d_j\big]
=
\boxed{\frac{r(r-2)}{2r-3}}.
\tag{2.9}
\]

If `d_i=-d_j`, then `b_j=-b_i`, the remaining population has total zero, and (2.7) has mean `b_i`. Therefore

\[
\mathbb E\big[(PC)_{ij}^2\mid i\in S,j\notin S,d_i=-d_j\big]
=
\boxed{\frac{r^2-2}{2r-3}}.
\tag{2.10}
\]

For every ordered pair `i ne j`,

\[
\Pr(i\in S,j\notin S)=\frac{r}{2(2r-1)}.
\tag{2.11}
\]

The number of ordered same-diagonal-sign pairs is

\[
(r+a)(r+a-1)+(r-a)(r-a-1)=2r(r-1)+2a^2,
\]

while the number of ordered opposite-sign pairs is

\[
2(r+a)(r-a)=2(r^2-a^2).
\]

Multiplying these counts by (2.9)-(2.11) and simplifying gives (2.3). Setting `a=0` gives (2.4). QED.

### Corollary 2.2 — the endpoint can be avoided at only linear entropy cost

Every centered matrix (1.1) has at least one balanced cut with

\[
\boxed{
\mathcal T(S)\ge\frac{r^4}{2r-1}.
}
\tag{2.12}
\]

There are only

\[
\binom{2r}{r}=2^{O(r)}
\]

balanced cuts. Consequently, if `A_{S_0}` denotes the centered matrices for which a fixed standard cut `S_0` satisfies (2.12), then permutation symmetry gives

\[
\boxed{
\#\{H\text{ satisfying }(1.1)\}
\le
\binom{2r}{r}\,|A_{S_0}|.
}
\tag{2.13}
\]

Thus a subquadratic count for the **good-cut** standard family closes the entire centered two-eigenvalue branch with only `2^{O(r)}` overhead. In particular, the `T=0` embedded-Hadamard construction from the previous report is not an unavoidable cut geometry: every completed centered matrix admits another balanced cut with macroscopic mixed energy.

### Corollary 2.3 — quantitative interior spectral mass

For a good cut satisfying (2.12), let `lambda_1,...,lambda_r in [0,2r]` be the eigenvalues of `K`. Since

\[
\mathcal T=\sum_i\lambda_i(2r-\lambda_i),
\]

at least

\[
\boxed{
q\ge
\frac{r(2r+7)}{9(2r-1)}
>
\frac r9
}
\tag{2.14}
\]

of the eigenvalues lie in

\[
\boxed{[r/4,\,7r/4]}.
\tag{2.15}
\]

Indeed outside this interval `lambda(2r-lambda)<=7r^2/16`, whereas it is always at most `r^2`; comparison with (2.12) gives (2.14).

Also

\[
\operatorname{tr}K^2
=2r^3-\mathcal T
\le
r^3\frac{3r-2}{2r-1},
\tag{2.16}
\]

so the effective rank obeys

\[
\boxed{
\frac{(\operatorname{tr}K)^2}{\operatorname{tr}K^2}
\ge
r\frac{2r-1}{3r-2}
=\left(\frac23+o(1)\right)r.
}
\tag{2.17}
\]

This is stronger information than mere nonsingularity: the selected cut has a linear-dimensional spectral bulk bounded away from both endpoints `0` and `2r`.

---

## 3. Hypercube-rich subspaces: exact saturation and sparse stability

For a real subspace `V<=R^n` of dimension `d`, define

\[
Q(V):=V\cap\{\pm1\}^n.
\]

Odlyzko's cube-intersection bound gives

\[
|Q(V)|\le2^d.
\tag{3.1}
\]

When `Q(V)` is nonempty define its deficiency

\[
\boxed{
\sigma(V):=d-\log_2|Q(V)|\ge0.
}
\tag{3.2}
\]

The next theorem identifies the equality case exactly and gives a quantitative structural statement near equality.

### Theorem 3.1 — equality classification

If `|Q(V)|=2^d`, then there is a surjection

\[
\phi:[n]\to[d]
\]

and signs `epsilon_j in {+-1}` such that

\[
\boxed{
V=\left\{v\in\mathbb R^n:
 v_j=\epsilon_j x_{\phi(j)}\text{ for some }x\in\mathbb R^d
\right\}.
}
\tag{3.3}
\]

Equivalently, after choosing `d` pivot coordinates, every coordinate functional on `V` is a signed copy of one pivot coordinate.

#### Proof

Choose `d` coordinate functionals whose restrictions to `V` form a basis of `V^*`; let `pi:V->R^d` be the corresponding coordinate projection. It is an isomorphism. On cube points it is injective and maps into `{+-1}^d`. Since both sets have cardinality `2^d`,

\[
\pi:Q(V)\longrightarrow\{\pm1\}^d
\]

is a bijection.

For any ambient coordinate `j`, write the corresponding functional in pivot coordinates as

\[
L_j(x)=\sum_{u=1}^d c_u x_u.
\]

Because every `x in {+-1}^d` lifts to a cube point of `V`, one has `L_j(x) in {+-1}` for every cube point `x`. Therefore `L_j(x)^2=1` identically on the discrete cube. Expanding in Walsh characters,

\[
L_j(x)^2
=
\sum_u c_u^2
+2\sum_{u<v}c_uc_v x_ux_v.
\]

All degree-two Fourier coefficients must vanish, hence `c_uc_v=0` for `u ne v`, and the constant coefficient gives `sum c_u^2=1`. Exactly one coefficient is nonzero and it equals `+-1`. This proves (3.3). QED.

### Theorem 3.2 — near equality forces sparse coordinate dependence

Suppose

\[
|Q(V)|\ge2^{d-s}
\tag{3.4}
\]

for some real `s>=0`. With the same choice of pivot coordinates as above, write an arbitrary ambient coordinate functional as

\[
L_j(x)=\sum_{u\in S_j}c_{j,u}x_u,
\qquad c_{j,u}\ne0.
\]

Then

\[
\boxed{
|S_j|\le \frac8\pi\,4^s
}
\tag{3.5}
\]

for every coordinate `j`.

#### Proof

Let `X=pi(Q(V))`. Then `|X|=|Q(V)|>=2^{d-s}` and `L_j(x) in {+-1}` for all `x in X`. Thus for a uniformly random `xi in {+-1}^d`,

\[
\Pr(L_j(\xi)\in\{\pm1\})\ge2^{-s}.
\tag{3.6}
\]

Let `m=|S_j|`. After absorbing coefficient signs into the independent Rademacher variables, the classical Erdos-Littlewood-Offord/Sperner atom bound gives, for every real `t`,

\[
\Pr(L_j(\xi)=t)
\le
2^{-m}\binom{m}{\lfloor m/2\rfloor}
\le
\sqrt{\frac{2}{\pi m}}.
\tag{3.7}
\]

Taking the union of the two target atoms `t=+-1`,

\[
2^{-s}
\le2\sqrt{\frac{2}{\pi m}},
\]

which rearranges to (3.5). QED.

The exact equality theorem is much stronger at `s=0`: it gives support one, whereas the deliberately uniform estimate (3.5) gives only a constant.

---

## 4. Hadamard-tail normal form and exact nested recursion

The preceding subspace theorem becomes directly relevant to Hadamard counting because every unfinished Hadamard row flag has a tail subspace containing an orthogonal sign basis.

### Theorem 4.1 — sparse Gram-root normal form

Let `V<=R^n` have dimension `d`, suppose (3.4) holds, and suppose `V` contains an ordered orthogonal sign basis. Equivalently there is a matrix

\[
R\in\{\pm1\}^{d\times n},\qquad RR^T=nI_d,
\tag{4.1}
\]

whose row space is `V`.

Choose the pivot coordinates used in Theorem 3.2 and permute columns so that they come first. Then

\[
\boxed{
R=Y\,[I_d\ A],
}
\tag{4.2}
\]

where

* `Y in {+-1}^{d x d}` is invertible;
* every column of `A` has support at most `(8/pi)4^s`;
* orthogonality is equivalent to the exact sign-Gram equation

\[
\boxed{
Y^TY=n\,(I_d+AA^T)^{-1}.
}
\tag{4.3}
\]

#### Proof

The pivot block `Y` records the pivot coordinates of the `d` orthogonal sign rows and is invertible because pivot projection is an isomorphism on `V`. Every nonpivot coordinate is a linear functional of the pivot coordinates, so its column across the `d` rows is `Ya_j`; collecting these coefficient vectors gives (4.2). The support bound is Theorem 3.2.

From `RR^T=nI`,

\[
Y(I_d+AA^T)Y^T=nI.
\]

Since `Y` is square and invertible, if `G=I_d+AA^T`, then `YG^{1/2}` is a square matrix with row Gram `nI`, hence also column Gram `nI`. Therefore

\[
G^{1/2}Y^TYG^{1/2}=nI,
\]

which is exactly (4.3). QED.

Equation (4.3) is the promised bridge to the existing F0011 Gram-fiber machinery: **near-maximal cube intersection converts the Hadamard tail into a square sign-Gram-root problem whose coefficient matrix is column-sparse**.

### Corollary 4.2 — exact saturation is literal smaller-order Hadamard recursion

Under the hypotheses of Theorem 4.1, assume `sigma(V)=0`. Then `d` divides `n`; after the same coordinate normalization, the `n` coordinates split into `d` signed groups of equal size `n/d`, and

\[
\boxed{Y^TY=dI_d.}
\tag{4.4}
\]

Thus `Y` is a Hadamard matrix of order `d`. Conversely every Hadamard matrix `Y` of order `d` lifts through the fixed signed coordinate groups to an orthogonal sign basis of `V`.

Hence, for a fixed saturated tail subspace `V`, the ordered tail completions are in bijection with order-`d` Hadamard matrices.

#### Proof

By Theorem 3.1, every nonpivot coefficient column of `A` is a signed standard basis vector. Let `m_u` be the number of ambient coordinates belonging to group `u`, including pivot `u`. Then

\[
I+AA^T=\operatorname{diag}(m_1,\ldots,m_d).
\]

Equation (4.3) gives

\[
Y^TY=n\operatorname{diag}(m_1^{-1},\ldots,m_d^{-1}).
\]

The diagonal of `Y^TY` is identically `d`, because every column of `Y` has `d` signs. Therefore `m_u=n/d` for every `u`; in particular `d|n`. The off-diagonal entries vanish and (4.4) follows. The converse is immediate by repeating each Hadamard coordinate `n/d` times with the fixed group sign. QED.

### Corollary 4.3 — a Hadamard row flag has an entropy-versus-recursion dichotomy

Let `w_1,...,w_n` be ordered rows of an `n x n` Hadamard matrix and

\[
V_k:=\operatorname{span}(w_1,\ldots,w_k)^\perp,
\qquad d=n-k.
\]

At the next extension there are exactly `|Q(V_k)|` candidate sign rows before the remaining orthogonality constraints, so Odlyzko's bound can be written as

\[
|Q(V_k)|=2^{d-\sigma(V_k)}.
\tag{4.5}
\]

Thus every flag step either pays the explicit entropy deficit `sigma(V_k)`, or, when that deficit is small, Theorem 4.1 forces the remaining tail into a sparse Gram-root normal form. If `sigma(V_k)=0`, the tail is not merely structured: it **recurses exactly to an order-`d` Hadamard completion problem**.

This is the structural mechanism absent from the previous one-shot spectral-profile bound.

---

## 5. Consequence for the previous endpoint obstruction

The previous report showed that one particular balanced cut can have `T=0` and can encode an arbitrary smaller Hadamard matrix. Theorems 2.1-2.3 and 4.1-4.3 refine that obstruction in two complementary ways:

1. **Cut selection removes the exact endpoint.** Every centered completed matrix has some balanced cut with `T >= r^4/(2r-1)` and hence a linear-dimensional spectral bulk in the interior of the Gram cone. Passing to a canonical good cut costs only `2^{O(r)}` labels.
2. **If a row-flag subspace is instead hypercube-rich, it becomes recursive.** Exact saturation is literally a smaller Hadamard problem, while near saturation gives the sparse coefficient/Gram-root representation (4.2)-(4.3).

Therefore the remaining centered-branch problem is no longer correctly described as "control arbitrary singular Gram fibers." A more precise formulation is:

> Count the standard-good-cut family with `T >= r^4/(2r-1)`, while recursively compressing any row-flag stage for which the Odlyzko cube deficit is small.

A proof that the accumulated deficits are `(1/2-o(1))n^2`, except on recursively compressible branches whose total description length is `o(n^2)`, would give the desired `2^{o(n^2)}` count for the centered two-eigenvalue slice.

---

## 6. What is and is not proved

**Proved here (project deductions):**

* the exact balanced-cut mixed-energy expectation (2.3), including the centered identity (2.4);
* good-cut reduction (2.13), paying only linear entropy;
* a good cut has more than `r/9` Gram eigenvalues in `[r/4,7r/4]` and effective rank asymptotically at least `2r/3`;
* equality classification for the `2^d` Odlyzko cube-intersection bound;
* quantitative near-saturation sparsity `support <= (8/pi)4^s`;
* the sparse Hadamard-tail Gram-root normal form (4.2)-(4.3);
* exact recursion to order-`d` Hadamard completions at zero deficiency.

**Not proved:**

* `2^{o(n^2)}` for Hadamard matrices or symmetric Hadamard matrices;
* `2^{o(n^2)}` even for the whole centered two-eigenvalue F0011 slice;
* a stability theorem counting all sparse `(A,Y)` pairs in (4.3) with subquadratic entropy;
* any reduction from arbitrary integral spectra to the two-eigenvalue branch;
* Vu Conjecture 9.4 itself.

No external novelty claim is made. Odlyzko's cube-intersection inequality and Erdos-Littlewood-Offord anti-concentration are classical inputs; the equality/stability/Gram-recursion and balanced-cut deductions above are recorded as internal project mathematics pending independent comparison and review.

---

## 7. Literature boundary checked in this iteration

The canonical source remains Vu, arXiv:2005.02797 / Probability Surveys 18 (2021), Conjecture 9.4. A bounded 20 September 2026 search did not surface a proof of the exact integral-spectrum asymptotic; this is negative search evidence only.

Relevant established inputs/boundaries:

* A. M. Odlyzko, *On the ranks of some (0,1)-matrices with constant row sums* (1981): a `d`-dimensional real subspace contains at most `2^d` Boolean cube vertices (equivalently after affine/sign translation for the sign cube).
* A. M. Odlyzko, *On subspaces spanned by random selections of +/-1 vectors* (1988): random sign spans typically acquire very few additional cube points in a broad range; this is context rather than a theorem used in the proofs above.
* Ferber-Jain-Zhao, *On the number of Hadamard matrices via anti-concentration* (2022): current general Hadamard enumeration gives a constant quadratic improvement, while `2^{o(n^2)}` is explicitly identified as requiring major new ideas.
* Tuomo Valtonen, *Classification of Symmetric Hadamard Matrices Up to Order 32* (arXiv:2608.06920, 2026): finite classification, not an asymptotic count.

---

## 8. Next concrete attack

The strongest next lemma is now sharply specified.

**Sparse-tail counting lemma.** For `R=Y[I A]` satisfying (4.3), prove that if every column of `A` has support `n^{o(1)}`, then either

1. the number of possible `(A,Y)` pairs is `2^{o(n^2)}` after the already-paid prefix entropy, or
2. `A` contains a macroscopic block decomposition which yields two or more strictly smaller Hadamard/Gram-root instances whose quadratic dimensions contract.

This would turn the entropy-versus-recursion dichotomy into an actual recurrence rather than another constant improvement. In parallel, the good-cut constraint (2.12) should be imposed from the start so that the exact `T=0` endpoint never needs to be counted on the selected cut.
