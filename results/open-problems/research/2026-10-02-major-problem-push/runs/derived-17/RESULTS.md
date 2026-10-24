# Derived-17 research result: disjoint-pair NC over every weighted cycle backbone

## Completed theorem

Let an arbitrary finite weighted cycle carry an arbitrary nonnegative vertex
profile.  Add four new vertices whose spoke rows are `a,b,c,d` times that
profile, and add exactly two disjoint marked edges pairing the new vertices.
The marked indicators are negatively correlated at every activity.  For
positive marked-edge fields, strictness is exactly `abcd>0` and at least two
positive profile entries.  The conclusion survives every positive-
probability coordinate conditioning of cycle edges; strictness then uses
positive contracted profile blocks.

This is a genuine cyclic extension of derived-15, whose analytic theorem
required a forest backbone.  It is not the full forest negative-correlation
conjecture and does not cover nonproportional rows or whole-vector NA.

## New analytic input

For rim activities `lambda_i` and profile `beta_i`, the one-apex forest
partition has the exact two-state transfer

`D(s)=tr(T_0(s)...T_(n-1)(s))-2 product_i lambda_i`,

with

`T_i=[[1+lambda_i+s beta_i, s beta_i lambda_i],[1,lambda_i]]`.

At a zero of D, the monodromy has multiplier rho satisfying
`|rho|^2=product_i lambda_i(1+lambda_i)`.  Eliminating one transfer coordinate
gives a quasi-periodic tridiagonal generalized eigenproblem.  The explicit
inner-product weights

`m_(i+1)=m_i/[lambda_i(1+lambda_i)]`

make every interior term and the wraparound term Hermitian precisely because
of the multiplier-modulus identity.  Hence every zero is real; positivity of
the forest coefficients makes every zero negative.  Zero rim activities
reduce to a forest, and zero profile entries follow by coefficientwise
limits.  The degree is the number of positive profile entries.

The already audited arbitrary-backbone four-core identity needs only this
negative-root factorization.  Its two explicit Stieltjes sums then prove the
marked Rayleigh difference and exact strictness.

## Independent verification

The full independent analytic audit passes, including the separate
coincident-neighbor calculation for a two-vertex cycle with unequal parallel
edges.  Its standalone exact checker imports no author helper and passes:

- 28 prescribed plus 120 seeded rational apex cases, with three independent
  coefficient constructions and exact Sturm/gcd root multiplicities;
- eight literal graphs containing all four new vertices (six strict, two
  equality); and
- all 106 positive-probability partial rim coordinate conditionings (88
  strict, 18 equality).

The author checker passes 67 further exact apex cases and five literal
marked graphs.  A separate uniform-cycle Chebyshev proof and independent
checker provide an analytically different special-case route.

## Status and prior art

The closest located September 2026 primary result proves pairwise edge
negative correlation for unit-weight wheel graphs.  It is credited in the
source report.  The present external-four-vertex weighted/profile theorem is
different, but historical novelty and external review remain unverified.
Current sources still describe the general forest conjecture as open.

Full forest negative dependence, full Boolean FEI, unrestricted ML10
Sidorenko, and Kaplansky/direct finiteness remain open in this campaign.

