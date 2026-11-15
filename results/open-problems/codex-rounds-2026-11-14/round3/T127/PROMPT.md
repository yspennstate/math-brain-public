# Open problem T127: Recurrence of the frog model on 3-ary and 4-ary trees

Statement: On the rooted d-ary tree, place one sleeping frog at each vertex and an active frog at the root; active frogs perform independent simple random walks and wake every frog they visit. Decide for d = 3 and d = 4 whether the root is visited infinitely often almost surely (recurrence) or finitely often (transience).

Caveat: Hoffman, Johnson and Junge settled d = 2 and d ≥ 5 and left the two middle cases; the problem is to find the transition.

Source: C. Hoffman, T. Johnson and M. Junge, Recurrence and transience for the frog model on trees, Ann. Probab. 45 (2017)

Where it stands (checked by us, Nov 2026): Recurrent for d = 2 and transient for d ≥ 5 (Hoffman–Johnson–Junge, arXiv:1404.6238); with Poisson(μ) sleeping frogs per site the critical μ is known to grow linearly in d (Johnson–Junge, Electron. Commun. Probab. 21 (2016)). Mathews (arXiv:2309.14443) still treats d = 3 and d = 4 as known only from simulation. With one frog per site, d = 3 and d = 4 are open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T127 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

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
VERDICT: PARTIAL proved transience for Bernoulli(q) sleepers at q<=41/100 on the 3-ary tree and q<=33/50 on the 4-ary tree

PROOF.md gives a complete weighted three-type upper comparison, including a
coupling and the reflecting root. It retains one remembered empty child and
collisions between two frogs in a packet. Exact rational supervectors yield
finite expected root visits. The sufficient q endpoints exceed those of the
elementary branching test, 1/3 and 9/16, by 23/300 and 39/400. These are bounds
for a diluted distribution; no claim of novelty or best published constants
is made.

For one initially active root frog, with no additional root sleeper, the
proved expected-visit bounds (including time zero) are 1640000/1239 and
273700/461. An additional root frog doubles these bounds.

Reproduce with:
```
OMP_NUM_THREADS=1 nice -n 15 python3 certificate.py > certificate_output.txt 2>&1
```
The saved run exits 0. Its exact output is in certificate_output.txt and
LOG.md; all matrix and boundary data are in certificate_data.json. The script
compares the derived matrix with exhaustive one-step enumeration and uses
rational arithmetic throughout. A separate audit computes the contraction
factor from normalized slacks and checks the expectation bounds. Peak memory
was 15,351,808 bytes and runtime was under one second. The sandbox rejected
priority changes and OS memory limits; the requested nice command was used,
the script measures RSS and has a 30-second alarm, and no heavy runs occurred.

What failed: these certificates have negative slack at q=1, so they do not
settle either original one-per-site case. A simpler exploratory d=3 vector
(1,39/20,19/20) at q=2/5,t=2 also failed its D-row inequality and was not used.

Literature: within the ten-minute search, an opened primary repository and
its release notes reported a complete solution by mt0-svg, with recurrence
for d=3 and transience for d=4. SOLVED_ELSEWHERE.md preserves the reference and
the limits of verification. The actual paper and formal sources could not be
retrieved, so the claimed full resolution was not certified here. No arXiv id
was found for it. The older papers actually opened were those of Christopher
Hoffman, Tobias Johnson and Matthew Junge (arXiv:1404.6238), Poly Mathews Jr
(arXiv:2309.14443), and Samyah Ahmed and Matthew Junge (arXiv:2510.18792).

Uncertainties: the validity of the reported full solution, whether stronger
Bernoulli bounds are already published, and how much further these packet
comparisons can be pushed. No optimized threshold or obstruction for every
possible supervector was proved.

Next worker: first obtain the reported full solution and inspect its model
definitions, theorem statements and proof dependencies. If valid, both cases
of T127 are settled elsewhere. Otherwise, an available exact starting point
is the three-type matrix here; retaining the empty child on a two-frog
backward move, or tracking more than two frogs, may give stronger bounds.

Task: “push this problem forward by one checkable piece” — 14 November 2026,
approximately 21:17 Asia/Tbilisi.
