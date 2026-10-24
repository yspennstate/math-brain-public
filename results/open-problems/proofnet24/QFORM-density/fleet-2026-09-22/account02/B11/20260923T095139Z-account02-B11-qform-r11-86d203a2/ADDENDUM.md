# account02/B11 addendum — operator-stable four-bank crosscut

Status: `SUPPORTING_STABILITY_COROLLARY / SOURCE_REVIEW_PENDING / FULL_QFORM_OPEN`.

After the main report was written, I applied the current owner-required volume-stability result at

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,
`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

That source proves: if an ORIGINAL-coordinate cross block `M=M0+E` has `s3(M0)>=a0`, maximum range leverage of `M0` at most `1/2`, and `||E||op<=a0/16`, then the full ambient quadratic-plus-affine form has a continuous density with

`||p_Q||_infinity < 23/a0`,

while all within-bank curvature, outside couplings and affine terms remain arbitrary. The perturbation is kept inside the Fourier argument; it is not treated as a small random quadratic error.

## Corollary — `QFORM-WALSH-CROSSCUT-OP-STABILITY-v1`

Use the balanced four-bank frame and the equal sign-class cut `I,J` from Proposition 4.1 of the main report, with `n=8m>=16`. Let

`M0 = R_I diag(a,b,c) R_J^T`,
`mu=min(|a|,|b|,|c|)>0`,

and suppose the ACTUAL physical cross block is

`A_IJ=M0+E`,
`||E||op <= mu/32`.                                                   (A1)

No assumptions are made on `A_II`, `A_JJ`, outside-coordinate blocks or affine terms. Then

`boxed: ||p_Q||_infinity < 46/mu.`                                    (A2)

**Proof.** With `U=sqrt(2)R_I`, `V=sqrt(2)R_J`,

`M0=(1/2)U diag(a,b,c)V^T`.

Hence

`s3(M0)=mu/2`.                                                        (A3)

Its range projection is `UU^T`, whose diagonal entries are the row leverages

`||U_i||^2=6/n<=3/8<1/2`.                                            (A4)

Take `a0=mu/2` in the source theorem. Condition (A1) is exactly `||E||op<=a0/16`. Therefore

`||p_Q||_infinity <23/a0=46/mu`. QED.

This is a genuine matrix-level robustness statement. It does NOT claim that `X^T E X` is small on unbounded inputs.

## Application to the account03/B11 r26 target family

For the partner family,

`a=(1-2delta)n`, `b=delta n`, `c=-delta n`, `0<delta<1/4`,

so `mu=delta n`. In the target-valid range `delta(n-2)>=1`,

`mu=delta n >= n/(n-2)>1`.                                           (A5)

Consequently any arbitrary cross-block perturbation satisfying

`||E||op <= delta n/32`                                               (A6)

is paid uniformly by

`boxed: ||p_Q||_infinity <46/(delta n)<46,`                           (A7)

with arbitrary same-side self curvature and outside couplings.

Thus the explicit four-bank obstruction is stable under a target-scale dense cross perturbation. What remains is structural: show that a general balanced no-fixed-packet survivor admits such a growing cut (perhaps after choosing the correct banks), or force a different already-paid exit.

The source volume-stability theorem itself is marked independent-review pending; this corollary inherits that review status.
