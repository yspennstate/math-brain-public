# A comparison of spectral gaps on Specht modules: four vertices, hooks, and graphs with two Laplacian eigenvalues

Abstract. For a weighted graph G on n vertices and a partition nu of n let lambda_min(G, nu) be the least eigenvalue
of the interchange Laplacian of G on the Specht module V_nu. Alon [1] conjectures that
lambda_min(G, tau) >= (2/3) lambda_min(G, sigma) whenever sigma != [n] dominates tau. We give an equivalent dual
form of such comparisons, prove the conjecture for n = 4, where the constant 2/3 is attained, and prove it with the
constant k/j for pairs of hooks [n-j, 1^j], [n-k, 1^k]. For the pair tau = [2, 1^(n-2)], sigma = [2, 2, 1^(n-4)] we
propose the constant (n-2)/(n-1), attained on the star, and prove it for every n >= 5 on the weighted graphs whose
Laplacian has only two nonzero eigenvalues, the larger one simple.

## 1. Setting and results

Let G = ([n], w) be a weighted graph, w_ij = w_ji >= 0, W = sum_{i<j} w_ij. For a partition nu of n let rho_nu be
the irreducible representation of S_n on the Specht module V_nu, with an invariant inner product, and

    L(G, nu) = sum_{i<j} w_ij (I - rho_nu((i j))),

a positive semidefinite operator on V_nu with least and largest eigenvalues lambda_min(G, nu), lambda_max(G, nu).
For nu = [n-1, 1] this is the graph Laplacian L_G restricted to V = {x in R^n : sum x_i = 0}; its eigenvalues are
written 0 <= lambda_1 <= ... <= lambda_(n-1). The theorem of Caputo, Liggett and Richthammer [3] states that
lambda_min(G, nu) >= lambda_1 for every nu != [n].

Conjecture (Alon [1, Conjecture 1.5]). If sigma != [n] and sigma dominates tau, then
lambda_min(G, tau) >= (2/3) lambda_min(G, sigma) for every weighted graph G on [n].

By [1, Theorem 1.8] it implies the conjecture of Oliveira [4] on the mixing time of the interchange process. Alon
proves the inequality for quasi-complete graphs, a class introduced in [5] which contains the complete graphs
[1, Section 4]; it holds with constant 1 for the pairs shown in [5] to be comparable in the Aldous order, and for
sigma = [n-1, 1] by [3]. The results of this note are the following.

Proposition 2.1 (dual form). A comparison lambda_min(G, tau) >= c lambda_min(G, sigma) for all G holds if and only if
every pure state of V_tau is matched, transposition by transposition, by a mixed state of V_sigma.

Proposition 3.1 (hooks). For 1 <= j < k <= n-1 and every G,
lambda_min(G, [n-k, 1^k]) >= (k/j) lambda_min(G, [n-j, 1^j]).

With constant 1 this is the ordering of the hooks due to Bacher [2], see [5, Appendix A]; the constant k/j comes from
the same description of the spectrum.

Theorem 4.2 (n = 4). For every weighted graph on four vertices lambda_min(G, 211) >= (2/3) lambda_min(G, 22), with
equality on the star K_{1,3}. Hence the conjecture holds for n = 4.

Conjecture F. For n >= 4 and every weighted graph G on [n],

    lambda_min(G, [2, 1^(n-2)]) >= ((n-2)/(n-1)) lambda_min(G, [2, 2, 1^(n-4)]).

Theorem 5.2. Let n >= 5 and let G be a weighted graph on [n] whose Laplacian has spectrum
{0, mu (n-2 times), lam} with 0 <= mu <= lam. Then Conjecture F holds for G. Equality holds on the star and on a
single edge.

For n = 4 Conjecture F is Theorem 4.2. For n >= 5 its constant exceeds 2/3. It cannot be increased: on the star the
two sides of the comparison are n - 2 and n - 1, which is how [5, Corollary 1] shows that this pair is not comparable
in the Aldous order. The graphs of Theorem 5.2 are those with
weights w_ij = c - g x_i x_j for a unit vector x in V; they form a family of dimension n in the cone of weighted
graphs, and it contains both graphs at which Conjecture F is an equality.

## 2. A dual form

Proposition 2.1. Let tau, sigma be partitions of n >= 2 and c > 0. The following are equivalent.

(a) lambda_min(G, tau) >= c lambda_min(G, sigma) for every weighted graph G on [n].

(b) For every unit vector psi in V_tau there is a density matrix rho on V_sigma (positive semidefinite, of trace
    one) with

        1 - <psi, rho_tau((i j)) psi>  >=  c (1 - tr(rho rho_sigma((i j))))     for all i < j.

Proof. (b) implies (a): given w, let psi be a unit eigenvector of L(G, tau) for lambda_min(G, tau) and take rho as
in (b). Multiplying the inequality for the pair ij by w_ij and adding gives
lambda_min(G, tau) >= c tr(rho L(G, sigma)) >= c lambda_min(G, sigma).

(a) implies (b): fix psi. On the product of the simplex {w >= 0, W = 1} and the set of density matrices on V_sigma
put

    f(w, rho) = sum_{i<j} w_ij [ c (1 - tr(rho rho_sigma((i j)))) - (1 - <psi, rho_tau((i j)) psi>) ].

Both sets are compact and convex and f is bilinear, so min_rho max_w f = max_w min_rho f. For fixed w,
min_rho f = c lambda_min(G, sigma) - <psi, L(G, tau) psi> <= c lambda_min(G, sigma) - lambda_min(G, tau) <= 0 by
(a). Hence some rho has f(w, rho) <= 0 for all w, and the vertices of the simplex give (b). []

For each psi, condition (b) is a semidefinite feasibility problem in rho.

## 3. Conjugation and hooks

Since V_nu' = V_nu tensor sign for the conjugate partition nu',

    lambda_min(G, nu') = 2W - lambda_max(G, nu).                                           (3.1)

In particular lambda_min(G, [1^n]) = 2W and lambda_min(G, [2, 1^(n-2)]) = 2W - lambda_max(L_G).

Lemma 3.2 (Bacher [2]). For 1 <= k <= n-1 the operator L(G, [n-k, 1^k]) is the derivation induced by L_G on the exterior power
Lambda^k V, so its eigenvalues are the sums of k distinct eigenvalues of L_G on V (with multiplicity), and
lambda_min(G, [n-k, 1^k]) = lambda_1 + ... + lambda_k.

Proof. V_[n-k, 1^k] = Lambda^k V, see [5, Appendix A]. A transposition (i j) acts on V as the reflection s = I - 2p, p the orthogonal
projection onto the line of e_i - e_j. As p has rank one, p x ^ p y = 0, so Lambda^k(s) = I - 2 D(p), where D(p)
is the derivation induced by p. Hence I - Lambda^k(s) = D(I - s); multiply by w_ij and add. []

Bacher works with the exterior powers of V; their identification with the Specht modules of the hooks is proved in
[5, Appendix A], where the chain [n-1, 1], [n-2, 1^2], ..., [1^n] in the Aldous order is deduced.

Proof of Proposition 3.1. The mean of the j smallest eigenvalues of L_G on V is at most the mean of the k smallest.
[]

Two further families are known. If tau = [1^n] then lambda_min(G, tau) = 2W >= lambda_min(G, sigma), because
I - rho_sigma((i j)) <= 2I [5, Corollary 2]. If sigma = [n-1, 1] then lambda_min(G, tau) >= lambda_min(G, sigma) for every
tau != [n] by [3].

## 4. Four vertices

The partitions of 4 other than [4] are 31, 22, 211, 1111. By Section 3 the only dominating pair left is
tau = 211, sigma = 22.

Lemma 4.1. Let a = w_12 + w_34, b = w_13 + w_24, c = w_14 + w_23 be the weights of the three perfect matchings and
D = (a^2 + b^2 + c^2 - ab - bc - ca)^(1/2). Then

    lambda_min(G, 211) = 2W - lambda_max(L_G),        lambda_min(G, 22) = W - D.

Proof. The first identity is (3.1). V_22 is the two-dimensional irreducible representation of S_3 pulled back along
S_4 -> S_4/V_4 = S_3, under which the two transpositions of a perfect matching have the same image. So L(G, 22) is
the Laplacian of the triangle with edge weights a, b, c on the complement of the constants in R^3, with eigenvalues
(a + b + c) +- D. []

Theorem 4.2. For every weighted graph G on four vertices

    lambda_max(L_G) <= (4/3) W + (2/3) D,

that is, lambda_min(G, 211) >= (2/3) lambda_min(G, 22). Equality holds for the star K_{1,3} with equal weights.

Proof. Write v = (a, b, c) and let P be the orthogonal projection of R^3 onto {u : u_a + u_b + u_c = 0}. Then
|Pv|^2 = (2/3) D^2, so

    (2/3) D = max { (2/3)^(1/2) <u, v> : u_a + u_b + u_c = 0, |u| <= 1 }.

For an edge ij let m(ij) be the perfect matching containing it. For u as above,
(4/3) W + (2/3)^(1/2) <u, v> = sum_{i<j} w_ij (4/3 + (2/3)^(1/2) u_{m(ij)}), and lambda_max(L_G) is the maximum of
sum w_ij (x_i - x_j)^2 over unit x in V. So it is enough to show:

(*) for every unit x in V there is u with u_a + u_b + u_c = 0, |u| <= 1 and
    (x_i - x_j)^2 <= 4/3 + (2/3)^(1/2) u_{m(ij)} for all six edges.

Let e_a = (1,1,-1,-1)/2, e_b = (1,-1,1,-1)/2, e_c = (1,-1,-1,1)/2, an orthonormal basis of V, and
x = p e_a + q e_b + r e_c, p^2 + q^2 + r^2 = 1. Then

    x_1 - x_2 = q + r,  x_3 - x_4 = q - r,  x_1 - x_3 = p + r,  x_2 - x_4 = p - r,  x_1 - x_4 = p + q,  x_2 - x_3 = p - q.

The larger of the two squares in each matching is (|q| + |r|)^2, (|p| + |r|)^2, (|p| + |q|)^2, so we may take
p, q, r >= 0 and, by the symmetry in the three matchings, p >= q >= r. Set

    t_a = (q + r)^2 - 4/3,   t_b = (p + r)^2 - 4/3,   t_c = (p + q)^2 - 4/3,

so that t_a <= t_b <= t_c, and (*) asks for u with sum zero, |u| <= 1 and (3/2)^(1/2) t_m <= u_m for m = a, b, c.
We use

    t_a + t_b + t_c = 2(pq + qr + rp) - 2 <= 0,                                            (4.1)
    t_c <= 2/3,                                                                            (4.2)
    t_b + t_c <= 1/3.                                                                      (4.3)

(4.2) holds because (p + q)^2 <= 2(p^2 + q^2) <= 2. For (4.3),
(p + r)^2 + (p + q)^2 = 1 + p^2 + 2p(q + r) <= 1 + p^2 + 2 sqrt(2) p (1 - p^2)^(1/2), and with p = cos(theta) the
right side is 3/2 + (1/2) cos(2 theta) + sqrt(2) sin(2 theta) <= 3/2 + (1/4 + 2)^(1/2) = 3.

Case 1: t_c <= 0. Take u = 0.

Case 2: t_c > 0 and t_b <= -t_c/2. Take u = (3/2)^(1/2) (-t_c/2, -t_c/2, t_c). The sum is zero, u dominates
(3/2)^(1/2) t because t_a <= t_b <= -t_c/2, and |u|^2 = (9/4) t_c^2 <= 1 by (4.2).

Case 3: t_c > 0 and t_b > -t_c/2. Take u = (3/2)^(1/2) (-t_b - t_c, t_b, t_c). The sum is zero and
-t_b - t_c >= t_a by (4.1). Further

    |u|^2 = 3 (t_b^2 + t_b t_c + t_c^2) = (9/4)(t_b + t_c)^2 + (3/4)(t_c - t_b)^2,

where 0 < t_b + t_c <= 1/3 by (4.3) and 0 <= t_c - t_b < (3/2) t_c <= 1 by (4.2). So |u|^2 <= 1/4 + 3/4 = 1.

For the star with centre 1 and unit weights, lambda_max(L_G) = 4, W = 3 and a = b = c = 1, D = 0. []

In the language of Proposition 2.1 the states of V_22 form a disc and u is, up to the factor (2/3)^(1/2), the vector
of the three numbers tr(rho rho_22(m)). The state chosen in the proof depends on x in a piecewise linear way
through the numbers (x_i - x_j)^2; at the vector of a single edge it is a pure state.

The equality case is the case m = 2 of [1, Theorem 4.5].

## 5. The pair [2, 1^(n-2)], [2, 2, 1^(n-4)]

By (3.1), with [2, 2, 1^(n-4)]' = [n-2, 2], Conjecture F is the bound

    lambda_max(L_G) <= ( 2W + (n-2) lambda_max(G, [n-2, 2]) ) / (n-1).                      (5.1)

On the star with unit weights L(G, nu) is n - 1 minus a Jucys-Murphy element, whose eigenvalues on V_nu are the
contents of the removable boxes of nu [7]. So lambda_min(G, [2, 1^(n-2)]) = n - 2 and
lambda_min(G, [2, 2, 1^(n-4)]) = n - 1 (compare [5, Corollary 1]), and Conjecture F is an equality. On a single edge both sides of (5.1) equal
the weight of the edge times 2.

A model of V_[n-2, 2]. Let S_0 be the space of symmetric n x n matrices with zero row sums and trace zero, with the
Frobenius inner product; S_n acts by simultaneous permutation of rows and columns. The map T -> diag T is
equivariant from S_0 onto V, and its kernel

    M_n = { T symmetric, zero diagonal, zero row sums },   dim M_n = n(n-3)/2,

is V_[n-2, 2]. The orthogonal projection of S_0 onto M_n is

    P T = T - (n/(n-2)) Pi diag(T) Pi,     |P T|^2 = |T|^2 - (n/(n-2)) |diag T|^2,           (5.2)

Pi the orthogonal projection of R^n onto V and diag(T) the diagonal part of T.

Graphs with two Laplacian eigenvalues. Let L_G have spectrum {0, mu (n-2 times), lam}, g = lam - mu > 0, and let x
be the unit eigenvector for lam. Then L_G = lam x x^t + mu (Pi - x x^t), so

    w_ij = c - g x_i x_j,   c = mu/n,   and conversely such weights are admissible exactly when c >= g m(x),

    m(x) = max_{i<j} x_i x_j   (m(x) >= 0 for n >= 3).

For these weights lam = cn + g and 2W = c n (n-1) + g, because sum_{i<j} x_i x_j = -1/2, and

    L(G, [n-2, 2]) = (2c(n-1) + g/2) I + g X(x),     X(x) = sum_{i<j} x_i x_j rho_[n-2,2]((i j)),

because sum_{i<j} rho_[n-2,2]((i j)) = (n-1)(n-4)/2. Inserting this in (5.1), Conjecture F for G reads
lambda_max(X(x)) >= 1/2 - 2(n-1) c/g. The right side decreases in c, so Theorem 5.2 is equivalent to the following
statement (the case mu = lam is a multiple of the complete graph, where (5.1) is clear).

Theorem 5.3. Let n >= 5 and let x be a unit vector in V. Then

    lambda_max( sum_{i<j} x_i x_j rho_[n-2,2]((i j)) )  >=  1/2 - 2(n-1) max_{i<j} x_i x_j,

with equality at x = (1, -1, 0, ..., 0)/sqrt(2) and at x = (n-1, -1, ..., -1)/(n(n-1))^(1/2).

Write q = sum x_i^4, p_3 = sum x_i^3, m = m(x), and

    Psi(x) = (n-4)(2q - 1) - 2(n-3) p_3^2 + (n-1)(n^2 - 6n + 6 + 2nq) m.

Lemma 5.4. Let n >= 5, let x be a unit vector in V, Q the orthogonal projection onto {1, x}^perp, and for y in
{1, x}^perp put A y = P( (x y^t + y x^t)/sqrt(2) ) in M_n. Then

    tr(A A^*) = (n-2) Z,   Z = (n^2 - 6n + 6 + 2nq)/(n-2)^2 > 0,

and R(x) = tr(X(x) A A^*) / tr(A A^*) satisfies

    ( R(x) - 1/2 + 2(n-1) m ) Z = (2/(n-2)^2) Psi(x).

Proof. Let y be a unit vector of {1, x}^perp and S = (x y^t + y x^t)/sqrt(2), so |S| = 1 and
diag S = sqrt(2) (x_k y_k)_k. Write sigma for the permutation matrix of (i j), d = x_i - x_j, e = y_i - y_j. Since
x.(sigma x) = 1 - d^2, y.(sigma y) = 1 - e^2 and x.(sigma y) = y.(sigma x) = -de,

    <S, sigma S sigma> = (1 - d^2)(1 - e^2) + d^2 e^2,
    <Pi diag(S) Pi, sigma S sigma> = 2 sum_k x_k y_k x_sigma(k) y_sigma(k) = 2 ( K - (x_i y_i - x_j y_j)^2 ),

with K = sum_k x_k^2 y_k^2. The operator T -> sum_{i<j} x_i x_j sigma_ij T sigma_ij on S_0 commutes with P and
restricts to X(x) on M_n, so by (5.2)

    |A y|^2 = 1 - (2n/(n-2)) K,
    <A y, X(x) A y> = sum_{i<j} x_i x_j [ 1 - d^2 - e^2 + 2 d^2 e^2 - (2n/(n-2)) ( K - (x_i y_i - x_j y_j)^2 ) ].

Now sum over an orthonormal basis of {1, x}^perp, that is, replace y y^t by Q = Pi - x x^t. This replaces

    e^2 by 2 - d^2,   K by 1 - 1/n - q,
    (x_i y_i - x_j y_j)^2 by (1 - 1/n)(x_i^2 + x_j^2) - x_i^4 - x_j^4 + (2/n) x_i x_j + 2 x_i^2 x_j^2,

and the constant 1 by n - 2. The sums over pairs are, for a unit vector with sum zero,

    sum x_i x_j = -1/2,   sum x_i x_j d^2 = -1,   sum x_i x_j d^4 = 3 p_3^2 - 4q,
    sum x_i x_j (x_i^2 + x_j^2) = -q,   sum x_i^2 x_j^2 = (1 - q)/2,
    sum x_i x_j (x_i^4 + x_j^4) = -p_6,   sum x_i^3 x_j^3 = (p_3^2 - p_6)/2,

with p_6 = sum x_i^6, which cancels. This gives tr(A A^*) = (n-2) - (2n/(n-2))(1 - 1/n - q) = (n-2) Z and

    tr(X(x) A A^*) = (n-2)/2 + 8q - 6 p_3^2 - 4 - (n/(n-2)) (3q - 2 p_3^2 - 1 - 1/n).

Hence (n-2)^2 (R(x) - 1/2) Z = 2(n-4)(2q - 1) - 4(n-3) p_3^2, and adding 2(n-1) m (n-2)^2 Z gives the identity.
Finally n^2 - 6n + 6 >= 1 for n >= 5. []

Proof of Theorem 5.3, given Theorem 6.1. lambda_max(X(x)) >= R(x), and R(x) - 1/2 + 2(n-1) m = 2 Psi(x)/((n-2)^2 Z)
is nonnegative by Theorem 6.1. At the two vectors named, the graph w_ij = g (m - x_i x_j) is a single edge and a
star, where Conjecture F is an equality. []

The operator A A^*/tr(A A^*) is the image of the uniform state on {1, x}^perp. Lemma 5.4 compares it with the top
eigenvector x of L_G only after summation against the weights c - g x_i x_j; the inequalities of Proposition 2.1 for
the single transpositions can fail for it, for instance for n = 5, x = (1, 1, 0, 0, -2)/sqrt(6) and the transposition
(1 5).

## 6. The inequality Psi >= 0

Psi is homogeneous of degree zero if q, p_3^2, m are replaced by Q/T^2, P^2/T^3, M/T, where T, P, Q are the power
sums of x of degree 2, 3, 4 and M = max_{i<j} x_i x_j. We use this form for vectors that are not normalised.

Theorem 6.1. For n >= 5 and every nonzero x in R^n with sum zero, Psi(x) >= 0.

Put C = (n-1)(n^2 - 6n + 6 + 2nq) > 0, and for a number M' <= M

    G_{M'} = (n-4)(2Q - T^2) T - 2(n-3) P^2 + (n-1)((n^2 - 6n + 6) T^2 + 2nQ) M',

so that T^3 Psi >= G_{M'}.

Normalisation. Psi(-x) = Psi(x). Sort x decreasingly; if x_1 + x_n < 0 replace x by -x and sort again. Then
x_1 > 0 > x_n, x_1 + x_n >= 0, and x lies in one of the cones

    R_1 = { x_1 >= ... >= x_n, sum x = 0, x_1 + x_n >= 0, x_2 + x_(n-1) >= 0 },   where M >= x_1 x_2 =: M_1,
    R_2 = { x_1 >= ... >= x_n, sum x = 0, x_1 + x_n >= 0, x_2 + x_(n-1) <= 0 },   where M >= x_n x_(n-1) =: M_2.

Proof for n >= 14. Scale so that x_1 = 1 and put b = -x_n, so 0 < b <= 1. On R_1 let eps = x_2; then eps >= 0
(otherwise x_(n-1) <= x_2 < 0) and M_1 = eps. On R_2 let eps = -x_(n-1); then eps >= 0 (otherwise
x_2 >= x_(n-1) > 0) and M_2 = b eps. In both cases the middle coordinates x_2, ..., x_(n-1) lie in [-eps, eps], so
Y_2 := x_2^2 + ... + x_(n-1)^2 <= (n-2) eps^2, T = 1 + b^2 + Y_2, and delta := 1 - b = -(x_2 + ... + x_(n-1)) lies
in [0, (n-2) eps].

Step 1. There is the identity Psi = 2(n-3)(q - p_3^2 - 1/n) + C (m - 1/(n(n-1))). The Gram determinant of the
vectors (1, ..., 1), x, (x_i^2) is n(TQ - P^2) - T^3 >= 0, that is, q - p_3^2 >= 1/n. Hence Psi >= 0 whenever
m >= 1/(n(n-1)).

Step 2. Let e_1 = 2.1/(n(n-1)) and e_2 = 2/((n-2)(n+1)); e_2 <= e_1 for n >= 7.

On R_1, T <= 2 + (n-2) eps^2, so M_1/T >= eps/(2 + (n-2) eps^2), and this is at least 1/(n(n-1)) when
(n-2) eps^2 - n(n-1) eps + 2 <= 0. The quadratic is convex and is <= 0 at eps = e_1 and at eps = 1, hence on
[e_1, 1], and Step 1 applies there.

On R_2, b >= max(eps, 1 - (n-2) eps), and b eps/(1 + b^2 + (n-2) eps^2) increases with b on [0, 1]. For
eps >= 1/(n-1) take b = eps: M_2/T >= eps^2/(1 + (n-1) eps^2) >= 1/(n(n-1)). For eps <= 1/(n-1) take
b = 1 - (n-2) eps: the inequality M_2/T >= 1/(n(n-1)) becomes -(n-2)(n^2-1) eps^2 + (n^2+n-4) eps - 2 >= 0, whose
roots are e_2 and 1/(n-1). So Step 1 applies for eps >= e_2.

Step 3. It remains to treat eps <= e_1 on both cones. Put kappa = (n-1)/(n+1). On R_1, M_1 = eps >= kappa eps; on
R_2 we may assume eps <= e_2, so b >= 1 - (n-2) e_2 = kappa and M_2 >= kappa eps. Since (n-2)/(n^2 (n-1)^2)
decreases in n, Y_2 <= (n-2) e_1^2 < 0.002, and 1 <= T <= 2.002. With Y_3, Y_4 the sums of the third and fourth
powers of the middle coordinates,

    2Q - T^2 = (1 - b^2)^2 + 2 Y_4 - 2(1 + b^2) Y_2 - Y_2^2 >= -4 Y_2 - Y_2^2,
    P = (1 - b^3) + Y_3,   0 <= 1 - b^3 <= 3 delta <= 3(n-2) eps,   |Y_3| <= eps Y_2,   Q >= 1,

and therefore, with M' = kappa eps,

    G_{M'} >= -(n-4) T (4 Y_2 + Y_2^2) - 2(n-3)(3(n-2) eps + eps Y_2)^2 + (n-1)((n^2-6n+6) T^2 + 2n) kappa eps.

Let D_n = (n-1)^2 (n^2-6n+6)/(n+1), so the last term is at least D_n T^2 eps >= D_n T eps. The first term is at
most 4.002 (n-4)(n-2) e_1 T eps < 8.41 T eps, and 8.41 < D_14/100 <= D_n/100 because D_n increases for n >= 5. The
second is at most 2(n-3)(3(n-2) + 0.002)^2 e_1 eps, and

    2(n-3)(3(n-2) + 0.002)^2 e_1/(n-2) = (189/5) ((n-3)(n-2)/(n(n-1))) (1 + 1/(1500(n-2)))^2 < 37.9.

Finally D_n/(n-2) = n^2 - 7n + 14 - (18n - 34)/(n^2 - n - 2) increases for n >= 4 and 0.99 D_14/12 > 109 > 37.9.
So G_{M'} >= (0.99 D_n - 37.9 (n-2)) eps >= 0, and Psi >= 0. []

For n >= 14 equality holds only at the edge vector (eps = 0) and at the star vector (eps = b = 1/(n-1) on R_2), up
to scaling, permutation and sign: Step 3 is strict for eps > 0, and equality in Step 1 forces q - p_3^2 = 1/n, so
that x takes two values, together with m = 1/(n(n-1)), which excludes two repeated values.

Proof for 5 <= n <= 13. On R_1, T^3 Psi >= G_{M_1}, and on R_2, T^3 Psi >= G_{M_2}; both are polynomials in x,
homogeneous of degree 6. Each cone is polyhedral and pointed. Writing x as a combination of the extreme rays of the
cone with nonnegative coefficients c_r turns G_{M_1} (on R_1) and G_{M_2} (on R_2) into a polynomial in the c_r with
integer coefficients once the rays are scaled to integer vectors. For n = 5, ..., 13 none of these polynomials has
a negative coefficient; hence both are nonnegative on their cones. The rays were enumerated and the polynomials
expanded in exact integer arithmetic (in SymPy [6] for n <= 11, and by a dense expansion with
128-bit integers for 9 <= n <= 16); R_1 has s^2 + s - 1 extreme rays for n = 2s + 1 and
s^2 + s for n = 2s + 2. In the coordinates x_i - x_(i+1) >= 0 each cone is cut out by two further half-spaces, so
an extreme ray has at most three nonzero coordinates, and the enumeration runs over these supports. []

## 7. Remarks

Disjoint unions. If G is the disjoint union of G_1 on A and G_2 on B, |A| = k, then

    lambda_min(G, nu) = min { lambda_min(G_1, alpha) + lambda_min(G_2, beta) : c^nu_{alpha, beta} > 0 },

the minimum over partitions alpha of k and beta of n - k with nonzero Littlewood-Richardson coefficient, because
V_nu restricted to S_k x S_(n-k) is the sum of c^nu_{alpha,beta} copies of V_alpha tensor V_beta. Letting the
weights of a connected G_2 tend to infinity leaves beta = [n-k], and c^nu_{alpha,[n-k]} > 0 exactly when nu/alpha
is a horizontal strip. So the conjecture at n contains, for every graph G_1 on k vertices,

    min { lambda_min(G_1, alpha) : tau/alpha a horizontal strip }
        >= (2/3) min { lambda_min(G_1, alpha) : sigma/alpha a horizontal strip },

whenever the set on the right is not empty.

With G_1 = K_{1,3} this shows that the value 2/3 of Theorem 4.2 is approached at n = 6 for (2211, 222), at n = 7
for (3211, 322) and at n = 8 for (4211, 422), although the ratio of these pairs on the star is larger.

Numerical evidence. In a local search over weighted graphs, with the Specht modules in Young's orthogonal form [7], the
smallest ratios lambda_min(G, tau)/lambda_min(G, sigma) found over all dominating pairs are 2/3, 3/4, 2/3, 2/3, 2/3
for n = 4, ..., 8, and for the pair of Conjecture F they are 3/4, 4/5, 5/6, 6/7 for n = 5, ..., 8, on the star. A
local search does not certify a global minimum.

The pairs left at n = 5. After Section 3 the open pairs at n = 5 are (311, 32), (221, 32), (2111, 32), (221, 311)
and (2111, 221); the last is Conjecture F with constant 3/4.

## References

[1] G. Alon, Spectral comparison on Specht modules and mixing of the interchange process, arXiv:2610.22151 (2026).

[2] R. Bacher, Valeur propre minimale du laplacien de Coxeter pour le groupe symétrique, J. Algebra 167 (1994),
    460-472.

[3] P. Caputo, T. M. Liggett, T. Richthammer, Proof of Aldous' spectral gap conjecture, J. Amer. Math. Soc. 23
    (2010), 831-851.

[4] R. I. Oliveira, Mixing of the symmetric exclusion processes in terms of the corresponding single-particle
    random walk, Ann. Probab. 41 (2013), 871-913.

[5] G. Alon, G. Kozma, Ordering the representations of S_n using the interchange process, Canad. Math. Bull. 56
    (2013), 13-30.

[6] A. Meurer et al., SymPy: symbolic computing in Python, PeerJ Comput. Sci. 3 (2017), e103.

[7] A. Okounkov, A. Vershik, A new approach to representation theory of symmetric groups, Selecta Math. (N.S.) 2
    (1996), 581-605.
