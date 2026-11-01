# R01 TFIK22 final-profile orbit quotient — idea before code

Date: 2026-09-19.

This note records the new route before any checker is added.

For the already-complete `(n4,n3)=(2,12)` profile, the remaining finite core in the adjacent-degree-4 case is represented by alternating `R/B` words on the nine edges of a fixed `K_{3,3}` subdivision, with exactly three `R` and three `B` internal vertices in total. The old exact checker tested all 22,530 raw word placements and then found 60 non-2-apex placements collapsing to three graph-isomorphism classes.

The new route is to quotient *before* planarity testing.

1. **B18 / say it in another language.** Encode one oriented base edge by the bivariate generating function for alternating words. Truncated to total `R,B <= 3`,

   `F(x,y)=1+x+y+2xy+x^2y+xy^2+2x^2y^2+x^3y^2+x^2y^3+2x^3y^3`.

   Then the raw count should be `[x^3 y^3] F(x,y)^9 = 22530`; similarly `[xy]F^9=90`, independently checking the two raw counts used in the structural proof.

2. **B19 / make it an algorithm.** Act on the nine-word assignment by

   `Gamma = Aut(K_{3,3}) x C2_{a<->b}`,

   of order `72*2=144`. A side-preserving automorphism of `K_{3,3}` only permutes edge positions; a side-swapping automorphism also reverses every edge word; swapping the two degree-4 vertices exchanges `R` and `B`. Canonicalize assignments under this exact finite action and run the 2-apex test on one representative per orbit only.

3. **B3 / prove something stronger.** Aim to prove the stronger finite statement that the 22,530 raw assignments form a small exact set of structural symmetry orbits, and that the entire non-2-apex residue consists of exactly three `Gamma`-orbits, not merely three graph-isomorphism classes discovered after 22,530 tests. If true, archive orbit sizes and a canonical word-matrix normal form for each survivor.

This does not change `R_TFIK22=0`; its value is auditability. It would replace the largest raw finite core by a much smaller symmetry quotient and give independent arithmetic checks on the enumerator's completeness.