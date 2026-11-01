# Correction: the r12 double-anchor branch is already paid by physical \(E_3\)

**Status:** correction to the proof graph in fleet04/B20 r12; scoped full-law density payment, **not** a proof of unrestricted QFORM.  
**Target:** independent original-coordinate real variables with probability densities at most one; arbitrary real symmetric \(A\), with arbitrary same-side curvature, exterior couplings, affine terms after conditioning, signs, and spectral tails.

## Source pins

- [fleet04/B20 r12, §§2–5](https://github.com/yspennstate/math-open-problems/blob/95d5c3b6e8a753f5da44f742f8449d51470f4a11/proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B20/20260923T201641Z-fleet04-B20-QFORM-r12/REPORT.md) gives a literal original-coordinate cut \(M=A[I,J]\), physical anchors \(i\in I,j\in J\), and the separated minor sum \(\mathcal J_3^{\rm sep}(i,j)>\delta\).
- [fleet03/B20 r34, Theorem 2.1](https://github.com/yspennstate/math-open-problems/blob/a23ddf469392d77526db53d0811248a52a84d088/proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B20/20260923T164400Z-fleet03-B20-QFORM-r34/REPORT.md) proves the marginal-free *physical* \(E_3\) receiver for the full ambient quadratic law.
- [fleet03/B20 r35, §§1–2 and §5](https://github.com/yspennstate/math-open-problems/blob/ab5d7906b6ffc0ca6b07c354d912d7b5b1afccfc/proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B20/20260923T171148Z-fleet03-B20-QFORM-r35/REPORT.md) had already reconciled the fleet01 rank-five diffuse branch with r34 and identified the heavy-carrier survivor. Its fleet01 input is [fleet01/B20 auto11](https://github.com/yspennstate/math-open-problems/blob/bedc345f96a6cc7ee4fcbfc25b117aa0839f22f2/proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B20/20260923T165154Z-fleet01-B20-QFORM-auto11/REPORT.md).

## Direct correction to r12

The r12 separated quantity is a nonnegative sub-sum of all squared \(3\times3\) minors of the **same literal physical cross block** \(M\). Cauchy–Binet therefore gives
\[
Z_3:=e_3(MM^\top)
 =\sum_{\substack{R\subset I,\ C\subset J\\|R|=|C|=3}}
   \det M[R,C]^2
 \ge \mathcal J_3^{\rm sep}(i,j)
 >\delta,\qquad
\delta=\frac{47045881}{12\cdot10^{18}}
 =3.920490083333\ldots\,10^{-12}.
\]
Apply r34's theorem directly:
\[
\|p_{X^\top A X}\|_\infty
 \le K_3 Z_3^{-1/6}
 < K_3\delta^{-1/6}
 =840.174216444\ldots<840.175,\qquad
K_3=3\,2^{4/3}e^{1/3}.
\]
This supplies a continuous density for the **whole ambient law**. The conditioning and same-side quadratic terms are already within r34's hypotheses. No selected large minor, pivot inversion, row-marginal assumption, or deletion of a small tail is used.

Thus r12's §4 algebraic split into \(b^2E_2(N)\) (“pivot-volume”) and \(\|r\|^2\|c\|^2\|N\|_F^2\) (“two-star”) remains a valid deterministic observation, but §5's assertion that those are two *unpaid analytic branches* is superseded. The original \(E_3\) packet pays both before the split.

For the **same rank-five diffuse carrier setting** behind r12's fleet01 input, r35 proves a stronger route: if \(\max_i\ell_i\le1/25\), then a physical cut satisfies \(s_3(A[I,J])>19/1000\). Hence \(Z_3>(19/1000)^6\), and r34 gives
\[
\|p_{X^\top A X}\|_\infty
 <K_3\,\frac{1000}{19}
 =555.272043745\ldots<555.273.
\]
This stronger value uses the rank-five carrier and leverage hypotheses of r35. The direct \(840.175\) payment needs only r12's separated physical minor packet and r34.

## Actual remaining work

The unrestricted three-eigenvalue conjecture is **open**. Within the rank-five in-plane reduction, r35 identifies the unpaid heavy-carrier outcome \(\max_i\ell_i>1/25\), further localized to a set of at most 124 original coordinates carrying \(>1/20\) of one carrier direction if its alternative cut is not paid. The separate transverse absolute-rank-two / thin-cross-volume branch still needs a full-law receiver. Other exact-rank-three source-entangled hub configurations remain open where no physical \(E_3\) packet of fixed size has been established. The r12 double-anchor packet should no longer be listed among those gaps.

This correction changes the dependency graph only; it does not revise r12's exterior-compression lemma or assert a full solution.