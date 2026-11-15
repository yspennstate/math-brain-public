# Open problem T097: Critical behaviour of level-set percolation of the three-dimensional Gaussian free field

Statement: For the discrete Gaussian free field φ on Z^3, the excursion set {φ ≥ h} has an infinite cluster for h < h_* and none for h > h_*. Determine its behaviour at and near h_*: whether the percolation probability, the correlation length and the one-arm probability at h_* follow power laws, with which exponents, and whether these agree with those of the cable-system field.

Caveat: On the metric graph (cable system) the critical level is 0 and several exponents are known exactly; the lattice field has h_* > 0 and is not covered by those results.

Source: A. Drewitz, A. Prévost and P.-F. Rodriguez, Critical exponents for a percolation model on transient graphs, Invent. Math. 232 (2023), 229–299; H. Duminil-Copin, S. Goswami, P.-F. Rodriguez and F. Severo, Equality of critical parameters for percolation of Gaussian free field level sets, Duke Math. J. 172 (2023)

Where it stands (checked by us, Nov 2026): The transition is sharp, h_* = h_** = h̄ (Duminil-Copin–Goswami–Rodriguez–Severo, arXiv:2002.07735), and h_* > 0 on Z^d for every d ≥ 3 (Drewitz–Prévost–Rodriguez, arXiv:1708.03285). On the cable system h_* = 0 (Lupu 2016) and critical exponents are computed in low dimensions (Ding–Wirth, Ann. Probab. 48 (2020); Drewitz–Prévost–Rodriguez, Invent. Math. 232 (2023); Cai–Ding, arXiv:2406.02397, which gives the one-arm probability up to constants for 3 ≤ d ≤ 5); the recent arXiv:2406.02397 and arXiv:2610.03703 are also about the cable system. For the lattice field no critical exponent is known to exist.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T097 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T097 (read it,
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
VERDICT: PARTIAL an optimized shell capacity bound and an explicit relative crossover coefficient

The earlier report's Gaussian comparison and its three main consequences
hold under independent verification. No subsequent solution of the lattice
critical-exponent problem was found in the requested brief web check.

The new piece is the exact optimization of its capacity test function over
functions constant on sup-norm shells. For simple-random-walk Green
covariance, PROOF.md proves

    cap(B_R) <= A_R := [sum_{k=R}^infinity (2k+1)^(-2)]^(-1)
                    <= 4R+1/(3R),
    A_R = 4R+1/(3R)+O(R^(-3)).

This improves the earlier explicit bound (28R-1/R)/3 for every R>=1.
The value A_R is optimal within the shell class, not asserted to be the
actual capacity of the cube. Its proof is a finite-annulus quadratic
minimization followed by a positive rational telescoping identity.

For the same relative one-arm radius as in the earlier report,

    L_rel(t) = min{R>=1: p_R(h_*+t)<=p_R(h_*)/2},

the refined comparison and the earlier critical arm bound give

    liminf_{t->0} t^2 log(1/t) L_rel(t) >= (log 2)^2/32.

This replaces an unspecified small constant by an explicit asymptotic
lower coefficient. It uses the existing density theorem of Stephen
Muirhead, [arXiv:2206.10724v2](https://arxiv.org/html/2206.10724v2), as the
earlier report did. No endpoint density estimate at exponent 4 is assumed.

AUDIT.md independently checks the minimization by Lagrange multipliers,
the coefficients 4 and 1/3 by an integral calculation, the rational
identity by symmetric algebra, and the coefficient 32 by optimized
Holder bounds. It also constructs increasing half-space events on the
same lattice Gaussian marginals for which a probability ratio drops below
1/2 even while t^2 cap(B_R) tends to zero. Thus removing the logarithmic
loss requires information specific to connection events.

Commands and output: no numerical script, simulation or numerical workload
was needed or run. Read-only commands were prefixed with
`OMP_NUM_THREADS=1 nice -n 15`; the sandbox denied the priority change.
Proofs and exact hand calculations are in PROOF.md and AUDIT.md. LOG.md
records the read commands, web queries, findings and final file checks.
All authored files are inside this folder. The earlier folder was read
only; no git, external writes or subagents were used.

What did not follow: the optimized shell profile does not change the power
or logarithmic order of the prior L_rel bound. It gives no connection-event
score improvement and no comparison to a two-point or crossing correlation
length. Exact lattice exponents, their existence, critical nonpercolation,
and agreement with cable exponents remain unresolved. Neither novelty of
these elementary refinements nor optimality of the displayed crossover
coefficient is established.

Next worker: seek a connection-specific bound on

    -d/dh log p_R(h)

near h_* that improves the general Gaussian scale
sqrt(cap(B_R) log(1/p_R(h))). A bound C sqrt(R), uniform for
h in [h_*,h_*+c/sqrt(R)], would remove the logarithmic loss in the lower
bound for this particular relative radius. Alternatively, compare L_rel
to a separately specified conventional correlation length. Further
optimization of deterministic shell functions cannot improve their
leading energy coefficient below 4.

Task: “take the NEXT checkable step on this problem, building on that work”
— 15 November 2026, first recorded local time 01:24:34 +04 (Asia/Tbilisi).
