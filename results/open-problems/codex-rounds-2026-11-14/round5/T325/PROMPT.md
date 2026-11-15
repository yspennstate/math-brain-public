# Open problem T325: Do trained transformers learn in-context regression by gradient descent?

Statement: Pretrain a transformer on prompts (x_1, y_1, ..., x_N, y_N, x_query) with x_i ~ N(0, I_d), y_i = <w, x_i> and w ~ N(0, I_d). Zhang, Frei and Bartlett prove that gradient flow on a one-layer linear self-attention model from a suitable initialization converges to a predictor implementing one step of preconditioned gradient descent. Prove that gradient-based training of a multi-layer softmax transformer (or of a linear transformer with L ≥ 2 layers from a random initialization) converges to a predictor whose in-context risk approaches that of the Bayes-optimal ridge predictor as N → ∞, and identify the algorithm it implements.

Caveat: Constructions show transformers can implement gradient descent and ridge regression in context (von Oswald et al.; Akyürek et al.); stationary points of multi-layer linear models are characterized (Ahn et al.). Convergence of training beyond one layer is the open part.

Source: R. Zhang, S. Frei and P. L. Bartlett, Trained Transformers Learn Linear Models In-Context, arXiv:2306.09927 (2023); J. von Oswald et al., Transformers learn in-context by gradient descent, arXiv:2212.07677 (2022); E. Akyürek et al., What learning algorithm is in-context learning? Investigations with linear models, arXiv:2211.15661 (2022); K. Ahn, X. Cheng, H. Daneshmand and S. Sra, Transformers learn to implement preconditioned gradient descent for in-context learning, arXiv:2306.00297 (2023); S. Garg, D. Tsipras, P. Liang and G. Valiant, What Can Transformers Learn In-Context? A Case Study of Simple Function Classes, arXiv:2208.01066 (2022)

Where it stands (checked by us, Nov 2026): Open beyond one layer / linear attention as far as the writer knows.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T325 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T325 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T325 (read it,
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
VERDICT: PROVED global population-gradient-flow convergence at every finite depth for untied scalar attention step sizes with all other blocks fixed

The round-3 two-layer theorem holds. The extension here covers every
finite L>=1 in the same d=1 architecture. At every finite prompt length
N>=1, gradient flow from any pairwise distinct scalar initialization
converges to the global minimizer with that coordinate ordering.
Independent non-atomic random step-size initialization therefore succeeds
almost surely. Only the L direct scalar Q entries are trained.

The limiting predictor implements L empirical least-squares gradient
steps from zero. Set alpha=N/2. Its residual polynomial is

    r_*(s)=sum_(k=0)^L (-1)^k binom(L,k) alpha^k s^k/(alpha+1)_k.

The learned step sizes are the reciprocals of its L distinct positive
roots, in the initial ordering. The exact prediction risk is

    L!/(alpha+1)_L = 2^L L! / product_(j=1)^L (N+2j).

Thus the excess over the noiseless scalar Bayes risk zero is asymptotic
to 2^L L!/N^L for each fixed L. At depth three it is exactly
48/[(N+2)(N+4)(N+6)]. Depth two recovers the earlier 8/[(N+2)(N+4)].

The new convergence ingredient resolves the earlier report's
repeated-root obstruction. Each pair difference satisfies

    (a_i-a_j)' = (a_i-a_j) 2 E[S^2(1-a_i S)(1-a_j S)R(S)^2],

where S=sum x_i^2/N and R contains the remaining residual factors.
The multiplier is uniformly positive near collisions on a bounded
sublevel set. Every initially nonzero gap therefore stays bounded away
from zero. The coefficient Jacobian remains uniformly invertible along
the trajectory, and strict convexity in polynomial coefficients gives
exponential loss-gap convergence. PROOF.md supplies all steps and a
second quantitative derivation of the collision neighborhood. No general
analytic-flow or stable-manifold theorem is needed.

Every nonglobal stationary point is a strict saddle with a repeated
pair. Repeated initial steps remain equal and cannot attain the global
risk; pairwise distinctness is the exact success condition. Negative
initial values and a single zero value are allowed. No uniform training
time in N, L, or the initial gaps is proved.

Validation commands:

```
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114r3/briefs/T325/audit_scalar.py
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_depth.py
```

Both passed. The new standard-library script independently computes
Gaussian moments, solves the coefficient normal equations, verifies the
exact risk, and counts positive simple roots by rational Sturm sequences
for N=1,2,3,5,10,100,1000 and L=1,...,8. It also verifies 105 pair
identities and 315 collision cases, plus Jacobians, loss gaps, and token
updates. Final arithmetic run: 0.710 seconds, peak RSS 15.48 MiB,
inherited nice=20. The nice wrapper prints a priority-setting warning;
the script explicitly checks that the inherited priority is low enough.
The earlier script's optional address-space cap remains unavailable;
no hard RAM cap is claimed. All arithmetic is small and exact.

The initial five-minute literature check found no full solution changing
the task. Sources actually opened and the architectural differences are
recorded in LOG.md. The architecture used here is from Khashayar Gatmiry,
Nikunj Saunshi, Sashank J. Reddi, Stefanie Jegelka, Sanjiv Kumar,
*Can Looped Transformers Learn to Implement Multi-step Gradient Descent
for In-context Learning?*, [arXiv:2410.08292v1](https://arxiv.org/html/2410.08292v1),
Section 3 and Appendix A.1. No exhaustive novelty claim is made.

What failed or remains uncertain: no proof failed within the stated
scalar model; the brief literature check cannot establish priority.
The full T325 problem remains open here. Nothing establishes convergence
with all transformer blocks randomly initialized and trained, d>1,
softmax attention, separately factorized keys/queries, or discrete or
stochastic training. All writes stayed in this folder; no git, external
mutations, subagents, or model training were used.

Next worker: keep the scalar architecture and analyze gradient flow when
each direct step is replaced by a_i=k_i q_i with both factors trained.
Then a_i'=-h_i partial_i F, h_i=k_i^2+q_i^2, and k_i^2-q_i^2 is
conserved. The pair-difference equation above no longer factors, so the
uniform gap argument does not directly apply. Establishing global
convergence for independent continuous factor initialization would close
another concrete restriction. Alternatively, derive a discrete-step
training theorem with an explicit step-size condition.

Task: “take the NEXT checkable step on this problem, building on that work.” — 15 November 2026, approximately 06:31 Asia/Tbilisi.
