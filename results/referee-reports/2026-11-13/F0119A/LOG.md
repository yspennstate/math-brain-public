# F0119 work log

Task clock: 2026-11-13 08:43 Asia/Tbilisi (first directly observed session clock;
the prompt timestamp was unavailable).
Request: “Open problem F0119” — determine reconstruction for the three-state
Potts broadcast channel, literature first, then reduction/proofs/computation if
the problem remains open.

## 2026-11-13 08:44 +04:00 — orientation and scope

- Read the startup memory index, compute state, and mesh protocol. The task's
  explicit instruction to work only in this directory supersedes global
  instructions to mutate shared brain/mesh/checklist stores outside it. This
  log is the local task record; no shared stores have been changed.
- No subagents, publication, pushes, or background services. Source PDFs will
  be processed from memory through pdftotext, never saved to disk. Only plain
  text source files are retained.
- Compute state: warn / owner_away_open, existing CPU saturation; use one
  process at nice 10 and single-thread numerical libraries for our work.
- Search found a September 25, 2026 OpenAI preprint claiming all-degree,
  both-sign sharpness. This is a lead, not an accepted resolution yet.
- Bibliographic correction: arXiv:0905.3797 is unrelated quantum physics;
  Sly's Potts paper is arXiv:0811.1208.

Status: working on source extraction and literature audit.

## 2026-11-13 08:49 +04:00 — primary sources read

- Saved all 16 pages of arXiv:math/0406446v1 as sources/mossel2004.txt.
  Read Sections 2–4 and the main part of Section 5 through PDF page 9.
  Subsections 5.1–5.2 continue on page 10 and were read subsequently,
  completing the requested Sections 2–5.
  Definition 2.1 is on pages 2–3; Proposition 2.1 on page 3; Theorem 4.1 on
  pages 6–7; equation (8) on page 7; Problem 1 on page 8; revealing-color
  non-reconstruction bound on page 9.
- Exact convention: off-diagonal delta = epsilon, diagonal 1-2 epsilon,
  lambda = 1-3 epsilon, epsilon in [0,1/2], lambda in [-1/2,1]. The survey
  assumes ergodicity; epsilon=0 is a trivial deterministic extension.
- Saved Sly arXiv:0811.1208 (40 pages). Its Theorem 1.1, PDF page 4, covers
  BOTH ferromagnetic and antiferromagnetic channels for sufficiently large
  degree, including equality. No explicit small-degree cutoff is supplied.
- Saved the actual 60-page OpenAI September 25, 2026 manuscript, not just
  its abstract. Theorem 1.1, page 3, states the all-degree, both-sign answer.
  Proof assembled on page 33 from Propositions 2.7, 3.3, and 6.3.
  It is a public preprint; journal acceptance has not been established.
- PDF bytes were piped from memory to pdftotext. Source hashes and page
  counts are in data/*.metadata.json. No PDFs or images were retained.
- The first three launches printed a macOS sandbox error when nice tried
  to alter the inherited priority. os.getpriority confirmed that the shell
  already has nice=10. The fetcher now checks that value directly.
- Continuing the requested named-literature search and checking the new
  manuscript's verification package before choosing the final status.

## Literature audit and verification completed

- The public 2026 preprint is pinned to commit
  adc7f1241b42e322a6451854ab7e4b4c146bf78a. Its pinned PDF hash equals the
  original main-branch download. Provenance is in data/resolving_source.json.
- Searched the requested authors/titles, small degrees, both signs, 2011–2026
  work, and possible corrections/counterexamples. Retrieved primary texts
  for all identifiable relevant leads; no joint Chen–Gu reference was invented
  from the ambiguous author fragment. LITERATURE.md records exact locations.
- Detected and documented two misleading preprint statements by reading their
  proofs: Mossel–Peres Theorem 1.6 is a census theorem, and Bhatnagar–Maneva
  Theorem 12(2) establishes non-reconstruction at lambda <= .555, despite a
  missing “non-” in that item's statement.
- Vendored the 2026 certificate programs under code/literature_verification/.
  Their SHA-256 digests match Appendix D, page 49, exactly.
- The first replay-driver attempt failed before running certificates because
  macOS/Python rejected the requested finite resource limit. No mathematical
  test failed. The final driver uses sequential subprocesses, single-thread
  environment settings, a 600-second timeout per execution, and records child
  peak RSS. The code's finite allocation bounds were inspected before replay.
- Replayed pair.py, interval cases 0 and 1, and grid case -1 successfully.
  Interval totals were exactly 414080 and 756096; grid stopped exactly at 162.
  Both C++ programs used assertions and undefined-behavior sanitization.
  A second replay followed a stricter log-validation change; it also passed.
  Final replay peak child RSS: 153206784 bytes. The earlier replay peaked
  at 158171136 bytes. Both were far below 4 GB; inherited nice was 10.
- Did not rerun Poisson-only cases and did not describe this subset as the
  complete package's 37-record replay. No new proof or population-dynamics
  work was started after the all-degree theorem was identified and checked.
- Checked the parameter translation in two ways: exact rational matrix action
  on the mean-zero eigenspace, and an independent polynomial expansion of KS.
  Also checked radical endpoints to 60 digits for b=2..6. These are theorem
  evaluations, not empirical threshold estimates.
- REPORT.md now begins RESOLVED_IN_LITERATURE, with an explicit public-preprint
  qualification, complete parameter region, definition matching, proof
  dependencies, and verification limits. No journal-acceptance or independent
  end-to-end proof claim is made.

Task result: “Open problem F0119” — resolved in a public 2026 preprint;
regular-tree certificates replayed; sources, report, code, and logs saved here.
