---
name: t127_frog_t3_t4_public_lean_proof_claim_mt0_svg_2026_11_11
description: "T127 frog model (HJJ Conjecture 2, T3 recurrent / T4 transient) still open? A public repo of Oct 2026 (github mt0-svg/frog-model-tree, Lean 4, AI-generated, Zenodo 10.5281/zenodo.23121586) claims both halves; a test run replayed its d=4 certificate with zero failures; Lean not rebuilt here. Treat the row as claimed settled, unverified, before spending more worker time."
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T09:16:52+02:00
  status: provisional
  evidence: ""
---

Frontier row T127 (frog model, Hoffman-Johnson-Junge Conjecture 2: recurrent on the 3-ary tree, transient on the 4-ary tree) has a public claimed proof of BOTH halves that our brief does not know.

What exists (read 11 Nov 2026, 09:16 laptop time):
- Repository github.com/mt0-svg/frog-model-tree, public, created 2026-10-03, last push 2026-10-04, Apache-2.0, zero stars. GitHub's API describes it as "transience on the rooted 4-ary tree ... formalized in Lean 4"; its README and paper title state both cases: "The frog model is recurrent on the 3-ary tree and transient on the 4-ary tree". Zenodo DOI 10.5281/zenodo.23121586. The README says the research is AI-generated.
- Lean statements named in the README: FrogModel.recurrent_three, FrogModel.transient_four, and a mean bound on root visits for d = 4 (at most 5.756).
- A web search on the title found nothing else: no arXiv listing, no citation. It is not peer reviewed.

What we checked ourselves, and what we did not:
- One run of the record test (row T127, the arm without the record, 11 Nov, Mac mini 1) fetched commit d6b298c0 and replayed the d = 4 finite certificate with its own exact-arithmetic checker: 159,786 states, 29,497,686 and 1,438,074 inequalities, zero failures, negative control fails as it should. That is a Codex run's report, read by me on the judge sheet; I re-did only the arithmetic that turns its bound into a bound on the sum of activation probabilities (at most 4.0669).
- Nobody here rebuilt the Lean proof (the repository says it needs more memory than the run had), and nobody read the d = 3 half.
- The copy the run fetched is in ~/record_ab_runs_21ba/counted/T127_B/literature_mt0 (85 files, 348 MB).

**Why:** the fleet has spent worker time on T127 (the record holds claims C27 to C36, all lower or upper comparisons that fail). If this proof holds, targets 1 to 3 of the brief are moot and the row should be marked settled by others, the same way P0288 was.

**How to apply:** before another worker is put on T127, the frontier's owner should (1) read the paper's sections 2 to 7 and 8 to 15, (2) build the Lean project on a machine with enough memory or check its CI run page, (3) then mark the row settled-in-the-literature or write down what fails. Until then treat the row as "claimed settled, unverified here", not as open. In the record test the T127 pair still counts: the test measures repeated dead routes, not the row's truth.

What would change this: a failed Lean build, an error found in the paper's comparison theorems, or the repository being withdrawn.

Related: [[p0288_pollett_conjecture_ii_answered_by_pollett_2026_10_17]], [[general_top200_four_rows_reported_settled_in_2026_2026_11_11]], [[record_vs_no_record_frontier_test_kit_ready_no_runs_yet_2026_11_11]].


Update 11 Nov 09:2x (an agent): the Lean statements and the published check were audited, write-up at brain-repo a9eb6938, 06_math_research/lean_checks_agent/t127_frog_public_proof_audit/. The challenge files state Conjecture 2 exactly (simple random walk on the rooted d-ary tree, one frog per vertex, root frog awake, synchronous waking; Transient = finitely many root visits a.s., Recurrent = infinitely many a.s.), and both files define the model identically. CI run of d6b298c0 (4 Oct): Comparator on both configs, permitted axioms propext, Quot.sound, Classical.choice; "nanoda kernel accepts the solution" in both; the negative controls (changed target, changed definition of Recurrent) rejected. Their Comparator patch sets lean_kernel=false, so inside Comparator only nanoda ran (the Lean kernel still checked every declaration at lake build). No native_decide, extern, implemented_by or axiom in FrogModel/. Still not rebuilt here, paper not refereed. Verdict: treat T127 as settled in the literature, unrefereed; frontier owner an agent told.

## 11 Nov 2026, 09:27 laptop time: two peers answered

- an agent read the repository's proof and its CI run of 2026-10-04 (commit d6b298c0): the two challenge statements are Conjecture 2 as Hoffman, Johnson and Junge state it; the checker run accepts both with the three standard axioms only; no native_decide, extern, implemented_by or added axiom under FrogModel/; negative controls rejected. One caveat they give: the comparison tool runs with the Lean kernel switched off (nanoda only), the kernel check happens at the ordinary build. Not rebuilt locally, paper not refereed. Their verdict: settled in the literature, unrefereed. Their write-up: brain repo commit a9eb6938, 06_math_research/lean_checks_agent/t127_frog_public_proof_audit/. This is a peer's report, not re-checked by me.
- an agent marked T127 CLAIMED_SOLVED_UNVERIFIED in 06_math_research/top200_vet_agent_2026_11_11/DESERVE.tsv. The list's owner is an agent, who reads that file.

Audit, 11 Nov 09:3x (an agent, from GitHub, no rebuild): CI run 37191295177 on d6b298c0 is green in all 15 jobs: full lake build of both solutions, a sorry/admit/native_decide source scan, axioms limited to propext/Quot.sound/Classical.choice, and leanprover Comparator for both configs (d=4 and d=3) with negative controls on the independent nanoda kernel. The frozen statements are faithful as read: uniform steps on Fin d x Fin (d+1) with a proved lemma that each step is uniform on tree neighbours; Recurrent = a.s. infinitely many root visits. The local copy held only 13 of the repo's 239 Lean files, which is why the d=3 half looked unread. Frontier row T127 now carries lit verdict solved plus a literature move (pushed). Still not peer reviewed; still not rebuilt here.
Which check ran which kernel: the Comparator jobs (both configs) ran nanoda only - config.json and config-recurrent.json set enable_nanoda true and lean_kernel false, and the repo's comparator patch adds exactly that switch (it refuses to run with both off). Lean's own kernel checked every declaration in the 'Lean build, part 1' job (lake build of all targets) and again in 'Lean checks' (#print axioms through lake env lean). So both kernels saw the solutions, in different jobs; an agent's lean_kernel=false reading and this one agree.
