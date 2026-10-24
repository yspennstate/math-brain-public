SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B17, 2026-09-23T12:03:07Z.
attacking: an unpaid low-total-tail/rank-two-cross stress family; derive a sharp analytic cap-one reduction and a uniform limiting density bound.

# Early substantive checkpoint

Take
\[
A_m=[1]\oplus J_m/m\oplus(-J_m/m).
\]
Its nonzero spectrum is exactly \(\{1,1,-1\}\).  For every disjoint original-coordinate cut \(I,J\), the cross block \(A_m[I,J]\) has rank at most two: the singleton block contributes no cross entry and each of the two \(J_m/m\) banks contributes rank at most one.  Hence the newest volume-stability certificate has \(s_3(M)=0\), \(E_3(M^TM)=0\), and collective tail \(T_2=0\) on every cut.  This is therefore an exact source-valid stress family in the still-unpaid low-cross-rank/low-total-tail class.

With independent centered unit-interval variables in the two banks,
\[
Q_m=X_m^2+S_m^2-T_m^2,
\qquad S_m=m^{-1/2}\sum_{k=1}^mU_k,\quad T_m=m^{-1/2}\sum_{k=1}^mV_k,
\]
where the heavy coordinate \(X_m\) may have an arbitrary density \(0\le f_m\le1\).

The first essential inequality is the sharp square-density estimate.  If \(H=X_m^2\) has density \(h_m\), then
\[
h_m(u)\le u^{-1/2},\qquad \|h_m\|_{3/2}\le2.
\]
Indeed \(\int h_m^{3/2}\le E|X_m|^{-1/2}\le\int_{-1/2}^{1/2}|x|^{-1/2}dx=2\sqrt2\).

Let \(v=1/12\).  The completed account04/B17 weighted local Edgeworth theorem implies that the square density of \(S_m\) converges in \(L^{3/2}\) at rate \(O(m^{-1})\) to the square density of \(G\sim N(0,v)\).  Consequently the density \(k_m\) of \(S_m^2-T_m^2\) converges in \(L^3\) to
\[
k_v(t)={1\over2\pi v}K_0\!\left({|t|\over2v}\right),
\]
the product-normal density of \((G-H)(G+H)\).  Young's inequality then gives, uniformly over the arbitrary heavy law,
\[
\limsup_m\|p_{Q_m}\|_\infty\le 2\|k_v\|_3
=2\left[{1\over2\pi^3v^2}\int_0^\infty K_0(r)^3dr\right]^{1/3}.
\]
At \(v=1/12\) this exact Bessel constant is numerically about \(5.05391617\) (diagnostic only; finiteness follows analytically from the standard logarithmic/exponential behavior of \(K_0\)).

Next step in this run: prove the \(L^{3/2}\to L^3\) transfer carefully, derive the exact bathtub extremizer for the heavy coordinate at each output level, and compare with the completed account04/B17 lower bound \(C_*\ge3\sqrt2\).