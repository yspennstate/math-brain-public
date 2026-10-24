Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — the requested GPT-6/maximum setting is a preference, not authenticated runtime telemetry, so I do not claim it ran.**

# C0036: an index-two constant-coset lifting theorem and a strictly noncentral `S_3` class

Date: 2026-09-20 UTC  
Role: C03 / R7-03, native ID `6aabe7be74008191b526b109ee4e9e80`  
Canonical ownership: preserved; this is the complementary C03 role in `operations/progress_first_2026-09-20/REGISTRY.md`.  
Captured fresh master before this artifact: `06f22e78957ea2a180ed10e375a8ba6d400262a9`.  
Previous checkpoint: `research7_2026-09-17/R7-03/runs/2026-09-20/2026-09-20T034500Z__report.md`.  
Status: **PROVED PARTIAL relative to the full source.**

## 1. Exact source target

Russell Lyons, *Determinantal Probability: Basic Properties and Conjectures* (ICM 2014), arXiv:1406.2707, Section 5.2, Conjecture 5.7.

The section fixes a **sofic group** `Gamma`. The conjecture ranges over every `Gamma`-equivariant positive contraction

\[
0\le Q\le I\quad\text{on }\ell^2(\Gamma),
\]

with group trace

\[
\operatorname{tr}_\Gamma(T)=\langle T\delta_e,\delta_e\rangle
\]

and Fuglede--Kadison determinant

\[
\operatorname{FK}_\Gamma(Q)=\exp\bigl(\operatorname{tr}_\Gamma\log|Q|\bigr).
\]

Writing `P^Q` for the associated determinantal law, the target is the **full stochastic-domination statement on every increasing event**

\[
\boxed{
\mathbf P^{\operatorname{FK}_\Gamma(Q)I}
\preccurlyeq \mathbf P^Q
\preccurlyeq
\mathbf P^{I-\operatorname{FK}_\Gamma(I-Q)I}
}
\tag{1.1}
\]

with both product densities optimal. For a finite group of order `N`,

\[
\operatorname{FK}_\Gamma(Q)=(\det Q)^{1/N}.
\tag{1.2}
\]

The source explicitly states that Conjecture 5.7 is open even for finite groups. Nothing below is represented as full-source closure.

## 2. Inherited lemma

The preceding R7-03 checkpoint proved the following full-process finite-DPP lemma.

Let `D` be a diagonal unitary involution on a finite ground set. Suppose

\[
\ell^2(E)=W\oplus\operatorname{span}\{u,v\}
\]

orthogonally, `W` is `D`-invariant, `Q|_W` commutes with `D|_W`, and

\[
Qu=au,\qquad Qv=bv,\qquad Du=v,\qquad Dv=u.
\]

Replacing `a,b` by their geometric mean `g=sqrt(ab)` while leaving `Q|_W` unchanged gives a contraction `Q_tilde` satisfying

\[
\boxed{\mathbf P^{Q_{\rm tilde}}\preccurlyeq\mathbf P^Q},
\qquad
\boxed{\det Q_{\rm tilde}=\det Q}.
\tag{2.1}
\]

The proof is event-level, not merely principal-minor comparison.

The question in this run is whether this can be converted into a group-theoretic lifting criterion substantially broader than the central generalized-dihedral class proved previously.

## 3. Index-two quotient notation

Let `Gamma` be a finite group and let `H` be a subgroup of index two. Then `H` is normal and there is a quotient character

\[
\varepsilon:\Gamma\to\{\pm1\},\qquad H=\ker\varepsilon.
\tag{3.1}
\]

Let `D` be multiplication by `epsilon` on `ell^2(Gamma)`:

\[
(Df)(x)=\varepsilon(x)f(x).
\tag{3.2}
\]

For a `Gamma`-equivariant convolution operator with kernel `q`,

\[
Q(x,y)=q(x^{-1}y),
\]

conjugation by `D` multiplies the kernel by the quotient character:

\[
(DQD)(x,y)=\varepsilon(x^{-1}y)q(x^{-1}y).
\tag{3.3}
\]

Hence a `Gamma`-equivariant operator commutes with `D` exactly when its convolution kernel is supported in `H`.

Define the normalized quotient-character vectors

\[
u_+=|\Gamma|^{-1/2}\sum_{x\in\Gamma}\delta_x,
\qquad
u_-=|\Gamma|^{-1/2}\sum_{x\in\Gamma}\varepsilon(x)\delta_x.
\tag{3.4}
\]

Then

\[
D\nu_+=\nu_-,\qquad D\nu_-=\nu_+.
\tag{3.5}
\]

Let

\[
V=\operatorname{span}\{\nu_+,\nu_-\},\qquad W=V^\perp.
\tag{3.6}
\]

Both `V` and `W` are `D`-invariant.

## 4. The constant complementary-coset operator has rank two

Fix `t in Gamma\H` and let `C` be convolution by the indicator of the complementary coset `tH=Gamma\H`:

\[
c(g)=\mathbf 1_{\Gamma\setminus H}(g).
\tag{4.1}
\]

Because `H` is normal,

\[
\sum_{g\in tH}R_g
=R_t\sum_{h\in H}R_h,
\tag{4.2}
\]

where `R_g` denotes right translation. The averaging operator

\[
\frac1{|H|}\sum_{h\in H}R_h
\]

is the orthogonal projection onto the right-`H`-invariant subspace. Since `[Gamma:H]=2`, this subspace is exactly `V`. Consequently

\[
\operatorname{rank}C=2,
\qquad C|_W=0.
\tag{4.3}
\]

On the quotient characters,

\[
C\nu_+=|H|\nu_+,
\qquad
C\nu_-=-|H|\nu_-.
\tag{4.4}
\]

Thus a convolution term that is constant on `Gamma\H` acts only on the single `D`-swapped pair `(nu_+,nu_-)` and vanishes identically on the entire orthogonal complement.

This is the structural observation that removes the centrality hypothesis from the previous generalized-dihedral theorem.

## 5. Main theorem: index-two constant-coset lift

### Theorem 5.1

Let `Gamma` be a finite group, let `H normal Gamma` have index two, and assume Lyons's lower product bound is valid for every `H`-equivariant positive contraction on `ell^2(H)`.

Let `Q` be a `Gamma`-equivariant positive contraction whose Hermitian convolution kernel `q` is **constant on the complementary coset**:

\[
q(g)=\tau\qquad(g\in\Gamma\setminus H)
\tag{5.1}
\]

for some real `tau`. No centrality or conjugacy invariance is assumed for `q|_H`.

Then

\[
\boxed{
\mathbf P^{\operatorname{FK}_\Gamma(Q)I}
\preccurlyeq \mathbf P^Q.
}
\tag{5.2}
\]

If the lower theorem on `H` is available for complements as well (in particular, if the full two-sided Lyons theorem is known on `H`), then

\[
\boxed{
\mathbf P^{\operatorname{FK}_\Gamma(Q)I}
\preccurlyeq \mathbf P^Q
\preccurlyeq
\mathbf P^{I-\operatorname{FK}_\Gamma(I-Q)I}.
}
\tag{5.3}
\]

Both constants in (5.3) are optimal.

### Proof

Split the kernel into its `H`-supported and complementary-coset parts:

\[
q=k+\tau\mathbf 1_{\Gamma\setminus H},
\tag{5.4}
\]

and let `K` be convolution by `k`. Because `k` is supported in `H`, equation (3.3) gives

\[
DKD=K.
\tag{5.5}
\]

In particular, `K` commutes with `D`, preserves `V` and `W`, and `K|_W` commutes with `D|_W`.

On both quotient-character vectors, the `H`-supported convolution has the same eigenvalue. Indeed the trivial and sign characters coincide on `H`, so

\[
K\nu_+=\kappa\nu_+,
\qquad
K\nu_-=\kappa\nu_-,
\qquad
\kappa:=\sum_{h\in H}k(h).
\tag{5.6}
\]

By (4.3)--(4.4), the complementary-coset term vanishes on `W` and has eigenvalues `+tau|H|` and `-tau|H|` on `nu_+` and `nu_-`. Hence

\[
Q|_W=K|_W,
\tag{5.7}
\]

while

\[
Q\nu_+=a\nu_+,
\qquad
Q\nu_-=b\nu_-,
\tag{5.8}
\]

with

\[
a=\kappa+\tau|H|,
\qquad
b=\kappa-\tau|H|.
\tag{5.9}
\]

Because `Q` is a positive contraction, `a,b in [0,1]`.

All hypotheses of the inherited single-gauge-pair theorem now hold with the pair `(nu_+,nu_-)`. Put

\[
g=\sqrt{ab}
\tag{5.10}
\]

and define `Q_tilde` by replacing `a,b` with `g,g` and leaving `Q|_W` unchanged. Then

\[
\mathbf P^{Q_{\rm tilde}}\preccurlyeq\mathbf P^Q,
\qquad
\det Q_{\rm tilde}=\det Q.
\tag{5.11}
\]

Moreover `Q_tilde` commutes with `D`: it is scalar on the `D`-swapped space `V` and agrees with the `D`-commuting operator `K` on `W`. By (3.3), the convolution kernel of `Q_tilde` is therefore supported entirely in `H`.

The two right cosets of `H` consequently reduce `Q_tilde`, and the two blocks are unitarily identical copies of one `H`-equivariant positive contraction `L` on `ell^2(H)`. Thus

\[
\mathbf P^{Q_{\rm tilde}}=\mathbf P^L\otimes\mathbf P^L.
\tag{5.12}
\]

Since `|Gamma|=2|H|` and the determinant is preserved,

\[
\operatorname{FK}_\Gamma(Q)
=(\det Q)^{1/(2|H|)}
=(\det Q_{\rm tilde})^{1/(2|H|)}
=(\det L)^{1/|H|}
=\operatorname{FK}_H(L).
\tag{5.13}
\]

By the assumed lower theorem on `H`,

\[
\operatorname{Ber}(\operatorname{FK}_H(L))^{\otimes H}
\preccurlyeq \mathbf P^L.
\]

Taking the product coupling on the two cosets, then using (5.11)--(5.13), gives

\[
\operatorname{Ber}(\operatorname{FK}_\Gamma(Q))^{\otimes\Gamma}
\preccurlyeq \mathbf P^{Q_{\rm tilde}}
\preccurlyeq \mathbf P^Q,
\]

which proves (5.2).

For the upper bound, observe that `I-Q` has complementary-coset kernel equal to the constant `-tau`, so it lies in the same class. Apply the lower theorem just proved to `I-Q`, then complement configurations. This gives the upper inequality in (5.3).

For sharpness, the full-set event has probability

\[
\mathbf P^Q[X=\Gamma]=\det Q
=\operatorname{FK}_\Gamma(Q)^{|\Gamma|},
\]

so no larger lower product density is possible. Applying the same statement to `I-Q`, equivalently to the empty-set event, proves optimality of the upper density. `QED`

## 6. Strictly noncentral `S_3` corollary

Take

\[
\Gamma=S_3,
\qquad
H=A_3\cong C_3.
\]

The prior R7-03 work gives the full sharp two-sided theorem on `C_3`. Therefore Theorem 5.1 yields:

### Corollary 6.1

Let `Q` be any `S_3`-equivariant positive contraction whose Hermitian convolution kernel takes one common value on the three transpositions. The values on the two nontrivial three-cycles may be arbitrary complex conjugates; in particular, the kernel need not be central. Then

\[
\boxed{
\operatorname{Ber}(\operatorname{FK}_{S_3}(Q))^{\otimes S_3}
\preccurlyeq \mathbf P^Q
\preccurlyeq
\operatorname{Ber}(1-\operatorname{FK}_{S_3}(I-Q))^{\otimes S_3}
}
\tag{6.1}
\]

on every increasing event, with both constants sharp.

This strictly enlarges the previous central `S_3` theorem. Centrality would additionally require the two three-cycle kernel values to be equal, hence real. Corollary 6.1 allows them to be unequal complex conjugates.

### Exact noncentral interior example

Let `r` generate `A_3=C_3`, and choose the `C_3` Fourier eigenvalues

\[
(\lambda_0,\lambda_1,\lambda_2)=\left(\frac12,\frac14,\frac34\right).
\tag{6.2}
\]

The corresponding `H`-supported Hermitian convolution kernel has

\[
k(e)=\frac12,
\qquad
k(r)=-\frac{i\sqrt3}{12},
\qquad
k(r^2)=\frac{i\sqrt3}{12}
\tag{6.3}
\]

(up to the harmless Fourier-sign convention). Extend it to `S_3` by taking the common transposition value

\[
\tau=\frac1{24}.
\tag{6.4}
\]

The quotient-character eigenvalues become

\[
\frac12\pm 3\tau
=\frac58,\frac38,
\]

while the standard-sector eigenvalues remain `1/4` and `3/4` (each with its regular-representation multiplicity). Thus `0<Q<I`. The kernel is not central because `k(r) != k(r^2)`, yet Corollary 6.1 proves the full sharp two-sided stochastic domination for this operator and, more importantly, for the entire class containing it.

The equalized quotient eigenvalue is

\[
\sqrt{\frac58\frac38}=\frac{\sqrt{15}}8,
\]

and after the single-pair step the kernel is `A_3`-supported, exactly as the theorem predicts.

## 7. Why the arbitrary `S_3` midpoint step is still nontrivial

The previous checkpoint reduced arbitrary `S_3` to the candidate midpoint inequality

\[
\mathbf P^{Q\#(DQD)}\preccurlyeq\mathbf P^Q.
\tag{7.1}
\]

Theorem 5.1 proves (7.1) in the rank-two quotient-perturbation situation above, because the only non-`D`-commuting spectral sector is one swapped pair. It does **not** prove (7.1) for a general `S_3` kernel, whose standard isotypic sector can also fail to commute with `D`.

There is a precise algebraic obstruction to naively iterating the one-pair proof. If one tries to smooth a pair with eigenvalues `a,b` while the complementary kernel is not `D`-invariant, the two one-added-mode event probabilities need not agree. Writing

\[
h_{00},h_{10},h_{01},h_{11}
\]

for the corresponding conditional increasing-event probabilities and `g=sqrt(ab)`, the exact difference is

\[
F(a,b)-F(g,g)
=(a-g)(h_{10}-h_{00})+(b-g)(h_{01}-h_{00}).
\tag{7.2}
\]

When `a>b`, the first coefficient is positive but the second is negative. The previous proof succeeded because `D`-invariance of the complement forced

\[
h_{10}=h_{01},
\]

turning (7.2) into

\[
(\sqrt a-\sqrt b)^2(h_{10}-h_{00})\ge0.
\]

Without that equality, monotonicity alone does not control the sign. Thus a full arbitrary-`S_3` proof requires a genuinely simultaneous argument for the quotient pair and the standard sector; sequential one-pair averaging is not justified.

This is a proof obstruction, not a counterexample to (7.1).

## 8. Ledger delta and next attack

- full C0036 source: **UNCHANGED / PROVED PARTIAL**;
- candidate full `Z/6Z`: inherited unchanged;
- central `S_3`: inherited as a candidate full proof for that restricted class;
- index-two constant-coset lift: **NEW, PROVED**;
- `S_3` kernels constant on transpositions but arbitrary on `A_3`: **NEW, CANDIDATE FULL PROOF for this strictly noncentral source class**;
- arbitrary `S_3`: **OPEN in this work**.

The next useful attack is the genuinely simultaneous `S_3` midpoint problem. In `A_3`-Fourier coordinates, write

\[
Q_0=\begin{pmatrix}a_0&z_0\\z_0&a_0\end{pmatrix},\qquad
Q_1=\begin{pmatrix}a_1&z\\\bar z&a_2\end{pmatrix},\qquad
Q_2=\begin{pmatrix}a_2&\bar z\\z&a_1\end{pmatrix}.
\]

The theorem above is exactly the face `z=0`. The next attack should therefore not reprove that face: it should control the standard-sector parameter `z` simultaneously with `z_0`, either by a direct increasing-event midpoint inequality or by identifying another finite-rank stochastic symmetrization that reduces `|z|` while preserving the determinant and the already-proved quotient structure.
