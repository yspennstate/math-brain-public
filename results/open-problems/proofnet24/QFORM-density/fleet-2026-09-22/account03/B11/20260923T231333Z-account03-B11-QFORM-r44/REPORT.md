SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B11, 2026-09-23T23:13:33Z.
attacking: the unique-heavy-row two-star linear small-ball endpoint: retain the rank-two crossing and use two source-disjoint star banks to obtain a linear interval bound.

# account03/B11 r44 — arbitrary-pivot rank-one shared-hub tensor receiver and a paid subbranch of the unique-heavy-row collar

Programme: `QFORM-DENSITY-3EIG-20260922`.
Assignment: indefinite signatures `(2,1)` / `(1,2)`.
Status: **NEW ANALYTIC RECEIVER / NEW CONTINUITY BRANCH / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN**.
Execution: `WITHOUT_VERIFIED_BRAIN`.

The full owner target remains open. This report proves a new product-preserving receiver that removes the literal-zero-pivot restriction from the rank-one shared-hub tensor theorem, then applies it to a genuine subbranch of the account03/B11 r43 unique-heavy-row/two-star survivor. It does **not** prove the full exact-rank-three theorem and does not address arbitrary additional nonseparable spectrum.

No Gaussian, log-concave, moment, compact-support, connected-support, finite-fragmentation, post-rotation independence, conditional-density-cap, arbitrary-joint coarea, pointwise law-uniform van-der-Corput decay, or perturbative deletion of a small nonzero coefficient is used.

## 1. Fresh sources and inherited hard chamber

Fresh owner controls were resolved from `yspennstate/math-research-brain` main at invocation start. OWNER CONTROL remains revision `2026-09-22.15`, QFORM is the sole research target, and the full conjecture is `OPEN / NOT PROVED / NOT DISPROVED`.

The immediate B11 predecessor is

- repository: `yspennstate/math-open-problems`
- commit: `d75835c958b5dcdd28649eb79af0faf3103b5d89`
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260923T221215Z-account03-B11-QFORM-r43/REPORT.md`.

In its exact-rank-three indefinite hard chamber,

\[
A=RMR^T,\qquad R^TR=I_3,\qquad s:=\min_a|\lambda_a(M)|\ge1,
\]

r43 reduces the unpaid finite-heavy-row state to one physical row `i` with tiny scalar pivot, no individually strong edge, and a robust off-diagonal self-star. Put

\[
\beta_0:=\frac{289}{15984}=0.01808058058058\ldots,
\]
\[
\eta_0:=\frac{\sqrt{191}}{16}\beta_0
=0.01561741219248\ldots,
\qquad
\theta_0:=\frac{\eta_0}{2}
=0.007808706096240\ldots .
\]

After all earlier exits fail, r43 produces two disjoint sets of ORIGINAL independent coordinates `B_1,B_2` such that

\[
\sum_{j\in B_r}A_{ij}^2>\theta_0^2s^2,
\qquad r=1,2.
\tag{1.1}
\]

The newest account02/B11 correction shows that (1.1) alone is not enough: splitting the leaves of one shared physical hub into two banks still leaves only a rank-two logarithmic saddle. Therefore the present run explicitly retains a genuine transverse interbank crossing and spends it as the third smoothing direction.

The analytic source used and strengthened here is account02/B02:

- repository: `yspennstate/math-open-problems`
- commit: `aeaba9e3351623ead11450857c2d014b43664aef`
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260923T200844Z-account02-B02-qform-auto11/REPORT.md`.

Its tensor lemma permits an arbitrary phase in the shared scalar bank. That observation removes the zero-pivot hypothesis from its rank-one physical-crossing application.

The designated account04/B11 dependency actually applied below is

- repository: `yspennstate/math-open-problems`
- commit: `30555c1ca97752e10f5089ccd95f8514c704be5a`
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account04/B11/20260923T131400Z-account04-B11-extension-mass-r6/REPORT.md`.

It supplies the full-line pair-area estimate

\[
\|p_Q\|_\infty\le \frac{128\sqrt2}{s\sqrt{g_{ij}}},
\qquad g_{ij}=\|r_i\wedge r_j\|^2.
\tag{1.2}
\]

## 2. Product-preserving three-bank tensor lemma with arbitrary shared-hub phase

The following is the analytic engine. It is restated because the arbitrary `F_H` term is exactly what matters for the nonzero-pivot extension.

### Lemma 2.1 — shared-hub tensor smoothing

Let `H`, `Y=(Y_1,Y_2)`, and `Z=(Z_1,Z_2)` be three mutually independent ORIGINAL-coordinate banks. Assume

\[
\|p_H\|_\infty\le K_H,
\qquad
\|p_Y\|_\infty\le M_Y,
\qquad
\|p_Z\|_\infty\le M_Z.
\]

Here no independence between the two coordinates of `Y`, nor between the two coordinates of `Z`, is required. Let `F_H,F_Y,F_Z` be arbitrary measurable real phases on the respective source banks. For nonzero `\alpha,\beta,\sigma`, put

\[
Q_0=F_H(H)+F_Y+F_Z
  +2H(\alpha Y_1+\beta Z_1)+2\sigma Y_2Z_2.
\tag{2.1}
\]

Then

\[
|\phi_{Q_0}(t)|
\le
\min\left\{1,
\pi^{3/2}K_H\sqrt{M_YM_Z}
|\alpha\beta\sigma|^{-1/2}|t|^{-3/2}
\right\}.
\tag{2.2}
\]

Consequently `Q_0` has a continuous `C_0` density and

\[
\boxed{
\|p_{Q_0}\|_\infty
\le
3K_H^{2/3}(M_YM_Z)^{1/3}
|\alpha\beta\sigma|^{-1/3}.
}
\tag{2.3}
\]

#### Proof

Push the phase-twisted measures of the three independent banks to the displayed coordinates. Denote their complex densities by `g_t(h),a_t(y),b_t(z)`. Since phase multiplication has modulus one,

\[
|g_t(h)|\le p_H(h)\le K_H,
\qquad
\|a_t\|_2^2\le M_Y,
\qquad
\|b_t\|_2^2\le M_Z.
\tag{2.4}
\]

After integrating the shared hub, define

\[
k_t(u):=\int g_t(h)e^{i2thu}\,dh.
\]

The remaining bilinear kernel factors:

\[
K_t(y,z)=k_t(\alpha y_1+\beta z_1)e^{i2t\sigma y_2z_2}.
\]

For the first one-dimensional operator

\[
(T_1f)(y)=\int k_t(\alpha y+\beta z)f(z)\,dz,
\]

Plancherel gives

\[
\|T_1\|_{2\to2}
\le |\alpha\beta|^{-1/2}\|\widehat{k_t}\|_\infty.
\]

With the angular Fourier convention used in the source,

\[
\widehat{k_t}(\xi)=\frac{\pi}{|t|}
 g_t\!\left(-\frac{\xi}{2t}\right),
\]

so

\[
\|T_1\|_{2\to2}
\le \pi K_H|t|^{-1}|\alpha\beta|^{-1/2}.
\tag{2.5}
\]

The second bilinear Fourier operator satisfies exactly

\[
\|T_2\|_{2\to2}
=\left(\frac{\pi}{|t\sigma|}\right)^{1/2}.
\tag{2.6}
\]

Taking the tensor-product norm and pairing with `a_t,b_t` gives (2.2). If

\[
K=\pi^{3/2}K_H\sqrt{M_YM_Z}|\alpha\beta\sigma|^{-1/2},
\]

then

\[
\int_{\mathbb R}\min\{1,K|t|^{-3/2}\}\,dt=6K^{2/3}.
\]

Fourier inversion therefore gives (2.3), and `\phi\in L^1` gives a continuous `C_0` density. QED.

The key exponent is visible directly: the shared hub supplies a full `|t|^{-1}` operator gain and the independent transverse bilinear crossing supplies another `|t|^{-1/2}`. Their product is the integrable `|t|^{-3/2}`. With only the shared-hub saddle, the decay is the nonintegrable rank-two endpoint `|t|^{-1}`.

## 3. New theorem: the rank-one shared-hub physical receiver does not need zero pivot

Fix a physical coordinate `i` and two disjoint sets `L,R` of ORIGINAL coordinates. Condition on all coordinates outside `{i}\cup L\cup R`; the conditioned variables remain mutually independent across the three retained banks.

Write

\[
a=A_{ii},\qquad
c=A[L,i],\qquad
r=A[i,R],\qquad
N=A[L,R].
\tag{3.1}
\]

Assume

\[
c\ne0,\qquad r\ne0,\qquad \operatorname{rank}N=1.
\tag{3.2}
\]

Let

\[
P_c=I-\frac{cc^T}{\|c\|^2},
\qquad
P_r=I-\frac{rr^T}{\|r\|^2},
\qquad
C=P_cNP_r,
\tag{3.3}
\]

and define

\[
T:=\|c\|^2\|r\|^2\|C\|_F^2.
\tag{3.4}
\]

### Theorem 3.1 — `QFORM-ANYPIVOT-RANKONE-SHAREDHUB-TENSOR-L1-v1`

If `T>0`, then for arbitrary real pivot `a=A_{ii}` — including arbitrarily small nonzero `a` — the full ambient quadratic form has a continuous `C_0` density and

\[
\boxed{
|\phi_Q(t)|
\le
\min\left\{1,
2\pi^{3/2}T^{-1/4}|t|^{-3/2}
\right\},
}
\tag{3.5}
\]

\[
\boxed{
\int_{\mathbb R}|\phi_Q(t)|\,dt
\le 6\pi\,2^{2/3}T^{-1/6},
}
\tag{3.6}
\]

and

\[
\boxed{
\|p_Q\|_\infty
\le3\,2^{2/3}T^{-1/6}
=4.762203155904598\ldots\,T^{-1/6}.
}
\tag{3.7}
\]

All same-bank quadratic terms, all conditioned outside couplings, all affine terms, and the hub square `aX_i^2` are retained exactly.

### Proof

Set

\[
e=c/\|c\|,\qquad f=r/\|r\|.
\]

Because `rank N=1` and `C=P_cNP_r\ne0`, there are unit vectors `v\perp e` in the `L` coefficient space and `z\perp f` in the `R` coefficient space such that, in the two-dimensional orthonormal bases `(e,v)` and `(f,z)`, the entire rank-one crossing is represented by

\[
B=\begin{pmatrix}d&q\\p&\sigma\end{pmatrix},
\qquad
\sigma\ne0,
\qquad
\det B=0,
\qquad
|\sigma|=\|C\|_F.
\tag{3.8}
\]

Let

\[
Y_1=e^TX_L,\quad Y_2=v^TX_L,
\qquad
Z_1=f^TX_R,\quad Z_2=z^TX_R.
\]

The determinant-one shears

\[
Y_2'=Y_2+(q/\sigma)Y_1,
\qquad
Z_2'=Z_2+(p/\sigma)Z_1
\tag{3.9}
\]

leave `Y_1,Z_1` unchanged and, since `d\sigma=pq`, give the exact crossing identity

\[
Y^TBZ=\sigma Y_2'Z_2'.
\tag{3.10}
\]

No coefficient is discarded.

The hub-star terms are

\[
2X_i(c^TX_L+r^TX_R)
=2X_i(\|c\|Y_1+\|r\|Z_1).
\tag{3.11}
\]

Every within-`L` term, including the effect of the shear and all conditioned affine terms, is absorbed into an arbitrary phase `F_L`; similarly for `R`. Crucially, the physical pivot is retained as

\[
F_H(X_i)=aX_i^2+\ell_iX_i+	ext{constant},
\tag{3.12}
\]

for the conditioned affine coefficient `\ell_i`. Lemma 2.1 permits **arbitrary** `F_H`; therefore no assumption `a=0` is needed anywhere in the analytic argument.

The two-dimensional orthogonal projection `(Y_1,Y_2)` of the independent cap-one `L`-bank has density cap at most `2`, and the same is true for `(Z_1,Z_2)`. The determinant-one shears preserve those caps. The physical hub `X_i` has density cap at most `1`. Hence Lemma 2.1 applies with

\[
K_H=1,\qquad M_Y=M_Z=2,
\qquad
\alpha=\|c\|,
\quad\beta=\|r\|,
\quad |\sigma|=\|C\|_F.
\]

Since `(\alpha\beta\sigma)^2=T`, (3.5)--(3.7) follow.

Finally average over the conditioned outside coordinates. The bound is uniform in all induced affine terms and same-bank phases, while the coefficients `c,r,N,a` are deterministic entries of `A`; thus the unconditional law obeys the same estimate. QED.

### Why this is a genuine new scope extension

The preceding physical application of the tensor lemma in account02/B02 imposed `A_{ii}=0` because its geometric partner identity for an overlap packet was proved at the literal zero-pivot endpoint. The analytic tensor lemma itself never needed that hypothesis. Theorem 3.1 separates these issues: the hub square is retained exactly in `F_H`, so an arbitrarily small or large nonzero pivot costs nothing in this rank-one-crossing receiver.

This does **not** invoke the invalid rule “a small nonzero term may be deleted.” The term is not deleted; it remains inside the unit-modulus hub phase throughout the Fourier operator estimate.

## 4. Application to the r43 unique-heavy-row/two-star survivor

Take the two disjoint original-coordinate star banks `B_1,B_2` from (1.1), and set

\[
c=A[B_1,i],\qquad r=A[i,B_2],\qquad N=A[B_1,B_2].
\tag{4.1}
\]

Then

\[
\|c\|>\theta_0s,
\qquad
\|r\|>\theta_0s.
\tag{4.2}
\]

Suppose this actual interbank crossing has

\[
\operatorname{rank}N=1,
\qquad
\|P_cNP_r\|_F\ge \nu s
\tag{4.3}
\]

for some `\nu>0`. Theorem 3.1 gives

\[
T
=\|c\|^2\|r\|^2\|P_cNP_r\|_F^2
>\theta_0^4\nu^2s^6.
\tag{4.4}
\]

Therefore

\[
\boxed{
\|p_Q\|_\infty
<3\,2^{2/3}\theta_0^{-2/3}\nu^{-1/3}\,s^{-1}
<120.992\,\nu^{-1/3}s^{-1}.
}
\tag{4.5}
\]

This branch has a continuous `C_0` density.

Thus the arbitrary small physical pivot in the r43 punctured collar is no longer an obstacle whenever the two diffuse star banks carry a rank-one interbank crossing with quantitative component transverse to both star directions.

What remains of this r43 endpoint is narrower:

1. a genuinely rank-two-or-higher interbank crossing for which the current rank-one tensor shear does not factor exactly; or
2. a rank-one crossing whose doubly projected transverse coefficient `\|P_cNP_r\|_F` is arbitrarily small/zero, so the two star banks share essentially the same hub direction and do not themselves supply the third smoothing resource.

The second survivor is consistent with the account02/B11 obstruction: two star banks attached to one hub are still only rank two until some same-bank curvature, transverse crossing, pair area, or rank-three volume is spent.

## 5. Designated account04/B11 result applied to an actual inequality

The current hard chamber reaches Section 4 only after removing the multi-heavy-row branch. Here is the actual partner application used for that gate.

If two distinct physical rows `i,j` in the selected rank-three `H`-space satisfy

\[
q_i>3/4,\qquad q_j>3/4,
\]

then the projection calculation from r43 gives

\[
\|z_i\wedge z_j\|^2>\frac12.
\]

Since the spectral coordinate map on this bank has squared least singular scale `>\beta_0`, the actual physical pair satisfies

\[
g_{ij}=\|r_i\wedge r_j\|^2>\frac{\beta_0^2}{2}.
\tag{5.1}
\]

Applying the completed designated account04/B11 inequality (1.2) at (5.1),

\[
\boxed{
\|p_Q\|_\infty
<\frac{256}{\beta_0s}
=\frac{14158.83737024\ldots}{s}.
}
\tag{5.2}
\]

Hence the new rank-one shared-hub theorem is needed only after the designated-partner pair-area branch has forced the survivor to have a unique heavy row.

## 6. Opposite-sign rank-two control and the third-direction mechanism

For independent centered unit uniforms `X,Y`,

\[
p_{2XY}(t)=\log\frac1{2|t|},
\qquad 0<|t|<1/2,
\tag{6.1}
\]

so an opposite-sign rank-two saddle has a genuine logarithmic density singularity.

Theorem 3.1 identifies exactly how a third direction removes it in the present rotated/product setting. The shared physical hub coupled to one scalar projection on each side generates the rank-two hyperbolic operator with `|t|^{-1}` norm. A source-disjoint transverse bilinear crossing gives an additional `|t|^{-1/2}` Plancherel factor. Their product is `|t|^{-3/2}`, which is integrable. The hub square may be present with any coefficient because it is retained as a phase and does not change the operator norm.

This is a genuinely product-preserving mechanism: all independence is between literal disjoint original-coordinate banks, never between spectral coordinates.

## 7. Current first unpaid implication

The next B11 target is

`QFORM-R43-NONRANKONE-OR-ALIGNED-SHAREDHUB-CURVATURE-v1`:

inside the unique-heavy-row/two-star chamber, either

- extend the tensor receiver to a genuinely rank-two-or-higher interbank block with a bound uniform as its extra singular values tend to zero; or
- if `P_cNP_r` is small/aligned, combine the quantitative same-bank internal curvature retained by r42/r43 with the shared-hub star structure before conditioning or taking absolute values.

The proof must retain every small nonzero term, arbitrary fragmented cap-one laws, and original-coordinate product provenance. Two star banks alone cannot be counted as two independent hubs.

Even a complete resolution of this exact-rank-three collar would leave the separate bridge to arbitrary additional nonseparable spectrum. Full-target continuity likewise remains open.
