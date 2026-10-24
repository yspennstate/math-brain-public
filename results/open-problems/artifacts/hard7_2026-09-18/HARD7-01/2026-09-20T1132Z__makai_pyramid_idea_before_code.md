# HARD7-01 fresh-target route note before code — Makai Jr. Conjecture 1.3 on all pyramids

Fresh canonical target: `operations/claims/MAKAI-POLAR-DIFFERENCE-BODY.md`.

In dimension three the conjecture is

\[
|L|\,|(L-L)^\circ|\ge \frac23.
\]

Attack the negation first on the entire three-dimensional pyramid family.  Let `B subset R^2` be any planar convex body.  After an affine shear/height normalization every nondegenerate pyramid is equivalent to

\[
L=\operatorname{conv}(B\times\{0\},(0,1)).
\]

Write `A=|B|` and `E=B-B`.  The earlier HARD7-01 pyramid calculation, which was derived for a different combined functional, already gives exact independent identities

\[
|L|=A/3,
\qquad
|(L-L)^\circ|=\frac43|E^\circ|.
\]

Therefore the Makai functional on every pyramid factorizes exactly as

\[
|L|\,|(L-L)^\circ|
=\frac49 A|E^\circ|.
\]

The planar Eggleston theorem is exactly

\[
A|E^\circ|=|B|\,|(B-B)^\circ|\ge\frac32,
\]

with equality iff `B` is a triangle.  Hence every three-dimensional pyramid satisfies

\[
|L|\,|(L-L)^\circ|\ge\frac49\cdot\frac32=\frac23,
\]

and equality within the pyramid family occurs iff the base is a triangle, i.e. iff `L` is a tetrahedron.

This is an all-parameter theorem for the full pyramid family, not finite sampling. It does not move `d_Makai=2`, because general three-dimensional convex bodies remain untreated.

Method outcomes planned for the fresh target:

- **B2 (attack the negation):** any pyramidal counterexample would induce a planar counterexample to Eggleston; thus none exists.
- **B5 (add/deform a parameter):** apex height and horizontal apex location are affine/shear parameters; normalizing them shows the product depends only on the affine class of the base through `A|E^circ|`.
- **B11 (dualize):** the exact polar fiber identity `|(L-L)^circ|=(4/3)|(B-B)^circ|` is the decisive dimensional collapse.

Before promotion: re-check the fiber derivation and constants, run an exact rational endpoint certificate for a triangular base and a nontriangular base, and search specifically for an existing published all-pyramids Makai theorem. Priority remains UNVERIFIED absent that search.