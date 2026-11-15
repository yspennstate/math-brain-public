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

Later work: a round 5 worker built on the latest of these. Its folder is ~/codex_op_1114r5/briefs/T092 (read it, never
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
VERDICT: PROVED a quantitative weighted residue-transport bound with explicit coefficient discrepancy

The round 4 analytic block estimate holds. Direct pairwise integration
reproduces its variance and predictor identities; the loss coefficient
243/82 and the diagonal-transfer tolerance also check out. The bounded
literature check found no newly verified resolution of the finite-measure
problem. The previously located OpenAI claim remains unverified here.

The new result in [PROOF.md](PROOF.md) is a finite bound for the
residue-density step of a linear-jitter passage. For P residues, slope L,
and passage integer N, it bounds the sum of all folded residue errors by

    E_N + (B-A) J_1/N + J_2/N^2 + P H/(2L) + C_cut.

E_N is the actual coefficient-intensity discrepancy; the next two terms
bound sampling the slow argument; H is a weighted derivative integral;
C_cut is removed mass. Every quantity is defined in the proof. The
sampling terms have no factor P. The estimate allows negative indices,
arbitrary residue offsets, and all positive N, without requiring P to
divide N.

The derivative coefficient 1/2 in the underlying lattice quadrature
bound improves the coefficient 1 used in the inspected neutral-refresh
calculation. Two proofs and smooth extremizing bumps establish that
local coefficient's sharpness. No historical novelty is claimed for
this elementary inequality or for the qualitative residue-balancing idea.

A second bound expresses E_N using the L2 error eta_N between the
exact complex Fourier array and its proposed leading array, together
with an explicit rounding error. It shows exactly how eta_N->0 would
complete this density step. This convergence is not proved or assumed
as an unconditional construction result.

The inspected source is **OpenAI**, *A smooth three-torus diffeomorphism
with simple Lebesgue spectrum*, September 23, 2026; no arXiv identifier
was located. Its [passage section](https://raw.githubusercontent.com/openai/math/main/preprints/A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026/build/sections/02-passages.tex)
contains the fine-density and neutral-refresh formulas, especially
`neutral-riemann-error`. Its [signal section](https://raw.githubusercontent.com/openai/math/main/preprints/A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026/build/sections/03-signals.tex)
uses refreshed residues for transmission. These mutable main-branch
sources were opened; no formal proof replay was performed.

Commands and checks are in [LOG.md](LOG.md). Read all three earlier
reports, logs and available proofs; their directories contain no scripts.
Web searches were the exact title and `"Banach" "simple Lebesgue"
"2026" probability`, followed by primary-source opens. Tiny local reads
used `env OMP_NUM_THREADS=1 nice -n 15 /bin/sh -c '...'`; the sandbox
refused priority adjustment. No numerical computation, script, Lean build,
git operation or external write ran. Files were saved with apply_patch.

What failed or remains uncertain: no contradiction to the geometric
producer was found. This verifies its weighted residue-density mechanism
conditional on a measured coefficient error. It does not certify the
stationary-phase estimate, simultaneous support and physical smooth
control, transmission, or the limiting spectral conclusion. Banach's
finite-measure problem remains unresolved here.

Next worker: prove or refute eta_N->0 for the exact coefficient array
with the retained support cutoffs. The required normalization and the
rounding-removal bound are now explicit in (16)--(18) of PROOF.md.
In particular check uniformity when a stationary point enters or leaves
the coefficient support and summability over all j. After that, audit
simultaneous physical smooth closeness and support tracking before
combining refresh with transmission. Repeating the scalar block or
residue quadrature proofs is unnecessary.

Task: “take the NEXT checkable step on this problem, building on that
work” — received 2026-11-15 approximately 08:13 +04 (Asia/Tbilisi).
