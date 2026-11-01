Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED** — GPT-6 / maximum was requested as an owner preference, but authenticated completed-run effort telemetry is unavailable, so I do not claim otherwise.

# P07-A — exact affine positivity barrier and a buffered overcomplete hinge route

**Native role:** `P07-A`, task `6aa7b46f70a8819184095c277974c256`  
**Repository / branch:** private `yspennstate/math-open-problems` / `master`  
**Captured pre-write master:** `2ea173b2d482ead49e63e7ecd303057d2f46d9f4`  
**Previous own substantive checkpoint:** `probability_campaigns/progress_first_2026-09-20/P07/primal/2026-09-20T1511+0300__prime_half_support_hinge_certificate.md`, blob `b30ae17565ae638f2ed7362c6c5613f61488db3b`.  
**Complementary P07-B checkpoint read:** `probability_campaigns/progress_first_2026-09-20/P07/fourier_dual/2026-09-20T1508+0300__selected_quadratic_energy_scale_sharpness.md`, blob `338c47183c62feea3824db3048caa2611691f473`. P07-B owns Fourier-dual / exceptional-frequency interpolation. This report uses only its already-shared empirical Gaussian radial-field input and stays on primal positive-certificate geometry.

**Outside target:** Bandeira et al., *Randomstrasse101: Open Problems of 2025*, arXiv:2603.29571, Conjecture 18.  
**Primary partial-result paper:** A. S. Bandeira, J. Błasiok, D. Dmitriev, U. Faure, A. Kireeva, D. Kunisky, *The Lovasz number of random circulant graphs*, arXiv:2502.16227.  
**Exact source model:** odd `n`; the `(n-1)/2` conjugate nonzero difference pairs are selected independently with probability `1/2`.  
**Endpoint:**
\[
\mathbb E\,\vartheta(G_n)=(1+o(1))\sqrt n.
\]
A bounded current-source check on 20 September 2026 again found the primary paper describing exact asymptotics as open and retaining only
\[
\sqrt n\le \mathbb E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]
No later source-matching sharp-constant proof was found in that bounded check. This is not a worldwide novelty certificate.

The full-source metric remains
\[
\boxed{\alpha_{LL}=1/2\to1/2.}
\]
Status: **OPEN / PROVED PARTIAL**. The new results are exact deterministic reductions valid for every odd `n`, plus source-high-probability consequences using the inherited P07-B empirical Gaussian theorem. They do not yet prove the theta asymptotic.

---

## 0. Preserved predecessor handoff: SRG69 remains OPEN / PARTIAL

The reassigned predecessor remains archived under

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-13/rotations/SHPECTOROV-ZHAO-2026-SRG69/`

with frozen `R_SRG69=1`, status **OPEN / PARTIAL**. Preserve its no-Cayley theorem, rooted `L/B/C` system, centered spectral transfer, endpoint/cycle filters, block-moment and Gram reductions, low-rank residual work and star-complement handoff. Nothing here edits that root or calls SRG69 solved.

---

# 1. Exact cosine geometry for every odd order

Let
\[
M=\{1,\ldots,m\},\qquad m=(n-1)/2,
\]
with one representative from every nonzero conjugate pair. Let `D subset M`, `d=|D|`, and
\[
\phi_a(j)=\cos(2\pi aj/n),\qquad
C=(\phi_a(j))_{a\in D,\,j\in M}.
\]
For every odd `n`, no primality assumption is needed for
\[
\sum_{j\in M}\phi_a(j)=-\frac12,
\tag{1.1}
\]
and
\[
\boxed{CC^T=\frac n4 I_d-\frac12J_d.}
\tag{1.2}
\]
Indeed these are just the ordinary full cyclic Fourier orthogonality identities, folded over the conjugate pairs.

Define
\[
s_D(j)=\sum_{a\in D}\phi_a(j),
\qquad
Z_D(j)=\frac4{\sqrt n}\left(s_D(j)+\frac d{2m}\right).
\tag{1.3}
\]
With `q_0` uniform on `M`, (1.1)--(1.2) give exactly
\[
\mathbb E_{q_0}Z_D=0,
\qquad
\boxed{
\mathbb E_{q_0}Z_D^2=\sigma_D^2:=\frac{4d(m-d)}{m^2}.
}
\tag{1.4}
\]
Under the fair source mask, `d/m -> 1/2` in probability, so `sigma_D^2 -> 1`. The inherited P07-B radial theorem gives the stronger empirical statement
\[
Z_D\Longrightarrow N(0,1)
\tag{1.5}
\]
in source probability, with enough fixed exponential-moment control for the one-sided quadratic functions used below. The centering in (1.3) differs from P07-B's uncentered field only by `O_P(n^{-1/2})`.

For a probability `w` on pair sites, put
\[
r_j=mw_j,
\qquad
m_a(w)=\sum_{j\in M}w_j\phi_a(j).
\tag{1.6}
\]
If `w` is exact-flat at depth `delta`,
\[
m_a(w)=-\delta\qquad(a\in D),
\tag{1.7}
\]
then summing over `D` gives the exact radial identity
\[
\boxed{
\mathbb E_{q_0}[rZ_D]
=-a_D(\delta),
\qquad
a_D(\delta):=\frac{4d}{\sqrt n}\left(\delta-\frac1{2m}\right).
}
\tag{1.8}
\]
Thus at the conjectural scale `delta=c/sqrt(n)` and source density `d/m->1/2`, one has `a_D(delta)->c`.

---

# 2. New exact theorem: the unique minimum-energy signed flat profile is affine

Ignore nonnegativity temporarily and minimize
\[
\mathbb E_{q_0}r^2
\tag{2.1}
\]
over all real densities satisfying
\[
\mathbb E_{q_0}r=1,
\qquad
\mathbb E_{q_0}[r\phi_a]=-\delta\quad(a\in D).
\tag{2.2}
\]

## Theorem P07-A.30 — affine signed optimizer and exact complement-dispersion identity

The unique minimizer of (2.1)--(2.2) is
\[
\boxed{
r_{\rm lin}(j)=1-\kappa_D(\delta)Z_D(j),
\qquad
\kappa_D(\delta)=\frac{a_D(\delta)}{\sigma_D^2}
=\frac{m^2}{\sqrt n\,(m-d)}\left(\delta-\frac1{2m}\right).
}
\tag{2.3}
\]
Its collision is exactly
\[
\boxed{
\mathbb E_{q_0}r_{\rm lin}^2
=1+\frac{a_D(\delta)^2}{\sigma_D^2}.
}
\tag{2.4}
\]
Moreover every other signed exact-flat density has the orthogonal decomposition
\[
r=r_{\rm lin}+h,
\qquad
\mathbb E h=0,
\qquad
\mathbb E[h\phi_a]=0\quad(a\in D),
\tag{2.5}
\]
and therefore
\[
\boxed{
\mathbb E r^2
=\mathbb E r_{\rm lin}^2+\mathbb E h^2.
}
\tag{2.6}
\]

### Proof

The affine constraint normals are `1` and the selected cosine rows. By (1.1)--(1.2), the equal right-hand side in (2.2) makes the least-norm Lagrange multiplier equal on every selected row. Equivalently the signed minimizer lies in
\[
\operatorname{span}\{1,s_D\}
=\operatorname{span}\{1,Z_D\}.
\]
The normalization forces the constant coefficient to be `1`, and (1.8) plus (1.4) forces the coefficient of `Z_D` to be `-a_D/sigma_D^2`. This proves (2.3). Equation (2.4) follows from `E Z_D=0`. Any other feasible density differs by a vector orthogonal to every affine constraint normal, hence in particular to `r_lin`, which proves (2.6). `square`

There is an exact Fourier interpretation. Every pair probability satisfies
\[
\sum_{a\in M}m_a(w)=-\frac12.
\tag{2.7}
\]
Hence if the selected moments equal `-delta`, the mean unselected moment is forced to be
\[
\eta_D(\delta)=\frac{d\delta-1/2}{m-d}.
\tag{2.8}
\]
The affine profile `r_lin` is exactly the signed measure whose Fourier moments are **two-level**:
\[
m_a=-\delta\quad(a\in D),
\qquad
m_b=\eta_D(\delta)\quad(b\notin D).
\tag{2.9}
\]
Thus every nonlinear positive repair acts entirely by creating dispersion among the unselected frequencies.

For an exact-flat probability `w`, define
\[
V_{D^c}(w)
:=\sum_{b\notin D}
\bigl(m_b(w)-\eta_D(\delta)\bigr)^2.
\tag{2.10}
\]
Applying Parseval to the symmetric signed difference between `w` and `w_lin` gives the exact identity
\[
\boxed{
V_{D^c}(w)
=\frac{n}{4m}\,
\mathbb E_{q_0}(r-r_{\rm lin})^2.
}
\tag{2.11}
\]
This is an exact structural bridge to the complementary-frequency line: the unselected Fourier dispersion is precisely the physical `L^2` cost of repairing the least-energy two-level signed profile.

---

# 3. Positivity forces a macroscopic nonlinear repair

If `r>=0`, then on every site where `r_lin<0`,
\[
h=r-r_{\rm lin}\ge-r_{\rm lin}.
\]
Therefore (2.6) and (2.11) immediately imply
\[
\boxed{
\mathbb E r^2
\ge
1+\frac{a_D^2}{\sigma_D^2}
+
\mathbb E[(r_{\rm lin})_-^2],
}
\tag{3.1}
\]
and
\[
\boxed{
V_{D^c}(w)
\ge
\frac{n}{4m}\,
\mathbb E[(r_{\rm lin})_-^2].
}
\tag{3.2}
\]
At source density and depth `delta=c/sqrt(n)`, the empirical Gaussian theorem makes
\[
r_{\rm lin}\Longrightarrow1-cZ,
\qquad Z\sim N(0,1).
\tag{3.3}
\]
Hence every source-valid sharp-scale positive flat certificate obeys
\[
\boxed{
\liminf V_{D^c}(w)
\ge
\frac12 B(c),
\qquad
B(c):=\mathbb E[(cZ-1)_+^2]
=(c^2+1)\overline\Phi(1/c)-c\varphi(1/c),
}
\tag{3.4}
\]
in the corresponding source-probability sense.

At the conjectured constant `c=1`,
\[
B(1)=2\overline\Phi(1)-\varphi(1)
\approx0.07533978334,
\]
so
\[
\boxed{
\liminf V_{D^c}(w)\ge0.03766989167.
}
\tag{3.5}
\]
Also the signed affine solution itself is negative on an asymptotic fraction
\[
\boxed{
\Pr\{Z>1\}=0.1586552539\ldots
}
\tag{3.6}
\]
of pair sites. Therefore an `o(1)` physical-`L^2` perturbation of the least-energy signed solution can never produce a sharp positive certificate. A genuinely nonlinear active-set correction is mathematically necessary.

This all-odd-`n` obstruction is weaker numerically than the previous **prime exact-half-support** lower bound, which forced the larger complementary-dispersion constant `gamma_*≈0.112418471`; its value is that (3.2)--(3.5) require neither prime order nor the exact-support theorem.

---

# 4. Stronger radial positivity bound and the continuous hinge constant

The negative-part estimate is not optimal even in the one-dimensional radial relaxation.

## Theorem P07-A.31 — one-sided radial collision inequality

Let real numbers `z_j` have uniform empirical measure `q_0`, and let `r_j>=0` satisfy
\[
\mathbb E r=1,
\qquad
\mathbb E[rz]=-a.
\]
Then for every real `t` with `t+a>0`,
\[
\boxed{
\mathbb E r^2
\ge
\frac{(t+a)^2}{\mathbb E[(t-z)_+^2]}.
}
\tag{4.1}
\]

### Proof

For every `lambda>=0`,
\[
r_j^2\ge2\lambda(t-z_j)r_j-\lambda^2(t-z_j)_+^2.
\]
If `t-z_j>=0` this is completion of the square; if `t-z_j<0`, the right-hand side is nonpositive. Averaging gives
\[
\mathbb E r^2
\ge2\lambda(t+a)-\lambda^2\mathbb E[(t-z)_+^2].
\]
Optimizing in `lambda` proves (4.1). `square`

At `a=1` and `z=>Z~N(0,1)`, let `t_*` be the unique positive solution
\[
\boxed{(1-t_*)\Phi(t_*)=\varphi(t_*).}
\tag{4.2}
\]
Numerically
\[
\boxed{t_*=0.481058387034628\ldots .}
\tag{4.3}
\]
This is exactly the optimizer of (4.1). Consequently every positive sharp-radial certificate satisfies the Gaussian-relaxation lower bound
\[
\boxed{
\liminf\mathbb E r^2
\ge C_{\rm rad}
:=\frac{1+t_*}{\Phi(t_*)}
=2.16287893903121\ldots .
}
\tag{4.4}
\]
The extremizer of the limiting **radial relaxation** is the continuous hinge
\[
r_*(z)=\frac{(t_*-z)_+}{\Phi(t_*)},
\tag{4.5}
\]
because at (4.2)
\[
\mathbb E[(t_*-Z)_+]=\Phi(t_*),
\qquad
\mathbb E[Z(t_*-Z)_+]=-\Phi(t_*).
\]
Its support fraction is
\[
\boxed{\Phi(t_*)=0.684762498865527\ldots .}
\tag{4.6}
\]
This is a useful contrast with the prime optimizer, whose exact support fraction is `1/2`: positivity by itself prefers about `68.5%` support at the sharp radial constant, whereas prime optimality forces additional sparsification.

---

# 5. New construction: a buffered overcomplete hinge family

The exact-half-support hinge from the previous report has the right radial constant and a large positivity margin, but on primes it uses exactly `d` sites, leaving no linear degrees of freedom for transverse repair. The continuous hinge (4.5) has substantial support surplus, but its density vanishes at the support boundary, leaving no positivity margin.

There is a one-parameter family interpolating between these two extremes while retaining **both** a linear support surplus and a strictly positive margin on its support.

For `0<=t<t_*`, define
\[
\boxed{
b(t)=
\frac{\Phi(t)-(t+1)\varphi(t)}{\Phi(t)-\varphi(t)}.
}
\tag{5.1}
\]
Because
\[
b(t)-t
=\frac{(1-t)\Phi(t)-\varphi(t)}{\Phi(t)-\varphi(t)},
\tag{5.2}
\]
one has `b(t)>t` exactly for `t<t_*`. Put
\[
A(t)=b(t)\Phi(t)+\varphi(t)
\tag{5.3}
\]
and
\[
\boxed{
r_t(z)=\frac{(b(t)-z)\mathbf1_{\{z\le t\}}}{A(t)}.
}
\tag{5.4}
\]
A direct truncated-normal calculation gives
\[
\mathbb E r_t(Z)=1,
\qquad
\boxed{\mathbb E[Zr_t(Z)]=-1.}
\tag{5.5}
\]
Indeed
\[
\mathbb E[Z(b-Z)\mathbf1_{\{Z\le t\}}]
=-\Phi(t)+(t-b)\varphi(t),
\]
and (5.1) makes this equal to `-A(t)`.

The three key parameters are
\[
\rho(t)=\Phi(t),
\qquad
\mu(t)=\frac{b(t)-t}{A(t)},
\tag{5.6}
\]
where `rho` is the support fraction and `mu` is the minimum density on the support, and
\[
\boxed{
C(t)=
\frac{(b(t)^2+1)\Phi(t)+(2b(t)-t)\varphi(t)}{A(t)^2}
}
\tag{5.7}
\]
for the collision.

The endpoints are exact:

- `t=0`: `b=1`, support fraction `1/2`, recovering the previous half-support hinge and `C(0)=4/(1+sqrt(2/pi))=2.22483694849...`.
- `t up t_*`: `b down t_*`, `mu down0`, support fraction `0.68476249...`, and `C(t) down C_rad=2.16287893903...`.

A useful interior point is
\[
\boxed{t=0.2:}
\]
\[
\rho=0.57925970944,
\qquad
\mu=0.52696455226,
\qquad
C=2.17168663236.
\tag{5.8}
\]
Thus this choice retains a density margin larger than `0.52` on its support while providing an asymptotic support surplus of
\[
(0.5792597-0.5)m=0.0792597m
\tag{5.9}
\]
relative to the `d~m/2` exact-flat equations.

### Source implementation

For a source mask `D`, use the centered empirical field `Z_D` and define
\[
S_t(D)=\{j\in M:Z_D(j)\le t\},
\tag{5.10}
\]
\[
r^{(0)}_{D,t}(j)
=
\frac{(b(t)-Z_D(j))\mathbf1_{S_t(D)}}
{A_{D,t}},
\qquad
A_{D,t}=\mathbb E_{q_0}[(b(t)-Z_D)_+\mathbf1_{\{Z_D\le t\}}].
\tag{5.11}
\]
(The positive part is redundant because `b(t)>t`.) The inherited empirical Gaussian theorem yields, for every fixed `t<t_*`,
\[
\frac{|S_t(D)|}{m}\to\rho(t),
\tag{5.12}
\]
\[
\min_{j\in S_t}r^{(0)}_{D,t}(j)\to\mu(t)>0,
\tag{5.13}
\]
\[
\mathbb E_{w^{(0)}}Z_D\to-1,
\qquad
m\sum_j(w_j^{(0)})^2\to C(t)
\tag{5.14}
\]
in source probability.

If
\[
\delta^{(0)}_D
:=-\frac1d\sum_{a\in D}m_a(w^{(0)}),
\tag{5.15}
\]
then (1.8) gives
\[
\boxed{\sqrt n\,\delta_D^{(0)}\to1.}
\tag{5.16}
\]
So the buffered hinge has the sharp **average selected moment**, a linear support surplus, and a fixed positive coordinate margin simultaneously.

By Parseval, the total within-group Fourier dispersion of this radial candidate satisfies
\[
V_D(w^{(0)})+V_{D^c}(w^{(0)})
\to
\boxed{\Gamma(t):=\frac{C(t)-2}{2}.}
\tag{5.17}
\]
For `t=0.2`,
\[
\Gamma(0.2)=0.08584331618\ldots,
\qquad
\sqrt{\Gamma(0.2)}=0.2929903\ldots .
\tag{5.18}
\]
In particular the selected transverse residual has `l2` norm at most this constant asymptotically.

---

# 6. Prime orders: overcomplete support removes the algebraic repair obstruction exactly

The previous half-support hinge used a square cosine matrix. The buffered support is wider than the number of selected rows. On prime order, this gives an exact theorem.

## Theorem P07-A.32 — augmented full row rank on every overcomplete prime support

Let `p` be an odd prime, `D subset M`, `|D|=d`, and `S subset M` with
\[
|S|\ge d+1.
\]
Then the `(d+1) x |S|` augmented cosine matrix
\[
\boxed{
\mathcal A_{D,S}
=
\begin{pmatrix}
\mathbf1_S^T\\
C_{D,S}
\end{pmatrix}
}
\tag{6.1}
\]
has full row rank `d+1`.

### Proof

If the rows were dependent, there would be a nonzero even trigonometric polynomial
\[
P(j)=\alpha_0+\sum_{a\in D}\alpha_a\cos(2\pi aj/p)
\]
vanishing on every `j in S`. Hence it also vanishes on `-S`. Its Fourier support is contained in
\[
\{0\}\cup\pm D,
\]
of size at most `2d+1`, while its physical support has size at most `p-2|S|`. Tao/Chebotarev prime uncertainty would require
\[
(2d+1)+(p-2|S|)\ge p+1,
\]
which is equivalent to `d>=|S|`, contradicting `|S|>=d+1`. `square`

Therefore, on the source-high-probability event `|S_t(D)|>=d+1`, **every** transverse residual can be corrected exactly inside the buffered support while preserving total mass. There is no longer any algebraic solvability or square-minor obstruction.

Define the selected residual
\[
e_a=m_a(w^{(0)})+\delta_D^{(0)},
\qquad
\sum_{a\in D}e_a=0.
\tag{6.2}
\]
A density correction `h` supported on `S_t` gives an exact-flat certificate at the same depth precisely when
\[
\mathbf1^Th=0,
\qquad
C_{D,S_t}h=-m e.
\tag{6.3}
\]
By Theorem P07-A.32 such an `h` always exists on prime order once the support is overcomplete.

Positivity is now the **only** missing issue. The deterministic sufficient condition is simply
\[
\boxed{
\|h\|_\infty
<\min_{j\in S_t}r^{(0)}_{D,t}(j).
}
\tag{6.4}
\]
For a scale-free target define
\[
L(D,S_t)
:=
\sup_{\substack{e\perp\mathbf1\\e\ne0}}
\frac{1}{\|e\|_2}
\inf_{\substack{\mathbf1^Th=0\\C_{D,S_t}h=-me}}
\|h\|_\infty.
\tag{6.5}
\]
Then the `t=0.2` buffered hinge would be repaired positively whenever
\[
L(D,S_{0.2})
<
\frac{\mu(0.2)}{\sqrt{\Gamma(0.2)}}+o(1)
=
\boxed{1.79857\ldots+o(1).}
\tag{6.6}
\]
This is a concrete new primal bottleneck. Unlike the previous square-support condition, it asks only for a bounded `l2 -> l_infinity` correction on a system with about `0.0793m` excess columns and a fixed positivity margin.

If (6.6), or any fixed-`t` analogue strong enough for the **actual** residual, holds with source probability `1-o(1)` for both `D` and `D^c`, then one gets exact flat certificates with
\[
\delta_D,\delta_{D^c}\ge(1-o(1))/\sqrt p.
\]
Using vertex-transitive complementarity
\[
\vartheta(G_D)\vartheta(G_{D^c})=p,
\]
this would imply
\[
\boxed{\vartheta(G_D)=(1+o_P(1))\sqrt p}
\tag{6.7}
\]
on prime orders. A separate quantitative tail/uniform-integrability step would still be required for the requested expectation asymptotic and then for general odd `n`.

---

# 7. The buffered support has the correct average transverse conditioning

The remaining repair problem is not caused by a collapse of the **average** singular scale.

For each pair site `j`, let
\[
N_j(D)=\sum_{a\in D}\phi_a(j)^2.
\]
Under the exact Bernoulli source mask,
\[
N_j(D)-\frac d2
=\sum_{a\in M}\xi_a\left(\phi_a(j)^2-\frac12\right),
\]
a sum of independent bounded terms whose deterministic coefficient sum is `-1/4`. Hoeffding plus a union bound over `j in M` gives
\[
\boxed{
\max_j\left|N_j(D)-\frac d2\right|
=O_P(\sqrt{n\log n}).
}
\tag{7.1}
\]
Similarly, from
\[
s_D(j)+\frac d{2m}
=\sum_{a\in M}\xi_a
\left(\phi_a(j)+\frac1{2m}\right)
\]
with zero coefficient sum,
\[
\boxed{
\max_j\left|s_D(j)+\frac d{2m}\right|
=O_P(\sqrt{n\log n}).
}
\tag{7.2}
\]

Let
\[
G_t=C_{D,S_t}C_{D,S_t}^T,
\qquad
P_\perp=I_d-\frac1dJ_d.
\]
Then (7.1), (7.2), and `|S_t|/m->rho(t)` imply
\[
\boxed{
\frac1{d-1}
\operatorname{tr}(P_\perp G_tP_\perp)
=
\left(\rho(t)+o_P(1)\right)\frac n4.
}
\tag{7.3}
\]
On the other hand the exact full-pair Gram identity (1.2) gives, on the transverse row space,
\[
0\preceq P_\perp G_tP_\perp
\preceq\frac n4P_\perp.
\tag{7.4}
\]
Hence the normalized transverse eigenvalues lie in `[0,1]` and have empirical mean `rho(t)+o_P(1)`. In particular, for every fixed `0<alpha<rho(t)`, at least
\[
\boxed{
\frac{\rho(t)-\alpha}{1-\alpha}-o_P(1)
}
\tag{7.5}
\]
of the transverse eigenvalues are at least `alpha n/4`.

So a positive fraction of the transverse row space is automatically well conditioned at the correct `Theta(n)` Gram scale. The remaining issue is specifically the **lower spectral tail plus leverage / l_infinity control**, not total covariance mass. That is substantially narrower than proving a generic random partial-Fourier RIP theorem.

---

# 8. What this changes and the next attack

The previous prime half-support hinge had the right radial constant but no linear repair freedom. This run gives a different route:

1. The least-energy exact-flat signed solution is explicitly `1-kappa Z_D`; at the sharp constant it is negative on about `15.9%` of sites, proving that infinitesimal perturbative repair is impossible.
2. Every nonlinear positive repair is measured **exactly** by dispersion on the unselected Fourier half through (2.11).
3. The Gaussian radial positivity relaxation has an explicit optimum `C_rad=2.162878939...` supported on about `68.5%` of sites.
4. The buffered family `r_t` retains sharp radial depth while simultaneously having support fraction `>1/2` and a positive margin. At `t=0.2` it has about `7.93% m` excess columns and margin `0.52696`.
5. On prime orders, every such overcomplete support gives an augmented constraint matrix of full row rank by prime uncertainty. Exact repair always exists algebraically.
6. The buffered restricted Gram has the correct average transverse spectral scale. Only a bounded `l2 -> l_infinity` correction estimate remains.

The next P07-A attack is therefore to prove (6.6) for one fixed `t` (initially `t=0.1` or `0.2`) by combining the linear surplus `|S_t|-d=Theta(n)`, the exact full-Gram identity, and leverage control for the adaptive threshold support. A weaker source-specific statement only for the actual residual `e` in (6.2) is already sufficient and is preferable to a generic operator theorem. P07-B's exceptional-frequency / quadratic-chaos work remains complementary; no attempt here is made to take over that line.

Status remains **OPEN / PROVED PARTIAL**. Candidate arguments require later independent review before any publication or closure claim.
