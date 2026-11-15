# Open problem T225: Convergence time of mean-field Langevin dynamics at low temperature

Statement: Mean-field Langevin dynamics minimizes F_lambda(rho) = R(rho) + lambda·KL(rho || pi) for a two-layer network risk R, where pi is a confining reference measure (e.g. a Gaussian prior, equivalently an L2 weight penalty plus entropy; with Lebesgue entropy on unbounded parameters F_lambda is unbounded below: spreading the output weights a as N(0, s²) independently of w leaves f_rho = 0 and the risk fixed while the entropy goes to −∞). It converges exponentially at a rate set by a uniform log-Sobolev constant of the proximal Gibbs measures, which in general is exp(−C/lambda). For a realizable two-layer regression problem in dimension d (smooth activation, Gaussian inputs, a teacher with a bounded number of neurons and bounded weights, all of which the bound may depend on polynomially), decide whether the time for MFLD (with lambda tuned or annealed) to reach risk R ≤ inf R + epsilon is polynomial in d and 1/epsilon, or prove an exponential lower bound.

Caveat: The question is about the unregularized risk reached through small lambda, not the regularized objective at fixed lambda. Chizat's theorems exclude the vanilla unbounded two-layer parameterization and note a smoothness issue for ReLU, so they do not cover plain ReLU (auditor codex-w687, 16 Oct).

Source: L. Chizat, Mean-Field Langevin Dynamics: Exponential Convergence and Annealing, arXiv:2202.01009 (2022); A. Nitanda, D. Wu and T. Suzuki, Convex Analysis of the Mean Field Langevin Dynamics, arXiv:2201.10469 (2022)

Where it stands (checked by us, Nov 2026): Open. Exponential-in-1/lambda LSI constants are what the general theory gives; annealing gives only logarithmic convergence. Some structured targets (e.g. single-index) have polynomial guarantees in later work (to verify).

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T225 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T225 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T225 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 5 worker built on the latest of these. Its folder is ~/codex_op_1114r5/briefs/T225 (read it, never
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
VERDICT: PARTIAL exact initial nonlinear residual motion and a quantitative positivity window for the sine teacher

The general polynomial-versus-exponential MFLD risk-time question remains
unresolved. The preceding shear obstruction is correct. The new result
derives the actual nonlinear flow's initial motion and shows why that
shear cannot substitute for it.

For the same one-neuron sine teacher, Gaussian inputs and fixed standard
Gaussian parameter prior, define
\[
 g(w)=e^{-(1+w^2)/2}\sinh w,\qquad
 G_t(w)=\mathbb E[(\sin X-f_{\rho_t}(X))\sin(wX)].
\]
Starting from the prior, PROOF.md proves
\[
 \dot G_0(w)=-\frac{e^{-(1+w^2)/3}}{9\sqrt3}
 [(10-2w^2)\sinh(w/3)+5w\cosh(w/3)].
\]
This derivative includes output-weight and hidden-weight motion and is
independent of the initial temperature. Its sign changes exactly once
on the positive half-line, from negative to positive, at a frequency
between 3 and 5. In particular the true initial residual derivative is
positive in the far-frequency tail; the earlier shear's derivative is
negative there.

Writing D for the negative of this derivative, the tangent residual
`g-tD` is positive on the entire positive half-line for sufficiently
small t. For actual local MFLD solutions, the proof also establishes
\[
 |G_t(w)-g(w)+tD(w)|\leq C_Tt^2\min(|w|,1),
\]
uniformly over constant temperatures `0<lambda<=1`. Consequently
`G_t(w)>=g(w)/4>0` for
\[
 0<w\leq\sqrt{4\log(1/t)-1-2\log(4C_T)}
\]
at sufficiently small times. The explicit, loose constant is
`C_T=15000(13exp(20T))^2`. These statements apply to W2-continuous
weak MFLD solutions with locally bounded fourth moments and the
free-energy inequality, initialized at the prior. No general
well-posedness theorem is claimed.

The initial risk slope is exactly
\[
 \dot R_0=-\frac{13e^{-1/3}-3e^{-1}}{18\sqrt3}.
\]
AUDIT.md independently recovers the residual derivative from the initial
Fokker–Planck density derivative and Gaussian moment-generating functions,
and the risk slope from parameter-gradient dissipation. It rechecks
the moment and Taylor constants with scalar Itô calculus and a second
product-rule expansion of the generator. The earlier restricted-gap
exponent is re-derived using exact bridge capacity, including the rare
well's mass. No discrepancy was found.

What failed: the Taylor estimate is absolute, not relative to the
Gaussian-decaying g. It cannot establish positivity on the whole
half-line at a fixed positive time. A remote or later negative lobe
remains possible. No restricted proximal-gap estimate along the actual
flow, polynomial learning-time guarantee, exponential learning-time lower
bound, or annealing remainder estimate is obtained.

The five-minute web update found no whole-problem solution. LITERATURE.md
records the three opened primary sources and their scope. This is a
limited check and does not establish absence of a solution or novelty.

Commands: earlier work and the deliverables were inspected with
`rg --files`, `cat`, `head`, `sed` and `wc`, using
`OMP_NUM_THREADS=1 nice -n 15` after the initial directory listing.
The sandbox reports `nice: setpriority: Operation not permitted`, so no
simulation or numerical program was run under unverified priority.
There is no computation script or dataset: the result is analytic.
LOG.md records the searches, derivations and readback commands. All
writes used apply_patch inside this folder. Earlier folders were read
only; no git, subagents or shared-state commands were used.

Next worker: obtain a remainder estimate that resolves the residual
tail at positive time, rather than merely its derivative at zero.
The useful exact starting point is
`dot rho_0 = a[g(v)+v g'(v)-g''(v)]pi` and the kernel generator formula
in PROOF.md (37). Determine whether remote negative lobes occur beyond
the positivity window, or whether an appropriate sign/shape property
persists. Any eventual risk-time obstruction must also quantify the
prediction mass of the secondary well. The shear is a valid nearby-law
counterexample, but its tail sign does not match the full initial flow.

Task: “take the NEXT checkable step on this problem, building on that work”
— 15 November 2026, approximately 08:44 Asia/Tbilisi.
