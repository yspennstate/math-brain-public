# Open problem T347: The Amit–Gutfreund–Sompolinsky capacity of the Hopfield model

Statement: In the Hopfield model with N neurons and M = alpha·N iid uniform ±1 patterns xi^mu, with energy H(sigma) = −(1/(2N)) Σ_mu (Σ_i xi_i^mu sigma_i)², prove that at zero temperature there are, with high probability, local minima of H (fixed points of the zero-temperature dynamics) with overlap close to 1 with each pattern if and only if alpha < alpha_c, where alpha_c ≈ 0.138 is the replica-symmetric value of Amit, Gutfreund and Sompolinsky; and prove the replica-symmetric free energy in the retrieval phase.

Caveat: Retrieval states are proved to exist for small alpha (Newman: alpha < 0.056; Loukianova: alpha < 0.071; to verify Talagrand's bounds; Feng, Shcherbina and Tirozzi, arXiv:math-ph/0012038, state that a stable fixed point exists with probability tending to one for alpha <= 0.113, with retrieval errors matching the replica prediction at small alpha, to verify); the replica-symmetric formula is proved at high temperature or small alpha (Talagrand; Bovier and Gayrard). The threshold 0.138 is not proved.

Source: D. J. Amit, H. Gutfreund and H. Sompolinsky, Storing infinite numbers of patterns in a spin-glass model of neural networks, Phys. Rev. Lett. 55 (1985) 1530; M. Talagrand, Rigorous results for the Hopfield model with many patterns, Probab. Theory Related Fields 110 (1998) 177-276

Where it stands (checked by us, Nov 2026): Open (the 0.138 threshold).

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T347 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T347 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T347 (read it,
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
VERDICT: PROVED strict decrease of a limiting shell profile does not exclude strict local minima for correlated binary Hopfield patterns

The round-3 result holds under independent rechecking. Its flat-profile
limitation is removed: [PROOF.md](PROOF.md) constructs distinct binary
patterns with a strictly decreasing limiting shell ground-state profile
around a stored reference, although that reference is a strict single-spin
local minimum with a positive limiting flip cost.

For K=2^q, B>=3, N=BK and M=2K-1, the construction has exact energy
numerator

Q=2K sum_z S_z^2-(sum_z S_z)^2.

At distance d from the all-positive stored reference, with r=d mod B,
the shell energy-gain profile is exactly

E_N(d)=1-m_d^2/2-4K r(B-r)/N^2.

It converges uniformly to E(m)=1-m^2/2, strictly decreasing on [0,1].
Nevertheless, exactly 2^K configurations are local minima: all states
constant within each block. Every stored pattern is one of them. All
are strict and every spin flip costs at least 2(1-M/N). At B=14, the
limiting load is 1/7 and the limiting minimum flip cost is 12/7.
The strict-decrease assertion concerns the constant stored reference,
not every stored reference. The patterns are correlated, with antipodal
pairs and repeated neuron rows inside blocks. This does not refute an
iid capacity theorem.

New beyond round 3: strict profile decrease replaces a flat profile;
the shell maximum is given by an exact formula; all local minima are
classified and counted; and every pattern is itself stable, with no
core correction. A block reversal gives a path to a lower-energy state
with a barrier of order one in total energy. Normalizing energy by N
removes this barrier even though the limiting profile has a strict slope
at the reference.

Reproduce from this folder:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 recheck_previous.py
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 audit_strict_profile.py
```

[recheck_previous.py](recheck_previous.py) uses weighted cuts to verify
the earlier 12-spin certificate and a different Walsh instance, with
65,536 states. [audit_strict_profile.py](audit_strict_profile.py) checks
all actual projection energies and all neighbors for instances up to
16 spins, independently checks shell optima by dynamic programming,
and checks stability at every stored pattern of a 224-spin instance.
The resource-audited run took 0.524 seconds and used 14.375 MiB peak RSS.
Actual niceness was 20: the sandbox rejects increasing it to 15.
Commands and exact output are in [LOG.md](LOG.md).

What failed: no mathematical verification failed. Boundary checks show
that B=1 loses reference stability and B=2 loses a positive limiting
margin. No iid exclusion bound was obtained. The AGS threshold and the
replica-symmetric free energy remain unresolved in this work.

The bounded literature update found no newer solution. Opened sources
still show only v1: Ayman Ali, Jeanne Boursier, Hong-Bin Chen, Fu-Hsuan Ho,
Victor Issa, Jean-Christophe Mourrat, *Free energy of the Hopfield model*,
[arXiv:2611.03306v1](https://arxiv.org/html/2611.03306v1); and Yuwen Zhou,
*THE CRITICAL CAPACITY OF THE HOPFIELD MODEL*,
[Hexagon 2611.00105v1](https://hexagonmath.org/pdf/2611.00105v1).
Their full proofs and numerical capacity certificates were not audited.

Next worker: an upper bound for iid retrieval minima needs an explicit
probabilistic estimate for simultaneous zero-diagonal stability within
a fixed numerical error cap. Strict decrease of a uniformly convergent
shell profile alone is insufficient, even with nonvanishing single-spin
stability and linearly many distinct stored patterns. Use this example
to test any proposed deterministic reduction before applying iid bounds.

Task: “take the NEXT checkable step on this problem, building on that work.” Start: 15 November 2026, 06:32 +04.
