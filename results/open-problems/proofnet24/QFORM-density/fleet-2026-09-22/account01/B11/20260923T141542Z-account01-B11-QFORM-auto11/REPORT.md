SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B11, 2026-09-23T14:15:42Z.
attacking: the finite-shared-spike null-sum chamber via a four-row L2 matching estimate that removes the leverage<=1/2 gate.

# Four-row L2 matching compiler for the indefinite null-sum chamber

Programme: `QFORM-DENSITY-3EIG-20260922`  
Worker: `account01/B11`  
Run: `20260923T141542Z-account01-B11-QFORM-auto11`  
Status: `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / PARTNER_RESULT_APPLIED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Source-pinned starting point


The designated completed partner source actually used below is account02/B11 r31,

`yspennstate/math-open-problems@15189fa11c0c752c1d9022c60e253a9e8d457df8`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B11/20260923T124731Z-account02-B11-QFORM-r31/REPORT.md`.

Its product-preserving null-sum normal form is the following. Let `S,T` be disjoint sets of ORIGINAL independent coordinates, each input density bounded by one. Put

\[
U=a\cdot X_S,\qquad H=h\cdot X_S,\qquad V=c\cdot X_T,\qquad C=\|c\|_2>0,
\]

and consider

\[
Q=\beta U^2+2\alpha VH+R_T(X_T)+\sum_{i\in S}q_i(X_i),             \tag{1.1}
\]

where `R_T` and the coordinate-separable `q_i` are arbitrary real measurable functions. The partner proves the Fresnel reduction, for `t!=0`,

\[
|\phi_Q(t)|\le (4\pi|\beta t|)^{-1/2}
 {\sqrt2\over 2|\alpha t|C}
 \int_{\mathbb R^2}\prod_{i\in S}
 |\widehat g_{i,t}(a_i\xi+h_i y)|\,d\xi\,dy,                         \tag{1.2}
\]

where `g_{i,t}(x)=f_i(x)e^{itq_i(x)}` and hence `|g_{i,t}|=f_i<=1`, `\int f_i=1`. Its Brascamp--Lieb compiler pays (1.2) when a chosen planar frame has all normalized leverages at most `1/2`; in the exact balanced null-sum chamber this yields a continuous density bound `96/s`. Failure of that gate, after the scalar-pivot exit, leaves at most three finite shared-direction spikes.

The previous account01/B11 run at

`yspennstate/math-open-problems@0fdef4c0a98afec689f4310872bdac4fc1010579`

proved that, inside that finite-spike chamber, the exact rank-one residual left frame is already paid by `2048/s`. The purpose of the present run is to attack the positive-area transition without assuming a low-leverage planar frame.

## 2. New analytic theorem: two disjoint wedge pairs suffice

### Theorem 2.1 — `QFORM-FOURROW-L2-MATCHING-v1`

Assume (1.1). Suppose there are four **distinct** indices `i,j,k,l in S`. Write

\[
v_r=(a_r,h_r)\in\mathbb R^2,
\]

and suppose

\[
\Delta_1=|\det(v_i,v_j)|>0,\qquad
\Delta_2=|\det(v_k,v_l)|>0.                                        \tag{2.1}
\]

Then `Q` has a continuous density and

\[
\boxed{
\|p_Q\|_\infty
\le
3\,2^{1/3}
|\beta|^{-1/3}(|\alpha|C)^{-2/3}
(\Delta_1\Delta_2)^{-1/3}.}                                      \tag{2.2}
\]

No leverage hypothesis is imposed. No independence between `U` and `H` is assumed. The only independence used is the original-coordinate product structure needed for (1.2).

### Proof

Start from the partner's exact inequality (1.2). Every Fourier factor has modulus at most one, so discard every factor except the four in (2.1). Let

\[
F_r=|\widehat g_{r,t}|.
\]

The remaining two-dimensional integral is

\[
I=\int_{\mathbb R^2}
F_i(v_i\cdot z)F_j(v_j\cdot z)
F_k(v_k\cdot z)F_l(v_l\cdot z)\,dz.                              \tag{2.3}
\]

Cauchy--Schwarz, grouping the two disjoint nonparallel pairs, gives

\[
I\le
\left(\int F_i(v_i\cdot z)^2F_j(v_j\cdot z)^2dz\right)^{1/2}
\left(\int F_k(v_k\cdot z)^2F_l(v_l\cdot z)^2dz\right)^{1/2}.      \tag{2.4}
\]

For the first factor, the exact linear change of variables

\[
(u,w)=(v_i\cdot z,v_j\cdot z)
\]

has Jacobian `Delta_1`. Therefore Plancherel gives

\[
\int F_i(v_i\cdot z)^2F_j(v_j\cdot z)^2dz
={1\over\Delta_1}\|\widehat g_{i,t}\|_2^2\|\widehat g_{j,t}\|_2^2.
\]

Since `|g_{r,t}|=f_r`, `0<=f_r<=1`, and `\int f_r=1`,

\[
\|\widehat g_{r,t}\|_2^2
=2\pi\int f_r^2\le2\pi.                                           \tag{2.5}
\]

Thus the first factor in (2.4) is at most `2pi Delta_1^{-1/2}` and the second at most `2pi Delta_2^{-1/2}`. Hence

\[
\boxed{I\le(2\pi)^2(\Delta_1\Delta_2)^{-1/2}.}                    \tag{2.6}
\]

Substituting (2.6) into (1.2) yields

\[
|\phi_Q(t)|\le\min\{1,K|t|^{-3/2}\},                             \tag{2.7}
\]

with

\[
K=\sqrt2\,\pi^{3/2}
|\beta|^{-1/2}(|\alpha|C)^{-1}(\Delta_1\Delta_2)^{-1/2}.          \tag{2.8}
\]

For every `K>0`, direct integration gives

\[
{1\over2\pi}\int_{\mathbb R}\min\{1,K|t|^{-3/2}\}\,dt
={3\over\pi}K^{2/3}.                                              \tag{2.9}
\]

Equations (2.8)-(2.9) give exactly (2.2). In particular `phi_Q in L^1`, so Fourier inversion gives a continuous density vanishing at infinity. QED.

## 3. Why this is the correct rank-three smoothing mechanism

The rank-two opposite-sign endpoint remains genuinely singular. For independent centered unit uniforms,

\[
p_{2XY}(t)=\log{1\over2|t|},\qquad0<|t|<1/2.                     \tag{3.1}
\]

In (1.2), the right scalar `V` and the change `y=2alpha t V` contribute the borderline factor `|t|^{-1}`. This is exactly the logarithmic rank-two scale. Fresnel linearization of the third quadratic direction `beta U^2` contributes the additional `|t|^{-1/2}`. The four-row L2 estimate controls the shared left source without rotating it into independent spectral variables. Thus the third direction changes the nonintegrable borderline into the integrable envelope `|t|^{-3/2}`.

## 4. Actual application of the designated partner result

The partner report gives the target-valid six-coordinate family

\[
\begin{aligned}
r_1&=(1/2,1/(2\sqrt2),0),&r_2&=(1/2,1/(2\sqrt2),0),\\
r_3&=(1/2,-1/(2\sqrt2),0),&r_4&=(1/2,-1/(2\sqrt2),0),\\
r_5&=(0,0,1),&r_6&=(0,1/\sqrt2,0),
\end{aligned}                                                         \tag{4.1}
\]

with

\[
M=\begin{pmatrix}1&0&0\\0&0&1\\0&1&0\end{pmatrix},
\qquad \operatorname{spec}(M)=\{1,1,-1\}.                            \tag{4.2}
\]

It gives

\[
Q=U^2+2V(Z+W),                                                         \tag{4.3}
\]

where

\[
U=(X_1+X_2+X_3+X_4)/2,
\quad Z=(X_1+X_2-X_3-X_4)/(2\sqrt2),
\quad V=X_5,
\quad W=X_6/\sqrt2.                                                    \tag{4.4}
\]

The partner's leverage-bound theorem gives `||p_Q||_infinity<=12` on this family. Apply Theorem 2.1 instead with the vertex-disjoint pairs `(1,3)` and `(2,4)`. Their wedge magnitudes are

\[
\Delta_1=\Delta_2={1\over2\sqrt2},
\qquad \Delta_1\Delta_2={1\over8},                                    \tag{4.5}
\]

while `beta=alpha=C=1`. Therefore

\[
\boxed{
\|p_Q\|_\infty
\le3\,2^{1/3}(1/8)^{-1/3}
=6\,2^{1/3}
=7.559526299\ldots<7.560.}                                            \tag{4.6}
\]

This is an actual quantitative use of the completed designated partner result, not a copied citation.

## 5. Exact wedge-matching bookkeeping

For an arbitrary finite planar frame `v_1,...,v_m`, define

\[
w_{ij}=\det(v_i,v_j)^2,\qquad
D=\sum_{i<j}w_{ij}=\det\!\left(\sum_i v_iv_i^T\right),                 \tag{5.1}
\]

and the weighted degree

\[
d_i=\sum_{j\ne i}w_{ij}.                                               \tag{5.2}
\]

When `D>0`, the normalized planar leverage is exactly

\[
\boxed{v_i^T\left(\sum_r v_rv_r^T\right)^{-1}v_i={d_i\over D}.}         \tag{5.3}
\]

This is the two-dimensional cofactor/Cauchy--Binet identity and will be used in the star classification below.

Let `M_4` be the total weight of unordered vertex-disjoint edge pairs,

\[
M_4=\sum_{\substack{\{i,j\},\{k,l\}\text{ disjoint}\\
                     \{\{i,j\},\{k,l\}\}\text{ unordered}}}
       w_{ij}w_{kl}.                                                     \tag{5.4}
\]

Then the exact identity

\[
\boxed{
M_4={1\over2}\left(D^2+\sum_{i<j}w_{ij}^2-\sum_i d_i^2\right).}         \tag{5.5}
\]

holds. Indeed, all unordered pairs of distinct edges have total weight

\[
{1\over2}\left(D^2-\sum_e w_e^2\right),
\]

whereas adjacent edge pairs have total weight

\[
{1\over2}\sum_i\left(d_i^2-\sum_{e\ni i}w_e^2\right)
={1\over2}\sum_i d_i^2-\sum_e w_e^2.
\]

Subtracting gives (5.5).

### Exact zero-matching classification

If `D>0` and `M_4=0`, the graph of positive wedge weights has matching number at most one. Such a simple graph is either a star or a triangle (isolated vertices allowed).

* **Star.** There is a center `e` such that all positive wedges are incident to `e`. Then `d_e=D`, so (5.3) gives leverage exactly one: the center is necessarily among the partner's exceptional `>1/2` rows. After removing that exceptional center (and any other exceptional leaves), every pair of remaining rows has zero determinant; all nonzero residual rows are parallel. Thus the residual planar Gram has rank at most one, precisely the endpoint already paid by account01/B11 `QFORM-NULLSUM-RANKONE-RESIDUAL-COMPILER-v1` (unless the center triggers the earlier scalar-pivot exit).
* **Triangle.** Three rows have pairwise nonzero wedges. Any outside row must have zero wedge with all three, otherwise it creates a disjoint positive edge with the opposite triangle edge. Since two triangle rows span `R^2`, every outside row is therefore zero. In the partner normalization `sum_i a_i^2=1`; hence one of the three nonzero rows has `a_i^2>=1/3`. Its physical diagonal is `beta a_i^2`, and the exact-rank-three scalar-pivot theorem gives the dimension-free estimate

\[
\|p_Q\|_\infty
\le128[(1/3)(s/3)s^3]^{-1/4}
={128\sqrt3\over s}<221.703/s.                                        \tag{5.6}
\]

Therefore the **exact** `M_4=0` endpoint of the balanced null-sum chamber is fully paid by existing product-safe branches.

## 6. What remains unpaid

The present theorem does **not** turn an arbitrarily small positive matching product into a universal constant. If `M_4>0` but tends to zero, selecting a single matching in (2.2) can still lose scale. A dimension-dependent lower bound obtained by dividing `M_4` by the number of matchings would be useless.

The first remaining B11 implication is therefore

`QFORM-NULLSUM-NEAR-STAR-MATCHING-MASS-COMPILER-v1`:

> In the balanced exact-rank-three null-sum chamber, control the regime `0<M_4<<D^2` by a product-preserving averaged/multilinear estimate, or combine the near-star geometry with the already-paid rank-one half-Riesz endpoint without treating a small matrix coefficient as a uniformly small random quadratic perturbation on unbounded supports.

This is strictly narrower than the previous finite-shared-spike statement: two disjoint nondegenerate wedge pairs are now paid explicitly, and the exact matching-number-one endpoint is classified and paid. Arbitrary additional nonseparable spectrum beyond exact rank three remains a separate full-QFORM interface.

## 7. Continuity and scope

Theorem 2.1 proves a continuous `C_0` density because its characteristic function is absolutely integrable. The star/rank-one endpoint from the preceding account01/B11 theorem proves essential boundedness but did not establish continuity. The full conjecture and full continuity conclusion remain OPEN.
