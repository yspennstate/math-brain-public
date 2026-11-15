# Open problem T092: Simple Lebesgue spectrum for a transformation of a probability space (Banach's problem, finite-measure form)

Statement: Is there an invertible measure-preserving transformation T of a probability space (X, μ) whose Koopman operator f ↦ f∘T, restricted to the orthocomplement of the constants in L²(μ), has simple Lebesgue spectrum, that is, is unitarily equivalent to multiplication by z on L²(S¹, Lebesgue measure)?

Caveat: Banach's question as recorded by Ulam is for the real line with Lebesgue measure, an infinite measure; for that version el Abdalaoui claims positive answers with conservative maps (arXiv:1508.06439; arXiv:2210.15480). The finite-measure version, which el Abdalaoui attributes to Rokhlin, is the open one (arXiv:2210.15480v2, introduction).

Source: S. M. Ulam, A Collection of Mathematical Problems (Interscience, 1960), reprinted as Problems in Modern Mathematics (Wiley, 1964), p. 76, where Banach's problem from the Scottish Book is restated; A. Katok and J.-P. Thouvenot, Spectral properties and combinatorial constructions in ergodic theory, in Handbook of Dynamical Systems, vol. 1B (Elsevier, 2006); E. H. el Abdalaoui, L¹-flat polynomials and simple Lebesgue spectrum for conservative maps exist: a simple proof, arXiv:2210.15480

Where it stands (checked by us, Nov 2026): For probability-preserving transformations, Lebesgue spectrum of finite multiplicity is not known to occur. A Lebesgue component of multiplicity two occurs (Mathew–Nadkarni, Bull. London Math. Soc. 16 (1984)), Lebesgue components of every even multiplicity occur (Ageev, Sb. Math. 64 (1989)), and many other spectral multiplicity sets are realized (survey: Danilenko, arXiv:1104.1961, Ergodic Theory Dynam. Systems 33 (2013)); a Lebesgue component is not pure simple Lebesgue spectrum. Open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T092 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T092 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T092 (read it,
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
VERDICT: PROVED a centered-block analytic transfer estimate with square-root loss at most 3 delta squared

The earlier orbit-count bound holds. This session independently derives
it in LOG.md, then follows the round 3 report into the centered-block
calculation. The bounded literature check established no newly verified
resolution of the finite-probability Banach problem.

The new result is a complete analytic single-block lemma in
[PROOF.md](PROOF.md). For nonnegative color densities of total mass at
most two, tags in the complex unit disk, and a center q bounded by two,
assume the weighted centering error is at most delta and
delta/2 <= n lambda^2 <= delta <= 1/100. The positive product-phase
model has square-root-integral loss at most

    (243/82) delta^2 < 3 delta^2.

Its estimator is unbiased separately at each temporal point and for
each color. The increase in the squared error against an arbitrary
previous bounded estimator is at most 4/delta.

Both estimates transfer simultaneously to literal diagonal Fourier
phases with arbitrary successive frequency lower bounds. They remain
valid, with additive tolerance nu, for any nonnegative final densities
within an explicit L1 error fixed before selecting those frequencies.
Measurable input densities and bounded measurable centers suffice.

This improves the coefficient 300 in the scalar transfer estimate
underlying the claimed construction to 3. The argument uses the unit-disk
constraint on the tags through a variance decomposition, rather than
bounding every color bias by three throughout. It validates and sharpens
this analytic part only. No historical novelty is claimed for the
individual inequalities.

The source inspected is OpenAI, *A smooth three-torus diffeomorphism with
simple Lebesgue spectrum*, September 23, 2026; no arXiv identifier was
located. The relevant [manuscript calculation](https://raw.githubusercontent.com/openai/math/main/preprints/A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026/build/sections/04-blocks.tex)
is at lines 272–415. Its [analytic transfer interface](https://raw.githubusercontent.com/openai/math/main/lean/OAI/Dynamics/ThreeTorus/ColorBlocks.lean)
is `block_diagonal_transfer`, lines 95–115. All inspected URLs use mutable
main-branch sources; no Lean compilation or certificate was obtained.

Checks and commands:

- Read both earlier REPORT.md and LOG.md files, the round 3 PROOF.md and
  CLAIM_AUDIT.md, and the original claim notice. Directory listings
  confirmed that neither earlier folder contains scripts.
- Web searches: `Banach simple Lebesgue spectrum probability transformation
  2026 solution` and `"Banach" "ControlledBlocks" spectrum`. Opened the
  primary introduction, arXiv:2210.15480, and the block sources named in
  LOG.md. General status searching stopped within five minutes.
- File reads and checks used `env OMP_NUM_THREADS=1 nice -n 15 /bin/sh -c
  '...'`; the sandbox refused the priority adjustment. No substantive
  computation, numerical script, Lean build, git or external write ran.
  Files were saved with apply_patch; wc, sed and tail checked the artifact.
- Re-derived the mixture variance by two methods, the estimator variance
  by two methods, and the constant comparison with exact rational
  arithmetic. Checked zero densities, one color, n=1, complex tags,
  conjugation symmetry, adaptive frequency bounds and perturbation errors.
  An explicit example shows that dropping the centering hypothesis permits
  first-order loss in delta.

What did not succeed: no contradiction was found in the scalar block
calculation. The result supplies no upper bound on Laurent support, so
the earlier orbit-count constraint still cannot refute the construction.
No physical passage, smooth perturbation estimate, finite-stage existence
theorem or limiting spectral conclusion has been certified. The constant
three is not asserted optimal. Banach's finite-measure problem remains
unresolved here.

Next worker: audit the geometric producer used by
`ColoredSignalControlledRealizes.iterate` and its input
`exists_refresh_transmit_reflected_state`, beginning with the residue
equidistribution and spectral-density transport estimates. The analytic
block now has an independent proof, including its tolerance and frequency
quantifiers. The unresolved question is whether actual packet passages
simultaneously realize those L1 errors, support tracking and physical
smooth closeness. Repeating the top-level trace or the block probability
calculation is unnecessary.

Task: “take the NEXT checkable step on this problem, building on that
work” — received 2026-11-15 04:47 +04 (Asia/Tbilisi).
