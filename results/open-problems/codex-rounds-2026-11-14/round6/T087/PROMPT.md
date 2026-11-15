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

Later work: a round 5 worker built on the latest of these. Its folder is ~/codex_op_1114r5/briefs/T087 (read it, never
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
VERDICT: PARTIAL scale-dependent rectangular crossing criterion for subpolynomial component counts

The earlier reverse exponent-transfer theorem was independently
re-derived and holds. The new result proves the geometric reduction
suggested in the round 4 report, for its exact free-boundary K_n.

Let R(n) be the probability of a short-direction open crossing of
[0,n] x [-2n,2n]^{d-1}, and let delta(n)=1-R(n). Then

    P(K_n>=u) <= 2d R(n)^{ceil(u/(2d))},
    E K_n <= 2d R(n)/delta(n).

Thus a subpolynomial reciprocal crossing deficit,

    log(1/delta(n))/log n -> 0,

implies the stronger expected-count hypothesis (H), and hence the
probability hypothesis (P) used by rounds 3 and 4. The deficit may
tend to zero; it need not be uniformly positive. For every epsilon>0,
the criterion gives eventually

    P(K_n>n^epsilon) <= 2d exp[-n^{epsilon/2}/(2d)].

Estimates only on logarithmically dense scales suffice. More precisely,
the same conclusions hold if a sequence m_j tends to infinity with

    log(m_{j+1})/log(m_j) -> 1,
    log(1/delta(m_j))/log(m_j) -> 0.

The finite-scale bridge, proved by an explicit shell cover, is

    E K_n <= C_d (n/m)^{d-1}/delta(m),  1<=m<=n/8,
    C_d=4d^2 4^{d-1}.

Distinct components are first dominated by maximal edge-disjoint
rectangle crossings. BK is applied only to those increasing path
events. The component-count events need not be increasing.

Neither crossing-deficit criterion is proved at p_c on Z^3. They
therefore provide conditional inputs to the earlier exponent-transfer
and volume-tail theorems, without establishing exponent existence,
values, pointwise decay, or near-critical matching. The geometric
method is classical; no literature priority is claimed.

## Verification and commands

Read REPORT.md, LOG.md, PROOF.md and AUDIT.md in all three predecessor
folders. File searches found no computation scripts. Rechecked the
original pair inequality, round 3 tail interpolation, and especially
round 4's buffered quadratic estimate and contracting recurrence.
LOG.md records these checks before the new piece was chosen.

This was a proof task, with no numerical program or simulation. Command:

    OMP_NUM_THREADS=1 nice -n 15 sed -n '1,360p' PROOF.md

printed the complete saved proof and completed with exit code 0.
The sandbox reports `nice: setpriority: Operation not permitted`;
no sustained computational workload was launched. AUDIT.md re-derives
the shell bound by a disjoint combinatorial partition, the geometric
expectation by memorylessness, and the sparse-scale limit by a second
logarithmic calculation. All load-bearing constants and thresholds
were checked independently, including the dimension-three bound
C_3=576 and the boundary case n=8m.

The literature status check finished within five minutes. No verified
complete solution of T087 was found. Opened primary sources are listed
in LOG.md. The relevant classical comparison is C. Borgs, J. T. Chayes,
H. Kesten and J. Spencer, *Uniform Boundedness of Critical Crossing
Probabilities Implies Hyperscaling*, MSR-TR-98-26 (1998), Lemma 4.2:
https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-98-26.pdf .

All new artifacts are in this folder: LOG.md, PROOF.md, AUDIT.md and
REPORT.md. No git, subagent, external posting or shared-memory write
was used. The predecessor folders were read only.

## What failed or remains uncertain

No mathematical failure was found in the predecessor claims or this
extension. Direct BK on component counts would be invalid. Merely
knowing the finite-scale deficit is positive does not give its needed
asymptotic bound. A fixed polynomial reciprocal deficit gives only a
polynomial count estimate here. An arbitrary sparse sequence leaves a
polynomial covering loss; logarithmic density is used explicitly.

The criterion is sufficient; no converse is claimed. It uses rectangles
with transverse side 4n, and no aspect-ratio conversion from the classical
side 3n is silently assumed. Novelty beyond this local continuation has
not been established.

## Next step

The geometric target is now an explicit scalar estimate: at p_c on Z^3,
find integers m_j with log(m_{j+1})/log(m_j)->1 for which the no-crossing
probability of [0,m_j] x [-2m_j,2m_j]^2 has subpolynomial reciprocal.
Proving this would supply both predecessor count hypotheses. Existence
of either the one-arm or averaged two-point exponent would still be
needed. A weaker polynomial deficit estimate would give a quantitative
count bound through (2)–(4), but would not by itself establish (P).

Task: “take the NEXT checkable step on this problem, building on that
work.” — T087, 15 November 2026, approximately 08:05 Asia/Tbilisi.
