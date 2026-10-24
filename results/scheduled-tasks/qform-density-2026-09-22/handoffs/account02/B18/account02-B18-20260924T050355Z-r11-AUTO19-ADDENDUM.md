SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B18, 2026-09-24T05:03:55Z.
attacking: latest-partner refresh after account03/B18 auto19 arrived; apply its aggregate Hilbert--Schmidt bilinear/private-square theorem to the same target stress family and sharpen the remaining structural bridge.

Status: FULL QFORM OPEN / NOT PROVED / NOT DISPROVED. Execution: WITHOUT_VERIFIED_BRAIN.

A newer compatible designated-partner report arrived after this run's main report/handoff were already committed: account03/B18 auto19, scientific commit `7308d156465db33641b1db6e8609777b832c5da2`, PASS check `bc79736952c7095dde0944018c4d5ba45e79673a`. It now supersedes auto18 as the latest partner for this invocation.

Auto19 proves source-valid bilinear concentration extremality (Juškevičius--Lee plus Hu--Paouris), then

`sup_t E|X^T M Y-t|^(-1/2) <= K_HP ||M||_HS^(-1/2)`

and for a genuinely private original scalar square

`||p_(X^T M Y+aW^2+dW+c)||inf <= K_HP/sqrt(|a| ||M||_HS)`.

Apply it to the run's target family

`Q_N=2(N-1)^(-1/2)sum_{j=1}^N X_jY_j+2UV+W^2`, `N>=5`.

Condition on original U,V. Then `M=2(N-1)^(-1/2)I_N`, `a=1`, so

`||M||_HS=2 sqrt(N/(N-1))`

and

`||p_QN||inf <= [K_HP/sqrt(2)]((N-1)/N)^(1/4) < K_HP/sqrt(2)`.

The required pinned e5f D5 theorem applied to the same physical cut gives `<23.843`, hence

`||p_QN||inf <= min{[K_HP/sqrt(2)]((N-1)/N)^(1/4),23.843}`.

The account02 RV rank-one-tail theorem from the main report remains complementary rather than superseded: it permits arbitrary same-bank `G(Y)` and Y-dependent aligned square shift `h(Y)W`, while auto19's aggregate-HS theorem is stronger in the cleaner pure bilinear-plus-private-square scope.

The sharpened first unpaid implication is `QFORM-TWOSIDED-OVERLAP-OR-AGGREGATE-HS-EXIT-v1`: force either an auto19 clean HS/private-square packet, the broader one-sided account02 packet with `A_II=A_Iw=0` and `|A_ww|S_1(A_IJ)>=c`, or an aggregate Theorem-F/projected-crossing/D5/grouped-hub/physical-pair exit. The harmonic exact-rank-three frame in the main report rules out requiring a sparse/private spectral eigenvector.

Math addendum: `yspennstate/math-open-problems@4e5f0a5011833adba70b9c5a9b2b989245ba3902`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B18/account02-B18-20260924T050355Z-r11/LATEST_PARTNER_ADDENDUM.md`, read back.
