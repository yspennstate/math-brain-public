SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B05, 2026-09-23T06:39:32Z.
attacking: QFORM-INTERPACKET-ESCAPED-THIRD-CURVATURE-COAREA-v1, specialized by the newest owner source to the unpaid indefinite two-sheet / near-parallel packet transition.

# Early substantive checkpoint

Programme: QFORM-DENSITY-3EIG-20260922. Full conjecture remains OPEN. Execution: WITHOUT_VERIFIED_BRAIN.

## First essential implication

Use the ratio-variance packet normal form from
`yspennstate/math-open-problems@b0299facc04ea0c03276dddb1a12c027aed5a946:proofnet24/QFORM-density/fleet-2026-09-22/account01/B05/20260923T033640Z-account01-B05-QFORM-r26/REPORT.md`.

After conditioning the complement, one original-coordinate packet G gives orthonormal product projections S,R and two disjoint scalar-bank variables Y,Z. Put

- m = sum_{i in G} u_i^2 > 0;
- sigma^2 = sum_{i in G}(t_i-r u_i)^2;
- B = the invertible indefinite quadratic matrix on (Y,Z);
- D=|det B| and kappa=sigma_min(B);
- the Schur remainder over B is lambda [[m,0],[0,0]] in (S,R);
- mu = D |lambda|.

The key observation is that **sigma does not enter the post-completion quadratic remainder**. In original product coordinates X_G it is exactly

`R_G = lambda*m*(u_G/sqrt(m) dot X_G)^2 + b_G dot X_G + c`,

with an arbitrary affine vector b_G (which may contain the whole R-direction). Therefore the rank-one affine small-ball lemma from
`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f:proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`
applies directly, WITHOUT conditioning on R:

`sup_t P(|R_G-t|<rho) <= min(1,10 sqrt(rho/(|lambda|m))).`

The scalar projections Y,Z have density caps at most sqrt(2). Rescale both by sqrt(2), so their caps become one and the pair matrix becomes B/2. Hence

`D' = D/4`, `kappa' = kappa/2`, and `D' kappa' = D kappa/8`.

The pair-log theorem then yields

`||p_Q||_infty <= 8*2^(3/4)*sqrt(5) * (D*kappa*|lambda|*m)^(-1/4)`

and therefore

`boxed(||p_Q||_infty <= 8*2^(3/4)*sqrt(5) * (mu*kappa*m)^(-1/4)).`

Numerical prefactor: `8*2^(3/4)*sqrt(5)=30.0848247447...`.

This bound is **independent of the ratio-variance residual sigma**. Thus the nonzero near-parallel residual itself is not the missing analytic factor. The only degeneration in this receiver is the physical scalar-pair singular scale kappa.

Using the packet lemma with h=1 gives m>=3/20, hence the concrete branch estimate

`||p_Q||_infty <= 48.3421 * (mu*kappa)^(-1/4).`

## Designated partner application

The completed designated partner account04/B05 result is
`yspennstate/math-open-problems@59c6ff7db9aceb8b575abe0e064ebeda06f6f77f:proofnet24/QFORM-density/fleet-2026-09-22/account04/B05/20260923T041255Z-account04-B05-dominant-slope-r2/REPORT.md`.
It proves that an exact slope atom of u-mass m_* gives

`||p_Q||_infty < 51.6 (mu*m_*)^(-1/3)`

with no kappa cost. For the actual inequality `mu>=1` and `m_*>=1/4`, this gives

`||p_Q||_infty < 51.6*4^(1/3) < 81.91`,

uniformly even as kappa tends to zero.

Together, the two receivers isolate the remaining two-sheet packet debt as the **nonatomic / no-exact-slope, kappa->0 branch**. Small nonzero sigma is no longer itself a loss.

## Newest-Claude exit actually applied

The required volume-stability theorem at
`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba:proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`
says that for an original-coordinate cross block M=M0+E with
`s3(M0)>=a`, `max diag(P_range(M0))<=1/2`, and `||E||op<=a/16`, the full ambient form has a continuous density `<23/a`.

Applying it with the actual threshold a=1/4 closes every such two-sheet survivor by

`||p_Q||_infty < 92`,

with continuity. Therefore the unpaid kappa->0 packet branch may additionally be restricted to configurations for which every candidate a=1/4 near-diffuse cross certificate fails at least one of the stated matrix gates.

This checkpoint is a supporting branch reduction, not a proof of full QFORM and not a continuity proof outside the volume-stability exit.
