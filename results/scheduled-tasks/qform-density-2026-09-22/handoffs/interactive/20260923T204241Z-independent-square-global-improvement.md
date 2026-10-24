# Stronger all-level receiver for a physical independent square component

Status: source-pinned rigorous scoped theorem, full QFORM open.

The previous 20:37 handoff supplied a bound only at central levels. The [new addendum](https://github.com/yspennstate/math-open-problems/blob/1a79f3525d40fef2baf7a1d19d2614f2b786bc49/proofnet24/QFORM-density/interactive/20260923T203741Z-independent-v-square-product-band/GLOBAL_LEVEL_ADDENDUM.md), read back at the pinned commit, proves the stronger **all-target** estimate.

For original-product orthonormal leaf forms L,V,P, physical independent cap-one H, and
\[
Q=2HL+\beta L^2+V^2+2\epsilon LP,
\]
suppose the original-coordinate support of V contains indices T unused by both L and P, with \(\rho=\|v_T\|_2>0\). Then
\[
\|p_Q\|_\infty\le\frac{8+3\sqrt2/2}{\rho}<\frac{10.13}{\rho}
\]
for arbitrary real beta,epsilon and any overlap among L,P,V outside T. The conclusion is global in the target value, not restricted to \((-1,0)\).

Key correction: setting U=H+beta L/2+epsilon P, independence and f_H≤1 give \(p_{L,U}(l,u)\le p_L(l)\), i.e. \(U|L=l\) has density ≤1, not merely p_{L,U}≤√2. For arbitrary center c and 0<t≤1,
\[
\Pr\{c<2LU<c+t\}\le t(2K+K\log(1/t)+1/2),\quad K=\|p_L\|_\infty.
\]
This logarithmic product band is integrable against an independent square component's \(t^{-1/2}\) kernel, proving \(\|p_Q\|_\infty\le B(4K+3/2)\), where B bounds that component's density. Product marginal caps give K≤√2 and B≤√2/rho.

This does **not** cover fully overlapping V with rho=0, any arbitrary-rank matrix, or the whole conjecture. It gives a quantitative original-coordinate gate that future structural decompositions can use without a target cutoff.
