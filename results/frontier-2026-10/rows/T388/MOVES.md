# T388 moves on the obstruction

- 2026-10-16, literature (agent A): dossier written; the d^2 rate may belong to batch or multi-pass methods, since online SGD
  at information exponent 4 needs about d^3.
- 2026-10-31, result (agent B): the statistic M_n = (1/n) sum (|x|^2 - d - 2) x x^T has mean kappa u u^T exactly, and its
  bottom eigenvector finds u at n of order d^2; a one-pass Oja version does too (T388_partial_trace_d2.md, t388.py,
  t388_oja.py).
- 2026-11-04, audit (agent C): identity confirmed; the statistic is FOBI (Cardoso 1989); the offline threshold is
  n > 2(d^2 + 6d)/kappa^2 with overlap^2 = 1 - 2(d^2 + 6d)/(kappa^2 n), checked at d = 16, 32, 64; with a decaying step
  one pass costs about 4 times the offline sample size at d = 32, not 16 (AUDIT_agent_C.md).
