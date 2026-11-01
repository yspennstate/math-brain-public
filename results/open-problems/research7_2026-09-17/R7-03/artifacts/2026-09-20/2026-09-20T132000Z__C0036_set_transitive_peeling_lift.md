Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — the requested GPT-6/maximum setting is a preference, not authenticated runtime telemetry, so I do not claim it ran.**

# C0036: set-transitive symmetrization lifts determinant-preserving peeling to the sharp uniform product bound

Date: 2026-09-20 UTC  
Role: C03 / R7-03, native ID `6aabe7be74008191b526b109ee4e9e80`  
Canonical ownership: preserved; C03 remains the explicitly complementary progress-first role.  
Status: **PROVED PARTIAL** relative to Lyons Conjecture 5.7. The finite-DPP theorem below is proved analytically here, pending independent review.

## 1. Exact outside source target

Russell Lyons, *Determinantal Probability: Basic Properties and Conjectures*, Proc. ICM 2014, arXiv:1406.2707, Section 5.2, Conjecture 5.7.

Section 5.2 fixes a **sofic group** `Gamma`. The conjecture ranges over every `Gamma`-equivariant positive contraction

\[
0\le Q\le I\qquad\text{on }\ell^2(\Gamma),
\]

with group trace and Fuglede--Kadison determinant

\[
\operatorname{tr}_\Gamma(T)=\langle T\delta_e,\delta_e\rangle,
\qquad
\operatorname{FK}_\Gamma(Q)=\exp\!\bigl(\operatorname{tr}_\Gamma\log|Q|\bigr),
\]

and asks for the sharp stochastic domination, for **every increasing event**,

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
\tag{1.2}
\]

Lyons states immediately before Conjecture 5.7 that it is open even for finite groups. A bounded current-source search in this run did not identify a later paper resolving this exact conjecture; that negative search result is not treated as proof of worldwide openness.

## 2. Inherited theorem from the preceding R7-03 run

The preceding checkpoint proved the following finite-DPP statement.

### Singleton gauge-midpoint theorem

For every finite positive contraction `Q` on a ground set `E=F sqcup {e}`, let `D` be the diagonal sign matrix that is `+1` on `F` and `-1` at `e`. Then

\[
\mathbf P^{Q\#(DQD)}\preccurlyeq \mathbf P^Q,
\qquad
\det(Q\#(DQD))=\det Q,
\tag{2.1}
\]

and the midpoint `Q#(DQD)` decouples the coordinate `e` from `F`.

Iterating singleton flips in any chosen coordinate order therefore yields a diagonal kernel

\[
D_* = \operatorname{diag}(d_1,\ldots,d_n)
\]

such that

\[
\boxed{
\mu_d:=\bigotimes_{i=1}^n\operatorname{Ber}(d_i)
\preccurlyeq \mathbf P^Q,
\qquad
\prod_{i=1}^n d_i=\det Q.
}
\tag{2.2}
\]

The obstruction noted in that run was that (2.2) alone cannot imply the uniform product inequality by coordinatewise comparison: if `p=(prod_i d_i)^{1/n}`, then `Ber(p)^n <= product Ber(d_i)` coordinatewise would force every `d_i>=p`, hence all `d_i=p`.

The present run supplies a different mechanism: **symmetry of the test events**, not coordinatewise comparison.

## 3. Orbit-test reduction for an invariant DPP

Let `E` be a finite set of size `n`. Let `H<=Sym(E)` act on configurations in the usual way. Assume `Q` is `H`-invariant:

\[
U_h Q U_h^*=Q\qquad(h\in H).
\tag{3.1}
\]

Then `P^Q` is `H`-invariant. Put

\[
p=(\det Q)^{1/n}.
\tag{3.2}
\]

Choose any singleton-peeling order and let `mu_d` be the product lower bound from (2.2).

### Proposition 3.1 — invariant-upper-set criterion

If

\[
\mu_d(U)\ge \operatorname{Ber}(p)^{\otimes E}(U)
\tag{3.3}
\]

for every `H`-invariant increasing event `U`, then

\[
\boxed{
\operatorname{Ber}(p)^{\otimes E}\preccurlyeq \mathbf P^Q.
}
\tag{3.4}
\]

#### Proof

Let `A` be an arbitrary increasing event and define its orbit average

\[
f_A(x):=\frac1{|H|}\sum_{h\in H}{\bf1}_A(hx).
\tag{3.5}
\]

The function `f_A` is increasing and `H`-invariant. Since both `P^Q` and `Ber(p)^{\otimes E}` are `H`-invariant,

\[
\mathbf P^Q(A)=\mathbf E_{P^Q}f_A,
\qquad
\operatorname{Ber}(p)^{\otimes E}(A)=\mathbf E_{\operatorname{Ber}(p)^{\otimes E}}f_A.
\tag{3.6}
\]

Every superlevel set `{f_A>=t}` is an `H`-invariant increasing event. Hence (3.3), by finite layer-cake integration, gives

\[
\mathbf E_{\mu_d}f_A
\ge
\mathbf E_{\operatorname{Ber}(p)^{\otimes E}}f_A.
\tag{3.7}
\]

On the other hand `mu_d <= P^Q` from (2.2), so stochastic domination applied to the increasing function `f_A` gives

\[
\mathbf E_{P^Q}f_A\ge\mathbf E_{\mu_d}f_A.
\tag{3.8}
\]

Combining (3.6)--(3.8) proves (3.4). QED.

This proposition is useful because for a group-equivariant kernel the remaining comparison can be moved entirely to an **ordinary product measure**. No DPP inclusion--exclusion remains in the final symmetry-restoring step.

A convex variant will also be useful later: if `mu^{(j)} <= P^Q` are product lower bounds from several peeling orders, then every convex mixture `nu=sum_j w_j mu^{(j)}` also satisfies `nu<=P^Q`; it suffices that `nu` dominate `Ber(p)^E` on all `H`-invariant increasing tests.

## 4. Product-count lemma at fixed geometric mean

The key inequality needed for highly symmetric actions is independent of determinantal processes.

### Lemma 4.1 — Poisson-binomial count dominates the equal-parameter binomial at fixed product

Let `d_1,...,d_n in[0,1]` and

\[
p:=\left(\prod_{i=1}^n d_i\right)^{1/n}.
\]

Let `X_i` be independent Bernoulli(`d_i`) variables and let `Y_i` be independent Bernoulli(`p`) variables. Then

\[
\boxed{
\sum_{i=1}^n Y_i
\preccurlyeq_{\rm st}
\sum_{i=1}^n X_i.
}
\tag{4.1}
\]

Equivalently, for every `k`,

\[
\mathbb P\!\left(\sum_iX_i\ge k\right)
\ge
\mathbb P\!\left(\operatorname{Bin}(n,p)\ge k\right).
\tag{4.2}
\]

#### Proof

If `p=0`, the right side of (4.2) is zero for every `k>=1`, so the claim is trivial. If `p=1`, every `d_i=1` and equality holds. Assume `0<p<1`.

Take two coordinates with parameters `a,b` and keep their product fixed. Put

\[
g=\sqrt{ab}.
\]

For the two-coordinate success count `N_{a,b}`, the only nontrivial tails are

\[
\mathbb P(N_{a,b}\ge2)=ab=g^2
\tag{4.3}
\]

and

\[
\mathbb P(N_{a,b}\ge1)=a+b-ab
\ge 2\sqrt{ab}-ab
=2g-g^2
=\mathbb P(N_{g,g}\ge1),
\tag{4.4}
\]

where the inequality is AM--GM. Thus

\[
N_{g,g}\preccurlyeq_{\rm st}N_{a,b}.
\tag{4.5}
\]

Adding an independent integer-valued random variable preserves stochastic order. Hence replacing any pair `(a,b)` by `(sqrt(ab),sqrt(ab))` can only decrease the total success count in stochastic order, while preserving the product of all parameters.

In logarithmic coordinates this replacement averages two coordinates. Repeated pairwise averaging drives every coordinate to the common logarithmic mean `log p`. Tail probabilities are continuous in the parameters. Taking the limit proves (4.1). QED.

This lemma is strictly stronger than the one-event full-set identity: the top tail is fixed because `prod d_i=p^n`, while **every lower success-count tail can only increase when the parameters become uneven**.

## 5. Main new theorem: set-transitive automorphism criterion

Call a permutation group `H<=Sym(E)` **set-transitive** if it acts transitively on the `k`-element subsets of `E` for every `k=0,...,n`.

### Theorem 5.1 — sharp Lyons sandwich under set-transitive automorphisms

Let `Q` be any finite positive contraction on `ell^2(E)`. Suppose its coordinate automorphism group contains a set-transitive subgroup `H`, i.e.

\[
U_h Q U_h^*=Q\qquad(h\in H).
\tag{5.1}
\]

Then, with

\[
p=(\det Q)^{1/n},
\qquad
r=(\det(I-Q))^{1/n},
\tag{5.2}
\]

we have the full all-increasing-event stochastic sandwich

\[
\boxed{
\operatorname{Ber}(p)^{\otimes E}
\preccurlyeq \mathbf P^Q
\preccurlyeq
\operatorname{Ber}(1-r)^{\otimes E}.
}
\tag{5.3}
\]

Both constants are sharp.

#### Proof of the lower bound

Choose any peeling order and obtain `mu_d <= P^Q` with `prod_i d_i=det Q=p^n`.

Because `H` is set-transitive, every `H`-invariant increasing event is a pure cardinality threshold

\[
U_k=\{X\subseteq E:|X|\ge k\}
\tag{5.4}
\]

for some `k` (together with the trivial empty/full events). Indeed, if an invariant increasing event contains one `k`-set, set-transitivity makes it contain every `k`-set, and increasingness then forces every larger set.

Therefore Lemma 4.1 gives, for every `H`-invariant increasing `U_k`,

\[
\mu_d(U_k)
=\mathbb P\!\left(\sum_iX_i\ge k\right)
\ge
\mathbb P(\operatorname{Bin}(n,p)\ge k)
=\operatorname{Ber}(p)^{\otimes E}(U_k).
\tag{5.5}
\]

Proposition 3.1 now yields

\[
\operatorname{Ber}(p)^{\otimes E}\preccurlyeq P^Q.
\tag{5.6}
\]

#### Upper bound

The same `H` preserves `I-Q`. Apply the lower result to the vacancy DPP `P^{I-Q}`:

\[
\operatorname{Ber}(r)^{\otimes E}\preccurlyeq P^{I-Q}.
\tag{5.7}
\]

Complementing configurations reverses stochastic order, and the complement of `P^{I-Q}` is `P^Q`. Hence

\[
P^Q\preccurlyeq\operatorname{Ber}(1-r)^{\otimes E}.
\tag{5.8}
\]

#### Sharpness

For the lower density, the all-occupied event has

\[
P^Q(E\subseteq X)=\det Q=p^n,
\]

so no Bernoulli product with density greater than `p` can be stochastically dominated by `P^Q`.

For the upper density, apply the same argument to vacancies, or equivalently use the nonempty increasing event and `P^Q(X=\varnothing)=\det(I-Q)=r^n`. Thus no upper Bernoulli density smaller than `1-r` can dominate `P^Q`. QED.

## 6. Consequence for Lyons Conjecture 5.7 on finite groups

Every finite group is sofic. Let `Gamma` be a finite group of order `n`, and let `Q` be a `Gamma`-equivariant positive contraction on `ell^2(Gamma)`. If the coordinate automorphism group of `Q` contains a set-transitive subgroup, then Theorem 5.1 gives exactly Lyons's Conjecture 5.7 because

\[
p=\operatorname{FK}_\Gamma(Q),
\qquad
r=\operatorname{FK}_\Gamma(I-Q).
\tag{6.1}
\]

Thus we obtain the structural finite-group criterion

\[
\boxed{
\operatorname{Aut}(Q)\text{ set-transitive on subsets}
\quad\Longrightarrow\quad
\text{full sharp Lyons 5.7 for }Q.
}
\tag{6.2}
\]

This is an arbitrary-cardinality theorem, not a finite example or a single-event inequality.

### Explicit all-orders family on every finite group

For every finite group `Gamma` of order `n`, consider the permutation-invariant two-parameter kernels

\[
Q=aI+b(J-I)=(a-b)I+bJ.
\tag{6.3}
\]

Here `J` is the all-ones matrix. Such a kernel is invariant under the full symmetric group `S_n`, so Theorem 5.1 applies whenever `0<=Q<=I`. Its two eigenvalues are

\[
\lambda_{\mathbf1}=a+(n-1)b,
\qquad
\lambda_\perp=a-b
\tag{6.4}
\]

with multiplicities `1` and `n-1`, respectively. Hence the positive-contraction condition is exactly

\[
0\le a+(n-1)b\le1,
\qquad
0\le a-b\le1.
\tag{6.5}
\]

For the full interior of this family,

\[
\operatorname{FK}_\Gamma(Q)
=
\bigl[(a+(n-1)b)(a-b)^{n-1}\bigr]^{1/n},
\tag{6.6}
\]

and

\[
\operatorname{FK}_\Gamma(I-Q)
=
\bigl[(1-a-(n-1)b)(1-a+b)^{n-1}\bigr]^{1/n}.
\tag{6.7}
\]

Therefore (5.3) is the complete sharp source inequality on this nontrivial two-eigenvalue family for **every finite group and every group order**.

The regular action of a general finite group is not set-transitive once the order is large, so (6.2) does **not** settle arbitrary finite groups. It instead identifies an exact symmetry condition under which the nonuniform peeling theorem automatically upgrades to Lyons's required uniform density.

## 7. Why this changes the remaining bottleneck

Before this run, determinant-preserving peeling produced a product lower bound but left an apparent coordinatewise-uniformization obstruction. Theorem 5.1 shows that coordinatewise comparison was the wrong metric: once the relevant increasing tests collapse to cardinality thresholds, fixed-product AM--GM gives the uniform Bernoulli law in the correct stochastic direction.

More generally Proposition 3.1 says that for an arbitrary finite equivariant kernel the DPP part of the problem can be separated from the symmetry-restoring part:

1. singleton gauge peeling supplies `mu_d <= P^Q` with the exact determinant product;
2. one only needs to compare `mu_d` with `Ber(p)^E` on **group-invariant upper sets**.

For `S_3` under its regular action those invariant tests are the previously enumerated 76 upper sets. The next attack therefore no longer needs determinant inclusion--exclusion for `P^Q`: it can work entirely with ordinary product probabilities generated by the peeling parameters. If one fixed peeling order is too anisotropic, convex mixtures over several or all peeling orders remain valid lower measures because stochastic domination is convex in the lower law.

This suggests a concrete route to arbitrary `S_3`:

- express the singleton-peeling parameters through the successive Schur/geometric-mean pivots;
- average the resulting product lower laws over a symmetry-compatible family of orders;
- prove the 76 invariant product-event inequalities against the uniform parameter `p=(det Q)^{1/6}`.

A proof of those product inequalities would close the full `S_3` lower bound, and applying the same construction to `I-Q` would close the upper bound.

## 8. Honest status

**New proved result in this run:** Theorem 5.1, the set-transitive automorphism criterion, plus the invariant-upper-set reduction and the fixed-geometric-mean Poisson-binomial lemma.

**Full-source metric:** unchanged — Lyons Conjecture 5.7 for arbitrary sofic groups, and even arbitrary finite groups, remains unproved in this work.

**Genuinely broader source class:** complete sharp two-sided domination now follows for every finite group kernel whose coordinate automorphism group contains a set-transitive subgroup, including the arbitrary-order two-eigenvalue family (6.3).

**Remaining obstruction:** for a regular group action with several subset orbits at a fixed cardinality, invariant upper sets are not merely count thresholds. The product peeling parameters must be controlled orbitwise rather than only through their geometric mean.

**Next attack:** use Proposition 3.1 on arbitrary `S_3`, replacing the prior DPP-event algebra by product-event inequalities for a symmetry-averaged family of peeling endpoints. This is a materially different route from the failed sequential sector smoothing and from the earlier Hessian/event expansions.