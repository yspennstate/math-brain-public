# Handoff — B16 first-hit two-scale curvature reduction

**Execution:** WITHOUT_VERIFIED_BRAIN  
**Full FEI:** OPEN / NOT PROVED.

The common-order first-hit covariance now has the exact decomposition
\[
\sum_v\operatorname{Var}(W_v)
=\sum_v\int_0^1\operatorname{Var}_{\mathrm{Ber}(t)}(\partial_vC)dt
+\sum_v\operatorname{Var}_{t\in[0,1]}\partial_vC(t\mathbf1).
\]
For relation supports `A,B`, with `r=|A|`, `s=|B|`, `h=|A cap B|`, `u=|A cup B|`, the two PSD kernels are
\[
K_{int}=h(1/u-1/(r+s-1)),
\qquad
K_{rad}=h(1/(r+s-1)-1/(rs)).
\]
They sum to the inherited centered-Jaccard kernel. The signed coefficients remain inside each covariance, so negative R32 credits are preserved.

Universal product-Bernoulli and weighted-uniform Poincare inequalities give
\[
K(C)\le
\int t(1-t)\sum_{v\ne u}E_t(\partial_{uv}C)^2dt
+\frac12\int t(1-t)\sum_v(\sum_{u\ne v}\partial_{uv}C(t\mathbf1))^2dt.
\]
Thus the aggregate selector problem reduces to an internal mixed-curvature square bank plus a one-dimensional signed moment bank.

Do **not** try to absorb the radial bank generically into the internal bank. The explicit all-positive triple-star family `R_{ij}={0,i,j}` has
\[
K_{int}=d^2(d-1)/10,
\qquad
K_{rad}=d(d-1)^2(d+4)/45,
\]
so their ratio is `2(d-1)(d+4)/(9d) ~ 2d/9`. This is a route obstruction, not an FEI counterexample; admissibility as a complete Boolean/R32 coefficient family is not claimed.

For the inherited genuine `q=3`, overlap-two `+1/8,-1/8` diagnostic, the negative covariance refund splits exactly as
\[
5/576=1/320+1/180
\]
(internal plus radial), showing that the radial channel itself carries useful negative-credit cancellation.

**Next target:** insert the authentic Borel R32 coefficients into the radial moment polynomial
\[
m_v(t)=\sum_{A:v\in R_A}c_A t^{q_A-1}
\]
and compare its variance to the existing alternating R16 first-separation/moment reservoir, while keeping the terminal response only as its authorized signed endpoint. In parallel, identify the internal mixed-derivative square bank with the existing noisy-square/plaquette capacity without double-spending negative credits.

See `REPORT.md`, `check_first_hit_two_scale.py`, `check_output.json`, `check_radial_star_obstruction.py`, and `radial_star_output.json` in this folder.
