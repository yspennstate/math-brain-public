# The open core on one page

X_h, X_1, ..., X_m are independent with densities at most 1, X' = (X_1, ..., X_m), and w, v, b are orthonormal in
R^m with small leverages (w_i^2 + v_i^2 <= 1/2, or the three-dimensional form where b enters). L = <w, X'>,
V = <v, X'>, B = <b, X'>. The conjecture asks for an absolute bound on the density of X^T A X + b^T X + c when A has
three eigenvalues of modulus at least 1. The reductions of this record (README.md, "What remains") leave one hub:

  Q = a X_h^2 + 2 X_h (L + beta) + lambda V^2 + 2 L <q, X'> + sum_i phi_i(X_i),   |lambda| >= 1.

Three other items listed there (the twist bound TL_perp, the leaking hub of exact rank three, and many heavy rows
with two partner directions) meet the same obstruction; a small hub diagonal is SQ in hub_with_diagonal/. What
follows is the case a = 0.

## The smallest open instance

For homogeneous forms the conjecture is open already at rank exactly three, and only in one place (two_sheet_side/).
There the one-sheet side is bounded by pi sqrt 2 for every product law (Theorem C of the first record), and diffuse
frames and pivots are bounded on both sides. What is left is the two-sheet side of a heavy row with a small diagonal,
whose simplest form is the leaking hub

  Q = 2 X_h L + lambda V^2 + 2 eps L P = 2 L (X_h + eps P) + lambda V^2,   s lambda < 0,

with P = <p, X'> orthogonal to L and V: a matrix of rank three with eigenvalues lambda and +-(1 + eps^2)^{1/2}, bounded
for eps = 0 (degenerate_hub/) and up to log K or log log(1/eps) for eps > 0 (single_hub_core/). The inputs of
Theorem C, a bounded density and bounded integrals over every line for the three-dimensional marginal, cannot settle
it: with the constants of a product law for both, rings on a two-sheet hyperboloid make the density of Q as large as
desired (two_sheet_side/, Proposition 1). Once L is fixed the leak costs nothing in Fourier: the density is at most
C + 2 sqrt 2 log(1 + C H(f_0)) with H(f_0) = int |f^_0(omega)| |omega|^{-1/2} d omega, uniformly in eps and in the direction of
the cross term (two_sheet_side/, Proposition 2). So a hub law that makes the leaking hub large spreads its transform
over many dyadic bands: density M needs about exp(M/sqrt 2) of them, and log(1/eps) of the same order.
A leak of range R costs at most sqrt 2 log log R, uniformly in eps and the hub law (Proposition 3 there): smoothing the
hub law at the scale eps R absorbs the leak in physical space, and the transform is needed only above 1/(eps R). What is
left is the hub transform on 1/(eps |P|) <= |omega| <= 1/eps for large |P|, where the light transform in the direction of
the leak has not decayed: the tails of P, and light laws that are spread and rough at once.
For light laws supported in intervals of length K the tails of P tilt away, repeatedly, and the bound is
C + sqrt 2 log log K, uniformly in eps, the hub law and the dimension (Proposition 4 there). For all laws at once, the
average over the shift beta is bounded: int_I p(s) d beta <= |I|/2 + 7.28 over every interval I of beta when
|lambda| >= 1, since averaging adds a variable that carries only the partner, and the average over eps in
[eps_0, 2 eps_0] is at most 128 sqrt 2 |lambda|^{-1/2}, since it smooths the hub law along the leak below its maximal
function (Proposition 5 there). A density M can occur only on sets of measure O(1/M) in beta and in log eps.
The leaking hub is bounded for every hub law when the light laws have bounded total variation, unimodal laws among
them, or are such laws convolved with anything (single_hub_core/, Corollary 3.6), and by 372 when every law is
unimodal (extremal_laws/, Corollary 4.4): a large density needs light laws with no such factor, combs with many
teeth for instance.

## Related results

For Gaussian coordinates a robust form of the conjecture holds: if the quadratic part F is at Frobenius distance at
least eta^{1/2} ||F||_F from every form of rank at most two, then sup_x P(|f - x| <= eps) <= C_eta eps/sigma(f) (Kwan, Sah,
Sauermann and Sawhney, arXiv:2208.02874, Theorem 1.6). The proof there uses the rotation invariance of the Gaussian,
which product laws with densities at most one do not have. The statement (CS) below is a global nonlinear
Brascamp-Lieb inequality for sections of a product density by quadrics (single_hub_core/, after Corollary 3.5): at each
point of the section the linearised datum is a flat one with a bounded constant. Local nonlinear Brascamp-Lieb
inequalities hold near any point where the linearised datum is finite (Bennett, Bez, Buschenhenke, Cowling and Flock,
arXiv:1811.11052), and Duncan (arXiv:2101.07672) proves a heat-flow near-monotonicity at small scales together with a
qualitative stability of finiteness under bounded perturbations; the global results listed there all need rigid
structural assumptions, which quadric sections of product densities do not satisfy.

(P2) below is a continuous form of the parabola case of a geometric Littlewood-Offord problem. For Rademacher sums X
of arbitrary nonzero vectors in R^2, Pr(X in S) <= C_S n^{-1/2} when S is a strictly convex plane curve (Fox, Kwan and
Spink, Ann. Probab. 51 (2023), Theorem 1.7, arXiv:2106.04894), and Costello (Israel J. Math. 194 (2013), Lemma 13)
had n^{-1/2+o(1)} for parabolas, through a weighted Szemeredi-Trotter bound, on the way to the quadratic
Littlewood-Offord problem. The argument splits X into two independent halves and uses that two translates of a
parabola meet in at most one point. For densities and a thickened parabola the same Cauchy-Schwarz decoupling gives
at best a bound of order |c|^{-1/2}: translates that differ by d cross at an angle of order |c d_v|, so their
eta-neighbourhoods share an area of order eta^2/(|c| |d_v|), which is large exactly when c is small.

## Two sufficient statements

(CS) For every l, y, V_0, lambda != 0, beta and r > 0, the density at (l, y) of (L, lambda (V - V_0)^2 + beta B),
restricted to {|V - V_0| > r}, is at most C/(|lambda| r).

With the fold slab {|V - V_0| <= r}, which has mass at most 4r in every slice, and Lemma 3.1 of single_hub_core/, (CS)
bounds Q without light diagonal for every hub law, every cross term q and all light laws. The cross term costs nothing
here: at L = l it is the linear term 2l <q, X'>, which (CS) allows through beta B.

(SP) A bound for the form with no cross term and a hub whose law may depend on P = <p, X'>, p the unit direction of the
cross term outside span(w, v). Taking X_h + eps P as the hub turns every eps into this case.

## The simplest form

Drop the slice in L. With u, v orthonormal, u_i^2 + v_i^2 <= 1/2, U = <u, X'>:

  (P2) the density of U + c V^2 is at most an absolute constant, for every real c and all laws.

It equals the integral of the density of (U, V) along the parabola u = s - c v^2, in dv. At c = 0 it is the marginal
bound sqrt 2. Known: 8 |c|^{-1/2} for all frames and laws (Fourier); 4 (|v_i| + |v_j|)/|u_i v_j - u_j v_i| for every pair
of coordinates (conditioning), so at most 4 sqrt 2 (m(m - 1)/2)^{1/2} on m coordinates; and 8 on the four-coordinate
frame of Example 5.2 of single_hub_core/, where two block sums play the part of two coordinates; of order K when the rows
(u_i, v_i) take only K directions (grouping, after Proposition 3.19); C (1 + R^{1/2}) for every c and every frame when
|V - v_0| <= R, and so C (1 + K^{1/2}) in every dimension when the coordinates that carry V are supported in intervals of
length K, and C (1 + T)^2 in every frame for laws of total variation T (curved_marginal/). Open: c small on frames whose rows point in many directions, where the parabola bends
only far out in the laws, for laws spread over long ranges with gaps. (P2) is (CS) without the slice, the
curved-section question in its simplest form; it has no fold, since |u + 2cVv| >= 1.

Every computation so far fits a stronger form with a sharp constant (curved_marginal/, Section 3):

  (P2') the density of U + cV^2 at s is at most the largest density of a linear form cos t U + sin t V,

for every frame, all laws, every c and every s. With the flat bound, (P2') gives (P2) with the constant sqrt 2. On the
lattice frames where the parabola collects two to three times the density of U, the lines along the lattice rows
collect more; in adversarial searches over comb laws on random frames with 6 to 24 coordinates, the best parabola never
reached the best line for the same laws. (P2') is false for densities on the plane that are not marginals of product
laws, so a proof has to use the product structure.

## Comb laws reduce (P2) to a discrete question

Let each X_i be uniform on N teeth of width 1/N at arbitrary positions spaced at least 1/N apart. Then X_i = A_i + E_i/N
with A_i uniform on the left endpoints, E_i uniform on [0, 1], all independent, and (U, V) = A + C with the atom sum
A = sum_i A_i (u_i, v_i) and C = N^{-1} sum_i E_i (u_i, v_i), a log-concave vector at scale 1/N independent of A.
Conditioning on A, the density of U + c V^2 at s is the average over the atoms of the curve integral of the density
of C along the parabola translated by the atom. That curve integral is at most of order N when the atom lies within
O(1/N) of the parabola, and it decays exponentially in N times the distance otherwise. So for comb laws (P2) follows from

  P(dist(A, Gamma) <= eta) <= C eta   for every eta >= 1/N and every parabola Gamma = {u + c (v - v_0)^2 = s}.

For lines (c = 0) this follows from the marginal bound. When the teeth sit at the integers and the frame is rational,
the atoms lie on a lattice, with multiplicities, and a count with Jarnik's bound suggests the inequality with room to
spare: a strictly convex arc of length L carries O(L^{2/3}) lattice points, in lattice units, where a line can carry L.
What is missing is the statement for atom sets with no lattice structure, a small-ball estimate near curves for sums of
independent vectors, each supported on a line. One route is of inverse Littlewood-Offord type: concentration of the
sum near a parabola should force lattice structure in the atoms, which the curvature then rules out.

## What an argument cannot be

- Bounds that use only the interval profile of each slice (Lemma 1.1) and rho_L <= sqrt 2 give at best a logarithm
  of the hub law's complexity: Proposition 3.18 attains it, and a family of slices with n bumps along n lines through
  one point shows it is sharp for that information. If the slices did not move with t, the density would be bounded
  for every hub law.
- A supremum over the position of the curve taken before integrating (the maximal functionals M and M_2 of
  single_hub_core/, and that of its Proposition 5.4) is unbounded for comb laws with a rational fibre, while the
  curved marginals stay bounded (Example 5.2).
- Fourier bounds that take moduli of a twisted transform are unbounded for laws with many narrow bumps, however
  small the twist (twist_obstruction/, Theorem 1).
- Bounds that use only the density of the three-dimensional marginal and its integrals over lines (every
  two-dimensional marginal) settle the one-sheet side of rank three and say nothing on the two-sheet side
  (two_sheet_side/, Proposition 1).
- Bounds that take the modulus of the transform of the hub law lose a logarithm of H(f_0) already at eps = 0, where
  the form is bounded for every hub law; the proof of that case keeps the hub law in physical space
  (two_sheet_side/, Section 3).

So a proof has to use the curvature of the level sets against the product structure, at the scales between the width
of the bumps and 1.

## Numerics

No configuration tested moves the density: comb laws on random frames with m = 8, 32, 128 light coordinates and
eps = 0.01, 0.001 give 0.078 to 0.091 for a rough hub and 0.123 to 0.132 for a uniform one, a hub diagonal of 0.5 or
-0.5 changes nothing, a hub that sees P never exceeded 0.70 over 40 comb laws, and U + c V^2 on a rational plane in
R^8 stays within 13 per cent of the flat marginal while M_2 grows linearly in N (single_hub_core/num/).
