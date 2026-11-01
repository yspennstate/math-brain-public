Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated binding model/effort selector or runtime telemetry is exposed.

# F0011 — uniform half-completion entropy beyond the soft-edge split

Date: 2026-09-20 UTC  
Role: C05 / R7-06, native ID `6aabe827777c8191a43330b4a87d481d`  
Canonical target: Van H. Vu, *Recent progress in combinatorial random matrix theory*, Probability Surveys 18 (2021), Conjecture 9.4  
Status: **PROVED PARTIAL**, pending later independent review. Nothing below proves the full source conjecture.

## 1. Source target and inherited obstruction

For the symmetric Rademacher matrix `M_n^sym`, whose entries on and above the diagonal are independent fair signs and whose lower triangle is filled by symmetry, Vu's Conjecture 9.4 asks for

\[
\Pr\!\left(\operatorname{Spec}(M_n^{\rm sym})\subset\mathbb Z\right)
=2^{-(1/2+o(1))n^2}.
\]

Equivalently, source closure requires the total number of labelled symmetric sign matrices with integral spectrum to be `2^{o(n^2)}`.

The present project attacks the centered two-eigenvalue boundary

\[
H=\begin{pmatrix}P&C\\ C^T&D\end{pmatrix}=H^T\in\{\pm1\}^{2r\times2r},
\qquad H^2=2rI.
\tag{1.1}
\]

For a fixed symmetric sign seed `P`,

\[
K:=CC^T=2rI-P^2.
\tag{1.2}
\]

The preceding C05 run proved a constant quadratic saving for a positive Gram fiber when `lambda_min(K)>=gamma r`, but left the spectrally soft and singular endpoint as the principal conditioned obstruction. Earlier work also proved that, if `k=corank C`, then after fixing `(P,C)` the allowed symmetric endpoint blocks `D` lie in an affine space of dimension at most `binom(k+1,2)`.

The main point of this note is that a *minimum* spectral edge is not necessary. The exact trace and spectral cap in (1.2) force a positive proportion of well-conditioned spectral directions in every independent principal prefix of `K`, even when `K` is singular. Projecting to those directions and using a many-block version of the Ferber-Jain-Zhao atom inequality gives a uniform quadratic entropy saving for **every** fixed seed `P`, including every corank.

## 2. A projected spectral base-packing lemma

The following form is useful beyond F0011.

### Lemma 2.1 — projected covariance gives many disjoint bases

Let `A` be an `m x R` real matrix with columns `a_1,...,a_R`, and suppose

\[
\|a_j\|_2^2\le L\qquad(1\le j\le R).
\]

Let the eigenvalues of `AA^T` be

\[
\mu_1\ge\mu_2\ge\cdots\ge\mu_m\ge0.
\]

Fix `q<=m` and `tau>0` with `mu_q>=tau`. Let `U` be an orthonormal basis of the span of the top `q` eigenvectors and set `B=U^TA`, a `q x R` matrix. Then the columns of `B` contain at least

\[
\boxed{\left\lfloor\frac{\tau}{L}\right\rfloor}
\tag{2.1}
\]

pairwise disjoint bases of `R^q`.

**Proof.** We have

\[
BB^T\succeq \tau I_q.
\]

For every subspace `W<=R^q` of dimension `d`,

\[
\sum_{j=1}^R\|P_{W^\perp}b_j\|_2^2
=\operatorname{tr}(P_{W^\perp}BB^T)
\ge \tau(q-d).
\]

Also `||b_j||^2<=||a_j||^2<=L`. Hence at least `(tau/L)(q-d)` columns lie outside `W`. The vector-matroid base-packing criterion therefore supplies `floor(tau/L)` pairwise disjoint bases. ∎

### Corollary 2.2 — projected inhomogeneous atom bound

Let

\[
p_\ell:=2^{-\ell}\binom{\ell}{\ell/2}
\]

for even `ell`. If `tau/L>=ell`, then for every target `b`,

\[
\boxed{
\#\{x\in\{\pm1\}^R:Ax=b\}\le 2^R p_\ell^q.
}
\tag{2.2}
\]

Indeed any solution of `Ax=b` solves the projected system `Bx=U^Tb`; Lemma 2.1 gives `ell` disjoint full-rank blocks in `R^q`, and Ferber-Jain-Zhao Theorem 1.10 gives atom at most `p_ell^q`.

This differs from the preceding minimum-eigenvalue lemma: only `q` robust spectral directions are needed, while the remaining `m-q` directions can be arbitrarily soft or exactly singular.

## 3. Uniform spectral mass in every independent prefix of the F0011 Gram matrix

Fix `P` and let `K=2rI-P^2` be positive semidefinite and sign-rootable. Put

\[
\rho:=\operatorname{rank}K,
\qquad k:=r-\rho.
\]

Two exact facts are automatic:

\[
\operatorname{tr}K=r^2,
\qquad 0\preceq K\preceq 2rI.
\tag{3.1}
\]

Therefore

\[
\boxed{\rho\ge r/2.}
\tag{3.2}
\]

Choose from `K` a fixed principal positive-definite row basis `I` of size `rho`; for definiteness use the lexicographically first one. Order it arbitrarily once and for all. For `m<=rho`, let `K_m` be the principal Gram matrix on the first `m` selected indices. Then

\[
\operatorname{tr}K_m=mr,
\qquad 0<K_m\preceq 2rI_m.
\tag{3.3}
\]

Let `q_m` be the number of eigenvalues of `K_m` at least `(3/10)r`. Since every eigenvalue is at most `2r`,

\[
mr
\le q_m(2r)+(m-q_m)(3r/10),
\]

and hence

\[
\boxed{q_m\ge\frac7{17}m.}
\tag{3.4}
\]

This estimate holds for every prefix of the chosen independent basis and for every corank. It is the mechanism that removes the soft-edge exclusion.

## 4. Thirty-block anti-concentration at the first `r/100` basis steps

Let `C` be any sign root of `K`. Expose only the `rho` independent rows indexed by `I`; all remaining rows are uniquely determined from the Gram data after those basis rows are fixed.

After `m` basis rows have been exposed, write their `m x r` sign matrix as `A_m`. The next basis row `x in {+-1}^r` must solve

\[
A_mx=b_m
\tag{4.1}
\]

for an inhomogeneous target fixed by `K`. The ordinary affine-cube/Odlyzko bound gives at most `2^{r-m}` choices.

For

\[
1\le m\le M:=\left\lfloor\frac r{100}\right\rfloor,
\tag{4.2}
\]

project `A_m` onto the `q_m` eigendirections of `K_m=A_mA_m^T` having eigenvalue at least `(3/10)r`. Every original column of `A_m` has squared norm exactly `m`, hence every projected column has squared norm at most `m`. By Lemma 2.1, the projected columns contain at least

\[
\left\lfloor\frac{(3/10)r}{m}\right\rfloor\ge30
\]

disjoint bases of `R^{q_m}`.

Set

\[
p_{30}=2^{-30}\binom{30}{15}
=\frac{155117520}{1073741824},
\qquad
a_{30}:=\log_2(1/p_{30})\approx2.7912135978.
\]

Ferber-Jain-Zhao Theorem 1.10 and (3.4) imply

\[
\#\{x:A_mx=b_m\}
\le 2^r p_{30}^{q_m}
\le 2^{r-a_{30}(7/17)m}.
\tag{4.3}
\]

Define

\[
\boxed{
g_0:=\frac7{17}a_{30}-1\approx0.1493232461>0.
}
\tag{4.4}
\]

Comparing (4.3) with the Odlyzko factor `2^{r-m}`, each of the first `M` nontrivial basis extensions gains an additional factor

\[
\boxed{2^{-g_0m}.}
\tag{4.5}
\]

The gain is completely uniform in `P`, `K`, the corank, and the inhomogeneous targets.

## 5. The uniform all-corank fixed-seed theorem

### Theorem 5.1 — every fixed seed loses a quadratic amount of completion entropy

For every symmetric sign seed `P` for which `K=2rI-P^2` is sign-rootable, let `k=corank K`. Then the number of sign pairs `(C,D)` satisfying (1.1) with that fixed `P` obeys

\[
\boxed{
\#\{(C,D)\text{ completing }P\}
\le
2^{r(r+1)/2-g_0M(M+1)/2},
\qquad M=\lfloor r/100\rfloor.
}
\tag{5.1}
\]

In particular,

\[
\boxed{
\log_2\#\{(C,D)\text{ completing }P\}
\le
\left(\frac12-c_0\right)r^2+O(r),
}
\tag{5.2}
\]

where

\[
\boxed{
c_0:=\frac{g_0}{20000}
=\frac1{20000}\left(
\frac7{17}\log_2\frac{2^{30}}{\binom{30}{15}}-1
\right)
\approx7.46616\times10^{-6}.
}
\tag{5.3}
\]

**Proof.** Exposing the `rho=r-k` independent basis rows of `C` with only the affine-cube bound gives

\[
2^{\rho r-\binom\rho2}.
\]

Section 4 improves this by the multiplicative factor

\[
2^{-g_0\sum_{m=1}^M m}
=2^{-g_0M(M+1)/2}.
\]

The dependent rows of `C` are then uniquely reconstructed from `K`. The inherited endpoint theorem gives at most

\[
2^{\binom{k+1}{2}}
\]

sign choices for symmetric `D`. Finally,

\[
\rho r-\binom\rho2+\binom{k+1}{2}
=\frac{r(r+1)}2,
\]

so (5.1) follows. Because `rho>=r/2`, the range `m<=M` always lies inside the independent-basis exposure for all sufficiently large `r`; small orders are absorbed in the `O(r)` term. ∎

This is the main advance of the run. The previous theorem required `lambda_min(K)>=gamma r`; Theorem 5.1 gives a fixed positive quadratic saving **uniformly over the entire allowed Gram cone, including exact singular endpoints**.

## 6. Consequence for the centered two-eigenvalue fixed-spectrum boundary

There are at most

\[
2^{r(r+1)/2}
\]

symmetric sign choices for `P`. Summing (5.1) over all of them gives

\[
\boxed{
\#\{H=H^T\in\{\pm1\}^{2r\times2r}:H^2=2rI\}
\le
2^{r(r+1)-g_0M(M+1)/2}.
}
\tag{6.1}
\]

Writing `N=2r`,

\[
\boxed{
\log_2 \#\{H:H^2=NI\}
\le
\left(\frac14-\frac{c_0}{4}\right)N^2+O(N).
}
\tag{6.2}
\]

Numerically `c_0/4≈1.86654e-6`. This is a strict quadratic improvement on the previous project bound `2^{N^2/4+O(N)}` for the entire symmetric-Hadamard/two-eigenvalue boundary.

The estimate is uniform in the multiplicities of `+sqrt(N)` and `-sqrt(N)`; fixing a trace or a particular two-eigenvalue spectrum can only reduce the count. For Vu's integral-spectrum event this branch contributes only when `sqrt(N)` is integral, but (6.2) is stated for all orders because the combinatorial theorem does not require integrality of `sqrt(N)`.

This remains far from the `2^{o(N^2)}` needed for full F0011. It is nevertheless a genuine uniform fixed-spectrum entropy theorem, and it no longer carves out the singular/corank endpoint.

## 7. Exact mixed-energy identity and why the remaining endpoint is genuinely Hadamard-hard

The soft-edge analysis also admits a useful exact invariant. From

\[
K=CC^T=2rI-P^2
\]

we obtain

\[
\boxed{
T(P,C):=\operatorname{tr}(K(2rI-K))
=\|PC\|_F^2
=2r^3-\operatorname{tr}(P^4).
}
\tag{7.1}
\]

Thus `T>=0`, and `T=0` iff `PC=0`, equivalently the spectrum of `K` is supported on `{0,2r}`. Since every entry of `PC` is an inner product of two sign vectors of length `r`,

- if `r` is even, every nonzero entry of `PC` has magnitude at least `2`, hence `#supp(PC)<=T/4`;
- if `r` is odd, every entry of `PC` is odd, hence
  \[
  \boxed{T\ge r^2.}
  \tag{7.2}
  \]

At the exact endpoint `T=0`, trace and spectral-cap equality force

\[
\boxed{\operatorname{rank}P=\operatorname{rank}C=r/2.}
\tag{7.3}
\]

Indeed `P^2` and `CC^T` have complementary spectra in `{0,2r}`, while `tr(P^2)=tr(CC^T)=r^2`.

One should not expect rank deficiency by itself to make this endpoint low-entropy. Let `r=2s`. Suppose `A` and `E` are symmetric Hadamard matrices of order `s`, and `B` is an arbitrary Hadamard matrix of order `s`. Define

\[
P=\begin{pmatrix}A&A\\A&A\end{pmatrix},\qquad
C=\begin{pmatrix}B&B\\-B&-B\end{pmatrix},\qquad
D=\begin{pmatrix}E&-E\\-E&E\end{pmatrix}.
\tag{7.4}
\]

Then

\[
P^2=r\begin{pmatrix}I&I\\I&I\end{pmatrix},\qquad
CC^T=r\begin{pmatrix}I&-I\\-I&I\end{pmatrix},\qquad
PC=CD=0,
\]

and

\[
C^TC=r\begin{pmatrix}I&I\\I&I\end{pmatrix},\qquad
D^2=r\begin{pmatrix}I&-I\\-I&I\end{pmatrix}.
\]

Therefore

\[
\boxed{
H=\begin{pmatrix}P&C\\C^T&D\end{pmatrix}
}
\tag{7.5}
\]

is a symmetric Hadamard matrix of order `4s=2r`, with exact endpoint energy `T=0` and `corank C=r/2`.

The construction is injective in `(A,B,E)` from the displayed blocks. In particular, whenever one symmetric Hadamard of order `s` exists, fixing `A=E` and varying `B` embeds **every** labelled Hadamard matrix of order `s` into a labelled symmetric Hadamard matrix of order `4s`:

\[
\boxed{H_{\rm sym}(4s)\ge H(s).}
\tag{7.6}
\]

This is an explicit obstruction to any proposed intermediate theorem asserting that the maximally singular endpoint can be counted by a merely polynomial, `2^{O(r log r)}`, or rank-only argument. It does **not** refute Vu's conjecture; the general Hadamard growth conjecture itself predicts subquadratic entropy. The lesson is narrower: the remaining endpoint contains a genuine smaller-order Hadamard counting problem and cannot be dismissed as a degenerate technical case.

The block construction is presented here as a project obstruction/example; no external novelty claim is made for the construction form.

## 8. What moved and what remains

Before this run:

- a constant quadratic saving was available only when the full positive Gram matrix had `lambda_min(K)>=gamma r`;
- arbitrary corank was controlled only at the half-triangular `r(r+1)/2` conditioned baseline;
- the soft edge was the declared fixed-seed gap.

After this run:

- projected spectral base-packing uses only a positive fraction of robust directions;
- the exact trace `mr` and cap `2r` force at least `7m/17` robust directions in every early independent prefix;
- thirty-block anti-concentration produces a uniform quadratic saving `c_0 r^2` for **every** fixed seed, singular or nonsingular;
- the entire centered two-eigenvalue family improves from exponent `N^2/4+O(N)` to `(1/4-c_0/4)N^2+O(N)`;
- an exact endpoint embedding shows why further progress must confront Hadamard-scale structure rather than rely on rank deficiency alone.

The full Vu conjecture still requires eliminating the remaining positive quadratic exponent and then extending beyond this two-eigenvalue boundary to arbitrary integral spectra.

## 9. Next attack

The most useful next step is no longer another minimum-eigenvalue split. Two routes are now clean:

1. **Iterate spectral-profile savings at multiple scales.** Replace the single threshold `(3/10)r` and the first `r/100` basis steps by an optimized integral over thresholds and even block counts `ell`. The exact profile theorem in Section 2 permits this without excluding soft directions. The goal is a substantially larger universal constant, or a recurrence showing cumulative savings on a sequence of nested principal Gram problems.
2. **Exploit the mixed-energy endpoint algebra.** In the regime `T=o(r^3)`, the complementary Gram pair is close to rank-`r/2` tight-frame projectors. Either prove a stability decomposition into a bounded-complexity Naimark/Hadamard frame model and count it, or construct a large family showing that such a stability reduction is false.

A source-level solution still needs a mechanism that drives the exponent all the way to `o(N^2)` and treats general integral spectra.

## 10. Literature boundary checked 20 September 2026

Vu's source remains arXiv `2005.02797`, Conjecture 9.4. A bounded fresh search on 20 September 2026 did not surface a proof of the exact integral-spectrum asymptotic; this is negative search evidence only, not an openness certificate.

Ferber-Jain-Zhao, *On the number of Hadamard matrices via anti-concentration*, Combin. Probab. Comput. 31 (2022), Theorem 1.10, is the imported atom inequality used above. Their paper proves a constant quadratic improvement for general Hadamard counting and explicitly leaves `2^{o(n^2)}` as a much stronger goal. No part of that published theorem is claimed as new here; the project contribution is the projected spectral-prefix mechanism and its all-corank application to the fixed-seed F0011 block equations.
