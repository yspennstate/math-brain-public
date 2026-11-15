# Open problem T080: The freezing transition of hard spheres

Statement: The hard-sphere gas in R^d, d ≥ 2, has a phase transition as the density increases: close enough to close packing its infinite-volume Gibbs measures break translational symmetry when d ≥ 3, and have long-range orientational order when d = 2 (hard disks).

Source: B. J. Alder and T. E. Wainwright, Phase transition for a hard sphere system, J. Chem. Phys. 27 (1957); E. P. Bernard and W. Krauth, Two-step melting in two dimensions: first-order liquid–hexatic transition, Phys. Rev. Lett. 107 (2011)

Where it stands (checked by us, Nov 2026): Hard-core lattice gases order at high activity (Dobrushin 1968). In the continuum: uniqueness at low density by cluster expansion; hard disks cannot break translational symmetry (Richthammer, arXiv:0706.3637, CMP 2007); the densest packings are known in d = 3 (Hales 2005) and in d = 8, 24 (Viazovska, arXiv:1603.04246; Cohn–Kumar–Miller–Radchenko–Viazovska, arXiv:1603.06518; Ann. of Math. 185 (2017)). No phase transition has been proved for hard spheres or hard disks in the continuum. See also T044.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T080 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T080 (read it,
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
VERDICT: PARTIAL uniform Gibbs bounds for completely vacant thick seams

The earlier quantitative mixing-packing result holds. An independent tagged-nucleus calculation recovers its exact density formula. A new numerical audit compares that formula with a conditional second-arrival integral in dimensions 2, 3, 4, and 8: 24 comparisons agree within 3.34e-16. Its geometric separation, mixing constant, and limiting quantifiers also survive re-check.

The new piece is a restricted version of the requested interface partition-function estimate. PROOF.md proves, for a rectangular seam S, activity z, and every admissible exterior eta,

\[
m\log(1+zv_da^d)
\leq-\log\Pr_\eta(S\text{ empty})
\leq\log\sum_{n=0}^M\frac{(z|S|)^n}{n!}
\leq U(z|S|,M).
\]

Here m counts explicit radius-a insertion balls, separated by 1+2a and protected from the exterior by center-to-boundary distance 1+a; M is an explicit packing-number upper bound. The function U(T,M) is T for T<=M and M[1+log(T/M)] for T>M. Every selected particle displacement is integrated, including the Gibbs factorial. Conditioning extends the bounds to arbitrary surrounding finite volumes and all infinite-volume Gibbs measures.

For a fixed seam width W>=2(1+a), the negative log empty-seam probability is bounded above and below by explicit positive multiples of area times log z at high activity. The proof also permits insertion sites from any slightly dilated periodic packing, in any chosen orientation, using a suitable phase. An optional upper cap uses the unrestricted optimal packing density from the earlier result.

The width restriction cannot simply be dropped: an exterior unit-spaced planar row blocks every potential center in a strip of width less than sqrt(3)/2. Its empty probability is exactly one at every activity. This obstruction is proved explicitly.

Reproduce from this folder:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify.py > VERIFY_OUTPUT.txt 2>&1
```

The successful run took 0.030 seconds and peaked at 15.188 MiB RSS, with actual nice priority 20. It passed the density checks, 81 exact rational grid-threshold checks, exact factorial cancellation, 48 independent truncated-exponential/tilt comparisons, and six seam examples. Full output and independent hand checks are in LOG.md; data are in density_audit.csv, seam_bounds.csv, and verification.json. Numerical checks support the analytic proof and are not interval certificates.

What failed: two initial audit launches stopped before computation because this managed Mac rejected address-space/data resource-limit changes. The final script keeps a 60-second CPU limit, uses small fixed lists, and records peak memory; it does not claim an enforced address-space cap. The nice wrapper warns because inherited priority is already 20. Extending a positive boundary-uniform bound to arbitrary thin seams fails by the blocking example.

The bounded literature check found no solution after the earlier report. Opened sources were Lewis Bowen, Marcus Michelen, Will Perkins, *A phase transition for the hard sphere model on the hyperbolic plane*, [arXiv:2607.23873v1](https://arxiv.org/html/2607.23873v1); Andreas Göbel, Matthew Jenssen, Marcus Michelen, Marcus Pappik, Will Perkins, Leon Schiller, *Uniqueness, analyticity and mixing for Gibbs point processes via spectral gaps*, [arXiv:2606.28009](https://arxiv.org/abs/2606.28009); and Biman Bagchi, *From Freezing to Terminal Packing: A Puzzle and a Paradox*, [arXiv:2608.29676](https://arxiv.org/abs/2608.29676). These concern a hyperbolic transition, uniqueness bounds, and a density-functional framework respectively. None proves Euclidean Gibbs freezing.

What remains uncertain: no novelty claim is established for this elementary Gibbs insertion bound. A general orientation defect need not contain a completely vacant region of the required width. No comparison with a healed interface, Peierls estimate, symmetry breaking, or long-range orientational order is proved. T080 remains open.

Next worker: define an interface ensemble allowing continuum displacement on both sides of two differently oriented, slightly dilated periodic regions. Compare its integrated partition function with an aligned ensemble while keeping a common exterior and changing only a bounded strip. Prove a positive cost proportional to area without assuming that strip is completely vacant; the blocking example explains why protected insertion alone cannot do this.

Task: “take the NEXT checkable step on this problem, building on that work” — 2026-11-15, first retained local clock reading 01:19:29 Asia/Tbilisi; exact receipt time unavailable.
