# Source-match correction and surviving new interface

Run: `20260924T043626Z-fleet03-B14-QFORM-auto11`.

This addendum is authoritative for the novelty/status labels in this run. The earlier `REPORT.md` mathematics remains valid, but two items initially developed there were found, on the required source search, to match earlier fleet results and therefore must **not** be presented as new results of this run.

## 1. Exact source match: definite physical pair

The ambient theorem

`||p_{X^T A X}||_{infinity,ess} <= pi/sqrt(det B)`

for a positive- or negative-definite physical `2x2` principal block `B`, with arbitrary outside couplings and conditioning-generated affine terms, is already proved as

`QFORM-DEFINITE-PHYSICAL-PAIR-v1`

in fleet02/B06:

`yspennstate/math-open-problems@43eab33dc9cd6063c84089b5fc3692abceeadb21`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T113045Z-d47192d10a82/REPORT.md`.

That source also already gives the delocalized Hadamard obstruction showing the bare three-large-eigenvalue condition need not produce any definite physical pair. Hence the physical-pair corollary in this run is a rederivation/control, not a new theorem.

## 2. Exact source match: opposite-sign slope/remainder barrier

The mechanism that an opposite-sign transverse square plus a bounded-density random slope can be exactly Schur-cancelled by a correlated remainder is already recorded in the live correction

`QFORM-INDEFINITE-INNOVATION-ARBITRARY-REMAINDER-FALSE-v1`

from fleet03/B06, canonical source

`yspennstate/math-open-problems@eb5cd7bd244d799988b7fa618280b46713bd13c8`.

Its family `X^2-epsilon Y^2+2CY-C^2/epsilon` includes the same mechanism as the `W^2-U^2+UZ-Z^2/4` control developed in this run. The latter remains a useful explicit check but is not a new correction.

## 3. Surviving supporting lemma: arbitrary overlap in a same-sign two-square compiler

What survives as the useful mathematical contribution of this run is the following interface, which is stronger in form than the physical-pair statement because the first square's center may depend **arbitrarily measurably** on the same transverse variable used by the second square.

### `QFORM-OVERLAP-SAME-SIGN-SQUARE-COMPILER-v1`

Let `W,U,Z` be mutually independent. Assume `W,U` have densities bounded by `K_W,K_U`. Let `a,d` be nonzero and have the same sign. For arbitrary measurable functions `Phi(U,Z)`, `theta(Z)`, and `R(Z)`, define

`T = a (W+Phi(U,Z))^2 + d (U+theta(Z))^2 + R(Z)`.

Then `T` is absolutely continuous and

`boxed: ||p_T||_{infinity,ess} <= pi K_W K_U / sqrt(|a d|).`

No support, tail, fragment, diameter, moment, smoothness, connectedness or translation parameter appears.

### Proof

Reflect the output if necessary and assume `a,d>0`. Conditional on `(U=u,Z=z)`, translation of `W` preserves its density cap, and the square pushforward has the pointwise envelope

`p_{a(W+Phi(u,z))^2}(v) <= K_W /(sqrt(a) sqrt(v)) 1_{v>0}`.

Fix `z` and an output point `q`, put `s=q-R(z)`. Averaging over `U` gives

`p_{T|Z=z}(q)
 <= K_W/sqrt(a) * int p_U(u) 1_{d(u+theta(z))^2<s}/sqrt(s-d(u+theta(z))^2) du`.

For `s<=0` this is zero. For `s>0`, use `p_U<=K_U`, translate `u`, and calculate exactly

`int_{|v|<sqrt(s/d)} dv/sqrt(s-dv^2)=pi/sqrt(d)`.

Thus

`p_{T|Z=z}(q) <= pi K_W K_U/sqrt(ad)`

uniformly in `z,q`. Averaging over `Z` proves the theorem.

The constant is sharp for this abstract compiler: take `a=d=1`, `Phi=theta=R=0`, and independent `W,U~Unif[-1/2,1/2]`. For `0<s<1/4`, the disk `{w^2+u^2<=s}` lies inside the unit square, so `P(W^2+U^2<=s)=pi s`, and the output density equals `pi` there.

### Random same-sign slope is zero-tax

If an additional random affine slope is present,

`dU^2 + D(Z)U = d(U+D(Z)/(2d))^2 - D(Z)^2/(4d)`,

so it is absorbed into `theta(Z)` and `R(Z)` without any density-cap assumption on `D(Z)`. Therefore the same bound survives **arbitrary** random slope translations whenever the retained transverse curvature has the same sign as the first square.

This is the exact same-sign successor to the preceding run's random-slope receiver. The live fleet03/B06 correction shows why no corresponding arbitrary-remainder assertion can hold on the opposite-sign branch.

## 4. Actual partner application

The designated fleet04/B14 r10 theorem is pinned at

`yspennstate/math-open-problems@deb713bc8e6df3f7e0ac5398e8cccbf00d1e7513`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B14/20260924T001624Z-fleet04-B14-scaled-schur-localization-r10/REPORT.md`.

For

`A_*=[[2,1,0],[1,2,0],[0,0,-1]]`,

`spec(A_*)={3,1,-1}` and the positive physical pair has determinant three. The source-matched definite-pair theorem / new overlap compiler gives

`||p_Q||_infinity <= pi/sqrt(3)=1.8137993642342178...`.

The designated partner r10 theorem, applied to the same actual three-coordinate block, has `sigma=1` and gives

`||p_Q||_infinity <= 6sqrt(pi)=10.634723105433096...`.

Hence the concrete combined proved inequality is

`boxed: ||p_Q||_infinity <= min(pi/sqrt(3),6sqrt(pi))=pi/sqrt(3).`

This is a literal target-valid chamber, not a claim of the full theorem.

## 5. Status and next implication

Full QFORM remains `OPEN / NOT PROVED / NOT DISPROVED`. Full-target continuity remains open; this lemma proves essential boundedness/absolute continuity only.

The useful next structural question is no longer the already-solved definite-pair case. It is: after product-preserving elimination, can the third spectral resource force either (i) a same-sign two-square overlap compiler before reciprocal-pivot payment, or (ii) one of the fleet's already-certified grouped/physical-triple receivers? On the opposite-sign branch, the Schur-cancellation correction requires retaining genuine third curvature rather than only an affine slope.
