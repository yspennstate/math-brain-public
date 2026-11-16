---
name: cn0533_converting_brw_two_generation_concavity_no_monotone_coupling_2026_11_16
description: "CN0533 Deijfen-Vilkas converting BRW: what's proved? Exact gen-2 pgf identity, concave in p, nonmonotone witness F(p) max at 412/847, no coupling monotone in p (audit holds); finite-time only, novelty unchecked, no paper yet - follow-up OPC31F on a second machine"
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T14:40:51+02:00
  status: provisional
  evidence: "Mac1 the worker folder"
---

Status: provisional. The mathematics is audit-held; novelty and paper-worthiness are open.

CN0533 asks, for the Deijfen–Vilkas converting branching random walk (arXiv:2203.14166, ECP 28, 2023), which conversion probabilities p give almost-sure infinite blue expansion. Codex brief OPC31 (a second machine, 16 Nov) did not answer that. AUD_OPC31 confirmed what it did prove (5 of 7 claims hold; the other 2 are scope statements):

- With exactly nearest-neighbour jumps and blue-priority ties, there is an exact pgf identity for the expected number of blue sites through generation two.
- Under the catalogue's offspring assumptions, that expectation is strictly concave in p.
- An explicit witness: binary offspring, uniform nearest-neighbour blue jumps, red weights (3,2,2,2)/9. It gives F(p) = 472835/110592 + (721/20736)p − (5929/165888)p², maximised at 412/847, so F is not monotone in p. Blue is strictly faster than red in the +e1 direction.
- So no coupling nests the blue sets monotonically in p (the expected cardinality would have to be monotone). A monotone-coupling argument therefore cannot settle CN0533.

Limits:
- Finite time only; nothing follows for the infinite-expansion probability.
- The audit's boundary checks show the identity fails for red-priority ties and for holding steps.
- Only arXiv v1 of the source was read, and no forward-citation census was done.

Decision (16 Nov 14:3x): no paper yet. This is not a "proof with no paper" for CN0533, and the "what existed before / what is new" paragraph cannot be written until novelty is checked. Follow-up brief OPC31F is queued on a second machine. It reads the published version and runs the citation census, then pushes past generation two: generation n, a quantity tied to the expansion event, or no monotone coupling under the full catalogue hypotheses. Write a paper only if OPC31F confirms novelty and gets beyond two generations.

Files: a worker folder (PROOF.md, CLAIMS.md, exhaustive.cpp, verify.py) and AUD_OPC31/AUDIT.md.
Related: [[open_problem_catalogue_1128_probability_networks_computation_2026_11_16]], [[catalogue_row_already_solved_in_store_recall_first_2026_11_16]].


Update 16 Nov 15:1x (OPC31F report read, a worker folder): the follow-up read the published ECP 28 (2023) article 15 (Chalmers repository scan, OCR) and arXiv v1, the only arXiv version. It proved a stronger obstruction: for every positive offspring pair and every full-support exactly-nearest-neighbour jump pair, the blue-set laws at p=0 and p=1 are stochastically incomparable under every fixed local tie rule. Two cylinder gaps are explicit, for example P_1(2e in B_2)-P_0(2e in B_2)=f_b(1-b_e)[1-f_r(1-r_e a_+)]>0, and they are 959/9216 and 847/9216 on the OPC31 witness. It also extends to prescribed finite supports by epsilon perturbation, and gives an all-horizon delay statement (P_0(x_n in B_n)>0 while P_1(x_n in B_{n+1})=0). Precedents: Candellero-Stauffer (EJP 29, 2024, hostile FPP is not monotone) and Finn-Stauffer (AAP 32, 2022, the natural conversion coupling fails). Those are different models, but "competition can be nonmonotone" and "the natural coupling fails" are already known. Citation census: 2 citing papers found (Ghosh-Jahnel arXiv:2512.09153; Zhu-Hou-Zhang AIMS Math 11, 2026); neither addresses p-monotonicity, and Scholar was unreachable, so the census is incomplete. Verdict, kept: no paper. The results are elementary and finite-time only, and novelty is unconfirmed. Reopen only with a complete citation census plus an infinite-time statement. Codex workers were not re-queued on this line.
