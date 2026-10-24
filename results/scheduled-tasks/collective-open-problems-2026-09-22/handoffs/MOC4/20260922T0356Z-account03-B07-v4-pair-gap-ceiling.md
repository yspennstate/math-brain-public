# MOC4 handoff — account03/B07 `MOC4-V4-PAIR-GAP-CEILING-v1`

Outcome: **ESSENTIAL_STEP_APPLIED**. Parent MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**. Execution remains `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

Canonical scientific report: `yspennstate/math-open-problems`, `proofnet24/collective-MOC4/account03/B07/account03-B07-20260922T033411Z-d2a63b2a/REPORT.md`, commit `dcce2e52aee9c3fb338be4dd56acb02114ebfdde`, blob `28cbce0f0a6213c0760e0777a5baa5b0de12b31a`. Exact verifier creation commit `8dd7bd8bc867be60444522925bdd40fb7a890d1f`; captured Fraction-only output commit `fc91ef6763f567d737798bc84da1311a107958b1`.

## Named other-account result consumed

**account04/B08**, run `20260922T031434Z-account04-B08-MOC4-r11`, `MOC4-PAIR-SPECIFIC-ENDPOINT-ROOF-v1`, report blob `0c611698463f4f00abe78c96a10308759d3cb716`. For every true unitary and every column transposition `tau`, `(h(U)+h(U P_tau))/2` is bounded by the exact two-endpoint-pair roof. This result is used directly, not merely cited.

## New exact result

For endpoint supports `H_sigma`, let `M=max H_sigma`, `m=average H_sigma`, `d=M-m`. Let `V4` be the Klein kernel of `S4 -> S3`, let `Q` be the maximum average of the four endpoints in one `V4` fiber, and put `Delta=M-Q`. Let `g_tau=2M-max_sigma(H_sigma+H_{tau sigma})` for the six column transpositions and `G=sum_tau g_tau`.

A four-point true-unitary `V4` twirl kills the standard/orientation block while preserving the genuine complementary-pair transport. After a Birkhoff decomposition of that preserved transport, uniformly spreading each weight over its four even-sign fiber gives an exact common lift of the **twirled** data. Hence the twirl is at most `Q`.

Combining this with the account04/B08 six pair roofs and the exact transposition group identities gives, for **every genuine support violation** `h(U)=M+gamma`,

`0 < gamma <= (3 d - Delta - G/2)/4`.

Therefore the endpoint-only condition

`Delta + G/2 >= 3 d`

is a rigorous certificate that the whole support direction is safe for **all** `U in U(4)`. No stationarity or invertibility is needed.

## Decisive negative control and next obligation

The endpoint certificate is not automatic. Exact simple real spectra `a=(-1,2,1,0)`, `b=(-1,1,-2,2)`, real support give `M=36`, `m=29/6`, `Q=15`, `d=187/6`, `Delta=21`, pair gaps `36,9,36,32,4,24`, `G=141`, leaving the exact allowance `gamma<=1/2`. The committed verifier constructs a half-integer `S4` low-frequency/twirl-relaxation function attaining that `1/2` while respecting all pair roofs and all `V4` roofs. It is explicitly **not** a unitary determinant orbit and not a MOC4 counterexample.

Thus more averaging of these same roofs cannot close the residual. The next implication is `MOC4-RESIDUAL-PR-RESERVE-v1`: on positive reserve `R=3d-Delta-G/2`, use the genuine same-unitary compatibility now available from account03/B09 (`D=(1/4)E^TPE`, `R>=|D|`, unistochastic `P`, odd-Weyl gates) together with the existing stationarity/Cartan constraints to rule out `0<gamma<=R/4`, or produce a genuine common-unitary/spectrum witness.

Recommended immediate consumers: account04/B08 assigned partner; account03/B09 P-R compatibility lane; account01/B07 Hessian/stationarity lane; account03/B20 integrator. No cross-account native action was taken by this run.
