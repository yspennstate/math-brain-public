# Same-partition quantifier correction for REPORT.md Section 7

This companion is part of the same B14 run and must be read with `REPORT.md`. It preserves the original commit rather than silently rewriting it.

The analytic theorems in Sections 2--6 are unchanged. Section 7's conditional compiler needs one quantifier made explicit:

> The partition/order witnessing the residual estimate must be a **high-drop** two-colour partition, i.e. the SAME selected partition must satisfy both
> 
> `J-Q_P >= delta_0 J` (hence `D_P>=delta_0 J`)
> 
> and
> 
> `B_seq(P,pi) <= L D_P`.

The random-colour theorem guarantees existence of at least one partition satisfying the first condition, but it does **not** by itself guarantee that an arbitrary partition satisfying the second condition is the same one. Therefore the correct residual is the following.

## Corrected conditional compiler

Let `r_0<1` and `delta_0=(1-r_0)/2`. Suppose there is a dimension-independent `L` such that every minimal hybrid `H/J`-critical centered core with `r_c<=r_0` admits a two-colour partition `P` and an ordering `pi` of its nonanchors for which

`J-Q_P >= delta_0 J`                                      (C.1)

and

`B_seq(P,pi) <= L D_P`.                                   (C.2)

Then, because `D_P>=J-Q_P>=delta_0 J`, Section 5 gives

`Delta_P H <= B_seq + Phi-M_P
             <= [L+c_*/delta_0] D_P`,                     (C.3)

where `c_*=2/ln 2`. Hybrid ratio-criticality gives `Delta_P H>=R D_P`; hence

`R <= L+c_*/delta_0`.                                     (C.4)

At the inherited calibration `r_0=0.3156061323581677`,

`c_*/delta_0 < 8.431957731356981`.

Thus the actual unpaid implication is not merely `B_seq<=L D` for some partition. It is:

**find a high-drop partition supplied by the shell-poor mass budget, together with an order (possibly chosen adaptively from its genuine Boolean restriction histories), whose sequential erasure is `O(D_P)`.**

This is exactly where the existential-selector quantifier remains. No every-partition or prescribed-coordinate statement is asserted.

## Coordinate-ledger clarification

The affine change of basis does not preserve the potential `Phi`. In Sections 5--6, `Phi` on the parent means the potential in the original median-centered physical coordinates, while the final child potential is computed in the actual quotient coordinates after recentering. The displayed inequalities are therefore an explicit original-root-to-quotient accounting ledger, not a claim that `H-Phi` is invariant under arbitrary linear changes of basis. The plain-entropy compiler (C.3) avoids any ambiguity from this bookkeeping.

No other claim in `REPORT.md` is changed by this correction. Full FEI remains OPEN / NOT PROVED.
