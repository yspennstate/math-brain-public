# Open problem T185: Stability of α-fair bandwidth sharing networks with general file-size distributions

Statement: In the connection-level model of Massoulié and Roberts, flows on each route arrive as a Poisson (or renewal) process and bring a random amount of work with a general distribution, and the link capacities are shared among the flows present according to the weighted α-fair allocation. Prove that whenever the network is subcritical (the offered load on every link is below its capacity) the process describing the flows and their residual work is positive recurrent.

Caveat: For exponential file sizes the number of flows per route is a Markov chain and stability under α-fair policies for all α > 0 is known (de Veciana–Lee–Konstantopoulos, Bonald–Massoulié). For general file sizes the state must include residual work, and the Markov-chain arguments for the exponential case do not transfer. A standard route is to prove stability of the fluid model and then deduce stability of the stochastic model; Fu and Williams treat the first step.

Source: M. Bramson, Network stability under max–min fair bandwidth sharing, Ann. Appl. Probab. 20 (2010) 1126–1176; status as in Y. Fu and R. J. Williams, Stability of a subcritical fluid model for fair bandwidth sharing with general file size distributions, Stoch. Syst. 10 (2020) 251–273

Where it stands (checked by us, Nov 2026): Bramson (arXiv:1010.3142) proved stability of weighted max–min fair sharing for general interarrival and service distributions with 2 + δ moments. Massoulié (arXiv:0707.4542) proved stability of proportional fairness with Markovian routing and phase-type service times. Gromoll and Williams (Ann. Appl. Probab. 2009) established fluid limits. Paganini, Tang, Ferragut and Andrew (IEEE Trans. Automat. Control 57 (2012) 579–591) gave a Lyapunov function for the fluid model under smoothness assumptions, and Fu and Williams proved stability of subcritical fluid model solutions for general file sizes. Positive recurrence of the stochastic model for α-fair policies with general file sizes is the step these works leave open. Open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T185 (read it,
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
VERDICT: PARTIAL sharp linear-workload certificate and finite-mean stability when sum_i rho_i/b_i < 1

For route `i`, let `b_i` be its rate when it is the only route present, equal to the smallest capacity on its path. Wrote a complete proof in `PROOF.md` of the following statements for independent Poisson arrivals and arbitrary strictly positive finite-mean file sizes:

- A positive linear residual-workload function has uniform strictly negative generator drift outside a workload threshold if and only if `beta=sum_i rho_i/b_i<1`.
- The optimal normalized certificate is `Y=sum_i W_i/b_i`, with negative-drift margin `1-beta`.
- In this region the full residual-state process is positive Harris recurrent, with `E_x tau_empty <= Y(x)/(1-beta)`. Its mean empty-to-empty regenerative cycle is at most `1/[nu(1-beta)]`, where `nu` is the total arrival rate. The invariant empty probability is at least `1-beta`.

The argument uses only feasibility and Pareto efficiency, and therefore applies to every weighted alpha-fair policy with positive weights and `alpha>0`. No smoothness or second moment is needed. This elementary sufficient region is not asserted to be new.

The obstruction is exact. In a two-link unit-capacity network with a through route and one local route per link, route loads `(1/5,1/2,1/2)` give link loads `(7/10,7/10)` but `beta=6/5`. Every positive linear residual-workload function has positive generator drift at some arbitrarily large states. This excludes that proof method; it does not show instability.

The literature check finished in about three minutes. No later unrestricted solution was found. The supplied status omits conditional stochastic recurrence through Nam H. Lee's 2008 dissertation, explicitly noted on p. 1863 of Yingjia Fu and Ruth J. Williams's [2022 paper](https://mathweb.ucsd.edu/~williams/bandwidth/AAP1723forposting.pdf). This is not a new removal of the distributional restrictions. Maria Vlasiou, Jiheng Zhang and Bert Zwart's [2026 paper](https://link.springer.com/article/10.1007/s11134-026-09978-1), [arXiv:1411.4841](https://arxiv.org/abs/1411.4841), treats phase-type files and heavy traffic. Full references and search limitations are recorded in `LOG.md`. The search does not certify that no other paper exists.

Reproduce the finite checks with:

```sh
nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 check_certificate.py
```

Output: all exact checks passed; both link loads `7/10`, scalar load `6/5`, 512 weight vectors checked, and the minimum service formula verified by rational vertex enumeration over 7 and 15 active supports. Full output/data: `certificate_checks.json`; command and output: `LOG.md`. The run finished in under one second. The sandbox rejected setting nice priority (`setpriority: Operation not permitted`), although the command ran; no heavy computation was attempted.

`AUDIT.md` independently re-derives the emptying-time bound by a scalar busy-period branching argument and checks the service bound through link utilizations. It also records the bounded-support, small-residual, heavy-tail, boundary-load, and regeneration cases.

What failed: a fixed positive linear residual-workload drift cannot use the full subcritical region, even in the small two-link example. What remains unproved: T185 outside `beta<1`, renewal-arrival extensions, and any claim of novelty for the certificate. No counterexample to stochastic stability was found or claimed.

Next worker: use the explicit two-link example to test a nonlinear residual-profile Lyapunov function or drift over a state-dependent interval. Such an argument must overcome the positive instantaneous linear drift at states containing files on a single route. For a fluid-to-stochastic approach, first compare Lee's precise hypotheses with the intended file-size class; do not assume the general bridge theorem already applies.

Task: “push this problem forward by one checkable piece,” received 14 November 2026, approximately 22:06 Asia/Tbilisi; exact receipt time unavailable.
