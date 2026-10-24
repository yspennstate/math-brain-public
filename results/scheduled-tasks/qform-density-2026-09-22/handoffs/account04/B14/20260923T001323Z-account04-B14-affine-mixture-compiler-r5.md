SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B14, 2026-09-23T00:13:23Z.
attacking: zero-loss conditional localization for physical-fibre and ruled estimates, with singular-core kernel leakage explicit.

Status: SUPPORTING TARGET-LEVEL THEOREMS PROVED; FULL QFORM OPEN; continuity separate; WITHOUT_VERIFIED_BRAIN.

New theorem: if an interval estimate for

u^T B u + l^T u + c

is uniform over every affine parameter l,c and every smooth cap-one product law on a fixed original-coordinate block, then conditioning and mollifying only that block transfers the estimate with exactly the same constant to arbitrary cap-one product laws, arbitrary outside tails/fragments and arbitrary outside couplings. A finite-mixture version shows it is enough to prove the affine-uniform estimate for finite-fragment indicator products; no unattained bathtub threshold is assumed.

The exact leakage identity is

u^TBu+l^Tu+c
=(u+(1/2)B^dagger l_R)^TB(u+(1/2)B^dagger l_R)
 + l_K^Tu+c-(1/4)l_R^TB^dagger l_R.

Thus only the range part can be translated away. For l(v)=a+2Cv, a sufficient no-leakage gate is P_Ker(B)a=P_Ker(B)C=0.

Applying completed account01/B14 r23 to an invertible physical 3x3 block B of signature (2,1), sigma_min_abs(B)>=sigma, gives

P{Q in J, Q>=tau(X_out)} <= (pi sqrt(2)/sigma)|J|,

where tau(v)=r(v)-(1/4)ell(v)^TB^-1ell(v), with arbitrary rough laws and outside couplings. This remains only the moving one-sheet part.

Applying the newest determinant-only physical-pair theorem gives, for an actual indefinite original-coordinate pair with D=|det B_2| and s=s_3(A),

||p_Q||inf <= D^-1/2[9.2+log_+(10000sqrt(D)/s)].

Hence if s>=1 and D>=delta,

||p_Q||inf <= delta^-1/2[9.2+log_+(10000sqrt(delta))].

The remaining gap is structural: s_3(A)>=1 need not force a universal delta; the ruled estimate leaves the two-sheet/convex complement; singular cores retain the displayed kernel term.

Canonical mathematics: yspennstate/math-open-problems@19d9434e07142e6b9fe19b4a88bbd46ccec8eeee, proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260923T001323Z-account04-B14-affine-mixture-compiler-r5/REPORT.md, blob 3af36c47726d1aabb2a9cb0281818d9d3bb3297c.

Source pins: newest Claude directory commit 2f3340cd21be3e8b1a0d3a738e1fa7b7c6b76926; source blobs RESULTS 56edacbd7aa105e7aaabfcfb6f377c268a134817, FOURIER 9da148eed6cd43b1046a6f91d0f9329e12921cb4, COUNTEREXAMPLE d11ace6dbf5ecdf6ce5921f80f727e92e95bf8fc; Claude-review correction blob 44ee51368aad3796beda43e15534087cd0b298fd; completed account01/B14 report blob 7908503d72472b58359c14e5011bcd65c0ba6a05.
