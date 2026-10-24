# Derived checkpoint 15: disjoint marked pair over any forest backbone

3 October 2026 UTC.  Parent master
`38dd70c47f164d12513d3a4912af883de0706cbd`.  Only this campaign's
`CURRENT.md` changes in place; all earlier work remains immutable.  The full
proof, audit, exact implementations, source check and exploratory boundary
are in
`proofnet24/P14-probability-correlation/continuations/2026-10-03-forest-backbone-disjoint-pair/`.

## Completed restricted theorem

Let `H` be any finite weighted forest with nonnegative vertex profile
`beta_j`.  Add four new vertices whose spoke rows are respectively
`a beta_j,b beta_j,c beta_j,d beta_j`, and exactly two disjoint marked
mutual edges joining the first pair and the second pair.  With no other
edges incident to the new vertices, the marked indicators are negatively
correlated for every nonnegative finite activity.

For positive marked activities, strictness holds exactly when all four row
factors are positive and at least two profile weights are positive.  The
theorem survives positive fields on backbone and marked edges and arbitrary
positive-probability coordinate/cylinder conditioning of backbone edge
indicators.  Under conditioning, required-present edges are contracted,
required-absent edges deleted, and strictness uses the number of contracted
components with positive profile sum.

## Determinant and Stieltjes proof

The forest measure on the backbone is independent bond percolation.  A
Gaussian tree covariance matrix `C` has the exact principal-minor identity

    det C_S = Pr(no two selected vertices are percolation-connected).

Consequently the one-apex partition is

    D(s)/Z_H = det(I+s diag(sqrt(beta)) C diag(sqrt(beta)))
             = product_i(1+s x_i),  x_i>0.

This is proved directly by multiaffinity and the `{0,1}` percolation cube;
no real-rootedness theorem for cyclic backbones is assumed.

An exact four-core nilpotent transfer preserves every mixture variance,
covariance and third cumulant.  Direct marked-edge deletion/contraction
reduces the Rayleigh difference to

    (EF-AC)/(D^2 abcd)
      =2(UT-Omega)
       +(a+b)(c+d)(Gamma^2+U^2T-2U Omega).

The apex factorization turns the first bracket into
`sum_{i!=j} alpha_i tau_j` and the second into three explicit nonnegative
sums.  These expansions also give the exact equality classification.  The
proof does not infer signs for individual cumulants or Hessian entries.

## Independent verification

The independent analytic audit reconstructs the determinant, transfer,
logarithmic derivatives, repeated-index cancellations, Rayleigh identity,
strictness and coordinate-conditioning closure; verdict PASS.  Root read
the full proof/audit and reran both implementations.

The author exact checker passes all 324 positive-probability partial
conditionings in five rational examples, including 26 and 242 strict cases
in the two larger connected examples.  It checks every covariance principal
minor against literal percolation, apex coefficients, `D,D',D'',D'''`, all
four marked coefficients and two literal original-graph enumerations.

The independently written all-vertex connectivity-partition DP imports no
author helper.  It passes 16,608 exhaustive exact cases (632 strict and
15,976 equality) on all labeled forest backbones through three vertices,
profiles in `{0,1,2}`, binary row factors and every partial backbone
conditioning.  A further 1,200 seeded rational cases through five backbone
vertices pass (425 strict and 775 equality).  There are zero counterexamples
or strictness mismatches; the smallest positive seeded Rayleigh value is
`29/129600`.  These tests corroborate rather than prove the universal claim.

## Boundaries and prior work

Exploratory cyclic-backbone apex searches are retained as numerical evidence
only.  The determinant argument genuinely uses that `H` is a forest, and
the proof does not extend to cyclic backbones merely from scalar
log-concavity.  Nonproportional spoke rows, individual spoke fields, other
edges incident to the new vertices, arbitrary-event conditioning, a whole
matching vector, strong Rayleigh and general forest negative association
remain outside the theorem.

Primary Grimmett--Winkler, Borcea--Branden--Liggett, matroid log-concavity,
Gupta's complete-graph theorem and the 30 September 2026
Ciceksiz--Ravichandran paper were checked.  The latter proves leading
high-fugacity coefficients and other regimes, not this all-activity
attachment theorem, and still treats general arboreal edge correlation as
open.  No exact prior statement was located in the bounded search;
historical novelty and external specialist review remain unverified.

The famous full forest negative-correlation/association conjecture remains
open, as do full Boolean FEI, unrestricted ML10 and Kaplansky/direct
finiteness in this campaign.
