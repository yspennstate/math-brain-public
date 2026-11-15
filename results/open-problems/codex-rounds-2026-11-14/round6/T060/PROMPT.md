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

Later work: a round 5 worker built on the latest of these. Its folder is ~/codex_op_1114r5/briefs/T060 (read it, never
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
VERDICT: PARTIAL a competing ground state's norm distance survives removal of every finite interval, conditional on the published local gap inequality

The new result beyond round 4 is proved in [PROOF.md](PROOF.md). For the known state omega and every competing algebraic ground state rho,

`||(rho-omega)|A_(I^c)|| = ||rho-omega||`

for every finite interval I. Thus a ground state whose discrepancy vanishes in norm outside growing intervals equals omega. Any distinct pure ground state would remain perfectly distinguishable from omega outside every finite interval: the distance there is exactly two, without the factor one half. These are general deductions from the local gap premise; no literature priority is claimed.

The proof splits a competitor into a normal ground-state component p omega and a disjoint ground-state component of weight 1-p. It verifies that the components are ground states, rather than assuming this from convexity. Removing a finite interval removes a finite matrix tensor factor and preserves the sector weight p. Both the full norm distance and every complement norm distance are exactly 2(1-p). Equivalently, for each fixed n, the reduced-state trace distances on `[-m,-n-1] union [n+1,m]` increase to the full norm distance as m tends to infinity. Purity of omega is not needed for this result.

Round 4's normal-sector exclusion holds. It was re-derived using purification and negative-frequency averages, independently of its trace-class eigenvector decomposition. The frequency sign was checked in a two-level system. The new factor two was checked using both central projections and positive/negative functional masses, and directly in a ferromagnetic Ising chain whose product-state GNS gap is exactly two. No numerical computation was required.

The external spin-1 premise remains **Hal Tasaki**, *On the uniqueness of translation-invariant ground states of the S=1 Heisenberg and J–D antiferromagnetic chains*, [arXiv:2610.34330v2, Theorem 2.1, equation (2.12)](https://arxiv.org/html/2610.34330v2). Its finite numerical inputs were not independently verified. The bounded literature check found no later resolution of unrestricted uniqueness.

The stronger attempted inference from round 3's density condition fails. A product configuration with defects at powers of two has vanishing fixed-block discrepancy density but distance two on every complement. The proof gives the uniform density count and checks that this configuration violates local stability in the Ising test model. Another limitation is that distance strictly below two forces equality only for a pure competitor; mixtures can have any distance 2(1-p). The complement algebra includes joint observables on both sides of the removed interval, of unrestricted finite support size. No estimate for one half-chain alone is proved.

Readback and validation commands:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 /bin/sh -c 'wc -l -c LOG.md PROOF.md; cat PROOF.md; date "+%Y-%m-%d %H:%M:%S %Z"'
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 /bin/sh -c 'head -n 1 REPORT.md; wc -l -c REPORT.md PROOF.md LOG.md; test -s REPORT.md && test -s PROOF.md && test -s LOG.md; rg -n "tag|purity|irreducib|finite-range" PROOF.md'
```

Detailed outputs and the final audit are in [LOG.md](LOG.md). The sandbox rejected priority adjustment with `nice: setpriority: Operation not permitted`; only short file operations ran. No scripts, git, subagents, external messages or outside writes were used.

Unrestricted Heisenberg uniqueness remains unproved. The next step needs a Hamiltonian-specific bound on joint observables in the two exterior intervals, uniform in their lengths. One sufficient target for excluding a pure competitor is to bound its exterior trace distances by `2-eta`, for some eta>0 and one fixed removed interval, uniformly as the exterior blocks grow. Existing fixed-support density convergence does not provide that bound. For a general mixed competitor the theorem instead requires an estimate forcing p=1; a merely positive p is insufficient. No such estimate is established here.

Task: “take the NEXT checkable step on this problem, building on that work” — November 15, 2026, 07:48:50 Asia/Tbilisi (first retained explicit clock).
