Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED** — GPT-6 / maximum was requested as an owner preference, but authenticated completed-run effort telemetry is unavailable, so I do not claim otherwise.

# P07-A — prime half-support hinge certificate and the forced complementary-dispersion constant

**Native role:** `P07-A`, task `6aa7b46f70a8819184095c277974c256`  
**Repository / branch:** private `yspennstate/math-open-problems` / `master`  
**Captured pre-write master:** `194a028d88d1d717026268eb192490457bfe8a2a`  
**Previous own substantive checkpoint:** `probability_campaigns/progress_first_2026-09-20/P07/primal/2026-09-20T1345+0300__density_profile_entropy_barrier.md`, blob `cec6c74664d70f9b4b99ef271831526df577c2a1`.  
**Complementary P07-B input used:** the empirical Gaussian radial-field theorem in `probability_campaigns/progress_first_2026-09-20/P07/fourier_dual/2026-09-20T0927+0300__gibbs_radial_exceptional_frequencies.md`. P07-B owns Fourier-dual / exceptional-frequency control. This report uses that theorem only as an input and stays on primal support geometry and a new positive half-support construction.

**Outside target:** Bandeira et al., *Randomstrasse101: Open Problems of 2025*, arXiv:2603.29571, Conjecture 18.  
**Primary partial-result paper:** A. S. Bandeira, J. Błasiok, D. Dmitriev, U. Faure, A. Kireeva, D. Kunisky, *The Lovász number of random circulant graphs*, arXiv:2502.16227.  
**Exact source model:** odd `n`; the `(n-1)/2` conjugate nonzero difference pairs are selected independently with probability `1/2`.  
**Endpoint:**
\[
\mathbb E\,\vartheta(G_n)=(1+o(1))\sqrt n.
\]
The bounded current-source check on 20 September 2026 again found the primary paper describing the exact asymptotics as open and retaining only the square-root scale up to the iterated-log loss,
\[
\sqrt n\le \mathbb E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]
No later source-matching resolution was found in that bounded check. This is not a worldwide novelty certificate.

The fixed full-source metric therefore remains
\[
\boxed{\alpha_{LL}=1/2\to1/2.}
\]
Status: **OPEN / PROVED PARTIAL**. The main theorems below are prime-order structural results and a source-high-probability radial construction. They do not yet prove exact flatness and therefore do not close Conjecture 18.

---

## 0. Preserved predecessor handoff: SRG69 remains OPEN / PARTIAL

The reassigned predecessor remains archived under

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-13/rotations/SHPECTOROV-ZHAO-2026-SRG69/`

with frozen `R_SRG69=1`, status **OPEN / PARTIAL**. Preserve its no-Cayley theorem, rooted `L/B/C` feasibility system, centered spectral transfer, endpoint/cycle filters, block-moment and Gram reductions, low-rank residual work and star-complement handoff. Nothing here edits that root or calls SRG69 solved.

---

# 1. Prime normalization and the exact support size of the optimal flat measure

Let `p` be an odd prime,
\[
M=\{1,\ldots,m\},\qquad m=(p-1)/2,
\]
and let `D\subset M` be the source-selected edge-pair set, `d=|D|`. Put
\[
\phi_a(j)=\cos(2\pi aj/p).
\]
For a pair-site probability `w=(w_j)_{j\in M}`, define
\[
m_a(w)=\sum_{j\in M}w_j\phi_a(j).
\tag{1.1}
\]
An exact-flat certificate at depth `delta>0` satisfies
\[
\boxed{m_a(w)=-\delta\qquad(a\in D).}
\tag{1.2}
\]
The earlier exact moment-polytope reduction gives the maximal such depth `delta_D` and
\[
\vartheta(\overline{G_D})=1+\frac1{\delta_D},
\qquad
\vartheta(G_D)=\frac{p\delta_D}{1+\delta_D}.
\tag{1.3}
\]

It is useful to make one support point explicit.

### Lemma P07-A.28 — an optimal flat measure has no origin atom

In the full symmetric formulation on `Z_p`, every maximizing flat probability has zero mass at the origin.

**Proof.** Suppose an optimal symmetric probability has origin mass `rho>0` and selected moments `-delta`. Remove the origin and renormalize the remaining probability. Since every selected cosine equals `1` at the origin, the renormalized selected moments are
\[
\frac{-\delta-\rho}{1-\rho}
=-\frac{\delta+\rho}{1-\rho},
\]
which is strictly more negative than `-delta`. This produces a strictly larger feasible flat depth, contradicting maximality. `square`

Thus an optimal symmetric full probability can be written as
\[
p(\pm j)=w_j/2,\qquad j\in M.
\tag{1.4}
\]
If `m_x=E_p cos(2\pi xJ/p)`, then
\[
f(x)=\frac{m_x+\delta_D}{1+\delta_D}
\tag{1.5}
\]
is the optimal cyclic theta primal for `G_D`; its spectral probability is
\[
\mu_f=\frac{p+\delta_D\,\delta_0}{1+\delta_D}.
\tag{1.6}
\]
The prime exact-rank theorem from P07-A.13--P07-A.15 says every optimal primal for a graph with `d` edge pairs has exactly `2d+1` spectral support points. Therefore the nonzero pair support of `p`, hence of `w`, has size exactly `d`:
\[
\boxed{|\operatorname{supp}w|=d.}
\tag{1.7}
\]
This is stronger than the previous uncertainty lower bound `|supp w|>=d`: the **actual prime optimizer uses exactly half of the pair sites asymptotically** under the fair source law, because `d/m -> 1/2` in probability.

---

# 2. The normalized radial field

Define on pair sites
\[
X_D(j)=\frac1{\sqrt p}\sum_{a\in D}\phi_a(j),
\qquad
Y_D(j)=4X_D(j).
\tag{2.1}
\]
Let `q_0` be uniform on `M`. P07-B proved that, under the exact fair source mask, the empirical law of `X_D` converges in probability to `N(0,1/16)` with fixed exponential-moment control. Equivalently,
\[
\boxed{Y_D\Longrightarrow N(0,1)}
\tag{2.2}
\]
in empirical law, with enough uniform integrability for the fixed quadratic truncations used below.

For any pair probability `w`, let its density relative to `q_0` be
\[
r_j=mw_j.
\tag{2.3}
\]
Then `E_{q_0}r=1`. If `w` is exact-flat at depth `delta`, summing (1.2) over `a in D` gives
\[
\mathbb E_wY_D
=\frac4{\sqrt p}\sum_{a\in D}m_a(w)
=-\frac{4d\delta}{\sqrt p}.
\tag{2.4}
\]
Thus, if
\[
\sqrt p\,\delta\to c
\]
and `d/p->1/4`, then
\[
\boxed{\mathbb E_wY_D\to-c.}
\tag{2.5}
\]
The conjectured constant corresponds exactly to radial mean `-1` in the standardized field `Y_D`.

---

# 3. A new deterministic half-support collision inequality

The next lemma uses only nonnegativity, support size and the radial mean. It is independent of Fourier invertibility.

For real numbers `y_1,...,y_m`, a nonnegative density `r` on `{1,...,m}`, and a support set `S=supp(r)`, define
\[
C(r)=\frac1m\sum_j r_j^2,
\qquad
K_d(y)=\max_{|A|\le d}\frac1m\sum_{j\in A}(1-y_j)_+^2.
\tag{3.1}
\]

### Theorem P07-A.29 — support-aware one-sided collision bound

Assume
\[
\frac1m\sum_jr_j=1,
\qquad
\frac1m\sum_jr_jy_j=-a,
\qquad
|S|\le d.
\tag{3.2}
\]
Then
\[
\boxed{
C(r)\ge\frac{(1+a)^2}{K_d(y)}.
}
\tag{3.3}
\]

**Proof.** For any `lambda>=0`, put
\[
h_j=\lambda(1-y_j).
\]
For `r_j>0`, completing the square gives
\[
r_j^2\ge2h_jr_j-(h_j)_+^2,
\]
while for `r_j=0` the stronger form
\[
r_j^2\ge2h_jr_j-(h_j)_+^2\mathbf1_{j\in S}
\]
is also true. Averaging and using (3.2),
\[
C(r)
\ge2\lambda(1+a)
-\lambda^2\frac1m\sum_{j\in S}(1-y_j)_+^2
\ge2\lambda(1+a)-\lambda^2K_d(y).
\]
Optimize the quadratic at
\[
\lambda=(1+a)/K_d(y),
\]
which proves (3.3). `square`

The function `(1-y)_+^2` is decreasing on `(-infinity,1]` and zero above `1`. Hence `K_d(y)` is simply the average of `(1-y_j)_+^2` over the `d` smallest `y_j` values (up to irrelevant ties).

---

# 4. Sharp source consequence at the conjectured constant

Apply Theorem P07-A.29 to the **optimal prime flat certificate**. By (1.7), its support has exactly `d` pair sites. By (2.4),
\[
a_p=\frac{4d\delta_D}{\sqrt p}.
\tag{4.1}
\]
Under the fair source law,
\[
\frac dm\to\frac12.
\tag{4.2}
\]
By the empirical Gaussian limit, the `d` smallest `Y_D` values have asymptotic cutoff zero, and therefore
\[
K_d(Y_D)
\xrightarrow{\mathbb P}
K_*:=\mathbb E[(1-Z)^2\mathbf1_{\{Z\le0\}}],
\qquad Z\sim N(0,1).
\tag{4.3}
\]
Using
\[
\mathbb E[Z\mathbf1_{Z\le0}]=-\frac1{\sqrt{2\pi}},
\qquad
\mathbb E[Z^2\mathbf1_{Z\le0}]=\frac12,
\]
we get
\[
\boxed{
K_*=1+\sqrt{\frac2\pi}.
}
\tag{4.4}
\]

Consequently, on any prime subsequence on which
\[
\sqrt p\,\delta_D\to1
\tag{4.5}
\]
in probability, Theorem P07-A.29 gives the new necessary collision bound
\[
\boxed{
\liminf\; m\sum_jw_j^2
\ge
C_*:=\frac4{1+\sqrt{2/\pi}}
\approx2.2248369485
}
\tag{4.6}
\]
in probability.

This is stronger than the unconstrained radial `L^2` lower bound because it uses the **exact prime support fraction** `|supp w|/m ->1/2`.

---

# 5. New explicit construction: the half-support hinge law hits the sharp radial constant

The previous lower bound is not merely formal. There is a canonical positive law that attains it asymptotically.

Let `S_D` be the set of the `d` smallest values of `Y_D(j)` among `j in M`. On the source-high-probability event that the `d`-th order statistic is below `1` (it actually converges to `0`), define
\[
A_D:=\frac1m\sum_{j\in S_D}(1-Y_D(j)),
\tag{5.1}
\]
and the density
\[
\boxed{
r_D^{\rm hing}(j)
=\frac{(1-Y_D(j))\mathbf1_{\{j\in S_D\}}}{A_D},
\qquad
w_D^{\rm hing}(j)=\frac{r_D^{\rm hing}(j)}m.
}
\tag{5.2}
\]
This is a genuine positive probability with **exactly `d` support sites**.

Set
\[
A_*:=\mathbb E[(1-Z)\mathbf1_{\{Z\le0\}}]
=\frac12+\frac1{\sqrt{2\pi}}.
\tag{5.3}
\]
The empirical Gaussian theorem gives
\[
A_D\xrightarrow{\mathbb P}A_*.
\tag{5.4}
\]
Also
\[
\mathbb E[Z(1-Z)\mathbf1_{\{Z\le0\}}]
=-\frac1{\sqrt{2\pi}}-\frac12
=-A_*.
\tag{5.5}
\]
Therefore
\[
\boxed{
\mathbb E_{w_D^{\rm hing}}Y_D\xrightarrow{\mathbb P}-1.
}
\tag{5.6}
\]
Equivalently, if
\[
\bar m_D^{\rm hing}
=\frac1d\sum_{a\in D}m_a(w_D^{\rm hing}),
\]
then
\[
\boxed{
\sqrt p\,\bar m_D^{\rm hing}\xrightarrow{\mathbb P}-1.
}
\tag{5.7}
\]
Thus the hinge law hits **exactly the conjectured radial depth constant** while already matching the exact prime optimizer's support size.

Its collision is
\[
m\sum_j(w_D^{\rm hing}(j))^2
=
\frac{m^{-1}\sum_{j\in S_D}(1-Y_D(j))^2}{A_D^2}
\xrightarrow{\mathbb P}
\frac{K_*}{A_*^2}.
\]
Since `K_*=2A_*`,
\[
\boxed{
 m\sum_j(w_D^{\rm hing}(j))^2
\xrightarrow{\mathbb P}
\frac2{A_*}
=rac4{1+\sqrt{2/\pi}}
=C_*.
}
\tag{5.8}
\]
So the hinge law asymptotically **attains the support-aware lower bound**. In this precise sense it is the `L^2`/collision-optimal half-support radial certificate at the sharp constant.

This is a materially different primal construction from the full-support Gibbs tilt. The Gibbs law is entropy-optimal for a prescribed radial mean; the new hinge law is collision-optimal once the exact prime half-support geometry is imposed.

### What is still missing

The hinge law only has the correct **average** selected moment. It has not yet been proved that
\[
m_a(w_D^{\rm hing})=-p^{-1/2}+o(p^{-1/2})
\]
uniformly over `a in D`, let alone exactly. Hence (5.2) is not yet a theta-feasible flat certificate and does **not** prove an `O(sqrt p)` theta bound by itself.

---

# 6. Exact Fourier energy budget and a new forced complementary-dispersion constant

The collision optimum has a useful Fourier interpretation.

For any pair probability `w`, form the symmetric probability on `Z_p\setminus{0}` by
\[
p(\pm j)=w_j/2.
\]
Its real Fourier coefficients are exactly `m_a(w)`. Parseval gives
\[
p\sum_xp(x)^2
=1+2\sum_{a\in M}m_a(w)^2.
\tag{6.1}
\]
Because
\[
\sum_xp(x)^2=\frac12\sum_jw_j^2,
\]
we have the exact identity
\[
\boxed{
\frac p{p-1}\,m\sum_jw_j^2
=1+2\sum_{a\in M}m_a(w)^2.
}
\tag{6.2}
\]
Also, for every nonzero pair site `j`,
\[
\sum_{a\in M}\phi_a(j)=-\frac12,
\]
so every pair probability satisfies
\[
\boxed{
\sum_{a\in M}m_a(w)=-\frac12.
}
\tag{6.3}
\]

For the hinge law, (5.7), (6.3), and `d/p ->1/4` imply
\[
\sqrt p\,\bar m_D^{\rm hing}\to-1,
\qquad
\sqrt p\,\bar m_{M\setminus D}^{\rm hing}\to+1.
\tag{6.4}
\]
Define the within-group dispersions
\[
V_D(w)=\sum_{a\in D}(m_a-\bar m_D)^2,
\qquad
V_C(w)=\sum_{a\notin D}(m_a-\bar m_C)^2.
\tag{6.5}
\]
Using (5.8) in (6.2), the total Fourier energy tends to `(C_*-1)/2`. The two group means contribute asymptotically `1/4+1/4=1/2`. Therefore
\[
\boxed{
V_D(w_D^{\rm hing})+V_C(w_D^{\rm hing})
\xrightarrow{\mathbb P}
\gamma_*:=\frac{C_*-2}{2}
=\frac{1-\sqrt{2/\pi}}{1+\sqrt{2/\pi}}
\approx0.112418471.
}
\tag{6.6}
\]
This constant is not a numerical fit; it is the exact half-Gaussian collision defect.

There is a second consequence for the **true exact-flat optimizer**. Suppose along a prime source subsequence
\[
\sqrt p\,\delta_D\to1.
\]
Then its selected dispersion is exactly zero,
\[
V_D(w_D^{\rm opt})=0.
\]
The support-aware collision lower bound (4.6), Parseval (6.2), and the complement mean from (6.3) force
\[
\boxed{
\liminf V_C(w_D^{\rm opt})\ge\gamma_*
\approx0.112418471.
}
\tag{6.7}
\]
Thus a sharp prime optimizer **cannot** make both selected and unselected Fourier moments nearly flat. Exact flatness on the selected half necessarily expels at least `gamma_*` of transverse `l2` energy into the unselected half.

In the physical primal `f=(m+delta)/(1+delta)`, adding the common `delta` does not change within-complement variance. Hence (6.7) equivalently says that, at the sharp constant, the allowed physical coefficients of the optimal prime theta primal have asymptotic total variance at least `gamma_*` around their own mean.

This is a new structural obstruction to overly uniform primal ansätze. It is compatible with Conjecture 18; it says what any sharp proof must accommodate.

---

# 7. A concrete new primal repair problem

The hinge construction suggests a more source-specific attack than another all-sign RIP theorem.

Let `S_D` be the `d` lowest radial sites from Section 5 and let
\[
C_{D,S_D}=(\phi_a(j))_{a\in D,\,j\in S_D}
\tag{7.1}
\]
be the `d x d` cosine matrix. On prime order the relevant Fourier-minor nonsingularity implies this basis matrix is nonsingular in the equivalent real-even system used in the earlier positive-basis reduction. An exact flat certificate supported on `S_D` exists precisely when
\[
\boxed{x_D:=-C_{D,S_D}^{-1}\mathbf1>0.}
\tag{7.2}
\]
After normalization,
\[
w_j=\frac{x_j}{\mathbf1^Tx},
\qquad
\delta=\frac1{\mathbf1^Tx}.
\tag{7.3}
\]

The hinge law supplies an explicit positive comparison vector of the right support and right radial scale. Put, schematically,
\[
x_D^{\rm hing}:=\sqrt p\,w_D^{\rm hing}.
\tag{7.4}
\]
Then the average coordinate of
\[
C_{D,S_D}x_D^{\rm hing}+\mathbf1
\tag{7.5}
\]
over the selected rows is `o_P(1)`, while (6.6) quantifies the total transverse Fourier budget that remains.

The next concrete P07-A lemma is therefore the **support-preserving hinge repair estimate**
\[
\boxed{
\left\|\operatorname{diag}(x_D^{\rm hing})^{-1}
C_{D,S_D}^{-1}
\bigl(C_{D,S_D}x_D^{\rm hing}+\mathbf1\bigr)
\right\|_\infty<1-o(1).
}
\tag{7.6}
\]
If (7.6) holds with the correct normalization, then `x_D=-C^{-1}1` is positive on exactly the hinge support. A quantitative version showing
\[
\mathbf1^Tx_D=(1+o(1))\sqrt p
\]
would give an exact-flat certificate with
\[
\delta_D\ge(1-o(1))/\sqrt p
\]
and hence the sharp theta constant on prime orders, subject still to the expectation/uniform-integrability step. This is a primal positive-basis repair problem and does not duplicate P07-B's Fourier-dual exceptional-frequency route.

The important change from the previous Gibbs route is that the starting vector now already satisfies the **exact prime support cardinality** and the **sharp radial constant** simultaneously.

---

# 8. Obligation ledger

- **Full source endpoint:** unchanged, `alpha_LL: 1/2 -> 1/2`; no arbitrary-`n` sharp theorem yet.
- **New proved prime fact:** every optimal flat measure has exactly `d` nonzero pair sites, using the earlier exact-rank theorem plus the zero-origin lemma.
- **New proved deterministic lemma:** support-aware one-sided collision bound (3.3).
- **New source theorem:** at sharp radial constant, any prime optimizer has collision at least
  \[
  C_*=4/(1+\sqrt{2/\pi}).
  \]
- **New explicit construction:** the half-support hinge law attains both radial constant `1` and collision `C_*` while using exactly `d` sites, with high probability.
- **New exact obstruction constant:** sharp exact flatness forces at least
  \[
  \gamma_*=(1-\sqrt{2/\pi})/(1+\sqrt{2/\pi})
  \]
  of complement transverse Fourier variance.
- **Remaining gap:** prove support-preserving positive repair (7.6), or obtain a different exact-flat correction with the same radial scale; then upgrade the resulting prime high-probability statement to the requested expectation and to general odd `n`.

Status remains **OPEN / PROVED PARTIAL**. Candidate arguments here should receive later independent review before any publication claim.
