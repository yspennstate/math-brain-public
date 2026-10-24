# MOC4 handoff — account01/B08 r12

Outcome: `CANDIDATE_REFUTED`; parent MOC4 remains OPEN.

Consumed assigned OTHER-account result: account02/B09 run `20260922T064517Z-account02-B09-MOC4-r17`, especially `MOC4-TRANSPOSE-TIE-SAFE-v1`, `MOC4-SPIN4-SATURATION-EXCLUSION-v1`, and the zero-face strict-pair residual. Latest lead snapshot consumed: account03/B07 run `20260922T060726Z-account03-B07-MOC4-r11`.

## New exact theorem

`MOC4-ZERO-FACE-COMMON-LIFT-FACET-NOGO-v1`:
there is a true rational orthogonal `4 x 4` unitary with exactly `u_00=0` and all 36 two-minors nonzero for which no positive probability law on `S_4` can simultaneously reproduce its degree-one and degree-two compound marginals, hence no all-compound common law exists.

Exact witness:

```text
[ 0,        16/25,    -48/65,      69/325 ]
[ 16/25,   -72/125,   -33/65,     -48/1625]
[-69/325,   48/1625,  -16/65,   -1536/1625]
[ 48/65,    33/65,     24/65,      -16/65 ]
```

With `P_ij=|u_ij|^2`, `Q_{I,J}=|det U[I,J]|^2`, every common law on the zero face obeys the facet

`-P_01 + P_12 - P_20 - P_21 + Q_{01,01}+Q_{02,01}+Q_{02,02} <= 0`,

because `P_00=0` removes the six permutations fixing column 0 to row 0, and on the remaining 18 permutation vertices the left side is exactly 0 on 12 and -1 on 6. The true unitary above gives

`5810112/446265625 > 0`.

Exact affine ranks are 12 for the allowed joint `(P,Q)` polytope and 11 for the tight face, so this is a genuine facet. Standard-library rational verification is in the scientific run.

## Representation route that survives

Full `Q` reproduction is stronger than needed. If `lambda` is only a Birkhoff decomposition of `P`, then determinant expansion degrees `k=0,1,3,4` already match (the `k=3` step uses unitary complementary-minor duality). Only the spectrally weighted `k=2` term remains.

For `c_{I,J}=Re(conj(eta) a_{I^c}b_J)`, define the `P`-fiber roof

`R_c(P)=max_{lambda>=0, sum lambda P^sigma=P} sum_sigma lambda_sigma <c,Q^sigma>`.

The first representation-specific unpaid implication is now `MOC4-ZERO-FACE-SPECTRAL-ROOF-v1`:
for a true zero-entry global support maximizer in the strict-pair branch forced by account02/B09 r17, prove

`<c,Q(U)> <= R_c(P(U))`

for the actual spectral-product coefficients `c`. This suffices for the zero-face support bound but is not contradicted by the new arbitrary joint-polytope facet.

Scientific report: `proofnet24/collective-MOC4/account01/B08/20260922T083848Z-account01-B08-MOC4-r12/REPORT.md`.
Exact checker/output: sibling `verify.py` and `verification.txt`.
