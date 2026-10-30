SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B04, 2026-09-23T18:24:51Z.
attacking: heavy-row rotated cross blocks: optimize three-volume currency, apply the pinned fifth-volume bound, and compare both with the partner projected-crossing hub certificate and direct ridge gates on the same physical matrix.

# Early substantive checkpoint

Let

\[
V=I_5-\frac25\mathbf 1\mathbf 1^T,
\qquad D_L=\operatorname{diag}(L,1,1,1,1),
\qquad M_L=D_LV,
\quad L\ge1.
\]

Since \((\mathbf1\mathbf1^T)^2=5\mathbf1\mathbf1^T\), one has \(V^2=I_5\).  Every diagonal entry of \(V\) is \(3/5\), every off-diagonal entry is \(-2/5\), so every physical coefficient of \(M_L\) is nonzero.  The singular values of \(M_L\) are exactly \(L,1,1,1,1\).

For the symmetric physical matrix

\[
A_L=\begin{pmatrix}0&M_L\\M_L^T&0\end{pmatrix},
\]

the spectrum is \(\{\pm L,\pm1,\pm1,\pm1,\pm1\}\).  Hence this is a genuinely non-diagonal indefinite target family with ten eigenvalues of modulus at least one.

The pinned Claude/e5 fifth-volume theorem applies to the full cross block because

\[
Z_5=e_5(M_L^TM_L)=L^2,
\]

and gives the actual inequality

\[
\|p_{X^TA_LX}\|_\infty\le5\sqrt{2e}\,L^{-1/5}.
\]

The pinned q=1 third-volume theorem, even with arbitrary supported weights, has an exact support obstruction on the same block: every probability law on physical 3x3 minors has row marginals summing to three, but there are only five physical rows, so they cannot all be at most one half.

For the partner projected-crossing route, take physical row 1 as a one-coordinate hub.  Its coefficient row is \(L v_1\), while rows \(v_2,\dots,v_5\) are orthonormal and perpendicular to \(v_1\).  Thus the projected residual crossing has four orthonormal rows.  For ell=2 all six positive pair Gram determinants equal one.  The uniform pair law has every marginal exactly one half and

\[
\Gamma_*=\exp\{-4(1/2)\log(1/2)\}=4.
\]

The fleet03/B04 arbitrary-weight projected-crossing theorem therefore gives

\[
\|p_{X^TA_LX}\|_\infty
\le 3\,2^{5/6}L^{-1/3}.
\]

The remaining calculation in this run is to solve the admissible third-volume entropy optimization exactly and compare it with the completed ridge theorem on this identical physical matrix.
