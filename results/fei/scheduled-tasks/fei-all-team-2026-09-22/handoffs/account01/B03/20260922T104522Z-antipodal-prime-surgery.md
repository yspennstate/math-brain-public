# account01/B03 FEI handoff — antipodal prime surgery

**Run:** `20260922T104522Z-antipodal-prime-surgery`  
**Status:** `ESSENTIAL_STEP_APPLIED`; full FEI remains OPEN.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

Full source: `yspennstate/math-open-problems`, branch `master`, run root `proofnet24/P03-fei/fleet-2026-09-22/account01/B03/20260922T104522Z-antipodal-prime-surgery/`; report creation history begins at commit `abbc45c211d1adc4de74477e3114e7b18522e748`, with checker added at `35354ce3e8ccffb52ff9764725ef73481a9eb494` and claims at `3d1806dbbda551eb094f659c7c8d0f0902f1e922`.

For every `n>=3`, define `f_n` by taking dictator `x_1` and flipping only the two antipodal rows `(+1)^n` and `(-1)^n`. In `{0,1}` ANF,

`F_n=z_1 xor prod_i(1 xor z_i) xor prod_i z_i`.

The report proves this family is all-essential and composition-prime: every split with both sides at least two has GF(2) ANF flattening rank 3; singleton-complement splits have three distinct truth-table row types, so no one-bit inner summary can represent them.

Put `alpha=2^(2-n)`. Uniformly,

`hat f({1})=1-alpha`, `hat f(S)=-alpha` for odd `|S|` other than `{1}`, and zero for even `|S|`. Hence `I=1+alpha(n-2)` and `H/(I-1)->4`.

More usefully, on the project one-core bias line `p_1=t`, `p_2=...=p_n=1/2`, let `c=1-2t`, `C=Gamma(1/2)` and `q=t+alpha*c/2`. Applying the exact gate normalization from account02/B17 (`f5946fb64d336ed7369de279159643944efc47af`) gives

`D_Gamma,n(t) = (1-alpha) Gamma(t) + (n-1) alpha C - Gamma(t+alpha(1-2t)/2) + 2(1-alpha)^2 log2(1-alpha) - (4alpha-2alpha^2)(n-2)`.

The Poincare denominator is

`M_n(t)=alpha/4 * [n-2-(1-2t)^2(1-alpha)]`.

For fixed interior `t` and differentiable `Gamma`, `c_f=-D/M -> -4(C-4)`. Thus fixed interior bias is asymptotically slack for every `C>4`; for the current source-reported center near `6.55844528307`, the limit is about `-10.23378113`. The first unpaid implication is the **boundary layer** `t=t_n`, especially `t=Theta(alpha)` and `Theta(alpha n)`, using the exact current candidate potential bytes. A negative value would be a genuine growing-arity prime falsifier of that candidate; a uniform nonnegative bound would eliminate this entire near-dictator prime class.

`CHECKER.py` reports PASS: 459 nontrivial block checks for `3<=n<=8`, 992 exact rational one-core spectral-entry checks for `3<=n<=7` at four rational biases, and balanced current-center regression through `n=30`.

The designated current partner account02/B03 had no completed run artifact at the pre-write snapshot, so no partner result was fabricated. The named complete OTHER-account result actually used is account02/B17's strong-prime normalization above.
