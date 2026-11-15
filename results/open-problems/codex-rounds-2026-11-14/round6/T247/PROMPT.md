# Open problem T247: The singular-value spectrum of deep network Jacobians in the joint depth-width limit (dynamical isometry)

Statement: Pennington, Schoenholz and Ganguli compute, via free probability, the limiting singular-value distribution of the input-output Jacobian J = Π D_l W_l of a depth-L network with orthogonal or Gaussian weights, assuming asymptotic freeness of the diagonal derivative matrices D_l and the weights W_l, and find 'dynamical isometry' at criticality for orthogonal weights and sigmoid-like activations. Prove the formula and the isometry claim when depth and width tend to infinity jointly (L = L(n) → ∞), not only at fixed depth.

Caveat: At fixed depth asymptotic freeness of the layer Jacobians has been proved (Pastur and Slavin; Collins and Hayase, to verify). The joint limit needs control of errors accumulated over L layers.

Source: J. Pennington, S. S. Schoenholz and S. Ganguli, Resurrecting the sigmoid in deep learning through dynamical isometry: theory and practice, arXiv:1711.04735 (2017)

Where it stands (checked by us, Nov 2026): Fixed-depth freeness proved; joint limit open as far as the writer knows.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T247 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T247 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T247 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 5 worker built on the latest of these. Its folder is ~/codex_op_1114r5/briefs/T247 (read it, never
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
VERDICT: PARTIAL unnormalized joint-limit empirical isometry for orthogonal tanh networks with small Gaussian biases at simultaneous forward/backward critical initialization

The earlier result holds. The new result adds independent Gaussian biases and uses the usual simultaneous Gaussian forward- and backward-critical parameters. The full joint-limit spectral distribution remains unresolved.

For \(G\sim N(0,1)\), write

\[
\mu_G(a)=\mathbb E\operatorname{sech}^4(\sqrt aG),\qquad
A_G(a)=\mathbb E\tanh^2(\sqrt aG).
\]

Take independent real Haar \(O_l\), independent \(\xi_l\sim N(0,I_n)\), and

\[
h_l=\tanh(g_nO_lh_{l-1}+\sqrt{b_n}\xi_l),\qquad
g_n^2=\mu_G(a_n)^{-1},\qquad
b_n=a_n-g_n^2A_G(a_n),\qquad
\|h_0\|^2/n=A_G(a_n).
\]

The input may have any deterministic direction. We prove \(0<b_n\leq14a_n^3\) eventually. If \(n,L(n)\to\infty\) and

\[
L(n)a_n^2+\frac{L(n)a_n}{n}\longrightarrow0,
\]

the empirical squared-singular-value measure of the ordinary, unnormalized input-output Jacobian converges to \(\delta_1\) in \(W_2\), in probability. The parameters obey exactly \(g_n^2\mu_G(a_n)=1\) and \(g_n^2A_G(a_n)+b_n=a_n\); exact finite-width stationarity is not assumed. The condition allows \(La_n\to\infty\).

[PROOF.md](PROOF.md) contains a self-contained proof and the explicit finite probability bound (38). It also covers any deterministic \(0\leq b\leq14a^3\), \(|\log(g^2)-2a|\leq15a^2\), and initial relative signal-radius error at most \(14a^2\).

The new one-layer estimate averages the biases while retaining the dependence between gates and weights. Its first-order directional corrections are the previous \(-4q(n\alpha-T)/(n+2)\) and \(-8q(n\gamma-Q)/(n+2)\). Bias enters the uniformly controlled \(O((q+b)^2)\) remainders. A stopped relative-radius argument and two martingales show that the forward radii stay near \(a\) and the accumulated auxiliary scalar tends to one. This supplies both missing biased-network steps identified by round 4.

Verification commands, all exit 0:

~~~sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 15 python3 recheck_independent.py > recheck_independent_output.txt 2>&1
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 15 python3 recheck_dependent.py > recheck_dependent_output.txt 2>&1
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 15 python3 verify_critical.py > recheck_critical_output.txt 2>&1
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 15 python3 verify_bias.py > verification_output.txt 2>&1
~~~

The earlier checks reproduced without discrepancy. New checks include exact formal bias coefficients and independent 70-digit Gaussian quadrature, 42 global bias-averaged gate checks, 25 direct Haar/Gaussian trace quadratures, 48 exact correlated eighth-moment bounds, 36 forward drift/scalar quadratures, 100000 stopped crossing checks, and actual biased-network products. Zero bias, pure-noise gates, aligned/transverse rank-one matrices and extreme permitted gains were checked. The direct Haar quadrature refinement difference was at most \(1.24\cdot10^{-14}\).

At \(n=64,L=180,a=1/16384\), the actual critical biased network had mean unnormalized distortion \(3.18116915\cdot10^{-5}\), versus the stopped normalized-distortion bound \(0.0563979862\); mean scalar was \(0.999992801\). The final verification used 92.1 MiB peak RSS, 3.71 seconds, one thread and niceness 20. Data, seeds and outputs are in [results.json](results.json), [verification_output.txt](verification_output.txt), and [LOG.md](LOG.md).

No mathematical or numerical check failed. A direct extension of the old log-radius proof would need control near rare Gaussian cancellations; the relative-increment argument avoids that issue. At \(n=64,L=10000,a=.0002\), a forward stress test gives mean scalar \(0.910487743\), consistent with the retained \(La/n\to0\) requirement. Necessity of that condition is not proved. Expected unnormalized distortion convergence, fixed positive stationary variance, spectral edges, operator isometry and the full density are not established.

The five-minute literature check found no verified resolution; opened sources and scope are in [LITERATURE.md](LITERATURE.md). No claim of novelty against the entire literature is made. All intentional writes stayed in this folder; earlier folders were read without modification.

Next worker: determine whether the \(La/n\) restriction can be removed for empirical isometry by tracking the forward-direction energy more accurately. The present proof still bounds that energy by completing a square and can accumulate a \(q/n\) error even if only a negligible spectral fraction carries the effect. Alternatively, a nontrivial spectral limit at \(La^2\to\tau>0\) requires second-order trace and scalar drift terms beyond the remainder bounds proved here.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, approximately 08:50 Asia/Tbilisi.
