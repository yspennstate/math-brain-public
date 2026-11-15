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
VERDICT: PARTIAL uniform exponential bounds for connected underoccupied regions

The earlier density construction and vacant-seam estimate hold. The round-3 audit was rerun unchanged from a copy inside this folder, and its main inequalities were independently re-derived in LOG.md.

The new piece allows particles in the defect and sums over its possible connected shapes. Partition space into boxes of side ell. Suppose each box admits m_0 mutually compatible protected insertion balls of volume b. Set v=ell^d and choose 0<r<m_0. For zv>=r, define

\[
\tau=m_0\log(1+zb)-r[1+\log(zv/r)],\qquad
q=(2d)^2e^{-\tau}.
\]

For any prescribed n boxes, the probability that their union contains at most rn centers is at most exp(-n tau), capped at one. All continuum displacement variables are integrated. A canonical tree traversal bounds the number of connected n-box sets containing a fixed box by (2d)^(2(n-1)). Consequently, in every infinite-volume hard-sphere Gibbs measure,

\[
\Pr\{|K(j)|\geq n\}\leq
\min\{1,q^n/(2d)^2\},
\]

where K(j) is the face-connected component of boxes with at most r centers containing box j. Thus q<1 excludes infinite underoccupied components. Finite-volume versions use only boxes wholly inside the sampling region and are uniform over admissible fixed exteriors.

For ell=4 and insertion radius a=1/4, the following rigorous sufficient constants use only pi>3 and e<3:

| Dimension | Maximum count in an underoccupied box | Sufficient activity | Bound on q |
|---|---:|---:|---:|
| 2 | 2 | z>=4096 | 4/9 |
| 3 | 4 | z>=65536 | 729/16384 |

More generally, for every fixed number-density threshold 0<rho<rho_*, periodic insertion families permit a box size and activity threshold for which the same exponential component bound holds for boxes containing at most rho ell^d centers. These choices are not uniform as rho approaches the optimal packing density rho_*.

Reproduce both audits from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 prior_recheck/verify.py > prior_recheck/VERIFY_OUTPUT.txt 2>&1
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify.py > VERIFY_OUTPUT.txt 2>&1
```

The new audit passed 3,072 exact weighted-graph comparisons, 150 floating-point tilt comparisons, two independent enumerations of connected sets, and exact rational checks of both stated activity bounds. Anchored connected-set counts were 1,4,18,76,315 in d=2 through size five and 1,6,45,344 in d=3 through size four. The run took 0.271 seconds, peaked at 16.219 MiB RSS, and confirmed actual nice priority 20. PROOF.md contains the analytic argument; LOG.md contains commands, complete output, and attempts to break it. Floating-point checks are not interval certificates. The copied earlier audit passed in 0.030 seconds at 15.625 MiB RSS.

What failed or required correction: the sufficient bound is uninformative for the tested d=3, z=10000 case. The finite-volume component statement needed an explicit restriction to boxes inside the sampling region; including arbitrary exterior boxes would be false. The corrected proof includes that restriction. No new computation failed. The nice wrapper warns because the inherited priority is already 20.

The five-minute literature check found no later Euclidean solution. Opened sources were Lewis Bowen, Marcus Michelen, Will Perkins, *A phase transition for the hard sphere model on the hyperbolic plane*, [arXiv:2607.23873](https://arxiv.org/abs/2607.23873), and Andreas Göbel, Matthew Jenssen, Marcus Michelen, Marcus Pappik, Will Perkins, Leon Schiller, *Uniqueness, analyticity and mixing for Gibbs point processes via spectral gaps*, [arXiv:2606.28009](https://arxiv.org/abs/2606.28009). They concern a hyperbolic transition and improved uniqueness bounds, respectively. Neither settles Euclidean freezing. This bounded search is not exhaustive.

What remains uncertain: novelty of this elementary Gibbs estimate is not established. A dense orientation interface need not be underoccupied at the chosen scale or threshold. No comparison with an aligned interface, positive orientational surface tension, orientational order, or translational symmetry breaking is proved. T080 remains open.

Next worker: test the missing geometric implication for two fixed, non-equivalent planar triangular-lattice orientations, allowing continuum displacements and relative shifts on both sides of a bounded strip. Determine whether the interface forces enough underoccupied boxes for this bound to apply, or exhibit an interface that evades such a count. Any positive claim must retain its dependence on orientation angle, dilation, and box scale. The present result supplies the Gibbs weight and shape count only after an occupation deficit has been established.

Task: “take the NEXT checkable step on this problem, building on that work” — 2026-11-15, first retained clock reading 04:41:23 Asia/Tbilisi; exact receipt time unavailable.
