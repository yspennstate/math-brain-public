# Open problem T092: Simple Lebesgue spectrum for a transformation of a probability space (Banach's problem, finite-measure form)

Statement: Is there an invertible measure-preserving transformation T of a probability space (X, μ) whose Koopman operator f ↦ f∘T, restricted to the orthocomplement of the constants in L²(μ), has simple Lebesgue spectrum, that is, is unitarily equivalent to multiplication by z on L²(S¹, Lebesgue measure)?

Caveat: Banach's question as recorded by Ulam is for the real line with Lebesgue measure, an infinite measure; for that version el Abdalaoui claims positive answers with conservative maps (arXiv:1508.06439; arXiv:2210.15480). The finite-measure version, which el Abdalaoui attributes to Rokhlin, is the open one (arXiv:2210.15480v2, introduction).

Source: S. M. Ulam, A Collection of Mathematical Problems (Interscience, 1960), reprinted as Problems in Modern Mathematics (Wiley, 1964), p. 76, where Banach's problem from the Scottish Book is restated; A. Katok and J.-P. Thouvenot, Spectral properties and combinatorial constructions in ergodic theory, in Handbook of Dynamical Systems, vol. 1B (Elsevier, 2006); E. H. el Abdalaoui, L¹-flat polynomials and simple Lebesgue spectrum for conservative maps exist: a simple proof, arXiv:2210.15480

Where it stands (checked by us, Nov 2026): For probability-preserving transformations, Lebesgue spectrum of finite multiplicity is not known to occur. A Lebesgue component of multiplicity two occurs (Mathew–Nadkarni, Bull. London Math. Soc. 16 (1984)), Lebesgue components of every even multiplicity occur (Ageev, Sb. Math. 64 (1989)), and many other spectral multiplicity sets are realized (survey: Danilenko, arXiv:1104.1961, Ergodic Theory Dynam. Systems 33 (2013)); a Lebesgue component is not pure simple Lebesgue spectrum. Open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T092 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T092 (read it,
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
VERDICT: PROVED a necessary orbit-count bound for finite-stage approximations near an invariant observable

The earlier report holds: the external claim has exactly the scope of
T092, and the named Lean solution has a proof body. Neither observation
validates its construction. The bounded literature check found no newly
verified resolution. Banach's finite-measure problem is not resolved by
this session.

The new mathematical result is the following. If U is unitary, g has an
orthonormal bilateral orbit, `A=||h||>0`, and a Laurent polynomial P
approximates h to error `ε<A`, then

\[
 \#\operatorname{supp}P\ge
       \frac{A^2-\varepsilon^2}{A\|Uh-h\|}.
\]

A zero denominator makes such an approximation impossible. Completeness
of the orbit is unnecessary. The proof and an independent Fourier
derivation are in [PROOF.md](PROOF.md). The coefficient inequality used
in the proof has optimal universal constant one; this is checked using
geometric sequences, with their sums evaluated two ways. No claim of
historical novelty for the underlying sequence inequality is made.

For a map R uniformly δ-close to a twist fixing the slow coordinate u,
take `h=sin(2 pi u)`. Any approximation with error at most half its norm,
using an orthonormal orbit for R, requires

\[
 \#\operatorname{supp}P\ge\frac{3}{8\sqrt2\,\pi\delta}.
\]

This gives a checkable constraint on the claimed finite construction:
polynomial support must diverge as physical perturbations shrink. It
does not refute that construction, whose polynomials are unrestricted.

The source audit goes beyond the earlier top-level inspection. It traces
the basis through the diagonal to `Stages.exists_one_stage`, then to
controlled prediction and whitening. The opened sources and precise
locations are in [CLAIM_AUDIT.md](CLAIM_AUDIT.md). The full dependency
closure and actual construction remain unchecked.

Commands and checks:

- Read-only `cat` of the earlier REPORT.md, LOG.md and claim notice;
  directory inspection confirmed there was no earlier PROOF.md or script.
- Web searches for the exact title, 2026 Banach/simple-Lebesgue results,
  and errors or reviews; primary-source `open` and `find` calls listed
  in [LOG.md](LOG.md) and CLAIM_AUDIT.md.
- Read the startup memory and compute-state file. Tiny shell reads used
  `env OMP_NUM_THREADS=1 nice -n 15`; the sandbox denied the priority
  adjustment. No computation script, Lean build, git or external write
  was run. Files were saved with apply_patch.
- Symbolic checks covered both signs of the orbit, proper cyclic
  subspaces, sparse polynomials, zero residual, and changing coordinate
  charts. The torus constant was re-derived after normalizing h.

What failed or remains uncertain: source inspection supplied no proof
certificate, and the finite-stage theorem has not been independently
proved or disproved. The count bound alone gives no contradiction,
because its required growth is allowed by the theorem. It gives no
upper bound on the polynomial support produced by that construction.

Next worker: audit the centered block estimates feeding
`actual_controlled_tagged_prediction` in ControlledBlocks, especially the
simultaneous prediction error and Hellinger-loss estimates. Compare their
eventual Laurent support with the necessary bound above in the fixed
twist/slow-coordinate test. A sufficiently large support passes this
necessary check but does not establish validity. Do not spend another
session merely locating the top-level theorem.

Task: “take the NEXT checkable step on this problem, building on that
work” — received 2026-11-15 01:20 +04 (Asia/Tbilisi).
