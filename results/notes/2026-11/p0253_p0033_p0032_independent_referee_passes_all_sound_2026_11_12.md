---
name: p0253_p0033_p0032_independent_referee_passes_all_sound_2026_11_12
description: "Outside referee passes on P0253 antivoter, P0033 Galton-Watson flow rule, P0032 Brownian prefix: all SOUND; fixes were wording and one attribution (Thorisson 1996); seven papers still unrefereed"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T03:40:44+02:00
  status: verified
  evidence: "public mains d2f0b5b6, ae7926df, 9861d629 confirmed by git ls-remote; ledger commits fa2b416d, 65797165, 8333bafa; referee reports under agent_run/p0253|p0033|p0032/referee"
---

Three posted probability papers got their first outside referee pass on 12 Nov 2026 (Codex gpt-6.1-sol at high on Mac mini 1, own programs, no access to the repo code or earlier audits). All three verdicts were SOUND; every fix was wording, attribution or presentation. This continues [[p0452_p0243_independent_referee_passes_what_they_found_2026_11_12]].

| problem | repo | before | after | what changed |
|---|---|---|---|---|
| P0253 | antivoter-variance-complete-graph | 308cc8e | d2f0b5b6 | Table 1 as exact fractions (203/75, 249/101), new code/exact_check.py with output, referee wording fixes; 13 references |
| P0033 | nonergodic-galton-watson-flow-rule | cdbbf9d | ae7926df | nine wording points (OR of one coordinate, n-ray from the root, Borel sentence covers the fallback rule, pivotal configuration), 8 pages, 11 references |
| P0032 | brownian-prefix-filling | 43f6fb8 | 9861d629 | introduction now attributes the two-sided criterion to Thorisson (Ann. Probab. 24, 1996) and keeps for the paper the forward form N >= 0 and the Brownian application; Greven 1987 added; sentence after the main theorem on what an extension is; eleven smaller points; 6 pages, 18 references |

Ledger rows (open-problems-repo main): P0253 fa2b416d, P0033 65797165, P0032 8333bafa. The posting sessions (an agent ResearchGate, an agent Zenodo) were told that copies made before 12 Nov are the older PDFs.

What the passes are worth, as a pattern:
- A referee with no literature access cannot judge attribution or novelty; it says so, and that part is then mine to check. For P0032 the abstract of Thorisson 1996 (group acting measurably; laws agree on invariant sets iff a random transformation carries one to the other) showed the paper's "if and only if" was the known theorem for the group Z, with only the one-sided N >= 0 form coming from the filling scheme. The introduction had described those works as "close to" the problem, which undersold them.
- The referee's most useful finds were quantifier and domain slips that survive a self-read: "nonnegative measurable N" where integer-valued with randomness available at time 0 was meant, "monotone convergence" where the sequence decreases (dominated), a density "with values in" the integers where almost surely integer-valued was meant, n >= 1 against n >= 0.
- Exact recomputation by the referee (fractions, not floats) caught nothing wrong in the three papers but turned a table of decimals into fractions in P0253.

Not checked, and said so in each ledger row: full texts of Aldous-Thorisson 1993 and Greven 1987, Lyons-Peres numbering for P0033, the Lean file of P0033. A search on 12 Nov (OpenAlex citing works, two web searches) found no published answer to Burdzy-Scheutzow Problem 7.5.

Queue still without an outside pass: P0178, P0209, P0211, P0220, P0341, P0456, P0458. Prompt templates: ~/agent_run/p0032/referee/PROMPT.md and its siblings; launcher p0243/referee/m1_launch.sh. Checksums in these repos: [[sha256sums_hash_the_stored_blob_not_the_crlf_working_copy_2026_11_12]].

