# T390 moves on the obstruction

- 2026-10-16, literature (agent A): dossier written from the arXiv abstracts; see FRONTIER and TARGETS.
- 2026-10-18, result (agent A): target 1 numerically. For 1/2 N(-m,1) + 1/2 N(m,1) the efficiency of score matching
  against maximum likelihood stays near 1 for the means but decays like e^(-m^2/2) for the weight; denoising at a noise
  level of order m restores it (are_dsm.py, are_dsm_weight.py and their outputs).
- 2026-10-31, result (agent B): closed form for the weight, ARE(m) ~ sqrt(2 pi) e^(-m^2/2)/m (1 - c/m^2) with c read as
  about 2.5 (T390_weight_are_asymptotic.md, t390.py).
- 2026-11-04, audit (agent C): leading term confirmed; c = 4/3 + pi^2/8 = 2.56703 exactly, and the next coefficient is
  d = 58/9 - pi^2/2 + 5 pi^4/128; the noise table matches to every printed digit; the sandwich regularity holds on a
  compact parameter set (AUDIT_agent_C.md).
