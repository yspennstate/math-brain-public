# B12 FEI sprint: region-2 secant/divided-difference tightening

Status: **new rigorous enclosure proposed and implementation/self-check delivered; assigned x in [1,2] region is NOT yet certified in this run.** Full FEI remains OPEN.

## Inherited target

The current sprint assigns account01/B12 the remaining read-once certificate region 2 with x in [1,2] for the M=96, K=40, C0=6.4548 candidate and margin c=0.003.  The pinned candidate is `cert_vi_h96k40.npz`, 70,354 bytes, Git blob `1e2a1a5c293fa7b6ec9885b7a410910d6589be80`.  The standing report already has region 1, region 3, T2, T3 and the tail at this margin; region 2 is the last reported open piece.  A repository search at the start/end of this run found no newer `c=0.003` region-2 VERIFIED result.

The existing improved region-2 code already keeps the piecewise-linear numerator

`D(x,lambda)=G_num(x)-G_num(x+lambda)`

exactly over cells, which reduced the observed depth-0 failure fraction in the standing report from about 7.8% to 3.5%.  Its remaining weakness is that `D` is then divided by an interval for v, while the mean-value alternative replaces a secant by the full slope range.  Both throw away the exact relation between lambda and v.

## 1. Exact secant identity: remove the small-v division

Write

- `p=2^{-x}`,
- `v=2^{-y}`,
- `lambda=L(1-v)=-log_2(1-v)=v ell(v)/ln 2`,
- `Ghat(x)=G_num(x)+c(1-p)`.

The region-2 A term is

`A=[Ghat(x)-Ghat(x+lambda)]/v`.

Since `2^{-lambda}=1-v`, the margin part cancels **exactly**:

`c[(1-p)-(1-p 2^{-lambda})]/v = -c p`.

Hence

`A = -(ell(v)/ln 2) Sec_G(x,lambda) - c p`,

where

`Sec_G(x,lambda)=[G_num(x+lambda)-G_num(x)]/lambda`.

This identity is exact, not an asymptotic expansion.  It removes the catastrophic `O(v)/v` interval division altogether.  The high-precision self-check gives maximum identity error `2.62e-72`; evaluating the unreduced difference directly in ordinary double precision loses as much as `2.67e-7` on the same random sample, which is already a non-negligible fraction of the current `c=0.003` margin.

## 2. Linear-fractional vertex lemma for a PL secant

**Lemma.** Let `G` be continuous piecewise linear.  Suppose `[x0,x1]` is contained in one source segment of G and `0<l0<=l1`.  Cut the rectangle

`R=[x0,x1] x [l0,l1]`

by every line `x+lambda=s_j`, where `s_j` is a node of G.  On each resulting polygon, both the minimum and maximum of

`Sec_G(x,lambda)=[G(x+lambda)-G(x)]/lambda`

occur at a polygon vertex.  Consequently it is enough to evaluate the four rectangle corners and the intersections of the node diagonals with rectangle edges.

**Proof.** On a polygon the source segment has slope `a_i` and the endpoint segment has slope `a_j`.  Thus

`G(x+lambda)-G(x)=(a_j-a_i)x+a_j lambda+(b_j-b_i)`.

Dividing by positive `lambda` gives a linear-fractional function.  Restricted to any line segment in the polygon it has the form `(at+b)/(ct+d)` with positive denominator; its derivative has constant sign (or is identically zero).  It therefore reaches its extrema at endpoints of every line segment, hence at polygon vertices.  The only vertices are the rectangle corners and the stated diagonal/edge intersections.  QED.

This is stronger than taking the minimum/maximum slope touched by `[x,x+lambda]`: it uses the exact *weighted average* of the PL slopes.  The deterministic implementation test used arbitrary, even nonmonotone, PL functions and 20,000 random rectangles.  Against a 17x19 dense grid per rectangle there were 0 containment failures.  On those stress tests the crude touched-slope width divided by the exact secant-vertex width had median 4.66 and 90th percentile 13.98.  These ratios are implementation diagnostics, not claims about the FEI candidate.

The code also returns the exact segment slope directly when both endpoints lie in the same segment, avoiding cancellation for tiny lambda.

## 3. Two exact monotonic endpoint reductions on B12's x-range

Two other losses in the old lower bound can be removed on `1<=x<=2`.

First,

`-8 p x -8(1-p) = -8[1+p(x-1)]`.

The derivative of `p(x-1)` is

`p[1-(ln 2)(x-1)] > 0` on `[1,2]`.

Therefore this whole negative term is minimized exactly at the upper x endpoint of the cell.

Second,

`D0=-8(1-v)(1-p)ell(v)/ln 2`.

Here `1-p` increases with x and

`h(v)=(1-v)ell(v)=-(1-v)ln(1-v)/v`

satisfies

`h'(v)=[v+ln(1-v)]/v^2 < 0`.

Since `v=2^{-y}` decreases with y, `h(v(y))` increases with y.  Thus `D0` is minimized exactly at `(x_hi,y_hi)`.  The delivered bound takes the maximum of the old interval lower bound and these endpoint lower bounds, so it is fail-safe.

## 4. Joint A+F divided difference

There is a second cancellation that the existing code separates.  Let

`F=[Psi(p)-Psi(p(1-v))]/v`

and define

`K(t)=Ghat(t)+Psi(2^{-t})`.

Then, exactly,

`A+F = [K(x)-K(x+lambda)]/v`

and therefore

`A+F = -(ell(v)/ln 2) average_{t in [x,x+lambda]} K'(t)`.

On a candidate segment with slope `s_j`,

`K'(t)=s_j + (ln 2) r [c-Psi'(r)],  r=2^{-t}`.

This exposes a Boolean-certificate-specific correlation: the candidate slope and the Psi derivative occur in the **same** derivative before taking an extremum.  Bounding A and F separately discards that correlation.  The delivered module precomputes rigorous per-segment interval bounds for `K'`, builds sparse min/max tables, and obtains an additional lower bound for A+F in logarithmic range-query time.  The final bound takes the maximum of the old separate A+F bound and this joint bound, so the new path cannot weaken certification.

## 5. Delivered executable

`r2_secant_enclosure.py` is a bounded/sharded driver for precisely account01's `x in [1,2]` region.  It:

1. refuses any candidate whose byte count / canonical Git-blob SHA-1 differs from the pinned M=96 candidate;
2. retains all three existing A bounds as fallbacks;
3. adds the exact PL secant-vertex A bound;
4. adds the joint A+F divided-difference bound;
5. uses the two endpoint monotonicity bounds above;
6. shards by y-node index so a worker can run independent bounded pieces instead of launching one uncheckpointed multi-hour job.

Source SHA-256 for the final local text before commit: `916997aa6a5f87a895adbb9e42ba4f6c808ff3ed49ae35a285858d44f6ab294a`.

`selfcheck_r2_secant_vertex.py` is deliberately separate from the certificate code.  It tests the geometry on arbitrary PL functions and the algebraic identities at high precision.  Its saved output is `selfcheck_output.json`.  This self-check is **not** promoted to a certificate result.

## 6. What was not completed

The private GitHub connector exposes the pinned NPZ as authenticated base64 text but does not materialize the binary into the native execution environment.  I therefore did **not** claim an M=96 interval run or a VERIFIED x-in-[1,2] shard in this invocation.  The implementation was syntax-checked locally and its mathematical core was stress-tested, but the actual production candidate run remains the next step in an environment with the repository checkout / NPZ present.

No settled read-once certificate was rerun, no FEI audit was performed, and no full-FEI claim is made.

## 7. Next target

Run the new driver on small y-index shards first and compare the number/depth of survivors against `phi2_over_v_lower_exact`.  If the secant/joint A+F bound removes the remaining x-in-[1,2] failures, concatenate the shard logs into a certificate record.  If survivors remain, inspect which of `B`, the remaining smooth F width, or the y-only `Psi(1-v)/v` term is binding; do not spend more cells until the binding cancellation is identified.
