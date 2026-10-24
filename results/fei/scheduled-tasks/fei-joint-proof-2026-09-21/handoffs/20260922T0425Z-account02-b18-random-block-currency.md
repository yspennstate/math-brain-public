# account02/B18 FEI handoff — exact random fixed-size restriction currency

Outcome: `ESSENTIAL_STEP_APPLIED` at mechanism level; full FEI remains OPEN / NOT PROVED.

Source-bound report: `proofnet24/P03-fei/fleet-2026-09-21/account02/B18/20260922T040428Z-random-block-currency/REPORT.md`, scientific commit `f50a43aa8fbf2207f23bd412f0183028a236ab52`, report blob `bd4972b11cb13989282f555deb9354509d1da590`.

Current target remains account01/B18 `LIMIT-PRIME-GATE-LIFT-v1` for the stable potential

`C_*=6.5218512`, `a_*=0.2682048`, `Gamma_*=Gamma_RO+a_* p(1-p)`.

Named OTHER-account theorem consumed and actually applied: account01/B17 `20260922T040831Z-balanced-arity5-complete/REPORT.md`, blob `076b4f50407e7af639566671c0367728decc0d28`. Since it proves `H/(I-1)<=6` for every balanced five-input uniform gate, the stable candidate has `D_* >= (C_*-6)(I-1)=0.5218512(I-1)>0` on that entire slice. Any arity-five falsifier must therefore be unbalanced at uniform bias or genuinely nonuniformly biased.

New theorem. For biased Fourier level masses `W_k=sum_{|S|=k} \hat G_p(S)^2`, reveal a uniformly random `r`-subset of the `n` inputs and average over the original product values. If `P_r` is the expected Poincare currency remaining after restriction, then

`P_r = (1/4) sum_{k>=2} W_k [ k(1-r/n)-1 + (r)_k/(n)_k ]`,

`Q_r:=P_0-P_r = (1/4) sum_{k>=2} W_k [ kr/n - (r)_k/(n)_k ]`.

Consequences:

1. `P_r <= (1-r/n)P_0`, hence `Q_r >= (r/n)P_0` dimension-independently.
2. For `0<r<n`,
   `Q_r >= (r/n)P_0 + r(n-r)/(4n(n-1)) W_{>=2}`.
3. Exact one-step aggregate identity:
   `sum_i Q_i = P_0 + W_{>=2}/4`.
   Thus the stronger account04/B18 sufficient bank `sum_i(-R_i^RO)<=a_*P_0` discards the valid scalar payment `a_* W_{>=2}/4`.
4. Increments are exact and front-loaded:
   `P_r-P_{r+1}=(1/(4n)) sum_{k>=2} kW_k[1-(r)_{k-1}/(n-1)_{k-1}]`.

Integration with account02/B16 signed block martingale: define

`B_r^RO = D_RO(G)-E D_RO(G restricted on random r-block)`.

Then exactly

`D_*(G)-E D_*(child)=B_r^RO+a_*Q_r`.

Therefore the named remaining implication is

**EXACT-RANDOM-BLOCK-RO-DEFICIT-v1:** for every non-affine Boolean gate and interior product bias, some `1<=r<n` satisfies `B_r^RO+a_*Q_r>=0`.

This statement plus lower-arity induction closes all gates, hence `LIMIT-PRIME-GATE-LIFT-v1`, hence FEI with `C=6.5218512`.

A minimal-essential-arity counterexample would have to violate the inequality at every scale simultaneously:

`B_r^RO < -a_* Q_r <= -a_*[(r/n)P_0+r(n-r)/(4n(n-1))W_{>=2}]` for every `1<=r<n`.

Nonoverlap: B16 already owns the general adaptive signed restriction martingale. B18 should next attack the source-specific base-defect/currency crossing above, ideally through discrete derivatives in `r`. Do not re-prove the block martingale or return to the exhausted nine-host shared-core tuning.

Exact checker output: 42,875 coefficient tests, aggregate identity true, zero failures, PASS=1. Checker is a self-check only; analytic proof is in the source report.

No novelty-priority claim is made.
