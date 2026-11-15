# Open problem T081: The liquid–vapour transition for continuum particles with pair interactions

Statement: Classical point particles in R^d, d ≥ 2, interacting through a fixed stable, translation-invariant pair potential with a short-range repulsion and a finite-range attraction (of Lennard-Jones type) have a liquid–vapour transition: for some temperature and chemical potential there are two infinite-volume Gibbs measures with different densities.

Caveat: The class of potentials must be fixed; the known proofs add Kac scaling, a four-body repulsion or an attraction tied to a fixed partition of space.

Source: J. L. Lebowitz, A. Mazel and E. Presutti, Liquid–vapor phase transitions for systems with finite-range interactions, J. Stat. Phys. 94 (1999); D. Ruelle, Existence of a phase transition in a continuous classical system, Phys. Rev. Lett. 27 (1971)

Where it stands (checked by us, Nov 2026): Proved with Kac potentials at small scale parameter and a four-body repulsion (Lebowitz–Mazel–Presutti, arXiv:cond-mat/9809145, J. Stat. Phys. 1999), for the Widom–Rowlinson model (Ruelle 1971; a stochastic-geometric proof by Chayes–Chayes–Kotecký, CMP 1995) and the continuum Potts model (Georgii–Häggström, CMP 1996). With pair interactions only, He–Jauslin–Lebowitz–Peled (arXiv:2510.24825) prove it at a fixed small Kac parameter in a boxed model whose attraction follows a fixed partition into cubes, so not translation invariant. Open for translation-invariant pair potentials.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T081 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T081 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T081 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 5 worker built on the latest of these. Its folder is ~/codex_op_1114r5/briefs/T081 (read it, never
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
VERDICT: PARTIAL uniform surface-pressure estimate verified for the safe-state restricted ensembles

The round 4 geometric result holds on recheck. Its full finite checker passes again, and an independent bit-mask count recovers 388 connected supports and 204 ordered separated pairs. The boundary-connectivity, containment and nesting arguments were also re-derived. The earlier conditional replacement checks still give all 54 exact comparisons and the examples 160 and 128 versus the incorrect independent-average value 144.

The new piece is [PROOF.md](PROOF.md): a complete safe-state surface-pressure theorem with explicit constants. For a product one-cell reference with universal safe-set mass at least `exp(-kappa)` and a bounded interaction on connected supports with incident norm M, both free and conditioned finite-volume logarithmic partition functions differ from their common bulk pressure by at most

`(5*M + kappa) * |inner boundary|`.

The estimate is uniform in microscopic exterior states. The proof constructs a stationary Gibbs law and supplies both conditional-entropy inequalities, including infinite conditioning. It requires no mixing. Substitution of the endpoint-density and safe-packing estimates gives the continuum coefficient

`C[delta^2 + e_R + (1+C_delta)/beta + epsilon_U/(beta*L^d)]`.

The Section 6 surface formula then follows **conditional on** its connected effective-interaction norm and exact finite-domain identity. That cluster expansion is not established here. This verifies the surface-pressure argument recommended by round 4, not the full Hexagon theorem. No novelty claim is made for the entropy method or the safe-state mechanism.

## Checks and commands

Run from this folder:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 prior_check_geometry.py > prior_geometry_output.txt
OMP_NUM_THREADS=1 nice -n 15 python3 prior_recheck_replacement.py > prior_replacement_output.txt
OMP_NUM_THREADS=1 nice -n 15 python3 check_surface.py > surface_output.txt
OMP_NUM_THREADS=1 nice -n 15 python3 audit_calculations.py > calculation_audit.txt
OMP_NUM_THREADS=1 nice -n 15 python3 audit_artifacts.py > artifact_audit.txt
```

The `prior_` files are copies; no earlier folder was modified. New exact checks cover 18 free and 162 conditioned intervals, 189 irregular free and 756 irregular conditioned domains, safe-event probabilities and density ratios. Direct configuration sums agree with transfer matrices and a separate spectral formula. The pressure also equals stationary entropy minus energy. Eighteen finite-block entropy checks supplement the analytic argument. Examples have correlation lengths up to about 20,099 cells, and the family has unbounded correlation length as its parameter grows; the theorem does not use a correlation-length bound.

A separate rational convolution checks both conditioned and free centering identities in 756 cases each, including the diagonal correction and both boundary signs. All surface constants are re-derived by separate coefficient arithmetic. The final artifact audit checks saved results, syntax, resource bounds and report format.

All computations use one OpenMP thread and effective nice 20, below the requested priority. The `nice` warning reports an unsuccessful attempt to raise that inherited priority to 15. The largest run used about 57.5 MB and 3.9 seconds; new computations use under 20 MB and one second each. Commands and detailed outputs are in [LOG.md](LOG.md) and the saved output files.

## Failures, sources and limits

No failed exact check or counterexample to the stated theorem was found. Removing the safe-state hypothesis does fail: equal-state hard constraints with opposite pinned boundaries have partition function zero. Removing connectedness of soft supports also fails: summable horizontal `1/n^2` pair constants give a finite-size error of order `N log N` in a square with boundary of order N. These are scope checks, not flaws in the manuscript. A displayed eigenvector typesetting slip was corrected before verification.

The initial literature check ended within five minutes. Opened [Qidong He, Ian Jauslin, Joel Lebowitz, Ron Peled, arXiv:2510.24825](https://arxiv.org/abs/2510.24825), which retains the boxed interaction; [Francesco Baffioni, Tobias Kuna, Immacolata Merola, Errico Presutti, arXiv:2611.05641](https://arxiv.org/html/2611.05641v1), which retains higher-body interactions; and the [Hexagon manuscript](https://hexagonmath.org/2610.00734v1), credited as generated by GPT-6 Astra and prompted by Qidong He, which remains unverified. Its [actual TeX source](https://hexagonmath.org/api/v1/works/2610.00734v1/source?path=liquid-solid.tex) was opened through the source-files page after direct opens failed. No verified newer solution was found; no SOLVED_ELSEWHERE.md is warranted. The Hexagon identifier is not an arXiv identifier.

The theorem's continuum constants depend on fixed geometry; the required lower threshold on R may depend on delta and the chosen periodic packing. There is no uniform estimate as delta tends to zero at fixed R. The explicit constant 5 is sufficient, not claimed optimal. No contour-weight bound, truncation removal or distinct-density infinite-volume Gibbs measures are proved. T081 remains unresolved by this work.

## Next step

Audit the Section 6 fixed-background polymer expansion: establish its interaction norm on the full product macrostate space and its exact finite-domain identity, with repeated contours, nested supports and overlapping exterior collars. Check whether recursive activities are independent of the surrounding domain and depend only on their stated exterior collar. With that input established, the present surface theorem and rounds 3–4 can be used directly; the remaining new analytic step is the defect-energy estimate and the final parameter inequalities.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 Nov 2026, 08:05:55 Asia/Tbilisi (first recorded session clock).
