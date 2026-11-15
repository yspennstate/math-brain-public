# Open problem T081: The liquid–vapour transition for continuum particles with pair interactions

Statement: Classical point particles in R^d, d ≥ 2, interacting through a fixed stable, translation-invariant pair potential with a short-range repulsion and a finite-range attraction (of Lennard-Jones type) have a liquid–vapour transition: for some temperature and chemical potential there are two infinite-volume Gibbs measures with different densities.

Caveat: The class of potentials must be fixed; the known proofs add Kac scaling, a four-body repulsion or an attraction tied to a fixed partition of space.

Source: J. L. Lebowitz, A. Mazel and E. Presutti, Liquid–vapor phase transitions for systems with finite-range interactions, J. Stat. Phys. 94 (1999); D. Ruelle, Existence of a phase transition in a continuous classical system, Phys. Rev. Lett. 27 (1971)

Where it stands (checked by us, Nov 2026): Proved with Kac potentials at small scale parameter and a four-body repulsion (Lebowitz–Mazel–Presutti, arXiv:cond-mat/9809145, J. Stat. Phys. 1999), for the Widom–Rowlinson model (Ruelle 1971; a stochastic-geometric proof by Chayes–Chayes–Kotecký, CMP 1995) and the continuum Potts model (Georgii–Häggström, CMP 1996). With pair interactions only, He–Jauslin–Lebowitz–Peled (arXiv:2510.24825) prove it at a fixed small Kac parameter in a boxed model whose attraction follows a fixed partition into cubes, so not translation invariant. Open for translation-invariant pair potentials.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T081 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T081 (read it,
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
VERDICT: PARTIAL conditional contour replacement verified under explicit geometric hypotheses

The earlier averaging obstruction holds. An independent exact midpoint-grid calculation confirms the excess `(q-1)^2/4` for aligned distant pairs, its negative for staggered pairs, and the extensive energy-gap limit `-j/4` per particle.

The new piece is an audit of the finite-volume replacement step recommended in the earlier report. [PROOF.md](PROOF.md) proves a conditional contour identity by induction, retaining microscopic boundary variables and nested contour families. Its assumptions explicitly include constant phase collars, separated complementary components, and the disjoint-or-nested geometry of compatible filled supports. No mixing assumption is used in this algebraic step. The general geometric assumptions themselves are not proved here.

The cancellation works because the nested auxiliary families reconstruct the physical same-phase interior partition functions before the maximal contour denominator cancels. It permits correlations through a shared microscopic background. It therefore avoids the independent averaging operation ruled out by the earlier work. No novelty claim is made for the replacement identity.

## Checks

Run from this folder:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 recheck_previous.py > recheck_output.txt
OMP_NUM_THREADS=1 nice -n 15 python3 check_replacement.py > replacement_output.txt
```

The first run passed 48 exact four-particle excess checks and distant-pair histograms through twelve pairs. The second passed 44 exact comparisons between physical-state enumeration, recursive ratios, and auxiliary-background integration on trees with one, three, and seven supports. Selected cases independently enumerate compatible-family subsets. Data are in [replacement_checks.json](replacement_checks.json).

Two hand-checkable examples give physical and conditional-replacement partition functions 160 and 128, while independently averaging activities gives 144 in both. Their discrepancies are independently recovered as covariances. Replacing a diluted-interior denominator by a pure-interior denominator gives 880 instead of 160; forbidding nested families gives 88. Dense-block shell geometry was checked separately in dimensions two and three. These finite-state and geometric examples do not certify the full continuum argument.

Both scripts finish in under a second, use under 20 MB peak RSS, and assert one OpenMP thread and effective nice at least 15. The inherited nice was 20. `nice` warns that it cannot change priority; the processes already have lower priority than requested.

## Source audit and limits

The initial newer-result search stayed within five minutes. No verified newer solution was found. The [Hexagon manuscript](https://hexagonmath.org/2610.00734v1), credited as generated by GPT-6 Astra and prompted by Qidong He, remains explicitly unverified. Its identifier is not an arXiv identifier.

An apparent wrong interior phase in its extracted PDF was rejected after opening the [actual TeX source](https://hexagonmath.org/api/v1/works/2610.00734v1/source?path=liquid-solid.tex): the numerator correctly uses `c_j`; extraction had dropped the subscript. This is not a flaw in the manuscript. The source's equation `eq:ratios` and Proposition 5.6 motivate the conditional identity checked here. The proof audit establishes only that algebra under the stated assumptions, not the manuscript's full theorem.

The [Qidong He, Ian Jauslin, Joel Lebowitz, Ron Peled paper](https://arxiv.org/html/2510.24825v1) still concerns the boxed model. No SOLVED_ELSEWHERE.md is warranted on this audit. The unrestricted translation-invariant pair-potential problem remains unresolved by this work.

## Next step

Audit the geometric hypotheses against the exact source definitions, especially constant collars and nesting of filled supports. Then examine the surface-pressure estimate and its application to the truncated contour ensemble, including uniformity over microscopic exterior states. A later worker can now treat the conditional algebra as a separately stated lemma, rather than repeat the common-shift averaging shortcut.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 Nov 2026, 01:18:37 Asia/Tbilisi (first recorded session clock).
