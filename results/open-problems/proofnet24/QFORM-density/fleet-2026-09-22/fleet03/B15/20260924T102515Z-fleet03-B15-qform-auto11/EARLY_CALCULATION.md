# Early calculation — Gaussian-mixture closure barrier

Run `20260924T102515Z-fleet03-B15-qform-auto11`.

Let `Y=M+sqrt(T)G`, where `G~N(0,1)` is independent of `(M,T)`, `T>0`, and assume `E[T^{-1/2}]<=kappa`. For every interval `J` of length `L`, conditionally on `(M,T)=(m,t)`, symmetry and unimodality of the Gaussian give

`P(Y in J | M=m,T=t) <= 2 Phi(L/(2 sqrt(t)))-1`.

Put `u=t^{-1/2}` and `g_L(u)=2 Phi(Lu/2)-1`. Then

`g_L'(u)=L phi(Lu/2)` and `g_L''(u)=-(L^3/4)u phi(Lu/2)<=0`,

so `g_L` is increasing and concave. Hence Jensen yields the sharp concentration bound

`sup_{|J|=L} P(Y in J) <= 2 Phi(kappa L/2)-1`.

For the Gaussian-mixture QFORM class, `kappa=sqrt(2 pi)`, so at `L=1` the bound is

`q_* = 2 Phi(sqrt(pi/2))-1 = 0.789908594556...`.

Therefore every such marginal stays at total-variation distance at least

`1-q_* = 0.210091405444...`

from `Uniform[0,1]`, using the event `[0,1]`. More strongly, the class is not even weakly dense in cap-one laws: any weak limit retains the interval concentration bound on open intervals by Portmanteau, whereas `Uniform[0,1]` assigns mass one to every open interval `(-eps,1+eps)` while the right side remains strictly below one for finite `eps`.

For products of `n` such marginals, the cube event gives

`d_TV(Unif[0,1]^n, product_i nu_i) >= 1-q_*^n`,

which tends to one exponentially.

This is not a QFORM counterexample. It proves that the completed Gaussian-mixture QFORM theorem cannot be extended to arbitrary cap-one laws by weak- or total-variation density of its present input class; a different rough-law mechanism is necessary.
