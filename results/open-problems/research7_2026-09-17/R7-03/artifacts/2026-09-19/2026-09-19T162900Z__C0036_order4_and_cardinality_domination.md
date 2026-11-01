Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this was not GPT-6 at maximum, and I do not claim otherwise.** No authenticated runtime model/effort telemetry or binding selector was exposed.

# C0036 admission-stage mathematics: all cardinality tails and every group of order at most four

Date: 2026-09-19 UTC  
Worker: R7-03 Boundary-Case Research  
Canonical candidate: `C0036`  
Outside source: Russell Lyons, *Determinantal Probability: Basic Properties and Conjectures*, ICM 2014, Conjecture 5.7.  
Source endpoint: for every group Gamma and every Gamma-equivariant positive contraction Q on l^2(Gamma), prove the sharp product-measure bounds with densities FK(Q) and 1-FK(I-Q).

This artifact is **PARTIAL source-scope progress only**. It does not solve the all-group conjecture and is not an admission/claim record.

## 1. A geometric-mean stochastic-order lemma for Bernoulli sums

### Lemma 1
Let `lambda_1,...,lambda_N` lie in `[0,1]`, let `xi_i` be independent Bernoulli variables with parameters `lambda_i`, and put

\[
p=(\lambda_1\cdots\lambda_N)^{1/N}.
\]

Then

\[
\sum_{i=1}^N \xi_i\ \succeq_{\rm st}\ \operatorname{Bin}(N,p).
\]

### Proof
If some `lambda_i=0`, then `p=0` and the assertion is trivial. Assume all parameters are positive.

First take two parameters `a,b` and put `g=sqrt(ab)`. For independent `B_a~Bern(a)` and `B_b~Bern(b)`,

\[
\Pr(B_a+B_b\ge2)=ab=g^2=\Pr(\operatorname{Bin}(2,g)\ge2),
\]

while

\[
\Pr(B_a+B_b\ge1)=a+b-ab\ge2g-g^2
=\Pr(\operatorname{Bin}(2,g)\ge1)
\]

by AM-GM. Hence

\[
B_a+B_b\succeq_{\rm st}\operatorname{Bin}(2,\sqrt{ab}).
\tag{1.1}
\]

Adding an independent random variable preserves stochastic domination. Therefore replacing any pair `(lambda_i,lambda_j)` by `(sqrt(lambda_i lambda_j),sqrt(lambda_i lambda_j))`, while keeping all other Bernoulli parameters fixed, can only decrease the distribution of the total sum in stochastic order.

Now work with `x_i=log lambda_i`. Repeatedly average pairs `(x_i,x_j)` on a connected averaging schedule. The mean of the `x_i` is preserved and their variance decreases to zero, so the parameter vector converges to the constant vector

\[
(\exp(\tfrac1N\sum_i x_i),\ldots,\exp(\tfrac1N\sum_i x_i))=(p,\ldots,p).
\]

At every finite averaging step the Bernoulli sum is stochastically no larger than at the preceding step, by (1.1). Tail probabilities are continuous in the parameters, so passing to the limit gives the claim. `□`

### Consequence for finite determinantal processes
For a finite positive contraction `Q` with eigenvalues `lambda_1,...,lambda_N`, the standard determinantal cardinality theorem gives

\[
|X|\stackrel d=\sum_{i=1}^N \operatorname{Bern}(\lambda_i),\qquad X\sim P^Q.
\]

If `Q` is equivariant on a finite group of order `N`, then

\[
\operatorname{FK}(Q)=(\det Q)^{1/N}=(\lambda_1\cdots\lambda_N)^{1/N}=p.
\]

Thus, **for every finite group and every equivariant positive contraction, all increasing events depending only on cardinality already satisfy Lyons's conjectured lower product bound**:

\[
\Pr_{P^Q}(|X|\ge m)\ge\Pr(\operatorname{Bin}(N,p)\ge m),\qquad m=0,\ldots,N.
\tag{1.2}
\]

Any finite-group counterexample to Conjecture 5.7 must therefore use an orbit-sensitive increasing event rather than a pure cardinality threshold.

## 2. Why invariant upper sets suffice

Let `mu=P^Q` and `nu=Ber(p)^{\otimes Gamma}` on a finite group Gamma. Both laws are invariant under left translation. For an arbitrary increasing event `E`, define

\[
f(A)=\frac1{|\Gamma|}\sum_{g\in\Gamma}{\bf 1}_E(gA).
\]

Then `f` is translation-invariant and increasing, and invariance of the two laws gives

\[
\mathbb E_\mu f=\mu(E),\qquad \mathbb E_\nu f=\nu(E).
\]

Because the state space is finite,

\[
f=\int_0^1 {\bf 1}_{\{f\ge t\}}\,dt,
\]

and each superlevel set `{f>=t}` is a translation-invariant increasing event. Consequently it is enough to check translation-invariant upper sets.

This reduction is important at order four: the regular action ceases to be transitive on the two-element layer, but it has only a few pair orbits.

## 3. The cyclic group Z/4Z

Every `Z/4Z`-equivariant Hermitian positive contraction is diagonal in the Fourier basis. Denote its four eigenvalues, in cyclic character order, by

\[
a,b,c,d\in[0,1],\qquad p=(abcd)^{1/4}.
\]

Translation has exactly six orbits on subsets:

1. the empty set;
2. four singletons;
3. four adjacent pairs;
4. two antipodal pairs;
5. four triples;
6. the full set.

There are exactly eight translation-invariant upper sets. Besides the trivial empty/all events, they are: full set only, `|X|>=3`, contains an adjacent pair, contains an antipodal pair, `|X|>=2`, and nonempty. The four cardinality events are already covered by (1.2), so only the two pair-orbit events remain.

Let `D_A` be the inclusion probability of any fixed adjacent pair, `D_O` that of any fixed antipodal pair, and `T` that of any fixed triple. Fourier calculation gives

\[
D_O=\frac{(a+c)(b+d)}4,
\tag{3.1}
\]

\[
D_A=\frac{(a+c)(b+d)+2(ac+bd)}8,
\tag{3.2}
\]

and, since the four principal `3x3` minors are equal and sum to the third elementary symmetric polynomial,

\[
T=\frac{abc+abd+acd+bcd}{4}.
\tag{3.3}
\]

Also `det Q=abcd=p^4`.

### 3.1 Antipodal-pair event
There are two antipodal pairs and their union is the full set, so inclusion-exclusion yields

\[
\Pr(E_O)=2D_O-p^4.
\]

Under product measure of density `p`,

\[
\Pr_p(E_O)=2p^2-p^4.
\]

By AM-GM,

\[
D_O=\frac{(a+c)(b+d)}4\ge\sqrt{acbd}=p^2.
\]

Hence `Pr(E_O)>=Pr_p(E_O)`.

### 3.2 Adjacent-pair event
Exact-set inclusion-exclusion gives

\[
\Pr(E_A)=4D_A-4T+p^4,
\]

whereas

\[
\Pr_p(E_A)=4p^2-4p^3+p^4.
\]

Thus it remains to prove

\[
D_A-T\ge p^2(1-p).
\tag{3.4}
\]

Set

\[
u=\sqrt{ac},\quad v=\sqrt{bd},\quad A=a+c,\quad B=b+d.
\]

Then `p=sqrt(uv)`, `A>=2u`, `B>=2v`, and (3.4), multiplied by eight, is

\[
F(A,B,u,v):=AB+2u^2+2v^2-2u^2B-2v^2A-8uv+8(uv)^{3/2}\ge0.
\tag{3.5}
\]

Because `0<=u,v<=1`,

\[
\frac{\partial F}{\partial A}=B-2v^2\ge2v(1-v)\ge0,
\]

and similarly

\[
\frac{\partial F}{\partial B}=A-2u^2\ge2u(1-u)\ge0.
\]

Therefore `F` is minimized at `A=2u`, `B=2v`. Writing `x=sqrt(u)` and `y=sqrt(v)`,

\[
\begin{aligned}
F(2u,2v,u,v)
&=2(u-v)^2-4uv(u+v-2\sqrt{uv})\\
&=2(x-y)^2\bigl((x+y)^2-2x^2y^2\bigr).
\end{aligned}
\tag{3.6}
\]

The last factor is nonnegative for `x,y in [0,1]`: indeed `(x+y)^2>=4xy` and `2x^2y^2<=2xy`. Hence (3.4) holds.

Thus the lower product domination holds for every invariant upper set on `Z/4Z`, and therefore for every increasing event.

## 4. The Klein four group (Z/2Z)^2

Again write the four Fourier eigenvalues as `a,b,c,d` and `p=(abcd)^{1/4}`. Translation has seven subset orbits: empty, singletons, three distinct pair-orbits (each a perfect matching of two pairs), triples, and full.

There are exactly twelve invariant upper sets. Besides cardinality/trivial events, the only ones to check are:

- `E_j`: contains a pair of one specified matching type `j`;
- `E_{j,k}`: contains a pair of either of two specified matching types.

For every nonzero group element `g`, the characters split into two `+1` and two `-1` values. Hence the principal two-point inclusion determinant has the form

\[
D_g=\frac{(\lambda_{+1}+\lambda_{+2})(\lambda_{-1}+\lambda_{-2})}{4}\ge p^2
\tag{4.1}
\]

by AM-GM. Since the two pairs in one matching are disjoint,

\[
\Pr(E_j)=2D_j-p^4\ge2p^2-p^4=\Pr_p(E_j).
\]

For two matching types, relabel the eigenvalues so that

\[
D_1=\frac{(a+c)(b+d)}4,\qquad
D_2=\frac{(a+b)(c+d)}4.
\]

The exact event probability is

\[
\Pr(E_{1,2})=2(D_1+D_2)-4T+p^4,
\]

while product measure gives

\[
\Pr_p(E_{1,2})=4p^2-4p^3+p^4.
\]

Thus the required inequality is

\[
D_1+D_2-2T\ge2p^2(1-p).
\tag{4.2}
\]

Multiplying (4.2) by four produces exactly the same polynomial-radical expression (3.5), after the harmless relabeling in which the doubled pair-products are `ad` and `bc` rather than `ac` and `bd`. The proof in (3.5)-(3.6) therefore applies verbatim. Hence every invariant upper set satisfies the lower product bound on `(Z/2Z)^2` as well.

## 5. Order-four theorem and upper domination

### Theorem 2
Let Gamma be a finite group with `|Gamma|<=4` and let Q be a Gamma-equivariant positive contraction on `l^2(Gamma)`. Then

\[
\boxed{\operatorname{Ber}(\operatorname{FK}(Q))^{\otimes\Gamma}\preccurlyeq P^Q
\preccurlyeq\operatorname{Ber}(1-\operatorname{FK}(I-Q))^{\otimes\Gamma}.}
\]

Both constants are optimal.

### Proof
Orders at most three were proved in the preceding R7-03 run. The two isomorphism classes of groups of order four are handled in Sections 3 and 4 above, proving the lower domination.

Apply the lower domination to `I-Q`. If `q=FK(I-Q)`, the complement process `Gamma\\X` has determinantal kernel `I-Q`, so a Bernoulli-`q` product set can be coupled inside `Gamma\\X`. Taking complements yields an upper coupling of `X` inside a Bernoulli-`1-q` product set.

Optimality is forced by the extreme events. If Bernoulli density `r` is dominated by `P^Q`, then the full-set event gives

\[
r^{|\Gamma|}\le\det Q=\operatorname{FK}(Q)^{|\Gamma|},
\]

so `r<=FK(Q)`. If `P^Q` is dominated by Bernoulli density `r`, the empty-set event gives

\[
\det(I-Q)\ge(1-r)^{|\Gamma|},
\]

so `r>=1-FK(I-Q)`. `□`

## 6. What this changes and what it does not

The preceding R7-03 screen proved the source conjecture for group orders at most three and identified order four as the first place where a Boolean layer splits into several translation orbits. This artifact closes that first gluing boundary completely.

It also proves a stronger structural statement valid for **every finite group**: cardinality thresholds can never witness failure of the lower FK bound. Any finite-group counterexample must exploit the internal orbit geometry of configurations with the same cardinality.

However, Lyons's source quantifies over all groups and all equivariant positive contractions. Nothing here controls arbitrary finite-group orbit posets, much less general infinite groups. Therefore `C0036` remains a **HARD / PARTIAL** source in this worker's screening and is **not** promoted to a CLOSABLE R7-03 assignment.
