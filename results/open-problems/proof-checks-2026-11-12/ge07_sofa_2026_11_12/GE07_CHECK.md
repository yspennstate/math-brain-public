# GE07 moving sofa: Baek's proof that Gerver's sofa is optimal, read in part and tested

Checked 12 Nov 2026 by an agent.

## Verdict

The problem has a complete claimed solution: J. Baek, "Optimality of Gerver's Sofa", arXiv 2411.19826v1
(29 Nov 2024, 119 pages), proves that Gerver's sofa, of area 2.2195..., has the largest area. The parts read
here contain no error that I could find, and every statement about Gerver's sofa and about the upper bound Q
that could be put on a computer came out as the paper says. About half of the paper was not read (list below),
so this is not a verification of the proof. The row should not be worked on as an open problem.

Status of the source as far as the arXiv record shows on 12 Nov 2026: one version, no journal reference. Whether
it has been accepted or formalized was not established here.

Sources:

- J. Baek, arXiv 2411.19826v1. Read: Sections 1.1, 1.7, 1.8; Section 6.5; Definitions 8.1.1–8.1.4 and 8.2.1–8.2.2
  with Lemmas 8.2.2–8.2.3; Section 8.3 in full; Section 8.4 up to Theorem 8.4.3; the statements of 8.4.4–8.5.8.
  Not read: Chapters 2–5 (a maximum sofa may be taken monotone, balanced, with rotation angle pi/2), Chapter 6
  apart from 6.5, Chapter 7 (Mamikon's theorem and the convex curve area functionals), the proof of Theorem 8.2.4
  (area <= Q under the injectivity condition) and the proofs in Section 8.5.
- D. Romik, "Differential equations and exact solutions in the moving sofa problem", arXiv 1606.08111v3: Theorem 1
  (the balance equations), Theorem 3 and Table 1 (the explicit rotation path of Gerver's sofa).
- J. Baek, arXiv 2406.10725v2 (the conditional bound 1 + pi^2/8); its arXiv comment says it is superseded by
  2411.19826.
- D. Trela, "Certified Geometry and Admissible Motion of Gerver's Sofa", arXiv 2610.13955 (19 Aug 2026). The
  abstract states an exact-rational certification of Gerver's construction (Krawczyk inclusions for Romik's
  equations, interval propagation through the five phases) and that the Gerver-specific hypotheses of Baek's
  framework are certified. Abstract only; not read, not run.

## Structure of the proof

1. Reductions (Chapters 2–5): a maximum-area sofa can be taken monotone, balanced, and with rotation angle pi/2.
2. Injectivity (Section 1.7, Chapter 6): for a balanced maximum sofa the rotation path x is C^1 with
   x'.u_t < 0 and x'.v_t > 0 on (0, pi/2). With the arm lengths f, g (distances from the outer corner to the
   contact points A(t), C(t)) this reads f, g > 1. It follows from the differential inequality (1.9),
   <A',v> <= max(<-B',v>, 0) + |<x',v>|, which gives f' >= m0(g) with m0(x) = x - max(|x-1|, (|x-1|+1)/2), and from
   an iteration f_{n+1} = max(f_n, F f_n), F f(x) = 1 + int_0^x m0(f(pi/2 - u)) du, that passes 1 after eleven steps
   (Lemma 6.5.3: F j_c >= j_{c+1/12} for 0 <= c <= 2/3, where j_c = max(1 - x, c)).
3. Upper bound (Chapter 8): on triples (K, B, D) of convex bodies with K a cap and B, D contained in K and
   touching the inner walls as in Definition 8.1.3, the functional Q of Definition 8.2.2 is quadratic, bounds the
   area of the sofa with cap K from above (Theorem 8.2.4), is concave (Theorem 8.3.8, by Mamikon's theorem), has
   non-positive directional derivative at Gerver's triple (Theorem 8.5.7, from Romik's equations), and equals the
   area there (Theorem 8.4.6).

## Checked by hand

- (1.9) implies (1.10), in the two cases <A',v> < 1 and >= 1.
- m0 is 2x - 1 for x < 0, 3x/2 - 1 on [0, 1], min(1, x/2) for x >= 1, and increasing; this is what the
  monotonicity of F needs.
- Both cases of Lemma 6.5.3, with exact minima: -1/8 + 3 pi/8 - 3 pi^2/32 = 0.12782 at c = 7/6 - pi/4, and
  -1/2 + 3 pi/4 - 3 pi^2/16 = 0.00564 at c = 5/3 - pi/2. The second margin is thin but positive.
- Lemma 8.3.4, Q = P_K - R_B - L_D: the identity reduces to J(Y, x) = J(Z, x) - J(Z, Y) for collinear Z, x, Y
  and to the vanishing of J on pairs collinear with the origin.
- Section 8.3 as a whole: given Theorem 7.4.2 (Mamikon areas are convex and quadratic) and Theorem 7.1.2
  (linearity of support values and of intersections of support lines), each step of Lemmas 8.3.5–8.3.7 and of
  Theorem 8.3.8 follows.

## Checked by computer (floating point)

`ge07_check.py`, output `ge07_check.out`:

1. Romik's Table 1: x and x' continuous at the four break points to 1e-14; x(0) = 0; x(pi/2) = (-1.2275264589, 0);
   the mirror symmetry holds to 4e-15.
2. Arm lengths on Gerver's sofa: f(0) = 1, g(0) = 2.4206448441, f increasing, g decreasing, f, g > 1 inside.
3. Romik's balance equations hold on the five intervals exactly as in the table of Baek's Theorem 8.4.2
   (residuals below 5e-15), and <A',u> = 0.
4. (1.9), (1.10), (1.11) hold on Gerver's sofa: with equality on the second and fourth intervals, strictly on the
   others (margins 1.4, 0.028, and 2.4e-6 on the last interval, where equality is reached at t = pi/2).
5. The iteration: f_n >= j_{(n-1)/12} for n <= 10; min f_n = 0, 0.096, 0.227, 0.443, 0.747 for n = 1..5 and
   f_n > 1 away from 0 from n = 6 on; Gerver's f stays above every f_n (40 steps).
6. Area of the set cut out by the rotating hallway, computed column by column with no assumption on its shape:
   2.2074 for Hammersley's sofa (exact pi/2 + 2/pi = 2.20741610) and 2.21953 for Gerver's; every interior column
   is non-empty.
7. Area from the boundary curves of Theorem 8.4.1 by Green's theorem: |K| = 2.860972951, niche 0.641441282,
   difference 2.219531669.
8. Gerver's remark quoted in Remark 8.4.1: at t = pi/4 the point x(phi) is 0.001238 from the inner wall.

`ge07_q.py`, outputs `ge07_q_800.out`, `ge07_q_1600.out`. Convex bodies are polygons with edge normals on one fixed
grid containing the angles phi, theta, pi/2 - theta, pi/2 - phi; on such polygons Minkowski combinations are linear
in the support values and Q is an exact quadratic form (checked: residual 1e-14 along a segment).

9. Q at Gerver's triple: 2.219533645 on 801 base angles, 2.219532163 on 1601; the error falls by a factor 4.0 and
   the extrapolated value is 2.219531669, the area (Theorem 8.4.6).
10. Area <= Q (Theorem 8.2.4) on 19 other caps satisfying the injectivity condition (semicircular and elliptical
    rotation paths, and mixtures of these with Gerver's path): Q minus the area lies between -1.5e-6 and +1.6e-4,
    where the area is accurate to about 4e-6.
11. Q < Q(Gerver) on all 19; the closest is 1.6e-6 below.
12. Concavity (Theorem 8.3.8): negative second-order coefficient on all 253 segments between 23 points of the
    domain (the 20 caps with their B_K, D_K and three triples with B, D cut smaller).
13. Directional derivative at Gerver's triple (Theorem 8.5.7) towards the other 22 points: at most +8e-8 on the
    finer grid (+3e-7 on the coarser, so the positive values are grid error), and clearly negative in several
    directions (-1.1e-2, -3.2e-3 towards two elliptical caps, -2e-5 to -1.1e-3 towards smaller B, D).

Mixtures continued past Gerver's path (negative weight on the other path) leave the family of caps: the support
values are no longer those of a convex body. They are listed in the output as excluded.

## Two small points in the text

- The caption of Figure 1.10 says that numerically three iterations already give f_3 > 1. With Definitions 6.5.1
  and 6.5.2 as written, the numerical iteration first exceeds 1 (away from 0) at n = 6. The proof uses eleven
  steps and is not affected.
- Lemma 6.5.5 is stated on (0, 1]; its proof gives (0, pi/2].

## Literature

arXiv search all:"moving sofa", by date, 12 entries (lit/search/s1.xml). After Baek's paper: Trela 2610.13955
(above); He 2608.11206 (an algorithm for variants); Tang 2610.14050 and 2610.14051 (bounds for a three-dimensional
snaky corridor). None disputes the result. Before it: Kallus–Romik 1706.06630 (upper bound 2.37), Romik 1606.08111,
Deng 2407.02587, Leng et al. 2407.11106.

## For the list

GE07 is claimed solved by a preprint whose tested parts hold. Take it off the problems to attack; keep one line
saying "solved by Baek 2024 (preprint), publication and formalization status to be confirmed". Open neighbours that
the search shows active: the ambidextrous sofa (Romik's shape, area 1.64495..., optimality open), sofas in
three-dimensional corridors, and other corridor shapes.
