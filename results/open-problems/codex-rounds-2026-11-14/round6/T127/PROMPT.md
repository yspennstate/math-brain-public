# Open problem T127: Recurrence of the frog model on 3-ary and 4-ary trees

Statement: On the rooted d-ary tree, place one sleeping frog at each vertex and an active frog at the root; active frogs perform independent simple random walks and wake every frog they visit. Decide for d = 3 and d = 4 whether the root is visited infinitely often almost surely (recurrence) or finitely often (transience).

Caveat: Hoffman, Johnson and Junge settled d = 2 and d ≥ 5 and left the two middle cases; the problem is to find the transition.

Source: C. Hoffman, T. Johnson and M. Junge, Recurrence and transience for the frog model on trees, Ann. Probab. 45 (2017)

Where it stands (checked by us, Nov 2026): Recurrent for d = 2 and transient for d ≥ 5 (Hoffman–Johnson–Junge, arXiv:1404.6238); with Poisson(μ) sleeping frogs per site the critical μ is known to grow linearly in d (Johnson–Junge, Electron. Commun. Probab. 21 (2016)). Mathews (arXiv:2309.14443) still treats d = 3 and d = 4 as known only from simulation. With one frog per site, d = 3 and d = 4 are open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T127 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T127 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T127 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 5 worker built on the latest of these. Its folder is ~/codex_op_1114r5/briefs/T127 (read it, never
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
VERDICT: PARTIAL retrieved and audited the formal model of the claimed outside solution

Round 4's retrieval claim holds: the paper and statement map remain
accessible. The new step obtains the formal model and target files that
round 4 could not access, pins them to a commit, and checks applicability
to T127. PROOF.md derives the uniform walk law, activation rule and visit
event from the definitions, and handles an additional sleeping root frog.

The claimed outside answer remains recurrence for d=3 and transience for
d=4. Exact attribution and references are in SOLVED_ELSEWHERE.md. This
session does not independently certify the complete solution. Under step 1,
the literature branch ends further original-model research; no new packet
refinement or Bernoulli computation was undertaken.

The GitHub connector succeeded where raw web retrieval failed. Fourteen
source files are saved under outside/, including the formal definitions,
both target and challenge files, paper, citation metadata, input manifest,
license and historical verification records. outside_manifest.json records
their URLs, Git blob identities and fixed commit
d6b298c0100af57a8f46f8314eca8bf8f7eb4693.

Reproduce the local source checks:
```
OMP_NUM_THREADS=1 nice -n 15 python3 audit_sources.py > audit_sources_output.txt 2>&1
```
Exit 0; all 14 blob hashes match. Thirteen shared definitions match the
d=4 challenge, twelve match the d=3 challenge, and the recurrence predicate
matches separately. The four inspected development files have no executable
sorry, axiom or native_decide tokens. These are finite source checks, not
verification of the imported proof graph. Peak RSS was 18497536 bytes and
runtime below one second. The sandbox denied the requested nice adjustment;
the denial is retained in the output. No heavy computation was run.

What failed: raw web retrieval of the formal files and the Zenodo record.
The first source-audit run expected a Transient definition in the recurrence
challenge, which intentionally omits it; the audit was corrected. Saving
the archive initially added a terminal LF to each source; the script removed
it only after checking that removal recovered the exact advertised blob.

Uncertainty: no Lean build, comparator run, certificate replay or audit of all
imported modules was performed. The saved historical records are not a fresh
verification of the pinned tree. The complete outside argument therefore
remains unverified here. The earlier Bernoulli results were read but not
rerun under the step-1 stopping branch; nothing here contradicts them.

Next worker: use the now-local formal sources, not another retrieval-only
session. Inspect the imported assembly/checker arguments and obtain the
three inputs named in outside/ASSETS.md. A complete formal replay needs a
separately authorized environment: the recorded comparator used more than
1 GB and more than 20 minutes. Smaller checker or source audits may fit the
current limits. Keep source-reported PASS distinct from a reproduced PASS.

Task: “take the NEXT checkable step on this problem, building on that work.”
— 15 November 2026, 08:25 Asia/Tbilisi.
