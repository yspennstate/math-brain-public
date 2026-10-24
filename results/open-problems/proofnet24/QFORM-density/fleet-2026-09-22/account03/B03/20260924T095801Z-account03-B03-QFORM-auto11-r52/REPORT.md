SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B03, 2026-09-24T09:58:01Z.
attacking: zero-pivot determinant completion for a dependent same-bank pair plus one independent scalar; absorb arbitrary same-bank quadratic baggage into the square-hyperbola compiler and recover the whole-copy weighted time estimate.

# account03/B03 r52 — zero-pivot determinant completion

Status: **new supporting theorem proved; full QFORM OPEN; full-target continuity OPEN; WITHOUT_VERIFIED_BRAIN**.

## 1. Scope and corrections retained

The owner target remains: for independent real original-coordinate inputs with densities bounded by one and real symmetric A having at least three eigenvalues of modulus at least one, prove a universal essential L-infinity bound for the density of X^T A X, or produce a valid counterexample. No Gaussian, moment, compact-support, log-concavity, connected-support or post-rotation independence hypothesis is used here.

This run explicitly avoids the live refuted interfaces: no pointwise quadratic van-der-Corput bound, no independence of X-X' and X+X', no conditional cap for conjugate sum/difference variables, no arbitrary-joint 3D coarea lemma, and no positive conditional projection-density moment.

## 2. Main analytic lemma: arbitrary same-bank shear and baggage

### Theorem `QFORM-SAMEBANK-SHEAR-BAGGAGE-HYPERBOLIC-v1`

Let (S,R) be a real pair with joint probability density g satisfying ||g||_infinity <= M. Let V be independent of (S,R), with probability density h satisfying ||h||_infinity <= N. Let a,b be nonzero reals. Let G,H be arbitrary measurable real functions for which the displayed random variable is well-defined. Then

    Q = a (S+G(R))^2 + 2 b R V + H(R)

has an essentially bounded density and

    ||p_Q||_(infinity,ess)
      <= 6 M^(2/3) N^(2/3) |a|^(-1/3) |b|^(-2/3).        (2.1)

Translations of S,R,V and an additive constant are included at no cost.

### Proof

First replace S by S+G(R). The triangular map (s,r) -> (s+G(r),r) has Jacobian one, so the transformed pair still has joint density cap M. Thus it suffices to treat

    Q = a S^2 + 2 b R V + H(R).

Fix z in R and split at a parameter delta>0.

**Far region |R|>delta.** Conditional on (S,R)=(s,r), the map v -> a s^2 + 2 b r v + H(r) is affine with slope 2br. Hence its conditional density is at most N/(2|b r|). Averaging gives

    p_far(z) <= N/(2 |b| delta).                              (2.2)

**Near region |R|<=delta.** For fixed r and v, integration in s against the cap g(s,r)<=M gives the square-root kernel

    integral g(s,r) delta_z(a s^2 + c) ds
      <= M |a|^(-1/2) |z-c|^(-1/2),

where c=2brv+H(r), with the standard convention that the right side is +infinity at c=z. Therefore

    p_near(z)
      <= M |a|^(-1/2)
         integral_{|r|<=delta} E |z-H(r)-2brV|^(-1/2) dr.    (2.3)

If a scalar Y has probability density bounded by K, then for every u

    E |Y-u|^(-1/2) <= 2 sqrt(2K).                            (2.4)

Indeed the extremal cap-K probability density for the decreasing kernel |x|^(-1/2) is K times the indicator of the centered interval of length 1/K, giving exactly 2 sqrt(2K).

For fixed r!=0, the variable 2brV has density cap N/(2|br|). Applying (2.4) yields

    E |z-H(r)-2brV|^(-1/2)
      <= 2 sqrt(N/(|b r|)).                                  (2.5)

Substitution in (2.3), using integral_{-delta}^{delta}|r|^(-1/2)dr=4 sqrt(delta), gives

    p_near(z)
      <= 8 M sqrt( N delta / (|a b|) ).                      (2.6)

Combining (2.2) and (2.6),

    p_Q(z)
      <= A sqrt(delta) + B/delta,
    A = 8 M sqrt(N/(|ab|)),
    B = N/(2|b|).

The minimum occurs at delta^(3/2)=2B/A. Using

    min_{delta>0}(A sqrt(delta)+B/delta)
      = 3*2^(-2/3) A^(2/3) B^(1/3),

one obtains exactly (2.1). This proves essential boundedness. No continuity claim is made. QED.

## 3. Determinant completion for every invertible 2+1 zero-pivot quadratic

### Theorem `QFORM-2PLUS1-ZEROPIVOT-DETERMINANT-v1`

Let Y=(Y_1,Y_2) have arbitrary joint probability density bounded by M. Let V be independent of Y with density bounded by N. Let

    B = [[A,c],[c^T,0]]

be any real symmetric invertible 3x3 matrix, with A symmetric 2x2 and c in R^2. For arbitrary affine vector ell and constant d, set

    Q = (Y,V)^T B (Y,V) + ell^T (Y,V) + d.

Then Q has an essentially bounded density satisfying the determinant-homogeneous estimate

    ||p_Q||_(infinity,ess)
      <= 6 M^(2/3) N^(2/3) |det B|^(-1/3).                  (3.1)

### Proof

Because B is invertible and its scalar pivot is zero, c!=0. Apply an orthogonal change only inside the two-dimensional Y-bank, preserving the joint density cap M, so that c=(0,b) with b=||c||>0. In the resulting coordinates write

    A = [[a,e],[e,k]].

A direct determinant expansion gives

    det B = -a b^2.                                           (3.2)

Thus invertibility forces a!=0.

Write the affine quadratic explicitly:

    Q = a S^2 + 2eSR + kR^2 + 2bRV
        + l_S S + l_R R + l_V V + d.

Complete the square in S:

    a S^2 + 2eSR + l_S S
      = a ( S + (e/a)R + l_S/(2a) )^2 + H_0(R)

for a quadratic H_0. Next translate R by alpha=l_V/(2b), so that 2bRV+l_VV becomes 2b R_new V; all other terms remain of the form arbitrary H(R_new) plus an arbitrary shear inside the square. Theorem 2 applies and gives

    ||p_Q||_infinity
      <= 6 M^(2/3)N^(2/3)|a|^(-1/3)b^(-2/3)
      = 6 M^(2/3)N^(2/3)|det B|^(-1/3)

by (3.2). QED.

This theorem is materially stronger than the previous r51 packet: the entire same-bank quadratic baggage kR^2+2eSR, all affine terms, and arbitrary measurable R-baggage are retained exactly. The only structural condition is a genuinely zero scalar pivot for the independent third source and invertibility of the resulting 3x3 scalar matrix.

## 4. Product-projection specialization

If (S,R) is an orthonormal two-dimensional projection of one cap-one product bank, the standard two-dimensional product-projection estimate gives M<=2. If V is a genuine original physical coordinate, N<=1. Hence every invertible zero-pivot scalar matrix B in this 2+1 architecture satisfies

    ||p_Q||_(infinity,ess)
      <= 6*2^(2/3) |det B|^(-1/3).                           (4.1)

If instead V is a normalized one-dimensional projection of a disjoint product bank, use N<=sqrt(2), giving the convenient universal form

    ||p_Q||_(infinity,ess) <= 12 |det B|^(-1/3).             (4.2)

The transformed two coordinates in the same bank are not declared independent; only their joint density cap is used.

## 5. Whole-copy decoupled time integral

Let Q' be an independent copy of the whole scalar output Q and H=||p_Q||_(infinity,ess). Convolution gives ||p_(Q-Q')||_infinity<=H. For any probability density p<=H,

    integral |x|^(-1/2)p(x)dx <= 2 sqrt(2H).                 (5.1)

Using the scalar independent-copy identity only at the whole-output level,

    |phi_Q(t)|^2 = E exp(it(Q-Q')),

and the Fourier-Riesz identity

    integral_R |t|^(-1/2) exp(itx) dt = sqrt(2pi)|x|^(-1/2)

in the standard distributional/monotone regularization sense, one gets

    integral_R |t|^(-1/2)|phi_Q(t)|^2 dt
      <= 4 sqrt(pi H).                                        (5.2)

Combining with (3.1),

    integral |t|^(-1/2)|phi_Q(t)|^2 dt
      <= 4 sqrt(6pi) M^(1/3)N^(1/3)|det B|^(-1/6).           (5.3)

No X-X' variable is ever separated from its conjugate X+X'.

## 6. Strict target-valid nontrivial-baggage test

Take an orthonormal same-bank pair S,T and a disjoint physical scalar V, and let

    B_* = [[3,2,0],[2,5,3],[0,3,0]],
    Q_* = 3S^2 + 4ST + 5T^2 + 6TV.

Then det B_*=-27 and its characteristic polynomial is

    p(lambda)=lambda^3-8lambda^2+2lambda+27.

One has

    p(-2)=-17, p(-1)=16,
    p(2)=7,    p(3)=-12,
    p(7)=-8,   p(8)=43.

Since B_* is symmetric, its three real eigenvalues lie in (-2,-1), (2,3), (7,8). Thus all three have modulus >1, so this is a literal target instance with genuinely nonzero same-bank baggage.

For an orthonormal two-dimensional product projection M<=2 and physical V with N<=1, (3.1) gives

    ||p_(Q_*)||_(infinity,ess)
      <= 6*2^(2/3)*27^(-1/3)
      = 2*2^(2/3)
      = 3.1748021039363987... .                               (6.1)

Hence every interval I satisfies

    P(Q_* in I) <= 3.174802103936399 |I|.

The corresponding assigned time estimate is

    integral |t|^(-1/2)|phi_(Q_*)(t)|^2 dt
      <= 12.632614909877057... .                              (6.2)

## 7. Required partner application: account04/B03 r4

Use the same physical frame as in r51,

    s=(1/sqrt2,1/sqrt2,0,0),
    t=(1/sqrt6,-1/sqrt6,2/sqrt6,0),
    v=e_4.

Its only nonzero squared 3x3 Plucker weights are

    w_124=w_134=w_234=1/3.

For H={1,4}, q_H=2/3 and r_H=2/9. The newest completed account04/B03 r4 theorem gives

    J_2(H)=Delta^2(q_H^2-r_H),

with Delta=|det B_*|=27, hence

    J_2(H)=27^2*(2/9)=162.

Applying its completed density inequality at the literal equation,

    ||p_(Q_*)||_(infinity,ess)
      <= 129.924435862525374 * 162^(-1/6)
      = 55.64656197133566... .                                (7.1)

The present theorem improves the constant on this zero-pivot target, but (7.1) is an actual equation-level use of the designated partner result.

The partner density bound also implies, through the same whole-copy conversion (5.2),

    integral |t|^(-1/2)|phi_(Q_*)(t)|^2 dt
      <= 52.88762884254536... .                               (7.2)

Partner source: `yspennstate/math-open-problems@5f93186cf8952b2b8b0255e08a78fd8506c613e4`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B03/20260924T051411Z-account04-B03-plucker-overlap2-r4/REPORT.md`.

## 8. Boundary and next implication

This run pays **every invertible 2+1 scalar packet with a genuinely independent zero-diagonal third source**, even with arbitrary quadratic and affine baggage on the dependent same-bank pair. It proves essential boundedness and linear small-ball scaling in that scope. It does not prove continuity.

The unrestricted three-large-eigenvalue conjecture remains OPEN. The next structural implication is now sharper: in any remaining heavy-hub / near-rank-two survivor, either expose a product-preserving 2+1 scalar reduction with a zero (or perturbatively controllable) physical pivot and determinant bounded below, or route the geometry into one of the already-paid E3/balanced-carrier/grouped receivers. A small but nonzero independent scalar square is not covered by Theorem 3 without an additional argument; it must not simply be deleted.
