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

Later work: a round 5 worker built on the latest of these. Its folder is ~/codex_op_1114r5/briefs/T245 (read it, never
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
VERDICT: PARTIAL first-order learning-rate correction to the endpoint flow and full NTK in the structured deep-linear model

The round-4 result holds on independent recheck. The new result is a complete first-order expansion in the learning rate eta, with uniform O(eta^2) remainders at training nodes on every fixed continuous-time interval. It corrects both the end-to-end matrix/bias trajectory and the full test NTK. It retains one symmetric matrix field in depth, driven by the known balanced endpoint flow; the nonlinear depth profile need not be evolved.

This remains the fully trainable linear network with scalar-identity initialization. The original independent-Gaussian/ReLU joint-limit training-law problem is not solved. A literature check under five minutes found no whole-problem solution; sources and their scopes are recorded in [LOG.md](LOG.md).

For endpoint P, set H=P^TP/S^2, A_0(z)=H^z, v=P^Te and K=log H. The previously established flow is

\[
\dot P=-tP\int_0^1 A_0^{-1}v g^TA_0\,dz,\qquad \dot b=-h.
\]

The additional field J satisfies

\[
\dot J=R^TJ+JR-tN,\qquad J(0,z)=0,
\]
\[
R(z)=-t\int_0^z A_0(a)^{-1}v g^TA_0(a)\,da,
\]
\[
N(z)=(g^TA_0g)vv^T-(v^TA_0^{-1}v)A_0gg^TA_0.
\]

At each training time its excess prefix-Gram correction W solves

\[
W_{zz}=W_zK+KW_z-KWK+tJ,\qquad W(0)=W(1)=0.
\]

[PROOF.md](PROOF.md) gives an explicit scalar Green function in an eigenbasis of K, including repeated eigenvalues. It derives J from the accumulated discrete commutator defect and proves that the following expansion holds at the actual discrete endpoint:

\[
M_k^\eta=M_{\rm bal}(P_k^\eta)+\eta\mathcal M(P(\tau_k),J(\tau_k))+O_T(\eta^2),
\quad
B_k^\eta=B_{\rm bal}(P_k^\eta)+\eta\mathcal B(P(\tau_k),J(\tau_k))+O_T(\eta^2),
\]
\[
\mathcal M=t\int_0^1
\{(v^TA_0^{-1}v)W-(v^TA_0^{-1}WA_0^{-1}v)A_0\}\,dz,
\quad
\mathcal B=-t\int_0^1v^TA_0^{-1}WA_0^{-1}v\,dz.
\]

The full kernel is

\[
K(x,x')=1+x_E^TMx'_E+B\langle x_\perp,x'_\perp\rangle.
\]

Equation (12) of PROOF.md gives the finite-dimensional linear sensitivity equation for the endpoint's first correction. Its forcing includes both imbalance and the ordered double-insertion Hessian, in addition to Euler's usual time-discretization term.

The order of limits is size first, then eta to zero on a fixed training interval. All randomness remains the initial S=exp(mu t+sigma sqrt(t) Z). Bounds are conditional on S>0; uniform moment bounds over lognormal tails are not asserted. No novelty claim is made for balanced deep-linear flow or for the general Euler error expansion.

Verification command:

    OMP_NUM_THREADS=1 nice -n 15 python3 verify.py > verification_output.txt 2>&1

[verify.py](verify.py) uses only the standard library and imports earlier arithmetic/spectral helpers and the raw nonlinear profile solver read-only, with bytecode disabled. [verification_output.txt](verification_output.txt) and [verification_data.json](verification_data.json) contain the complete output.

- Fresh exact rational calculations reproduce the earlier M1, B1, C2_22, eta^6/32 profile commutator, eta^3/48+eta^5/640 kernel commutator and discrete defect.
- The new small-time kernel corrections are -eta*tau/24 in M22 and -eta*tau/48 in B for the mandatory two-example benchmark. Direct one-step Gram/power expansions independently give the same constants.
- Manufactured boundary solutions, including repeated eigenvalues, show fourth-order depth convergence. At grid 64 their maximum error is below 2.42e-8.
- Ordered Hessian insertion agrees with central differences of the original profile within 2.00e-8. Reversing the multiplication order gives error .003636.
- The new endpoint-driven memory field agrees with direct integration of the original profile and its accumulated commutator within 2.84e-9. Dropping its coordinate-transport terms gives error .006113.
- Scalar commuting orbits, zero residuals, zero inputs, and bias-only Euler correction passed. Scalar orbits have no imbalance correction even though their endpoint time-discretization correction can be nonzero.

At training time .4, the maximum entry error across P,b,M,B was:

| (t,S) | eta=.04 | eta=.02 | eta=.01 | eta=.005 |
| --- | ---: | ---: | ---: | ---: |
| (.5,.7) | 2.296e-5 | 5.657e-6 | 1.404e-6 | 3.499e-7 |
| (1,1), two-example benchmark | 1.047e-4 | 2.571e-5 | 6.369e-6 | 1.586e-6 |
| (2,1.3) | 9.809e-4 | 2.391e-4 | 5.896e-5 | 1.457e-5 |

Halving eta reduces corrected errors by approximately four; the uncorrected flow errors decrease by approximately two. Refining the correction equations changes their coefficients by at most 2.18e-9. Refining the raw profile grid changes the tested observables by at most 7.65e-8. These are diagnostics, not rigorous numerical error bounds. The final run took 10.26 seconds, used 28.6 MB peak RSS, one thread, and inherited nice priority 20. The macOS nice warning and the direct priority check are recorded.

What failed: omission of memory transport and reversal of ordered insertions fail the independent checks. No mathematical assertion in the final test suite failed. No finite-matrix replacement for J was obtained, and these formulas do not prove that one is impossible. Fixed positive eta, nonaligned random initialization, ReLU gates, simultaneous size/step limits and unbounded training times remain unresolved.

Next worker: determine whether the functionals of J in equations (10)–(12) close under differentiation using finitely many additional matrices, at least for the two-example benchmark. The changing endpoint spectrum changes their depth weights, so a moment truncation needs a proof. The scalar reduction, the two exact commutators, the constants -1/24 and -1/48, and the observed O(eta^2) full-state error provide mandatory checks for any proposed compression.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, 08:49 Asia/Tbilisi (session receipt).
