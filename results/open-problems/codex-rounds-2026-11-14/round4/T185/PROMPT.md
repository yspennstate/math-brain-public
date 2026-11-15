# Open problem T185: Stability of α-fair bandwidth sharing networks with general file-size distributions

Statement: In the connection-level model of Massoulié and Roberts, flows on each route arrive as a Poisson (or renewal) process and bring a random amount of work with a general distribution, and the link capacities are shared among the flows present according to the weighted α-fair allocation. Prove that whenever the network is subcritical (the offered load on every link is below its capacity) the process describing the flows and their residual work is positive recurrent.

Caveat: For exponential file sizes the number of flows per route is a Markov chain and stability under α-fair policies for all α > 0 is known (de Veciana–Lee–Konstantopoulos, Bonald–Massoulié). For general file sizes the state must include residual work, and the Markov-chain arguments for the exponential case do not transfer. A standard route is to prove stability of the fluid model and then deduce stability of the stochastic model; Fu and Williams treat the first step.

Source: M. Bramson, Network stability under max–min fair bandwidth sharing, Ann. Appl. Probab. 20 (2010) 1126–1176; status as in Y. Fu and R. J. Williams, Stability of a subcritical fluid model for fair bandwidth sharing with general file size distributions, Stoch. Syst. 10 (2020) 251–273

Where it stands (checked by us, Nov 2026): Bramson (arXiv:1010.3142) proved stability of weighted max–min fair sharing for general interarrival and service distributions with 2 + δ moments. Massoulié (arXiv:0707.4542) proved stability of proportional fairness with Markovian routing and phase-type service times. Gromoll and Williams (Ann. Appl. Probab. 2009) established fluid limits. Paganini, Tang, Ferragut and Andrew (IEEE Trans. Automat. Control 57 (2012) 579–591) gave a Lyapunov function for the fluid model under smoothness assumptions, and Fu and Williams proved stability of subcritical fluid model solutions for general file sizes. Positive recurrence of the stochastic model for α-fair policies with general file sizes is the step these works leave open. Open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T185 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T185 (read it,
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
VERDICT: PARTIAL obstruction to smooth homogeneous workload Lyapunov functions

The earlier linear-workload result holds under its stated Poisson
assumptions. It was rederived independently through a link-slack argument
and a scalar busy-period comparison. T185 remains unresolved.

New beyond the earlier report: in its same two-link network, with loads
(1/5,1/2,1/2), deterministic unit files, arbitrary alpha>0 and positive
fairness weights, no function V=F(W) in the following class has uniformly
strictly negative pointwise generator drift outside a finite V-sublevel:
F is positively homogeneous of any degree d>0, is C^1 away from zero
including the orthant boundary, and satisfies F(e_0)>0. This extends the
earlier obstruction from positive linear functions to a class of nonlinear
functions, without convexity or coordinate monotonicity assumptions.

For each such F, PROOF.md constructs states with V tending to infinity and

\[
 \lim_{N\to\infty}N^{1-d}\mathcal GV(x_N)
 \ge dF(e_0)/5>0.
\]

There are N through-route files and N^3 nearly completed files on one local
route. The normalized workloads approach e_0, while service approaches
either e_1 or e_2. The two limiting drifts average to dF(e_0)/5. A separate
Poisson event reaches nearby obstructing states from empty with strictly
positive probability; the theorem does not rely on hitting equal-residual
states exactly. Each link has load 7/10, so the example is strictly
subcritical. Positive instantaneous drift does not imply instability:
the almost completed local files clear on a time scale tending to zero.

The literature update found no unrestricted later stochastic stability
theorem. Opened primary sources were Yingjia Fu and Ruth J. Williams's
[2020 publisher page](https://pubsonline.informs.org/doi/10.1287/stsy.2019.0058)
and [2022 paper](https://mathweb.ucsd.edu/~williams/bandwidth/AAP1723forposting.pdf),
and Maria Vlasiou, Jiheng Zhang and Bert Zwart's
[arXiv:1411.4841](https://arxiv.org/abs/1411.4841).
The 2022 paper discusses a distributionally conditional bridge through
Lee's work. The arXiv abstract concerns heavy traffic. This brief search
does not certify that the problem is open, or establish novelty of the
obstruction. The publisher confirms DOI 10.1287/stsy.2019.0058; an initial
contrary bibliographic note in LOG.md is corrected later in that log.

Reproduce the exact checks from this folder:

```sh
nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 check_obstruction.py
```

Output: `all exact checks passed`; 216 earlier coefficient witnesses;
120 exact KKT checks; direct generator evaluations equal independent
Laurent expansions for five polynomial functions and both service
branches. Their respective limiting drift pairs are (1/5,1/5),
(2/5,2/5), (4/5,4/5), (21/10,-9/10), and (14/5,-6/5).
The general theorem is symbolic, not inferred from these finite checks.
Full output is obstruction_checks.json. The successful run took 0.0099
seconds and peaked at 15,843,328 bytes RSS, with actual process nice 20.

What failed: a smooth homogeneous nonlinear workload replacement cannot
repair the earlier pointwise drift method. Three initial script attempts
stopped before mathematical checks because macOS rejected RLIMIT_DATA
settings. The final script reports that restriction, caps CPU time, and
records and checks its tiny measured RSS. The nice wrapper warns, but a
direct priority query confirms the process already runs at nice 20.

AUDIT.md independently checks the earlier certificate, the new drift
constant, all positive real degrees, accessibility, the boundary derivative
assumption, unequal weights, and the order of limits. No mistake in the
earlier mathematical result or counterexample to stability was found.

Unresolved: nonsmooth or nonhomogeneous workload functions, residual-profile
functions, and drift sampled over time. The result requires C^1 behavior
at the through-route axis; interior differentiability alone is insufficient.
It proves no additional stochastic recurrence region and no renewal-arrival
extension.

Next worker: retain this example as an adversarial test for a sampled-drift
argument. A concrete next lemma would estimate the expected change of the
maximum link workload over a fixed sufficiently long interval, uniformly
over the two hostile state sequences here. Such a lemma must retain actual
unit arrival jumps and control newly arriving local files after the original
tiny residuals clear. A negative result for pointwise drift cannot be
substituted for that interval calculation. For a general fluid bridge,
compare Lee's exact distributional hypotheses before invoking it.

Task: “take the NEXT checkable step on this problem, building on that work.”
First recorded task time: 15 November 2026, 01:38:59 Asia/Tbilisi;
completion resumed at 03:30 Asia/Tbilisi. Exact receipt time is unavailable.
