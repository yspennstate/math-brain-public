Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — the requested GPT-6/maximum setting is a preference, not authenticated runtime telemetry, so I do not claim it ran.**

# C0036: a two-dimensional gauge-block symmetrization theorem and an exact obstruction to sequential `S_3` smoothing

Date: 2026-09-20 UTC  
Role: C03 / R7-03, native ID `6aabe7be74008191b526b109ee4e9e80`  
Canonical ownership: preserved; this is the complementary C03 role registered in `operations/progress_first_2026-09-20/REGISTRY.md`.  
Captured fresh master before this artifact: `bd1b9de5fb883242eb7f54c52cc73825d60035e1`.  
Previous checkpoint: `research7_2026-09-17/R7-03/runs/2026-09-20/2026-09-20T043800Z__report.md`.  
Status: **PROVED PARTIAL relative to the full source.**

## 1. Exact source target

Russell Lyons, *Determinantal Probability: Basic Properties and Conjectures* (ICM 2014), arXiv:1406.2707, Section 5.2, Conjecture 5.7.

The section works with a sofic group `Gamma`. The operator is a `Gamma`-equivariant positive contraction

\[
0\le Q\le I\quad\text{on }\ell^2(\Gamma),
\]

with group trace

\[
\operatorname{tr}_\Gamma(T)=\langle T\delta_e,\delta_e\rangle
\]

and Fuglede--Kadison determinant

\[
\operatorname{FK}_\Gamma(Q)=\exp\!\left(\operatorname{tr}_\Gamma\log|Q|\right).
\]

Writing `P^Q` for the determinantal law, the source target is stochastic domination on **every increasing event**:

\[
\boxed{
\mathbf P^{\operatorname{FK}_\Gamma(Q)I}
\preccurlyeq \mathbf P^Q
\preccurlyeq
\mathbf P^{I-\operatorname{FK}_\Gamma(I-Q)I},
}
\tag{1.1}
\]

with both product densities optimal. The source explicitly says this is open even for finite groups. Nothing below is represented as full-source closure.

## 2. Inherited `S_3` bottleneck

Let

\[
H=A_3\cong C_3\triangleleft S_3
\]

and let `D` be multiplication by the sign character on `ell^2(S_3)`. In an `H`-Fourier basis, the preceding R7-03 work writes an arbitrary Hermitian `S_3`-equivariant contraction as three two-dimensional blocks

\[
Q_0=\begin{pmatrix}a_0&z_0\\ z_0&a_0\end{pmatrix},\qquad
Q_1=\begin{pmatrix}a_1&z\\ \bar z&a_2\end{pmatrix},\qquad
Q_2=\begin{pmatrix}a_2&\bar z\\ z&a_1\end{pmatrix}.
\tag{2.1}
\]

The full operator geometric midpoint

\[
G:=Q\#(DQD)
\tag{2.2}
\]

commutes with `D`, hence is `A_3`-supported. In the positive-definite interior,

\[
G_0=\sqrt{a_0^2-z_0^2}\,I_2,
\tag{2.3}
\]

and, putting

\[
r=\sqrt{1-\frac{|z|^2}{a_1a_2}},
\]

one has

\[
G_1=\operatorname{diag}(a_1r,a_2r),\qquad
G_2=\operatorname{diag}(a_2r,a_1r).
\tag{2.4}
\]

Thus the single full-process inequality

\[
\mathbf P^{G}\preccurlyeq \mathbf P^Q
\tag{2.5}
\]

would close the arbitrary `S_3` case, because `G` factors over the two `A_3` cosets and the sharp `C_3` theorem is already available in this research chain.

The previous single-pair theorem handled only the special situation where the nonsymmetric part of `Q` was one `D`-swapped eigenpair and the whole orthogonal complement already commuted with `D`. The first goal here is to remove the unnecessary eigenpair-balance assumption in the genuinely two-dimensional active sector.

## 3. New theorem: an arbitrary two-dimensional active gauge block

### Theorem 3.1 (two-dimensional gauge-block symmetrization)

Let `E` be a finite ground set and let `D` be a diagonal unitary involution on `ell^2(E)`. Suppose there is an orthogonal `D`-invariant decomposition

\[
\ell^2(E)=W\oplus V,
\qquad \dim V=2,
\tag{3.1}
\]

such that the `+1` and `-1` eigenspaces of `D|_V` are each one-dimensional. Let

\[
Q=Q_W\oplus K,
\tag{3.2}
\]

where `0<=Q<=I`, `Q_W` commutes with `D|_W`, and `K` is an arbitrary positive contraction on `V`. Define

\[
H:=K\#(DKD),
\qquad
\widetilde Q:=Q_W\oplus H,
\tag{3.3}
\]

where `#` denotes the Kubo--Ando geometric mean (defined on the boundary by continuity).

Then

\[
\boxed{\mathbf P^{\widetilde Q}\preccurlyeq \mathbf P^Q}
\tag{3.4}
\]

on every increasing event, and

\[
\boxed{\det\widetilde Q=\det Q.}
\tag{3.5}
\]

In particular, `H` commutes with `D|_V`, so `\widetilde Q` commutes with `D`.

### Proof

Because `Q_W` and `D|_W` are commuting Hermitian operators, choose an orthonormal basis of `W` consisting of simultaneous eigenvectors. Use the standard spectral-mixture representation of a finite determinantal process: independently retain each eigenvector of `Q_W` with its eigenvalue and, independently, sample the spectral subset of the two-dimensional block `K`; conditional on the retained subspace, the process is the projection DPP onto that subspace.

Fix a retained subset of the common eigenvectors in `W`, and let `P_R` be the corresponding projection. Since each retained eigenvector is a `D`-eigenvector,

\[
DP_RD=P_R.
\tag{3.6}
\]

Fix an increasing event `A`. For a unit vector `u in V`, define

\[
h(u):=\mathbf P^{P_R+P_u}(A),
\qquad
h_0:=\mathbf P^{P_R}(A),
\qquad
h_2:=\mathbf P^{P_R+I_V}(A).
\tag{3.7}
\]

Here `P_u` is the rank-one projection onto `u`.

#### Step 1: the rank-one event functional is quadratic

A projection DPP of rank `r+1` is supported on `(r+1)`-element subsets. For each such subset `S`, its probability under `P_R+P_u` is the squared modulus of the corresponding Pluecker coordinate. With `R` fixed this is a Hermitian quadratic form in `u`. Summing those quadratic forms over all `S in A` gives a positive semidefinite Hermitian operator `N` on `V` such that

\[
h(u)=\langle u,Nu\rangle.
\tag{3.8}
\]

Since

\[
P_R\le P_R+P_u,
\]

finite-DPP monotonicity under Loewner order gives `h(u)>=h_0` for every unit `u`. Therefore

\[
M:=N-h_0I_V\succeq0.
\tag{3.9}
\]

Moreover diagonal gauge conjugation does not change a determinantal law. By (3.6),

\[
h(Du)=\mathbf P^{D(P_R+P_u)D}(A)=\mathbf P^{P_R+P_u}(A)=h(u).
\tag{3.10}
\]

Thus `M` commutes with `D|_V`. In the `D`-eigenbasis of `V`,

\[
D|_V=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad
M=\begin{pmatrix}m_+&0\\0&m_-\end{pmatrix},
\qquad m_+,m_-\ge0.
\tag{3.11}
\]

#### Step 2: exact dependence of the event probability on the active block

Let the eigenvalues/eigenvectors of `K` be `(lambda_1,u_1)` and `(lambda_2,u_2)`. Conditional on `R`, the spectral mixture in `V` has four possibilities: retain neither active eigenvector, retain only `u_1`, retain only `u_2`, or retain both. Hence

\[
\begin{aligned}
\Phi_A(K)
&:=(1-\lambda_1)(1-\lambda_2)h_0
 +\lambda_1(1-\lambda_2)h(u_1)\\
&\quad +(1-\lambda_1)\lambda_2h(u_2)
 +\lambda_1\lambda_2 h_2.
\end{aligned}
\tag{3.12}
\]

Using `h(u)=h_0+<u,Mu>` and `det K=lambda_1 lambda_2`, this simplifies exactly to

\[
\boxed{
\Phi_A(K)=h_0+\operatorname{tr}(MK)+c_A\det K,
}
\tag{3.13}
\]

where

\[
c_A:=h_2-h_0-\operatorname{tr}M.
\tag{3.14}
\]

No sign information about `c_A` is required.

#### Step 3: geometric midpoint comparison

The geometric mean is symmetric, so

\[
DHD=(DKD)\#K=K\#(DKD)=H.
\tag{3.15}
\]

Thus `H` is diagonal in the basis (3.11). Write

\[
K=\begin{pmatrix}x&w\\\bar w&y\end{pmatrix}.
\tag{3.16}
\]

Then

\[
\frac{K+DKD}{2}=\begin{pmatrix}x&0\\0&y\end{pmatrix}.
\tag{3.17}
\]

The operator arithmetic--geometric mean inequality gives

\[
H=K\#(DKD)\preceq \frac{K+DKD}{2}.
\tag{3.18}
\]

Since `H` is diagonal, if `H=diag(h_+,h_-)`, then

\[
h_+\le x,\qquad h_-\le y.
\tag{3.19}
\]

Also

\[
\det H=\sqrt{\det K\,\det(DKD)}=\det K.
\tag{3.20}
\]

Subtracting (3.13) for `H` from (3.13) for `K`, the determinant term cancels:

\[
\begin{aligned}
\Phi_A(K)-\Phi_A(H)
&=\operatorname{tr}\bigl(M(K-H)\bigr)\\
&=m_+(x-h_+)+m_-(y-h_-)\ge0.
\end{aligned}
\tag{3.21}
\]

This proves the desired event inequality conditional on every `R`; averaging over `R` proves (3.4). Equation (3.20), multiplied by the unchanged determinant of `Q_W`, proves (3.5). Singular `K` follows by approximation from `K+epsilon I` (or directly from the continuous extension of the geometric mean). Since the geometric mean is monotone and both inputs are contractions, `H<=I`, so `\widetilde Q` is again a positive contraction. `QED`

### Relation to the inherited one-pair theorem

The preceding R7-03 single-pair theorem required the active block to be diagonal in a basis that `D` swaps, equivalently to have equal diagonal entries in the `D`-eigenbasis. Theorem 3.1 allows an **arbitrary** positive `2x2` block `K`; the two diagonal entries in the `D`-eigenbasis may be unequal. Thus Theorem 3.1 strictly generalizes the finite-DPP symmetrization lemma used in the previous dihedral lifting arguments.

## 4. Group-theoretic consequence: an index-two active-sector lifting criterion

### Corollary 4.1

Let `H normal Gamma` be a finite index-two subgroup and let `D` be multiplication by the quotient sign character. Assume Lyons's lower product bound is known for every `H`-equivariant positive contraction.

Suppose a `Gamma`-equivariant positive contraction `Q` has an orthogonal `D`-invariant reducing decomposition

\[
\ell^2(\Gamma)=W\oplus V,
\qquad \dim V=2,
\tag{4.1}
\]

such that `D|_V` has one `+1` and one `-1` direction and `[Q|_W,D|_W]=0`. No balance assumption is imposed on the arbitrary active block `K=Q|_V`.

Then

\[
\boxed{
\operatorname{Ber}(\operatorname{FK}_\Gamma(Q))^{\otimes\Gamma}
\preccurlyeq \mathbf P^Q.
}
\tag{4.2}
\]

If the full two-sided theorem is available on `H`, then the sharp upper bound follows as well whenever the same active-sector hypothesis is satisfied by `I-Q` (which it is for the same reducing decomposition), so the complete two-sided conclusion holds.

### Proof

Apply Theorem 3.1 on `V`. The resulting `\widetilde Q` satisfies

\[
\mathbf P^{\widetilde Q}\preccurlyeq\mathbf P^Q,
\qquad
\det\widetilde Q=\det Q,
\qquad
D\widetilde QD=\widetilde Q.
\tag{4.3}
\]

For a convolution operator, conjugating by `D` multiplies the kernel coefficient at `g` by the quotient character `epsilon(g)`. Hence commuting with `D` means precisely that the convolution kernel is supported in `H`. Therefore `\widetilde Q` splits over the two right cosets of `H` into two unitarily identical copies of an `H`-equivariant contraction `L`:

\[
\mathbf P^{\widetilde Q}=\mathbf P^L\otimes\mathbf P^L.
\tag{4.4}
\]

With `|Gamma|=2|H|` and determinant preservation,

\[
\operatorname{FK}_\Gamma(Q)
=(\det Q)^{1/|\Gamma|}
=(\det L)^{1/|H|}
=\operatorname{FK}_H(L).
\tag{4.5}
\]

Tensor the two subgroup couplings and use (4.3). The upper bound follows by applying the same lower statement to `I-Q` and complementing configurations. Sharpness again follows from the full-set and empty-set events. `QED`

The previous constant-complementary-coset theorem is recovered when `V` is the quotient-character subspace and the complementary-coset part vanishes on `W`. Corollary 4.1 shows that the real finite-DPP mechanism is not constancy of a kernel coefficient per se; it is **two-dimensionality of the entire gauge-active sector**.

## 5. Why this still does not close arbitrary `S_3`

For a general `S_3` kernel, both the quotient block `Q_0` and the four-dimensional standard sector `Q_1\oplus Q_2` can fail to commute with `D`. Thus, if one tries to apply Theorem 3.1 to `Q_0` while leaving the standard sector untouched, the orthogonal complement does **not** satisfy the commuting hypothesis. The same problem occurs in the opposite order.

This is not merely a technical gap: quotient-first sequential smoothing can reverse the desired stochastic order.

## 6. Exact obstruction to quotient-first sequential smoothing on `S_3`

Choose the block parameters

\[
a_0=\frac58,\qquad z_0=\frac38,
\tag{6.1}
\]

and

\[
a_1=\frac14,\qquad a_2=\frac12,\qquad
z=\frac{1+i}{10}.
\tag{6.2}
\]

Thus

\[
Q_0=\begin{pmatrix}5/8&3/8\\3/8&5/8\end{pmatrix},
\qquad
Q_1=\begin{pmatrix}1/4&(1+i)/10\\(1-i)/10&1/2\end{pmatrix},
\tag{6.3}
\]

with `Q_2` the companion block required by (2.1).

The eigenvalues of `Q_0` are `1` and `1/4`. For `Q_1`,

\[
\det Q_1=\frac18-\frac1{50}=\frac{21}{200}>0,
\tag{6.4}
\]

while

\[
\det(I-Q_1)=\frac34\frac12-\frac1{50}=\frac{71}{200}>0.
\tag{6.5}
\]

The same holds for `Q_2`. Hence `0<=Q<=I`.

Now perform only the quotient-block geometric symmetrization, leaving `Q_1,Q_2` unchanged. Since

\[
\sqrt{a_0^2-z_0^2}
=\sqrt{\frac{25-9}{64}}
=\frac12,
\]

this gives

\[
\widehat Q_0=\frac12I_2,
\qquad
\widehat Q_1=Q_1,
\qquad
\widehat Q_2=Q_2.
\tag{6.6}
\]

The determinant is preserved.

Let `s_1,s_2` be two distinct transpositions and let `A` be the left-translation-invariant increasing event generated by the three-set

\[
T=\{e,s_1,s_2\}:
\qquad
A=\bigcup_{g\in S_3}\{gT\subseteq X\}.
\tag{6.7}
\]

This is a genuine increasing event. Exact evaluation by inclusion--exclusion over the translated generating triples and the determinantal inclusion formula `P[T subset X]=det Q_T` gives

\[
\mathbf P^Q(A)
=\frac{26291-908\sqrt3}{96000},
\tag{6.8}
\]

whereas

\[
\mathbf P^{\widehat Q}(A)
=\frac{7973+160\sqrt3}{32000}.
\tag{6.9}
\]

Consequently

\[
\boxed{
\mathbf P^Q(A)-\mathbf P^{\widehat Q}(A)
=\frac{593-347\sqrt3}{24000}<0.
}
\tag{6.10}
\]

The sign is exact because

\[
3\cdot347^2=361227>351649=593^2.
\tag{6.11}
\]

Therefore

\[
\boxed{\mathbf P^{\widehat Q}\not\preccurlyeq \mathbf P^Q.}
\tag{6.12}
\]

This **refutes the quotient-first sequential proof route** for arbitrary `S_3`. It does not refute the simultaneous midpoint conjecture (2.5), because `\widehat Q` is not the full midpoint `Q#(DQD)`: the standard sector has deliberately been left unsymmetrized.

This exact example also pinpoints why the commuting-complement hypothesis in Theorem 3.1 is substantive rather than cosmetic. Cross-sector compensation can be necessary even when each sector separately admits a determinant-preserving geometric midpoint.

## 7. What remains plausible, and what is not being claimed

The exact counterexample (6.10) rules out one natural global proof strategy but not Lyons's conjecture and not the full `S_3` midpoint inequality.

A bounded numerical search during this run evaluated the simultaneous midpoint against all left-translation-invariant upper-set tests for many interior `S_3` contractions and found no genuine violation. This is **supporting evidence only**, not a proof and not source progress by itself. It is not used in any theorem above.

A particularly promising analytic face is

\[
z_0=0,
\tag{7.1}
\]

where the quotient sector already commutes with `D` and only the standard sector is active. On that face, write the three real transposition coefficients as `x_1,x_2,x_3` with

\[
x_1+x_2+x_3=0.
\tag{7.2}
\]

If `r` is the standard-sector midpoint contraction factor from (2.4), the Fourier relation is

\[
|z|^2=a_1a_2(1-r^2)
=3(x_1^2+x_2^2+x_1x_2).
\tag{7.3}
\]

The midpoint sets all transposition coefficients to zero and replaces the standard Fourier eigenvalues by `ra_1,ra_2`. Exact symbolic reduction of representative invariant upper-set differences already yields positive factors in simple cases, e.g.

\[
2a_0^2a_1a_2r^2(a_1+a_2)(1-r)\ge0
\tag{7.4}
\]

and

\[
2a_0a_1a_2(1-r^2)\ge0.
\tag{7.5}
\]

These identities are recorded only as guideposts for the next proof; they are not claimed to settle all invariant upper sets on the face.

## 8. Literature/status check and ledger delta

The primary Lyons paper remains the controlling source. A bounded current check also recovered the related Lyons--Thom monotone-coupling theorem for operator order and later determinantal negative-dependence/BK literature, but no source-matching resolution of Conjecture 5.7 was identified. Failure to find a resolution is not a certificate of worldwide openness or novelty.

Ledger delta:

- full C0036 source: **UNCHANGED / PROVED PARTIAL**;
- candidate full `Z/6Z`: inherited unchanged;
- index-two constant-coset theorem: inherited unchanged;
- arbitrary two-dimensional active gauge-block full-process symmetrization: **NEW, PROVED**;
- index-two two-dimensional-active-sector lifting criterion: **NEW, PROVED**, conditional only on the subgroup source theorem;
- arbitrary `S_3`: **OPEN in this work**;
- quotient-first sequential `S_3` symmetrization: **REFUTED as a proof route by the exact increasing-event example (6.1)--(6.12)**;
- simultaneous `S_3` geometric midpoint order: **OPEN / plausible, not proved**.

## 9. Next attack

Do not retry sequential quotient smoothing. The next useful target is the full-process midpoint inequality on the codimension-one face `z_0=0`, where only the standard sector is gauge-active. Prove it by reducing all translation-invariant upper-set differences to the constraint (7.3), or replace that enumeration by a multiplicity-two active-sector theorem that couples the conjugate standard blocks simultaneously. A proof on this face would give a genuinely new full `S_3` restricted class and isolate exactly the cross-sector compensation needed for the remaining arbitrary case.