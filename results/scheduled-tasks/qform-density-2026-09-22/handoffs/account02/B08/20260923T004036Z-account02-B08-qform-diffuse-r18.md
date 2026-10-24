SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B08, 2026-09-23T00:40:36.798579Z.
attacking: the newest localized/diffuse split with an explicit ACTUAL principal-spectrum gate, and the one-/two-direction hybrid left after the cross-volume payment.

# account02/B08 r18 source-pinned handoff

Control refreshed through `yspennstate/math-research-brain@4faad47c73251c03932c297213feec85f779e874`; OWNER CONTROL remains revision `2026-09-22.15`, QFORM sole target. Full target remains **OPEN**. Execution: `WITHOUT_VERIFIED_BRAIN`.

Canonical mathematics: `yspennstate/math-open-problems@9fb59f9549a85af6173ade505fd53bc035c611ba`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/20260923T004036Z-account02-B08-qform-diffuse-r18/REPORT.md`. Checker/output are in the same run root; executed output ends `QFORM_B08_ACTUAL_SPECTRAL_GATE_CHECK_PASS`.

## Result 1: `QFORM-DIFFUSE-ACTUAL-SPECTRAL-GATE-v1`

Apply designated partner account03/B08 r24, source `math-open-problems@1bf6f41d81ffddcc6e8ff93b4df165d0ce5bbd05:.../account03/B08/20260922T231729Z-account03-B08-qform-diffuse-r24/REPORT.md`.

For three genuine full-matrix eigenvectors with `min |lambda_j|>=L` and selected-frame leverage `mu<=1/48`, take the partner balanced physical cut. Set

`c_L=(L/2)sqrt(3/5)`, `beta_L=(3/16)sqrt(3/5)L`.

If `k_K` is the number (capped at three) of ACTUAL eigenvalues of physical child `A[K,K]` with modulus at least `c_L`, then for each side `K`,

`k_K<3 => s_{3-k_K}(A[I,J])>beta_L`.

Thus the mixed states are exactly quantified: zero retained child directions force three large cross singular directions, one retained direction forces two, and two retained directions force one.

## Result 2: newest Claude D' pays the zero-child spread-cross branch

Use `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`, Theorem D'.

If `k=min(k_I,k_J)=0`, then `Z_3=e_3(B^TB)>=beta_L^6`. If either orientation has maximum three-volume row marginal at most `5/8`, D' gives the actual full-form inequality

`||p_Q||_infinity <= 128 sqrt(e/3)/L =121.841877690545.../L`.

If D' fails in both orientations, there are a physical row `i` and column `j` for which more than one quarter of all squared three-volume is simultaneously incident:

`sum_{S contains i,T contains j} det(B_ST)^2 > Z_3/4 >= beta_L^6/4`.

There are at most four such `>5/8` heavy rows and at most four such heavy columns.

## Result 3: explicit ACTUAL no-pivot gate

In the matrix part of N3 at `tau_0=1/8192`, every off-diagonal entry has magnitude at most `eps_0=sqrt(tau_0+tau_0^2)=0.011049217785...`. Therefore every `m`-coordinate principal block satisfies

`||A[K,K]||op <= tau_0+(m-1)eps_0`.

Since `tau_0+35 eps_0=0.3868446928... < c_1=(1/2)sqrt(3/5)`, no physical block on at most 36 coordinates can pass even the first `c_L` actual spectral gate. Any retained child curvature at this scale is supported on at least 37 original coordinates.

In the zero-child/D'-failure branch, the no-pivot entry cap plus Hadamard's determinant inequality forces at least **47,759 nonzero incident 3x3 cross minors** through one heavy row and one heavy column. This rules out a renewed single-good-minor closure at this scale.

## Result 4: sharp target-valid no-pivot hybrid family

For normalized Hadamard `U` (`m x 3`) and `P=diag(p_j)`, set

`A=[[UPU^T,U(I-P)U^T],[U(I-P)U^T,UPU^T]]`,

where exactly `k in {1,2}` entries of `P` equal `1-delta` and the rest equal `1/5`, `0<delta<=1/10`.

The plus spectrum is exactly `1,1,1`; the minus spectrum is `1-2delta` in the first `k` directions and `-3/5` in the others; all remaining eigenvalues are zero. Hence **exactly three** eigenvalues have modulus at least one. Selected plus-frame leverage is `3/(2m)->0`. The physical children have exactly `k` `c_1`-large eigenvalues while the cross block has exactly `3-k` `beta_1`-large singular values; its other `k` singular values equal `delta` and can tend to zero. Thus the one-/two-direction hybrid cannot be eliminated by stronger delocalization or by assuming exactly three large eigenvalues.

Every matrix entry is at most `3/m` and every physical 2x2 principal determinant at most `18/m^2`, so for any fixed `tau` the family enters N3 for large `m`; at `tau_0`, `m=32768` works.

This is not a target counterexample: the same exact family is paid by newest Claude Theorem F because its whole six-dimensional nonzero spectral range is diffuse. For all cap-one product laws,

`||p_Q||infinity <= 6[(4/5)^k(3/5)^(3-k)]^(-1/6)`,

which is `7.38334...` for `k=1` and `7.03768...` for `k=2`.

## First unpaid implication

`QFORM-DIFFUSE-HYBRID-ONE-TWO-DIRECTION-PAYMENT-v1` remains open: in an arbitrary full matrix, combine one/two ACTUAL child eigen-directions with the complementary two/one ACTUAL cross singular directions while preserving original-coordinate product structure and arbitrary spectral remainder. The Hadamard witness proves one may not assume the remaining cross singular values are uniformly nonzero. The promising missing compiler is a remainder-stable version of the whole-range Fresnel payment, not another local-minor extraction.

No scheduler/task mutation, email/notification action, paid call, public release, permission change, remote workflow, FEI/installation/benchmark work, or cross-account authentication occurred.
