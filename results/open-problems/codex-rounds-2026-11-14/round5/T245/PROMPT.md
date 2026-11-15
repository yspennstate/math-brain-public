# Open problem T245: Evolution of the neural tangent kernel when depth and width are comparable

Statement: For a depth-L network of width n trained by gradient descent, the NTK is deterministic and frozen during training in the limit n → ∞ at fixed L. Hanin and Nica show that at initialization its fluctuations are of order exp(c·L/n) − 1, so it is random when L/n is not small. Determine the law of the NTK and of its change over training in the joint limit L, n → ∞ with L/n → t > 0, and decide whether feature learning (a nontrivial change of the NTK) occurs at a rate set by t.

Caveat: Huang and Yau's neural tangent hierarchy gives the finite-width dynamics as an infinite hierarchy; the question is a closed description in the joint limit.

Source: B. Hanin and M. Nica, Finite Depth and Width Corrections to the Neural Tangent Kernel, arXiv:1909.05989 (2019); J. Huang and H.-T. Yau, Dynamics of Deep Neural Networks and Neural Tangent Hierarchy, arXiv:1909.08156 (2019)

Where it stands (checked by us, Nov 2026): Open (initialization fluctuations known; training-time behaviour in the joint limit not rigorous).

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T245 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T245 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T245 (read it,
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
VERDICT: PARTIAL finite-dimensional global gradient-flow closure and exact discrete-GD balance defect for the structured deep-linear model

The earlier scalar and matrix-profile results hold on recheck. The new result replaces the depth profile by an end-to-end matrix and bias **after the small-step limit**, and proves global existence of that flow. This is still the scalar-identity initialization of a fully trainable linear network. The original independent-Gaussian/ReLU joint training-law problem is not solved.

For fixed active dimension d, conditional on the same initial gain

\[
S=\exp(\mu t+\sigma\sqrt t\,Z),
\]

the limiting state is P in R^{d by d} and b in R. With weighted residual mean h and residual-input sum g, [PROOF.md](PROOF.md) proves

\[
\dot P=-t\int_0^1(PP^T)^{1-z}eg^T(P^TP)^z\,dz,
\qquad \dot b=-h,\qquad P(0)=SI,
\]
\[
f(x)=b+e^TPx_E,
\qquad K(x,x')=1+x_E^TMx'_E+B\langle x_\perp,x'_\perp\rangle,
\]
\[
M=t\int_0^1[e^T(PP^T)^{1-z}e](P^TP)^z\,dz,
\quad B=t\int_0^1S^{2z}e^T(PP^T)^{1-z}e\,dz.
\]

These integrals are explicit logarithmic-mean functions of the singular values and singular vectors; no depth grid is part of the state. All randomness still comes from S. The order of limits is size first, then step size, on each fixed continuous training interval.

The main bridge is the conserved profile identity

\[
\mathcal D(C):=(C+C^T)_z-t[C,C^T]=0.
\]

It forces U(z)^TU(z)=(U(1)^TU(1))^z and V(z)V(z)^T=(U(1)U(1)^T)^{1-z}. Thus noncommuting profiles can still have an endpoint description of their output and kernel. For initial squared loss ell_0, every finite-time singular value satisfies

\[
S e^{-\sqrt{t\tau\ell_0}}\le\sigma_j(P(\tau))
\le S e^{\sqrt{t\tau\ell_0}},\qquad
|b(\tau)|\le\sqrt{\tau\ell_0}.
\]

This proves global existence without requiring the data to span the active space.

The balanced end-to-end operator and its infinite-depth form are existing deep-linear mathematics, discussed by [Armin Eftekhari](https://proceedings.mlr.press/v119/eftekhari20a/eftekhari20a.pdf) and [Nadav Cohen, Govind Menon, Zsolt Veraszto](https://arxiv.org/abs/2210.12497). The advance beyond the earlier session is the direct connection to its unequal-gain random profile, the full perpendicular kernel, the finite-time bounds, and control of the discrete defect. No literature novelty claim is made for the operator itself. A literature check lasting less than five minutes found no whole-problem solution.

The formula fails as an exact discrete-GD closure. If G is the current profile vector field, one Euler step satisfies exactly

\[
\mathcal D(C+\eta G)=\mathcal D(C)-t\eta^2[G,G^T].
\]

Its accumulated defect is O(eta) on each fixed training interval. In the preceding two-example benchmark, after just one step,

\[
[M_1,P_1^TP_1]_{12}=\eta^3/48+\eta^5/640>0,
\]

whereas the flow kernel always commutes with P^TP. Substituting the discrete endpoint into the balanced formula gives errors beginning at eta^2/24 in M_22 and eta^2/48 in B. This rules out using this particular flow formula unchanged at fixed learning rate; it does not rule out every finite-dimensional discrete description.

Verification command:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 verify.py > verification_output.txt 2>&1
```

The script uses only the standard library. [LOG.md](LOG.md) records commands and results; [verification_output.txt](verification_output.txt) and [verification_data.json](verification_data.json) contain the complete output and data.

- Exact rational arithmetic rechecks the earlier first-step kernel, second-step depth dependence and eta^6/32 commutator, and verifies the new kernel commutator and finite-layer balance-defect identity.
- Spectral logarithmic means versus independent depth quadrature: error below 2.25e-12. Initial kernel rate versus central differences: below 2.16e-10.
- Raw finite-layer flow kernels versus the exact finite-depth balanced power sum: below 1.13e-10. At n=256, full-state errors versus the infinite-depth law were .001365, .000326, .002126 for t=.5,1,2 in the tested cases, decreasing by about four per factor-four size increase.
- The earlier discrete profile approaches the endpoint flow at time .4: errors .00350,.00172,.000855,.000426 for eta=.04,.02,.01,.005. Depth-grid refinement changes the finest result by less than 4.61e-8.
- Scalar reduction, positive and negative residuals, repeated singular values, zero residuals, zero inputs, and loss dissipation passed. Unequal gains and their reversals approach the same limit in the tested deterministic arrays.
- Final run: 1.05 seconds, below 26 MB peak RSS, one thread, inherited priority 20. The nice warning and direct priority check are recorded in the log.

What failed: exact balanced closure at fixed discrete learning rate. No failed numerical assertions occurred. What remains uncertain: any finite-variable closure at fixed eta, stability under nonaligned perturbations or independent Gaussian matrices, ReLU gate changes, and simultaneous size/step-size or infinite-time limits. The numerical errors above are diagnostics, not rigorous finite-size error bounds.

Next worker: use the exact defect recurrence to derive a first correction in eta to the endpoint flow, or show what additional depth information that correction requires. In particular, decide whether the accumulated commutator field can be recovered from P and finitely many extra matrices. The exact positive commutator above and the earlier C_2(z) formula are mandatory checks. This would address the gap left by the present small-step reduction while retaining the same model.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, 05:11 Asia/Tbilisi (session receipt).
