# Open problem T087: Existence and values of the critical exponents of three-dimensional percolation

Statement: For Bernoulli bond percolation on Z^3 the critical exponents exist: θ(p) = (p − p_c)^{β+o(1)} as p ↓ p_c, the mean cluster size is (p_c − p)^{−γ+o(1)} as p ↑ p_c, the correlation length is |p − p_c|^{−ν+o(1)}, and at p_c the one-arm probability P(0 ↔ ∂B_n) is n^{−1/ρ+o(1)} and the two-point function decays like |x|^{−(1+η)+o(1)}; and they satisfy the scaling and hyperscaling relations, for example γ = ν(2 − η) and 3ν = γ + 2β.

Caveat: Existence of the exponents is part of the problem. Their values are known only numerically (β ≈ 0.418, ν ≈ 0.876, η ≈ −0.046, from 1/ν = 1.1410(15) and β/ν = 0.47705(15) for bond and site percolation on the cubic lattice: Wang, Zhou, Zhang, Garoni and Deng, arXiv:1302.0421, Phys. Rev. E 87 (2013)); no exact values are conjectured. Continuity at p_c (T001) would be a first step.

Source: H. Kesten, Scaling relations for 2D-percolation, Comm. Math. Phys. 109 (1987); G. Grimmett, Percolation, 2nd ed. (Springer, 1999)

Where it stands (checked by us, Nov 2026): In d = 2 the exponents are known for site percolation on the triangular lattice (Smirnov 2001; Lawler–Schramm–Werner 2002; Smirnov–Werner 2001, through Kesten's scaling relations). Mean-field values (β = γ = 1, ν = 1/2) hold for d ≥ 11 (Hara–Slade 1990; Fitzner–van der Hofstad 2017) and for spread-out models with d > 6. For 3 ≤ d ≤ 6 no exponent is known to exist, and θ(p_c) = 0 is open for 3 ≤ d ≤ 10 (T001). Some inequalities hold in every dimension, for example γ ≥ 1 (Aizenman–Newman, J. Stat. Phys. 36 (1984)) and β ≤ 1 (Chayes–Chayes, Phys. Rev. Lett. 56 (1986); Aizenman–Barsky, Comm. Math. Phys. 108 (1987), who also get δ ≥ 2). A short proof of the mean-field lower bound on θ is in Duminil-Copin–Tassion, arXiv:1502.03050.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T087 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T087 (read it,
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
VERDICT: PARTIAL conditional volume-tail exponent existence with crossing counts controlled in probability

The earlier finite-scale inequality and its exponent-existence transfer
were independently re-derived and hold. The new result extends that
work to the cluster-volume tail and weakens the crossing-count assumption
for the forward averaged two-point conclusion.

For the exact earlier free-boundary count K_n in B_{2n}, assume

    pi(n)=n^{-a+o(1)},  0<a<d/2,
    P(K_n>n^epsilon) -> 0 for every epsilon>0.         (P)

PROOF.md proves

    P(|C(0)|>=t)=t^{-a/(d-a)+o(1)},
    delta=(d-a)/a=d rho-1,
    X(n)=n^{d-2a+o(1)}.

The earlier subpolynomial E K_n assumption implies (P), as does tightness
of K_n. The proof does not infer an expectation bound from (P). Rare
large counts can still dominate expectation, exactly as the earlier
audit warned. It avoids that expectation through a buffered annulus and
selected scales at which arm-probability ratios are bounded. Logarithmic
one-arm decay supplies enough such scales to obtain the tail law at
every sufficiently large size. No regular variation is assumed.

The finite geometric lemma is

    J_m <= sum_{z in m*partial B_12} K_m(z),

where J_m counts crossing components in the induced annulus with radii
8m and 16m. Every small box lies between radii 10m and 14m. The inner
arm variables stop at radius 7m, so they are independent of J_m.
This proves a largest-cluster mass estimate at good scales and then the
volume-tail lower bound. The upper bound is a radius/volume split using
the independent-endpoint-arm estimate from the earlier work.

The relation delta=d rho-1 and the annular method are classical. The
deliverable is a self-contained conditional extension of the earlier
folder's result for its exact K_n and logarithmic limits. No priority
claim over classical conditional hyperscaling results is made.

## Verification and commands

Read the earlier REPORT.md, LOG.md, PROOF.md and AUDIT.md with `cat`.
`ls -la ~/codex_op_1114/briefs/T087` confirmed that
there were no earlier computation scripts. LOG.md records the independent
re-derivation, source openings, choice before proof, and audit.

This was a proof task: no simulation, numerical dataset, Python run,
subagent, git operation, or external posting was used. AUDIT.md checks
the covering, independence, tail directions, integer scales, parameter
limits, exponent arithmetic, and counterexamples to tempting stronger
claims. Its constants are exact arithmetic re-derived separately.

Final text check: `OMP_NUM_THREADS=1 nice -n 15 sed -n '1,380p' PROOF.md`
printed the entire proof. The sandbox denied the priority adjustment
(`nice: setpriority: Operation not permitted`); the brief text read
completed. No numerical workload was launched.

The status search finished in less than five minutes. No verified
complete solution of T087 was found. The September 2026 OpenAI continuity
manuscript's README was opened, but its claim was not independently
certified. Nothing here depends on it. Primary sources and exact URLs
are recorded in LOG.md; the relevant classical comparison is
C. Borgs, J. T. Chayes, H. Kesten and J. Spencer, *Uniform Boundedness of
Critical Crossing Probabilities Implies Hyperscaling*, MSR-TR-98-26,
especially Sections 2 and 5.

## What failed or remains uncertain

No bound on the actual critical K_n distribution in dimension three was
proved. Neither the one-arm exponent nor (P) is established here for
Z^3. The result gives no uniform pointwise two-point exponent, numerical
exponent value, or near-critical matching. The earlier reverse existence
transfer from X to pi is not extended to (P). Novelty beyond this local
continuation has not been established.

A direct replacement of E K_n by a typical count in the earlier
Cauchy–Schwarz inequality is invalid. A bound on every fixed-ratio arm
comparison also does not follow from a logarithmic exponent. The proof
uses independent buffered events and a telescoping selection of scales
to avoid these two failed shortcuts.

## Next step

The weaker concrete geometric target is now (P): for every epsilon>0,
prove P(K_n>n^epsilon)->0 at p_c on Z^3, with the exact induced-box
definition. An expectation estimate is sufficient but not required for
the new forward theorem. Separately, investigate whether the reverse
transfer from an existing X exponent to a one-arm exponent can be
recovered under (P), without assuming arm-ratio regularity. Keep that
question separate from the theorem proved here.

Task: “take the NEXT checkable step on this problem, building on that
work.” — T087, 15 November 2026, approximately 01:19 Asia/Tbilisi.
