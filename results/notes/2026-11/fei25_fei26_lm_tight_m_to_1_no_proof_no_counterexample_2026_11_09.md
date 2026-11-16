---
name: fei25_fei26_lm_tight_m_to_1_no_proof_no_counterexample_2026_11_09
description: "[PROVISIONAL] Neither (FEI25/26): no counterexample to LM/CT on 226 pairs, max M 1-5.6e-9 where Delta/i->pi^2/2 (LM is sharp); proof stops at a Bellman bound"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T05:43:51+04:00
  status: provisional
  evidence: "workers/FEI25/REPORT.md PROOF.md; workers/FEI26/REPORT.md MAX_M_WITNESS.json; frontier T021 21c6606e4a"
---

Is the coupled lemma left open by FEI23 proved or broken? Neither (FEI25 and FEI26, 9 Nov, run side by side and blind to each other).

FEI26 hunted for counterexamples. It found none: all 226 retained dyadic path pairs pass outward certification of LM (M < 1) and of CT at every real z >= 1. The log-moment lemma is tight, though. The largest certified M is 0.9999999944126, 5.587e-9 below 1, at root influence 2.84e-14, on an inside-out path of 32,768 gates with p_j close to ((32768-j)/(32769-j))^3. Its partner is nearly constant one, at 2^-160. At that same point Delta/i = 4.9348021872, which is pi^2/2 to 8 digits. So LM is approached from below in the same limit where the reserve ratio goes to pi^2/2, and any proof of LM has to be sharp. The CT margin goes to 0 as z goes to 1 on every pair; the smallest positive breakpoint margin was 4.1e-15.

FEI25 tried for a proof. There isn't one yet. It proved a sufficient two-moment criterion: with q = sum over tau>1 of xi and J = sum over tau>1 of xi tau^2, qJ <= (2-q)^2 gives CT at every z, and q ln sqrt(J/q) <= 1 gives LM. The criterion covers 3,740 to 4,042 of FEI23's 4,050 grid pairs, depending on the version, but neither saved sharp witness, so it cannot close the case alone. FEI25 also wrote down the exact fixed-left Bellman game and found exact obstructions to tensoring the one-path marginal bounds. The open step is the continuous-state Bellman origin bound (FEI25 PROOF.md section 2).

What this means: the two-path reserve conjecture now hangs on one sharp lemma, LM, with matching numerics from both sides ([[fei24_two_path_small_influence_no_counterexample_sup_pi2_over_2_2026_11_09]]). The reduction itself is in [[fei23_two_path_reserve_reduced_to_log_moment_lemma_2026_11_09]], and the one-path floor is in [[fei19_reserve_floor_pi2_over_2_2026_11_09]].

I read the heads of both reports and have not rerun their checkers yet. Pushed to frontier T021 as fei25_two_path_ct_moment_criterion_bellman_open_2026_11_09 and fei26_two_path_lm_ct_hunt_no_counterexample_m_to_1_2026_11_09 (21c6606e4a, 64 files).

Rerun 9 Nov 05:46 (an agent) in a copy laid out like the fleet tree: FEI25 verify.py, analytic_audit.py, final_audit.py and FEI26 independent_checks.py, final_audit.py all rc 0. Every JSON they rewrite matched the originals field for field (timing fields ignored) except FEI25 FINAL_AUDIT artifact_file_count, which counts the copy's files. bellman.py itself was not rerun; its three outputs were left unchanged and verify.py read them.
