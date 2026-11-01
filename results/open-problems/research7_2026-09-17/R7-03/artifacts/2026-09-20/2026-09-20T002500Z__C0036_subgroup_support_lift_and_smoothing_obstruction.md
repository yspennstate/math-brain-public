Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED; no authenticated runtime telemetry establishes the requested GPT-6/maximum setting.

# C0036 progress-first mathematics: subgroup-support lifting and an exact obstruction to naive global smoothing

Date: 2026-09-20 UTC  
Worker: C03 / R7-03, native ID `6aabe7be74008191b526b109ee4e9e80`  
Repository: private `yspennstate/math-open-problems`, branch `master`  
Source: Russell Lyons, *Determinantal Probability: Basic Properties and Conjectures* (ICM 2014), §5.2, Conjecture 5.7, arXiv:1406.2707.  
Status: **PROVED PARTIAL** relative to the full source. No claim of full-source resolution is made.

## 1. Exact source target recovered

Section 5.2 works with a sofic group `Gamma`. Conjecture 5.7 takes a `Gamma`-equivariant positive contraction

\[
0\le Q\le I\quad\text{on }\ell^2(\Gamma),
\]

where equivariance is with respect to the left translation action. The associated determinantal process `P^Q` on subsets of `Gamma` is characterized on finite `A subset Gamma` by

\[
P^Q[A\subseteq X]=\det(Q\upharpoonright A).
\]

For a `Gamma`-equivariant operator, write `tr_Gamma` for the group von Neumann trace; equivalently

\[
\operatorname{tr}_\Gamma(T)=\langle T\delta_e,\delta_e\rangle
\]

(and for finite `Gamma`, this is the normalized matrix trace). Lyons writes

\[
\operatorname{FK}_\Gamma(Q)
:=\exp\big(\operatorname{tr}_\Gamma\log|Q|\big),
\]

with the usual extended-value convention when the logarithmic trace is `-infinity`.

The conjecture is the sharp two-sided stochastic domination

\[
\boxed{
\operatorname{Ber}(\operatorname{FK}_\Gamma(Q))^{\otimes\Gamma}
\preccurlyeq P^Q
\preccurlyeq
\operatorname{Ber}\!\left(1-\operatorname{FK}_\Gamma(I-Q)\right)^{\otimes\Gamma}.
}
\tag{1.1}
\]

Here stochastic domination means domination on every increasing event (equivalently, existence of a monotone coupling). The source states that the bounds should be optimal and that the conjecture is open even for finite groups.

The inherited R7-03 order-six bottleneck is the adjacent-pair event on `Z/6Z`. The previous report rewrote its complement, the independent-set event of `C_6`, as

\[
F(\lambda):=\mathbb E_\lambda f(J),
\qquad
F(\lambda)\le F(p,p,p,p,p,p),
\quad p=(\lambda_0\cdots\lambda_5)^{1/6},
\tag{1.2}
\]

for one explicit decreasing set function `f` on spectral subsets. It also proved strict positive Hessian of the adjacent-event gap at the scalar point on each fixed-product slice.

## 2. First attack: local Hessian positivity does **not** globalize by arbitrary pairwise geometric smoothing

A natural global route would repeatedly replace two coordinates `(a,b)` by `(sqrt(ab),sqrt(ab))`. This preserves the product and drives the spectrum toward the scalar point. For (1.2), such an argument would require each smoothing step to *increase* `F`.

That monotonicity is false, even for smoothing two adjacent frequency coordinates.

Take

\[
\lambda=\left(\frac1{16},\frac1{16},\frac1{16},\frac1{16},\frac14,1\right)
\]

and smooth coordinates `3,4` to their geometric mean:

\[
\widetilde\lambda
=\left(\frac1{16},\frac1{16},\frac1{16},\frac18,\frac18,1\right).
\]

Both products equal `2^{-18}`, hence both have geometric mean

\[
p=2^{-3}=\frac18.
\]

Using the exact projection-mixture table from the previous run gives

\[
F(\lambda)=\frac{218025}{262144},
\qquad
F(\widetilde\lambda)=\frac{217065}{262144},
\]

so

\[
\boxed{
F(\widetilde\lambda)-F(\lambda)
=-\frac{15}{4096}<0.
}
\tag{2.1}
\]

For comparison the scalar value is

\[
F(p,p,p,p,p,p)=\frac{120393}{131072}
=\frac{240786}{262144},
\]

so this is not a counterexample to (1.2): both nonscalar values are still below the scalar one. What (2.1) proves is sharper methodologically: **strict local scalar stability cannot be promoted to the global comparison by an unrestricted sequence of product-preserving two-coordinate geometric averages.** Such a sequence can initially move `F` in the wrong direction.

This discharges the requested local-to-global test and forces a change of method rather than another local spectral expansion.

## 3. New structural criterion: subgroup-supported kernels lift Conjecture 5.7 from the subgroup to the ambient group

The following theorem gives a genuinely broader source class and works for finite or infinite index.

### Theorem 3.1 (subgroup-support lifting)

Let `Gamma` be a countable sofic group and `H <= Gamma` any subgroup. Let `Q` be a `Gamma`-equivariant positive contraction on `ell^2(Gamma)`. Write its translation-invariant kernel as

\[
Q(x,y)=q(x^{-1}y).
\]

Assume the convolution kernel is supported in `H`:

\[
q(g)=0\qquad(g\notin H).
\tag{3.1}
\]

Let `Q_H` denote the restriction of `Q` to `ell^2(H)`. If the two-sided Lyons domination (1.1) holds for `Q_H` on `H`, then it holds for `Q` on `Gamma`. Moreover

\[
\boxed{
\operatorname{FK}_\Gamma(Q)=\operatorname{FK}_H(Q_H),
\qquad
\operatorname{FK}_\Gamma(I-Q)=\operatorname{FK}_H(I-Q_H).
}
\tag{3.2}
\]

Thus the Bernoulli densities are unchanged by the lift.

#### Proof

Partition `Gamma` into right cosets `xH`. If `xH != yH`, then for `u in xH` and `v in yH` we have `u^{-1}v notin H`; by (3.1),

\[
Q(u,v)=0.
\]

Hence every `ell^2(xH)` is a reducing subspace for `Q`, and

\[
\ell^2(\Gamma)=\bigoplus_{xH\in\Gamma/H}\ell^2(xH)
\]

is a block decomposition of `Q`. The unitary

\[
U_x:\ell^2(H)\to\ell^2(xH),
\qquad U_x\delta_h=\delta_{xh},
\]

intertwines the restriction on the coset with `Q_H`, because

\[
Q(xh_1,xh_2)=q(h_1^{-1}h_2).
\]

So all blocks are unitarily identical.

For any finite `A subset Gamma`, write `A_C=A cap C` over right cosets. Block diagonality gives

\[
\det(Q\upharpoonright A)
=\prod_C \det(Q\upharpoonright A_C).
\tag{3.3}
\]

The determinantal inclusion probabilities therefore factor over cosets. Since those finite inclusion probabilities characterize the discrete DPP, (3.3) yields the exact process decomposition

\[
\boxed{
P^Q=\bigotimes_{xH\in\Gamma/H} P^{Q_H},
}
\tag{3.4}
\]

after transporting each copy by `U_x`.

For the Fuglede-Kadison determinant, the `H`-block containing the identity reduces `Q`, and Borel functional calculus respects reducing subspaces. Hence the spectral measure of `Q` at `delta_e` is exactly the spectral measure of `Q_H` at `delta_e`. Consequently

\[
\operatorname{tr}_\Gamma \log|Q|
=\langle \log|Q|\delta_e,\delta_e\rangle
=\langle \log|Q_H|\delta_e,\delta_e\rangle
=\operatorname{tr}_H\log|Q_H|.
\]

This remains valid when the logarithmic integral is `-infinity`, either directly from the spectral measure or by monotone regularization. Exponentiating proves the first identity in (3.2). Applying the same argument to `I-Q`, which has the same block decomposition, proves the second.

Now suppose on `H` there are monotone couplings

\[
\operatorname{Ber}(a)^{\otimes H}
\preccurlyeq P^{Q_H}
\preccurlyeq
\operatorname{Ber}(b)^{\otimes H},
\]

where

\[
a=\operatorname{FK}_H(Q_H),
\qquad
b=1-\operatorname{FK}_H(I-Q_H).
\]

Take these couplings independently on all right cosets. Their countable product is a monotone coupling of the product processes in (3.4), while the products of the Bernoulli blocks are exactly `Ber(a)^{otimes Gamma}` and `Ber(b)^{otimes Gamma}`. With (3.2), this is exactly (1.1) for `Q` on `Gamma`. ∎

### Proposition 3.2 (sharpness is inherited from a finite subgroup)

If `H` is finite and the two densities for `Q_H` are sharp, then the lifted densities in Theorem 3.1 are sharp for `Q` as well.

#### Proof

Let `m=|H|` and `a=FK_H(Q_H)`. If `Ber(c)^{otimes Gamma} <=st P^Q`, restriction to the coordinates of the identity coset gives `Ber(c)^{otimes H} <=st P^{Q_H}`. On the increasing event that all `m` sites of `H` are occupied,

\[
c^m\le \det Q_H=a^m,
\]

hence `c<=a`.

Similarly, if `P^Q <=st Ber(c)^{otimes Gamma}`, restriction to `H` and the increasing event `X cap H != empty` give

\[
1-\det(I-Q_H)
\le 1-(1-c)^m.
\]

Writing `b=1-FK_H(I-Q_H)` gives `(1-b)^m <= (1-c)^m`, hence `c>=b`. ∎

## 4. Source-valid consequences

### Corollary 4.1 (published integer-lattice theorem lifts into nonabelian ambient groups)

Lyons's Theorem 5.2 proves the sharp two-sided product bounds for every translation-invariant determinantal process on `Z^d`. Therefore, if a sofic group `Gamma` contains a subgroup `H isomorphic to Z^d`, then **every** `Gamma`-equivariant positive contraction whose convolution kernel is supported in `H` satisfies Conjecture 5.7 on the full ambient group `Gamma`.

This is a genuinely broader source class than the original integer-lattice theorem: the ambient group may be nonabelian and `H` may have infinite index. The restriction is structural (operator support in a subgroup), not finite-volume.

### Corollary 4.2 (finite-subgroup lift from the cumulative R7-03 package)

The current R7-03 package contains internally proved full sharp finite-group results through order four and on `Z/5Z`. Conditional only on those earlier proofs surviving independent review, Theorem 3.1 lifts them to every sofic ambient group containing such a finite subgroup: any equivariant positive contraction supported in that subgroup satisfies the full sharp two-sided Conjecture 5.7. By Proposition 3.2 the lifted constants remain sharp.

This corollary is therefore **CANDIDATE FULL for this structural class**, not a claim that the all-group/all-operator source conjecture is solved.

## 5. What changed, what remains, and next attack

Full-source metric: **unchanged / still open in this work**. The source quantifies over all `Gamma`-equivariant positive contractions, while Theorem 3.1 requires subgroup support.

Obligation ledger movement:

1. `Z/6Z` adjacent orbit: still unresolved globally.
2. Naive global pair-geometric smoothing route: **closed negatively** by the exact obstruction (2.1).
3. Structural lift beyond finite cyclic groups: **new proved theorem**. Any solved subgroup instance now lifts to subgroup-supported kernels on arbitrary sofic ambient groups, including infinite nonabelian ambient groups.

The next attack should not repeat Hessian/local spectral expansion or arbitrary pair smoothing. The two promising routes are:

- exploit the explicit six-Bernoulli function `f` through a cycle-respecting reflection/three-pair symmetrization rather than arbitrary pair averaging; or
- seek a decomposition of a general equivariant operator into subgroup-supported pieces compatible with stochastic domination, which would extend Theorem 3.1 beyond exact support.

The first is the more direct route to closing the remaining `Z/6Z` adjacent event.
