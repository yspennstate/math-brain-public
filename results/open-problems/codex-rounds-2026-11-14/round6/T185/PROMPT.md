# Open problem T185: Stability of α-fair bandwidth sharing networks with general file-size distributions

Statement: In the connection-level model of Massoulié and Roberts, flows on each route arrive as a Poisson (or renewal) process and bring a random amount of work with a general distribution, and the link capacities are shared among the flows present according to the weighted α-fair allocation. Prove that whenever the network is subcritical (the offered load on every link is below its capacity) the process describing the flows and their residual work is positive recurrent.

Caveat: For exponential file sizes the number of flows per route is a Markov chain and stability under α-fair policies for all α > 0 is known (de Veciana–Lee–Konstantopoulos, Bonald–Massoulié). For general file sizes the state must include residual work, and the Markov-chain arguments for the exponential case do not transfer. A standard route is to prove stability of the fluid model and then deduce stability of the stochastic model; Fu and Williams treat the first step.

Source: M. Bramson, Network stability under max–min fair bandwidth sharing, Ann. Appl. Probab. 20 (2010) 1126–1176; status as in Y. Fu and R. J. Williams, Stability of a subcritical fluid model for fair bandwidth sharing with general file size distributions, Stoch. Syst. 10 (2020) 251–273

Where it stands (checked by us, Nov 2026): Bramson (arXiv:1010.3142) proved stability of weighted max–min fair sharing for general interarrival and service distributions with 2 + δ moments. Massoulié (arXiv:0707.4542) proved stability of proportional fairness with Markovian routing and phase-type service times. Gromoll and Williams (Ann. Appl. Probab. 2009) established fluid limits. Paganini, Tang, Ferragut and Andrew (IEEE Trans. Automat. Control 57 (2012) 579–591) gave a Lyapunov function for the fluid model under smoothness assumptions, and Fu and Williams proved stability of subcritical fluid model solutions for general file sizes. Positive recurrence of the stochastic model for α-fair policies with general file sizes is the step these works leave open. Open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T185 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T185 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T185 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 5 worker built on the latest of these. Its folder is ~/codex_op_1114r5/briefs/T185 (read it, never
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
VERDICT: PARTIAL positive Harris recurrence for the two-link unit-file example under every weighted alpha-fair policy

Round 4's sampled-drift result holds. Its script was copied into this
folder and rerun: all 504 exact paths and both Poisson-series calculations
passed. A separate symbolic rederivation recovered its original-service
charging bound and finite-state constant -201/1900. Earlier folders were
not edited.

New beyond round 4: the same maximum link workload now has uniformly
negative four-unit drift at **all** sufficiently large workload states in
its two-link network, with deterministic unit arrivals, independent
Poisson rates (1/5,1/2,1/2), arbitrary fixed alpha>0 and positive weights.
There are no bounds on initial finite counts or positive lower bounds
on residuals; initial residuals are at most one. This closes the gap its
report identified. Positive Harris recurrence follows for this specified
example by an explicit empty-state regeneration argument. T185 for general
file-size distributions and networks remains unresolved here.

The new estimate uses the common potential local service q=1-Lambda0,
its integral Q, and m=max(W1(0),W2(0)). Local reflection gives

    Delta M <= A0(T)-T+max(A1(T),A2(T))+(Q(T)-m)^+.

If m>=T the error is zero, including when only one local workload is
large or the through route is empty. If m<T and W0(0)>T, put
R=W0(0)-T and choose an integer K>=1. The last original local population
to fall below K charges the earlier potential local service to at most
m units of original work. Afterward both original local counts are small.
This proves

    E Delta M <= d(T)+T^2/K+c*T*(2K+T)/(a0*R),

where d(T)<=-3T/10+sqrt(T)/2, a0=kappa0^(1/alpha), and
H(u1,u2)<=c*(u1+u2). First taking K large and then R large gives uniform
negative drift in the remaining region. For equal weights and alpha=1,

    M(x)>65544  =>  E_x[M(X(4))-M(x)] <= -2171/20480.

The bounded-workload set need not be compact: a no-arrival interval of
length 2B empties every state with M<=B because its total work is at most
2B and aggregate service is at least one while nonempty. Sampled drift
bounds the expected return time to this set after each failed attempt.
Uniform positive success probability yields finite mean emptying time,
finite mean regenerative cycles and positive Harris recurrence.
PROOF.md writes out every step; AUDIT.md gives a second proof of the
count-threshold estimate and checks the recurrence argument.

Commands, run here:

```sh
nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 prior_check_sampled_drift.py
nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 check_uniform_drift.py
```

Both print `all exact checks passed`. The new script uses exact rational
event-driven trajectories: 672 paths, 3,733 events, 1,920 threshold checks,
434 original-cohort departures, 230 paths with Q>m and 72 with positive
empty time. It includes mixed routes, simultaneous arrivals, new counts
above K, no through population, tiny residuals, large original counts and
unequal weights. Computational checks use alpha=1; the proof covers all
alpha>0. Full outputs: sampled_drift_checks.json and uniform_drift_checks.json.
The new run took 0.2447 seconds, peak RSS 16,465,920 bytes, actual nice 20,
one thread, CPU cap 60 seconds. The wrapper's priority warning reflects
its inability to change the already lower inherited priority.

The literature update found no later unrestricted stochastic theorem.
Opened Yingjia Fu and Ruth J. Williams, *Asymptotic behavior of a critical
fluid model for bandwidth sharing with general file size distributions*,
Ann. Appl. Probab. 32 (2022), 1862–1901:
https://mathweb.ucsd.edu/~williams/bandwidth/AAP1723forposting.pdf .
The attempted 2020 author-PDF fetch timed out. The limited search neither
certifies openness nor establishes novelty of this special-case proof.

What failed: no mathematical check failed. The tempting deterministic
bound Q<=m is false in the presence of new local arrivals; the proof
retains its explicit positive error. General arriving files, arbitrary
topologies, renewal input and an unrestricted fluid-to-stochastic bridge
are not proved. No stationary mean-workload estimate is asserted.

Next worker: extend this same two-link proof to bounded random file sizes.
Replace arrival counts in the workload/reflection identities by compound
Poisson input work, retain new-file counts in the threshold lemma, and
use a common file-size bound to recover n0>=W0/b_max. Verify this carefully
before attempting truncation to unbounded sizes: large through work then
need not imply a large through count, which is the unresolved obstruction
for this argument. No claim that such a truncation preserves stability
has been made.

All writes stayed in this folder; no git, subagents, external publication
or shared-state logging was used.

Task: “take the NEXT checkable step on this problem, building on that work.”
First local clock: 15 November 2026, 08:32:25 Asia/Tbilisi;
exact receipt time unavailable.
