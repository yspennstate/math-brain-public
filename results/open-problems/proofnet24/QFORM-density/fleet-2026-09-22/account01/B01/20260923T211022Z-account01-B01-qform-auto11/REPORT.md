SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B01, 2026-09-23T21:10:22Z.
attacking: zero quadratic slope-kernel curvature via residual linear-phase averaged-frequency smoothing in an invertible two-bank cross packet.

# account01/B01 — zero-curvature linear-kernel averaged-frequency compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Oscillatory replacement  
**Status:** `PROVED_SUPPORTING_THEOREM_PENDING_INDEPENDENT_REVIEW / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Regularity:** the theorem below gives a continuous `C_0` density on its stated scope; continuity for the unrestricted target remains open.

## 1. Why this is the next endpoint

The preceding B01 theorem treated the two-bank packet

\[
Q=aX^2+2X p^TU+2Xq^TV+U^TAU+2U^TBV+V^TCV+\text{affine},                 \tag{1.1}
\]

where `X` is scalar, `U,V in R^2` are mutually independent, `B` is invertible, and all three random blocks are source-disjoint.  It used the exact slope change

\[
r=B^TU+qX                                                        \tag{1.2}
\]

and paid the packet whenever the resulting scalar quadratic curvature

\[
d_U:=a-2p^TB^{-T}q+q^TB^{-1}AB^{-T}q                           \tag{1.3}
\]

is nonzero.  The difficult endpoint is `d_U=0`: the scalar square-phase `L^4(dt)` budget disappears exactly, while the two-dimensional `V`-Plancherel factor remains only at the critical `|t|^{-1}` level.

The theorem below shows that this endpoint is still paid unless the exact slope-kernel vector is an **actual algebraic null vector** of the quadratic matrix.  The replacement is an integrated linear-phase estimate, not a pointwise quadratic van-der-Corput estimate.

## 2. Main theorem

### `QFORM-TWOBANK-ZEROCURVATURE-LINEAR-KERNEL-LP-v1`

Let `X` be a real random variable with density bounded by one.  Let `U,V in R^2` be independent of `X` and of each other, with Lebesgue densities satisfying

\[
\|p_U\|_\infty\le M_U,\qquad \|p_V\|_\infty\le M_V.             \tag{2.1}
\]

Let `A,C` be real symmetric `2 x 2` matrices, let `B` be invertible, and let `p,q in R^2`.  Allow arbitrary deterministic affine terms in (1.1).  Assume

\[
d_U=0.                                                          \tag{2.2}
\]

Define

\[
h_U:=p-AB^{-T}q,\qquad
\theta_U:=h_U^TB^{-T}q.                                          \tag{2.3}
\]

After the change (1.2), the coefficient of the remaining `X`-linear phase is an affine function `beta(r)`.  If the random variable

\[
\beta(R),\qquad R=B^TU+qX,                                      \tag{2.4}
\]

has a density bounded by `L_beta<infinity`, then for every `rho>2`, `Q` has a continuous density vanishing at infinity and

\[
\boxed{
\|p_Q\|_\infty
\le K_\rho
(M_UM_V)^{\rho/[2(\rho+1)]}
|\det B|^{-\rho/[2(\rho+1)]}
L_\beta^{1/(\rho+1)},}
                                                                    \tag{2.5}
\]

where

\[
K_\rho={\rho+1\over\pi}
\left[
{\pi(4\pi)^{1/\rho}(1-2/\rho)^{-1/2}
[2(\rho-1)]^{(\rho-1)/\rho}\over 2\rho}
\right]^{\rho/(\rho+1)}.                                      \tag{2.6}
\]

At `rho=4`,

\[
\boxed{
\|p_Q\|_\infty
\le 4.83295511233\,
(M_UM_V)^{2/5}|\det B|^{-2/5}L_\beta^{1/5}.}                    \tag{2.7}
\]

There is also a logarithmic near-endpoint form.  Put

\[
D_0=(M_UM_V)^{1/2}|\det B|^{-1/2},\qquad R_0={L_\beta\over D_0}. \tag{2.8}
\]

Then

\[
\boxed{
\|p_Q\|_\infty
\le 12D_0\bigl[1+\log_+R_0\bigr].}                              \tag{2.9}
\]

Thus the zero-curvature endpoint costs only a logarithm as the residual linear slope becomes nearly degenerate.

## 3. Exact kernel identity

Let the quadratic matrix of (1.1), in the block ordering `(X,U,V)`, be

\[
K=\begin{pmatrix}
 a&p^T&q^T\\
 p&A&B\\
 q&B^T&C
\end{pmatrix}.                                                   \tag{3.1}
\]

Define the slope-kernel vector

\[
w_U=(1,-B^{-T}q,0).                                              \tag{3.2}
\]

Set `s=p^TB^{-T}q` and `t=q^TB^{-1}AB^{-T}q`.  Under `d_U=0`, `a=2s-t`.  Hence

\[
\begin{aligned}
Kw_U
&=(a-s,\ p-AB^{-T}q,\ q-B^TB^{-T}q)\\
&=(s-t,\ h_U,\ 0).
\end{aligned}                                                     \tag{3.3}
\]

But

\[
\theta_U=h_U^TB^{-T}q=s-t,                                      \tag{3.4}
\]

so the exact structural identity is

\[
\boxed{Kw_U=(\theta_U,h_U,0).}                                  \tag{3.5}
\]

In particular, if `d_U=0` and `h_U=theta_U=0`, then

\[
\boxed{Kw_U=0.}                                                   \tag{3.6}
\]

The analytic compiler therefore fails at exact zero only when the product-preserving slope kernel has become a true algebraic null direction.  This is a much narrower endpoint than merely `d_U=0`.

## 4. Exact phase reduction

Write `u=B^{-T}(r-qx)`.  Then

\[
2u^TBv+2xq^Tv=2r^Tv.                                             \tag{4.1}
\]

Also

\[
u^TAu=r^TB^{-1}AB^{-T}r
-2xq^TB^{-1}AB^{-T}r
+x^2q^TB^{-1}AB^{-T}q,                                          \tag{4.2}
\]

and

\[
2xp^Tu=2x p^TB^{-T}r-2x^2p^TB^{-T}q.                            \tag{4.3}
\]

Because `d_U=0`, all `x^2` terms cancel.  Up to an irrelevant deterministic affine shift, the remaining coefficient of `x` is

\[
\beta(r)=2h_U^TB^{-T}r+\beta_0.                                 \tag{4.4}
\]

Substituting the random slope `R=B^TU+qX` gives

\[
\boxed{
\beta(R)=2h_U^TU+2\theta_U X+\beta_0.}                           \tag{4.5}
\]

This is the exact residual linear phase which replaces the vanished quadratic curvature.

## 5. Integrated linear-phase estimate

For fixed `r`, define

\[
g_r(x)=p_X(x)\,p_U(B^{-T}(r-qx)),\qquad
m_r=\int g_r(x)\,dx,                                             \tag{5.1}
\]

and

\[
F_r(t)=\int g_r(x)e^{it\beta(r)x}\,dx.                           \tag{5.2}
\]

Because `p_X<=1` and `p_U<=M_U`,

\[
0\le m_r\le M_U,\qquad
\int_{\mathbb R^2}m_r\,dr=|\det B|.                             \tag{5.3}
\]

Moreover the density of `R` is

\[
p_R(r)=|\det B|^{-1}m_r.                                       \tag{5.4}
\]

For `beta(r)!=0`, one-dimensional Plancherel gives

\[
\int_{\mathbb R}|F_r(t)|^2dt
={2\pi\over|\beta(r)|}\int g_r(x)^2dx
\le {2\pi M_Um_r\over|\beta(r)|}.                               \tag{5.5}
\]

Since `|F_r(t)|<=m_r`, interpolation with `L^infinity` yields, for every `rho>2`,

\[
\boxed{
\|F_r\|_\rho^\rho
\le {2\pi M_Um_r^{\rho-1}\over|\beta(r)|}.}                     \tag{5.6}
\]

This is the first key averaged-frequency replacement.  It is valid for arbitrarily fragmented cap-one densities and makes no pointwise decay assertion.

Let

\[
A(t)^2=|\det B|^{-2}\int_{\mathbb R^2}|F_r(t)|^2dr.              \tag{5.7}
\]

Minkowski in `L^{rho/2}(dt)`, followed by (5.3)-(5.6), gives

\[
\begin{aligned}
\|A\|_\rho^2
&\le |\det B|^{-2}(2\pi M_U)^{2/\rho}
\int m_r^{2(\rho-1)/\rho}|\beta(r)|^{-2/\rho}dr\\
&\le |\det B|^{-1}(2\pi)^{2/\rho}M_U
\mathbb E|\beta(R)|^{-2/\rho}.                                  \tag{5.8}
\end{aligned}
\]

If a real random variable `Y` has density cap `L`, then for every `0<alpha<1` the bathtub/rearrangement estimate gives

\[
\mathbb E|Y|^{-\alpha}
\le {2^\alpha\over1-\alpha}L^\alpha.                             \tag{5.9}
\]

Applying this with `alpha=2/rho` to `beta(R)` yields

\[
\boxed{
\|A\|_\rho
\le |\det B|^{-1/2}(4\pi)^{1/\rho}
(1-2/\rho)^{-1/2}M_U^{1/2}L_\beta^{1/\rho}.}                    \tag{5.10}
\]

Notice why `rho>2` is the natural endpoint: the naive `L^2(dt)` route would require the generally divergent negative first moment `E|beta(R)|^{-1}`, whereas every exponent `2/rho<1` is integrable under a bounded density.

## 6. Spend the linear budget against the critical two-dimensional packet

Let

\[
b_t(v)=p_V(v)e^{it(v^TCv+\text{affine}(v))}.                    \tag{6.1}
\]

Then `||b_t||_2<=M_V^{1/2}`.  The `2r^Tv` term in (4.1), two-dimensional Plancherel, and Cauchy-Schwarz in `r` give

\[
\boxed{
|\phi_Q(t)|
\le \min\{1,\ \pi M_V^{1/2}|t|^{-1}A(t)\}.}                    \tag{6.2}
\]

The packet is therefore pointwise only at the critical `|t|^{-1}` threshold, but its coefficient belongs to `L^rho(dt)` by (5.10).

Let `rho'=rho/(rho-1)`.  Holder gives

\[
\int_{|t|>T}|t|^{-1}A(t)dt
\le [2(\rho-1)]^{(\rho-1)/\rho}T^{-1/\rho}\|A\|_\rho.           \tag{6.3}
\]

Consequently

\[
\int_{\mathbb R}|\phi_Q(t)|dt
\le 2T+D_\rho T^{-1/\rho},                                      \tag{6.4}
\]

where

\[
D_\rho=
\pi(M_UM_V)^{1/2}|\det B|^{-1/2}L_\beta^{1/\rho}
(4\pi)^{1/\rho}(1-2/\rho)^{-1/2}
[2(\rho-1)]^{(\rho-1)/\rho}.                                   \tag{6.5}
\]

Optimizing at

\[
T=(D_\rho/(2\rho))^{\rho/(\rho+1)}                              \tag{6.6}
\]

and using Fourier inversion `||p_Q||_infinity <= (2pi)^(-1)||phi_Q||_1` proves (2.5)-(2.6).  In particular `phi_Q in L^1`, so the density is continuous and vanishes at infinity.

For `rho=4`, (2.6) reduces to

\[
K_4=5\,6^{3/5}4^{-4/5}=4.832955112329406\ldots.                 \tag{6.7}
\]

## 7. Logarithmic near-endpoint optimization

Rewrite (2.5) as

\[
\|p_Q\|_\infty\le K_\rho D_0 R_0^{1/(\rho+1)}.                 \tag{7.1}
\]

For `rho>=4`, the elementary bounds

\[
(4\pi)^{1/\rho}<2,\qquad
(1-2/\rho)^{-1/2}\le\sqrt2,\qquad
[2(\rho-1)]^{(\rho-1)/\rho}\le2\rho                            \tag{7.2}
\]

imply

\[
K_\rho\le {5\sqrt2\over2}\rho<3.536\rho.                      \tag{7.3}
\]

If `R_0<e^4`, take `rho=4`; then `K_4R_0^{1/5}<11`.  If `R_0>=e^4`, take `rho=log R_0`; then

\[
R_0^{1/(\rho+1)}=e^{\rho/(\rho+1)}<e,                           \tag{7.4}
\]

and (7.3) gives a coefficient below `10 log R_0`.  This proves the clean bound (2.9).

## 8. Original-product corollary and exact null endpoint

Suppose now that `X` is one original cap-one coordinate and

\[
U=PY,\qquad PP^T=I_2,                                            \tag{8.1}
\]

where `Y` is a disjoint bank of original independent cap-one coordinates.  Then (4.5) is a normalized original-source linear form with coefficient vector

\[
2(\theta_U,P^Th_U),                                               \tag{8.2}
\]

whose Euclidean norm is

\[
2H_U,\qquad
H_U:=\sqrt{\theta_U^2+\|h_U\|_2^2}=\|Kw_U\|_2.                  \tag{8.3}
\]

The current source-valid Rogozin/Ball product-projection theorem gives density cap `sqrt(2)` for a unit one-dimensional linear form.  Therefore, when `H_U>0`,

\[
\boxed{L_\beta\le {1\over\sqrt2 H_U}.}                           \tag{8.4}
\]

At `rho=4`,

\[
\boxed{
\|p_Q\|_\infty
\le4.50930656642
(M_UM_V)^{2/5}|\det B|^{-2/5}H_U^{-1/5}.}                        \tag{8.5}
\]

If both `U` and `V` are orthonormal two-dimensional projections of disjoint original cap-one product banks, the reviewed two-dimensional projection theorem gives `M_U,M_V<=2`, hence

\[
\boxed{
\|p_Q\|_\infty
\le7.85115874295\,|\det B|^{-2/5}H_U^{-1/5}.}                    \tag{8.6}
\]

The logarithmic form becomes

\[
\boxed{
\|p_Q\|_\infty
\le {24\over\sqrt{|\det B|}}
\left[1+\log_+\left({\sqrt{|\det B|}\over2\sqrt2 H_U}\right)\right].} \tag{8.7}
\]

All these formulas have the correct `A -> sA` homogeneity `|s|^{-1}`.

If `H_U=0`, (3.5) gives the exact algebraic statement `Kw_U=0`.  Thus the limiting obstruction is not a hidden failure of the oscillatory estimate: it is a literal null direction of the packet matrix.

There is a completely symmetric orientation.  Define

\[
d_V=a-2q^TB^{-1}p+p^TB^{-T}CB^{-1}p,                            \tag{8.8}
\]

\[
h_V=q-CB^{-1}p,\qquad
\theta_V=h_V^TB^{-1}p,\qquad
w_V=(1,0,-B^{-1}p).                                               \tag{8.9}
\]

If `d_V=0`, the same proof with `U,V` reversed applies, and

\[
Kw_V=(\theta_V,0,h_V).                                           \tag{8.10}
\]

Hence simultaneous failure of both zero-curvature linear compilers at exact zero forces one or two explicit algebraic null directions rather than merely two vanishing Schur curvatures.

## 9. Strict target-valid no-pivot family

This theorem is not a disguised favorable physical-pivot estimate.  Consider the five-dimensional spectral packet with

\[
A=C=0,\qquad B=I_2,\qquad p=e_1,\qquad q=e_2,\qquad a=0.          \tag{9.1}
\]

Its matrix is

\[
K_*=\begin{pmatrix}
0&1&0&0&1\\
1&0&0&1&0\\
0&0&0&0&1\\
0&1&0&0&0\\
1&0&1&0&0
\end{pmatrix}.                                                   \tag{9.2}
\]

The characteristic polynomial is exactly

\[
\boxed{\chi_{K_*}(z)=z(z-1)(z+1)(z^2-3),}                       \tag{9.3}
\]

so the nonzero spectrum is

\[
\{-\sqrt3,-1,1,\sqrt3\}.                                       \tag{9.4}
\]

Thus there are four eigenvalues of modulus at least one.  Here

\[
d_U=0,\qquad h_U=e_1,\qquad\theta_U=0,\qquad H_U=1,\qquad\det B=1. \tag{9.5}
\]

Embed the two `R^2` banks as flat orthonormal two-dimensional projections of two disjoint banks of `m` original coordinates.  Concretely, take two orthonormal flat rows in each bank (Walsh rows for a convenient even `m`) and let `S` be the resulting isometric embedding.  Then the physical matrix is `SK_*S^T`, so its nonzero spectrum remains (9.4).

Every physical diagonal is zero.  Hub-bank entries have magnitude `m^{-1/2}`, and bank-to-bank entries have magnitude at most `2/m`.  Therefore

\[
\max_{i\ne j}|A_{ij}|\le m^{-1/2},\qquad
\max_{|P|=2}|\det A[P,P]|\le m^{-1}.                             \tag{9.6}
\]

All physical scalar and pair pivots can hence be made arbitrarily small while the target spectrum remains fixed.  Nevertheless (8.6) gives, for **every** admissible cap-one product input law,

\[
\boxed{\|p_Q\|_\infty\le7.85115874295,}                         \tag{9.7}
\]

and the density is continuous and vanishes at infinity.

## 10. The phase-aligned counterexample remains intact

Nothing above asserts a law-uniform bound of the form

\[
|\mathbb E e^{itX^2}|\le C|t|^{-1/2}.                            \tag{10.1}
\]

Indeed, for any fixed nonzero `t` and any small `eta>0`, the set

\[
\{x:\operatorname{dist}(tx^2,2\pi\mathbb Z)\le\eta\}           \tag{10.2}
\]

has infinite Lebesgue measure after taking sufficiently many separated phase windows.  Choose a measurable subset `E` of measure one and put `f=1_E`.  Then `0<=f<=1`, `int f=1`, but

\[
\operatorname{Re}\mathbb E e^{itX^2}\ge\cos\eta.                \tag{10.3}
\]

Thus no law-uniform pointwise power decay can hold.  The present theorem instead uses Plancherel/interpolation **after** exposing the exact random linear slope `beta(R)`, then spends the bounded-density negative fractional moment `E|beta(R)|^{-2/rho}`.  Fragmentation is allowed throughout.

## 11. Designated partner application

The newest completed `account02/B01` handoff available before this publication is `QFORM-ONEHUB-Z1-NOMARGINAL-HALFRIESZ-v1`, canonical report

`yspennstate/math-open-problems@339c1fdf3bc65a79f5be126e730dd3b251320e66:proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260923T180438Z-auto11/REPORT.md`.

It proves, after an original-coordinate scalar completion,

\[
\|p_Q\|_\infty
\le8|a|^{-1/2}(\|m\|_2\|C\|_F)^{-1/4}                           \tag{11.1}
\]

with no projected-row marginal gate.  On its actual strict-N3 family

\[
a=\varepsilon,\qquad\|m\|_2=\varepsilon^{-1},\qquad
\|C\|_F=\varepsilon^{-1},                                       \tag{11.2}
\]

so (11.1) gives the concrete equation-level inequality

\[
\boxed{
\|p_Q\|_\infty
\le8\varepsilon^{-1/2}(\varepsilon^{-2})^{-1/4}=8.}             \tag{11.3}
\]

Their sharper heavy-row subbranch gives `2^(11/4)=6.727171322...` on the same unique-heavy-row endpoint.  The partner theorem pays every nonzero projected crossing after the scalar peel; the present theorem is complementary because it pays an invertible two-bank packet when scalar **quadratic** kernel curvature is exactly zero but the residual **linear** kernel slope is nonzero.

## 12. What remains open

The unrestricted conjecture remains **OPEN**.  The first structural implication suggested by this run is

`QFORM-TWOBANK-TRUE-NULL-OR-SINGULAR-CROSS-ROUTING-v3`.

After an invertible two-bank crossing is identified, a zero Schur curvature is now not itself an unpaid analytic endpoint:

* if `H_U=||Kw_U||>0` or the symmetric `H_V>0`, the present averaged-frequency theorem pays it, with only logarithmic deterioration as `H` tends to zero;
* if `H_U=0` (respectively `H_V=0`), the corresponding product-preserving slope-kernel vector is an **exact null vector** of the packet matrix.

The remaining global work is therefore to show that target-scale three-eigenvalue mass forces either a target-scale invertible-cross/linear-kernel currency, an already-paid scalar-square/projected-crossing/pair/ridge/volume receiver, or else that the exact/near-null vectors can be quotient-routed without losing the third spectral resource.  Singular or nearly singular `B`, extra spectral tails, and the quantitative near-null routing are not solved here.

## 13. Source and integrity notes

No Gaussian, moment, compact-support, connected-support, log-concavity, iid, or post-rotation independence assumption was used.  The only grouped-density inputs are the current source-valid one- and two-dimensional product-projection bounds, and the theorem explicitly keeps source-disjoint original banks when those bounds are invoked.  No conditional projected-density cap or arbitrary-joint coarea estimate is used.

A narrow prepublication review of this report found no credentials, account identifiers beyond the logical fleet label, signed URLs, machine paths, or unrelated private data.  The deterministic checks attached to this run verify only algebra/constants/spectrum; they are not an independent proof review.
