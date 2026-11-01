Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — the requested GPT-6/maximum setting is a preference, not authenticated runtime telemetry, so I do not claim it ran.**

# C0036: candidate full sharp Lyons domination for every `S_3`-equivariant determinantal process

Date: 2026-09-20 UTC  
Role: C03 / R7-03, native ID `6aabe7be74008191b526b109ee4e9e80`  
Canonical ownership: preserved; this is the explicitly complementary progress-first role registered in `operations/progress_first_2026-09-20/REGISTRY.md`.  
Status: **CANDIDATE FULL PROOF for the finite group `Gamma=S_3`; PROVED PARTIAL relative to the full Lyons Conjecture 5.7.** The argument is analytic except for one finite exact symbolic certificate over all invariant upper sets; the certificate is supplied as a separate exact-arithmetic checker and has not yet received independent review.

## 1. Exact outside source target

Russell Lyons, *Determinantal Probability: Basic Properties and Conjectures*, Proc. ICM 2014, arXiv:1406.2707, Section 5.2, Conjecture 5.7.

Section 5.2 fixes a **sofic group** `Gamma`. For every `Gamma`-equivariant positive contraction

\[
0\le Q\le I\quad\text{on }\ell^2(\Gamma),
\]

write

\[
\operatorname{tr}_\Gamma(T)=\langle T\delta_e,\delta_e\rangle,
\qquad
\operatorname{FK}_\Gamma(Q)=\exp\!\left(\operatorname{tr}_\Gamma\log|Q|\right).
\]

The source asks for stochastic domination on **every increasing event**:

\[
\mathbf P^{\operatorname{FK}_\Gamma(Q)I}
\preccurlyeq \mathbf P^Q
\preccurlyeq
\mathbf P^{I-\operatorname{FK}_\Gamma(I-Q)I},
\tag{1.1}
\]

with both constants optimal. Lyons states immediately before Conjecture 5.7 that the conjecture is open even for finite groups. For a finite group of order `n`,

\[
\operatorname{FK}_\Gamma(Q)=(\det Q)^{1/n}.
\tag{1.2}
\]

This note proves (subject to the exact finite certificate described below) the complete sharp two-sided statement (1.1) for **every** `S_3`-equivariant positive contraction. It does not close the original all-sofic-group conjecture.

## 2. Previous checkpoint and the new pivot

The preceding R7-03 checkpoint proved the block Schur stochastic-decoupling theorem. In the strict finite case, for

\[
Q=\begin{pmatrix}A&X\\X^*&D\end{pmatrix}
\]

relative to `E=F sqcup B`, with

\[
C=D-X^*A^{-1}X,
\]

it proved

\[
\mathbf P^{A\oplus C}\preccurlyeq\mathbf P^Q,
\qquad
\det(A\oplus C)=\det Q.
\tag{2.1}
\]

Iterating (2.1) along an ordered block partition gives independent Schur-pivot DPPs below the original DPP, with the product of the pivot determinants equal to `det Q`.

The preceding report applied this only to a **normal** subgroup and then tried to uniformize one resulting block-product law. That last uniformization is false in general: the report gave an exact two-coset counterexample to it.

The new pivot has two parts:

1. normality was unnecessary: **right cosets of any subgroup** are invariant under its left action, so Schur reduction works for arbitrary subgroups; and
2. one need not find one product lower bound that works for every event. Since the target and DPP are group-invariant, **a different subgroup lower bound may be chosen for each invariant increasing event**.

For `S_3`, the `C_3` subgroup covers 64 of the 76 invariant upper sets, while a `C_2` subgroup covers exactly the remaining 12. This closes the finite group.

## 3. Schur reduction along right cosets of an arbitrary subgroup

### Theorem 3.1 — arbitrary-subgroup Schur lower bound

Let `Gamma` be a finite group, `H<=Gamma` any subgroup of order `m`, and suppose the lower half of Lyons's theorem is valid for every `H`-equivariant positive contraction. Put

\[
k=[\Gamma:H].
\]

Let `Q` be a strictly positive `Gamma`-equivariant contraction, and partition `Gamma` into right cosets

\[
\Gamma=Hg_1\sqcup\cdots\sqcup Hg_k.
\]

Apply the ordered block Schur factorization to these `k` blocks, obtaining positive contractions `L_1,...,L_k` on the respective cosets. Then each `L_j` is `H`-equivariant after identifying `Hg_j` with `H`, and therefore, with

\[
p_j=(\det L_j)^{1/m},
\qquad
p=(\det Q)^{1/|\Gamma|},
\]

one has

\[
\boxed{
\bigotimes_{j=1}^k \operatorname{Ber}(p_j)^{\otimes Hg_j}
\preccurlyeq \mathbf P^Q,
}
\tag{3.1}
\]

and

\[
\boxed{
\prod_{j=1}^k p_j=p^k.
}
\tag{3.2}
\]

#### Proof

For every `h in H`, left multiplication by `h` preserves every right coset `Hg_j`:

\[
h(Hg_j)=Hg_j.
\]

Hence it preserves every union of the first `j` blocks. Since `Q` commutes with the left regular action of `Gamma`, each principal block and every inverse occurring in the Schur formula commutes with the restricted left action of `H`. Every Schur pivot `L_j` is therefore `H`-equivariant.

The lower Lyons theorem on `H` gives

\[
\operatorname{Ber}(p_j)^{\otimes Hg_j}\preccurlyeq \mathbf P^{L_j}.
\]

Tensor these block couplings and then use the inherited block-Schur domination to obtain (3.1). The Schur determinant identity telescopes:

\[
\det Q=\prod_j\det L_j=\prod_j p_j^m.
\]

Taking `m`-th roots and using `|Gamma|=mk` yields (3.2). `QED`

The strictness assumption is harmless for the final theorem: after proving the desired inequality for

\[
Q_\varepsilon=(1-2\varepsilon)Q+\varepsilon I,
\qquad 0<\varepsilon<1/2,
\]

we let `epsilon downarrow 0`; all finite DPP event probabilities and determinants are continuous.

## 4. The subgroup base cases `C_2` and `C_3`

The required subgroup theorems are elementary and self-contained.

Let `C_m` act regularly on itself for `m=2` or `3`. Translation is transitive on every cardinality layer of `2^{C_m}`. Consequently, after averaging an increasing test over translations, it depends only on `|X|`. If the eigenvalues of an equivariant contraction are `lambda_1,...,lambda_m`, then

\[
|X|\ \stackrel d=\ \sum_{i=1}^m \xi_i,
\qquad \xi_i\sim\operatorname{Bern}(\lambda_i)
\]

independently.

Set

\[
p=(\lambda_1\cdots\lambda_m)^{1/m}.
\]

For `m=2`, the level-2 tail is equality, and the level-1 inequality follows from

\[
\sqrt{\lambda_1\lambda_2}+
\sqrt{(1-\lambda_1)(1-\lambda_2)}\le1.
\]

For `m=3`, the three nontrivial tails satisfy

\[
\Pr(|X|\ge3)=p^3,
\]

\[
\Pr(|X|\ge2)
=e_2(\lambda)-2p^3
\ge3p^2-2p^3
\]

by AM--GM on the three pairwise products, while generalized Holder gives

\[
p+\bigl((1-\lambda_1)(1-\lambda_2)(1-\lambda_3)\bigr)^{1/3}\le1,
\]

hence

\[
\Pr(|X|\ge1)\ge1-(1-p)^3.
\]

Thus the sharp lower product theorem holds on both `C_2` and `C_3`; applying it to `I-Q` and complementing gives their sharp upper halves as well.

## 5. Eventwise subgroup-cover criterion

The following observation is the structural step that repairs the failed one-product uniformization strategy.

### Lemma 5.1 — eventwise subgroup cover

Let `Gamma` be finite, let `Q` be `Gamma`-equivariant, and let

\[
p=(\det Q)^{1/|\Gamma|}.
\]

Suppose a collection of subgroups `{H_alpha}` has the lower Lyons theorem. Assume that for every **left-`Gamma`-invariant increasing event** `U`, there exists one `H_alpha` such that every product measure arising from Theorem 3.1 on the right `H_alpha`-cosets satisfies

\[
\mu_{\alpha,Q}(U)\ge \operatorname{Ber}(p)^{\otimes\Gamma}(U).
\tag{5.1}
\]

Then

\[
\operatorname{Ber}(p)^{\otimes\Gamma}\preccurlyeq \mathbf P^Q.
\tag{5.2}
\]

The subgroup `H_alpha` is allowed to depend on `U`.

#### Proof

Theorem 3.1 gives, for the subgroup chosen for `U`,

\[
\mathbf P^Q(U)\ge\mu_{\alpha,Q}(U),
\]

so (5.1) proves the desired inequality on every invariant increasing event.

Now let `A` be an arbitrary increasing event and average its indicator:

\[
f(x)=\frac1{|\Gamma|}\sum_{g\in\Gamma}\mathbf 1_A(gx).
\]

The function `f` is invariant and increasing. Since both `P^Q` and the uniform product law are invariant,

\[
\mathbf E_{P^Q}f=P^Q(A),
\qquad
\mathbf E_{\operatorname{Ber}(p)^\Gamma}f
=\operatorname{Ber}(p)^\Gamma(A).
\]

Every superlevel set `{f>=t}` is an invariant increasing event. The layer-cake formula and the already-proved event inequalities therefore give

\[
\mathbf E_{P^Q}f\ge
\mathbf E_{\operatorname{Ber}(p)^\Gamma}f.
\]

This is (5.2) for arbitrary increasing `A`. `QED`

The important point is that the subgroup may change with the superlevel event. No single Schur-product measure must dominate the uniform product law globally.

## 6. Exhausting the invariant increasing events of `S_3`

Write

\[
S_3=\langle r,s:r^3=s^2=e,\ srs=r^{-1}\rangle.
\]

The exact companion checker constructs the left-translation action on `2^{S_3}`. There are exactly

\[
16
\]

subset orbits. The induced orbit poset has exactly

\[
76
\]

upper ideals, hence exactly 76 left-invariant increasing events.

Everything below is an identity of exact integer/rational polynomials. No floating point sampling is used.

### 6.1. The `C_3=A_3` subgroup certifies 64 of 76 events

Take

\[
H=A_3=\{e,r,r^2\}.
\]

There are two right cosets. Theorem 3.1 supplies a product lower law having density `a` on `H` and density `c` on the other coset, with

\[
ac=p^2.
\]

Write

\[
a=x^2,\qquad c=y^2,\qquad p=xy,
\qquad 0\le x,y\le1.
\]

For each invariant upper set `U`, define the exact product-measure difference

\[
\Delta_U^{(3)}(x,y)
:=\mu_{x^2,y^2}(U)-\operatorname{Ber}(xy)^{\otimes6}(U).
\tag{6.1}
\]

The checker reconstructs all 76 `U` from the group law and proves:

- 9 of the differences vanish identically;
- 54 have the exact form
  \[
  \Delta_U^{(3)}=(x-y)^2R_U(x,y),
  \]
  where every Bernstein coefficient of `R_U` on `[0,1]^2` is nonnegative;
- 1 has the exact form
  \[
  \Delta_U^{(3)}=(x-y)^4R_U(x,y)
  \]
  with the same nonnegative-Bernstein certificate.

Thus `A_3` certifies 64 events. Across the nonzero certificates the checker verifies 1,311 exact Bernstein coefficients; 677 are zero and the smallest positive coefficient is `1/12`.

The remaining 12 upper sets are deterministic checker indices

\[
11,19,24,29,48,51,54,57,62,65,68,71.
\tag{6.2}
\]

For human traceability, if `O(T)={gT:g in S_3}` and an event is the upward closure of the listed minimal orbits, these are:

| checker index | minimal left-orbit generators |
|---:|---|
| 11 | `O({e,r,s,rs})`, `O({e,r^2,s,rs})` |
| 19 | `O({e,r,s,rs})`, `O({r,r^2,s,rs})` |
| 24 | `O({e,r^2,s,rs})`, `O({r,r^2,s,rs})` |
| 29 | all three preceding 4-set orbits |
| 48 | `O({e,r,s})`, `O({e,r^2,s})`, `O({r,r^2,s})` |
| 51 | `O({e,s})`, `O({r,r^2,s})` |
| 54 | `O({r,s})`, `O({e,r^2,s})` |
| 57 | `O({e,s})`, `O({r,s})` |
| 62 | `O({e,r,s})`, `O({r^2,s})` |
| 65 | `O({e,s})`, `O({r^2,s})` |
| 68 | `O({r,s})`, `O({r^2,s})` |
| 71 | `O({e,s})`, `O({r,s})`, `O({r^2,s})` |

The last event is precisely “hit both `A_3` cosets,” the event that defeated the preceding one-product normal-subgroup argument.

### 6.2. A `C_2` subgroup certifies exactly those 12 exceptions

Take

\[
K=\langle s\rangle=\{e,s\}.
\]

Its three right cosets are

\[
B_1=\{e,s\},\qquad
B_2=\{r,r^2s\},\qquad
B_3=\{r^2,rs\}.
\tag{6.3}
\]

Theorem 3.1 supplies a product lower law with densities `A,B,C` on these three two-point blocks and

\[
ABC=p^3.
\tag{6.4}
\]

For the 12 events in (6.2), their product-probability polynomials fall, under permutations of `(A,B,C)`, into six classes represented by checker indices

\[
11,29,48,54,65,71.
\tag{6.5}
\]

The exact classes are

\[
\{11,19,24\},\quad
\{29\},\quad
\{48\},\quad
\{51,54,62\},\quad
\{57,65,68\},\quad
\{71\}.
\tag{6.6}
\]

Fix one representative and call its product-event polynomial `F(A,B,C)`. The certificate proves the desired geometric-mean comparison in two global smoothing steps.

First put

\[
A=x^2,\qquad B=y^2,\qquad C=c,
\]

so replacing `(A,B)` by `(sqrt{AB},sqrt{AB})=(xy,xy)` preserves `ABC`. Exact symbolic division gives

\[
F(x^2,y^2,c)-F(xy,xy,c)
=(x-y)^2R_1(x,y,c),
\tag{6.7}
\]

and every Bernstein coefficient of `R_1` on `[0,1]^3` is nonnegative.

Now write the already-equalized value as

\[
g=u^3,\qquad C=v^3.
\]

Then the common geometric mean of `(g,g,C)` is

\[
p=(g^2C)^{1/3}=u^2v.
\]

Again exact symbolic division gives

\[
F(u^3,u^3,v^3)-F(u^2v,u^2v,u^2v)
=(u-v)^2R_2(u,v),
\tag{6.8}
\]

and every Bernstein coefficient of `R_2` on `[0,1]^2` is nonnegative.

Therefore

\[
F(A,B,C)\ge F(p,p,p)
\qquad\text{whenever }ABC=p^3
\tag{6.9}
\]

for each of the six representatives, and variable permutation proves it for all 12 events. The checker verifies 492 exact Bernstein coefficients for these `C_2` certificates; 245 are zero and the smallest positive coefficient is `1/126`.

Combining Sections 6.1 and 6.2, **every one of the 76 invariant increasing events has an exact subgroup-product certificate**.

## 7. Main theorem: full sharp two-sided domination on `S_3`

### Theorem 7.1

Let `Q` be an arbitrary `S_3`-equivariant positive contraction on `ell^2(S_3)`. Put

\[
p=(\det Q)^{1/6},
\qquad
r=(\det(I-Q))^{1/6}.
\]

Then, on every increasing event,

\[
\boxed{
\operatorname{Ber}(p)^{\otimes S_3}
\preccurlyeq \mathbf P^Q
\preccurlyeq
\operatorname{Ber}(1-r)^{\otimes S_3}.
}
\tag{7.1}
\]

Both constants are optimal.

#### Proof

First assume `0<Q<I`. For each invariant increasing event `U`, Sections 6.1--6.2 choose either `H=A_3=C_3` or `K=<s>=C_2`. The corresponding subgroup has the lower Lyons theorem by Section 4. Theorem 3.1 gives a block-product measure below `P^Q`, and the exact event certificate gives that block-product probability at least the uniform product probability at density `p`. Lemma 5.1 therefore yields

\[
\operatorname{Ber}(p)^{\otimes S_3}\preccurlyeq\mathbf P^Q.
\tag{7.2}
\]

For a boundary contraction, apply (7.2) to

\[
Q_\varepsilon=(1-2\varepsilon)Q+\varepsilon I
\]

and pass to the limit.

Apply the lower result to `I-Q`. If `Y~P^{I-Q}`, then `S_3\setminus Y~P^Q`. Complementation reverses stochastic order, giving

\[
\mathbf P^Q\preccurlyeq
\operatorname{Ber}(1-r)^{\otimes S_3}.
\]

Finally,

\[
P^Q[X=S_3]=\det Q=p^6,
\]

so no larger lower Bernoulli density can work. Applying the same argument to `I-Q`, equivalently the empty-set event of `P^Q`, shows the upper density is also optimal. `QED`

## 8. Exact certificate and what it proves

The companion checker is deliberately independent of any hand-entered list of 76 events. It:

1. constructs `S_3` from the presentation and its left action on all 64 subsets;
2. reconstructs the 16 subset orbits and the 76 upper ideals of their inclusion poset;
3. constructs each product-event probability exactly as a polynomial;
4. checks the `C_3` certificates for 64 events and identifies the 12 failures;
5. reconstructs the `C_2` block-product polynomials for those 12 events, verifies the six permutation classes, and certifies both smoothing steps;
6. converts every residual polynomial exactly from the power basis to the multivariate Bernstein basis over `[0,1]^d` and requires every rational coefficient to be nonnegative.

Its archived output ends

`ALL_EXACT_S3_SUBGROUP_COVER_CERTIFICATES_PASS`.

This is an exact finite symbolic certificate, not a numerical sample. It remains owner-track self-verification; an independent review should rederive or independently implement the orbit enumeration and the Schur/eventwise argument before the `S_3` theorem is treated as externally established.

## 9. Ledger delta and next attack

- full Lyons Conjecture 5.7 over all source sofic groups: **UNCHANGED / PROVED PARTIAL**;
- block Schur decoupling: inherited;
- normal-subgroup reduction: **strictly strengthened** to arbitrary subgroups via right cosets;
- eventwise subgroup-cover criterion: **NEW structural theorem**;
- arbitrary `S_3` lower and upper sharp product domination: **NEW CANDIDATE FULL PROOF for the complete finite group `S_3`**;
- no centrality, mean-zero, constant-coset, hidden-cyclic, low-rank, or local-neighborhood restriction remains in the `S_3` statement.

The next source-relevant attack should not return to another `S_3` spectral expansion. The new method suggests studying finite groups through the hypergraph of subgroup-coset partitions: determine whether every invariant increasing event admits a geometric-mean product comparison for at least one subgroup whose Lyons theorem is already known. The first useful tests are finite extensions built from already-solved `C_2`/`C_3` pieces (for example small dihedral or solvable groups), with the aim of extracting a reusable induction criterion rather than another isolated finite certificate. Any extension beyond finite groups will still require a genuine approximation/limit argument compatible with the Fuglede--Kadison determinant; the present theorem does not supply that infinite-sofic step.
