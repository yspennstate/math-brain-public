# Open problem T430: Asymptotic independence in the supermarket model with general service times

Statement: Consider N FIFO unit-rate servers, Poisson arrivals of rate lambda N with 0<lambda<1, iid service requirements of a fixed law G of mean one, and routing to a shortest queue among d>=2 uniformly sampled servers. In the stationary law, does the joint state of every fixed k servers converge, as N tends to infinity, to pi_G^{tensor k} for a single-server law pi_G? The state includes the queue length and service age or residual requirement.

Caveat: The proposed statement fixes FIFO and the full queue state; it does not conflate queue lengths with Markov states.

Source: Bramson-Lu-Prabhakar, general-service supermarket ansatz; Decay of tails at equilibrium for FIFO join the shortest queue networks (arXiv:1106.4582).

Where it stands (checked by us, Nov 2026): 1106.4582 states the ansatz and proves tail results conditional on it; it records decreasing-hazard-rate cases where the ansatz is known. General-service transient propagation of chaos does not by itself justify exchange with the stationary limit.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T430 (read it,
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
VERDICT: PARTIAL stationary variance reduction and an explicit obstruction to averaging deterministic-start estimates

PROOF.md gives an exact decomposition of stationary empirical variance into conditional fluctuations and variance of the conditional mean over the initial state. With one-server marginal convergence assumed, it identifies the additional concentration needed for full-state asymptotic independence. It also gives a quantitative sufficient condition on sets of large stationary probability.

The reduction is tested inside the FIFO supermarket model with G=δ₁. An exchangeable mixture of all-empty and all-busy initial states has

\[
\operatorname{Var}\!\left(N^{-1}\sum_i1_{\{Q_i(t)=0\}}\right)
\geq \tfrac14 e^{-2\lambda dt},\qquad 0\leq t<1.
\]

A separate calculation proves tagged emptiness covariance at least 1/8 at t=min(1/2,1/(8λd)), for every N≥max(d,2). Both sampling conventions are covered. This is a transient example, not a counterexample to stationary independence. The reduction and example use elementary identities; no novelty claim is made for those identities.

The literature check took about four minutes. No verified resolution was found. Pooja Agarwal and Kavita Ramanan characterize hydrodynamic invariant states but leave the stationary-limit identification conjectural in the opened [arXiv:2008.08510](https://arxiv.org/pdf/2008.08510), Section 4.2. Reza Aghajani and Kavita Ramanan likewise distinguish transient results from stationary convergence in [arXiv:1707.02005](https://arxiv.org/pdf/1707.02005).

A claimed stationary result deserves further audit: Maria Clara Fittipaldi, Matthieu Jonckheere, Sergio I. Lopez, [arXiv:1809.05373](https://arxiv.org/pdf/1809.05373), Proposition 4.1. Its Section 4 invokes initial-law uniformity, whereas Proposition 2.1 explicitly concerns deterministic starts. The example proves that this distinction needs an additional argument. This session does not certify or refute the proposition through a complete audit of the paper. No SOLVED_ELSEWHERE.md was created.

Validation was symbolic: conditional variance versus a direct joint-event calculation; inclusion-exclusion versus a union bound; exact t=0 values; N=d; replacement sampling; and the time-one boundary. The product-test proof independently checks the k(k-1)/(2N) sampling error. Details and limitations are in PROOF.md and LOG.md.

Commands: literature used the web search/open/find tool; files were written with apply_patch. Local checks used `OMP_NUM_THREADS=1 nice -n 15 /bin/sh -c 'wc -l PROOF.md LOG.md'`. No computation script or numerical data is claimed. The shell reported a priority-setting restriction; no heavy computation was run. No git, external writes, or subagents were used.

What remains unproved: convergence and uniqueness of the one-server stationary marginal; the additional conditional-mean concentration; and the original arbitrary-G stationary product-limit assertion. The stationary occupation/tightness idea initially considered was replaced before proof work.

Next worker: audit the deterministic-to-stationary passage in arXiv:1809.05373 before treating its claim as a solution. For a constructive continuation, prove estimate (14) of PROOF.md at times t_N for which the conditional fluctuation error also tends to zero. An estimate only for queue-length tests will not establish the full-state assertion.

Task: “Open problem T430: Asymptotic independence in the supermarket model with general service times”; received 2026-11-14 approximately 22:16 Asia/Tbilisi (18:16 UTC).
