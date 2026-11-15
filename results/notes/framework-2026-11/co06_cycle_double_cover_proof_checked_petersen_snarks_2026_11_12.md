---
name: co06_cycle_double_cover_proof_checked_petersen_snarks_2026_11_12
description: "Cycle double cover conjecture proved (July 2026) by an F_2 linear system on a nowhere-zero F_2^3-flow: every step read, system solved and cover tested for all 28560 flows of the Petersen graph and on snarks; remove the row"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T01:38:58+02:00
  status: verified
  evidence: "06_math_research/co06_cdc_agent_2026_11_12/CO06_CHECK.md, co06_check.out; push e65cdd837979a7ad8a7904848ca5a33587eabe84"
---

Row CO06 (cycle double cover conjecture), 12 Nov 2026.

Proved in July 2026 (credited to GPT 5.6; expositions arXiv 2607.15399 Geelen, 2607.16356 Oum). Inputs: reduction to cubic graphs and Jaeger's nowhere-zero F_2^3-flow f.

The proof in one paragraph. At a vertex with edges a, b, c set alpha_{v,a} = f_b, alpha_{v,b} = f_c, alpha_{v,c} = f_a. Look for potentials p : V -> F_2^3 so that every edge e = uv carries the same pair of colours {p + alpha, p + alpha + f_e} from both ends; that is the F_2-linear system p_u + p_v + z_e f_e = alpha_{u,e} + alpha_{v,e}. If unsolvable there is a certificate y : E -> F_2^3 with sum of y at each vertex 0, f_e . y_e = 0, and sum (alpha_u + alpha_v) . y_e = 1. Then alpha_{v,e} . y_e is one value delta_v per vertex; where delta_v = 0 an even number of the y_e are nonzero; so the number of edges between {delta = 0} and {delta = 1} is even, and that number is the sum that should be 1. The cover has at most 8 even subgraphs.

Checked: every step by hand; by computer without the proof: the system solved and the cover tested directly for all 28560 nowhere-zero F_2^3-flows of the Petersen graph, all flows of K_4, K_{3,3}, the prism and the cube, random flows on flower snarks J3, J5, J7 and 40 random cubic graphs; a control with labels that are not flows fails every time.

Technique card: existence of a combinatorial structure as solvability of a linear system over F_2 built from a flow; prove solvability by taking the dual certificate and reading it as a parity count across a vertex cut. Same family as [[co08_erdos_sos_counting_proof_checked_small_graphs_2026_11_12]]: a short argument that the standard approaches (minimal counterexamples, snark structure) never looked for.

Still open after it (Oum, last section): 5-cycle double cover, orientable 5-cycle double cover (implies the 5-flow conjecture), strong embedding for non-cubic graphs, Bondy's small CDC, Berge-Fulkerson. Files: 06_math_research/co06_cdc_agent_2026_11_12/ (CO06_CHECK.md, co06_check.py, co06_check.out). Row proposal: remove; vet the orientable 5-CDC conjecture for the slot.

