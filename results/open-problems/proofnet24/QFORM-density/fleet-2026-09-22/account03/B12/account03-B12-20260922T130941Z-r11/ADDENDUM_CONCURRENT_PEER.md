# Concurrent-peer addendum: perturbative physical-block transfer with the optimized constant

After the main report was written, a fresh compatible B12 result became visible:

`yspennstate/math-open-problems@c33a86e95c0934f08acacf9d0c4fd5f9ba20738e`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B12/20260922T131954Z-account01-B12-qform-r11/REPORT.md`.

It proves `QFORM-LOW-LEVERAGE-VERTEX-COVER-ABSORPTION-v1` and, independently, a perturbative physical-block transfer using the then-current same-sign constant `<24.193`. I apply its perturbative setup to the optimized constant proved in this run.

## Corollary — optimized perturbative physical-block completion

Let `I` be a set of `m>=4` original coordinates. Suppose a symmetric reference block `B[I,I]` has at least `m-1` eigenvalues all `>=L` or all `<=-L`. Let `F` be an arbitrary symmetric perturbation satisfying only

`||F[I,I]||_op <= delta L`, `0<=delta<1`.

There is **no restriction** on `F` outside `I x I`: all outside eigenvalues and cross-couplings may be arbitrary. Put `A=B+F`. Then independent coordinate inputs with density caps one satisfy

`||p_{X^T A X}||_infinity <= C_*/((1-delta)L)`,

where

`C_* = (2*pi+3*sqrt(3)) + sqrt((2*pi+3*sqrt(3))^2+3*pi^2)`

`=24.1830382899615...`.

### Proof

Weyl's inequality gives at least `m-1` eigenvalues of `A[I,I]` of the same sign and magnitude at least `(1-delta)L`. Condition on all original coordinates outside `I`; cross-couplings become affine linear tilts. The optimized codimension-one same-sign theorem from the main report, applied to the `m` selected coordinates, gives the displayed bound uniformly in the conditioned outside values. Averaging preserves the cap. QED.

This directly sharpens the account01/B12 perturbative inequality `24.193/((1-delta)L)` while preserving its full arbitrary-completion scope.

## Combined B12 state

The two compatible mechanisms are now quantitatively complementary:

1. **physical same-sign block:** arbitrary outside completion is allowed with cap `C_*/L` (or `C_*/((1-delta)L)` under a `delta`-perturbation);
2. **diffuse rank-r core plus nonseparable remainder with low-leverage vertex cover:** the account01/B12 theorem gives the exact cap
   `[r/(r-2)] B(U_T G^{-1/2})^(2/r) [det(G)|det Lambda|]^(-1/r)`,
   in particular `3e/(1-tau_S)` for rank three under its stated trace-leverage sufficient condition.

The remaining full-target implication is not another local constant optimization. It is to prove that the bare three-large-eigenvalue hypothesis forces one of these product-preserving basins or a third mixed-sign multipivot mechanism. Full QFORM remains OPEN.
