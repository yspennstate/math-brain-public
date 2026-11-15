# Checks and attempted counterexamples

The analytic proof, not the finite calculation, establishes the theorem.

1. **Two-point constant, second derivation.** In the unsaturated case set `b=a-u`, `c=2a-v`. Then `2b-c=v-2u`. Cauchy–Schwarz gives `||2u-v||^2 <= 5(||b||^2+||c||^2)`, independently of completing the square in PROOF.md. Also `u1>=7/16` and `v1<=9/16`, so `2u1-v1>=5/16`. This independently gives `5/256`. The scalar choice `u=7/16`, `v=9/16`, `a=5/16` attains that value without saturation. This sharpness statement concerns the two-point inequality, not the integrated constant.

2. **Clipping.** If `||a||>=1/2`, the second projected output has norm exactly one, whereas every posterior mean has norm at most `9/16`. The error is at least `49/256`. This includes the boundary. If `||a||<1/2`, both projections are identities. In higher dimensions, radial projection cannot evade the argument by placing weight in other coordinates, because saturation fixes the full output norm to one.

3. **Posterior support, second derivation.** The posterior is a probability measure on a convex ball, so its barycenter lies in that ball. Alternatively, take the supremum over unit vectors `v` of `E[v dot (X0-mu) | Xt=x]`; each such expectation is at most `1/16`. This gives the norm bound without relying on the triangle-inequality calculation in the proof.

4. **Noise normalization.** Solving the linear SDE gives `Xt=e^(-t) X0 + sqrt(2) int_0^t e^(-(t-s)) dBs`. The conditional covariance is `2 int_0^t e^(-2(t-s)) ds I=(1-e^(-2t)) I`. This checks (1) independently of the named OU convention. On the selected regions, `t>=1/2`, so `2h>1`; the exponent bound is `(1/16+9/16)^2=25/64<1`. The Gaussian prefactor is bounded below, since `h<1`.

5. **Region and constant.** There are `d` spatial side lengths `1/(32 sqrt(d))` and one time side length `1/4`. Dilating each of the `d+1` coordinates by two multiplies volume by `2^(d+1)`. The two shifted-time intervals have disjoint interiors. Multiplying the density floor, rectangle volume and pair bound gives the displayed `C_d`; the script independently compares the product with the simplified formula in dimensions 1, 2, 3 and 5.

6. **Moving time endpoints.** The proof uses physical times between `1/2` and `2`, uniformly for `T0 in [0,1/2]`. It survives `T0 -> 0` and `T=O(log N)` and gives a floor of order `1/log N`. It does not silently assume a fixed lower diffusion cutoff. The endpoint `t=0` itself is never used.

7. **Score versus denoiser.** The weight `h^2/alpha^2` cancels the score prefactor exactly. The excess DSM identity is a conditional-expectation orthogonality identity; it is not a claim that the full denoising loss should vanish. The unweighted bound uses only the selected regions, where the prefactor is at least `e^(-4)`. No reverse implication from score error to total-variation sampling error is asserted.

8. **Architecture escape routes.** An output bias, hidden bias, constant input coordinate, or suitable nonhomogeneous time embedding invalidates (2). A separate network at each time also need not obey (2). The result does not apply to these classes. Output clipping radius one is explicit; choosing a different radius requires new analysis. The compactly supported smooth bump is non-Gaussian and lies strictly inside the unit ball, so the declared radius is a valid, possibly loose, support bound.

9. **Relation to the cited theorem.** The displayed architecture and projection were checked in both the arXiv HTML and PDF. The homogeneous-kernel corollary follows from its own displayed definition. This does not establish that every hypothesis of the paper's conditional training theorem is satisfied by the counterexample; in particular its separate sample Gram-eigenvalue assumption has not been verified. The approximation obstruction itself does not use such an assumption.

10. **Numerical checks and resource use.** `audit_obstruction.py` used exact rational arithmetic for 9,225 identity/clipping checks and 1,025 scalar interval-distance checks. The grid includes the exact minimizing scalar `5/16`. These checks are finite and do not substitute for the all-input proof. Its recorded nice value was 20, `OMP_NUM_THREADS` was 1, peak RSS was 14,745,600 bytes on macOS, and user CPU time was about 0.16 seconds. An attempted RLIMIT_DATA setting failed twice and was removed; the audit is a tiny standard-library calculation with a 30-second CPU cap.
