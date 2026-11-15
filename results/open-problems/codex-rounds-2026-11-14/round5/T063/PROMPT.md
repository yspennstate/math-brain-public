# Open problem T063: Gaussian free field limit of the six-vertex height function

Statement: For the six-vertex model on Z^2 with weights a = b = 1 and c ∈ (0, 2), so that Δ = 1 − c²/2 ∈ (−1, 1), the height function converges in the scaling limit to a Gaussian free field whose variance is an explicit function of Δ.

Source: R. J. Baxter, Exactly Solved Models in Statistical Mechanics (Academic Press, 1982); B. Nienhuis, Critical behavior of two-dimensional spin models and charge asymmetry in the Coulomb gas, J. Stat. Phys. 34 (1984)

Where it stands (checked by us, Nov 2026): Δ = 0 is the dimer model, with GFF limit (Kenyon 2001); small perturbations of it by interacting-dimer methods (Giuliani–Mastropietro–Toninelli, arXiv:1406.7710). For a = b = 1, logarithmic variance (delocalization) for c ∈ [1, 2] (Duminil-Copin–Karrila–Manolescu–Oulamara, arXiv:2012.13750, JEMS 2024), after unbounded variance for c ∈ [√(2+√2), 2] (Lis, arXiv:2004.05337); localization for c > a + b and delocalization at c = a + b (Glazman–Peled, arXiv:1909.03436). Averous–Duminil-Copin–He–Lammers–Manolescu (arXiv:2610.07454) prove convergence to the GFF in simply connected domains with piecewise constant boundary conditions for a wide range of Δ, including Δ near 0 and Δ between −1 and −1/2. The whole range Δ ∈ (−1, 1) is open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T063 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T063 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T063 (read it,
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
VERDICT: PROVED free-energy minimality for simultaneous near-balanced torus limits with one or both fluxes fixed

The earlier result holds. Its reflection and row-insertion argument was independently re-derived, its unchanged script passed again, and a new edge enumerator reproduced all 348 small gluing images. No newer full-range GFF solution was certified in the literature check, which took under five minutes.

The new result removes the earlier requirement to take an infinite-cylinder limit first. Fix a=b=1 and any c>0. Let Z(N,L;n,m) prescribe n right arrows per vertical cut and m up arrows per horizontal cut, and let p_c be the maximal specific pressure among all translation-invariant allowed arrow laws. Set

\[
H=2\min(n,L-n),\qquad W=2\min(m,N-m).
\]

For W,H>=2, the finite-volume bound is

\[
\log Z(N,L;n,m)\ge WHp_c-3(W+H)\log2.
\]

Thus, whenever N,L both tend to infinity and n/L,m/N tend to 1/2, the pressure tends to p_c and every local subsequential limit minimises specific free energy. No aspect ratio bound is needed. These limits are also zero-slope gradient Gibbs measures, by a direct check that bounded local replacements preserve the winding sectors.

The original ensemble with only n fixed has the same conclusion for arbitrary simultaneous limits with n/L tending to 1/2: retain the summand m=floor(N/2) in its partition function. This also handles odd dimensions. [PROOF.md](PROOF.md) contains the complete argument, including the local entropy estimate and conditional uniqueness implication. It establishes no uniqueness or GFF convergence.

The new [check_two_flux.py](check_two_flux.py) uses exact integer partition polynomials. It compares two independent edge enumeration methods on six shapes, verifies 348 gluing images and 2296 row-and-column insertion images with explicit inverses, and passes 60 coefficientwise partition comparisons. The reported run took 0.474 seconds with peak RSS 14,663,680 bytes. Coefficientwise inequalities check every c>0 simultaneously.

Commands:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 check_two_flux.py
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114r3/briefs/T063/check_surgery.py
```

What failed or remains uncertain: no finite checks failed. The nice launcher reports a denied priority change because inherited priority is already nice 20; both scripts confirm that value. Neither the uniqueness proof in Yan Ru Pei's [November preprint](https://hexagonmath.org/pdf/2611.00291v1), identifier hexagon:2611.00291v1, nor the September correlation argument has been audited. No arXiv identifier is assigned here to the Hexagon item. The other opened paper was Emile Averous, Hugo Duminil-Copin, Tiancheng He, Piet Lammers and Ioan Manolescu, [Conformal invariance of the six-vertex model's height function](https://arxiv.org/abs/2610.07454). Global novelty of the elementary finite-volume extension is not claimed. c=0 and extreme fluxes are outside the stated finite bound.

Next worker: audit Pei's Corollary 1.3 and its dependencies. If its unique-minimiser assertion is sound, the present theorem identifies all these simultaneous near-balanced limits with the balanced plane state. Correlation asymptotics and GFF convergence still require a separate proof-level audit.

All files written are in this folder. Both earlier folders were read only; no git, subagents, external messages, accounts, or publication were used. [LOG.md](LOG.md) records the search, rechecks, outputs and audit.

Task: “take the NEXT checkable step on this problem, building on that work” (T063); received approximately 04:32 Asia/Tbilisi, 15 November 2026.
