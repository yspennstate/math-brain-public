# A lower bound for a two-eigenvalue form: Psi >= 0 for n >= 14

Status: candidate, one author. To be refereed.

## Setting

Let n >= 5 and x in R^n, x != 0, with x_1 + ... + x_n = 0. Put

    T = sum x_i^2,   P = sum x_i^3,   Q = sum x_i^4,
    q = Q / T^2,     p^2 = P^2 / T^3,
    m = max_(i<j) x_i x_j / T,
    C = (n-1)(n^2 - 6n + 6 + 2nq),
    Psi(x) = (n-4)(2q - 1) - 2(n-3) p^2 + C m.

Psi is homogeneous of degree 0 and invariant under permutations of the coordinates and under x -> -x.

For a real number M with M <= m T write

    G_M = (n-4)(2Q - T^2) T - 2(n-3) P^2 + (n-1)((n^2-6n+6) T^2 + 2nQ) M,

so that T^3 Psi = G_(mT) >= G_M (the coefficient of M is positive).

## Theorem

For every n >= 14 and every x in R^n, x != 0, with sum x = 0: Psi(x) >= 0.

## Proof

Step 1 (large m). The identity

    Psi = 2(n-3)(q - p^2 - 1/n) + C (m - 1/(n(n-1)))

holds. The Gram determinant of the three vectors (1, ..., 1), x, (x_i^2) equals n(TQ - P^2) - T^3 and is >= 0,
that is q - p^2 >= 1/n. Since C > 0, Psi >= 0 whenever m >= 1/(n(n-1)).

Normalisation. Sort x decreasingly, replace x by -x if x_1 + x_n < 0, and scale so that x_1 = 1. Then
x_1 = 1 >= b := -x_n > 0. Two cases:

  (I)  x_2 + x_(n-1) >= 0. Then eps := x_2 >= 0 (otherwise x_(n-1) <= x_2 < 0), the middle coordinates
       x_2, ..., x_(n-1) lie in [-eps, eps], and m T >= M := x_1 x_2 = eps.
  (II) x_2 + x_(n-1) <= 0. Then eps := -x_(n-1) >= 0 (otherwise x_2 >= x_(n-1) > 0), the middle coordinates lie in
       [-eps, eps], and m T >= M := x_n x_(n-1) = b eps.

In both cases let Y2, Y3, Y4 be the sums of the 2nd, 3rd, 4th powers of the middle coordinates. Then
Y2 <= (n-2) eps^2, T = 1 + b^2 + Y2, and delta := 1 - b = -(sum of the middle coordinates) lies in [0, (n-2) eps].

Step 2 (eps not small).
(I): T <= 2 + (n-2) eps^2, so M/T >= eps / (2 + (n-2) eps^2), and this is >= 1/(n(n-1)) as soon as
(n-2) eps^2 - n(n-1) eps + 2 <= 0. This convex quadratic is <= 0 at eps = e1 := 2.1/(n(n-1)) and at eps = 1,
hence on [e1, 1]. So Step 1 applies when eps >= e1.
(II): b >= max(eps, 1 - (n-2) eps), and b eps / (1 + b^2 + (n-2) eps^2) increases with b on [0, 1].
For eps >= 1/(n-1) take b = eps: M/T >= eps^2 / (1 + (n-1) eps^2) >= 1/(n(n-1)).
For eps <= 1/(n-1) take b = 1 - (n-2) eps: the inequality M/T >= 1/(n(n-1)) becomes
-(n-2)(n^2-1) eps^2 + (n^2+n-4) eps - 2 >= 0, whose roots are e2 := 2/((n-2)(n+1)) and 1/(n-1).
So in (II) Step 1 applies when eps >= e2. Moreover e2 <= e1 for n >= 7.

Step 3 (eps <= e1 in (I), eps <= e2 in (II): a perturbation of the vector (1, 0, ..., 0, -1)).
Put kappa := (n-1)/(n+1). Then M >= kappa eps (in (I) M = eps; in (II) b >= 1 - (n-2) e2 = kappa).
Also Y2 <= (n-2) e1^2 <= 0.002, 1 <= T <= 2.002, and

    2Q - T^2 = (1 - b^2)^2 + 2 Y4 - 2(1 + b^2) Y2 - Y2^2 >= -4 Y2 - Y2^2,
    P = (1 - b^3) + Y3,   0 <= 1 - b^3 <= 3 delta <= 3(n-2) eps,   |Y3| <= eps Y2,   Q >= 1.

Therefore

    G_M >= -(n-4) T (4 Y2 + Y2^2) - 2(n-3) (3(n-2) eps + eps Y2)^2 + (n-1)((n^2-6n+6) T^2 + 2n) kappa eps.

The first term is at most 4.002 (n-4)(n-2) e1 T eps in absolute value, which is less than one hundredth of
(n-1)(n^2-6n+6) kappa T eps <= (n-1)(n^2-6n+6) kappa T^2 eps. The second is at most
2(n-3)(3(n-2) + 0.002)^2 e1 eps <= 37.9 (n-2) eps. And 0.99 (n-1)(n^2-6n+6)(n-1)/(n+1) >= 37.9 (n-2) for n >= 14
(1316 against 455 at n = 14, and the ratio grows with n). So G_M >= 0, hence Psi >= 0.  []

## Remarks

1. Equality in the theorem: the vector (1, 0, ..., 0, -1) (eps = 0) and, in Step 2 (II), the vector
   (1, -1/(n-1), ..., -1/(n-1)) (eps = b = 1/(n-1)).
2. The constants are not tight: the same computation goes through from n = 10.
3. For sorted x the maximum defining m is attained at one of the two pairs (1, 2), (n-1, n):
   m T = max(x_1 x_2, x_(n-1) x_n).
