# fleet02/B10 r12 — hyperbolic phase collapse and curved-cap obstruction

## Status

PROVED_SUPPORTING_LEMMA / VALID_COUNTEREXAMPLE_TO_JOINT-CAP-ONLY_CURVED_RECEIVER / RULED-SIDE-SOURCE-RESULT-APPLIED. Full exact-rank-three QFORM remains OPEN.

First unpaid implication: **QFORM-CURVED-COMPLEX-SECTION-FRESNEL-RECEIVER-v1**. After legal hub conditioning, retain the ORIGINAL-coordinate product-generated complex section through the quadratic V-phase and obtain a uniform two-sheet density bound without support, moments, log-concavity, fiber suprema, post-rotation independence, or pointwise characteristic-function decay.

Control used: owner programme QFORM-DENSITY-3EIG-20260922, owner revision 2026-09-22.15. Required source pin: math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837. Latest completed compatible partner report consumed: fleet03/B10 r29 (20260924T044022Z). Current master also contains the bounded-square curved-marginal result at 0ec096bcf1f9f4a31fdbada3d4af4322f8edf6cc; it is only a bounded-support partial result and is not used as though it covered the target.

## 1. Target-valid exact-null harmonic survivor

Retain the r11 harmonic frame. Let m=123, theta_j=2 pi j/m, and

    z_j = sqrt(2/m) cos(2 theta_j),
    r_j = sqrt(2/m) cos(theta_j),
    y_j = sqrt(2/m) sin(theta_j).

The three leaf coefficient vectors z,r,y are orthonormal by discrete Fourier orthogonality. Every transverse leverage is r_j^2+y_j^2=2/m=2/123<1/61. For 0<rho<1/64, c=1-rho, use the physical rows sqrt(c)e_1 and leaf rows sqrt(rho) z_j e_1+r_j e_2+y_j e_3. This is a Parseval frame. With

    M_0 = [[0,1,0],[1,0,0],[0,0,1]],

A=R M_0 R^T has exactly the three nonzero eigenvalues {1,-1,1}. For independent ORIGINAL-coordinate inputs H,X_1,...,X_m with densities <=1, set

    Z=sum z_j X_j,   L=sum r_j X_j,   V=sum y_j X_j.

Then exactly

    Q = 2 (sqrt(c) H + sqrt(rho) Z) L + V^2.                 (1)

No independence among Z,L,V is asserted. Only H is independent of the leaf bank.

## 2. New lemma: complex conditional section and exact q-collapse

For every p in R define the complex measure on R^2

    nu_p(B)=E[ exp(i p Z) 1_{(L,V) in B} ].

Let mu be the law of (L,V). Since |exp(i p Z)|=1, total variation satisfies |nu_p|<=mu. The two-dimensional ORIGINAL-product marginal theorem gives a density p_{L,V} for mu in this harmonic frame. Hence

    nu_p(dl dv)=g_p(l,v) dl dv,
    g_p(l,v)=a_p(l,v) p_{L,V}(l,v),
    |a_p(l,v)|<=1,                                           (2)

so in particular

    |g_p(l,v)|<=p_{L,V}(l,v),
    integral |g_p(l,v)| dv <= p_L(l).                        (3)

With the Fourier convention used in r11,

    Phi(p,q,w)=E exp(i(pZ+qL+wV))
              = integral integral exp(i(q l+w v)) g_p(l,v) dl dv.  (4)

The r11 Gaussian-regularised hyperbolic/square Fresnel representation was

    phi_Q(t)=omega_t/(8 pi^(3/2)|t|^(3/2))
      integral integral integral
      exp(-i xi q/(2t)) exp(-i w^2/(4t))
      psi_H(sqrt(c) xi) Phi(sqrt(rho) xi,q,w)
      dxi dq dw,                                              (5)

for t!=0 and |omega_t|=1.

Do NOT take absolute values in q. Fourier inversion in q, first with the same Gaussian regularisation as (5), gives at Lebesgue points

    integral exp(-i xi q/(2t)) Phi(p,q,w) dq
      =2 pi integral exp(i w v) g_p(xi/(2t),v) dv.             (6)

Therefore the entire q-collapsed absolute majorant obeys

    integral |psi_H(sqrt(c)xi)|
      |2 pi integral exp(iwv)g_{sqrt(rho)xi}(xi/(2t),v)dv| dxi
    <=2 pi integral p_L(xi/(2t)) dxi
    =4 pi |t|.                                                (7)

This is uniform in rho and uses only ORIGINAL-coordinate provenance. In particular, the logarithmic hub-L1 divergence found in r11 is completely absent once the mixed hyperbolic phase is retained through the q integration. That logarithm was an artefact of taking |Phi| before q inversion, not an intrinsic near-null obstruction.

One can also perform the w Fresnel integral before absolute values:

    integral exp(-i w^2/(4t)) exp(iwv) dw
      =2 sqrt(pi|t|) sigma_t exp(i t v^2), |sigma_t|=1.

Thus (5) collapses to

    phi_Q(t)=tilde_omega_t/(2|t|)
      integral psi_H(sqrt(c)xi)
        [ integral exp(i t v^2)
          g_{sqrt(rho)xi}(xi/(2t),v) dv ] dxi,                (8)

with a harmless unit-modulus convention factor. Equivalently, after xi=2tl, (8) is the direct conditional identity

    phi_Q(t)= integral integral
       psi_H(2 sqrt(c)t l) exp(i t v^2)
       g_{2 sqrt(rho)t l}(l,v) dl dv.                         (9)

Formula (8), rather than the three-frequency absolute majorant, is the endpoint-stable interface to attack.

A final absolute value in (8) gives only |phi_Q(t)|<=1, so the lemma is not itself a proof of QFORM. The surviving analytic debt is cancellation in the curved complex section

    C_{t,p}(l)=integral exp(i t v^2) g_p(l,v) dv,              (10)

averaged along p=2 sqrt(rho)t l against the legal hub factor. Any successful receiver must use more than the scalar bound (3).

## 3. New obstruction: a joint-density cap alone cannot control a curved marginal

The current curved-marginal work shows why bounded support helps. Here is an exact obstruction to dropping provenance and keeping only a two-dimensional density cap.

Let C=1/(2 pi), a(v)=C/(1+v^2), and define on R^2

    h(u,v)=1_{ |u+v^2| <= a(v) }.                             (11)

Then 0<=h<=1 and

    integral integral h(u,v) du dv
      = integral 2C/(1+v^2) dv =1,                            (12)

so h is a probability density with joint density cap one. Its V marginal is exactly standard Cauchy:

    p_V(v)=2a(v)=1/(pi(1+v^2)).                               (13)

But for Y=U+V^2 the change of variables y=u+v^2 gives

    p_Y(y)=integral 1_{ |y| <= C/(1+v^2) } dv
          =2 sqrt(C/|y|-1),   0<|y|<C,                        (14)

and p_Y(y)=0 for |y|>=C. Hence ess sup p_Y=infinity.

Therefore the statement

    ||p_{U,V}||_infinity <= const  ==>  ||p_{U+cV^2}||_infinity <= universal const

is false even at c=1. This is a counterexample to a **joint-cap-only proof interface**, not to QFORM: (11) is not claimed to be a linear image of independent source coordinates. Precisely for that reason, a valid endpoint proof must retain stronger ORIGINAL-product information, such as the full family g_p in (2)-(4), rather than project and then forget provenance.

This also explains the scope of the current bounded-square result at commit 0ec096bcf1f9f4a31fdbada3d4af4322f8edf6cc: its Proposition 1 assumes |V-v_0|<=R and obtains a bound C_1+C_2 R^(1/2); Proposition 2 assumes bounded coordinate supports. Those hypotheses are forbidden in the exact target. The curved strip (11) shows that some additional structure beyond a bare joint cap really is necessary when V is unbounded.

## 4. Partner result consumed

The completed fleet03/B10 r29 reduction treats the generic near-coloop rank-three matrix

    M=[[alpha,s,0],[s,b,k],[0,k,d]],

with |alpha|<1/16, s^2>255/256 and diffuse transverse leaves. Its exact algebra gives a normalized hub form with a hard transverse square |d|>=1 and a discriminant floor |D_H|>0.94106; in particular the remaining endpoint problem is a rough curved-section receiver, not matrix degeneracy.

Our harmonic core has alpha=0, s=1, k=0, d=1, so it saturates the hard-square floor. Formula (8) shows that in this extremal matrix geometry the old rho-dependent hyperbolic absolute-value barrier can be removed exactly. The remaining obstruction is therefore genuinely the rough-law curved complex section (10), in agreement with the partner's `QFORM-ROUGH-CURVED-SECTION-WITH-HARD-SQUARE-v1` diagnosis.

## 5. Required pinned source result spent on an actual inequality

At source pin e5f71d79eff325201dd0274053d20268ce65b837, the completed ruled-level-set theorem for signature (+,+,-) states, for eigenvalue moduli lambda_1,lambda_2,mu>=1 and all majority-sign levels s>=0,

    p_Q(s)
      <=(lambda_1 lambda_2 mu)^(-1/2)
        integral_0^(2pi)
        [sin^2(theta)/lambda_1 + cos^2(theta)/lambda_2 + 1/mu]^(-1/2) dtheta
      <= pi sqrt(2).                                         (15)

It uses the ORIGINAL product measure through its two-dimensional marginal and does not assert post-rotation independence.

For the harmonic family above lambda_1=lambda_2=mu=1, so directly

    p_Q(s) <= pi sqrt(2) < 4.443,   for every s>=0.            (16)

Thus this run does not re-prove the ruled side. The actual unresolved levels are the minority/two-sheet side s<0.

## 6. What is now ruled out / what remains

Paid or removed:
- the r11 logarithmic `int |psi_H|` divergence after full three-frequency absolute values: removed by (6)-(8);
- matrix degeneration in the partner's canonical near-coloop form: partner r29 gives |d|>=1 and |D_H|>0.94106;
- majority-sign levels: paid by (16).

Still unavailable:
- arbitrary-support curved complex-section cancellation in (10);
- any proof based only on a cap for p_{L,V}: false by (11)-(14);
- pointwise characteristic-function decay: prohibited by the correction ledger and unnecessary in the desired formulation;
- moments, compact support, log-concavity, fiber suprema, or independence after projection/rotation.

Next attack: use the product formula (4) before collapsing all leaf frequencies. A promising target is a weak-L1 or dyadic estimate for the **integrated** curved sections C_{t,p}(l), averaged simultaneously in l and p=2 sqrt(rho)t l, based on the source line-L1 / two-frequency product inequalities. It must avoid estimating each fixed-l fiber separately.

## Provenance/status

- Mathematical status: supporting lemma + receiver-level counterexample; not a full solution.
- Product provenance: retained through the original independent source characteristic functions and the complex conditional measure nu_p.
- Continuity is not used as a substitute for a density bound.
- No hidden support, moment, log-concavity, diagonal-basis, or post-rotation-independence assumption.
- Privacy/secret fallback review of this explicit math-only file: no credentials, personal secrets, external private data, or machine paths included. Repository-side secret scanner was not exposed through the available connector, so this is a narrow manual allowlist review rather than an automated scan.
