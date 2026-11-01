# Semidefinite forms, the lower levels, and the reduction to one hub

Programme QFORM-DENSITY-3EIG-20260922. Record 20260922T231000Z-semidefinite-and-hub-reduction. It continues
record 20260922T211500Z-decoupling-brascamp-lieb (RESULTS.md, GEOMETRIC_ROUTE_REPORT.md, FOURIER_ROUTE_REPORT.md
there), whose notation it uses: X has independent coordinates with densities at most 1, Q = X^T A X + b^T X + c,
and "no c-pivot" means every |a_ii| < c and every 2 x 2 principal minor has modulus < c.

The unrestricted conjecture is not proved here. Each subfolder holds one piece: REPORT.md (statements and full
proofs), NOTES.md (the working record, with the derivations in order) and the scripts with their outputs.

## Proved in this record

1. Semidefinite forms (semidefinite/). If A is positive semidefinite with lambda_3(A) >= 1, then
   ||p_Q||_inf <= 1.71 * 10^4 for every b, c and every product law, whatever the rank of A; by scaling
   ||p_Q|| <= C_0/lambda_3. Negative semidefinite A follows from -Q. Writing A = B B^T makes "no pivot" mean that
   every row of B is small even when rows of A are huge. An exact identity for a random partition gives
   s_k(A_IJ) >= lambda_k/4 with no dimension factor, and the volume-sampling marginals are bounded by twice a ridge
   leverage.
2. Indefinite forms with small |A|-diagonal (semidefinite/, Theorem 4). With |A| = (A^2)^{1/2}: if
   max_i (|A|)_ii <= |lambda|_(k)/680 then a partition exists on which Theorem D (k = 3) applies, and
   ||p_Q|| <= 34.4/|lambda|_(3). So the open part of the no-pivot regime consists of matrices with a coordinate
   that is hub-like in this sense.
3. The lower levels (lower_levels/, architecture/). For matrices with no c-pivot, uniformly in the linear and
   constant terms: sup_s E log_+ 1/|s - Q| <= 12 and alpha_1 <= 25 when one eigenvalue has modulus >= 1;
   sup_s E[|s - Q|^{-1/2}; |s - Q| <= 1] <= 10^6 when two do. With the reduction theorem of the earlier record,
   the conjecture is equivalent to its three-eigenvalue statement for matrices with no c-pivot, for any fixed
   small c.
4. No hub, no pivot (structure/, architecture/). If A has three eigenvalues of modulus >= 1 and every row has
   norm at most 1/20, a random partition has s_3(A_IJ) >= 0.26 and marginals <= 0.11, so ||p_Q|| <= 38. The light-rows
   form: if e_3(nu^2) >= 72 rho_L^2 e_2(nu^2) for the singular values nu of the light rows, Theorem D applies with
   ||p_Q|| <= 22.2 (nu_1 nu_2 nu_3)^{-1/3}.
5. Structure of the failure (structure/, architecture/). All off-diagonal 2 x 2 minors vanish => A is diagonal
   plus rank <= 2 (sharp, stars); in general 2r <= f(r) <= 3r. A skeleton identity gives a robust version with a
   Frobenius remainder. A dichotomy: either Theorem D applies to a partition that puts the heavy rows on the
   unconstrained side, or the light block is diagonal + rank two + a zero-diagonal remainder of small Frobenius
   norm, i.e. the input of Theorem H up to a twist.
6. Hubs. Any number of hubs with zero hub block and sigma_2(A_{H,L}) > 0: ||p_Q|| <= 2 sqrt(pi)(sigma_1 sigma_2)^{-1/2}
   whatever else (structure/). Private leaves, any hub block: ||p_Q|| <= C_k/sigma_k(A_HJ), C_2 = sqrt(2 pi)
   (hub_pairs/). Two hubs with ANY hub block B and a remainder carrying a square lambda V^2 transverse to the hub
   partners (plus every term containing a hub partner, any diagonal, any linear term): ||p_Q|| <= 11.5 (s_1 s_2)^{-2/5}
   |lambda|^{-1/5} for all laws (single_hub_core/, Theorem 6.1: Plancherel in the two-dimensional hub partner gives
   |eta|^{-1} whatever B is, and the Fresnel factor of the slice makes the frequency integral converge). Two hubs need of
   the remainder only some power of |I| on intervals for its frozen slices, mu(I) <= K |I|^b with any b > 0
   (Theorem 6.4), and with a crossing block of the remainder across a split of the light coordinates they need nothing
   else, twists included (Theorem 6.5, 5.35 (s_1' s_2' F)^{-1/3}). THREE hubs need nothing of the remainder: for any hub block B and any function R of the light
   coordinates, X_H^T B X_H + 2 <X_H, L + beta> + R(X') with L in R^3 has |phi_Q(eta)| <= ||rho_L||^{1/2} (pi/|eta|)^{3/2}
   and ||p_Q|| <= 3 sqrt 2 (s_1 s_2 s_3)^{-1/3} (Theorem 6.3, Plancherel in the three-dimensional hub partner). So for ANY
   symmetric A and any three coordinates H, ||p_Q|| <= 3 sqrt 2 (s_1 s_2 s_3)^{-1/3} with s_j the singular values of the
   off-diagonal block A_{H, H^c}, without any eigenvalue hypothesis.
   One hub diagonal and no hub-hub coupling: bounded for every remainder (hub_pairs/). A general
   small-ball bound P(|zeta - s| <= rho) <= 4 (rho/||S||)^{1/4} for any quadratic with matrix S (hub_pairs/).
   A loss-free decoupling at hubs when the cross block between the two halves has low rank: each hub counts with
   its full |t|^{-1}, whatever quadratic forms sit inside the halves (hub_decoupling/, Theorem 5.1). Theorem H with
   a remainder that has no coupling between two frame-carrying blocks (twist_obstruction/, Corollary 3.2).
   A level-two hub reduction to a discriminant form of matrix -4a(A/a) (architecture/, lower_levels/).
7. Rank three (rank_three_geometry/). Definite rank-three forms have density <= 82 for every linear term, <= 12 when
   the linear part lies in the range; equivalently the spherical means of the density of an orthonormal 3D projection
   of a product measure satisfy M_{y0}(r) <= 6/(pi r) uniformly in the centre. Every rank-two form whose nonzero
   eigenvalues have modulus >= 1 has alpha_2 <= 87.3 with any linear term (a discriminant identity reduces the
   conditional small ball to one unit projection). An indefinite rank-three form with any c-pivot has bounded density
   on both sides of its level sets. So rank three is open only for no-pivot matrices with a hub (a row of leverage
   > 1/2), and that core reduces to the twist estimate (TW) of that report, which holds numerically on the laws tested.
8. A hub against a compressed rank-one term (multiscale_fourier/). For Q = 2 X_h (L + beta) + lambda (V + gamma)^2
   + (the part of the twist inside span(w, v)) + any linear terms, the density is bounded by an absolute constant.
   After completing the square the hub carries a quadratic phase; a one-dimensional Strichartz-type bound,
   int int |int f(x) e^{isx^2 + i tau x} dx|^6 ds dtau <= 4 pi^3/sqrt 3 for every density f <= 1, controls
   frequencies above 1/|sigma|, and a three-event comparison with two Theorem-H forms controls the scales below.
   No bound |phi(t)| <= C |t|^{-3/2} holds on this family, so the proof has to average over t.
9. Interval laws (extremal_laws/). A bounded density for unit-interval laws transfers, with the same constant, to
   every law of the form U[a, a + r] * nu (r >= 1) and mixtures of these; only uniform laws on non-interval sets
   are not reached. A three-dimensional coarea inequality holds for densities with convex superlevel sets
   (p_{q(Z)} <= 71.1 |det M_0|^{-1/3} K^{2/3}); it is false without convexity. Consequently, for X uniform on any
   unit cube and A of rank 3 + k, ||p_Q|| <= 142.2 * 2.61^{k'} for all n, all signatures and all linear terms;
   rank three is settled for interval laws (<= 372). Rearrangement at a fixed level s is false (an exact
   example), but no non-interval configuration beat intervals at the level of the supremum over s. Writing each law
   by the layer-cake formula as a mixture of uniform laws on intervals and averaging the Gram determinant over the
   widths (Cauchy-Binet and convexity of x^{-1/3}), rank three is settled for laws of total variation at most T
   (<= 372 (T/2)^2, Corollary 4.4), and so for every unimodal law with density at most 1 with the constant 372 of
   interval laws; this includes laws with a sharp peak, which the U[a, a + r] * nu class does not.
10. Audit of the earlier record (audit/). Every result labelled proved there was re-derived; none is false.
   Theorem C (the ruled one-sheet bound) needs the linear term in the range of A. Several constants are corrected.

11. Exact rank three and bounded rank (low_rank_plus_diagonal/). For an exact rank-two form whose nonzero
   eigenvalues have modulus >= 1, alpha_2 <= 88 with any linear terms and any hub diagonal: conditioning on one
   coordinate leaves a discriminant that is a rank-one form with eigenvalue -det(M) l_j. So the pivot tree for exact
   rank three has depth one, and any c-pivot gives density <= 176 c^{-1/2}. Without a pivot, exact rank three is
   bounded when all leverages are at most 1/2 (<= 12), for a leak-free hub with the linear term in the range (<= 278),
   and for a leaking hub with a spread light frame (<= 41 + 27 log_+(1/(6 eps)), eps the leak). A definite form of
   exact rank r whose nonzero eigenvalues are >= 1 has density <= 304 for every r and every linear term.
12. One hub with a small nonzero diagonal (hub_with_diagonal/). In the plane of (L + beta, R) the level set {Q = s}
   is the family of lines tangent to the parabola r = s + t^2/a (a pencil at a = 0). If the remainder has a
   square-root profile around a random centre C along L (hypothesis SQ), the whole effect of a is one negative quarter
   moment, E|(L + beta)^2 - a(C - s)|^{-1/4}, and the density is bounded uniformly in a for a genuine hub and at cost
   |a|^{1/2} log(1/|a|) where the hub block is nearly rank one (Theorems 3.3-3.4). Unconditionally, a hub whose
   transverse square lives on its own coordinates, with any dense twist on the hub's leaves, has density
   <= 118 |lambda|^{-1/2} |v|^{-1} (Theorem 5.1). No hypothesis on the marginal law of the remainder can suffice, even
   at a = 0, and the logarithm is attained when the matrix has only two large eigenvalues. The Fourier route does not
   see the diagonal: every zero-diagonal bound proved through the first step of Theorem H holds for every hub diagonal.
13. Freezing the hub projection (real_variable_hub/). Condition on the leaves and keep L = <w, X'> as a real variable.
   Once L is frozen, the terms that Theorem H would have to linearise along the hub direction (kappa L^2, L V,
   L <r, X'>) are constants, shifts of the square's centre or linear terms, so none of them enters the frequency
   integral, which is where the bumpy laws of twist_obstruction/ act. For a hub law supported in an interval of
   length D and a separable remainder, ||p_Q|| <= 1/2 + sigma^{-1}(1.54 + 21.9 D^{1/2} |lambda|^{-1/2}); the
   degenerate hub 4 X_h L + 2L^2 + 2V^2 + sum d_i X_i^2 + <b, X>, which Theorem H and Proposition 5.4 both miss, has
   density <= 8.99 for an interval hub law. A hub law covered by M unit intervals costs C(1 + log M). A dense twist
   reduces to one estimate, TL_perp, for twists that annihilate the span of the hub row and the transverse square.
14. Counterexample search and two sharper hub bounds (counterexample_search/). Nothing grows with n, eps sqrt(n), the
   hub diagonal, the hub block, row overlap, entry scales, comb spacing or bump number. For the pure star + rank one,
   |mu_3| sup_s p_Q(s) = 3.606 +- 0.051 against its Gaussian limit 3.6207 (exact quadrature); the largest value in the
   hub families, 4.079, is reached by spreading the hub row until the form becomes the Gaussian (1, 1, -1) form, whose
   value is 3 sqrt 2. For a hub with zero diagonal and a transverse square (w, v orthonormal), Q = 2(L + beta) X_h + lambda (V - v_c(L))^2
   + F_c(L) with any functions v_c, F_c (so every twist in span(w, v)) and any laws,
   ||p_Q|| <= 2 sqrt 2 + sqrt 2 log(1/3 + 4 sqrt 2/|lambda|), which is 5.36 at |lambda| = 1 (Proposition S). Two hubs
   with zero hub block: ||p_Q|| <= 2 sqrt 2 (s_1 s_2)^{-1/2} with s_1, s_2 the singular values of A_{H,H^c}
   (Proposition S2). The bumpy laws that defeat Fourier L^1 bounds lower the density.

15. The degenerate hub, for every hub law (degenerate_hub/). For
   Q = a X_h^2 + 2 X_h (L + beta) + sigma L^2 + lambda U^2 + sum_i phi_i(X_i) with (L, U) a spread frame and each
   phi_i an arbitrary quadratic in one coordinate, ||p_Q|| <= 2.23 (1.53 B_0)^{6/7} with
   B_0 = 16.8 |lambda|^{-1/2} |sigma|^{-1/6} |1 - a sigma|^{-1/6} (det G)^{-5/12} |u|^{-1/6}, for every hub law and every
   linear term; with a = 0 the bound is uniform in sigma. Completing the square in L turns the hub into a chirp, and
   the one-dimensional Strichartz bound of multiscale_fourier/ controls it; the separable part rides inside the
   coordinate transforms, which Lemma 1 bounds whatever their phases. So 4 X_h L + 2L^2 + 2V^2 + X'^T D X' + <b, X>
   has density <= 18 for every diagonal D (case M-DEG of the proof tree), and exact rank three (O2) is closed except
   for the corner p' -> 0 with a nonzero hub diagonal.

16. One hub with every term that contains L (single_hub_core/). For Q = 2 X_h (L + beta) + lambda V^2 + 2 L <q, X'>
   + sum_i phi_i(X_i), with (w, v) orthonormal of leverages w_i^2 + v_i^2 <= 1/2, any q and any one-coordinate
   quadratics phi_i, and X_h supported in an interval of length D, ||p_Q|| <= 22 (D/|lambda|)^{1/3}. Freezing L turns
   every term containing L (sigma L^2, L V, and every cross term L <r, X'> with an outside direction) into a linear
   term, which the Brascamp-Lieb bound does not see; no smallness is needed. For an arbitrary hub law: Q = 2 X_h (L +
   beta) + lambda V^2 + 2 V g(L, Z) + F(L, Z), with Z a k-dimensional projection orthogonal to (w, v) and g, F arbitrary,
   has density <= 1/2 + 8 M_k |lambda|^{-1/2}, where M_k = sup_l int sup_u rho_{L,V,Z}(l, u, z) dz (Theorem 3.2, no leverage
   condition). When the light coordinates are supported in intervals of length K, an exponential tilt and Hoeffding's
   lemma give M_1 <= 20.5 K, so (0.1) without diagonal (every cross term) is <= 1/2 + 51.2 (K/|lambda|)^{1/2} for every
   hub law (Proposition 3.3). Splitting the hub law off first cannot work: the frozen-hub forms 2 x L + lambda V^2 +
   2 eps L <q^, X'> have density of order (|lambda| eps)^{-1/2} for a translated Gaussian law (Example 2.2). The hub
   bathtub needs only a profile K |S|^theta with some theta > 0, not the square root. With a hub diagonal a as well, the
   random-centre argument of hub_with_diagonal/ goes through with the same maximal weight (Theorem 3.4):
   ||p_Q|| <= 1 + 9.05 |lambda|^{-1/2} |1 - a sigma_c|^{-1/4} N_k. So exact rank three is bounded for every law of the hub
   coordinate when all other coordinates are supported in intervals of length K, including the leaking hub (O1), the
   corner p' -> 0 of (O2) and (O3), with constants depending on K. For light laws of the form U[0, 1] * nu (any nu) the
   constants are universal (Corollary 3.5): the hub law is arbitrary there, unlike in every earlier interval-law result.
   The same holds, with constants polynomial in the total variation, when the light laws have bounded total variation
   (unimodal laws among them) or are such laws convolved with anything (Corollary 3.6): given the intervals of the
   layer-cake representation the light coordinates are uniform on intervals, the maximal quantities are bounded by
   conditional variances of a log-concave vector, and averaging over the widths costs a constant.
   Every cross term 2L<q, X'> whose part orthogonal to (w, v) has size eps > 0 is bounded for every hub law, with any
   hub diagonal and any light diagonal, by 9.6 (eps |lambda|)^{-1/3} when the light frame (w, v, q^) has leverages
   <= 1/2 (Proposition 2.3: integrate the hub in Fourier and keep P = <q^, X'> as a variable of the Parseval step; the
   p-integral pins l, so the parts of q along w and v cost nothing), and by 17.0 eps^{-1/6} |lambda|^{-1/3} (Proposition 3.12:
   Plancherel in the hub partner at fixed frequency gives |phi_Q(eta)| <= 4.72 |lambda|^{-1/4} |eta|^{-3/4} for every form
   (0.1), every hub diagonal and every hub law). A hub density of bounded variation V makes all of (0.1) without hub
   diagonal bounded by 14.9 V^{2/3} when |lambda| >= 1, every cross term included (Proposition 3.13; window hub laws have
   V <= 2), so the open case needs a rough hub law as well as rough light laws. If part of the hub partner, of norm omega,
   lives on light coordinates that carry nothing but the partner, (0.1) without hub diagonal is bounded by
   1/2 + 10.3/omega for every hub law, every cross term and all light laws (Proposition 3.14: conditioning on the other
   coordinates leaves t with a bounded density, and the hub then enters through dilates of one set, which only needs
   the interval profile of the remainder). With eps = 0 this is degenerate_hub/. In the
   tilted-hub picture the hub coordinate has leverage 1/(1 + eps^2), so only the nearly aligned hub is open; for
   exact rank three this improves (c1) of low_rank_plus_diagonal/ from eps^{-2/3} to eps^{-1/3}. When P = <q^, X'>
   lives on a set T of coordinates whose complement still carries the (w, v) frame (Gram G_I invertible, relative
   leverages <= 1/2), 7.6 (|lambda| det G_I)^{-1/3} holds for cross terms of every size, any hub law and any diagonal
   (Proposition 2.4: conditioning on P turns e^{i kappa L P} into a shift in the integrated frequency, so the twisted
   frame integral is at most the average conditional one); what is left of the cross terms is spread leakage of small
   size. For the
   curved section, each dyadic shell of |V - V_0| is bounded in L^2 by 8 log 2/|lambda| for all laws and frames
   (Lemma 3.6, a collision count with the four-dimensional projection bound), which improves Proposition 3.3 to
   1/2 + C |lambda|^{-1/2} (1 + log(1 + K^2 |lambda|))^{1/2} (Proposition 3.7). In Fourier the slice is square-integrable
   with a logarithm of |lambda|/gamma in place of the number of shells, gamma the size of its linear term, for all laws
   (Lemma 3.8: the Fresnel factor in V and the three-dimensional Brascamp-Lieb bound over the frequency of the linear
   term); so (0.1) without diagonal, with the cross-term and linear directions spread, is at most
   17.6 + sqrt 2 log(101.2 + 16 log_+(|lambda|/(2 eps))) for |lambda| >= 1, for every hub law and all light laws
   (Proposition 3.9), against (eps |lambda|)^{-1/3} in Proposition 2.3. For exact rank three (O1) with m = 0 this replaces
   41 + 27 log_+(1/(6 eps)). Pairing the hub window with the slice in Fourier (the hub through its L^2 norm, the slice
   through Lemma 1.1 up to frequency 1/delta) gives, for EVERY Q of the form (0.1) - any q, any diagonal, any linear
   term, every hub law, all light laws - P(|Q - s| <= delta) <= 2 delta (1/2 + 2 sqrt 2 + sqrt 2 log_+(2 B_delta^2)) with
   B_delta^2 of order log(|lambda|/delta)/|lambda| (Theorem 3.10); with Proposition 2.3 below the scale eps this bounds the
   density with any light diagonal by 58.2 + 7.7 log_+(2 B_eps^2) (Corollary 3.11), a double logarithm in 1/eps.
   Uniformly in eps instead of in the dimension: conditioning on all light coordinates but one with w_i != 0 leaves t
   with density at most 1/|w_i| and the hub value of the form alpha/(2t) + c_0 - sigma t/2, whatever v_i and q_i are
   (Proposition 3.16), and confining that density to |t| < |w_i|^3/(1 + |lambda|) gives, without diagonal,
   ||p_Q|| <= C (1 + |q|_inf + log(1 + |lambda|)) + (3/sqrt 2) log m on m light coordinates, for every hub law and all
   light laws (Proposition 3.17). With a hub diagonal the same conditioning gives 1 + pi |w_i|^{-1} |kappa|^{-1/2} when
   kappa = 1 - a C < 0, and in the frame of w the dimension-free version becomes a (CS)-type integral over half a quadric
   whose Jacobian along w is 1 (single_hub_core/, Section 3). Conditioning on a group of light coordinates with parallel
   rows (w_i, v_i, q_i, b_i) works like conditioning on one, so log m improves to log K, K the number of row directions
   (Proposition 3.19). The hub law enters through a logarithm too: at most
   1/2 + 3 sqrt 2 + sqrt 2 log(1 + 2 pi^4 V/|lambda|) for a hub density of total variation V, every cross term and all light
   laws, against V^{2/3} before (Proposition 3.18); interval profiles of the slices cannot do better, while slices that did
   not move with t would give a bound for every hub law. For a hub that sees P (Section 5): at most 1/2 + 2 rho* (1 + log_+(c M*/rho*)), rho* the
   density of L near -beta (Proposition 5.5), hence log K for partner coordinates of support K, 13.9 for window laws
   there (|lambda| >= 1), and a bound falling with N for the comb laws of the numerics; and 10.8 when w lives on two
   window-law coordinates, the partner pointing anywhere there (Proposition 5.6).
17. The two-sheet side (two_sheet_side/). For homogeneous forms the conjecture is open already at rank exactly three,
   and only on the two-sheet side of a heavy row with a small diagonal, in its simplest form the leaking hub
   Q = 2 L (X_h + eps P) + lambda V^2 with s lambda < 0: the one-sheet
   side is Theorem C of the first record, diffuse frames and pivots are bounded on both sides, and eps = 0 is
   degenerate_hub/. On the two-sheet side the dilation centre of Propositions 3.14 and 3.16 satisfies |alpha| >= |s|,
   so those bounds need no small-ball estimate there; the factor 1/|w_i| remains. Conditioning on L and integrating the
   hub in Fourier makes the cross term free: for (0.1) with a = 0, any cross term, any light diagonal and linear terms,
   ||p_Q|| <= 1/2 + 2 sqrt 2 (1 + log_+(2 H(f_0)/(pi |lambda|)^{1/2})), H(f_0) = int |f^_0| |omega|^{-1/2}, which is finite for
   every hub law with positive Sobolev smoothness and of order J^{1/2} for laws without structure below 2^{-J}; with the
   three-dimensional Brascamp-Lieb bound the same computation gives min(H(f_0), 12.9 + 2 (pi log(1/eps))^{1/2}) in place
   of H (two_sheet_side/, Proposition 2). If the leak has range R, smoothing the hub law at the scale eps R absorbs it in
   physical space and the density is at most C + sqrt 2 log log R, uniformly in eps and the hub law (Proposition 3 there);
   for light laws supported in intervals of length K, exponential tilting of the tails of P, repeated with the density
   cap doubling at each step, gives C + sqrt 2 log log K in every dimension, against (log K)^{1/2} in Proposition 3.7
   (Proposition 4 there); for all laws, the average of the density over the shift beta of the partner, against any
   density phi, is at most 1/2 + ||phi||_inf (2 + log(1 + 2 pi^4/|lambda|)), because averaging adds a variable that carries
   only the partner (from Proposition 3.14 of single_hub_core/), and the average over eps in [eps_0, 2 eps_0] is at most
   128 sqrt 2 |lambda|^{-1/2}, because it smooths the hub law along the leak below its maximal function (Proposition 5
   there);
   with a leak-dependent smoothing scale the Hardy-Littlewood maximal function bounds all the smoothed parts, so what is
   left is the hub transform on 1/(eps |P|) <= |omega| <= 1/eps for large |P|. Numerically the two-sheet side of the leaking hub is below the one-sheet side
   and settles as eps -> 0 (two_sheet_side/num/).
18. The curved marginal with a bounded square (curved_marginal/). If |V - v_0| <= R almost surely, the density of
   U + c V^2 is at most C_1 + C_2 R^{1/2} for every real c and every frame with u_i^2 + v_i^2 <= 1/2: below the frequency
   1/(|c| R^2) the chirp is a smooth multiplier, which the one-dimensional Brascamp-Lieb bound absorbs, and above it the
   Fresnel factor and the bandwidth of the localised chirp meet at a loss R^{1/2}. The iterated tilt of two_sheet_side/
   turns this into C (1 + K^{1/2}) in every dimension when the coordinates that carry V are supported in intervals of
   length K, so for (P2) only laws spread over long ranges with gaps remain open. For laws of total variation T,
   unimodal laws among them, (P2) holds with C (1 + T)^2 and without the leverage condition (Proposition 3 there),
   by the same average over widths. In every computation so far the
   parabola collects less than the best line for the same laws, including searches that maximised the parabola and
   lattice frames where it collects two to three times the density of U; this suggests the sharp form (P2') of
   OPEN_CORE.md, the density of U + cV^2 at most the largest density of a linear form, hence at most sqrt 2.

## Proved negative results

- The Fourier twist lemma is false (twist_obstruction/, Theorem 1). For any kappa != 0 and spread p there are
  product laws (many narrow bumps at spread positions) with int |E exp(i<Pu,X> + i kappa <p,X>^2)| du as large as
  desired, while the untwisted integral stays bounded. No smallness condition on the twist helps; the L^2 version
  always holds (Plancherel).
- Two hubs with det(A_HH) < 0 and the Schur-matched remainder L^T A_HH^{-1} L have P(|Q| <= eps) >= c eps log(1/eps)
  (hub_pairs/, Theorem 1). The matrix has rank two and no pivot, so this is consistent with the conjecture; it shows
  that a bound for a hub pair must use the third eigenvalue.
- Rudelson-Vershynin's Lemma 3.1 bounds the decreasing rearrangement of |psi|, not |psi| pointwise; the pointwise
  form fails for laws on fine lattices of tiny intervals (audit/).
- A density on R^3 bounded by 2 sqrt 2 whose integrals over all lines are bounded by an absolute constant (numerically
  below 1.04, under the bound 2 of every two-dimensional marginal of a product law) can give Z_1^2 + Z_2^2 - Z_3^2 a
  density as large as desired on the two-sheet side (two_sheet_side/, Proposition 1: rings of radii 4^k and thickness
  c 4^{-3k} on the hyperboloid). The argument of Theorem C uses only those two facts, so it cannot reach that side.

## What remains

OPEN_CORE.md states the open case on one page, with its simplest form and what an argument cannot be.

By the above, the conjecture is equivalent to a bounded density for no-pivot matrices with three eigenvalues of
modulus >= 1 and a hub-like coordinate. Three well-conditioned hubs are bounded whatever else A is (single_hub_core/,
Theorem 6.3), and two hubs are bounded whatever the remainder is once the remainder crosses a split of the light
coordinates (Theorem 6.5); a pair whose third large eigenvalue lies along the partners reduces to one hub. So the core is
ONE hub: Q = a X_h^2 + 2 X_h (L + beta) + R with R a transverse square lambda V^2 plus terms that are small in Frobenius
norm (cross terms 2 L <q, X'>, a twist, the diagonal). There every method in this record stops at |phi_Q(eta)| of order
|eta|^{-1}: Plancherel in the partner gives the hub only |eta|^{-1/2} because the Fourier transform of a rough hub law is
only square-integrable (its two eigenvalues +-|w| count once), the square gives the other |eta|^{-1/2}, and the
L^1 route (Theorem H), which gives the hub its full |eta|^{-1}, needs the frame integral in the partner frequency, which
the cross terms and twists can inflate. What is proved there: bounded for eps = 0 with any diagonal, for localised cross
terms, for q in span(w, v), for window laws and for bounded supports, for hub laws of bounded variation
(Proposition 3.13), and whenever part of the partner or part of the transverse direction lives on light coordinates
that carry nothing else (Propositions 3.14 and 3.15); delta log log(1/delta) small balls and a log log(1/eps) density
for a = 0 without twist (Theorem 3.10, Corollary 3.11); delta log(1/delta) and log(1/eps) with a hub diagonal or a
twist (Proposition 6.6, Corollary 6.7). So the open single hub has a rough hub law, rough light laws, a small cross
term, and no light coordinate that carries w or v without also carrying the partner of the cross term. Rough light
laws are meant literally: without a light diagonal, (0.1) is bounded for every hub law when the light laws have
bounded total variation, or are such laws convolved with anything (single_hub_core/, Corollary 3.6), so a large
density needs light laws with no such factor, combs with many teeth for instance; a light diagonal or a twist is not
reached by that corollary. Its hub term
is a bilinear form of rank one between the independent variables X_h and X'; the density bound for bilinear forms in
independent vectors (Banks, Garza-Vargas, Kulkarni and Srivastava, arXiv:2005.08930, Corollary 2.4) needs rank two,
which is the two-hub case. Without the slice, the curved-section question behind (CS) and (VD) is (P2) of
single_hub_core/, Section 5: the density of U + c V^2 for orthonormal spread U, V is bounded uniformly in the frame for
|c| bounded below and uniformly in c for each fixed frame (Proposition 5.1 there), and nothing here bounds it for small
|c| on frames spread over many coordinates. The missing
statements, each stated precisely in the folder named:

- TL_perp (real_variable_hub/, Section 4; single_hub_core/, Section 4): the frequency-integral bound for a twist that
  annihilates the span of the hub row and the transverse square. With it, star + rank one + eps W is bounded for every
  hub law when the twist has no cross terms with L. Cross terms with L are already covered for interval hub laws
  (item 16).
- CSP_gen (real_variable_hub/, Section 5): a bound for the conditional law of the remainder given L. Any concave
  profile phi with int_0 phi(x) dx/x finite suffices (single_hub_core/, Lemma 3.1). For small cross terms (eps -> 0,
  the only case Proposition 2.3 leaves) with an arbitrary hub law, the statement needed is the collision bound (VD) of
  single_hub_core/, Section 3: independent copies, with the difference Y - Y' normalised by its gradient
  |(lambda (|V - V_0| + |V' - V_0|), beta)|, have a bounded joint density with (L, L') at (l, l, 0). It is weaker than
  the curved slicing statement (CS) there, and it removes the logarithm of Lemma 3.6, which counts dyadic shells. It
  holds for bounded support up to that logarithm and for window laws; the maximal bound M fails for comb laws with a
  rational fibre, where (CS) and the shell norms behave well numerically. The loss is now a double logarithm of 1/eps
  for all light laws, with or without light diagonal (single_hub_core/, Proposition 3.9 and Corollary 3.11, the latter
  from a small-ball bound delta log log(1/delta) that holds for every cross term); what remains is that double
  logarithm, from slices whose linear term is of size eps, and a hub diagonal together with a small spread cross term (now
  at most 17.0 eps^{-1/6} |lambda|^{-1/3}, single_hub_core/, Proposition 3.12, where Proposition 2.3 had eps^{-1/3}). Through Theorem H the same case would
  follow from a frame bound for the twist e^{i kappa L P}, which lowers the frame integral on the four-coordinate Walsh
  frame, raises it (by at most 3.5 at N = 4, below the untwisted constant) on a sheared rational frame, and on a frame
  spread in three dimensions raises it by a factor that grows with the spread of the laws while the density of Q does
  not move (single_hub_core/num/, Section 13). Pairing the hub law by Hoelder instead gives the same conclusion from an
  L^p form of that bound, any p < 2 (single_hub_core/, Proposition 5.3); on one rotation of the spread frame the p = 3/2
  norm stays bounded where the p = 1 norm grows, on another every norm with p <= 2 grows for comb laws at the integers,
  so the loss is in taking moduli of the twisted transform, not in the exponent of the hub pairing; for fine combs of
  bounded range all of them stay flat, and the transform of Q itself is integrable uniformly in eps. Without hub
  diagonal the cross term can also be moved into the hub: X_h + eps P is a hub whose law depends on X' only through P,
  so the case follows for every eps at once from the eps = 0 bound for such hubs, (SP) in single_hub_core/, Section 5.
  Numerically, net of the estimator bias, that supremum exceeds the ordinary eps = 0 bathtub by at most 2 per cent for
  laws of bounded range, and for comb laws at the integers by a factor that grows slowly with N without levelling off
  (1.54 at N = 20), while the supremum itself falls as the laws spread. The argument of Proposition S carries over to such hubs with a maximal functional of the pair
  (L, P), local in L, in place of the bound for the density of (L, V) (Proposition 5.4). That functional stays between
  0.1 and 1 on the spread frame for every comb family computed, but it is not bounded uniformly in the light laws: it
  grows like N^{1/2} in its windowed form and like log N in its sharp form in configurations that Propositions 3.14 and
  3.15 cover. Where P determines V the hub knows V, and what keeps the density bounded is that lambda (V - v_c)^2 rarely
  falls near s; a proof of (SP) has to use that as well as the curvature. Integrated over P first, the first bound of
  Proposition 5.4 is at most 1/2 + 2 rho* (1 + log_+(c M*/rho*)), rho* the density of L near -beta and M* the integral
  over P of the largest density of (L, V, P) in V, so (SP) can fail only where M* is exponentially large in 1/rho*.
  Without light diagonal on the frame this gives (SP) up to log K when the light coordinates that carry both q^ and the
  frame are supported in intervals of length K, and with a universal constant (13.9 for |lambda| >= 1) when they have
  window laws, all other light laws arbitrary (Proposition 5.5: the partner coordinates off the frame are conditioned
  away and the tilt of Proposition 3.3 bounds M*). For the combs at the integers of the numerics N rho* stays near 1.35,
  and the bound falls from 5.9 at N = 4 to 1.1 at N = 64. When w lives on a block of window laws on which v vanishes,
  a hub that sees P is bounded (10.8 for a block of two coordinates, |lambda| >= 1) even though the partner may have
  any part on that block orthogonal to w (Proposition 5.6, the dilation argument of Proposition 3.14 conditioned on the
  rest of the block). What remains of (SP) is a density of order one for L near
  -beta together with structure below unit scale on the coordinates that carry both; in a random search over 40 comb
  laws a hub that sees P never exceeded 0.70, and over 113 random frames on four to six coordinates never 0.52. For the
  single hub itself (not a hub that sees P), conditioning on all light coordinates but one leaves t with density at
  most 1/|w_i| and x* of the form alpha/(2t) + c_0 - sigma t/2, so without diagonal the density is at most
  1/2 + |w_i|^{-1}(27.9 + 0.5 log(1 + 2 |sigma|)) for |lambda| >= 1, for every cross term and all laws
  (single_hub_core/, Proposition 3.16). Confining that factor to |t| < |w_i|^3/(1 + |lambda|), where the dilation makes
  it harmless, and using only rho_L <= sqrt 2 above it gives C(1 + |q|_inf + log(1 + |lambda|)) + (3/sqrt 2) log m on m
  light coordinates, for every hub law and all laws, uniformly as eps -> 0 (Proposition 3.17). The earlier bounds carry
  log log(1/eps) uniformly in m; what is open is uniformity in both at once, the spread regime.
- SQ for a rank-one square with a dense twist on its own coordinates (hub_with_diagonal/, Section 9): it settles
  every small hub diagonal.
- (LH) (low_rank_plus_diagonal/, Section 3.3): the leaking-hub estimate that finishes exact rank three. It is the
  same slice estimate as Omega in hub_decoupling/ and (TW) in rank_three_geometry/, and the maximal quantity N_k of
  single_hub_core/, Theorem 3.4 is a form of it. It holds when the light coordinates have bounded support. For light
  laws of unbounded support the leaking hub with zero hub diagonal (m = 0) is now bounded up to a double logarithm of
  1/eps (single_hub_core/, Proposition 3.9 and Corollary 3.11); what is missing is that double logarithm, and the
  leaking hub with a hub diagonal, with a universal constant (with a hub diagonal the loss is now eps^{-1/6},
  Proposition 3.12).
- Hub pairs are no longer open in the form stated before: two hubs with ANY hub block and ANY quadratic remainder
  (every twist included) are bounded by 5.35 (s_1' s_2' F)^{-1/3} as soon as some split of the light coordinates into
  I and J keeps the partners of rank two on J and the block of the remainder that crosses the split, projected off
  the partners, has Frobenius norm F with no row carrying more than half of F^2 (single_hub_core/, Theorem 6.5:
  Plancherel in the partner, then a Cauchy-Schwarz decoupling of the averaged slice transforms, in which every twist
  inside a half cancels or becomes a phase, then Hoelder with weights proportional to the squared row norms). A third
  large eigenvalue not along the partners gives such a split, a spread one for a random split; one along the partners
  reduces the pair to one hub (end of Section 6). What is left for pairs is the bookkeeping that turns this into a
  statement about no-pivot matrices, with constants, including the interpolation between the two cases when the
  third eigenvector is nearly along the partners. Many heavy rows and peeling are settled whenever three hub
  directions are well conditioned (Theorem 6.3: any three coordinates whose off-diagonal block has s_1 s_2 s_3 bounded
  below give a bounded density, whatever else A is); open there: many heavy rows whose partners span only two
  directions (architecture/PROOF_TREE.md, M-MH), which Theorem 6.5 covers when their partner block has exact rank two
  (the Plancherel step then runs on the two-dimensional projection of the hub vector, whose density is at most 2).
- One hub with any remainder: |phi_Q(eta)| <= 2 pi (|w_J| F)^{-1/2} |eta|^{-1} and a small-ball bound
  C delta log(1/delta), for every twist, every hub diagonal and every hub law (single_hub_core/, Proposition 6.6); the
  single hub is where the decoupling stops at |eta|^{-1}, because its crossing block is of rank one (the transverse
  square) up to terms of the size of the cross term, which is the borderline for a density. When the crossing block
  has exact rank two (two transverse squares, twists inside either half allowed) one hub is bounded,
  6.73 (|w_J| sigma_1 sigma_2)^{-1/3} (Proposition 6.8): a single hub inside a matrix with four large eigenvalues is
  bounded, and three is exactly the case that is open. A hub spread over several coordinates, U = <c, X_H> with no
  coordinate carrying more than half of |c|^2, is bounded by 12 (|c|^2 |lambda|)^{-1/3} for every cross term and all laws
  (Proposition 6.9: its characteristic function is integrable, so it pairs with the slices like a hub law of bounded
  variation); this is the exact form of many heavy rows with one common partner direction.

The degenerate single hub is no longer on this list (item 15). The first, fourth and fifth items meet the same
obstruction: a twist coupling the hub row to directions outside the
frame, on which the bumpy-law mechanism of twist_obstruction/ could act. Numerically nothing grows in any
configuration tested.
