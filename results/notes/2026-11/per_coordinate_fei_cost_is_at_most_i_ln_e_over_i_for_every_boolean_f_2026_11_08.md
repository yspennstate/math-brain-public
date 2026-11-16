---
name: per_coordinate_fei_cost_is_at_most_i_ln_e_over_i_for_every_boolean_f_2026_11_08
description: "[VERIFIED] FEI T021 8 Nov 02:5x: R_i <= I_i ln((1-I_i)/I_i) for I_i<=0.2029 and R_i <= I_i ln(e/I_i) always, any Boolean f, by Jensen against Parseval; constant in [0.396,1]"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T02:58:08-05:00
  status: provisional
  evidence: ""
---

For any Boolean f and coordinate i, with a_S = fhat(S), b_S = fhat(S+i) (i not in S), R_i = sum K(a^2,b^2), K(s,t) = min ln(max/min): on the pairs where b^2 < a^2, Jensen with weights b^2/I_T gives sum b^2 ln(a^2/b^2) <= I_T ln((1-I)/I_T) since sum a^2 <= 1-I by Parseval; the other pairs give at most b^2/e each. Hence R_i <= max_x [x ln((1-I)/x) + (I-x)/e], which is I ln((1-I)/I) for I <= 0.2029, and R_i <= I ln(e/I) always. No monotonicity or read-twice needed. G(c,1) attains 0.396 I ln(1/I), so the ln(1/I) order is tight; the constant lies in [0.396, 1]. It supersedes my 02:2x entropy lemma (R_i <= I(ln(1/I)+Ent(g_i)+1/e)), which bounded each a_S^2 by 1 separately and lost an unbounded factor. The lesson: when a per-term bound uses a coefficient <= 1, try Jensen against the Parseval sum first. Checked on 307 functions, max R/bound 0.855 (check_jensen.out). Files: the private brain repository, 06_math_research/frontier/T021/fei4_agent_2026_11_08/. Probably known in the FEI literature; not searched. Related: [[monotone_read_twice_dnf_with_wide_terms_has_an_unbounded_coordinate_2026_11_08]].
