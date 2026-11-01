Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — the requested GPT-6/maximum setting is a preference, not authenticated runtime telemetry, so I do not claim it ran.**

# C0036: block Schur decoupling and a normal-subgroup reduction for Lyons domination

Date: 2026-09-20 UTC  
Role: C03 / R7-03, native ID `6aabe7be74008191b526b109ee4e9e80`  
Canonical ownership: preserved; this is the explicitly complementary progress-first role registered in `operations/progress_first_2026-09-20/REGISTRY.md`.  
Status: **PROVED PARTIAL** relative to Lyons Conjecture 5.7. The finite-DPP lemmas below are proved analytically in this note, but have not yet received an independent review.

## 1. Exact outside source target

Russell Lyons, *Determinantal Probability: Basic Properties and Conjectures*, Proc. ICM 2014, arXiv:1406.2707, Section 5.2, Conjecture 5.7.

Section 5.2 fixes a **sofic group** `Gamma`. The conjecture ranges over every `Gamma`-equivariant positive contraction

\[
0\le Q\le I\quad\text{on }\ell^2(\Gamma),
\]

with group trace and Fuglede--Kadison determinant

\[
\operatorname{tr}_\Gamma(T)=\langle T\delta_e,\delta_e\rangle,
\qquad
\operatorname{FK}_\Gamma(Q)=\exp\!\left(\operatorname{tr}_\Gamma\log|Q|\right),
\]

and asks for the sharp stochastic domination, on **every increasing event**,

\[
\mathbf P^{\operatorname{FK}_\Gamma(Q)I}
\preccurlyeq \mathbf P^Q
\preccurlyeq
\mathbf P^{I-\operatorname{FK}_\Gamma(I-Q)I}.
\tag{1.1}
\]

For a finite group of order `n`,

\[
\operatorname{FK}_\Gamma(Q)=(\det Q)^{1/n}.
\]

Lyons states immediately before Conjecture 5.7 that it is open even for finite groups. A bounded fresh search on 20 September 2026 found the source statement but no later exact resolution; absence from that search is not treated as proof of worldwide openness.

The immediately preceding R7-03 checkpoint proved singleton gauge-midpoint/product peeling and then a set-transitive symmetry lift. The remaining finite-group issue was that a nonuniform product lower bound with the correct total determinant does not automatically dominate the uniform product at the geometric-mean density.

This run changes the decoupling method. Instead of the geometric midpoint, it keeps an arbitrary coordinate block **exactly unchanged** and replaces the complementary block by its Schur complement. This gives a simpler and stronger block factorization theorem, explicit Cholesky-pivot product lower bounds, and a normal-subgroup reduction that applies to every equivariant kernel without any constant-coset or mean-zero restriction.

## 2. Main theorem: block Schur decoupling lowers the entire DPP

Let the finite ground set split as

\[
E=F\sqcup B.
\]

First assume the strict case `0<Q<I`, and write

\[
Q=
\begin{pmatrix}
A & X\\
X^* & D
\end{pmatrix}
\tag{2.1}
\]

relative to `ell^2(F) direct-sum ell^2(B)`. Thus `A=Q_F`.

Define the Schur complement

\[
C:=D-X^*A^{-1}X.
\tag{2.2}
\]

Since `Q>0`, one has `C>0`; since `C<=D<=I`, it is a positive contraction. Put

\[
G:=A\oplus C.
\tag{2.3}
\]

### Theorem 2.1 — block Schur stochastic decoupling

For every finite positive contraction `Q`, with the boundary case interpreted by the continuous generalized Schur complement,

\[
\boxed{\mathbf P^{A\oplus C}\preccurlyeq \mathbf P^Q.}
\tag{2.4}
\]

Moreover,

\[
\boxed{\det(A\oplus C)=\det Q.}
\tag{2.5}
\]

Thus one may make an arbitrary block `F` independent of its complement, leave its marginal kernel `A` **unchanged**, and replace the other block by the kernel obtained by conditioning on all of `F` being present; this operation lowers the full determinantal process on every increasing event while preserving determinant.

This is strictly more explicit than the preceding singleton geometric-midpoint peeling: for singleton blocks it produces the ordinary Schur/Cholesky pivot ratios of principal minors.

## 3. Proof by exact conditional kernels

Let `Y` have law `P^Q`. Its marginal on `F` is `P^A`.

Fix an exact configuration `S subseteq F`, and write

\[
Z:=F\setminus S.
\]

Condition first on `S subseteq Y`. The standard determinantal conditioning formula gives, on `B union Z`,

\[
K^{S}
=
Q_{B\cup Z}
-Q_{B\cup Z,S}Q_S^{-1}Q_{S,B\cup Z}.
\tag{3.1}
\]

Now also condition on `Z cap Y = emptyset`. Conditioning a DPP kernel `K` on a set `Z` being absent changes the kernel on the remaining coordinates to

\[
K_{\rm rem}+K_{{\rm rem},Z}(I-K_Z)^{-1}K_{Z,{\rm rem}}.
\tag{3.2}
\]

The second term is positive semidefinite. Therefore the exact conditional kernel on `B`, given `Y cap F=S`, satisfies

\[
K_{B\mid S}
\succeq
D-Q_{B,S}Q_S^{-1}Q_{S,B}
=:C_S.
\tag{3.3}
\]

It remains to compare `C_S` with the all-`F` Schur complement `C` from (2.2).

Partition `A` according to `F=S sqcup Z` and define

\[
R:=A_Z-A_{Z,S}A_S^{-1}A_{S,Z}>0,
\tag{3.4}
\]

and

\[
U:=Q_{B,Z}-Q_{B,S}A_S^{-1}A_{S,Z}.
\tag{3.5}
\]

The block inverse formula gives the exact identity

\[
Q_{B,F}A^{-1}Q_{F,B}
=
Q_{B,S}A_S^{-1}Q_{S,B}
+UR^{-1}U^*.
\tag{3.6}
\]

Consequently

\[
\boxed{C_S-C=UR^{-1}U^*\succeq0.}
\tag{3.7}
\]

Combining (3.3) and (3.7),

\[
K_{B\mid S}\succeq C
\quad\text{for every exact }S\subseteq F.
\tag{3.8}
\]

Determinantal kernel monotonicity now gives

\[
\mathbf P^C
\preccurlyeq
\mathcal L(Y\cap B\mid Y\cap F=S)
\tag{3.9}
\]

for every `S` of positive marginal probability.

Construct a coupling as follows. First sample `S` with its true marginal law `P^A`. Independently sample `W_B~P^C`. Conditional on `S`, use a monotone coupling from (3.9) to sample the true conditional `Y_B` so that

\[
W_B\subseteq Y_B.
\]

Then

\[
W:=S\cup W_B
\]

has law `P^{A\oplus C}`, while

\[
Y:=S\cup Y_B
\]

has law `P^Q`, and `W subseteq Y` almost surely. This proves (2.4).

The determinant identity (2.5) is the ordinary Schur determinant formula

\[
\det Q=\det A\,\det C.
\tag{3.10}
\]

For `0<=Q<=I` on the boundary, replace `Q` by

\[
Q_\varepsilon=(1-2\varepsilon)Q+\varepsilon I,
\]

apply the strict theorem, and pass to the limit. Positivity of the block matrix gives the range condition needed for the Moore--Penrose/generalized Schur complement, and finite DPP probabilities are continuous in the kernel. Thus (2.4) holds on the closed contraction body.

## 4. Ordered block factorization

The block theorem iterates with no geometric means.

Let

\[
E=B_1\sqcup B_2\sqcup\cdots\sqcup B_k
\]

be any ordered partition, and put

\[
P_j:=B_1\cup\cdots\cup B_j,
\qquad P_0=\varnothing.
\]

In the strict case define the block pivot

\[
L_1:=Q_{B_1},
\]

and for `j>=2`,

\[
L_j
:=
Q_{B_j}
-Q_{B_j,P_{j-1}}
Q_{P_{j-1}}^{-1}
Q_{P_{j-1},B_j}.
\tag{4.1}
\]

Equivalently, `L_j` is the `B_j` principal block of the Schur complement after conditioning all previous blocks `P_{j-1}` present.

Repeated application of Theorem 2.1 gives

\[
\boxed{
\mathbf P^{L_1\oplus\cdots\oplus L_k}
\preccurlyeq
\mathbf P^Q.
}
\tag{4.2}
\]

The determinant telescopes:

\[
\boxed{
\det Q=\prod_{j=1}^k\det L_j.
}
\tag{4.3}
\]

The boundary case again follows by approximation.

### Singleton consequence: explicit Cholesky-pivot product bound

For an ordering `e_1,...,e_n` and `P_j={e_1,...,e_j}`, let

\[
d_j:=\frac{\det Q_{P_j}}{\det Q_{P_{j-1}}}
\tag{4.4}
\]

in the strict case (`det Q_emptyset=1`). Then

\[
\boxed{
\bigotimes_{j=1}^n\operatorname{Ber}(d_j)
\preccurlyeq
\mathbf P^Q,
\qquad
\prod_{j=1}^n d_j=\det Q.
}
\tag{4.5}
\]

So the nonuniform product lower bound can be chosen with **ordinary LDL/Cholesky pivots of principal minors**. This is much more explicit than the preceding geometric-midpoint recursion.

Applying the same theorem to `I-Q` gives vacancy pivots

\[
r_j:=\frac{\det (I-Q)_{P_j}}{\det (I-Q)_{P_{j-1}}}
\]

and therefore

\[
\boxed{
\mathbf P^Q
\preccurlyeq
\bigotimes_{j=1}^n\operatorname{Ber}(1-r_j),
\qquad
\prod_j r_j=\det(I-Q).
}
\tag{4.6}
\]

## 5. Normal-subgroup reduction for every finite equivariant kernel

The block theorem gives a new group-theoretic reduction with **no restriction on cross-coset coefficients**.

Let `Gamma` be finite and let

\[
H\triangleleft\Gamma,
\qquad |H|=m,
\qquad [\Gamma:H]=k.
\]

Order the left cosets

\[
C_1,\ldots,C_k.
\]

Because `H` is normal, every left coset and every union of left cosets is invariant under the left action of `H`. If `Q` is `Gamma`-equivariant, then every Schur complement appearing in the ordered coset factorization remains `H`-equivariant. After identifying each `C_j` with `H`, every block pivot `L_j` is therefore an `H`-equivariant positive contraction.

Assume the **lower half** of Lyons Conjecture 5.7 is known on `H`. Put

\[
p_j:=(\det L_j)^{1/m}.
\tag{5.1}
\]

Then on each coset

\[
\operatorname{Ber}(p_j)^{\otimes C_j}
\preccurlyeq
\mathbf P^{L_j}.
\]

Tensoring these couplings and using (4.2),

\[
\boxed{
\bigotimes_{j=1}^k
\operatorname{Ber}(p_j)^{\otimes C_j}
\preccurlyeq
\mathbf P^Q.
}
\tag{5.2}
\]

By (4.3),

\[
\prod_{j=1}^k p_j
=(\det Q)^{1/m}.
\tag{5.3}
\]

If

\[
p=(\det Q)^{1/(mk)}
=\operatorname{FK}_\Gamma(Q),
\]

then the exact constraint is

\[
\boxed{\prod_{j=1}^k p_j=p^k.}
\tag{5.4}
\]

The same argument applied to `I-Q` yields a blockwise Bernoulli **upper** bound whose vacancy parameters have geometric mean `FK_Gamma(I-Q)`.

### Corollary 5.1 — quotient-uniformization reduction

For a finite normal extension `H normal Gamma`, once Lyons 5.7 is known on `H`, the remaining lower-bound problem on `Gamma` is purely this:

> show that the blockwise product measure in (5.2), or a suitable convex combination of the product lower bounds obtained from different coset/block flags, dominates the uniform product `Ber(p)^Gamma` on the `Gamma`-invariant increasing tests.

No determinant or DPP calculation remains inside the individual cosets; all such information has been compressed into the positive numbers `p_j` satisfying (5.4).

This reduction is source-valid for **every** `Gamma`-equivariant `Q`. It does not require centrality, constant coset coefficients, mean-zero conditions, hidden cyclic symmetry, or a low-dimensional gauge-active sector.

## 6. Arbitrary S3 is reduced to a two-density quotient problem

Take

\[
\Gamma=S_3,
\qquad H=A_3\cong C_3.
\]

The preceding R7-03 work contains a candidate full proof of the sharp `C_3` theorem. Conditional on that inherited result, Theorem 5 gives the following for **every** `S_3`-equivariant positive contraction `Q`.

Write the two cosets as `H` and `sH`. Let

\[
a=(\det Q_H)^{1/3}
\]

and let `c` be the cube root of the determinant of the Schur pivot on the other coset. Then

\[
\boxed{
\operatorname{Ber}(a)^{\otimes H}
\otimes
\operatorname{Ber}(c)^{\otimes sH}
\preccurlyeq
\mathbf P^Q,
}
\tag{6.1}
\]

with

\[
\boxed{ac=p^2,\qquad p=(\det Q)^{1/6}.}
\tag{6.2}
\]

Starting the block factorization from the other coset gives the swapped lower bound

\[
\operatorname{Ber}(c)^{\otimes H}
\otimes
\operatorname{Ber}(a)^{\otimes sH}
\preccurlyeq
\mathbf P^Q.
\tag{6.3}
\]

Hence every convex combination of (6.1) and (6.3) is also stochastically below `P^Q`.

This is a full-arbitrary-`S_3` structural reduction, not a restricted kernel family. The only missing step is to recover the **uniform** density `p` from the two block densities while retaining enough of the cross-coset compensation lost by Schur decoupling.

## 7. Exact obstruction: the geometric-product constraint alone is not enough

It is tempting to hope that `ac=p^2` and coset-swap symmetry force

\[
\operatorname{Ber}(p)^{\otimes6}
\preccurlyeq
\tfrac12\bigl(\mu_{a,c}+\mu_{c,a}\bigr),
\tag{7.1}
\]

where

\[
\mu_{a,c}
=
\operatorname{Ber}(a)^{\otimes H}
\otimes
\operatorname{Ber}(c)^{\otimes sH}.
\]

This is false, even for an `S_3`-invariant increasing event and for block parameters that arise from an actual interior `S_3`-equivariant contraction.

Let

\[
U:=\{X:X\cap H\ne\varnothing\text{ and }X\cap sH\ne\varnothing\}.
\tag{7.2}
\]

This event is increasing and `S_3`-invariant. Put

\[
a=\frac49,
\qquad
c=\frac19,
\qquad
p=\sqrt{ac}=\frac29.
\tag{7.3}
\]

For

\[
\phi(t):=1-(1-t)^3,
\]

one has

\[
\mu_{a,c}(U)=\phi(a)\phi(c)
=\frac{131068}{531441},
\tag{7.4}
\]

whereas

\[
\operatorname{Ber}(p)^{\otimes6}(U)
=\phi(p)^2
=\frac{148996}{531441}.
\tag{7.5}
\]

Thus

\[
\boxed{
\operatorname{Ber}(p)^{\otimes6}(U)
-\mu_{a,c}(U)
=\frac{664}{19683}>0.
}
\tag{7.6}
\]

The symmetric mixture with swapped blocks has the same value on `U`, so it also fails (7.1).

These parameters are not artificial. Let `s` be a transposition and `R_s` the right-regular permutation operator. Define

\[
Q=\frac49 I+\frac{2}{3\sqrt3}R_s.
\tag{7.7}
\]

Because `R_s` is an involution, the eigenvalues of `Q` are

\[
\frac49\pm\frac{2}{3\sqrt3},
\]

each with multiplicity three; both lie strictly between `0` and `1`. Thus `Q` is an interior `S_3`-equivariant positive contraction.

In the decomposition `H sqcup Hs`, after the natural identification of the two cosets,

\[
Q=
\begin{pmatrix}
\frac49 I_3 & \frac{2}{3\sqrt3}I_3\\
\frac{2}{3\sqrt3}I_3 & \frac49 I_3
\end{pmatrix}.
\tag{7.8}
\]

The first Schur block has density `a=4/9`, and the second Schur complement is

\[
\left(\frac49-\frac{(2/(3\sqrt3))^2}{4/9}\right)I_3
=\frac19 I_3,
\]

so its density is exactly `c=1/9`. Also

\[
\det Q=\left(\frac4{81}\right)^3,
\qquad
(\det Q)^{1/6}=\frac29.
\]

This is **not** a counterexample to Lyons. In fact the actual DPP has a much larger probability of `U`:

\[
\mathbf P^Q(U)
=1-2\left(\frac59\right)^3
+\left(\frac{13}{81}\right)^3
=\frac{351388}{531441}
>\frac{148996}{531441}.
\tag{7.9}
\]

So the failure in (7.6) measures information lost by the Schur product factorization: the original cross-coset coupling supplies substantial positive compensation for this increasing union event.

## 8. What changed, and what remains

### New proved mathematics

1. **Block Schur stochastic decoupling:** `P^{A direct-sum (Q/A)} <= P^Q` for an arbitrary finite block split, with determinant preservation.
2. **Explicit block/Cholesky factorization:** every finite DPP dominates a direct product of DPPs on arbitrary ordered blocks; singleton factors are exact principal-minor pivot ratios.
3. **Normal-subgroup reduction:** if Lyons lower domination is known on `H normal Gamma`, every `Gamma`-equivariant kernel admits a blockwise Bernoulli lower bound on the `H`-cosets with exactly the correct geometric product of densities.
4. **Arbitrary-S3 reduction:** using `A_3 normal S_3`, all `S_3` kernels reduce to a two-density coset product lower bound with `ac=p^2`, plus its swapped companion.
5. **Exact obstruction:** even the symmetric mixture of those two block products need not dominate the uniform `p` product; an explicit interior `S_3` kernel and invariant event show the missing cross-coset compensation.

### Full-source metric

Still **PROVED PARTIAL**. The original conjecture quantifies over every sofic group and every equivariant positive contraction. Arbitrary `S_3` is not yet closed by this note, because the quotient-uniformization step cannot discard cross-coset dependence as in (7.6).

## 9. Next attack

The obstruction identifies the right next object. Do **not** try to prove a false product-only statement from `ac=p^2`.

For `S_3`, retain one controlled piece of the cross-coset dependence instead of replacing the whole second block by its Schur complement. Two concrete options are now natural:

1. **Two-stage compensated Schur interpolation.** Interpolate between the original block matrix and `A direct-sum C`, calculate the derivative of an arbitrary `S_3`-invariant event probability using the exact conditional-kernel coupling above, and isolate a lower bound on the compensation term sufficient to bridge the explicit deficit in (7.6).
2. **Flag mixture.** Form convex lower bounds from several Schur flags, not only the `A_3` two-coset flag. In `S_3`, combine the normal `C_3` flag with flags built from the three `C_2` subgroups. Every component is stochastically below `P^Q`; the question becomes whether a symmetry-weighted flag mixture retains enough cross-orbit information to dominate `Ber(p)^6` on the 76 invariant upper sets.

The second route is especially suitable for an exact finite certificate if it succeeds, while the first has a clearer path to a reusable theorem beyond `S_3`.