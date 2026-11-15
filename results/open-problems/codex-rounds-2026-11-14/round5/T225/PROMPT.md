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
VERDICT: PARTIAL prediction-relevant exponentially small symmetry-restricted proximal gaps arbitrarily near Gaussian initialization

The general nonlinear MFLD risk-time question remains unresolved. The new
result shows that the polynomial frozen quotient gap from round 3 cannot
be extended uniformly to even a small fixed KL neighborhood of its Gaussian
initialization, including symmetric laws of lower risk and bounded moments.

For the same sine teacher, Gaussian inputs and fixed Gaussian parameter
prior, take independent standard Gaussians B,W and the explicit laws

\[
 \rho_\eta=\operatorname{Law}(B+\eta g(W),W),\qquad0<\eta\leq1.
\]

Here `g(w)=E sin(X)sin(wX)`. These laws have
`KL(rho_eta||pi)=eta^2 J/2`, second parameter moment `2+eta^2 J`, and
strictly lower teacher risk than pi, where
`J=(exp(-1/3)-exp(-1))/(2sqrt(3))`.
Their exact residual correlation is

\[
 G_\eta(w)=g(w)-\frac\eta{\sqrt3}
                   e^{-(1+w^2)/3}\sinh(w/3).
\]

PROOF.md proves that G_eta has exactly one positive zero. It has a positive
lobe and a negative lobe on the positive half-line. If A_eta and B_eta
are their positive heights, the corresponding proximal law satisfies

\[
 \limsup_{\lambda\downarrow0}\lambda^2\log\beta_S(p_{\eta,\lambda})
 \leq-\tfrac12\min(A_\eta^2,B_\eta^2)<0,
\]

and the same bound holds for its restricted LSI constant. Here S reverses
both parameter signs, as in round 3. The usual density comparison supplies
an exponential lower bound of the same order in lambda^-2; the precise
exponent is not claimed. The separating cutoffs are S-invariant, and
centered perturbations along them change predictions and give a nonconstant
quadratic teacher risk. Thus this bottleneck survives symmetry reduction
and is visible to prediction.

The earlier results hold. LOG.md records the independent re-derivation of
the original exponent, round-3 folded inequality, physical-time factor,
and nonlinear symmetrization identity. AUDIT.md independently checks the
new residual by two-kernel Gaussian integration, the unique zero by a
second-derivative test, the gap exponent by exact bridge capacity, and
prediction visibility by a conditional covariance. It also recovers J a
second way. No numerical simulation or eigenvalue computation was needed.

What failed: a nearby-law counterexample cannot be promoted to a statement
about the actual nonlinear trajectory. These rho_eta are explicit frozen
output-drift shears, not proved MFLD states. A rare well's prediction effect
can be very small, so visibility alone does not prove a lower bound for
reaching epsilon risk. The exponent depends on eta and tends to zero as
eta tends to zero; no contradiction with the earlier initialization gap
is present. No nonlinear runtime or annealing guarantee is claimed.

The brief web update found no whole-problem solution. LITERATURE.md lists
the three opened primary sources and their scope. This check does not
establish absence of a solution or novelty of the present application.

Commands: read-only inspections used `rg --files`, `cat` and `sed` under
`OMP_NUM_THREADS=1 nice -n 15`; final inspections are recorded in LOG.md.
The sandbox printed `nice: setpriority: Operation not permitted`, so no
heavy or numerical program was run with unverified priority. There is no
computation script or dataset. Deliverables were written with apply_patch
only inside this folder. Both earlier folders were read only. No git,
subagents, shared-state commands, posting or external mutation was used.

Next worker: analyze the actual trajectory's broader residual tails and
their prediction mass. One concrete starting point is the exact initial
predictor derivative: it has both output-weight and hidden-weight motion,
whereas the shear above keeps only the former and freezes the residual.
Determine whether the true residual develops a negative secondary lobe,
then whether that lobe carries enough mass to affect epsilon risk. A
uniform quotient-gap argument based only on symmetry, nearby KL, lower
risk and bounded second moments is now ruled out.

Task: “take the NEXT checkable step on this problem, building on that work”
— 15 November 2026, approximately 05:07 Asia/Tbilisi; first recorded clock
was 05:07:42.
