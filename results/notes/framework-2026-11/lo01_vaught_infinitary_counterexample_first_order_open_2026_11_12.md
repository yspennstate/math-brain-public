---
name: lo01_vaught_infinitary_counterexample_first_order_open_2026_11_12
description: "Vaught's conjecture refuted (arXiv 2610.15217)? Only for L_omega1,omega; rests on Lean, whose statement reads right; first-order form stays open"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T01:11:56+02:00
  status: provisional
  evidence: "paper text and three Lean files read with the library definitions; nothing built; one arXiv search"
---

Row LO01 (Vaught's conjecture), 12 Nov 2026.

arXiv 2610.15217v1 (Ackerman, Freer, Knight, 10 Oct 2026): a sentence of L_{omega_1,omega} in a countable relational language with exactly aleph_1 countable models and no perfect set of non-isomorphic models. This refutes the infinitary form and the topological Vaught conjecture for S_infinity. It does NOT refute the first-order conjecture; the paper and the repository both say so. Knight's 2002 first-order claim was never accepted.

The written paper is not a complete proof: three propositions (4.32, 4.34, 4.35) are stated with proofs omitted and "many details are elided"; the claim rests on the Lean development (github.com/cameronfreer/vaught-conjecture-counterexample, 765 Lean files, pinned library cameronfreer/infinitary-logic 004f638).

What I read in Lean (not built): the main theorem is HasThinAlephOneSpectrum densitySentence, i.e. the isomorphism classes of models coded on N number exactly aleph 1 and there is no nonempty perfect set of codes of models with pairwise non-isomorphic points; the infinitary connectives are indexed by N, so it is L_{omega_1,omega}. No sorry/admit/axiom in the three files read; README lists the three standard axioms. The README's own limits: the theorem is for the repository's sentence, which is not identified with the paper's class of strongly coded templates.

Not checked: the build, the topology of the code space, the proofs, the Palomar/Comparator record, the mathematics of the paper.

Method worth keeping: for a result that rests on a formalization, the cheap useful check is the statement, read down through its definitions to the library (what is counted, what "perfect" quantifies over, what the logic's connectives are indexed by) and the repository's own list of what it does not cover. That takes minutes and catches the usual failure, a theorem that proves something else.

Files: 06_math_research/lo01_vaught_agent_2026_11_12/LO01_CHECK.md. Row proposal: keep the row, stated as the first-order conjecture. Related: [[it01_mds_even_characteristic_preprint_last_section_checked_2026_11_12]], [[al04_kaplansky_zero_divisor_positive_char_finite_parts_recomputed_2026_11_12]].

