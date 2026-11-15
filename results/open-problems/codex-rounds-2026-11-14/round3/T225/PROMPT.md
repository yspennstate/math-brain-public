# Open problem T225: Convergence time of mean-field Langevin dynamics at low temperature

Statement: Mean-field Langevin dynamics minimizes F_lambda(rho) = R(rho) + lambda·KL(rho || pi) for a two-layer network risk R, where pi is a confining reference measure (e.g. a Gaussian prior, equivalently an L2 weight penalty plus entropy; with Lebesgue entropy on unbounded parameters F_lambda is unbounded below: spreading the output weights a as N(0, s²) independently of w leaves f_rho = 0 and the risk fixed while the entropy goes to −∞). It converges exponentially at a rate set by a uniform log-Sobolev constant of the proximal Gibbs measures, which in general is exp(−C/lambda). For a realizable two-layer regression problem in dimension d (smooth activation, Gaussian inputs, a teacher with a bounded number of neurons and bounded weights, all of which the bound may depend on polynomially), decide whether the time for MFLD (with lambda tuned or annealed) to reach risk R ≤ inf R + epsilon is polynomial in d and 1/epsilon, or prove an exponential lower bound.

Caveat: The question is about the unregularized risk reached through small lambda, not the regularized objective at fixed lambda. Chizat's theorems exclude the vanilla unbounded two-layer parameterization and note a smoothness issue for ReLU, so they do not cover plain ReLU (auditor codex-w687, 16 Oct).

Source: L. Chizat, Mean-Field Langevin Dynamics: Exponential Convergence and Annealing, arXiv:2202.01009 (2022); A. Nitanda, D. Wu and T. Suzuki, Convex Analysis of the Mean Field Langevin Dynamics, arXiv:2201.10469 (2022)

Where it stands (checked by us, Nov 2026): Open. Exponential-in-1/lambda LSI constants are what the general theory gives; annealing gives only logarithmic convergence. Some structured targets (e.g. single-index) have polynomial guarantees in later work (to verify).

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T225 (read it,
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
VERDICT: PARTIAL sharp exp(-Theta(lambda^-2)) proximal LSI asymptotic for a realizable sine teacher with fixed Gaussian prior

For `X~N(0,1)`, activation `sin`, teacher `sin(X)`, half squared loss, and
fixed prior `N(0,I_2)`, PROOF.md proves that the proximal Gibbs law at
initialization `rho_0=pi` satisfies

\[
 \lim_{\lambda\downarrow0}\lambda^2\log\alpha_\lambda
 =\lim_{\lambda\downarrow0}\lambda^2\log\beta_\lambda
 =-M^2/2,
 \quad
 M=\max_w e^{-(1+w^2)/2}|\sinh w|.
\]

Here alpha is the best LSI constant and beta is the best Poincare constant,
both defined explicitly in the proof. The maximum occurs at the unique
positive root of `w tanh(w)=1` and its negative. Completing the square in
the unbounded output weight, followed by a bounded density comparison and
a Lipschitz shear, gives the lower estimate. A sign test gives the matching
upper estimate. The proof includes the functional-inequality ingredients.

This rules out a uniform bound `alpha>=c exp(-C/lambda)` in this allowed
example with a fixed Gaussian prior. It sharpens the caveat about vanilla
unbounded output weights: bounded activation alone does not give the usual
Arrhenius scale. A fixed quadratic penalty independent of temperature is a
different convention and is not covered by this asymptotic.

It does **not** establish an exponential risk-time lower bound. Simultaneous
sign reversal of `(a,w)` leaves `a sin(wx)` unchanged. The bottleneck
perturbations used here therefore have exactly equal predictors and risks.
Also, this proximal law is frozen at initialization; it is not asserted to
be a self-consistent stationary law. The full question remains unresolved
by this session.

The short primary-source literature check found no whole-problem solution.
LITERATURE.md lists the opened sources and their scope, including
[Mousavi-Hosseini, Wu, Erdogdu, arXiv:2408.07254v2](https://arxiv.org/html/2408.07254v2)
and
[Shang, Wakayama, Lecué, Suzuki, arXiv:2606.31429v2](https://arxiv.org/html/2606.31429v2).
The search is not exhaustive and originality of the proximal-LSI calculation
has not been established.

Verification: AUDIT.md re-derives the load-bearing constants and records
attempts to break the result. No numerical experiment or numerical value
of an LSI constant is claimed. There is no computation script or data file
because the contribution is a proof.

Commands and tools: the exact web queries and significant shell output are
in LOG.md. The mathematical result requires no execution. Files were written
with `apply_patch`. Read-only shell commands included `pwd`, `rg --files`,
`cat` of the compute governor state, and `sed` of startup memories. Later
reads were invoked with `OMP_NUM_THREADS=1 nice -n 15`; the sandbox reported
`nice: setpriority: Operation not permitted` and denied `ps`. No heavy
program was run under the unverified priority. No git, network posting,
subagent, or file mutation outside this folder was used.

Next worker: study the dynamics after quotienting out
`(a,w)~(-a,-w)`, or derive a dissipation inequality directly for prediction
risk. Any runtime lower bound must exhibit a slow mode that changes the
predictor and persists under the changing self-consistent drift. The exact
Gaussian elimination in Sections 2–3 offers a simple test case for that work.

Task: “push this problem forward by one checkable piece” — 14 November 2026,
approximately 21:21 Asia/Tbilisi.
