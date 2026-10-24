Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED** — GPT-6 / maximum was requested as an owner preference, but this runtime exposes no authenticated completed-run effort telemetry or binding model/effort selector, so I do not claim otherwise.

# P07-B — adaptive positive quadratic tilt reduces the iterated-log problem to a mean interpolation bound

**Status:** **OPEN / PROVED PARTIAL** on Randomstrasse101 Conjecture 18.  
**Native role:** `P07-B`, task `6aabe797a39081919acc889f29f4c556`.  
**Repository / branch:** private `yspennstate/math-open-problems` / `master`.  
**Fresh pre-write master:** `54d24129090cc4c2bb418eef7cc4bd4835173677`.  
**Previous own substantive report:** `probability_campaigns/progress_first_2026-09-20/P07/fourier_dual/2026-09-20T1714+0300__physical_variance_imbalance_duality.md`.  
**Latest complementary P07-A checkpoint read:** `probability_campaigns/progress_first_2026-09-20/P07/primal/2026-09-20T1745+0300__bipositive_basis_plucker_volume_balance.md`. P07-A owns the primal basis / complementary-minor / Pluecker-volume route. This report stays on the Fourier-moment interpolation route and uses none of P07-A's optimizer-selection claims.

**Outside target:** Bandeira et al., *Randomstrasse101: Open Problems of 2025*, arXiv:2603.29571, Conjecture 18.  
**Primary partial result:** A. S. Bandeira, J. Blasiok, D. Dmitriev, U. Faure, A. Kireeva, D. Kunisky, *The Lovasz number of random circulant graphs*, arXiv:2502.16227.  
**Exact endpoint:** for the dense random undirected circulant source model,
\[
\mathbb E\vartheta(G_n)=(1+o(1))\sqrt n.
\]
The source bound remains
\[
\sqrt n\le \mathbb E\vartheta(G_n)\le C\sqrt{n\log\log n},
\]
so the fixed full-source metric is still
\[
\boxed{\alpha_{LL}=1/2\to1/2.}
\]
No improved arbitrary-`n` theta bound is claimed in this report.

The exact Fourier LP and assignment-time repository history were already recovered in the first P07-B iterations and were checked again only to maintain normalization. In the source paper the frequency-primal form is
\[
\max n y_0
\quad\text{s.t.}\quad y_k=y_{n-k},\quad \|y\|_1=1,\quad y\ge0,\quad \langle y,f_k\rangle=0\ \text{on edge differences},
\]
with the equivalent frequency dual
\[
\min 1+n t_0
\quad\text{s.t.}\quad t_k=t_{n-k},\quad Ft\ge0,\quad t_k=-1/n\ \text{on edge differences}.
\]
The inherited moment-polytope normalization used below is
\[
\delta_D:=\max\left\{\delta\ge0:\exists\text{ symmetric probability }p\text{ on }\mathbb Z_n,\ 
\mathbb E_p\cos(2\pi aJ/n)=-\delta\ \forall a\in D\right\},
\tag{0.1}
\]
with
\[
\mathbb E\vartheta(G_n)=1+\mathbb E\frac1{\delta_D}.
\tag{0.2}
\]

The previous route was

`QBI with O(n^{-1/2}) failure -> analytic Gibbs remainder -> TRBI -> E theta=O(sqrt n)`.

The main point of this run is that the high-probability QBI requirement and the analytic remainder are both unnecessary. An **exact positive quadratic density**, with a mask-adaptive scalar tilt, turns a mere **first-moment bound on the quadratic interpolation norm** into `E theta=O(sqrt n)`.

---

## 1. Exact source moments on the excluded-origin law

Let
\[
M=\{1,\ldots,m\},\qquad m=(n-1)/2,
\]
let `D subset M` be the Bernoulli-`1/2` source mask, and write `d=|D|`. Let `q_0` be uniform on `Z_n\setminus{0}` and put
\[
\phi_a(j)=\cos(2\pi aj/n),\qquad
S_D(j)=\sum_{a\in D}\phi_a(j),\qquad
X(j)=X_D(j):=\frac{S_D(j)}{\sqrt n}.
\tag{1.1}
\]
For nonzero time sites the folded cosine identities give
\[
\mathbb E_{q_0}\phi_a=-\frac1{n-1},
\tag{1.2}
\]
and
\[
\mathbb E_{q_0}[\phi_a\phi_b]
=\frac{\frac n2\mathbf1_{a=b}-1}{n-1}.
\tag{1.3}
\]
Hence, with
\[
M_k:=\mathbb E_{q_0}X^k,
\]
one has exactly
\[
\boxed{M_1=-\frac{d}{(n-1)\sqrt n}},
\tag{1.4}
\]
and
\[
\boxed{M_2=\frac{d(n/2-d)}{n(n-1)}}.
\tag{1.5}
\]
Define the source-typical density event
\[
\mathcal B_n:=\left\{\frac n8\le d\le\frac{3n}{8}\right\}.
\tag{1.6}
\]
On `B_n`,
\[
\boxed{\frac1{64}\le M_2\le\frac18}
\tag{1.7}
\]
for every sufficiently large odd `n`; the upper constant is deliberately coarse. Since `d` is binomial with mean `(n-1)/4`,
\[
\Pr(\mathcal B_n^c)\le 2e^{-c n}
\tag{1.8}
\]
for an absolute `c>0`.

There is also an exact relation with the same-mask physical field from the previous report. Extend
\[
Y(0)=0,\qquad Y(\pm a)=\varepsilon_a:=2\mathbf1_{a\in D}-1,
\]
and put
\[
G_D(j)=\frac{\widehat Y(j)}{\sqrt n}
=\frac2{\sqrt n}\sum_{a\in M}\varepsilon_a\phi_a(j).
\tag{1.9}
\]
Because `sum_{a in M} phi_a(j)=-1/2` for every nonzero `j`, one has pointwise
\[
\boxed{X(j)=\frac14G_D(j)-\frac1{4\sqrt n}.}
\tag{1.10}
\]
The previous report proved, for every transverse selected test
\[
f_z(j)=\sum_{a\in D}z_a\phi_a(j),\qquad \sum_{a\in D}z_a=0,
\]
the exact cancellations
\[
\mathbb E f_z=0,\qquad \mathbb E[f_zG_D]=0,
\tag{1.11}
\]
and
\[
\langle r_D''(0),z\rangle=\frac1{16}\mathbb E[f_zG_D^2].
\tag{1.12}
\]
Combining (1.10)--(1.12) gives the useful exact identity
\[
\boxed{\mathbb E[f_zX^2]=\langle r_D''(0),z\rangle.}
\tag{1.13}
\]
Thus the transverse selected Fourier moments of `X^2` are **exactly** the quadratic Gibbs target; there is no Taylor error in (1.13).

---

## 2. Quadratic interpolation norm

For a bounded even function `h` on the nonzero time sites, let
\[
\mathcal T_Dh
:=P_{\mathbf1^\perp}
\left(\bigl(\mathbb E_{q_0}[h\phi_a]\bigr)_{a\in D}\right),
\tag{2.1}
\]
where the projection is in `R^D`. Define the quadratic interpolation cost
\[
\boxed{
K_D^{(2)}
:=\inf\{\|h\|_\infty:\mathcal T_Dh=r_D''(0)\}.
}
\tag{2.2}
\]
This is the same `K_D^(2)` isolated in the preceding reports. Restricting to even `h` costs nothing: replacing `h(j)` by `(h(j)+h(-j))/2` preserves every cosine moment and does not increase its sup norm.

Fix an interpolant with `||h||_infty <= K_D^(2)+eta`, and suppress `eta>0` until the end. Since its transverse moment vector equals `r_D''(0)`, there is a scalar `lambda_h` such that
\[
\left(\mathbb E[h\phi_a]\right)_{a\in D}
=r_D''(0)+\lambda_h\mathbf1_D.
\tag{2.3}
\]
Averaging (2.3) and using `sum_D phi_a=sqrt(n) X` gives
\[
\boxed{
\lambda_h=\frac{\sqrt n}{d}\mathbb E[hX].
}
\tag{2.4}
\]
Therefore
\[
\boxed{
|\lambda_h|
\le\frac{\sqrt n}{d}K_D^{(2)}\sqrt{M_2}.
}
\tag{2.5}
\]

---

# 3. New theorem: an exact positive quadratic equalizer

The earlier Gibbs construction used `exp(-beta X)` and then had to control every higher Taylor order. Here we replace the exponential by a specially centered quadratic polynomial.

Assume `d>0` and `M_2>0`, and define
\[
\gamma_D:=\frac{M_3}{M_2}.
\tag{3.1}
\]
For `beta>0`, put
\[
\boxed{
R_{\beta,D}(j)
:=1-\beta X(j)+\frac{\beta^2}{2}
\left(X(j)-\frac{\gamma_D}{2}\right)^2.
}
\tag{3.2}
\]

## Theorem P07-B.27 — exact quadratic equalization

Let `h` satisfy (2.3), and define
\[
Q_{\beta,D}(j)
:=R_{\beta,D}(j)-\frac{\beta^2}{2}h(j).
\tag{3.3}
\]
Then:

1. the selected Fourier moment vector of `Q_{beta,D}` is **exactly constant** on `D`;
2. if
   \[
   \beta|\gamma_D|\le\frac1{64},\qquad
   \beta K_D^{(2)}\le\frac1{64},\qquad
   \beta\le\frac1{64},
   \tag{3.4}
   \]
   then, after letting `eta downarrow0`, `Q_{beta,D}` is strictly positive on every nonzero time site;
3. on `B_n`, under (3.4), the common unnormalized selected moment obeys
   \[
   \boxed{
   \overline m(Q_{\beta,D})
   \le-\frac{\beta}{16\sqrt n}.
   }
   \tag{3.5}
   \]

### Proof

**Exact equalization.** Expand (3.2):
\[
R_{\beta,D}
=1-\beta X+\frac{\beta^2}{2}X^2
-\frac{\beta^2\gamma_D}{2}X
+\frac{\beta^2\gamma_D^2}{8}.
\tag{3.6}
\]
The constant and `X` terms have flat selected cosine moments: the constant has the same moment `-1/(n-1)` for every selected frequency, and for transverse `z`,
\[
\mathbb E[f_zX]=0
\tag{3.7}
\]
by (1.10)--(1.11). By (1.13), the transverse moment vector of `X^2` is `r_D''(0)`. Hence
\[
\mathcal T_D R_{\beta,D}=\frac{\beta^2}{2}r_D''(0).
\]
Equation (2.3) gives
\[
\mathcal T_DQ_{\beta,D}=0,
\]
which proves exact equality of all selected moments.

**Pointwise positivity.** Set `u=beta X` and `a=beta gamma_D/2`. Then
\[
R_{\beta,D}=1-u+\frac12(u-a)^2.
\]
The minimum over real `u` equals `1/2-a`, and therefore
\[
R_{\beta,D}\ge\frac12-\frac{\beta|\gamma_D|}{2}
\ge\frac{31}{64}.
\tag{3.8}
\]
Moreover
\[
\left|\frac{\beta^2}{2}h\right|
\le\frac{\beta^2K_D^{(2)}}2
\le\frac1{8192}.
\]
So `Q_{beta,D}>0` pointwise.

**Radial sign and scale.** Since `sum_{a in D} phi_a=sqrt(n)X`, the common selected moment of an exactly flat vector equals
\[
\overline m(Q_{\beta,D})
=\frac{\sqrt n}{d}\mathbb E[Q_{\beta,D}X].
\tag{3.9}
\]
By the definition `gamma_D=M_3/M_2`, the cubic term cancels *exactly*:
\[
\begin{aligned}
\mathbb E[R_{\beta,D}X]
&=M_1-\beta M_2
+\frac{\beta^2}{2}
\left(M_3-\gamma_D M_2+\frac{\gamma_D^2}{4}M_1\right)\\
&=M_1-\beta M_2+\frac{\beta^2\gamma_D^2}{8}M_1.
\end{aligned}
\tag{3.10}
\]
Both `M_1` terms are nonpositive. Thus, by Cauchy-Schwarz,
\[
\mathbb E[Q_{\beta,D}X]
\le-\beta M_2+\frac{\beta^2}{2}K_D^{(2)}\sqrt{M_2}.
\tag{3.11}
\]
On `B_n`, `sqrt(M_2)>=1/8`; hence (3.4) implies
\[
1-\frac{\beta K_D^{(2)}}{2\sqrt{M_2}}
\ge\frac{15}{16}.
\tag{3.12}
\]
Also, by (1.5),
\[
\frac{\sqrt n}{d}M_2
=\frac{n/2-d}{\sqrt n(n-1)}
\ge\frac1{8\sqrt n}
\tag{3.13}
\]
on `B_n`. Combining (3.9)--(3.13) yields the stronger bound `-(15/128) beta/sqrt(n)`; (3.5) follows. `square`

---

# 4. Adaptive tilt: no high-probability QBI is needed

Set
\[
\boxed{
\beta_D:=\frac1{64\,[1+K_D^{(2)}+|\gamma_D|]}.
}
\tag{4.1}
\]
Then all three smallness conditions (3.4) hold automatically, for every realized mask with `M_2>0`.

Let
\[
Z_D:=\mathbb E_{q_0}Q_{\beta_D,D}.
\]
The preceding positivity gives `Z_D>0`. A direct use of `|M_1|<=1/sqrt(n)`, `M_2<=1/8` on `B_n`, `beta<=1/64`, `beta|gamma|<=1/64`, and `beta K<=1/64` gives the deliberately coarse deterministic upper bound
\[
\boxed{Z_D\le2}
\tag{4.2}
\]
for all sufficiently large odd `n` on `B_n`.

Define a symmetric probability on `Z_n` by
\[
p_D(0)=0,
\qquad
p_D(j)=\frac{Q_{\beta_D,D}(j)}{(n-1)Z_D},\quad j\ne0.
\tag{4.3}
\]
Its selected cosine moments are exactly equal, by Theorem P07-B.27. By (3.5) and (4.2), every such moment is at most
\[
-\frac{\beta_D}{32\sqrt n}.
\]
Therefore:

## Theorem P07-B.28 — deterministic adaptive depth bound

On `B_n`,
\[
\boxed{
\delta_D
\ge
\frac{1}{2048\,[1+K_D^{(2)}+|\gamma_D|]\sqrt n}.
}
\tag{4.4}
\]
Equivalently,
\[
\boxed{
\frac1{\delta_D}
\le
2048\sqrt n\,[1+K_D^{(2)}+|\gamma_D|].
}
\tag{4.5}
\]

This is the main structural improvement of the run. The old route demanded a fixed constant bound on `K_D^(2)` outside an `O(n^{-1/2})` exceptional event, because on failure it paid the trivial `theta<=n` bound. Equation (4.5) instead **adapts the Fourier tilt continuously to the realized interpolation cost**. Large `K_D^(2)` is paid linearly rather than converted into a catastrophic all-or-nothing failure event.

There is also no analytic Gibbs remainder: the transverse cancellation is an exact degree-two identity.

---

# 5. The auxiliary scalar gamma has bounded source mean

The new reduction only helps if `gamma_D=M_3/M_2` is harmless on `B_n`. It is.

For every fixed nonzero time site, decompose the source field as
\[
X_D(j)
=-\frac1{4\sqrt n}
+\frac1{2\sqrt n}\sum_{a\in M}\varepsilon_a\phi_a(j).
\tag{5.1}
\]
The second term is a Rademacher sum. Since
\[
\sum_{a\in M}\phi_a(j)^2=\frac{n-2}{4},
\]
the exact fourth-moment inequality for Rademacher sums gives a uniform absolute bound
\[
\sup_{n,j\ne0}\mathbb E_D|X_D(j)|^4\le C_4.
\tag{5.2}
\]
Averaging over `j` yields
\[
\mathbb E_D M_4\le C_4.
\tag{5.3}
\]
By Holder,
\[
|M_3|\le M_4^{3/4}.
\tag{5.4}
\]
On `B_n`, `M_2>=1/64`, so Jensen gives
\[
\boxed{
\mathbb E_D\bigl[|\gamma_D|\,\mathbf1_{\mathcal B_n}\bigr]
\le64\,\mathbb E M_4^{3/4}
\le64C_4^{3/4}
=O(1).
}
\tag{5.5}
\]
No independence among the time-domain Fourier coordinates is used: only independence of the original Bernoulli/Rademacher mask bits is used in the one-site fourth moment.

---

# 6. New exact theorem-sized missing lemma: a mean QBI is enough

The excluded-origin uniform law itself gives the universal fallback
\[
\delta_D\ge\frac1{n-1}
\tag{6.1}
\]
for every mask, because every nonzero cosine moment under `q_0` is exactly `-1/(n-1)`. Thus `1/delta_D<=n-1` even on `B_n^c`.

Combine (0.2), (1.8), (4.5), (5.5), and (6.1). We obtain:

## Theorem P07-B.29 — expectation reduction

If
\[
\boxed{
\mathbb E\left[K_D^{(2)}\,\mathbf1_{\mathcal B_n}\right]=O(1),
}
\tag{Mean-QBI}
\]
then
\[
\boxed{
\mathbb E\vartheta(G_n)=O(\sqrt n).
}
\tag{6.2}
\]
In particular **Mean-QBI removes the entire published `sqrt(log log n)` loss**.

### Proof

By (4.5),
\[
\mathbb E\left[\frac1{\delta_D};\mathcal B_n\right]
\le2048\sqrt n
\left(
1+\mathbb E[K_D^{(2)};\mathcal B_n]
+\mathbb E[|\gamma_D|;\mathcal B_n]
\right).
\]
The last term is `O(1)` by (5.5), and Mean-QBI controls the middle term. On the complement, (6.1) and (1.8) give
\[
\mathbb E\left[\frac1{\delta_D};\mathcal B_n^c\right]
\le(n-1)\Pr(\mathcal B_n^c)=o(\sqrt n).
\]
Now use (0.2). `square`

### Why this is strictly weaker than the previous missing lemma

The previous `QBI` target was essentially
\[
\Pr\{K_D^{(2)}>C\}=O(n^{-1/2}),
\]
plus a separate uniform `O(beta^3)` interpolation theorem for the Gibbs remainder. The new theorem needs neither. `K_D^(2)` may be unbounded on a non-negligible set, provided its **mean on the overwhelmingly likely balanced-density event stays bounded**. This is a materially weaker target and changes the probabilistic architecture of the remaining proof.

A direct high-probability consequence is also available from (4.5): for any deterministic `L>=1`, on `B_n cap {K_D^(2)+|gamma_D|<=L}`,
\[
\vartheta(G_n)\le C L\sqrt n.
\tag{6.3}
\]
Thus any useful tail estimate for `K_D^(2)` transfers immediately to a theta tail bound. For the expectation problem, however, the first-moment statement Mean-QBI is enough.

Mean-QBI does **not** yet prove the sharp leading constant `1`; it proves the square-root order and hence removes the iterated logarithm. Achieving `(1+o(1))sqrt(n)` still requires a critical-scale, constant-sharp argument.

---

# 7. New exact involution behind the interpolation problem

There is one further structural identity that should be useful for attacking Mean-QBI. Recall
\[
G_D=\widehat Y/\sqrt n,
\qquad Y(0)=0,\quad Y(a)^2=1\ (a\ne0).
\]
With the unnormalized cyclic convolution used in the previous report,
\[
\widehat{G_D}=\sqrt n\,Y.
\]
Therefore
\[
\widehat{G_D*G_D}=nY^2=n\mathbf1_{\{a\ne0\}},
\]
and inversion gives the exact autocorrelation
\[
\boxed{
(G_D*G_D)(j)
=\begin{cases}
n-1,&j=0,\\
-1,&j\ne0.
\end{cases}
}
\tag{7.1}
\]
Define on time functions
\[
\mathcal K_D f:=\frac1{\sqrt n}G_D*f.
\tag{7.2}
\]
On the zero-mean subspace its Fourier multiplier is `Y`, so
\[
\boxed{\mathcal K_D^2=I.}
\tag{7.3}
\]
It is a self-adjoint orthogonal involution. The selected-frequency test functions satisfy exactly
\[
\boxed{\mathcal K_D f_z=f_z,}
\tag{7.4}
\]
while complement-supported Fourier functions lie in its `-1` eigenspace.

Thus `K_D^(2)` is not a generic random-Fourier extension constant. It is the `L^infty` cost of representing the particular quadratic target `X^2` after fixing only its transverse component in the **`+1` eigenspace of a random orthogonal involution generated by the same mask**. The global Kashin theorem is known to fail from the preceding runs, but Mean-QBI only asks for the expected extension cost of this source-generated quadratic vector.

This exact involution is the next attack: exploit the identity `K_D^2=I`, the deterministic simplex autocorrelation (7.1), and the fact that the target is a degree-two chaos generated by the same `Y`, to control the expected quotient
\[
K_D^{(2)}
=\sup_{z\perp\mathbf1}
\frac{|\langle r_D''(0),z\rangle|}{\mathbb E|f_z|}
\tag{7.5}
\]
directly in expectation. The preceding sparse-support and bounded-collision theorems remain available; only the high-collision mesoscopic class has to be controlled, now in **mean** rather than with `O(n^{-1/2})` failure.

---

# 8. Handoff, gaps, and next attack

### Proved this run

- Exact relation `T_D(X^2)=r_D''(0)` from the same-mask physical representation.
- Exact positive quadratic density `R_{beta,D}` whose only transverse selected moment is `(beta^2/2) r_D''(0)`.
- Exact bounded-interpolant correction producing **perfectly flat** selected moments with no analytic remainder.
- Adaptive deterministic depth bound
  \[
  \delta_D\ge c/[\sqrt n(1+K_D^{(2)}+|\gamma_D|)]
  \]
  on the source-typical density event.
- `E[|gamma_D|;B_n]=O(1)` from a same-mask one-site fourth-moment argument.
- Therefore **Mean-QBI**, `E[K_D^(2);B_n]=O(1)`, is sufficient for `E theta=O(sqrt n)`.
- Exact physical convolution involution `K_D^2=I` on zero-mean functions.

### Still open

- Mean-QBI itself is not proved here.
- The sharp leading constant `1` in Conjecture 18 is not proved.
- A finite LP certificate at any bounded `n` would remain evidence only, not an asymptotic solution.
- No dependent Fourier coordinates were treated as independent.

### Complementary P07-A handoff

P07-A need not reproduce this interpolation proof. The useful shared lemma is simply: **any primal/structural estimate implying `E[K_D^(2);B_n]=O(1)` now removes the iterated-log loss, without an `O(n^{-1/2})` bad-event theorem.** Conversely P07-B will not duplicate P07-A's bi-positive basis / Pluecker-volume selector.

### Next concrete attack

Prove Mean-QBI by decomposing the dual quotient (7.5) into the classes already solved in earlier runs and treating only the high-collision, mesoscopically delocalized remainder through the involution (7.2). The most promising form is a dependence-aware second-moment/chaining estimate for the source-generated quadratic target conditional on additive-energy level, integrated over the energy levels rather than union-bounded to `O(n^{-1/2})` failure. The target is now an expectation theorem, so logarithmic tail strata can be paid according to their probability instead of all being forced below one deterministic constant.
