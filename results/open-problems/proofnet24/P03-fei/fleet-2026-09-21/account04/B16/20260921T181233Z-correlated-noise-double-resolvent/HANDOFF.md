# B16 handoff — correlated-noise double-resolvent current

Full unrestricted FEI remains **OPEN / NOT PROVED**. Execution: **WITHOUT_VERIFIED_BRAIN**.

For the signed paired parity field
\[
\Phi(S)=\sum_{R:\ |R|\text{ odd}} b_R\chi_R(S),
\]
let `q_R=|R|`, let `k_R` be the number of clone pairs hit oddly, and let `r_R=(q_R-k_R)/2` be the number hit twice. The existing parity-current frame energy is
\[
\mathcal E_{cur}=2\sum_R\left(\frac1{q_Rk_R}-\frac1{q_R^2}\right)b_R^2.
\]

Define ordinary fine noise `N_x` by `N_x chi_R=x^{q_R} chi_R`. Define a pair-correlated flip operator `C_{y,lambda}` by giving each clone pair flip bits with marginal flip probability `(1-y)/2` and interpolating from independent flips (`lambda=0`) to perfectly coupled pair flips (`lambda=1`). Its Walsh eigenvalue is
\[
y^{k_R}[y^2+\lambda(1-y^2)]^{r_R}.
\]
Writing `B_y=C_{y,1}`, the new exact identity is
\[
\boxed{
\mathcal E_{cur}
=2\int_0^1\!\int_0^1\frac{\langle\Phi,N_x(B_y-N_y)\Phi\rangle}{xy}\,dx\,dy.
}
\]
Moreover `partial_lambda C_{y,lambda}` is PSD frequency by frequency, so this endpoint gap is a positive correlation-flow integral, not an endpoint `L2` estimate.

If
\[
D_j=(I-\tau_{j0})(I-\tau_{j1})
\]
is the XOR four-point curvature on clone pair `j`, then
\[
\boxed{
\mathcal E_{cur}
=\frac18\int_0^1\!\int_0^1\!\int_0^1
\frac{1-y^2}{xy}
\sum_j
\langle D_j\Phi,
N_x C_{y,\lambda}^{(j)}D_j\Phi\rangle
\,d\lambda\,dy\,dx.
}
\]
Every integrand is nonnegative. Both inverse-number factors are retained exactly; singleton syndrome is killed because it has no doubled pair. Negative R32 credits have already cancelled inside the signed `b_R` before the square. In the live retained field, the `D_d` terminal subtraction remains inside `Phi`, so this identity does not separately spend the terminal bank.

The central small-resolvent subbank obtained by restricting `x,y<=1/2` has frequency multiplier
\[
\varepsilon_{q,k}
=2\frac{2^{-q}}q\left(\frac{2^{-k}}k-\frac{2^{-q}}q\right),
\]
and obeys the sharp bound
\[
\boxed{
\varepsilon_{q,k}\le\frac{11}{192}\left(1-\frac1q\right),
}
\]
with equality at `(q,k)=(3,1)`. Thus the genuinely central piece costs at most `11/192` of the Ward refinement bank frequency by frequency; the high/endpoint complement remains unspent for the R16/moment and terminal mechanisms.

Exact checker status: PASS — 80 pair-law eigenvalue checks, 24 direct signed operator checks, 24 curvature-square checks, 820 full multiplier checks, 820 central-truncation checks. Checker SHA-256 `352ff99acd661ead8c6d1b15d99e5bad8878f037c2cca0749c8b71fc8b14f8d6`.

**Next attack:** substitute the exact retained Borel/MacWilliams potential into one central term
\[
\langle D_j\Phi,N_xC_{y,\lambda}^{(j)}D_j\Phi\rangle
\]
and push this already-squared signed clone-pair curvature through the dependent-q-flip Radon/original-cut identity. Start with `x,y<=1/2`; do not touch the endpoint/terminal complement unless the central physical multiplier is controlled. If the authentic R32 field violates the desired original-coordinate bound, preserve the counterexample and change route; do not fall back to unit-weight q-flip frames, one-resolvent transport, generic endpoint `L2`, or unsigned relation sums.
