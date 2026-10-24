# PROB10-05 idea checkpoint — corrected even-Hermite tail acceleration

Status on entry: **PARTIAL / source target OPEN**. Frozen source model is centered standard fBM at `H=1/4`, `I(t)=int_0^t B_{1/4}(s) ds`, continuous event `sup_{0<=t<=T} I(t)<=1`. The newest valid self-certified repository candidate read before this checkpoint is

`theta_{2,1/4} > 15664/91031 = 0.17207324977205568...`,

from `runs/prob10_2026-09-20/PROB10-05/2026-09-20T1420Z__corrected_parity_split_172073249.md`. The source-valid upper endpoint remains `1/4`; the exact exponent is UNKNOWN and independent validation is outstanding. The withdrawn pre-normalization endpoints remain historical only.

## Three materially different nonexhausted attacks considered

1. **Corrected even-Hermite tail acceleration (primary this run).** Keep the corrected `r=22/25` comparator, the exact odd-sector arcsine identity, and the degree-56 direct moment certificate. The current trace proof computes only the first `K=1000` even Hermite modes and then bounds every unresolved mode by the single largest remaining weight factor `q^(2K+2)`. Because the exact recurrence for `P_j,D_j` is O(K), extend the certified even block substantially and/or split the residual into certified blocks before using Parseval on the final tail. This attacks the corrected four-cycle trace cap without touching the repaired normalization. A lower trace cap should increase the spectral-gap allowance in the Kato--Temple step.

2. **Direct optimization of the Kato--Temple threshold.** For a fixed corrected trace cap `C`, the limiting admissible `x` solves approximately `(x-mu_hi)(mu_lo-(C-x^4)^(1/4))=eps2_hi`, and the largest exponent then approaches `log(x)/(4 log r)`. This is mathematically different from improving the trace itself, but with the current cap it can only recover a very small amount because the previous run already chose `x,beta` close to the feasibility boundary. Use it as a secondary synthesis after any genuine trace improvement.

3. **Reverse continuous-time interpolation via a negative-margin grid.** The deterministic derivative estimate and Borell--TIS bound from the previous report reduce an upper-exponent improvement to proving that a negative-margin sampled survival event costs only subexponentially relative to zero-margin survival as the mesh shrinks. A Cameron--Martin shift or Gaussian boundary-sensitivity estimate could address this, but no such uniform long-horizon margin theorem is currently available. Do not infer a continuous persistence bound from discrete sampling alone.

## Critical claim to falsify before promotion

For attack 1, the only permissible new trace improvement is one obtained with the corrected normalized cyclic variance `G0=(1+r^4)/(1-r^4)` and the resulting corrected `rho_adj,rho_opp,q,A`. The recurrence must preserve outward bounds for `pi`, square roots, `atan`, and `asin`; any finite-mode sum is theorem evidence only together with a certified nonnegative remainder and a final Parseval tail bound. No Monte Carlo or floating-point-only trace estimate may move the source metric.

If a materially tighter corrected trace cap is certified, recompute the spectral separation and Kato--Temple/log comparison from scratch with exact rational signs. Otherwise record the obstruction and do not relabel an unchanged checker as progress.
