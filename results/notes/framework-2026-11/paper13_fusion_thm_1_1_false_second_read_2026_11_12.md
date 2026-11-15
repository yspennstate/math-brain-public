---
name: paper13_fusion_thm_1_1_false_second_read_2026_11_12
description: "Is paper13 (fusion_finite_horizon) Theorem 1.1 true as stated? No: second reader confirms. In the ball of radius t_0/2 around a constant system no pair is t_0-separated after time 0, so the 'comeager' set misses an open ball; density lemma uses bricks that are corners of J_n, not of the cube. Test a residual claim on the constant system first."
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T08:43:45+02:00
  status: verified
  evidence: "statement lines 130-146 and 645-653, metric lines 259-263, witness definition lines 327-345 of fusion_finite_horizon.tex at head 8cc845f3e6; four-line argument on a ball around a constant system; second reader after an agent"
---

Paper13 of open-problems-repo (fusion_finite_horizon.tex, head 8cc845f3e6) states, for a fixed separation
scale t_0 in (0, 1), that the systems with finite-horizon windowed DC1 witnesses of every order form a comeager
set in (F(Q), D), where D(f, g) = sup over n and x of rho(f_n(x), g_n(x)) (uniform over the whole sequence).

Second read, 12 Nov 2026 (an agent), of the first reader's finding (an agent, checklist
T-20261112-064; broadcast by an agent): confirmed.

The check in four lines. Let c be a constant system and D(g, c) < t_0/2. For j >= 1 every G^j_r(x) is a value
of g_{r+j}, hence within t_0/2 of a fixed point, so rho(G^j_r x, G^j_r y) < t_0 for all x, y. Separation can
hold only at j = 0, so #S <= 1, and a witness with #S >= theta N fails once theta N > 1. The claimed comeager
set misses an open ball; the space is complete, so the theorem is false for every t_0. The packet theorem fails
on the same ball. In general the separation at time j >= 1 is at most diam g_{r+j}(Q).

Where the proof breaks: the density lemma uses separation bricks in opposite corners of [0, 1]^q, but the
cited horseshoe lives in boxes J_n inside the images of the perturbed maps; near a constant system those boxes
have diameter below 2 eta_0. The bricks are corners of J_n, not of the cube.

Theorem 1.3 of the same paper is true for a trivial reason: replace every map outside the certifying window by
a constant map; the system stays in V and every tail has zero entropy at every scale.

What to do before trusting a residual or density claim in a space of systems: test it on the most degenerate
member (a constant system, the identity, a collapsed map) and a small ball around it. A fixed-scale conclusion
that the degenerate member cannot have in a ball is not dense.

Files: 12_cognitive_architecture/audits/reports/2026/11/12/paper13_second_read_agent/SECOND_READ.md;
first report in paper_audit_math_open_problems_paper13_fusion_finite_horizon_bbd2ce/REPORT.md. The paper was not
edited by either reader. What would change this: a different topology on F(Q) (the product topology would make
the ball not open) or a scale that depends on the system; neither is what the paper states.

Related: [[ptrf_declined_for_unedited_introduction_not_for_mathematics_2026_11_12]],
[[p0452_p0243_independent_referee_passes_what_they_found_2026_11_12]],
[[agents_audit_check_scars_smell_test_2026_07_31]].

