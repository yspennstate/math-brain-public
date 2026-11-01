# PROB10-04 second idea before code — the pair obstruction is an r-block obstruction

The degree-two center mechanism from the preceding idea has an exact higher-arity extension, still distinct from NM13-13's degree-one random-score matching.

For any fixed `r>=2` within the Díaz light-degree cutoff, use a true center of class `t_{r,r}`.  Require all `r` of its `ps` copies to land in the safe anchor clause type `a=((1,1),(1,0))`.  Use `r` false leaves of class `f_{1,1,1}`, each with its unique `ns1` copy in a blocker of type `b=((0,1),(1,1))`.  If the center's `r` `nu` copies occupy the `r` unique `nu` slots of those blockers, flipping the center down and all `r` leaves up preserves flat satisfiability and changes the number of true light variables by `r-1>0`.  Hence a Hamming-weight-maximal flat assignment forbids every such completed `r`-block.

At fixed coarse type, if `A` available `t_{r,r}` centers contribute `A` disjoint marked `r`-sets among `U` `nu` copies, and the selected leaf blockers define `S` canonical `nu` slots, the exact rescue-free count is

`N_{r,0}(U,A,S) = [z^S] (((1+z)^r-z^r)^A (1+z)^(U-rA)).`

Indeed each marked center block may contribute any proper subset of its `r` copies, while the other `U-rA` copies are unrestricted.

With `z=S/(U-S)`, coefficient domination and the binomial-mode lower bound should give the fully finite inequality

`N_{r,0}(U,A,S)/C(U,S) <= (U+1) [1-(S/U)^r]^A`.       (r★)

The case `r=2` is exactly the pair formula already checked.  This second checker should exhaust small `(U,r,A,S)` by subset enumeration and verify both the generating-function coefficient and (r★) in exact integer/rational arithmetic.

For the Díaz application, the available-center density has mean asymptotic to

`a_r(x)=t_{r,r}(c_a/ell_ps)^r`,

while the selected-blocker density is the same

`s(x)=f_{1,1,1} c_b/ell_ns1`.

Thus each `r` supplies a positive interior exponential defect.  The run can take the best of finitely many `r` values, while explicitly acknowledging that the defect need not be uniform on boundary faces where the relevant type mass vanishes.
