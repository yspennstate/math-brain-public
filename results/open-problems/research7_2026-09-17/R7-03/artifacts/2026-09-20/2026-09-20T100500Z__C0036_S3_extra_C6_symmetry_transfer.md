Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — the requested GPT-6/maximum setting is a preference, not authenticated runtime telemetry, so I do not claim it ran.**

# C0036: a second regular-group symmetry transfers the full `Z/6Z` result to a new nonabelian `S_3` class

Date: 2026-09-20 UTC  
Role: C03 / R7-03, native ID `6aabe7be74008191b526b109ee4e9e80`  
Canonical ownership: preserved; this is the explicitly complementary role registered in `operations/progress_first_2026-09-20/REGISTRY.md`.  
Captured fresh master before this artifact: `8e565f20c41ea44172a6f3b03917cd476da59f89`.  
Previous own checkpoint: `research7_2026-09-17/R7-03/runs/2026-09-20/2026-09-20T070500Z__report.md`.  
Status: **PROVED structural transfer lemma; CANDIDATE FULL PROOF for the stated `S_3` subclass conditional only on the inherited candidate full `Z/6Z` theorem; PROVED PARTIAL relative to full C0036.**

## 1. Exact outside target

Russell Lyons, *Determinantal Probability: Basic Properties and Conjectures*, Proc. ICM 2014, arXiv:1406.2707, Section 5.2, Conjecture 5.7, <https://arxiv.org/abs/1406.2707>.

Section 5.2 fixes a sofic group `Gamma`. The conjecture ranges over every `Gamma`-equivariant positive contraction

\[
0\le Q\le I\qquad\text{on }\ell^2(\Gamma),
\]

with group trace

\[
\operatorname{tr}_\Gamma(T)=\langle T\delta_e,\delta_e\rangle
\]

and Fuglede--Kadison determinant

\[
\operatorname{FK}_\Gamma(Q)=\exp\!\bigl(\operatorname{tr}_\Gamma\log|Q|\bigr).
\]

The source asks for the sharp stochastic domination on every increasing event

\[
\mathbf P^{\operatorname{FK}_\Gamma(Q)I}
\preccurlyeq \mathbf P^Q
\preccurlyeq
\mathbf P^{I-\operatorname{FK}_\Gamma(I-Q)I}.
\tag{1.1}
\]

For a finite group of order `n`, the normalized group trace is `Tr/n`, hence

\[
\operatorname{FK}_\Gamma(Q)=(\det Q)^{1/n}.
\tag{1.2}
\]

The source says Conjecture 5.7 is open even for finite groups. A bounded literature check dated 2026-09-20 again found related determinantal/operator-order work but no source-matching resolution; that negative search is not a proof of worldwide openness.

## 2. Inherited facts and the unresolved implication

The R7-03 chain already contains:

1. a **candidate full proof on `Z/6Z`** for every circulant positive contraction and every increasing event, with an exact finite certificate (`2026-09-20T022700Z__report.md`);
2. a full-process theorem on the mean-zero-transposition face of arbitrary `S_3` kernels (`2026-09-20T070500Z__report.md`);
3. a constant-transposition-coset/index-two class and several other structured `S_3` subclasses.

Arbitrary `S_3` is still open in this work. The previous run attacked the simultaneous sign-gauge midpoint directly. This run changes viewpoint: instead of forcing every `S_3` kernel through that midpoint, look for kernels carrying a **second regular group symmetry**. On such a class the already-developed `Z/6Z` theorem transfers without another 76-event expansion.

## 3. General finite regular-symmetry transfer lemma

### Lemma 3.1

Let `E` be a finite set of cardinality `n`. Suppose two groups `Gamma` and `Lambda`, each of order `n`, act regularly on `E`. Let `Q` be a positive contraction on `ell^2(E)` that is equivariant for both regular actions. If the sharp Lyons product domination theorem is known for the `Lambda`-equivariant kernel `Q`, then the same two-sided conclusion holds when `Q` is viewed as a `Gamma`-equivariant kernel.

### Proof

The determinantal law `P^Q` depends only on the matrix `Q` in the coordinate basis indexed by `E`; it does not depend on which regular group action is used to describe its equivariance. Likewise, because both groups are finite of the same order `n`, their canonical regular normalized traces are the same ordinary normalized matrix trace:

\[
\operatorname{tr}_\Gamma(T)=\operatorname{tr}_\Lambda(T)=\frac1n\operatorname{Tr}(T)
\]

for every operator commuting with the relevant regular action, and in particular

\[
\operatorname{FK}_\Gamma(Q)=\operatorname{FK}_\Lambda(Q)=(\det Q)^{1/n},
\]

\[
\operatorname{FK}_\Gamma(I-Q)=\operatorname{FK}_\Lambda(I-Q)=(\det(I-Q))^{1/n}.
\]

Therefore the two product comparators and the middle determinantal law are literally identical probability measures under the two descriptions. Any all-increasing-event stochastic domination theorem for the `Lambda` description is exactly the desired theorem for the `Gamma` description. ∎

This trivial-looking lemma is useful here because `S_3` and `C_6` have the same order but inequivalent regular group structures.

## 4. A new explicit `S_3` family with a hidden regular `C_6` symmetry

Write

\[
S_3=D_3=\langle r,s\mid r^3=s^2=1,\ srs=r^{-1}\rangle
\]

and let a Hermitian `S_3`-equivariant convolution kernel be

\[
q(e)=u\in\mathbb R,
\qquad q(r)=v,
\qquad q(r^2)=\bar v,
\]

\[
q(s)=x_0,\qquad q(rs)=x_1,\qquad q(r^2s)=x_2,
\qquad x_0,x_1,x_2\in\mathbb R.
\tag{4.1}
\]

Assume

\[
\boxed{v\in\mathbb R,\qquad x_0=x_2.}
\tag{4.2}
\]

No condition is imposed on `x_1`, and in particular neither the previous mean-zero condition `x_0+x_1+x_2=0` nor the constant-coset condition `x_0=x_1=x_2` is required.

Order the six points by

\[
c_0=e,\quad c_1=s,\quad c_2=r,\quad c_3=rs,\quad c_4=r^2,\quad c_5=r^2s.
\tag{4.3}
\]

Let `sigma` be the six-cycle

\[
\sigma:c_j\mapsto c_{j+1\pmod 6}.
\tag{4.4}
\]

The `S_3` convolution matrix has entries

\[
Q_{ij}=q(c_i^{-1}c_j).
\tag{4.5}
\]

A direct group multiplication table gives the difference-index table

\[
\begin{array}{c|cccccc}
 &c_0&c_1&c_2&c_3&c_4&c_5\\\hline
c_0& e&s&r&rs&r^2&r^2s\\
c_1& s&e&r^2s&r^2&rs&r\\
c_2& r^2&r^2s&e&s&r&rs\\
c_3& rs&r&s&e&r^2s&r^2\\
c_4& r&rs&r^2&r^2s&e&s\\
c_5& r^2s&r^2&rs&r&s&e
\end{array}
\tag{4.6}
\]

where the `(i,j)` entry is `c_i^{-1}c_j`.

Under (4.2), set

\[
a:=q(r)=q(r^2)=v,\qquad x:=q(s)=q(r^2s)=x_0,\qquad y:=q(rs)=x_1.
\]

Then the first row of `Q` in ordering (4.3) is

\[
[u,x,a,y,a,x],
\tag{4.7}
\]

and (4.6) shows that every subsequent row is the cyclic right shift of the preceding row. Hence

\[
\boxed{Q\sigma=\sigma Q,}
\tag{4.8}
\]

so `Q` is not only `S_3`-equivariant but also a Hermitian circulant `C_6`-equivariant positive contraction on the same six-point set.

### Theorem 4.1

Assume the inherited candidate `Z/6Z` theorem from the R7-03 chain. Then every `S_3`-equivariant positive contraction satisfying (4.2) obeys the complete sharp Lyons bounds

\[
\boxed{
\operatorname{Ber}(\operatorname{FK}_{S_3}(Q))^{\otimes S_3}
\preccurlyeq \mathbf P^Q
\preccurlyeq
\operatorname{Ber}\!\left(1-\operatorname{FK}_{S_3}(I-Q)\right)^{\otimes S_3}.
}
\tag{4.9}
\]

### Proof

By (4.8), `Q` is a `C_6`-equivariant positive contraction. Apply the inherited all-events two-sided `C_6` theorem. Lemma 3.1 identifies the two FK product densities with the `S_3` quantities because both regular actions have six points. This yields (4.9), including sharpness of the constants. ∎

## 5. Conjugate versions: any equal pair of transposition coefficients

Conjugation by powers of `r` cyclically permutes the three transpositions and preserves the condition `q(r)=q(r^2)` when this common value is real. Therefore Theorem 4.1 immediately gives:

### Corollary 5.1

If

\[
q(r)=q(r^2)\in\mathbb R
\tag{5.1}
\]

and **any two** of

\[
q(s),\ q(rs),\ q(r^2s)
\tag{5.2}
\]

are equal, then `Q` has, after a coordinate permutation, a regular `C_6` symmetry and hence satisfies the full sharp two-sided Lyons domination, conditional only on the inherited candidate `C_6` theorem.

This is a union of three explicit four-real-parameter families inside the six-real-parameter space of Hermitian `S_3` convolution kernels.

## 6. This family is genuinely outside the previously closed faces

Take for example

\[
q(e)=\frac12,\qquad
q(r)=q(r^2)=\frac1{20},
\]

\[
q(s)=q(r^2s)=\frac1{30},\qquad
q(rs)=-\frac1{60}.
\tag{6.1}
\]

The sum of the three transposition coefficients is

\[
\frac1{30}-\frac1{60}+\frac1{30}=\frac1{20}\ne0,
\]

so this kernel is **not** on the mean-zero-transposition face. The transposition coefficients are not all equal, so it is **not** in the previous constant-coset class either.

It is nevertheless an interior positive contraction. Indeed every row has diagonal `1/2` and total off-diagonal absolute sum

\[
2\cdot\frac1{20}+2\cdot\frac1{30}+\frac1{60}
=\frac{11}{60}<\frac12.
\]

By the Hermitian Gershgorin theorem every eigenvalue lies in

\[
\left[\frac12-\frac{11}{60},\frac12+\frac{11}{60}\right]
=\left[\frac{19}{60},\frac{41}{60}\right]\subset(0,1).
\tag{6.2}
\]

Thus Theorem 4.1 adds genuinely new `S_3` operators with both quotient and standard sign-gauge sectors active.

## 7. Structural interpretation

The important point is not the particular equality `x_0=x_2`; it is the existence of a **second regular symmetry**. The direct simultaneous-midpoint attack sees noncommutative cross-sector compensation. On the subclass above, that difficulty disappears because the same six-point operator lives in the commutant of a regular cyclic action, where the earlier Fourier-reflection argument already gives all-event stochastic domination.

Equivalently: some apparently nonabelian `S_3` kernels are secretly abelian at the level of their full coordinate symmetry algebra even though their original convolution coefficients are noncentral.

This also suggests a broader search principle for finite groups: before expanding all invariant upper sets, search for intersections of regular commutant algebras with finite groups for which the conjecture has already been established. Such intersections transfer the theorem at essentially zero stochastic cost.

## 8. Honest status and remaining gap

- Full Lyons C0036 source: **PROVED PARTIAL / unchanged at the all-group level**.
- Full `Z/6Z`: inherited **CANDIDATE FULL PROOF**, pending independent review.
- Arbitrary `S_3`: **OPEN in this work**.
- Mean-zero-transposition `S_3` face: inherited **CANDIDATE FULL PROOF for that restricted class**.
- New hidden-`C_6` `S_3` families (5.1)--(5.2): **NEW CANDIDATE FULL PROOF for these restricted classes**, conditional only on the inherited `Z/6Z` candidate theorem.
- Structural regular-symmetry transfer Lemma 3.1 and the explicit circulant identification (4.6)--(4.8): **PROVED**.

No claim is made that this resolves arbitrary `S_3`, and this is not an independent audit of the inherited `Z/6Z` certificate.

## 9. Next attack

The new class handles a rank-three sign-gauge-active situation that is outside both previously closed faces. The next useful step is to exploit it as an exact boundary/base manifold for arbitrary `S_3`:

1. write a general Hermitian `S_3` kernel as the hidden-`C_6` part plus the two symmetry-breaking coordinates
   \[
   \Im q(r),\qquad q(s)-q(r^2s)
   \]
   (after choosing the closest equal-transposition pair);
2. derive the simultaneous-midpoint event difference to second order in those two defects while retaining exact dependence on the four hidden-`C_6` coordinates;
3. test whether the first variation vanishes by the cyclic symmetry and whether the resulting Hessian is positive on the full feasible hidden-`C_6` base;
4. if the Hessian is uniformly positive away from natural degeneracy faces, bootstrap to a genuine open neighborhood of the four-dimensional class; otherwise an exact negative direction will identify the first obstruction.

This is a materially different route from another raw 76-event expansion.