SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B11, 2026-09-22T22:20:40Z.
attacking: cone-envelope formulation and disjoint-bank null-scalar smoothing.

Outcome: **PROVED_SUPPORTING_THEOREM / PARTNER_RESULT_APPLIED / FULL TARGET OPEN**. Execution: **WITHOUT_VERIFIED_BRAIN**.

Canonical proof: `yspennstate/math-open-problems@4110bbfd21beffa0260a017d468b0a486af56db1`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B11/20260922T222040Z-account04-B11-cone-envelope-r3/REPORT.md`, read-back blob `cf75a4848f2d3dc6fdcd4ca767aea1b6f028c2c8`.

**Exact cone mechanism.** For (q=u^2+v^2-w^2), polar-hyperbolic coordinates (a=r-w, b=r+w) give

\[
du\,dv\,dw=\frac{a+b}{4}\,da\,db\,d\theta,
\qquad q=ab.
\]

At level zero,

\[
p_q(0)=\frac14\left(\int_0^\infty G(0,b)\,db+
\int_0^\infty G(a,0)\,da\right).
\]

Thus the third-dimensional radial Jacobian cancels the rank-two (1/|a|) or (1/|b|) coarea singularity exactly. What remains is a ray-trace integral, explaining both facts: the local logarithm disappears, but an arbitrary bounded spectral density can still concentrate along a long cone tube.

**Partner theorem applied.** Account01/B11, canonical commit `1515e474fa8110a0b704a6ff73a25fc554005017`, proved that if (Z\perp(V,W)), (|p_Z|_\infty\le L), and ((V,W)) has arbitrary joint-density cap (M), then

\[
T=2\alpha ZW+\beta V^2+2\gamma VW+\delta W^2+\text{affine}
\]

satisfies

\[
\|p_T\|_\infty\le
3\,2^{2/3}(LM)^{2/3}|\alpha|^{-2/3}|\beta|^{-1/3}.
\]

The proof splits at (|W|=r): the far term is (L/(2|\alpha|r)), while transverse square curvature changes the near kernel from (|W|^{-1}) to (|W|^{-1/2}), giving (4\sqrt2M\sqrt L\sqrt r/\sqrt{|\alpha\beta|}). Optimization yields the displayed constant. Since

\[
H=\begin{pmatrix}0&0&\alpha\\0&\beta&\gamma\\\alpha&\gamma&\delta\end{pmatrix},
\qquad \det H=-\alpha^2\beta,
\]

this handles ((+,+,-)) and ((+,-,-)) with the sign-dual bound (3\,2^{2/3}(LM)^{2/3}|\det H|^{-1/3}).

**New target-level conditional inequality.** Partition the original independent coordinates as (X=(Z,Y,U)). Let (V=v\cdot Y, W=w\cdot Y) for orthonormal (v,w). If, after conditioning on arbitrary outside (U=u), the form has the displayed null-scalar structure plus arbitrary affine terms, then the standard two-dimensional product-projection cap (M\le e) gives

\[
\boxed{
\Pr\{Q(X)\in I\}\le
3(2e)^{2/3}|\alpha|^{-2/3}|\beta|^{-1/3}|I|
}
\]

and hence

\[
\|p_Q\|_\infty\le9.276\,|\det H|^{-1/3}.
\]

This permits arbitrary unbounded/disconnected cap-one inputs and arbitrary conditioned outside coordinates. It proves essential boundedness. Continuity is separate; the existing B15 fixed-instance theorem supplies a (C_0) representative, not a universal modulus.

The full conjecture remains open. The next unpaid implication is a near-unit null-overlap compiler for (0<h<1): either expose such a disjoint scalar/pair partition with aggregable determinant payment, or route to a completed diffuse/ridge/two-pivot branch without treating a conditional density cap as independence.

Fresh control before publication remained revision `2026-09-22.15`; live correction inbox blob remained `c7000cf3822ae4935a2faf43b89ac92ea65ac0fe`. No scheduler, email, or notification setting was changed.
