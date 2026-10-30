# A039 independent reconstruction of B08 inputs

This is a source-bound analytic reconstruction by A039, not a replay of either author's code and not an external peer review. It does not modify their files. A039 supplied no repair to the reviewed versions.

## A037 v1

Sources: A037 REPORT.md and CLAIMS.json in runs/20261011T220010Z-fleet05-A037-conditional-credit-ledger. For CONDITIONAL-CREDIT-CONSERVATION, factor the joint likelihood ratio in two orders, first W then Y and first Y then W. Their expected logarithms give K+j=d+E Kchild. For a new reference r, adding log(q_pred/r) gives the stated signed correction. Conditional entropy conservation follows by chain rule at each side-information atom and telescoping node visit weights; leaf transcript includes the stopping event. Both statements hold at the stated finite/supported scope.

For PHYSICAL-SPECTRAL-COMMON-LIFT, independently form P(U,T,Y)=p(U,T) p_Y(T)/(2 q(T)) for singleton physical queries, and the same 2^-|B| expression for blocks. Summing U gives 2^-|B| times the actual child spectrum. Parseval gives fair branch probabilities. The kernel is independent of all erased root labels given current residual T and history; hence the chain-rule release from the full root label equals the local child-mixture J. Parent H minus expected child H equals erased conditional entropy B plus J. Telescope and subtract released root information to get the stated terminal root posterior identity. Zero q fibers have zero P mass and the explicit arbitrary extension is legitimate. This proof uses the signed restriction transform, not spectral conditioning.

Verdict: ACCEPT_AT_STATED_SCOPE for both A037 v1 claims. No universal influence estimate, witness-generator compatibility or reference-reset payment is thereby accepted. Our separate exhaustive checker implements the Bayes reference calculation on all 768 three-bit coordinate splits rather than rerunning A037's checker. In particular it verifies delta_bar=D_out+J-G with exact formal logarithm cancellation.

## A038 v1 normalization interface and obstruction

Sources: A038 REPORT.md, OCCUPANCY_TARGET_SOURCE.md and local out/sources/K_OCC_DEFINITION.md, all under runs/20261011T221733Z-fleet05-A038-occupancy-term-audit. On nonempty support, log Q_r is affine in the indicators, so matching marginals imply E_P+ log Q_r=E_Qr log Q_r. The log ratio log(M/product(d)) is likewise affine there and constant on empty; both P and M have the same empty mass and unconditional marginals. This proves K_full=v K_occ+Delta with Delta=D(M||product(d))>=0. Constants, forced coordinates and singleton supports require the explicit endpoint conventions; they do not invalidate the identity.

For an m-bit point defect, the nonempty conditional law is uniform and therefore its own maximum-entropy projection, hence K_occ=0. Independently, the exact formula H_m=-2(1-a)^2 log2(1-a)+2a(2-a)(m-1), a=2^(1-m), implies H_m<=4ma. Since h2(a)>=a(m-1), Delta=ma times at least m-5. This confirms the divergent normalization gap. A039 goes further by computing its signed restriction change; the earlier identity is not refuted. Verdict: ACCEPT_AT_STATED_SCOPE for the cross-law normalization identity and point-defect normalization-gap obstruction. No acceptance of the separate signed collision lower bound or remote source chain is claimed; those were not independently reconstructed here.

These reviews consume the pending B08 dependencies before A039 introduces its restriction extension. B20 must decide index adoption; no shared index edit or supervisor acceptance is inferred.
