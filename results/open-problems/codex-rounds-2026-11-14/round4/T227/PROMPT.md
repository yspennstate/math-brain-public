# Open problem T227: The catapult phase of large-learning-rate training

Statement: Lewkowycz et al. observe for wide networks three regimes in the step eta relative to lambda_0, the top eigenvalue of the neural tangent kernel at initialization: lazy for eta < 2/lambda_0, a catapult phase for 2/lambda_0 < eta < eta_max ≈ c/lambda_0 in which the loss first grows, the curvature drops, and training then converges, and divergence above eta_max. Prove the existence of the catapult phase and identify eta_max for a fixed deep nonlinear architecture of large finite width (stated activation, input and label law, normalization of the initialization), as an eta interval on which the loss rises and then converges with high probability.

Caveat: The two-layer linear 'uv' model is solved in the original paper; the question is about nonlinear and deep networks.

Source: A. Lewkowycz, Y. Bahri, E. Dyer, J. Sohl-Dickstein and G. Gur-Ari, The large learning rate phase of deep learning: the catapult mechanism, arXiv:2003.02218 (2020)

Where it stands (checked by us, Nov 2026): Proved for the uv model and some quadratic models (Zhu et al. 2022-23, to verify). Open for deep nonlinear networks.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T227 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T227 (read it,
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
VERDICT: PARTIAL a probability-one catapult interval for a fully connected three-layer tanh network with noncentered initialization; eta_max remains open

The earlier sparse-network certificate holds on independent recheck. The new result replaces its diagonal second hidden layer with a fully connected layer. All `m^2+2m` coordinates are independently initialized and separately trained; the proof does not restrict training to equal neurons or an invariant subspace.

For every finite width `m>=1`, the architecture is

\[
 F_\theta(x)=\frac1m\sum_i a_i\tanh\left(
 \frac1{\sqrt m}\sum_j B_{ij}\tanh(c_jx)\right),
 \qquad L=\tfrac12F_\theta(1)^2.
\]

The data law is the point mass at `(1,0)`. Independently initialize

\[
 a_i\sim\mathrm{Unif}[7.99,8.01],\quad
 B_{ij}\sim\mathrm{Unif}[.499/\sqrt m,.501/\sqrt m],\quad
 c_j\sim\mathrm{Unif}[1.999,2.001].
\]

Training is ordinary simultaneous Euclidean GD in `(a,B,c)`. The fixed middle-layer normalization is `m^{-1/2}`; output normalization is `m^{-1}`. The initialization is noncentered and narrowly concentrated.

For every initialization in this box, simultaneously for every

\[
 \boxed{.9m\leq\eta\leq1.1m},
\]

the initial loss is below `6.5`, the loss after the first update exceeds `19`, and the subsequent loss contracts by at least a factor `1/64` per step to zero. Every parameter converges. The scalar NTK satisfies

\[
 \frac{37}m<\lambda_0<\frac{39}m,\qquad
 \frac{1-10^{-8}}m<\lambda_t<\frac{1+10^{-8}}m\quad(t\geq1).
\]

Thus `[36/lambda_0,40/lambda_0]` is also a certified interval, entirely above `2/lambda_0`. The probability is exactly one under the stated law. The kernel quantity is the NTK, not the loss Hessian.

The new lemma bounds the full Euclidean cross-gradient throughout the saturated dense region

\[
 |a_i|\leq16,\qquad-26\leq\sqrt m B_{ij}\leq-18,\qquad c_j\geq1.
\]

In particular, the shared first-layer derivative obeys
`|m*partial F/partial c_j|<=416*10^{-10}`. The first update enters this region, and summable movement preserves both bounds on every dense weight. A segment integral then proves contraction. All steps are in [PROOF.md](PROOF.md).

Reproduce the independent old-result check and the two dense audits with:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B recheck_previous.py
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B verify_dense.py
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B audit_dense_intervals.py
```

All passed. The first script checks the earlier arithmetic independently and runs 50 sparse-network audits. The second checks exact rational bounds, 450 dense-network trajectories, and 256 cross-gradient pairs. Automatic-differentiation error was below `4.5e-16`, finite-difference gradient error below `2.0e-10`, and disagreement between actual Euclidean updates and the auxiliary-coordinate recurrence below `5.4e-15`. The third independently sums rational interval gradients in the original coordinates at widths 1, 4, 9 and 64, confirming the entrance and tail margins. Its checks cover full boxes, not sampled initializations. The general-width theorem is proved analytically.

Each script used less than 24 MB peak RAM and finished in under two seconds. They use one thread, standard-library scalar arithmetic, no torch or GPU, and a CPU limit of at most 120 seconds. The inherited nice value is 20; the sandbox's warning on `nice -n 15` does not increase the process priority. Commands, outputs, exact fractions and audit details are in [LOG.md](LOG.md), `previous_recheck.json`, `dense_verification.json`, and `interval_audit.json`.

The literature update took less than five minutes. Opened primary sources included Aitor Lewkowycz, Yasaman Bahri, Ethan Dyer, Jascha Sohl-Dickstein and Guy Gur-Ari, [arXiv:2003.02218](https://arxiv.org/abs/2003.02218); Libin Zhu, Chaoyue Liu, Adityanarayanan Radhakrishnan and Mikhail Belkin, [ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/file/949b3011c50300a2b4e60377466f52a8-Paper-Conference.pdf); Quan Nguyen, Robin Yadav, Param Mody and Mark Schmidt, [arXiv:2610.23007](https://arxiv.org/abs/2610.23007); and Thomas Hofmann, [arXiv:2607.04993](https://arxiv.org/html/2607.04993v1). Their checked scopes did not supply a solution of the requested deep finite-width problem. This bounded check is not an exhaustive absence or novelty claim.

No certificate or numerical audit failed. A direct reuse of the sparse tail estimate would leave dense column sums uncontrolled; the bounded dense-weight region supplies the missing estimate. What remains open is `eta_max`, a divergence theorem, the behavior near `2/lambda_0`, centered initialization, and nontrivial data laws. The upper endpoint of this certificate is not a maximal stable step.

Next worker: retain the full-space dense tail lemma and seek an entrance certificate for a product initialization with independent signs. Simply symmetrizing this box does not preserve the common residual and row-sign estimates. Establish a concrete finite-width sign/margin event before using concentration; a centered law alone does not imply the entrance conditions. Identifying `eta_max` requires a separate argument.

Task T227: “take the NEXT checkable step on this problem, building on that work.” Session start: 2026-11-15 03:33 Asia/Tbilisi.
