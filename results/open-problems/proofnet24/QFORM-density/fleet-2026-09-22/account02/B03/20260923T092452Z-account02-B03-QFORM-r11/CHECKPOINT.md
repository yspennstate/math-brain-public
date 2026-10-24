# B03 checkpoint: collision-to-density saddle splice

Run `20260923T092452Z-account02-B03-QFORM-r11`.

Fresh designated-partner input: account03/B03 r29 proves, for its exact angular-cancellation packet `T`,

\[
\int_{\mathbb R}|\phi_T(t)|^2\,dt < \frac{54.27326850232713}{s},\qquad s=s_3(A_T)>0.
\]

Hence `T` has an `L^2` density and

\[
\|p_T\|_2^2 < \frac{8.637858959899031}{s}.
\]

For independent cap-one `U,V` and arbitrary shifts `alpha,beta`, the previously proved sharp-Young product packet gives

\[
\|p_{c(U+\alpha)(V+\beta)}\|_2^2\le \frac{3\sqrt3}{|c|}.
\]

Therefore, whenever this saddle packet is independent of the r29 packet (or conditionally independent after conditioning only outside original coordinates), Young/Cauchy-Schwarz gives

\[
\|p_{T+c(U+\alpha)(V+\beta)}\|_\infty
<\sqrt{8.637858959899031\,3\sqrt3}\,(s|c|)^{-1/2}
=6.699524741463198\,(s|c|)^{-1/2}.
\]

Thus the collision certificate becomes a genuine one-copy linear small-ball estimate on this product-preserving branch. No conjugate sum/difference variables are separated or declared independent.

Pinned Claude-package exit also retained: if any disjoint physical cross block has fifth volume `Z_5=e_5(M^T M)>0`, Theorem D5 at commit `e5f71d79eff325201dd0274053d20268ce65b837` gives

\[
\|p_Q\|_\infty\le 5\sqrt{2e}\,Z_5^{-1/10}.
\]

So the remaining structural collar after this checkpoint must simultaneously escape D5 and fail to expose an independent saddle packet of controlled coefficient next to the exact-cancellation core.
