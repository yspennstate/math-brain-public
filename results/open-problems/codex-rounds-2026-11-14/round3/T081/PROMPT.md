# Open problem T081: The liquid–vapour transition for continuum particles with pair interactions

Statement: Classical point particles in R^d, d ≥ 2, interacting through a fixed stable, translation-invariant pair potential with a short-range repulsion and a finite-range attraction (of Lennard-Jones type) have a liquid–vapour transition: for some temperature and chemical potential there are two infinite-volume Gibbs measures with different densities.

Caveat: The class of potentials must be fixed; the known proofs add Kac scaling, a four-body repulsion or an attraction tied to a fixed partition of space.

Source: J. L. Lebowitz, A. Mazel and E. Presutti, Liquid–vapor phase transitions for systems with finite-range interactions, J. Stat. Phys. 94 (1999); D. Ruelle, Existence of a phase transition in a continuous classical system, Phys. Rev. Lett. 27 (1971)

Where it stands (checked by us, Nov 2026): Proved with Kac potentials at small scale parameter and a four-body repulsion (Lebowitz–Mazel–Presutti, arXiv:cond-mat/9809145, J. Stat. Phys. 1999), for the Widom–Rowlinson model (Ruelle 1971; a stochastic-geometric proof by Chayes–Chayes–Kotecký, CMP 1995) and the continuum Potts model (Georgii–Häggström, CMP 1996). With pair interactions only, He–Jauslin–Lebowitz–Peled (arXiv:2510.24825) prove it at a fixed small Kac parameter in a boxed model whose attraction follows a fixed partition into cubes, so not translation invariant. Open for translation-invariant pair potentials.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T081 (read it,
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
VERDICT: PARTIAL exact obstruction to removing the boxed partition by common-shift Boltzmann averaging

For a stable boxed hard-core interaction with equal within-cube and neighboring-cube attraction, [PROOF.md](PROOF.md) derives the translation-invariant pair potential obtained by averaging its energy over grid translations. It is a hard core plus an explicit finite-range sum of tent products.

Averaging its Boltzmann weight gives a different result. Two pairs, each of length (3L/2), separated by any integer (M\geq3) cube sides in a transverse direction, have isolated weights ((1+q)/2) and joint weight ((1+q^2)/2), where (q=e^{\beta j}>1). Their joint weight exceeds the product by exactly ((q-1)^2/4), independently of their separation. The resulting effective energy therefore has no pair representation and is not additive beyond any finite range. The strict discrepancy persists on an open set of configurations.

For (n) such distant pairs, the effective energy minus the averaged energy, divided by the (2n) particles, tends to (-j/4). Thus there is also no uniform subextensive error bound between these two averages over all finite configurations. This is a statement about finite configurations, not about their equilibrium prevalence.

The concrete piece completed is an audit of this averaging shortcut. No liquid–vapour transition is proved, and no novelty claim is made for the general hidden-variable mechanism.

## Verification

Run from this folder:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 check_averaging.py > check_output.txt
```

The run passed 784 exact rational checks of the tent kernel, 24 four-particle checks in dimensions 2 and 3, variance checks at (q=2,3,5), and checks of one through eight distant pairs. Data are in [averaging_checks.json](averaging_checks.json); full output and the command are in [LOG.md](LOG.md) and [check_output.txt](check_output.txt).

The stability constant was re-derived using the occupation quadratic form. The four-particle discrepancy was re-derived as a Bernoulli variance; a half-cube shift reverses its sign relative to the product weight. The extensive limit was derived both through a hyperbolic cosine and directly from the two possible energies. Sub-core separations were checked separately: weight averaging also fails to preserve the hard core.

The checker used about 17.4 MB peak RSS and finished in about 0.03 seconds. `nice -n 15` printed a sandbox priority warning; the inherited effective nice was 20, which the script checked. No heavy computation was run.

## Literature check

The search took less than ten minutes. The opened [Qidong He, Ian Jauslin, Joel Lebowitz, Ron Peled paper, arXiv:2510.24825](https://arxiv.org/html/2510.24825v1), retains the fixed partition. The opened [Francesco Baffioni, Tobias Kuna, Immacolata Merola, Errico Presutti paper, arXiv:2611.05641](https://arxiv.org/html/2611.05641v1), treats a quantum LMP model with four-body interactions.

An additional [Hexagon manuscript](https://hexagonmath.org/pdf/2610.00734v1), dated 31 October 2026, claims the target hard-sphere/Kac coexistence theorem. Its first page credits generation to GPT-6 Astra, prompting to Qidong He, and explicitly says the results are not human-verified. Its proof was not verified here. This is an unresolved claim requiring audit, so SOLVED_ELSEWHERE.md was not created. Its Hexagon identifier is **not** an arXiv identifier: [arXiv:2610.00734](https://arxiv.org/abs/2610.00734) is an unrelated paper by Jon Lee.

## What failed and what remains uncertain

Common-shift Boltzmann averaging fails to preserve pair interactions, even though each fixed-grid Hamiltonian has finite range. Energy averaging preserves pair form, but this supplies no transfer of phase coexistence. Mixtures of normalized infinite-volume Gibbs measures have not been analyzed; their conditional grid distributions require separate work. No flaw in the Hexagon coexistence manuscript is established here, and the bounded search does not certify that no solution exists elsewhere.

## Next step

First audit the recent Hexagon claim, particularly its exact contour replacement and microscopic-background integration. If that claim does not settle the problem, work directly with the explicit averaged pair potential (5) in PROOF.md. A useful next statement would control its constrained partition functions or contour costs without interchanging energy averaging and Boltzmann averaging. The sparse configurations above rule out an unrestricted subextensive comparison; any successful comparison needs additional hypotheses on configurations or ensembles.

Task: “push this problem forward by one checkable piece” — 14 Nov 2026, 21:57 Asia/Tbilisi (session receipt).
