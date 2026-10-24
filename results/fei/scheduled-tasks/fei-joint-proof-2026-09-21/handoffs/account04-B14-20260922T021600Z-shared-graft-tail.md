# account04/B14 handoff — recursive shared-graft tail closed

**Source report:** `proofnet24/P03-fei/fleet-2026-09-21/account04/B14/20260922T021600Z-shared-graft-tail/REPORT.md`  
**Scientific commit:** `6c930d3dfc89be47caf2fb54dfe37efadec1232a`  
**Report blob:** `adba1f7d9aa222cf5f93ea2f8291a70197bb4396`  
**Status:** `ESSENTIAL_STEP_APPLIED / SHARED_GRAFT_TAIL_CLOSED`; full FEI remains **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

Consumed account01/B18's exact recursive shared-core recurrence (report blob `cbe682d84b52232ab4e91367b08bbfe73d74a39e`) and account03/B18's certified `F_4` interval (report blob `4d1e86bd941df8bb941ba974f6478bbe4842ef84`).

Write `R_t=H(F_t)/(I(F_t)-1)`, with designated singleton `c_t`. The inherited recurrence can be rewritten exactly as

`R_{t+1}=(1-w_t)R_t+w_t T(c_t)`, where `T(c)=(128/133)K(c^4)` and `w_t=(133/128)/(I_{t+1}-1)`.

New theorem: for every `t>=4`,

- `c_t in [0.22266585228,0.22266585229]`;
- `6.52185116734757174868 < T(c_t) < 6.52185116734807310137`;
- `sum_{t>=4} w_t < 0.004506766276547687`;
- `R_t < 6.52185116 < T(c_t)` and hence `R_{t+1}>R_t` for every future round.

The proof is a first-crossing argument: the total possible future motion from the certified `F_4` interval is `<1.043026e-9`, while the gap to the barrier `6.52185116` is `>2.1143555e-7`.

A new finite source-valid lower bound follows:

`C_FEI > R_5 > 6.5218509495173311787059282417417271320120`.

The whole infinite family is also trapped above `R_5` and below

`6.5218509496074708514840160706969912973269`.

So this exact recursive shared-graft mechanism is now analytically saturated: it improves forever but converges in a tiny interval. Do not spend further runs certifying `F_6,F_7,...` one at a time. The next all-gate arrow is either a distinct source-valid prime/shared-coordinate interference mechanism exceeding this trap, or an all-prime/all-bias upper inequality for a finite-cap potential above the saturated envelope.

Local standard-library rational checker passed. Checker SHA-256 `f09abae4b07423842a5f83e1d1dbf85ce8a1d4f4e65eedc68130aa6c0019485e`; output SHA-256 `0c5efa9aa77aeb2bcdefafdbd039eb902a2e9e711b58016f7881413d0791f8f8`. Platform safety blocked checker-source upload; no bypass was attempted.
