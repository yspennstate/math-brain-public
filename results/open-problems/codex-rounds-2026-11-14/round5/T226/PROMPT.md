# Open problem T226: The edge of stability: why full-batch gradient descent hovers at sharpness 2/eta

Statement: For full-batch gradient descent with fixed step eta on a neural-network training loss, the top Hessian eigenvalue first rises to about 2/eta and then hovers there while the loss keeps decreasing non-monotonically (Cohen et al.). Fix a model (e.g. a smooth two-layer network of moderate width on Gaussian data with square loss, or a deep linear network), an initialization law and a range of eta. Prove that with probability bounded below over the initialization GD enters the edge-of-stability regime, stays there, and converges to a global minimizer whose sharpness is 2/eta + o(1) as eta → 0 (or show the event has small probability). Local theorems near a minimizing manifold (Gan 2026, Theorem 4.4, assumes a C4 loss and a nondegeneracy condition) leave open whether random initialization reaches their basin.

Caveat: Results that assume a specific cubic structure of the loss, or study two-parameter toy models, are partial. Divergence above the classical 2/L threshold is NOT what happens: the point is convergence without the descent-lemma condition.

Source: J. M. Cohen, S. Kaur, Y. Li, J. Z. Kolter and A. Talwalkar, Gradient Descent on Neural Networks Typically Occurs at the Edge of Stability, arXiv:2103.00065 (2021)

Where it stands (checked by us, Nov 2026): Partial: self-stabilization under assumptions on third derivatives (Damian, Nichani and Lee 2209.15594); Arora, Li and Panigrahi 2205.09745 for normalized losses; Ahn et al. 2204.01050; analyses of two-layer and scalar toy models. Open for genuine networks (not re-checked against 2025–26).

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T226 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T226 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T226 (read it,
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
VERDICT: PARTIAL almost-sure parameter convergence in the larger zero-target spectral rectangle

The earlier results hold on independent audit. The new result proves the missing convergence lemma named in round 3, for the same fully trainable multi-input two-layer linear network. It does not settle the distribution of endpoint sharpness.

For L_0(a,W)=||W^Ta||^2/2, set A=sqrt(eta)a, U=sqrt(eta)W, q=||A||^2, C=U^TU and v=U^TA. Suppose m>=d+1. On the larger open region

\[
 q_0<2,\qquad \|C_0\|_{\rm op}<2,
\]

almost every initial point converges in parameter space to a full-augmented-rank global minimizer. Here “almost every” is with respect to Lebesgue measure, so the claim holds for any jointly absolutely continuous initialization law, including independent N(0,tau^2/eta) original parameters. The prior theorem required q_0+||C_0||<2. The new region permits sums arbitrarily close to 4, initial residual squares above 1, and nonmonotone loss.

The deterministic theorem excludes initial rank deficiency and exact finite-time rank collapse ||v_t||^2=1. Those exclusions form a countable union of polynomial zero sets. The proof handles all other starts in the rectangle, not an aligned or balanced slice. It gives no rate and treats zero target only.

What is new is the convergence argument after strict residual contraction becomes unavailable. The exact recurrences still imply sum_t ||v_t||^2<infinity. Retaining the finitely many determinant factors with ||v_t||^2>1 preserves a positive Gram determinant unless a factor vanishes. This gives a uniform lower bound on H_t=C_t+q_t I. Put

\[
 w_t=H_t^{-1}v_t,\qquad
 F_t=Z_t(I-K(w_t)),\qquad Z_t=[A_t\ U_t],
\]

where K(x) has off-diagonal blocks x and x^T. Then w_(t+1)-w_t=-v_t+O(||v_t||^3). The linear parameter motion cancels in F_(t+1)-F_t, leaving a bound O(||v_t||^2). Thus F_t converges and Z_t-F_t tends to zero. PROOF.md writes out the identities, bounds and exceptional-set argument, including a parameter tail bound.

An exact counterexample prevents an unwarranted endpoint conclusion. Full-rank rational vectors with q_0=c_0=17/9 and v_0=(5/3,0,...,0) reach a global minimum in one step, with

\[
 q_1=\lambda_{\max}(C_1)=128/81,
 \qquad \eta\lambda_{\max}(\nabla^2L_0)=256/81>2.
\]

The construction embeds in m=16,d=8 with 144 trainable parameters. The active output mode itself gives this largest endpoint eigenvalue. Exact one-step landing is algebraically exceptional and has zero probability under Gaussian initialization. This example refutes a universal subcritical-endpoint bound on the larger region; it establishes no positive-probability edge phase.

Verification command, run in this folder:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify_rectangular.py > verification.final.stdout.txt 2> verification.final.stderr.txt
```

Exit 0. Standard library only, one thread, effective nice 20, elapsed 2.5671 seconds, peak RSS 18,317,312 bytes. CPU and wall caps were 60 and 90 seconds. The nice utility printed a permission warning; the program independently checked its already-lower execution priority before arithmetic.

Thirty-two exact rational cases verified the recurrences, Gram determinant and both new cancellation identities. Direct parameter updates and independent Gram formulas agree on all counterexample constants; a lifted eigenvector checks the full endpoint Hessian eigenvalue 256/81. A separate full-rank example with h_0=1 verifies that rank collapse really occurs inside the rectangle. The earlier bootstrap constants and 3.47305198969e-51 Chernoff bound pass independent recomputation.

Twenty-six finite trajectories started outside the old basin, all inside the larger rectangle; thirteen had h>1 and sixteen had loss increases. Twenty-five reached residual norm below 1e-13. One remained at 4.137805211333266e-7 after 5,000 updates. An initial script wrongly demanded a tiny residual within that fixed budget and failed there. That unsupported finite-time expectation was removed; the failed output is retained. No proved identity failed. Finite trajectories do not replace the convergence proof or supply a rate.

The literature check stopped within five minutes. No opened source supplied the requested random-entry theorem, so no SOLVED_ELSEWHERE.md was created. This is a bounded search, not an exhaustive openness claim. Sources actually opened:

- Jaerin Lee and Kyoung Mu Lee, *A Journey to the Edge of Stability*, [arXiv:2609.32290](https://arxiv.org/abs/2609.32290): its abstract concerns empirical optimizer and learning-rate regimes.
- Peter Zaika and Zakhar Shumaylov, *Non-Euclidean Gradient Descent Has Many Edges of Stability*, [arXiv:2610.15223](https://arxiv.org/abs/2610.15223): its abstract concerns non-Euclidean dynamics on quadratic objectives.
- Hee-Sung Kim and Sungyoon Lee, *Gradient Descent with Large Step Size Restores Symmetry in Deep Linear Networks with Multi-Pathway*, [arXiv:2606.05219, Appendix E.7](https://arxiv.org/html/2606.05219v1): the opened full text keeps its EoS analysis local and conditional on self-stabilized sharpness bracketing; it does not prove the general entry statement here.
- Berk Tinaz, Changzhi Xie and Mahdi Soltanolkotabi, *When Both Layers Learn: Training Dynamics of Representing Linear Models via ReLU Networks*, [arXiv:2606.04476](https://arxiv.org/abs/2606.04476): its abstract proves global convergence from moderately small random initialization, without an edge-endpoint assertion.

What remains uncertain: no sharpness law is proved on the enlarged rectangle, no rate is established there, and rank-collapse starts are not classified by this proof. The earlier small-nonzero-target persistence does not automatically extend to critical or supercritical endpoints. There is no novelty claim against the full orthogonalization or matrix-factorization literature.

Next checkable step: determine whether, for Gaussian starts in this rectangle, the limiting output matrix C_infinity+q_infinity I has an eigenvalue >=2 with positive probability. The convergence theorem removes the need to assume parameter convergence for this question. The exact supercritical example rules out a universal endpoint bound but lies in a null set; the critical value 2 needs separate attention from ordinary unstable endpoints above 2. Do not infer edge residence from either endpoint event.

Artifacts: PROOF.md, LOG.md, verify_rectangular.py, verification.json, the failed verification.stdout.txt/verification.stderr.txt, and audited/final stdout and stderr files. All writes remained inside this folder; earlier folders were read only.

Task: “Open problem T226: The edge of stability: why full-batch gradient descent hovers at sharpness 2/eta” — received 15 November 2026, approximately 05:09 Asia/Tbilisi.
