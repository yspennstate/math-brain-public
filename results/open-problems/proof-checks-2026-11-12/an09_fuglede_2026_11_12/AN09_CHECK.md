# Row AN09 (Fuglede's conjecture in dimensions one and two): the finite sets of arXiv 2607.15632 checked

12 Nov 2026. Source: arXiv 2607.15632v1 (Tao Zhang, 17 Jul 2026), "Both directions of Fuglede's conjecture fail in
dimension two". One preprint; no follow-up or comment found on arXiv (search of 12 Nov, lit/search/s1.xml).

## What the preprint claims

In G = Z60 x Z12 (order 720) two explicit 60-point sets:
- A-, with a 12-point T- such that A- + T- = G, and A- has no spectrum (its Theorem 3.1, formulas (23), (24));
- A+, with a 60-point spectrum Lambda+ (formula (30)), and A+ does not tile G (its Theorem 4.1).
Its Proposition 2.1 then passes from G to Z^2 and to finite unions of unit squares in R^2.

## What was checked here, and how

Two programs, written separately, no shared code.

an09_check.py works in G from the explicit formulas. Character sums are tested for zero exactly in
Z[x]/(Phi_60), with a floating value beside it; the two tests agreed on every frequency.
- A- + T- = G: 720 sums, 720 distinct.
- The transform of the indicator of A- vanishes at 529 of the 719 nonzero frequencies, 105 of them in the
  index-5 subgroup S = {(a, b): 5 | a} of the dual group. A spectrum would have 60 points, so 12 of them in one
  coset of S, pairwise differing by zeros in S. An exhaustive clique search in the Cayley graph of S on those 105
  zeros gives largest clique 10. So A- has no spectrum.
- Lambda+ is a spectrum of A+: all 3540 ordered pairs of distinct points differ by a zero of the transform of A+.
- A+ - A+ has 615 elements. A tiling complement T has 12 points with (T - T) meeting A+ - A+ only in 0; the
  largest such set has 10 points (exhaustive). So A+ does not tile G.
- Controls for the search: the seed sets B0, B1, B2 in Z12 x Z12 have a common tiling complement of size 12 and
  no common orthogonal family above 10; V0, V1, V2 have a common spectrum of size 12 and no common tiling
  complement above 10. The search finds 12 exactly where the paper exhibits a set.

an09_check2.py works in K = Z12 x Z12 x Z5 from the layer definitions, with floating sums only (the smallest
nonzero modulus met is 12.0, so the zero test has no borderline case), and a layered backtracking in place of
the clique search: no zero of the transform of A- has the form (0, v, 0), so an orthogonal 12-family in a fibre has
one point over each first coordinate; A+ - A+ contains H x (Z5 minus 0) and every (0, k, 0), so a tiling complement
lies in one layer with one point over each first coordinate. Result: no 12-point family in either case, the
deepest partial family has 10 points. The images of the layer sets under the map (22) of the paper equal the
explicit formulas (23), (30) and the display for A+. Controls with the layering on the second coordinate find
576 common tiling complements of B0, B1, B2 and 576 common spectra of V0, V1, V2 through the origin.

Outputs: an09_check.out, an09_check2.out. Each program runs in about two seconds.

## What was not checked

Proposition 2.1 of the preprint (finite group to Z^2 to R^2). Its spectral parts are quoted from Kolountzakis and
Matolcsi, "Tiles with no spectra", Forum Math. 18 (2006), Theorems 4.1 and 4.2; the non-tiling part for a
rectangular group Z_{n1} x Z_{n2} is proved in the preprint after Matolcsi's Proposition 2.5, with the threshold
k > max(2, 8 n1 n2 / |A|), which is 96 here. I did not read that source or verify the rectangular argument.

## Proposal for the row

The finite statement (both implications of Fuglede's conjecture fail in Z60 x Z12) is confirmed by computation.
The statement in R^2 follows if Proposition 2.1 holds, which rests on a 2006 theorem and a short adaptation.
Dimension one stays open in both directions; the row should be restated to dimension one (with the three-interval
result, arXiv 2607.24005, as the newest partial result), and the two-dimensional half marked as reported disproved,
finite part checked.
