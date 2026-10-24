# account04/B12 handoff — multirank resonance separation

Run: `20260923T071518Z-account04-B12-multirank-resonance-r3`  
Status: proved supporting theorem; full QFORM conjecture open; not independently reviewed.

Canonical mathematics:
- repository commit: `yspennstate/math-open-problems@d460b6cc1d557090dce30e824744c2dd3d335fb1`
- report: `proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/20260923T071518Z-account04-B12-multirank-resonance-r3/REPORT.md`
- report blob: `cdddab6ff5544b65a7d17a6aa19f34ac595bad5f`

New theorem: for a scalar rank-`r` hub `B+tau U U^T`, the local resonance set is the spectrum of `-F^(-1/2) C F^(-1/2)`, of size at most `r`. If two original-coordinate physical cores have resonance sets separated by `Delta>0`, then for every real `tau` one actual core has gap

`gamma_*=ell_*^2 min{mu_*,f_* Delta/2}`.

After an arbitrary globally unbounded modification whose two core compressions have norm at most `eta`, and any arbitrary-rank dense tail of operator norm at most `delta<gamma_*-eta`,

`||p_Q||_infinity <= 6 sqrt(pi)/(gamma_*-eta-delta)`

for physical triples, or `2 sqrt(6 pi m)/(gamma_*-eta-delta)` for bounded cores of size at most `m`.

Concrete target-class application: `A_0=diag(1,1,3,1,1,3,3)`, with two orthonormal eigenvectors split in proportions `1/4` and `3/4` between two triples. Replacing both eigenvalues `1` by `1+tau` for arbitrary signed `tau`, then adding any dense `T` with `||T||_op<=1/12`, gives

`||p_(X^T(A_tau+T)X)||_infinity <= 24 sqrt(pi) < 42.539`.

The dense tail is used only through deterministic Weyl perturbation of an actual principal block.

Remaining implication: derive, from `s_3(A)>=1` alone, either separated multirank local resonance sets or another paid physical-core/cross-volume/mixed-hub/grouped-bank/Schur certificate. No universally good minor is asserted.

Sources:
- Claude physical-core theorem: `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`.
- completed partner account01/B12 r28: `math-open-problems@c63eec6fd03d23bb41493a502670d52bed383d35`.
- brain control: `math-research-brain@da6e4d750e712d00d07673214f4aaf73403131d1`, OWNER CONTROL `2026-09-22.15`.
- corrections blob: `c7000cf3822ae4935a2faf43b89ac92ea65ac0fe`.

Execution: `WITHOUT_VERIFIED_BRAIN`; repository transport is not native learned-memory ingestion.
