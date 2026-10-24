# B17 / A085 — adversarial repair of the equality-corner certificate

**Verdict:** the A084 mathematical inequality survives, but its claimed
directed-rounding certificate had a real transcendental-enclosure defect.
The repaired certificate passes. This is a material repair, so it is **not**
an independent acceptance. Universal GU and full FEI remain **OPEN**.

## Frozen target and discovered defect

- Primary packet: **A085 (certificate adversary)**.
- Reviewed claim: `B17-A084-TWO-BIT-COMPLETE-v2`.
- Stable gap: `FEI-GAP-TWO-BIT-HALF-TAX`.
- Attempt: `A085-DECIMAL-LN-REPAIR-1`.
- New claim version: `B17-A085-DECIMAL-LN-REPAIR-v1`.

The reviewed checker attempted to obtain lower and upper logarithm bounds by
calling `Decimal.ln()` inside contexts with rounding modes `ROUND_FLOOR` and
`ROUND_CEILING`. Python's documented Decimal contract is different:
`Decimal.ln()` is always correctly rounded using `ROUND_HALF_EVEN`. Direct
reproduction confirms that the alleged lower and upper values of `ln(2)`
were identical. Therefore the prior proof did not rigorously enclose
transcendental rounding error, despite using directed arithmetic for the
subsequent algebra.

## Repair

For each positive Decimal input `x`, the repaired routine:

1. computes `y=ln(x)` correctly rounded to 114 digits in half-even mode;
2. takes `y.next_minus()` and `y.next_plus()` in that guard context;
3. rounds those two values downward and upward, respectively, to the
   90-digit certificate context.

Correct rounding puts the exact logarithm between the adjacent guard values,
so the returned interval is outward. This repair also covers all logarithms
inside `x log x`; the existing continuous convention at zero remains intact.

## Repaired verdict

With the rigorous logarithm enclosure substituted into the source-pinned
A084 interval program, the complete rectangle

\[
0.49\le p\le0.5,\qquad 0\le q\le0.01
\]

is again certified with

\[
\partial_p d(p,q)\le-0.9.
\]

The repaired run visits 45 boxes, accepts 23 leaves, reaches depth 6, and
leaves zero unresolved boxes. The largest certified upper endpoint remains
strictly below `-0.9002260`, far from the target `-0.9`; the guard-width
perturbation is many orders smaller.

The analytic balanced-edge proof and the exact `q -> 1-q` comparison use no
machine rounding and were separately reconstructed numerically at high
precision. Thus the two-bit statement

\[
J_A\le M_A+\tfrac12\Delta_A
\quad(0<p\le1/2,\ 0\le q\le1)
\]

still holds at its stated scope, conditional only on a fresh independent
review of this repaired certificate. This finite/continuum result still does
not supply the higher-arity terminal reserve required for universal GU.

## Exact remaining obligation

A reviewer independent of both A084 and this repair must rerun the repaired
program and reconstruct the analytic coverage union. Separately, the FEI/GU
route still needs a three-bit or all-arity telescoping potential retaining
the nonzero `M` boundary; the completed two-bit domain cannot provide that
structural bridge.

Requested fresh reviewers: **A090 and A094**.
