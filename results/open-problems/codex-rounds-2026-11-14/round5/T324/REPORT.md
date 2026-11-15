VERDICT: PARTIAL stopped concentration for independently noisy groups and preservation of the deterministic merging prefactor in probability

The round-4 deterministic result holds. Its derivative and internal mean-drift cancellation were re-derived, its verification script was rerun with all writes redirected here, and a separate explicit-midpoint solver agreed with its six-token RK4 times within 1.550e-7 relative error. No complete later resolution was found in the bounded literature check; opened references and limitations are in LITERATURE.md. Publication priority is not established.

The new result treats normalized identity-matrix attention on the circle, including self-attention, with independent angular noise \(\sqrt{2\nu_\beta}\,dW_i\) on every token. There are two labelled groups of fixed sizes \(n_A,n_B\), all token weights equal. Set \(p=n_A/(n_A+n_B)\), \(q=1-p\). Fix an initial lifted arithmetic center gap \(x\) and a first-entrance target \(\delta\), with \(0<\delta<x<\pi\).

If both initial group diameters are at most \(w_\beta\leq1/(4\sqrt\beta)\), and

\[
 \liminf_{\beta\to\infty}\frac{-\log\nu_\beta}{\beta}>1-\cos x,
\]

then

\[
 \frac{\log\tau_\delta}{\beta}\longrightarrow1-\cos x
 \quad\text{in probability}.
\]

If also \(\beta^2w_\beta^3\to0\), the full deterministic prefactor survives:

\[
 \tau_\delta\sim
 \frac{\exp\{\beta(1-\cos x)\}}
      {(p/q+q/p)\beta\sin^2x}
 \quad\text{in probability}.
\]

This includes initial widths \(O(1/\beta)\). The strict noise condition includes every \(\nu_\beta=\exp(-r\beta)\) with \(r>1-\cos x\), as well as faster decay.

The proof supplies the concentration estimate missing from the earlier report. In a separated narrow tube satisfying an explicit contraction condition, let \(\sigma\) be first exit through either gap boundary or a width boundary. For a horizon \(T\), initial width \(w_0\), and \(w_0+Ku\) below the tube width,

\[
 \mathbb P\{\exists t\leq T\wedge\sigma:
 W(t)>w_0e^{-t/2}+Ku\}
 \leq4M\lceil T\rceil e^{-u^2/(8\nu)},
\]

where \(K=2+2/(1-e^{-1/2})\) and
\(M=\binom{n_A}{2}+\binom{n_B}{2}\). Section 9 gives a separate exponential-Lyapunov proof of width-exit suppression. The exact center-gap martingale has quadratic variation

\[
 2\nu(1/n_A+1/n_B)t.
\]

The center gap is not assumed to be a scalar Markov process. Its error relative to the two-atom drift is bounded explicitly; subtracting its Brownian path then gives a deterministic scalar hitting-time sandwich. This is the new step beyond the noiseless concentration theorem.

Commands, run from this folder:

~~~sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 recheck.py > recheck_output.txt 2>&1
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify.py > verification_output.txt 2>&1
~~~

Both final runs exited 0. The independent predecessor recheck took 4.709 seconds and 17.563 MiB RSS; the final new verification took 2.254 seconds and 15.313 MiB RSS. It uses only the standard library and checks center variance in two ways, 81 drift-residual configurations, adapted pair-contraction equations, the independent exponential-Lyapunov calculation, exponent choices near both angular endpoints, finite-time noisy concentration, and coupled time-step full merging simulations. All runs used one thread and effective nice 20. The launcher warning reflects an inherited priority already lower than requested. Data and output are saved here; no predecessor file was changed.

What failed: the independent midpoint recheck initially used steps .02 and .01 and failed its own refinement tolerance. Refining to .01 and .005 preserved the original tolerances and passed. No mathematical counterexample was found. The proof specifically avoids replacing a group by a noisy atom: this would give the wrong noise variance and omit the internal drift residual.

Limits and uncertainties: no generic cluster count, formation theorem, successive mergers, general matrices, growing-token-count limit, or noise-dominated merging law is proved. The conclusion is convergence in probability, not a mean entrance-time asymptotic. Exceptional trajectories are not controlled sufficiently to pass to expectations. The width and strict noise conditions are sufficient; necessity is not proved. Initial centers are non-antipodal; the stopping event uses lifted arithmetic means and a positive gap threshold. Numerical paths are consistency checks, not proofs or probability certificates; in particular a discrete Brownian grid cannot certify the continuous maximum bound.

Next worker: address the critical or noise-dominated regime using the stopped concentration and current-separation residual estimates (7)–(9). A reduction must control accumulated residuals and center excursions near the antipodal gap before applying a scalar hitting-time formula. Alternatively, to upgrade the present weak-noise result to a mean-time prefactor, first obtain a tail estimate outside the good tube event; convergence in probability alone is insufficient.

Task: T324, “take the NEXT checkable step on this problem, building on that work.” First recorded session clock: 15 November 2026, 09:09 +04 (Asia/Tbilisi); the prompt's own timestamp was not supplied.
