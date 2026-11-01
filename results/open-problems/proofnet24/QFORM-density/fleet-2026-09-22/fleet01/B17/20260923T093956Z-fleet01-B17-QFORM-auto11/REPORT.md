SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B17, 2026-09-23T09:39:56.766093Z.
attacking: exact tetrahedral-cube signature rotations; optimize the negative eigendirection and derive a stronger finite analytic witness, then apply fleet02/B17's completed uniform-bank theorem to the same core.

# QFORM B17 — an out-of-plane tetrahedral signature rotation gives a stronger exact finite witness

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T093956Z-fleet01-B17-QFORM-auto11`  
Classification: **SUPPORTING_SHARP-WITNESS_THEOREM**  
Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains separate.  
Execution context: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source-valid premises and corrections

This run uses the exact product-provenance tetrahedral projection established in the preceding B17 report

`yspennstate/math-open-problems@4e2b1356186ad8b35a1626dc5bb6c739f7259805`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B17/20260923T090822Z-fleet01-B17-QFORM-auto11/REPORT.md`.

For

\[
R=\frac12\begin{pmatrix}
1&1&1\\
1&-1&1\\
1&1&-1\\
1&-1&-1
\end{pmatrix},\qquad R^TR=I_3,
\]

and independent physical inputs `X_i ~ Unif[-1/2,1/2]`, the exact spectral marginal of `Y=R^T X` is

\[
\rho(y)=2\bigl(1-M_1(y)-M_2(y)\bigr)_+,
\tag{1.1}
\]

where `M_1>=M_2>=M_3` are the ordered absolute coordinates. This identity comes from integrating the original product cube along the one-dimensional null fibre. It does **not** invoke an arbitrary-joint coarea theorem or post-rotation independence.

The source-valid target-level lower obstruction remains

\[
C_{\rm univ}\ge 3\sqrt2,
\tag{1.2}
\]

from the diffuse block-CLT construction in

`yspennstate/math-open-problems@8624982153e5a2154e4ae8922d2fe4dc77080efc`.

The current live correction inbox was reread before publication. In particular, this proof does not use the refuted arbitrary-joint coarea bound, refuted positive conditional-density moments, post-rotation independence, a fixed fragment-count reduction, or law-uniform pointwise oscillatory decay.

## 2. Exact rational out-of-plane rotation

The preceding one-parameter experiment rotated the negative eigendirection inside the first two spectral coordinates. Here move it genuinely out of that plane. Choose

\[
n_* = \frac{(5,5,2)}{\sqrt{54}},
\qquad
B_* = I_3-2n_*n_*^T.
\tag{2.1}
\]

Because the normalization cancels, the core is the exact rational matrix

\[
\boxed{
B_* = \frac1{27}
\begin{pmatrix}
2&-25&-10\\
-25&2&-10\\
-10&-10&23
\end{pmatrix}.}
\tag{2.2}
\]

Direct exact arithmetic gives `B_*^2=I_3` and `tr B_*=1`; hence

\[
\operatorname{spec}(B_*)=\{1,1,-1\}.
\tag{2.3}
\]

Set

\[
A_* = R B_* R^T.
\]

Then

\[
\boxed{
A_*=\frac1{108}
\begin{pmatrix}
-63&3&-69&-3\\
3&77&-43&31\\
-69&-43&17&43\\
-3&31&43&77
\end{pmatrix}.}
\tag{2.4}
\]

Every physical entry is nonzero, and since `R^TR=I_3`,

\[
\operatorname{spec}(A_*)=\{1,1,-1,0\}.
\tag{2.5}
\]

Thus this is an exact finite target matrix with three eigenvalues of modulus one. It uses exactly the same physical product cube, range projection `RR^T`, and physical row leverages `3/4` as the earlier axis and 45-degree signature orientations. Only the signature orientation inside the same three-dimensional range has changed.

## 3. Exact cone-tip representation

Choose an orthonormal positive basis perpendicular to `n_*`:

\[
e_1=\frac{(1,-1,0)}{\sqrt2},
\qquad
e_2=\frac{(1,1,-5)}{3\sqrt3}.
\tag{3.1}
\]

The unit cone ray on one nappe is

\[
\omega(\theta)=\frac{n_*+\cos\theta\,e_1+\sin\theta\,e_2}{\sqrt2},
\qquad 0\le\theta<2\pi.
\tag{3.2}
\]

Then `|omega|=1` and `omega^T B_* omega=0`. Its coordinates are

\[
\begin{aligned}
\omega_1(\theta)&=\frac5{6\sqrt3}+\frac{\cos\theta}{2}+\frac{\sin\theta}{3\sqrt6},\\
\omega_2(\theta)&=\frac5{6\sqrt3}-\frac{\cos\theta}{2}+\frac{\sin\theta}{3\sqrt6},\\
\omega_3(\theta)&=\frac1{3\sqrt3}-\frac{5\sin\theta}{3\sqrt6}.
\end{aligned}
\tag{3.3}
\]

Let

\[
H(x)=\text{sum of the two largest numbers among }|x_1|,|x_2|,|x_3|.
\tag{3.4}
\]

For `y=s omega(theta)`, (1.1) becomes `rho(y)=2(1-sH(omega(theta)))_+`. In Lorentz polar coordinates, the coarea factor on either nappe, with `s=|y|`, is `ds dtheta/(2sqrt2)`. The two nappes have equal mass by central symmetry. Hence the density at the cone tip is exactly

\[
\boxed{
 p_*(0)=\frac1{\sqrt2}\int_0^{2\pi}
 \frac{d\theta}{H(\omega(\theta))}.}
\tag{3.5}
\]

This is an exact one-dimensional integral for a finite product-law QFORM witness.

## 4. Rigorous interval certificate: p_*(0) > 89/25

The function `H` admits the representation

\[
H(x)=\max_{1\le i<j\le3}\max_{\varepsilon_i,\varepsilon_j\in\{\pm1\}}
(\varepsilon_i x_i+\varepsilon_jx_j).
\tag{4.1}
\]

Every linear functional in (4.1) has Euclidean norm `sqrt(2)`, so `H` is `sqrt(2)`-Lipschitz. From (3.2),

\[
|\omega'(\theta)|=\frac1{\sqrt2}.
\]

Therefore

\[
h(\theta):=H(\omega(\theta))
\quad\text{is 1-Lipschitz.}
\tag{4.2}
\]

Partition `[0,2pi]` into `N=20000` equal subintervals of length `Delta=2pi/N`, and let `theta_k` be each midpoint. For `theta` in the kth subinterval,

\[
h(\theta)\le h(\theta_k)+\frac\Delta2,
\]

so

\[
\int_{I_k}\frac{d\theta}{h(\theta)}
\ge\frac{\Delta}{h(\theta_k)+\Delta/2}.
\tag{4.3}
\]

The accompanying interval-arithmetic checker evaluates (3.3) with directed enclosures and applies (4.3). It proves

\[
\boxed{
3.56028975295842053938599747198
\le p_*(0)\le
3.56119321242131681160003608966.}
\tag{4.4}
\]

In particular,

\[
\boxed{p_*(0)>\frac{89}{25}=3.56.}
\tag{4.5}
\]

This is a certified lower bound, not a histogram or floating-point optimizer.

## 5. It strictly improves the preceding exact finite orientation witness

The preceding 45-degree in-plane orientation had the exact global peak

\[
4\log(1+\sqrt2)=3.525494348078172\ldots.
\tag{5.1}
\]

The certified lower endpoint in (4.4) gives

\[
\boxed{
 p_*(0)>3.56028\ldots>4\log(1+\sqrt2).}
\tag{5.2}
\]

Thus the 45-degree orientation is not even extremal within this natural tetrahedral product projection once the negative eigendirection is allowed to leave its original coordinate plane.

At the same time,

\[
p_*(0)<3.56120<3\sqrt2=4.242640687119\ldots.
\tag{5.3}
\]

Therefore this new finite witness does **not** improve the strongest known target-level lower obstruction (1.2). Its role is structural: same spectrum, same range projection, same row leverage, and same product cube can yield substantially different high-leverage finite peaks solely from the orientation of the positive/negative signature.

The exact chain now includes

\[
8(\sqrt2-1)=3.313708\ldots
<4\log(1+\sqrt2)=3.525494\ldots
<p_*(0),
\tag{5.4}
\]

with all three matrices sharing the nonzero spectrum `{1,1,-1}` and the same tetrahedral physical range.

## 6. Designated fleet02/B17 theorem applied to this actual core

The completed partner theorem used here is

`yspennstate/math-open-problems@fefb4cf4f0af17c810341152311c3822c78d5b7f`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B17/20260923T082513Z-fleet02-B17-QFORM-r12/UNIFORM_EXTENSION.md`.

It proves that there is one deterministic `Delta_m -> 0` such that for every symmetric `3x3` core `C_m` with `s_3(C_m)>=1`, every normalized three-bank interval frame `P_m`, and arbitrary independent translations of all physical unit intervals,

\[
\|p_{X^TP_mC_mP_m^TX}\|_\infty\le3\sqrt2+\Delta_m.
\tag{6.1}
\]

For canonical spectrum `{1,1,-1}`, centered banks attain the `3sqrt(2)` limit.

Apply (6.1) to the **actual matrix from this run**, `C_m=B_*` for every `m`. Since `B_*^2=I_3`, `s_3(B_*)=1`. Thus

\[
\boxed{
\|p_{X^TP_mB_*P_m^TX}\|_\infty\le3\sqrt2+\Delta_m,
\qquad \Delta_m\to0,}
\tag{6.2}
\]

uniformly over independent translations. For centered banks,

\[
\boxed{
\lim_{m\to\infty}
\|p_{X^TP_mB_*P_m^TX}\|_\infty=3\sqrt2.}
\tag{6.3}
\]

Combining the new finite certificate with the partner theorem gives the concrete inequality

\[
\boxed{
\frac{89}{25}<p_*(0)<3\sqrt2
=\lim_{m\to\infty}\|p_{X^TP_mB_*P_m^TX}\|_\infty.}
\tag{6.4}
\]

So moving the negative eigendirection out of the earlier plane makes the four-coordinate all-heavy core more dangerous, but diffuse Gaussianisation of the **same signature core** is still strictly worse. The partner theorem additionally rules out arbitrary independent translations of the unit-smoothed diffuse comparator as an asymptotic escape mechanism.

For context, the other completed fleet02/B17 finite-bank theorem gives

\[
C_{\rm bank}=\frac{\pi\sqrt2}{3}\left(1+\frac4{\sqrt5}\right)
=4.1301845169\ldots<3\sqrt2
\tag{6.5}
\]

for the one-heavy majority-sign equal-bank branch. The checker verifies (6.5), but (6.2)-(6.4) are the partner result actually applied to the present witness.

## 7. What this constrains, and what remains open

The new witness rules out any proposed *sharp finite* invariant that depends only on the nonzero eigenvalue multiset and the coordinate leverages of the spectral range. Those data are identical across the three tetrahedral orientations in (5.4), while their peaks differ. Signature orientation inside the product projection must be retained.

This run does not prove that `p_*(0)` is the global mode for the new out-of-plane orientation; only the cone-tip value is certified. It makes no new full-target continuity claim. It does not prove that `3sqrt(2)` is the unrestricted sharp universal constant. The strongest known target-level lower bound remains `C_univ>=3sqrt(2)`.

The next sharp-witness search should therefore focus on genuinely non-tetrahedral shared-coordinate heavy geometries or multiscale mixtures that can beat the diffuse comparator, rather than further in-plane rotations or one-heavy equal-bank families already excluded by the completed partner results.

## 8. Checker

`qform_b17_tetra_outofplane_check.py` performs exact rational matrix checks and directed interval quadrature. Its saved output begins

```
QFORM_B17_TETRA_OUTOFPLANE_CHECK_PASS
tip_interval=[3.56028975295842053938599747198, 3.56119321242131681160003608966]
rational_lower=89/25
old_45_interval=[3.52549434807817219095227301295, 3.52549434807817219095227301295]
partner_bank_interval=[4.13018451693174881711456691846, 4.13018451693174881711456691846]
3sqrt2_interval=[4.24264068711928477029005080112, 4.24264068711928477029005080112]
```

The privacy/secret review for the changed-file allowlist is a narrow local fallback scan only; it found no credential-like material. No public release, remote workflow, paid call, permission change, email, notification change, new task, or schedule mutation was performed.
