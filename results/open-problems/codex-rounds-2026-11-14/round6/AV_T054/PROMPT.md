# Verify: has open problem T054 been settled by the OpenAI math release?

Our row: Bulk universality and quantum unique ergodicity for random regular graphs of fixed degree
Statement: For fixed d ≥ 3, the adjacency eigenvalues of a uniform random d-regular graph on N vertices have GOE local statistics in the bulk of the Kesten–McKay law as N → ∞, and the eigenvectors are delocalized and satisfy quantum unique ergodicity.
Where it stands (our note, Nov 2026, written before we knew of the release): Bulk GOE statistics for degree growing with N (Bauerschmidt–Huang–Knowles–Yau 2017, 2020); local Kesten–McKay law and delocalization for fixed large d (Bauerschmidt–Huang–Yau, arXiv:1609.09052); edge Tracy–Widom statistics and the Ramanujan property with probability about 0.69 for fixed d (Huang–McKenzie–Yau, arXiv:2412.20263). He–Huang–Wang (arXiv:2610.08127) prove Sine_1 bulk universality (point process, gaps and fixed-energy correlations) for every fixed d ≥ 3. Quantum unique ergodicity at fixed d is open.

The OpenAI math release (github.com/openai/math, preprints dated September-October 2026, AI-generated, not refereed) has
preprints whose titles match this row:
- https://github.com/openai/math/tree/main/preprints/GOE-bulk-universality-for-fixed-degree-random-regular-graphs-September-23-2026  (title match score 59)
- https://github.com/openai/math/tree/main/preprints/Fixed-energy-universality-for-weak-Anderson-disorder-on-random-regular-graphs-October-5-2026  (title match score 32)
- https://github.com/openai/math/tree/main/preprints/Conformal-universality-of-bulk-Ising-correlations-under-weak-interactions-September-23-2026  (title match score 20)

Your job (a literature verification, not a new proof):
1. For each candidate, open the preprint itself (the folder holds paper.tex or build/paper.tex or paper.pdf; raw files are
   at https://raw.githubusercontent.com/openai/math/main/preprints/<folder>/...). Copy its main theorem statement exactly.
2. Compare it with OUR statement word by word: same model, same dimension or range, same quantity, same strength (a
   bound vs an asymptotic, a special case vs the general one). Say precisely what is covered and what is not.
3. Search for anything after the preprint: an arXiv version or exposition, a refutation, an error report, a referee or
   expert comment, a Lean formalisation (the repository's lean/ folder and docs). Record what you opened.
4. Write VERIFY.md with: the theorem quoted, the comparison, the follow-ups found, and a recommended new "where it stands"
   sentence for our row, in plain words, at most three sentences, naming the preprint by its title and date.
5. Write REPORT.md whose first line is exactly one of:
   VERDICT: SOLVED-CLAIMED <the whole statement is claimed>  |  VERDICT: PARTIAL-CLAIMED <which part>  |
   VERDICT: NOT-THIS <the preprint is about something else>  |  VERDICT: UNREADABLE <why>
   Then two or three lines of reasons. Do not judge the preprint's proof correct; you may note a step that looks wrong.
If time remains after REPORT.md, pick the single most load-bearing lemma of the preprint and check it carefully; append what
you found to VERIFY.md under "Spot check".

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/AV_T054 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/AV_T054 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 5 worker built on the latest of these. Its folder is ~/codex_op_1114r5/briefs/AV_T054 (read it, never
edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Your job for this session: take the NEXT checkable step on this problem, building on that work.
1. Five minutes at most: check whether anything after the earlier report changes the picture. If the problem was
   solved elsewhere, write SOLVED_ELSEWHERE.md (reference, arXiv id, what exactly is proved) and REPORT.md, then stop.
2. First re-check the earlier result: re-derive its main claim or re-run its computation an independent way, and
   write in LOG.md whether it holds. If it does not hold, that finding is your result.
3. Then choose ONE piece that extends it: the next step its report names, a wider special case, a sharper constant,
   more cases computed, the missing lemma. Write the choice and why in LOG.md first, then do it. A proof goes in
   PROOF.md with every step written out; a computation is a script in this folder with the command and output in LOG.md.
4. Try to break your own result: re-derive every load-bearing number a second way; look for the case you miss.
5. Finish with REPORT.md: first line exactly one of  VERDICT: PROVED <what> | VERDICT: PARTIAL <what> | VERDICT: COMPUTED
   <what> | VERDICT: NO PROGRESS <why> | VERDICT: EARLIER RESULT WRONG <what> . Then what is new beyond the earlier
   report, the commands, what failed, what you are unsure of, and what the next worker should do.

Rules (the author's standing laws):
- Work only inside this folder. Read anything, but never edit files elsewhere, never use git, never push, post, email or
  create accounts. Nothing you write leaves this folder except when the coordinating agent copies it.
- Compute: every program you run stays under 1 GB of RAM, one thread (set OMP_NUM_THREADS=1), runs under `nice -n 15`,
  and finishes within 20 minutes per run. No GPU, no MLX, no torch. This Mac is shared; never fill it.
- Literature: use the web search tool. Cite only papers you actually opened, with the authors exactly as on the paper or
  its arXiv page. Never invent a reference, a number or a step.
- Save as you go: append to LOG.md after every step (what you did, the command, the output that matters). The account's
  weekly allowance runs out within hours and the session may stop at any moment; LOG.md is what survives.
- Write plainly, like a working mathematician: no hype, no talk about yourself or the process inside PROOF.md.




----- earlier REPORT.md -----
VERDICT: PROVED relative QUE for prescribed k-sets when k/[L^2(M+log N)] tends to infinity, under all-eigenvector delocalization and label symmetry
The round-4 claim survives independent derivation and its unchanged audit. New: a variance-sensitive Bernstein/net argument gives failure <= epsilon + 2N 9^M exp[-k^2 r^2/(8L^2(min(k,N-k)+kr/6))], where M bounds eigenspace dimension; M<=L^2 improves the previous sufficient threshold L^8 log N to L^2(L^2+log N). Every unit vector in repeated eigenspaces is included. PROOF.md contains all steps and a simple-spectrum specialization.
The release assessment remains PARTIAL-CLAIMED: OpenAI's September 23 clean GOE manuscript explicitly claims bulk eigenvalue universality, without spatial QUE in its main theorem; no new settlement, matching Lean proof or specialist validation was identified. VERIFY.md contains exact original theorem quotations for all three candidates and the updated row sentence. No judgment on the full OpenAI proof or novelty of the corollary is made.

Commands: `OMP_NUM_THREADS=1 nice -n 15 python3 audit_bernstein.py` passed 6,132 subset instances, 595 tail comparisons, 189 exact mgf comparisons, 3,465 smoothing identities, 3,654 constant/inversion checks, and 69,680 quadratic-form comparisons across 536 eigenspace compressions; runtime 1.869 s, peak RSS 14.9 MB, one thread, niceness 20. Round-4 audit rerun via runpy also passed; exact executable command is in LOG.md.
What failed or remains uncertain: no check failed. The method does not cover graph-dependent sets, singleton QUE, or simultaneous control of every set. A block-Walsh counterexample shows failure at k=L^2 with probability tending to e^(-1). Optimal powers of log N and the OpenAI proof remain unresolved; finite audits supplement the proof and do not prove its asymptotic statements.
Next worker: sharpen the eigenspace-net step using a proved matrix concentration inequality for sampling without replacement, aiming to replace the M cost by a logarithmic factor; otherwise specify the intended graph-dependent QUE observable class before claiming more.

Task: “Verify: has open problem T054 been settled by the OpenAI math release?” — session start 2026-11-15T07:23:36.996674+04:00
