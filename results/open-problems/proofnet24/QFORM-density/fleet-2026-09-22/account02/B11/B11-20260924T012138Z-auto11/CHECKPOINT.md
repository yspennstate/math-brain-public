# Early substantive checkpoint — dependent-remainder hyperbolic L2 and half-Riesz receiver

Programme: QFORM-DENSITY-3EIG-20260922. Full target OPEN.

## Lemma A: arbitrary same-bank remainder is harmless at L2

Let H be independent of a random element Z. Suppose H has density f with ||f||_infinity<=F. Let Y=Y(Z) have a one-dimensional density g with ||g||_infinity<=G. Let R=R(Z) be arbitrary measurable and let a!=0. Then

    S = a H Y + R(Z)

has an L2 density and

    ||p_S||_2^2 <= 4 F G / |a|.                                    (A.1)

Proof. Conditional on Z=z, with y=Y(z), r=R(z),

    p_S(s)=E_Z [ f((s-r)/(a y)) / |a y| ],

and P(Y=0)=0. For two independent copies z,z', square this formula, integrate in s, and set h=(s-r)/(a y). The inner overlap is

    1/|a y'| int f(h) f((r-r'+a y h)/(a y')) dh.

For every rho!=0 and b,

    int f(h) f(rho h+b) dh <= F min(1,|rho|^{-1}),

by bounding either factor by F and changing variables in the other. Hence the overlap is at most

    F / ( |a| max(|y|,|y'|) ).

If Y,Y' are iid with density cap G, then

    E 1/max(|Y|,|Y'|)
      = int_0^infinity P(|Y|<u)^2 du/u^2
      <= int_0^{1/(2G)} 4G^2 du + int_{1/(2G)}^infinity du/u^2
      = 4G.

This proves (A.1). Notice that R may depend arbitrarily on Y and on every other component of Z; it enters only through a translation in the overlap integral. No conditional density of the companions of Y is used.

The constant is sharp already for the rank-two logarithmic control. If H,Y are centered unit uniforms and a=2, then

    p_{2HY}(t)=log(1/(2|t|)),  0<|t|<1/2,

and

    ||p_{2HY}||_2^2 = int_{-1/2}^{1/2} log^2(1/(2|t|)) dt = 2,

which equals 4/|a|. Thus this receiver deliberately preserves, rather than falsely removes, the rank-two logarithmic singularity.

## Lemma B: the same translation invariance gives a half-Riesz receiver

Under the same hypotheses,

    sup_t E |a H Y + R(Z)-t|^{-1/2}
       <= 8 sqrt(FG) |a|^{-1/2}.                                 (B.1)

Indeed, conditioning on Z gives

    E_H |a y H+b|^{-1/2} <= 2 sqrt(2F) |a y|^{-1/2},

by the one-dimensional bathtub bound for a probability density of cap F/|a y|. A second bathtub bound gives

    E |Y|^{-1/2} <= 2 sqrt(2G),

and (B.1) follows. Again R is completely arbitrary and may be same-bank dependent.

## Apply to the newest account03/B11 r45 puncture normal form

Partner r45 gives the exact source-valid rank-three model

    Q = 2 kappa sqrt(q) H W
        + 2 kappa sqrt(1-q) T W
        + d W^2 + 2 e W V + c V^2,                              (C.1)

where H is an original cap-one scalar independent of the residual triple (T,W,V), while (T,W,V) is a three-dimensional orthonormal projection of the residual original product source. It also gives

    kappa=||M e_1|| >= s := min |eig(M)|,
    kappa^2 |c-e^2 correction in the sheared basis| = |det M| >= s^3,

and, more precisely before/after the displayed shear, kappa^2|c|=|det M|. The overlap coefficient ratio is sqrt((1-q)/q).

The one-dimensional projection W has density cap G<=sqrt(2) by the product-projection marginal theorem. Take

    a = 2 kappa sqrt(q),
    R(T,W,V)=2 kappa sqrt(1-q) T W+dW^2+2eWV+cV^2.

Lemma A yields

    boxed: ||p_Q||_2^2 <= 2 sqrt(2)/(kappa sqrt(q))
                         <= 2 sqrt(2)/(s sqrt(q)).                (C.2)

Thus for the live near-coloop chamber q>=63/64,

    ||p_Q||_2^2 <= 16 sqrt(2)/(sqrt(63) s) < 2.851/s,
    ||p_Q||_2 < 1.689/sqrt(s).                                   (C.3)

In particular every interval I obeys

    P(Q in I) <= 1.689 s^{-1/2} |I|^{1/2}                         (C.4)

in that chamber. The TW puncture has disappeared from the L2 cost without being deleted from the form and without conditioning on T or W.

Lemma B similarly gives

    boxed: H_{1/2}(Q)
      := sup_t E|Q-t|^{-1/2}
      <= 2^(11/4) (kappa sqrt(q))^{-1/2}
      <= 2^(11/4) (s sqrt(q))^{-1/2}.                             (C.5)

This is a genuinely overlap-safe fractional receiver for the whole punctured form.

## Sign-specific one-sheet payment from the required pinned e5 source

The completed ruled-level-set Theorem C in math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837 applies to the same exact rank-three matrix. After scaling by s:

- signature (+,+,-): p_Q(t) <= pi sqrt(2)/s for t>=0;
- signature (+,-,-): p_Q(t) <= pi sqrt(2)/s for t<=0.

This is a real inequality on the r45 survivor, not an X-ray claim on the opposite side. The live QFORM-TWOSHEET-XRAY-ONLY-FALSE correction forbids extending it to the remaining two-sheet side.

## First unpaid implication sharpened

The puncture is now paid uniformly at the L2 and half-Riesz levels. What remains is not a same-bank-shear stability problem at those levels. It is the genuinely stronger endpoint

    QFORM-R45-TWOSHEET-L2-TO-LINFINITY-THIRD-CURVATURE-v1:

use the quantitative third curvature in (C.1), together with the fact that (T,W,V) is an orthonormal projection of a product source, to upgrade (C.2)/(C.5) to a uniform L-infinity bound on the opposite two-sheet side. A proof based only on the L2 estimate cannot work: the pure rank-two hyperbola saturates Lemma A yet has a logarithmically unbounded density. The third direction must therefore enter at the upgrade step, not by pretending the rank-two receiver was already bounded.
