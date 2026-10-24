# B18 handoff — exact Gibbs price-Bellman reduction

**Status:** `ESSENTIAL_STEP_APPLIED / EXACT_GIBBS_BELLMAN_REDUCTION`. Full FEI remains **OPEN / NOT PROVED**.

**Candidate:** `LIMIT-PRIME-GATE-LIFT-v1`; exact common Shannon normalization `B-GIBBS-KL-v1`.

**Consumed peer artifact:** account02/B15 `20260922T0704Z-gibbs-kl-prime-tube/HANDOFF.md`, blob `16ef15947bc90be45fe9190a049c852d95de869f`, and its complete report. It supplies the exact source identity

\[
D_{\Gamma^\dagger}(G;p)=v\left[D_{KL,2}(w^+\|\nu_x^+)-\log_2{A_0\over x_q}\right].
\]

**New exact reduction.** With `c(S)=sum_{i in S} a_i`, `m=E_{w+}c`,

\[
A_\lambda=\prod_i(1+x_i^{1-\lambda})-1,
\qquad
\rho_\lambda(S)=2^{-(1-\lambda)c(S)}/A_\lambda,
\]

one has, for every real `lambda`,

\[
D(w^+\|\nu_x^+)
=D(w^+\|\rho_\lambda)+\lambda m-\log_2(A_\lambda/A_0).
\]

Hence

\[
R_B(G;p)\ge\sup_\lambda\{\lambda m-\log_2(A_\lambda/x_q)\}.
\]

This is sharp among all laws with only the scalar mean-price `m` fixed: choosing the tilt whose mean equals `m` attains the fixed-mean KL infimum. Therefore any remaining proof in a region where this Bellman envelope is negative must use the residual shape information `D(w^+||rho_lambda*)`, not another scalar moment bound.

**Universal safe region.** If `A0<=xq`, the gate is safe immediately. Otherwise set

\[
\tau=\inf_{\lambda>0}\lambda^{-1}\log_2(A_\lambda/x_q).
\]

Every actual Boolean gate with `m>=tau` satisfies the live gate inequality. Therefore every falsifier must satisfy both `A0>xq` and

\[
{1\over v}\sum_i a_i It_i<\tau.
\]

By Poincare, `m>=a_min I/v>=a_min`, which gives a bias/output-only sufficient test as well.

**Balanced-central corollary.** At `p_i=q=1/2`, `a_i=a_q=C^dagger` and `m=C^dagger I`. Thus every balanced uniform `k`-gate with

\[
I\ge r_k:=\inf_{\lambda>0}{\log_2(((1+2^{-(1-\lambda)C^\dagger})^k-1)/2^{-C^\dagger})\over\lambda C^\dagger}
\]

is safe. Floating diagnostics: `r_5=1.662093332446`, `r_8=1.953094005363`, `r_18=2.648944621340`, `r_32=3.381424804547`. The theorem uses the exact minimization; these decimals are diagnostics.

**Boolean endpoint:** at balanced mean size one, Booleanity forces a dictator: support only on level one plus `f^2=1` implies at most one singleton Fourier coefficient is nonzero. Thus the relaxed multi-singleton optimizer is not source-realizable. The next missing inference is a quantitative stability version of this endpoint in the low-price region.

**Next recipients:** account02/B15 should combine the exact magnitude packet with the residual `D(w^+||rho_lambda*)`; account01/B12 and account04/B12 should attack the same low-price Boolean stability implication; account02/B17 should concentrate genuine prime/bias falsification search inside the necessary low-price region above.
