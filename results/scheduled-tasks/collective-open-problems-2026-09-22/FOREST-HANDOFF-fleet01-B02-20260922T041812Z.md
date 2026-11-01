# FOREST handoff — fleet01/B02 — candidate-transfer correction

Outcome: `CANDIDATE_REFUTED` for the current end-to-end proof candidate only; FOREST itself is not refuted. Context: `WITHOUT_VERIFIED_BRAIN`.

Consumed latest complete lead `FOREST-KN-HERMITE-REDUCTION-v1`, shared handoff blob `cad5f1b8546f44f200d441b71095a9fde4a20d4b`, and named partner fleet02/B03 run `20260922T031602Z-b03-forest-r12`, report blob `ee00454cbfa035fa8778274340630f3a872b492a`.

## Decisive correction

The candidate used a fixed-graph upgrade

`unit p-NC on G -> M(G) independence-correlated for all positive weights`.

The detailed Cocks/Erickson mechanism does not justify that implication from one graph. Erickson Proposition 5.2.2 requires unit I-negative correlation for **every rational two-terminal gadget expansion** `M[Q^{E-{e,f}}]`; Corollary 5.2.3 is class-level: **all graphs** are unit I-negatively correlated iff **all graphs** are I-Rayleigh. Oxley §15.8 records the same class-level Cocks theorem.

Sanity check: Stark (2011) already proves unit p-NC for `K_n` for all sufficiently large `n`. If the fixed-graph upgrade plus minor closure were valid, Stark would already imply FOREST for every finite graph by choosing a sufficiently large `K_n` and deleting edges. Later literature still treats the general conjecture as open. Therefore the Semple--Welsh end-note wording that appears fixed-graph cannot safely be used as the candidate's transfer theorem without the primary proof resolving this conflict.

Corrected first unpaid implication: prove unit NC for every Cocks/Erickson rational gadget expansion of `K_n` (all marked pairs and gadget vectors), or prove weighted I-Rayleigh of `K_n` directly. Only then does Semple--Welsh minor closure yield arbitrary graphs.

## New complete-graph subresult

Applying fleet02/B03's continued-fraction recurrence one level deeper, for `k=n-4`, `x=k+5`, `s=k He_{k-1}(x)/He_k(x)`,

`C2 = k(k^2+9k+27)/((k+5)(k^2+8k+28)) <= s`,

and

`C2-C1 = k(k-1)(k-2)/((k+5)(k^2+8k+28)(k^2+9k+26)) >= 0`,

so `C2` strictly strengthens B03's `C1` for `k>2`. For the hard disjoint orbit,

`G_k(C2) = (4k^6+115k^5+1499k^4+10815k^3+46297k^2+111160k+117600)/((k+5)^2(k^2+8k+28)^2) > 0`.

Exact regression: brute `K3..K6` plus exact rational checks through `n=500`, PASS. Full report is in fleet01/B02 run `20260922T041812Z-b02-forest-r11/attempt_report.md`.
