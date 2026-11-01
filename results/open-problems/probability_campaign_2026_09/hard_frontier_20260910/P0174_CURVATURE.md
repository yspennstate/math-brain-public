# Sharp mode curvature after free Brownian smoothing

Author derivation, 10 September 2026. This continues P0174 after the owner retired the Cayley/cutoff line. The diameter threshold was already a checked candidate in the campaign; the sharp mode-curvature estimate below is a further result derived here. Neither statement is being counted as a novelty-certified publication. Numerical controls are supplementary, not a proof for all measures.

Let mu be a compactly supported probability measure on the real line. Write D for its support diameter and S(0,t) for the centered semicircle law of variance t, with density sqrt(4t-x^2)/(2 pi t).

## The statements

1. The law mu boxplus S(0,t) is unimodal for t >= D^2. The constant 1 is optimal. This is the campaign's P0174 answer to Hasebe-Ueda Problem 3.3.
2. For t > D^2, its density p_t has a unique mode m_t and

       p_t''(m_t) <= -(t-D^2) / [4 pi (t-D^2/4)^(5/2)].

   The estimate is sharp for every t > D^2. If D>0, equality holds exactly for translates of the equally weighted law on {-D/2,D/2}. If D=0, the input is a point mass and equality is the elementary semicircle calculation.
3. At t=D^2>0, zero second derivative at the mode occurs only for that symmetric two-point law. Its mode remains strict; the first nonconstant local term is quartic.

The new part of this packet is statement 2 and its optimality, together with the quantitative use of the tilted moment constraints. It is a bound for the density in the physical x coordinate, not for the auxiliary parameter u.

## 1. The only free-probability input

Use Biane's semicircle-convolution parametrization, as stated in Hasebe-Ueda Section 2.2. For u in the positivity domain, v=v_t(u)>0 is the unique solution of

    F(u,v) = integral [(u-x)^2+v^2]^(-1) mu(dx) = 1/t.

The real map

    psi_t(u) = u + t integral (u-x)/[(u-x)^2+v_t(u)^2] mu(dx)

is increasing and satisfies p_t(psi_t(u))=v_t(u)/(pi t). The density is continuous and is analytic wherever positive. All derivatives used below are inside the positivity domain, where compact support and v>0 justify differentiating under the integral.

For t>=D^2 and D>0, the positivity domain is one interval containing the support of mu. Indeed, for u between the extreme support points, integral (u-x)^(-2) mu(dx)>1/D^2: all distances are at most D, and equality would force all mass onto a single opposite endpoint, contradicting positive diameter. Outside the support interval this integral is strictly monotone toward zero. The point-mass case is explicit.

## 2. Tilted moments and a stronger inequality

At a critical point of v_t, put y=v^2, z=u-x and

    Z = integral (z^2+y)^(-2) mu(dx),
    Q(dx) = Z^(-1)(z^2+y)^(-2) mu(dx),
    a = E_Q z^2,  b = E_Q z^4,  V=b-a^2,  M=a+y.

The critical-point condition is E_Q z=0. The tilted law has the same support diameter D as mu. Consequently

    0 <= a <= D^2/4,       0 <= V <= a(D^2-4a).

For the variance bound, center the support interval [l,h] and use E[(z-l)(h-z)]>=0. This gives a<=-lh<=D^2/4. For the fourth-moment bound, take an independent copy z':

    E(z-z')^4 = 2b+6a^2 <= D^2 E(z-z')^2 = 2D^2 a.

Subtract a^2 to obtain the bound on V. The Q normalization also gives the exact identities

    1/t = Z M,       t = M + V/M.

In particular,

    t <= y-3a+D^2 - y(D^2-4a)/(a+y) <= y-3a+D^2.       (1)

To check (1), write t=M+V/M, bound V by a(D^2-4a), and use

    D^2+y-3a-t = D^2-4a-V/M.

Thus t>D^2 implies y>3a at every critical point.

## 3. Qualitative threshold and its endpoint

At a critical point, direct differentiation gives

    F_uu/(2Z) = 3-4y E_Q[1/(z^2+y)]
              <= 3-4y/(a+y) = (3a-y)/(a+y),

where Jensen is used in the direction E[1/(z^2+y)]>=1/(a+y). Also F_v=-2vZ, so

    v_t''(u) = F_uu/(2vZ).

For t>D^2, (1) makes every critical point a strict local maximum. A positive continuous profile on one bounded positivity interval, vanishing at its endpoints, cannot have two maxima without an intervening local minimum. Hence it has one mode, and so does the density under the increasing map psi_t.

At t=D^2, a critical point with v_t''>=0 would require y<=3a. Inequality (1) then forces y=3a and 4a=D^2. Equality in the variance bound implies that Q is equally weighted on the two endpoints u+/-D/2. The two reweighting factors are equal, so mu is the same symmetric two-point law.

Write c=D/2. In this exceptional case,

    v_t(u)^2 = (t+sqrt(t^2+16c^2 u^2))/2-u^2-c^2

after translating the midpoint to zero. At t=4c^2 this is

    3c^2-u^4/(4c^2)+O(u^6),

a strict quartic maximum. There is no local minimum at the endpoint either. This completes the threshold statement, including t=D^2. Alternatively, the same calculation gives the Cauchy-profile level-crossing proof recorded in the original P0174 packet.

For c^2<t<4c^2, the symmetric two-point example instead has

    v_t''(0) = (4c^2-t)/(t sqrt(t-c^2)) > 0.

Its positive central minimum prevents unimodality. Every universal constant below 1 therefore fails.

## 4. Passing to the physical density coordinate

At a critical point,

    psi_t'(u) = 1+tZ(y-a) = 2y/M > 0.

Because v_t'=0 there, the chain rule has no additional psi_t'' term:

    p_t''(psi_t(u)) = v_t''(u) / [pi t (psi_t'(u))^2].

Set J=E_Q[1/(z^2+y)]. Combining the exact formulas gives

    -p_t''(psi_t(u))
      = (4yJ-3) M^2 / [4 pi t y^(5/2)]
      >= M(y-3a) / [4 pi t y^(5/2)].                    (2)

The factor (psi_t')^2 is essential. Omitting it would confuse the auxiliary curve with the actual density and would already give the wrong curvature for a point-mass input.

## 5. Exact optimization of the moment bound

For D>0, rescale space by D/2, so the normalized diameter is 2 and t>4. Curvature scales as length^(-3). In these units,

    0<=a<=1,       0<=V<=4a(1-a),       t=M+V/M,
    y=M-a,        M>4a.

It remains to prove

    B(a,M):=M(M-4a)/[t(M-a)^(5/2)]
        >= (t-4)/(t-1)^(5/2).                          (3)

The moment conditions imply

    M in [L(a),t],
    L(a) = (t+sqrt(t^2-16a(1-a)))/2.

Indeed, M^2-tM+4a(1-a)>=0. At M=4a this quadratic equals 4a(3a-t+1)<=0, so M>4a excludes the lower-root branch. The square root is real because t>4 and 16a(1-a)<=4.

For fixed a, the sign of the M derivative of B is the sign of

    -M^2+8aM+8a^2.

This polynomial is strictly decreasing for M>4a. It crosses at most once, from positive to negative. Thus B has no interior minimum on [L(a),t], and it suffices to examine its two endpoints.

**Endpoint M=t.** Here B=(t-4a)/(t-a)^(5/2), whose derivative with respect to a has numerator -(3/2)t-6a. It is strictly decreasing on [0,1], so its minimum is the right side of (3), attained at a=1.

**Endpoint M=L(a).** Equality V=4a(1-a) holds. Put r=a/M. Then

    M=(t-4r)/(1-4r^2),       0<=r<=1/t<1/4.

The bound r<=1/t follows exactly from a<=1 after this substitution. At this endpoint,

    B = (1-4r)sqrt(1-4r^2)
        / [t sqrt(t-4r)(1-r)^(5/2)].

Its logarithmic derivative is

    -4/(1-4r)-4r/(1-4r^2)+2/(t-4r)+5/[2(1-r)].

Since t>=4, the term 2/(t-4r) is at most 1/[2(1-r)]. The derivative is therefore at most

    -(1+8r)/[(1-4r)(1-r)] - 4r/(1-4r^2) < 0.

The minimum occurs at r=1/t, corresponding to a=1 and M=t, and again equals the right side of (3). This proves (3) on the entire feasible moment region.

Substitution into (2), followed by undoing the spatial scaling, proves

    -p_t''(m_t) >= (t-D^2)/[4 pi (t-D^2/4)^(5/2)].

## 6. Sharpness and equality

For the equally weighted law at +/-c, with t>4c^2,

    y=t-c^2,  a=c^2,  M=t,
    v_t''(0)=-(t-4c^2)/(t sqrt(t-c^2)),
    psi_t'(0)=2(t-c^2)/t.

Consequently

    p_t''(0)=-(t-4c^2)/[4 pi (t-c^2)^(5/2)],

which attains the estimate exactly. In the normalized optimization, equality requires a=1. The variance equality then forces Q to be the equal endpoint law, and equal reweighting factors force mu to be that same law. These are the only equality cases up to translation when D>0.

For D=0, p_t is a translated semicircle and p_t'' at its mode is -1/(4 pi t^(3/2)), again equality in the formula. At t=D^2>0, the argument in Section 3 proves the zero-curvature rigidity statement.

## Scope and literature

- Governing source: Hasebe and Ueda, *Large time unimodality for classical and free Brownian motions with initial distributions*, ALEA 15 (2018), 353-374, Section 2.2 and Problem 3.3. https://doi.org/10.30757/ALEA.v15-15
- The original campaign proof of C=1 is P0174_free_brownian_unimodality_constant_candidate.md. This packet does not count that established campaign candidate again.
- Biane's density parametrization is imported through the cited source; the weighted moments, optimization and physical-coordinate curvature calculation are proved above.
- The source's printed lower bracket 2<=C<=4 does not follow from its own variance-t, diameter-2 Bernoulli example. Its example gives C>=1. Our argument does not rely on the printed bracket.
- A recent anonymous candidate on closure of symmetric unimodal laws under free addition concerns a different input class. It is not a source for the arbitrary compact-input threshold or the mode-curvature estimate here.
- Novelty remains unconfirmed. No assertion of independent referee approval, complete Lean formalization, or journal acceptance is made for this new packet.

## Author controls completed

`check_free_curvature.py` passed five exact symbolic identities, 28 atomic-law/time cases at 80 decimal digits, and seven independent finite-difference checks in the physical density coordinate. The latter solve the two defining equations at nearby physical x values and do not use the curvature formula to produce their second differences. Equal two-point laws and point masses attain the proposed sharp bound in the controls. The immutable result record is `audits/evidence/2026/09/10/probability_publishability/p0174_curvature_controls.json` in the brain repository. These are checks of the derivation and its implementation; the proof for all compactly supported laws is Sections 1-6 above.
