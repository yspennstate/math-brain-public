# The gap-weighted state in terms of N = lam Pi - L_G (working note, 11 Nov 2026)

Status: algebra checked numerically (gapN_check.py, gapN_check.out: deviation 7e-15 on 500 graphs, n = 4..9).
The inequality itself is open. Notation as in HOOKS_AND_TWO_ROWS.md, section 5 (d). Not audited.

## Setting

G a weighted graph on n vertices, x a unit top eigenvector of L_G with eigenvalue lam, Pi the projection onto the
sum-zero space V. Put

    N = lam Pi - L_G,   tau = tr N = (n-1) lam - 2W,   t = sum_i x_i^2 N_ii,   d_ij = x_i - x_j.

N is positive semidefinite, N 1 = 0, N x = 0, and w_ij = N_ij + lam/n for i != j. Conversely a positive
semidefinite N with N 1 = N x = 0 and a number lam >= n max_{i != j} (-N_ij) define a weighted graph with top
eigenvector x. The eigenvalues of N on {1, x}^perp are the gaps g_k = lam - lam_k.

## The inequality

Gval of section 5 (d) is

    Gval/(n-2) = a lam + b,
    a = (2(n-1)/n) (tau - (2n/(n-2)) t),
    b = - tr N^2 - tau^2/(n-2) + (2n/(n-2)^2) tau t + (2n/(n-2)) sum_{i,j} x_i x_j N_ij^2
        - 2 sum_{i<j} N_ij d_ij^2 (N_ii + N_jj - 2 N_ij).

Used on the way: sum_{i<j} d_ij^2 (N_ii + N_jj - 2 N_ij) = n t + tau, because N 1 = 0 and N x = 0.

## Two consequences

1. a >= 0. Indeed tau - (2n/(n-2)) t is the total squared norm of the [n-2,2] components of the vectors
   (x y^t + y x^t)/sqrt 2, y running over an orthonormal eigenbasis of N weighted by the gaps.

2. For fixed (N, x) the quantity is affine and nondecreasing in lam. Raising lam by c n with N fixed is adding
   c times the complete graph to G. So Gval(G + c K_n) = Gval(G) + c n (n-2) a >= Gval(G), and it is enough to
   prove Gval >= 0 at lam = n max_{i != j} (-N_ij), that is, for graphs with at least one pair of weight zero
   among the pairs where N_ij is most negative.

## The leading terms

Without the two correction terms (the pair term sum w_ij d_ij^2 N(e_i - e_j) and the [n-1,1] term) the inequality is

    2 lam tau - sum_k g_k^2 - tau^2/(n-2) >= 0,

true because 0 <= g_k <= lam gives sum g_k^2 <= lam tau and Cauchy-Schwarz gives tau^2/(n-2) <= sum g_k^2. Equality
needs all g_k = 0 (an equally weighted complete graph) or all g_k = lam (a single edge) [corrected after the
Codex referee, AUDIT_CODEX_HOOKS_REPORT.md]. On the unit star the left side is 2(n-1)(n-2), and the corrections use all
of it.

## Checks at the unit star

N = (n-1) times the projection onto sum-zero vectors on the leaves; lam = n = n max(-N_ij); tau = (n-1)(n-2);
t = (n-2)/n; a lam = 2(n-1)((n-1)(n-2) - 2); b = -a lam. Equality.

## The two-eigenvalue family

Take N = g Q, Q the projection onto {1, x}^perp. The graph is w_ij = (lam - g)/n - g x_i x_j, with Laplacian
lam x x^t + (lam - g)(Pi - x x^t): one simple top eigenvalue and one other eigenvalue lam - g of multiplicity n - 2 (zero for a single edge).
The star (g = n - 1, lam = n) and the single edge (g = lam) both lie in it, and both equality cases of Gval are of
this form. Write q = sum x_i^4, p3 = sum x_i^3, m = max_{i != j} x_i x_j (m >= 0). The weights are nonnegative
exactly when lam >= g (1 + n m). At lam = g (1 + n m),

    Gval = 2 g^2 Psi(x),
    Psi(x) = (n-4)(2q - 1) - 2(n-3) p3^2 + (n-1)(n^2 - 6n + 6 + 2nq) m.

Derivation: tau = g(n-2), t = g((n-1)/n - q), sum_{i,j} x_i x_j Q_ij^2 = 1 + p3^2 - 2q,
sum_{i<j} Q_ij d_ij^2 (2 - d_ij^2) = -3(q - 1/n - p3^2); the terms free of q, p3, m add up to -2(n-4)/(n-2).
Checked against Gval on 300 vectors, n = 4..9 (two_eig_family.py, deviation 2e-14).

Values: Psi = 0 at the edge vector (q = 1/2, p3 = 0, m = 0) and at the star vector; at the vector of K_{1,k} padded
with zeros, 2 <= k <= n-1 and u = k/(k+1), Psi = (n-4)(2u-1)(3u-2)/u - 2(n-3)(2u-1)^2/u + (n-1)(n^2-6n+6+2nq)(1-u)^2/u,
positive for k < n-1. At n = 4, Psi = 6(4q - 1) m - 2 p3^2, zero also at (1,1,-1,-1)/2.

Numerical minimum of Psi over unit sum-zero x (60 starts each, two_eig_family.out): 0 for n = 4..8, attained at the
star vector for n >= 5. So the gap-weighted state proves Conjecture F on this family if Psi >= 0, which is an
inequality between q, p3^2 and the largest product of two coordinates.

A first attempt at Psi >= 0 for x with one positive coordinate S (u = S^2 >= 1/2, negatives -b_i): bounding
m >= (2u - 1)/((n-1)(n-2)) (average over pairs of negatives), sum b^3 >= (1-u)^2/S, sum b^4 >= (1-u)^3/u gives
Psi >= (2u - 1) 6n (u - 2/3)(u - (n-1)/n) / ((n-2) u), which is negative for 2/3 < u < (n-1)/n. The three bounds are
tight together only at the star; a proof has to use the number of nonzero negatives, or m = b_1 b_2 itself.

## Open

Prove Psi >= 0 for n >= 5 (the two-eigenvalue family), then

Prove a lam + b >= 0 for n >= 5 for every positive semidefinite N with N 1 = N x = 0 and lam = n max(-N_ij).
It is false at n = 4 (canon_gap.out). The difficulty is that lam enters through a maximum over pairs: bounding the
maximum by an average over pairs loses at the star unless the average is supported on the pairs with x_i = x_j.

## A split of Psi (11 Nov, 03:5x)

Put K = n^2 - 6n + 6 + 2nq and D = q - 1/n - p3^2. Then, identically,

    Psi = K ((n-1) m - 1/n) + 2 (n-3) D.

(Expand: -K/n - 2(n-3)/n = -(n-4) - 2q, and -2q + 2(n-3) q = 2(n-4) q.) Both factors have a sign:

- K >= (n-2)(n-4) > 0 for n >= 5, because q >= 1/n.
- D >= 0: since sum x_i = 0 and |x| = 1, p3 = <x, x^2 - 1/n> and |x^2 - 1/n|^2 = q - 1/n, so D is the
  Cauchy-Schwarz defect. D = 0 exactly when x_i^2 - 1/n = c x_i for all i, that is when x takes two values.

So Psi >= 0 whenever m >= 1/(n(n-1)), and the whole question is the region m < 1/(n(n-1)), where the claim reads

    K (1/n - (n-1) m) <= 2 (n-3) D.

The star has m = 1/(n(n-1)) and D = 0, both terms vanish; the edge has m = 0, K = (n-2)(n-3), D = (n-2)/(2n).
A two-valued x other than the star has m >= 1/n, so D = 0 never meets the open region.

Where the earlier one-positive bound lost. With one positive coordinate S, u = S^2, and m replaced by the mean of
b_i b_j over all pairs of negatives, (2u-1)/((n-1)(n-2)), the claim becomes K (n-1-nu)/(n(n-2)) <= (n-3) D. The
left side minus the right is decreasing in beta_4 = sum b_i^4 and in beta_3 = sum b_i^3 (coefficients
(n^2-7n+8+2nu)/(n-2) > 0 and (n-3)(2u^(3/2) - beta_3) > 0 for n >= 5), so the worst case is the smallest beta_3,
beta_4 for the given sum and sum of squares. Cauchy-Schwarz gives beta_3 >= (1-u)^2/u^(1/2), attained only by
equal nonzero b_i, i.e. only at u = k/(k+1); for other u the bound is not attained and for k < n-1 the mean over
all pairs is far below m. That is the loss recorded above (negative for 2/3 < u < (n-1)/n): it comes from the
choice of pairs, not from D.

Numerical test of the remedy (psi_split_check.py, 24 starts, n = 5, 6, 7): replace m by the largest mean of
x_i x_j over the pairs inside a set A, the maximum taken over all sets A with |A| >= 2, keep q and p3 exact. The
minimum over x of the resulting lower bound is 0 to rounding (+8e-13, -2e-15, +1e-7), attained at the star. With
only the complements of at most two indices as A it is negative at n = 6, 7 (-1.28, -1.86, at vectors with three
positive coordinates where the right A is the positive set). So on this evidence

    for every x there is a set A with  K ((n-1) mu_A - 1/n) + 2 (n-3) D >= 0,   mu_A = ((sum_A x)^2 - sum_A x^2)/(|A|(|A|-1)),

which is a family of polynomial inequalities with no maximum over pairs. Candidate, numerical only.

## A bound for m in power sums (11 Nov, 04:0x)

Let S be the coordinate of x of largest modulus; after x -> -x (which fixes q, m, D and K) take S = max x > 0, so
S^2 >= 1/n. Put c_i = S - x_i >= 0. Since m >= x_i x_j for i != j,

    m ((sum c)^2 - sum c^2) >= (sum c_i x_i)^2 - sum c_i^2 x_i^2,

and sum c = nS, sum c^2 = nS^2 + 1, sum c_i x_i = -1, sum c_i^2 x_i^2 = S^2 - 2 S p3 + q. Hence

    m >= M := (1 - q + 2 S p3 - S^2) / (n(n-1) S^2 - 1),

with equality exactly when x_i x_j = m for all i != j outside the coordinates equal to S. This is an equality at
the star (the other coordinates are equal) and at the edge (products -1*0 and 0*0, m = 0). The denominator is
positive unless x is minus the star, where S^2 = 1/(n(n-1)) is excluded by S^2 >= 1/n.

Inserting M for m in the split,

    n (n(n-1)S^2 - 1) Psi >= Phi' := K N + 2n(n-3) (n(n-1)S^2 - 1) D,   N = n(n-1)(1 - q + 2 S p3 - 2 S^2) + 1.

Numerically the minimum of the right side over x is 0 to rounding for n = 5..8, at the star
(psi_linear_weight_check.out, 40 starts each, both with the better of max x, min x and with the coordinate of
larger modulus alone). So on this evidence Psi >= 0 follows from Phi' >= 0, a polynomial inequality in q, p3 and S.

Concavity. For fixed S, Phi' is a quadratic polynomial in (q, p3) with second derivatives
-4n^2(n-1), 4n^2(n-1) S (mixed), -4n(n-3)(n(n-1)S^2 - 1), and determinant
16 n^3 (n-1) [ (n-4) n(n-1) S^2 - (n-3) ], which is positive when S^2 >= 1/n and n >= 5 (n^2 - 6n + 7 > 0).
So for n >= 5 and fixed S, Phi' is strictly concave in (q, p3), and its minimum over the attainable pairs
(q, p3) is taken at an extreme point of their convex hull. With y the other n-1 coordinates (sum -S, sum of squares
1 - S^2, |y_i| <= S), a point y that maximises a linear form a sum y^3 + b sum y^4 has every coordinate in the open
interval a root of one cubic, so at most three values there. What is left to prove is Phi' >= 0 on those vectors:
S, possibly -S, and at most three other values. Not done.

## Where Phi' >= 0 can and cannot be proved (11 Nov, 04:1x)

Two scans, both numerical evaluations on a grid (floating point, no arithmetic certificate).

1. The relaxation to measures fails. Replace the empirical measure of the other n-1 coordinates by any probability
   measure on [-S, S] with the same mean and second moment. For fixed S the pairs (third, fourth moment) then form
   a convex set and the minimum of the concave Phi' is on its boundary: two atoms inside the interval, or atoms
   -S, t, S. On both families Phi' is negative near S^2 = 0.41..0.44 (phi_boundary_scan.out: -2.79 at n = 5,
   -2245 at n = 16), at weights that are not multiples of 1/(n-1) (two atoms with weight 0.69 at n = 5). So a proof
   of Phi' >= 0 has to use that the multiplicities are integers, as with the count of nonzero negatives earlier.
   The relaxed arc of phi_parabola_scan.py is negative too, at points that violate |y_i| <= S.

2. On genuine vectors x = (S, s x k, t x (n-1-k)) with |s|, |t| <= S, every k, Phi' >= 0 on a grid of 2001 values
   of S^2 for n = 5..12 (phi_integer_scan.out: no point below -1e-9), with zeros only at the edge (S^2 = 1/2,
   s = 0, t = -S, k = n-2) and the star.

So the state is: Psi >= Phi'/(n(n(n-1)S^2 - 1)) is proved; Phi' >= 0 is supported by local minimisation over all x
(n = 5..8) and by the grid on three-valued vectors (n = 5..12); by concavity it is enough to treat vectors with
values S, possibly -S, and at most three others, with integer multiplicities. Not proved.


## Psi >= 0 for n = 5, 6, 7, 8 by an exact coefficient certificate (11 Nov, 06:1x)

Statement. For n = 5, 6, 7, 8 and every x in R^n with sum x_i = 0 and |x| = 1, Psi(x) >= 0. Computer-assisted, exact
integer arithmetic.

Proof. Psi is invariant under permutations and under x -> -x, so take x_1 >= x_2 >= ... >= x_n and x_1 + x_n >= 0.
Then S = x_1 is the coordinate of largest modulus, the bound m >= M of the section "A bound for m in power sums"
applies, and n (n(n-1) S^2 - 1) Psi >= Phi' with a positive factor on the left. It remains to show Phi' >= 0 on the
cone C = {sum x = 0, x_1 >= ... >= x_n, x_1 + x_n >= 0}. With T = sum x^2, P = sum x^3, Q = sum x^4 and a = x_1,

    H = K Nh + 2 (n-3) (n(n-1) a^2 - T) Dh,
    K = (n^2 - 6n + 6) T^2 + 2 n Q,   Nh = n(n-1)(T^2 - Q + 2 a P - 2 a^2 T) + T^2,   Dh = n Q T - T^3 - n P^2,

is homogeneous of degree 8 and equals Phi' when T = 1. The cone {sum x = 0, x_1 >= ... >= x_n} is simplicial with
rays r_j = (n-j, ..., n-j, -j, ..., -j) (j entries n-j), j = 1, ..., n-1, since x = sum_j ((x_j - x_(j+1))/n) r_j;
the functional x_1 + x_n takes the value n - 2j on r_j. Cutting a simplicial cone by a half-space leaves the rays on
the closed side and one new ray on each two-face that joins a ray strictly inside to a ray strictly outside, so the
extreme rays of C are

    r_j with n - 2j >= 0,   and   (2j - n) r_i + (n - 2i) r_j with n - 2i > 0 > n - 2j.

Write x = sum_k z_k rho_k over these rays with z_k >= 0. As a polynomial in z, H has no negative coefficient:

    n   rays   monomials   negative
    5     6       1,277        0
    6     7       2,991        0
    7    12      75,561        0
    8    13     125,947        0

so H >= 0 on C. QED. The pure powers z_k^8 are absent exactly for the star ray r_1 and the edge ray
(n-2)(r_1 + r_(n-1)) = (n(n-2), 0, ..., 0, -n(n-2)), the two equality cases.

Checks. The table was computed twice with no shared code: by a Codex prover (gpt-6.1-sol high on Mac mini 1, sympy,
its scripts cone_certificate.py and cone_extensions.py, kept with its log) and by `cone_recheck.py` here (integer
polynomials as dictionaries, the ray list derived as above), which also compares the polynomial in z with a direct
evaluation of H at six random rational points of the cone for each n (no mismatch) and asserts that every ray lies
in C. Output: `cone_recheck_56.out`, `cone_recheck_789.out`. The steps before the certificate are the split (in
Lean, an agent, brain bf2d35db) and the bound m >= M, which is a three-line computation and has not been
read by a second person yet.

What it gives and what it does not. With the formula Gval = 2 g^2 Psi(x) of "The two-eigenvalue family" this settles
that family at n = 5, 6, 7, 8 by the gap-weighted state. It is not a proof for general n: the number of rays grows
like n^2/4 and the certificate is a separate finite computation for each n. (Later: it cannot work for all n, the polynomial is negative at n = 14; see the last section.) The relaxation to measures fails (see
above), so a proof for all n has to keep the integer multiplicities, which is what the ray coordinates do; whether
the coefficients have a closed form in n is open.

Check of the steps before the certificate (`chain_check.py`, `chain_check.out`, exact rationals, about 4,000 points
of the cone for each n = 5, ..., 12, including points near the star and near the edge): n(n-1)a^2 - T > 0, m >= M,
and the identity n (n(n-1)a^2 - T) Psi - H = n (n-1) K (n(n-1)a^2 - T)(m - M) hold at every point, and every point
tested decomposes into the listed rays with nonnegative coefficients.


## After the prover's report: n = 9, zero padding, and the failure of Phi' >= 0 at n = 14 (11 Nov, 06:3x)

The Codex prover ended with PARTIAL (its text: `CODEX_PSI_PROOF.md`, log `CODEX_PSI_LOG.md`, scripts in
`codex_psi_scripts/`). Three things change the picture above.

1. Phi' >= 0 is false for large n. For y = (s, 1 repeated s times, -s, -s), n = s + 3,

       H_n(y) = -2 s^2 (s-1)(s+1)^4 (s+3)(s^2 - 11 s + 6)(s^2 + 4 s - 1),

   negative from s = 11. At n = 14, x = (11, 1 x 11, -11, -11)/sqrt(374): Phi' = -357073920/10106041 (about -35.3)
   while Psi = 28579680/54043 (about 528.8), with m = 11/34 against M = 1/374. So the bound m >= M throws away too
   much when the largest modulus is attained twice, and the remark "a separate finite computation for each n" in the section
   above is wrong as a route to all n: the coefficient certificate must fail at some n between 10 and 14. Psi itself
   is not touched. Rechecked here in exact rationals with the forms of chain_check.py (factorisation for s = 2..60,
   the n = 14 values): `phi_fails_n14_check.py`, `.out`.

2. Zero padding (prover's section 7; identities rechecked in the same script). With rho = 2q - 1, B = p^2,
   t = 2B - rho and C_n = (n-1)(n^2 + (rho - 5) n + 6), Psi_n = C_n m - ((n-4) t + 2B); C_n > 0 and increasing for
   n >= 5, and (n-4)/C_n and 1/C_n decrease, so Psi_n(x) >= 0 implies Psi_(n+1)(x, 0) >= 0 (m >= 0 always, since
   three reals of sum zero have two of one sign). Hence a certificate at n covers every vector of any length with
   at most n nonzero coordinates.

3. n = 9. `cone_recheck.py 9` (Mac mini 1, 355 s): 20 rays, 2,220,039 monomials, 0 negative, identity check exact,
   zero only on the star and edge rays (`cone_recheck_789.out`). This is one computation, by one program; the prover
   did not run n = 9, so it has one reader. n = 5..8 have two.

State of the two-eigenvalue family after this:

    Psi >= 0  proved for n = 5..8 (two independent exact computations), n = 9 (one);
              for every n >= 5 when at most 8 (resp. 9) coordinates are nonzero;
              for every n >= 5 when m >= 1/(n(n-1))  (the split, K >= 0, D >= 0);
              for every n >= 5 when x takes at most three distinct values (prover's section 8: three integer
              parametrisations of the multiplicities, coefficients nonnegative after splitting each of R, U, V
              into 0, 1, >= 2, one exceptional cell r = 1, t = 2, s >= 4 covered by m >= 1/(n(n-1)); not yet
              recomputed here, so one reader).
    Open:     n >= 10 with at least ten nonzero coordinates, at least four distinct values and m < 1/(n(n-1)).

What a proof for all n now needs. The loss is in m >= M, which is sharp only when a single coordinate carries the
largest modulus and the others are balanced. In the open region m < 1/(n(n-1)) the vector cannot have two large
coordinates of one sign, so a bound for m that uses the two largest coordinates of each sign (m >= x_1 x_2 and
m >= x_n x_(n-1)) together with the power sums is the natural replacement; the prover's reduction (its section 9:
at fixed S a minimiser of Phi has at most two distinct values strictly between -S and S) says where to look for the
extremal vectors of such a bound. Not done.

## n = 10 (11 Nov, 06:5x)

`cone_recheck2.py` computes the same coefficient certificate with a monomial z^e stored as the integer
sum_k e_k 16^k (no exponent exceeds 8, so products are sums of codes); about a fifth of the memory of the tuple
version. It reproduces the term counts 1,277 / 2,991 / 75,561 at n = 5, 6, 7 and 2,220,039 at n = 9 (115 s), and at

    n = 10:  21 rays, 3,108,067 monomials, 0 negative, identity check exact at three random rational points,
             zero only on the star ray (1) and the edge ray (1, 9), least coefficient 645120000000 (159 s, 1.1 GB).

So Psi >= 0 holds at n = 10, and by zero padding for every n and every vector with at most ten nonzero coordinates.
The program shares `rays` and `H_num` with cone_recheck.py and only the polynomial arithmetic is new, so n = 9 and
n = 10 each still have one reader of the ray construction. The count of rays grows to 30 at n = 11 (38.6 million
monomials of degree 8) and 43 at n = 14, out of reach for this method on a 16 GB machine; and the certificate must
fail by n = 14, where Phi' is negative at a point of the cone. (Superseded by the next section: n = 11, 12 are done.) Open then: n >= 11 with at least eleven nonzero
coordinates, at least four distinct values and m < 1/(n(n-1)).

## n = 11 and 12, and a third implementation for n = 5..10 (11 Nov, 07:1x)

`cone_dense.c` computes the coefficient certificate again with no code in common with cone_recheck.py,
cone_recheck2.py or the prover's sympy scripts: C with 128-bit integers, polynomials stored densely by the rank of
the monomial (a multiset of ray indices in the combinatorial number system), every product checked against an
overflow bound (at most binom(d, d_A) contributions of size max|A| max|B| to a coefficient; the bound stays below
2e18 against a limit of 1e37), and the whole array compared with the formula for H at three random points modulo
2^61 - 1. The rays are not taken from the closed formula: `rays_enum.py` finds the extreme rays of
C = {sum x = 0, x_1 >= ... >= x_n, x_1 + x_n >= 0} by trying every set of n - 2 of the n inequalities as the tight
ones (exact rationals), and the two lists agree for n = 5, ..., 14.

     n   rays    monomials     nonzero     negative   identity check   seconds
     5     6         1,287       1,277         0          3 of 3          0.0
     6     7         3,003       2,991         0          3 of 3          0.0
     7    12        75,582      75,561         0          3 of 3          0.1
     8    13       125,970     125,947         0          3 of 3          0.1
     9    20     2,220,075   2,220,039         0          3 of 3          2.5
    10    21     3,108,105   3,108,067         0          3 of 3          4.0
    11    30    38,608,020  38,607,965         0          3 of 3         41.7
    12    31    48,903,492  48,903,435         0          3 of 3         54.6

(Mac mini 1 for n <= 10, Mac mini 2 for n = 11, 12; outputs `dense_n9_10.out`, `dense_n11_12.out`.) The nonzero
counts for n = 5..10 are those of the earlier programs, so n = 9 and n = 10 now have two independent computations
and an independent derivation of the rays. In every case the pure powers vanish only on the star ray and the edge
ray, and the least coefficient sits on the two-face of the last two rays.

n = 11 and n = 12 are new: H has no negative coefficient, so Phi' >= 0 on the cone and Psi >= 0 for n = 11, 12,
and by zero padding for every n and every vector with at most twelve nonzero coordinates. These two rest on one
program (cone_dense.c) and one ray derivation checked against the formula.

Where the certificate must stop: on x = (p, t x (n-3), -q, -q) and its relatives H is nonnegative for n = 11, 12,
13 and negative at n = 14 (`h_scan.py`), in line with the factorisation above. n = 13 has 42 rays and
450,978,066 monomials; `cone_chunk.c` (built from cone_dense.c by `mk_chunk.py`) forms the product one chunk at a
time, a chunk being the monomials with a given smallest ray index, so that the peak is binom(k+6, 7) coefficients.
It reproduces the n = 10 line exactly.

## n = 13, and a family with one positive coordinate for every n (11 Nov, 07:3x)

`cone_chunk.c` at n = 13 (Mac mini 2, one core, 1,113 s):

    n = 13:  42 rays, 450,978,066 monomials, 450,977,988 nonzero, 0 negative, identity check 3 of 3,
             pure powers zero only on the star ray and the edge ray, least coefficient 123552 on the
             two-face of the last two rays, largest 6.49e18 (overflow bound 1.5e19 against 1e37).

Output `chunk_n13.out`. So H has no negative coefficient at n = 13, Phi' >= 0 on the cone, and Psi >= 0 for n = 13
and for every vector with at most thirteen nonzero coordinates. Like n = 11 and 12 this rests on one program and
one ray derivation. At n = 14 the same computation has to show negative coefficients, since Phi' is negative at
y = (11, 1 x 11, -11, -11); n = 13 is therefore the last n this certificate can reach.

The step from n to "at most n nonzero coordinates" (zero padding, section 7 of the prover's note) has been checked
in Lean by an agent: `06_math_research/lean_checks_agent/t104_pad/`, commit b78e4e14, eight theorems,
standard axioms only.

A family for every n. Take one positive coordinate and negatives with three values, the outer two of multiplicity
one, and any number of zeros:

    x = (a, -tau, -t (k times), -b, 0 (j times)),   a = tau + k t + b,   0 <= tau <= t <= b,   n = k + 3 + j >= 5.

The only positive products of two coordinates are among the negatives, so m T = b t. Put tau = z1, t = z1 + z2,
b = z1 + z2 + z3 with z >= 0. Then T^3 Psi is a form of degree 6 in z with coefficients in Z[k, j], and
`one_positive_family2.py` finds that each of its 27 coefficients, written in kappa = k - 2 and j (the case k >= 2),
or in j - 1 with k = 1 (the case k = 1, j >= 1), is a polynomial without a negative coefficient. The monomial z3^6
is absent (the edge vector, tau = t = 0), and the coefficient of z1^6 carries the factor j (the star, tau = t = b
and no zeros). The form agrees exactly with Psi computed from the definition, m by brute force over pairs, at 300
random rational points with k <= 9, j <= 5. Every other coefficient has a positive constant term in these variables (`one_positive_eq.py`).
Hence Psi >= 0 on this family for every n, with equality only at the
star and the edge. The family has up to five distinct values and reaches into the region m < 1/(n(n-1)) with all
coordinates nonzero (k large, j = 0), which neither the three-value result nor zero padding covers; it is the
simplest piece of the star-like component of that region.

State. Psi >= 0 is proved for n = 5, ..., 13; for every n when at most thirteen coordinates are nonzero, or
m >= 1/(n(n-1)), or at most three distinct values, or on the family above. Open: n >= 14 with at least fourteen
nonzero coordinates, at least four distinct values, m < 1/(n(n-1)), outside that family. `h_region_scan.py` looked
for a negative H inside the region m < T/(n(n-1)) for n = 14, ..., 50 and found none, but its grid puts only a few
hundred points there, so it settles nothing.

## One positive coordinate: the two extreme arrangements (11 Nov, 07:33)

Write a vector with one positive coordinate as x = (a, -b, -t, -y_1, ..., -y_r), b >= t >= y_i >= 0,
a = b + t + sum y, r = n - 3. Then m T = b t whatever y is, and for fixed b, t, sum y the vectors y are ordered by
majorisation between the equal one, y_i = sum y / r, and the spread one, (t, ..., t, tau, 0, ..., 0). The spread
arrangement is the family of the previous section. The equal arrangement is

    x = (a, -b, -t, -u (k times)),   0 <= u <= t <= b,   a = b + t + k u,   n = k + 3,

and with u = z1, t = z1 + z2, b = z1 + z2 + z3 the form T^3 Psi again has no negative coefficient as a polynomial
in k - 2 (26 monomials; `one_positive_reduce.py`). So Psi >= 0 at both ends of the majorisation order, for every n.

That does not yet give all one-positive vectors. On 200,000 random ones (n = 5, ..., 40, several shapes of y) Psi
was never negative; T^3 Psi was below its value at the equal arrangement in 9 percent of the samples and below its
value at the spread arrangement in 89 percent, and below both in 27 samples, by at most 2.2e-4 in Psi at points
where Psi is near 2.9. So Psi is not minimised over y at one of the two ends, though it is close to it; a proof for
one positive coordinate needs either a third family (y with two values) or monotonicity along a path between the
ends. T^3 Psi is linear and increasing in sum y^4, concave and increasing in sum y^3, and a cubic in sum y^2, at
fixed a, b, t.

## Psi >= 0 for every vector with exactly one positive coordinate, every n (11 Nov, 07:44)

Proposition. Let n >= 5 and x in R^n with sum x = 0 and exactly one positive coordinate (or exactly one negative
one; Psi(-x) = Psi(x)). Then Psi(x) >= 0.

Proof. Write x = (a, -y_1, ..., -y_(n-1)) with y_1 >= ... >= y_(n-1) >= 0 and a = sum y. Every product of two
coordinates is <= 0 except those of two negative coordinates, and n - 1 >= 2, so m T = y_1 y_2 and

    G := T^3 Psi = (n-4)(2Q - T^2) T - 2(n-3) P^2 + (n-1)((n^2-6n+6) T^2 + 2nQ) y_1 y_2

is a polynomial in y, homogeneous of degree 6. Put w_i = y_i - y_(i+1) >= 0 (y_n = 0), so y_i = w_i + ... +
w_(n-1); the w_i are free nonnegative variables, and it is enough that G, as a polynomial in w, has no negative
coefficient. A monomial of degree 6 contains at most six of the variables, say those with indices
i_1 < ... < i_r, r <= 6, and its coefficient is unchanged when every other w_i is put to zero. That substitution
gives the vector with r levels

    v_1 > ... > v_r > 0,  v_s = z_s + ... + z_r  (z_s = w_(i_s)),  taken c_1 = i_1, c_s = i_s - i_(s-1) times,
    and j = n - 1 - i_r zeros,

and y_1 y_2 = v_1 v_2 if c_1 = 1 (v_1 * 0 if also r = 1), y_1 y_2 = v_1^2 if c_1 >= 2. So the coefficients of G
for all n are among the coefficients of twelve explicit forms G_r(z; c, j), r = 1, ..., 6, in the two shapes
c_1 = 1 and c_1 >= 2, whose coefficients are polynomials in the integers c_s >= 1 and j >= 0. Written in
g_s = c_s - 1 (g_1 = c_1 - 2 in the second shape) and j, none of these polynomials has a negative coefficient
(`one_positive_all.py`, output `one_positive_all_r4_6.out` and the r <= 3 lines below). Hence every coefficient of
G is >= 0 and G >= 0 on w >= 0.  []

    r   shape c_1 = 1          shape c_1 >= 2
    1    0 monomials (edge)      1, none negative
    2    6, none negative        7, none negative
    3   27, none negative       28, none negative
    4   83, none negative       84, none negative
    5  209, none negative      210, none negative
    6  461, none negative      462, none negative

Checks. The forms are built in the sparse polynomial ring Z[z, g, j] of sympy. `one_positive_all_check.py` builds
them again, evaluates them at 311 random integer points (r <= 4, both shapes) and finds exact agreement with
T^3 Psi computed from the definition, m as the maximum over all pairs; and Psi computed exactly from the
definition is >= 0 on 20,000 random integer vectors with one positive coordinate, n <= 60. The two families of
the previous sections are the cases r <= 3 of this.

What this covers and what it does not. The argument uses that the cone {one positive coordinate, sorted} is
simplicial with the increments as free coordinates and that m T is a single polynomial there. For two or more
coordinates of each sign m T = max(x_1 x_2, x_n x_(n-1)) is a maximum of two polynomials; the cone of all sorted
vectors with sum zero is still simplicial (rays (n-k repeated k times, -k repeated n-k times), k = 1, ..., n-1),
and the same six-level reduction applies to any single polynomial lower bound for m T, so a bound for m that is
polynomial on a fixed finite subdivision of that cone would give all n by a finite computation. Phi' is such a
bound and fails at n = 14, so a sharper one is needed. One reader so far.

## Two or more coordinates of each sign: a polyhedral split (11 Nov, 07:50)

Sort x decreasingly and write A = x_1 x_2, B = x_n x_(n-1), so m T = max(A, B), and Psi_A, Psi_B for Psi with m
replaced by A/T, B/T. Psi increases with m, hence Psi >= Psi_A, Psi_B.

Smooth lower bounds for the maximum do not work. With m T >= (A^(p+1) + B^(p+1)) / (A^p + B^p) (valid for
A, B >= 0) the resulting bound for Psi is negative for p = 0 at every n, for p = 1 from n = 14, for p = 2 from
n = 30 and for p = 4 at n = 40 (`powmean_scan.py`): near the star, with a small second positive coordinate chosen
so that A is comparable to B, Psi is close to 0 and any loss in m of fixed relative size is too much.

A split along hyperplanes does better. Negating x if necessary, x_1 + x_n >= 0. Then

    R1 = {x_2 + x_(n-1) >= 0}:  if x_(n-1) <= 0 then x_2 >= |x_(n-1)| and x_1 >= |x_n|, so A >= B and Psi = Psi_A
                                 (if x_(n-1) > 0 there is one negative coordinate, done above);
    R2 = {x_2 + x_(n-1) <= 0}:  claim Psi_B >= 0, although A > B on a large part of R2.

`split_scan.py` (n = 5, ..., 60; 40,000 samples per n of six shapes, then a local search minimising Psi_B inside
R2): Psi_B has no negative value on R2 beyond rounding at the star (about 1e-13), and its least value moves away
from 0 as n grows once the search leaves the star. A > B in a third to a half of the samples in R2.

So the conjecture for the two-eigenvalue family would follow from two polynomial inequalities of degree 6 on
polyhedral cones,

    (I)   T^3 Psi_A >= 0 on {sorted, sum 0, x_1 + x_n >= 0, x_2 + x_(n-1) >= 0},
    (II)  T^3 Psi_B >= 0 on {sorted, sum 0, x_1 + x_n >= 0, x_2 + x_(n-1) <= 0},

and (I) is the conjecture itself on R1, with nothing lost. Both cones have explicit extreme rays, and a sextic
written in nonnegative combinations of rays touches at most six rays in each monomial, so if the coefficients are
nonnegative the six-level reduction of the previous section would turn each into a finite computation valid for
all n. Not yet tested exactly; the first step is the coefficient test in ray coordinates for n = 5, ..., 14, where
n = 14 is the case the old certificate cannot reach.

## Psi >= 0 for every n: an elementary argument for n >= 14 (11 Nov, 08:11)

Statement. For every n >= 5 and every x in R^n, x != 0, with sum x = 0, Psi(x) >= 0. For n = 5, ..., 13 this is
the cone certificate above. For n >= 14 it follows from the three steps below. Two readers (11 Nov):
an agent, by hand and in exact arithmetic for n = 14, ..., 3000, found no gap, and then checked Steps 1 to 3
in Lean (`06_math_research/lean_checks_agent/t104_all_n`, commit 628d7761, standard axioms only, with looser
constants in Step 3; the whole statement, normalisation included, is
`06_math_research/lean_checks_agent/t104_all_n_full`, commit 952215e, theorem T104Full.psi_nonneg); a Codex referee on Mac mini 1,
working from a copy with no history (`AUDIT_CODEX_ALLN_NOTE_AS_READ.md`, brief `AUDIT_CODEX_ALLN_BRIEF.md`), reports
the theorem SOUND once two small gaps are filled, and one side remark wrong (`AUDIT_CODEX_ALLN_REPORT.md`). Its corrections are marked [referee] below.

Notation. T, P, Q the power sums of degree 2, 3, 4, q = Q/T^2, p^2 = P^2/T^3, C = (n-1)(n^2-6n+6+2nq) > 0,
Psi = (n-4)(2q-1) - 2(n-3)p^2 + C m, m = max_(i<j) x_i x_j / T. For a number M <= m T write
G_M = (n-4)(2Q - T^2) T - 2(n-3) P^2 + (n-1)((n^2-6n+6) T^2 + 2nQ) M, so T^3 Psi >= G_M.

Step 1 (large m). Psi = 2(n-3)(q - p^2 - 1/n) + C (m - 1/(n(n-1))), an identity. The Gram determinant of the
vectors (1, ..., 1), x, (x_i^2) is n(TQ - P^2) - T^3 >= 0, that is q - p^2 >= 1/n. Hence Psi >= 0 whenever
m >= 1/(n(n-1)).

Normalisation. Sort x decreasingly; if x_1 + x_n < 0 replace x by -x and sort again [referee: the sign change
reverses the order; without the second sort (1, ..., 1, -(n-1)) is returned unchanged with b = n-1]; scale:
x_1 = 1 >= b := -x_n > 0 (a nonzero sum-zero vector has x_1 > 0 > x_n).
  (I)  x_2 + x_(n-1) >= 0. Then eps := x_2 >= 0 (otherwise x_(n-1) <= x_2 < 0), the middle coordinates
       x_2, ..., x_(n-1) lie in [-eps, eps], and m T >= M := x_1 x_2 = eps.
  (II) x_2 + x_(n-1) <= 0. Then eps := -x_(n-1) >= 0 (otherwise x_2 >= x_(n-1) > 0), the middle coordinates lie in
       [-eps, eps], and m T >= M := x_n x_(n-1) = b eps.
In both cases Y2 := sum of the squares of the middle coordinates <= (n-2) eps^2, T = 1 + b^2 + Y2, and
delta := 1 - b = -(sum of the middle coordinates) lies in [0, (n-2) eps].

Step 2 (eps not small). (I): T <= 2 + (n-2) eps^2, so M/T >= eps / (2 + (n-2) eps^2) >= 1/(n(n-1)) as soon as
(n-2) eps^2 - n(n-1) eps + 2 <= 0; this convex quadratic is <= 0 at eps = e1 := 2.1/(n(n-1)) and at eps = 1,
hence on [e1, 1]. (II): b >= max(eps, 1 - (n-2) eps) and b eps / (1 + b^2 + (n-2) eps^2) increases with b on
[0, 1] (its derivative has the sign of 1 + (n-2) eps^2 - b^2). For eps >= 1/(n-1) take b = eps: M/T >= eps^2 / (1 + (n-1) eps^2) >= 1/(n(n-1)). For eps <= 1/(n-1) take
b = 1 - (n-2) eps: M/T >= 1/(n(n-1)) is the inequality -(n-2)(n^2-1) eps^2 + (n^2+n-4) eps - 2 >= 0, whose roots
are e2 := 2/((n-2)(n+1)) and 1/(n-1) (the second is the star). So in (II) Step 1 applies for eps >= e2, and
e2 <= e1 for n >= 7.

Step 3 (eps <= e1, a perturbation of the edge vector (1, 0, ..., 0, -1)). Here kappa := (n-1)/(n+1) <= M/eps
(in (II), b >= 1 - (n-2) e2 = kappa), Y2 <= (n-2) e1^2 <= 0.002, 1 <= T <= 2.002, and

    2Q - T^2 = (1 - b^2)^2 + 2 Y4 - 2(1 + b^2) Y2 - Y2^2 >= -4 Y2 - Y2^2,
    P = (1 - b^3) + Y3,  0 <= 1 - b^3 <= 3 delta <= 3(n-2) eps,  |Y3| <= eps Y2,   Q >= 1,

    G_M >= -(n-4) T (4 Y2 + Y2^2) - 2(n-3) (3(n-2) eps + eps Y2)^2 + (n-1)((n^2-6n+6) T^2 + 2n) kappa eps.

The first term is at most 4.002 (n-4)(n-2) e1 T eps, less than one hundredth of (n-1)(n^2-6n+6) kappa T eps
<= (n-1)(n^2-6n+6) kappa T^2 eps; the second is at most 2(n-3)(3(n-2) + 0.002)^2 e1 eps <= 37.9 (n-2) eps; and
0.99 (n-1)(n^2-6n+6)(n-1)/(n+1) >= 37.9 (n-2) for n >= 14 (1316.172 against 454.8 at n = 14).
So G_M >= 0, hence Psi >= 0.  []

[referee] Why the comparisons hold for every n >= 14 and not only where they were computed. Put
D = (n-1)^2 (n^2-6n+6)/(n+1), the main coefficient per unit eps.
(a) (n-2)/(n^2 (n-1)^2) decreases for n >= 3, so Y2 <= (n-2) e1^2 <= 27/16900 < 0.002.
(b) 4.002 (n-4)(n-2) e1 < 4.002 * 2.1 < 8.41 < 13.29 < D(14)/100, and D increases for n >= 5 (the factors
    (n-1)^2/(n+1) and n^2-6n+6 are positive and increasing).
(c) 2(n-3)(3(n-2) + 0.002)^2 e1 / (n-2) = (189/5) ((n-3)(n-2)/(n(n-1))) (1 + 1/(1500(n-2)))^2
    < (189/5)(18001/18000)^2 < 37.9.
(d) D/(n-2) = n^2 - 7n + 14 - (18n - 34)/(n^2 - n - 2) has derivative 2n - 7 + (18n^2 - 68n + 70)/(n^2-n-2)^2 > 0
    for n >= 4 (the quadratic has negative discriminant), and 0.99 D(14)/12 = 109.68 > 37.9.
For eps = 0 the vector is the edge vector and Psi = 0; for eps > 0 the bound of Step 3 is strict.

Equality: the edge vector (eps = 0) and, in Step 2 (II), the star (eps = b = 1/(n-1)); no others up to scaling,
permutation and sign [referee]. For eps > 0 Step 3 is strict. In Step 1 equality needs q - p^2 = 1/n, that is
x_i^2 = alpha + beta x_i for all i, so x takes two values, and m = 1/(n(n-1)); if both values are repeated then
m >= 1/n, so one of them occurs once and x is the star vector.

Checks. `all_n_check.py`: the scalar facts of Steps 2 and 3 for n = 14, ..., 2000 in exact arithmetic, and
22,260 vectors built region by region (n = 14, ..., 40, 50, 64, 100, 150, 257; middle coordinates random, all
+-eps, all of one sign, sparse) on which every displayed inequality is asserted exactly. `all_n_check2.py`:
arbitrary sum-zero vectors of eight shapes (near the edge, near the star, few values, thresholds near
2/(n(n-1)), ...), normalised and classified afterwards; all four cases occur (I large 2,169, I small 558, II large
2,066, II small 532) and the step that applies holds on each. [referee] The remark first made here, that the same
computation goes through from n = 10, was wrong as printed: with the constants above the argument closes from
n = 13 (at n = 10, 11, 12 the bound Y2 <= 0.002 fails, for instance x = (1, 7/300 four times, -7/300 four times,
-1) at n = 10 has eps = e1 and Y2 = 49/11250). With 0.005 in place of 0.002 and one fiftieth in place of one
hundredth it closes from n = 10 (`all_n_remark2_check.py`, exact). Nothing in the theorem depends on it.

The split of the previous section, tested exactly. Independently of the argument above, T^3 Psi_A on R1 and
T^3 Psi_B on R2, written in the extreme rays of the two cones, have no negative coefficient: sympy for
n = 5, ..., 11 (`split_cert.py`, `split_cert_5_8.out`; an agent with separate code for n = 5, ..., 10), and
a dense C program with 128-bit integers and an identity check modulo 2^61 - 1 (`split_dense.c`, rays from
`split_rays.py`, run on Mac mini 2):

    n=9 A rc=0 10:03 RESULT n=9 mode A rays 19 negative 0 identity 3/3 time 0.1 s
    n=9 B rc=0 10:03 RESULT n=9 mode B rays 17 negative 0 identity 3/3 time 0.0 s
    n=10 A rc=0 10:03 RESULT n=10 mode A rays 20 negative 0 identity 3/3 time 0.1 s
    n=10 B rc=0 10:03 RESULT n=10 mode B rays 18 negative 0 identity 3/3 time 0.0 s
    n=11 A rc=0 10:03 RESULT n=11 mode A rays 29 negative 0 identity 3/3 time 0.7 s
    n=11 B rc=0 10:03 RESULT n=11 mode B rays 26 negative 0 identity 3/3 time 0.4 s
    n=12 A rc=0 10:03 RESULT n=12 mode A rays 30 negative 0 identity 3/3 time 0.9 s
    n=12 B rc=0 10:03 RESULT n=12 mode B rays 27 negative 0 identity 3/3 time 0.5 s
    n=13 A rc=0 10:03 RESULT n=13 mode A rays 41 negative 0 identity 3/3 time 6.0 s
    n=13 B rc=0 10:03 RESULT n=13 mode B rays 37 negative 0 identity 3/3 time 3.1 s
    n=14 A rc=0 10:03 RESULT n=14 mode A rays 42 negative 0 identity 3/3 time 6.9 s
    n=14 B rc=0 10:04 RESULT n=14 mode B rays 38 negative 0 identity 3/3 time 3.5 s
    n=15 A rc=0 10:04 RESULT n=15 mode A rays 55 negative 0 identity 3/3 time 35.9 s
    n=15 B rc=0 10:04 RESULT n=15 mode B rays 50 negative 0 identity 3/3 time 19.4 s
    n=16 A rc=0 10:05 RESULT n=16 mode A rays 56 negative 0 identity 3/3 time 40.0 s
    n=16 B rc=0 10:06 RESULT n=16 mode B rays 51 negative 0 identity 3/3 time 21.9 s

The ray counts are s^2 + s - 1 and s^2 + s for n = 2s + 1, 2s + 2 on R1. n = 14 is the first case the old
certificate (the bound Phi') cannot reach; there the old certificate has 31 negative coefficients, all in
monomials containing the seventh power of one ray (`chunk_n14.out` on Mac mini 2).

## What Psi >= 0 gives: Conjecture F on graphs with two Laplacian eigenvalues (11 Nov, 08:41)

Proposition. Let n >= 5 and let G be a weighted graph on n vertices whose Laplacian has spectrum
{0, mu (n-2 times), lam} with 0 <= mu <= lam. Then Conjecture F of HOOKS_AND_TWO_ROWS.md holds for G:

    lambda_min(G, [2,1^(n-2)]) >= ((n-2)/(n-1)) lambda_min(G, [2,2,1^(n-4)]),

which for this pair is stronger than the constant 2/3 of Conjecture 1.5 of arXiv 2610.22151. Equality on the star
(mu = 1, lam = n) and on a single edge (mu = 0).

Proof. If mu = lam, G is a multiple of the complete graph, 2W/(n-1) = lam, and F in its first form
lam <= (2W + (n-2) lambda_max(G, [n-2,2]))/(n-1) is clear. Let g = lam - mu > 0 and x the unit top eigenvector.
Then L_G = lam x x^t + mu (Pi - x x^t), N = lam Pi - L_G = g Q with Q the projection onto {1, x}^perp, and
w_ij = mu/n - g x_i x_j, so the weights are nonnegative exactly when lam >= g (1 + n m), m = max_(i<j) x_i x_j.
By consequence 2 above Gval is affine and nondecreasing in lam for fixed (N, x), and at lam = g (1 + n m) it equals
2 g^2 Psi(x) >= 0. So Gval(G) >= 0. The state is admissible: tau = g (n-2) > 0, and the normalisation of Reduction R
is Z = 1 - 2(n - 1 - n q)/(n-2)^2 >= 1 - 2/(n-2) > 0 because q = sum x_i^4 >= 1/n. Section 5 (d) of
HOOKS_AND_TWO_ROWS.md then gives F for G.  []

These graphs are the rank-one changes of the complete graph, w_ij = c - g x_i x_j; they form a family of dimension
n in the cone of weighted graphs (dimension n(n-1)/2), containing both equality cases of F. The proposition says
nothing about a graph with three or more distinct nonzero Laplacian eigenvalues.

Direct check, not using Psi or Gval (`family_F_check.py`, `family_F_check.out`): Specht modules in Young's
orthogonal form, 2,030 / 2,040 / 2,050 graphs of the family for n = 5, 6, 7 (random x, near the star, near the edge,
few values, heavy-tailed; mu at the least admissible value and at 1.001, 1.1, 2, 10 times it). The smallest ratio
lambda_min(tau)/lambda_min(sigma) is 0.750000000, 0.800000000, 0.833333333, attained at the star.

Status of the proposition: one author; it rests on Psi >= 0 (two readers and a Lean check for n >= 14; n = 5, ..., 13 by the cone
certificate, by two programs up to n = 10; n = 10, ..., 13 also by the argument with the repaired constants) and on
Reduction R and 5 (d) as corrected after the first referee.

## n = 5: Gval < 0 next to a double top eigenvalue (11 Nov, 10:20)

Gval = tr(M N) is the quantity of the section "The inequality", with x the unit top eigenvector of L_G, lam its
eigenvalue, N = lam Pi - L_G and W = 1. Files gval_n5_check_lib.py, gval_n5_check2.py, gval_n5_check2.out.

Two local minimisers of Gval over weighted graphs on 5 vertices have a double top eigenvalue: spectra
(0, 0.0588, 0.6469, 0.6471, 0.6471) and (0, 0.0386, 0.6538, 0.6538, 0.6538). Over the unit vectors x of the top
plane Gval runs from -2.40e-3 to +0.482 (second graph: -1.43e-3 to +0.486) and is negative on a fraction 0.047
(0.036) of the circle. At the double point any x of the plane may be chosen, so the double point itself decides
nothing. Next to it the choice is forced: adding delta H, H the graph with weights max(0, -x_i x_j) for the worst x,
makes that x the unique top eigenvector, and

    gap      1e-6        1e-5        1e-4        1e-3       1e-2
    Gval    -2.396e-3   -2.338e-3   -1.764e-3   +3.98e-3   +6.08e-2      (first graph)
    Gval    -1.425e-3   -1.370e-3   -7.88e-4    +5.07e-3   +6.31e-2      (second graph)

so Gval is about 6.4 gap - 0.0024 along this line. A search with the gap bounded below finds Gval = -2.83e-3 at gap
9.8e-5 and -1.87e-3 at gap 2.95e-4 (second start: -1.44e-3 and -1.7e-4).

Consequence. Gval >= 0 is false at n = 5 on weighted graphs with a simple top eigenvalue, in a neighbourhood of the
graphs with a double one (gap up to about 3e-4 at lam = 0.65). The state built from the single top eigenvector
therefore does not prove the comparison at n = 5 on all graphs; near a multiple top eigenvalue the state has to use
the whole near-top eigenspace. Proposition 1 of N4_PROOF.md asks only for some state, so Conjecture F is not
affected, and the theorem for graphs with two Laplacian eigenvalues is not affected (there the top eigenvalue is
simple or the bottom one is).

Status: numerical, one implementation of M; the value with a prescribed x (gval_x) and the value with the computed
top eigenvector (gval) agree to three digits at gap 1e-6. Not recomputed independently.

## n = 5: the failure next to a double top eigenvalue is a matter of which x (12 Nov, 00:25)

Files state_mix_n5.py, state_mix_n5.out, state_mix_n5_id.py, state_mix_n5_id.out. V_[3,2] is modelled by the
symmetric 5 x 5 matrices with zero diagonal and zero row sums, S_5 acting by conjugation; no formula for Gval is
used. For a unit sum-zero x put N_x = the positive part of Q (x^t L x Pi - L_G) Q, Q the projection onto
{1, x}^perp, and D_x = sum_k g_k a_k a_k^t / trace with a_k the [3,2] component of (x y_k^t + y_k x^t)/sqrt 2.
D_x is a density matrix for every x, so

    slack(G) = 3 lambda_max(G, [3,2]) - 4 lam + 2W >= s(G, x) := 3 tr(D_x L(G, [3,2])) - 4 lam + 2W.

Agreement of the two implementations. With x the top eigenvector and Dt the unnormalised state,
Gval = 3 tr(Dt L) - (4 lam - 2W) tr Dt on 300 random graphs with gap >= 1e-3 (ratio 1 to 4e-13). So the section
above is reproduced by independent code: s(G, top x) < 0 at gap 1e-6, 1e-5, 1e-4 next to both graphs (first graph
-0.214, -0.209, -0.155, and -0.041 at gap 3e-4; second graph -0.384, -0.369, -0.202), positive from gap 1e-3 on.

What the plane gives. At the same graphs, W = 1:

                             true slack   s(G, top x)   max of s(G, x) over the plane of the top two eigenvectors
    first graph,  gap 1e-6     3.2168       -0.214        1.475
    first graph,  gap 1e-4     3.2167       -0.155        1.475
    second graph, gap 1e-6     3.2615       -0.384        1.425
    second graph, gap 1e-4     3.2613       -0.202        1.425

On the circle of the plane s is negative on a fraction 0.045 (0.035) of the angles; the eigenvector that the
perturbation H selects lies in that arc by construction. Over 400 random perturbations of each graph (size 1e-6
to 3e-3) the maximum over the plane stays above 1.437 (1.403).

Reading. These two graphs are far from extremal for Conjecture F (slack 3.2 against lam = 0.65), and the negative
value of Gval there says nothing about the conjecture: it is produced by forcing x to be the eigenvector of a nearly
double eigenvalue. A state D_x with x chosen in the near-top eigenspace has a wide margin. What is not shown: that
max over the plane of s(G, x) is nonnegative on all weighted graphs on 5 vertices. That is a min-max search
(minimise over graphs the maximum over the plane), the next computation. The last column of state_mix_n5.out
("plane-supported") is empty of content at n = 5: the vectors a(x, y) with x in the plane span all of V_[3,2],
which has dimension 5.

Status: numerical, two implementations agree on the single-eigenvector state; the plane values come from one
implementation.

## n = 5: the min-max search, the stars with isolated vertices, and a state without a chosen eigenvector (12 Nov, 07:08)

The search (minmax_n5.py, minmax_n5.out; Mac mini 1, 300 starts, seed 21, 23,167 s). F(G) = max over unit x in the
plane of the top two Laplacian eigenvectors of s(G, x), minimised over the weights by Nelder-Mead from ten families
of starts. No negative value; the smallest F is -9.8e-15. The 300 end points:

     95  a single edge                              F = 0 (to 2e-7), slack 0
     53  the uniform star K_{1,4}                   F = 0 (to 2e-7), slack 0
     49  K_{1,2} and two isolated vertices          F = 0.0200, slack 1/2
     22  K_{1,3} and one isolated vertex            F = 0.0145, slack 2/3
      5  a triangle and two isolated vertices       F = 1.00, slack 4.00
     40  next to a nearly double top eigenvalue     F from 1.32 to 1.46, slack 2.7 to 3.3
     36  stopped before convergence: 25 on the way to the edge (F/slack at least 0.81), 3 on the way to the star,
         8 near K_{1,2} or K_{1,3} (F from 0.0146 to 0.21)

The zeros of F that the search finds are the two graphs where the slack itself is zero, and the two other low end
points are stars with isolated vertices. Next to the uniform star F is far below the slack (F = 7e-5 at slack
6e-3), as it would be if F were of second order there and the slack of first order.

The stars with isolated vertices, exactly (star_gval_exact.py, star_gval_exact.out; star_states_n.py,
star_states_n5.out). At K_{1,k} with n-1-k isolated vertices and weights 1/k the top eigenvalue (k+1)/k is simple,
and the value of the gap-weighted state at the top eigenvector follows from the closed form of Gval in rational
arithmetic. For n = 5 and k = 1, 2, 3, 4 it is 0, 1/50, 1/69, 0: the two low end points of the search. The explicit
model gives 0.020000 and 0.014493, so the closed form and the model agree at these graphs. For n = 5 to 40 and
1 < k < n-1 the value is positive; it is smallest at k = n-2 (3/196 at n = 6, 6/445 at n = 7, 5/438 at n = 8,
333/549062 at n = 40) and decreases roughly like 1/n^2. On this family the top-eigenvector state does not fail, and
its margin tends to zero.

The true slack at K_{1,2} and K_{1,3} for n = 5 is 1/2 and 2/3. The maximum of s(G, x) over all unit sum-zero x, not
only the plane, equals the slack at both (0.500000 and 0.666667, multi-start Nelder-Mead), and the maximising x has
a large component on the isolated vertices. So the family D_x contains an exact state at these graphs, and the
plane of the top two eigenvectors is not where it lies.

A state that does not choose an eigenvector (beta_state_n5.py, beta_state_n5.out). For the Laplacian eigenpairs
(lam_k, u_k) on the sum-zero space put

    D_beta = sum over lam_k > lam_l of exp(beta (lam_k - lam)/lam) (lam_k - lam_l) a_kl a_kl^t / trace,
    a_kl = the [3,2] component of (u_k u_l^t + u_l u_k^t)/sqrt 2,      s_beta(G) = 3 tr(D_beta L(G, [3,2])) - 4 lam + 2W.

D_beta is a function of L_G alone and continuous in G; beta to infinity gives the top-eigenvector state where the
top eigenvalue is simple. Values (W = 1; the last two rows are the smallest value over 400 perturbations of size
1e-6 to 3e-3 of the two graphs with a double top eigenvalue):

                                slack    beta = 3      10       30      100      1e6
    K_{1,2}, two isolated       0.500     -0.0720   0.0191   0.0200   0.0200   0.0200
    K_{1,3}, one isolated       0.667     -0.0381   0.0142   0.0145   0.0145   0.0145
    first graph, perturbed      3.22       1.428    1.429    1.430    1.433   -0.172
    second graph, perturbed     3.26       1.385    1.386    1.387    1.391   -0.128

For beta from 30 to 300 the failure next to a double top eigenvalue is gone (at least 1.38 on every perturbation)
and the star values are those of the top state. On 20,000 graphs drawn from the ten families, not optimised, the
smallest value is zero to rounding for every beta from 10 up.

One fixed beta is not enough. At beta = 10 a minimisation started near the uniform star ends at -1.58e-8 (leaf
weights 0.250089, 0.25, 0.25, 0.249911; slack 3.8e-4), twice from different starts. Next to the star the pairs
inside the second eigenspace enter at first order in the distance with weight exp(-0.8 beta), against a margin of
the top state of second order, which puts the minimum at the order of -exp(-1.6 beta): 1e-7 at beta = 10, 1e-21 at
beta = 30, where double precision cannot see it. The quantity to minimise over graphs is H(G) = max over beta of
s_beta(G).

Queued: minbeta_n5.py on Mac mini 1 (2,000 starts, seed 31, thirteen families of starts, four objectives a start:
s_10, s_30, s_1e6 as a control, and H over beta in {3, 10, 30, 100, 300, 1e3, 1e4, 1e6}). Smoke test on the
laptop, 13 starts: the control is negative at both graphs with a double top eigenvalue (-0.39, -0.47); H and s_30
are never below -1e-15.

Status: numerical. The search for F is one implementation and one optimiser. The star values are exact and agree
with the model. Nothing here is a proof; Conjecture F at n = 5 is open.

## Stars with isolated vertices, n = 6 to 8 (12 Nov 08:18)

Files: star_states_n6_8.out (first search: Nelder-Mead in all x from 40 starts), star_struct_check.py, .out
(x in the span of the top eigenvector, the leaf block, the star against the isolated vertices and the isolated
block) and star_struct_check2.py, .out (x in the span of the top eigenvector, the star against the isolated
vertices and the differences leaf-leaf, leaf-isolated, isolated-isolated; 150 starts, then a polish in all x).
The graph is K_{1,k} with weights 1/k and m = n - 1 - k isolated vertices.

With m = 1 or m = 2 the maximum of s(G, x) over x equals the slack at every such star for n = 6, 7, 8, in both
structured searches (six stars each). The first search missed this at K_{1,6} + 1 for n = 8, where it stopped at
0.103 against the slack 0.833333; its values are those of a local search. Maximisers found: the top eigenvector
plus the difference of the two isolated vertices, or plus the star against the isolated vertices (m = 2); an
isolated vertex against a leaf (m = 1). This agrees with n = 5, where both stars have m <= 2 and attain the slack.

With m >= 3 all three searches stop at the same value, far below the slack (second structured search):

    n = 6:  K_{1,2} + 3 isolated: slack +0.500000  structured max +0.045003  after polish in all x +0.045003
    n = 7:  K_{1,2} + 4 isolated: slack +0.500000  structured max +0.047260  after polish in all x +0.047260
    n = 7:  K_{1,3} + 3 isolated: slack +0.666667  structured max +0.060952  after polish in all x +0.060952
    n = 8:  K_{1,2} + 5 isolated: slack +0.500000  structured max +0.048780  after polish in all x +0.048780
    n = 8:  K_{1,3} + 4 isolated: slack +0.666667  structured max +0.065195  after polish in all x +0.065195
    n = 8:  K_{1,4} + 3 isolated: slack +0.750000  structured max +0.057028  after polish in all x +0.057028

These values are lower bounds for the maximum over x. That the maximum stays below the slack when three or more
vertices are isolated is what the searches suggest; it is not proved, and no statement with "exactly when" is
claimed.

Added 12 Nov 08:37. The maximisers are not unique, and the three listed above are examples, not all of them:
at K_{1,6} + 1 (n = 8) the second structured search ends at x = (0.297, 0.184, -0.621, 0.184, 0.184, 0.184,
0.184, -0.597) in the order centre, leaves, isolated vertex, where one leaf and the isolated vertex lie on the
same side (star_struct_check2.out).

## n = 5: the minimisation of s_10, s_30 and H over 2,000 starts (12 Nov, 14:2x)

Files: minbeta_n5.py (Mac mini 1, seed 31, 2,000 starts from thirteen families, about 154 starts each, 13,783 s),
minbeta_n5_summary.out (the four summary lines and the counts below; the full 1 MB log stays on the mini, in
~/t104_alon/minbeta_n5.out). Each start is minimised four times by Nelder-Mead over the edge weights, once for each
objective. Counts are of end points below -1e-10.

    objective      end points below -1e-10   smallest value     where
    s_10                   448               -1.58e-8           next to the uniform star (leaf weights 0.25, 0.25,
                                                                0.250089, 0.249911; slack 3.8e-4)
    s_30                     0               -8.9e-15           a single edge (slack 0)
    s_1e6 (control)        249               -0.482             next to a double top eigenvalue (gap 8.2e-6,
                                                                slack 3.30)
    H = max over beta        0               -1.1e-14           graphs with slack 0 (edge, two edges, triangle)

Every value below -1e-13 for s_30 and H is at a graph whose slack is itself zero to rounding, so these are rounding,
not failures. Among end points with slack above 1e-3, the smallest ratio H/slack is 0.0217 = (1/69)/(2/3), at K_{1,3}
with one isolated vertex, reached from several families (k13, complete, sparse); no such end point has H below 1e-6.

What this confirms. The two failures predicted in the section before are both found by the search, at the predicted
graphs: the top-eigenvector state (the beta = 1e6 control) fails next to a double top eigenvalue, by a margin of
order one, and one fixed beta = 10 fails next to the uniform star at the order exp(-1.6 beta) = 1.1e-7 (found
-1.6e-8). That s_30 has no negative end point does not mean s_30 >= 0: the same mechanism puts its minimum at about
-1e-21, below what double precision sees. The candidate is H, which takes beta large next to the star and beta
moderate next to a double top eigenvalue.

Status: numerical, one implementation and one optimiser. H >= 0 on graphs with five vertices is supported by 2,000
minimisations with no failure, and it is not proved. Next: a proof of H >= 0 next to the uniform star (expand s_beta
to second order in the distance, with beta of order log(1/distance)); a second implementation of D_beta by an
independent reader before any of this is relied on.

## Next to the uniform star: H >= s_inf, and s_inf = |delta|^2 + 4 eta + higher order (12 Nov, 16:50)

Files: t104_star_local.py, t104_star_local.out (n = 5, 6, 7; 150 to 300 random directions, eps from 1e-2 to
3e-7).

A reduction. Split D_beta into the pairs (top, l) and the pairs (k, l) with k below the top. With N, D the
numerator and denominator sums,

    s_beta = s_inf + (n - 2) (D_x / (D_t + D_x)) (N_x / D_x - N_t / D_t),

and D_x carries the factor exp(beta (lam_k - lam)/lam) <= exp(-beta gap/lam). Where the top eigenvalue is simple,
s_beta -> s_inf as beta -> infinity, so H = sup over beta of s_beta is at least s_inf there. Next to the uniform
star the top eigenvalue is simple with relative gap (n - 1)/n, so H >= 0 next to the star follows from s_inf >= 0
next to the star. The failure of a fixed beta that the searches found there (of order -exp(-1.6 beta) at n = 5) is
the second term. It is of first order in the distance because the second eigenspace of the star (multiplicity
n - 2) splits at first order, while D_x = 0 at the star itself. It does not affect H.

s_inf next to the star. Write the graph as the star with leaf weights 1/(n-1) + delta_i (sum delta_i = 0, so W
stays 1) plus leaf-leaf weights eta_ij >= 0, and eta = sum eta_ij. Measured over random directions at each eps:

    direction          s_inf / eps (at eps = 1e-6)       s_inf / eps^2 (at eps = 1e-6)    negatives
    delta only, |delta| = eps            -              [0.9974, 1.0036] (n = 5, 6, 7)       0
    eta only, eta = eps         [4.0000, 4.0000]                    -                         0
    both                        [0.0043, 3.95]          positive                              0

The spread around 1 in the delta row is rounding (s_inf is about 1e-12 there); at eps = 1e-4 it is
[0.99969, 1.00030]. So, to the order measured, s_inf = |delta|_2^2 + 4 eta + higher order, with the same constants
for n = 5, 6, 7. In the mixed directions the smallest s/eps is 4 times the smallest leaf-leaf share drawn (1.1e-3),
which is what the formula gives. The star is a strict local minimum of s_inf on the cone of nonnegative weights:
first order in the leaf-leaf weights and second order along the star family.

What this gives, if the expansion is proved: H > 0 on a punctured neighbourhood of the uniform star, for every n
measured. Together with the n = 5 minimisation, the open places for H at n = 5 are then away from the star. The
expansion is measured, not derived. The next step is the first order perturbation of the top eigenpair and of
the [3,2] components in eta, and the second order perturbation in delta. Not proved; T104 stays open.

## The local expansion at the star is fixed by symmetry and two constants (12 Nov, 16:56)

Files: t104_star_constants.py, t104_star_constants.out.

Near the uniform star the top eigenvalue is simple and the denominator D_t is positive, so s_inf is a real-analytic
function of the weights there. Write delta for the leaf-weight deviations (sum zero) and eta_ij >= 0 for the
leaf-leaf weights. The automorphism group S_{n-1} of the star acts on both, and s_inf is invariant. Hence:

- the linear term in delta vanishes (an invariant linear form on the sum-zero representation is zero);
- the linear term in eta is c1 * eta, eta = sum eta_ij (the invariant linear forms on the edge space are the
  multiples of the sum);
- the quadratic term in delta is c |delta|^2 (the sum-zero representation of S_{n-1} is absolutely irreducible, so
  by Schur an invariant quadratic form on it is a multiple of the norm);
- the mixed term is bilinear in (delta, eta). The swap of leaves i and j fixes eta_ij, so the coefficient of
  eta_ij delta_k is k_1 when k is in {i, j} and k_2 otherwise. Because sum delta = 0 this is (k_1 - k_2) sum eta_ij
  (delta_i + delta_j), and the measured coefficient on the edge with delta_i = -delta_j is zero.

So s_inf = c1 eta + c |delta|^2 + O(eta |delta| + eta^2 + |delta|^3), and the star is a strict local minimum of s_inf
on the cone eta >= 0 as soon as c > 0 and c1 > 0. Richardson-extrapolated differences give

    n        5         6         7         8         9         10        11        12
    c     1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000  1.000000
    c1    4.000000  4.000000  4.000000  4.000000  4.000000  4.000000  4.000000  4.000000

and the mixed coefficient on an edge with one changed end runs from +0.71 (n = 5) to +0.16 (n = 12). The value on
the edge with both ends changed is -0.005, the size of the difference error. With c = 1 and c1 = 4, for n = 5 to 12
H > 0 on a punctured neighbourhood of the uniform star: H >= s_inf there, and s_inf > 0 off the star.

Status: the symmetry reduction is a proof. The two constants are measured to six digits, not derived; positivity
is all the argument uses, and both are far from zero. That c = 1 and c1 = 4 do not depend on n suggests a short
closed form. Next: derive c and c1 (one leaf-weight swap, one leaf-leaf edge). Row T104: not solved; this settles
only the neighbourhood of one equality case.

## c = 1 and c1 = 4 for every n >= 5: the proof (12 Nov, 17:2x)

Files: t104_star_exact.py, t104_star_exact.out (exact rationals for n = 5, 6 by Kato's second order formulas; it agrees
with the hand computation below and with the Richardson values for n = 5 to 12).

Notation. m = n - 1 leaves, a = 1/m, r = sqrt(n m). At the star L has top eigenvalue lam0 = n/m with
u = (m, -1, ..., -1)/r, the eigenvalue a on E = {leaf vectors with sum 0} (multiplicity m - 1), and 0 on the constants;
lam0 - a = 1. V is the space of symmetric matrices with zero diagonal and zero row sums (the [n-2,2] representation of
S_n), M = sum_e w_e (I - K_e) on V, K_e the conjugation by the transposition e. Summing over l,
sum_l g_l S_l S_l^* = (1/2)(I + F)(P (x) A)(I + F), with P = u u^T and A = lam I - L, and Pi F = Pi. So

    s_inf = (n - 2) tr(M T)/tr(T) - (n - 1) lam + 2,     T = 2 Pi (P (x) A) Pi.

Constants and the matrix u 1^T + 1 u^T are orthogonal to V, so the constant direction of A never contributes.

Branching. V restricted to S_{n-1} (the leaves) is V1 + V2 with V1 ~ [n-2,1] and V2 ~ [n-3,2], each once. The
Jucys-Murphy element X = sum_j K_{0j} acts on them by the contents 0 and n - 3, so at the star M = a(m I - X) is 1 on V1
and beta = 2/m on V2. V2 is V', the same space for the m leaves (embedded with zero centre row and column). The map
y -> Pi(u (x) y) from E is equivariant, so its image is V1; explicitly Pi(u (x) y) = rho W(y), with
W(y)_{0j} = -(m-2) y_j, W(y)_{ij} = y_i + y_j between leaves, |W(y)|^2 = 2(m-1)(m-2)|y|^2 and rho = -n/(2 r (n-2)).
Pi(u (x) v) = 0 for v a constant, u or e_0, so T at the star lives on V1, and

    t0 = tr T = 2 rho^2 2(m-1)(m-2)(m-1) = n(n-3)/(n-1),   tr(M T)/tr(T) = 1 at the star, s_inf(star) = 0.

The useful split: s_inf = (n-2) tr((M - I) T)/tr(T) - (n-1)(lam - lam0) + ... with M - I = 0 on V1 and beta - 1 on V2.

c1 (one leaf-leaf edge 12, renormalised; first order direction e_12 - star). Any first order change of T has zero
V2-V2 block, because every term carries a factor Pi(u (x) .), which lies in V1. So the first order of
tr((M - I) T) is tr(M1 T0) with M1 = (I - K_12) - M_0. T0 = (t0/dim V1) Pi_1 by Schur, and the character of a
transposition on [m-1,1] of S_m is (m - 3)/(m - 1) of the dimension. Hence the first order of tr(MT)/tr(T) is
1 - (n-4)/(n-2) - 1 = -(n-4)/(n-2). lam1 = (u_1 - u_2)^2 - lam0 = -n/(n-1). So

    c1 = (n - 2)(-(n-4)/(n-2)) + (n - 1) n/(n - 1) = 4.

c (leaf deviation delta in E, total weight fixed). L1 = sum delta_i L_{0i}, L1 u = -g delta with g = sqrt(n/(n-1)), and
delta is an eigenvector of the reduced resolvent with value 1/(lam0 - a) = 1. So lam1 = 0, lam2 = g^2 |delta|^2 and
u1 = -g delta. The first order of tr((M - I)T) is tr(M1 T0) = 0 (M1 = -sum delta_j K_{0j} and the K_{0j} have equal trace
on V1). With N2 the second order of tr((M - I) T),

    s2 = (n - 2) N2 / t0 - (n - 1) g^2 |delta|^2,     N2 = tr(M1 T1) + (beta - 1) tr(Pi2 T2).

(i) tr(Pi2 T2). Only P2's term u1 u1^T survives in the V2 block: tr(Pi2 T2) = 2 g^2 sum_y |Pi_{V'}(delta (x) y)|^2 over
an orthonormal basis y of E. This is S_{n-1}-invariant in delta, so it is kappa |delta|^2, and summing delta over a basis
gives kappa (m-1) = tr(Pi_{V'}) = m(m-3)/2. So tr(Pi2 T2) = n(n-4)/(n-2) |delta|^2.

(ii) tr(M1 T1) = 2(I_a + I_b), T1 = 2 Pi(P1 (x) A0 + P0 (x) A1)Pi with A1 = -L1.
I_b = sum_{i,j} delta_i delta_j rho^2 <W(e_i'), K_{0j} W(e_i')>, e_i' = e_i - 1/m (the projection to E). A direct count
gives <W(y), K_{0j} W(y)> = 2(m-1)(m y_j^2 - |y|^2) (it sums to zero over j, as the content 0 requires), so
I_b = rho^2 2(m-1)(m-2) |delta|^2 = n(n-3)/(2(n-1)(n-2)) |delta|^2.
I_a = 2 g rho sum_j delta_j sum_y delta^T (K_{0j} W(y)) y (leaf block). With sum_y y y^T = I - J/m the inner sum is
-(m-1)(m-2) delta_j, and g rho = -n/(2(n-1)(n-2)), so I_a = n(n-3)/(n-1) |delta|^2.
Hence tr(M1 T1) = n(n-3)(2n-3)/((n-1)(n-2)) |delta|^2.

(iii) With beta - 1 = -(n-3)/(n-1):
N2 = n(n-3)/((n-1)(n-2)) ((2n - 3) - (n - 4)) |delta|^2 = n(n-3)(n+1)/((n-1)(n-2)) |delta|^2,
(n - 2) N2/t0 = (n + 1)|delta|^2, and

    s2 = (n + 1)|delta|^2 - n |delta|^2 = |delta|^2,   c = 1.

Theorem (n >= 5). Next to the uniform star K_{1,n-1}, s_inf = 4 eta + |delta|^2 + O(eta |delta| + eta^2 + |delta|^3).
So s_inf > 0 on a punctured neighbourhood of the star in the cone of nonnegative weights, and since H >= s_inf wherever
the top eigenvalue is simple, H > 0 there. The equality case at the star is isolated.

Checks: the exact rational computation (independent route: Kato's projector expansion in sympy, no use of the branching
argument) gives c = 1, c1 = 4 for n = 5, 6; the Richardson differences give both to six digits for n = 5 to 12.
Status: proof written once, not yet independently audited. Row T104: not solved; this settles the neighbourhood of
one equality case. Next: the single-edge equality case, the same way.

## The single-edge equality case is isolated too: first order, slopes 3/2 and (4n-10)/(n-3) (12 Nov, 17:2x)

Files: t104_edge_local.py, t104_edge_local.out (n = 5 to 8, Richardson slopes and 100 random nonnegative directions).

The edge (0,1) of weight 1, everything else 0. L0 = (e_0 - e_1)(e_0 - e_1)^T has the simple top eigenvalue 2 with
u = (e_0 - e_1)/sqrt 2, and 0 on the rest of u-perp, so A0 = 2 (I - u u^T), need = 2(n - 2), M0 = I - K_01. Near the edge
the top eigenvalue stays simple, so s_inf is real-analytic there in all weight directions, including negative ones.
The perturbation adds weights w_f >= 0 on the other edges (and renormalises). The symmetry group is S_2 x S_{n-2}, with
two orbits: type a, the 2(n-2) edges from {0,1} to the rest R; type b, the edges inside R. An invariant linear form is
constant on each orbit, so

    s_inf = p_a A + p_b B + O(|w|^2),   A = sum of type a weights, B = sum of type b weights.

T0. The vectors x in u-perp are symmetric under the swap of 0 and 1. For y in E' = {vectors on R with sum 0} the matrix
Z(y) = sym(u y^T) (entries +-y_j/(2 sqrt 2) between {0,1} and R) already lies in V, and |Z(y)|^2 = |y|^2/2. The remaining
directions (the constants and (1, 1, c, ..., c) with 2 + (n-2)c = 0) project to 0: such a projection would be an
S_{n-2}-invariant element of V that is odd under the swap, and the row-sum condition forces it to vanish. So
T0 = 4 sum_y |Z(y)><Z(y)| over an orthonormal basis of E', t0 = 2(n - 3) > 0, and T0 lives where K_01 = -1, i.e. M0 = 2
there: tr(M0 T0)/t0 = 2 and s_inf(edge) = (n - 2) 2 - 2(n - 1) + 2 = 0.

First order. Write f = tr(MT)/tr(T). The first order of tr((M - 2)T) is tr(M1 T0) + tr((M0 - 2) T1), and the second
term is zero: M0 - 2 = -(I + K_01) vanishes on the odd part, and the even-even block of T1 is zero because
every term of T1 = 2 Pi(P1 (x) A0 + P0 (x) A1)Pi has a factor Pi(u (x) x) with x symmetric (odd, so killed by the even
projection) except (u (x) u)(u (x) u)^*, whose coefficient u^T A1 u = lam1 - u^T L1 u is 0. Along the renormalised
direction e_f - edge,

    s1 = (n - 2)(tr((I - K_f) T0)/t0 - 2) - (n - 1) lam1 = (n - 2)(-1 - <K_f>) - (n - 1) lam1,
    <K_f> = sum_y <Z(y), K_f Z(y)> / sum_y |Z(y)|^2,   lam1 = (u_i - u_j)^2 - 2.

Type b, f = (2,3): K_23 Z(y) = Z(tau y), so <K_23> = tr(tau on E')/dim E' = (n - 5)/(n - 3) (the transposition on the
standard representation of S_{n-2}), and lam1 = -2:
    p_b = -(n - 2)(2n - 8)/(n - 3) + 2(n - 1) = (4n - 10)/(n - 3).
Type a, f = (0,2): counting entries, <Z(y), K_02 Z(y)> = (y_2^2 + sum_{j != 2} y_j^2)/4 = |y|^2/4, so <K_02> = 1/2, and
lam1 = 1/2 - 2 = -3/2:
    p_a = -(3/2)(n - 2) + (3/2)(n - 1) = 3/2.

These match the measured slopes (1.500000; 5, 4.666667, 4.5, 4.4 for n = 5 to 8), and the smallest s_inf/eps over 100
random nonnegative directions at each n is 1.50 to 1.97, never below p_a.

Theorem (n >= 5). s_inf > 0 on a punctured neighbourhood of the single edge in the cone of nonnegative weights, so
H > 0 there. With the star section above: both equality cases of H are isolated, for every n >= 5.

Status: proof written once, not yet independently audited; slopes also measured. Row T104: not solved. What is left
for H >= 0 is global: the region away from both equality cases (searched at n = 5 with 2,000 starts, no negative
value) and the places where the top eigenvalue is not simple, where H >= s_inf is not available.

## The uniformly weighted complete graph is not a third equality case

At uniform weights on K_n every nontrivial eigenvalue of L is 2/(n-1), so need = (n-1) lam - 2 = 0, every gap
vanishes, the quotient defining s_beta is empty, and the search code returns -need = 0. The control objective
(beta = 10) at n = 5 stopped there (round 192 of np_n5_a0.1_s31, H = -9e-16), because the distance mask in
t104_np_hsearch.py excludes only the star and the single edge. The zero comes from the convention for an empty quotient. H
does not tend to it.

Lemma. M(K_n) = (4/n) I on V_[n-2,2]. As w tends to the uniform weighting, H(w) tends to 4(n-2)/n.

Proof. M(w) = sum_ij w_ij (I - pi(i j)) restricted to V_[n-2,2]. At uniform weights this is the class sum of the
transpositions divided by the number of edges, which acts on the irreducible V_[n-2,2] as the scalar
1 - chi(tau)/dim. The content sum of [n-2,2] is (n-2)(n-3)/2 - 1 = (n-1)(n-4)/2, so chi(tau)/dim = (n-4)/n
and the scalar is 4/n. Away from K_n, s_beta is (n-2) times an average of Rayleigh quotients a.M a / a.a with
nonnegative weights f gap |a|^2, minus need. So every s_beta, and H, lies between (n-2) lambda_min(M) - need and
the slack (n-2) lambda_max(M) - need. Both ends tend to 4(n-2)/n, because M is continuous in w and need tends to 0.

Measured (t104_kn_local.py, .out): at distance eps = 1e-3 from K_n, the smallest H over 400 random directions and
over the edge, star and triangle directions is 2.3976, 2.6640, 2.8543, 2.9970 for n = 5 to 8, against
4(n-2)/n = 2.4, 2.6667, 2.8571, 3.0. So small values of H do not accumulate at K_n, and the only equality cases
are still the star and the single edge. At K_n itself need = 0 and M is positive definite, so the inequality holds
there with room 4(n-2)/n, whatever value is assigned to the empty quotient.

The same sandwich gives a bound that can be used anywhere: H >= (n-2) lambda_min(M) - need. On 6,000 graphs
drawn from the search's start families it settles H >= 0 for 12.0, 12.0, 12.2 and 12.6 per cent at n = 5 to 8 (the
graphs close to the uniform complete graph). need is never negative, since lam is at least the mean 2/(n-1) of the
nontrivial eigenvalues (t104_minM_bound.py, .out).

## H on the stratum where the top eigenvalue is double

H is continuous where lam_1 = lam_2 (a pair with zero gap contributes nothing); only the proof route H >= s_inf
is unavailable there. Measured values:

A uniformly weighted K_k on k of the n vertices, 3 <= k < n, has a top eigenvalue of multiplicity k - 1 and

    H = 2(k - 2)/(k - 1)        (1, 4/3, 3/2, 8/5, 5/3 for k = 3..7, the same for n = 5, 6, 7, 8),

unchanged to six digits under random perturbations of size 1e-6 (t104_subclique.py, .out). The triangle, H = 1,
is the smallest, and there H equals the slack. A short penalty search on the stratum at n = 5 (t104_degen_top.py,
six rounds of 48) found no value below 1.0, the smallest at the triangle. Longer runs at n = 5, 6, 7 are queued on
Mac mini 2 (dg_n*_s*.out). So far the double-top stratum has a margin of 1 away from the single edge (k = 2,
H = 0) and K_n (the empty-quotient convention, H -> 4(n-2)/n). The formula 2(k-2)/(k-1) is proved below.

Lemma. For the uniform K_k on k of the n vertices, 3 <= k < n, H = 2(k-2)/(k-1) exactly, for every beta.

Proof. With weight 1/C(k,2) on each clique edge, L has eigenvalue lam = 2/(k-1) on Top (vectors supported on
the clique with sum zero, dimension k - 1) and 0 on Zero (vectors constant on the clique and orthogonal to 1,
dimension n - k). So need = (n-1) lam - 2 = 2(n-k)/(k-1). The only pairs with a positive gap are (top, zero),
all with gap lam and f = 1, so s_beta does not depend on beta. For a clique transposition tau, u in Top and v in
Zero, pi(tau)u (x) pi(tau)v = (pi(tau)u) (x) v, so the full operator sum_e w_e (I - pi(e) (x) pi(e)) acts on
Top (x) Zero and on Zero (x) Top as the average of I - pi(tau) on the standard representation [k-1,1] of S_k,
which is the scalar 1 - (k-3)/(k-1) = 2/(k-1). Each pi(e) (x) pi(e) preserves the S_n-invariant subspace
V_[n-2,2], so the full operator commutes with the orthogonal projection B B^t onto it. For a = B^t sym(u (x) v)
this gives M a = B^t M_full B B^t s = B^t M_full s = (2/(k-1)) a: every a is an eigenvector of M with eigenvalue
2/(k-1). Hence H = (n-2) 2/(k-1) - 2(n-k)/(k-1) = 2(k-2)/(k-1). (k = 2 is the single edge, H = 0; k = n is the
empty quotient above.)

The claim that the triangle is
the smallest H on the double-top stratum is still only measured.

### Disjoint unions of cliques

The lemma above extends to every disjoint union of uniform cliques whose top eigenvalues agree.

**Lemma.** Let G be the disjoint union of cliques K_{a_1}, ..., K_{a_r} (each a_i >= 2) on some of the n vertices,
the rest isolated, with every edge of K_{a_i} weighted proportionally to 1/a_i. Put D = sum_i (a_i - 1) and assume
n - D >= 2. Then the top eigenvalue of L has multiplicity D and H = 2 - 2/D = 2(D - 1)/D for every beta.

*Proof.* With total weight one, each edge of K_{a_i} carries 2/(a_i D), so each clique contributes the eigenvalue
2/D with multiplicity a_i - 1 and L has spectrum {2/D (multiplicity D), 0 (multiplicity n - D)}. Hence lambda = 2/D,
need = (n - 1) 2/D - 2, and the only pairs with a gap are (Top, Zero). Top is the direct sum of the standard
representations S_i of the S_{a_i}, and every Zero vector is constant on each clique. For an edge e of K_{a_i} and
u in Top, v in Zero we have pi(e) v = v, so (I - pi(e) (x) pi(e)) sym(u (x) v) = sym((I - pi(e)) u (x) v). On S_i the
sum over the C(a_i, 2) transpositions of I - pi(e) is the scalar C(a_i, 2) (1 - (a_i - 3)/(a_i - 1)) = a_i, and on
S_j (j != i) each such I - pi(e) is zero. So the full operator sum_e w_e (I - pi(e) (x) pi(e)) acts on
sym(Top (x) Zero) as the scalar (2/(a_i D)) a_i = 2/D, the same for every i. As before it commutes with the
projection onto the S_n-invariant subspace V_[n-2,2], so every nonzero vector a in the sums for num and den is an
eigenvector of M with eigenvalue 2/D, and num/den = 2/D whatever the weights f and gaps. The condition n - D >= 2
makes Zero larger than the constants, so the quotient is not empty. Therefore
H = (n - 2) 2/D - (n - 1) 2/D + 2 = 2 - 2/D. QED

The single clique K_k is the case r = 1, D = k - 1. The value increases with D, so on this family the smallest
value on the double-top stratum (D >= 2) is H = 1, attained exactly when D = 2: the triangle and two disjoint
edges. Checked against the search code for n = 5..8 on nine unions, largest difference 4.9e-15
(t104_degen_family.py, .out). The same file measures the other symmetric double-top graphs: C_5 (1.27-1.51), C_7
(1.73-1.87) and K_4 minus an edge (1.150-1.156), all above 1. The triangle with a pendant edge has H = 0.77-0.79,
but its top eigenvalue is simple (gap12/lambda = 0.25), so it is not on the stratum. Whether H >= 1 on the whole
double-top stratum is open; it would follow from the stratum minimum being one of these unions.

The double-top search t104_degen_top.py on Mac mini 2 (n = 5, seed 41, 1,667 rounds of 128 starts at the time of
writing) agrees: no negative value, and the smallest values on the stratum (gap12/lambda < 1e-5) are two disjoint edges
and the triangle, at H = 1 to six digits. Its lowest reading, H = 0.9999984, is two disjoint edges joined by a third
edge of weight 3.5e-6, a point that has just left the stratum (gap12/lambda = 3.5e-6). Along that bridge
(t104_2k2_bridge.py, .out: weight (1 - t)/2 on 14 and 23, t on 12, so lambda_1 = 1 + O(t^2)) one has
1 - H = gap12 to within 0.6 per cent for 1e-8 <= t <= 1e-3, with beta taken up to 1e10 (on the search grid, which
stops at 1e6, the ratio reads up to 1.7 below t = 1e-5, so the search's values near the stratum are slightly low). So the value 1 is a minimum along the stratum only. Off it H decreases at unit
rate in the gap, and a lower bound proved on the stratum does not extend to a neighbourhood of it; near the stratum
positivity has to come from the gap-dependent terms.


### The beta -> infinity value on the stratum

On the double-top stratum let beta -> infinity in s_beta. Only the pairs (k, l) with lambda_k = lambda and
lambda_l < lambda survive, each with weight lambda - lambda_l, so

    s_inf = (n - 2) sum_{k in Top, l} (lambda - lambda_l) <a_kl, M a_kl> / sum_{k in Top, l} (lambda - lambda_l) |a_kl|^2 - need,

a trace over Top (x) e_l, hence independent of the basis chosen in Top, and H >= s_inf on the stratum. On the clique
unions H = s_inf = 2 - 2/D, and C_5 gives s_inf = H = 1.5056. Random points of the stratum (t104_sinf_stratum.py:
Nelder-Mead on the relative gap from the search's start families, kept at relative gap below 1e-7 and away from
uniform K_n): n = 5, 60 points, smallest s_inf 1.0209 (a perturbed pair of disjoint edges), H - s_inf between
-3e-13 and 1.1e-5; n = 6, 30 points, smallest s_inf 1.2338, H - s_inf up to 0.090 (t104_sinf_stratum_n5.out, _n6.out).
So at n = 5 the maximum over beta sits at beta = infinity on every sampled point, at n = 6 not always, and in both
cases s_inf >= 1 on the sample.

**Lemma (proved).** On the stratum lambda <= 1, with equality exactly for the balanced triangle and for two equal
disjoint edges. *Proof.* With total weight one, tr L = 2, and lambda_1 = lambda_2 = lambda gives
2 lambda <= sum_i lambda_i = 2. Equality forces every other eigenvalue to vanish, so L has rank 2 and the graph has
n - 2 components: a path or triangle on three vertices, or two disjoint edges, the rest isolated. A path with weights
a, b has eigenvalues a + b +- (a^2 - ab + b^2)^(1/2), never equal; a triangle has a double top only when its three
weights agree; two disjoint edges only when their weights agree. QED

Write R for the gap-weighted Rayleigh average of M over the V_[n-2,2] parts of sym(Top (x) e_l), so that
s_inf = (n - 2) R - (n - 1) lambda + 2, that is

    s_inf - 1 = (n - 2)(R - lambda) + (1 - lambda).

The second term is nonnegative by the lemma. The stronger inequality R >= lambda would give s_inf >= 1 at once, and
it holds on the clique unions (R = lambda = 2/D exactly) and at all 90 points of t104_sinf_stratum_n5.out and _n6.out
(smallest R - lambda 0.00096 at n = 5, 0.0059 at n = 6). It is false all the same: point 13 of
t104_R_identity_n5.out (seed 11; relative top gap below 1e-7, weights in t104_sinf_stratum.py with arguments 5 13 11)
has lambda = 0.8508 and R - lambda = -0.0091, while s_inf = H = 1.1218 to 1e-6. The term 1 - lambda is needed, and the
statement to prove on the stratum is

    (n - 2)(R - lambda) + (1 - lambda) >= 0,

with equality only where lambda = 1 and R = lambda, i.e. at the two cases above.

An explicit form of R. For u in Top, v = e_l with eigenvalue mu < lambda, X = (u v' + v u')/sqrt 2 and A the
V_[n-2,2] part of X: the map Y -> sum_e w_e (Y - P_e Y P_e) on symmetric matrices is a weighted sum of transposition
actions, so it keeps each isotypic part of Sym^2, and V_[n-2,2] occurs there once. It equals
(lambda + mu) X - sqrt 2 sum_e w_e (b_e . u)(b_e . v) b_e b_e' on X, and <A, b_e b_e'> = -2 A_ij for e = ij, so

    <A, M A> = (lambda + mu) |A|^2 + 2 sqrt 2 sum_{e = ij} w_e (u_i - u_j)(v_i - v_j) A_ij,
    (R - lambda) sum g |A|^2 = sum g [ mu |A|^2 + 2 sqrt 2 sum_{e = ij} w_e (u_i - u_j)(v_i - v_j) A_ij ],

summed over the pairs (u, e_l) with g = lambda - mu. This agrees with the operator to 1e-14 (t104_R_identity.py,
_n5.out). The mu |A|^2 part is positive and the edge part negative on 75 of the 80 pairs sampled; R - lambda is their
difference, small against either (at C_5 each pair has mu |A|^2 = 0.0921 and edge part -0.0667).

How far the target is from failing: rho = (n - 2)(lambda - R)/(1 - lambda) must stay at most 1. Over the 125 stratum
points measured (t104_sinf_stratum_n5.out, _n6.out, t104_R_identity_n5.out, _n6.out) rho is positive at one point
only, the one above, where it is 0.183; at n = 6 R - lambda is at least 0.0011 with lambda up to 0.9973.

R >= lambda fails more badly off the stratum. With a simple top eigenvalue (Top = the top vector alone, the same beta ->
infinity weights) it fails on 1,220 of 3,000 random weighted graphs at n = 5 (t104_R_vs_lambda.py, _n5.out); at the
uniform star R / lambda = 4/5 with lambda = 5/4, where the global form (n - 2) R >= (n - 1) lambda - 2, i.e.
s_inf >= 0, holds with equality. Off the stratum lambda can exceed 1, and the term 1 - lambda that makes the
reduction work is negative there.

### A closed form of the stratum target

For orthonormal eigenvectors u, v of L (eigenvalues lambda, mu, both orthogonal to 1) put p_i = u_i v_i, so that
sum p_i = u . v = 0, and q_e = (u_i - u_j)(v_i - v_j) for e = ij. Let A be the V_[n-2,2] part of
X = (u v' + v u')/sqrt 2. The off-diagonal part of X has row sums -sqrt 2 p_i, its projection onto the trivial and
standard parts is (a_i + a_j) with a_i = -sqrt 2 p_i/(n - 2), and sum_j w_ij q_ij = (lambda + mu) p_i - (Lp)_i. With
the edge formula above this gives

    |A|^2    = 1 - 2n/(n - 2) |p|^2,
    <A, M A> = lambda + mu - 2n/(n - 2) p'Lp - 2 sum_e w_e q_e^2.

Hence, per pair (u in Top, v = e_l),

    <A, M A> - lambda |A|^2 + (1 - lambda)/(n - 2) |A|^2 = P - 2 sum_e w_e q_e^2,
    P = mu + 2n/(n - 2) (lambda |p|^2 - p'Lp) + (1 - lambda)/(n - 2) |A|^2,

and every term of P is nonnegative on the stratum: mu >= 0, p'Lp <= lambda |p|^2 because p is orthogonal to 1, and
lambda <= 1 by the lemma. The stratum target (n - 2)(R - lambda) + (1 - lambda) >= 0 is therefore

    2 sum_pairs g sum_e w_e q_e^2 <= sum_pairs g P,     g = lambda - mu,

a single fourth-order term against three nonnegative ones. Both identities agree with the operator to 1.1e-14
(t104_R_closed.py, _n5.out with 20 points, _n6.out with 12 points). The ratio Q of the left side to the right is
largest at C_5 (0.877 at n = 5) and at most 0.857 at the random stratum points; at 2K_2 and the triangle both sides
vanish. Measured only: the inequality itself is not proved.

The sum over pairs has no basis left in it. Let Pi be the projector onto Top (dimension D) and
G = sum_{l below} (lambda - mu_l) v_l v_l' = lambda (I - J/n) - L (the top terms vanish), so
G_ii = lambda (n-1)/n - d_i, G_ij = w_ij - lambda/n, and b_e' G b_e = 2 lambda - d_i - d_j - 2 w_ij for e = ij. Since
g depends on l alone, sum_l g (b_e . u)^2 (b_e . v_l)^2 = (b_e . u)^2 b_e' G b_e, and summing over an orthonormal basis
of Top gives

    S1 = sum g mu         = D (2 lambda - tr L^2),
    S2 = sum g |p|^2      = sum_i Pi_ii G_ii,
    S3 = sum g p'Lp       = sum_{e = ij} w_e (Pi_ii G_ii + Pi_jj G_jj - 2 Pi_ij G_ij),
    S4 = sum g            = D ((n-1) lambda - 2),
    S5 = sum g sum w q^2  = sum_{e = ij} w_e (b_e' Pi b_e)(2 lambda - d_i - d_j - 2 w_ij),

and the stratum target is

    T = S1 + 2n/(n-2) (lambda S2 - S3) + (1 - lambda)/(n-2) (S4 - 2n/(n-2) S2) - 2 S5 >= 0,

with s_inf - 1 = (n - 2) T / (S4 - 2n/(n-2) S2). Each 2 lambda - d_i - d_j - 2 w_ij = b_e' G b_e is nonnegative. Checked
at 15 stratum points, n = 5: T agrees with the pair sum to 7.2e-15 and gives s_inf to 4.1e-14 (t104_trace_form.py,
_n5.out). So H >= 1 on the stratum is a statement about L, the projector onto its top eigenspace and lambda only.

Which terms carry the bound. Write T = X1 + X2 + X3 - Y with X1 = S1 = D(2 lambda - tr L^2), X2 = 2n/(n-2)(lambda S2 -
S3), X3 = (1 - lambda)/(n-2) sum g |A|^2 and Y = 2 S5. Over 20 stratum points at n = 5 and 12 at n = 6
(t104_trace_terms.py, _n5.out, _n6.out) the largest values of Y over a sub-sum are

    n = 5:  X1 1.49,  X1 + X2 1.04,  X1 + X3 1.25,  X2 + X3 4.24,  X1 + X2 + X3 0.857;
    n = 6:  X1 1.12,  X1 + X2 0.924, X1 + X3 0.862, X2 + X3 2.39,  X1 + X2 + X3 0.743.

So no two of the three terms suffice at n = 5, and X1 (the eigenvalue term D(2 lambda - tr L^2)) carries most of
the weight: a proof has to use all three, with X1 as the main one. X2 can be nearly 0 (smallest measured 2e-5).

The eigenvalue term is a sum over edges. Since tr L = 2 and sum w = 1, 2 lambda - tr L^2 = sum_e w_e gamma_e with
gamma_e = 2 lambda - d_i - d_j - 2 w_e = b_e' G b_e >= 0, so X1 = D sum_e w_e gamma_e, while Y = 2 sum_e w_e tau_e gamma_e
with tau_e = |Pi b_e|^2 in [0, 2]. The target is

    sum_e w_e gamma_e (2 tau_e - D) <= X2 + X3,

so only edges with more than D/2 of their squared length in Top push against it (for D = 2: tau_e > 1). Checked
to 2.1e-15 at 15 stratum points, n = 5, where the left side over X2 + X3 is at most 0.661 and is negative at some
points (t104_edge_excess.py, _n5.out).

### C_5 as the test case for the edge-sum target

At C_5 (weights 1/5 on the cycle) lambda = (2/5)(1 + cos(pi/5)) = 0.7236 is double, every edge has tau_e = 2 lambda = 1.447 > 1
and gamma_e = 2 lambda - 6/5 = 0.2472, so X1 = 2 gamma and the left side is gamma (4 lambda - 2) = 0.2211 exactly. The right
side is X2 + X3 = 0.2667 + 0.0549 (X2 = 4/15 to 12 digits), ratio 0.6875 (t104_c5_terms.py, _out). Every edge pushes against
the bound here, so C_5 is the case a proof for D = 2 has to get right; its ratio sits above the 0.661 of the random sample.

The seed-11 point edge by edge (t104_seed11_edges.py, _out; the sum agrees with Y - X1 to 1e-9). Its two heaviest edges,
13 and 24 (weights 0.343, 0.326), lie almost in Top (tau = 1.998, 1.877) and have gamma = 0.0011, 0.069, so they push
against the bound with 0.0007 and 0.0394; edges 12 and 23 add 0.031 and 0.036; the six light edges have tau < 1 and pay
back 0.037. Left side 0.0699 against X2 + X3 = 0.1391, ratio 0.503: the point that breaks R >= lambda is far from
breaking this target.

Why heavy edges in Top cost little. G = lambda(I - J/n) - L is positive semidefinite on 1-perp and vanishes on Top, with
largest eigenvalue lambda - mu_min <= lambda there, so

    gamma_e = b_e' G b_e = ((I - Pi) b_e)' G ((I - Pi) b_e) <= lambda |(I - Pi) b_e|^2 = lambda (2 - tau_e).

Hence each edge pushes at most w_e lambda (2 - tau_e)(2 tau_e - D), which for D = 2 is at most lambda w_e / 2 (at
tau_e = 3/2). This alone does not close the target: at C_5 it gives 0.358 against X2 + X3 = 0.322. The loss is in
replacing the gap weights lambda - mu_l by lambda; a proof has to keep them.

### The target does not split by pairs, nor by low eigenvectors

In the eigenbasis (u_k in Top, v_l below it with gap g_l = lambda - mu_l on 1-perp) each trace term is a sum over pairs:
S2 = sum g_l |p_kl|^2 and S3 = sum g_l p_kl' L p_kl with p_kl = u_k * v_l; S4 = D((n-1) lambda - 2) = sum_{k,l} g_l;
2 lambda - tr L^2 = sum_l g_l mu_l; S5 = sum_{k,l} g_l sum_e w_e q_e^2 with q_e = (b_e . u_k)(b_e . v_l). So the trace form
is the closed form of push 117 summed with the gap weights, and nothing is lost by keeping them. The question is how much
of the sum a proof needs.

Pair by pair, 2 sum_e w_e q_e^2 <= P(u, v) for every unit u in Top and every low v_l, is false: at n = 5 the ratio reaches
1.370 (point 9 of t104_per_pair_n5.out, seed 11) and exceeds 1 at 6 of 15 points (360 angles in Top per point); at C_5 it
is 0.877, the same as the summed ratio, since there every pair is equivalent. Fixing v_l and taking the trace over Top
(basis-free) is also false, barely: 1.020 at point 13, the seed-11 point where R >= lambda fails (t104_per_l.py,
t104_per_l_n5.out); the other 14 points stay at or below 0.968. So a proof has to use the gap-weighted sum over the low
eigenvectors, not only the trace over Top.

### What the sum over low eigenvectors buys

Write F_l = P_l - Q_l (traces over Top), so the target is sum_l g_l F_l >= 0 with g_l = lambda - mu_l. At the seed-11 point
(t104_per_l_seed11.py, _out) the low eigenvector with mu = 0.0072 has g = 0.844 and F = 0.0914, the one with mu = 0.291
has g = 0.560 and F = -0.0143 (Q/P = 1.020); the weighted sum 0.0691 matches the trace form to 3e-9. At C_5 both low
eigenvectors are equivalent, F = 0.112 each.

A Chebyshev step (F ordered like g, so sum g F >= (1/m)(sum g)(sum F)) does not work: F is not non-increasing in mu at 10
of 15 points at n = 5 and at all 12 at n = 6 (t104_chebyshev.py, _n5.out, _n6.out); more often F grows with mu. What the
sample does show: F_l < 0 at only 2 of the 27 points (n = 5 seed 11, F = -0.014 at the larger mu; n = 6 point 3,
F = -0.0055 at the middle mu), always small against the other F_l, and the unweighted trace sum_l F_l is positive at every
point. So a proof can afford to lose on one low direction; it cannot treat the directions one at a time.

Searching for the worst point. Maximising the margin ratio sum_l g_l Q_l / sum_l g_l P_l (the target says it is at most 1)
by Nelder-Mead with Top forced to the top two eigenvectors and a penalty on the relative top gap, then polishing back onto
the stratum (relative gap below 1e-7), from the seed-11 point and seven stratum points at n = 5: every start climbed, the
largest value reached is 0.8733 (from the seed-11 point; t104_worst_ratio.py, _n5.out), below the C_5 value 0.8769 and
none above it. So at n = 5 C_5 looks like the maximiser, with margin 0.12. (An earlier version minimised
sum gF / sum g|F|, which is flat at 1 wherever every F_l >= 0 and stalls there; t104_worst_search.py, _n5.out, kept for
the record: from the seed-11 point it went to 0.199, still positive.) A wider search is queued on the Mac mini.

### Circulants

For n odd every nonzero eigenvalue of a circulant weighting is double, so all circulants lie on the stratum. The margin
ratio sum g Q / sum g P (target: at most 1) at C_n is 0.8769 (n = 5), 0.6538 (n = 7), 0.5075 (n = 9), and no one of 40
random circulants per n beats C_n (t104_circulant_ratio.py, .out). With the n = 5 search above, C_5 is the largest value
seen anywhere on the stratum, and the margin grows with n. A wider search (n = 5, 6, 7; 40, 30, 20 starts) is running on
the Mac mini.

### C_5 is a local maximum of the margin ratio

Perturb the C_5 weights (z = w^(1/2), Gaussian on the five cycle edges, one-sided on the five chords, which start at
zero), pull the point back onto the stratum by minimising |z - z_pert|^2 + 10^4 relgap^2 and then relgap alone until
relgap < 1e-7, and evaluate the margin ratio sum g Q / sum g P (t104_c5_local.py, seed 7, t104_c5_local_s7.out). C_5 has
ratio 0.876857. At perturbation sizes 0.01, 0.03 and 0.1 (25 points each, L1 distance from C_5 between 0.007 and 0.48)
no point exceeds it: the largest values are 0.876686, 0.876223 and 0.865586. Together with the circulant scan, where
C_n is the worst circulant for n = 5, 7, 9, and the eight-start search on the n = 5 stratum (0.8733), the measured
picture is that C_5 is the global maximum of the ratio at n = 5, at 0.877 against the limit 1. This is numerical; the
second variation at C_5 has not been computed in closed form.

### First-order conditions at C_5

Near C_5 the stratum (n = 5) has dimension 7: ten weights, total one, and two conditions that the top 2 x 2 block stays
scalar; the linearised conditions have rank 3 (singular values 2.29, 2.29, 2.24). Five of its directions add chords,
which start at zero and can only grow; the other two stay on weighted 5-cycles. t104_c5_first_order.py
(t104_c5_first_order.out) pulls every point onto the stratum to a relative top gap below 1e-9 before reading the margin ratio.

Chords. One chord at weight t, the cycle weights moved the least amount that keeps the top double and the total one:
ratio - ratio(C_5) = -0.380 t + O(t^2) (slopes -0.3802, -0.3785, -0.3751 at t = 0.001, 0.002, 0.004). All five chords
are equivalent under the dihedral group, so to first order the ratio falls by 0.380 times the total chord weight.

Cycle face. Along twelve directions in the two-dimensional face the ratio falls as -2.047 s^2 (s = 0.01, 0.02, 0.04
give -2.047e-4, -8.17e-4, -3.25e-3), the same in every direction. That isotropy is what the symmetry predicts: the
face's tangent space is a two-dimensional irreducible representation of the dihedral group, on which any invariant
quadratic form is a scalar.

So C_5 is a strict local maximum of the margin ratio on the stratum: a negative one-sided derivative in each chord
direction and a negative definite Hessian on the cycle face. The constants -0.380 and -2.047 are measured, not derived.

### The same at C_7

t104_cn_first_order.py generalises the C_5 script to C_n, n odd (t104_cn_first_order_n7.out, n = 7; the run stopped at
its time limit after four of twelve face directions). C_7 has ratio 0.653753. Near it the stratum has dimension 18:
fourteen chord directions, which fall into two dihedral orbits (cyclic distance 2 and 3), and a four-dimensional face
of weighted 7-cycles. Chords lower the ratio at first order: slope -0.658 for a distance-2 chord, -0.129 for a
distance-3 chord. On the face the ratio falls quadratically in each of the four random directions tried, with
curvature between -9.4 and -11.0. A spread is expected here, unlike the single value at C_5: the four-dimensional face
splits into two two-dimensional irreducible representations of the dihedral group, each with its own scalar. So C_7 is
also a strict local maximum of the ratio on the stratum, by a wider margin (0.654 against the limit 1).

### The double-top searches at n = 6 and n = 7

The stratum search of t104_degen_top.py (Nelder-Mead on the relative top gap from the start families, then H evaluated
wherever gap12/lambda is below the tolerance) ran to completion on Mac mini 2 at n = 6 (seed 42) and n = 7 (seed 43),
one hour each.

    n = 6: 3,173 rounds, 301,525 points on the stratum, no negative value, smallest H 1.000009
           (at the balanced triangle 12, 13, 23, the other weights below 5e-7)
    n = 7: 1,837 rounds, 179,303 points on the stratum, no negative value, smallest H 1.000014
           (at two equal disjoint edges 26, 45, the other weights below 2e-6)

With n = 5 (516,075 points, smallest 0.999996 just off the stratum at two disjoint edges and a 4e-6 bridge) this makes
about one million stratum points with H >= 1 to search precision. The minima sit exactly at the two equality cases of the
lemma lambda <= 1. Every round whose smallest H is below 1.01 (1,879 of 3,173 at n = 6, 519 of 1,837 at n = 7) has two or
three edges of weight above 0.05, so the search walks toward those configurations and finds no other basin near 1. The
snapshots t104_dg_n6_s42_snapshot.out and t104_dg_n7_s43_snapshot.out keep every round with H < 1.02, every hundredth
round, and the totals.

### Odd circulants with n >= 21

Take n odd, m = (n-1)/2, weight w_s = a_s/n on the n edges {i, i+s} (s = 1..m, sum a_s = 1), C_j(s) = cos(2 pi j s/n) and
theta_j = (2/n) sum_s a_s (1 - C_j(s)). If the largest theta_j is attained at one frequency k, then lambda = theta_k is
double with Top spanned by the cosine and sine at frequency k, and the low eigenvectors come in cos/sin pairs at the other
frequencies j = 1..m. Every term of the target is then a Fourier sum:

    sum g Q = 16 sum_s (a_s/n)(1 - C_k(s))(lambda - 2/n - a_s/n),
    P_j     = 4 theta_j + 8 lambda/(n-2) - 16 (1 - sum_s a_s C_k(s) C_j(s))/(n(n-2)) + 4 (1 - lambda)(n-4)/(n-2)^2,
    sum g P = sum_{j != k} (lambda - theta_j) P_j

(P_j is the trace over Top and over the pair at frequency j). The first comes from the edge form 2 sum_e w_e tau_e gamma_e
with tau_e = (4/n)(1 - C_k(s)) and gamma_e = 2 lambda - d_i - d_j - 2 w_e, d = 2/n; the second from sum_u u_i^2 = 2/n on Top.
Both agree with the direct computation to 2e-15 on 240 random circulants at n = 5..15 (t104_circ_fourier.py, _out).

**Proposition (proved).** For odd n >= 21, every circulant with a unique top frequency satisfies sum g Q <= sum g P.

*Proof.* Since sum_{s=1..m} (1 - C_k(s)) = n/2, Cauchy-Schwarz gives sum_s a_s^2 (1 - C_k(s)) >= (n lambda/2)^2 (2/n), and with
sum_s a_s (1 - C_k(s)) = n lambda/2 this yields sum g Q <= (8 lambda/n)((n-1) lambda - 2). For the other side, 0 <= theta_j <= lambda,
sum_{j=1..m} theta_j = 1 (because sum_{j=1..m} C_j(s) = -1/2) and 1 - sum_s a_s C_k(s) C_j(s) <= 2 give
P_j >= 4 theta_j + K(lambda) with K(lambda) = 8 lambda/(n-2) - 32/(n(n-2)) + 4 (1 - lambda)(n-4)/(n-2)^2, and so
sum g P >= K(lambda) sum_{j != k} (lambda - theta_j) = K(lambda) ((n-1) lambda - 2)/2. Here (n-1) lambda - 2 > 0, since lambda is
larger than the average 1/m of the theta_j. Hence sum g Q <= sum g P as soon as E(lambda) = K(lambda)/2 - 8 lambda/n >= 0.
E is linear in lambda, and 2/(n-1) < lambda < 4/n, so it is enough to check the two ends, which are

    E(2/(n-1)) = 2 (n^3 - 19 n^2 + 60 n - 48) / (n (n-2)^2 (n-1)),   E(4/n) = 2 (n^3 - 24 n^2 + 80 n - 64) / (n^2 (n-2)^2).

The two cubics have largest real roots 15.279 and 20.196 (t104_circ_ends.py, output appended to t104_circ_linear.out),
so both ends are positive for n >= 21; t104_circ_linear.py confirms in exact rationals that both ends are positive for odd n = 21..201 and that an end is negative for every odd n <= 19. QED

The bound is crude at both places it loses (the cross term bounded by 2, and sum g theta >= 0), which is why it fails for
n = 5..19, where the measured worst ratios are 0.877, 0.654, 0.507, 0.413 at n = 5, 7, 9, 11. Next: for fixed k both
sides are quadratic forms in a, so for small n the claim is a nonconvex QP over the polytope {a >= 0, sum a = 1,
theta_k >= theta_j}, and can be settled exactly face by face. Even n (the s = n/2 orbit) and circulants with a tied top
frequency (D >= 4) are not covered.

### Odd circulants with n <= 17: an exact face search

For a fixed top frequency k, F(a) = sum g P - sum g Q is a quadratic form in the weights once sum a = 1 is used to
homogenise, and the circulants with top frequency k form the polytope {a >= 0, sum a = 1, theta_k >= theta_j for all j}.
The minimum of a quadratic over a polytope is attained at a KKT point of some face, so enumerating every active set of
the m + (m - 1) inequality constraints and solving the KKT system on each face finds it (t104_circ_qp.py; the quadratic
form is read off the Fourier formulas of the previous section and checked against them at a random point).

NUMERICAL (floating point, lstsq on each face): for every odd n from 5 to 17 and every top frequency k, the minimum of F
over the polytope is 0 to 4e-15, attained at the uniform weights, which is K_n with all theta_j equal and both sides zero.
Every other KKT point has F at least 0.100, 0.118, 0.083, 0.059, 0.044, 0.033, 0.026 at n = 5, 7, ..., 17
(t104_circ_qp_5_13.out, t104_circ_qp_15_17.out). With the proposition for n >= 21, the stratum claim holds on every odd
circulant with a unique top frequency except at n = 19 (running); the small cases rest on floating point and a rigorous
version would repeat the face enumeration in exact arithmetic over Q(cos(2 pi/n)).

### All weighted circulants, all D >= 4, and constant-diagonal projectors with n >= 8

PROVED (Codex worker run STRAT on Mac mini 1, 12 Nov; full text t104_strat_RESULT.md; audited by an independent script,
t104_strat_audit.py / .out). Three statements, in the notation of the trace form (X1 = D sum_e w_e gamma_e, Qtotal = 2 S5 =
2 sum_e w_e tau_e gamma_e, X2, X3 >= 0):

1. D >= 4. Since tau_e = |Pi b_e|^2 <= |b_e|^2 = 2 and w_e gamma_e >= 0, Qtotal <= 4 sum_e w_e gamma_e = (4/D) X1, so
   T = X1 + X2 + X3 - Qtotal >= (1 - 4/D) X1 >= 0. (The edge-excess form of push 118 already said only edges with
   tau_e > D/2 push against T; at D >= 4 there are none.)
2. Constant diagonal Pi_ii = D/n, n >= 8. |Pi_ij| <= sqrt(Pi_ii Pi_jj) = D/n gives tau_e <= 4D/n, hence
   Qtotal <= (8/n) X1 <= (8/n) Ptotal. This covers every weighted vertex-transitive graph with n >= 8 (the spectral
   projectors commute with the automorphisms), in particular every circulant with n >= 8, by a far shorter route than the
   Fourier proof for odd n >= 21 above, which it supersedes.
3. Circulants with n = 5, 6, 7. For a fixed top set K the target is a quadratic in the orbit weights on a polytope sector; if
   the sector is the hull of v_0..v_s, T(sum alpha_i v_i) = sum alpha_i alpha_j q_ij with q_ij = 2T((v_i+v_j)/2) - (T(v_i)+T(v_j))/2,
   so an entrywise nonnegative q proves T >= 0 on the sector. The certificates: n = 5, K = {1} (entries in Q(sqrt 5)); n = 6,
   K = {1}, {2}, {1,3}, {2,3} (rational); n = 7, K = {1} (entries in Q(2cos(2pi/7)), each at least 1/10 by a rational bracket
   1.246 < 2cos(2pi/7) < 1.247). Relabelling j -> aj mod n reduces the other unique top frequencies to K = {1}; every other top
   set has D >= 4. At n = 5 the worst ratio is exactly 18 sqrt 5 / (25 sqrt 5 - 10) = 0.87686, attained at C_5.

AUDIT (t104_strat_audit.out): the sector vertices recomputed from the inequalities match in all six sectors; every q entry
recomputed from the original pair definitions (real Fourier eigenvectors, P_l and Q_l summed over top pairs) agrees with the
certificate to 6.5e-16; 200 random points per sector satisfy T = alpha' q alpha to 1e-12 and T >= 0; the root bracket is exact
(f(1.246) < 0 < f(1.247)) and the exact minimum of the nine nonzero n = 7 entries over the bracket is 7688343/76562500 = 0.10042,
above the stated bound 0.10023. The two general arguments were checked by reading: each is two lines from tau_e <= 2 and
|Pi_ij| <= sqrt(Pi_ii Pi_jj). The face search above (now including t104_circ_qp_19.out: n = 19, every k, min F = 0 only at
uniform, every other KKT point >= 0.0212) agrees.

So the stratum claim holds for every weighted circulant (n = 4 by N4_PROOF.md), every graph with D >= 4, and every graph on
n >= 8 vertices with constant projector diagonal. Open: D = 2 or 3 with a nonconstant diagonal of Pi; the bound tau_e <= 2
fails to close C_5 there (every C_5 edge has tau_e = 2 lambda > 1 = D/2).


## Uniform joins with a capped interior, and a dead route for D = 2

Split the vertices into q >= 3 blocks of sizes a_1, ..., a_q (n in all), put the same weight t on every pair in
different blocks, and put any weighted graph inside each block whose largest Laplacian eigenvalue is below a t. The
vectors constant on blocks and orthogonal to 1 have eigenvalue n t; a vector supported in block a with zero sum has
eigenvalue t(n - a) + h_int with h_int < a t. So lambda = n t, D = q - 1, and Pi has the value 1/a - 1/n on the block of
size a and -1/n off the blocks. Unequal sizes give a nonconstant diagonal.

The cross entries of G = lambda(I - J/n) - L are -lambda/n + t = 0, so G is block diagonal with G_a = a t H_a - L_a
(H_a the centring matrix of the block), whose eigenvalues h on zero-sum vectors lie in (0, a t] and which kills 1_a.
Internal edges have tau = 0; a cross edge between blocks a and b has tau = 1/a + 1/b and gamma = G_ii + G_jj. With
c = 2n/(n-2) and p_a = 1/a - 1/n this gives

    X1 = D sum_a tr((lambda I - G_a) G_a),      X2 = c sum_a p_a tr(G_a^2),
    X3 = (1 - lambda)/(n-2) sum_a (D - c p_a) tr(G_a),      2 S5 = 2t sum_a (q - 2 + n/a) tr(G_a).

Theorem. T >= 0 for every member of the family.

Proof. q >= 5 is the case D >= 4. For q = 4 (D = 3) the only edges with tau > 3/2 join two singleton blocks, and those
have gamma = 2nt - 2t(n-1) - 2t = 0; so 2 S5 <= 3 sum w gamma = X1. For q = 3 (D = 2) compare X1 + X2 with 2 S5 one
eigenvalue h of one G_a at a time (a >= 2; singleton blocks have G_a = 0). After dividing by h > 0 the margin is
2nt - 2t(1 + n/a) - A_a h with A_a = 2 - c p_a = 2((n-1)a - n)/(a(n-2)) > 0, smallest at h = a t, where

    a(n-2) [2(n-1) - 2n/a - a A_a] / 2 = (n - 2 - a)((n-1)a - n) >= 0,

since a <= n - 2 when q = 3. Finally X3 >= 0 because 1 - lambda >= 0 (D >= 2 and tr L = 2) and D - c p_a =
2(a(n-1) - n)/(a(n-2)) >= 0 for a >= 2. []

The derivation is from the second Codex run on Mac mini 1; the identities and the endpoint factorisation were rederived by
hand, and t104_join_audit.py (output t104_join_audit.out) checks them on 400 random joins (q = 3, 4; block sizes 1-5;
interiors up to 0.999 of the cap): D = q - 1 and lambda = n t every time, block formulas against the direct sums to
5.3e-14, T >= 0 (smallest 5.3e-3), the q = 3 margin X1 + X2 - 2 S5 >= 0 with equality reached at a = n - 2 on the cap,
largest 2 S5/(X1 + X2 + X3) = 0.923. The argument is the first in this file that uses X2 term by term in the eigenbasis
of G; for D = 2 that is the only way it can go, as the next paragraph shows.

Bounding tau_ij by (sqrt Pi_ii + sqrt Pi_jj)^2 in 2 S5 and keeping X1 + X2 + X3 as they are fails at n = 5: the bound
exceeds X1 + X2 + X3 by up to 3.65 percent on 15 stratum points (t104_diag_route.py, t104_diag_route_n5.out), and the
cruder 2(Pi_ii + Pi_jj) by up to 19.7 percent, while the exact ratio there is at most 0.8505. A proof for D = 2 cannot
replace tau by a function of the diagonal of Pi alone.

Still open: D = 2 or 3 with a nonconstant diagonal outside the join family.

## A neighbourhood of the complete graph, and n = 5 with D = 3

Two further partial results, with full proofs in t104_strat2_result.md (Codex run STRAT2, 12-13 Nov). Notation as above, with s = tr G = (n-1)lambda - 2, B = (D-1)n - 2D and Z = (n-1)(n-2)^2(n+2D) - B(n-4).

Theorem (neighbourhood of K_n). For n >= 5 put

    eps_n = (n-4)(3n-8) / [(n-1)(n-2)^2(n+4) - (n-4)^2].

Every graph on the stratum with s <= eps_n satisfies T >= 0, strictly when 0 < s < eps_n, for every top multiplicity D >= 2 and with no assumption on diag Pi. In edge weights this covers the box max |w_ij - 2/(n(n-1))| <= eps_n/(n(n-1)). Values: eps_5 = 7/323, eps_8 = 1/47, eps_12 = 7/548.

The proof combines four estimates. Any unit v orthogonal to 1 has v_i v_j <= (n-2)/(2n), so G_ij <= kappa s with kappa = (n-2)/(2n), and w_ij = lambda/n + G_ij. The zero row sums of Pi and G and Pi G = 0 give the identity sum_{i<j} tau_ij gamma_ij = n S2 + D s, so 2 S5 <= 2(lambda/n + kappa s)(n S2 + D s). Since Pi + vv' <= H for every unit v in the complement of the top space in 1-perp, Cauchy-Schwarz gives S2 <= eta s with eta = D(n-1)/(n(D+1)). Finally X1 >= D(lambda s - s^2) because tr G^2 <= s^2. The coefficient of S2 is nonpositive, and assembling gives

    T >= D s / [(D+1) n (n-2)^2] * [B(3n-8) - Z s].

The threshold B(3n-8)/Z increases in D, so D = 2 is the binding case.

Theorem (n = 5, D = 3). Here G = g vv' with v a unit zero-sum vector and lambda = (2+g)/4, and

    T = g/45 * [7 + 16g + (70 - 200g) m4 + 120 g m3^2],    m_k = sum_i v_i^k.

On the unit zero-sum sphere in R^5 the maximum of m4 is 13/20 (Lagrange: at most three coordinate values, then a finite case list). Hence T >= 0 whenever g <= 35/76, that is lambda <= 187/304.

Checks. t104_strat2_audit.py builds 3000 random stratum graphs (n = 5..10, D = 2, 3, 4; 1470 of them with s < eps_n) and computes T from the definitions of this file: the identity holds to 8e-15, G_ij <= kappa s and S2 <= eta s hold on all of them, T minus the displayed lower bound has minimum 9.9e-7, and every graph with s < eps_n has T > 0. On 774 graphs at n = 5, D = 3 formula (4) agrees with the definitions to 2e-15, the largest m4 found by ascent is 0.650000, and T >= 6.2e-3 where g <= 35/76 (the remaining window is closed in the next section). t104_strat2_sym.py confirms symbolically that the assembled bound equals the displayed one, the derivative of the threshold in D, and the n = 5 threshold.

Equitable partitions. t104_equitable_test.py replaces the uniform cross weights of the join family by Sinkhorn-balanced block matrices, so the block contrasts stay top eigenvectors while G is no longer block diagonal. T > 0 on every kept instance (q = 3: 43 instances; q = 4: 13). The equitable case is proved in the next section, where X3 is needed for block sizes 1, a, b: there X1 + X2 >= 2 S5 can fail.

Searches over nonconstant diag Pi (STRAT2, 60-digit reprojection) give largest ratios 2 S5/(X1 + X2 + X3) of 0.808 (n = 8, D = 2), 0.786 (9, 2), 0.777 (10, 2), 0.729 (12, 2) and at most 0.546 for D = 3. No counterexample. Still open: D = 2 and D = 3 away from these families.

## n = 5 with D = 3 in full, and equitable partitions into three or four blocks

Proofs in t104_strat3_result.md (Codex run STRAT3, 12 Nov). Notation as above.

Theorem (n = 5, D = 3). Every graph on five vertices whose top eigenvalue has multiplicity exactly three satisfies T >= g/9 > 0, where G = g vv' and g = 4 lambda - 2. With m_k = sum_i v_i^k, a = max v_i, b = -min v_i and p = ab = max_{i<j}(-v_i v_j), the residues r_i = (a - v_i)(b + v_i) are nonnegative with sum 5p - 1, and weighted Cauchy-Schwarz on sum v_i r_i = h - m3 and sum v_i^2 r_i = p + h m3 - m4 (h = a - b) gives

    m4 <= p + (3 + 5p) m3^2 / 4.

Nonnegative weights w_ij = lambda/5 + g v_i v_j give p <= (2+g)/(20g). For g <= 7/20 every nonconstant term of the bracket in formula (4) is nonnegative; for 7/20 <= g <= 2/3 the two bounds give

    7 + 16g + (70 - 200g) m4 + 120 g m3^2  >=  5 + (3g-2)(4g-7)/(2g) + 5(14 + 51g - 68g^2)/(8g) m3^2  >=  5.

The weight constraint enters only through p; without it the bracket goes negative inside the window 35/76 < g <= 2/3.

Theorem (equitable partitions, q = 3 or 4). Let the vertex set split into q nonempty blocks whose cross matrices C_rs have every row sum lambda a_s/n and every column sum lambda a_r/n, with lambda the top eigenvalue of multiplicity exactly D = q - 1. Then T > 0. For q = 4, and for q = 3 with no singleton block, X1 >= 2 S5 already: X1 = D sum w_ij gamma_ij, tau_ij = 0 inside a block and tau_ij = 1/a + 1/b <= D/2 across blocks of sizes a, b, and gamma_ij = 0 between two singletons. Two singletons reduce to the identity X1 + X2 - 2S5 = A0 tr[A(hH - A)] with 0 <= A <= hH. Block sizes 1, a, b with a, b >= 2 need X3: from 0 <= G_rr <= (lambda a_r/n) H_r, the bound ||B||_F^2 <= h_b tr A (and its mirror) for the cross block B of G, and lambda <= n/(ab + a + b),

    T >= [E_a/h_b + E_b/h_a - K] ||B||_F^2,    E_a/h_b + E_b/h_a - K >= 2(n-5)/[ab(n-2)^2] >= 0.

The inequality X1 + X2 >= 2 S5 does not hold for every equitable partition. The graph on {0}, {1,2}, {3,4} with w_0j = 1/8, w_13 = w_24 = 49/200, w_14 = w_23 = 1/200 and no internal edges has Laplacian spectrum 0, 27/200, 123/200, 5/8, 5/8 and

    X1 = 723/5000,  X2 = 241/5000,  X3 = 1/16,  2S5 = 2071/10000,  X1 + X2 - 2S5 = -143/10000,  T = 241/5000.

Checks. strat3/exact_audit.py (Codex) checks every coefficient identity in rationals, the moment bound on 3000 rational zero-sum vectors and the example. t104_strat3_audit.py checks the same identities again in sympy, the moment bound on random unit zero-sum vectors (minimum slack 6.7e-4), the bracket over 1313 feasible pairs (v, g) (minimum 9.75), the 1, a, b bound on 371 random Sinkhorn-balanced graphs with a, b in 2..6 (T minus the lower bound >= -3e-16, minimum T 4.2e-2, minimum X1 + X2 - 2S5 -2.0e-2), and the example's spectrum and terms exactly.

Row T104 after this: proved for D >= 4, circulants, the K_n neighbourhood, n = 5 with D = 3, and equitable partitions with D = 2, 3. Open: D = 2 and D = 3 with a top space that is not spanned by block contrasts, for example n = 5 with D = 2 and n = 6 with D = 3 away from the K_n neighbourhood.

## n = 5 with D = 2: disconnected graphs and three regions of the connected stratum

Proofs in t104_strat4_result.md (Codex run STRAT4, 13 Nov). Write G = a uu' + b ww' with u, w orthonormal and zero-sum, 0 < b <= a <= lambda = (2 + a + b)/4, and w_ij = lambda/5 + G_ij. In the moments A = sum u_i^4, B = sum w_i^4, C = sum u_i^2 w_i^2, d = sum u_i^3, e = sum u_i^2 w_i, f = sum u_i w_i^2, h = sum w_i^3, T has a closed form (formula (1) of the result) in which the odd fourth moments sum u_i^3 w_i and sum u_i w_i^3 cancel. The cubic part is

    R = (8/3) a^2 [d + 3sf/(8a)]^2 + (8/3) b^2 [h + 3se/(8b)]^2 + (7b-a)(b+9a) f^2/24 + (7a-b)(a+9b) e^2/24,   s = a + b,

so R >= 0 whenever b/a >= 1/7.

Theorem (disconnected graphs). T >= 0 for every disconnected graph on the n = 5, D = 2 stratum. Equality holds exactly at the balanced triangle with two isolated vertices and at two disjoint edges of weight 1/2 with one isolated vertex. With one isolated vertex, T is a concave quadratic in the remaining gap, positive at gap 0, and at the weight boundary its numerator equals 2048 times an explicit degree-six polynomial in the three ordered differences of the four-vector, nonnegative after splitting one binary quartic at x = y.

Theorem (connected regions). With r = b/a and D(r) = 34 + 52r - 22r^2 + (1-7r)_+(9+r)/2, every graph on the stratum with a <= 14(1+r)/D(r) has T >= 0. The threshold is at least 4/11 for every r and equals 7/16 at r = 1. Independently, b/a <= 1/3000 gives T >= 2a/2025: the rank-one boundary functional satisfies T(a,0) >= a/81, by a certificate of 165 rational 3-by-3 coefficient matrices with every principal minor positive, and the weight constraint a(20p-1) <= 2 + 11b lets a rank-two graph be compared with a feasible rank-one graph with the same u.

The worst quotient found, in 14,400 constrained optimisation starts over two coordinate charts, is

    T/(X1+X2+X3) = 0.0202763515094560301...,

attained on the one-parameter family of a triangle with a pendant vertex and an isolated vertex, where the quotient is an explicit rational function and its minimiser is the root near 6.3942 of a sextic. The rational member l = 32/5 has quotient 55411/2732767 < 1/40. The cycle C5 gives 0.1231. This is a numerical estimate of the infimum, not a bound.

Checks. strat4/exact_audit.py, isolated_certificate.py, rank_one_certificate.py and sparse_family.py rerun cleanly here in sympy. t104_audit_isolated.py samples 40,000 random isolated-vertex graphs (T > 0, quotient >= 0.0209, approaching the sparse minimum at the weight boundary). t104_audit_regions.py samples 3,000 feasible frames in each of the regions a <= 4/11 and a = b <= 7/16 and 3,000 unrestricted ones (T > 0; least quotients 0.168, 0.149, 0.173).

Row T104 after this: proved for D >= 4, circulants, the K_n neighbourhood, n = 5 with D = 3, equitable partitions with D = 2, 3, and, for n = 5 with D = 2, every disconnected graph and the connected graphs with a <= A0(b/a) or b/a <= 1/3000. Open: the rest of the connected n = 5, D = 2 stratum, and D = 2, 3 for n >= 6 away from the cases above.

## n = 5 with D = 2: more of the connected stratum

Proofs in t104_strat5_result.md (Codex run STRAT5, 13 Nov). Notation as in the previous section; r = b/a, s = a + b.

For a fixed frame (u, w), T(a, ar)/a is affine in a: T = a L_u + b L_w + a^2 P + ab Q0 + b^2 R_w, with L_u = 14(A + C - 1/5)/9 and P, Q0, R_w explicit in the moments. Every frame satisfies

    7/30 <= A, B <= 13/20,   0 <= C <= 3/10,   1/4 <= A + C, B + C <= 4/5,   A + B + 2C <= 7/5,   2C <= A + B.

The upper bounds come from ||diag Z||^2 <= (3/5)||Z||_F^2 for symmetric Z with Z1 = 0 and tr Z = 0; the lower bounds from 84 exact positive semidefinite coefficient matrices on the ordered cone.

Theorem. On the n = 5, D = 2 stratum, T >= 0 for every graph in each of the following classes, connected or not:
(i) a <= 443/1000, for every r; more generally a <= A1(r), where A1 is the minimum over the 19 vertices of the moment polytope above of an explicit ratio (A1(0) = 448/1067, A1(1) = 5/11);
(ii) 0 < r <= 3/25 (it was r <= 1/3000), by a quartic sum-of-squares certificate with 286 rational 6-by-6 Gram matrices at r = 3/25, after sharpening the rank-one bound to 86/125 and the weight constraint to a(20p - 1 - rk) <= 2 with k <= 7 - 5v^2;
(iii) forty rational cells covering 3/5 <= r <= 1 up to an explicit a_hi per cell;
(iv) equal gaps a = b <= (209 + 3 sqrt 305)/476 = 0.54914... (it was 7/16);
(v) every graph with min w_ij >= (lambda - a)/5, that is, a disconnected frame of the previous section plus a uniform complete graph; there T >= (7/45)(a + b)(lambda - a).

Connected graphs reach the disconnected infimum: adding epsilon to every weight of the rational triangle-plus-pendant member l = 32/5 gives exact quotients 3035108992/79790990305 at epsilon = 1/1000 and 1571443463992/77430760925305 (0.020295) at epsilon = 10^-6, and the quotient tends to 0.0202763515... as epsilon -> 0. So no connected quotient bound above that value holds.

What remains for n = 5, D = 2: connected graphs with 3/25 < r <= 1, a > max(443/1000, A1(r), the cell bound), a < 2/(3 - r), some weight below (lambda - a)/5, and the moment conditions of the result failing. The equal-gap interval above 0.5491 is in it.

Checks. The six replay scripts of the result (moment_explore.py, verify_moments.py, verify_quartic_certificate.py, weight_moment_audit.py, verify_cells.py, rational_connected_family.py) rerun cleanly here. t104_strat5_psd_check.py and t104_strat5_quartic_check.py recheck the rank-one, ratio and quartic certificates in exact Fraction arithmetic from my own formula (the quartic check fails all 286 forms at the wrong ratio r = 1/5, as it should). t104_audit_strat5.py samples 3,000 feasible frames in each of classes (i), (ii), (iv) and (v), with the term code of the earlier audits: T > 0 throughout, least quotients 0.167, 0.204, 0.151 and 0.119, and the moment bounds hold on all 12,000 frames.

Row T104 after this: proved for D >= 4, circulants, the K_n neighbourhood, n = 5 with D = 3, equitable partitions with D = 2, 3, and for n = 5 with D = 2 every disconnected graph and the connected classes (i)-(v). Open: the rest of connected n = 5, D = 2, and D = 2, 3 for n >= 6 away from the cases above.

## n = 5 with D = 2: the radial reduction and a larger connected region (13 Nov)

For a fixed frame (u, w) and ratio r = b/a, the admissible scales form an interval 0 < a <= a_end, where
D_ij = -1 - r - 20(u_i u_j + r w_i w_j), Dmax = max(3 - r, max D_ij) and a_end = 2/Dmax. The projector stays fixed along
the ray, and

    T(a, ar) = a (1 - a/a_end) L(r) + (a/a_end)^2 T(a_end, r a_end),        L(r) >= 7(1 + r)/90 > 0.

So T >= 0 on the whole ray if and only if it holds at the far end, which is either disconnected (already proved) or has a zero
weight. The reduction does not iterate: on a zero face the zero weight becomes positive as soon as the scale decreases.

Proved in addition, with exact certificates (strat6/):
- eight moment inequalities in A = sum u^4, B = sum w^4, C = sum u^2 w^2 (and K = A + B + 2C >= 4/5), by Polya multipliers;
  5,445 rational 3-by-3 coefficient matrices checked by principal minors;
- 176 rational (r, a) cells (88 base, 44 on a 33-vertex moment polytope, 44 directional) covering 3/25 <= r <= 1 up to the
  uniform ceiling a <= 103/200, higher on most cells;
- the equal-gap case r = 1 up to G, the real root in (551/1000, 69/125) of 6272 G^3 - 2989 G^2 - 1034 G + 427 (G ~ 0.551713;
  the previous endpoint was 0.549144);
- 47 rational boxes directly on the zero-weight face (the face polynomial has 1,254 coefficients), which together with the
  moment tests cover all 76 exact endpoint witnesses found by search.

What remains: connected frames with 3/25 < r <= 1, max(103/200, cell ceilings) < a < 2/(3 - r), whose far endpoint is connected,
has a zero weight, fails every moment test at both a and a_end, and lies in none of the 47 face boxes. The proof is RESULT.md
(t104_strat6_result.md). Replays: all nine certificate scripts rerun here (77 s, rc 0) and on Mac mini 1. Independent black-box
checks with separate term code: t104_audit_strat6_result.py (equal gap at G, a = 58/125 over r, the moment slacks, (W2), the ray
identity to 3e-7), no negative T; t104_audit_strat6_final.py (every cell at its ceiling, and a = 103/200 over 23 ratios) finds least T 6.9545e-02 over 528 cell
points and 7.8453e-02 at a = 103/200, no negative T.
Row T104: not solved.

## Disconnected N = 6 with D = 2 (13 Nov)

Proved (Codex STRAT7, strat7/): T >= 0 for every disconnected six-vertex graph on the D = 2 stratum whose components are
4+2 (the four-vertex part carrying one or both top eigenvalues), 4+1+1, 3+3, 3+2+1, 3+1+1+1, 2+2+2 or 2+2+1+1, with boundary
graphs included. Equality holds exactly at the balanced triangle of weight 1/3 with three isolated vertices and at two edges of
weight 1/2 with two isolated vertices. Padding: X1 and S5 do not depend on the number N of isolated vertices, X2 = 2N B/(N - 2)
and X3 = (1 - lambda)[D(N - 1)(N - 4)lambda - 2D(N - 2) + 2N h]/(N - 2)^2, so each fixed-graph statement holds for every N >= 6.
Also, S5 = 0 implies T >= 0 for every N on the D = 2 stratum.

Open: 5+1, a connected five-vertex component carrying both top eigenvalues plus one isolated vertex; proved there for internal
scale a <= 11/25 (margin 94/3125). Disconnected graphs with larger components on N >= 7 are not covered.
Replays: the seven certificate scripts rerun here (rc 0). Black-box: t104_audit_strat7_padding.py (padding identities) and
t104_audit_strat7_classes.py (two-carrier classes built with a forced tie, Nelder-Mead on T: least T -3e-16, the equality cases
give T = 0).

## The 5+1 class and the residual face (13 Nov 2026)

5+1 class at N = 6 (t104_strat9_result.md, folder strat9/). For a connected five-vertex carrier with both top eigenvalues and one
isolated vertex, T >= 0 holds at every admissible scale when 0 < b/a <= 3/20, for every frame when a <= 14/25 (previously 11/25),
and up to the rational scale ceilings of the ratio-strip table (66/125 on r in [0, 1/10] up to 76/125 on [3/10, 1/2], 14/25 on
[9/10, 1]); also for every frame passing a saved pointwise moment bound, every frame whose radial endpoint lies in one of the 47
face boxes, and every frame whose radial endpoint is disconnected. With more isolated vertices, every N >= 6: b/a <= 3/25,
a <= 64/125, the all-N ceilings, the same 47 boxes. Open: the explicit intersection (11) of t104_strat9_result.md, and for N >= 7
the same region with r > 3/25 and a > max(64/125, Vinf(r)). residual_witness.json is a rational point of (11) missed by every
covering certificate and has T6 = 2219640933/6719605760 > 0, so the gap is real but no counterexample is known.

Residual face for n = 5, D = 2 (t104_strat8_result.md, folder strat8/). 43 new closed rational face boxes with Cface > 0 cover 34
exact connected zero-weight endpoints that miss every earlier certificate. An exact bisection tree of the whole face chart (80,363
nodes, leaf volumes summing to the root volume 1152) splits it into 24,702 nonnegative leaves, 10,208 leaves excluded by exact
necessary conditions, and 5,272 open leaves, listed in open_boxes.json. A pendant subface theorem is in pendant_symbolic.txt.

Replays. Both exact replays were rerun on Mac mini 2 with a separate Python (sympy 1.14): strat9/replay_mini2.txt (17 of 17 scripts
pass) and strat8/replay_mini2.txt (same 80,363 nodes and leaf counts). Black-box searches: t104_audit_strat9_51.py finds least T 0.1397 (least T/a^2 0.205) on the 5+1
class. t104_audit_strat6_final.py finds least T 0.0703 on the 88 strong and 0.0695 on the 44 enhanced moment cells at their
ceilings, and 0.0749 on the 44 directional cells (t104_audit_strat6_final.out: 528 cell points, least T 6.9545e-02, all positive).

Status of T104: not solved. Open on (11) for 5+1, on the 5,272 face leaves for n = 5, and for connected carriers with n >= 6.

## Region (11) of the 5+1 class at N = 6: sextic moment bound, wider ceilings, and a zero at the corner

Codex STRAT10 (strat10/, result t104_strat10_result.md) worked on the residual region (11) left by STRAT9.

A new exact inequality: for every zero-sum unit vector u in R^5,

    (sum u_i^3)^2 >= 3 sum u_i^4 - 3/2,

proved by writing the homogeneous sextic as 625 K^2 plus a sum of nonnegative monomials in the sorted gap coordinates
(cubic_moment_certificate.json, verify_cubic_moment.py; a second Gram certificate in cubic_sos.json). It is sharp, with
equality at u = (-1,0,0,0,1)/sqrt 2; t104_check_strat10_sextic.py checks it independently on 400,000 random vectors and
40 local searches. Averaged over alpha u +/- beta w it gives degree-six frame inequalities, which added to the STRAT9
cells raise the uniform scale ceilings to a <= 2849/5000 at N = 6 (from 14/25) and a <= 129/250 for every N >= 6 (from
64/125); the ratio-dependent ceilings rise to between 3/5 and 31/50 (ceiling_table.csv).

The region cannot be closed by cells alone. The connected family U = (-4, 1+s, 1+s, 1-s, 1-s), W = (0,1,-1,-1,1), r = 1,
a = (5+s^2)/(5+10s-s^2), 0 < s <= 1/100, satisfies every filter of (11) and has

    T6 = s(1100 - 335s + 185s^2 + 19s^3 + 26s^4 - 11s^5) / [4(s^2+5)(s^2-10s-5)^2],

positive and tending to 0 as s -> 0 (pressure_family.json, verify_family.py, every N >= 6). So the infimum of T on (11)
is 0, attained at the corner r = a = 1. The exact partition of the N = 6 chart ends with 24,708 positive leaves (24,458
of them valid for every N >= 6), 10,226 excluded and 5,244 open leaves after 80,355 visits (global_cover.json); the open
count grew with refinement, as the corner predicts. Sampling 160,000 rays found no negative value; the least sampled T is
about 4.7e-4 near r = 0.9997, a = 0.9996. Every certificate is replayed in exact rational arithmetic by replay_all.py,
rerun from scratch on Mac mini 2 (strat10/replay_mini2.txt).

The corner is attacked separately (STRAT11) by a local expansion: the first-order part of T at r = a = 1 is
(11/10)(1-a) - (1/20)(1-r), and admissibility gives 2(1-a) >= 1-r to first order, so no tangent direction is negative.
