Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED** — GPT-6 / maximum reasoning was requested as an owner preference, but this runtime exposes no authenticated completed-run effort telemetry or binding scheduler selector, so I do not claim otherwise.

# P07-B — positivity-preserving square-Newton Fourier correction and a new mean orbit criterion

**Status:** **OPEN / PROVED PARTIAL** on Randomstrasse101 Conjecture 18.  
**Native role:** `P07-B`, task `6aabe797a39081919acc889f29f4c556`.  
**Repository / branch:** private `yspennstate/math-open-problems` / `master`.  
**Fresh pre-write master:** `b18fa21185c8b647a03409b2ffb45ae916b8192e`.  
**Previous own substantive checkpoint:** `probability_campaigns/progress_first_2026-09-20/P07/fourier_dual/2026-09-20T2014+0300__cubic_preconditioning_matched_decoupling.md`.  
**Latest complementary checkpoint read:** `probability_campaigns/progress_first_2026-09-20/P07/primal/2026-09-20T2045+0300__repair_energy_obstruction_radial_cap_flattening.md`. P07-A owns the primal orthogonal-core / one-sided cap-flattening route. This report does not duplicate that work; it stays on a Fourier-dual feasible probability certificate.

**Outside target:** Bandeira et al., *Randomstrasse101: Open Problems of 2025*, arXiv:2603.29571, Conjecture 18.  
**Primary partial result:** A. S. Bandeira, J. Błasiok, D. Dmitriev, U. Faure, A. Kireeva, D. Kunisky, *The Lovász number of random circulant graphs*, arXiv:2502.16227.  
**Exact endpoint:** for the dense random undirected circulant source model on odd `n`,
\[
\mathbb E\vartheta(G_n)=(1+o(1))\sqrt n.
\]
The strongest inherited source bound remains
\[
\sqrt n\le \mathbb E\vartheta(G_n)\le C\sqrt{n\log\log n},
\]
so the fixed full-source metric remains
\[
\boxed{\alpha_{LL}=1/2\to1/2.}
\]
No improved arbitrary-`n` theta asymptotic is claimed here.

The source statement, exact Fourier LPs, strongest bound, and repository history were recovered already on assignment and are not rerun as an admission screen. For normalization, the frequency primal/dual pair remains
\[
\max n y_0
\quad\text{s.t.}\quad
 y_k=y_{n-k},\ \|y\|_1=1,\ y\ge0,\ \langle y,f_k\rangle=0
\ \text{on selected edge differences},
\]
\[
\min 1+n t_0
\quad\text{s.t.}\quad
 t_k=t_{n-k},\ Ft\ge0,\ t_k=-1/n
\ \text{on selected edge differences}.
\]
The inherited moment-depth identity is
\[
\mathbb E\vartheta(G_n)=1+\mathbb E\frac1{\delta_D}.
\tag{0.1}
\]

The previous run preconditioned the quadratic target by the exact same-mask involution and proved that the initial interpolant is a degree-at-most-three Rademacher chaos with bounded pointwise moments and low source-bit influences. It then isolated the same-mask fourth-moment recoupling lemma `SMR4` for the clipping route.

This run takes a genuinely different nonlinear step: **do not subtract a bounded interpolant at all**. Instead, cancel the Fourier residual by *adding a nonnegative square*. Positivity then becomes automatic. The resulting Newton-like orbit has an exact one-line contraction estimate, and the first nonlinear step is already dimension-free using the cubic theorem from the preceding run.

---

## 1. Full-group Fourier normalization

Let
\[
M=\{1,\ldots,(n-1)/2\},
\qquad
\varepsilon_a=2\mathbf1_{\{a\in D\}}-1,
\]
extend the signs evenly to `Z_n` by
\[
Y(0)=0,\qquad Y(\pm a)=\varepsilon_a,
\]
and define
\[
G=\frac{\widehat Y}{\sqrt n},
\qquad
\mathcal K h=\frac1{\sqrt n}G*h.
\tag{1.1}
\]
Use uniform probability `mu` on `Z_n` and write
\[
\langle f,h\rangle=\mathbb E_\mu[fh],
\qquad
\|h\|_p=(\mathbb E_\mu|h|^p)^{1/p}.
\]
For every selected-frequency transverse vector
\[
z=(z_a)_{a\in D},\qquad \sum_{a\in D}z_a=0,
\]
put
\[
f_z(x)=\sum_{a\in D}z_a\cos(2\pi ax/n).
\tag{1.2}
\]
The inherited exact multiplier identity is
\[
\boxed{\mathcal Kf_z=f_z.}
\tag{1.3}
\]
Also `K` kills the zero Fourier mode and is an `L^2(mu)` contraction.

Put
\[
\boxed{w=\frac{G^2}{16}.}
\tag{1.4}
\]
The preceding P07-B calculations give, for every transverse `f_z`, the exact quadratic target identity. Passing from the nonzero-site law to `mu` does not change the identity except by the same factor on both sides because `f_z(0)=0`. Thus `w` represents the full transverse quadratic moment defect.

The new construction below only uses (1.3), nonnegativity of a square, and ordinary `L^p` inequalities. No Fourier coordinate is treated as independent of another.

---

# 2. New deterministic lemma: cancel any represented Fourier residual by adding a positive square

Suppose an even mean-zero field `g` represents the current transverse selected-moment defect, in the sense that the defect functional is
\[
f_z\longmapsto \langle f_z,g\rangle.
\tag{2.1}
\]
Let
\[
\sigma=\|g\|_2.
\]
If `sigma=0`, the defect is already zero. Otherwise fix `A>0`, set
\[
\boxed{c^2=A\sigma,}
\tag{2.2}
\]
and define the nonnegative square
\[
\boxed{
s_g(x)=\left(c-\frac{g(x)}{2c}\right)^2
=c^2-g(x)+\frac{g(x)^2}{4c^2}.
}
\tag{2.3}
\]

## Theorem P07-B.35 — positive square cancellation

For every transverse selected test `f_z`,
\[
\boxed{
\langle f_z,g+s_g\rangle
=\left\langle f_z,\frac{g^2}{4c^2}\right\rangle.
}
\tag{2.4}
\]
Consequently the field
\[
\boxed{
g^+:=\mathcal K\left(\frac{g^2}{4c^2}\right)
}
\tag{2.5}
\]
represents the new transverse defect exactly:
\[
\boxed{
\langle f_z,g+s_g\rangle=\langle f_z,g^+\rangle.
}
\tag{2.6}
\]
Moreover `g^+` is mean zero, and
\[
\boxed{
\|g^+\|_2
\le
\frac{\|g\|_4^2}{4A\|g\|_2}.
}
\tag{2.7}
\]
The correction mass is exactly
\[
\boxed{
\mathbb E_\mu s_g
=A\sigma+\frac{\sigma}{4A}.
}
\tag{2.8}
\]

### Proof

Every transverse `f_z` has full-group mean zero. Expanding (2.3), the constant term therefore disappears and the linear term is exactly `-g`, giving (2.4). Equation (1.3) and self-adjointness of `K` give
\[
\left\langle f_z,\mathcal K\frac{g^2}{4c^2}\right\rangle
=
\left\langle \mathcal Kf_z,\frac{g^2}{4c^2}\right\rangle
=
\left\langle f_z,\frac{g^2}{4c^2}\right\rangle,
\]
which proves (2.6). Since the zero Fourier multiplier of `K` is `Y(0)=0`, `g^+` has mean zero. The `L^2` contraction of `K` and `c^2=A sigma` give
\[
\|g^+\|_2
\le\frac{\|g^2\|_2}{4A\sigma}
=
\frac{\|g\|_4^2}{4A\sigma},
\]
proving (2.7). Finally `Eg=0`, so
\[
\mathbb E s_g=c^2+\frac{\|g\|_2^2}{4c^2}
=A\sigma+\frac{\sigma}{4A}.
\]
QED.

### Why this is different from bounded interpolation

The earlier route sought a signed bounded function `h` and then had to prove that subtracting `h` did not destroy positivity. Here every correction is a square and is therefore positive by construction. There is no `L^infinity` interpolation norm and no pointwise clipping threshold in the feasibility argument. The only remaining analytic issue is whether the nonlinear residuals have summable `L^2` size.

---

# 3. Exact square-Newton orbit

Starting from a mean-zero representative `g_0`, define recursively, whenever `sigma_k:=||g_k||_2>0`,
\[
\boxed{
 c_k^2=A\sigma_k,
\qquad
 s_k=\left(c_k-\frac{g_k}{2c_k}\right)^2,
\qquad
 g_{k+1}=\mathcal K\left(\frac{g_k^2}{4A\sigma_k}\right).
}
\tag{3.1}
\]
If `sigma_k=0`, terminate the recursion. Define the time-domain kurtosis
\[
\boxed{
\kappa_k:=\frac{\|g_k\|_4^4}{\sigma_k^4}\ge1.
}
\tag{3.2}
\]
Then Theorem P07-B.35 gives the deterministic recursion
\[
\boxed{
\sigma_{k+1}
\le
\frac{\sqrt{\kappa_k}}{4A}\sigma_k.
}
\tag{3.3}
\]
The natural orbit burden is therefore
\[
\boxed{
\mathcal H_A(D)
:=\sum_{k\ge0}\sqrt{\kappa_k}\,\sigma_k,
}
\tag{3.4}
\]
with the convention that terminated terms vanish.

Because `kappa_k>=1`, finiteness of `H_A` implies both
\[
\sum_k\sigma_k<\infty
\quad\text{and}\quad
\sigma_k\to0.
\tag{3.5}
\]
It also controls the total mass of all square corrections:
\[
\boxed{
\sum_k\mathbb E s_k
\le
\left(A+\frac1{4A}\right)\mathcal H_A(D).
}
\tag{3.6}
\]

There is also a clean bound on the change in the **common** selected Fourier moment. For any even `h`, full-group cosine orthogonality gives the Bessel estimate
\[
\sum_{a\in D}|\langle h,\phi_a\rangle|^2
\le\frac12\|h\|_2^2,
\qquad \phi_a(x)=\cos(2\pi ax/n).
\tag{3.7}
\]
Hence
\[
\left|\frac1{|D|}\sum_{a\in D}\langle h,\phi_a\rangle\right|
\le\frac{\|h\|_2}{\sqrt{2|D|}}.
\tag{3.8}
\]
Applying this first to `g_k` and then to `g_k^2`, expansion (2.3) yields
\[
\boxed{
|\overline m_D(s_k)|
\le
\frac{\sigma_k}{\sqrt{2|D|}}
+
\frac{\sqrt{\kappa_k}\,\sigma_k}{4A\sqrt{2|D|}}.
}
\tag{3.9}
\]
Therefore
\[
\boxed{
\sum_k|\overline m_D(s_k)|
\le
\frac{1+1/(4A)}{\sqrt{2|D|}}\,\mathcal H_A(D).
}
\tag{3.10}
\]
This is the key radial estimate: if the same quantity that makes the nonlinear orbit summable has finite mean, the accumulated damage to the desired negative common Fourier moment is only `O(H_A/sqrt(n))` on a typical source mask.

---

# 4. Insert the actual random-circulant quadratic target

The previous run proved that the best first representative is not `w` itself but its exact involution preconditioner
\[
\boxed{g_0:=\mathcal K w.}
\tag{4.1}
\]
For every transverse selected test,
\[
\langle f_z,g_0\rangle=\langle f_z,w\rangle.
\tag{4.2}
\]
Thus `g_0` represents exactly the quadratic Fourier defect while having a much better source-mask structure: the preceding report proved that for every physical site, `g_0(x)` is a degree-at-most-three Rademacher chaos with bounded Walsh multiplicity, and in particular
\[
\boxed{
\mathbb E_D\|g_0\|_4^4\le26.
}
\tag{4.3}
\]
It also proved the nondegeneracy event
\[
\boxed{
\Pr\{\sigma_0^2<c_0\}=O(n^{-1})
}
\tag{4.4}
\]
for an absolute `c_0>0`, and the pointwise sub-Weibull tail
\[
\Pr\{|g_0(x)|>t\}\le C e^{-ct^{2/3}}.
\tag{4.5}
\]

The next theorem extracts a new consequence of those facts tailored specifically to the positive-square orbit.

## Theorem P07-B.36 — the first square-Newton weighted-kurtosis cost is dimension-free

For `g_0=K w`,
\[
\boxed{
\mathbb E_D\bigl[\sqrt{\kappa_0}\,\sigma_0\bigr]=O(1).
}
\tag{4.6}
\]
Consequently, for every fixed `A>0`, the first square-Newton residual satisfies
\[
\boxed{
\mathbb E_D\sigma_1=O(A^{-1}),
}
\tag{4.7}
\]
and the expected mass of the first positive correction is `O(A)`.

### Proof

Since
\[
\sqrt{\kappa_0}\,\sigma_0
=
\frac{\|g_0\|_4^2}{\sigma_0},
\tag{4.8}
\]
split according to the good event
\[
\mathcal G_n=\{\sigma_0^2\ge c_0\}.
\]
On `G_n`, (4.3) gives
\[
\mathbb E\left[
\frac{\|g_0\|_4^2}{\sigma_0}\mathbf1_{\mathcal G_n}
\right]
\le
c_0^{-1/2}\,(\mathbb E\|g_0\|_4^4)^{1/2}
=O(1).
\tag{4.9}
\]
On the bad event, interpolation on the probability space gives
\[
\|g_0\|_4^2\le\|g_0\|_\infty\|g_0\|_2,
\]
so the ratio in (4.8) is at most `||g_0||_infinity`. By the union bound applied to (4.5),
\[
\mathbb E\|g_0\|_\infty^2=O((\log n)^3).
\tag{4.10}
\]
Together with `P(G_n^c)=O(n^{-1})`, Cauchy-Schwarz yields
\[
\mathbb E[\|g_0\|_\infty\mathbf1_{\mathcal G_n^c}]
=O((\log n)^{3/2}n^{-1/2})=o(1).
\tag{4.11}
\]
This proves (4.6). Equation (3.3) then gives (4.7). Finally, (2.8) and `E sigma_0=O(1)` give expected first correction mass `O(A)` for fixed `A`. QED.

### Significance

The initial nonlinear correction no longer needs a conjectural small-ball or recoupling estimate. It is already rigorously dimension-free. The unresolved issue begins only after the first squaring has fed the source-dependent field back through the same Fourier multiplier.

---

# 5. Exact positive certificate from a summable square-Newton orbit

Now connect the orbit to the actual theta moment depth.

Return briefly to the nonzero-site law `q_0` from the preceding adaptive-quadratic report. Let
\[
X_D(j)=\frac1{\sqrt n}\sum_{a\in D}\cos(2\pi aj/n),
\qquad j\ne0,
\]
let
\[
M_k=\mathbb E_{q_0}X_D^k,
\qquad
\gamma_D=\frac{M_3}{M_2},
\]
and define the positive quadratic base
\[
R_{\beta,D}(j)
=
1-\beta X_D(j)
+\frac{\beta^2}{2}
\left(X_D(j)-\frac{\gamma_D}{2}\right)^2.
\tag{5.1}
\]
On
\[
\mathcal B_n=\{n/8\le |D|\le3n/8\},
\tag{5.2}
\]
the previous exact calculation gives, whenever `beta|gamma_D|` and `beta` are sufficiently small,
\[
R_{\beta,D}>0,
\tag{5.3}
\]
and, **before any interpolation correction**, its common selected moment obeys
\[
\boxed{
\overline m_{q_0}(R_{\beta,D})
\le-\frac{\beta}{8\sqrt n}.
}
\tag{5.4}
\]
Its transverse selected moment is exactly
\[
\frac{\beta^2}{2}
\times\text{the transverse moment of }w.
\tag{5.5}
\]

Extend `R_{beta,D}` to all of `Z_n` by assigning value zero at the origin; call the extension `\widetilde R_{beta,D}`. Since every transverse `f_z` vanishes at the origin, (5.5) becomes under full-group `mu`
\[
\boxed{
\langle f_z,\widetilde R_{\beta,D}\rangle_{\rm transverse}
=
\frac{\beta^2}{2}\langle f_z,g_0\rangle.
}
\tag{5.6}
\]
Also, for all sufficiently large odd `n`, (5.4) implies
\[
\boxed{
\overline m_D(\widetilde R_{\beta,D})
\le-\frac{\beta}{16\sqrt n}.
}
\tag{5.7}
\]

Assume for the moment that `H_A(D)<infinity`. Put
\[
\tau=\frac{\beta^2}{2}
\]
and define
\[
\boxed{
P_L
=\widetilde R_{\beta,D}
+\tau\sum_{k=0}^{L-1}s_k.
}
\tag{5.8}
\]
Every `P_L` is nonnegative. By Theorem P07-B.35, the transverse selected moment of `P_L` is represented exactly by
\[
\tau g_L.
\tag{5.9}
\]
Since `H_A<infinity` implies `sigma_L->0`, the transverse moment tends to zero. Equations (3.6) and monotone convergence show that
\[
P_\infty
=\widetilde R_{\beta,D}
+\tau\sum_{k\ge0}s_k
\tag{5.10}
\]
is an integrable nonnegative symmetric density whose selected Fourier moments are **exactly flat**.

The only remaining concern is that the positive squares might move their common value back toward zero. On `B_n`, (3.10) gives
\[
\sum_k|\overline m_D(\tau s_k)|
\le
\frac{\beta^2}{\sqrt n}
\left(1+\frac1{4A}\right)\mathcal H_A(D).
\tag{5.11}
\]
Here we used `|D|>=n/8` and a deliberately coarse absolute constant.

Choose a small absolute `b>0` and set the **mask-adaptive tilt**
\[
\boxed{
\beta_D
=
\frac{b}{1+|\gamma_D|+\mathcal H_A(D)}.
}
\tag{5.12}
\]
For example, after fixing `A>=1`, any sufficiently small absolute `b` (such as `b=1/256`) makes both the positivity conditions and
\[
\beta_D\left(1+\frac1{4A}\right)\mathcal H_A(D)
\le\frac1{32}
\tag{5.13}
\]
hold. Combining (5.7), (5.11), and (5.13), the exact common selected moment of `P_infinity` satisfies
\[
\boxed{
\overline m_D(P_\infty)
\le-\frac{\beta_D}{32\sqrt n}.
}
\tag{5.14}
\]

The total mass is bounded by an absolute constant depending only on fixed `A`. Indeed the quadratic base has mass at most `2` under the same smallness conditions, while (3.6) gives
\[
\tau\sum_k\mathbb E s_k
\le
\frac{\beta_D^2}{2}
\left(A+\frac1{4A}\right)\mathcal H_A(D)
=O_A(1).
\tag{5.15}
\]
In fact (5.12) makes the last term uniformly small after `b` is fixed sufficiently small. Therefore, after normalizing `P_infinity` to a probability measure, one obtains
\[
\boxed{
\delta_D
\ge
\frac{c_A\beta_D}{\sqrt n}
}
\tag{5.16}
\]
for an absolute `c_A>0` on `B_n`.

Equivalently,
\[
\boxed{
\frac1{\delta_D}
\le
C_A\sqrt n\,
\bigl(1+|\gamma_D|+\mathcal H_A(D)\bigr)
\qquad\text{on }\mathcal B_n.
}
\tag{5.17}
\]
This is a new feasible-certificate theorem. It requires no bounded signed interpolant and no rare-event declaration for a large interpolation norm.

---

# 6. New exact missing lemma: mean square-Newton orbit summability

The preceding adaptive-quadratic report already proved
\[
\mathbb E[|\gamma_D|\mathbf1_{\mathcal B_n}]=O(1),
\tag{6.1}
\]
and the source density failure has exponentially small probability. The universal moment-depth fallback handles `B_n^c`.

Therefore the entire iterated-logarithmic loss would be removed by the single orbit statement
\[
\boxed{
\mathbb E\bigl[
\mathcal H_A(D)\mathbf1_{\mathcal B_n}
\bigr]=O(1)
}
\tag{PSNO}
\]
for one fixed absolute `A`.

Indeed, (5.17), (6.1), the exponential tail of `B_n^c`, and (0.1) then give
\[
\boxed{
\mathbb E\vartheta(G_n)=O(\sqrt n).
}
\tag{6.2}
\]
This would remove the full published `sqrt(log log n)` loss. It would **not** yet prove the sharp leading constant `1`.

There is a particularly concrete sufficient form of `PSNO`. The initial term already satisfies Theorem P07-B.36. For the later same-mask iterates it is enough to prove:

## Missing lemma `PSNK` — positive-square Newton weighted kurtosis

For some fixed `A` and some absolute `C_*<4A`, for every `k>=1`,
\[
\boxed{
\mathbb E\left[
\sqrt{\kappa_k}\,\sigma_k\,
\mathbf1_{\mathcal B_n}
\right]
\le
C_*\,
\mathbb E\left[
\sigma_k\mathbf1_{\mathcal B_n}
\right].
}
\tag{PSNK}
\]
Then (3.3) gives
\[
\mathbb E[\sigma_{k+1};\mathcal B_n]
\le
\frac{C_*}{4A}
\mathbb E[\sigma_k;\mathcal B_n],
\tag{6.3}
\]
so the expected `L^2` residual decays geometrically. Summing `PSNK` and using the proved `k=0` estimate (4.6) gives `PSNO`.

This is the exact theorem-sized lemma for the next attack. It is narrower than asking for a global Kashin theorem or a uniform `L^1/L^2` bound over all selected Fourier polynomials: only one endogenous nonlinear orbit must satisfy a first-moment weighted-kurtosis estimate.

---

# 7. Relation to the previous `SMR4` bottleneck

The previous report isolated `SMR4`, a fourth-moment comparison between the actual same-mask multiplier and an independent multiplier after clipping. That remains a valid route, but the present construction shows it is not the only route.

The square-Newton recursion asks directly for
\[
\mathbb E[\sqrt{\kappa_k}\sigma_k]
\]
rather than a full fourth-moment comparison for every clipped low-influence residual. Positivity is automatic because the correction is a square. There is no signed `L^infinity` correction whose pointwise size has to be controlled.

The same-mask dependence has **not** disappeared: for `k>=1`, `g_k` is generated from the same mask that defines `K`, so one may not import the independent-multiplier estimate from the previous report as though it applied conditionally. The new obligation `PSNK` is exactly where that dependence still lives.

The first nonlinear step, however, is now completely proved: the cubic preconditioning theorem implies (4.6), so
\[
\mathbb E\sigma_1=O(A^{-1})
\]
with no independence fiction. This is substantive progress beyond merely renaming the recoupling gap.

---

# 8. A useful failed variant: coordinatewise positive squares are too expensive

One tempting construction is to correct each bad selected frequency separately with a square of the form
\[
(c_a+q_a\phi_a)^2.
\]
The linear term can indeed repair the chosen coordinate, with only a simple doubled-frequency spill. But optimizing the mass of such separate squares charges essentially an `l^1` norm of the residual coefficient vector. For the source quadratic residual, the proved information is naturally `l^2`-scale and the residual is spread over many frequencies; the crude `l^1` cost can therefore be as large as a square-root-of-dimension factor. That is too expensive for a constant-mass probability certificate.

The coupled field square (2.3) is precisely what avoids that loss: its mass is linear in the single `L^2` size `sigma`, while all frequencies are corrected simultaneously.

---

# 9. Obligation ledger

**PROVED PARTIAL in this run**

1. Any mean-zero physical interpolant can have its Fourier residual canceled by adding one **nonnegative square**, with exact new residual `K(g^2/(4c^2))`.
2. With `c^2=A||g||_2`, the nonlinear residual obeys the deterministic contraction formula
   \[
   \sigma_{k+1}\le(\sqrt{\kappa_k}/4A)\sigma_k,
   \]
   while the positive correction costs only `(A+1/(4A))sigma_k` mass.
3. The same orbit burden `H_A=sum sqrt(kappa_k)sigma_k` controls both total correction mass and cumulative drift of the common selected Fourier moment.
4. Using the preceding run's cubic preconditioner, the initial square-Newton weighted-kurtosis cost is rigorously dimension-free:
   \[
   \mathbb E[\sqrt{\kappa_0}\sigma_0]=O(1),
   \qquad
   \mathbb E\sigma_1=O(A^{-1}).
   \]
5. If `H_A` has bounded mean on the source-typical density event, an adaptive positive quadratic base plus the positive-square series gives an exact feasible probability certificate with
   \[
   1/\delta_D
   \le C_A\sqrt n(1+|\gamma_D|+H_A).
   \]

**CONDITIONAL**

- `PSNO`, or the local sufficient condition `PSNK`, implies
  \[
  \mathbb E\vartheta(G_n)=O(\sqrt n),
  \]
  removing the entire source iterated-logarithmic loss.

**NOT CLAIMED**

- `PSNK` is not yet proved for all later same-mask iterates.
- The source upper bound is therefore not yet improved in this report.
- The sharp `(1+o(1))sqrt(n)` leading constant remains open.
- No dependent Fourier coordinates were treated as independent.

---

# 10. Next concrete attack

Attack `PSNK` at `k=1` directly. The field
\[
g_1
=\mathcal K\left(\frac{g_0^2}{4A\sigma_0}\right)
\]
comes from the degree-at-most-three low-influence cubic preconditioner `g_0`. On the already proved event `sigma_0^2>=c_0`, the normalization is harmless. Expand `g_0^2` in the Walsh basis and classify the quartic physical moment of `g_1` into:

- independent-pairing terms;
- matched one-bit recouplings;
- genuine off-diagonal dependence cycles.

Unlike the previous clipped route, it is enough to bound the **weighted first moment** `E[sqrt(kappa_1)sigma_1]`, not a uniform fourth-moment norm. The target is to charge each genuine cycle to two low influences of `g_0`; the existing `O(1/n)` individual influence bound should then make the total cycle contribution dimension-free. A proof at `k=1` would establish the first post-cubic instance of `PSNK`; the same bookkeeping can then be tested for propagation under the square-Newton map.

**Handoff to P07-A:** the positive-square correction theorem is a Fourier-dual feasible-measure construction. P07-A's current one-sided cap-flattening / orthogonal-core work remains distinct; no primal file or ownership is changed.