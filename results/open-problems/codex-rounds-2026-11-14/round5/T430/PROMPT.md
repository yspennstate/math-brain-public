# Open problem T430: Asymptotic independence in the supermarket model with general service times

Statement: Consider N FIFO unit-rate servers, Poisson arrivals of rate lambda N with 0<lambda<1, iid service requirements of a fixed law G of mean one, and routing to a shortest queue among d>=2 uniformly sampled servers. In the stationary law, does the joint state of every fixed k servers converge, as N tends to infinity, to pi_G^{tensor k} for a single-server law pi_G? The state includes the queue length and service age or residual requirement.

Caveat: The proposed statement fixes FIFO and the full queue state; it does not conflate queue lengths with Markov states.

Source: Bramson-Lu-Prabhakar, general-service supermarket ansatz; Decay of tails at equilibrium for FIFO join the shortest queue networks (arXiv:1106.4582).

Where it stands (checked by us, Nov 2026): 1106.4582 states the ansatz and proves tail results conditional on it; it records decreasing-hazard-rate cases where the ansatz is known. General-service transient propagation of chaos does not by itself justify exchange with the stationary limit.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T430 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T430 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T430 (read it,
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
VERDICT: PARTIAL quantitative full-state finite-time product-mixture bound retaining the random initial empirical measure

The earlier result holds. Conditional competitor sampling independently recovers the append-shorter factor \((N+1-d)/N\) and the periodic witness's strict decreases. The original transient initial-mixture obstruction also checks out. Neither result was a stationary counterexample.

New beyond the earlier reports: PROOF.md replaces the false arrival-rate monotonicity step by a uniform routing estimate and a quantitative full-state path coupling. For arbitrary exchangeable initial states, fixed \(k\), \(N\geq d\), and horizon \(T\), the total variation distance between the actual tagged paths and the product-mixture directed by the nonlinear queue started from \(L_N(0)\) is at most

\[
 \min\left\{1,\
 k\left(\frac4{\sqrt N}+\frac d{2N}\right)
       (e^{\lambda d(d-1)T}-1)
 +\frac{k(k-1)}{2N}\right\}.
\]

The same estimate holds conditional on the empirical initial measure. It concerns residual requirements and ordered waiting requirements, and can retain service age. It assumes no service density, hazard monotonicity, second moment, or positive limiting queue-length class masses. Atoms at zero are allowed. The proof constructs the nonlinear reference law and proves the independent, nonidentically distributed empirical-tail estimate it uses. This is progress within this work sequence; no literature novelty claim is made for the transient coupling method.

For stationary initial laws, the comparison remains a mixture. For a measurable full-state test \(f:E\to[0,1]\), the actual two-tag covariance differs from \(\operatorname{Var}(\mu_t^{L_N(0)}f)\) by at most three times the two-path error above. The bound also vanishes on \(T_N=a\log N\) for \(0<a<1/[2\lambda d(d-1)]\). No concentration or forgetting estimate on such horizons has been obtained. The arbitrary-\(G\) stationary independence assertion remains unresolved.

Validation: every load-bearing constant has a second symbolic derivation in PROOF.md, Section 7. Command:

    OMP_NUM_THREADS=1 nice -n 15 python3 check_bounds.py

Output: 4,770 exact routing count cases passed, 378 independent subset enumerations passed, 8,190 fair-sign walks passed, and 36 earlier periodic-witness cases passed. The inherited priority was independently certified as 20; peak RSS was 14,057,472 bytes, one thread, and runtime was under one second. These finite checks supplement the all-parameter proof. Full output and commands are in LOG.md.

What failed or required correction: the sandbox rejected address-space and data-segment resource-limit setters before computation; the final small streamed audit used a 30-second CPU cap and reported RSS. A draft sentence incorrectly excluded zero-size departures coinciding with arrivals; the final proof treats these as part of the candidate update. No constant changed. No numerical simulation, stationary convergence computation, or proof of empirical concentration is claimed.

The literature check took less than five minutes and found no verified later solution. Opened Maria Clara Fittipaldi, Matthieu Jonckheere, Sergio I. Lopez, *Convergence properties of many parallel servers under power-of-D load balancing*, [arXiv:1809.05373](https://arxiv.org/abs/1809.05373), including its PDF; and Pooja Agarwal and Kavita Ramanan, *Invariant states of hydrodynamic limits of randomized load balancing networks*, [arXiv:2008.08510](https://arxiv.org/pdf/2008.08510), whose retrieved Section 4.2 still leaves the relevant stationary identification conjectural. This brief check is not an exhaustive literature certification. No SOLVED_ELSEWHERE.md was created.

Next worker: under stationary starts, prove \(\operatorname{Var}(\mu_{t_N}^{L_N(0)}f)\to0\) for a convergence-determining collection of full-state tests, on horizons where the displayed error tends to zero, and identify a unique limit for their means. Alternatively, establish a strict dissipation or attraction argument which forces invariant probability laws of the nonlinear evolution to concentrate on one fixed point. Uniqueness of the fixed point alone does not rule out a nontrivial invariant law of the evolution. The routing and transient steps here do not establish that missing fact.

All writes stayed in this folder. No git, subagents, external posts, messages, accounts, global mesh writes, or brain writes were used.

Task: “Open problem T430: Asymptotic independence in the supermarket model with general service times”; received 15 November 2026, approximately 06:41 Asia/Tbilisi (02:41 UTC).
