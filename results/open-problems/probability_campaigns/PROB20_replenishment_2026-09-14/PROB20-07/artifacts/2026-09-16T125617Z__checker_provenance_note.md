# PROB20-07 checker provenance note — 2026-09-16T125617Z

The first local execution of the new robust-tube checker stopped on the assertion comparing the global-entry radius

\[
\frac{(1-q)(5R^2/8)}{2(227/32)}
\]

with

\[
\frac{10}{227}(1-q)R^2.
\]

The failure was caused by using Python/SymPy structural equality (`==`) on two algebraically equivalent expressions rather than simplifying their difference. Direct simplification gives zero, so no mathematical constant changed. The checker was changed to test

```python
sp.simplify(global_radius - sp.Rational(10,227)*(1-q)*R**2) == 0
```

and the full exact checker then completed successfully with `ALL EXACT ROBUST-TUBE CHECKS PASSED`.

No theorem statement, bound, archived report formula, or numerical certificate was altered as a result of this implementation-only correction.
