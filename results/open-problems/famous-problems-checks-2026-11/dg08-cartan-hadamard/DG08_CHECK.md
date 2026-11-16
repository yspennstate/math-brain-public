# DG08: the Cartan-Hadamard conjecture

12 Nov 2026, an agent. Row DG08 of the top-200 general list.

## Verdict

The row is solved in 2026, by two routes that share nothing beyond Kleiner's confined-profile argument.
It should leave the list of problems to attack. Every source is an unrefereed preprint; none is in a
journal or in the OpenAI Lean index on 12 Nov 2026.

The conjecture: in a complete simply connected Riemannian n-manifold with sectional curvature at most
kappa <= 0, a domain has at least the boundary area of the ball of equal volume in the space form of
curvature kappa (kappa = 0 is the Cartan-Hadamard conjecture proper, kappa < 0 the generalized form).
Known before 2026: n = 2 (Weil; Beckenbach-Rado; Bol for kappa < 0), n = 3 (Kleiner, with kappa <= 0),
n = 4 for kappa = 0 (Croke).

## Sources

| source | date | what it proves | how |
|---|---|---|---|
| Chen, Ghomi, Wang, arXiv 2609.11005 | 10 Sep 2026 | kappa = 0, n = 5 | integrals over pairs of boundary points, Jacobi fields along chords |
| Chen, Ghomi, Wang, arXiv 2609.20517 | 17 Sep 2026 | kappa = 0, 3 <= n <= 9, with rigidity | same, weights chosen dimension by dimension; exact-arithmetic certificates |
| OpenAI, "Generalized Cartan-Hadamard isoperimetry and Euclidean equality rigidity" (openai/math, preprint 337, 42 pages) | 23 Sep 2026 | kappa <= 0, every n >= 2, sets of finite perimeter; rigidity for kappa = 0 | sharp critical Sobolev inequality on hypersurfaces |
| Agnoletto, Da Silva, Nardulli, Resende, arXiv 2609.17093v3 | Sep 2026 | small volumes under a Ricci lower bound; reduction of the general case to rigidity | profile comparison |
| Agnoletto, Da Silva, Nardulli, Resende, arXiv 2610.37817 (18 pages) | 27 Oct 2026 | kappa <= 0, every n, with rigidity for every kappa; Alexandrov spaces with two-sided bounds | their own proof of the same Sobolev inequality, then their reduction |
| Case, Mengesha, arXiv 2610.12309 (20 pages) | Oct 2026 | the Sobolev inequality in Euclidean space, any codimension, with the equality case | conformal invariance |
| Wheeler, arXiv 2609.14505 | Sep 2026 | kappa = 0, every n, under a pinching condition | abstract read only |

Chen-Ghomi-Wang and Agnoletto et al. (2610.37817) disclose the use of AI tools in preparing the papers.

## The inequality everything turns on

For a hypersurface S of dimension m = n - 1 >= 3 in a manifold with sec <= -b^2, with h the normalized
mean curvature, q = 2m/(m-2), s_m = |S^m|:

    int_S  4/(m-2) |grad v|^2 + m (h^2 - b^2) v^2   >=   m s_m^(2/m) ( int_S |v|^q )^(2/q).

On the round sphere in R^n this is the sharp Sobolev inequality of Aubin and Talenti. With v = 1 on a
hypersurface of constant mean curvature it reads |S| >= s_m / h^m when b = 0, which is exactly
Theorem 1.2 of Chen-Ghomi-Wang (arXiv 2609.20517), proved there by other means for 3 <= n <= 9. The two
routes therefore agree on the one statement where they meet.

From the inequality to the conjecture (OpenAI, Sections 4 and 5; read in full for Lemma 4.5, Lemma 5.4,
Proposition 5.5, Theorem 5.6): minimize perimeter at volume v inside a large geodesic ball B; at a
volume where the profile I is differentiable the minimizer's boundary has h = I'(v)/m on the free part
and 0 <= h <= I'(v)/m on the part touching the sphere; the constant test function gives

    I'(v) >= m sqrt( b^2 + (s_m / I(v))^(2/m) ),

and with W(A) the volume of the model ball of boundary area A one has W'(A) = 1 / (m sqrt(b^2 +
(s_m/A)^(2/m))), so (W o I)' >= 1 almost everywhere, W(I(v)) >= v, I(v) >= I_model(v). I checked the
derivative of W and the integration by hand; the argument needs I locally Lipschitz (their Lemma 4.4)
and the singular set of the minimizer to have zero capacity (dimension at most n - 8, their Lemmas
5.2, 5.3). Dimensions 2 and 3 are taken from Weil, Bol and Kleiner.

## What was checked here

By hand, in arXiv 2610.37817 (all of it except 22 lines of Section 3.2), the proof of the inequality:

1. A map Phi into the unit sphere with conformal-type factor f, built from the distance to a point p and
   a scale lambda; Hessian comparison gives Hess(log f) <= d log f (x) d log f - (1/2)(b^2 + f^2 +
   |grad log f|^2) g and |d Phi|^2 <= m f^2 on S. In R^n both are identities.
2. Integrating 4 v <grad v, grad log f> by parts and completing the square gives
   Q(v) >= m int v^2 (f^2 + (h + d_nu log f)^2) + (q-2) int |grad v - ((m-2)/2) v grad log f|^2.
3. If the best constant on a compact piece were below the sphere's, a minimizer v0 would exist
   (Brezis-Lieb). Choose p and lambda so that every coordinate of Phi has mean zero against |v0|^q
   (a Brouwer argument). The second variation in the directions v0 Phi_j, summed over j, with steps 1 and 2,
   forces v0 = const f^((m-2)/2), which cannot vanish on the boundary of the piece.

By computer (dg08_check.py, dg08_check.out):

- the three model identities for log f in curvature -kappa^2 and 0, and the two conformal-factor
  identities of Phi: residuals below 2e-15 at 40 random points each;
- the completing-the-square identity and the form of the lower bound in step 2: exact, symbolic;
- equality on geodesic spheres of the model spaces, 45 cases (n = 4, 5, 6, 7, 9; three curvatures; three
  radii): relative error below 2e-12;
- the inequality in R^n on 30 hypersurfaces of revolution (spheroids, non-convex peanut and lens
  profiles; n = 4, 5, 6) with 5 test functions: lowest ratio of the two sides 1.000000, attained on the
  round sphere by the constant and by a Moebius-type extremal; all other cases between 1.002 and 8.09.

Not checked: the regularity inputs for confined minimizers (Ghomi-Spruck obstacle regularity, the
OpenAI Lemmas 4.1-4.4 and 5.1-5.3), the passage to sets of finite volume (Section 6), both rigidity
arguments (OpenAI Sections 7, 8; Agnoletto et al. Section 3), the reduction paper 2609.17093, and the
Chen-Ghomi-Wang proof.

## Literature search

arXiv, 12 Nov 2026: "Cartan-Hadamard conjecture" (s1), isoperimetric with "Cartan-Hadamard manifolds" or
"nonpositive curvature" (s2), authors Ghomi or Nardulli with isoperimetric (s3), each newest first. No
paper disputing any of the proofs was found. The OpenAI collection also holds a companion on sharp
integral fillings in CAT(0) spaces (23 Sep 2026) and a preprint on the isoperimetric conjecture for the
cubic flat three-torus (24 Sep 2026); neither was read.

## Proposal for the list

Mark DG08 solved 2026 (Chen-Ghomi-Wang for 3 <= n <= 9; OpenAI and Agnoletto-Da Silva-Nardulli-Resende
in every dimension, generalized form included), check level "key inequality re-derived and tested, the
regularity and rigidity parts not read", and replace the row.
