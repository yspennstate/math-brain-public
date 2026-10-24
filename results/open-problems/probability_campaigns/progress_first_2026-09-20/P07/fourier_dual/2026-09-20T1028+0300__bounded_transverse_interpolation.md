Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED** — GPT-6 / maximum was requested as an owner preference, but this runtime exposes no authenticated completed-run effort telemetry or binding model/effort selector, so I do not claim otherwise.

# P07-B — bounded transverse Fourier interpolation replaces the full covariance-tube bottleneck

**Native role:** `P07-B`, task `6aabe797a39081919acc889f29f4c556`  
**Repository / branch:** private `yspennstate/math-open-problems` / `master`  
**Captured start master:** `4c358240ab500c3c1d47a89fa018b0a10803d7bd`  
**Fresh pre-write master:** `440025cb40571d82048668eabaf795bfb11547a0`  
**Previous own substantive report:** `probability_campaigns/progress_first_2026-09-20/P07/fourier_dual/2026-09-20T0927+0300__gibbs_radial_exceptional_frequencies.md`, creation commit `4cd4938de5aea3a33a808d03c0a01fee220b93eb`.  
**Complementary P07-A checkpoint used:** `probability_campaigns/progress_first_2026-09-20/P07/primal/2026-09-20T1008+0300__profiled_gibbs_flat_homotopy.md`, creation commit `4c358240ab500c3c1d47a89fa018b0a10803d7bd`. P07-A owns the primal/profiled-homotopy route. This report uses its exact-flat objective only to sharpen the Fourier-dual bottleneck; it does not duplicate its homotopy proof.

**Outside target:** Randomstrasse101, arXiv:2603.29571, Conjecture 18; primary partial-result paper arXiv:2502.16227.  
**Source endpoint:** for the dense random undirected circulant model,
\[
\mathbb E\vartheta(G_n)=(1+o(1))\sqrt n.
\]
**Inherited rigorous source bound:**
\[
\sqrt n\le \mathbb E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]
The fixed full-source metric therefore remains
\[
\boxed{\alpha_{LL}=1/2\to1/2.}
\]
Status: **OPEN / PROVED PARTIAL**. No arbitrary-`n` improvement of the published theta bound is claimed in this report.

The new point is that the previous missing lemma `STCL(beta)` — a uniform minimum-eigenvalue bound throughout an endogenous `O(beta^2)` Gibbs tube — is stronger than necessary. There is an exact alternative: solve one **bounded transverse Fourier interpolation problem** for the actual radial Gibbs residual. If the required correcting function has `L^infinity` norm `O(beta^2)`, then adding a bounded amount of the excluded-origin uniform law restores positivity while preserving exact flatness, and one obtains `delta_D=Omega(n^{-1/2})`. The corresponding dual norm is a static `L^1` small-ball quantity for random cosine polynomials, with no pathwise Hessian and no independence assumption on the Gibbs coordinates.

---

## 1. Setup inherited from P07-B and P07-A

Let `n` be odd,
\[
M=\{1,\dots,(n-1)/2\},\qquad D\subset M,\qquad d=|D|,
\]
and
\[
\phi_a(j)=\cos(2\pi aj/n),\qquad
\Phi(j)=(\phi_a(j))_{a\in D}.
\]
Let `q_0` be the uniform probability on `Z_n\setminus\{0\}`. Then, exactly,
\[
\mathbb E_{q_0}\phi_a=-\frac1{n-1},
\tag{1.1}
\]
\[
\mathbb E_{q_0}\phi_a^2=\frac{n-2}{2(n-1)},
\qquad
\mathbb E_{q_0}\phi_a\phi_b=-\frac1{n-1}\quad(a\ne b).
\tag{1.2}
\]
For a fixed `beta>0`, the previous P07-B report constructed the excluded-origin Gibbs law
\[
p_{\beta,D}(j)=\frac{e^{-\beta X_D(j)}}{\sum_{k\ne0}e^{-\beta X_D(k)}},
\qquad
X_D(j)=\frac1{\sqrt n}\sum_{a\in D}\phi_a(j),
\tag{1.3}
\]
with `p(0)=0`. Write its relative density with respect to `q_0` as
\[
R(j):=\frac{p_{\beta,D}(j)}{q_0(j)}=(n-1)p_{\beta,D}(j),
\qquad \mathbb E_{q_0}R=1,
\tag{1.4}
\]
and its selected moment vector
\[
m:=\mathbb E_{p_{\beta,D}}\Phi
=\mathbb E_{q_0}[R\Phi].
\tag{1.5}
\]
Put
\[
\bar m:=\frac1d\mathbf1^Tm,
\qquad
r:=m-\bar m\mathbf1,
\qquad
\mathbf1^Tr=0.
\tag{1.6}
\]
The previous report proved, for every fixed `beta`,
\[
\bar m=-\frac{\beta}{4\sqrt n}+o_{\mathbb P}(n^{-1/2}),
\tag{1.7}
\]
and
\[
\|r\|_2^2\le R_*(\beta)+o_{\mathbb P}(1),
\qquad
R_*(\beta):=\frac{e^{\beta^2/16}-1}{2}-\frac{\beta^2}{32}
=\frac{\beta^4}{1024}+O(\beta^6).
\tag{1.8}
\]
The exact moment-polytope identity remains
\[
\mathbb E\vartheta(G_n)=1+\mathbb E\frac1{\delta_D},
\tag{1.9}
\]
where `delta_D` is the largest common negative selected cosine moment attainable by a symmetric probability on `Z_n`.

P07-A's newest report proves that exact flat positive certificates exist along a profiled Gibbs homotopy and converge to `delta_D`. The issue here is different: can the **specific radial Gibbs residual `r`** be removed by a uniformly bounded time-domain Fourier correction?

---

# 2. Exact transverse geometry of the excluded-origin uniform law

Let
\[
u:=d^{-1/2}\mathbf1,
\qquad P:=I-uu^T.
\]
For `z in u^perp`, define the real cosine polynomial
\[
f_z(j):=\langle z,\Phi(j)\rangle
=\sum_{a\in D}z_a\phi_a(j),
\qquad j\ne0.
\tag{2.1}
\]
Because `sum_a z_a=0`, (1.1) gives
\[
\boxed{\mathbb E_{q_0}f_z=0.}
\tag{2.2}
\]
Using (1.2) and
\[
\sum_{a\ne b}z_az_b=-\|z\|_2^2,
\]
one gets the exact transverse Parseval identity
\[
\boxed{
\mathbb E_{q_0}f_z^2
=\frac{n}{2(n-1)}\|z\|_2^2.
}
\tag{2.3}
\]
Thus there is no Euclidean conditioning issue at the base measure: all transverse selected directions have the same `L^2(q_0)` norm. The only possible obstruction to a bounded correction is an `L^1/L^2` small-ball failure of an endogenous transverse trigonometric polynomial.

---

# 3. The bounded interpolation constant and its exact LP dual

Define a linear map from bounded symmetric functions on `Z_n\setminus\{0\}` to transverse selected moments by
\[
\mathcal T_D h
:=P\,\mathbb E_{q_0}[h(J)\Phi(J)]\in u^\perp.
\tag{3.1}
\]
Symmetrizing `h(j)` with `h(-j)` does not change `T_D h` and does not increase `||h||_infinity`, so symmetry costs nothing.

Define the **actual-residual bounded interpolation cost**
\[
\boxed{
K_D(\beta)
:=\inf\left\{K\ge0:\exists h,\ \|h\|_\infty\le K,\ \mathcal T_D h=r\right\}.
}
\tag{3.2}
\]
This is finite because the selected cosine rows are linearly independent on the nonzero sites.

## Theorem P07-B.12 — exact dual formula

\[
\boxed{
K_D(\beta)
=
\sup_{\substack{z\in u^\perp\\z\ne0}}
\frac{|\langle r,z\rangle|}
{\mathbb E_{q_0}|f_z(J)|}.
}
\tag{3.3}
\]

### Proof

For `z in u^perp`,
\[
\langle z,\mathcal T_Dh\rangle
=\mathbb E_{q_0}[h(J)f_z(J)].
\tag{3.4}
\]
Therefore the support function of the convex symmetric set
\[
\mathcal T_D\{h:\|h\|_\infty\le K\}
\]
in direction `z` equals
\[
K\,\mathbb E_{q_0}|f_z|.
\tag{3.5}
\]
By finite-dimensional Hahn-Banach separation, `r` lies in this image exactly when
\[
|\langle r,z\rangle|
\le K\mathbb E_{q_0}|f_z|
\qquad\forall z\in u^\perp.
\tag{3.6}
\]
Taking the least such `K` proves (3.3). `square`

This formula is important because it is **residual-specific**. It does not ask for a uniform covariance lower bound on every vector and every point of a path. It asks only whether the actual source-generated transverse Gibbs residual defines a bounded functional on the `L^1(q_0)` norm of the random transverse cosine space.

---

# 4. A stronger static Kashin width that suffices

Define the transverse `L^1/L^2` width
\[
\boxed{
\rho_D
:=\inf_{\substack{z\in u^\perp\\\|z\|_2=1}}
\mathbb E_{q_0}|f_z(J)|.
}
\tag{4.1}
\]
By (2.3), a lower bound `rho_D>=c>0` is exactly a Kashin-type `L^1-L^2` inequality for the random selected cosine subspace after removal of the radial direction.

From (3.3), Cauchy gives immediately
\[
\boxed{
K_D(\beta)\le\frac{\|r\|_2}{\rho_D}.
}
\tag{4.2}
\]
Hence the preceding Gibbs dispersion estimate (1.8) implies, on any event where `rho_D>=c`,
\[
K_D(\beta)
\le \frac{\sqrt{R_*(\beta)+o(1)}}c
=O_c(\beta^2).
\tag{4.3}
\]

The full Kashin width (4.1) is stronger than necessary. The genuinely minimal missing statement is the residual-aligned bound
\[
\boxed{
K_D(\beta)\le C\beta^2.
}
\tag{4.4}
\]
I will call this `TRBI(beta,C)` — **transverse residual bounded interpolation**. It is a single static Fourier statement for the actual mask and actual residual. No independent copy of the Fourier field is introduced.

---

# 5. New constructive theorem: bounded interpolation gives an exact positive flat certificate

The useful point is that (4.4) does not merely control a signed correction. A bounded correction can be converted to a bona fide positive probability while preserving exact selected flatness.

Assume there is an `h` with
\[
\|h\|_\infty\le K,
\qquad
\mathcal T_Dh=r.
\tag{5.1}
\]
Write
\[
\mu:=\mathbb E_{q_0}h,
\qquad
\lambda:=\frac1d\mathbf1^T\mathbb E_{q_0}[h\Phi].
\tag{5.2}
\]
Since `P E[h Phi]=r`, necessarily
\[
\mathbb E_{q_0}[h\Phi]=r+\lambda\mathbf1.
\tag{5.3}
\]
Now define the nonnegative relative density
\[
\boxed{
G(j):=R(j)-h(j)+K,
\qquad j\ne0.
}
\tag{5.4}
\]
Indeed `h(j)<=K` and `R(j)>=0`, so `G(j)>=0` pointwise. Its mass is
\[
Z:=\mathbb E_{q_0}G=1-\mu+K,
\tag{5.5}
\]
and because `|mu|<=K`,
\[
\boxed{1\le Z\le1+2K.}
\tag{5.6}
\]
Let `p^*` be the symmetric probability on `Z_n` with `p^*(0)=0` and relative density `G/Z` with respect to `q_0` on the nonzero sites.

Using (1.5), (1.6), (5.3), and the fact that the constant relative density `1` has every selected moment `-1/(n-1)`, one obtains for **every** `a in D`
\[
\boxed{
\mathbb E_{p^*}\phi_a
=\frac{\bar m-\lambda-K/(n-1)}Z.
}
\tag{5.7}
\]
Thus `p^*` has exactly equal selected moments. No covariance inversion, no clipping error and no approximate flatness remain.

It remains only to show that the common value in (5.7) is negative at scale `n^{-1/2}`. This requires a very cheap bound on `lambda`.

Because
\[
\lambda
=\mathbb E_{q_0}\left[h(J)\frac1d\sum_{a\in D}\phi_a(J)\right],
\]
Cauchy and `||h||_infinity<=K` give
\[
|\lambda|
\le K\sqrt{\mathbb E_{q_0}\left(\frac{S_D(J)}d\right)^2}.
\tag{5.8}
\]
The exact raw second moment is
\[
\mathbb E_{q_0}S_D(J)^2
=\frac{d(n-2d)}{2(n-1)},
\tag{5.9}
\]
so
\[
\boxed{
|\lambda|
\le K\sqrt{\frac{n-2d}{2d(n-1)}}.
}
\tag{5.10}
\]
For source-typical `d/n ->1/4`, the square root is `(1+o(1))/sqrt(n)`.

Combining (5.6)--(5.10), whenever `-bar m>|lambda|`,
\[
\boxed{
\delta_D
\ge
\frac{-\bar m-|\lambda|}{1+2K}.
}
\tag{5.11}
\]
This is a deterministic implication from the radial Gibbs law plus one bounded Fourier interpolant.

---

# 6. Exact theorem-sized lemma that removes the iterated-log loss

The previous missing lemma `STCL(beta)` asked for a minimum covariance eigenvalue throughout an endogenous tube. The construction above shows that the following is enough and is strictly more targeted.

## Missing lemma `TRBI(beta,C)`

For one sufficiently small fixed `beta>0`, prove that there is a finite constant `C` such that
\[
\boxed{
\mathbb P\{K_D(\beta)>C\beta^2\}=O(n^{-1/2}).
}
\tag{6.1}
\]

### Why it suffices

The radial free-energy proof in the preceding report has variance `O_beta(1/n)` for the partition function and its first derivatives. Therefore for every fixed `beta>0` and any fixed slack, the radial mean estimate (1.7) has fixed-gap failure at most `O_beta(1/n)` after Chebyshev, while the binomial density event `d/n in [1/5,3/10]` has exponentially small failure. In particular, for all sufficiently large `n`, outside an `O_beta(n^{-1})` event,
\[
-\bar m\ge\frac\beta{5\sqrt n}
\tag{6.2}
\]
and, from (5.10),
\[
|\lambda|\le\frac{2K}{\sqrt n}.
\tag{6.3}
\]
Choose `beta` small enough that
\[
C\beta^2\le\frac\beta{20}.
\tag{6.4}
\]
Then on the intersection of the good events,
\[
-\bar m-|\lambda|
\ge\frac\beta{10\sqrt n},
\]
and (5.11) gives
\[
\boxed{
\delta_D
\ge
\frac{\beta}{10(1+2C\beta^2)\sqrt n}.
}
\tag{6.5}
\]
On the exceptional event use the universal excluded-origin uniform certificate
\[
\delta_D\ge\frac1{n-1}.
\tag{6.6}
\]
Thus (6.1) implies
\[
\mathbb E\frac1{\delta_D}=O(\sqrt n),
\qquad
\boxed{\mathbb E\vartheta(G_n)=O(\sqrt n).}
\tag{6.7}
\]
Hence `TRBI(beta,C)` removes the published `sqrt(log log n)` loss completely. It does **not** by itself prove the sharp leading constant `1`.

---

# 7. A still stronger but cleaner random-Fourier lemma

By (4.2) and (1.8), `TRBI` follows from a source-static statement that no longer mentions the Gibbs law:

> **Transverse Kashin inequality `TKI(c)`.** There is an absolute `c>0` such that
> \[
> \mathbb P\{\rho_D<c\}=O(n^{-1/2}),
> \tag{7.1}
> \]
> where
> \[
> \rho_D=\inf_{z\perp\mathbf1,\ \|z\|_2=1}
> \frac1{n-1}\sum_{j\ne0}
> \left|\sum_{a\in D}z_a\cos(2\pi aj/n)\right|.
> \tag{7.2}
> \]

Because (2.3) gives `L^2(q_0)^2=n/[2(n-1)]` for every unit transverse `z`, (7.1) says precisely that the random transverse cosine subspace has a constant `L^1/L^2` width. This is a dependence-aware small-ball theorem for the **same source mask**. It is not an assertion that the time-domain Fourier coordinates are independent.

`TKI(c)` is stronger than `TRBI`: it controls every transverse target, whereas `TRBI` controls only the actual Gibbs residual. The new dual formula (3.3) makes clear that proving the stronger uniform theorem is optional. Any direct argument exploiting the special residual `r` is enough.

---

# 8. Why this is materially different from `STCL` and from P07-A

The earlier `STCL(beta)` route required
\[
\lambda_{min}\nabla^2\psi_D(\lambda)\ge c_\beta
\]
for **every** point in an endogenous `O(beta^2)` parameter ball. A single nearly singular covariance direction anywhere in that tube would kill the hypothesis even if the actual residual never uses it.

The new route instead asks for the affine interpolation of one vector `r`. Its exact obstruction is the scalar quotient (3.3). The correction is performed directly in the time domain and positivity is restored by the `+K` term, which is itself a flat selected-frequency perturbation because the excluded-origin uniform law has the same cosine moment on every nonzero frequency.

This also separates P07-B cleanly from P07-A. P07-A proves that the exact positive flat optimizer is reached by an information-geometric homotopy. P07-B now gives a different constructive route: **radial Gibbs -> bounded transverse Fourier correction -> add bounded flat uniform mass -> exact positive flat certificate**. The routes meet at the same moment-polytope target but use different mathematics.

---

# 9. Failed route learned from this run

The orthogonal `L^2(q_0)` correction is explicit: because the transverse covariance under `q_0` is `n/[2(n-1)] I`, one can take
\[
h_{2}(j)=\frac{2(n-1)}n\sum_{a\in D}r_a\phi_a(j).
\tag{9.1}
\]
It satisfies `T_D h_2=r` and
\[
\|h_2\|_{L^2(q_0)}^2
=\frac{2(n-1)}n\|r\|_2^2
=O_\mathbb P(\beta^4).
\tag{9.2}
\]
However, `L^2` alone gives no useful uniform bound on `||h_2||_infinity`; a source-dependent Fourier polynomial can have rare large peaks. Simply clipping `h_2` destroys the exact transverse moments. This is why the quotient formulation (3.3) matters: the unused time-domain degrees of freedom must be exploited to lower the `L^infinity` norm **without changing the required Fourier data**.

A certified finite LP for `K_D(beta)` at moderate `n` would be evidence only. It would not prove (6.1) or (7.1) asymptotically.

---

# 10. Next concrete attack

The next P07-B iteration should attack `TRBI` before the stronger `TKI` unless a uniform argument falls out automatically.

The most direct dual form is
\[
\boxed{
\sup_{z\perp\mathbf1}
\frac{|\mathbb E_{p_{\beta,D}}f_z|}
{\mathbb E_{q_0}|f_z|}
=O(\beta^2)
}
\tag{10.1}
\]
with `O(n^{-1/2})` failure, because for `z perp 1`,
\[
\langle r,z\rangle=\mathbb E_{p_{\beta,D}}f_z.
\tag{10.2}
\]
There is an exact first-order cancellation:
\[
\mathbb E_{q_0}f_z=0,
\qquad
\mathbb E_{q_0}[X_D f_z]=0
\quad(z\perp\mathbf1),
\tag{10.3}
\]
where the second identity follows from the base covariance having no radial-transverse block. Therefore the numerator in (10.1) begins at **quadratic order in `beta`**. This matches the `O(beta^2)` target and explains why `TRBI` is the natural scale.

A productive next proof attempt is therefore a dependence-aware second-order comparison of
\[
R(j)-1+\beta\big(X_D(j)-\mathbb E_{q_0}X_D\big)
\tag{10.4}
\]
against the `L^1` norm of transverse `f_z`, exploiting the random Fourier support before applying a full uniform Kashin theorem. If this residual-specific comparison closes, the iterated-log loss disappears without any pathwise covariance theorem.

---

## 11. Result status

- Full source conjecture: **OPEN**.
- Published-bound exponent: **`alpha_LL=1/2 -> 1/2`**.
- Exact transverse `L^2` identity (2.3): **PROVED PARTIAL**.
- Exact bounded-interpolation LP duality (3.3): **PROVED PARTIAL**.
- Constructive positive exact-flat repair (5.4)--(5.11): **PROVED PARTIAL**.
- `TRBI(beta,C)` implication `E theta(G_n)=O(sqrt(n))`: **PROVED CONDITIONAL**.
- `TRBI(beta,C)` itself: **CONJECTURAL MISSING LEMMA**.
- Stronger `TKI(c)`: **CONJECTURAL SUFFICIENT LEMMA**, not assumed true by fiat.

No shared ledger, peer report, historical report, public endpoint, email, Drive file, permission, schedule, workflow or canonical ownership file was modified in this run.

## `ledger_delta`

```yaml
ledger_delta:
  role: "P07-B"
  native_task_id: "6aabe797a39081919acc889f29f4c556"
  target: "Randomstrasse101 Conjecture 18 / random-circulant Lovasz theta"
  input_master: "4c358240ab500c3c1d47a89fa018b0a10803d7bd"
  prewrite_master: "440025cb40571d82048668eabaf795bfb11547a0"
  previous_report: "probability_campaigns/progress_first_2026-09-20/P07/fourier_dual/2026-09-20T0927+0300__gibbs_radial_exceptional_frequencies.md"
  complementary_checkpoint: "probability_campaigns/progress_first_2026-09-20/P07/primal/2026-09-20T1008+0300__profiled_gibbs_flat_homotopy.md"
  metric: "alpha_LL"
  metric_before: "1/2"
  metric_after: "1/2"
  new_proved_partial:
    - "exact L_infinity interpolation dual K_D(beta)=sup |<r,z>|/E|f_z|"
    - "bounded interpolation plus flat uniform mass yields an exact positive flat moment certificate"
    - "deterministic depth lower bound delta_D >= (-bar m-|lambda|)/(1+2K)"
  new_missing_lemma: "TRBI(beta,C): K_D(beta)=O(beta^2) with O(n^-1/2) failure"
  stronger_optional_lemma: "TKI(c): constant transverse L1/L2 width for the random cosine subspace"
  implication: "TRBI removes sqrt(log log n), yielding E theta(G_n)=O(sqrt(n)); sharp leading constant 1 remains"
  status: "OPEN / PROVED PARTIAL"
```
