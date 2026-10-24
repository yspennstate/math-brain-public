# PROB10-06 idea before code — sibling-chord control inside the branch-gap derivative

Runtime metadata available to this worker: model family **GPT-5.6 Sol**. Reasoning-effort telemetry is **UNVERIFIED**; GPT-6/maximum is prompt-only and is not claimed.

Status entering this run: parent Lyons--Pemantle--Peres problem OPEN/PARTIAL. Immediate PROB10-06 predecessor proves, pending independent audit, the restricted `{2,3}` theorem `p>=3/4, lambda<=12/5`, with all-mixture endpoint still `1.85527`. Its correction artifact preserves the theorem while replacing one overstrong finite-depth derivative sentence by a valid truncation/derivative-passage argument.

## New idea to test first

Keep the predecessor's exact cancellation

`Delta=(log(c3/c2))' <= (-J')/c3`,  `J=c2-c3`,

but do **not** lower-bound every denominator in `-J'` by `a=lambda-1`. In the natural four-branch coupling,

`D2=a+B0+B1+B2`, `D3=D2+B3`,

and

`-j'=(U0 B3+B0 U3)/(D2 D3) + B0 B3 D2'/(D2^2 D3)+B0 B3 D3'/(D2 D3^2)`

with `j=B0B3/(D2D3)` and `D2',D3'<=1`.

Because `B0,U0` and `B3,U3` are independent of the **sibling pair** `(B1,B2)`, dropping only the distinguished branches from the denominators gives

`-J' <= 2 eta mu C2 + 2 mu^2 C3`,

where

`mu=E B`, `eta=E U`,
`Cr=E[(a+B1+B2)^(-r)]`, `r=2,3`.

This retains two sibling escapes inside every denominator; the predecessor replaced `C2,C3` by `a^-2,a^-3`.

For the `{2,3}` family, the inherited reciprocal type-vector supersolution gives conditional mean lower bounds `E[B|nu=k]>=d_k`, and the support-at-most-three recursion gives `0<=B<=u=(3-lambda)/3`. Put

`dbar=(1-p)d2+p d3`.

For `f_r(s)=(a+s)^(-r)`, convexity on `[0,2u]` gives the endpoint chord

`f_r(s) <= f_r(0)+s/(2u) [f_r(2u)-f_r(0)]`.

Since `E(B1+B2)>=2 dbar` and the chord slope is negative,

`Cr <= a^(-r) + (dbar/u)[(a+2u)^(-r)-a^(-r)]`.

Using `c3>=mu/Dmax`, `Dmax=(9-lambda)/3`, and `mu<=u` then yields the new deterministic score bound

`Delta <= Dmax [ 2 eta C2 + 2 u C3 ]`.

This is strictly sharper than the predecessor's

`Delta <= Dmax [2 eta/a^2 + 2u/a^3]`

whenever `dbar>0`. The primary target is to see whether this moves the certified `p>=3/4` endpoint beyond `12/5` with an explicit speed-derivative margin and truncation constant.

## Three genuinely different attacks for this run

1. **Move #3 / stronger recursive observable (primary):** sibling-chord control above. Falsification target: check every independence step and the sign reversal when replacing `E(B1+B2)` by its lower bound in a negative-slope chord.
2. **Move #24 / extremal object:** test whether, given only `0<=B<=u` and `E B>=dbar`, the endpoint two-point law `{0,u}` maximizes the denominator kernels `E(a+B1+B2)^(-r)`. If true it validates the chord as the exact moment-envelope, not merely a convenient bound; if false preserve the counterexample.
3. **Move #12 / conserved weighted derivative:** try the ratio `q=U/B` directly inside `j`, i.e. `-j'/j=q0+q3+D2'/D2+D3'/D3`, and look for a `j`-weighted contraction. This is materially different from the annealed `eta` route. If the weighting fails to close, record the exact missing correlation rather than reverting to a pathwise uniform contraction already known to degenerate near criticality.

No code has been written for this run before this note. Existing R02 handoff and all prior artifacts remain untouched. Neighboring P01 minimum-one and NM13-05 `{3,4}` work are complementary; this run stays on the `{2,3}` high-mixture branch-gap route.
