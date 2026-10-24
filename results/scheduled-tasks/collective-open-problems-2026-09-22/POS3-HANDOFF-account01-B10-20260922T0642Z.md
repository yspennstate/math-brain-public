# POS3 handoff — account01/B10 — cross-anchor PQD refuted

Source report: `yspennstate/math-open-problems`, `proofnet24/collective-POS3/account01/B10/20260922T061815Z-b10-pos3-r11/REPORT.md`, blob `8530091b5d47d9ae4c431026cabb70a6a6afde5d`.

Outcome: `CANDIDATE_REFUTED`. Parent POS3 remains open.

Consumed/applied named partner: account02/B11 `20260922T055456Z-b11-pos3-r16-7136730f`, report blob `09ccf73a03359bcc0545abff5a8a5bc79cc2f42d` (exact leaf splice; majority-facing nonempty chain leaf side excluded in a series-indecomposable no-balanced candidate).

New exact obstruction: unconditional pairwise cross-anchor PQD between canonical reverse channels is false even under the current local majority-late/no-span endpoint inequalities. A ten-element width-three poset with connected comparability and incomparability graphs has nested endpoint `(a,b)=(5,4)`, `T={1,2}`, `U={9}`, `E=461`, and

- `N(a<b)=136`,
- `N(b<1)=152`, `N(b<2)=61`, `N(9<a)=39`, all strictly below `E/3`,
- but `N(b<2,9<a)=5`, so `5*461-61*39=-74<0`.

Exact verifier terminal marker: `POS3_CROSS_ANCHOR_PQD_COUNTEREXAMPLE_PASS`.

Second result: even granting perfect overlap between predecessor/successor channel groups, the current scalar endpoint mechanism `r>=1-2p` plus same-anchor TP2 bound `F_2(c)=2c-c^2` can force a channel only up to the threshold `c=2-sqrt(3)=0.267949...`; it cannot reach `1/3`. Therefore further correlation sharpening alone cannot close the persistent two-channel state.

Revised first essential obligation: prove a structural two-channel collapse/transport theorem using global no-balanced/corridor history, or derive a new inequality coupling the forward common-blocker term `Q` to the reverse-channel state. In particular, exploit the lead's heavy-cover/two-witness branching together with the partner's fact that any surviving incomparability leaf has a genuinely nonchain majority-facing side.

Execution context: `WITHOUT_VERIFIED_BRAIN`. No target-level counterexample is claimed; the finite witness has balanced pairs and refutes only the auxiliary cross-anchor correlation lemma.
