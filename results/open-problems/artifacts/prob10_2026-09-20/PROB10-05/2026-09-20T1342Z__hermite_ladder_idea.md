# PROB10-05 idea checkpoint — finite even-Hermite ladder for the softened four-cycle

Runtime request: GPT-6 / maximum. No authenticated runtime model/effort telemetry is exposed here, so runtime model/effort is UNVERIFIED.

Status on entry: PARTIAL / source target OPEN. Frozen model: centered standard fBM, H=1/4, I(t)=int_0^t B_{1/4}(s)ds, continuous one-sided event sup_{0<=t<=T} I(t)<=1. The strongest own-track self-certified candidate read on current master is

    theta_{2,1/4} > 1738/10099 = 0.172096247153...

from `runs/prob10_2026-09-20/PROB10-05/2026-09-20T1304Z__even_block_hgr_172096247.md` (blob `f056c342e1410c65719069dd64b96172448d0dfa`). The newer neighboring persistence report `proofnet24/NM13-09/progress-persistence/runs/2026-09-20/2026-09-20T1312Z__corrected_mesh22_trace_17207285.md` is weaker and is consumed, not overwritten. Canonical ownership remains HARD7-05 through `operations/claims/MOLCHAN-2025-THETA2H.md`.

## Three materially different nonexhausted attacks

1. **Finite even-Hermite ladder for the opposite-pair observable — main attack.** The preceding report used only that the conditional opposite-pair sign observable h is even, replacing a generic HGR factor kappa by kappa^2. The new idea is to compute many leading even Hermite coefficients exactly and move only the uncomputed tail to the next Hermite contraction. This should strictly reduce the certified fourth-trace cap without changing the covariance comparator or importing a spectral number from another operator.

2. **Higher-degree Perron quasimode / residual reduction — distinct operator attack.** Recompute a degree >56 finite-polynomial witness for the present r=22/25 softened operator, then certify its one- and two-step Gaussian moments. This can reduce the Kato-Temple residual independently of the four-cycle trace. It is not used in the present attack because the parity/Hermite structure gives a proof-level improvement without another numerical eigensearch.

3. **Reverse continuous interpolation — distinct upper-endpoint attack.** A sampled path below a negative safety margin plus a sufficiently small inter-mesh modulus implies continuous survival. The unresolved issue is a lower bound for the *joint* margin/modulus event under long survival with only subexponential loss. Until that is proved, discrete survival is not promoted to a continuous upper-exponent bound. The source-valid upper endpoint remains UNKNOWN beyond the published 1/4 bound.

## Exact new identity before code

Retain the incoming softened comparator r=22/25, s=936901/940000 and the cyclic four-Gaussian representation. Let rho=rho_opp be the opposite correlation and

    q = sqrt((1+rho)/(1-rho)).

For an independent standard Gaussian pair (X,B), define the wedge event

    E = {|B| < q |X|}.

For F=sgn(V_0)sgn(V_2), conditioning on the normalized common mode gives

    h(X)=E(F|X)=2 P(E|X)-1 = 4 Phi(q|X|)-3.

Let alpha=atan(q)=pi/4 + (1/2) asin(rho), so sin(2 alpha)=sqrt(1-rho^2). For n>=1 let He_{2n} be the probabilists' Hermite polynomial and

    M_n = E[He_{2n}(X) 1_E].

Polar coordinates give, for m>=0,

    E[X^(2m) 1_E]
      = (2^(m+1) m! / pi) J_m(alpha),

where

    J_0(alpha)=alpha,
    J_m(alpha)=((2m-1)/(2m)) J_{m-1}(alpha)
               + [sqrt(1-rho^2)/(4m)] ((1-rho)/2)^(m-1).

Write J_m=A_m alpha+sqrt(1-rho^2) B_m. Then A_0=1,B_0=0 and

    A_m=((2m-1)/(2m)) A_{m-1},
    B_m=((2m-1)/(2m)) B_{m-1}
        +(1/(4m))((1-rho)/2)^(m-1).

Expanding He_{2n} in monomials shows the alpha coefficient cancels exactly for every n>=1. Thus

    M_n = [sqrt(1-rho^2)/pi] C_n,

where C_n is an explicit rational function of the rational rho obtained by the finite recurrence above. Since E[He_{2n}(X)]=0,

    E[He_{2n}(X) h(X)] = 2 M_n,

and the squared orthonormal Hermite coefficient is exactly

    a_{2n}^2 = 4(1-rho^2) C_n^2 / (pi^2 (2n)!).

For example C_1=1 and C_2=-(rho+2), recovering

    a_2^2 = 2(1-rho^2)/pi^2,
    a_4^2 = (rho+2)^2(1-rho^2)/(6 pi^2).

Now let X,Y be the common modes of the two opposite pairs with Corr(X,Y)=kappa. If

    h = m + sum_{n>=1} a_{2n} psi_{2n},
    m=(2/pi)asin(rho),

then Mehler gives the exact series

    m_4 := E[h(X)h(Y)]
         = m^2 + sum_{n>=1} a_{2n}^2 kappa^(2n).

For every finite N, Parseval therefore yields the rigorous upper bound

    m_4 <= kappa^(2N+2) E[h^2]
           +(1-kappa^(2N+2)) m^2
           +sum_{n=1}^N a_{2n}^2 (kappa^(2n)-kappa^(2N+2)).

This strictly refines the incoming N=0 even-parity/HGR bound. The plan is to certify N=100 with outward rational pi/arcsin bounds, retain the same exact degree-56 Perron data for this exact operator, and test whether the resulting smaller fourth-trace budget improves the Kato-Temple exponent certificate.

No source-level claim is made by this checkpoint. The exact exponent and upper endpoint remain UNKNOWN; the old theta=H(1-H) formula remains Molchan's refuted prior conjecture, not a target or result of this track.