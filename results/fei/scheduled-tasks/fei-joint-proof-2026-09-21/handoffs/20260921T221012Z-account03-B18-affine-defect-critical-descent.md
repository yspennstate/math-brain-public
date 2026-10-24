# FEI joint handoff — account03/B18 affine-defect critical descent

Execution: **WITHOUT_VERIFIED_BRAIN**. Full FEI: **OPEN / NOT PROVED**.

Scientific source:
`proofnet24/P03-fei/fleet-2026-09-21/account03/B18/20260921T221012Z-affine-defect-critical-descent/REPORT.md`
in `yspennstate/math-open-problems`, report blob `075eaed4478012929ddf58cd3fea4d96f221415d`.

## New proved implication

For an affine-subspace defect `g_Q=1-2 1_Q`, `Q=a+L`, codimension `c>=2`, let
`m=#{i:e_i notin L}` be the number of nonzero physical quotient columns. Then

- `H(g_Q)=H_c` depends only on `c`;
- `J(g_Q)=m 2^(1-c)`;
- `H(g_Q)<4J(g_Q)`;
- if `m>c`, a redundant nonzero physical quotient column can be restricted away while preserving codimension and entropy, reducing `m` to `m-1`, hence multiplying `H/J` by `m/(m-1)>1`.

Therefore no affine-subspace defect with `m>c` is restriction-maximal. The irredundant `m=c` branch is exactly the coordinate-subcube branch; after removing free coordinates, its minimum-dimensional normal form is a one-point defect.

## Application to the known interface-C obstruction

The dummy-extended half-band Boolean obstruction has direction
`span(e_2+e_3,e_D)`, so `c=D-2` and `m=D-1=c+1`. Either coordinate 2 or 3 is redundant. Both corresponding restrictions have the same codimension and `m'=c`, so their `H/J` ratio is larger by `(D-1)/(D-2)`. Thus the exact family that refutes an **all-Boolean positive** interface-C contraction is not a restriction-maximal FEI core.

This does **not** prove a critical-core contraction.

## Precise surviving compatibility gap

The authentic account02/B16 compiler parents are coordinate one-subcube defects, exactly the surviving `m=c` branch. Account03/B18 already proved their pair response lands exactly in the signed physical curvature sink:
`kappa=P=2^(2-c)=(2/c)J` on every frustrated pair.

But scalar postcompression remains invalid as a dimension-free generic reconstruction: if a scalar charge `eta` is represented as `eta=integral P dLambda`, then the account02 normalization barrier forces
`||Lambda||_TV >= 2^(c-2)|eta|` and `J||Lambda||_TV >= (c/2)|eta|`.

So the next valid source-exact interface is precompression:
`signed dual-code field -> three-phase mixed difference -> compensated live-window signed square -> physical kappa sink`, or else a genuine codimension-weighted source estimate.

## Checker

The standard-library checker exhausted `654,702` full-rank quotient representations through `n=5`, including `551,436` redundant `m>c` cases. Every redundant case had a deletable nonzero physical quotient column preserving rank and the exact ratio-improvement factor. Checker output blob: `49bffe2996836ce166ef690c61ab80082ff8c770`.

## Joint fields

- consumed_peer_artifact: account02/B18 `20260921T190755Z-affine-subspace-plaquette-payment/REPORT.md`, plus account02/B16 `20260921T184541Z-actual-current-parent-mask-incidence/REPORT.md`.
- applied_to_claim: whether the current half-band obstruction survives a legitimate restriction-maximal critical-core reduction and which authentic parent masks survive.
- remaining_implication: prove compensated finite-window precompression on restriction-maximal/high-ratio cores, or produce a restriction-maximal Boolean counterexample; do not revert to scalar positive parent reconstruction.
- next_recipient: account03/B16 (compensated window), account02/B16 (source normalization), account03/B17 (critical-core adversary).
