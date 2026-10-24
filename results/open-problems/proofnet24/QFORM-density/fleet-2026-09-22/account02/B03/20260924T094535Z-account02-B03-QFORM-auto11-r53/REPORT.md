SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B03, 2026-09-24T09:45:35Z.
attacking: replace the false conditional-projection-moment gate by a determinant-homogeneous dual receiver: spread rank-three Fresnel when leverage is small, and the newest same-bank square-hyperbola theorem when it is not; compare their whole-copy half-Riesz budgets on the same invariant.

# QFORM-DETERMINANT-DUAL-RECEIVER-v1

Status: NEW SUPPORTING THEOREM / FALSE CONDITIONAL-MOMENT GATE BYPASSED ON ITS OWN FULL-RANK STRESS FAMILY / LATEST PARTNER r51 APPLIED. The unrestricted QFORM density conjecture remains OPEN. Unrestricted continuity remains OPEN.

## 1. First unpaid implication

The preceding B03 environment-conditioned weighted-time compiler is only a sufficient interface. It must NOT be promoted into a structural requirement that one condition on the orthogonal complement of the three large directions and control positive moments of the resulting conditional projection-density cap: the live correction QFORM-CONDITIONAL-PROJECTION-POSITIVE-MOMENT-FALSE-v1 proves those moments diverge on an admissible full-rank target family.

A more robust structural target is now visible. Seek an original-product packet whose deterministic three-dimensional determinant currency

    J = |a| |b|^2 rho^2 sigma^2 tau^2

is bounded below. When the corresponding three-dimensional coefficient frame is spread, the pinned Fresnel theorem pays J directly and gives strong time decay. When the packet is localized, the newest account03/B03 same-bank square-hyperbola theorem pays the SAME J through product projection densities, without any conditional-cap moment. The remaining global debt is therefore to extract such a packet (or another already-paid aggregate receiver) from every survivor of the existing exterior/volume/finite-hub branches. Do not route through universal positive conditional-density moments.

## 2. Determinant-homogeneous same-bank packet

Let X=(X_i)_{i in K} and Z=(Z_j)_{j in L} be disjoint banks of genuine independent scalar coordinates, all with densities at most one. Let r,t in R^K satisfy r perpendicular t, let v in R^L, and write

    rho=||r||_2,   sigma=||t||_2,   tau=||v||_2,
    S=<r,X>,       T=<t,X>,         V=<v,Z>.

Fix a,b nonzero and c real. Allow arbitrary translations of S,T,V coming from a fourth source-disjoint physical environment W; condition on W below, so the translations are deterministic. Consider

    Q = a(S+d)^2 + 2b(T+cS+alpha)(V+beta) + gamma.       (2.1)

In the normalized deterministic mode basis

    S0=S/rho,  T0=T/sigma,  V0=V/tau,

the quadratic coefficient matrix is

        [ a rho^2       0          b c rho tau ]
    B = [    0          0          b sigma tau ]          (2.2)
        [ b c rho tau   b sigma tau      0       ].

Hence

    det B = - a b^2 rho^2 sigma^2 tau^2,                 (2.3)

independently of the shear c. Define

    J := |det B| = |a| |b|^2 rho^2 sigma^2 tau^2.        (2.4)

This is the natural cubic spectral-volume currency of the packet.

## 3. New dual-receiver synthesis

### 3.1 Leverage-free endpoint from newest account03/B03 r51

The newest compatible partner report, account03/B03 r51, proves QFORM-SAMEBANK-PAIR-HYPERBOLIC-SQUARE-v1. Its product-bank specialization gives

    ||p_Q||_{infty,ess}
       <= 12 (rho sigma tau)^(-2/3)
              |a|^(-1/3)|b|^(-2/3)
       = 12 J^(-1/3).                                    (3.1)

The bound is uniform in c and in all translations from W, so conditioning on W and averaging preserves (3.1). No rotated coordinate is declared probabilistically independent: S and T are two projections of the SAME original product bank, and their dependence is retained through the partner theorem's joint two-dimensional projection-density input.

Thus every interval I obeys

    P(Q in I) <= 12 J^(-1/3) |I|.                        (3.2)

For an independent copy Q' of the WHOLE scalar output, convolution gives the same density cap for Q-Q'. The elementary cap-to-half-Riesz estimate and the whole-copy identity

    |phi_Q(t)|^2 = E exp(i t (Q-Q'))                     (3.3)

give

    E |Q-Q'|^(-1/2) <= 4 sqrt(6) J^(-1/6),              (3.4)

and therefore

    int_R |t|^(-1/2)|phi_Q(t)|^2 dt
       <= 8 sqrt(3 pi) J^(-1/6).                         (3.5)

No coordinatewise X-X' is ever detached from its conjugate X+X'.

### 3.2 Spread endpoint from the required pinned e5f71d79... theorem

Suppose, in addition, the three-dimensional deterministic coefficient range in original coordinates has physical leverage at most 1/2. Apply completed Theorem F of

    math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837
    proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md.

Because the product of the three nonzero eigenvalues of (2.2) has modulus J and the restricted Gram determinant is one after choosing an orthonormal basis of the packet range, Theorem F gives the actual characteristic-function envelope

    |phi_Q(t)| <= min{1,(4 pi)^(3/2) J^(-1/2)|t|^(-3/2)}.  (3.6)

Integrating (3.6) yields exactly the SAME density scale and constant as (3.1):

    ||p_Q||_infty <= 12 J^(-1/3).                        (3.7)

The agreement is not dimensional bookkeeping: it identifies J=|det B| as a receiver-invariant currency across two different product-preserving mechanisms. The partner theorem removes the leverage requirement; the Fresnel theorem supplies stronger pointwise time decay when leverage is available.

Squaring (3.6) and integrating at the crossover

    t0 = [(4 pi)^(3/2) J^(-1/2)]^(2/3)

improves (3.5) in the spread regime to

    int_R |t|^(-1/2)|phi_Q(t)|^2 dt
       <= (48/5) sqrt(pi) J^(-1/6),                     (3.8)

hence, by (3.3),

    E|Q-Q'|^(-1/2)
       <= (24 sqrt(2)/5) J^(-1/6).                      (3.9)

The envelope (3.6) is integrable, so the spread branch has a continuous C_0 density. Continuity is not asserted from the leverage-free partner endpoint alone.

## 4. Exact-target diffuse same-bank family: both receivers meet at constant 4

Let m>=4 be even. On one physical bank K of size m choose flat orthonormal sign vectors r,t, so every coordinate has |r_i|=|t_i|=m^(-1/2). On a disjoint bank L of size m take the flat unit vector v. Put

    S=<r,X>,  T=<t,X>,  V=<v,Z>,
    Q_m = 3 S^2 + 6(S+T)V.                              (4.1)

The deterministic mode matrix is

        [3 0 3]
    B = [0 0 3],                                        (4.2)
        [3 3 0]

with

    det B=-27,
    spec(B) = {-3.74093881..., 1.33512560..., 5.40581321...}. (4.3)

Thus Q_m is a strict exact-owner-target family: all three nonzero eigenvalues have modulus >1. Here J=27, and the newest partner theorem gives immediately

    ||p_{Q_m}||_{infty,ess} <= 12*27^(-1/3)=4.          (4.4)

This is an equation-level use of account03/B03 r51 on an actual exact-target family.

The range projection has diagonal leverage 2/m on K and 1/m on L, hence at most 1/2 for m>=4. Therefore the required pinned Theorem F applies to the same family and independently gives the same height constant 4 together with

    |phi_{Q_m}(t)|
       <= min{1,(4 pi)^(3/2)/sqrt(27) * |t|^(-3/2)}.    (4.5)

Consequently

    int_R |t|^(-1/2)|phi_{Q_m}(t)|^2 dt
       <= (48/5) sqrt(pi/3)
       = 9.823936396286289...,                           (4.6)

and

    E|Q_m-Q_m'|^(-1/2)
       <= 24 sqrt(2)/(5 sqrt(3))
       = 3.919183588453085... .                         (4.7)

The generic leverage-free conversion from (4.4) would only give 8sqrt(pi)=14.1796... in (4.6), so the direct spread-time resource is quantitatively stronger even though the one-copy density constant agrees exactly.

This family is also a bounded-localizer obstruction. In original coordinates every matrix coefficient is O(1/m): specifically |A_ij|<=6/m. Hence every fixed k x k physical minor is at most

    (6 sqrt(k)/m)^k                                      (4.8)

by Hadamard, while the aggregate determinant currency J stays exactly 27. A proof that pays one bounded physical minor before aggregation therefore loses all scale on this family. This is an obstruction to that proof mechanism, not to QFORM.

## 5. The false conditional-moment family is uniformly paid before conditioning

The live correction QFORM-CONDITIONAL-PROJECTION-POSITIVE-MOMENT-FALSE-v1 uses 3m independent Uniform[0,1] coordinates, split into three blocks, with block-constant unit vectors u_1,u_2,u_3 and E=span{u_1,u_2,u_3}. It takes

    A_m^corr = P_1 + P_2 - P_3 + (1/128)(I-P_E),        (5.1)

whose spectrum is

    {1,1,-1, 1/128,...,1/128}.                           (5.2)

For W=P_(E^perp)X and Y=P_E X, that correction proves for every 0<s<2

    E ||p_(Y|W)||_infty^s
       = J_m(1-s)^3
       ~ Gamma(2-s)^3 m^(3s/2),                          (5.3)

so EVERY fixed positive conditional-cap moment diverges with m. In particular the previously tempting s=2/3 gate grows linearly in m. This is a source-valid obstruction to extending the prior B03 environment-conditioned compiler by conditioning on the spectral orthogonal complement.

But the same matrix can be rewritten as

    A_m^corr
      = (1/128) I
        + (127/128)P_1 + (127/128)P_2 - (129/128)P_3.    (5.4)

This is exactly the pinned Theorem-F architecture: diagonal remainder plus three rank-one directions. Each physical row leverage is 1/m<=1/2, the Gram matrix is I_3, and

    D0 := |(127/128)^2 (-129/128)|
        = (127/128)^2(129/128)
        = 0.9921269416809082... .                        (5.5)

Therefore, for EVERY choice of independent cap-one input densities on this same coefficient matrix (not only the uniforms used to refute the conditional moment), the pinned theorem gives

    |phi_Q(t)|
      <= min{1,(4 pi)^(3/2) D0^(-1/2)|t|^(-3/2)},       (5.6)

and hence

    ||p_Q||_infty
      <= 12 D0^(-1/3)
      = 12.031658545595015... .                          (5.7)

Thus the conditional-density moment can diverge to infinity while the actual QFORM output on the same admissible full-rank matrices has a uniform density bound about 12.03. The divergence is genuinely an artifact of the conditional interface, not a sign of large quadratic-form density.

The assigned whole-copy time estimate is likewise dimension-free:

    int_R |t|^(-1/2)|phi_Q(t)|^2 dt
      <= (48/5)sqrt(pi) D0^(-1/6)
      = 17.037987508728477...,                           (5.8)

and

    E|Q-Q'|^(-1/2)
      <= (24sqrt(2)/5)D0^(-1/6)
      = 6.797173590183264... .                           (5.9)

Again only the whole-output identity |phi_Q|^2=phi_(Q-Q') is used.

## 6. Consequence for the structural programme

This run changes mechanism after the conditional-environment approach. The correct lesson of the live correction is stronger than "conditional moments are hard": they can diverge polynomially on a family where the pre-conditioning aggregate Fresnel resource is uniformly excellent.

The new dual-receiver synthesis shows a useful invariant continuity across geometry:

* spread packet: pinned Fresnel, height 12 J^(-1/3), stronger weighted time (48/5)sqrt(pi)J^(-1/6);
* arbitrary same-bank square-hyperbola packet: partner r51, the SAME height 12 J^(-1/3), and leverage-free whole-copy weighted time 8sqrt(3pi)J^(-1/6).

The first unpaid implication is therefore to derive, from the three-large-eigenvalue hypothesis plus failures of already-paid exterior/volume/grouped exits, a product-valid packet with J>=c or an equivalent aggregate determinant currency. It is no longer acceptable to make a positive conditional projection-density moment an intermediate obligation.

This does NOT solve the unrestricted conjecture, does NOT assert a universal good bounded physical localizer, and does NOT claim unrestricted continuity.

Sources consumed and checked: fresh math-research-brain main owner/control and corrections; required pinned e5f71d79eff325201dd0274053d20268ce65b837 RESULTS.md / FOURIER_ROUTE_REPORT.md / COUNTEREXAMPLE_SEARCH.md; current same-directory continuation; latest compatible account03/B03 r51 report; live conditional-moment correction source. Execution context remains WITHOUT_VERIFIED_BRAIN.
