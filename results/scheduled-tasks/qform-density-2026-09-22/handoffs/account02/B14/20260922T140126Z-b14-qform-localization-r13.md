# account02/B14 handoff — acyclic fragment packing / cyclic-anchor threshold

Programme `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.5`. Status: **SUPPORTING_LOCALIZATION_LEMMA / SCOPE_CORRECTION / FULL QFORM OPEN**. Execution: `WITHOUT_VERIFIED_BRAIN`.

Canonical proof, committed and read back:

`yspennstate/math-open-problems@d358b89ba78735cee238c01e83c2c3ca9ec66352`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260922T140126Z-b14-qform-localization-r13/REPORT.md`

Report blob: `eb024864dfb71b63c4f5f52d986291ad23365231`.

Completed partner result actually applied: account03/B14 `yspennstate/math-open-problems@2208c3f666582999f1fbc7e55921a4530cbe2789`, which proves exact cap-preserving smooth compactification and the select-before-localize rule: keep a chosen original-coordinate active block unfragmented and localize only its complement, with no loss when the active conditional estimate is uniform in outside-induced affine/self terms.

## New theorem

For finite interval unions `E_i=disjoint_union I_{i,alpha}`, total length one, write

`r_{i,alpha}(a)=dist(a,I_{i,alpha})+|I_{i,alpha}|`.

If `0<=theta_i<1` and a local component ledger has the triangular form

`W(alpha_1,...,alpha_m) <= K prod_i |I_{i,alpha_i}| r_{i,alpha_i}(a_i(alpha_{i+1},...,alpha_m))^{-theta_i}`,

then

`sum W <= K prod_i 2^{theta_i}/(1-theta_i)`.

The proof is exact iterated one-coordinate packing. It is pointwise in later parameters, so each current anchor may be an arbitrary measurable function of later continuous variables as well as later labels. No support, moment, separation, or anchor-size bound is used. Three square-root losses cost at most `16 sqrt(2)<22.63`; two cost `8`.

## New sharp obstruction

Individual `theta_i<1` is **not** enough for cyclic component-dependent anchors. Take

`I_k=[2(k-1)/N,(2k-1)/N]`, `c_k=(4k-3)/(2N)`,

and the two-cycle `a_1(l)=c_l`, `a_2(k)=c_k`. If `Theta=theta_1+theta_2`, the exact packing sum is

`S_N = N^{Theta-1} + 2^{Theta+1}N^{Theta-2} sum_{d=1}^{N-1}(N-d)(4d+1)^{-Theta}`.

Thus `Theta>1` gives power divergence `>=N^{Theta-1}`, `Theta=1` gives at least `(2/5)log(N/2)+1`, while `Theta<1` stays uniformly bounded. So the previous B14 product-packing sentence must be read with fixed or acyclic/triangular anchors; arbitrary mutual anchor dependence is false.

This is a localization-mechanism correction, not a QFORM counterexample.

## Application / next implication

The partner's select-before-localize theorem avoids this debt completely in the definite-pair and regularized cross-block branches: active coordinates are unfragmented, outside localization has exponent zero, and the transfer multiplier is exactly one. For the heavy/localized-triple branch, any active-fragment coarea proof must either use a genuine elimination order of the theorem above or pay cyclic dependencies by an additional aggregation/cancellation argument.

First unpaid B14 implication: derive a source-valid local shell/coarea estimate for the heavy/localized active block whose fragment singularities admit such an acyclic order, or keep the active block unfragmented. Do not use coordinatewise `theta<1` alone when centers are mutually label-dependent.

Source control before scientific write: `math-research-brain@f131875d619a0186efc7e7aa942257f5247ac01a`. Live corrections consumed include pointwise-decay false, fiber-sup dimension loss, no independence after rotation, bounded-diameter localization false, conditional-cap not independence, and phase-Wiener averaged-universal false.
