# Open problem T080: The freezing transition of hard spheres

Statement: The hard-sphere gas in R^d, d ≥ 2, has a phase transition as the density increases: close enough to close packing its infinite-volume Gibbs measures break translational symmetry when d ≥ 3, and have long-range orientational order when d = 2 (hard disks).

Source: B. J. Alder and T. E. Wainwright, Phase transition for a hard sphere system, J. Chem. Phys. 27 (1957); E. P. Bernard and W. Krauth, Two-step melting in two dimensions: first-order liquid–hexatic transition, Phys. Rev. Lett. 107 (2011)

Where it stands (checked by us, Nov 2026): Hard-core lattice gases order at high activity (Dobrushin 1968). In the continuum: uniqueness at low density by cluster expansion; hard disks cannot break translational symmetry (Richthammer, arXiv:0706.3637, CMP 2007); the densest packings are known in d = 3 (Hales 2005) and in d = 8, 24 (Viazovska, arXiv:1603.04246; Cohn–Kumar–Miller–Radchenko–Viazovska, arXiv:1603.06518; Ann. of Math. 185 (2017)). No phase transition has been proved for hard spheres or hard disks in the continuum. See also T044.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T080 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T080 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T080 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 5 worker built on the latest of these. Its folder is ~/codex_op_1114r5/briefs/T080 (read it, never
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
VERDICT: PARTIAL robust triangular interfaces evade the earlier underoccupation detector

The round-4 Gibbs bound holds. Its partition-function estimate and connected-set count were independently re-derived, and its unchanged audit passed from a copy inside this folder.

The new result answers the geometric test proposed by round 4 negatively for its explicit planar detector. Join triangular lattices of spacing 101/100 and orientations 0 and pi/6 across a vertical strip of width 101/100. Allow arbitrary relative translations and arbitrary simultaneous particle displacements of magnitude less than 1/400. Every resulting configuration is a diameter-one packing, and **every axis-parallel square of side four contains at least three centers**. Thus no translated four-by-four grid has a box with at most two centers, even along the interface.

More generally, for lattice spacing s, displacement radius delta, and strip width g satisfying s-2delta>1 and g-2delta>1, put rho_s=2/(sqrt(3)s^2) and R=s/sqrt(3). The uniform count proved in PROOF.md is

\[
N_X(Q)\geq\rho_s(\ell-2\delta-2R)_+
                    (\ell-2\delta-g-4R)_+.
\]

It applies to every square translation, both lattice phases, both orientations, and every allowed displacement. For any fixed threshold rho<rho_s, all squares exceed rho ell^2 once

\[
\ell>\frac{4\delta+g+6R}{1-\rho/\rho_s}.
\]

This dependence matters: the result does not rule out a finer detector whose threshold and scale are chosen together near close packing.

The explicit four-square count is certified by the rational lower bound

\[
N_X(Q)>\frac{3317635}{1591356}
=2+\frac{134923}{1591356}>2.
\]

A second exact calculation expands the original bound in Q(sqrt(3)) and independently verifies that it exceeds two. The finite displacement sectors have positive continuum volume, with weight (z pi delta^2)^M for one particle in each of M prescribed displacement balls. This is a restricted sector weight, not a Gibbs interface probability. The independent-jitter packing law is explicitly shown not to satisfy DLR.

Reproduce from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 prior_recheck/verify.py > prior_recheck/VERIFY_OUTPUT.txt 2>&1
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify.py > VERIFY_OUTPUT.txt 2>&1
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_artifacts.py > ARTIFACT_AUDIT.txt 2>&1
```

The new audit passed exact scalar comparisons, six cell-vertex and shoelace calculations, 720 lattice-vector comparisons, 560 exact phase/square enumerations and 35 exact split-width cases. Its sampled minimum was eight safe sites; only the analytic lower bound of three is asserted globally. Three floating-point jitter trials support the separation argument. The new run took 1.862 seconds and peaked at 16.891 MiB RSS; the copied round-4 audit took 0.431 seconds at 17.703 MiB. Actual nice priority was 20. Full output and second derivations are in LOG.md; machine-readable results are in verification.json. The nice wrapper warning reflects the already inherited lower priority.

What failed: the proposed deterministic implication from differing orientations to boxes with at most two centers is false. No mathematical audit failed. Omitting square erosion or strip width would invalidate the count; explicit negative controls detect both shortcuts. A bounded strip may still have a particle deficit proportional to its length and a positive Gibbs cost.

The bounded literature check found no later Euclidean solution. Opened sources were Lewis Bowen, Marcus Michelen, Will Perkins, *A phase transition for the hard sphere model on the hyperbolic plane*, [arXiv:2607.23873](https://arxiv.org/abs/2607.23873), and Andreas Göbel, Matthew Jenssen, Marcus Michelen, Marcus Pappik, Will Perkins, Leon Schiller, *Uniqueness, analyticity and mixing for Gibbs point processes via spectral gaps*, [arXiv:2606.28009](https://arxiv.org/abs/2606.28009). They prove a hyperbolic transition and improved uniqueness bounds, respectively. This search was not exhaustive.

What remains uncertain: novelty of this elementary geometric bound is not established. There is no estimate for the Gibbs probability of these interfaces, no comparison with an aligned ensemble, and no orientational surface tension or symmetry breaking. T080 remains open.

Next worker: replace occupation alone by a local defect condition that detects the two disjoint families of nearest-neighbor directions in this example. At fixed angles 0 and pi/6, first determine whether an intervening chain of such local defects is geometrically forced when a bounded strip is filled arbitrarily rather than left empty. Keep dilation, displacement radius and observation scale explicit. Any subsequent Gibbs bound must integrate those dense defect configurations; the present underoccupation estimate cannot charge them automatically.

Task: “take the NEXT checkable step on this problem, building on that work” — 2026-11-15, first retained clock reading 08:05:35 Asia/Tbilisi; exact receipt time unavailable.
