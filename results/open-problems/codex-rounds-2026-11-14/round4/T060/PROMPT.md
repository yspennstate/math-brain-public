# Open problem T060: The Haldane conjecture for integer-spin chains

Statement: The spin-1 antiferromagnetic Heisenberg chain H = Σ_x S_x·S_{x+1} has a unique infinite-volume ground state, a spectral gap above it, and exponentially decaying correlations; more generally antiferromagnetic Heisenberg chains are gapped for integer spin and gapless for half-integer spin.

Source: F. D. M. Haldane, Nonlinear field theory of large-spin Heisenberg antiferromagnets, Phys. Lett. A 93 (1983); F. D. M. Haldane, Continuum dynamics of the 1-D Heisenberg antiferromagnet, Phys. Rev. Lett. 50 (1983)

Where it stands (checked by us, Nov 2026): The AKLT chain, a different spin-1 Hamiltonian, is gapped (Affleck–Kennedy–Lieb–Tasaki 1987); half-integer chains cannot have a unique gapped ground state (Lieb–Schultz–Mattis 1961; Affleck–Lieb 1986); a loop-model reformulation (Aizenman–Nachtergaele 1994). Open for the spin-1 Heisenberg chain.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T060 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T060 (read it,
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
VERDICT: PARTIAL uniform-density restriction on competing ground states, assuming the published translation-invariant uniqueness and purity theorem

The new result beyond the earlier report is in [PROOF.md](PROOF.md): every algebraic ground state agrees with the known state's marginal on any fixed block outside a set of positions of vanishing upper Banach density. Convergence is uniform over competing ground states and starting positions of the averaging intervals. The mean block trace distance tends to zero as well. In particular, every ground state with any finite translation period equals the known state.

The external premise is the uniqueness and purity assertion in **Hal Tasaki**, *On the uniqueness of translation-invariant ground states of the S=1 Heisenberg and J–D antiferromagnetic chains*, [arXiv:2610.34330v2, Theorem 2.1](https://arxiv.org/html/2610.34330v2). The proposition is proved here from that premise, using compactness, translation averages and purity. It requires no additional numerical inputs. This is a new deduction relative to the earlier report; no literature priority is claimed for the abstract lemma.

The earlier report's main scope distinction holds. Its periodic-gap implication was independently re-derived from Gibbs probabilities, including ground-state multiplicity and the strict lower bound log(20)/784, conditional on the published purity estimates. There was no earlier computation or PROOF.md to rerun. Neither session independently certifies the finite trace inputs. The bounded literature check found no later resolution of unrestricted infinite-volume uniqueness; the already reported periodic result does not resolve that remaining question. The opened sources and queries are in [LOG.md](LOG.md).

The audit gives two proofs of finite-period exclusion and two independent matrix-norm estimates. It also supplies a fully worked single-defect example showing why compactness, purity and averaging alone cannot imply equality of all states. That example is a set of states, not a Heisenberg ground-state construction. Thus the attempted extension to full uniqueness fails at an identified point: sparse discrepancies remain possible under the abstract premises.

No computation script or numerical experiment was needed. Readback and final artifact checks used:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 /bin/sh -c 'wc -l -c LOG.md PROOF.md; sed -n "1,240p" PROOF.md'
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 /bin/sh -c 'head -n 1 REPORT.md; wc -l -c REPORT.md PROOF.md LOG.md; test -s REPORT.md && test -s PROOF.md && test -s LOG.md'
```

The sandbox rejected priority adjustment with `nice: setpriority: Operation not permitted`; only brief file reads ran. The original paper's mirror also failed to reopen. All writes stayed in this folder; no git, subagents, external messages or heavy workloads.

There is no quantitative convergence rate for Heisenberg competitors, no independent certificate verification, and no proof of unrestricted uniqueness or of the general integer-spin assertion. The next worker should use the Heisenberg local stability condition to prove a discrepancy-amplification lemma: if a competing ground state differs on some finite block, then some fixed-size local discrepancy occurs on a set of positive upper Banach density. Combined with the proposition, such a lemma would imply unrestricted uniqueness. The single-defect example shows that this step needs Hamiltonian-specific input.

Task: “take the NEXT checkable step on this problem, building on that work” — November 15, 2026, 01:06:28 Asia/Tbilisi (session start).
