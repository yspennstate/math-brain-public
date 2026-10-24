# Certificate adversary: exact audit record

Target: `B17-A084-TWO-BIT-COMPLETE-v2`, equality-corner interval component.

## Checks

| Risk | Result |
|---|---|
| Wrong transcendental rounding direction | **FOUND.** `Decimal.ln()` ignores floor/ceiling and uses half-even. |
| Algebraic interval operations | Passed inspection; multiplication uses all corners and division requires positive denominator. |
| Zero atoms | Preserved through the continuous `x log x` implementation. |
| Monotonicity domains | Valid: every `x log x` interval lies below `1/e`; every entropy interval lies in `[0,1/2]`. |
| Empty/unresolved boxes | None after repair. |
| Symmetry reduction | The upper collar follows from the displayed exact entropy comparison, not numerical symmetry. |
| Dimension/arity bridge | No universal bridge is claimed; theorem remains exactly two-bit. |

## Repair invariant

If `y` is a correctly rounded guard-precision logarithm, the exact value lies
between `next_minus(y)` and `next_plus(y)`. Rounding those endpoints outward
at the working precision gives a certified enclosure independent of the
half-even choice used by `Decimal.ln()`.

Verdict: **REPAIRED, FRESH INDEPENDENT REVIEW REQUIRED**.
