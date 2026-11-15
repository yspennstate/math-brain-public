# Open problem T305: Metropolized HMC under operator-norm Hessian regularity

Statement: Let pi be proportional to exp(-V) on R^d, with mI<=Hessian V<=LI, bounded L/m, and ||Hessian V(x)-Hessian V(y)||op<=M||x-y||, with m,L,M independent of d. From an M0-warm start, determine whether leapfrog Metropolized HMC reaches total-variation error epsilon in O-tilde(d^{1/4} polylog(M0/epsilon)) gradient evaluations uniformly over this class, or construct a counterexample requiring a larger dimension exponent. No dimension-independent Frobenius-norm Hessian bound is assumed.

Caveat: The warm-start factor is explicit. A stronger-regularity theorem does not settle the stated uniform class.

Source: Chen-Gatmiry-Jiang, When does Metropolized Hamiltonian Monte Carlo provably outperform Metropolis-adjusted Langevin algorithm? (arXiv:2304.04724).

Where it stands (checked by us, Nov 2026): The source gives the desired dimension exponent under its stronger Frobenius-Lipschitz regularity and warm-start assumptions. Operator-norm Lipschitzness alone can cost a factor sqrt(d) on conversion and is a distinct class.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T305 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T305 (read it,
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
VERDICT: PARTIAL finite-step Gaussian remainder bounds and an unavoidable entropy drift

The earlier result holds on independent rechecking. The new result resolves
its proposed remainder question for all Gaussian targets and identifies a
drift that persists at the critical step size. It does not settle T305.

Write
\[
 R_{h,T}=\mathcal H(\Psi_h^nZ)-\mathcal H(Z)
 -h^2[A(Z)-A(\Phi_TZ)],\qquad T=nh,
\]
with the earlier report's coefficient
\(A=p^T\nabla^2V p/12-|\nabla V|^2/24\).

[PROOF.md](PROOF.md) first proves, throughout the stated class,
\[
 E_\rho R_{h,T}
 =D_{\rm KL}((\Psi_h^n)_\#\rho\,\|\,\rho).
\]
The right side concerns the proposal before the accept/reject decision.
Stationary average rejection equals the total variation distance between
this proposal law and \(\rho\), and is at most the square root of half
this entropy. A direct warm-start transfer of that average bound would
cost \(M_0\), so it does not supply the requested logarithmic dependence.

For a Gaussian target with precision eigenvalues \(\lambda_i\in[m,L]\),
let
\[
 \phi_i=2n\arcsin(h\sqrt{\lambda_i}/2),\quad
 \mu=\sum_i\frac{h^4\lambda_i^2\sin^2\phi_i}
                         {32(1-h^2\lambda_i/4)},\quad
 b=\frac{h^4L^2(1+T\sqrt L)}8.
\]
If \(h\sqrt L\le1\), the proof gives the exact mean \(E_\rho R=\mu\),
\(0\le\mu\le dh^4L^2/24\), and
\[
 \Pr\{|R-\mu|>2b\sqrt{2ds}+2bs\}\le\delta,
 \qquad s=\log(2M_0/\delta),
\]
from every \(M_0\)-warm position start with fresh Gaussian momentum.
The centering is the stationary mean; no stationarity of the numerical
endpoint is assumed.

For standard Gaussian targets, fixed \(T\notin\pi\mathbb Z\), and
\(dh^4\to\ell^4>0\),
\[
 R_{h,T}\longrightarrow\frac{\ell^4\sin^2T}{32}>0
 \quad\text{in stationary }L^2.
\]
The convergence also holds in probability for warm starts satisfying
\(\log M_0=o(d)\). Thus an uncentered \(o(1)\) remainder at the critical
step size is impossible, even with constant Hessian. The previous report
did not claim such a bound; its leading-coefficient theorem remains valid.
This example is not a counterexample to the desired mixing exponent.

The proof uses exact two-dimensional matrix blocks. Independent checks use
rational matrix powers and direct kick/drift iteration, Gaussian covariance
formulas, and asymmetric non-Gaussian quadrature for the earlier variance
identity. Reproduce with:

```sh
nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 audit.py > audit_output.txt 2>&1
```

The audit passed in 0.024 seconds, with one Python thread and about 19.2 MB
maximum RSS. Inherited nice was 20; this explains the wrapper's warning.
The variance-identity residual was at most \(6.939\times10^{-18}\), and
the finite-step pointwise residual at most \(4.947\times10^{-15}\).
The critical-scale calculation gives mean limit
\(\sin^2(1)/32=0.0221272943210491\); at \(n=256\), the mean is
0.0221273967965 and the standard deviation is \(6.07601\times10^{-7}\).
Large displayed dimensions are scalar multiplicities, not allocated arrays.
These floating-point checks are audits, not certified numerical proofs.
See [LOG.md](LOG.md), [audit_output.txt](audit_output.txt), and
[audit_data.json](audit_data.json) for commands and results.

Attempts to break the result included the stability-range boundary,
several precisions and integration times, and resonance at \(T=\pi\).
At resonance the positive limit vanishes, as required. Two independent
drift calculations agree: the invariant quadratic form and the relative
entropy of the powered Gaussian map. Exact rational algebra also checks
the exponential energy identity and the energy-error variance.

What remains uncertain is the finite-step behavior for nonquadratic
potentials under operator-norm Hessian regularity alone. The quadratic
calculation cannot control third-derivative effects. No uniform entropy
bound, nonquadratic centered-remainder bound, or mixing theorem is proved.
The next worker should try to bound the proposal entropy by \(Cdh^4\)
under the original assumptions, or construct a family violating that
bound. For logarithmic warm dependence, a separate tail/local argument is
still needed. A direct remainder approach should allow an \(O(dh^4)\)
drift and control fluctuations around it.

The literature check finished within five minutes and found no settlement.
Papers actually opened:

- Yuansi Chen, Khashayar Gatmiry, and Minhui Jiang,
  *When does Metropolized Hamiltonian Monte Carlo provably outperform
  Metropolis-adjusted Langevin algorithm?*,
  [arXiv:2304.04724v3](https://arxiv.org/html/2304.04724v3).
  Section 2.4 and Table 1 retain Frobenius Hessian regularity.
- P. Dobson, J.M. Sanz-Serna, and K.C. Zygalakis,
  *Optimal scaling of MCMC algorithms: the Hamiltonian approach*,
  [arXiv:2607.00586v2](https://arxiv.org/abs/2607.00586).
  The abstract describes scaling results for product targets; it does not
  establish the uniform class in T305.
- Fan Chen, Sinho Chewi, Jianfeng Lu, and Matthew S Zhang,
  *Smoothed Picard Hamiltonian Monte Carlo*,
  [arXiv:2609.06906v2](https://arxiv.org/abs/2609.06906).
  Its abstract uses smoothing, Picard iteration, and higher-order
  discretization, followed by a different high-accuracy sampler.

This is a bounded literature check, with no claim of priority for the
Gaussian formulas or entropy identities. All files written are in this
session's folder; the earlier folder was read only.

Task: “take the NEXT checkable step on this problem, building on that work.”
— 15 November 2026, approximately 03:45 Asia/Tbilisi.
