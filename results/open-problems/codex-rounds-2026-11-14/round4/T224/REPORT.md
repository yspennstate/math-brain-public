VERDICT: PARTIAL improved curvature-dependent uniform weak rates by concentration on iid trajectories

The round 3 result holds. An independent velocity subtraction recovers its energy inequality and constants; rerunning its audit reproduces its results. The new step replaces its Markov estimate on the time-integrated iid output fluctuation by concentration in trajectory Hilbert space. This improves the conditional width exponents under the same additional stability assumption.

In the same bounded-feature Euclidean population-flow setting, write \(A,B,M\) for uniform bounds on \(\phi,D\phi,D^2\phi\), \(L_t=\|f_t-g\|^2\), and

\[
 h(t)=\sup_{w,|u|=1}[-\langle f_t-g,D^2\phi(w)[u,u]\rangle]_+,
 \quad H(T)=\int_0^T h(t)dt,\quad S_T=\int_0^T e^{2H(s)}ds.
\]

PROOF.md establishes, for deterministic \(T\ge1\) and \(m\ge2M^2A^2 T S_T\),

\[
\begin{split}
 \sup_{t\ge0}\mathbb E\|f_t^m-f_t\|^2
 \le {}&\frac{8A^2+16A^2B^2T e^{2H(T)}}m+6L_T\\
 &+16A^2\exp\!\left(-\frac{m}{4M^2A^2 T S_T}\right).
\end{split}
\]

If \(AM=0\), omit the exponential term and the width condition. This replaces the round 3 term of order \(T^2e^{2H(T)}/m\) by a term of order \(Te^{2H(T)}/m\) plus an exponentially small exceptional-event contribution.

Suppose additionally

\[
 L_t\le C(1+t)^{-c},\qquad H(T)\le h_0+\kappa\log(1+T).
\]

For \(0<c\le1\), the new rate is

\[
 O\!\left(\left(\frac{\log(em)}m\right)^{c/(2+2\kappa)}\right).
\]

For \(c>1\), the new rate is

\[
 O\!\left(m^{-c/(c+1+2\kappa)}\right).
\]

These improve the preceding exponent \(c/(c+2+2\kappa)\). For example, \(c=1,\kappa=0\) improves from \(m^{-1/3}\) to \(\sqrt{\log(em)/m}\); \(c=3/2,\kappa=0\) improves from \(m^{-3/7}\) to \(m^{-3/5}\). Explicit constants and width thresholds are in Corollaries 2 and 3 of PROOF.md. For each fixed \(c,\kappa\), the prefactors are polynomial in \(d\) when \(A,B,M,C\) are polynomial in \(d\), \(h_0=O(\log d)\), and \(\kappa\) is dimension independent. The log-free constant for \(c>1\) deteriorates as \(c\downarrow1\). No exponent or logarithmic factor is claimed sharp.

The key observation is that \(\sqrt{J_T}=\|m^{-1}\sum_i X_i-\mathbb EX_i\|_{L^2([0,T];\mathcal H)}\), where the entire mean-field paths \(X_i(t)=\phi(v_i(t))\) are iid and have norm at most \(A\sqrt T\). Changing one initial neuron changes this scalar norm by at most \(2A\sqrt T/m\). A self-contained bounded-difference proof controls the bad event without assuming temporal independence. The coupling cancellation and loss monotonicity then give the output estimate above. The result concerns the requested output norm with the supremum outside expectation, not a Wasserstein sampling rate.

Verification commands, run from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114r3/briefs/T224/audit_cancellation.py
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_concentration.py
```

Both passed. The new audit checks 48 exact trajectory variances, 488 exact finite-law concentration tails, 179 simplified tails, 3,888 coordinate replacements, 300 exact constant identities, 21 exact exponent cases, 500 logarithmic-rate prefactors, and 263 log-free prefactors. Four complete ordered-sample enumerations independently match the multinomial laws. A separate exact binomial tail agrees with Pascal recursion. The path laws include perfect temporal dependence and the zero case. These are concentration and algebra checks, not simulations of infinite-time neural convergence. Each script ran in under one second, actual nice 20, peak RSS below 17 MB. Full results: cancellation_results.json and concentration_results.json; derivations, commands and outputs: LOG.md.

The literature check, completed within five minutes, found no later settlement. The current source by Margalit Glasgow and Joan Bruna remains [arXiv:2605.22010v3](https://arxiv.org/html/2605.22010v3), dated 11 November 2026. Remark 6 already handles \(c=2\); Section 6 leaves \(c<2\) open. No full-settlement SOLVED_ELSEWHERE.md was created. No literature-priority claim is made for the new bounds.

What failed or remains uncertain: concentration does not remove the exponential dependence on \(H(T)\). The slow-loss envelope alone still allows \(H(T)=O(T^{1-c/2})\) for \(c<2\), and this argument does not yield a polynomial width rate in that case. There is no admissible counterexample, no necessary stability condition, and no sharp exponent for the original problem. The scope remains bounded features, fixed output coefficients, Euclidean parameters, exact population flow and iid initialization; unbounded activations, sphere constraints, trained output coefficients, finite training data and discretization are not covered.

Next worker: address deterministic output stability rather than further improving iid tails. One concrete target is to retain the negative output square in (14)--(16) of PROOF.md and prove a coercivity estimate controlling the Taylor remainder through output discrepancy along the coupled trajectories. Such a bound would have to hold beyond a parameter-discrepancy stopping threshold and avoid the factor \(e^{2H(T)}\); otherwise this concentration improvement still leaves the decay-only obstruction intact. Alternatively, an admissible example must amplify sampling error in the output, not merely separate parameter trajectories.

Task: “take the NEXT checkable step on this problem, building on that work” — 2026-11-15 05:06 Asia/Tbilisi (first captured shell clock).
