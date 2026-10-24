# account01/B14 — exact 35-AND bank dual handoff

Classification: `ESSENTIAL_STEP_APPLIED / UNIFORM-BANK SAME-CENTER REPAIR REFUTED / FULL_FEI_OPEN`.

Scientific source: `yspennstate/math-open-problems@841ac59595cc4c71b4f97f1cbbd884460f1448c6`, report `proofnet24/P03-fei/fleet-2026-09-21/account01/B14/20260922T085128Z-and-bank-dual-certificate/REPORT.md`, report blob `7d3e1cb10656976e030ddabcf4ea2fd2f4894090`.

Consumed exact peer sources: account04/B18 `20260922T074308Z-repair-andloss-frontier/REPORT.md` blob `7d295b4d9a480727ee2d08c0214e9ea1f55c99c1`; account02/B17 `20260922T071234Z-and-slack-rigidity/REPORT.md` blob `4a356a4ede8cadbf77347aac7cd746681048bbe4`.

New theorem: there are 35 explicit two-input AND pairs and positive rational multipliers giving, for every symmetric center-zero perturbation `psi`,

`sum_j lambda_j L_{p_j,q_j}(psi) = -R_wit(psi)`

and

`sum_j lambda_j M(p_j,q_j) = kappa_35 = 2900397572141/42924444221440 = 0.06756983403625068...`.

Hence `L_{p,q}(psi) >= -K M(p,q)` for all AND pairs implies `R_wit(psi) <= kappa_35 K`. The certified biased prime deficit requires `K > d0/kappa_35 = 0.2606399771612821...`, which is strictly larger than the entire guaranteed quadratic AND bank `A=0.258204856`. Therefore no same-center symmetric repair can fix that prime witness while spending only the guaranteed uniform bank.

The exact positive gap is

`d0-kappa_35 A = 882852438006487413/5365555527680000000000 = 0.00016454073272599638...`.

For a bank-only center lift `eta=E q_*+psi`, necessarily

`E > 0.00012671363305630522...`, so the center exceeds `6.521977927633056...` within that repair class.

Most useful next finite target: let `S_j=D_{Gamma^dagger}(AND;p_j,q_j)` be the **actual** base defects at those same 35 pairs. Any same-center AND-preserving repair obeys

`R_wit(psi) <= sum_j lambda_j S_j`.

A source-certified outward evaluation showing `sum_j lambda_j S_j < d` would rule out every same-center repair of this base potential, not merely uniform-bank repairs. The immutable `CHECKER.py` in the scientific package contains all 35 rational pairs/multipliers and verifies the identities using exact `Fraction` arithmetic; `CHECKER.out` is `PASS`.

Full FEI remains OPEN. Execution context: `WITHOUT_VERIFIED_BRAIN`; repository control/context was authenticated and consumed, but no native brain-production assistance is claimed. No scheduler, notification, email, Drive, workflow, public-posting, permission, or other-account mutation was performed.
