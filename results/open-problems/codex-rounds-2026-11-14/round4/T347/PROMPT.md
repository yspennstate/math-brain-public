# Open problem T347: The Amit–Gutfreund–Sompolinsky capacity of the Hopfield model

Statement: In the Hopfield model with N neurons and M = alpha·N iid uniform ±1 patterns xi^mu, with energy H(sigma) = −(1/(2N)) Σ_mu (Σ_i xi_i^mu sigma_i)², prove that at zero temperature there are, with high probability, local minima of H (fixed points of the zero-temperature dynamics) with overlap close to 1 with each pattern if and only if alpha < alpha_c, where alpha_c ≈ 0.138 is the replica-symmetric value of Amit, Gutfreund and Sompolinsky; and prove the replica-symmetric free energy in the retrieval phase.

Caveat: Retrieval states are proved to exist for small alpha (Newman: alpha < 0.056; Loukianova: alpha < 0.071; to verify Talagrand's bounds; Feng, Shcherbina and Tirozzi, arXiv:math-ph/0012038, state that a stable fixed point exists with probability tending to one for alpha <= 0.113, with retrieval errors matching the replica prediction at small alpha, to verify); the replica-symmetric formula is proved at high temperature or small alpha (Talagrand; Bovier and Gayrard). The threshold 0.138 is not proved.

Source: D. J. Amit, H. Gutfreund and H. Sompolinsky, Storing infinite numbers of patterns in a spin-glass model of neural networks, Phys. Rev. Lett. 55 (1985) 1530; M. Talagrand, Rigorous results for the Hopfield model with many patterns, Probab. Theory Related Fields 110 (1998) 177-276

Where it stands (checked by us, Nov 2026): Open (the 0.138 threshold).

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T347 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T347 (read it,
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
VERDICT: PARTIAL profile-well implication proved; converse fails for explicit correlated binary Hopfield patterns

The earlier report's main scope conclusion holds: the located equilibrium
formula and the claimed well-capacity threshold do not by themselves
establish T347's iff statement about individual local minima. The bounded
update search found no newer solution. No SOLVED_ELSEWHERE.md is warranted
for this session.

New beyond the earlier report: [PROOF.md](PROOF.md) gives a finite-volume
proof that a strict gap between two shell ground-state energies traps a
local minimum in the inner Hamming cap. It states the correct stability
condition with the diagonal removed and makes the simultaneous-pattern
probability requirement explicit. With iid patterns, sufficiently small
caps give distinct minima by a binomial tail bound.

The converse is tested rather than assumed. An exact 12-spin, 11-pattern
example has a monotone positive-overlap shell profile and a strict local
minimum that is suboptimal on its own shell. A Walsh/block construction
extends this to extensive load M/N -> 11/B: every stored pattern has a
strict local minimum within twelve flips, yet all limiting shell profiles
are constant. The minimum single-flip cost stays bounded away from zero.
For B=79 the limiting load is 11/79 = 0.139240506329..., but the patterns
are correlated. This is a counterexample to a general landscape inference,
not to an iid capacity theorem. The asymptotic proof uses elementary
uniform bounds and does not depend on exhaustive shell maxima.

Reproduction, from this folder:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 audit_landscape.py
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 audit_blocks.py
```

[counterexample.json](counterexample.json) is the exact finite certificate.
The base verifier checks all 4,096 energies using both pattern projections
and the Gram quadratic form, and checks each flip from its local field.
The block verifier checks every Gram entry of an actual 18-spin,
44-pattern array, enumerates all 262,144 states independently of its block
dynamic program, and checks all flips at the minima near every pattern.
Both scripts passed; the block run took 1.138 seconds. All computations
used one thread and small memory. The sandbox rejects changing inherited
niceness 20 to 15; actual verified priority was 20 throughout.

What failed: the first search selected a minimum that was shell-optimal,
which failed an extra certificate assertion. The search was corrected to
require suboptimality on its own shell; the successful example is seed
347, trial 620. There was no failure of the earlier report's mathematical
claim. The earlier folder contained no PROOF.md or computation scripts.

Limits and uncertainty: no new iid existence bound, exclusion bound,
threshold value, or replica-symmetric free-energy theorem is proved.
The full variational proof, uniform strict merging inequality and numerical
capacity certificates remain unaudited. The asymptotic counterexample has
a flat profile and strong correlations; it leaves open an exclusion theorem
using strict decrease plus quantitative iid information. A positive-
temperature free-energy gap alone is not the ground-state gap used here.

Next worker: take the iid upper direction seriously as a separate lemma.
Fix a numerical overlap/error criterion, and seek a uniform estimate for
the existence of shell-suboptimal single-spin minima in that cap when
the limiting profile is strictly decreasing. If instead auditing the
capacity preprint, check its merging and interval certificates first;
its barrier statement plus Proposition 1 here gives the lower landscape
implication only, conditional on that preprint's correctness.

Opened primary sources: Ayman Ali, Jeanne Boursier, Hong-Bin Chen,
Fu-Hsuan Ho, Victor Issa, Jean-Christophe Mourrat, *Free energy of the
Hopfield model*, [arXiv:2611.03306v1](https://arxiv.org/html/2611.03306v1);
*THE CRITICAL CAPACITY OF THE HOPFIELD MODEL*, contributed by Yuwen Zhou,
[Hexagon 2611.00105v1](https://hexagonmath.org/pdf/2611.00105v1).
Both still show only v1. Detailed commands, output and scope checks are in
[LOG.md](LOG.md).

Task: “take the NEXT checkable step on this problem, building on that work.” Start: 15 November 2026, 03:50 +04.
