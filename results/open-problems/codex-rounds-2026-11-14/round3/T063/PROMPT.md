# Open problem T063: Gaussian free field limit of the six-vertex height function

Statement: For the six-vertex model on Z^2 with weights a = b = 1 and c ∈ (0, 2), so that Δ = 1 − c²/2 ∈ (−1, 1), the height function converges in the scaling limit to a Gaussian free field whose variance is an explicit function of Δ.

Source: R. J. Baxter, Exactly Solved Models in Statistical Mechanics (Academic Press, 1982); B. Nienhuis, Critical behavior of two-dimensional spin models and charge asymmetry in the Coulomb gas, J. Stat. Phys. 34 (1984)

Where it stands (checked by us, Nov 2026): Δ = 0 is the dimer model, with GFF limit (Kenyon 2001); small perturbations of it by interacting-dimer methods (Giuliani–Mastropietro–Toninelli, arXiv:1406.7710). For a = b = 1, logarithmic variance (delocalization) for c ∈ [1, 2] (Duminil-Copin–Karrila–Manolescu–Oulamara, arXiv:2012.13750, JEMS 2024), after unbounded variance for c ∈ [√(2+√2), 2] (Lis, arXiv:2004.05337); localization for c > a + b and delocalization at c = a + b (Glazman–Peled, arXiv:1909.03436). Averous–Duminil-Copin–He–Lammers–Manolescu (arXiv:2610.07454) prove convergence to the GFF in simply connected domains with piecewise constant boundary conditions for a wide range of Δ, including Δ near 0 and Δ between −1 and −1/2. The whole range Δ ∈ (−1, 1) is open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T063 (read it,
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
VERDICT: PARTIAL located a November uniqueness preprint and a conditional repair of the GFF state identification

The literature search found a substantial update absent from the supplied status. Following step 1, work stops at this literature handoff. No new proof or finite computation is claimed.

[SOLVED_ELSEWHERE.md](SOLVED_ELSEWHERE.md) gives the references, identifiers, theorem numbers, scopes and outstanding conditions. The new item is Yan Ru Pei's November preprint, **hexagon:2611.00291v1**; this is not an arXiv number. A September OpenAI manuscript claims the entire balanced plane regime, but its proof has not been certified here. The November repair is conditional and does not itself establish the full GFF conjecture.

The web searches and opened papers are recorded in [LOG.md](LOG.md). The search ran from approximately 16:49 to 16:52 UTC on 14 November 2026, within the ten-minute limit. Main queries were `six vertex model Gaussian free field convergence 2026 full disordered regime` and `"The Gaussian free field limit of the balanced" gap proof`.

Audit: compared the theorem statements with their assumptions and the November proof's explicit qualification. Independently checked the parameter conversions by solving c² = 2(1−Δ), and the variance formula by the cosine double-angle identity. Details are in the log. A primary-source GitHub directory fetch failed; the linked manuscript PDF was opened through its mirror. No proof-level audit of either new manuscript was completed; the accuracy of their deeper arguments remains uncertain.

Next worker: check the existence and free-energy minimality of the auxiliary state (O1 and O2), then audit the rest of the September full-range proof and the November uniqueness proof. Do not infer full GFF convergence from uniqueness alone.

Only small read-only Python commands ran, using `OMP_NUM_THREADS=1 nice -n 15 python3`; effective niceness was verified as 20. No numerical data were generated. No files outside this folder were written, and no git or external mutations were used.

Task: “push this problem forward by one checkable piece” (T063); received approximately 20:49 Asia/Tbilisi, 14 November 2026.
