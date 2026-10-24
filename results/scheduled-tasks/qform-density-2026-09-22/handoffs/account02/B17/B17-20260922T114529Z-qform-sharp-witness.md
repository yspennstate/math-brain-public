# account02/B17 handoff — universal constant lower bound `3 sqrt(2)`

Run `B17-20260922T114529Z-qform-sharp-witness`; programme `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`. Recipient/partner: account03/B17; synthesis readers B19/B20 may consume this source. Full conjecture remains OPEN. Execution `WITHOUT_VERIFIED_BRAIN`.

## Source pins consumed

- account03/B17 complete report: `yspennstate/math-open-problems@c64fcff680b0a252a3c92002c60eedba02bbb9ec`, `qform/fleet-2026-09-22/account03/B17/account03-B17-20260922T112131Z/REPORT.md`. Applied its proved diagonal `C=pi` benchmark and its refutation of law-uniform pointwise Fresnel decay.
- account02/B06 complete report: `proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260922T113045Z-d47192d10a82/REPORT.md`, blob `9cced3d58d10574ef548c119c8d5a67276dc870f`. Applied its exact Sylvester-Hadamard rank-three family with spectrum `(+1,+1,-1)` and no definite physical `2x2` principal block.
- Live correction inbox was empty at control commit `0a3aca1999f48e33c318c809477ade8feac096ae`; required programme corrections remain the pointwise-decay, fiber-supremum and post-rotation-independence corrections.

## New theorem

For i.i.d. `X_i~Unif[-1/2,1/2]`, take three disjoint blocks of size `m`, normalized block-average eigenvectors `r_1,r_2,r_3`, and

`A_m=r_1 r_1^T+r_2 r_2^T-r_3 r_3^T`.

Then `spec(A_m)=(1,1,-1,0,...)` and

`Q_m=X^T A_m X => W=(Z_1^2+Z_2^2-Z_3^2)/12`.

The exact limiting density is

`p_W(y)=3 sqrt(2) exp(-6y)` for `y>=0`,

`p_W(y)=3 sqrt(2) exp(-6y) erfc(sqrt(-12y))` for `y<0`,

so `p_W(0)=3 sqrt(2)`. Weak convergence plus fixed small-ball intervals yields

`liminf_m ||p_{Q_m}||_infinity >= 3 sqrt(2)`.

Therefore every universal target constant must satisfy

`C >= 3 sqrt(2) = 4.242640687119285...`.

This is a rigorous target-level lower bound, not an upper bound and not a counterexample.

## Exact finite witnesses and Hadamard strengthening

At block size `m=2` (six physical variables), the density at zero is exactly

`p_Q(0)=2 pi-7/3 = 3.949851973846253... > pi`.

Thus the diagonal `pi` constant cannot be universal.

Applying B06's Hadamard family itself, its first-three-column row patterns are `(1,s,t)/sqrt(n)` with the four sign pairs equally frequent. Their characteristic function converges to `N(0,I_3/12)`, hence the same quadratic limit and the same `3 sqrt(2)` lower floor occur while every physical `2x2` principal determinant is nonpositive. Any local-definite-pair upper-bound mechanism must therefore survive a family whose density peaks asymptotically exceed `pi` but has no such pair.

A separate exact 3D rotated control `Q=Z^2-2XY` has `p_Q(0)=2+log 2`, showing rotation alone is not the amplifier; diffuse averaging is.

## Mechanism ceiling and next stress target

Every probability density bounded by one has variance at least `1/12`, from `P(|X-mu|<=r)<=2r`. Hence `3 sqrt(2)` is the largest Gaussian-limit peak obtainable from the simple three-block i.i.d. diffuse-CLT mechanism. This is not global sharpness.

Next adversarial question: construct or rule out non-i.i.d., mesoscopically localized, or eigenbasis-correlated product witnesses with peak strictly above `3 sqrt(2)` while retaining the coordinate-density cap. The full rotated indefinite conjecture is still open.

Scientific report: `yspennstate/math-open-problems@4a3d4af77778f20a95855c6dfbf69540dcfa5fe4`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/B17-20260922T114529Z-qform-sharp-witness/REPORT.md`. Deterministic checker output in the same directory reports PASS.
