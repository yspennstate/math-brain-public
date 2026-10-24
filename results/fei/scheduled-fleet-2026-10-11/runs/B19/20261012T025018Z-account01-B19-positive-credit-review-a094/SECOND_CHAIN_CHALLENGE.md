# A094 second-chain challenge: B05 A023 positive-credit bound

## Hard implications selected independently

1. **Dyadic orientation.** The local term is
   `delta [s(2^-m)-s(2^-(m-1))]_+`. Although the dyadic arguments decrease as
   `m` increases, reversing a unimodal function still has only one increasing
   run. Positive variation is therefore bounded by the range, not multiplied
   by the number of levels.
2. **Endpoint `y=0`.** The logarithmic singularity occurs in `F''`, but the
   secant derivative uses `integral_0^x t F''(t) dt`, which converges.
   Meanwhile `F'(0)=4` continuously, so the range bound remains valid.
3. **Endpoint `y=1/2`.** The affine argument of `F` is constant; all secant
   credits vanish.
4. **One-bit terminal stage.** The parent packet is exactly `F(1/2)=2`, both
   children have packet `F(y)`, and reach is `2 delta`. This yields the
   separate `4 delta` bound and avoids applying a nonexistent `s(2x)` at
   `x=1/2`.
5. **Reach normalization.** The unique continuing point-defect branch at
   residual dimension `m` has reach `2^(m-a)=delta/x`; it cancels the local
   factor `x` once and only once.
6. **Arbitrary order.** Remaining factors enter only through a scalar parity
   disagreement `y in [0,1/2]`. The stage estimate is uniform in `y`, so no
   hidden best-order choice is present.
7. **Composition dependency.** The signed identity used after the positive
   bound is the separately accepted physical Möbius ownership theorem. The
   present review does not infer it from the new scalar estimate.

All seven implications survive reconstruction. No hypothesis was widened.
The challenge therefore accepts the theorem exactly at its declared scope.

