SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B10, 2026-09-24T06:19:31Z.
attacking: the diffuse near-coloop parabolic endpoint after three source-overlap runs; change mechanism by testing whether the entire overlapping leaf bank can be compressed to bounded joint/marginal density data without retaining product-projection provenance.

# fleet01/B10 — near-coloop marginal caps do not replace product-projection provenance

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T061931Z-fleet01-B10-QFORM-auto11`  
Status: `NEW_EXACT_INTERFACE_COUNTEREXAMPLE / PARTNER_RESULT_APPLIED / FULL_EXACT_RANK3_OPEN / FULL_QFORM_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source boundary


The newest completed designated partner input is fleet02/B10 at

`yspennstate/math-open-problems@f860f87d88af57a9c67d68cb7c247afc7958f841`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B10/20260924T053442Z-fleet02-B10-QFORM-auto11/REPORT.md`.

Its genuine target-valid harmonic family is

`Q=2(sqrt(c)H+sqrt(rho)Z)L+V^2`,

with `c=1-rho`, `0<rho<1/64`, and `(Z,L,V)` three orthogonal linear forms of the SAME original leaf product bank. It proves that clean-square and exact-regression extraction can simultaneously fail. The purpose of this run is to test the next tempting simplification: forget that source provenance and retain only density caps for the compressed triplet.

## 2. Exact counterexample to the compressed-joint-density interface

### Theorem 2.1 — `QFORM-NEARCOLOOP-MARGINAL-CAPS-NOT-PROVENANCE-v1`

Put

`beta=1/8`, `c=64/65`, `rho=1/65`, `s=sqrt(c)=8/sqrt(65)`.

There exist a random variable `H` and a random vector `(Z,L,V)` such that:

1. `H ~ Uniform(0,1)` and is independent of the whole triplet `(Z,L,V)`;
2. `(Z,L,V)` has a probability density `g` with `0<=g<=1/8`;
3. every one-dimensional coordinate marginal of `(Z,L,V)` has density cap at most one;
4. every two-dimensional coordinate marginal `(Z,L)`, `(Z,V)`, `(L,V)` has density cap at most one;
5. nevertheless

   `Q = 2(s H + sqrt(rho) Z)L + V^2`

   has an unbounded density. More quantitatively, for every `0<q<s`,

   `p_Q(q) >= (1/(4s)) log(s/q)`.

Thus `ess sup p_Q = infinity`.

The quadratic coefficient matrix of the displayed form in coordinates `(H,Z,L,V)` has exactly three nonzero eigenvalues `{-1,1,1}`. This is NOT a counterexample to QFORM because the coordinates of `(Z,L,V)` are dependent and are not asserted to arise as an orthogonal projection of an original independent product vector. It is a counterexample to replacing that product-projection provenance by any collection of ordinary one-, two-, and three-dimensional density-cap statements, even at the exact near-coloop coefficients and with an independent heavy hub.

### Proof

Let

`E = {(z,l,v): -1<l<0, 1<v<2, 0< -beta z - v^2/(2 s l) <1}`

and set

`g(z,l,v)=beta 1_E(z,l,v)`.

For every fixed `(l,v)` in `(-1,0)x(1,2)`, the admissible `z`-section has length `1/beta=8`. Hence

`int g = beta * 1 * 1 * (1/beta)=1`,

so `g` is a probability density and `||g||_infinity=beta=1/8`.

The same section calculation gives the exact marginals

`p_L(l)=1_{(-1,0)}(l)`,
`p_V(v)=1_{(1,2)}(v)`,
`p_(L,V)(l,v)=1_{(-1,0)x(1,2)}(l,v)`.

For the other marginals, simply integrate the indicator over a set of length at most one:

`p_(L,Z)(l,z) <= beta`,
`p_(V,Z)(v,z) <= beta`,
`p_Z(z) <= beta`.

Therefore every coordinate marginal and every coordinate-pair marginal has density cap at most one, while the full triplet density is capped by `1/8`.

Let `H` be independent Uniform(0,1). Conditional on `(z,l,v)`, the map

`h -> 2 s (h+beta z) l + v^2`

is affine with derivative `2 s l`. Hence a density representative of `Q` is

`p_Q(q) = int_E beta [2 s |l|]^{-1} 1_{0<h_q(z,l,v)<1} dz dl dv`,

where

`h_q(z,l,v)= -beta z - v^2/(2 s l) + q/(2 s l)`.

Parameterize the `z`-section of `E` by

`theta = -beta z - v^2/(2 s l) in (0,1)`.

Then `|dz|=dtheta/beta`, so the factor `beta` in `g` cancels exactly. For `q>0` and `l<0`,

`h_q = theta - q/(2 s |l|)`.

If `theta in (1/2,1)` and `|l|>=q/s`, then `0<h_q<1`. Thus, for every `0<q<s`,

`p_Q(q)
 >= int_{q/s}^1 [1/(2 s r)] dr * int_1^2 dv * int_(1/2)^1 dtheta
 = (1/(4s)) log(s/q)`.

This diverges as `q downarrow 0` on an interval of positive measure at every height, proving `ess sup p_Q=infinity`.

Finally, the matrix of the quadratic form is

`[[0,0,s,0],
  [0,0,sqrt(rho),0],
  [s,sqrt(rho),0,0],
  [0,0,0,1]]`.

Since `s^2+rho=c+rho=1`, its nonzero eigenvalues are `-1,1,1`. QED.

## 3. What this rules out, and what it does not

The theorem is stronger than the generic arbitrary-joint coarea warning for the present near-coloop endpoint. It preserves all of the following information simultaneously:

- exact algebra `2(sH+sqrt(rho)Z)L+V^2` with `rho=1/65<1/64` and `c=64/65>63/64`;
- an independent cap-one hub `H`;
- a full three-dimensional leaf density cap `<1`;
- cap-one densities for all three scalar leaf marginals;
- cap-one densities for all three coordinate-pair leaf marginals;
- exact three-nonzero-eigenvalue spectrum `{-1,1,1}`.

Yet the logarithmic singularity survives. Therefore a successful proof for the genuine harmonic survivor cannot compress the original leaf product law to `(Z,L,V)` and then use only ordinary marginal/joint density caps. It must retain a specifically product-linear invariant: phase cancellation, a source-bank BL/Finner inequality, an averaged minor identity before projection, or an equivalent source-level structure.

Again, this does not challenge QFORM itself because the constructed leaf law is dependent and has not been realized as a product projection.

## 4. Designated partner result applied at an actual inequality

In the genuine target-valid harmonic family, fleet02/B10 proves for every original subset `I`

`||r_I||_2^2 + ||z_I||_2^2 >= (4sqrt(2)-5)||y_I||_2^2`.

Its completed application of the disjoint hard-square certificate supplies a square-heavy original bank `Vbank` with

`||y_Vbank||_2^2 >= 1/162`.

Therefore, on that actual guaranteed bank,

`boxed: ||r_Vbank||_2^2+||z_Vbank||_2^2
        >= (4sqrt(2)-5)/162
        = 0.004054655861... .`

This is the partner result spent at a concrete inequality in the precise remaining endpoint: the hard square cannot be source-cleaned, and the nonzero contamination cannot then be replaced merely by a bounded compressed joint density, because Theorem 2.1 shows that even much stronger compressed density metadata permits a logarithmic blow-up.

## 5. Remaining implication

The first unpaid implication is now

`QFORM-HARMONIC-PRODUCT-PROVENANCE-TWOSHEET-RECEIVER-v1`:

For the genuine harmonic/product-projection law

`Q=2(sqrt(c)H+sqrt(rho)Z)L+V^2`,

use the fact that `(Z,L,V)` are orthogonal linear forms of the SAME vector of independent original cap-one coordinates to remove the logarithm on the two-sheet endpoint. The proof may not replace that provenance by arbitrary joint/marginal density caps, exact regression, a clean square bank, post-rotation independence, a fiber supremum, moments/support assumptions, or deletion of a small coefficient times an unbounded variable.

A natural next mechanism is a source-level multilinear/Fourier inequality before projection, not another finite-dimensional density-cap estimate.

## 6. Status

- New result: exact near-coloop interface counterexample `QFORM-NEARCOLOOP-MARGINAL-CAPS-NOT-PROVENANCE-v1`.
- Partner fleet02/B10 result applied at the explicit contamination lower bound `0.004054655861...`.
- No QFORM counterexample found.
- Arbitrary exact rank three: OPEN.
- Full QFORM: OPEN / NOT PROVED / NOT DISPROVED.
- Full-target continuous density: OPEN. The fake compressed law above is absolutely continuous but has an unbounded logarithmic density, so it supplies no positive continuity conclusion for QFORM.
- Repository transport used; no authenticated native brain retrieval/receiver use occurred: `WITHOUT_VERIFIED_BRAIN`.
