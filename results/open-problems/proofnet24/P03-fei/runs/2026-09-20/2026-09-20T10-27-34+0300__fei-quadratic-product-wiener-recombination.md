Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.

# P03 FEI — quadratic-product Wiener width and paid cross-block recombination

## Status / before-after

**Parent problem.** Friedgut--Kalai Fourier entropy--influence (FEI): prove one finite universal constant `C` such that
\[
H(\widehat f^{\,2})\le C I(f)
\]
for every Boolean function on every finite uniform cube.

**Source-level status before -> after:** **OPEN/PARTIAL -> OPEN/PARTIAL.** The universal finite upper bound remains **UNKNOWN -> UNKNOWN**. P03's inherited native finite-dimensional atlas remains **6 -> 6**. No finite check or restricted theorem below is promoted to full FEI.

**New mechanism-level movement.** This run proves an all-dimensional, fresh-variable-free **quadratic-product Wiener recombination theorem**. It removes the multiplicative accumulation in the quadratic-normalized Wiener parameter across arbitrarily many independent physical blocks, even when an arbitrary global quadratic phase couples all blocks. The controlling parameter is the **maximum** quadratic-normalized Wiener norm of one block, not a product over blocks and not the number of blocks.

The resulting theorem also gives a canonical reduction through the connected components of the degree-at-least-three algebraic-normal-form interaction hypergraph: arbitrary quadratic interactions between distinct high-degree components are paid at exact half-influence splits, so they do not compound the FEI constant. The unresolved full-scope difficulty is thereby localized to a single connected high-degree interaction core. This is a structural reduction, not full FEI.

No retired resolvent/interpolation inequality, false pointwise erasure shortcut, fixed-coefficient affine drift, Han absolute-overlap selector, derivative-degree scalar scheduler, blind curvature bound, or direct curvature/query ratio is revived.

## Dependencies actually consumed

The progress-first instruction was followed; no whole-repository scan was performed.

- `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`: T01 remains P03's assignment; roughly 90% of effort is new derivation; NM13-02 is the current complementary FEI theory worker.
- `operations/PROB10_2026-09-20.md`, blob `6f0fcee836d93371d43b84af1a55150fedc80779`: the theorem `L(Gamma_c f)<=12 Delta_aff(Gamma_c f)` uses appended fresh controls and the density hypothesis `2^{-c}M_0(f)<=1`; it is not full FEI and is not used below.
- `proofnet24/P03-fei/README.md`, blob `9201da45afcf21156ae078cc505d37b57a1ae4b7`: full FEI remains open; the fixed-coefficient drift, pointwise-erasure, resolvent, and Han absolute-overlap routes remain retired.
- Newest preceding owner report `proofnet24/P03-fei/runs/2026-09-20/2026-09-20T09-29-44+0300__fei-wiener-hereditary-arrangements.md`, blob `5a79ac2d8b2bbc29831c4b2764c18e24090a37e2`: proves raw-Wiener hereditary control and bounded affine-flat arrangements, but leaves quadratic/nonquadratic normalization and cancellation-sensitive max-splicing as the full-scope obstruction.
- P03 paid-recombination report `proofnet24/P03-fei/runs/2026-09-20/2026-09-20T02-31-19__fei-hereditary-recombination-refinement.md`, blob `8ffb9da5bc03c30e6ed5f62adc17640d1570878c`: supplies the exact one-step/tree entropy identity and the valid dependent-branch recombination payment. Only the exact identity is needed in the main cross-block proof below.
- Newest companion report `proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T10-08-55+0300__quadratic-normalized-wiener-hereditary.md`, blob `aec413db2f0dca3b1733e40ba9fc22807bc909b8`: defines
  \[
  \Lambda_2(g)=\min_{\deg q\le2}\Lambda((-1)^qg),
  \qquad \Lambda(g)=\sum_S|\widehat g(S)|,
  \]
  proves restriction monotonicity of `Lambda_2`, and proves
  \[
  H(g)\le C_{QW}(\Lambda_2(g))I(g),
  \quad
  C_{QW}(L)=\max\{15,2\log_2e+12\log_2L\}.
  \]
  It identifies the next obstruction as universally payable control of `log Lambda_2` or a second stopping potential terminating large-`Lambda_2` branches. The present theorem is complementary: it shows that disconnected high-degree blocks and arbitrary cross-block quadratics do **not** cause `Lambda_2` costs to accumulate.
- Current `POSTED.md` was checked. Its entropy/singularity paper is a distinct restricted percolation result; no posted unrestricted FEI theorem or exact theorem below is claimed.

The master head immediately before persistence was `fd59226aa09e627416414f3b6c85ad41a156397d`. All writes below use new immutable paths and do not overwrite peer or historical files.

## Current public-source scope

A fresh 20 September 2026 check of González--MacManus--Pereyra, arXiv:2606.00246, *Further evidence towards the Fourier Entropy-Influence conjecture*, still states universal FEI as a conjecture. Its restriction/stopping-tree framework proves proper subclasses and observes that a key branching inequality would imply the full conjecture if it held universally; it does not prove that universal inequality.

The Friedgut--Kalai 1996 attribution remains the source of the universal conjecture. A bounded fresh search also recovered older class/complexity upper bounds and composition results, but did not establish prior publication of the exact quadratic-product width theorem below. This is negative evidence only: **publication priority is UNVERIFIED**.

## 1. Notation and inherited exact identities

All logarithms are base two. Let
\[
p_S=\widehat f(S)^2,
\qquad
H(f)=-\sum_Sp_S\log_2p_S,
\qquad
I(f)=\sum_i\operatorname{Inf}_i(f).
\]
For the spectral random set `Z`, put
\[
B_i(f)=H(Z_i\mid Z_{-i}).
\]
For a physical split at coordinate `i`, write `f^+`, `f^-` for the two restrictions. The exact one-step entropy identity is
\[
H(f)-\frac{H(f^+)+H(f^-)}2
=B_i(f)+JS_i(f),
\tag{1.1}
\]
where `JS_i` is the equal-weight Jensen--Shannon divergence of the two restriction spectral laws. In particular
\[
0\le B_i(f)\le1,
\qquad
0\le JS_i(f)\le1,
\tag{1.2}
\]
the second inequality because equal-weight Jensen--Shannon divergence is mutual information with a fair binary branch label.

The exact influence identity is
\[
I(f)=\operatorname{Inf}_i(f)+\frac{I(f^+)+I(f^-)}2.
\tag{1.3}
\]
Weighted summation of (1.1) and (1.3) over any physical restriction tree gives the usual entropy and influence telescopes. Nothing here uses the retired false pointwise shortcut.

We also use the companion theorem, with its exact scope:
\[
H(g)\le C_{QW}(\Lambda_2(g))I(g),
\quad
C_{QW}(L)=\max\{15,2\log_2e+12\log_2L\},
\tag{1.4}
\]
and
\[
\Lambda_2(g^b)\le\Lambda_2(g)
\tag{1.5}
\]
for every physical restriction.

## 2. Quadratic-product Wiener width

### Definition 2.1

A **quadratic product presentation** of a Boolean function `f` is an exact representation
\[
f(x)=(-1)^{q(x)}\prod_{a=1}^m u_a(x_{B_a}),
\tag{2.1}
\]
where `(B_1,...,B_m)` is a partition of the active physical coordinates into pairwise disjoint nonempty blocks, `q` is an arbitrary multilinear `F_2` polynomial of degree at most two, and each `u_a` is Boolean on `B_a`.

For nonconstant `f`, define
\[
\boxed{
\Omega_2(f)
:=\min_{(2.1)}\max_a\Lambda_2(u_a).
}
\tag{2.2}
\]
For a constant function set `Omega_2(f)=1`. The minimum exists because the cube is finite and the one-block presentation is always available.

This parameter explicitly quotients both operations that should not be paid repeatedly: arbitrary quadratic twisting and independent physical products.

### Lemma 2.2 — elementary stability

For Boolean functions on finite cubes:

1. `1 <= Omega_2(f) <= Lambda_2(f)`.
2. If `r` is quadratic, then
   \[
   \Omega_2((-1)^r f)=\Omega_2(f).
   \tag{2.3}
   \]
3. Every physical restriction satisfies
   \[
   \boxed{\Omega_2(f^b)\le\Omega_2(f).}
   \tag{2.4}
   \]
4. If `f` and `g` use disjoint variable sets, then
   \[
   \boxed{
   \Omega_2(fg)\le\max\{\Omega_2(f),\Omega_2(g)\}.
   }
   \tag{2.5}
   \]

#### Proof

The one-block presentation with global quadratic chosen to minimize `Lambda_2(f)` gives item 1. For item 2, absorb `r` into the global quadratic in either direction. For item 3, restrict a minimizing presentation (2.1). The global quadratic remains quadratic, every untouched core is unchanged, and the affected core becomes a physical restriction; (1.5) says its `Lambda_2` cannot increase. Empty/constant blocks may be discarded. For item 4, concatenate minimizing block presentations for `f` and `g` and add their two global quadratics. QED.

The important distinction from raw Wiener norm is the **max** in (2.5), not a multiplicative cost.

## 3. Exact half-influence on a live cross-block quadratic edge

### Lemma 3.1

Suppose a current restriction has a presentation
\[
g=(-1)^q\prod_a u_a(x_{B_a}),
\tag{3.1}
\]
and the quadratic polar part of `q` contains a monomial `x_i x_j` with `i in B_a`, `j in B_b`, `a ne b`. Then
\[
\boxed{\operatorname{Inf}_i(g)=\frac12.}
\tag{3.2}
\]
The same holds for `j`.

#### Proof

Use the multiplicative physical derivative
\[
D_i g(x_{-i})=g(+1,x_{-i})g(-1,x_{-i}).
\]
All core factors except `u_a` cancel because they occur identically in the two restrictions. Thus
\[
D_i g=(-1)^{\partial_i q}\,D_i u_a,
\tag{3.3}
\]
up to an irrelevant constant sign. Since `x_i x_j` is a cross-block quadratic monomial, the affine polynomial `partial_i q` contains `x_j` with coefficient one. The function `D_i u_a` depends only on coordinates of `B_a\setminus\{i\}` and is independent of `x_j`. Averaging (3.3) first over the uniform bit `x_j` therefore gives
\[
\mathbb E D_i g=0.
\]
For a Boolean function,
\[
\operatorname{Inf}_i(g)=\Pr(D_i g=-1)=\frac{1-\mathbb E D_i g}{2},
\]
which proves (3.2). QED.

This is the key recombination payment. It does not assume any independence between the two physical branches; it exploits only an actually live external quadratic character bit.

### Corollary 3.2 — full entropy decrement costs at most four times queried influence

At a split covered by Lemma 3.1,
\[
H(g)-\frac{H(g^+)+H(g^-)}2
=B_i(g)+JS_i(g)
\le2
=4\operatorname{Inf}_i(g).
\tag{3.4}
\]

This uses only (1.1), (1.2), and the exact half-influence (3.2). No fresh variable is introduced.

## 4. Main theorem — quadratic-product Wiener recombination

### Theorem 4.1

For every Boolean function `f`, put `L=Omega_2(f)` and
\[
C=C_{QW}(L)=\max\{15,2\log_2e+12\log_2L\}.
\]
Then
\[
\boxed{H(f)\le C I(f).}
\tag{4.1}
\]
Moreover there exists a full adaptive physical restriction tree `T` such that
\[
\boxed{R_T(f)\le C I(f).}
\tag{4.2}
\]

The theorem is all-dimensional and fresh-variable-free. It is **not full FEI**, because `Omega_2(f)` is not shown to be universally bounded.

### Proof of the direct inequality

Fix a minimizing quadratic product presentation
\[
f=(-1)^q\prod_{a=1}^m u_a,
\qquad
\Lambda_2(u_a)\le L\quad\text{for every }a.
\tag{4.3}
\]

Build a finite stopping tree `T_0` as follows. At a current node, retain the induced restricted blocks. If the current quadratic polar graph of `q` has an edge joining two distinct blocks, choose one endpoint `i` of any such edge and query `x_i`. Otherwise stop.

Every internal split of `T_0` is covered by Lemma 3.1, so its queried influence is exactly `1/2`, and by (3.4) its entropy decrement is at most four times that queried influence.

The tree terminates because every query removes one physical variable. At a stopping leaf `ell`, the remaining quadratic has no cross-block polar edge. Hence it decomposes as
\[
q_\ell=c+\sum_a q_{a,\ell},
\tag{4.4}
\]
where every `q_{a,ell}` is quadratic on the residual coordinates of block `B_a`; affine terms are included in the corresponding block. Therefore
\[
f_\ell=\pm\prod_a v_{a,\ell},
\qquad
v_{a,\ell}=(-1)^{q_{a,\ell}}(u_a)_{\ell}.
\tag{4.5}
\]
By quadratic invariance and restriction monotonicity,
\[
\Lambda_2(v_{a,\ell})
=\Lambda_2((u_a)_\ell)
\le\Lambda_2(u_a)
\le L.
\tag{4.6}
\]
Applying the companion direct theorem (1.4) to each factor gives
\[
H(v_{a,\ell})\le C I(v_{a,\ell}).
\tag{4.7}
\]
Because the factors use disjoint coordinates, their squared Fourier law is a product law and their influences add. Hence
\[
H(f_\ell)=\sum_aH(v_{a,\ell})
\le C\sum_aI(v_{a,\ell})
=C I(f_\ell).
\tag{4.8}
\]

Let `w_v` be the cylinder weight of node `v`, let
\[
Q_0=\sum_{v\in T_0^\circ}w_v\operatorname{Inf}_{i(v)}(f_v),
\qquad
I_L=\sum_{\ell}w_\ell I(f_\ell).
\]
The exact influence telescope gives
\[
I(f)=Q_0+I_L.
\tag{4.9}
\]
The exact entropy telescope, (3.4), and (4.8) give
\[
H(f)
\le4Q_0+C I_L.
\tag{4.10}
\]
Since `C>=15>4`,
\[
H(f)\le C(Q_0+I_L)=CI(f).
\]
This proves (4.1). QED.

### Proof of the hereditary allocation statement

Lemma 2.2 shows that every physical restriction `g` of `f` satisfies
\[
\Omega_2(g)\le L.
\]
Applying (4.1) to `g` gives
\[
H(g)\le C I(g).
\tag{4.11}
\]
Han--Shearer gives
\[
\sum_iB_i(g)\le H(g),
\]
while
\[
I(g)=\sum_i\operatorname{Inf}_i(g).
\]
Therefore, unless `g` is constant, at least one remaining coordinate `i` satisfies
\[
B_i(g)\le C\operatorname{Inf}_i(g).
\tag{4.12}
\]
Query such a coordinate and repeat independently on both descendants. Continuing to constants gives a full adaptive tree `T`. Multiplying (4.12) by node cylinder weights and summing, then using the exact influence telescope for a full tree, yields
\[
R_T(f)
\le C\sum_{v\in T^\circ}w_v\operatorname{Inf}_{i(v)}(f_v)
=C I(f).
\]
This proves (4.2). QED.

### What the theorem actually removes

Suppose there are arbitrarily many disjoint cores with
\[
\Lambda_2(u_a)\le L.
\]
A naive global residual-Wiener estimate can accumulate a product-scale upper bound as the number of factors grows. Theorem 4.1 instead keeps the coefficient at exactly `C_QW(L)`, independent of the number and sizes of blocks and independent of the rank/density of an arbitrary quadratic coupling between them.

The theorem does **not** assert that the actual global `Lambda_2` equals a product, nor that every Boolean function has bounded `Omega_2`. It removes a proof-artifact accumulation, not the universal obstruction.

## 5. Canonical algebraic-normal-form reduction

Every Boolean `f` has a unique sign-polynomial representation
\[
f(x)=(-1)^{P(x)}
\]
with multilinear `P` over `F_2`. Write
\[
P=P_{\le2}+P_{\ge3}.
\]
Form the hypergraph whose hyperedges are supports of the monomials of `P_{\ge3}`. Let `B_1,...,B_m` be its nontrivial connected components, and let `P_a` be the sum of all high-degree monomials supported in component `B_a`. Then
\[
f=(-1)^{P_{\le2}}\prod_{a=1}^m(-1)^{P_a},
\tag{5.1}
\]
with disjoint physical blocks. Variables absent from `P_{\ge3}` may be absorbed into the quadratic factor or harmless singleton constant cores.

Therefore Theorem 4.1 gives the canonical corollary
\[
\boxed{
H(f)
\le
C_{QW}\!\left(
\max_a\Lambda_2((-1)^{P_a})
\right) I(f),
}
\tag{5.2}
\]
with the convention that the maximum is `1` if `P_{\ge3}=0`; the same parameter yields a hereditary allocation certificate.

### Interpretation

Arbitrary quadratic interactions between distinct connected high-degree ANF components are now fully paid: they create half-influence query coordinates and cost no factor-count penalty. Thus a universal hereditary FEI proof may, without losing a constant through this recombination mechanism, focus on a **single connected degree-at-least-three interaction core**.

This does not solve that connected-core problem. A connected high-degree core can have unbounded quadratic-normalized Wiener norm, and no universal bound on the right side of (5.2) is proved.

## 6. Relation to existing P03/NM13-02 results

- P03's preceding raw-Wiener theorem controls `Lambda(f)` and bounded affine-flat arrangements. The new `Omega_2` quotient is no larger than `Lambda_2`, is invariant under arbitrary global quadratic twists, is restriction-nonincreasing, and uses a max under disjoint products.
- NM13-02's newest theorem pays one global quadratic normalization and leaves large `Lambda_2` as its next obstruction. The present theorem shows that large global complexity caused merely by combining many separately controlled high-degree blocks is not a real obstruction: only the worst block is paid.
- The earlier P03 quadratic-twist theorem for symmetric independent cores already had a stronger constant on that special class. The theorem here has broader cores—any core with bounded `Lambda_2`—at a weaker explicit constant. It is an extension in scope, not a replacement of the sharper symmetric theorem.
- The fresh-control theorem from `PROB10` is not used. All physical branches remain the actual dependent restrictions of the original cube.

## 7. Sanity checks executed now

The preserved checker is

`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T10-27-34+0300__check_quadratic_product_wiener.py`

and its preserved output is

`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T10-27-34+0300__quadratic_product_wiener_check.json`.

Executed results:

1. **Exhaustive n=4 cross-edge test.** All `16 x 16` Boolean core pairs on blocks of size two and all `15` nonempty cross-block quadratic edge sets were checked: `3,840` structured functions and `12,288` incident-coordinate checks. Every queried cross-edge endpoint had disagreement count exactly `8/16`, hence influence exactly `1/2`. Maximum exact half-influence count error: `0`. Maximum observed `B_i-1`: `0.0`.
2. **Sampled n=6 test.** `2,000` deterministic-seed cases with arbitrary 3-bit cores, nonempty cross-block quadratic edges, random within-block quadratic edges, affine terms and constants produced `10,584` incident-coordinate checks. Maximum exact half-influence count error: `0`. The sampled direct theorem had maximum `H-CI=-20.5`; maximum sampled `H/I=2.1084585933443494`.
3. **Factor-count demonstration.** Repeated 3-bit one-point cores have `Lambda_2=2.5` in the exact small-core enumeration. With deterministic cross-block quadratic couplings, the observed `H/I` values for one, two and three blocks were approximately `2.95589`, `2.34050`, and `2.21070`, while the theorem uses the same block parameter `2.5` in all three cases (`C_QW(2.5)=18.748527220426276...`). This is illustration only; factor-count independence is proved analytically above.

Checker status: `PASS`. These are self-checks, not independent audits and not evidence of full FEI closure.

Checker creation commit: `e5421bbaab4dd2c73e2e13cdc64a19c46c0bc63a`.
Output creation commit: `e81ce3a9b96b5200ebc17c0d738aeb13e03b3a8e`.

## 8. Failed routes retained / exact remaining obstruction

Retained failures and corrections:

- false pointwise erasure inequality: retired;
- every fixed finite affine-drift coefficient closure killed by the recovered majority obstruction: retired;
- full-resolvent/interpolation pointwise target: retired;
- Han all-coordinate absolute-overlap selector: refuted by shifted thresholds;
- derivative-degree scalar scheduling: refuted by one-point defects;
- character-defect selector: refuted by majority;
- blind root square-curvature and direct consumed-curvature/query payment: refuted by quadratic/cubic-star examples;
- individual affine-flat codimension as a recombination cost: invalid because parallel flats can algebraically cancel/recombine.

The new theorem removes **disconnected high-degree block recombination** as an additional obstruction. The remaining full-scope target is now sharper:

> prove a universal hereditary allocation estimate for one connected degree-at-least-three ANF interaction core, or find a decisive connected-core family showing that `Omega_2`/`Lambda_2`-based stopping cannot be universally paid.

A nonredundant next attack is to study connected high-degree cores by separator width rather than factor count: query a small physical separator of the degree-at-least-three interaction hypergraph, use Theorem 4.1 after the descendant splits into components, and try to charge separator queries to actual influence. If bounded-treewidth high-degree interaction hypergraphs admit a dimension-free hereditary constant, that would extend the max-splicing mechanism beyond exact disconnected products. Conversely, a connected bounded-width family with diverging hereditary allocation would decisively kill this route.

## ledger_delta

```yaml
ledger_delta:
  track: P03
  parent: T01_FEI
  source_status_before: OPEN
  source_status_after: OPEN
  universal_C_before: UNKNOWN
  universal_C_after: UNKNOWN
  native_finite_atlas_before: 6
  native_finite_atlas_after: 6
  new_result:
    name: quadratic_product_wiener_width_recombination
    status: PROVED_SELF_CHECKED_PENDING_INDEPENDENT_REVIEW
    statement: "H(f) <= C_QW(Omega_2(f)) I(f), and some full physical restriction tree has R_T <= C_QW(Omega_2(f)) I(f)"
    C_QW: "max{15, 2 log_2 e + 12 log_2 L}"
    fresh_variables: false
    all_dimensions: true
    full_FEI: false
  new_mechanism:
    cross_block_quadratic_edge_influence: "exactly 1/2"
    product_cost: "max block Lambda_2, not product / block count"
    canonical_reduction: "degree>=3 ANF interaction components; only worst connected component paid"
  latest_peer_consumed:
    path: proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T10-08-55+0300__quadratic-normalized-wiener-hereditary.md
    blob: aec413db2f0dca3b1733e40ba9fc22807bc909b8
  checker:
    status: PASS
    commit: e5421bbaab4dd2c73e2e13cdc64a19c46c0bc63a
  checker_output:
    commit: e81ce3a9b96b5200ebc17c0d738aeb13e03b3a8e
  independent_review: PENDING
  publication_priority: UNVERIFIED
  remaining_obstruction: "hereditary allocation for a single connected degree>=3 ANF interaction core; next try separator-width splicing"
```

**End of complete run report.**
