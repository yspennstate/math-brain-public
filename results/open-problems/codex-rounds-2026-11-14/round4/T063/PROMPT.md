# Open problem T063: Gaussian free field limit of the six-vertex height function

Statement: For the six-vertex model on Z^2 with weights a = b = 1 and c ∈ (0, 2), so that Δ = 1 − c²/2 ∈ (−1, 1), the height function converges in the scaling limit to a Gaussian free field whose variance is an explicit function of Δ.

Source: R. J. Baxter, Exactly Solved Models in Statistical Mechanics (Academic Press, 1982); B. Nienhuis, Critical behavior of two-dimensional spin models and charge asymmetry in the Coulomb gas, J. Stat. Phys. 34 (1984)

Where it stands (checked by us, Nov 2026): Δ = 0 is the dimer model, with GFF limit (Kenyon 2001); small perturbations of it by interacting-dimer methods (Giuliani–Mastropietro–Toninelli, arXiv:1406.7710). For a = b = 1, logarithmic variance (delocalization) for c ∈ [1, 2] (Duminil-Copin–Karrila–Manolescu–Oulamara, arXiv:2012.13750, JEMS 2024), after unbounded variance for c ∈ [√(2+√2), 2] (Lis, arXiv:2004.05337); localization for c > a + b and delocalization at c = a + b (Glazman–Peled, arXiv:1909.03436). Averous–Duminil-Copin–He–Lammers–Manolescu (arXiv:2610.07454) prove convergence to the GFF in simply connected domains with piecewise constant boundary conditions for a wide range of Δ, including Δ near 0 and Δ between −1 and −1/2. The whole range Δ ∈ (−1, 1) is open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T063 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T063 (read it,
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
VERDICT: PROVED free-energy minimality of every near-balanced torus subsequential limit

For a=b=1 and every c>0, let mu_L be the infinite-cylinder limit in the sector with n_L right arrows per transverse cut. If n_L/L tends to 1/2, every local subsequential limit of mu_L minimises specific free energy among all translation-invariant allowed arrow laws. This is the new result beyond the earlier literature handoff. It does not prove a GFF limit.

The complete argument is in [PROOF.md](PROOF.md). Two weight-preserving constructions suffice: four reflected rectangles give a balanced torus, and insertion of straight rows embeds a smaller balanced torus into a near-balanced sector. If p_c is the variational pressure, H=2 min(n,L-n)>=2, and p_L(n) is the sector strip pressure, the explicit bound is

\[
p_L(n)\ge \frac{H}{L}p_c-\frac{3\log2}{L}.
\]

Fixed-block entropy subadditivity then proves that all near-balanced subsequential states attain p_c. This avoids the September manuscript's rectangle operator-norm estimate and any Bethe-ansatz free-energy formula.

The earlier finding holds: Yan Ru Pei's [November preprint](https://hexagonmath.org/pdf/2611.00291v1), identifier hexagon:2611.00291v1, makes its state identification conditional on existence (O1) and free-energy minimality (O2). The present proof supplies O2 for every subsequential state. If its Corollary 1.3, uniqueness of the translation-invariant minimiser for 1<c<=2, is valid, compactness now gives O1 and identification for the whole near-balanced sequence. That uniqueness proof has not been audited here. There is no arXiv identifier for this November item in the opened record.

The literature check lasted under five minutes and found no newer resolution than the earlier report. Opened the November PDF, the [September OpenAI manuscript](https://mathcommunity.github.io/oai-math-revised/papers/The-Gaussian-free-field-limit-of-the-balanced-six-vertex-model-with-variance-multiplier-1-over-arcsin-c-over-2-September-23-2026/The-Gaussian-free-field-limit-of-the-balanced-six-vertex-model-with-variance-multiplier-1-over-arcsin-c-over-2-September-23-2026.pdf), and [arXiv:2610.07454](https://arxiv.org/abs/2610.07454) by Emile Averous, Hugo Duminil-Copin, Tiancheng He, Piet Lammers and Ioan Manolescu. No full-range solution was certified. The earlier folder contained no PROOF.md or scripts; its theorem-scope summary and parameter identities were independently rechecked.

Verification command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 check_surgery.py
```

[check_surgery.py](check_surgery.py) uses exact integer and rational arithmetic. It passed 72 row-insertion comparisons, 12 rectangle comparisons, checks at c=1/2, hand formulas for a single vertex and the balanced 2x2 torus, 348 direct gluing-map images, and 30 direct insertion checks. Every image was checked for seam compatibility, balanced flux, and preservation of weight. The largest matrix has dimension 20. Final runtime was about 0.17 seconds and measured peak resident memory 14,925,824 bytes. The nice launcher reports a failed priority change because priority is already inherited at nice 20; the script prints that value. Full outputs and the coefficient audit are in [LOG.md](LOG.md).

What failed or remains uncertain: the direct September PDF open initially failed; its landing-page link worked. An initial diagonal-selection formulation used insufficient individual-pattern error control; the final proof uses total variation on the entire finite marginal. No remaining failed finite checks. Global novelty of this elementary minimisation lemma is not claimed. Neither the November uniqueness argument nor the September root/correlation and GFF arguments have been verified. The minimisation lemma itself does not require either manuscript.

Next worker: audit the November Corollary 1.3 and its dependencies. If sound, combine it with this proof to certify auxiliary-state existence and identification, then examine the September correlation argument separately. Do not infer GFF convergence from state identification alone.

Task: “take the NEXT checkable step on this problem, building on that work” (T063); received about 01:07 Asia/Tbilisi, 15 November 2026.
