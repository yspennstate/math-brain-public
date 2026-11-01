SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B13, 2026-09-22T22:57:28Z.
attacking: the near-null two-bank residual by a combined-Gram paving cut, preserving original-coordinate independence and aggregating both banks before any reciprocal minor selection.

# fleet02/B13 r19 — combined-bank paving closes the diffuse misaligned/tiny-leakage collar

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Extremal product laws  
**Run:** `20260922T225728Z-fleet02-B13-extremal-r19`  
**Status:** SUPPORTING TARGET-LEVEL THEOREM / FULL QFORM OPEN  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Source-pinned inherited state and first unpaid implication

The exact target is unchanged: independent original-coordinate laws with densities at most one, and a real symmetric matrix with at least three eigenvalues of modulus at least one. No moments, bounded support, post-rotation independence, connected-support, interval-extremality, or bounded-fragment assumption is used.

The already-proved fleet02/B13 bang-bang reduction remains the front end: for each fixed slab functional the supremum over cap-one product densities equals the supremum over arbitrary measure-one product indicators, with no loss. The latest designated-partner result fleet03/B13 r18, canonical mathematics `yspennstate/math-open-problems@dbd31282f36494993f2fe8c838116dd8c63538eb`, further makes the full slab supremum countable by rational finite-grid extreme witnesses, but does not provide a uniform slab constant.

The structural input actually used below is designated partner fleet03/B13 r17, canonical mathematics `yspennstate/math-open-problems@eac866b378f5c54411a55f7eb49f89336a4701ae`. In its exact-rank-three near-null residual,

`A=R Lambda R^T`, `R^T R=I_3`, `min |lambda(Lambda)|>=1`,

there is a heavy original row `r_i=sqrt(c)u`, `c>3/10`, and two disjoint light original-coordinate banks `L_1,L_2`. In the splitting `R^3=span(u) direct_sum u^perp`, write each bank Gram as

`S_a = [[tau_a,h_a^T],[h_a,G_a]]`,  `G_a >= kappa I_2`,  `kappa=7/800`,

and define

`w_a=G_a^{-1}h_a`,
`rho_a=tau_a-h_a^T G_a^{-1}h_a >=0`.

Partner r17 already proves a fixed heavy-to-bank cross-row energy in each bank and hence `O(sqrt(|I|))` small-ball concentration. Its unpaid step is to turn the two-bank same-coordinate curvature into a linear slab law without a forbidden worst conditional projection cap.

The first implication attacked here is therefore:

`QFORM-NEARNULL-TWOBANK-SLOPE-OFFSET-PAYMENT-v1`.

Rather than another scalar slope split, this run aggregates both bank Grams first and cuts the *physical coordinates* only after a dimension-three paving argument.

## 2. Exact combined-Schur identity

Let

`S=S_1+S_2`, `G=G_1+G_2`, `h=h_1+h_2`, `tau=tau_1+tau_2`.

Since `h_a=G_aw_a` and `tau_a=w_a^T G_a w_a+rho_a`, the Schur complement of `G` in `S` is

`rho = tau-h^T G^{-1}h`.

### Lemma 2.1 — two-bank graph-variance identity

\[
\boxed{
\rho=\rho_1+\rho_2+(w_1-w_2)^T(G_1^{-1}+G_2^{-1})^{-1}(w_1-w_2).
}
\]

This is the standard parallel-sum identity, and follows by expanding the minimum

\[
\rho-\rho_1-\rho_2
=\min_w\{(w_1-w)^TG_1(w_1-w)+(w_2-w)^TG_2(w_2-w)\}.
\]

Because `G_a>=kappa I_2`,

`(G_1^{-1}+G_2^{-1})^{-1} >= (kappa/2)I_2`.

Also `G>=2kappa I_2`, so `det G>=4kappa^2`. Therefore, with

\[
V:=\rho_1+\rho_2+\frac\kappa2\|w_1-w_2\|^2,
\]

we obtain the source-valid full-volume lower bound

\[
\boxed{\det S=(\det G)\rho\ge 4\kappa^2 V.}\tag{2.1}
\]

This is useful precisely at the small-individual-leakage endpoint: two nearly planar banks generate a third aggregate direction whenever their graph slopes disagree.

## 3. Elementary physical-coordinate paving lemma

The next step avoids selecting any small principal minor.

### Lemma 3.1 — rank-d Rademacher paving

Let vectors `q_j in R^d` satisfy

`sum_j q_j q_j^T=I_d`,  `max_j ||q_j||^2<=delta`.

Then there is a partition `J=J_+ disjoint_union J_-` such that, for both signs,

\[
\sum_{j\in J_\pm}q_jq_j^T\ge
\theta I_d,
\qquad
\theta=\frac{1-\sqrt{d\delta}}2.
\tag{3.1}
\]

**Proof.** Give the rows independent Rademacher signs `eps_j` and set

`D=sum eps_j q_jq_j^T`.

Then

\[
E\|D\|_F^2
=\sum_j\|q_jq_j^T\|_F^2
=\sum_j\|q_j\|^4
\le\delta\sum_j\|q_j\|^2
=d\delta.
\]

Hence some sign choice satisfies `||D||_op<=||D||_F<=sqrt(d delta)`. Since the two partial Grams are `(I_d +/-D)/2`, (3.1) follows. QED.

No Kadison-Singer/MSS input is needed; the displayed second-moment proof is complete.

## 4. New theorem: diffuse combined-bank volume is already paid

For `j in L_1 union L_2`, define its leverage relative to the *combined* bank Gram

\[
\ell_j=r_j^TS^{-1}r_j.
\]

### Theorem 4.1 — `QFORM-TWOBANK-COMBINED-GRAM-PAVING-v1`

Assume the exact-rank-three partner state above and

\[
\boxed{\max_{j\in L_1\cup L_2}\ell_j\le\frac1{12}.}\tag{4.1}
\]

If `V>0`, then the full quadratic form, including arbitrary self-blocks, all outside coordinates, and all outside couplings, has a continuous density satisfying

\[
\boxed{
\|p_Q\|_\infty
\le
4C_1\,[4\kappa^2V]^{-1/3},
}\tag{4.2}
\]

where

\[
C_1=\frac{e\sqrt\pi}{2\sqrt2}\frac{\Gamma(1/4)}{\Gamma(3/4)}
=5.039897503914386\ldots .
\]

In particular, if

\[
V\ge \kappa/32=7/25600,
\]

then

\[
\boxed{\|p_Q\|_\infty<4607.907.}\tag{4.3}
\]

### Proof

Normalize the actual physical rows in the combined bank:

`q_j=S^{-1/2}r_j`.

Then `sum q_jq_j^T=I_3` and (4.1) says `||q_j||^2<=1/12`. Lemma 3.1 with `d=3`, `delta=1/12` gives a partition

`L_1 union L_2=J disjoint_union K`

whose spectral row Grams

`S_J=R_J^TR_J`, `S_K=R_K^TR_K`

satisfy

\[
S_J,S_K\ge\frac14S.\tag{4.4}
\]

Thus both have rank three. For the physical cross block

`B=A[J,K]=R_J Lambda R_K^T`,

the product of its three positive singular values is exactly

\[
\Pi_3(B)=|\det\Lambda|\sqrt{\det S_J\det S_K}.
\]

Using `|det Lambda|>=1`, (4.4), and (2.1),

\[
\Pi_3(B)
\ge \frac1{64}\det S
\ge\frac1{64}(4\kappa^2V).
\tag{4.5}
\]

Hence its geometric mean obeys

\[
g:=\Pi_3(B)^{1/3}\ge\frac14[4\kappa^2V]^{1/3}.\tag{4.6}
\]

It remains to check the leverage hypothesis of the completed three-cross theorem. For a row `r_j` on side `J`, (4.4) yields

\[
r_j^TS_J^{-1}r_j\le4r_j^TS^{-1}r_j\le1/3.\tag{4.7}
\]

Because `R_K` has full column rank and `Lambda` is invertible, `range(B)=range(R_J)`, so (4.7) is exactly the coordinate leverage of the cross range on that cut side.

Now apply completed fleet03/B10 theorem `QFORM-THREE-CROSS-GEOMEAN-v1`, canonical mathematics `yspennstate/math-open-problems@ed915899a1cc9f7582b8462998fe024d6045805c`. Its `q=1` hypothesis only asks for leverage at most `1/2`, and therefore applies. It gives

`||p_Q||_inf <= C_1/g`.

Substituting (4.6) proves (4.2). At `V=kappa/32`, `(4kappa^2V)^(1/3)=kappa/2`, so `g>=kappa/8=7/6400` and (4.3) is `C_1*6400/7=4607.906289293152...`. QED.

This is an original-coordinate cut. No source rotation occurs, and no conditional projection is declared independent.

## 5. Consequence for the designated partner's hard residual

Within fleet03/B13 r17, `rho_1,rho_2<1/100` is all that was known before the present cut. Theorem 4.1 gives a much sharper alternative.

If the combined-bank leverage is diffuse as in (4.1), then every state with either

\[
\rho_1+\rho_2\ge\kappa/32
\]

or

\[
\|w_1-w_2\|\ge1/4
\]

is already paid by the explicit bound (4.3), because in the latter case

`(kappa/2)||w_1-w_2||^2 >= kappa/32`.

Therefore an unpaid diffuse state must satisfy simultaneously

\[
\boxed{
\rho_1+\rho_2<7/25600,
\qquad
\|w_1-w_2\|<1/4.
}\tag{5.1}
\]

Thus the partner's old `rho_a<0.01` collar collapses, on the diffuse branch, to a genuinely tiny total graph leakage plus a common-graph alignment collar.

This is target-level movement: it closes a full quantitative open region of the actual exact-rank-three residual, with a dimension-free constant, rather than only profiling it.

## 6. What happens if combined-bank leverage is not diffuse

The complementary branch is now explicit:

\[
\exists j\in L_1\cup L_2:\quad r_j^TS^{-1}r_j>1/12.\tag{6.1}
\]

This is a *physical* high-leverage witness for the combined two-bank span, not a rotated coordinate. It is the only obstruction to the paving cut when `V` is bounded below.

For comparison, if one has the stronger bankwise transverse leverage witness

`p_j^TG_a^{-1}p_j>1/8`,

then `||p_j||^2>kappa/8`, and against the other bank `b` the exact determinant-bank identity gives

\[
\sum_{k\in L_b}|\det A_{\{i,j,k\},\{i,j,k\}}|
=|\det\Lambda|c\sum_k\det(p_j,p_k)^2
=|\det\Lambda|c\,p_j^T\operatorname{adj}(G_b)p_j
>\frac{3\kappa^2}{80}
=2.87109375\cdot10^{-6}.
\tag{6.2}
\]

So even this localized alternative retains an aggregate third-coordinate determinant bank; it need not contain one constant-size atom. Any continuation must aggregate (6.1)/(6.2) before a reciprocal local determinant is taken.

## 7. Partner use and extremal-product interpretation

The designated partner fleet03/B13 r17 is used essentially: its two physical banks, the exact `G_a>=7/800 I_2` currency, and its near-null residual are the hypotheses of Theorem 4.1.

The latest designated-partner r18 countable-extreme theorem is also compatible and applied to the remaining search space: if the owner target is false, a counterexample can be approximated by rational finite-grid product indicators; Theorem 4.1 then says any such witness entering this partner residual must, after the already-paid exits, lie in either the common-graph/tiny-leakage collar (5.1) or the physical high-combined-leverage branch (6.1). No interval or bounded-fragment extremality is inferred.

The fleet02/B13 zero-loss fixed-slab bang-bang theorem transfers (4.2) unchanged between arbitrary cap-one product densities and the product-indicator formulation.

## 8. First unpaid implication after this run

The first remaining B13 implication is now

`QFORM-NEARNULL-COMMON-GRAPH-OR-HIGHCOMBINEDLEVERAGE-v1`:

> In the exact-rank-three partner residual, pay either (A) the collar `rho_1+rho_2<7/25600`, `||w_1-w_2||<1/4` by an intrinsic near-null square-plus-hyperbolic/bank argument stable under arbitrary fragmented supports, or (B) the physical combined-bank leverage witness `r_j^TS^{-1}r_j>1/12` by routing its remaining aggregate determinant/cross-row bank before any reciprocal atom selection.

The full arbitrary-dimension owner conjecture remains OPEN. This report does not claim universal continuity outside the paid cross-cut branch.

## 9. Corrections respected

The proof does not use the refuted arbitrary-joint coarea lemma, positive conditional-projection moments, post-rotation independence, pointwise law-uniform scalar van der Corput, one-good-minor selection, bounded support/diameter, fixed fragment count, or centered-interval extremality. The only change of basis is in the three-dimensional spectral bookkeeping used to write a Gram; all probability cuts remain in original physical coordinate banks.
