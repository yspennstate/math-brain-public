# account03/B08 r54 handoff — quadratic suppression of the exact-child ultra-puncture

Programme: `QFORM-DENSITY-3EIG-20260922`  
Control: OWNER CONTROL revision `2026-09-22.15`; fresh startup main `9a94dc10b612d7f5f5a4a4f5aace294106411298`; prepublication refresh `62e742716e9bda0af84c1bba71ddcb7f0b37c2fe`.  
Status: supporting deterministic theorem; **FULL QFORM OPEN**, full continuous-representative claim OPEN; `WITHOUT_VERIFIED_BRAIN`.

Canonical mathematics:

- repository: `yspennstate/math-open-problems`
- commit: `0c03ca1a8984a3262fffd11aae668fa2f6e5f941`
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260924T112047Z-account03-B08-qform-diffuse-r54/REPORT.md`
- checks: same commit/path root, `CHECKS.md`, status `QFORM_B08_R54_QUADRATIC_S4_CHECK_PASS`.

## New theorem

`QFORM-ULTRAPUNCTURE-QUADRATIC-S4-SUPPRESSION-v1`.

In the r53 exact-rank-two child state

`A=[[a,b^T],[b,V Lambda V^T]]`, `b=Vc+u`, `V^T u=0`, `beta=||u||`,

assume only `s3(A)>=L` and `Lambda` invertible. Let `A0` delete only the transverse star `u`. Then

`||A-A0||op=beta`,

`s3(A0)>=L-beta`,

and, crucially,

`boxed: s4(A)<=beta^2/s3(A)<=beta^2/L.`

Writing `K0=[[a,c^T],[c,Lambda]]` and `sigma=a-c^T Lambda^-1 c`, one also has

`|sigma| >= (L-beta)sqrt(1+||Lambda^-1 c||^2) >=L-beta`,

and in the four-frame `[hub,V,u/beta]`

`K_beta congruent K0 direct_sum (-beta^2/sigma)`,

with congruence-shear norm at most `beta/(L-beta)`. This congruence is algebra only; it is not used to rotate/shear the independent product law.

At the r53 live collar `beta<=beta0 L`, `beta0=5.394796609394436e-6`, this gives

`s4(A)<=2.910383045673371e-11 L`,

`s3(A0)>=0.9999946052033906 L`,

`|sigma|>=0.9999946052033906 L`,

and final scalar Schur puncture `<=2.910398746682662e-11 L`.

The `O(beta^2/L)` scale is sharp at matrix level; `diag(1,1,1,0)` with a `beta` hub-null off-diagonal has `s4=beta^2+O(beta^4)`.

## Designated partner application

Account04/B08 `QFORM-DISTRIBUTED-STAR-DERIVATIVE-SPLIT-v1`, canonical `yspennstate/math-open-problems@f324267086411b9725aa0733e108ab6efc2e760a`, was applied to the same literal parent. With inherited `||b||>rho_*L`, `rho_*=0.0006247538095703261`,

`sup_t P(|Q-t|<eps)<190.311 sqrt(eps/L)`.

In the ultra-collar `beta/||b||<0.008635076`; more than `99.99254%` of star squared norm is aligned with the child plane. This partner result remains square-root small-ball, not a density bound.

## Corrections consumed

All standing source corrections were retained. In particular the latest relevant live correction `QFORM-HUBSTAR-FIBERL2-MIXEDNORM-UNIVERSAL-FALSE-v1` forbids upgrading the partner estimate using a universal absolute `|t|^-1/2 ||G_t||_2` mixed norm. No nonzero random puncture is deleted just because its matrix coefficient is tiny.

## Remaining implication

`QFORM-RANK3-CORE-PLUS-QUADRATICALLY-TINY-SHARED-PUNCTURE-v1`:

prove a product-source-valid receiver uniform under the exact shared-source rank-one puncture attached to the target-scale aligned rank-three core, or convert the source overlap into a literal original-coordinate crossing/pair/volume certificate. The missing issue is source stability, not spectral curvature.
