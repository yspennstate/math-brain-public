SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B16, 2026-09-23T09:41:06Z.
attacking: projection-product interaction in the overlapping-source line/plane transition, retaining shared original-coordinate sources through a translated independent square.

**Status:** `ESSENTIAL_STEP_APPLIED`; full QFORM remains `OPEN / NOT PROVED`; continuity remains separate.

**Fresh control:** initial full read at `math-research-brain@cd09ee373535c7f8845d89fc4514deb171b9d74a`, publication refresh through `77ba2bd7eb3021fbc8868217baba567cba7d27b5`, and immediate pre-handoff refresh `bc947890e1f879521eeb2455da5e7aee1f91cb3a`. OWNER CONTROL remains revision `2026-09-22.15`; no later B16 stop. Execution label `WITHOUT_VERIFIED_BRAIN`.

## New theorem

`QFORM-RANK2-PRODUCT-HALFRIESZ-TRANSLATED-SQUARE-v1`.

For disjoint original source banks `I,J`, let `Y=M X_I in R^2` with `rank M=2`, `Z=n^T X_J`, `B` invertible symmetric `2x2`, `gamma!=0`, arbitrary affine `d^T X_I+c`, and **arbitrary measurable shared-source shift** `h(X_I)`. Put

`R=Y^T B Y+d^T X_I+c`,
`Q=R+gamma(Z+h(X_I))^2`.

Then

`||p_Q||_inf <= 128 sqrt(2)/(||n||_2 sqrt(|gamma|)) [det(MM^T)|det B|]^(-1/4)`.

If `d` is in the row span of `M` (including `d=0`),

`||p_Q||_inf <= 16 sqrt(60)/(||n||_2 sqrt(|gamma|)) [det(MM^T)|det B|]^(-1/4)`.

If `Z=nu X_j` is a singleton source, replace the scalar `sqrt(2)/||n||_2` factor by the exact `1/|nu|`, so the improved constant is `16 sqrt(30)`.

Proof: condition on the true independent `I` bank only after reserving `J`. A translated square with scalar density cap `K_Z` has conditional density `<=K_Z |gamma|^(-1/2)|y|^(-1/2)`. The shift `h(X_I)` disappears from the upper bound. The remaining expectation is exactly the completed rank-two affine half-Riesz potential, after normalizing `M` by `S=(MM^T)^(1/2)`. No arbitrary-joint coarea or conditional projection cap is used.

Pinned dependency: `math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a:proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md` (`QFORM-RANK2-AFFINE-HALF-RIESZ-v1`).

## Overlapping line/plane corollary

If `Y=M X_I`, `L=r^T X_I`, `Z=n^T X_J`, and

`Gamma=[[C,b],[b^T,gamma]]`, `gamma!=0`, `det Gamma!=0`,

then

`Q=(Y,L+Z)^T Gamma (Y,L+Z)`

satisfies

`||p_Q||_inf <=16 sqrt(60)/||n||_2 * [det(MM^T)|gamma||det Gamma|]^(-1/4)`.

This follows from the exact completion

`Q=Y^T(C-bb^T/gamma)Y + gamma[Z+L+gamma^(-1)b^TY]^2`.

Thus **same-bank line leakage may be arbitrarily dependent on the plane projection**; only one disjoint line innovation is required. This pays the earlier one-sided overlap transition everywhere away from the null/isotropic line pivot.

For exact rank three `A=R Lambda R^T`, choose any physical row `r_i`, `c_i=||r_i||^2`, `e=r_i/sqrt(c_i)`. The complementary plane projection of the other original coordinates is exactly Parseval, and the singleton line innovation is `sqrt(c_i)X_i`. Since `gamma=e^T Lambda e=A_ii/c_i`, for `A_ii!=0` the full exact-rank-three form obeys the sharpened source-aligned bound

`||p_Q||_inf <=16 sqrt(30)[c_i |A_ii| |det Lambda|]^(-1/4)`.

With arbitrary outside conditioning/affine terms, the general constant becomes `128`, recovering the already-pinned full-ambient rank-three Schur theorem. In a near-coloop chamber, the overlap itself is therefore paid for every quantitatively non-isotropic normalized pivot `|gamma|>=tau`; the unresolved transition is `gamma ->0`.

## Designated partner actually applied

Consumed account02/B16 r26 canonical report:
`math-open-problems@df9ef8e92ae2669eb101e2a1b076594af329dc52:proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/20260923T071608Z-account02-B16-QFORM-r26/REPORT.md`, blob `7d14490486804ffacf62d2e54ab2b82b8671f9e7`.

For its exact target family

`Q_a=2(sqrt(c)X_0+sqrt(a)T)U+V^2`, `0<a<1/64`,

our new theorem gives `||p_(Q_a)||_inf <=16 sqrt(60)=123.935467...` directly despite same-bank `(T,U)` overlap. More strongly, the partner's completed true-bank regrouping gives

`||p_(Q_a)||_inf <=6 sqrt(pi)*32/(sqrt(253)-1)=22.8305205519...<23`.

Applying that partner inequality to any independent additional block `W` on further disjoint original coordinates gives the actual higher-rank inequality

`||p_(Q_a+W)||_inf <=22.8305205519...`,

because convolution with an arbitrary probability law cannot raise an `L^inf` density norm.

## Corrections preserved

Consumed and preserved: arbitrary-joint rank-three coarea false; conditional projection positive-moment/normalized-cap routes false; no independence after rotation; fiberwise trace and generic slice-Wiener interfaces not used. Product aggregation occurs before the curved singularity is paid.

## Canonical output

Full immutable mathematics:
`yspennstate/math-open-problems@ab9eee0f982c189620b67212476538c53db2ea60`
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B16/20260923T094106Z-account01-B16-QFORM-projprod/REPORT.md`
blob `b3bcdd3b6870ff72a7f28fa0274835b5b245c80f`.

## First unpaid implication

`QFORM-NULL-OVERLAP-LINE-PLANE-TRANSDUCER-v1`: treat uniformly the exact/near-isotropic `gamma=e^T Lambda e ->0` branch while the residual line leakage and plane projection reuse the same original sources. At `gamma=0`, hub conditioning produces a reciprocal linear factor `1/|b^TY|`; a bare planar projection cap does not pay this, and the live arbitrary-joint/conditional-cap corrections forbid the naive replacements. Need an unnormalized same-bank curved transducer, bounded source-bank regrouping, or a forced exit to existing ridge/pair/cross-transverse/mixed-Fresnel branches.
