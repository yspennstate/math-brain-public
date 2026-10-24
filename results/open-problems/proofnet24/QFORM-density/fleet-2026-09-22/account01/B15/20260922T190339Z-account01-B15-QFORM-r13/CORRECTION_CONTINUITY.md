# Correction to REPORT.md: full target-scope qualitative continuity is already proved by the assigned partner

This file corrects only the regularity-status paragraph of the immutable r13 report. The graph-trace theorem and the correction of the scalar conditional-height gates are unchanged.

After the initial r13 report was committed, I read the complete source-pinned account02/B15 r3 theorem:

- `yspennstate/math-open-problems@4b2e6a36bcffeb767998c43d27cee1d8f5eaa07e`
- `proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260922T150242Z-account02-B15-qform-r3/REPORT.md`.

It proves the following target-level qualitative regularity theorem.

> If `X_1,...,X_n` are independent with densities bounded by one and `A` is any real symmetric matrix with `rank(A)>=3`, then `X^T A X` has a **bounded continuous density**. If `B=A_{J,J}` is any nonsingular physical principal block of order `d in {3,4}`, then
>
> `||p_(X^TAX)||_infinity <= C_d/sigma_min(B)`,
>
> with `C_3=2*pi+3*sqrt(3)` and `C_4=4*pi+8`.

The continuity proof is product-structural rather than generic coarea. On a nondegenerate physical 3- or 4-coordinate block it splits away a small critical neighborhood, a far field and one-gradient-coordinate tubes; on the remaining compact transverse charts it uses two original-coordinate derivatives and an `L1` approximation of one moving one-dimensional factor. The fixed matrix-dependent height bound then permits dominated convergence after conditioning on all outside coordinates. This is precisely why the generic bounded-joint-density shell counterexample does not apply.

Therefore the correct regularity status after r13 is:

1. **Absolute continuity:** proved for any nonzero quadratic of an absolutely continuous joint law.
2. **Finite bounded density for each fixed rank-`>=3` matrix:** proved.
3. **Continuous representative for each fixed rank-`>=3` product target:** proved by account02/B15 r3.
4. **One matrix- and dimension-independent height constant:** still OPEN; this is the sole central target.

The live correction ledger can lag the source-pinned worker theorem, so `CLAIMS.json` marking continuity `OPEN` must not override this newer complete source result.

This correction strengthens the motivation for the r13 graph-trace identity: regularity no longer needs to be extracted from that identity. Its role is purely quantitative—retain scalar-level translation/packing and original-coordinate product provenance while seeking the universal height constant.
