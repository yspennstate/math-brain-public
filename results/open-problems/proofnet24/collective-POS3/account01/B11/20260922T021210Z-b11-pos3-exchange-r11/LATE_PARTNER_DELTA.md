# Late partner delta — linear-depth corridor = linear Q/R exchange transport

The immutable main report was already written when the assigned partner account02/B19 published its newer run `20260922T022215Z-account02-B19-pos3-r13`. This additive note consumes that newer exact result without rewriting the report history.

Partner report: `proofnet24/collective-POS3/account02/B19/20260922T022215Z-account02-B19-pos3-r13/REPORT.md`.

The partner constructs a width-three family `P_m` containing an autonomous chain

`b<c_1<...<c_m<d`

and an outside element `x` with `b<x<d`, with `x||c_j` for every `j`. Under the exact uniform extension law it proves

`Pr(x<c_j)=j/(m+1)`.

Apply Theorem 3.1 of this B11 run to the ordered pair

`X=c_j`, `Y=x`.

Then

`Pred(x)={b} ⊆ Pred(c_j)={b,c_1,...,c_{j-1}}`,

so the endpoint-exchange hypothesis holds. For `j<m`, the unique minimal successor blocker of `c_j` that is incomparable with `x` is `c_{j+1}`. Hence

`Q_j/E = Pr(x<c_{j+1})=(j+1)/(m+1)`.

The reverse orientation is `x<c_j`. In the partner's exact scaffold, the rank `r=#{i:c_i<x}` is uniform on `{0,...,m}`. Conditional only on the orientation `x<c_j`, the open interval from `x` to `c_j` is endpoint-neutral exactly when `r=j-1`; if `r<=j-2`, it contains at least one earlier chain element comparable with `c_j`. Therefore the B11 reverse nonneutral remainder is

`R_j/E=(j-1)/(m+1)`.

Thus the B11 identity becomes

`Q_j/E+R_j/E = 2j/(m+1)`,

and

`2 Pr(c_j<x)-1 = 1-2j/(m+1)`.

So the partner's linear-depth pair migration has an exact exchange interpretation: moving one step deeper into the autonomous chain increases **both** the common blocker term `Q_j` and reverse remainder `R_j` by exactly `1/(m+1)`, hence increases `Q_j+R_j` by `2/(m+1)`. The `1/3–2/3` crossing for the pair `x||c_j` occurs precisely when

`1/3 <= j/(m+1) <= 2/3`.

This sharpens the partner synthesis in the main report. The obstruction to a bounded-depth contraction lift is not only that a balanced pair migrates: the exact two masses controlling the endpoint exchange are forced to accumulate linearly across the module. Any viable chain-module induction should therefore track `Q+R` as a corridor potential, rather than try to preserve a fixed outside pair or inspect a bounded endpoint neighborhood.

For `j=1`, `R_1=0`; for interior `j`, `R_j` grows linearly. This is consistent with the seven-element first-boundary witness in the main report, where delayed nonautonomy can coexist with `R=0`: positive reverse remainder is a corridor-depth phenomenon, not an automatic local consequence of having a delayed distinguisher.

No parent POS3 closure is claimed. This is an exact application of the newer assigned-partner result to the B11 exchange identity.
