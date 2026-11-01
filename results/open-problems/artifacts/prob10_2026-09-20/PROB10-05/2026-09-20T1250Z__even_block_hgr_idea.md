# PROB10-05 idea checkpoint — even-block Hermite contraction before code

Runtime request: GPT-6 / maximum. Authenticated scheduler model/effort telemetry is unavailable here, so runtime model/effort is **UNVERIFIED**. This checkpoint does not modify any schedule, email, Drive, public posting, or peer claim.

## Frozen target and incoming frontier

Keep `H=1/4`, centered standard fBM, `I_H(t)=\int_0^t B_H(s)ds`, and the **continuous** event `sup_{0<=t<=T} I_H(t)<=1`. Molchan arXiv:2509.10265v11, revised 4 July 2026, is the current source: Statement 1.2 gives existence/equality of the self-similar and Lamperti persistence exponents in the relevant parameter region, while the same paper says the one-sided `alpha=2, H!=1/2` exact values remain unresolved and reports the old `theta_{2,H}=H(1-H)` proposal as refuted. That refutation is source prior art, not ours.

Canonical ownership remains `operations/claims/MOLCHAN-2025-THETA2H.md` (`HARD7-05`). PROB10-05 is a continuation of that claim, not a duplicate. The newest consumed PROB10 report is

`runs/prob10_2026-09-20/PROB10-05/2026-09-20T1214Z__mesh22_25_softened_172052.md`,

which gives the self-certified candidate

`theta_{2,1/4} > 43013/250000 = 0.172052`

with source-valid upper endpoint `1/4`, hence gap `0.077948`.

## Three materially different nonexhausted attacks

1. **Even-block Hermite contraction of the four-cycle — main route.** The preceding softened `r=22/25` checker bounds the fourth sign moment by a generic HGR inequality with factor `kappa`. The opposite-pair sign observable is actually an **even** function of the shared Gaussian mode, so its centered Hermite expansion starts at degree 2. Replacing `kappa` by `kappa^2` and computing the exact conditional second moment should sharply reduce the fourth-trace cap without changing the comparator or degree-56 witness.

2. **Continuous reverse interpolation — upper-endpoint route.** Use a negative grid margin plus a modulus-of-continuity event to imply continuous survival. The deterministic implication is easy, but a lower bound with only `exp(o(S))` loss on Lamperti horizon `S` still requires controlling the joint law under long survival. This remains genuinely different and nonexhausted; it is not used to claim an upper-endpoint improvement here.

3. **Comparator redesign / multimode subtraction — future lower-endpoint route.** Change `r,c,s` again or certify non-Perron modes for the present operator. This is a distinct operator-level attack and should be preferred once the new trace/Hermite envelope is saturated.

## Main new mathematical observation

For the softened Gaussian four-cycle `(V_0,V_1,V_2,V_3)` in the incoming report, write

`rho = Corr(V_0,V_2)=rho_opp`, `a = Corr(V_0,V_1)=rho_adj`,

and make the orthogonal change of variables

`A=(V_0+V_2)/sqrt(2)`, `B=(V_0-V_2)/sqrt(2)`,
`C=(V_1+V_3)/sqrt(2)`, `D=(V_1-V_3)/sqrt(2)`.

Then `(A,C)` is a correlated Gaussian pair, `(B,D)` are independent, and the two blocks are independent. After normalization,

`Corr(A,C)=kappa = 2 rho_adj/(1+rho_opp)`.

Let

`F_0 = sgn(V_0)sgn(V_2)`, `F_1 = sgn(V_1)sgn(V_3)`.

Conditioning on the normalized common modes `X=A/sqrt(1+rho)` and `Y=C/sqrt(1+rho)` gives

`E[F_0|X=x]=h(x)=4 Phi(c|x|)-3`,

with `c=sqrt((1+rho)/(1-rho))`; similarly for `F_1`. Hence

`m4 := E[F_0F_1] = E[h(X)h(Y)]`, `Corr(X,Y)=kappa`.

Crucially, `h` is even. In the normalized Hermite expansion

`h = m + sum_{n>=1} a_{2n} H_{2n}`,

only even degrees occur, where `m=E h=(2/pi)asin(rho)=q_opp`. Therefore

`m4 = m^2 + sum_{n>=1} a_{2n}^2 kappa^(2n)`

and, because `0<kappa<1`,

`m4 <= m^2 + kappa^2 (E[h(X)^2]-m^2)`.

The remaining second moment is also exact. Since

`h(x)=4 Phi(c|x|)-3`, put `p(x)=Phi(c|x|)`. For independent standard `Z_1,Z_2`,

`E p(X)^2 = P(Z_1<=c|X|, Z_2<=c|X|)`.

By symmetry this is twice a centered trivariate Gaussian orthant probability. The three correlations are `d,d,d^2`, where

`d^2=(1+rho)/2`.

Using the exact trivariate orthant formula gives

`E p(X)^2 = 1/2 + [asin(rho)+asin((1+rho)/2)]/(2 pi)`.

Since `E p=(3+m)/4`, simplification yields the closed form

`E h(X)^2 = -1 - 2 q_opp + 4 q_2`,

where

`q_2=(2/pi) asin((1+rho_opp)/2)`.

Thus a rigorous upper bound is obtained by outward arcsine intervals:

`Eh2_hi = -1 - 2*qopp_lo + 4*q2_hi`,

`m4_hi = kappa^2*Eh2_hi + (1-kappa^2)*qopp_hi^2`.

Numerical reconnaissance (not theorem evidence) indicates the resulting fourth-trace upper is about `1.1344092209`, versus the incoming generic-HGR cap `1.15053`. With the already certified degree-56 data

`mu in (0.9155053441,0.9155053442)`, `eps^2 < 270154/10^10`,

this should permit a Kato-Temple target around `0.1720962`, a nonzero improvement over `0.172052`.

## Falsification points to check exactly

- verify the orthogonal block decomposition and `kappa` formula from the exact circulant covariance;
- verify `h` is even and the Hermite contraction therefore starts at degree 2, not degree 1;
- verify the exact trivariate formula for `E p^2` and all outward arcsine directions;
- verify a rational fourth-trace cap above the outward interval;
- verify the spectral-tail and Temple margins with the unchanged certified `mu,eps^2` data;
- verify the final `x<r^(4 theta)` by an integer-power comparison, not floating logarithms;
- retain the continuous-event direction: this is still a continuous lower-exponent bound via continuous survival subset of grid survival, not a discrete-path replacement.
