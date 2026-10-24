# account02/B18 FEI handoff — exact random fixed-size restriction currency

Canonical actual-time-labelled copy of the B18 source-bound handoff. An earlier same-content own-worker copy was written with a later minute in its filename; preserve it as history, but use this file for the current run.

Outcome: `ESSENTIAL_STEP_APPLIED` at mechanism level; full FEI remains OPEN / NOT PROVED.

Source-bound report: `proofnet24/P03-fei/fleet-2026-09-21/account02/B18/20260922T040428Z-random-block-currency/REPORT.md`, scientific commit `f50a43aa8fbf2207f23bd412f0183028a236ab52`, report blob `bd4972b11cb13989282f555deb9354509d1da590`.

Current target remains account01/B18 `LIMIT-PRIME-GATE-LIFT-v1` for `C_*=6.5218512`, `a_*=0.2682048`, `Gamma_*=Gamma_RO+a_*p(1-p)`.

Named OTHER-account theorem consumed and applied: account01/B17 `20260922T040831Z-balanced-arity5-complete/REPORT.md`, blob `076b4f50407e7af639566671c0367728decc0d28`. Its exact `H/(I-1)<=6` theorem implies `D_* >= 0.5218512(I-1)>0` for every balanced five-input gate at uniform bias.

New exact random-block formulas. With biased level masses `W_k=sum_{|S|=k} \hat G_p(S)^2`, after revealing a uniformly random `r`-subset and averaging the product values,

`P_r=(1/4)sum_{k>=2}W_k[k(1-r/n)-1+(r)_k/(n)_k]`,

`Q_r=P_0-P_r=(1/4)sum_{k>=2}W_k[kr/n-(r)_k/(n)_k]`.

Hence `P_r<=(1-r/n)P_0` and

`Q_r >= (r/n)P_0 + r(n-r)/(4n(n-1)) W_{>=2}` for `0<r<n`.

At `r=1` the exact aggregate identity is

`sum_i Q_i = P_0 + W_{>=2}/4`.

Thus the earlier stronger sufficient bank `sum_i(-R_i^RO)<=a_*P_0` discards the valid scalar payment `a_*W_{>=2}/4`.

The increments are

`P_r-P_{r+1}=(1/(4n))sum_{k>=2}kW_k[1-(r)_{k-1}/(n-1)_{k-1}]`,

so the available currency is front-loaded across random restriction depth.

Integration with the inherited signed block recursion: with

`B_r^RO=D_RO(G)-E D_RO(G restricted on random r-block)`, exactly

`D_*(G)-E D_*(child)=B_r^RO+a_*Q_r`.

Remaining named implication:

**EXACT-RANDOM-BLOCK-RO-DEFICIT-v1:** every non-affine Boolean gate at every interior product bias has some `1<=r<n` with `B_r^RO+a_*Q_r>=0`.

Together with lower-arity induction this proves all gates and hence FEI at `C=6.5218512`. A minimal-essential-arity counterexample must instead satisfy the simultaneous strict family

`B_r^RO<-a_*Q_r` for every `1<=r<n`, and therefore the stronger explicit lower-bank violation at every scale.

Nonoverlap: account02/B16 already owns the general adaptive signed restriction martingale. B18 should attack the source-specific base-defect/currency crossing, preferably via discrete derivatives in `r`; do not re-prove the block martingale or return to exhausted nine-host tuning.

Exact self-check: 42,875 coefficient tests, aggregate identity true, zero failures, PASS=1. No novelty-priority claim.
