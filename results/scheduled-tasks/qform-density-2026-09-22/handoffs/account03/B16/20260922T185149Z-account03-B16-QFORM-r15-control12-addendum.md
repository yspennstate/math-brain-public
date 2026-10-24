SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B16, 2026-09-22T18:51:49Z.
attacking: revision-.12 localized-principal-triple validation and the claimed localized-versus-CLT exhaustion.

# account03/B16 final control-.12 addendum

A later owner control became visible after the initial r15 report/receipt: `OWNER CONTROL revision 2026-09-22.12`. The target remains QFORM. This addendum preserves the earlier report and applies the later instruction without rewriting immutable history.

Canonical addendum mathematics: `yspennstate/math-open-problems@8658479fb648f7c2b20908d61fcaef62aacb86d3`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260922T185149Z-account03-B16-QFORM-r15/FINAL_CONTROL_12_ADDENDUM.md`.

## Source-valid positive result

`QFORM-LOCALIZED-PRINCIPAL-TRIPLE-v1`: if an ORIGINAL-coordinate 3x3 principal block B has every eigenvalue of magnitude at least c>0, then after conditioning on all other ORIGINAL coordinates,

`||p_(X^TAX)||_infinity < 182/c`.

Proof avoids the refuted arbitrary-joint coarea lemma. After scaling to c=1: if some physical diagonal has magnitude >=1/4, the completed rank-three scalar-pivot theorem gives `<=128 sqrt2<182`; otherwise Frobenius norm forces an off-diagonal square >=15/32, making a physical 2x2 pair uniformly indefinite with `D>13/32` and `kappa>sqrt(15/32)-1/4`, and the completed exact-rank-three pair-log theorem gives `<27.60`. Arbitrary affine terms/outside couplings are allowed by those source theorems. Essential boundedness is proved; continuity is not.

## Structural correction to the new owner-message route

The implication `no uniformly good physical 3x3 block => pure diffuse/CLT spectral geometry` is not valid. The known target family

`A_m=[1] direct_sum J_m/m direct_sum (-J_m/m)`

has spectrum `{1,1,-1}` and every nonsingular physical principal 3x3 block has least singular value `1/m`, yet its high-spectral projection has `P_11=1`; one large eigenvector is exactly `e_1`. So near-singular physical triples can coexist with a maximally localized spectral direction. This is a hybrid bank geometry, not a pure three-direction CLT regime. The family itself is already bank-controlled, so this is not a QFORM counterexample.

Immutable correction event: `QFORM-NO-GOOD-TRIPLE-DOES-NOT-IMPLY-PURE-CLT-v1` at brain commit `1a0bbd1c03f98cc935b6c9f6125ae9b7fb856d36`. It is compatible with the earlier account02/B03 event `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`.

## Correct remaining decomposition

1. Localized principal triple: paid by `<182/c` above.
2. Truly diffuse spectral window: existing ridge-window theorem pays with continuous density `<64` under max high-window leverage `<=1/32`.
3. Hybrid heavy/grouped cases: still require an exhaustive bank/pair/group reduction stable under arbitrary extra spectrum.

Thus revision-.12's delocalized/local-limit route is useful for the genuinely diffuse branch, but is not yet an exhaustive reduction of the full target. Full QFORM remains OPEN. Execution remains `WITHOUT_VERIFIED_BRAIN`.
