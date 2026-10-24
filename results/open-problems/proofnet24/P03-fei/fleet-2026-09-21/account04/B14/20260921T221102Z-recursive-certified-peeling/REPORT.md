# B14 FEI posterior-crossing strategy — recursive certified peeling and a compiler-ready crossing branch

**Status:** PARTIAL / new source-exact reduction. Full uniform-cube Fourier entropy--influence remains **OPEN / NOT PROVED**.

**Execution:** `WITHOUT_VERIFIED_BRAIN`. The current runtime had Python but no importable `math_brain`, `lean`, `lake`, or `elan`; no brain-assisted or formal-checker claim is made.

**Joint interface:** A — realizable adaptive physical restriction. This run deliberately changes mechanism from the preceding Bernoulli posterior-variance selector. It recursively peels every currently certifiable near-subcube maximum-pivotality row and proves exact nonreuse across the whole physical restriction tree.

## 1. Exact completed inputs consumed

1. **account01/B18 newest compatible synthesis**: `proofnet24/P03-fei/fleet-2026-09-21/account01/B18/20260921T2205Z-folded-cooling-compiler/REPORT.md`, blob `9f2bb40584be20e5e440e7f3913873c34858bc91`. It proves the character-invariant folded activation bank and the conditional `(gamma,K,lambda)` compiler. Its remaining A-interface obligation is to find one physical block/survivor pair with
   \[
   c_j(A)\ge\gamma j_j,
   \qquad
   E_A-\lambda\Lambda_A\le K h_2(j_j),
   \]
   for fixed universal constants, or force a complementary already-paid branch.

2. **account01/B18 curvature-refunded inequality**: `account01/B18/20260921T1856Z-curvature-refunded-crossing/REPORT.md`, blob `ef9f471c019a7d81e9864fd457a0e4bae9da890d`. At a median-centered state,
   \[
   \Delta_A\mathcal F\le B_A-\sum_{j\notin A}\mathfrak j'(p_j)c_j(A),
   \]
   while on an `F/J`-critical core of ratio `rho`,
   \[
   B_A\ge \rho I_A+
   \sum_{j\notin A}(\rho+\mathfrak j'(p_j))c_j(A).
   \tag{1.1}
   \]
   This is the exact source-to-next-arrow use below: the new selected block creates a quantitatively large *actual* survivor crossing, so (1.1) immediately turns it into a curvature-refunded critical-core obstruction rather than a prescribed-coordinate assertion.

3. **account02 joint near-subcube block theorem**, `proofnet24/P03-fei/fleet-2026-09-21/account02/interactive/20260921T192650Z-joint-fei-subcube-peeling/ADDENDUM.md`, blob `baa3155a268d936d6b191667ee71a6df84969292`, Theorem C.1. If a pivot `x` has sensitivity event `E_x`, a codimension-`r` coordinate subcube `Q` on physical controls `Z`, `q=2^{-r}`, and
   \[
   I_Z\le r I_x,
   \qquad
   e:=\mu(E_x\triangle Q)\le \frac{q}{16r},
   \tag{1.2}
   \]
   then
   \[
   \Delta_ZH\le12 I_Z.
   \tag{1.3}
   \]
   Its proof also gives the lower boundary estimate
   \[
   I_Z\ge rq-r e\ge q\left(r-\frac1{16}\right).
   \tag{1.4}
   \]
   The known-false fixed-relative `q/16` replacement is not used.

4. **account01/B13 block crossing theorem**: if an event `E` of density `p` differs from a coordinate subcube `Q` by `e`, revealing the defining controls gives
   \[
   c(Z)\ge(p-e)_+.
   \tag{1.5}
   \]

5. The exact centered folded block drift remains
   \[
   \boxed{D_A=J-\mathbb E J_{\rm child}=I_A+C_A.}
   \tag{1.6}
   \]
   The Boolean addressing obstruction remains live; nothing below asserts cheap payment at every prescribed coordinate or block.

## 2. New local theorem: every C.1 block is automatically a universal crossing certificate

Median-center the current Boolean state by a character, so every folded influence equals its ordinary influence and is at most `1/2`. Let `x` be a **maximum-influence** relevant coordinate, put
\[
p=I_x,
\]
and suppose a coordinate subcube `Q` of codimension `r>=1` in the sensitivity domain of `x` satisfies (1.2), with defining controls `Z`.

Because `x` is maximum influence,
\[
I_Z\le rp.
\tag{2.1}
\]
Thus Theorem C.1 applies automatically once the support-error condition holds.

### Theorem 2.1 — uniform crossing fraction

The selected block satisfies
\[
\boxed{
c_x(Z)\ge\gamma_r p,
\qquad
\gamma_r:=1-\frac1{16r-1}\ge\frac{14}{15}.}
\tag{2.2}
\]

**Proof.** Densities differ by at most symmetric-difference measure, so `|p-q|<=e`, hence `q<=p+e`. From `e<=q/(16r)`,
\[
e\le\frac{p+e}{16r},
\]
so `(16r-1)e<=p`. Equation (1.5) now gives
\[
c_x(Z)\ge p-e\ge\left(1-\frac1{16r-1}\right)p.
\]
The minimum over `r>=1` is `14/15`. QED.

This is an actual multi-bit physical posterior crossing. It does not conflict with the high-ratio fact that singleton crossings vanish when `p<=1/4`.

### Theorem 2.2 — the block's control influence is no larger than the target marginal Shannon entropy

Under the same hypotheses,
\[
\boxed{I_Z\le rp\le h_2(p).}
\tag{2.3}
\]

**Proof.** From `p<=q+e`,
\[
p\le2^{-r}\left(1+\frac1{16r}\right).
\]
Set `delta_r=log_2(1+1/(16r))`. Then
\[
\frac{h_2(p)}p
=\log_2\frac1p+\frac{1-p}{p}\log_2\frac1{1-p}
\ge r-\delta_r+\frac{1-p}{\ln2}.
\]
Here `p<=1/2`, so the final term is at least `1/(2 ln2)`, while
\[
\delta_r\le\frac1{16r\ln2}<\frac1{2\ln2}.
\]
Therefore `h_2(p)/p>=r`. Combine with (2.1). QED.

### Corollary 2.3 — direct discharge of the newest account01/B18 certificate on this branch

Let
\[
E_Z=\Delta_Z\mathcal F=B_Z-Q_Z,
\qquad Q_Z\ge0,
\]
and let `Lambda_Z>=0` be the account01/B18 folded activation drop at the current dimension-cooling scale. For **every** `lambda>=0`,
\[
\boxed{
E_Z-\lambda\Lambda_Z
\le E_Z\le B_Z\le\Delta_ZH
\le12I_Z\le12h_2(p).}
\tag{2.4}
\]
Together with (2.2), every such near-subcube maximum row supplies a genuine
\[
\boxed{(\gamma,K,\lambda)=(14/15,12,\lambda)}
\tag{2.5}
\]
certificate in the exact sense of account01/B18's newest compiler.

This closes that compiler obligation **for the whole C.1-certifiable branch with constants independent of `r`**. It does not prove that every hard core has such a row.

### Corollary 2.4 — explicit use of the curvature-refunded inequality

If the current state is additionally an `F/J`-critical core of ratio `rho`, then (1.1), (1.3), and (2.2) imply
\[
\boxed{
(\rho+\mathfrak j'(p))\gamma_r p
\le (12-\rho)I_Z
\le r(12-\rho)p.}
\tag{2.6}
\]
Hence a C.1-certifiable maximum row of codimension `r` can occur only if
\[
\boxed{
(\rho+\mathfrak j'(p))\gamma_r\le r(12-\rho).}
\tag{2.7}
\]
This is the exact source-to-next-arrow use of the requested account01/B18 curvature refund.

## 3. New global theorem: a realizable recursive peeling policy with total unpaid Shannon entropy O(J)

Define the following physical policy at every reached node `u`.

1. Character-center the current restriction `f_u` (this changes neither `H` nor `J`, and does not alter the underlying physical restriction tree).
2. Among all maximum-influence pivots, search for a coordinate subcube satisfying `e<=2^{-r}/(16r)`.
3. If one exists, choose one deterministically, reveal its full physical defining block `Z_u`, and recurse independently on every resulting child.
4. If none exists, stop at that leaf.

Every internal step fixes at least one new coordinate, so the policy terminates after finitely many physical reveals on every branch.

Let `w_u` be the reach probability of an internal node. Then:

### Theorem 3.1 — exact nonreuse across the whole adaptive tree

\[
\boxed{
\sum_u w_u B_{Z_u}
\le
\sum_u w_u\Delta_{Z_u}H
\le12\sum_u w_u I_{Z_u}
\le12\sum_u w_uD_{Z_u}
\le12J(f).}
\tag{3.1}
\]

**Proof.** The first inequality is the exact block decomposition `Delta H=B+JS` with `JS>=0`; the second is Theorem C.1 at each selected node; the third uses the exact drift `D_Z=I_Z+C_Z>=I_Z`. Finally, weighted folded drifts telescope on any finite physical restriction tree:
\[
\sum_u w_uD_{Z_u}
=J(f)-\mathbb E_{\ell}J(f_\ell)\le J(f).
\]
QED.

Thus the **total Shannon erasure actually left unpaid along the entire certifiable phase is at most `12 J(root)`**, not `12J` separately for each row. Physical blocks may overlap across different branches; the drift telescope prevents reuse automatically.

Moreover entropy itself telescopes:
\[
H(f)-\mathbb E_\ell H(f_\ell)
=\sum_u w_u\Delta_{Z_u}H
\le12J(f).
\tag{3.2}
\]

This gives a genuine realizable stopping/peeling policy, not a distribution over hypothetical blocks.

## 4. Additional nonreuse: selected target rarity and posterior crossings are globally bounded

The same hypotheses yield a useful two-sided comparison with target marginal entropy.

From the proof of Theorem C.1,
\[
I_Z\ge q\left(r-\frac1{16}\right).
\tag{4.1}
\]
For `r=1`, centeredness gives `h_2(p)<=1` while (4.1) gives `I_Z>=15/32`, hence
\[
h_2(p)\le\frac{32}{15}I_Z.
\]
For `r>=2`, use `h_2(p)<=p\log_2(e/p)`, `p<=q(1+1/(16r))`, `log_2 e<3/2`, and `1+1/(16r)<=33/32` to obtain the crude bound `h_2(p)<=2rq`. Combining with (4.1) gives a ratio at most `2r/(r-1/16)<=64/31<32/15`. Therefore universally
\[
\boxed{h_2(p)\le\frac{32}{15}I_Z.}
\tag{4.2}
\]
Summing over the adaptive tree and using (3.1),
\[
\boxed{
\sum_u w_u h_2(p_{x_u})
\le\frac{32}{15}J(f).}
\tag{4.3}
\]
So even the selected pivots' logarithmic rarity costs are globally nonreused.

Also each selected target crossing is part of `C_{Z_u}`, hence
\[
\sum_u w_u c_{x_u}(Z_u)
\le\sum_u w_uD_{Z_u}
\le J(f).
\tag{4.4}
\]
Together with `c_x(Z)>=14p/15`,
\[
\boxed{\sum_u w_u p_{x_u}\le\frac{15}{14}J(f).}
\tag{4.5}
\]

Finally the account01/B18 curvature refund itself does not reuse: summing its survivor term along the same tree gives
\[
\sum_u w_u\mathfrak j'(p_{x_u})c_{x_u}(Z_u)
\le\mathcal P(f)
\le\frac2{\ln2}J(f),
\tag{4.6}
\]
because each such term is contained in the nonnegative decrement of the character-invariant phase potential.

## 5. Exact residual class after the paid phase

At every terminal nonconstant leaf of the policy, after median centering,

> for **every maximum-influence pivot** `x`, every codimension-`r>=1` coordinate subcube `Q` in its sensitivity domain satisfies
> \[
> \boxed{\mu(E_x\triangle Q)>\frac{2^{-r}}{16r}.}
> \tag{5.1}
> \]

Thus interface A can now remove *all* rows satisfying the sharp currently certified `q/r` near-subcube condition at total Shannon cost `<=12J`, while retaining the exact residual obstruction instead of paying each row separately.

This is the clean handoff to the quantitative derivative-stability/mixed-curvature interface: the remaining leaves have maximum pivotality rows uniformly separated from every coordinate subcube at the only tolerance presently known to support the dimension-free physical block theorem. Proving that this residual separation forces an influence-relative mixed-curvature/activation payment would close the next arrow. A fixed-relative `q/16` shortcut is known false and is not being revived.

## 6. Decisive finite sanity calculation

A fresh local truth-table checker (diagnostic only; the proof above is analytic) did two tests.

- Exhaustive Boolean functions in dimensions `1,2,3`: **276** roots, **232** roots with a certifiable first block. Across the recursively generated peeling trees, the maximum recorded values of
  `sum B - 12J`, `sum DeltaH - 12J`, `sum I_Z - J`, `sum D_Z - J`, and `sum h_2(p_x) - (32/15)J` were all exactly `0.0` in double arithmetic; both the entropy and folded-drift telescope discrepancies were `0.0`.
- **2,000** deterministic pseudorandom four-variable Boolean functions: **245** roots had a certifiable first block. The same five budget violations and both telescope discrepancies were all `0.0`.

A separate exhaustive local-step pass through dimensions at most three checked **232** selected certificate steps; the maximum violations of the new crossing fraction, `I_Z<=h_2(p)`, Theorem C.1's `Delta H<=12I_Z`, and `I_Z<=D_Z` were all nonpositive.

These finite calculations are only regression evidence and are not used to promote the all-dimensional theorem.

## 7. What changed and the remaining universal implication

**New this run:** the near-subcube block theorem is no longer merely a one-row structured case. It now plugs exactly into the newest folded-cooling compiler with universal `(gamma,K)=(14/15,12)`, and all such rows can be **recursively removed by a realizable physical policy** while spending at most `12J` total Shannon erasure and at most `(32/15)J` total selected-pivot marginal entropy.

**Preserved obstruction:** the addressing family still rules out prescribed-coordinate payment and superlinear edge majorants. The policy is existential/state-adaptive and pays only blocks that satisfy the proved Boolean near-subcube hypothesis.

**Remaining arrow:** control the terminal class (5.1). The most direct next target is an influence-relative stability theorem saying that a maximum pivotality row which is `q/(16r)`-far from every coordinate subcube must contribute a fixed amount to a globally telescoping mixed-curvature, folded-activation, or other already-paid bank. The current B-interface gives exact zero-defect classification but not yet this quantitative positive-defect implication.

**Full FEI remains OPEN / NOT PROVED.** No novelty or publication-priority claim is made.
