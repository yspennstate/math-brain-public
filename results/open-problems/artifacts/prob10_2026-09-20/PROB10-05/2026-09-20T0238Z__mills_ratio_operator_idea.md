# PROB10-05 idea checkpoint — replace the fourth-moment truncation by a Mills-ratio resolvent bound

Runtime request: GPT-6 / maximum. The execution environment identifies GPT-5.6 Sol; reasoning level is UNVERIFIED, so this is not claimed to be GPT-6 maximum.

Frozen source target: standard fBM with H=1/4, I(t)=int_0^t B_{1/4}(s) ds, continuous event sup_{0<=t<=T} I(t)<=1, and its persistence exponent theta_{2,1/4}. Current strongest repository candidate consumed before this idea is the complementary NM13-09 bound

    41369/250000 < theta_{2,1/4} <= 1/4,

with width 21131/250000 = 0.084524 and cyclic fourth-trace cap tr(K^4)<1.082139. This is PARTIAL and pending independent validation.

## New route, written before any new checker

The current equicorrelated four-cycle endpoint uses the inherited pointwise probit-product inequality

    Q(x)=Phi(x)Phi(-x) <= exp(-x^2/2)/(4 sqrt(1+6x^2/25)).

After the equicorrelated common-factor representation, the only lossy step in the newest proof is the global polynomial truncation

    E[1/(1+qY^2)] <= 1-q+3q^2-15q^3+105q^4,

where Y~N(0,1) and q=6 rho/[25(1+rho)] ~=0.11915. Numerically this polynomial is about 0.91923, while the exact expectation is about 0.90885. The planned replacement is analytic, not numerical:

1. Write x=q^{-1/2} and the Gaussian Mills ratio m(x)=(1-Phi(x))/phi(x). Direct integration gives

       E[1/(1+qY^2)] = x m(x).

2. Prove directly from the Riccati equation m'(x)=x m(x)-1 that

       m(x) < 4/(3x+sqrt(x^2+8)), x>0.

   If u(x)=4/(3x+sqrt(x^2+8)), then

       u'-(xu-1) < 0,

   because its numerator is

       x(x^2+6) - (x^2+2)sqrt(x^2+8) < 0,

   and squaring is exact since both sides are positive:

       (x^2+2)^2(x^2+8) - x^2(x^2+6)^2 = 32.

   Since (u-m)e^{-x^2/2}->0 at infinity, integrating the differential inequality backward gives u-m>0.

3. Therefore

       E[1/(1+qY^2)] < 4/(3+sqrt(1+8q)).

   For the frozen exact rho=168557580/170952323 this should be <91/100 by a single rational square comparison.

4. Relative to the already certified fourth-moment polynomial bound, this should lower the normalized equicorrelated endpoint by >0.000117 while leaving the arcsin enclosure untouched. Combining with the already proved 64-block Plackett decrement >147/40000 should give

       tr(K^4) < 1.082022,

   enough, with the inherited degree-18 quasimode/Temple step, to test theta*=0.16548.

## Negation / failure test before promotion

The tempting classical-looking bound 2/(x+sqrt(x^2+4)) is in the wrong direction here: at q~=0.11915 it gives x times the candidate Mills bound around 0.90287, below the actual expectation around 0.90885. It cannot be used as an upper bound. The 4/(3x+sqrt(x^2+8)) comparison gives about 0.90959 and survives the correct differential-sign test above.

## Two other materially different attacks to compare in the report

- Direct circulant-mode reduction of the cyclic four-orthant probability to a two-dimensional folded-normal integral. It has more theoretical room (true trace is numerically near 1.08171), but a short outward-rational integral enclosure has not yet been built.
- Direct positive-operator/Collatz-Wielandt control of the Perron root, avoiding the fourth trace. The current degree-18 quasimode is good enough that the bottleneck is the non-Perron spectral radius; a pointwise supersolution would remove that bottleneck, but no simple positive test function is presently known to dominate Kf/f uniformly near the killing boundary.

Only after the Mills argument is algebraically closed will an exact checker be written for the rational margins and the spectral contradiction.