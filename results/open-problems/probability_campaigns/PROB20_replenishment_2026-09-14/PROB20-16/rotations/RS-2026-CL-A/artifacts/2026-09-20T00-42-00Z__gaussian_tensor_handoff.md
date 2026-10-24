# Cross-role mathematical handoff — Renyi-smoothed Gaussian/tensor bridge

Source ownership remains RS-2026-CL-A. This is a supporting lemma for registered probability roles P08/P09; it does not transfer or duplicate their source claims.

Let `R_n=gamma_n` be standard Gaussian measure with Hermite chaos and OU semigroup `T_t|H_k=e^{-tk}`. For `P_n,Q_n << gamma_n`, set `Delta_n=dP_n/dgamma_n-dQ_n/dgamma_n` and

`Lambda_n(d)=sup_{deg f<=d, f!=0} E_{Q_n}f^2 / E_{gamma_n}f^2`.

The inherited bridge is

`||Pi_{1:d} Delta_n||_2^2 <= Lambda_n(d) Adv_{Q_n}^{<=d}(P_n,Q_n)^2`.

The new tail improvement is: for a target OU time `t>0`, it is **not** necessary to assume `log ||Delta_n||_2^2=o(D_n)`. It is enough that for some `s in (0,t)`,

`log_+ ||T_s Delta_n||_2^2 = o(D_n)`

(or more quantitatively has exponent `<2(t-s)`). The tail above `D_n` is then bounded by

`e^{-2(t-s)D_n} ||T_s Delta_n||_2^2`.

By Gaussian hypercontractivity,

`||T_s f||_2 <= ||f||_{1+e^{-2s}}`.

Hence a structural sufficient condition is

`D_r(P_n||gamma_n)+D_r(Q_n||gamma_n)=o(D_n)`, `r=1+e^{-2s}<2`.

For every fixed positive target noise time it is enough to have this for every fixed `r<2`, together with subexponential source-to-Gaussian low-degree inflation and fixed-degree source-signal escape.

Why this may help P08/P09: rare determinant/small-singular-value events can make global Gaussian `L2` likelihood complexity enormous while all fixed `L^r`, `r<2`, remain controlled. P08's dependence-aware phase-retrieval tail estimates and P09's current Gaussian tensor/chaining bounds may therefore be used to estimate Renyi orders below 2 instead of forcing an `L2` bound.

Strictness example on the Boolean analogue: a spike mixture with weight `epsilon_N=2^{-N/2}e^{sqrt N}` has `log ||Delta||_2^2~2sqrt N` (far larger than a polylog source degree) but `||Delta||_r->0` for every fixed `r<2`, and every fixed positive noise time kills it exponentially. This is the mechanism the Gaussian/tensor version should look for.

Classical hypercontractivity/Renyi machinery is prior art. The source-directed bridge is novelty-unverified.