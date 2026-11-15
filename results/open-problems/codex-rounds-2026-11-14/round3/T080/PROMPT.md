# Open problem T080: The freezing transition of hard spheres

Statement: The hard-sphere gas in R^d, d ≥ 2, has a phase transition as the density increases: close enough to close packing its infinite-volume Gibbs measures break translational symmetry when d ≥ 3, and have long-range orientational order when d = 2 (hard disks).

Source: B. J. Alder and T. E. Wainwright, Phase transition for a hard sphere system, J. Chem. Phys. 27 (1957); E. P. Bernard and W. Krauth, Two-step melting in two dimensions: first-order liquid–hexatic transition, Phys. Rev. Lett. 107 (2011)

Where it stands (checked by us, Nov 2026): Hard-core lattice gases order at high activity (Dobrushin 1968). In the continuum: uniqueness at low density by cluster expansion; hard disks cannot break translational symmetry (Richthammer, arXiv:0706.3637, CMP 2007); the densest packings are known in d = 3 (Hales 2005) and in d = 8, 24 (Viazovska, arXiv:1603.04246; Cohn–Kumar–Miller–Radchenko–Viazovska, arXiv:1603.06518; Ann. of Math. 185 (2017)). No phase transition has been proved for hard spheres or hard disks in the continuum. See also T044.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T080 (read it,
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
VERDICT: PARTIAL quantitative near-optimal mixing packings; the Gibbs freezing problem remains open

PROOF.md proves that in every dimension d >= 2, stationary, isotropic, translation-mixing sphere-packing laws can have intensity arbitrarily close to the unrestricted packing optimum. The result concerns unrestricted packing laws, not Gibbs measures. It gives a concrete obstruction to proving freezing from density and packing geometry alone.

For a periodic packing of intensity rho_P and Poisson grain-nucleus intensity lambda, the constructed law has intensity rho_P q_d(t), where

\[
t=(\lambda v_d)^{1/d},\qquad
q_d(t)=d\int_0^\infty u^{d-1}e^{-(u+t)^d}\,du
\geq 1-d\Gamma(2-1/d)t.
\]

For bounded local observables in radius-a windows separated by R > 8a, connected correlations are at most 8(1+m)exp(-m), with m=lambda v_d(R/4)^d. The proof gives a planar bond-orientation example, proves periodic approximation of the unrestricted optimum, and certifies that contact-containing instances are not finite-activity Gibbs laws. Mixing is asserted at each fixed grain scale; the estimate degenerates as the density approaches optimal.

The qualitative Euclidean density obstruction is already known. Section 1.4 of Lewis Bowen, Marcus Michelen, Will Perkins, *A phase transition for the hard sphere model on the hyperbolic plane*, [arXiv:2607.23873](https://arxiv.org/html/2607.23873v1), states equality of optimal and optimal Poisson-factor densities in Euclidean space. The contribution here is an explicit construction, density formula, and correlation bound, with no claim that these are new to the literature. Independent marks are used; the proof does not identify this construction with an unmarked Poisson factor.

The bounded literature check found no Euclidean high-density Gibbs ordering theorem. Two 2026 papers add context omitted from the brief: the hyperbolic theorem above, and improved uniqueness bounds in Andreas Göbel, Matthew Jenssen, Marcus Michelen, Marcus Pappik, Will Perkins, Leon Schiller, *Uniqueness, analyticity and mixing for Gibbs point processes via spectral gaps*, [arXiv:2606.28009](https://arxiv.org/abs/2606.28009). Both precede the brief's November 2026 status date and neither settles its Euclidean freezing statement. No SOLVED_ELSEWHERE.md was written.

Reproduce the numerical audit from this folder:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify.py > VERIFY_OUTPUT.txt
```

The corrected run passed in 0.222 seconds with peak RSS 27.109 MiB. Actual inherited nice priority was 20; the nice wrapper reported that it could not lower priority further. The script checks priority >= 15 and limits CPU time to 60 seconds. Outputs are q_table.csv, verification.json, and VERIFY_OUTPUT.txt; the complete output is also in LOG.md.

The audit compared integral and closed-form expressions in dimensions 2 and 3 (largest observed difference 2.50e-16), independently evaluated the loss constant in dimensions 2, 3, 4, and 8, and checked the radial-order-statistic interpretation with 200,000 samples per dimension. The original one-panel adaptive quadrature missed a peak and failed; a fixed initial mesh corrected it. This failure and the priority warning are retained in LOG.md. Floating-point and pseudorandom checks are supporting audits, not proof certificates. Geometric separation, density normalization, constants, covariance factors, guard bands, and limiting quantifiers were also checked independently in LOG.md.

What remains uncertain: no novelty claim is established, and no estimate for high-activity Gibbs probabilities of grain boundaries is proved. The construction has exact-contact singularities and does not supply a Gibbs competitor or a Gibbs counterexample.

Next worker: use the DLR specification to compare the weight of an interface between differently oriented, slightly dilated periodic regions with the weight after removing that interface. A useful next lemma would bound the constrained partition-function cost per unit interface area, uniformly in the finite-volume region and with the continuum displacement variables integrated. Density loss alone cannot supply such a bound; this construction shows the missing distinction explicitly.

Task: “push this problem forward by one checkable piece” — received 2026-11-14, approximately 21:56 Asia/Tbilisi.
