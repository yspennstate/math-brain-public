# Source-bound handoff — fleet04/B16 refined signed joint credit

**Status:** `ESSENTIAL_STEP_APPLIED`; full FEI open.

**Consumes:** fleet02/B13 `20260922T045511Z-joint-credit-critical-core`; fleet02/B16 actual parent weights at creation revision `7f9fdcbbba89432301a5e32985ae2bd3e7b1ac5e`; fleet03/B18 signed flag curvature at creation revision `4843e50690013fd18b85dd8763b53bdc75da79e8`.

**New theorem:** at an unbiased pivot of a balanced Boolean parent, if `a=E f0=-E f1`, `A=a^2`, and `delta=Pr[f0!=f1]`, then the forced empty Fourier atom has mass `A`, overlap magnitude one and negative relative sign. Keeping it exact before Jensen gives

\[
H(B\mid S)+I(S;J)
\ge h_2(\delta)-1+2A+(1-A)\Psi\left(\frac{|1-2\delta+A|}{1-A}\right).
\]

Inserted in the exact restriction cocycle, this yields the two-parameter necessary inequality `Q_Gamma(a,delta)<0` at every essential coordinate of a minimum-arity balanced central counterexample.

For the live cap `C*=6.5218512`, the zero-first-level slice is positive for every `delta>=7/40`, analytically. Therefore any such critical core must obey

\[
\widehat f(\{j\})=0 \Longrightarrow \operatorname{Inf}_j(f)<7/40.
\]

This improves the predecessor's `<1/4` threshold. The numerical root `0.17403113037837303` is context only.

**Next recipients:** fleet02/B13 and the gate-integration workers. Combine `Q_Gamma(a,delta)` with source-valid lower information on `Gamma_*((1-|a|)/2)` to exclude nonzero first-level mass, or construct a Boolean pair saturating the remaining region. Independently, fleet02/B16's newer coherent biased n=18 prime-gate direction remains the strongest finite falsification lead.
