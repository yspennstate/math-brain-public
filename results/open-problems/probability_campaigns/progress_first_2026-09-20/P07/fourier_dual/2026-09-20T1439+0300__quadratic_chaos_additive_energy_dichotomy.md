Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED** — GPT-6 / maximum was requested as an owner preference, but this runtime exposes no authenticated completed-run effort telemetry or binding model/effort selector, so I do not claim otherwise.

# P07-B — exact quadratic chaos, transverse isotropy, and an additive-energy dichotomy

**Native role:** `P07-B`, task `6aabe797a39081919acc889f29f4c556`  
**Repository / branch:** private `yspennstate/math-open-problems` / `master`  
**Fresh pre-write master:** `89d87cb133a20b9fe836bdaf7365cf2309a874bf`  
**Previous own substantive report:** `probability_campaigns/progress_first_2026-09-20/P07/fourier_dual/2026-09-20T1311+0300__near_sqrt_support_barrier.md`, creation commit `f0b249b1e76dcb32c2b22766548682abd658ddf3`.  
**Complementary P07-A checkpoint used:** `probability_campaigns/progress_first_2026-09-20/P07/primal/2026-09-20T1345+0300__density_profile_entropy_barrier.md`. P07-A owns primal positive-certificate geometry, density profiles and its fourth-collision criterion; this report stays on the Fourier-dual Gibbs interpolation obstruction and hands back only the exact additive-energy identity proved below.

**Outside target:** Bandeira et al., *Randomstrasse101: Open Problems of 2025*, arXiv:2603.29571, Conjecture 18.  
**Primary partial result:** A. S. Bandeira, J. Błasiok, D. Dmitriev, U. Faure, A. Kireeva, D. Kunisky, *The Lovász number of random circulant graphs*, arXiv:2502.16227.  
**Exact source model:** odd `n`; the `(n-1)/2` conjugate nonzero difference pairs are selected independently with probability `1/2`.  
**Endpoint:**
\[
\mathbb E\vartheta(G_n)=(1+o(1))\sqrt n.
\]
**Inherited source bound:**
\[
\sqrt n\le \mathbb E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]
The fixed full-source metric is therefore still
\[
\boxed{\alpha_{LL}=1/2\to1/2.}
\]
Status: **OPEN / PROVED PARTIAL**. No improved arbitrary-`n` theta asymptotic is claimed in this report.

The assignment-time source check, exact Fourier LP, and older TH18 attempts were recovered once in the first P07-B iteration and are not rerun here. The exact moment-polytope identity inherited from those reports is
\[
\kappa_D=\frac1{n\delta_D},\qquad
\mathbb E\vartheta(G_n)=1+\mathbb E\frac1{\delta_D}.
\tag{0.1}
\]
The current route is the bounded interpolation condition `TRBI`: for one sufficiently small fixed `beta>0`, control the exact Gibbs residual dual norm by `O(beta^2)` with failure `O(n^{-1/2})`. That alone implies `E theta(G_n)=O(sqrt n)` and removes the iterated-logarithmic loss. The previous run eliminated all genuinely sparse dual witnesses. This run identifies the leading nonlinear residual exactly and narrows the unsolved class much further.

---

# 1. A stronger version of the previous support barrier: effective support

Put
\[
M=\{1,\ldots,m\},\qquad m=(n-1)/2,
\]
and let `D subset M` be the fair random selected-pair set. On nonzero time sites define
\[
\phi_a(j)=\cos(2\pi aj/n),\qquad
X_D(j)=\frac1{\sqrt n}\sum_{a\in D}\phi_a(j).
\tag{1.1}
\]
Let `q_0` be uniform on `Z_n\setminus\{0\}`. For `z=(z_a)_{a\in D}` satisfying
\[
\sum_{a\in D}z_a=0,
\tag{1.2}
\]
write
\[
f_z(j)=\sum_{a\in D}z_a\phi_a(j).
\tag{1.3}
\]
The exact nonzero-site tight-frame identity is
\[
\|f_z\|_{L^2(q_0)}^2
=\lambda_n\|z\|_2^2,
\qquad
\lambda_n=\frac{n}{2(n-1)}.
\tag{1.4}
\]
Also `||f_z||_infty<=||z||_1`, hence
\[
\|f_z\|_{L^1(q_0)}
\ge
\frac{\lambda_n\|z\|_2^2}{\|z\|_1}.
\tag{1.5}
\]

Recall the exact radial Gibbs residual
\[
A_D(\beta)=\mathbb E_{q_0}e^{-\beta X_D},
\qquad
h_{\rm raw}=A_D(\beta)^{-1}e^{-\beta X_D}-1+\beta X_D.
\tag{1.6}
\]
The preceding report proved, with arbitrarily high polynomial probability for fixed `beta`, the coordinate bound
\[
\max_{a\in M}
\left|\mathbb E_{q_0}[h_{\rm raw}\phi_a]\right|
\le n^{-1/2+o(1)}.
\tag{1.7}
\]
Therefore, uniformly over all transverse `z`,
\[
\frac{|\mathbb E[h_{\rm raw}f_z]|}{\mathbb E|f_z|}
\le
\frac{n^{-1/2+o(1)}}{\lambda_n}
\frac{\|z\|_1^2}{\|z\|_2^2}.
\tag{1.8}
\]
Define the coefficient effective support
\[
s_{\rm eff}(z):=\frac{\|z\|_1^2}{\|z\|_2^2}.
\tag{1.9}
\]

## Corollary P07-B.18 — effective-support barrier

For every fixed `eta>0`, on the event (1.7),
\[
\frac{|\mathbb E[h_{\rm raw}f_z]|}{\mathbb E|f_z|}\ge\eta
\quad\Longrightarrow\quad
\boxed{s_{\rm eff}(z)\ge n^{1/2-o(1)}.}
\tag{1.10}
\]
This strengthens the previous cardinality statement. A formally dense vector with almost all of its coefficient mass concentrated on few frequencies is also excluded. Any fixed-size obstruction must be genuinely mesoscopic/delocalized in frequency coefficient mass.

---

# 2. Exact second-order factorization as a Rademacher convolution

The previous report proposed expanding the Gibbs numerator to second order. In this model that expansion has an unexpectedly clean exact form.

Let
\[
\varepsilon_a:=2\mathbf1_{\{a\in D\}}-1\in\{-1,+1\},
\qquad a\in M,
\tag{2.1}
\]
so the `epsilon_a` are independent Rademachers. Extend them evenly to `Z_n` by
\[
Y(0)=0,\qquad Y(k)=\varepsilon_{[k]}\quad(k\ne0),
\tag{2.2}
\]
where `[k]` is the representative of the pair `{k,-k}` in `M`. Let
\[
s(0)=0,\qquad s(k)=\mathbf1_{\{[k]\in D\}}=\frac{1+Y(k)}2\quad(k\ne0).
\tag{2.3}
\]
Define cyclic convolutions
\[
C_a:=(s*s)(a),
\qquad
W_a:=(Y*Y)(a)=\sum_{k\in\mathbb Z_n}Y(k)Y(a-k).
\tag{2.4}
\]
Since `Y(0)=0`, the terms `k=0,a` in `W_a` vanish automatically.

The full Fourier representation is
\[
X_D(j)=\frac1{2\sqrt n}
\sum_{k\in\mathbb Z_n}s(k)e^{2\pi i k j/n}.
\tag{2.5}
\]
Hence for every nonzero `a`,
\[
\frac1n\sum_{j\in\mathbb Z_n}X_D(j)^2\phi_a(j)
=\frac{C_a}{4n}.
\tag{2.6}
\]
Because `z` is transverse, `f_z(0)=sum_a z_a=0`; therefore removing the origin only multiplies the full average by `n/(n-1)`, and
\[
\mathbb E_{q_0}[X_D^2f_z]
=\frac1{4(n-1)}\sum_{a\in D}z_aC_a.
\tag{2.7}
\]

Let
\[
S:=\sum_{b\in M}\varepsilon_b.
\]
Expanding (2.3) in the convolution gives, for every `a\ne0`,
\[
C_a
=\frac{n-2}{4}+S-\frac{\varepsilon_a}{2}+\frac{W_a}{4}.
\tag{2.8}
\]
For `a in D`, `epsilon_a=1`; all first three terms in (2.8) are therefore common across the selected coordinates and vanish against `sum z_a=0`. Thus:

## Theorem P07-B.19 — pure quadratic transverse factorization

For every realized source mask and every transverse selected-frequency vector `z`,
\[
\boxed{
\mathbb E_{q_0}[X_D^2f_z]
=\frac1{16(n-1)}\sum_{a\in D}z_aW_a.
}
\tag{2.9}
\]
No approximation, independence assumption, or asymptotic limit is used.

Since the constant and linear terms in the Gibbs numerator already vanish exactly,
\[
\mathbb E f_z=0,
\qquad
\mathbb E[X_Df_z]=0,
\tag{2.10}
\]
Taylor's theorem now gives the exact decomposition
\[
\boxed{
\mathbb E[h_{\rm raw}f_z]
=\frac{\beta^2}{32A_D(\beta)(n-1)}
\sum_{a\in D}z_aW_a
+\mathcal R_{\beta,D}(z),
}
\tag{2.11}
\]
where the remainder obeys the deterministic bound
\[
|\mathcal R_{\beta,D}(z)|
\le
\frac{\beta^3}{6A_D(\beta)}
\mathbb E_{q_0}
\left[e^{\beta|X_D|}|X_D|^3|f_z|\right].
\tag{2.12}
\]
Thus the first genuinely transverse term is not an opaque correlated Fourier vector: it is the quadratic Rademacher convolution `W=Y*Y` restricted to the selected frequencies.

---

# 3. The quadratic field has an exact combinatorial design and exact transverse covariance

The dependence structure of `W` can be computed completely.

For `a in M`, define a graph `E_a` on the pair-frequency vertex set `M` by putting an unordered edge `{r,s}`, `r\ne s`, in `E_a` precisely when
\[
[r+s]=a\quad\text{or}\quad[r-s]=a.
\tag{3.1}
\]
For odd `n`, the following elementary design facts hold:

1. `|E_a|=m-1` for every `a`.
2. For distinct `a,b in M`, `|E_a cap E_b|=1`.
3. Every unordered pair `{r,s}` of distinct vertices lies in exactly two of the graphs, namely `E_[r+s]` and `E_[r-s]`.

For completeness, (3) follows because `[r+s]` and `[r-s]` are nonzero and distinct. Conversely, given distinct `a,b`, division by `2` is valid modulo odd `n`, and the half-sum / half-difference construction recovers the unique unordered pair `{r,s}` whose two labels are `{a,b}`. This also proves (2). Counting incidences gives (1); equivalently it follows directly by pairing the `k` and `a-k` summands in (2.4).

There is exactly one diagonal summand in `W_a`, at `k=a/2`, and it equals `1`; every non-diagonal edge occurs twice. Hence
\[
\boxed{
W_a=1+2\sum_{\{r,s\}\in E_a}\varepsilon_r\varepsilon_s.
}
\tag{3.2}
\]
Distinct degree-two Rademacher monomials are orthogonal in `L^2` of the source mask, even when their edges share one endpoint. Therefore (3.2) and the design identities give the exact moments
\[
\boxed{
\mathbb EW_a=1,
\qquad
\operatorname{Var}(W_a)=2n-6,
\qquad
\operatorname{Cov}(W_a,W_b)=4\quad(a\ne b).
}
\tag{3.3}
\]

## Theorem P07-B.20 — exact transverse isotropy of the quadratic leakage

For every deterministic `z in R^M` with `sum_a z_a=0`,
\[
\boxed{
\mathbb E_D\left(\sum_{a\in M}z_aW_a\right)^2
=(2n-10)\|z\|_2^2.
}
\tag{3.4}
\]
Indeed, the mean vanishes because `E W_a=1`, and (3.3) gives
\[
(2n-6)\sum_a z_a^2+4\sum_{a\ne b}z_az_b
=(2n-10)\|z\|_2^2+4\left(\sum_a z_a\right)^2.
\]

Consequently the second-order coefficient in (2.9), against any deterministic transverse test, has the exact `n^{-1/2}` scale
\[
\left\|
\mathbb E_{q_0}[X_D^2f_z]
\right\|_{L^2(D)}
=
\frac{\sqrt{2n-10}}{16(n-1)}\|z\|_2.
\tag{3.5}
\]
Moreover `sum z_a(W_a-1)` is a homogeneous degree-two Rademacher chaos. Bonami hypercontractivity therefore yields, for every `p>=2`,
\[
\left\|\sum_a z_a(W_a-1)\right\|_{L^p(D)}
\le
(p-1)\sqrt{2n-10}\,\|z\|_2,
\tag{3.6}
\]
and hence a subexponential fixed-test tail at the same natural scale.

This is substantially stronger than merely bounding the variance of each coordinate. The entire deterministic transverse covariance is exactly scalar.

### Important limitation

The dual optimizer `z=z(D)` is allowed to depend on the same source mask. Equation (3.4) **cannot** be applied to that adaptive witness as though `z` were independent of `W`. This report does not make that substitution. The remaining difficulty is precisely adaptive alignment.

---

# 4. Exact own-frequency decoupling

The design representation also gives a clean leave-one-frequency fact. Except in the harmless degeneracy `3a=0 mod n`, exactly one edge of `E_a` is incident to the frequency vertex `a`, namely the edge joining `a` to `[2a]`. Therefore one can write
\[
W_a=W_a^{(-a)}+2\varepsilon_a\varepsilon_{[2a]},
\tag{4.1}
\]
where `W_a^{(-a)}` is independent of `epsilon_a`. If `3a=0`, the would-be contribution collapses into the deterministic diagonal and `W_a` is already independent of `epsilon_a`; set `W_a^{(-a)}=W_a`.

Thus in all cases there is an own-bit-independent version satisfying
\[
\boxed{|W_a-W_a^{(-a)}|\le2.}
\tag{4.2}
\]
Since `sd(W_a)=sqrt(2n-6)`, conditioning on the event `a in D` perturbs the leading quadratic coordinate only at scale `O(1)` compared with its natural `Theta(sqrt n)` fluctuation. In particular
\[
\mathbb E[W_a\mid\varepsilon_a]=1,
\qquad
\mathbb E[\varepsilon_aW_a]=0.
\tag{4.3}
\]
More conceptually, `W_a-1` lies purely in the second Rademacher chaos and is orthogonal to every first-chaos source selector. This is the dependence-aware decoupling input for the next adaptive argument; it is not an assertion that the coordinates `W_a` are mutually independent.

---

# 5. A full-residual additive-energy dichotomy

The preceding quadratic calculation attacks the Taylor-leading term. There is also a deterministic statement for the **entire** Gibbs residual, with no truncation of its higher orders.

For transverse `z`, define a symmetric complex coefficient vector `u` on `Z_n` by
\[
u_0=0,
\qquad
u_a=\nu_{-a}=\frac{z_a}{2}\quad(a\in D),
\qquad
u_k=0\quad\text{otherwise}.
\tag{5.1}
\]
Then
\[
f_z(j)=\sum_{k\in\mathbb Z_n}\nu_ke^{2\pi i k j/n}.
\tag{5.2}
\]
Because `sum z_a=0`, one has `f_z(0)=0`. Parseval therefore gives the exact second- and fourth-moment formulas
\[
\mathbb E_{q_0}f_z^2
=\frac n{n-1}\|\nu\|_2^2,
\tag{5.3}
\]
\[
\mathbb E_{q_0}f_z^4
=\frac n{n-1}\|\nu*\nu\|_2^2.
\tag{5.4}
\]
Define the normalized fourth moment
\[
\mathcal K_4(z)
:=\frac{\mathbb E f_z^4}{(\mathbb E f_z^2)^2}.
\tag{5.5}
\]
Then
\[
\boxed{
\mathcal K_4(z)
=\frac{n-1}{n}
\frac{\|\nu*\nu\|_2^2}{\|\nu\|_2^4}.
}
\tag{5.6}
\]
Thus the fourth moment is exactly a weighted additive-collision energy of the symmetric frequency coefficients. This is the precise interface with P07-A's separate fourth-collision route; P07-A need not duplicate the dual derivation.

Interpolation between `L^1` and `L^4` gives
\[
\|f_z\|_2^3\le\|f_z\|_1\|f_z\|_4^2,
\]
so
\[
\frac{\|f_z\|_2}{\|f_z\|_1}
\le\sqrt{\mathcal K_4(z)}.
\tag{5.7}
\]
By Cauchy-Schwarz,
\[
\boxed{
\frac{|\mathbb E[h_{\rm raw}f_z]|}{\mathbb E|f_z|}
\le
\|h_{\rm raw}\|_{L^2(q_0)}
\sqrt{\mathcal K_4(z)}.
}
\tag{5.8}
\]
The earlier Gibbs calculation proved
\[
\|h_{\rm raw}\|_2^2
\xrightarrow{\mathbb P}
H(\beta):=
 e^{\beta^2/16}-1-\frac{\beta^2}{16}
=rac{\beta^4}{512}+O(\beta^6).
\tag{5.9}
\]
Therefore, for every fixed `K<infinity`, uniformly over the entire adaptive class satisfying `K_4(z)<=K`,
\[
\boxed{
\frac{|\mathbb E[h_{\rm raw}f_z]|}{\mathbb E|f_z|}
\le
\left(\frac{\sqrt K}{\sqrt{512}}+O_K(\beta^2)+o_{\mathbb P}(1)\right)\beta^2.
}
\tag{5.10}
\]
This is already the desired `O(beta^2)` bound for every bounded-additive-energy dual direction, with **no independence assumption and no restriction on how `z` is chosen from the mask**.

Combining (1.10) and (5.10), any sequence of witnesses capable of making the `TRBI` constant diverge must simultaneously satisfy
\[
\boxed{
s_{\rm eff}(z)\ge n^{1/2-o(1)}}
\tag{5.11}
\]
and
\[
\boxed{\mathcal K_4(z)\longrightarrow\infty.}
\tag{5.12}
\]
Thus the remaining obstruction is not merely “dense.” It must be frequency-delocalized **and** increasingly additive-collision-rich.

---

# 6. Exact remaining lemma that removes the iterated-log loss

Fix a large finite constant `K_0` and, for the previous coordinate-concentration event, choose any threshold
\[
s_n=n^{1/2-o(1)}
\]
for which (1.8) is `o(1)` below `s_n`. Define the genuinely unresolved class
\[
\mathcal H_D(K_0)
=
\left\{
 z:\ z\ne0,\ z\perp\mathbf1,\ \operatorname{supp}z\subset D,\
 s_{\rm eff}(z)\ge s_n,\ \mathcal K_4(z)>K_0
\right\}.
\tag{6.1}
\]

## Missing lemma `ACHL(beta,K_0)` — adaptive collision-rich leakage

For one sufficiently small fixed `beta>0` and one fixed finite `K_0`, prove that there is a finite `C_0` such that
\[
\boxed{
\Pr_D\left\{
\sup_{z\in\mathcal H_D(K_0)}
\frac{|\mathbb E_{q_0}[h_{\rm raw}f_z]|}
{\mathbb E_{q_0}|f_z|}
>C_0\beta^2
\right\}
=O(n^{-1/2}).
}
\tag{6.2}
\]

This lemma is strictly narrower than the previous `DWRL(beta)` target:

- effective-support smaller than `s_n` is already controlled by (1.8);
- every direction with `K_4<=K_0` is already controlled by (5.10);
- only the mesoscopic/dense, high-additive-collision, adaptively aligned class remains.

If `ACHL(beta,K_0)` holds, these three cases imply
\[
K_D(\beta)\le C\beta^2
\tag{6.3}
\]
with failure `O(n^{-1/2})`. Taking `beta` sufficiently small after the finite constant `C` is fixed, the positive bounded-interpolation construction from the `1028` report gives
\[
\delta_D\ge\frac{c_\beta}{\sqrt n}
\tag{6.4}
\]
off that event. The universal fallback `delta_D>=1/(n-1)` on the failure event and (0.1) then give
\[
\boxed{\mathbb E\vartheta(G_n)=O(\sqrt n).}
\tag{6.5}
\]
So `ACHL` alone removes the entire published `sqrt(log log n)` loss. It does **not** by itself prove the leading constant `1`.

---

# 7. What failed, and why it is useful

A tempting but invalid conclusion from the exact covariance (3.4) would be: “the quadratic leakage is isotropic, therefore the adaptive dual supremum is small.” That is false as a proof step because the maximizing `z(D)` sees the same mask that generates `W(D)`. I have not treated it as independent, nor union-bounded over an exponential net.

Likewise, large fourth moment by itself is not being declared an obstruction. Equation (5.8) is one-way: bounded fourth moment is harmless, while high fourth moment only identifies where a bad witness *could* hide. The actual remaining problem is high collision **plus same-mask adaptive alignment**.

The useful consequence is that two broad classes are now rigorously gone: coefficient-localized witnesses and bounded-additive-energy witnesses. Meanwhile the Taylor-leading field has an exact pure second-chaos representation with exact covariance and an `O(1)` own-selector perturbation. That is substantially more structure than the previous generic dense-witness formulation.

---

# 8. Next concrete attack

The next run should work on `ACHL`, not reopen source admission.

The most promising route is a weighted additive-energy decomposition of `nu` from (5.6). A collision-rich witness can be dyadically reduced to a level set with large additive energy. On that level set, use the exact design (3.2), the leave-one-frequency representation (4.1), and the pure second-chaos orthogonality to decouple the source selector from the quadratic score. The fixed-test estimate is already sharp by (3.4)/(3.6); the task is to make it uniform only over the low-complexity additive pieces forced by high energy, rather than over all dense vectors. The analytic remainder in (2.12) must be controlled on the same decomposition, not discarded.

A successful proof should therefore aim for either:

\[
\sup_{z\in\mathcal H_D(K_0)}
\frac{|\sum_{a\in D}z_aW_a|}
{(n-1)\mathbb E|f_z|}=O(1)
\]
plus a matching `O(beta^3)` bound for the remainder, or directly the full nonlinear estimate (6.2). The latter is the theorem-sized target that already implies the source-level `O(sqrt n)` bound.

**Handoff to P07-A:** the exact identity (5.6) identifies the dual normalized fourth moment with the weighted additive convolution energy `||nu*nu||_2^2/||nu||_2^4`. P07-A's fourth-collision / density-profile program can use that identity, but P07-B retains ownership of controlling its correlation with the Gibbs residual. No peer file is overwritten here.
