# account02/B18 — source-exact Bernoulli-switching transfer for quadratic forms

**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Run:** `20260922T130234Z-account02-B18-qform-r11b`  
**Assignment:** Literature-to-proof transfer  
**Status:** `SUPPORTING_LEMMA_PROVED / SCALE-DEPENDENT_STRUCTURE / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target and first unpaid implication

The full target remains: for arbitrary independent real `X_i` with densities `0<=f_i<=1` and arbitrary real symmetric `A` having at least three eigenvalues of absolute value at least one, prove

`P(X^T A X in [t,t+h]) <= C h`

for one universal finite `C`, all real `t`, all `h>0`, or give a valid counterexample.

The first unpaid implication addressed here is a source-valid structural reduction for a highly non-diagonal form **without rotating the inputs**: quantify what many physically disjoint, scale-`h` off-diagonal coefficients force. The result below does not close the `O(h)` target, but it proves that fixed positive small-ball mass is incompatible with arbitrarily large physical matching rank at the same scale.

All live corrections were enforced. In particular, this report does not use law-uniform pointwise Fresnel decay, unrestricted fiber suprema, independence after rotation, a single cross-minor extraction, a conditional density cap after sum/difference conditioning, or a forced single-pivot rank-two Schur block.

## 2. Primary source matched exactly

Raghu Meka, Oanh Nguyen, and Van Vu, **Anti-concentration for Polynomials of Independent Random Variables**, *Theory of Computing* 12 (2016), Article 11, DOI `10.4086/toc.2016.v012a011`.

The final published Theorem 1.7 states the following. For a degree-`d` multilinear polynomial `P` on independent `p`-biased Bernoulli variables, define `rank(P)=r` to be the largest number of pairwise disjoint degree-`d` monomials whose coefficients have absolute value at least one. Put `alpha=min(p,1-p)` and `r_tilde=2^d alpha^d r`. If `r_tilde>=3`, then for every interval `I` of length one,

`P(P(xi) in I) <= min( B d^(4/3) sqrt(log r_tilde) / r_tilde^(1/(4d+1)), exp(B d log(d) log log(r_tilde) + B d^2 log(d))/sqrt(r_tilde) )`,

where `B` is the absolute constant supplied by the source and `log` is natural logarithm. The source does **not** give a numerical value of `B`, so none is invented here.

The theorem itself is on Bernoulli variables, not on the owner's continuous inputs. The transfer below is source-valid because the Bernoulli variables are introduced only as an exact random-switch representation of the original product law.

## 3. Exact Bernoulli-switch representation

For each physical coordinate `i`, take two independent copies `X_i^0,X_i^1` of `X_i`, and let `eta_i` be independent Bernoulli(1/2), independent of all copies. Define

`D_i = X_i^1-X_i^0`, `Z_i=X_i^0+eta_i D_i`.

The `Z_i` are independent and each has exactly the same law as `X_i`; hence `Z` has exactly the target product law.

Conditional on the two copy-vectors, `Q(Z)=Z^T A Z` is a degree-at-most-two **multilinear** polynomial in `eta`. Indeed `eta_i^2=eta_i`, so the diagonal square terms contribute only constants and linear terms, while for `i<j` the coefficient of `eta_i eta_j` is exactly

`2 A_ij D_i D_j`.

Thus the source theorem can be applied conditionally in the original physical coordinates even when the original quadratic form has arbitrary diagonal entries.

## 4. New theorem: scale-dependent matching anti-concentration

Fix `0<a<1/2` and an interval length `h>0`. Define a physical graph `G_{h,a}(A)` on `[n]` by putting an edge `{i,j}` when

`|A_ij| >= h/(2 a^2)`.

Let `r` be its matching number, and put

`q=(1-2a)^2`, `m=floor(q r/2)`.

For integer `s>=3`, define the final-published Meka--Nguyen--Vu profile at degree two and bias one half by

`psi_B(s) = min{ 1, B*2^(4/3)*sqrt(log s)/s^(1/9), exp(2 B log(2) log log(s) + 4 B log(2))/sqrt(s) }`,

and `Psi_B(m)=sup_{integer s>=m} psi_B(s)`.

### Theorem `QFORM-MNV-SWITCHING-MATCHING-v1`

If `m>=3`, then for every real `t`,

`P( X^T A X in [t,t+h] ) <= exp(-q r/8) + Psi_B(m)`.

This theorem assumes only independence and the density caps `f_i<=1`. It has no moment, centering, support, identical-distribution, log-concavity, or eigenbasis-independence hypothesis.

### Proof

For every `i` and every realized `X_i^0=x`,

`P(|D_i|<a | X_i^0=x) = integral_{x-a}^{x+a} f_i(y)dy <= 2a`.

Hence `P(|D_i|>=a)>=1-2a`. Choose a maximum matching `M` of `G_{h,a}`. Because its edges are vertex-disjoint, the events

`E_{ij}={|D_i|>=a, |D_j|>=a}`, `{i,j} in M`,

are independent and each has probability at least `q=(1-2a)^2`.

Let `S` be the number of active matching edges. Its mean is at least `q r`. The standard multiplicative Chernoff lower-tail estimate therefore gives

`P(S<q r/2) <= exp(-q r/8)`.

On every active edge,

`| 2 A_ij D_i D_j / h | >= 2 * [h/(2a^2)] * a^2 / h = 1`.

Consequently, conditional on the copy-vectors, the normalized multilinear polynomial `Q(Z)/h` has Meka--Nguyen--Vu rank at least `S`. The selector variables are independent `p=1/2` Bernoulli variables. In source Theorem 1.7, with `d=2` and `alpha=1/2`, one has exactly

`r_tilde = 2^2 (1/2)^2 S = S`.

On `{S>=m>=3}`, Theorem 1.7 therefore bounds the conditional probability of any interval of length one by at most `Psi_B(m)`. On the complementary event use the trivial bound one. Averaging over the two copy-vectors and using `Z law = X law` yields

`P(Q(X) in [t,t+h]) <= exp(-q r/8)+Psi_B(m)`.

QED.

## 5. Concrete specialization and sparse-core corollary

Taking `a=1/4` gives `q=1/4`. Let `nu_h(A)` be the matching number of the graph with edges

`|A_ij| >= 8h`.

For `r=nu_h(A)>=24`,

`P(Q in [t,t+h]) <= exp(-r/32) + Psi_B(floor(r/8)).`

Because the right-hand side tends to zero with `r`, for every fixed `delta>0` there is a finite source-dependent threshold `R_B(delta)` such that

`sup_t P(Q in [t,t+h]) >= delta`

forces `nu_h(A)<R_B(delta)`.

The endpoints of a maximal matching form a vertex cover. Hence, under the same positive-mass hypothesis, there is a physical coordinate set `S` with

`|S| < 2 R_B(delta)`

such that every off-diagonal coefficient entirely outside `S` satisfies

`|A_ij| < 8h`.

Thus any fixed positive small-ball mass at scale `h` forces all scale-`h`-large off-diagonal interactions into a dimension-free physical core. This is a structural statement in the original coordinate system; it does not invoke spectral rotation.

## 6. Completed partner result applied

I consumed the completed account03/B18 report `20260922T120058Z-account03-B18-qform-r1`, scientific commit `53bf1a45bf46dfa09a963d95935f6413c911d1b5`. Its source-exact Banks transfer proves that a genuine physical bipartite block

`[[0,B],[B^T,0]]`

with `sigma_2(B)>=1` gives

`||p_Q||_infinity <= 2 sqrt(e pi)`,

hence

`P(Q in [t,t+h]) <= 2 sqrt(e pi) h`.

This is used as a complementary exact branch: when a rank-two physical singular block is actually present, the partner result upgrades all scales to the desired linear `h` bound. When no such block is available, `QFORM-MNV-SWITCHING-MATCHING-v1` still pays for a large *matching* of physical off-diagonal coefficients at the current scale and forces positive-mass concentration into a bounded coordinate core.

The live correction `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE` is respected: I do **not** claim that the three-eigenvalue hypothesis forces the partner's bipartite block after one Schur pivot.

## 7. Why this does not yet close QFORM

The Meka--Nguyen--Vu profile is a rank anti-concentration bound at a fixed interval scale; it is not linear in `h`. For a fixed finite matrix, `nu_h(A)` stabilizes as `h` tends to zero, so the theorem alone cannot imply `P(Q in [t,t+h])=O(h)`.

The sparse-core corollary also leaves a potentially huge cloud of entries of size below `O(h)`. Their aggregate operator norm can be large, so they cannot simply be deleted. This is the exact remaining connection to the full target:

> **`QFORM-SCALE-CORE-TO-LINEAR-v1` (OPEN):** combine the scale-dependent bounded physical core with a dimension-free control of the sub-`h` diffuse remainder, or show that the diffuse remainder itself yields an integrated/bilinear anti-concentration payment, to upgrade the structural reduction to `P(Q in [t,t+h])<=C h`.

The newly recorded correction against single-pivot rank-two extraction makes this scale-core/diffuse-remainder formulation preferable to another forced-minor claim.

## 8. Source screening

The final published Meka--Nguyen--Vu theorem is used with its exact Bernoulli hypotheses and its source constant `B`; no claim is made that its Bernoulli conclusion directly applies to the original continuous variables. The exact copy-switch identity is the bridge.

Results requiring Gaussian inputs, subgaussian moments, log-concavity, bounded variation of the marginal densities, compact support, or independence after diagonalizing `A` were not promoted to the target. The recent Gaussian quadratic-form literature is therefore a subclass source only, not a closure route here.

## 9. Claim status

- `QFORM-MNV-SWITCHING-MATCHING-v1`: **PROVED_IN_SOURCE_TRANSFER**, analytic proof above; independent end-to-end review false.
- Scale-`h` bounded-core corollary: **PROVED**, conditional only on fixed positive small-ball mass `delta` at that scale.
- account03/B18 physical bipartite density branch: **CONSUMED COMPLETED PARTNER RESULT**, not reproved here.
- `QFORM-SCALE-CORE-TO-LINEAR-v1`: **OPEN**.
- Full `QFORM-DENSITY-THREE-LARGE-EIGENVALUES`: **OPEN / NOT PROVED**.
