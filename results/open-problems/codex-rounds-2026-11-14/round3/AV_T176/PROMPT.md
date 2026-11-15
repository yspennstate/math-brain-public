# Verify: has open problem T176 been settled by the OpenAI math release?

Our row: The mixing time of the Thorp shuffle
Statement: The Thorp shuffle on a deck of n cards (n even) cuts the deck into two halves of n/2 cards and, for each k = 1, …, n/2, drops the k-th cards of the two halves in an order decided by an independent fair coin. Determine the order of magnitude of its total-variation mixing time as n → ∞.
Where it stands (our note, Nov 2026, written before we knew of the release): Morris (STOC 2005, math/0507307) proved the first polylogarithmic bound, O(log^44 n) for n a power of 2; Montenegro and Tetali improved it to O(log^29 n); Morris (Ann. Probab. 37 (2009) 453–477) proved O(log^4 n) for all even n, and O(log^3 n) for n a power of 2 (arXiv:0912.2759). Czumaj and Vöcking (ICALP 2014, LNCS, pp. 344–355) studied the shuffle through non-Markovian couplings. Jiang (arXiv:2610.18884) proves t_mix(ε) ≤ C d^{5/3} + O_ε(d^{4/3} log d) for n = 2^d, that is O(log^{5/3} n), against the lower bound of order log n. The order is not determined. Open.

The OpenAI math release (github.com/openai/math, preprints dated September-October 2026, AI-generated, not refereed) has
preprints whose titles match this row:
- https://github.com/openai/math/tree/main/preprints/Optimal-order-mixing-of-the-Thorp-shuffle-September-26-2026  (title match score 38)
- https://github.com/openai/math/tree/main/preprints/Compatibility-entropy-and-the-spectrum-of-a-Thorp-sweep-September-26-2026  (title match score 11)
- https://github.com/openai/math/tree/main/preprints/Routing-densities-and-representation-contraction-for-Thorp-sweeps-September-26-2026  (title match score 11)

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

Rules (the author's standing laws):
- Work only inside this folder. Read anything, but never edit files elsewhere, never use git, never push, post, email or
  create accounts. Nothing you write leaves this folder except when the coordinating agent copies it.
- Compute: every program you run stays under 1 GB of RAM, one thread (set OMP_NUM_THREADS=1), runs under `nice -n 15`,
  and finishes within 20 minutes per run. No GPU, no MLX, no torch. This Mac is shared; never fill it.
- Literature: use the web search tool. Cite only papers you actually opened, with the authors exactly as on the paper or
  its arXiv page. Never invent a reference, a number or a step.
- Save as you go: append to LOG.md after every step (what you did, the command, the output that matters). The account's
  weekly allowance runs out within hours and the session may stop at any moment; LOG.md is what survives.
Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/AV_T176 (read it,
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
VERDICT: PARTIAL-CLAIMED optimal total-variation mixing order Θ(log n) for n = 2^d only
All three OpenAI preprints dated September 26, 2026 claim the ordinary full-deck Thorp result in physical shuffles for power-of-two deck sizes.
Our statement ranges over every even n; the short preprint explicitly excludes that extension, so the whole row is not claimed solved.
Lean artifacts and later citations exist, with narrower scopes for some companions; proof correctness is not assessed. Exact quotations and opened follow-ups are in VERIFY.md.
