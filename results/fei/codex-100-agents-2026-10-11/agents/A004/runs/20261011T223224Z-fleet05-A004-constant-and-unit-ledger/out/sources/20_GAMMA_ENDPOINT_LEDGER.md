# Exact zero-outcome remainder for the stronger inverse-time TC question

30 September 2026. Natural logarithms. This is an exact reduction of the pending endpoint, not its proof. Use precisely the decaying-threshold policy in DECAYING_THRESHOLD.md, on a fixed finite n-bit initial law, with q_i<epsilon exp(-2t) off its finitely many event times.

At deterministic forced times use the right-continuous state after the complete finite cascade; all forced losses retain their pre-reveal conditional laws. Let D_t=DTC(P_t), T_t=TC(P_t), and let

    r_i=P_t(S_i=1 | S_without_i),
    Gamma(P_t)=sum_i Ent_(P_without_i)(1-r_i).

Zero-marginal coordinates are omitted. The elementary binary identity gives

    sum_i Ent(r_i)=TC(P_t)+DTC(P_t)-Gamma(P_t).

Indeed I(S_i;S_without_i)=Ent(r_i)+Ent(1-r_i), and the sum of these mutual informations is TC+DTC. The complete ordinary-click generator therefore satisfies

    G DTC= -TC-DTC+Gamma.

A forced full reveal reduces expected DTC by the actual conditional mutual information M_tau=I(S_i;S_without_i | pre-reveal history). Applying the finite-horizon generator identity to exp(t)D_t yields

    integral_0^T exp(t)E T_t dt
      =DTC(P0)-exp(T)E D_T
        +integral_0^T exp(t)E Gamma(P_t)dt
        -E sum_(forced tau<=T)exp(tau)M_tau.             (1)

Initial cascades are included. This retains the signed forced-information refund, rather than dropping it in the earlier integrating-factor bound.

For fixed n, the terminal term in (1) really tends to zero. Off event times,

    0<=DTC(P_t)<=H(P_t)<=sum_i h(q_i)
       <=n h(epsilon exp(-2t)).

Thus exp(t)DTC(P_t)->0 uniformly over histories. Also 0<=TC(P_t)<=sum_i h(q_i)<=n h(epsilon exp(-2t)). Similarly Gamma<=sum_i -(1-q_i)ln(1-q_i)<=J_t<=n epsilon exp(-2t). These explicit fixed-finite-n bounds make both weighted TC and Gamma integrals finite. The forced-information sum is nonnegative and (1) bounds its partial expectations, so its limit is finite as well. Monotone convergence consequently gives the exact identity

    integral_0^infinity TC(P_t)/s dt
      =DTC(P0)+integral_0^infinity Gamma(P_t)/s dt
        -E sum_forced M_tau/s_tau,                      (2)

with expectations inside both integrals and s=exp(-t).

The desired dimension-free endpoint would follow from an upper bound on the SIGNED remainder in (2) by C[DTC(P0)+J0]. No such estimate is proved here. Bounding Gamma by J alone gives an unwanted dimension/marginal-scale cost, and discarding the forced-information term loses the proposed mechanism.

## Existing controls do not refute the endpoint

For a uniform one-hot law on n labels, DTC0=ln n and J0=1. Until its threshold t*=(1/2)ln(epsilon n), no-click histories have weight s, TC=c_n=-(n-1)ln(1-1/n)<=1 and Gamma=c_n. The weighted TC integral is c_n t*=O(DTC0). The forced cascade's weighted DTC-information loss is exactly ln n. Consequently (2) holds with cancellation of its initial DTC and forced-information terms. This family does not refute the proposed TC endpoint.

For the actual Boolean ordinary-address source, the same calculation follows after the initial independent address reveals, as already checked in ADDRESS_HISTORY_GUARD.md. Its extra initial address energy changes neither the one-hot TC calculation nor its conclusion.

The earlier e^t/sqrt(1+t) estimate is insufficient on its own to bound (2), because multiplying a finite integral by the unbounded sqrt(1+t) is not justified. Source-realizability or a sharper information accounting must enter a proof of the remaining signed estimate. Full FEI remains open.

## A positive weighted-dissipation refinement for Gamma

This section proves a further nonreusing budget, still not a bound on the weighted lifetime in (2). For an active coordinate i with 0<q_i<1, hold its two conditional laws P0=P(S_without_i|S_i=0) and P1=P(S_without_i|S_i=1) fixed, and set

    d_i(q)=D(P0 || (1-q)P0+qP1),
    Gamma_i=(1-q_i)d_i(q_i).

The function d_i is convex, d_i(0)=0, and is differentiable at every interior q. Hence q d_i'(q)>=d_i(q). The source is finite, and the mixture denominator is bounded below by (1-q)P0 on P0's support, so zeros cause no derivative problem.

Under its own ordinary outcome-one observation, the no-click marginal drift is q'=-q(1-q); a click, at rate q, removes the coordinate and its Gamma_i term. Consequently

    G_i Gamma_i
       =-q_i Gamma_i-q_i(1-q_i) d/dq[(1-q)d_i(q)]_(q=q_i)
       =-q_i(1-q_i)^2 d_i'(q_i).

Define the nonnegative convexity surplus

    Omega_i=q_i(1-q_i)^2 d_i'(q_i)-(1-q_i)Gamma_i>=0.

For a different coordinate j, an observation is a channel of S_without_i. KL chain rule gives an expected decrease of Gamma_i, because after conditioning on that observation the remaining conditional KL is precisely the updated Gamma_i. For the infinitesimal one-click channel define

    a_ij=P(S_j=1|S_i=0),
    Psi_ij=(1-q_i)[a_ij ln(a_ij/q_j)-a_ij+q_j]>=0.

Then G_j Gamma_i=-Psi_ij for j not equal to i. The formula follows by expanding the two Bernoulli observation probabilities a_ij dt and q_j dt; its no-click term is essential. At zero-probability events use the continuous zero-weight convention. Put Omega=sum_i Omega_i and Psi=sum_(i!=j)Psi_ij. Summing yields the exact ordinary generator identity

    G Gamma+Gamma=sum_i q_i Gamma_i-Omega-Psi.          (3)

A forced full reveal of coordinate j also decreases expected Gamma. Its exact conditional loss is

    Delta_j Gamma
      =Gamma_j+sum_(i!=j)(1-q_i)
                     D(P(S_j|S_i=0)||P(S_j))>=0.       (4)

This is the finite-channel version of the same KL chain rule. It remains valid when the forced bit is deterministic, with zero terms omitted. No Boolean amplitude, source quantization or marginal-product hypothesis is used.

Apply (3) at finite horizon, retaining (4) at every forced event:

    E[e^T Gamma(P_T)]
      +integral_0^T e^t E[Omega(P_t)+Psi(P_t)]dt
      +E sum_(forced tau<=T)e^tau Delta Gamma_tau
       =Gamma(P0)+integral_0^T e^t E sum_i q_i Gamma_i dt. (5)

Since

    Gamma_i<=(1-q_i)ln(1/(1-q_i))<=q_i,
    sum_i q_i Gamma_i<=sum_i q_i²<=epsilon e^(-2t)J_t,
    E J_t<=e^(-t)J0,

the last integral is at most epsilon J0/2. Positivity, the finite-source terminal limit, and monotone convergence give the dimension-free positive theorem

    integral_0^infinity e^t E[Omega+Psi]dt
       +E sum_forced e^tau Delta Gamma_tau
        <=Gamma(P0)+(epsilon/2)J0
        <=(1+epsilon/2)J0.                             (6)

In particular all weighted forced Gamma losses are paid. Equations (2) and (6) control different quantities: (2) contains the weighted Gamma LIFETIME and the weighted forced DTC-information refund; (6) controls Gamma DISSIPATION and its own forced losses. They must not be substituted for each other.

For the one-hot control, the weighted Gamma level remains constant until its threshold, then disappears at the forced cascade. Its level/dissipation budget is O(1), whereas its weighted lifetime is c_n t*=Theta(ln n). Initial DTC is ln n, so the desired endpoint survives. For a general-real one-hot initial law, J0=1 and a lifetime bound using only J0 or the paid Gamma-dissipation total is false. The same normalized state occurs after the actual Boolean addressing source's initial independent address reveals, but that original Boolean source has I=a/2+1=Theta(ln n); it therefore does not refute a lifetime bound using its full original source influence.

The unresolved precise question remains whether the SIGNED difference

    integral e^t E Gamma(P_t)dt
       -E sum_forced e^tau I(S_i;S_without_i|history)

is at most C[DTC(P0)+J0] for this one policy and the desired source class. No argument here prices that difference. This note records the exact endpoint identity and a proved supplementary dissipation budget, rather than claiming a solution of the endpoint or of FEI.

## Review record

The coordinating researcher reconstructed the endpoint identity, fixed-finite-n terminal limit, own-coordinate generator, KL-chain-rule sign and integrated correction. The coordinating researcher then read this complete written note and checked both generator components, including the infinitesimal no-click KL term, the forced chain-rule loss and finite-n integrability. The trajectory researcher independently read the complete written note and checked the same endpoint, scalar, generator, forced-loss and integration claims. Both reviews retain the right-continuous post-cascade convention and the distinction between weighted lifetime and dissipation. No executable replay was performed or needed for this analytic note. No executable test or formal certification is claimed.
