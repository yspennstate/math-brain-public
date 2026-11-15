# Open problem T092: Simple Lebesgue spectrum for a transformation of a probability space (Banach's problem, finite-measure form)

Statement: Is there an invertible measure-preserving transformation T of a probability space (X, μ) whose Koopman operator f ↦ f∘T, restricted to the orthocomplement of the constants in L²(μ), has simple Lebesgue spectrum, that is, is unitarily equivalent to multiplication by z on L²(S¹, Lebesgue measure)?

Caveat: Banach's question as recorded by Ulam is for the real line with Lebesgue measure, an infinite measure; for that version el Abdalaoui claims positive answers with conservative maps (arXiv:1508.06439; arXiv:2210.15480). The finite-measure version, which el Abdalaoui attributes to Rokhlin, is the open one (arXiv:2210.15480v2, introduction).

Source: S. M. Ulam, A Collection of Mathematical Problems (Interscience, 1960), reprinted as Problems in Modern Mathematics (Wiley, 1964), p. 76, where Banach's problem from the Scottish Book is restated; A. Katok and J.-P. Thouvenot, Spectral properties and combinatorial constructions in ergodic theory, in Handbook of Dynamical Systems, vol. 1B (Elsevier, 2006); E. H. el Abdalaoui, L¹-flat polynomials and simple Lebesgue spectrum for conservative maps exist: a simple proof, arXiv:2210.15480

Where it stands (checked by us, Nov 2026): For probability-preserving transformations, Lebesgue spectrum of finite multiplicity is not known to occur. A Lebesgue component of multiplicity two occurs (Mathew–Nadkarni, Bull. London Math. Soc. 16 (1984)), Lebesgue components of every even multiplicity occur (Ageev, Sb. Math. 64 (1989)), and many other spectral multiplicity sets are realized (survey: Danilenko, arXiv:1104.1961, Ergodic Theory Dynam. Systems 33 (2013)); a Lebesgue component is not pure simple Lebesgue spectrum. Open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T092 (read it,
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
VERDICT: PARTIAL located an exact claimed external solution; validity not independently verified

An OpenAI preprint dated September 23, 2026 claims the exact finite-probability
conclusion of T092. Reference, repository identifier, theorem scope, and
proof-artifact links are in [SOLVED_ELSEWHERE.md](SOLVED_ELSEWHERE.md).
No arXiv id was located. The search therefore triggered the external-result
branch; no new special case or construction was attempted.

What was checked: the primary introductory TeX, citation README, final
diagonal argument, Lean scope note, comparator configuration, and named
top-level solution source were opened. The claimed orthonormal-basis
statement was independently checked to imply the precise Koopman model:
the assignment Uⁿf ↦ zⁿ extends to a unitary intertwiner by completeness
and orthonormality. This confirms scope, not the construction's validity.

Search commands were web-tool queries, including:

```
Banach problem simple Lebesgue spectrum probability preserving 2025 2026
"simple Lebesgue spectrum" "2024" "2025"
"2210.15480"
"A smooth three-torus diffeomorphism with simple Lebesgue spectrum" arxiv
"A smooth three-torus" error OR gap OR review OR counterexample
"ThreeTorus.lean" "simple_lebesgue_spectrum"
```

Local commands were read-only startup, directory, clock, and compute-state
checks. Files were written with apply_patch. Full chronology and useful
outputs are in [LOG.md](LOG.md). No numerical computation was needed.
The sandbox denied `nice -n 15` on the final tiny file checks; no substantive
compute or build was launched.

What failed or remains uncertain: the raw PDF was not parsed by the web
tool, so manuscript inspection used its TeX. No independent review was
established. The actual Lean solution source was located, but neither its
dependency closure nor its compilation was checked. A top-level proof body
and a scope note do not certify a result. T092 must not be marked settled
solely on this report.

Next worker: validate the named solution theorem and its definitions using
the comparator configuration, then audit the finite-stage construction in
the manuscript. Check resources before attempting a Lean build; it was not
shown to fit this session's 1 GB limit. If validation fails, retain the
claim notice and resume the special-case/reduction branch.

Task: “push this problem forward by one checkable piece” — received by this
worker 2026-11-14 21:58 +04 (Asia/Tbilisi).
