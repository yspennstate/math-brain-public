# MOC4 handoff — account01/B08 exact parity-roof refutation

Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Run: `20260922T013942Z-b08-moc4-r11`  
Outcome: **CANDIDATE_REFUTED**; parent MOC4 remains OPEN.  
Brain status: `WITHOUT_VERIFIED_BRAIN`.

## Scientific delivery

Private canonical report: `yspennstate/math-open-problems`, `proofnet24/collective-MOC4/account01/B08/20260922T013942Z-b08-moc4-r11/REPORT.md`, first report commit `1204bdd4463fa137bcfb1d53c3b5ce9702930924`. Exact standard-library verifier is beside the report; verifier creation commit `799e22b104ab23ae1187f3afb4fcb365ac979677`, exact output creation commit `82e2a71287a927a275c90c24195ece5f112bb883`.

## Peer result consumed

Named assigned-partner result: **account02/B09 `MOC4-BIPAIR-MAX-v1`**. Its exact pair-ellipse theorem is applied below to distinguish the scalar-certificate failure from a target counterexample. Lead input: account03/B07 `MOC4-PARITY-SLACK-v1`.

## New exact reduction

For any 3x3 doubly stochastic `R=(r_ij)`, every Birkhoff decomposition is one-dimensional. With `x=lambda_123`,

`lambda_231=r12-r33+x`, `lambda_312=r13-r22+x`, `lambda_132=r11-x`, `lambda_321=r22-x`, `lambda_213=r33-x`,

on

`L=max(0,r33-r12,r22-r13) <= x <= U=min(r11,r22,r33)`.

For the lead costs `F_rho=A_rho-2m_rho`, the absolute part is decomposition-independent, so

`Psi_K(R)=<R,|K|>-2 max{M_K(L),M_K(U)}`,

where `M_K(x)=sum lambda_rho(x)m_rho(K)`. Therefore the lead roof gate `<D,K><=Psi_K(R)` is equivalent to

`2 max{M_K(L),M_K(U)} <= <R,|K|>-<D,K>`.

This exposes a quantifier error in the current `MOC4-PARITY-SLACK-v1`: existence of one decomposition satisfying the payment controls the wrong extremum and does not imply the roof gate.

## Exact true-unitary structured witness

A rational orthogonal `U` obtained by applying the exact row-(2,4) Givens rotation `(c,s)=(399/401,40/401)` to account04/B09's rational matrix, together with exact simple Gaussian-rational spectra and unit direction `eta=(-85-132 i)/157`, gives strict positive complementary minors and a unique exposed permutation support vertex. Exact arithmetic yields

`L=3360256/2512515625`, `U=31264/390625`,

`M(L)=4584325741267946/246540595703125`,

`M(U)=19721109561978994/1232702978515625`,

`slack/2=112323046812873304/6163514892578125`.

Thus the lead's stated existential payment **holds** at endpoint `U`, but the actual roof is controlled by endpoint `L` and

`<D,K>-Psi_K(R)=4570193437650692/6163514892578125 > 0`.

So the stated existential certificate is not a valid implication, and the correctly strengthened unconditional scalar roof is itself false on genuine structured generic data.

This is **not** an MOC4 counterexample: in the same direction the actual determinant support is `371150847508507028/6163514892578125`, while the unique 24-vertex support maximum is `2973192/19625`, leaving exact positive slack `562623072007117972/6163514892578125`.

Applying account02/B09, the witness is not pair-stationary: the exact row-(1,2) support derivative is `245364861810144/3074072265625 > 0`. Hence it cannot be a global violating maximizer.

## Next shared implication

Replace the unconditional scalar gate by **`MOC4-STATIONARY-ROOF-v1`**: prove the corrected maximum-penalty roof inequality only under all twelve account02/B09 pair-ellipse north-pole conditions for the same true unitary/support direction; or construct a genuine pair-stationary simple-spectrum counterexample and retain the exact full `X`-dependent six-fiber inequality.

Recommended recipients: account03/B07 lead, assigned partner account02/B09, account01/B07, account04/B09, account03/B20.
