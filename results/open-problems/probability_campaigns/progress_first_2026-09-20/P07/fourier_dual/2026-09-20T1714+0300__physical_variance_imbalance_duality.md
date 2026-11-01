Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED** — GPT-6 / maximum was requested as an owner preference, but this runtime exposes no authenticated completed-run effort telemetry or binding model/effort selector, so I do not claim otherwise.

# P07-B — exact physical-space variance-imbalance duality for the quadratic Fourier obstruction

**Status:** **OPEN / PROVED PARTIAL** on Randomstrasse101 Conjecture 18.  
**Native role:** `P07-B`, task `6aabe797a39081919acc889f29f4c556`.  
**Repository / branch:** private `yspennstate/math-open-problems` / `master`.  
**Fresh pre-write master:** `c5e8719a1679f92520ab12e716351454cea3e12f`.  
**Previous own substantive report:** `probability_campaigns/progress_first_2026-09-20/P07/fourier_dual/2026-09-20T1610+0300__quadratic_energy_concentration_collision_reduction.md`.  
**Latest complementary P07-A checkpoint read:** `probability_campaigns/progress_first_2026-09-20/P07/primal/2026-09-20T1647+0300__complement_reduced_cost_leakage.md`. P07-A owns the primal/support/reduced-cost route; this report stays on the Fourier-dual quadratic interpolation obstruction.

**Outside target:** Bandeira et al., *Randomstrasse101: Open Problems of 2025*, arXiv:2603.29571, Conjecture 18.  
**Primary partial result:** A. S. Bandeira, J. Błasiok, D. Dmitriev, U. Faure, A. Kireeva, D. Kunisky, *The Lovász number of random circulant graphs*, arXiv:2502.16227.  
**Exact source endpoint:** for the dense random undirected circulant model,
\[
\mathbb E\vartheta(G_n)=(1+o(1))\sqrt n.
\]
The inherited rigorous source bound remains
\[
\sqrt n\le \mathbb E\vartheta(G_n)\le C\sqrt{n\log\log n},
\]
so the fixed full-source metric is still
\[
\boxed{\alpha_{LL}=1/2\to1/2.}
\]
No new arbitrary-`n` theta asymptotic is claimed here.

The assignment-time source check, exact Fourier LP, and old repository attempts were already recovered once and are not rerun. The inherited normalization is
\[
\kappa_D=\frac1{n\delta_D},\qquad
\mathbb E\vartheta(G_n)=1+\mathbb E\frac1{\delta_D}.
\tag{0.1}
\]
The current route is still `QBI -> analytic remainder -> TRBI -> E theta=O(sqrt n)`. The previous report reduced `QBI` to a simultaneous high-collision, mesoscopically delocalized class. This run changes the representation of that class: the quadratic dual numerator is exactly a **difference of two same-mask conditional variances** of the physical Fourier field. That is a more rigid object than an arbitrary quadratic correlation.

---

## 1. Inherited quadratic target and notation

Let
\[
M=\{1,\ldots,m\},\qquad m=(n-1)/2,
\]
let
\[
\varepsilon_a=2\mathbf1_{\{a\in D\}}-1,
\]
and extend the mask evenly to `Z_n` by
\[
Y(0)=0,\qquad Y(a)=Y(-a)=\varepsilon_a\quad(a\in M).
\tag{1.1}
\]
Use unnormalized cyclic convolution and Fourier transform
\[
(u*v)(a)=\sum_{b\in\mathbb Z_n}u(b)v(a-b),
\qquad
\widehat u(j)=\sum_{a\in\mathbb Z_n}u(a)e^{2\pi iaj/n}.
\tag{1.2}
\]
Put
\[
W=Y*Y.
\tag{1.3}
\]
The preceding reports proved that the transverse second derivative of the radial Gibbs moment vector is
\[
\boxed{
r_D''(0)=\frac1{16(n-1)}
\left(W_D-\overline W_D\mathbf1_D\right).
}
\tag{1.4}
\]
For a transverse test `z` supported on `D`,
\[
\sum_{a\in D}z_a=0,
\tag{1.5}
\]
define
\[
f_z(j)=\sum_{a\in D}z_a\cos(2\pi aj/n),
\qquad j\in\mathbb Z_n,
\tag{1.6}
\]
and let `q_0` be the uniform law on `Z_n\setminus{0}`. The exact frame identity is
\[
\boxed{
\|f_z\|_{L^2(q_0)}^2
=\lambda_n\|z\|_2^2,
\qquad
\lambda_n=\frac{n}{2(n-1)}.
}
\tag{1.7}
\]
The dual denominator is
\[
N(z):=\mathbb E_{q_0}|f_z|.
\tag{1.8}
\]
Finally introduce the normalized physical mask field
\[
\boxed{
G_D(j):=\frac{\widehat Y(j)}{\sqrt n}
=\frac2{\sqrt n}\sum_{a\in M}\varepsilon_a\cos(2\pi aj/n).
}
\tag{1.9}
\]
This is the same source mask; no independent Fourier-coordinate model is introduced.

---

# 2. New exact theorem: the quadratic dual numerator is `E[f G^2]/16`

## Theorem P07-B.24 — physical-space representation and two exact cancellations

For every odd `n`, every realized source mask, and every transverse `z` supported on `D`,
\[
\boxed{
\langle r_D''(0),z\rangle
=\frac1{16}\,\mathbb E_{q_0}\bigl[f_zG_D^2\bigr].
}
\tag{2.1}
\]
Moreover
\[
\boxed{
\mathbb E_{q_0}f_z=0,
\qquad
\mathbb E_{q_0}[f_zG_D]=0.
}
\tag{2.2}
\]
Thus the quadratic obstruction is exactly the first physical moment of `G_D` that survives against every selected transverse test.

### Proof

Extend `z` evenly to a vector `Z` on `Z_n` by `Z(0)=0` and `Z(+-a)=z_a`. Then
\[
\widehat Z(j)=2f_z(j).
\tag{2.3}
\]
Since `W=Y*Y`,
\[
\widehat W(j)=\widehat Y(j)^2=nG_D(j)^2.
\tag{2.4}
\]
Parseval gives
\[
\sum_{k\in\mathbb Z_n}Z(k)W(k)
=\frac1n\sum_{j\in\mathbb Z_n}\widehat Z(j)\widehat W(j)
=2\sum_j f_z(j)G_D(j)^2.
\tag{2.5}
\]
The left side equals `2 sum_{a in D} z_a W_a`, so
\[
\sum_{a\in D}z_aW_a=\sum_jf_z(j)G_D(j)^2.
\tag{2.6}
\]
The mean-removal term in (1.4) vanishes by (1.5), while `f_z(0)=sum z_a=0`; dividing (2.6) by `16(n-1)` proves (2.1).

For the first cancellation, for every nonzero frequency `a`,
\[
\sum_{j\ne0}\cos(2\pi aj/n)=-1,
\]
so (1.5) gives `E f_z=0`.

For the second, folded Fourier orthogonality gives
\[
\mathbb E_{q_0}\bigl[\cos(2\pi aj/n)\cos(2\pi bj/n)\bigr]
=\frac{\frac n2\mathbf1_{a=b}-1}{n-1}.
\tag{2.7}
\]
Therefore
\[
\mathbb E[f_zG_D]
=\frac{\sqrt n}{n-1}\sum_{a\in D}z_a\varepsilon_a.
\tag{2.8}
\]
On the support of `z`, `epsilon_a=+1`; hence the last sum is `sum z_a=0`. This proves (2.2). `square`

### A second exact structure: selected tests are convolution eigenfunctions

The same support condition gives another identity that will matter for a dependence-aware small-ball argument. Pointwise in frequency,
\[
YZ=Z
\tag{2.9}
\]
because `Z` is supported only where `Y=+1`. Fourier transforming the product and using (2.3) gives, with unnormalized convolution in the time variable,
\[
\boxed{
G_D*f_z=\sqrt n\,f_z.
}
\tag{2.10}
\]
So the dual witnesses appearing in (2.1) are not arbitrary functions that can choose their support after seeing `G_D`: they are exact eigenfunctions of convolution by the **same field** whose square occurs in the numerator. This is a precise way to retain the source dependence rather than replacing the Fourier coordinates by independent Gaussians.

---

# 3. New exact variance-imbalance formula

Equation (2.2) gives more than centering. Split
\[
f_z=f_z^+-f_z^-,
\qquad
N=N(z)=\mathbb E|f_z|.
\]
When `z` is nonzero, define two probability measures on nonzero time sites by
\[
\frac{d\nu_+}{dq_0}=\frac{2f_z^+}{N},
\qquad
\frac{d\nu_-}{dq_0}=\frac{2f_z^-}{N}.
\tag{3.1}
\]
The first cancellation in (2.2) says
\[
\mathbb E f_z^+=\mathbb E f_z^-=N/2,
\]
so these are probabilities. The second says their `G_D` means are exactly equal:
\[
\boxed{
\mathbb E_{\nu_+}G_D=\mathbb E_{\nu_-}G_D.
}
\tag{3.2}
\]
Consequently their squared-mean terms cancel when second moments are subtracted.

## Theorem P07-B.25 — sign-weighted conditional variance identity

For every nonzero transverse selected test,
\[
\boxed{
\frac{|\langle r_D''(0),z\rangle|}{N(z)}
=\frac1{32}
\left|
\operatorname{Var}_{\nu_+}(G_D)
-\operatorname{Var}_{\nu_-}(G_D)
\right|.
}
\tag{3.3}
\]

### Proof

By construction and (2.1),
\[
\frac{\mathbb E[f_zG_D^2]}{N}
=\frac12\left(
\mathbb E_{\nu_+}G_D^2-
\mathbb E_{\nu_-}G_D^2
\right).
\tag{3.4}
\]
The means are equal by (3.2), so the right side is one half of the variance difference. Multiply by `1/16`. `square`

This identifies the remaining obstruction much more sharply. A bad dual direction must split its positive and negative `L^1` mass into two probability laws which have **exactly the same mass and exactly the same first `G_D` moment**, yet have a large difference in `G_D` variance. Arbitrary concentration of `|f_z|` on large values of `G_D` is not by itself enough: the positive and negative sides must do so asymmetrically while maintaining the exact common mean and the convolution eigenrelation (2.10).

---

# 4. New all-moment tradeoff: collision enters with exponent `1/q`, not `1/2`

The preceding report controlled every bounded-fourth-collision direction through
\[
\mathcal K_4(z)
:=\frac{\mathbb E f_z^4}{(\mathbb E f_z^2)^2}.
\tag{4.1}
\]
The variance representation suggests exploiting higher moments of the **physical field** rather than demanding stronger moments of the dual witness.

## Theorem P07-B.26 — physical-moment / dual-collision interpolation

For every real `q>=2`, every realized mask, and every nonzero transverse `z` supported on `D`,
\[
\boxed{
\frac{|\langle r_D''(0),z\rangle|}{N(z)}
\le
\frac1{16}\,
\|G_D\|_{L^{2q}(q_0)}^2\,
\mathcal K_4(z)^{1/q}.
}
\tag{4.2}
\]
In addition, with
\[
s_{\rm eff}(z)=\frac{\|z\|_1^2}{\|z\|_2^2},
\]
one has deterministically
\[
\boxed{
\mathcal K_4(z)
\le\frac{s_{\rm eff}(z)}{\lambda_n}
=\frac{2(n-1)}n\,s_{\rm eff}(z)
<2s_{\rm eff}(z),
}
\tag{4.3}
\]
and hence
\[
\boxed{
\frac{|\langle r_D''(0),z\rangle|}{N(z)}
\le
\frac1{16}\,
\|G_D\|_{2q}^2
\left(2s_{\rm eff}(z)\right)^{1/q}.
}
\tag{4.4}
\]

### Proof

Let `p=q/(q-1)`, so `1<=p<=2`. Hölder and (2.1) give
\[
|\mathbb E[f_zG_D^2]|
\le\|f_z\|_p\|G_D\|_{2q}^2.
\tag{4.5}
\]
Interpolation between `L^1` and `L^2` gives
\[
\|f_z\|_p
\le N^{1-2/q}\|f_z\|_2^{2/q}.
\tag{4.6}
\]
The standard `L^1-L^2-L^4` interpolation used in the previous report is
\[
\|f_z\|_2^3\le N\|f_z\|_4^2,
\]
which is equivalent to
\[
\frac{\|f_z\|_2}{N}\le\sqrt{\mathcal K_4(z)}.
\tag{4.7}
\]
Divide (4.5)--(4.6) by `N`, use (4.7), and multiply by `1/16` to obtain (4.2).

For (4.3),
\[
\|f_z\|_\infty\le\|z\|_1
\]
and therefore
\[
\|f_z\|_4^4
\le\|f_z\|_\infty^2\|f_z\|_2^2
\le\|z\|_1^2\lambda_n\|z\|_2^2.
\]
Divide by `||f_z||_2^4=lambda_n^2||z||_2^4`. `square`

### Quantitative interpretation

The old direct bound paid `sqrt(K_4)`. Equation (4.2) replaces this by `K_4^{1/q}` for any physical moment that can be controlled. For example,
\[
\frac{|\langle r_D''(0),z\rangle|}{N(z)}
\le
\frac1{16}\|G_D\|_8^2\mathcal K_4(z)^{1/4}
\tag{4.8}
\]
at `q=4`. This does not by itself prove a uniform constant, because very high-collision witnesses can still grow with `n`, but it shows that the remaining collision barrier is substantially softer than the preceding square-root estimate suggested.

There is also a completely source-valid moment bound with no independence fiction. For each time site, `G_D(j)` is a normalized Rademacher sum with squared coefficient norm at most a universal constant. Khintchine's inequality therefore gives, for every integer `q>=2`,
\[
\mathbb E_D|G_D(j)|^{2q}\le(Cq)^q,
\]
uniformly in `j`, hence
\[
\boxed{
\mathbb E_D\|G_D\|_{2q}^{2q}\le(Cq)^q.
}
\tag{4.9}
\]
This is only a moment input, not a claim that the time coordinates are independent.

---

# 5. Exact remaining lemma in the new coordinates

The preceding report already disposed of two large classes simultaneously:

1. every adaptive direction with `K_4(z)<=K_0` for fixed `K_0`, and
2. every direction with effective support below the near-square-root barrier.

For the unresolved class, (3.3) converts `QACHL` into a conditional-variance problem.

## Missing lemma `SVIB(K_0,C)` — selected variance-imbalance bound

Prove that for some fixed finite `K_0,C`, with failure probability `O(n^{-1/2})`, simultaneously for every mask-dependent transverse `z` satisfying
\[
\operatorname{supp}(z)\subset D,
\qquad
s_{\rm eff}(z)>\frac{\sqrt n}{\log n},
\qquad
\mathcal K_4(z)>K_0,
\tag{5.1}
\]
the two probabilities (3.1) obey
\[
\boxed{
\left|
\operatorname{Var}_{\nu_+}(G_D)
-
\operatorname{Var}_{\nu_-}(G_D)
\right|
\le C.
}
\tag{SVIB}
\]

By (3.3), `SVIB` bounds the dual ratio on the only class not already covered by the previous report. Therefore `SVIB` plus the inherited bounded-collision and low-effective-support estimates implies
\[
\boxed{K_D^{(2)}=O(1)}
\tag{5.2}
\]
with `O(n^{-1/2})` failure, i.e. `QBI`.

The remaining analytic step is the already-isolated higher-order interpolation remainder: for one sufficiently small fixed `beta>0`, control
\[
\inf\left\{\|h\|_\infty:
T_Dh=r_D(\beta)-\frac{\beta^2}{2}r_D''(0)
\right\}
\le C_3\beta^3
\tag{5.3}
\]
with the same failure scale. `QBI` plus (5.3) yields the earlier `TRBI` condition, hence
\[
\boxed{\mathbb E\vartheta(G_n)=O(\sqrt n),}
\tag{5.4}
\]
which removes the full `sqrt(log log n)` loss. This still does not establish the sharp leading constant `1`.

The advantage of `SVIB` over the old statement is conceptual and technical: it no longer asks for a generic random-Fourier `L^1/L^2` theorem. It asks only that two **endogenous sign-weighted laws with identical first moment and an exact same-mask convolution eigenfunction constraint** cannot have arbitrarily separated second moments.

---

# 6. A materially different pivot tested in the same run: fresh reserve blocks

I also tested a different route intended to manufacture genuine independence rather than pretend that the original Fourier coordinates are independent.

The quadratic design writes
\[
W_a-1=2\sum_{e\in E_a}\chi_e,
\qquad
\chi_{\{r,s\}}=\varepsilon_r\varepsilon_s.
\tag{6.1}
\]
If frequency vertices are partitioned into endpoint blocks, the contribution from edges whose endpoints lie in two prescribed blocks depends only on mask bits in those endpoint blocks. One can then reserve a disjoint block of frequency bits for correction. Conditional on the endpoint bits, the **occupancy bits** in that reserve are genuinely fresh. This is a valid way to create independence at the mask-bit level.

What prevents this from already closing `QBI` is spectral, not probabilistic: after conditioning on the endpoint partition, the reserve Fourier columns occupy a restricted frequency block, and an endogenous exceptional time set can interact badly with that deterministic partial frame. Ordinary matrix Chernoff recovers a margin only when the exceptional set is small enough to reintroduce a logarithmic penalty.

The natural constant-aspect statement is a left-edge theorem for a random partial Fourier Gram matrix. If an exceptional row set has asymptotic density `alpha`, a genuinely independent reserve column set has density `beta>alpha`, the MANOVA/free-Jacobi prediction for the lower nonzero edge is
\[
\lambda_-(\alpha,\beta)
=
\left(
\sqrt{(1-\alpha)\beta}
-
\sqrt{\alpha(1-\beta)}
\right)^2>0.
\tag{6.2}
\]
Farrell's random-DFT erasure work (`arXiv:1003.1021`, later JFAA) establishes the limiting empirical law in the independent row/column model, but that paper explicitly does **not** supply the extremal-eigenvalue convergence needed here. Thus (6.2) is not used as a theorem in this report.

This pivot is still informative: a constant-aspect left-edge theorem, adapted to a block construction in which the exceptional set is measurable before the reserve mask bits are exposed, would give a finite-stage bounded repair and hence another route to `QBI`. The exact unresolved point is the extreme singular value, not a source-admission or finite-LP issue.

---

# 7. What changed, what did not, and next attack

### Proved this run

- Exact dependency-aware identity
  \[
  \langle r_D''(0),z\rangle=\frac1{16}E[f_zG_D^2].
  \]
- Exact cancellations `E f_z=E[f_zG_D]=0` for every selected transverse test.
- Exact convolution eigenfunction identity `G_D*f_z=sqrt(n) f_z`.
- Exact sign-weighted variance formula
  \[
  \frac{|\langle r_D''(0),z\rangle|}{E|f_z|}
  =\frac1{32}|Var_{nu_+}G_D-Var_{nu_-}G_D|.
  \]
- Deterministic all-`q` interpolation estimate
  \[
  R(z)\le\frac1{16}\|G_D\|_{2q}^2 K_4(z)^{1/q},
  \]
  plus `K_4(z)<2s_eff(z)` and the same-mask Rademacher moment bound (4.9).

### Not proved

- `SVIB`, `QBI`, the analytic `O(beta^3)` interpolation remainder, `TRBI`, or any improved arbitrary-`n` theta asymptotic.
- The left-edge partial-Fourier theorem in Section 6.
- The sharp leading constant `1` in Conjecture 18.

### Next concrete attack

The next run should attack `SVIB` directly through a weighted additive-energy decomposition of the two measures `nu_+,nu_-`. The exact equal-mean constraint (3.2) should be imposed before any truncation. The first target is a dichotomy:

1. either both sign-weighted laws have uniformly bounded `G_D` second moment, which closes (SVIB) immediately; or
2. one law puts substantial `L^1(f_z)` mass in a high-`|G_D|` tail. Use the convolution eigenrelation (2.10) and the existing effective-support lower bound to convert such tail concentration into a high additive-energy configuration, then apply the leave-one-frequency quadratic decoupling already available from the preceding report.

If that tail-to-additive-energy implication fails twice, the reserve-block spectral pivot in Section 6 is the genuinely different next method, not another admission screen.
