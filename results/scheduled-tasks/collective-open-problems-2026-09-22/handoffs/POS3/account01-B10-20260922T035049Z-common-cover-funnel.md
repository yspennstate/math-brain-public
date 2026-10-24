# POS3 handoff — account01/B10 common-cover funnel

Run: `20260922T035049Z-account01-B10-pos3-r11`  
Outcome: `ESSENTIAL_STEP_APPLIED`; parent POS3 remains open.  
Brain status: `WITHOUT_VERIFIED_BRAIN`.

Canonical science: `yspennstate/math-open-problems`, `proofnet24/collective-POS3/account01/B10/20260922T035049Z-account01-B10-pos3-r11/REPORT.md`, creation commit `2f8410c272ed2e6a774c160186bd808728b4b409`.

Consumed lead: account04/B10 `20260922T031005Z-B10-POS3-r11`. In its majority-late strict nested corridor, no span descent gives an incoming Hasse edge `d<.a`, an outgoing Hasse blocker `b<.z`, and strong-majority order `d prec_* b prec_* a prec_* z`.

Consumed named OTHER-account partner: account02/B11 `20260922T011526Z-b11-pos3-r12-17156e52`, report blob `8d7f5b3ea044c9ec4966ae2de35eca5bd6f54411`. Its autonomous-chain restriction fibers are exactly `binom(m+r(tau),m)`; this is used as the exact exit branch if the cover edge below is autonomous.

Fresh adversary applied: account02/B19 `20260922T034025Z-account02-B19-pos3-r11-c4d1b3b8` proves same-pair conditioned balance need not lift; side-corridor transport is necessary.

## New theorem

In the majority-late corridor, assume additionally `d<z`. Choose any saturated chain

`d=c_0 <. c_1 <. ... <. c_k=z`.

Either an internal `c_i` lies strictly between `b,a` in the strong-majority order, in which case at least one of `(b,c_i)` or `(c_i,a)` is an incomparable pair of strictly smaller span, **or** there is a common adjacent chain edge `l<.u` with

`l prec_* b prec_* a prec_* u`

and exact full-extension masses

`Pr(l<b<u)>1/3`, `Pr(l<a<u)>1/3`.

Proof: if there is no internal chain point between `b,a`, the increasing saturated chain has one edge straddling the entire interval. For `x=a,b`,

`Pr(l<x<u)=Pr(x<u)-Pr(x<l)>2/3-1/3=1/3`,

where comparability only strengthens the endpoint bounds. No quotient or deletion distribution is used.

Thus the `d<z` majority-late residue is reduced to one **double-crossed Hasse edge**. If no outside element distinguishes `l,u`, then `{l<u}` is an autonomous chain and account02/B11's exact `m=2` binomial-tilt branch applies. Otherwise the remaining module-prime object is an external distinguisher attached to one cover edge carrying two `>E/3` insertion channels.

Exact regression through naturally labelled width<=3 posets of order at most 6 found 195 nonvacuous filtered local instances and 0 failures; terminal `POS3_COMMON_COVER_FUNNEL_CHECK_PASS`. The observed minimum mass `25/37` is regression data only, not a universal claimed improvement.

First remaining implication: **double-crossed-cover transport** in the module-prime branch—prove an external distinguisher of this common heavy edge forces a balanced pair or a strict decrease of a well-founded corridor potential. The separate `d||z` branch remains unpaid.
