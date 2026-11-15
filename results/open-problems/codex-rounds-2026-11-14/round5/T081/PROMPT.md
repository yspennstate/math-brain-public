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
VERDICT: PARTIAL geometric hypotheses verified for conditional contour replacement on connected-complement domains

The round 3 conditional replacement result holds on independent recheck. The new piece is a proof of its geometric inputs for the actual radius-one Chebyshev contour construction: constant phase collars, containment in recursion domains, strictly nested or separated filled supports, and the physical decomposition and reconstruction. The proof is in [PROOF.md](PROOF.md). The boundary argument specializes Ádám Timár's standard graph method; no novelty claim is made for these geometric facts.

The connected-complement restriction on recursion domains is essential. An explicit realizable shell has support `B_3 minus B_1`, enlargement `B_4 minus B_0`, and filled support `B_3`. Taking the enlargement as the domain omits the origin from the filled support. The source already excludes this perforated domain. This is a counterexample to an unrestricted geometric assumption, not an error in the manuscript or the earlier conditional theorem.

Together with round 3's algebra, the result removes the outstanding geometric assumptions for this construction on the stated domains. Finiteness and positivity of the continuum partition functions remain separate requirements. No surface-pressure estimate or liquid–vapour transition is proved.

## Checks

Run from this folder:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 recheck_replacement.py > recheck_output.txt
OMP_NUM_THREADS=1 nice -n 15 python3 check_geometry.py > geometry_output.txt
OMP_NUM_THREADS=1 nice -n 15 python3 audit_artifacts.py > artifact_audit.txt
```

The independent replacement checker passed 54 exact comparisons of physical enumeration, conditional recursion and explicit auxiliary-family sums. It uses three phases and three microscopic states, including an asymmetric tree. The hand examples recover 160 and 128 versus the incorrect independent-average value 144.

The geometry checker passed all 19,683 ternary labelings on a 3-by-3 window, 256 binary and 729 sparse ternary labelings in three dimensions, and 204 ordered pairs drawn from the 388 connected nonempty subsets of the 3-by-3 window. Explicit three-level nested contours and separated contours with overlapping exterior neighborhoods also pass. The small support counts are independently re-derived by bit-mask enumeration in the final audit. Shell volumes are checked both by local correctness and by cube subtraction.

The final geometry run used 57,163,776 bytes peak RSS and 2.404 seconds. The replacement recheck used 15,237,120 bytes and 0.084 seconds. Effective nice was 20; all programs assert one OpenMP thread. The `nice` warning comes from an unsuccessful attempt to raise the inherited priority to 15. All runs remain below the time and memory limits.

## Source audit, failures and limits

The initial newer-result search ended within five minutes. The opened [Qidong He, Ian Jauslin, Joel Lebowitz, Ron Peled paper, arXiv:2510.24825](https://arxiv.org/abs/2510.24825), retains the boxed interaction. The [Hexagon manuscript](https://hexagonmath.org/2610.00734v1), credited as generated by GPT-6 Astra and prompted by Qidong He, remains unverified. No verified newer solution was found, and no SOLVED_ELSEWHERE.md is warranted.

The actual [TeX definitions in Section 5](https://hexagonmath.org/api/v1/works/2610.00734v1/source?path=liquid-solid.tex) agree with those used here. [Ádám Timár, *Boundary-connectivity via graph theory*, arXiv:0711.1713v2](https://arxiv.org/pdf/0711.1713v2), Lemma 2, was opened and its graph assumptions checked. PROOF.md writes out the cycle-generation and cut-parity argument.

The first geometry run failed because the constructed dense-annulus example was incorrectly expected to have two contours. Its two interfaces and central star give three. The corrected expectation is independently checked by the three filled volumes. Negative tests also confirm the need for dimension at least two and for a support to be a full incorrect component. No counterexample to the stated geometric theorem was found.

The finite label checks do not establish continuum configuration volumes, mixing, pressure estimates, or the full Hexagon theorem. The main problem remains unresolved by this work.

## Next step

Audit the Section 4 surface-pressure argument and its Section 6 application to the truncated contour ensemble. Check uniformity in microscopic exterior configurations and the conditional-entropy boundary terms. The geometric family decomposition and the conditional cancellation can now be used as separately proved inputs, subject to finite positive partition functions.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 Nov 2026, 04:46:16 Asia/Tbilisi (first recorded session clock).
