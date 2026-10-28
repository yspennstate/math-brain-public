# Partner addendum — account03/B11 applied after primary report

Fresh brain main later exposed the completed assigned-partner handoff


with canonical mathematics

`yspennstate/math-open-problems@87e1ab186dd03a3f8ba3aafcf4a9f23028e3bd6f:proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260922T114319Z-account03-B11-qform-r1/REPORT.md`.

This addendum applies that result to the primary report rather than leaving the earlier availability statement stale.

## Exact overlap and complementary constants

The partner proves that for independent density-`<=1` variables,

`R=2bXY+dY^2+alpha X+beta Y+gamma`,

plus an independent square

`S=cZ^2+eta Z+theta`,

one has

`||p_{R+S}||_infinity <= 4/sqrt(|bc|)`.

Our primary semi-cross principal block is

`[[alpha,a,0],[a,0,0],[0,0,d]]`.

After swapping the first two physical coordinates, the corresponding conditional three-variable quadratic is exactly of the partner form with

`b=a`, partner's `d=alpha`, and partner's `c=d`.

Therefore the same full conditional/outside-coupling argument gives the stronger-in-the-isotropic-regime bound

`||p_Q||_infinity <= 4 |ad|^{-1/2}`

for the whole semi-cross family in the primary report.

Our independent `L^3 * L^{3/2}` argument remains mathematically nonredundant because it gives the anisotropic estimate

`||p_Q||_infinity <= 6 |a|^{-2/3}|d|^{-1/3}`

and, more importantly, proves the standalone binary statement

`||p_{alpha X^2+2aXY+rX+sY+c}||_3 <= 3|a|^{-2/3}`,

which is not asserted in the partner handoff. Combining the two proved mechanisms gives the certified envelope

`||p_Q||_infinity <= min(4|ad|^{-1/2}, 6|a|^{-2/3}|d|^{-1/3})`.

The two terms are genuinely complementary: their ratio is

`(6|a|^{-2/3}|d|^{-1/3})/(4|ad|^{-1/2}) = (3/2)(|d|/|a|)^{1/6}`.

Thus the `L^3` route is numerically sharper when `|d|/|a| < (2/3)^6 = 64/729`, while the partner half-potential route is sharper when the square direction is not much weaker than the cross coefficient. Both have the correct homogeneous degree `-1` under common scaling of the quadratic coefficients.

For `|a|,|d|>=1`, the partner gives the clean universal constant `4`, improving the primary report's `6` on that normalized branch.

## Structural lesson

The two proofs identify the same regularization phenomenon at different functional levels:

- the rank-two opposite-sign saddle may have an unbounded logarithmic density;
- account03/B11 proves a uniformly bounded half-order Abel potential for that saddle;
- this run proves a uniform `L^3` norm on the semi-cross saddle;
- the third square supplies, respectively, a square-root Abel kernel or an `L^{3/2}` density;
- either pairing closes at `L^infinity` while preserving the original product coordinates.

This is precisely the mechanism that the invalid post-rotation-independence shortcut misses.

## Updated first unpaid implication

The first unpaid local implication is still the general binary theorem

`BINARY-INDEFINITE-L3:`

for every independent density-`<=1` pair and every affine indefinite binary quadratic with discriminant `D>0`, prove

`||p_q||_3 <= C D^{-1/3}`.

But the partner result changes how it should be used: a successful proof would not merely reprove the semi-cross `L^infinity` branch. Its value is to control fully nonzero binary diagonals and to provide an anisotropic norm that can be combined with a third-direction estimate even when the partner's zero-diagonal Abel normal form is unavailable in physical product coordinates.

After that, the genuinely three-way obstacle is nonzero coupling of the third selected coordinate into both hyperbolic variables, together with the global need to aggregate over coordinate triples in diffuse frames.

Status remains `ESSENTIAL_STEP_APPLIED`; full QFORM conjecture remains OPEN.
