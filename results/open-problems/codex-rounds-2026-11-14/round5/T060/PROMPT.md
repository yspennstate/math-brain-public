# Open problem T060: The Haldane conjecture for integer-spin chains

Statement: The spin-1 antiferromagnetic Heisenberg chain H = Σ_x S_x·S_{x+1} has a unique infinite-volume ground state, a spectral gap above it, and exponentially decaying correlations; more generally antiferromagnetic Heisenberg chains are gapped for integer spin and gapless for half-integer spin.

Source: F. D. M. Haldane, Nonlinear field theory of large-spin Heisenberg antiferromagnets, Phys. Lett. A 93 (1983); F. D. M. Haldane, Continuum dynamics of the 1-D Heisenberg antiferromagnet, Phys. Rev. Lett. 50 (1983)

Where it stands (checked by us, Nov 2026): The AKLT chain, a different spin-1 Hamiltonian, is gapped (Affleck–Kennedy–Lieb–Tasaki 1987); half-integer chains cannot have a unique gapped ground state (Lieb–Schultz–Mattis 1961; Affleck–Lieb 1986); a loop-model reformulation (Aizenman–Nachtergaele 1994). Open for the spin-1 Heisenberg chain.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T060 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T060 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T060 (read it,
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
VERDICT: PARTIAL exclusion of normal competing ground states, conditional on the published local gap inequality

The new result beyond round 3 is proved in [PROOF.md](PROOF.md): every algebraic ground state normal in the GNS representation of the known state equals that state. This excludes arbitrary local filtered defects, finite mixtures of them, and their limits in the norm of state functionals. Round 3's density conclusion alone did not exclude these possibilities. This is a general consequence of the gap premise, with a complete argument supplied here; no literature priority is claimed.

The external spin-1 premise is the local gap inequality in **Hal Tasaki**, *On the uniqueness of translation-invariant ground states of the S=1 Heisenberg and J–D antiferromagnetic chains*, [arXiv:2610.34330v2, Theorem 2.1, equation (2.12)](https://arxiv.org/html/2610.34330v2). Its finite numerical inputs have not been independently verified. The bounded literature check found no later resolution of unrestricted uniqueness.

The proof uses negative-frequency averages, which annihilate a ground vector in any ground-state representation. A trace-class decomposition transfers this annihilation to the vectors representing a normal competitor. Matrix elements against the known ground vector then eliminate every strictly positive-energy component; the gap inequality makes the zero-energy subspace one dimensional. No translation invariance is assumed for the competitor.

A separate direct calculation checks local unitary defects and supplies a quantitative statement: a block trace distance at least epsilon forces a local-stability violation at most `-gamma*epsilon^2/4`, where gamma is the local gap lower bound and trace distance has no factor one half. Both the sign and the coefficient were checked independently; the coefficient is sharp for the general premises in a two-level example.

The earlier density result holds: it was re-derived using measures on the compact ground-state set, pure-state barycenters, and continuity of block trace distance. The attempted extension from normal competitors to arbitrary local limits fails. An explicit product-state example in PROOF.md proves that weak-* limits of local unitary defects can leave the normal folium. Thus density convergence cannot simply be substituted for normality.

No numerical experiment or computation script was needed. Readback and artifact commands were:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 /bin/sh -c 'wc -l -c LOG.md PROOF.md; sed -n "1,280p" PROOF.md'
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 /bin/sh -c 'head -n 1 REPORT.md; wc -l -c REPORT.md PROOF.md LOG.md; test -s REPORT.md && test -s PROOF.md && test -s LOG.md'
```

The sandbox reports `nice: setpriority: Operation not permitted`; only short file operations ran. Detailed queries, commands, symbolic checks and limitations are in [LOG.md](LOG.md). All new artifacts are in this folder; earlier folders were read only.

Unrestricted uniqueness remains unproved. The next worker should investigate a Hamiltonian-specific normality criterion for a competing state satisfying round 3's density restriction. One concrete sufficient target is to construct local-filter mixtures converging locally to that state whose density operators in the known GNS representation are uniformly tight on finite-rank subspaces. Such tightness would give a trace-norm convergent subsequence and hence normality; local convergence by itself is insufficient. No such tightness estimate is established here.

Task: “take the NEXT checkable step on this problem, building on that work” — November 15, 2026, 04:31:30 Asia/Tbilisi (first recorded clock).
