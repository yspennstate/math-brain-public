# B03 lead - durable facts

## 2026-10-11 23:2xZ (run 20261011T223500Z-claude-B03-pp-congestion)

- The 7 log k of C003 comes from three quantities that the proof bounds separately: gate labels |F(A)| log k,
  subset choice (6/5) sum_l s_l log(kappa_l/s_l), and the rank/rarity average sum_j Inf_j E_{nu_j} G_j whose
  log k is a Cauchy-Schwarz loss over the <= k pivotal pieces of d_j f (union:Gtail). Keeping them exact is
  Theorem R; C003 follows from it.
- That Cauchy-Schwarz loss is an artefact when the pivotal pieces live on disjoint Fourier supports. For
  PP_q (lines of PG(2,q)), d_j g = sum of the q+1 line pieces + r with ||r||^2 <= 2q(q+1)^2 4^{-q}, and the
  pieces overlap only at the empty set. Equal piece masses make the K_eff lemma useless here; supports, not
  masses, are what matter.
- PP_q has read q+1 in every DNF (a term covering 1_L must have positive part exactly L), yet
  H(PP_q) <= C(q) I(PP_q) with C(q) -> 2 + log2 e + K0 + 12/5 = 26.95 (C(12) = 32.4). Unbounded read does not
  force log k.
- For q >= 10 the witness of a dense in-line set uses one gate (other lines through j are non-dense with
  kappa = 1 < 11(q+1)/120), so labels cost log k once per set and subset choice costs 0; mass off the lines is
  controlled by ||r||^2 because the ideal pieces put no mass there.
- Small q misleads: at q = 2,3,4, ||r||^2/Inf_j = 2.67, 2.43, 1.78, most mass is off the lines and the realised
  Cauchy-Schwarz loss is about k. Exact H/I = 2.483, 3.198, 3.710.
- A012's activation ledger is right (exhaustive check, 1,536 assertions). Hod's 6.278 is the floor any
  read-once AND/OR constant must respect.
- The harness refuses REPORT.md from a subagent; return the report text in the structured output and let the
  coordinator save it.
