# PROB10-05 idea checkpoint — continued-fraction Mills supersolution before code

Runtime request: GPT-6 / maximum. Authenticated scheduler model/effort telemetry is not exposed; runtime model/effort therefore remains **UNVERIFIED** in this checkpoint. No scheduler or external-delivery settings are changed.

Frozen target: standard centered fBM with H=1/4, I(t)=∫_0^t B_{1/4}(s)ds, continuous event sup_{0<=t<=T} I(t)<=1, and the source persistence exponent theta_{2,1/4}. Current master baseline consumed from the complementary NM13-09 report is the repository candidate

    165483/1000000 < theta_{2,1/4} <= 1/4,

with width 84517/1000000. This is PARTIAL and pending independent validation; the external-source baseline remains 1/8 <= theta <= 1/4.

## New idea A (primary): replace the algebraic Mills supersolution by an even continued-fraction convergent

The current PROB10-05 endpoint argument reduces the equicorrelated four-cycle loss to

    E[(1+qY^2)^(-1)] = x m(x),  x=q^(-1/2),

where m is the Gaussian Mills ratio, and uses x m(x)<0.91. Instead, use the tenth continued-fraction convergent

    u_10(x)=
      (x^10+54x^8+938x^6+6090x^4+12645x^2+3840)
      /[x(x^10+55x^8+990x^6+6930x^4+17325x^2+10395)].

Direct differentiation should give

    u_10'(x) - (x u_10(x)-1)
      = -39916800 /
        [x^2 (x^10+55x^8+990x^6+6930x^4+17325x^2+10395)^2] < 0.

Since m'(x)=xm(x)-1 and both u_10,m=O(1/x), the same integrating-factor argument as the previous Mills proof would imply m(x)<u_10(x) for all x>0. In q=x^{-2} coordinates this becomes the exact rational bound

    x u_10(x)=
      (1+54q+938q^2+6090q^3+12645q^4+3840q^5)
      /(1+55q+990q^2+6930q^3+17325q^4+10395q^5).

At the frozen q=202269096/1697549515, the planned exact check is whether this is <0.909 and whether the resulting trace improvement is enough to push the source lower endpoint strictly beyond 0.165483.

This is not another Plackett quadrature refinement: it attacks the scalar Gaussian resolvent endpoint loss while consuming the peer's already-certified 256-block Plackett decrement.

## Negation test for idea A

Before coding, the route can fail in three places: (i) the Riccati residual could have the wrong sign; (ii) the continued-fraction value could fail to improve 0.91; or (iii) the gain could be too small to survive the inherited Temple/quasimode margins. The derivative identity above gives the desired sign analytically; (ii) and (iii) will be tested exactly, not by floating-point promotion.

## New idea B (materially different): reverse continuum interpolation for an upper exponent bound

To move the upper endpoint rather than the lower endpoint one needs a grid-to-continuum statement of the form

    P[X(t)<0 for all t in [0,nΔ]]
      >= exp(-n epsilon(Δ)) P[X(jΔ)<-eta, j=1,...,n]

with an explicit epsilon(Δ)->0 after optimizing eta. A naive endpoint-conditioned bridge bound is not immediately valid because the Lamperti process is stationary Gaussian but not Markov: conditioning only on adjacent endpoint values does not control the conditional mean/variance of the interior after conditioning on the full outside sigma-field. The exact missing lemma is a uniform conditional-variance/mean comparison for each cell against the two-endpoint Gaussian bridge. This route has not been solved here and no upper-bound movement is claimed from it.

## New idea C (materially different): positive-operator supersolution

For the killed transfer operator K, a strictly positive h with Kh<=lambda h pointwise would give lambda_1<=lambda directly and bypass both tr(K^4) and Temple. The old degree-18 L^2 quasimode does not supply this because its pointwise relative residual blows up near the killing boundary. A possible repair is to multiply a Gaussian/Hermite core by a boundary factor h_a(x)=Phi(a x+b) chosen so that the Gaussian transition integral Kh_a is another probit expression. The exact obstruction to check is whether one can choose a,b and lambda below r^{4*0.165483} while keeping the ratio uniformly controlled as x approaches the boundary. No theorem is claimed from this route in this checkpoint.

Only after the analytic continued-fraction route is written here will an exact checker be created.