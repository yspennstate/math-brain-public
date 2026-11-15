# Open problem T087: Existence and values of the critical exponents of three-dimensional percolation

Statement: For Bernoulli bond percolation on Z^3 the critical exponents exist: θ(p) = (p − p_c)^{β+o(1)} as p ↓ p_c, the mean cluster size is (p_c − p)^{−γ+o(1)} as p ↑ p_c, the correlation length is |p − p_c|^{−ν+o(1)}, and at p_c the one-arm probability P(0 ↔ ∂B_n) is n^{−1/ρ+o(1)} and the two-point function decays like |x|^{−(1+η)+o(1)}; and they satisfy the scaling and hyperscaling relations, for example γ = ν(2 − η) and 3ν = γ + 2β.

Caveat: Existence of the exponents is part of the problem. Their values are known only numerically (β ≈ 0.418, ν ≈ 0.876, η ≈ −0.046, from 1/ν = 1.1410(15) and β/ν = 0.47705(15) for bond and site percolation on the cubic lattice: Wang, Zhou, Zhang, Garoni and Deng, arXiv:1302.0421, Phys. Rev. E 87 (2013)); no exact values are conjectured. Continuity at p_c (T001) would be a first step.

Source: H. Kesten, Scaling relations for 2D-percolation, Comm. Math. Phys. 109 (1987); G. Grimmett, Percolation, 2nd ed. (Springer, 1999)

Where it stands (checked by us, Nov 2026): In d = 2 the exponents are known for site percolation on the triangular lattice (Smirnov 2001; Lawler–Schramm–Werner 2002; Smirnov–Werner 2001, through Kesten's scaling relations). Mean-field values (β = γ = 1, ν = 1/2) hold for d ≥ 11 (Hara–Slade 1990; Fitzner–van der Hofstad 2017) and for spread-out models with d > 6. For 3 ≤ d ≤ 6 no exponent is known to exist, and θ(p_c) = 0 is open for 3 ≤ d ≤ 10 (T001). Some inequalities hold in every dimension, for example γ ≥ 1 (Aizenman–Newman, J. Stat. Phys. 36 (1984)) and β ≤ 1 (Chayes–Chayes, Phys. Rev. Lett. 56 (1986); Aizenman–Barsky, Comm. Math. Phys. 108 (1987), who also get δ ≥ 2). A short proof of the mean-field lower bound on θ is in Duminil-Copin–Tassion, arXiv:1502.03050.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T087 (read it,
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
VERDICT: PARTIAL finite-scale reduction and conditional equivalence of one-arm and averaged two-point exponent existence

For nearest-neighbour Bernoulli bond percolation on Z^d, let π(n) be the one-arm probability, X(n)=sum_{x in B_n} P(0↔x), and K_n the number of open components in the induced graph on B_{2n} meeting both B_n and ∂B_{2n}. PROOF.md proves the unconditional finite-scale inequality

    X(2n) ≥ (2n+1)^d π(3n)^2 / E K_n.

Together with a separated-arm upper bound, this gives the following conditional reduction. If E K_n is at most subpolynomial, existence of π(n)=n^(−a+o(1)) with 0<a<d/2 is equivalent to existence of X(n)=n^(s+o(1)) with 0<s<d, and s=d−2a. It also yields the supremum envelope law sup_{||x||≥n} P(0↔x)=n^(−2a+o(1)). Only logarithmic limits are assumed; no regular variation is used.

If the uniform pointwise two-point exponent b additionally exists in (0,d), any hyperscaling defect forces

    E K_n ≥ n^(b−2a+o(1)),     b≥2a.

For d=3 this defect is 1+η−2/ρ. Its vanishing, combined with separately proved β=ν/ρ and γ=ν(2−η), would give 3ν=γ+2β. None of those missing Z^3 inputs is established in this session. In particular, a supremum or averaged exponent does not prove the pointwise two-point law in T087.

The multiplicity approach is classical; this is a self-contained reduction, with finite-scale bounds and a transfer of existence in both directions. No claim of a new critical exponent or priority over earlier conditional hyperscaling work is made.

## Verification and commands

This was a proof task; no simulation, computed percolation data, or computational script was used. AUDIT.md gives a second derivation of the main factor by a variance argument, independent exact shell counts, and checks of exponent signs, boundary definitions, dependence, rare large counts, endpoint cases, and integer-scale limits.

Web queries and opened primary sources are recorded in LOG.md and SOLVED_ELSEWHERE.md. The recent-literature pass finished in less than ten minutes. No verified complete solution of T087 was found. Related high-dimensional and hierarchical results do not answer the cubic-lattice question. A September 2026 continuity manuscript was located but its PDF could not be read by the web tool, so its claim is not certified here.

Local orientation commands and relevant output are in LOG.md. In particular, the startup command `OMP_NUM_THREADS=1 nice -n 15 python3 .../brain.py recall ...` reported `nice: setpriority: Operation not permitted`; it completed, and no further Python or numerical workload was launched. The task's folder-only restriction took precedence over shared checklist/mesh writes. No git or external posting was performed.

## What failed or remains uncertain

The core unproved geometric condition is subpolynomial **expected** K_n at p_c on Z^3. A bound in probability is insufficient because rare configurations can dominate its expectation. At least one of the two exponent-existence statements must also be proved. Pointwise lower bounds and near-critical matching remain missing. The literature review establishes no novelty claim for this particular logarithmic formulation.

## Next work

Target a bound E K_n≤n^ε for every ε>0 for the exact free-boundary, induced-box component count defined above. A finite-size computation could test this quantity but would not prove an asymptotic bound. In parallel, compare the logarithmic-existence transfer with the precise hypotheses of the classical conditional hyperscaling theorems before claiming an improvement. Keep the stated boundary convention; wiring boundary vertices invalidates the pair-connectivity argument. AUDIT.md explains a separate whole-lattice-cluster variant.

Task: “push this problem forward by one checkable piece” — T087, 14 November 2026, approximately 20:54 Asia/Tbilisi.
