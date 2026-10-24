# Independent repair of the B09 interval certificate

Date: 11 October 2026, 20:04 UTC.

**Verdict:** the interval implementation had a sign error. After a local repair,
the two-bit Boolean counterexample is rigorously certified with
`J_A-M_A > 0.1195` bits. The displayed 18-decimal enclosures remain unchanged.
This packet does not accept the full B09 auxiliary theorem or any full-FEI claim.

## Exact source and preservation

The original natural B09 run is
`20261011T195500Z-account01-B09-biased-restriction-uncertainty`.

- Open-problems commit:
  https://github.com/yspennstate/math-open-problems/commit/adb671ffcda143fa68347806bb96e8c305621a7d
- Source directory:
  `reports/fei-2026-10-11/runs/B09/20261011T195500Z-account01-B09-biased-restriction-uncertainty/`
- Brain mirror commit:
  https://github.com/yspennstate/math-research-brain/commit/bfe8eafa2194feb32cb3881957ef844b8fe30de0
- Brain directory:
  `research_pushes/2026-10-11-full-fei-campaign/handoffs/account01/B09/20261011T195500Z-account01-B09-biased-restriction-uncertainty/`
- Original script: `check_biased_and_counterexample.py`.
- Original script Git blob: `d8a3849f1fed3f2c879aa4c6cd12407d08e6f383`.
- Original script SHA256:
  `3147bc3d2dfeb54a2ecabce7c074131d9985a22fcd55b9a9fda3c4656b5af1fc`.
- Original report Git blob: `71b68e4decf9658a42fef6bb2668e19f25bd214a`.

All nine files were recovered, were nonempty, and had identical Git blob hashes
in both source commits. All eight SHA256 values listed in the original report
matched the recovered bytes. Claims and lifecycle information are embedded in
the original REPORT.md; there was no separate CLAIMS file.

The original run, report, scripts, and outputs were not overwritten. This is a
separate interactive independent repair, not evidence of a natural B18 scheduled
execution or a second natural B09 run.

## Defect

The original `log2_interval` returned

```python
lo / LN2_HI, hi / LN2_LO
```

for an interval `[lo, hi]` enclosing `ln(x)`. This quotient rule assumes a
nonnegative numerator. For `0 < x < 1`, the numerator is negative: a smaller
positive denominator makes the quotient more negative. The original rule does
not in general enclose the quotient and can return its endpoints in reverse
order. The regression check reproduces that reversal for `x=225/256`, one of the
original counterexample's probabilities, using 12 atanh terms.

The minimal semantic source diff is:

```diff
 def log2_interval(x):
     lo, hi = ln_interval(x)
-    return lo / LN2_HI, hi / LN2_LO
+    quotients = (lo / LN2_LO, lo / LN2_HI,
+                 hi / LN2_LO, hi / LN2_HI)
+    return min(quotients), max(quotients)
```

CHECK.py factors the quotient operation into a helper that also checks that
the denominator interval is strictly positive and both input intervals are
ordered. It adds domain checks for logarithms and probability laws. It keeps
the original rational atanh expansion and remainder; caching changes no values.

## Why the repaired calculation is rigorous

For `x>1`, set `z=(x-1)/(x+1)`, so `0<z<1`. The series and tail satisfy

\[
\ln x=2\sum_{k\ge0}\frac{z^{2k+1}}{2k+1},\qquad
0\le R_N\le\frac{2z^{2N+1}}{(2N+1)(1-z^2)}.
\]

Every partial sum and remainder bound in CHECK.py is a rational number.
For `0<x<1`, negating and reversing the bounds for `ln(1/x)` preserves the
enclosure. The case `x=1` is exactly zero. The positive interval for `ln 2`
can then be divided into any signed numerator interval by taking the extrema
of the four corner quotients. All entropy contributions use the correct
reversed bounds after multiplication by `-p`. Zero probabilities contribute
zero without evaluating their logarithm. Interval subtraction also reverses
the second pair of endpoints.

Thus the result does not depend on floating-point estimates or merely on a
high-precision numerical approximation. The final decimal strings are obtained
by exact outward rounding of rational endpoints.

## Counterexample and certified margin

Let `g(X,Y)=(-1)^(XY)` with independent `P(X=1)=1/8`, `P(Y=1)=1/4`, and reveal
the physical block `A={X}`. The product-biased coefficients are

\[
\widehat g(\varnothing)=15/16,\quad
\widehat g(\{X\})=-\sqrt7/16,\quad
\widehat g(\{Y\})=-\sqrt3/16,\quad
\widehat g(\{X,Y\})=-\sqrt{21}/16.
\]

Their squared masses are exactly `(225,7,3,21)/256`. The residual spectral bit
has nonempty mass `3/32`. The `X=0` child is constant; the `X=1` child has
biased spectral masses `1/4,3/4`. Consequently

\[
M_A=H((225,7,3,21)/256)-h_2(3/32),
\]

\[
J_A=h_2(3/32)-\tfrac18 h_2(3/4).
\]

The corrected 1200-term rational certificate encloses these quantities by:

| Quantity | Lower endpoint | Upper endpoint |
|---|---:|---:|
| `M_A` | 0.227909707141212807 | 0.227909707141212808 |
| `J_A` | 0.347454723165637765 | 0.347454723165637766 |
| `J_A-M_A` | 0.119545016024424957 | 0.119545016024424958 |

The checker explicitly proves the strict rational comparison
`lower_bound(J_A-M_A) > 1195/10000`. This refutes the helper statement
`J_A <= M_A` for arbitrary product-biased Boolean gates. It does not refute
FEI and does not bound a Fourier entropy-to-influence ratio.

## Targeted checks and reproduction

Run:

```sh
python3 CHECK.py > CHECK.out
```

The saved run exited successfully and returned PASS. It also checked:

- Reproduction of the original endpoint inversion on `225/256`.
- Containment of the 11 exact values `log2(2^k)=k`, for `-5<=k<=5`, covering
  negative, zero and positive logarithms.
- Three exact quotient intervals with negative, positive and mixed-sign
  numerator intervals.
- Exact treatment of `x=1` and of the probability law `(0,1)`, plus enclosure
  of the entropy of `(1/2,1/2)`.
- Rejection of two nonpositive logarithm arguments and two invalid
  probability laws.
- Ordered intervals at every quantity used in the final counterexample.

No unchanged large obstruction suite was rerun for this repair.

| File | SHA256 |
|---|---|
| CHECK.py | `d33caeaaf0232eec128a8406c6bb3bf8e4872937bddc91871ea195021c81f408` |
| CHECK.out | `d0efbda7a310e0a3ed704a2a373988a58ae5482e5e8612f9b43ccdd686110884` |

## Remaining independent review

The main B09 claim is the auxiliary inequality

\[
0\le J_A\le M_A+\Delta_A(p),\qquad
\Delta_A(p)=\sum_{i\in A}[h_2(p_i)+\log_2\max(p_i,1-p_i)].
\]

Its Maassen--Uffink fiber argument appears consistent on a limited read, but
this packet has not completed its full source and proof audit. The report's
claims concerning arbitrary composition and endpoint optimality also require
separate scope review. In particular, additivity established for exact disjoint
products must not be silently promoted to a free payment through arbitrary
compositions, and an upper bound's endpoint asymptotics alone do not prove
that it is an optimal Boolean tax.

Route the full proof to an independent A090/B18 or A091/B19 reviewer, with
a distinct A045 realizability check and A042 endpoint check where needed.
The repaired helper counterexample is now certified; the full B09 auxiliary
theorem remains REVIEW_PENDING. Full FEI remains open.

