# E0011 scope correction for the B2 annulus poison screen

This immutable artifact narrows one overbroad sentence in the same-run report `runs/2026-09-19/2026-09-19T214800Z__report.md` without modifying that report.

The exact recursion and exact values of the CO-only poisoning event `C_n` are correct and were re-executed independently in the automation runtime after the report write. The recomputation exactly matched the archived output:

- `P(C_3)=1185137255209811/18149089959000000 > 1/64`;
- `P(C_4)=723562742238017127442332091656869461753752727645710378495688696943908133171453/341126154188145048161020444712901025342738778581342629588150560778240000000000000 < 1/64`.

However, the implication `f >= P(C_n)` is **not universal over every possible regenerative trial whose entrance happens to be `A_n`**. It requires that a path in `C_n` cannot be stopped earlier as RETRY. This condition is automatic for the narrow exact-entry class in which RETRY requires return to the exact translated `A_n` pattern: along `C_n` there is no O2 adsorption, so O count never increases and the exact entrance pattern cannot be recreated after the first effective CO event. It is also valid for any other trial whose stopping rule explicitly classifies the full `C_n` path as FATAL before RETRY.

For a broader location-flexible annular seed class that accepts intermediate deformed/smaller annuli as RETRY, `C_n` may intersect a RETRY stopping event before all-CO absorption. In that setting its full probability cannot simply be charged to the one-trial fatal probability `f`.

Therefore the correct B2 conclusion is:

1. the `3 x 3` annulus is rigorously rejected for **exact-pattern / no-early-RETRY** regenerative trials by the `1/64` screen;
2. `P(C_3)>1/64` is a quantitative poisoning hazard that any broader soft-annulus class must interrupt by a legal RETRY mechanism, not a universal impossibility theorem for the entrance geometry itself;
3. the `4 x 4` annulus passes this same necessary screen for the narrow class, but no positive `M_reg` certificate follows;
4. the separate rigid-collar statement remains correctly scoped as written: if first collar erosion is declared FATAL, the first-event O2 probability `1/3` alone rules out `a>63f`.

This correction does not change the run metric: `M_reg: 0 -> 0`. It strengthens the motivation for the B19 soft-collar RETRY architecture and should control any later use of the B2 calculation.
