# F0012 — rational-flag incidence reduction and the sharp fixed-stratum half exponent

Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

Target: Van H. Vu, *Recent progress in combinatorial random matrix theory*, Conjecture 9.5. For the iid nonsymmetric Rademacher matrix `M_n`, let

\[
E_n:=\{\operatorname{Spec}(M_n)\subset \mathbf Z[i]\}.
\]

The source conjectures `P(E_n)=2^{-(1+o(1))n^2}`. R7-07 has already refuted that literal exponent and proved the all-dimensional lower bound

\[
\mathbf P(E_n)\ge 3^{\lfloor n/2\rfloor}2^{-\lfloor n^2/2\rfloor}.
\]

The frozen metric remains

\[
u_{GI}:=\liminf_{n\to\infty}\frac{-\log_2\mathbf P(E_n)}{n^2},
\qquad 0\le u_{GI}\le \frac12.
\]

This note gives a new exact reformulation of the *matching upper-bound problem*. It does not move `u_GI` by itself.

## 1. B3 — prove a stronger restricted theorem: every fixed rational flag has at most half entropy

Put `K=Q(i)`. A complete `K`-rational flag is

\[
0=V_0<V_1<\cdots<V_n=K^n,\qquad \dim_KV_j=j.
\]

For such a flag `F`, let

\[
\mathfrak b_F:=\{T\in M_n(K):T(V_j)\subseteq V_j\text{ for every }j\}
\]

be its flag-preserving (Borel) algebra.

### Theorem 1 (exact rational-flag characterization)

For an integer matrix `M in M_n(Z)`, the following are equivalent.

1. `Spec(M) subset Z[i]`.
2. The characteristic polynomial of `M` splits over `K=Q(i)`.
3. `M` preserves a complete `K`-rational flag.

#### Proof

`(1) => (2)` is immediate.

For `(2) => (3)`, use the standard triangularizability criterion over a field: an endomorphism of a finite-dimensional `K`-vector space is triangularizable over `K` iff its characteristic polynomial splits over `K`. For completeness, this follows by induction on `n`. A split characteristic polynomial supplies an eigenvalue `lambda in K` and a nonzero eigenvector `v in K^n`; the invariant line `Kv` is `V_1`. The induced operator on `K^n/Kv` again has split characteristic polynomial, so the induction hypothesis lifts to an invariant complete flag.

For `(3) => (1)`, choose a basis adapted to the invariant flag. The matrix of `M` is upper triangular over `K`; therefore every eigenvalue lies in `K`. But `M` has integer entries, so every eigenvalue is an algebraic integer. The ring of integers of `Q(i)` is `Z[i]`. Hence every eigenvalue lies in `Z[i]`.

This proves the equivalence. `square`

Thus the event `E_n` is exactly the projection to the sign cube of the incidence relation

\[
M\in\{\pm1\}^{n\times n},\quad F\in\operatorname{Fl}_n(K),\quad M\in\mathfrak b_F.
\]

### Lemma 2 (hypercube-section bound)

If `W` is a real `d`-dimensional linear subspace of `R^N`, then

\[
|W\cap\{\pm1\}^N|\le 2^d.
\]

#### Proof

Choose a basis of `W` and form the corresponding `d x N` coordinate matrix. Since its row rank is `d`, some set `I` of `d` coordinate columns is linearly independent. The coordinate projection `pi_I:W->R^d` is injective. On cube points its image is contained in `{+-1}^d`, which has `2^d` elements. `square`

### Theorem 3 (sharp fixed-flag upper exponent)

For every complete `K`-rational flag `F`,

\[
\boxed{\left|\mathfrak b_F\cap\{\pm1\}^{n\times n}\right|\le 2^{n(n+1)/2}.}
\]

#### Proof

After extending scalars to `C`, the flag-preserving algebra has complex dimension

\[
d=1+2+\cdots+n=\frac{n(n+1)}2.
\]

Let

\[
W_F:=\mathfrak b_F(\mathbf C)\cap M_n(\mathbf R).
\]

Any real-linearly independent family in `W_F` is also complex-linearly independent: if real vectors `v_j` satisfy `sum_j(a_j+ib_j)v_j=0`, separating real and imaginary parts gives two real linear relations, forcing all `a_j,b_j` to vanish. Hence

\[
\dim_R W_F\le d.
\]

Apply Lemma 2 inside the real vector space `M_n(R) congruent R^{n^2}`. `square`

### Theorem 4 (the exponent `1/2` is already sharp inside one fixed flag)

For every even `n=2m` there is one fixed `Q`-rational complete flag `F_m` for which

\[
\left|\mathfrak b_{F_m}\cap\{\pm1\}^{n\times n}\right|
\ge 4^{m(m-1)}6^m
=2^{n^2/2+(n/2)\log_2(3/2)}.
\]

#### Proof

Write

\[
M=\begin{pmatrix}A&B\\ C&D\end{pmatrix},\qquad
S=\begin{pmatrix}I&0\\ I&I\end{pmatrix}.
\]

Then

\[
S^{-1}MS=
\begin{pmatrix}
A+B&B\\
C+D-A-B&D-B
\end{pmatrix}.
\]

Impose

- `A+B` upper triangular;
- `C+D=A+B`;
- `D-B` lower triangular.

Let `J` be the `m x m` reversal permutation matrix and set `Q=S diag(I,J)`. Then

\[
Q^{-1}MQ=
\begin{pmatrix}
A+B&BJ\\
0&J(D-B)J
\end{pmatrix},
\]

which is upper triangular. Therefore all these sign matrices preserve the single fixed rational flag `F_m=Q F_std`.

For each ordered off-diagonal position the constraints leave exactly four sign choices: below the diagonal, `a=-b` and `c=-d`; above the diagonal, `d=b` and `c=a`. Across all off-diagonal positions this gives `4^{m(m-1)}` choices. At each diagonal position the sole relation is

\[
c+d=a+b,
\]

which has exactly six sign quadruples. The choices are independent, giving exactly `4^{m(m-1)}6^m` matrices. `square`

Consequently the `n^2/2` exponent cannot be improved by any argument that only bounds one flag-preserving linear stratum. The remaining difficulty is the entropy of the *union of rational flags*.

## 2. B14 — quotient the exact flag problem by the signed-permutation group

Let `Gamma_n` be the image, under conjugation, of the signed permutation matrices

\[
G_n=\{DP:D=\operatorname{diag}(\pm1,\ldots,\pm1),\ P\in S_n\}.
\]

Conjugation by `DP` maps sign matrices to sign matrices and preserves the spectrum. Its kernel is exactly `{+-I}` for `n>=2`, hence

\[
\boxed{|\Gamma_n|=2^{n-1}n! = 2^{O(n\log n)}.}
\]

It acts on rational flags, and

\[
\mathfrak b_{gF}=g\mathfrak b_Fg^{-1}.
\]

Define `kappa_n` to be the minimum number of `Q(i)`-rational complete flags whose Borel strata cover `E_n` inside the sign cube. Define `q_n` to be the minimum number of `Gamma_n`-orbits of rational flags whose full orbit-strata cover `E_n`. Then

\[
q_n\le \kappa_n\le |\Gamma_n|q_n.
\]

Indeed, any flag cover determines at most that many orbits, while an orbit cover by `q_n` representatives expands to at most `|Gamma_n|q_n` individual flags. Therefore

\[
\boxed{
\limsup_{n\to\infty}\frac{\log_2\kappa_n}{n^2}
=
\limsup_{n\to\infty}\frac{\log_2q_n}{n^2}.
}
\]

So signed-permutation normalization is legitimate for the `n^2` exponent, but it cannot by itself create an exponential-in-`n^2` saving: the entire symmetry group costs only `2^{o(n^2)}`.

Combining Theorem 3 with a minimal flag cover gives the exact inequality

\[
|E_n|\le \kappa_n\,2^{n(n+1)/2},
\]

and hence

\[
\boxed{
\mathbf P(E_n)
\le
\kappa_n\,2^{-n(n-1)/2}.
}
\]

If

\[
c_{flag}:=\limsup_{n\to\infty}\frac{\log_2\kappa_n}{n^2},
\]

then

\[
\boxed{u_{GI}\ge \frac12-c_{flag}.}
\]

The same `c_flag` is obtained from `q_n` by the preceding symmetry quotient.

In particular, the single missing covering statement

\[
\boxed{\kappa_n=2^{o(n^2)}}
\]

would imply `u_GI>=1/2`; together with R7-07's explicit all-dimensional lower construction, it would give the corrected exact exponent

\[
\boxed{u_{GI}=1/2.}
\]

No such subquadratic flag-cover theorem is claimed here.

## 3. B29 — projectivize: the flag variety removes geometric escape and isolates arithmetic entropy

The natural compactification is not projective space for a single eigenvector but the complete flag variety

\[
\operatorname{Fl}_n/K.
\]

This is a projective algebraic variety. Define the rational incidence set

\[
\mathcal I_n(K)
=
\{(M,F):M\in\{\pm1\}^{n\times n},\ F\in\operatorname{Fl}_n(K),\ M(V_j)\subseteq V_j\ \forall j\}.
\]

By Theorem 1, projection onto `M` is *exactly* `E_n`. Thus eigenvector-coordinate charts do not need an ad hoc treatment of vectors whose denominators blow up: all such limits live on the projective flag variety already. There is no missing geometric boundary. What remains is arithmetic: how many `K`-rational flag strata are genuinely needed to cover the sign matrices in the projection?

This identifies the correct obstruction to a matching upper bound as **rational-flag covering entropy**, not geometric noncompactness.

There is a second exact reduction that reaches the same conclusion. Gershgorin gives `|lambda|<=n` for every eigenvalue of a sign matrix. Hence an `E_n` spectrum uses Gaussian integers from a set of size at most `(2n+1)^2`. The number of possible multisets of `n` eigenvalues, and therefore the number of possible characteristic polynomials occurring in `E_n`, is at most

\[
\binom{(2n+1)^2+n-1}{n}=2^{O(n\log n)}.
\]

Therefore a matching upper bound at exponent `1/2` would follow from the stronger uniform fiber statement

\[
\max_{p}\#\{M\in\{\pm1\}^{n\times n}:\chi_M=p\}
\le 2^{n^2/2+o(n^2)},
\]

where `p` ranges only over characteristic polynomials split over `Q(i)` with Gaussian-integer roots of modulus at most `n`.

This fiber route cannot be justified by characteristic-polynomial equations alone. Classical finite-field counting is a warning: the nilpotent characteristic polynomial `x^n` already has `q^{n^2-n}` matrices over `F_q` (Fine--Herstein/Gerstenhaber), and Reiner's 1961 work counts matrices with a prescribed characteristic polynomial. Thus a successful half-exponent upper bound must use the special intersection with the real sign hypercube, not merely the algebraic codimension of a characteristic-polynomial fiber.

## 4. What moved, and what did not

The frozen source metric does **not** move:

\[
0\le u_{GI}\le 1/2
\quad\longrightarrow\quad
0\le u_{GI}\le 1/2.
\]

What is new is an exact structural reduction:

1. `E_n` equals the sign-cube projection of `Q(i)`-rational flag incidence.
2. Every fixed rational flag contributes at most `2^{n(n+1)/2}` matrices.
3. One fixed rational flag already contributes `2^{n^2/2+Theta(n)}` matrices, so the half exponent is sharp at stratum level.
4. Signed-permutation quotienting changes the cover entropy only by `o(n^2)`.
5. The matching global exponent reduces to proving subquadratic rational-flag covering entropy (or, equivalently, a uniform half-entropy bound for each admissible characteristic-polynomial fiber).

This is a genuine narrowing of the post-refutation problem, but not a proof that the corrected exponent is `1/2`.

## 5. Dated prior-art boundary — 2026-09-19

Fresh bounded searches were run for the exact Vu conjecture/title, `Gaussian integral spectrum`, iid Rademacher matrices with Gaussian/integer spectrum, characteristic-polynomial irreducibility, and prescribed characteristic-polynomial counting.

- Vu's arXiv source remains the source statement used here: arXiv:2005.02797, Conjecture 9.5.
- Sean Eberhard, *The Characteristic Polynomial of a Random Matrix*, Combinatorica 42 (2022), proves conditionally on ERH that an iid sign/integer-entry random matrix has irreducible characteristic polynomial and Galois group containing `A_n` with high probability. This is qualitatively adjacent but does not state a `2^{-Theta(n^2)}` exceptional-event rate or a rational-flag-cover bound.
- Ferber--Jain--Sah--Sawhney prove the analogous high-probability irreducibility statement for random symmetric sign matrices, also conditional on ERH; that is a different model.
- Duvall--Harley (1971) explicitly cite Irving Reiner's 1961 prescribed-characteristic-polynomial count; Gerstenhaber (1961) records the exact `q^{n^2-n}` nilpotent count.
- The graph-integrality literature (e.g. Ahmadi--Alon--Blake--Shparlinski 2009) concerns symmetric adjacency matrices and only an exponential-in-`n` rarity relative to the graph cube, not Vu's nonsymmetric iid sign-matrix exponent.

No fresh search surfaced the fixed-rational-flag theorem or the explicit R7-07 shear construction as a published refutation of Vu 9.5. This is bounded negative evidence only. **Novelty remains UNVERIFIED.**

## 6. Next mathematical attack

A nonrepeating next triple is reserved as **B12 / B24 / B8**:

- **B12 (find what is conserved):** derive invariants of a rational flag stratum visible directly from sign entries (Plucker-coordinate valuations, determinantal divisors, or exterior-power eigenlines) that can bound how many distinct rational flag orbits one sign matrix family can realize.
- **B24 (find the extremal object):** maximize `|b_F cap {+-1}^{n^2}|` over rational flags and test whether the fixed shear flag is asymptotically extremal beyond the universal `2^{n(n+1)/2}` linear-subspace bound.
- **B8 (discretize):** use exact small-dimensional rational/projective normalization to classify flag orbits that actually meet the sign cube, with the goal of discovering a finite-height or finite-Plucker pattern that scales.

The source refutation remains mathematically complete, but protocol closure still depends on real independent P26 and distinct OTHER-track audits; self-analysis here is neither.