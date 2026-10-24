# Exact conditional-fiber obstruction for an isotropic simplex

Author: w354. Date: 2026-10-10. Status: author-proved special case; independent audit pending. Source tag: owner-own-work (campaign proof, no novelty claim).

## Statement

For every integer d>=2 there is a centered isotropic log-concave probability mu_d on R^d and a unit vector v such that, for Z=Proj_(v-perp)Y and T=<v,Y>, the conditional laws T|Z are uniform intervals and

    ess sup C_P(T|Z) = 2(d+1)(d+2)/pi^2,
    E C_P(T|Z) = 12/pi^2,
    ess inf h(T|Z) = sqrt(2/((d+1)(d+2))).

All essential extrema use the law of Z, not exceptional zero-probability fibers. In fact, on an event of probability (d+1)/2^d,

    C_P(T|Z) >= (d+1)(d+2)/(2 pi^2).

Furthermore the optimal constant in

    E Var(f(Y)|Z) <= C E |partial_v f(Y)|^2

over locally Lipschitz f with finite energies is exactly 2(d+1)(d+2)/pi^2. Thus replacing the conditional constants by their arithmetic mean 12/pi^2 in this inequality is false. This does not contradict the ordinary Poincare inequality, whose right side contains the full gradient.

## 1. Distribution and exact covariance

Let X be uniform on Delta_d={x_i>=0, sum_i x_i<=1}. Write m=(1,...,1)/(d+1), J for the d-by-d all-ones matrix, and K=(d+1)(d+2). Direct integration, equivalently the elementary simplex moment formula, gives

    E X_i=1/(d+1),
    E X_i^2=2/((d+1)(d+2)),
    E X_i X_j=1/((d+1)(d+2)) for i!=j.

For completeness, that formula is obtained by repeatedly integrating monomials over the simplex: for nonnegative integers k_i, its normalized integral is d! product_i(k_i!)/(d+sum_i k_i)!. Applying it at degrees one and two gives these values.

Consequently

    Sigma=Cov(X)=(I-J/(d+1))/K,
    Sigma^(-1)=K(I+J).

The inverse identity follows from J^2=dJ. Sigma is positive definite (its eigenvalues are 1/K on the orthogonal complement of the all-ones vector and 1/((d+1)K) on that vector). Let A=Sigma^(-1/2), Y=A(X-m), a=|Ae_1|=sqrt(2K), and v=Ae_1/a. Then E Y=0 and Cov(Y)=I. An invertible affine image of uniform measure on a convex simplex remains log-concave.

## 2. Orthogonal conditioning really fixes the other raw coordinates

Let P be orthogonal projection onto v-perp. The linear map PA has kernel span(e_1), since A is invertible and A e_1 is parallel to v. Its restriction to span(e_2,...,e_d) is injective and maps onto v-perp. Therefore fixing Z=P A(X-m) is exactly equivalent to fixing (X_2,...,X_d); this is a genuine orthogonal disintegration in isotropic coordinates, not an arbitrary oblique slice.

Put S=sum_(j=2)^d X_j. Conditional on the latter coordinates, X_1 is uniform on [0,1-S]. A constant Jacobian from the affine transformation does not change this conditional distribution. Moreover

    T=<v,Y> = e_1^T A^2(X-m)/a
              = K(2 X_1+S-1)/a
              = a (X_1-(1-S)/2).

Hence T|Z is uniform on [-a(1-S)/2, a(1-S)/2]. Its conditional mean is zero, and its Euclidean length is L(S)=a(1-S).

## 3. Exact one-dimensional constants and positive-probability tails

Uniform measure on an interval of length L has C_P=L^2/pi^2, Var=L^2/12 and h=2/L. The Neumann sine or cosine of frequency pi/L gives equality in Poincare; the Fourier expansion proves the upper bound. The half interval realizes h; any nontrivial finite-perimeter set has an interior boundary point and therefore ratio at least 2/L.

The density of S is d(d-1)s^(d-2)(1-s), 0<s<1. To derive it, the (d-2)-dimensional section volume for the d-1 fixed coordinates contributes s^(d-2)/(d-2)!, and integrating X_1 contributes (1-s); multiplying by d! gives the density. Thus S has Beta(d-1,2) law. It has positive density at every 0<s<1, so

    ess sup C_P = a^2/pi^2 = 2K/pi^2,
    ess inf h = 2/a = sqrt(2/K).

These are essential extrema even though the maximizing edge S=0 has probability zero: every neighborhood 0<S<epsilon has positive probability. The second residual-length moment is

    E (1-S)^2 = 6/K.

For example this follows by integrating d(d-1)s^(d-2)(1-s)^3 using the integer beta integral. Therefore E C_P=12/pi^2 and E Var(T|Z)=1. The latter agrees with Var(T)=1 because E(T|Z)=0. Finally direct integration up to 1/2 gives

    P(S<=1/2)=d/2^(d-1)-(d-1)/2^d=(d+1)/2^d.

On this event L>=a/2 and C_P>=K/(2 pi^2).

## 4. Averaging constants cannot be separated from test-function energy

Fiberwise Poincare and Fubini give

    E Var(f(Y)|Z) <= E [C_P(T|Z) E(|partial_v f(Y)|^2|Z)]
                         <= (a^2/pi^2) E |partial_v f(Y)|^2.

The first expression is the valid weighted inequality. There is no general inequality allowing the two factors inside its expectation to be separated.

For the matching lower bound, fix 0<epsilon<1. Choose a nonzero smooth eta supported on (epsilon/4,epsilon/2), and define on the simplex

    f(Y)=eta(S) sin(pi T/(a(1-S))).

This is locally Lipschitz with finite full gradient energy: on its support the denominator is bounded away from zero; elsewhere it extends by zero. It may also be extended smoothly to a neighborhood using a harmless smooth denominator cutoff outside the support. Since S is a function of Z, partial_v S=0; partial_v T=1. On each fiber the sine has mean zero and squared mean 1/2. Therefore

    E Var(f|Z)=(1/2) E eta(S)^2,
    E |partial_v f|^2=(pi^2/(2a^2)) E [eta(S)^2/(1-S)^2].

The quotient of these expressions is at least a^2(1-epsilon)^2/pi^2, since S<epsilon on the support. The support has positive probability by the strictly positive S density. Letting epsilon decrease to zero proves that the optimal directional conditional constant is a^2/pi^2, as claimed.

The factor by which the optimal directional constant exceeds the arithmetic mean of the fiber constants is exactly K/6. Orthogonal derivatives of eta are part of the full gradient and were not controlled in this construction. Omitting them would falsely suggest a KLS counterexample.

## 5. Explicit polynomial witness

The mean replacement already fails for a polynomial on an isotropic triangle, so it does not depend on an extreme limiting test function. More generally, let t=1-S and f(Y)=T t^k for any integer k>=0. The gradient b=grad_Y S has b perpendicular to v and

    |b|^2=2(d-1)/((d+1)K).

Indeed b=A^(-1)(0,1,...,1), so its squared norm is the quadratic form of Sigma at that raw vector. Since the conditional mean of T is zero, the mean of f is zero. The beta density gives E t^p=(p+1)! d!/(d+p)!. Consequently the directional Rayleigh quotient is exactly

    R_(d,k) = (K/6) (2k+2)(2k+3)/((d+2k+1)(d+2k+2)).

The full energy has the additional orthogonal term: grad f=v t^k-k T t^(k-1)b, whose cross term is zero. Its expectation is E t^(2k) times [1+k^2(d-1)/(3(d+1))]. Thus the full-gradient Rayleigh quotient is

    R_(d,k) / [1+k^2(d-1)/(3(d+1))].

For d=2, k=2, the variance is 1/2, directional energy 1/3, and full energy 13/27. The proposed mean-fiber inequality reads 1/2<=4/pi^2, false since pi>3. The full-gradient quotient is 27/26. This is an explicit smooth counterexample to the auxiliary directional averaging step, with the extra orthogonal energy accounted for exactly.

## What remains for a complete target proof by this route

The full target needs a universal estimate using the full gradient, with arbitrary dependence between orthogonal coordinates. This construction supplies no such estimate. The single hardest gap in this worker's conditional route is controlling the correlation between conditional fiber constants and localized directional energy using the orthogonal part of the energy. Uniform fiber bounds and simple averaging are both unavailable. Recent primary papers claim another route to the full target; their proofs are not audited here.
