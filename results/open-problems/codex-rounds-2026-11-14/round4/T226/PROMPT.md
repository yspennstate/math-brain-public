# Open problem T226: The edge of stability: why full-batch gradient descent hovers at sharpness 2/eta

Statement: For full-batch gradient descent with fixed step eta on a neural-network training loss, the top Hessian eigenvalue first rises to about 2/eta and then hovers there while the loss keeps decreasing non-monotonically (Cohen et al.). Fix a model (e.g. a smooth two-layer network of moderate width on Gaussian data with square loss, or a deep linear network), an initialization law and a range of eta. Prove that with probability bounded below over the initialization GD enters the edge-of-stability regime, stays there, and converges to a global minimizer whose sharpness is 2/eta + o(1) as eta → 0 (or show the event has small probability). Local theorems near a minimizing manifold (Gan 2026, Theorem 4.4, assumes a C4 loss and a nondegeneracy condition) leave open whether random initialization reaches their basin.

Caveat: Results that assume a specific cubic structure of the loss, or study two-parameter toy models, are partial. Divergence above the classical 2/L threshold is NOT what happens: the point is convergence without the descent-lemma condition.

Source: J. M. Cohen, S. Kaur, Y. Li, J. Z. Kolter and A. Talwalkar, Gradient Descent on Neural Networks Typically Occurs at the Edge of Stability, arXiv:2103.00065 (2021)

Where it stands (checked by us, Nov 2026): Partial: self-stabilization under assumptions on third derivatives (Damian, Nichani and Lee 2209.15594); Arora, Li and Panigrahi 2205.09745 for normalized losses; Ahn et al. 2204.01050; analyses of two-layer and scalar toy models. Open for genuine networks (not re-checked against 2025–26).

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T226 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T226 (read it,
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
VERDICT: PARTIAL a convergent subcritical basin and a small asymptotic edge-endpoint probability at initialization variance of order 1/eta

The earlier exponentially small bound for fixed-variance initialization holds on independent audit. The new result addresses the boundary variance scale named in its next step. It proves convergence on an open set for the same fully trainable multi-input two-layer linear network, and persists from the zero-target map to every fixed target b as eta tends to zero.

For

\[
L_b(a,W)=\tfrac12\|W^Ta-b\|^2,\qquad
A=\sqrt\eta\,a,\quad U=\sqrt\eta\,W,
\]

suppose m>=d+1, [A_0 U_0] has full column rank, and

\[
s_0=\|A_0\|^2+\|U_0\|_{\rm op}^2<2.
\]

For b=0 the exact scaled GD map converges geometrically after a finite transient to a global minimizer, with scaled endpoint sharpness at most s_0. For any fixed nonzero b, the same initial point converges to a global minimizer for every sufficiently small eta, and

\[
\eta\lambda_{\max}(\nabla^2L_b(a_\infty,W_\infty))
\leq (2+s_0)/2<2.
\]

The threshold on eta depends on the initial point. The proof is in PROOF.md, including the finite-time continuity and local contraction argument for nonzero targets.

## Gaussian consequence

Initialize all m(d+1) original parameters independently as N(0,tau^2/eta), with tau fixed. For any deterministic relative endpoint tolerance w(eta)->0, let E_eta mean parameter convergence to a global minimizer whose sharpness satisfies |eta lambda_max-2|<=w(eta). Then

\[
\limsup_{\eta\downarrow0}\Pr(E_\eta)
\leq\Pr\{\|A_0\|^2+\|U_0\|_{\rm op}^2\geq2\}.
\]

For m=16,d=8, with 144 trainable parameters and tau^2=1/288, a chi-square Chernoff bound gives

\[
\boxed{\limsup_{\eta\downarrow0}\Pr(E_\eta)
\leq e^{-72(3-\log4)}
=3.47305198969\ldots\times10^{-51}.}
\]

This covers the requested absolute o(1) endpoint window, and any event that additionally requires an edge phase. It is an asymptotic probability bound, not a bound at a specified finite eta. The initialization family depends on eta through the stated variance. The earlier report's estimate is vacuous at this variance: its prefactor and exponent give 2^72 exp(-288/256)>1.

## What is new

The earlier proof bounded trajectories under eta(S_0+2||b||)<=1/32 and did not prove convergence. Its probability bound vanishes when eta sigma_eta^2->0 and leaves the boundary law untreated. Here the condition is spectral rather than a small Frobenius norm condition. The proof uses the exact identities

\[
q^+=q-2\|v\|^2+v^TCv,\quad
C^+=C+(q-2)vv^T,\quad
\det G^+=\det G(1-\|v\|^2)^2,
\]

where q=||A||^2, C=U^TU, v=U^TA and G=[A U]^T[A U]. Monotonicity of q and C makes the residual squares summable. The determinant stays uniformly positive, supplying a spectral gap and eventual geometric contraction. All columns participate; no balanced or aligned invariant slice is assumed.

The basin also contains full-rank initial points with Hessian sharpness above 2/eta. An explicit rational example has s_0=33/20 and a Hessian Rayleigh quotient 121/50>2 in scaled coordinates. Thus this basin is not justified by a requirement that initial Hessian sharpness be below 2/eta. It still does not explain a sustained edge regime or nonmonotone loss.

## Verification

Read all earlier requested files without editing them. Re-derived the earlier balance bootstrap, noncircular descent induction, constants and Gaussian exponent; no error found.

Run in this folder:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify_extension.py > verification.audited.stdout.txt 2> verification.audited.stderr.txt
```

Exit 0; wall time 0.4271 seconds; effective nice 20; peak RSS 17,645,568 bytes; standard library only, one thread. The program has a 60-second CPU cap and 90-second wall alarm.

Forty exact rational cases verify the earlier imbalance and norm identities and the new Gram determinant, q, C and residual recurrences. Fifty-two finite trajectories, including width 16 and dimension 8, pass the tested endpoint inequalities; the largest iteration count is 262 and the largest final residual norm is 9.97e-13. The determinant identity's maximum relative numerical error is 3.54e-15. Independent differentiation of the gradient checks the endpoint Hessian with maximum error 9.17e-13. Exact loss evaluations along a line independently recover the supercritical Rayleigh quotient. Two separate evaluations of the Chernoff constant agree to rounding precision. Finite trajectories support implementation checks; the infinite-time claims follow from the proof.

Artifacts: PROOF.md; LOG.md; verify_extension.py; verification.json; verification.audited.stdout.txt and verification.audited.stderr.txt. The first successful run's stdout/stderr are also retained.

## Literature check

A bounded initial web search found no solution of the requested Gaussian entry problem. No SOLVED_ELSEWHERE.md was warranted. This is not an exhaustive claim of openness. References actually opened:

- Jaerin Lee and Kyoung Mu Lee, *A Journey to the Edge of Stability*, [arXiv:2609.32290](https://arxiv.org/abs/2609.32290): optimizer and learning-rate sweeps; its abstract describes empirical regimes rather than a Gaussian network-basin theorem.
- Peter Zaika and Zakhar Shumaylov, *Non-Euclidean Gradient Descent Has Many Edges of Stability*, [arXiv:2610.15223](https://arxiv.org/abs/2610.15223): quadratic objectives and non-Euclidean dynamics, not the neural-network endpoint problem here.
- Hee-Sung Kim and Sungyoon Lee, *Gradient Descent with Large Step Size Restores Symmetry in Deep Linear Networks with Multi-Pathway*, [arXiv:2606.05219](https://arxiv.org/html/2606.05219v1), [ICML 2026 proceedings](https://proceedings.mlr.press/v306/kim26aj.html): target-aligned and depth-balanced structure. Appendix E.7 states that global entry into the local self-stabilized neighborhood is not proved.
- Elon Litman, *The Origin of Edge of Stability*, [arXiv:2604.20446](https://arxiv.org/html/2604.20446v1): reopened the paper already audited in the earlier report; no new random-basin result was identified in this check.

## Failures and uncertainty

No mathematical check failed. The nice utility printed a permission warning, while the process independently reported effective nice 20 and passed its priority guard. Initial broad file discovery was too large and was replaced by targeted reads; two optional startup-memory paths did not exist. All writes stayed inside this folder, including the log; no shared mesh, checklist or brain writes were made under the task's restriction.

The complementary initializations s_0>=2 remain unclassified. Full column rank is used essentially in the convergence proof. At s_0=2 there are stationary full-rank zero-target minima with sharpness exactly 2, so the strict inequality cannot simply be removed. For nonzero b, the perturbation argument supplies no explicit initialization-uniform eta threshold. No claim is made for nonlinear networks or about novelty against all matrix-factorization convergence literature.

## Next checkable step

Analyze the larger zero-target region q_0<2 and ||C_0||<2 with q_0+||C_0||>=2. Equations for q and C still give monotonicity and summable residual squares there. The proof above loses its uniform bound ||v_t||^2<1 and its subcritical limiting output spectrum. A concrete next lemma would either prove parameter convergence and identify which limiting eigenvalues can reach 2, or construct a full-rank counterexample. Do not infer an edge phase from a limiting eigenvalue alone. Alternatively, extract an explicit target-size threshold on a compact subset of the proved basin to replace the limsup probability bound by a finite-eta statement.

Task: “Open problem T226: The edge of stability: why full-batch gradient descent hovers at sharpness 2/eta” — received 15 November 2026, approximately 03:34 Asia/Tbilisi.
