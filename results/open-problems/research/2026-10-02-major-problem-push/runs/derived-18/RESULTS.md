# Derived-18 research result: cactus-backbone determinant gluing and disjoint-pair NC

## Completed theorem

For every finite weighted cactus backbone (every block is an edge or a
cycle), the one-apex forest polynomial with arbitrary nonnegative vertex
profile has only negative real zeros. More strongly, its full multivariate
apex-spoke polynomial has a profile-uniform positive-definite rank-one
determinant representation, hence is real stable. The marginal law of all
apex-spoke indicators is therefore strongly Rayleigh and negatively
associated under arbitrary spoke external fields and spoke cylinder
conditioning.

Applying the previously audited arbitrary-backbone four-core identity gives
a separate result. Add four external vertices with arbitrary proportional
spoke rows to the cactus and exactly two disjoint external marked edges. The
two marked indicators are negatively correlated at every activity, strictly
exactly when all four row factors and at least two profile entries are
positive. Every positive-probability backbone cylinder conditioning is
included, with strictness determined by positive contracted profile blocks.

This extends derived-17 from one cycle to arbitrary cactus block trees with
arbitrarily many cycles. It does not cover a 2-connected block with two
independent cycles, nonproportional rows, or negative association involving
the backbone and external marked edges. The full forest conjecture remains
open.

## New analytic input

Define property `DR` by

`D_G(z)=c det(K+sum_x z_x q_x q_x*)`,

with `K` Hermitian positive definite and the vertex vectors spanning. The
cycle transfer proof from derived-17 actually yields `DR`: its
quasi-periodic Hermitian pencil is profile-independent, and leading
coefficients identify the entire polynomial, not only its roots.

Two closure operations are proved exactly.

1. **Leaf lift.** If a leaf of edge activity `w` is attached at `u`, replace
   `K` by `diag(K,1+w)`, lift old vectors, and use
   `q_v=(sqrt(w/(1+w))q_u,1)`. The matrix determinant lemma matches the exact
   absent/present leaf recurrence.
2. **One-vertex sum.** Normalize each shared vector to the first coordinate
   and identify those coordinates. The glued block pencil has top-left entry
   `a_1+a_2-1`. Split the shared spoke variable as
   `z_u=z_u^(1)+z_u^(2)` between the sides. Its Schur complement is exactly
   the component formula `D=D_1E_2+E_1D_2-E_1E_2`, where
   `E_i=partial_(z_u)D_i` deletes the apex factor of the articulation
   component.

Edge and cycle blocks have `DR`; induction over the cactus block tree proves
the theorem. Real stability follows immediately because positive imaginary
parts give a positive-definite imaginary matrix. The established
Borcea--Branden--Liggett implication supplies strong Rayleigh and negative
association for the spoke marginal.

## Exact verification and audit

The author checker uses literal Fraction forest enumeration and a standalone
square-free Sturm/gcd root counter. It passes:

- 24 rational determinant leaf lifts checked coefficient-by-coefficient;
- 12 exact one-vertex component-gluing identities;
- 24 connected unicyclic, eight disconnected pseudoforest, and 12 genuine
  connected multi-cycle cactus root cases;
- ten literal full marked graphs, including a figure-eight cactus; and
- all 78 positive-probability absent/present/free conditionings of a
  triangle-plus-leaf backbone; three forced-cycle zero measures are detected
  and excluded rather than counted as sign checks.

The fresh independent analytic audit **PASSes** after one incorporated
notation repair: the articulation variable is split into distinct side
variables whose sum is the final shared variable. Its standalone checker
imports no author helper and passes 20 normalization systems, 12 abstract
Schur one-sums, 12 unrelated literal split-profile one-sums, 12 connected
multi-cycle cactus root cases, one full figure-eight marked graph, and 64
positive-probability conditionings (32 strict, 32 equality), while detecting
and excluding 17 forced-cycle zero measures. No counterexample or remaining
proof gap was found.

## Status and prior art

Brand--Dell--Roth's established general apex component formula is credited.
Huang's graph-reduction results, Bado's 2026 unit-wheel theorem, the current
Ciceksiz--Ravichandran high-fugacity/general identities, Gupta's complete-
graph theorem, and Borcea--Branden--Liggett strong-Rayleigh theory are all
credited in the source report. No located primary source states the present
profile-uniform leaf/one-sum determinant closure or the precise cactus
external-marked-pair theorem, but bounded search does not certify historical
novelty. External specialist review is absent.

Full forest negative dependence, full Boolean FEI, unrestricted ML10
Sidorenko, and Kaplansky/direct finiteness remain open in this campaign.
