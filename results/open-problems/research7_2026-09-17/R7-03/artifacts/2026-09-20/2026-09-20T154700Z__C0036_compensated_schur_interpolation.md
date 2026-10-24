Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — the requested GPT-6/maximum setting is a preference, not authenticated runtime telemetry, so I do not claim it ran.**

# C0036: compensated Schur interpolation is globally stochastically monotone

Date: 2026-09-20 UTC  
Role: C03 / R7-03, native ID `6aabe7be74008191b526b109ee4e9e80`  
Canonical ownership: preserved; this is the explicitly complementary progress-first role registered in `operations/progress_first_2026-09-20/REGISTRY.md`.  
Status: **PROVED PARTIAL** relative to Lyons Conjecture 5.7. The finite-DPP theorem below is proved analytically here and is stronger than the preceding endpoint block-Schur decoupling theorem, but it has not yet received an independent review.

## 1. Exact outside source target

Russell Lyons, *Determinantal Probability: Basic Properties and Conjectures*, Proc. ICM 2014, arXiv:1406.2707, Section 5.2, Conjecture 5.7.

Section 5.2 fixes a **sofic group** `Gamma`. The conjecture ranges over every `Gamma`-equivariant positive contraction

\[
0\le Q\le I\quad\text{on }\ell^2(\Gamma),
\]

with

\[
\operatorname{tr}_\Gamma(T)=\langle T\delta_e,\delta_e\rangle,
\qquad
\operatorname{FK}_\Gamma(Q)=\exp\!\left(\operatorname{tr}_\Gamma\log|Q|\right),
\]

and asks for the sharp all-increasing-event sandwich

\[
\mathbf P^{\operatorname{FK}_\Gamma(Q)I}
\preccurlyeq \mathbf P^Q
\preccurlyeq
\mathbf P^{I-\operatorname{FK}_\Gamma(I-Q)I}.
\tag{1.1}
\]

For finite `Gamma` of order `n`, `FK_Gamma(Q)=(det Q)^(1/n)`. Lyons states immediately before Conjecture 5.7 that the conjecture is open even for finite groups. A bounded fresh source check this run recovered arXiv:1406.2707 and did not locate a later exact resolution; absence from that bounded search is not treated as proof of worldwide openness.

The immediately preceding R7-03 checkpoint proved the endpoint block-Schur theorem

\[
\mathbf P^{A\oplus C}\preccurlyeq \mathbf P^Q,
\qquad C=D-X^*A^{-1}X,
\]

and used it to reduce arbitrary `S_3` to a two-coset lower product plus a missing cross-coset compensation term. An explicit `S_3` event showed that the decoupled lower product alone can fall below the uniform Lyons comparator even though the original DPP remains well above it. The first attack here is therefore to retain the cross-coset coupling and ask whether the local Schur/Hessian stability can be upgraded to a **global** comparison along a determinant-preserving interpolation.

## 2. Main theorem: compensated Schur interpolation

Let a finite ground set split as

\[
E=F\sqcup B,
\]

and first assume the strict case `0<Q<I`. Write

\[
Q=
\begin{pmatrix}
A & X\\
X^* & D
\end{pmatrix},
\qquad
C:=D-X^*A^{-1}X.
\tag{2.1}
\]

Put

\[
M:=X^*A^{-1}X
\]

and, for `0<=t<=1`, define

\[
Q_t:=
\begin{pmatrix}
A & tX\\
tX^* & C+t^2M
\end{pmatrix}.
\tag{2.2}
\]

Thus

\[
Q_0=A\oplus C,
\qquad
Q_1=Q.
\]

### Theorem 2.1 — global compensated Schur monotonicity

For every `0<=s<=t<=1`,

\[
\boxed{\mathbf P^{Q_s}\preccurlyeq \mathbf P^{Q_t}.}
\tag{2.3}
\]

Every point of the path is a positive contraction and the determinant is constant:

\[
\boxed{0<Q_t<I,\qquad \det Q_t=\det Q.}
\tag{2.4}
\]

Consequently the endpoint block-Schur theorem is not merely an endpoint comparison. Turning on an arbitrary block coupling by `t`, while adding the exactly compensating quadratic term `t^2X^*A^{-1}X` to keep the Schur complement fixed, increases the **entire DPP** monotonically on every increasing event, all the way from `t=0` to `t=1`.

This is the requested global version of the local stability direction. No Hessian sign extrapolation is needed: the complete path is monotone.

## 3. Positivity, contraction, and determinant preservation

The Schur complement of the `A` block in `Q_t` is exactly `C` for every `t`:

\[
C+t^2M-t^2X^*A^{-1}X=C.
\]

Since `A>0` and `C>0`, this proves `Q_t>0`.

For the upper contraction bound, write

\[
I-Q_t=
\begin{pmatrix}
I-A & -tX\\
-tX^* & I-C-t^2M
\end{pmatrix}.
\]

Its Schur complement with respect to `I-A` is

\[
I-C-t^2\Bigl(M+X^*(I-A)^{-1}X\Bigr).
\tag{3.1}
\]

At `t=1` this is the positive Schur complement of `I-Q`; for `0<=t<=1` it is larger by

\[
(1-t^2)\Bigl(M+X^*(I-A)^{-1}X\Bigr)\succeq0.
\]

Hence `I-Q_t>0`.

Finally, the Schur determinant formula gives

\[
\det Q_t=\det A\,\det C=\det Q
\tag{3.2}
\]

for every `t`.

Thus the path moves only stochastic dependence/cross-block compensation: it leaves the determinant, and therefore the finite Lyons lower density `(det Q)^(1/|E|)`, unchanged.

## 4. Exact conditional-kernel formula

The decisive point is that the marginal law on `F` does not depend on `t`, because `(Q_t)_F=A`. Fix an exact configuration

\[
S\subseteq F,
\qquad
Z:=F\setminus S.
\]

Condition first on all points of `S` being present. Define

\[
R_S:=A_Z-A_{Z,S}A_S^{-1}A_{S,Z},
\tag{4.1}
\]

and

\[
U_S:=X_Z-A_{Z,S}A_S^{-1}X_S.
\tag{4.2}
\]

Here `R_S` is the conditional kernel on `Z` after forcing `S` present. Since `0<A<I`, one has `0<R_S<I` whenever `Z` is nonempty.

After forcing `S` present, the `B` block is

\[
C+t^2\Bigl(M-X_S^*A_S^{-1}X_S\Bigr),
\]

the `Z-B` cross block is `tU_S`, and the `Z` block is `R_S`. Conditioning also on `Z` being absent therefore adds

\[
t^2U_S^*(I-R_S)^{-1}U_S.
\]

The block inverse identity gives

\[
M-X_S^*A_S^{-1}X_S
=U_S^*R_S^{-1}U_S.
\tag{4.3}
\]

Hence the **exact** conditional DPP kernel on `B`, given `Y_t\cap F=S`, is

\[
\boxed{
K_{B\mid S}(t)=C+t^2H_S,
}
\tag{4.4}
\]

where

\[
\boxed{
H_S
:=U_S^*\Bigl(R_S^{-1}+(I-R_S)^{-1}\Bigr)U_S
=U_S^*\bigl(R_S(I-R_S)\bigr)^{-1}U_S
\succeq0.
}
\tag{4.5}
\]

For `S=F`, take `H_F=0`. The formula for `S=emptyset` is the evident special case with `R_emptyset=A` and `U_emptyset=X`.

This formula identifies the cross-block compensation exactly. It is not an unspecified positive remainder: every exact `F`-configuration has a fixed positive semidefinite compensation matrix `H_S`, and the interpolation scales it by precisely `t^2`.

## 5. Proof of full stochastic monotonicity

Let `Y_t~P^{Q_t}`. Its `F`-marginal is always `P^A`. Therefore we may couple `Y_s` and `Y_t` by first sampling a **common** exact configuration `S` on `F` with law `P^A`.

Conditional on this common `S`, (4.4) gives

\[
K_{B\mid S}(s)=C+s^2H_S
\preceq
C+t^2H_S=K_{B\mid S}(t).
\]

Determinantal kernel monotonicity yields a monotone conditional coupling on `B`. Keeping the common `F`-configuration fixed gives

\[
Y_s\subseteq Y_t
\]

almost surely under the resulting coupling. This proves (2.3) for every increasing event.

Equivalently, if `mathcal U` is any increasing event and

\[
\mathcal U_S:=\{T\subseteq B:S\cup T\in\mathcal U\},
\]

then the entire event probability has the exact disintegration

\[
\boxed{
\mathbf P^{Q_t}(\mathcal U)
=
\sum_{S\subseteq F}
\mathbf P^A(Y_F=S)\,
\mathbf P^{C+t^2H_S}(\mathcal U_S),
}
\tag{5.1}
\]

and every summand is nondecreasing in `t`.

The boundary case `0<=Q<=I` follows by the same regularization used in the previous checkpoint,

\[
Q^{(\varepsilon)}=(1-2\varepsilon)Q+\varepsilon I,
\]

followed by continuity of finite DPP probabilities. Thus the theorem extends to the closed contraction body with generalized Schur complements.

## 6. Local Hessian stability becomes global along the correct path

Write `u=t^2`. Formula (5.1) says

\[
F_{\mathcal U}(u)
:=\mathbf P^{Q_{\sqrt u}}(\mathcal U)
=
\sum_S \mu_A(S)\,
\mathbf P^{C+uH_S}(\mathcal U_S).
\tag{6.1}
\]

For every increasing event, `F_mathcalU(u)` is nondecreasing on the **whole interval** `[0,1]`.

At an interior point where directional derivatives are written classically,

\[
F'_{\mathcal U}(u)
=
\sum_S\mu_A(S)\,
D_{H_S}\mathbf P^{C+uH_S}(\mathcal U_S)
\ge0.
\tag{6.2}
\]

In the original parameter `t`, the first derivative at `t=0` vanishes and

\[
\boxed{
\frac{d^2}{dt^2}\mathbf P^{Q_t}(\mathcal U)\Big|_{t=0}
=2\sum_S\mu_A(S)\,
D_{H_S}\mathbf P^C(\mathcal U_S)
\ge0.
}
\tag{6.3}
\]

So the earlier local-Hessian phenomenon was pointing at a real global structure, but only after choosing the determinant-preserving **Schur-compensated** path. A generic linear spectral interpolation need not have this property and should not be used to extrapolate local positivity.

## 7. Consequence for the arbitrary `S_3` bottleneck

Take

\[
\Gamma=S_3,
\qquad H=A_3\cong C_3,
\]

and split the six coordinates into the two `A_3` cosets. For an arbitrary `S_3`-equivariant contraction `Q`, let `A` be the first coset block and `C` the Schur complement of that block. The preceding checkpoint already showed that, conditional on the inherited candidate full `C_3` theorem,

\[
\mathbf P^{A\oplus C}
\]

has a blockwise Bernoulli lower bound with coset densities `a,c` satisfying

\[
ac=p^2,
\qquad p=(\det Q)^{1/6}.
\]

That blockwise product does not by itself dominate `Ber(p)^6`; the prior exact `hit both cosets` example proved this failure.

The present theorem now identifies **all information discarded at that endpoint**. There is a canonical path

\[
Q_0=A\oplus C
\rightsquigarrow
Q_1=Q
\]

with constant determinant and

\[
\mathbf P^{Q_0}\preccurlyeq
\mathbf P^{Q_t}\preccurlyeq
\mathbf P^{Q_1}
\qquad(0\le t\le1),
\tag{7.1}
\]

and for every exact first-coset configuration `S`, the second-coset conditional kernel is exactly

\[
C+t^2H_S,
\qquad H_S\succeq0.
\tag{7.2}
\]

Thus the remaining arbitrary-`S_3` lower-bound problem is no longer an unspecified cross-coset effect. For each of the 76 invariant upper sets `mathcal U`, the missing compensation is the explicit nonnegative quantity

\[
\boxed{
\Delta_{\mathcal U}
=
\sum_S\mu_A(S)
\left[
\mathbf P^{C+H_S}(\mathcal U_S)
-
\mathbf P^C(\mathcal U_S)
\right].
}
\tag{7.3}
\]

The target is to show that this compensation is at least the deficit of the Schur-decoupled/blockwise product comparator relative to `Ber(p)^6`. This is a sharper obligation than another spectral expansion.

## 8. A second new route: random-order Schur pivots and the Shapley-product lemma

The endpoint block theorem also gives a promising finite-group reduction that is worth recording precisely, without promoting it to a theorem before the missing all-event inequality is proved.

For a strict finite contraction `Q` on `n` points and a permutation `pi=(pi_1,...,pi_n)`, put

\[
P_j^\pi=\{\pi_1,\ldots,\pi_j\},
\qquad
 d_{\pi_j}^\pi
=\frac{\det Q_{P_j^\pi}}{\det Q_{P_{j-1}^\pi}}.
\tag{8.1}
\]

The previous block theorem proves, for every `pi`,

\[
\mu_\pi:=\bigotimes_i\operatorname{Ber}(d_i^\pi)
\preccurlyeq
\mathbf P^Q,
\qquad
\prod_i d_i^\pi=\det Q.
\tag{8.2}
\]

Hence the random-order mixture

\[
\nu_Q:=\frac1{n!}\sum_\pi\mu_\pi
\tag{8.3}
\]

also satisfies `nu_Q <= P^Q` stochastically.

Now let

\[
g(S):=\log\det Q_S.
\]

Hadamard--Fischer makes `g` submodular. The vectors

\[
x_i^\pi:=\log d_i^\pi
\]

are exactly the greedy/marginal vectors of this submodular set function, and their permutation average is its Shapley vector.

If `Q` is equivariant under a transitive coordinate action, invariance forces that Shapley vector to be constant. Since every greedy vector has coordinate sum `log det Q`,

\[
\frac1{n!}\sum_\pi x_i^\pi
=\frac1n\log\det Q
=\log p,
\qquad
p=(\det Q)^{1/n}.
\tag{8.4}
\]

This immediately gives a rigorous but still only necessary family of inequalities. For every coordinate subset `T`,

\[
\nu_Q(T\subseteq X)
=
\frac1{n!}\sum_\pi
\exp\!\left(\sum_{i\in T}x_i^\pi\right)
\ge
\exp\!\left(
\sum_{i\in T}\frac1{n!}\sum_\pi x_i^\pi
\right)
=p^{|T|}
\tag{8.5}
\]

by Jensen. Thus the random-order lower mixture already dominates the uniform product on **every principal inclusion event**.

The exact missing statement is now isolated:

> **Shapley-product lemma (CONJECTURAL).** For a submodular `g` with all greedy increments nonpositive, let `x^pi` be its greedy vectors and `bar x` their permutation average. Is the mixture of product Bernoulli laws with parameters `exp(x_i^pi)` stochastically above the single product law with parameters `exp(bar x_i)` on every increasing event?

If this lemma is true, then for every finite transitive/equivariant DPP, (8.4) would give

\[
\operatorname{Ber}(p)^{\otimes n}
\preccurlyeq
\nu_Q
\preccurlyeq
\mathbf P^Q,
\]

settling the **lower half of Lyons 5.7 for every finite group**; applying the same result to `I-Q` would give the upper half. This implication is exact, so the lemma must not be claimed from principal-inclusion checks alone.

There is one structural reason the lemma is plausible and one clear place where proof is still missing. For any increasing event `mathcal U`, the product probability

\[
\Phi_{\mathcal U}(x)
:=\mathbf P_{\otimes_i\operatorname{Ber}(e^{x_i})}(\mathcal U)
\]

is convex on every line `x_i+x_j=constant` with all other coordinates fixed: after conditioning on the other coordinates, an increasing two-bit section is one of `0,1, AND, i, j, OR`, whose probabilities are respectively `0,1,e^{x_i+x_j},e^{x_i},e^{x_j},e^{x_i}+e^{x_j}-e^{x_i+x_j}`. Each is convex along the fixed-sum line. The greedy vectors are vertices of the generalized permutahedron/base polytope of `g`, whose edges are exactly parallel to such coordinate-transfer directions. What is **not yet proved** is the required Jensen inequality from edgewise convexity at the uniform greedy-vertex barycenter. Establishing that generalized-permutahedron Jensen step, or finding a counterexample, is the next high-value pivot.

## 9. What changed and what remains open

### New proved mathematics

1. The determinant-preserving Schur interpolation `Q_t` is a positive contraction for every `t`.
2. `det Q_t` is exactly constant.
3. For every exact configuration on the retained block, the complementary conditional kernel is `C+t^2H_S` with an explicit `H_S>=0`.
4. Therefore `P^{Q_s} <= P^{Q_t}` for **all increasing events** whenever `s<=t`.
5. The local Hessian sign along this compensated direction is the boundary value of a genuinely global monotone path.
6. For arbitrary `S_3`, the lost cross-coset compensation is now the exact quantity (7.3), not an unnamed remainder.
7. The random-order Schur-pivot mixture `nu_Q` is a rigorous stochastic lower bound and, under transitivity, dominates the uniform Lyons product on every principal inclusion event by the Shapley/Jensen calculation (8.5).

### Still open

- The full all-increasing-event comparison for arbitrary `S_3` is not proved.
- The Shapley-product lemma is not proved; principal inclusion inequalities do not imply stochastic domination.
- Arbitrary finite groups and the original all-sofic-group C0036 remain open in this work.

The next run should attack the Shapley-product lemma directly, first by trying to prove the generalized-permutahedron barycenter Jensen statement using successive coordinate-transfer/edge decompositions. If that fails, produce an explicit submodular counterexample and return to (7.3), where the `S_3` compensation is now fully quantified.
