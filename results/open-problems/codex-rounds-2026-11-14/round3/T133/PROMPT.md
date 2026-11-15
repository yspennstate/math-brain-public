# Open problem T133: The arctic curve of the six-vertex model with domain-wall boundary conditions

Statement: For the six-vertex model with domain-wall boundary conditions on an n × n square, in the disordered regime −1 < Δ < 1, the boundary between the frozen and disordered regions converges after rescaling by n to the curve predicted by Colomo and Pronko, and recovered by the tangent method of Colomo and Sportiello; the analogous prediction holds in the antiferroelectric regime Δ < −1.

Caveat: The predictions are explicit algebraic or transcendental curves depending on the weights; at Δ = 0 (free fermions) the curve is an ellipse, the arctic circle of domino tilings for equal weights.

Source: F. Colomo and A. G. Pronko, The limit shape of large alternating sign matrices, SIAM J. Discrete Math. 24 (2010); F. Colomo and A. Sportiello, Arctic curves of the six-vertex model on generic domains: the tangent method, J. Stat. Phys. 164 (2016)

Where it stands (checked by us, Nov 2026): At Δ = 0 the arctic circle is known (Jockusch–Propp–Shor 1995). At the ice point Δ = 1/2, which includes uniformly random alternating sign matrices, Aggarwal (arXiv:1812.03847, 2020) proved the Colomo–Pronko arctic curve for domain-wall boundary conditions, and the predicted boundaries for more general three-bundle domains. Other values of Δ are open; fluctuations of the height function are T063.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T133 (read it,
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
VERDICT: PARTIAL substantial limit-shape announcement found; full T133 remains unverified

The literature check found Alexey Bufetov, *Limit shape for domain-wall six-vertex model*, [arXiv:2609.20576v1](https://arxiv.org/abs/2609.20576v1), submitted 17 September 2026. Its asserted parameter ranges and proof-status caveat are recorded in [SOLVED_ELSEWHERE.md](SOLVED_ELSEWHERE.md).

This satisfies the instruction to stop upon finding a substantial advance. No original theorem or numerical result is claimed, and no computation was started. The announcement predates the brief's November 2026 check; it is a correction to that check, not a claim of a later publication.

Verification: compared the arXiv metadata, HTML theorem statements and PDF text. Checked Theorems 3.1–3.2 against Remark 3.3 and Section 4.2. Read the proof-strategy comments to avoid presenting an announcement as a supplied proof. These are checks of the source's statements, not independent mathematical proofs.

The decisive web query was `six vertex arctic curve rigorous general weights 2026 domain wall limit shape`. All queries, shell commands and material outputs are in [LOG.md](LOG.md). The literature search took less than ten minutes.

What failed or remains uncertain: no full proof was found in the inspected note; no proof audit was possible. The shell could not report process priority (`ps` denied), and `nice` reported a priority-setting error. No numerical workload was launched. A bounded literature search cannot certify the absence of a later proof.

Next worker: locate and audit the full proof behind the announcement; distinguish its height-convergence conclusion from any stronger microscopic frozen-boundary claim. If pursuing a parameter range omitted by it, focus on 1/2 < Delta < 1.

Task: "push this problem forward by one checkable piece" — 14 November 2026, approximately 22:01 Asia/Tbilisi.
