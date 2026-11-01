# fleet03/B06 — curved-fiber integration

**Run:** `20260922T114507Z-fleet03-B06-qform-curved-fiber-v1`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Status:** `SUPPORTING_LEMMA_PROVED / FULL_CONJECTURE_OPEN`  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`

## 1. Fresh control and scope

The later owner control supersedes the FEI prompt attached to this scheduled invocation. The active target is the quadratic-form bounded-density conjecture:

> For independent real random variables `X_1,...,X_n` with probability densities `0 <= f_i <= 1`, and every real symmetric `A` having at least three eigenvalues of absolute value at least one, prove that `Q=X^T A X` has density bounded by one universal constant, or give a valid counterexample.

The live B06 assignment is **Curved fiber integration**: retain ellipse/hyperbola geometry inside spectral fibers, avoid the dimension-losing operation `int sup_fiber`, and prove a weighted replacement.

Current corrections were consumed. In particular, law-uniform pointwise quadratic Fourier decay is false under only `f_i<=1`, and the unrestricted spectral-fiber supremum can grow linearly in dimension.

## 2. Peer dependency actually applied

A current peer result used in this derivation is fleet01/B05,

`qform/fleet-2026-09-22/fleet01/B05/20260922T1136Z-qform-principal2d-B05-r1/REPORT.md`

(blob `09383b90fdc49dcb3479c4ea6ede0b58994bfd8b`). It supplies two decisive tests:

1. a definite original-coordinate `2 x 2` principal block gives the sharp shell estimate `pi/sqrt(|det B|)` after conditioning;
2. for `F=1_[0,1]^n` and a flat Walsh two-plane `E`, the naive mixed norm
   `int_{E^perp} sup_{y in E} F(z+y) dz`
   equals `n/2` and therefore cannot be used in a dimension-free proof.

The assigned fleet04/B06 partner did not yet have a compatible completed QFORM handoff visible at publication time. No partner PASS or result is fabricated. The B05 Walsh stress family is instead used below as an actual adversarial check of the new mechanism.

## 3. New theorem: elliptic-energy L^p compression

### Theorem `QFORM-ELLIPTIC-ENERGY-LP-COMPRESSION-v1`

Let `E` be any two-dimensional subspace of `R^n` with an orthonormal basis `e_1,e_2`. Let `a,b>0`, and for

`y = u e_1 + v e_2`

define the positive definite fiber energy

`q_E(y) = a u^2 + b v^2`.

Let `F:R^n->[0,infinity)` be any probability density with `0<=F<=1`; in the target problem one has `F(x)=prod_i f_i(x_i)`, hence these hypotheses hold automatically. For `z in E^perp` and `s>0`, define the unnormalised energy pushforward

`H(z,s) = int_E delta(s-q_E(y)) F(z+y) dy`.

Then for every `1 <= p < infinity`,

`int_{E^perp} int_0^infinity H(z,s)^p ds dz
 <= pi^(p-1) (ab)^(-(p-1)/2) int_{R^n} F(x)^p dx
 <= pi^(p-1) (ab)^(-(p-1)/2).`

Equivalently,

`||H||_p <= pi^(1-1/p) (ab)^(-(1-1/p)/2) ||F||_p.`

At the endpoints,

`||H||_1 = 1`

and

`||H||_infinity <= pi/sqrt(ab) <= pi`

when `a,b>=1`.

In particular,

`int int H(z,s)^2 ds dz <= pi/sqrt(ab).`

This estimate is dimension free, is valid for an arbitrarily oriented spectral plane `E`, and never replaces a curved fiber by its unrestricted maximum before integration.

### Proof

Write

`alpha=sqrt(a) u`, `beta=sqrt(b) v`

and

`W_z(alpha,beta)=F(z+(alpha/sqrt(a))e_1+(beta/sqrt(b))e_2)`.

Then `dy=dalpha dbeta/sqrt(ab)` and `q_E=alpha^2+beta^2`. Polar coordinates give the exact identity

`H(z,s) = 1/(2 sqrt(ab)) int_0^(2pi) W_z(sqrt(s) cos theta, sqrt(s) sin theta) dtheta.`

For `1<=p<infinity`, Jensen/Hölder on the circle yields

`(int_0^(2pi) W_z dtheta)^p <= (2pi)^(p-1) int_0^(2pi) W_z^p dtheta.`

Hence

`int_0^infinity H(z,s)^p ds`

`<= (2 sqrt(ab))^(-p) (2pi)^(p-1)
    int_0^infinity int_0^(2pi) W_z(sqrt(s)omega_theta)^p dtheta ds.`

With `s=r^2`, so `ds=2r dr`, the final double integral equals

`2 int_{R^2} W_z(alpha,beta)^p dalpha dbeta`

`= 2 sqrt(ab) int_E F(z+y)^p dy.`

All constants cancel to

`int_0^infinity H(z,s)^p ds
 <= pi^(p-1)(ab)^(-(p-1)/2) int_E F(z+y)^p dy.`

Integrating `z` and using the orthogonal decomposition `dx=dy dz` proves the first bound. Since `0<=F<=1` and `int F=1`, `int F^p<=1`, proving the second.

For `p=infinity`, the same polar identity gives directly

`H(z,s) <= [1/(2sqrt(ab))] 2pi ||F||_infinity = pi/sqrt(ab)`.

For `p=1`, integration of the delta pushforward preserves total mass, so `int H=1`. QED.

### Sharpness of the operator constant at this level

For a radial amplitude on the spectral plane, the circular Jensen step is equality. Thus the factor `pi^(1-1/p)(ab)^(-(1-1/p)/2)` is the natural exact constant for this unrestricted positive-amplitude operator; improving the full theorem must exploit additional structure beyond this two-dimensional energy compression.

## 4. Integrated Fourier corollary

Define the fiber characteristic slice

`Psi(z,tau) = int_E exp(i tau q_E(y)) F(z+y) dy`.

By the definition of `H`,

`Psi(z,tau)=int_0^infinity exp(i tau s) H(z,s) ds`.

With the convention `hat h(tau)=int exp(i tau s)h(s)ds`, Plancherel and the `p=2` theorem give

`int_{E^perp} int_R |Psi(z,tau)|^2 dtau dz
 = 2pi int_{E^perp} int_0^infinity H(z,s)^2 ds dz`

`<= 2 pi^2 / sqrt(ab) <= 2 pi^2`

whenever `a,b>=1`.

So although the current correction ledger rules out a law-uniform **pointwise** `|tau|^(-1/2)` estimate, the same two same-sign large spectral directions always supply a law-independent, dimension-free **integrated L^2 oscillatory payment**. This is a genuinely different quantity and does not contradict the phase-alignment counterexample.

## 5. Why this repairs the Walsh fiber-sup failure

In the flat Walsh/cube stress family from fleet01/B05, the bad operation

`int_{E^perp} sup_{y in E} F(z+y) dz`

is exactly `n/2`.

The theorem replaces that operation by the actual elliptic level average before the complement is integrated. For the same cube density and the same arbitrarily oriented plane,

`||H||_infinity <= pi/sqrt(ab)`

and

`||H||_2^2 <= pi/sqrt(ab)`,

independently of `n`. Thus the dimension loss identified by B05 is not intrinsic to the curved fiber itself; it is created by discarding the level geometry through a fiber supremum.

This is the requested weighted replacement in a precise form.

## 6. Exact remaining bridge to the full conjecture

Among three eigenvalues with absolute value at least one, two have the same sign. Choose those two eigenvectors for `E`; write their eigenvalues as `sigma a, sigma b`, with `sigma in {+1,-1}` and `a,b>=1`. Orthogonal invariance of `A` gives

`Q(z+y)=q_perp(z)+sigma q_E(y)`.

The output density, at the formal coarea level and equivalently as a pushforward identity, is the graph trace

`p_Q(t)=int_{E^perp} H(z, sigma(t-q_perp(z)))
        1_{sigma(t-q_perp(z))>=0} dz.`

The new `L^p(E^perp x R_+)` estimates do **not by themselves** control this graph trace: an `L^p` function in the ambient `(z,s)` variables can concentrate near a codimension-one graph, and `E^perp` has unbounded volume. Therefore claiming the full theorem from the displayed `L^2` estimate would be invalid.

The third large eigenvalue must now be spent on a **trace/Carleson/transversality estimate for this special energy-pushforward H**, not on a generic continuity inequality and not by reintroducing the forbidden fiber supremum. A concrete sufficient next statement would be a dimension-free bound of the form

`sup_t int_{E^perp} H(z, sigma(t-q_perp(z))) dz <= C`

using that `q_perp` contains at least one eigenvalue of magnitude at least one and that `H` comes from a product density through the exact circular-average operator above.

A localized consequence illustrates the gap cleanly. For any measurable `Omega subset E^perp` of finite volume and interval `I` of length `eta`, Hölder gives

`P(Q in I, z in Omega)
 <= pi^(1-1/p)(ab)^(-(1-1/p)/2) (eta |Omega|)^(1-1/p)`.

The uncontrolled quantity is therefore precisely the effective complement volume/trace geometry, not the two-dimensional elliptic shell.

## 7. Status and next step

**Proved:** `QFORM-ELLIPTIC-ENERGY-LP-COMPRESSION-v1`, including exact constants and the dimension-free integrated Fourier `L^2` corollary.

**Applied peer failure:** the B05 Walsh example shows the theorem avoids a real `n/2` loss that kills the naive fiber-sup route.

**Not proved:** the full quadratic-form conjecture. The next decisive obligation is a trace estimate that spends the third large spectral direction while retaining the joint `(z,s)` structure of `H`. A promising exact target is to condition/decompose along that third eigenvector and prove a one-dimensional curved-graph trace inequality against the circular-average kernel, rather than bounding `H` pointwise and integrating over all `z`.

No FEI result, full QFORM proof, partner PASS, or native brain ingestion is claimed.
