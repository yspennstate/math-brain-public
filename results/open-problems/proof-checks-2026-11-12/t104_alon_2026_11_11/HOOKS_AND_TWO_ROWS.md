# Hooks, conjugation, and the family tau = [2, 1^(n-2)], sigma = [2, 2, 1^(n-4)] (working note, 11 Nov 2026)

Status: sections 1-3 and Lemma U of section 7 are short proofs, checked numerically (hooks_check.py,
hooks_check.out). Section 4 is a conjecture with numerical support. Section 5 reduces it to a covariance condition
and records the constructions tried. Sections 1-3 and 7 were read and checked with independent code by an agent (11 Nov 01:34Z, brain main 6abb227c, lean_checks_agent/t104_alon_n4/hooks_referee/); Sections 4-7 and GAP_STATE_FORM.md were then refereed by a Codex reader (gpt-6.1-sol high, Mac mini 1, 11 Nov,
AUDIT_CODEX_HOOKS_REPORT.md): the representation identities and the scalar algebra CORRECT; three statements
WRONG and three justifications with a GAP, all corrected below and marked [referee]. Nothing in the note is a
proof of Conjecture F or of Alon's conjecture for general n.

Notation as in N4_PROOF.md. V = {x in R^n : sum x_i = 0}, L_G the graph Laplacian on V with eigenvalues
0 < lambda_1 <= ... <= lambda_(n-1) (for connected G), W the total weight.

## 1. Hooks are exterior powers

Lemma H. For 1 <= k <= n-1 the operator L(G, [n-k, 1^k]) is the derivation of L_G on the exterior power
Lambda^k V: it sends x_1 ^ ... ^ x_k to the sum over a of x_1 ^ ... ^ L_G x_a ^ ... ^ x_k. Its eigenvalues are the
sums of k distinct eigenvalues of L_G on V. In particular
    lambda_min(G, [n-k, 1^k]) = lambda_1 + ... + lambda_k.

Proof. V_[n-k,1^k] = Lambda^k V_[n-1,1] = Lambda^k V. A transposition (i j) acts on V as the reflection
s = I - 2P, P the projection on the line of e_i - e_j. Since P has rank one, P x ^ P y = 0, so
Lambda^k(I - 2P) = I - 2 D(P), with D(P) the derivation of P. Hence I - Lambda^k(s) = D(2P) = D(I - s); multiply by
w_ij and add. QED

Consequence. For hooks sigma = [n-j, 1^j], tau = [n-k, 1^k] with 1 <= j < k,
    lambda_min(G, tau) / lambda_min(G, sigma) = (lambda_1 + ... + lambda_k)/(lambda_1 + ... + lambda_j) >= k/j,
so the conjecture holds for every pair of hooks, with room. (The search found 3/2 at (1111, 211) and 2 at
(211, 31) for n = 4, and 4/3 at (21111, 3111) for n = 6.)

## 2. Conjugation

For every nu, lambda_min(G, nu') = 2W - lambda_max(G, nu), because V_nu' = V_nu (x) sign. So
lambda_min(G, [2, 1^(n-2)]) = 2W - lambda_max(L_G) for every n, and the conjecture for tau = [2, 1^(n-2)] reads

    lambda_max(L_G) <= 2W (1 - c) + c lambda_max(G, mu),   mu = sigma' not in {[n], [1^n]},   c = 2/3:

the largest Laplacian eigenvalue is controlled by the top of the spectrum in any other representation.
For mu a hook this follows from Lemma H with c = 1.

## 3. A model for [n-2, 2]

V_[n-2,2] = { symmetric n x n matrices T with zero diagonal and zero row sums }, that is, signed weightings of the
edges of K_n whose sum at every vertex is zero, with S_n permuting the vertices. (This subspace of Sym^2 V is
invariant, has dimension n(n-3)/2, and is the kernel of T -> diag T on the trace-zero part, whose complement is
[n-1, 1].) In this model

    <T, (I - (i j)) T> / |T|^2 = sum_{k != i,j} (T_ik - T_jk)^2 / sum_{a<b} T_ab^2.

The orthogonal projection of a symmetric zero-row-sum T with trace 0 onto this space is
    P T = T - (n/(n-2)) Pi diag(T) Pi,     |P T|^2 = |T|^2 - (n/(n-2)) |diag T|^2,
Pi the projection of R^n onto V. Here |T| is the Frobenius norm (the sum over all ordered pairs, twice the sum over
a < b used in the Rayleigh quotient, plus the diagonal) and |diag T| the Euclidean norm of the diagonal.

## 4. The family tau = [2, 1^(n-2)], sigma = [2, 2, 1^(n-4)]

Here sigma' = [n-2, 2]. On the star both sides are Jucys-Murphy spectra: lambda_min(star, tau) = n - 2 and
lambda_min(star, sigma) = n - 1.

Conjecture F. For every weighted graph on n >= 4 vertices
    lambda_max(L_G) <= ( 2W + (n-2) lambda_max(G, [n-2, 2]) ) / (n-1),
equivalently lambda_min(G, [2,1^(n-2)]) >= ((n-2)/(n-1)) lambda_min(G, [2,2,1^(n-4)]), with equality on the star
(and on a single edge, where both sides vanish in the second form).

n = 4 is Theorem 3 of N4_PROOF.md. Support for n >= 5: the ratio search gives 0.750000 at n = 5 and 0.800001 at
n = 6 for this pair (dom_n5.tsv, dom_n6_local.tsv), both on the star; 3000 random weights each at n = 5, 6, 7 give
no violation (hooks_check.out). The constant (n-2)/(n-1) is above 2/3 for n >= 5, so F is stronger than what
Conjecture 1.5 asks for this pair.

Dual form (Proposition 1 of N4_PROOF.md, in the model of section 3). F holds iff for every unit x in V there is a
probability measure on unit-norm T (sum_{a<b} T_ab^2 = 1) in the model with

    (x_i - x_j)^2 <= 2/(n-1) + ((n-2)/(n-1)) E sum_{k != i,j} (T_ik - T_jk)^2      for all i < j.

Two points where the measure is known:
- x the star vector (n-1, -1, ..., -1)/sqrt(n(n-1)): T_1k = a_k, T_kl = -(a_k + a_l)/(n-3) for k, l >= 2, with a
  uniform on the unit sphere of sum-zero vectors (normalised); every star edge is tight.
- x = (1, -1, 0, ..., 0)/sqrt 2: T_1k = a_k = -T_2k, all other entries 0, a uniform as above; the edge 12 is tight,
  E-term 2, and the pairs 1k have E-term 1/2 against a need of (n-5)/(2(n-2)).

## 5. A construction that is exact at both points and fails between them

For a unit x in V and a unit y in V orthogonal to x put T(x, y) = P (x y^t + y x^t)/sqrt 2. With y uniform on the
unit sphere of {1, x}^perp this gives the two measures above at the star vector and at the edge vector. Closed form
(m4 = sum x_k^4, d = x_i - x_j, s = x_i^2 + x_j^2, q = x_i^2 - x_j^2, both sides multiplied by n - 2, pair energy
in the sign-twisted form):

    N = (n-2) - (2/(n-2)) (n - 1 - n m4),
    A_ij = (2 - d^2)(n - 3 + 2 d^2) - (n/(n-2)) [ 4 (1 - 1/n - m4) - 2 (s - d^2/n - q^2) ],
    wanted: (2 - d^2) N - ((n-2)/(n-1)) A_ij >= 0.

canon_state.py checks the closed form against direct matrices (deviation 5e-15) and finds the inequality false:
slack 0 at the star and edge vectors, but -0.140 at n = 4 (x = (-0.846, 0.194, 0.194, 0.458)), -0.237 at n = 5,
-0.303 at n = 6, -0.386 at n = 8, all at vectors of the shape (one large entry, one middle entry, the rest equal).
So the uniform measure in y is not the matching state away from the two extreme points.

A proof of Conjecture F needs less than the per-edge inequality: only sum_ij w_ij slack_ij(x) >= 0 at a top
eigenvector x of L_G. The uniform measure fails that too (canon_primal.py, canon_primal.out): on the path with two
unit edges and the other vertices isolated the weighted slack is -1/18 at n = 4, -1/12 at n = 5, -1/10 at n = 6
(total weight 1).

Weighted version: replace the uniform y by a centred y with covariance C on {1, x}^perp; N and A_ij are linear in
C. canon_cov.py maximises the smallest slack over C for each x. At n = 4 the best C has smallest slack >= 0 at all
120 vectors tried. [referee] This is not automatic: the earlier remark that the vectors P(x.y) span V_22 for
every x was wrong. At n = 4, x = (1,-1,0,0)/sqrt(2), the vector y = (1,1,-1,-1)/2 lies in {1, x}^perp and
P(x.y) = 0, so the image has dimension 1 while dim V_22 = 2; Theorem 3 gives a state on V_22, not one in a
prescribed proper image. At n = 5 (160 vectors) and n = 6 (60 vectors) the best C also has smallest slack >= 0 at every
vector tried, with 0 only at the star vector (canon_cov.out). At n = 5 the vectors P(x.y) span only 3 of the 5
dimensions of V_32, so this is not automatic.

In compact form (star_form_check.py: agreement with the matrices to 6e-15 for n = 4..8): with y centred of
covariance C on {1, x}^perp, tr C = 1, and
    kappa = E sum_k x_k^2 y_k^2,   g_ij = E (x_i y_i - x_j y_j)^2,   c_ij = E (y_i - y_j)^2,   d = x_i - x_j,
the slack of the pair ij times n - 1 is

    (*)   (2 - d^2) + (2 n kappa/(n-2)) ((n-1) d^2 - 2) - 2 n g_ij - (n-2)(2 d^2 - 1) c_ij.

Reduction R. If for every unit x in V there is a covariance C on {1, x}^perp with (*) >= 0 for all pairs ij, then
Conjecture F holds for that n. [referee] The state has to be normalised and the normalisation can vanish. Write
A_x y = P((x y^t + y x^t)/sqrt(2)) and, for C >= 0 of trace one,
    Z = tr(A_x C A_x^*) = 1 - (2n/(n-2)) kappa,     rho(x, C) = A_x C A_x^* / Z   when Z > 0;
(*) is (n-1) Z times the slack of rho(x, C) in Proposition 1 (weighting each image by its squared norm, not
normalising each image first). A_x is injective at a star vector, so its Gram determinant is not identically zero
and A_x is injective for a dense open set of x; there Z > 0 for every C and Proposition 1 applies to rho(x, C).
At an exceptional x take states at nearby injective x and a limit point (the set of density matrices is compact,
the conditions of Proposition 1 are closed). So R holds as stated, with this argument and not the pointwise one. The term in c_ij says what C has to do:
y should vary little across pairs with d^2 > 1/2 and may vary across pairs with d^2 < 1/2, so y lives where x is
flat. At the star vector that is the leaves, at the edge vector the zeros of x.

Explicit choices of C tried so far. None is a proof.

(a) C = Q diag(omega(x_k)) Q / trace, Q the projection onto {1, x}^perp (canon_omega.py). The best member found,
omega(t) = (1 + n t^2)^(-2), leaves the smallest value of (*) at -0.0095 for n = 4 and -0.0006 for n = 5.

(b) Three-valued x = (alpha, beta, gamma, ..., gamma). These form a circle; {1, x}^perp is spanned by the rotated
vector v = x(phi + pi/2) and the block B of sum-zero vectors on the last n-2 coordinates, and by symmetry the best
covariance is C(theta) = theta v v^t + (1 - theta) Pi_B/(n-3). Each of the four pair types gives an affine function
of theta. canon_theta.py: for n = 5, 6, 8, 12, 30 and 4801 points on the circle there is always a theta with all four
nonnegative. The interval of admissible theta shrinks to the single point 1/(n-2) (the uniform state) at the two
star vectors on the circle. [referee] At the edge vector for n = 5 the interval is [0, 1], not [0, 0.18] as first
written from the grid: there v = (3,3,-2,-2,-2)/sqrt(30) has A_x v = 0 and (*) is 0 on the pair 12,
(3/2)(1 - theta) on the pairs 1k, 2k and 5(1 - theta) on the pairs kl (k, l >= 3). At theta = 1, Z = 0; every
theta in [0, 1) gives the same normalised state (y supported on the zeros of x).

(c) Weighted form with a test vector taken from the graph. Let x be a top eigenvector of L_G, eigenvalue lam.
Summing (*) with the weights gives the quadratic form y^t M y on {1, x}^perp,
    M = (2W - lam) I + (2n/(n-2)) ((n-1) lam - 2W) D^2 - 2n D L_G D - (n-2) (2 L2 - L_G),
D = diag(x), L2 the Laplacian with weights w_ij (x_i - x_j)^2; Conjecture F holds for G as soon as y^t M y >= 0 for
one y in {1, x}^perp. On the star and on a single edge M vanishes identically on {1, x}^perp. canon_spectral.py
(W = 1, 20000 weightings for n = 4, 5, 6): the compression of M always has a nonnegative top eigenvalue, but each
of the simple choices is negative somewhere: the trace (uniform state), y the Fiedler vector, y the second-top
eigenvector, C proportional to (lam - L_G)^(-1).

(d) The gap-weighted state C = (lam Pi - L_G)/((n-1) lam - 2W), Pi the projection onto V. It kills x by itself and
is uniform on the star. With it Conjecture F for G follows from Gval(w) := tr(M (lam Pi - L_G)) >= 0, a quadratic
inequality in the weights:

    (n-2)(n-5) lam^2 + 2 lam^2 - (n-2) tr L_G^2 + 2(n-2) P + 4(n-2) S - 2n lam A + 2n tr(D L_G D L_G)
        >= tau^2 - (2n/(n-2)) tau (lam (n-1)/n - A),

with tau = (n-1) lam - 2W, A = sum_i deg_i x_i^2, P = sum_{i<j} w_ij d_ij^2 (deg_i + deg_j), S = sum w_ij^2 d_ij^2.
Both sides equal n(n-1)(n-2)(n-3) on the unit star. canon_gap.py (local search over weights): at n = 4 the
inequality is false, -0.0149 W^2 near two disjoint heavy edges joined by light ones, where the top two eigenvalues
almost coincide; at n = 5 (90 + 12 searches) and n = 6 (60 + 8 searches) no negative value, the minimum 0 at the
star and at a single edge (canon_gap.out, canon_gap_target.out). A larger search for n = 5..8 is queued on Mac
mini 1. If it survives, the statement to prove is: Gval >= 0 for n >= 5; with Theorem 3 for n = 4 that is
Conjecture F.

## 6. What is left at n = 5

By section 2 of N4_PROOF.md (tau = [1^n], sigma = [n-1, 1]) and Lemma H (both hooks), the pairs left are those with
a non-hook: (311, 32), (221, 32), (2111, 32) and (221, 311), (2111, 221). The last one is Conjecture F for n = 5
(value 3/4). The search minimum over the other four is 0.798 at (311, 32); (221, 32) and (221, 311) have minimum 1.

## 7. Disjoint unions, and where the value 2/3 comes from at n = 6, 7, 8

Lemma U. Let G = G_1 + G_2 be a disjoint union on A + B, |A| = k. Then
    lambda_min(G, nu) = min { lambda_min(G_1, mu) + lambda_min(G_2, lam) : c^nu_{mu, lam} > 0 },
the minimum over partitions mu of k and lam of n-k with nonzero Littlewood-Richardson coefficient.

Proof. Restricted to S_k x S_(n-k), V_nu is the sum of c^nu_{mu,lam} copies of V_mu (x) V_lam, and on each copy
L(G, nu) = L(G_1, mu) (x) 1 + 1 (x) L(G_2, lam). QED

Letting the weights of a connected G_2 go to infinity (which amounts to merging the vertices of B) only lam = [n-k]
survives, and c^nu_{mu,[n-k]} > 0 iff nu/mu is a horizontal strip. So the conjecture at n contains, for every graph
G_1 on k vertices,
    min { lambda_min(G_1, mu) : tau/mu a horizontal strip } >= (2/3) min { lambda_min(G_1, mu) : sigma/mu a horizontal strip }.

This is how 2/3 appears at pairs whose own star ratio is larger. [referee] Of the pairs below only (3211, 322) and
(4211, 422) have ratio 1 on the ordinary star; the others have star ratios 5/6, 8/9, 6/9 and 7/9. The search minimum 0.666668 at n = 7,
(tau, sigma) = (3211, 322), is at K_{1,3} with weight t on vertices {1,3,4,5} plus a heavy path on {2,6,7}
(extremal_spectra_n7.out): 3211/211 and 322/22 are horizontal strips, 322/211 and 322/31 are not, so the two bottoms
are lambda_min(K_{1,3}, 211) = 2t and lambda_min(K_{1,3}, 22) = 3t, the n = 4 extremal pair of Theorem 3. The same
holds at n = 6 for (2211, 222) (K_{1,3} plus one heavy edge) and at n = 8 for (4211, 422) (K_{1,3} plus a connected
heavy graph on the other four vertices). [referee] The other three pairs at n = 8 have width two, so a horizontal
strip of size four cannot be removed and the construction is different for each:
    (22211, 2222):   K_{1,3} plus two separate heavy edges, (22211, 2222) -> (2211, 222) -> (211, 22);
    (221111, 2222):  the six-vertex star plus one heavy edge, (221111, 2222) -> (21111, 222), star bottoms 4 and 6;
    (2111111, 2222): the eight-vertex star itself, bottoms 6 and 9 (Theorem 4.5 of Alon's paper).
These explain the value 2/3; they are examples, not lower bounds.

Search minima: n = 4: 2/3; n = 5: 3/4; n = 6: 2/3; n = 7: 2/3 (87 pairs, dom_n7.tsv); n = 8: 2/3 (194 pairs,
dom_n8.tsv). Nothing below 2/3. The pair of Conjecture F has search minimum 3/4, 4/5, 5/6, 6/7 at n = 5, 6, 7, 8.

[referee] zero images. In 5(c) a single y with y^t M y >= 0 certifies the graph only if A_x y != 0, and in 5(d)
Gval >= 0 gives Conjecture F through the covariance state only if the projected trace tau is positive (N != 0);
when the image vanishes the inequality is the empty statement 0 >= 0. These cases are covered by the same limit
argument as in Reduction R, or have to be treated separately. The grid scans called exact in this note and in
GAP_STATE_FORM.md are floating-point evaluations on a grid unless an arithmetic certificate is named.
