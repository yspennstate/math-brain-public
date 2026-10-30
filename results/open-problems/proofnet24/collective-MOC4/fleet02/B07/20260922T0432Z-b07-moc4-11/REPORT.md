# MOC4 fleet02/B07 — one-cycle four-corner reserve bound

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex-normal `4 x 4` Marcus-de Oliveira target  
**Worker:** fleet02/B07  
**Candidate:** `MOC4-ONE-CYCLE-RESERVE-BOUND-v1`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** **OPEN / NOT PROVED / NOT DISPROVED**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Exact state consumed

The source-exact target is: for spectra `a_1,...,a_4`, `b_1,...,b_4` of complex normal matrices, and every true unitary `U`, prove

`det(diag(a)+U diag(b) U*)` lies in the convex hull of the 24 points

`v_sigma = product_i (a_i+b_{sigma(i)})`.

This run consumed the newest complete campaign-lead snapshot available at the scientific archive tip inspected in this invocation:

- fleet03/B07 `MOC4-V4-PAIR-GAP-CEILING-v1`, run `fleet03-B07-20260922T033411Z-d2a63b2a`, report blob `28cbce0f0a6213c0760e0777a5baa5b0de12b31a`. It proves the exact `V_4` fiber roof and pair-gap ceiling, leaving `MOC4-RESIDUAL-PR-RESERVE-v1` as the global strict-support residual.
- named partner fleet03/B08 `MOC4-ONE-CYCLE-SU2-ELLIPSE-v1`, run `20260922T031831Z-a03-b08-moc4-r11`, report blob `cd4264eb161c05fd44ff188490e4e0354295213c`. For a first-three-gate chain followed by a genuine closing `SU(2)` gate, it proves the exact ellipse formula and reduces target safety in a real-linear support direction `L` to

`C^2 <= delta0 delta1`, where `delta_j=M-L(D_j)` and `C=L(K)`.
- fleet03/B20 `MOC4-ONE-CYCLE-FACET-REDUCTION-v1`, shared handoff blob `edd88ca121ad663ac670a7bc86564ba0ba30e7cc`, which shows that for this ellipse it suffices to check exposed target-hull facet normals.
- fleet01/B08 `MOC4-CHAIN-CUBE-FACE-PROPAGATION-v1`, shared handoff blob `9fda0599857c5d32216b7337b73c3445cee5e380`, which shows that a low-frequency relaxation can violate the formal payment, while many simultaneous genuine spectral face ties force a common-circle locus already known safe.

The previous fleet02/B07 handoff `MOC4-ONE-CYCLE-NORMAL-CONE-v1`, blob `68fe642358a3779f98db3c779678e6bf5f4a5add`, supplied the two universal rank-two chord identities used below.

## 2. Setup and the exact endpoint weights

Use the fleet03/B08 first-three real Givens chain with

`A=c1^2`, `B=s1^2`, `u=c2^2`, `v=s2^2`, `r=c3^2`, `t=s3^2`,

so `A+B=u+v=r+t=1`. For a support functional `L`, put

`M=max_sigma L(v_sigma)`, `d_sigma=M-L(v_sigma)>=0`.

The two forest endpoints have exact deficits

`delta0 = sum_sigma w0_sigma d_sigma`, `delta1 = sum_sigma w1_sigma d_sigma`,

with nonzero weights

```
w0:
1234 Aur, 1243 Aut, 1324 Arv, 1423 Avt,
2134 Bur, 2143 But, 3124 Brv, 4123 Bvt;

w1:
1423 Bvt, 2413 But, 2431 Bur, 3421 Brv,
4123 Avt, 4213 Aut, 4231 Aur, 4321 Arv.
```

Let

`chi = L(v_4123-v_1423)=d_1423-d_4123`.

The partner theorem has

`C=c1 s1 s2 s3 chi`, hence

`C^2 = A B v t chi^2`.                                             (1)

The two exact spectral chord identities are equivalent, after applying `L`, to

`chi = d_1243-d_2143+d_2413-d_4213`,                       (2)

`chi = d_1324-d_3124+d_3421-d_4321`.                       (3)

No inverse matrix, determinant division, simplicity assumption, or nonzero spectral difference is used here.

## 3. New theorem — `MOC4-ONE-CYCLE-RESERVE-BOUND-v1`

Define the four-corner reserve contributions

`R0 = u r (A d_1234 + B d_2134)`,

`R1 = u r (B d_2431 + A d_4231)`.                           (4)

### Theorem

If `chi>=0`, then

```
delta0 delta1 >= min(
  (R0+A chi v t)       (R1+B chi (1-u r)),
  (R0+A chi (1-u r))   (R1+B chi v t)
).
```                                                            (5)

If `chi<=0`, writing `q=|chi|`, then

```
delta0 delta1 >= min(
  (R0+B q v t)         (R1+A q (1-u r)),
  (R0+B q (1-u r))     (R1+A q v t)
).
```                                                            (6)

Consequently each exposed-facet payment is certified whenever the right side of (5) or (6) is at least `A B v t chi^2`.

### Proof for `chi>=0`

From `d_1423-d_4123=chi` and nonnegativity,

`delta0 >= R0 + A chi v t + (the two bridge groups)`,

`delta1 >= R1 + B chi v t + (the two bridge groups)`.

For the first bridge put

`rho=d_1243-d_2143`, so by (2)

`chi-rho=d_2413-d_4213`.

Set `lambda=clip(rho/chi,0,1)` when `chi>0`. Directly from nonnegativity,

`A d_1243+B d_2143 >= A lambda chi`,

`B d_2413+A d_4213 >= B(1-lambda)chi`.                         (7)

The same argument applied to (3) gives some `mu in [0,1]` such that

`A d_1324+B d_3124 >= A mu chi`,

`B d_3421+A d_4321 >= B(1-mu)chi`.                             (8)

Therefore

`delta0 >= R0 + A chi F`,

`delta1 >= R1 + B chi G`,                                      (9)

where

`F = v t + u t lambda + r v mu`,

`G = v t + u t(1-lambda) + r v(1-mu)`.

Since

`F+G=v+t`, and `v t <= F <= 1-u r`,

we have `G=v+t-F`. The product

`(R0+A chi F)(R1+B chi(v+t-F))`

is a concave quadratic in `F`. Its minimum on the interval `[v t,1-u r]` is therefore attained at an endpoint. The two endpoint values are exactly the expressions in (5). The case `chi=0` follows directly, and (6) follows by applying the same argument to `-chi`, which swaps `A` and `B` in the directed bridge costs. QED.

## 4. Structural consequences

Combining (1) with (5)-(6) gives a singular-safe, facet-local sufficient test for the partner payment.

### All Givens-boundary cases are automatically safe

If any of `c1,s1,s2,s3` is zero then `C=0`. If instead `u r=c2^2 c3^2=0`, the two endpoint expressions in (5) or (6) reduce exactly to `A B v t chi^2`; hence the payment is nonnegative. Thus a strict one-cycle payment failure requires every first-three mixing factor to be genuinely interior.

### Four-corner collapse is necessary for failure

For `chi>0`, if either

`R0 >= A u r chi`  or  `R1 >= B u r chi`,                       (10)

then both endpoint expressions in (5) are at least `A B v t chi^2`. Hence payment failure forces simultaneously

`R0 < A u r chi`, `R1 < B u r chi`.                            (11)

When `u r>0`, this is equivalently

`A d_1234+B d_2134 < A chi`,

`B d_2431+A d_4231 < B chi`.                                   (12)

For `chi<0`, failure forces the swapped inequalities

`R0 < B u r |chi|`, `R1 < A u r |chi|`.                        (13)

Thus the unresolved one-cycle facet branch is not merely "payment close to zero": it must simultaneously collapse the two exact corner reserves relative to the interference chord. This is the nonlinear same-spectra regime to which the fleet01/B08 cross-ratio mechanism is relevant.

## 5. Exact applications and a necessary non-claim

The adjacent standard-library verifier `verify_reserve_bound.py` performs exact `Fraction` arithmetic on two source-valid spectral data sets.

### 5.1 Partner near-saturation datum

For fleet03/B08's retained exact spectra and

`(c1,s1)=(3/5,4/5)`, `(c2,s2)=(c3,s3)=(7/25,24/25)`,

the exact spectral hull has nine vertices

`4213,2143,2134,2431,2413,1423,1432,1234,1243`.

For all nine exposed edges, the reserve lower bound (5)-(6) is strictly positive after subtracting `A B v t chi^2`. The smallest exact reserve margin is

`158299673505299970564422605824 / 95367431640625 > 0`.          (14)

Hence the new theorem independently certifies the partner's **entire closing SU(2) ellipse in every support direction** for this near-saturation datum, including the closest facet.

### 5.2 The tempting universal reserve gate is false

It would be incorrect to promote "the reserve lower bound is nonnegative on every genuine spectral facet" as the missing theorem. Exact complex spectra

`a=(-4-i,-4-4i,2-6i,-4-6i)`,

`b=(-3+4i,5-3i,-1+2i,-5-3i)`,

with rational Givens pairs

`(24/25,7/25)`, `(5/13,12/13)`, `(21/29,20/29)`

have an actual exposed edge `4231--2431` for which the new reserve lower bound is strictly negative:

`-1197741650400867575808 / 505016316025 < 0`,                  (15)

while the **true** B08 payment remains strictly positive:

`193355269568346202280949888 / 24279630578125 > 0`.            (16)

So (5)-(6) is a rigorous localization/certificate, not a complete characterization. This exact source-valid datum refutes only the stronger proposed reserve-gate shortcut; it is not a MOC4 counterexample.

## 6. Conditional end-to-end route and first remaining implication

The campaign-level route remains:

1. use the campaign's support separation and boundary reductions;
2. use the lead's `V_4`/pair-gap ceiling to eliminate directions with no positive residual reserve;
3. use true-unitary flat/zero-face results and the singular-safe pair-Rayleigh conditions on maximizing representatives;
4. on the one-cycle closing fibers, use fleet03/B20's facet reduction and the theorem above to eliminate every exposed facet outside the explicit four-corner-collapse branch;
5. exclude the remaining genuine common-unitary branch. Then all support directions are bounded by the 24 endpoint maximum, and the repeated/singular cases follow by the already source-valid direct/continuity reductions.

The first global unpaid implication is still the lead's `MOC4-RESIDUAL-PR-RESERVE-v1`. This run proves a strict subcase and sharpens the first unpaid implication on the one-cycle component to:

> **`MOC4-ONE-CYCLE-COLLAPSE-RIGIDITY-v1` (OPEN).** For actual complex spectra and an exposed target-hull facet normal, prove the B08 payment `delta0 delta1-C^2>=0` on the residual branch where the four-corner reserve test (5)-(6) does not already certify it, using the same-spectrum cross-ratio/common-unitary geometry; or produce exact data with strict reverse payment. By `MOC4-ONE-CYCLE-SU2-ELLIPSE-v1`, strict reverse payment would immediately be a genuine true-unitary MOC4 counterexample.

The exact residual example in (15)-(16) shows that this implication cannot be replaced by the stronger false claim that the reserve lower bound itself is always nonnegative.

## 7. Degenerate cases and status

The theorem is polynomial/inequality algebra in the endpoint values and nonnegative support deficits. It does not divide by `det(A+B)`, spectral gaps, the chord `chi`, or edge lengths. Therefore singular determinant values and repeated spectra are included directly; `chi=0` and Givens-boundary cases are harmless. If later generic facet arguments normalize by an edge difference, their repeated/degenerate limits still require the campaign's existing continuity treatment, but no such normalization is used in this theorem.

- `MOC4-ONE-CYCLE-RESERVE-BOUND-v1`: **proved**.
- B08 near-saturation full closing ellipse: **certified again, now by the reserve theorem on all nine exposed edges**.
- universal nonnegative reserve-lower-bound shortcut: **refuted by exact genuine spectral data**, without refuting MOC4.
- `MOC4-ONE-CYCLE-COLLAPSE-RIGIDITY-v1`: **open**.
- full MOC4: **open**.

No arbitrary bistochastic surrogate, benchmark material, credentials, scheduler identifiers, machine-local paths, unrelated private data, email/Drive data, paid model/API/Codex, remote workflow, public release, or permission bypass was used.
