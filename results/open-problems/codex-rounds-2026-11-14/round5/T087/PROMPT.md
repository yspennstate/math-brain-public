# Open problem T087: Existence and values of the critical exponents of three-dimensional percolation

Statement: For Bernoulli bond percolation on Z^3 the critical exponents exist: θ(p) = (p − p_c)^{β+o(1)} as p ↓ p_c, the mean cluster size is (p_c − p)^{−γ+o(1)} as p ↑ p_c, the correlation length is |p − p_c|^{−ν+o(1)}, and at p_c the one-arm probability P(0 ↔ ∂B_n) is n^{−1/ρ+o(1)} and the two-point function decays like |x|^{−(1+η)+o(1)}; and they satisfy the scaling and hyperscaling relations, for example γ = ν(2 − η) and 3ν = γ + 2β.

Caveat: Existence of the exponents is part of the problem. Their values are known only numerically (β ≈ 0.418, ν ≈ 0.876, η ≈ −0.046, from 1/ν = 1.1410(15) and β/ν = 0.47705(15) for bond and site percolation on the cubic lattice: Wang, Zhou, Zhang, Garoni and Deng, arXiv:1302.0421, Phys. Rev. E 87 (2013)); no exact values are conjectured. Continuity at p_c (T001) would be a first step.

Source: H. Kesten, Scaling relations for 2D-percolation, Comm. Math. Phys. 109 (1987); G. Grimmett, Percolation, 2nd ed. (Springer, 1999)

Where it stands (checked by us, Nov 2026): In d = 2 the exponents are known for site percolation on the triangular lattice (Smirnov 2001; Lawler–Schramm–Werner 2002; Smirnov–Werner 2001, through Kesten's scaling relations). Mean-field values (β = γ = 1, ν = 1/2) hold for d ≥ 11 (Hara–Slade 1990; Fitzner–van der Hofstad 2017) and for spread-out models with d > 6. For 3 ≤ d ≤ 6 no exponent is known to exist, and θ(p_c) = 0 is open for 3 ≤ d ≤ 10 (T001). Some inequalities hold in every dimension, for example γ ≥ 1 (Aizenman–Newman, J. Stat. Phys. 36 (1984)) and β ≤ 1 (Chayes–Chayes, Phys. Rev. Lett. 56 (1986); Aizenman–Barsky, Comm. Math. Phys. 108 (1987), who also get δ ≥ 2). A short proof of the mean-field lower bound on θ is in Duminil-Copin–Tassion, arXiv:1502.03050.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T087 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T087 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T087 (read it,
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
VERDICT: PARTIAL reverse exponent-existence transfer under crossing-count control in probability

The earlier conditional volume-tail theorem was independently re-derived
and holds. The new result resolves the reverse-transfer question left
open in the round 3 report.

Let K_n count open components of the induced free-boundary graph on
B_{2n} meeting B_n and partial B_{2n}, and let
X(n)=sum_{x in B_n} P(0<->x), with unrestricted connections. Assume

    for every epsilon>0, P(K_n>n^epsilon)->0.         (P)

PROOF.md proves

    X(n)=n^{s+o(1)}, 0<s<d
      => pi(n)=n^{-(d-s)/2+o(1)}.

Together with the verified predecessor theorem, (P) therefore makes
existence of a nondegenerate one-arm exponent equivalent to existence
of a nondegenerate averaged two-point growth exponent. Starting from
X alone now also gives

    P(|C(0)|>=t)=t^{-(d-s)/(d+s)+o(1)},
    delta=(d+s)/(d-s).

All limits are logarithmic. No arm-ratio regularity or expected-count
bound is assumed. The input hypotheses remain unproved at p_c on Z^3;
this does not solve T087 or establish any numerical exponent value.

The new finite-scale estimate is

    pi(20m) <= pi(3m) P(J_m>L)
                   + sqrt(L X(8m)/V_{4m}),

where J_m counts crossing components in the induced annulus of radii
8m and 16m, V_{4m}=(8m+1)^d, and L>=1. A deterministic covering
transfers (P) to J_m. Squared core-component masses give the square-root
error; independent inner edges control the bad-count contribution.
On scales m=8^j, this becomes a contracting recurrence with an error of
the desired power. It avoids needing a one-arm exponent in order to
select good arm-ratio scales.

## Verification and commands

Read REPORT.md, LOG.md, PROOF.md and AUDIT.md from both earlier folders.
The file search found no predecessor computation scripts. Independently
checked the earlier covering, largest-cluster estimate, logarithmically
dense good scales, volume-tail interpolation and recovery of X.
LOG.md records the verification before the new piece was chosen.

This was a proof task, with no simulation or numerical program. The
complete saved proof was reread using

    OMP_NUM_THREADS=1 nice -n 15 sed -n '1,360p' PROOF.md

The read completed with exit code 0. The sandbox denied the priority
adjustment (`nice: setpriority: Operation not permitted`), so no sustained
computational workload was launched. AUDIT.md independently re-derives
the quadratic bound by uniform pair sampling and the recurrence by
explicit geometric summation. It checks constants, exponent signs,
boundary conventions, component mergers, independence and all scales.

The status search finished within five minutes. No verified complete
solution of T087 was found. Opened primary sources and exact URLs are
recorded in LOG.md. The classical comparison is C. Borgs, J. T. Chayes,
H. Kesten and J. Spencer, *Uniform Boundedness of Critical Crossing
Probabilities Implies Hyperscaling*, MSR-TR-98-26. No priority claim is
made over classical conditional hyperscaling results.

All new artifacts are in this folder: LOG.md, PROOF.md, AUDIT.md and
REPORT.md. No git, subagent, external posting or shared-memory write
was used, and the predecessor folders were not edited.

## What failed or remains uncertain

Neither (P) nor exponent existence on critical Z^3 is proved. No
pointwise two-point lower bound, near-critical matching or exact exponent
value follows. Literature priority of this formulation is not established.
No mathematical failure was found in either the rechecked predecessor
theorem or the new reverse proof.

A fixed-ratio comparison of X cannot justify the needed subtraction
under logarithmic exponent existence alone. The proof uses distinct
power scales. Replacing bad-count probabilities by expectations, or
treating the core mass and annulus count as independent, would also be
unjustified; neither shortcut is used.

## Next step

The reverse-transfer gap is closed. The geometric target is still (P)
for the exact free-boundary K_n at criticality on Z^3. A concrete next
lemma is to derive an explicit sufficient condition on rectangular
crossing probabilities that implies (P), allowing scale-dependent
crossing deficits. Keep distinct-component counts separate from maximum
numbers of disjoint paths, and do not apply BK directly to count events.
Such a reduction would identify a more accessible geometric estimate;
proving it in dimension three remains separate work.

Task: “take the NEXT checkable step on this problem, building on that
work.” — T087, 15 November 2026, approximately 04:46 Asia/Tbilisi.
