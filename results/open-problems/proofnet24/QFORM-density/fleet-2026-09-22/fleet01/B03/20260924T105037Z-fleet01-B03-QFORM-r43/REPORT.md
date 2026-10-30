SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B03, 2026-09-24T10:50:37Z.
attacking: a cross-hub/shared-environment bridge — splice the partner's pivot-uniform twisted hyperbolic collision estimate with a two-dimensional physical slope hub before any conditional density is formed, and force an L1 characteristic-function bound.

# fleet01/B03 r43 — twisted bilinear pair plus shared-environment slope hub

## Status

**NEW SUPPORTING THEOREM / NEW LINEAR SMALL-BALL BRANCH / DESIGNATED PARTNER APPLIED / STRICT OWNER-TARGET EXAMPLE / FULL QFORM OPEN.**

The unrestricted quadratic-form bounded-density conjecture remains open. The unrestricted continuous-density conclusion also remains open. This report proves a new product-coordinate branch with a continuous C0 density and a universal linear small-ball estimate in its stated scope.

Execution label: `WITHOUT_VERIFIED_BRAIN`. Repository retrieval and publication were used; no native learned-memory receiver use is asserted.

## 1. Live corrections respected

This argument does **not** use any of the following refuted interfaces:

1. no pointwise law-uniform van-der-Corput decay for a quadratic phase;
2. no claim that conditioning on one member of an independent-copy sum/difference pair preserves a density cap;
3. no post-rotation probabilistic independence;
4. no arbitrary-joint three-dimensional coarea bound;
5. no positive conditional projection-density moment;
6. no reversal of finite whole-output collision energy into an L-infinity density bound.

The only Plancherel steps below are taken in genuine independent physical variables or in a marginal slope variable with an explicitly assumed marginal density cap.

## 2. Partner input actually used

The newest completed designated partner result available at publication is fleet02/B03 r54:

`yspennstate/math-open-problems@434585cef13aebbe1d21612b43f46c760fb5344a`

path

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B03/20260924T101139Z-fleet02-B03-QFORM-auto11-r54/REPORT.md`.

Its lemma `QFORM-TWISTED-HYPERBOLIC-COLLISION-v1` states the following. Let R have scalar density cap L. Let V be independent of the entire source containing R and have density cap N. Let F be any real random variable measurable with respect to the source containing R, with arbitrary dependence on R. For beta != 0 and arbitrary real c,d,

    T = F + 2 beta R V + c V^2 + d V

obeys, for t != 0,

    |phi_T(t)|^2 <= min{1, pi L N / (|beta| |t|)}.          (2.1)

The proof is source-preserving: cV^2+dV is a modulus-one twist inside the V-Plancherel integral. In the theorem below this estimate is used pointwise after conditioning on a shared environment, so it remains uniform in all environment-dependent coefficients.

## 3. New theorem: twisted bilinear pair plus a k-dimensional shared-environment slope hub

### Theorem `QFORM-B03-TWISTED-PAIR-SLOPE-HUB-v1`

Let k >= 2. Let R and V be independent real random variables with densities bounded by L and N, respectively. Let

    U = (U_1,...,U_k)

be a block of genuine independent physical coordinates, independent of (R,V), with each scalar density bounded by one. Let Y be an arbitrary random environment independent of (R,V,U).

Let

    ell(Y) in R^k

have a marginal Lebesgue density bounded by K. The coordinates of ell(Y) need not be independent and ell may be arbitrarily dependent on every other function of Y appearing below.

Let C be an arbitrary deterministic symmetric k x k matrix. Let F(r,y), c(y), d(y), H(y) be arbitrary measurable real functions for which the displayed expectations exist; no regularity, moment, compact-support, connected-support, or sign assumptions are imposed. Fix beta != 0. Define

    Q = F(R,Y)
        + 2 beta R V
        + c(Y) V^2 + d(Y) V
        + U^T C U + 2 U^T ell(Y)
        + H(Y).                                             (3.1)

Put

    a = L N K / |beta|,
    D = k+1.

Then for every t != 0,

    boxed:
    |phi_Q(t)|
      <= min{1, pi^(D/2) a^(1/2) |t|^(-D/2)}.              (3.2)

Equivalently,

    boxed:
    |phi_Q(t)|^2
      <= min{1, pi^D a |t|^(-D)}.                          (3.3)

Consequently phi_Q belongs to L1(R) and Q has a continuous density p_Q vanishing at infinity, with

    boxed:
    ||p_Q||_infinity
      <= D/(D-2) * a^(1/D).                                (3.4)

Thus for every interval I,

    boxed:
    P(Q in I)
      <= D/(D-2) * a^(1/D) |I|.                            (3.5)

The assignment-specific whole-output negative-half time integral also satisfies

    boxed:
    A_-(Q)
      := integral_R |t|^(-1/2)|phi_Q(t)|^2 dt
      <= [8D/(2D-1)] sqrt(pi) a^(1/(2D)).                  (3.6)

In the critical k=2, D=3 case,

    boxed:
    ||p_Q||_infinity <= 3 (L N K / |beta|)^(1/3),          (3.7)

and

    boxed:
    A_-(Q)
      <= (24/5) sqrt(pi) (L N K / |beta|)^(1/6).           (3.8)

### Proof

Fix t != 0 and condition only on the genuine environment Y=y. Define the pair amplitude

    A_y(t)
      = E_{R,V} exp(it[ F(R,y)
                         + 2 beta R V
                         + c(y)V^2+d(y)V ]).               (3.9)

For each fixed y, fleet02/B03 r54 applies with the same caps L,N and the same beta; y merely freezes the coefficients. Hence

    |A_y(t)|^2 <= pi L N/(|beta||t|),                      (3.10)

uniformly in y. No conditional law of R or V given Y changes because Y is source-independent of (R,V).

Now define the k-dimensional physical hub transform

    B_t(z)
      = E_U exp(it[ U^T C U + 2 U^T z ]).                 (3.11)

Write g(u)=prod_{j=1}^k f_j(u_j). Then

    B_t(z)
      = integral exp(it u^T C u) exp(i 2t u.z) g(u) du.   (3.12)

With the convention hat h(xi)=integral exp(i xi.u)h(u)du, Plancherel gives

    integral_R^k |B_t(z)|^2 dz
      = (2|t|)^(-k)(2pi)^k
        integral_R^k |g(u)|^2 du
      = pi^k |t|^(-k) integral |g(u)|^2 du.                (3.13)

Because each f_j is a probability density with 0<=f_j<=1,

    integral |g|^2
      = product_j integral f_j^2
      <= 1.                                                (3.14)

Since ell(Y) has marginal density at most K,

    E_Y |B_t(ell(Y))|^2
      <= K pi^k |t|^(-k).                                  (3.15)

The key point is that no conditional density of ell(Y) given any other environment statistic is formed.

Independence of the physical source blocks gives the exact conditional factorization

    phi_Q(t)
      = E_Y [ exp(itH(Y)) A_Y(t) B_t(ell(Y)) ].            (3.16)

Therefore, by Cauchy-Schwarz only on the final marginal Y-average,

    |phi_Q(t)|
      <= sup_y |A_y(t)|
         (E_Y |B_t(ell(Y))|^2)^(1/2)                       (3.17)

and (3.10),(3.15) imply

    |phi_Q(t)|
      <= pi^((k+1)/2)
         (L N K/|beta|)^(1/2)
         |t|^(-(k+1)/2).                                   (3.18)

Together with |phi_Q|<=1 this proves (3.2)-(3.3).

For completeness, set

    C0 = pi^(D/2) a^(1/2),
    T  = C0^(2/D) = pi a^(1/D).                            (3.19)

Then

    integral_R |phi_Q(t)| dt
      <= 2[ T + C0 integral_T^infinity t^(-D/2)dt ]
      = 2 pi [D/(D-2)] a^(1/D).                            (3.20)

Fourier inversion therefore produces a continuous C0 density and

    ||p_Q||_infinity
      <= (1/(2pi)) integral |phi_Q|
      <= D/(D-2) a^(1/D),                                  (3.21)

which is (3.4)-(3.5).

For the weighted whole-output integral, put

    G = pi^D a,
    T2 = G^(1/D) = pi a^(1/D).                             (3.22)

Using (3.3),

    A_-(Q)
      <= 2 integral_0^T2 t^(-1/2)dt
       + 2G integral_T2^infinity t^(-D-1/2)dt
      = 4 sqrt(T2) + 4 sqrt(T2)/(2D-1)
      = [8D/(2D-1)] sqrt(pi) a^(1/(2D)),                   (3.23)

which proves (3.6). QED.

## 4. Independent-copy interpretation

The proof of the density bound does not need to break an independent copy into coordinatewise sums and differences. The assigned independent-copy identity is used only in its safe whole-scalar form

    |phi_Q(t)|^2 = E exp(it(Q-Q')),                        (4.1)

where Q' is an independent copy of the complete scalar output Q.

Thus (3.6) is a genuine dependence-safe decoupled time-integral estimate. No coordinate pair `(X_i-X_i', X_i+X_i')` is separated or conditionally re-capped. The linear small-ball conclusion is obtained from the stronger L1 characteristic-function estimate (3.20), not by reversing finite collision energy.

Under the programme's regularized Riesz normalization,

    A_-(Q) = sqrt(2pi) E |Q-Q'|^(-1/2),                   (4.2)

so (3.6) also yields

    E|Q-Q'|^(-1/2)
      <= [4 sqrt(2) D/(2D-1)] a^(1/(2D)).                 (4.3)

For D=3 this is `(12sqrt(2)/5)a^(1/6)`.

## 5. Actual designated-partner splice at an inequality

At k=2, use fleet02/B03 r54 on the pair factor after fixing Y:

    |A_y(t)|^2 <= pi L N/(|beta||t|).                     (5.1)

The two-dimensional physical hub Plancherel estimate is

    E_Y |B_t(ell(Y))|^2 <= pi^2 K |t|^(-2).               (5.2)

Equations (5.1)-(5.2) enter the same Cauchy-Schwarz line and give

    boxed:
    |phi_Q(t)|^2
      <= pi^3 [L N K/|beta|] |t|^(-3).                    (5.3)

Thus the partner's pivot-uniform `|t|^-1` whole-pair collision gain has been converted into an integrable one-copy `|t|^-3/2` characteristic-function envelope by a disjoint two-dimensional physical slope hub, even when the environment generating the pair twists is exactly the same environment generating the hub slope.

This is an actual new implication rather than a citation-only splice.

## 6. Strict exact-target example with maximally shared environment

Take six independent cap-one physical coordinates

    R, V, U1, U2, Y1, Y2

and define

    Q = 2 R V
        + 2 R Y2
        + 2 V Y1
        + 2 U1 Y1
        + 2 U2 Y2.                                        (6.1)

Apply the theorem with

    beta=1,
    F(R,Y)=2 R Y2,
    c(Y)=0,
    d(Y)=2Y1,
    U=(U1,U2),
    ell(Y)=(Y1,Y2),
    C=0,
    H=0.                                                   (6.2)

Because Y1,Y2 are independent cap-one physical variables, their joint density has cap K<=1; also L,N<=1. The same environment `(Y1,Y2)` appears simultaneously in the bilinear-pair twist and the two-dimensional hub slope, so the source overlap is maximal at the environment level.

Therefore

    boxed: ||p_Q||_infinity <= 3,                          (6.3)
    boxed: P(Q in I) <= 3 |I|,                            (6.4)

and p_Q is continuous and vanishes at infinity. Moreover

    boxed:
    A_-(Q) <= (24/5)sqrt(pi)
            = 8.507778484346476... .                       (6.5)

The coefficient graph is the path P6 if the variables are ordered

    U1 -- Y1 -- V -- R -- Y2 -- U2.                        (6.6)

Hence the six eigenvalues are exactly

    2 cos(j pi/7),  j=1,...,6,                            (6.7)

namely approximately

    +/-1.8019377358,
    +/-1.2469796037,
    +/-0.4450418679.                                      (6.8)

Thus four eigenvalues have absolute value greater than one. This is a strict instance of the owner's full target, not an easier below-threshold control family.

## 7. What this changes and what remains unpaid

The previous fleet01/B03 r42 theorem paid two physical hub groups with arbitrarily overlapping slope sources only when there was no deterministic quadratic cross term between the physical groups. The present theorem introduces a genuine deterministic scalar bilinear cross hub `2 beta R V` and shows that its partner-proved collision gain can be multiplied with a two-dimensional physical slope-hub Plancherel gain **before** any conditional density is formed.

What remains open is the fully general deterministic cross-hub matrix. In particular, if the same physical variables entering the twisted bilinear pair also couple quadratically to U, then after conditioning on Y the factorization (3.16) is lost. A naive conditioning of the resulting U-dependent slope would reintroduce exactly the conditional-density interface prohibited by the correction corpus.

The next analytic mechanism should therefore attempt an operator-valued or iterated Plancherel estimate for

    2 beta R V + 2 R a.U + 2 V b.U + U^T C U             (7.1)

while retaining all genuine physical sources until their L2 gains are taken. If such an estimate cannot be made determinant/rank quantitative without reciprocal-small-coefficient loss, the structural route must extract the present scalar-pair-plus-two-hub packet or send the survivor to an already-paid grouped-hub/ridge/principal-pair branch.

Full universal boundedness: **OPEN**.
Full-target continuity: **OPEN**.

## 8. Source/control snapshot used


No task, schedule, enabled/paused state, email/push notification, permission, installation, cross-account authentication, paid API/model call, remote workflow, or public-release setting was changed in this run.
