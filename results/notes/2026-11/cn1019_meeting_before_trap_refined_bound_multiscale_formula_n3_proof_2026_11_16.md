---
name: cn1019_meeting_before_trap_refined_bound_multiscale_formula_n3_proof_2026_11_16
description: "[PROVISIONAL] CN1019 (ABOPS 2016 Conj 1.5, meet before hitting frozen Z >= 1/3): multi-scale chains give F -> 1/3+(2/3)sum pi^3 exactly; refined form F >= 1/3+(2/3)sum pi^3 proved for n=3, unbroken numerically n<=5; still open"
metadata:
  type: project
  created: 2026-11-16
  status: provisional
  evidence: ""
---

status: provisional

CN1019 = Addario-Berry, Oliveira, Peres, Sousi, Random walks colliding before getting trapped (arXiv:1506.07845, EJP 2016), Conjecture 1.5: X, Y rate 1, Z frozen, all from pi on a reversible chain; P(meet before either hits Z, ties good) >= 1/3?

Found 16 Nov 2026 by an agent:
- Exact minimisation over all chains: min F matches 1/3 + 2/(3n^2) for n=3..6 (Powell stalls 1e-5 above at n=7,8).
- Scale-separation limit: each merge of blocks of weights a,b lowers F by 2ab(a+b) = (2/3)((a+b)^3-a^3-b^3), so every binary multi-scale chain has F -> 1/3 + (2/3) sum pi^3. Holroyd's sharpness example (hypercube with geometric rates) is the balanced tree: limit 1/3 + (2/3)4^-n.
- D = F - 1/3 - (2/3) sum pi^3 is additive under scale-separated composition (D = D_top + sum w_B^3 D_B); D=0 for 2 states.
- Refined form F >= 1/3 + (2/3) sum pi^3 (= conditioned on not all equal at time 0, prob >= 1/3): proved for n=3 (h_z closed form; numerator of sum h_z - 1 has 25 positive coefficients); no violation at 36 fixed pi n<=5. Novelty search found no refined form or follow-up.
How to apply: evidence and a lead, NOT a solution. A proof of the general case would be new. Before any paper: first-reader audit and a fresh citation sweep (lesson from CN1014). What would change this: a negative D in dscan.py (n=4..10).
Files: results/referee-reports/2026-11-16/CN1019_meeting_before_trapped/ (01_working_note_agent_E.md, meet.py, dtest.py, dfixed.py, dscan.py, n3proof.py).
Related: [[open_problem_catalogue_1128_probability_networks_computation_2026_11_16]] [[cn1014_mlsi_complete_graph_already_solved_by_gu_polyanskiy_2026_11_16]]
