# Execution-reset addendum — candidate A-B14-selective-v1

**Later directive read during this invocation:** `FEI-PROOF-EXECUTION-20260921T230620Z`. This addendum binds the already-proved mathematics in `REPORT.md` to the new campaign-A execution format rather than starting another auxiliary route.

**Campaign lead candidate consumed:** account01/B18, `proofnet24/P03-fei/fleet-2026-09-21/account01/B18/20260921T2205Z-folded-cooling-compiler/REPORT.md`, blob `9f2bb40584be20e5e440e7f3913873c34858bc91` at scientific master `6bc64ffdcacf2e43fa43462758ab5663bffc7d14`.

## Candidate A-B14-selective-v1

Use the lead's character-invariant potentials
\[
\mathcal C(f)=\sum_i\mathfrak j(j_i),
\qquad
0\le\mathcal C(f)\le {2\over\ln2}J(f),
\]
and
\[
\mathcal A_{z_d}(f)\le J(f),
\qquad z_d=1-1/d,
\]
with the proved adaptive re-centering telescope for `A`. For a fixed universal `lambda>=0`, define the noncircular bounded potential
\[
\boxed{
\Phi_\lambda(f,d)=\mathcal C(f)+\lambda\mathcal A_{z_d}(f).
}
\tag{R.1}
\]
Then
\[
0\le\Phi_\lambda(f,d)
\le\left({2\over\ln2}+\lambda\right)J(f).
\tag{R.2}
\]
After character-centering a terminal character to a constant, `H=J=Phi_lambda=0`. Thus the terminal value is explicit.

The desired direct selective inequality is: at every nonterminal state choose a realizable physical block/tree `T` such that
\[
\boxed{
\Delta_T H
\le C_*\,D_T+\Delta_T\Phi_\lambda,
\qquad
D_T=J-\mathbb E J_{\rm leaf},
}
\tag{R.3}
\]
for one finite dimension-independent `C_*`. The lead's telescoping then gives
\[
H(f)\le\left(C_*+{2\over\ln2}+\lambda\right)J(f),
\]
and character centering transfers this to ordinary influence. No FEI bound is assumed in the definition of `Phi_lambda`.

## Proved application from this run

For a pivot row with proxy `Q={Z=a}`, `q=2^{-r}`, average-control condition `I_Z<=rI_x`, inside false negatives `E^-<=q/16`, and outside false positives
\[
E^+\le {q\over8(r+1)},
\]
`REPORT.md`, Theorem 4.1 proves
\[
\Delta_ZH\le12I_Z\le12D_Z.
\tag{R.4}
\]
Both pieces of `Phi_lambda` have nonnegative physical restriction drop: the corrected-entropy identities give `Delta C>=0`, and the lead's folded activation theorem gives `Delta A>=0` under the prescribed cooling schedule. Therefore the **same physical full block** satisfies the direct candidate inequality
\[
\boxed{
\Delta_ZH\le12D_Z+\Delta_Z\Phi_\lambda.
}
\tag{R.5}
\]
This closes that branch of (R.3) with `C_*=12`, for every `lambda>=0`.

Equivalently, any `H/J`-critical core of ratio above 12 satisfying the row hypotheses must have
\[
E^+>{q\over8(r+1)}.
\]
This is an actual selective-decrement application, not just a new statistic.

## First essential unproved implication after the paid branch

For the remaining fixed-relative row regime
\[
E^-+E^+\le q/16,
\qquad
E^+>{q\over8(r+1)},
\tag{R.6}
\]
`REPORT.md`, Theorem 6.1 constructs a deterministic first-mismatch order with
\[
D_T\ge15rq/16
\tag{R.7}
\]
and Theorem 7.1 gives
\[
H(Y_x\mid T)\le h_2(E),
\]
indeed at most one quarter of the root pivotality entropy for `r>=2`.

The exact B14 missing inference is now the **same-tree numerator bound**
\[
\boxed{
\Delta_T H-\Delta_T\Phi_\lambda
\le C_{\rm sc}D_T
}
\tag{R.8}
\]
for some finite universal `lambda,C_sc`, on the selected fixed-relative primitive row. By (R.7), it is sufficient to prove the source-scale estimate
\[
\Delta_T H-\Delta_T\Phi_\lambda
\le K rq
\tag{R.9}
\]
with universal `K`; then `C_sc=16K/15`.

This is not asserted. It is the decisive local implication for B14. Structural coverage — proving that every dangerous minimum-dimensional critical core supplies an eligible row — remains a separate campaign-A obligation assigned to the structural workers; it is not silently assumed here.

## Early adversarial status

The known fixed-relative **full-block** obstruction is not a counterexample to (R.8), because (R.8) uses the stopped first-mismatch tree, not the refuted full block. Account03/B14's exact computation on that obstruction gives the stopped raw ratio tending toward 4 and therefore does not refute the candidate. Addressing-type examples may refute the separate structural-coverage premise and are deliberately not converted into a prescribed-coordinate claim. Tensor replication does not turn the refuted full-block statement back on; the candidate requires one realizable selector at the current primitive state.

The next designated adversary under the reset is account01/B17, which can attack this exact version `A-B14-selective-v1` rather than an earlier selector.

**Outcome label:** `ESSENTIAL_STEP_APPLIED` for the asymmetric paid branch (R.5); the fixed-relative selective numerator (R.8) and structural coverage remain open.  
**FULL-PROBLEM CHANGE:** NONE — full FEI remains OPEN / NOT PROVED.  
**MECHANISM CHANGE:** YES — direct bounded-potential/selective-decrement candidate now has one enlarged paid branch and an exact same-tree residual.
