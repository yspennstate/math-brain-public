VERDICT: PARTIAL closed joint-limit NTK dynamics for a structured deep linear initialization

The original Gaussian ReLU problem is not solved. A special case is proved in [PROOF.md](PROOF.md): a width-$n$, depth-$L$ linear network, with every matrix entry and an output bias trainable, trained on one example. The initialization is $W_l=s_lI$, where the independent scalar gains have $\log s_l=\mu/n+\sigma Z_l/\sqrt n$. This is a deliberately aligned initialization, not independent Gaussian matrix entries. The fixed readout is $e_1$.

For $L/n\to t>0$, the full kernel at every fixed finite collection of GD steps converges in law. All randomness in its limit comes from

\[
 S=\exp(\mu t+\sigma\sqrt t\,Z).
\]

With $b_0=c_0=0$, the closed discrete training recursion is

\[
 P_k=Se^{tc_k},\quad r_k=b_k+P_k-y,\qquad
 b_{k+1}=b_k-\eta r_k,\quad
 c_{k+1}=c_k-\eta P_kr_k.
\]

The limiting kernel on arbitrary fixed test directions is

\[
 K^k(x,x')=1+tP_k^2x_1x'_1+
 S^2\left(\int_0^t e^{2c_ku}\,du\right)
 \langle x_\perp,x'_\perp\rangle.
\]

In particular its first change at the training example is exactly

\[
 K^1(e_1,e_1)-K^0(e_1,e_1)
 =tS^2\{\exp[-2\eta tS(S-y)]-1\}.
\]

This is nonzero almost surely when $t,\eta,\sigma>0$. In the small-step limiting flow, the absolute initial derivative has a $t^2$ prefactor; relative to the initial matrix-weight contribution its derivative has a $t$ prefactor. Along the training direction the initial change is twice the change in an orthogonal direction. Thus even in this simple model, “rate set by $t$” needs a specified normalization.

The small-step limiting flow has the conserved quantity $1/P+tb=1/S$. It exists globally, fits the sample, and its final kernel is explicit:

\[
 P_*=\frac{2}{\sqrt{(1/S-ty)^2+4t}+(1/S-ty)},\qquad
 A_*=tP_*^2,\qquad B_*=tS^2H(2\log(P_*/S)),
\]

where $H(z)=(e^z-1)/z$ and $H(0)=1$. This last statement takes the size limit first, then the small-step limit, then infinite continuous training time.

## Verification

Exact command:

~~~sh
OMP_NUM_THREADS=1 nice -n 15 python3 verify.py
~~~

The script uses only the standard library. Full output is in [verification_output.txt](verification_output.txt), numerical data in [verification_data.json](verification_data.json), and the commands and successive outputs in [LOG.md](LOG.md).

Checks include dense matrix GD, 180 numerical parameter derivatives including off-diagonal entries, independent finite-size differentiation of the kernel, products of scalar moments versus the limiting normal law, finite-size convergence for $t=0.5,1,2$, and 27 ODE integrations with different gains and targets. At $n=8192$, the maximum coefficient errors over seven states were below $7.17\times10^{-4}$ in the tested arrays. These arrays condition the initial product to a fixed value; separate iid sampling checks the initialization law.

The dense kernel discrepancy was $4.44\times10^{-16}$ and the numerical derivative discrepancy was $4.74\times10^{-12}$. The independent finite-size kernel-rate calculation agreed within $2.30\times10^{-10}$. ODE endpoints agreed with the explicit root within $8.50\times10^{-9}$. Resource measurements are saved with the data; each run took under one second and used under 25 MB peak RSS. The inherited priority was 20; macOS refused the additional relative nice adjustment, and the script independently checked that its priority remained at least 15.

## What failed or remains uncertain

A dense off-diagonal perturbation destroys the exact scalar orbit: the check produces a nonzero off-diagonal gradient. The proof therefore provides no perturbative stability or universality result for iid matrices. It does not address ReLU gate changes, multiple training examples, or an increasing number of discrete GD steps. The lognormal initial randomness is built into the gain distribution. The fixed-depth frozen kernel in this model is the input-independent bias kernel, so comparison with the ordinary Gaussian NTK limit is limited.

No claim of literature novelty is made for scalar deep-linear dynamics. The checkable piece is the stated joint-limit theorem, including the full perpendicular kernel and the limiting trained kernel. Numerical checks support the algebra but do not replace the proof.

The bounded literature search found partial advances, recorded with their scope in [SOLVED_ELSEWHERE.md](SOLVED_ELSEWHERE.md). No whole-problem solution was found; that search is not a proof that none exists.

## Next step

Test whether a two-dimensional invariant block admits a comparable matrix-valued closure, and quantify how small a nonaligned perturbation must be for the present law to survive at $L\asymp n$. A result for iid Gaussian matrices would require a separate argument controlling those perturbations and forward–backward dependence.

Task: “push this problem forward by one checkable piece” — 14 November 2026, 21:24 Asia/Tbilisi (session receipt).
