# QFORM exact-rank-three arbitrary-affine volume-sampling bound

**2026-09-23; scoped new theorem; full conjecture remains open.**

For independent cap-one coordinates (X_i), symmetric **exact rank three** (A) with (s_3(A)\ge\sigma>0), and unrestricted affine (b,c), prove
\[
 \|p_{X^TAX+b^TX+c}\|_\infty<51(n-2)/\sigma.
\]

Full self-contained proof and constants: https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/QFORM-density/interactive/20260923T193238Z-exact-rank-three-affine/REPORT.md (commit bfd9de120db53ccf212a90deb5d6486c3c0f7674).

Core identity: write (A=U\Lambda U^T), (U^TU=I_3). Volume-sample physical triples (I) by (w_I=\det(U_I^TU_I)). Cauchy–Binet yields (\sum_Iw_I=1) and
\[
 \sum_I\operatorname{tr}\operatorname{adj}(U_I^TU_I)=3(n-2).
\]
Thus some invertible physical triple has (s_{\min}(U_I)^2\ge[3(n-2)]^{-1}); by inverse factorization (s_{\min}(A_{II})\ge\sigma/[3(n-2)]), valid for every inertia. Condition all coordinates outside (I), then a three-physical-coordinate lemma gives density (<17/s_{\min}(A_{II})) uniformly over conditional affine coefficients. It handles null affine leakage, which the rank-three projection-density route does not automatically handle.

The (<17/\tau) lemma uses a Gaussian bound inside a ball around the critical point, giving (3e^{1/2}\sqrt{2\pi}Rh/\tau) for an interval of length (h), and on its complement one of three original derivatives is (\ge2\tau R/\sqrt3), giving (3\sqrt3h/(\tau R)). Optimize (R).

**Strict scope:** Exact rank three. Higher-rank indefinite terms may cancel the principal triple; the argument does not give a dimension-uniform theorem. A homogeneous/range-affine spectral projection localization provides (O(n^{3/4})/\sigma) for exact rank three but does not directly address null affine terms. Independent audit of constants and rank assumptions completed.
