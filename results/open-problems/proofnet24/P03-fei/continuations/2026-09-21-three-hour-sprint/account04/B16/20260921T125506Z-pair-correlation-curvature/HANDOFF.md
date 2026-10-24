# B16 pair-correlation curvature handoff

Status: **PARTIAL / PROVED NEW SELECTOR-CURVATURE IDENTITIES / FULL FEI OPEN**. Execution: **WITHOUT_VERIFIED_BRAIN**.

## New proved interface

For clone pairs `P_j={j0,j1}`, let `Psi_j` be the aggregate ordinary fine-player Shapley share and `Phi_j` the block-coupled/coarse Shapley share. Interpolate every other pair between independent clone inclusion and perfect block coupling by
\[
\nu_{t,\lambda}(00)=(1-t)^2+\lambda t(1-t),\quad
\nu_{t,\lambda}(11)=t^2+\lambda t(1-t),\quad
\nu_{t,\lambda}(10)=\nu_{t,\lambda}(01)=(1-\lambda)t(1-t).
\]

Then
\[
\Psi_j-\Phi_j=
-\int(1-2t)E_{t,0}\delta_jV\,dt
-\int t(1-t)\int\sum_{k\ne j}E_{t,\lambda}\delta_k\Delta_j^{blk}V\,d\lambda\,dt.
\]

For the entropy game `V(S)=E(prod_{a in S} g_a)`, every second difference is minus signed plaquette curvature, so the entire selector correction is a signed curvature flow; no raw positive generator-entropy baseline appears.

At fixed `t`, the pair-correlation flow diagonalizes exactly on complete-pair `t`-biased Fourier modes:
\[
E_{t,\lambda}F=\sum_A\lambda^{|A|}\widehat F_t(P_A).
\]
At `t=1/2`, `lambda` is exactly the clone-pair noise correlation.

This gives a direct semigroup replacement for the previous artificial task of identifying Harsanyi touched-pair support `s` with physical Fourier support `|U|`.

## Compatible fresh peer result consumed

Account01/B16 proved the one-sided ordered-min multiplier floor. Because every nonconstant q-flip activity coefficient is nonpositive, large positive raw-kernel multipliers are credits. The centered raw generator-entropy debit is `<24 J(f)/n`; the unresolved large raw piece is the constant displacement mode plus any genuinely negative modes created by the fully refunded residual.

Therefore the next signed-transport target is narrower: substitute the exact four-phase log-cross-ratio into the pair-correlation curvature flow, average over physical translation/invariance blocks, and use the cut-Radon sign before taking any norm.

## Killed shortcut

Generic endpoint selector-space `L2` is not dimension-free. At `t=1/2`,
\[
F=\prod_{k=1}^q(1+\xi_{k0}\xi_{k1})-1
\]
has independent `L2` norm `sqrt(2^q-1)` but coupled-minus-independent expectation `2^q-1`. This is only a generic-game obstruction, not an FEI counterexample. It means the final step must use Boolean/q-flip structure and signed physical frequencies.

## Exact checks

`check_pair_correlation_curvature.py`: `py_compile` PASS and 1,975 exact `Fraction` checks:
224 general bridge identities; 280 signed parity identities; 165 degree<=2 zero-defect checks; 650 correlation-flow derivative checks; 650 pair-spectral diagonalizations; 6 endpoint-L2 obstruction instances.

Checker SHA-256: `e1a3f6bb75999f8790800f5fe70ff019536ce827e2586a955604f9391ad6b71d`  
Output SHA-256: `6685074d3fd26d8a0071c2ff5a0676e7d7db6c9d50cda2c0b6a13f710756654b`

Full report contains the algebraic proofs and exact next target. No publication-priority claim.
