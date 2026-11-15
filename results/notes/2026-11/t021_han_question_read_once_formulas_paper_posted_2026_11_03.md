---
name: t021_han_question_read_once_formulas_paper_posted_2026_11_03
description: T021 posted 3 Nov: Han Question 3.1 (sum |f^(S)f^(S+k)| <= c I_k) is false - read-once formulas give Q_k >= L at every k; repo han-question-read-once-formulas
metadata:
  type: project
  created: 2026-11-03
  created_at: 2026-11-03T07:05:24+02:00
  status: verified
  evidence: "public repo github.com/yspennstate/han-question-read-once-formulas 07dc2aa; code/q31_check_output.txt 60/60 exact"
---

T021 posted 3 Nov 2026 (papers loop T-20261029-025, 8th row of PAPER_CANDIDATES): github.com/yspennstate/han-question-read-once-formulas, head 07dc2aa, public. Title "Read-once formulas and a question of Han on the Fourier entropy-influence conjecture". Index card in math-brain-public papers/README.md (dfa6586512). Row 8 marked POSTED.

Result: Han arXiv:2312.08271 Question 3.1 (a universal c with some k having sum_{S not ni k} |f^(S) f^(S+k)| <= c I_k) is false. Theorem: depth-L monotone read-once AND-OR formulas, fan-in <= 7, n <= 2*7^(L-1), have Q_k >= L at EVERY coordinate (min_k Q_k >= 1 + (log2 n - 1)/log2 7). Tribes give Q_k < 4 with sup 4 (Proposition 1.2); AND gives 2 - 2^(2-n) (Han's example).

Proof shape (the paper's Proposition 3.1): for h = (1-g)G on disjoint variables, g unate in k, mu = E g, beta = E G, p = (1-mu) beta: I_k(1-2h) = beta I_k(1-2g) and Q_k(1-2h) = Q_k(1-2g) + 2(1-mu) - |1-2mu| - 2p + |1-2p|. Uses only Fourier factorisation over disjoint variables, sum of G^2 = E G, and |f^({k})| = I_k for unate f. Telescoping from Q = 0 at a single variable gives the closed form 2L - 1 - 4 sum_{l<L} p_l - 2p_L + |1-2p_L|. Fan-in = least s with (1-p_{l-1})^s <= 1/4 keeps p_l in (3/16, 1/4], hence s_l <= 7 and Q = 2L - 4 sum p_l >= L.

Checks: code/q31_check.py, integer Walsh-Hadamard transform, exact rationals, 60/60 agree (AND n<=8, tribes sw<=20, 22 trees n<=20; every k for n<=14). deep_trees.py: L = 80 gives Q = 90.17, log2 n = 209. The derivation is an agent's (brain 508cb8d8); I re-derived the one-gate identity by hand and wrote my own check code.

Literature: Han v2 (10 Dec 2025) still states it open; Keller-Mossel-Schlank 2012 cited per Han's note added; GMP 2606.00246 and Li-Han 2512.03117 (withdrawn) do not answer it. FEI holds on these formulas (O'Donnell-Tan, bounded arity), so this closes only the route through Han's (3.18), not FEI; his sharper (3.17) is untouched by the paper.

What would change it: an earlier public counterexample (search 3 Nov found none), or a different normalisation in Han's (3.18) (read from v2 text: f on {-1,1}^n, I_k = sum_{S ni k} f^(S)^2, matches).

Related: [[t021_han_question_3_1_is_false_alternating_read_once_trees_2026_11_03]], [[t021_han_question_3_1_constant_at_least_4_tribes_2026_11_03]], [[t021_fei_dossier_written_li_han_2512_03117_is_withdrawn_2026_11_03]], [[t180_prophet_secretary_hardness_paper_posted_2026_11_03]].


Revision 3 Nov 07:4x (commit 3a876dc217): new Section 5 "The entropy split" - D_k(f) < (5+ln4) I_k(f) on every read-once AND/OR/NOT formula (any fan-in) at every coordinate, hence H <= (5+ln4) I there; proof = pair identity D_k = sum Phi, one-gate identity (Prop 5.3, parallel to Prop 3.1), path reduction (Lemma 5.4), two-sided bound on Phi(1,t) (Lemma 5.5), telescoping (eq. 4). Remark: ratio approaches pi^2/2 (AND+NOT path, beta = 1-delta), sharp constant open. 11 split scripts + outputs added to code/. Built 8 pp, 0 overfull, guard ok.
