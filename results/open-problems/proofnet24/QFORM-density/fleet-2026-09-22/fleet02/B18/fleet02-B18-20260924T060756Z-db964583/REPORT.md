# fleet02/B18 — Hilbert–Schmidt moving-private-square fusion

Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: **PROVED SUPPORTING THEOREM / FULL QFORM OPEN**  
Continuity: proved in the stated fused scope by the latest fleet03/B18 theorem; not claimed for the unrestricted target.

## First unpaid implication

The bare hypothesis `s_3(A)>=1` still does **not** force a source-separated packet consisting of a bilinear original-coordinate cross bank plus a genuinely private square. The live structural debt remains extraction of such a packet, or a different already-paid exit, while retaining two-sided overlap and same-bank curvature. The result below pays a larger analytic subcase once the private square is present: its center may move with the shared `Y` bank, while the cross smoothing is paid at Hilbert–Schmidt rather than operator-norm scale.

## 1. New theorem: `QFORM-HS-MOVING-DIFFUSE-SQUARE-v1`

Let `X in R^m`, `Y in R^n`, and `Z in R^k` be three pairwise-disjoint banks of ORIGINAL coordinates. Assume every scalar coordinate in the three banks is independent and has a probability density bounded by one. Let `M` be a nonzero real `m x n` matrix, `beta in R^k\{0}`, `a!=0`, `c in R`, and let `H:R^n->R` be arbitrary measurable. Put

\[
T=X^T M Y+a\bigl(\beta^T Z+H(Y)\bigr)^2+c.
\]

Write

\[
K_\beta=\|p_{\beta^T Z}\|_\infty,
\qquad H_M=\|M\|_{HS},
\qquad \sigma_M=\|M\|_{op}.
\]

Then `T` has a continuous density vanishing at infinity and

\[
\boxed{
\|p_T\|_\infty
\le {K_\beta\over\sqrt{|a|}}
\min\left\{
{K_{HP}\over\sqrt{H_M}},
{8\over\sqrt{\sigma_M}}
\right\}.}
\tag{1.1}
\]

Here `K_HP` is the universal source constant from fleet03/B18 auto19,

\[
K_{HP}=C\bigl[e^c+2C''(c+1)e^{-c}\bigr],
\]

where `c,C,C''` are the universal constants in Hu–Paouris Theorem 1.1. No unsupported numerical value is assigned to it. The sharp one-dimensional bounded-density theorem of Rudelson–Vershynin gives

\[
K_\beta\le {\sqrt2\over\|\beta\|_2},
\]

so

\[
\boxed{
\|p_T\|_\infty
\le {\sqrt2\over\|\beta\|_2\sqrt{|a|}}
\min\left\{
{K_{HP}\over\sqrt{\|M\|_{HS}}},
{8\over\sqrt{\|M\|_{op}}}
\right\}.}
\tag{1.2}
\]

The second branch, together with continuity, is exactly the latest completed partner theorem fleet03/B18 auto20 specialized to `alpha=0` and `G=0`. The first branch is the new fusion.

## 2. Proof of the Hilbert–Schmidt branch

Set

\[
B=X^T M Y,
\qquad U=\beta^T Z.
\]

Because `Z` is an original-coordinate bank disjoint from `X,Y`, `U` is independent of `(X,Y)`. We use no independence among spectral projections of a common bank.

For fixed `x,y`, let `h=H(y)` and `q=x^TMy+c`. Since `U+h` has density cap `K_beta`, the pushforward

\[
S_y=a(U+h)^2
\]

has density, on the appropriate half-line,

\[
g_y(s)\le {K_\beta\over\sqrt{|a|\,|s|}}.
\tag{2.1}
\]

Indeed every noncritical level has two preimages and each Jacobian has magnitude `2 sqrt(|a||s|)`. Crucially, the singular output value is **zero for every y**: moving the input center does not move the critical output of the completed square.

Therefore a regular conditional density of `T` given `(X,Y)=(x,y)` obeys

\[
p_{T\mid X,Y}(t)\le
{K_\beta\over\sqrt{|a|}}
|t-c-x^TMy|^{-1/2}.
\tag{2.2}
\]

Average (2.2) over the genuine original product banks `X,Y`:

\[
p_T(t)\le {K_\beta\over\sqrt{|a|}}
\mathbb E|X^T M Y-(t-c)|^{-1/2}.
\tag{2.3}
\]

Fleet03/B18 auto19 proves, by Juškevičius–Lee concentration rearrangement followed by Hu–Paouris tensor stochastic dominance and tensor small-ball estimates,

\[
\sup_s\mathbb E|X^T M Y-s|^{-1/2}
\le K_{HP}\,\|M\|_{HS}^{-1/2}.
\tag{2.4}
\]

Combining (2.3) and (2.4) gives

\[
\boxed{
\|p_T\|_\infty\le
{K_\beta K_{HP}\over\sqrt{|a|\,\|M\|_{HS}}}.}
\tag{2.5}
\]

No conditioning step converts a density cap into independence. The square shift `H(Y)` is allowed to share the full `Y` source with the bilinear term because only the **output critical value** of the square is used in (2.2).

The latest fleet03/B18 auto20 theorem applies to the same `T` and gives the independent operator-norm branch

\[
\|p_T\|_\infty\le {8K_\beta\over\sqrt{|a|\,\|M\|_{op}}},
\tag{2.6}
\]

and a continuous `C_0` representative. Taking the minimum proves (1.1), including continuity.

## 3. Primary-source match

The external hypotheses used above match the owner class exactly.

1. **Rudelson–Vershynin, Theorem 1.2.** If independent real variables have densities bounded by `K` and the coefficient vector has Euclidean norm one, their linear combination has density bounded by `sqrt(2) K`. Applied to `beta/||beta||_2` this yields `K_beta<=sqrt(2)/||beta||_2`. No moment, compact-support, log-concavity, iid, centering, symmetry, or smoothness assumption is imposed.

2. **Juškevičius–Lee, Theorem 1.** For independent summands with prescribed density caps, every small-set probability for their sum is dominated by the corresponding centered-uniform summands. In dimension one it is uniform in the interval center. This is used inside auto19 only after freezing the other ORIGINAL bank.

3. **Hu–Paouris, Theorems 1.1 and 1.3.** Their bounded-density tensor theorem assumes independent component vectors whose coordinates are independent and density-capped; Theorem 1.3 gives stochastic dominance on symmetric convex bodies by centered cube factors. Auto19 applies it only to the scalar bilinear tensor slab and obtains (2.4). No general quadratic-form extremality is inferred.

Thus the fusion adds no hidden moment/support/log-concavity condition and makes no post-rotation independence claim.

## 4. Genuine owner-target family with a shared moving square

Let `0<epsilon<1`, `N>=0`, and let `X=(X_0,...,X_N)`, `Y=(Y_0,...,Y_N)` be disjoint original-coordinate product banks. Let `Z` be a third disjoint bank and let `beta` be any unit vector on that bank. Put

\[
U=\beta^T Z,
\]

and define

\[
Q_{N,\varepsilon}
=4\sqrt3\,X_0Y_0
 +2\varepsilon\sum_{j=1}^N X_jY_j
 +3\left(U+\sqrt{2/3}\,Y_0\right)^2.
\tag{4.1}
\]

On the physical three-dimensional span generated by the `X_0` direction, the `Y_0` direction, and the unit `beta` direction, the symmetric matrix is

\[
A_0=
\begin{pmatrix}
0&2\sqrt3&0\\
2\sqrt3&2&\sqrt6\\
0&\sqrt6&3
\end{pmatrix}.
\tag{4.2}
\]

Its characteristic polynomial is

\[
\lambda^3-5\lambda^2-12\lambda+36
=(\lambda+3)(\lambda-2)(\lambda-6).
\tag{4.3}
\]

The remaining `N` disjoint cross pairs contribute eigenvalues `+epsilon,-epsilon`. Hence

\[
\boxed{
\operatorname{spec}_{\ne0}(A_{N,\varepsilon})
=\{-3,2,6\}\cup\{+\varepsilon,-\varepsilon\}^{N}.}
\tag{4.4}
\]

Thus for every `0<epsilon<1`, every `N`, every choice of the unit vector `beta`, and every allowed rough product law, (4.1) has **exactly three** eigenvalues of modulus at least one. The moving square genuinely shares the original `Y_0` source with the bilinear term; no rotated-coordinate independence is asserted.

For (4.1),

\[
M=\operatorname{diag}(4\sqrt3,2\varepsilon,\ldots,2\varepsilon),
\]

so

\[
\|M\|_{op}=4\sqrt3,
\qquad
\|M\|_{HS}=2\sqrt{12+N\varepsilon^2}.
\tag{4.5}
\]

Since `||beta||_2=1`, the fused theorem gives the whole-line bound

\[
\boxed{
\|p_{Q_{N,\varepsilon}}\|_\infty
\le
\min\left\{
{K_{HP}\over \sqrt3\,(12+N\varepsilon^2)^{1/4}},
{8\sqrt2\over\sqrt{12\sqrt3}}
\right\}.}
\tag{4.6}
\]

The explicit auto20 branch is

\[
{8\sqrt2\over\sqrt{12\sqrt3}}
=2.481612957605599\ldots.
\tag{4.7}
\]

The first branch retains the moving `Y_0` square center while aggregating **all** bilinear cross energy through the Hilbert–Schmidt norm; it decays like `(N epsilon^2)^(-1/4)` whenever that aggregate grows. This is a proof-certificate comparison, not a lower bound on the true density.

## 5. Required pinned `e5f71d79...` application

The pinned completed ruled-level-set theorem (`COUNTEREXAMPLE_SEARCH.md`, Theorem C) applies literally to the `N=0` member of (4.1), because its exact nonzero spectrum is `{-3,2,6}`. On the one-sheet side `t>=0`, its exact source-valid inequality is

\[
p_{Q_{0,\varepsilon}}(t)
\le {1\over\sqrt{2\cdot6\cdot3}}
\int_0^{2\pi}
{d\theta\over
\sqrt{\sin^2\theta/2+\cos^2\theta/6+1/3}}
=1.298116608224222\ldots .
\tag{5.1}
\]

In particular the coarser scaled theorem gives `p(t)<=pi/sqrt(2)` for `t>=0`. The new fused receiver is a whole-line statement and remains valid after the subthreshold `±epsilon` pairs are added. The pinned counterexample search's failure to find a counterexample is **not** used as novelty evidence.

For `N>=4`, pinned `D_5` can also be spent on the physical `X--Y` cut. Its fifth volume is

\[
Z_5
=12\binom N4\varepsilon^8
 +\binom N5\varepsilon^{10},
\tag{5.2}
\]

so it independently yields

\[
\|p_{Q_{N,\varepsilon}}\|_\infty
\le5\sqrt{2e}\,Z_5^{-1/10}.
\tag{5.3}
\]

This confirms that the Hilbert–Schmidt moving-square payment and the fifth-volume payment use different structural currencies.

## 6. Remaining gap

The full QFORM conjecture remains OPEN. The new theorem does **not** allow an arbitrary additive `G(Y)` in the Hilbert–Schmidt branch: such a term moves the output center in (2.3) by a `Y`-dependent amount, outside auto19's uniform-fixed-center tensor half-Riesz estimate. Latest auto20 does allow arbitrary `G(Y)` but pays only `||M||_op`.

The sharpened unpaid implication is therefore:

`QFORM-HS-MOVING-SQUARE-WITH-REMAINDER-OR-STRUCTURAL-EXIT-v1` — either control

\[
X^T M Y+G(Y)+a(\beta^T Z+H(Y))^2
\]

at an aggregate cross scale while retaining arbitrary `G(Y)`, or prove that the global three-large-eigenvalue hypothesis forces a different paid physical-pair / projected-crossing / D5 / grouped-hub exit before this remainder appears. Small nonzero curvature cannot be discarded under arbitrary unbounded cap-one inputs.

## 7. Source pins actually used

- fleet03/B18 auto20, `QFORM-CROSS-MOVING-DIFFUSE-SQUARE-v1`, scientific commit `866968bafb00203a9892c46bf761dbb150d705cc`.
- fleet03/B18 auto19, `QFORM-BILINEAR-HS-HALF-RIESZ-v1`, scientific commit `7308d156465db33641b1db6e8609777b832c5da2`.
- pinned Claude/e5f source: `e5f71d79eff325201dd0274053d20268ce65b837`, `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, `COUNTEREXAMPLE_SEARCH.md`.
- M. Rudelson and R. Vershynin, *Small Ball Probabilities for Linear Images of High-Dimensional Distributions*, arXiv:1402.4492 / IMRN 2015, Theorem 1.2.
- T. Juškevičius and J. D. Lee, *Small ball probabilities, maximum density and rearrangements*, arXiv:1503.09190, Theorem 1.
- X. Hu and G. Paouris, *Small Ball Probabilities for Simple Random Tensors*, arXiv:2403.20192, Theorems 1.1 and 1.3.

No search miss is treated as proof of novelty or completeness.
