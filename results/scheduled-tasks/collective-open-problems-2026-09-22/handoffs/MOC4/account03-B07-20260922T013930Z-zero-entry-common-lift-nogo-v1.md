# MOC4 handoff — zero-entry common-lift no-go

Source worker: `account03/B07`  
Run: `20260922T013930Z-account03-B07-MOC4-r11`  
Candidate: `MOC4-ZERO-ENTRY-COMMON-LIFT-v1`  
Outcome: `CANDIDATE_REFUTED`; parent MOC4 remains OPEN.  
Scientific report: `proofnet24/collective-MOC4/account03/B07/20260922T013930Z-account03-B07-MOC4-r11/REPORT.md` at scientific commit `457cce618ad2542b6590807b7e516eaf8b139585`, report blob `47f09f9f722aa8501330ca532a2ca261474c681c`.

## Consumed peer

Assigned partner `account04/B08`, `MOC4-PAIR-FLAT-BOUNDARY-v1`, report blob `3c71dc6a046f699b3248957d660b2c02fe968efb`: a flat pair orbit at a global support maximizer can be moved, at equal support, to a true unitary with a zero entry. Thus the zero-entry boundary is a genuine branch that must be closed.

## New decisive result

The tempting repair “every zero-entry true unitary admits one probability law on `S_4` reproducing all its two-subset squared-minor marginals” is false.

For the exact rational orthogonal matrix

```
[       0,       3/5,     16/25,    -12/25]
[ -69/325,  -192/325,     48/65,      16/65]
[    48/65,     16/65,    69/325,    192/325]
[    16/25,    -12/25,         0,       -3/5]
```

let `R_{I,J}=det(U[I,J])^2`. Every probability law on permutations must satisfy the pointwise-derived cut

`R_{02,23} <= R_{01,02}+R_{01,03}+R_{01,13}+R_{03,02}`.

The exact unitary instead gives a positive violation

`40448/2640625 > 0`.

The verifier checks orthogonality, all 24 permutation indicators, exact rational minors, and the gap. This does **not** refute MOC4; it refutes only the common-lift shortcut on the zero-entry branch.

## Positive boundary structure retained

When `u_00=0`,

`|det U[{0,i},{0,j}]|^2 = |u_0j|^2 |u_i0|^2`

for `i,j in {1,2,3}`. The corner second-minor block therefore factorizes rank one, but the exact witness proves that this does not extend to a globally consistent `S_4` subset-marginal law.

## Next shared implication

`MOC4-ZERO-FACE-SUPPORT-v1`: prove the exact support inequality directly on a zero-entry unitary face, using the boundary factorization plus the structured spectral/support coefficients and the exact six-fiber formulation; do **not** assume a common permutation lift. In parallel, the pair-strict interior still carries `MOC4-PARITY-SLACK-v1` as a sufficient structured gate.

Primary recipient: `account04/B08`; also relevant to `account01/B07`, `account04/B09`, `account02/B07`, and `account03/B20`.

Execution was `WITHOUT_VERIFIED_BRAIN`; no FEI proof content, benchmark gold, answer keys, repairs, witnesses, encryption keys, credentials, scheduler identifiers, machine paths, email/Drive material, public posting, paid model/API, Codex, or remote workflow was used.
