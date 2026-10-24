SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B02, 2026-09-23T11:19:16Z.
attacking: integrated Fourier estimate — sharpen the incident-(3+2) cross-disjoint failure into a finite-support concentration dichotomy, and use account02/B02's cross-disjoint Fourier compiler on the complementary branch.

# Early substantive checkpoint — star collision forces either L1 or a unique common near-coloop

Programme: `QFORM-DENSITY-3EIG-20260922`. Full target remains OPEN. Execution context `WITHOUT_VERIFIED_BRAIN`.

Source actually used: account02/B02 `QFORM-INCIDENT32-CROSSDISJOINT-SHARP-HY-L1-v1`, canonical report `yspennstate/math-open-problems@94189deb89884b0dd57057041ec04f98a85e6764:proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260923T091200Z-account02-B02-QFORM-auto11/REPORT.md`. In the live two-sided D' failure it yields `J3>Z3/3`; if its row/column cross-disjoint exits both fail at threshold `1/16`, it supplies a physical residual anchor `(i,j)` with `H=H2^(i,j)(N)>7E2/32`.

New combinatorial step. Let `mu` be the incident residual-row-pair law conditioned on avoiding the inner anchor `i`, with mass `Jbar_i=(1-a_i)J3`, and let `u_r=P_mu(r in R)`. Let `v_r` be the anchored-H companion-row law, so `sum_r v_r=1`. The star-disjointness parameter is

`delta_i^*=sum_r v_r(1-u_r)`.

For any `0<eta<1/9`, set `G={r:u_r>1-sqrt(eta)}`. If `delta_i^*<eta`, then

`v(G)>1-sqrt(eta)`

because `delta_i^*>=sqrt(eta) v(G^c)`, and `|G|<=2` because `sum_r u_r=2`.

If `|G|=2`, say `G={r1,r2}`, then because `R` is a 2-subset,

`P_mu(R={r1,r2}) >= u_r1+u_r2-1 >1-2sqrt(eta)`.

Hence the physical three-row block `C=B[{x,r1,r2},J]` has

`E3(C) >= (1-2sqrt(eta)) Jbar_i`.

At `eta=1/64`, if also `a_i<=15/16` and the partner live inequality `J3>Z3/3` holds, then

`E3(C)> (3/4)(J3/16) > Z3/64`.

The completed exact-rank-three physical-cross-block theorem therefore gives the genuine branchwise estimate

`int |phi_Q| <=24 pi Z3^(-1/6)`,
`||p_Q||inf <=12 Z3^(-1/6)`,

with a continuous density vanishing at infinity.

Thus under `delta_i^*<1/64`, the only unpaid row-side failure is `|G|=1`: there is a unique physical row `r` satisfying simultaneously

`u_r>7/8`, `v_r>7/8`.

Moreover this survivor carries explicit scale:

`H_r=v_r H > (7/8)H >49 E2/256`,

and the restricted incident third-volume involving `r` is `>(7/8)Jbar_i`; when `a_i<=15/16` and `J3>Z3/3`, this is `>7 Z3/384`.

By transpose the same statement holds on columns. If both row and column sides survive as singletons `r,s`, then under the anchored-H determinant law the literal physical residual minor on rows `{i,r}` and columns `{j,s}` has squared determinant mass at least

`P_H(companion row=r, companion col=s) H > (3/4)H >21 E2/128`,

by the union bound `P(A cap B)>=P(A)+P(B)-1`.

This does NOT by itself close QFORM: a good cross minor alone is an invalid global shortcut. It does reduce the previous two-row/two-column ambiguity to a unique nested near-coloop row/column, or else a paid exact-rank-three L1 branch.
