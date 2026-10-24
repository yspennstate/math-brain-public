# Disjoint marked pair over an arbitrary weighted forest backbone

The complete proof is
`forest_disjoint_rank_one_attachment_forest_backbone_proof.md`; the full
independent audit is
`FOREST_DISJOINT_RANK_ONE_ATTACHMENT_FOREST_BACKBONE_K_INDEPENDENT_AUDIT.md`.
Both exact implementations and reports are included.  Read those files in
full before using the result.

## Theorem

Let `H` be any finite weighted forest and give its vertices an arbitrary
nonnegative profile `beta_j`.  Add four new vertices with spoke activities
`a beta_j`, `b beta_j`, `c beta_j`, `d beta_j`, and add exactly the two
disjoint marked edges joining the first pair and the second pair.  There are
no other edges incident to the new vertices.  Then the two marked edge
indicators are negatively correlated for all nonnegative finite activities.

For positive marked-edge activities, strictness holds exactly when all four
row factors are positive and at least two backbone vertices have positive
profile.  Under coordinate/cylinder conditioning of backbone edges, present
edges are contracted, absent edges deleted, and strictness uses the number
of contracted components with positive profile sum.  Positive fields on
backbone and marked edges are allowed.  Individual spoke fields are not.

## Proof certificate

Under the forest law on `H`, backbone edges are independent percolation.
A Gaussian tree covariance `C` satisfies

    det C_S = Pr(no two vertices of S are connected).

The apex partition therefore has the exact factorization

    D(s)/Z_H = det(I+s diag(sqrt(beta)) C diag(sqrt(beta)))
             = product_i (1+s x_i),  x_i>0.

An exact four-core nilpotent transfer retains every mixture variance,
covariance and third cumulant.  If `U,Gamma,Omega,T` are the resulting
logarithmic-derivative quantities, direct deletion/contraction gives

    (EF-AC)/(D^2 abcd)
      = 2(UT-Omega)
        +(a+b)(c+d)(Gamma^2+U^2T-2U Omega).

The apex factorization turns both brackets into explicit nonnegative
Stieltjes sums.  The first is

    UT-Omega = sum_{i != j} alpha_i tau_j,

and is strictly positive exactly when the profile rank is at least two.
The second has a complete three-sum nonnegative expansion in the proof.
No sign is assigned heuristically to a cumulant, and no cyclic-backbone
real-rootedness is assumed.

## Verification

Run:

    python forest_disjoint_rank_one_attachment_forest_backbone_exact.py
    python forest_disjoint_rank_one_attachment_forest_backbone_k_independent.py

The author checker verifies every tree-covariance principal minor against
literal percolation, the apex polynomial, four-core coefficients, third
derivatives, both Stieltjes brackets, full Rayleigh cancellation and all 324
positive-probability partial coordinate conditionings in five rational
examples.  Two cases also match literal original-graph enumeration.

The independent checker imports no author helper and retains every original
vertex in a connectivity-partition skip/join DP.  It passes 16,608 exhaustive
exact cases (632 strict, 15,976 equality) and 1,200 seeded rational cases
(425 strict, 775 equality), with zero counterexamples or strictness
mismatches.  Finite checks corroborate; the determinant and Stieltjes
identities prove the unbounded theorem.

The exact primary-source and scope record is in
`FOREST_DISJOINT_PAIR_SOURCE_AND_SCOPE_CHECK.md`.  The full forest pair/NA
conjecture remains open.  Historical novelty and external specialist review
are unverified.
