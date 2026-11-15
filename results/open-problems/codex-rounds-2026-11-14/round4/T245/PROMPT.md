# Open problem T245: Evolution of the neural tangent kernel when depth and width are comparable

Statement: For a depth-L network of width n trained by gradient descent, the NTK is deterministic and frozen during training in the limit n → ∞ at fixed L. Hanin and Nica show that at initialization its fluctuations are of order exp(c·L/n) − 1, so it is random when L/n is not small. Determine the law of the NTK and of its change over training in the joint limit L, n → ∞ with L/n → t > 0, and decide whether feature learning (a nontrivial change of the NTK) occurs at a rate set by t.

Caveat: Huang and Yau's neural tangent hierarchy gives the finite-width dynamics as an infinite hierarchy; the question is a closed description in the joint limit.

Source: B. Hanin and M. Nica, Finite Depth and Width Corrections to the Neural Tangent Kernel, arXiv:1909.05989 (2019); J. Huang and H.-T. Yau, Dynamics of Deep Neural Networks and Neural Tangent Hierarchy, arXiv:1909.08156 (2019)

Where it stands (checked by us, Nov 2026): Open (initialization fluctuations known; training-time behaviour in the joint limit not rigorous).

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T245 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T245 (read it,
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
VERDICT: PARTIAL closed depth-profile NTK dynamics for multiple training directions in the structured deep-linear model

The earlier scalar result holds. The new result extends its initialization to any fixed-dimensional active block trained on finitely many noncollinear examples. [PROOF.md](PROOF.md) proves convergence of the outputs and full NTK at every fixed finite collection of gradient descent steps when L/n tends to t>0. This remains a scalar-identity initialization of a fully trainable linear network, not independent Gaussian weight matrices or a ReLU network.

The limiting state is a scalar bias and a continuous d by d matrix function C_k(z), with normalized depth z in [0,1]. All randomness enters through the same initial variable S=exp(mu*t+sigma*sqrt(t)*Z) as in the earlier report. Define

\[
U_k'=tC_kU_k,\quad U_k(0)=I,\qquad
V_k(z)=U_k(1)U_k(z)^{-1}.
\]

For weighted residual mean h_k and weighted residual-input sum g_k, the closed update is

\[
b_{k+1}=b_k-\eta h_k,\qquad
C_{k+1}(z)=C_k(z)-\eta S V_k(z)^Te\,g_k^TU_k(z)^T.
\]

The full kernel is

\[
K_k(x,x')=1+x_E^TM_kx'_E+B_k\langle x_\perp,x'_\perp\rangle,
\]
\[
M_k=tS^2\int_0^1\|V_k(z)^Te\|^2U_k(z)^TU_k(z)\,dz,
\quad B_k=tS^2\int_0^1\|V_k(z)^Te\|^2\,dz.
\]

This is a function-valued closure, not a recursion on one matrix. It recovers the earlier scalar recursion when there is one training direction.

A two-dimensional example makes the distinction explicit. Take t=S=1, readout e_1, training inputs e_1,e_2, both targets 1, and loss weights 1/2. The first active kernel matrix is exactly

\[
M_1=\begin{pmatrix}
1+\eta^2/12&\eta/4+\eta^3/96\\
\eta/4+\eta^3/96&1+\eta^2/6+\eta^4/480
\end{pmatrix},\qquad B_1=1+\eta^2/12.
\]

The diagonal kernel entries have zero initial derivative, while the off-diagonal entry has derivative 1/4. After two updates,

\[
(C_2(z))_{22}=\eta^2(1-\eta)(1-z)/4.
\]

Thus the common-matrix-per-layer ansatz fails for 0<eta<1. Moreover, the (2,1) entry of the commutator of C_2(0) and C_2(1) is eta^6/32, so these blocks genuinely do not commute. The choice S=1 is a deterministic benchmark covered by the proof; it is not a positive-probability event under the continuous lognormal law.

For general data the initial matrix-kernel rate is

\[
\dot M_0=-t^2S^3\left[(e^Tg_0)I+
                 \tfrac12(eg_0^T+g_0e^T)\right],\qquad
\dot B_0=-t^2S^3e^Tg_0.
\]

Here the rate means the first-step difference divided by eta as eta tends to zero, after the size limit. A separate finite-size differentiation gives the same formula. The absolute prefactor is t^2; dividing by the initial matrix-weight coefficient tS^2 gives a t prefactor. These comparisons fix S; its distribution also changes with t.

Verification command, run from this folder:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 verify.py
```

[verify.py](verify.py) uses only the standard library. Complete output is in [verification_output.txt](verification_output.txt), detailed data in [verification_data.json](verification_data.json), and the commands and decisions in [LOG.md](LOG.md).

- Independent scalar recheck: exact finite-size error 2.23e-16; limiting scalar recursion versus the matrix profile, 1.83e-12.
- Dense numerical parameter derivatives, including entries outside the active block: kernel error below 8.52e-12 over 432 partial derivatives; update error below 6.83e-14.
- Initial kernel rate, finite-size formula versus symmetric differences: error below 2.32e-10.
- First-step polynomial kernel: error below 4.96e-14. The second-step depth-profile formula agrees within 2.00e-17.
- At n=8192, maximum full-state errors over five states are 3.54e-5, 5.61e-5, and 1.89e-4 for t=0.5,1,2. These arrays condition the scalar product to S=1.3. Reference-grid refinement differences are below 3.0e-10.
- One-layer, zero-residual, zero-input, and reversed-gain-order cases were checked. Runs used under 50 MB peak RSS and finished in under three seconds at inherited priority 20. The script checks priority, memory and runtime; the macOS nice warning is recorded in LOG.md.

What failed: replacing the earlier scalar c_k by a single common matrix is not invariant under training. The depth profile resolves this obstruction within the structured model. No initial perturbation stability or Gaussian-matrix universality argument was obtained. A bounded literature check found no whole-problem solution; in particular Qiyang Han and Masaaki Imaizumi's [arXiv:2505.04898](https://arxiv.org/abs/2505.04898), which was opened, keeps width and depth bounded in its proportional regime. No claim of literature novelty is made for deep-linear dynamics.

What remains uncertain: the original Gaussian ReLU training law, robustness to nonaligned initialization, and convergence on a growing training horizon. The numerical convergence errors are diagnostics, not rigorous error bounds. The proved closure is still infinite dimensional in its depth argument.

Next worker: determine whether the profile can be replaced by finitely many variables for the two-example model, or prove an obstruction stronger than failure of the common-block ansatz. A concrete starting point is the balancedness identities for deep-linear gradient flow; their discrete-GD defects must be controlled before using them here. The present C_2(z) and its nonzero commutator are exact checks any proposed reduction must pass.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, 03:34 Asia/Tbilisi (session receipt).
