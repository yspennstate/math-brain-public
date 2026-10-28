SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B14, 2026-09-23T23:39:29Z.
attacking: overlapping third-resource localization after the zero-loss connected-support reduction; first test whether smooth connected support repairs the interval-only rough-hub receiver.

# account03/B14 — smooth connected support does not repair the interval-only rough-hub receiver

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260923T233929Z-account03-B14-QFORM-auto11`  
**Status:** `RIGOROUS COUNTEREXAMPLE TO AN INTERMEDIATE LOCALIZATION INTERFACE / PARTNER TARGET BRANCH APPLIED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** the counterexample outputs below have continuous densities; full-target continuity remains open.

## 1. Why this implication is the first missing one

The preceding B14 run proved a zero-loss closure reduction: for purposes of a universal interval-density constant, arbitrary cap-one product laws can be approximated by smooth strict-subcap laws whose support is a single finite interval, but with no uniform bound on interval length or positive density floor. That reduction does **not** license proofs that use connectedness quantitatively unless the estimate is uniform as the bridge density tends to zero and the interval diameter tends to infinity.

An earlier B14 correction already showed that an interval-only frozen-slice estimate

\[
\mu_l(I)\lesssim |I|^{1/2}
\]

cannot by itself control a rough hub of the form `2LX+Y`; the original example used visibly separated fragments. The essential question after the connected-support reduction is therefore whether filling those gaps by a tiny positive bridge and smoothing eliminates the obstruction.

It does not. The theorem below gives a smooth, positive-on-one-interval, strict-subcap counterexample with a uniform frozen-slice half-Frostman constant, while the rough-hub output density at zero diverges logarithmically along the family.

This refutes only the intermediate receiver inference. The associated quadratic matrix has only two eigenvalues of modulus at least one, so it is **not** a counterexample to the owner QFORM conjecture.

## 2. Smooth connected-support construction

Fix

\[
0<\varepsilon<\frac18,
\qquad
N=\left\lceil\frac2\varepsilon\right\rceil.
\tag{2.1}
\]

Define the separated unit-measure set

\[
E_N=\bigcup_{k=1}^N[4k,4k+N^{-1}],
\qquad |E_N|=1,
\tag{2.2}
\]

and its convex hull

\[
H_N=[4,4N+N^{-1}],
\qquad
L_N:=|H_N|=4(N-1)+N^{-1}\ge 2N.
\tag{2.3}
\]

Put

\[
f_N^0(x)=\frac34\mathbf 1_{E_N}(x)+\frac1{4L_N}\mathbf 1_{H_N}(x).
\tag{2.4}
\]

Then `f_N^0` is a probability density and

\[
\|f_N^0\|_\infty=\frac34+\frac1{4L_N}<1.
\tag{2.5}
\]

The second summand is the low bridge joining every distant component. Thus the essential support is already the single interval `H_N`; its bridge height tends to zero and its diameter tends to infinity as `N` grows.

### Lemma 2.1 — interval concentration of the bridged law

For every interval `J` of length `r`,

\[
\boxed{
\int_J f_N^0(x)\,dx
\le \frac{7\sqrt2}{8}\sqrt{\frac rN}.
}
\tag{2.6}
\]

**Proof.** If `r<=4`, the interval meets at most two components of `E_N`, hence

\[
|E_N\cap J|\le \min\{r,2/N\}\le \sqrt{2r/N}.
\tag{2.7}
\]

If `r>4`, it meets at most `r/4+2 <=3r/4` components, so

\[
|E_N\cap J|\le \min\{1,3r/(4N)\}\le \sqrt{3r/(4N)}\le\sqrt{r/N}.
\tag{2.8}
\]

Thus in all cases `|E_N cap J| <= sqrt(2r/N)`. Also, by `L_N>=2N`,

\[
\frac{|H_N\cap J|}{L_N}
\le \min\{r/(2N),1\}
\le \sqrt{r/(2N)}.
\tag{2.9}
\]

Insert (2.7)--(2.9) into (2.4):

\[
\int_Jf_N^0
\le \frac34\sqrt{\frac{2r}{N}}
 +\frac14\sqrt{\frac r{2N}}
=\frac{7\sqrt2}{8}\sqrt{\frac rN}.
\]

QED.

Now convolve with a nonnegative compactly supported `C^infty` probability mollifier `rho_delta`, positive on the interior of its support. Choose `delta=delta_N>0` so small that

\[
f_N=f_N^0*\rho_{\delta_N}
\qquad\text{satisfies}\qquad
\|f_N\|_2^2\ge\frac12.
\tag{2.10}
\]

This is possible because mollification converges in `L^2` and

\[
\|f_N^0\|_2^2\ge (3/4)^2|E_N|=9/16.
\tag{2.11}
\]

Then `f_N` is a `C_c^infty` probability density, positive throughout the interior of one compact interval, and

\[
0\le f_N<1.
\tag{2.12}
\]

Mollification preserves (2.6) with the **same constant**, since for every interval `J`,

\[
\int_J f_N(x)dx
=\int \rho_{\delta_N}(u)
   \left(\int_{J-u}f_N^0(x)dx\right)du
\le \frac{7\sqrt2}{8}\sqrt{\frac{|J|}{N}}.
\tag{2.13}
\]

For the hub-slope variable, let

\[
g_\varepsilon^0(l)=\frac34\mathbf 1_{[\varepsilon,\,\varepsilon+4/3]}(l),
\tag{2.14}
\]

and set

\[
g_\varepsilon=g_\varepsilon^0*\kappa_{\varepsilon/8},
\tag{2.15}
\]

where `kappa_{eps/8}` is again a nonnegative compactly supported smooth probability mollifier, positive in its support interior. Then `g_epsilon` is a `C_c^infty` probability density, positive on one interval,

\[
0\le g_\varepsilon\le 3/4<1,
\tag{2.16}
\]

its support is contained in

\[
[7\varepsilon/8,\,\varepsilon+4/3+\varepsilon/8],
\tag{2.17}
\]

and exactly

\[
g_\varepsilon(l)=3/4
\quad\text{for }l\in
[\varepsilon+\varepsilon/8,\,\varepsilon+4/3-\varepsilon/8].
\tag{2.18}
\]

In particular, for `epsilon<1/8`,

\[
g_\varepsilon(l)=3/4\qquad(2\varepsilon\le l\le1).
\tag{2.19}
\]

## 3. Uniform smooth connected frozen slices

Let `X,X',L` be independent with densities `f_N,f_N,g_epsilon`, respectively. Define

\[
Y=-2LX',
\qquad
T=2LX+Y=2L(X-X').
\tag{3.1}
\]

For frozen `l`, let the **unnormalised** `Y`-slice be

\[
\nu_l(B)=g_\varepsilon(l)\Pr\{-2lX'\in B\}.
\tag{3.2}
\]

For every `l` in the support of `g_epsilon`, `nu_l` has a smooth density positive on one compact interval. Nevertheless all slices satisfy one law-uniform interval estimate.

### Theorem 3.1 — `QFORM-SMOOTH-CONNECTED-SLICE-ROUGH-HUB-FALSE-v1`

For every interval `I`, every `epsilon` above, and every frozen `l`,

\[
\boxed{
\nu_l(I)\le \frac{3\sqrt7}{16}|I|^{1/2}<\frac12|I|^{1/2}.
}
\tag{3.3}
\]

At the same time the output density of `T` is continuous and

\[
\boxed{
p_T(0)\ge \frac3{16}\log\frac1{2\varepsilon}\longrightarrow\infty
\quad(\varepsilon\downarrow0).
}
\tag{3.4}
\]

Hence no universal `L^infinity` rough-hub receiver can follow only from a uniform interval half-Frostman bound, even if **all input densities and all frozen slice densities are smooth, strict-subcap, compactly supported, positive on connected interval interiors**.

**Proof of (3.3).** Let `s=|I|`. The inverse image of `I` under `x mapsto -2lx` is an interval of length

\[
r=\frac{s}{2l}.
\tag{3.5}
\]

Since `N>=2/epsilon` and `l>=7epsilon/8`,

\[
\frac1N\le\frac\varepsilon2\le\frac{4l}{7}.
\tag{3.6}
\]

Thus

\[
\frac rN=\frac{s}{2lN}\le\frac{2s}{7}.
\tag{3.7}
\]

Using `g_epsilon(l)<=3/4` and (2.13),

\[
\nu_l(I)
\le \frac34\frac{7\sqrt2}{8}\sqrt{\frac rN}
\le \frac34\frac{7\sqrt2}{8}\sqrt{\frac27}\,\sqrt s
=\frac{3\sqrt7}{16}\sqrt s.
\]

This proves (3.3).

**Proof of (3.4).** Put `D=X-X'`. Since `f_N` is smooth and compactly supported, `D` has a continuous density and

\[
p_D(0)=\int f_N(x)^2dx=\|f_N\|_2^2\ge\frac12.
\tag{3.8}
\]

Because `L>0`, conditioning on `L=l` gives

\[
p_{T\mid L=l}(0)=\frac{p_D(0)}{2l}.
\tag{3.9}
\]

Using the exact plateau (2.19),

\[
\begin{aligned}
p_T(0)
&=p_D(0)\int\frac{g_\varepsilon(l)}{2l}\,dl\\
&\ge\frac12\int_{2\varepsilon}^1\frac{3/4}{2l}\,dl
=\frac3{16}\log\frac1{2\varepsilon}.
\end{aligned}
\tag{3.10}
\]

For every fixed `epsilon`, the support of `L` is bounded away from zero, so the representation

\[
p_T(t)=\int g_\varepsilon(l)\frac1{2l}
            p_D\!\left(\frac{t}{2l}\right)dl
\tag{3.11}
\]

and dominated convergence also show that `p_T` is continuous. QED.

For any prescribed `M<infinity`, choosing

\[
\varepsilon<\frac12e^{-16M/3}
\tag{3.12}
\]

forces `p_T(0)>M` while preserving the slice constant in (3.3).

## 4. Scope guard: this is not a QFORM counterexample

In the original variables `(L,X,X')`,

\[
T=2LX-2LX'
\]

has homogeneous matrix

\[
A_2=
\begin{pmatrix}
0&1&-1\\
1&0&0\\
-1&0&0
\end{pmatrix},
\tag{4.1}
\]

with spectrum

\[
\{\sqrt2,-\sqrt2,0\}.
\tag{4.2}
\]

Thus only two eigenvalues have modulus at least one. The construction proves the failure of an intermediate localization/receiver principle and **does not disprove** the three-large-eigenvalue conjecture.

Its role is to prevent a subtle but tempting misuse of the preceding connected-support reduction: the tiny positive bridge that makes a fragmented law connected does not supply a quantitative anti-concentration floor. As that bridge tends to zero and the diameter grows, the same logarithmic rank-two rough-hub obstruction survives smoothly.

## 5. Designated partner result applied at an actual target inequality

The completed partner theorem actually used is account04/B14 r7:

- repository/commit: `yspennstate/math-open-problems@2ac84e141e8e939506cbd5cd8314589141b714d5`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260923T051013Z-account04-B14-scale-shear-r7/REPORT.md`;
- theorem: `QFORM-SCALE-COVARIANT-CONJUGATE-SHEAR-v1`.

Its direct small-ball/physical-pair proof is uniform in translations, support diameter and fragmentation and does not use the invalid interval-only rough-hub endpoint.

Apply it to four independent copies `X_1,...,X_4` of the **same smooth connected strict-subcap stress law** `f_N` above, with

\[
c=d=1,\qquad \alpha=0,\qquad \beta=0,
\qquad \ell_1=\ell_2=\gamma=0.
\tag{5.1}
\]

Then

\[
Q_N=2X_1X_2+\frac12(X_3+X_4)^2.
\tag{5.2}
\]

The homogeneous matrix is the orthogonal sum of the hyperbolic pair and the rank-one square block, with nonzero spectrum

\[
\{1,-1,1\}.
\tag{5.3}
\]

So this is genuinely inside the owner target. Account04/B14 r7 gives the concrete inequality

\[
\boxed{
\|p_{Q_N}\|_{\infty,\mathrm{ess}}
\le 4+2\log8
=8.158883083359672\ldots
}
\tag{5.4}
\]

uniformly in `N`, hence uniformly while

- the bridge height `1/(4L_N)` tends to zero;
- the connected support diameter grows like `4N`;
- the former fragment separation stays macroscopic;
- the smoothing scale tends to zero arbitrarily;
- no moment or centering bound is available uniformly.

Thus the third spectral resource **does** control this same low-bridge connected-support stress when it is paid by a valid joint shear/small-ball mechanism. The pathology in Sections 2--4 isolates the invalid proof interface rather than the QFORM target.

## 6. Consequence for localization strategy

The previous zero-loss connected-support reduction remains valid, but its correct interpretation is now sharper:

> One may reduce to smooth positive connected-support strict-subcap marginals only as a closure device. No universal lower bound on the bridge density, no bounded diameter, and no Borel-set profile may be inferred from connectedness. In particular, interval-only half-Frostman control of frozen slices still cannot be upgraded to a rough-hub `L^infinity` receiver.

Therefore the overlapping third-resource step must retain at least one of:

1. the coupled slice phase and integrate it before absolute values;
2. a direct small-ball/shear argument such as the partner r7 mechanism;
3. an exponent-matched `L^p` core convolved with a genuine third independent physical resource;
4. a product-provenance aggregate that pays the third curvature before normalized fiber conditioning.

The construction here shows that merely smoothing and filling the gaps cannot replace that missing geometry.

## 7. Status

- `QFORM-SMOOTH-CONNECTED-SLICE-ROUGH-HUB-FALSE-v1`: **PROVED as an intermediate-interface counterexample**.
- Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.
- Full-target continuity: **OPEN**.
- Partner application: **completed at equation (5.4)**.
- No Gaussian, moment, log-concavity, bounded-diameter, fixed-fragment, rotation-independence, arbitrary-joint coarea, or pointwise van-der-Corput premise is used.
