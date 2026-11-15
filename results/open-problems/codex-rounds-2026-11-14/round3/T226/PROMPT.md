# Open problem T226: The edge of stability: why full-batch gradient descent hovers at sharpness 2/eta

Statement: For full-batch gradient descent with fixed step eta on a neural-network training loss, the top Hessian eigenvalue first rises to about 2/eta and then hovers there while the loss keeps decreasing non-monotonically (Cohen et al.). Fix a model (e.g. a smooth two-layer network of moderate width on Gaussian data with square loss, or a deep linear network), an initialization law and a range of eta. Prove that with probability bounded below over the initialization GD enters the edge-of-stability regime, stays there, and converges to a global minimizer whose sharpness is 2/eta + o(1) as eta → 0 (or show the event has small probability). Local theorems near a minimizing manifold (Gan 2026, Theorem 4.4, assumes a C4 loss and a nondegeneracy condition) leave open whether random initialization reaches their basin.

Caveat: Results that assume a specific cubic structure of the loss, or study two-parameter toy models, are partial. Divergence above the classical 2/L threshold is NOT what happens: the point is convergence without the descent-lemma condition.

Source: J. M. Cohen, S. Kaur, Y. Li, J. Z. Kolter and A. Talwalkar, Gradient Descent on Neural Networks Typically Occurs at the Edge of Stability, arXiv:2103.00065 (2021)

Where it stands (checked by us, Nov 2026): Partial: self-stabilization under assumptions on third derivatives (Damian, Nichani and Lee 2209.15594); Arora, Li and Panigrahi 2205.09745 for normalized losses; Ahn et al. 2204.01050; analyses of two-layer and scalar toy models. Open for genuine networks (not re-checked against 2025–26).

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T226 (read it,
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
VERDICT: PARTIAL an exponentially small edge-entry probability for a fixed-width, multi-input two-layer linear network

For the fully trainable network f(a,W;x)=a^T W x and loss L=(1/2)||W^T a-b||^2, PROOF.md proves

\[
 \Pr\{\exists t\geq0:\lambda_{\max}(\nabla^2L_t)\geq1/\eta\}
 \leq\min\{1,\;2^{m(d+1)/2}e^{-1/(256\sigma^2\eta)}\}.
\]

Here all parameter entries are independent N(0,sigma^2), m,d,b,sigma are fixed, and eta<=1/(128||b||) when b is nonzero. For b=0 this extra restriction is absent. The loss is both an explicit finite full-batch empirical loss and the exact population loss for isotropic Gaussian inputs. One concrete choice is hidden width 16 and input dimension 8, with 144 trainable parameters. This is not a two-parameter restriction.

The probability that the iterates converge to a global minimizer with sharpness 2/eta+o(1) has the same bound. More precisely, this holds for every deterministic endpoint tolerance epsilon(eta)->0. It even holds for a relative window |eta lambda_max-2|<=1/2. The proof does not require deciding convergence on the exceptional set.

The deterministic statement is: if R=||a_0||^2+||W_0||_F^2+2||b|| and eta R<=1/32, then all iterates have squared parameter norm at most 6R, Hessian operator norm at most 10R, and loss decrease at least (eta/2)||gradient||^2 per step. The proof controls the discrete drift of WW^T-aa^T and closes a noncircular descent bootstrap. It does not assume a globally bounded Hessian. The model has global minima of arbitrarily large sharpness.

The same probability estimate excludes any variance scaling with eta sigma_eta^2->0, for fixed width and input dimension. No novelty claim relative to all existing small-step convergence results is made.

## Literature check

The targeted web check took less than ten minutes. No opened result closes the random-entry gap in the question; this is a bounded search, not an exhaustive assertion of openness. No SOLVED_ELSEWHERE.md was created.

- Eric Gan, *A Bifurcation Theory Framework for Gradient Descent on the Edge of Stability*, [arXiv:2606.15551](https://arxiv.org/html/2606.15551v1), Theorem 4.4: a local neighborhood guarantee at a fixed critical step, already covered by the prompt. It does not establish entry from the initialization law here.
- Eric Gan, *Product-Stability: Provable Convergence for Gradient Descent on the Edge of Stability*, [arXiv:2604.02653v3](https://arxiv.org/html/2604.02653v3), Theorems 4.3 and 5.2: convergence and endpoint sharpness for l(xy), under prescribed near-minimum product and near-edge initial sharpness conditions.
- Lachlan Ewen MacDonald, Hancheng Min, Leandro Palma, Salma Tarmoun, Ziqing Xu, René Vidal, *Convergence Rates for Gradient Descent on the Edge of Stability for Overparametrised Least Squares*, [NeurIPS 2025 paper](https://proceedings.nips.cc/paper_files/paper/2025/file/d9af4d6ac714626b652da5616ca71f99-Paper-Conference.pdf), Theorem 5.2: critical-step convergence rates under local hypotheses. This does not give a random-initialization entry theorem.
- Rotem Mulayoff, Sebastian U. Stich, *On the Stability of Nonlinear Dynamics in GD and SGD: Beyond Quadratic Potentials*, [arXiv:2602.14789](https://arxiv.org/html/2602.14789v1), Theorem 3.1: a local bifurcation criterion with a positive definite Hessian. It does not address the requested basin probability.
- Elon Litman, *The Origin of Edge of Stability*, [arXiv:2604.20446](https://arxiv.org/html/2604.20446v1), Theorems 4.1–4.3: trajectory identities and conditional concentration for directional curvature averages. The infinite-energy assumption E_K->infinity used for asymptotic concentration is not proved for the model and initialization here. These statements do not settle convergence to an endpoint with top Hessian eigenvalue 2/eta+o(1).

## Commands and checks

Final verification command, run in this folder:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify.py > verification.audited.stdout.txt 2> verification.audited.stderr.txt
```

Exit 0, elapsed 0.78 seconds, effective nice 20, peak RSS 16,318,464 bytes, one thread, no external numerical libraries. The CPU cap was 15 seconds and the wall alarm 30 seconds. The script checks its execution priority before numerical work.

Results: 24 exact rational cases verified the matrix imbalance, total-norm recurrence, residual recurrence, gradient-energy identity, quartic loss change and Hessian quadratic form. An independent central difference of the explicit gradient checked all Hessian entries with maximum error 4.08e-11. All rational constants were recomputed exactly. The full-Hessian eigenpair at a constructed global minimizer agreed exactly with sharpness 86/9. On 32 trajectories with 500 steps each, every tested norm, curvature bound and descent inequality held; the minimum observed normalized descent above the rounding cutoff was 0.98227, against a proved lower bound 0.5. Finite probes do not replace the induction proof.

Data: verification.json. Exact console output: verification.audited.stdout.txt. Earlier failed-run outputs and all commands are retained in LOG.md.

## Failures and remaining uncertainty

Two initial verification attempts stopped before numerical checks because this macOS sandbox rejected an address-space resource limit. A later data-limit request was also rejected, recorded by the script. The successful run's measured memory use was about 16 MB. The nice utility emitted a permission warning, but the independently measured effective nice value was 20, which passed the low-priority guard. No mathematical check failed.

This result concerns a linear activation and an isotropic loss. It gives an obstruction in the small-eta, fixed-initialization-scale formulation, using descent on a large-probability invariant region. It does not explain nonmonotone edge training, prove positive-probability entry, address general nonlinear networks, or classify the exceptional large initializations. It also does not claim convergence for every safe initialization: zero initialization with b nonzero is a stationary nonglobal point. No convergence claim is needed to exclude the sharp endpoint event.

## Next step

Study the unresolved boundary scale sigma_eta^2 of order 1/eta in this same multi-input model. With a=eta^(-1/2)A and W=eta^(-1/2)U, the exact updates are

\[
 A^+=A-U(U^TA-\eta b),\qquad
 U^+=U-A(U^TA-\eta b)^T.
\]

The rescaled initialization then has a fixed Gaussian law. Classifying the zero-target limit of this matrix/vector map is a concrete next problem; no entry or convergence classification is supplied here.

Task: “Open problem T226: The edge of stability: why full-batch gradient descent hovers at sharpness 2/eta” — received 14 November 2026, approximately 22:07 Asia/Tbilisi.
