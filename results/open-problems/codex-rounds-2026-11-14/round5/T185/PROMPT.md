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
VERDICT: PARTIAL uniform negative sampled drift near the through-workload axis

The earlier smooth homogeneous workload obstruction holds. It was rederived
independently by averaging the two limiting service vectors and pairing with
the boundary gradient. No error was found. T185 remains unresolved.

New beyond round 3: the fixed-horizon lemma it requested is proved for its
two hostile state sequences, their accessible perturbations, and a wider
class of initial states. Keep the two-link network, deterministic unit
files, Poisson rates (1/5,1/2,1/2), any fixed alpha>0 and positive weights.
For the maximum link workload

\[
 M=W_0+\max(W_1,W_2),
\]

the expected increment over any fixed horizon T converges uniformly to

\[
 d(T)=-\frac3{10}T+\frac12\mathbb E|P_1(T)-P_2(T)|
 \le-\frac3{10}T+\frac12\sqrt T,
\]

over all finite initial states with residuals at most one,
W_0>=N-1 and W_1+W_2<=1/N, as N tends to infinity. P_1 and P_2 are
independent rate-1/2 Poisson processes. Thus every fixed T>25/9 gives
uniformly negative drift for sufficiently large N. There is no restriction
on the finite initial counts or individual local residuals in this wider
class. The convergence is not claimed uniformly over weights or alpha.

PROOF.md gives explicit finite-state bounds. In particular, with equal
weights and alpha=1, every N>=100 in this class satisfies

\[
 \mathbb E_x[M(X(4))-M(x)]\le-201/1900<0.
\]

The proof retains actual unit arrivals. It first bounds the clearing time
of the old tiny local files. An independent service accounting argument
then removes the old count and individual-residual restrictions: loss of
through service is charged to original local work or to new local counts.
The latter have expected integrated count T^2/2. Combined with exact
workload balance, this gives, when W_0(x)>T,

\[
 d(T)-\max(W_1(x),W_2(x))
 \le \mathbb E_x\Delta M
 \le d(T)+W_1(x)+W_2(x)
       +\frac{cT^2}{2a_0(W_0(x)-T)}.
\]

Here a_0=kappa_0^(1/alpha), and one may take
c=(kappa_1+kappa_2)^(1/alpha); for equal weights and alpha=1 take c=1.
All steps, including the all-alpha allocation formula and both service
bounds, are written in PROOF.md. AUDIT.md checks the constants and scope.

Reproduce the exact checks:

```sh
nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 check_sampled_drift.py
```

Output: `all exact checks passed`. Full data: sampled_drift_checks.json.
Two independent rational-series calculations enclose d(4) in
[-0.428494478548, -0.428494478547]. They use a conditional symmetric random
walk and a separate double Poisson sum, with certified series tails and
exponential bounds. There are 27 earlier-gradient checks and 504 exact
cohort paths with 3,554 events. The path checks cover early arrivals,
unequal weights, mixed local routes, unequal residuals, original through
departures, and the charging inequality. They test alpha=1; the proof
covers every alpha>0. Final run: 0.222 seconds, 15,876,096 bytes peak RSS,
actual nice 20, one thread, CPU limit 60 seconds. The nice wrapper warns
because changing inherited priority is prohibited; its measured priority
is already below the requested level.

The brief literature update found no later unrestricted stochastic theorem.
Opened sources were Yingjia Fu and Ruth J. Williams's
[2022 critical-fluid paper](https://mathweb.ucsd.edu/~williams/bandwidth/AAP1723forposting.pdf)
and Maria Vlasiou, Jiheng Zhang and Bert Zwart's
[arXiv:1411.4841](https://arxiv.org/abs/1411.4841).
The first discusses a distributionally conditional recurrence bridge;
the second concerns heavy traffic. This search does not certify openness
or establish priority for the lemma proved here.

What failed or remains uncertain: no mathematical verification failed.
Positive pointwise drift persists even for M at the old exact states:
GM=1/5-1/(2N). The sampled estimate does not control states with large
initial local workloads, general arriving file sizes, or renewal input.
It proves no positive recurrence statement outside the first session's
region. No claim of novelty is made. All writes stayed in this folder;
no git, subagents or external publication was used.

Next worker: extend the sampled-drift bound to all sufficiently large
maximum link workloads in this same deterministic-unit-file network.
The remaining region has substantial local work. Start with the case
where both local workloads exceed the sampling horizon and therefore
both local routes stay occupied, then handle the case of one large local
workload. A uniform estimate on all large states is still needed before
using a recurrence criterion. The full general-file fluid-to-stochastic
bridge remains a separate gap.

Task: “take the NEXT checkable step on this problem, building on that work.”
First local clock reading: 15 November 2026, 05:01:45 Asia/Tbilisi;
exact receipt time unavailable.
