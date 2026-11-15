# Open problem T064: Percolation description of the nodal lines of random waves (Bogomolny–Schmit)

Statement: The nodal set of the random plane wave (the centred Gaussian field on R^2 with covariance J_0(|x − y|)), and conjecturally of high-energy eigenfunctions of chaotic billiards, has the large-scale behaviour of critical percolation: crossing probabilities of nodal domains converge to Cardy's formula and nodal lines to SLE(6).

Caveat: The predicted number of nodal domains per unit area, (3√3 − 5)/π times a normalisation, is off by a few percent in numerics (Nastasescu 2011; Beliaev–Kereta 2013), so the conjecture is the scaling-limit statement, not that constant.

Source: E. Bogomolny and C. Schmit, Percolation model for nodal domains of chaotic wave functions, Phys. Rev. Lett. 88 (2002); M. V. Berry, Regular and irregular semiclassical wavefunctions, J. Phys. A 10 (1977)

Where it stands (checked by us, Nov 2026): The number of nodal domains grows like a constant times the area (Nazarov–Sodin 2009, 2016). Russo–Seymour–Welsh bounds and sharp thresholds hold for positively correlated planar Gaussian fields with fast decay (Beffara–Gayet 2017; Rivera–Vanneuville 2019; Muirhead–Vanneuville 2020). The random plane wave correlates slowly and changes sign, so none of this applies; open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T064 (read it,
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
VERDICT: PARTIAL corrected literature status: noncritical percolation of the random plane wave is already proved

The supplied status paragraph omits a substantial advance. The opened paper
by Stephen Muirhead, Alejandro Rivera and Hugo Vanneuville, with an appendix
by Laurin Köhler-Schindler,
[arXiv:2010.11770v3](https://arxiv.org/abs/2010.11770v3), proves critical
level zero for the random plane wave without FKG. Exact statements,
theorem numbers, dates and links are in SOLVED_ELSEWHERE.md.

This is a correction of the stated baseline, not a newly discovered result
after November 2026. The Cardy/SLE(6) conjecture remains unresolved in the
sources checked. No new theorem or computation is claimed. The substantial
omitted advance triggers step 1's instruction to record it and stop.

Verification: compared the arXiv abstract, HTML and original PDF. Checked
level signs by setting the ordinary superlevel threshold u = -l: positive
u is the bounded-component regime. Independently substituted the RPW decay
envelope into the general crossing bound; details are in LOG.md. A separate
2025 paper by Stephen Muirhead and Igor Wigman still leaves criticality
open, corroborating the distinction between a critical level and behavior
at that level.

Commands and outputs: no computation script was run. The exact web-search
queries, opened URLs, read commands and relevant output are recorded in
LOG.md. File creation used apply_patch. Only this folder was changed.

What failed or remains uncertain: no solution of the scaling-limit statement
was located. A short web search cannot certify that none exists. The search
found no advance first appearing after the supplied November 2026 cutoff;
the omitted result dates from 2020/2023. The HTML rendering displayed a
2026 date inconsistent with the PDF and submission history; the latter
were used. Priority adjustment printed an OS error on read-only commands;
no compute-heavy work was attempted.

Next worker: correct the baseline to include arXiv:2010.11770, then focus on
zero-level rectangle crossings or the removal of sprinkling in gluing.
Fixed nonzero-level crossing estimates do not control constants uniformly
as the level tends to zero.

Task: “push this problem forward by one checkable piece” — 14 November 2026,
approximately 20:49 Asia/Tbilisi.
