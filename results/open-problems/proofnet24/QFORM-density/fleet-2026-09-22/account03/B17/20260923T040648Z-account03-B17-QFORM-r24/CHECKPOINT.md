# Early substantive checkpoint — compound-Poisson fragmented three-bank witness

Run `20260923T040648Z-account03-B17-QFORM-r24`.

I changed mechanism after the preceding mixed-leverage runs and attack the finite-row local-spike escape left open by the infinitesimal-frame Gaussian theorem.

Fix the designated partner's exact rotated matrix

\[
B=O^T\operatorname{diag}(1,1,-1)O,
\qquad
O={1\over7}\begin{pmatrix}6&-2&-3\\-2&3&-6\\-3&-6&-2\end{pmatrix}.
\]

For bank `j`, put `p_{j,m}=alpha_j/m` and use the exact cap-one density

\[
f_{j,m}=1_{[-(1-p_{j,m})/2,(1-p_{j,m})/2]}
+1_{[b_j\sqrt m-p_{j,m}/2,b_j\sqrt m+p_{j,m}/2]}.
\]

For all large `m` the intervals are disjoint, total support length is one, and the physical target matrix is unchanged, hence every finite member still has exact nonzero spectrum `{1,1,-1}`.

For the normalized bank sum `Y_{j,m}=m^{-1/2}\sum_{k=1}^mX_{jk}`, the characteristic function is

\[
\Phi_{j,m}(t)=\left[(1-p)sinc\!\left({(1-p)t\over2\sqrt m}\right)
+p e^{ib_jt}sinc\!\left({pt\over2\sqrt m}\right)\right]^m,
\]

and for fixed `t`

\[
\Phi_{j,m}(t)\to
\exp\left(-{t^2\over24}+\alpha_j(e^{ib_jt}-1)\right).
\]

Thus the candidate bank limit is `G_j+b_jN_j`, where `G_j~N(0,1/12)` and `N_j~Poisson(alpha_j)` are mutually independent.

The substantive missing step at this checkpoint is finite-to-limit local control at the cone tip. The route is to prove `L1` convergence of the bank characteristic functions, hence uniform convergence and uniform `Linf` bounds for the bank densities, then combine compact-radius coarea convergence with a uniform second-moment tail bound along the cone. If this closes, the previous exact noncentral-Gaussian cone-tip inequality gives the strict limit penalty

\[
p_{Q_\infty}(0)
\le3\sqrt2\left[1-	frac12(1-e^{-A})(1-e^{-6b_*^2})\right]<3\sqrt2,
\]

where `A=sum_{j:b_j!=0} alpha_j` and `b_*=min_{j:alpha_j>0,b_j!=0}|b_j|`.

Newest volume-stability source will also be applied to the partner witness's balanced physical split: for even `m`, the three nonzero singular values of that cross block are all `1/2`, and the range-projection diagonal is `2/m`; hence the peer-tail volume exit gives the explicit but nonsharp bound `9 sqrt(3) e` on the full ambient density for `m>=4`.

Status at checkpoint: proof route identified; full QFORM remains open.
