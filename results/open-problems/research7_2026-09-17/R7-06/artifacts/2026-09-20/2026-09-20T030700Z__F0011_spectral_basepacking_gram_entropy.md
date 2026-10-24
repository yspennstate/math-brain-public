Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated binding model/effort selector or runtime telemetry is exposed.

# F0011 — spectral base-packing and inhomogeneous Gram-fiber entropy

Date: 2026-09-20 UTC  
Role: C05 / R7-06, native ID `6aabe827777c8191a43330b4a87d481d`  
Canonical target: Van H. Vu, *Recent progress in combinatorial random matrix theory*, Probability Surveys 18 (2021), Conjecture 9.4  
Status: **PROVED PARTIAL**, pending later independent review. Nothing below proves the full source conjecture.

## 1. Source target and inherited bridge

For the symmetric Rademacher matrix `M_n^sym`, whose diagonal and upper-triangular entries are independent fair signs and whose lower triangle is filled by symmetry, Vu's Conjecture 9.4 asks for

\[
\Pr\!\left(\operatorname{Spec}(M_n^{\rm sym})\subset\mathbb Z\right)
 =2^{-(1/2+o(1))n^2}.
\]

Equivalently, since there are `2^{n(n+1)/2}` labelled symmetric sign matrices, source closure requires a total integral-spectrum count `2^{o(n^2)}`.

The current R7-06 two-eigenvalue boundary writes `N=2r` and

\[
H=\begin{pmatrix}P&C\\ C^T&D\end{pmatrix}=H^T\in\{\pm1\}^{N\times N},
\qquad H^2=NI_N.
\]

Then
\[
P^2+CC^T=NI_r,\qquad PC+CD=0,\qquad C^TC+D^2=NI_r.
\]
For a fixed symmetric sign seed `P`, put
\[
K:=NI_r-P^2=CC^T.
\]
Earlier C05 work reduced low-corank singular cuts to positive sign-Gram fibers at subquadratic overhead, proved determinant/seed coupling, classified the first local Gram trades, and obtained uniform small-row entropy loss plus a Walsh/bent-function theorem for one exact maximum-volume cross class. The remaining bridge is a genuinely global bound on arbitrary fixed Gram fibers and, ultimately, a coupling to the seed entropy.

This note gives two all-dimensional results. First, it gives a clean rank-adaptive bound that includes every singular Gram fiber and exactly matches the worst endpoint affine freedom. Second, it transfers the Ferber-Jain-Zhao inhomogeneous anti-concentration theorem from the orthogonal/Hadamard setting to **every uniformly well-conditioned positive sign Gram fiber** by proving a spectral base-packing lemma.

## 2. Rank-adaptive affine-cube bound, including singular Gram matrices

For a positive-semidefinite matrix `K` admitting a square sign root, define
\[
\mathcal R(K):=\{C\in\{\pm1\}^{r\times r}:CC^T=K\},
\qquad \rho:=\operatorname{rank}K.
\]

### Lemma 2.1 — affine cube sections

If an affine subspace `L subset R^r` has dimension `d`, then
\[
|L\cap\{\pm1\}^r|\le 2^d.
\]

**Proof.** Choose `d` coordinate functionals whose restrictions to the direction space of `L` are linearly independent. Projection to these `d` coordinates is injective on `L`; cube points have only `2^d` projected sign patterns. ∎

### Theorem 2.2 — rank-adaptive sign-Gram fiber bound

For every such `K`, singular or nonsingular,
\[
\boxed{
|\mathcal R(K)|
\le
2^{\rho r-\binom{\rho}{2}}
=2^{\rho(2r-\rho+1)/2}.
}
\tag{2.1}
\]

**Proof.** Fix once and for all from `K` an ordered set of row indices `I=(i_1,...,i_\rho)` for which the principal Gram matrix `K_{I,I}` is positive definite; for definiteness take the lexicographically first such set. In every root `C`, these selected rows are linearly independent. All remaining rows are uniquely determined once the selected rows are known: if `j notin I`, then the coefficient vector expressing row `R_j` in the selected basis is the unique solution of
\[
\alpha_j K_{I,I}=K_{j,I},
\]
hence depends only on `K`.

Expose the selected basis rows sequentially. Before choosing `R_{i_s}`, its inner products with the preceding `s-1` selected rows are fixed by `K`. Since those preceding rows are independent, these are `s-1` independent affine linear equations in `r` coordinates. Therefore `R_{i_s}` lies in an affine space of dimension `r-s+1`, and Lemma 2.1 gives at most `2^{r-s+1}` sign choices. Multiplying for `s=1,...,rho` proves
\[
|\mathcal R(K)|\le\prod_{s=1}^{\rho}2^{r-s+1}
=2^{\rho r-\rho(\rho-1)/2}.
\]
All dependent rows are already forced. ∎

For `rho=r`, (2.1) is the familiar Odlyzko-scale `2^{r(r+1)/2}` bound. The point here is the exact rank dependence at the singular endpoint.

### Corollary 2.3 — singular half-completions never exceed the same half-triangular baseline

Fix a seed `P` in the two-eigenvalue block problem and suppose
\[
K=NI-P^2
\]
has rank `rho=r-k`. Previous C05 work proved that for fixed `(P,C)`, symmetric solutions `D` of `PC+CD=0` lie in an affine space of dimension at most `binom(k+1,2)`, hence there are at most `2^{binom(k+1,2)}` sign choices for `D`. Combining this with (2.1),
\[
\begin{aligned}
\#\{(C,D):\text{complete this fixed }P\}
&\le
2^{\rho r-\binom\rho2}\,2^{\binom{k+1}{2}}\\
&=\boxed{2^{r(r+1)/2}}.
\end{aligned}
\tag{2.2}
\]
The identity in the exponent follows from `rho=r-k`.

This includes **all coranks** and does not assume distinct nonzero singular values. It also shows exactly why rank loss alone cannot solve the singular endpoint: the entropy saved in choosing `C` can be canceled, at this level of information, by the endpoint affine freedom in `D`. Any further singular improvement must use the sign/quadratic equations on that endpoint freedom, not merely its dimension.

## 3. Spectral base-packing

The next theorem addresses positive `K`. The key observation is that a lower spectral edge forces the coefficient columns in every partial-row system to contain several disjoint spanning sets, exactly the hypothesis needed by the strongest simple Ferber-Jain-Zhao atom bound.

### Lemma 3.1 — spectral base-packing

Let `A` be an `m x r` sign matrix satisfying
\[
\lambda_{\min}(AA^T)\ge \gamma r,
\qquad 0<\gamma\le1.
\]
Then the `r` columns of `A` contain at least
\[
\boxed{\left\lfloor\frac{\gamma r}{m}\right\rfloor}
\tag{3.1}
\]
pairwise disjoint bases of `R^m`.

**Proof.** Let the columns be `a_1,...,a_r`. For any subspace `W<=R^m` of dimension `d`,
\[
\sum_{j=1}^r\|P_{W^\perp}a_j\|_2^2
=\operatorname{tr}(P_{W^\perp}AA^T)
\ge \gamma r(m-d).
\tag{3.2}
\]
Each sign column has squared norm `m`, so every summand is at most `m`; a column lying in `W` contributes zero. Hence the number of columns outside `W` is at least
\[
\frac{\gamma r}{m}(m-d).
\tag{3.3}
\]
Put `q=floor(gamma r/m)`. Then for every `W`, at least `q(m-d)` columns lie outside `W`. The vector-matroid base-packing criterion (equivalently, Edmonds' disjoint-bases criterion applied to the column matroid) says precisely that this condition for all flats is equivalent to the existence of `q` pairwise disjoint bases. ∎

No randomness is used in Lemma 3.1.

## 4. Uniformly well-conditioned positive Gram fibers have a quadratic entropy penalty

We import one published inequality only. Ferber, Jain and Zhao, *On the number of Hadamard matrices via anti-concentration*, Combin. Probab. Comput. 31 (2022), Theorem 1.10, prove the following inhomogeneous atom bound. If coefficient vectors `a_1,...,a_r in R^m` can be partitioned into an even number `ell` of blocks whose spanning ranks are `r_1,...,r_ell`, then for independent Rademacher signs `epsilon_j`,
\[
\sup_u\Pr\!\left(\sum_j\epsilon_j a_j=u\right)
\le
\left(2^{-\ell}\binom{\ell}{\ell/2}\right)^{(r_1+\cdots+r_\ell)/\ell}.
\tag{4.1}
\]
For `ell=4` and four full-rank blocks this is `(3/8)^m`. The published theorem is uniform in the inhomogeneous target `u`, which is essential here because fixed-Gram row extension asks for `Ax=b`, not merely `Ax=0`.

### Theorem 4.1 — spectral lower edge implies fixed-Gram entropy loss

Let `K>0` be an `r x r` sign Gram matrix and suppose
\[
\lambda_{\min}(K)\ge\gamma r,
\qquad 0<\gamma\le1.
\tag{4.2}
\]
Set
\[
M:=\left\lfloor\frac{\gamma r}{4}\right\rfloor.
\]
Then
\[
\boxed{
|\mathcal R(K)|
\le
2^{r(r+1)/2}\left(\frac34\right)^{M(M+1)/2}.
}
\tag{4.3}
\]
Consequently
\[
\boxed{
\log_2|\mathcal R(K)|
\le
\left(\frac12-c_*\gamma^2\right)r^2+O_\gamma(r),
\qquad
c_*:=\frac{\log_2(4/3)}{32}>0.
}
\tag{4.4}
\]
Numerically `c_*≈0.01297`.

**Proof.** Expose a root `C` row by row. Suppose the first `m` rows have been exposed, and let `A_m` be the resulting `m x r` matrix. The next row `x in {+-1}^r` must solve
\[
A_mx=b_m,
\tag{4.5}
\]
where `b_m` is the vector of prescribed Gram entries from `K`.

Because `A_mA_m^T` is the leading `m x m` principal submatrix of `K`, Cauchy interlacing gives
\[
\lambda_{\min}(A_mA_m^T)\ge\lambda_{\min}(K)\ge\gamma r.
\tag{4.6}
\]
For `1<=m<=M`, Lemma 3.1 supplies at least four pairwise disjoint bases among the columns of `A_m`. Put one basis in each of four blocks and distribute all remaining columns arbitrarily among those blocks. Each block still has rank `m`. Applying (4.1) with `ell=4`,
\[
\#\{x\in\{\pm1\}^r:A_mx=b_m\}
\le 2^r\left(\frac38\right)^m
=2^{r-m}\left(\frac34\right)^m.
\tag{4.7}
\]
For all other `m`, the affine cube-section/Odlyzko bound gives at most `2^{r-m}` choices because the first `m` rows are independent (`K>0`). Multiplying the row-extension bounds for `m=0,...,r-1` yields
\[
|\mathcal R(K)|
\le
\left(\prod_{m=0}^{r-1}2^{r-m}\right)
\prod_{m=1}^{M}\left(\frac34\right)^m
=
2^{r(r+1)/2}\left(\frac34\right)^{M(M+1)/2}.
\]
Since `M=gamma r/4+O(1)`, taking binary logarithms gives (4.4). ∎

### Corollary 4.2 — a fixed-seed half-completion theorem away from the soft edge

In the two-eigenvalue block problem, suppose
\[
K=2rI-P^2>0
\]
and
\[
\|P\|_{\rm op}^2\le(2-\gamma)r.
\tag{4.8}
\]
Then `lambda_min(K)>=gamma r`; moreover `C` is invertible and `D=-C^{-1}PC` is forced. Hence the number of sign completions of this fixed `P` is at most the right side of (4.3):
\[
\boxed{
\#\{(C,D):H^2=2rI\text{ with this }P\}
\le
2^{r(r+1)/2}\left(\frac34\right)^{M(M+1)/2}.
}
\tag{4.9}
\]
This works for arbitrary positive Gram `K`, not only the Hadamard point `K=rI`.

## 5. An inverse consequence: any near-extremal Gram fiber must approach the spectral soft edge

Theorem 4.1 immediately localizes a possible quadratic-entropy obstruction. Suppose a sequence of positive sign Gram matrices `K_r` has
\[
\log_2|\mathcal R(K_r)|
\ge\left(\frac12-\varepsilon_r\right)r^2
\tag{5.1}
\]
with `epsilon_r -> 0`. Then (4.4) implies
\[
\boxed{
\frac{\lambda_{\min}(K_r)}r=O(\sqrt{\varepsilon_r})+o(1).
}
\tag{5.2}
\]
More explicitly, ignoring the lower-order term,
\[
\frac{\lambda_{\min}(K_r)}r
\le
\sqrt{\frac{32\varepsilon_r}{\log_2(4/3)}}.
\tag{5.3}
\]
For inherited half-completions this says that any positive Gram fiber retaining almost the half-triangular entropy must satisfy
\[
\|P\|_{\rm op}^2=(2-o(1))r.
\tag{5.4}
\]
So the difficult positive regime is no longer the whole cone: it is forced into a **spectrally near-singular soft-edge layer**.

This also explains why the previous log-determinant route does not by itself close the bridge. A determinant deficit can be concentrated in one or a few very small eigenvalues, while the rest remain near `r`; determinant loss therefore need not imply a macroscopic Frobenius defect or a fixed lower spectral edge. The missing theorem should now target the soft edge directly.

## 6. What is new here, what is imported, and what remains open

Imported published ingredients:

- the affine cube-section philosophy/Odlyzko bound is classical;
- Ferber-Jain-Zhao Theorem 1.10 supplies the inhomogeneous anti-concentration inequality (4.1);
- the vector-matroid base-packing criterion is standard.

Project deductions proved here:

1. the exact rank-adaptive sign-Gram root bound (2.1), together with the cancellation identity (2.2) showing why singular rank loss alone cannot beat the half-triangular baseline;
2. the spectral base-packing lemma (3.1), converting a deterministic Gram lower edge into several disjoint spanning coefficient blocks;
3. the resulting inhomogeneous fixed-Gram entropy theorem (4.3)-(4.4) for every positive sign Gram matrix with `lambda_min(K)>=gamma r`;
4. the inverse localization (5.2)-(5.4) forcing any near-extremal Gram fiber into the soft-edge regime.

The full source conjecture is still open in this project. Even (4.4) retains a positive quadratic exponent, and a full symmetric matrix count cannot pay the seed `P` entropy independently. The singular endpoint is included by Theorem 2.2/Corollary 2.3, but (2.2) shows that its endpoint degrees of freedom can exactly cancel the naive rank saving.

The sharp next mathematical obligation is therefore:

> **Soft-edge Gram-fiber theorem.** Prove that a large fixed Gram fiber with `lambda_min(K)=o(r)` has additional arithmetic/sign structure that yields a further entropy loss, or construct an explicit family showing this implication is false.

A natural route is an inverse Littlewood-Offord analysis of the near-kernel direction: many sign roots of the same nearly singular Gram matrix force many sign rows/columns to satisfy the same unusually concentrated linear form. The goal should be a bound coupling the arithmetic complexity of that near-kernel with the fiber size, rather than another finite census.

## 7. Current literature boundary checked 20 September 2026

- Vu's source remains arXiv:2005.02797 / Probability Surveys 18 (2021), Conjecture 9.4.
- Ferber-Jain-Zhao prove `H(n)<=2^{(1-c_H)n^2/2}` and explicitly state that even `H(n)=2^{o(n^2)}` would be a significant advance likely requiring new ideas. Their Theorem 1.10 is the anti-concentration input used above: https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/on-the-number-of-hadamard-matrices-via-anticoncentration/887EFBBF79B804BCDD942029283D4CD7 .
- A bounded current search did not surface a resolution of Vu's exact integral-spectrum conjecture. This is only negative search evidence and is not an openness or novelty certificate.
