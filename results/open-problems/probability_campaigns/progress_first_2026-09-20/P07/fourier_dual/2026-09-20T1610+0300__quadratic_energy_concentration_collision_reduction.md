Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED** — GPT-6 / maximum was requested as an owner preference, but this runtime exposes no authenticated completed-run effort telemetry or binding model/effort selector, so I do not claim otherwise.

# P07-B — quenched quadratic-energy concentration and a target-specific collision reduction

**Native role:** `P07-B`, task `6aabe797a39081919acc889f29f4c556`  
**Repository / branch:** private `yspennstate/math-open-problems` / `master`  
**Fresh pre-write master:** `8f85da4e95b29db2a06e796daae82b91cc5a458d`  
**Previous own substantive report:** `probability_campaigns/progress_first_2026-09-20/P07/fourier_dual/2026-09-20T1508+0300__selected_quadratic_energy_scale_sharpness.md`.  
**Complementary P07-A checkpoint read:** `probability_campaigns/progress_first_2026-09-20/P07/primal/2026-09-20T1544+0300__affine_barrier_buffered_hinge_repair.md`. P07-A owns the primal positive-certificate / buffered-hinge route; this report stays on the Fourier-dual quadratic interpolation obstruction.

**Outside target:** Bandeira et al., *Randomstrasse101: Open Problems of 2025*, arXiv:2603.29571, Conjecture 18.  
**Primary partial result:** A. S. Bandeira, J. Blasiok, D. Dmitriev, U. Faure, A. Kireeva, D. Kunisky, *The Lovasz number of random circulant graphs*, arXiv:2502.16227.  
**Exact source endpoint:** for the dense random undirected circulant model,
\[
\mathbb E\vartheta(G_n)=(1+o(1))\sqrt n.
\]
**Inherited rigorous source bound:**
\[
\sqrt n\le \mathbb E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]
Thus the fixed source metric remains
\[
\boxed{\alpha_{LL}=1/2\to1/2.}
\]
Status: **OPEN / PROVED PARTIAL**. No improved arbitrary-`n` theta asymptotic is claimed in this report.

The assignment-time source check, exact Fourier LP, and old TH18 attempts were already recovered once and are not rerun. The inherited exact normalization is
\[
\kappa_D=\frac1{n\delta_D},\qquad
\mathbb E\vartheta(G_n)=1+\mathbb E\frac1{\delta_D}.
\tag{0.1}
\]
The current Fourier-dual route is: prove the quadratic bounded-interpolation lemma `QBI`, then control the analytic `O(beta^3)` remainder, which together imply the earlier `TRBI` condition and hence `E theta(G_n)=O(sqrt n)`.

The last report proved only annealed macroscopic energy for the quadratic target and a constant-probability lower event. This run upgrades that to **quenched concentration with an `O(1/n)` fixed-deviation failure rate**, proves a high-probability `1/16` lower scale for the interpolation norm, and completely handles every adaptive dual direction of bounded additive collision. The unresolved class is now simultaneously high-collision and mesoscopically frequency-delocalized.

---

## 1. Inherited exact quadratic target

Let
\[
M=\{1,\ldots,m\},\qquad m=(n-1)/2,
\]
and
\[
\varepsilon_a=2\mathbf1_{\{a\in D\}}-1,\qquad
\xi_a=\mathbf1_{\{a\in D\}}=\frac{1+\varepsilon_a}{2}.
\tag{1.1}
\]
Extend the independent Rademachers evenly to `Z_n` by `Y(0)=0`, `Y(k)=epsilon_[k]`, and define
\[
W_a=(Y*Y)(a),\qquad U_a=W_a-1.
\tag{1.2}
\]
The exact design from the preceding reports is
\[
\boxed{
U_a=2\sum_{e\in E_a}\chi_e,
\qquad \chi_{\{r,s\}}=\varepsilon_r\varepsilon_s,
}
\tag{1.3}
\]
where every `E_a` has `m-1` edges, every unordered frequency edge belongs to exactly two `E_a`, and distinct `E_a,E_b` meet in one edge.

If
\[
Q_D=\sum_{a\in D}(W_a-\overline W_D)^2,
\tag{1.4}
\]
then the exact radial-Gibbs transverse second derivative is
\[
\boxed{
r_D''(0)=\frac1{16(n-1)}
\left(W_D-\overline W_D\mathbf1_D\right),
}
\tag{1.5}
\]
so
\[
\boxed{
\|r_D''(0)\|_2^2=\frac{Q_D}{256(n-1)^2}.
}
\tag{1.6}
\]
For the transverse moment operator `T_D`,
\[
T_DT_D^*=\lambda_n I,\qquad
\lambda_n=\frac{n}{2(n-1)}.
\tag{1.7}
\]
The last report showed `E Q_D/n^2 -> 1/2`; what was missing was source-probability concentration at the failure scale relevant to expectation bounds.

---

# 2. New theorem: the selected quadratic energy concentrates at scale `n^2`

Put
\[
F:=\sum_{a\in M}\xi_aU_a^2,
\qquad
S:=\sum_{a\in M}\xi_aU_a,
\qquad
d:=|D|.
\tag{2.1}
\]
On `d>0`, exactly
\[
Q_D=F-\frac{S^2}{d}.
\tag{2.2}
\]
As before the exponentially rare event `d=0` may be assigned `Q_D=0`.

## Theorem P07-B.22 — variance bound and quenched quadratic-energy law

There is an absolute constant `C` such that for every odd `n`,
\[
\boxed{
\operatorname{Var}(F)\le Cn^3.
}
\tag{2.3}
\]
Consequently, for every fixed `epsilon>0`,
\[
\boxed{
\Pr_D\left\{
\left|\frac{Q_D}{n^2}-\frac12\right|>\varepsilon
\right\}
=O_\varepsilon(n^{-1}).
}
\tag{2.4}
\]
In particular
\[
\boxed{
\|r_D''(0)\|_2^2
\xrightarrow{\mathbb P}\frac1{512},
}
\tag{2.5}
\]
with `O_epsilon(1/n)` failure for every fixed deviation.

### Proof of the variance bound

From (1.3),
\[
U_a^2
=4(m-1)+8\sum_{\substack{e,f\in E_a\\e<f}}
\chi_{e\triangle f},
\tag{2.6}
\]
where `triangle` denotes symmetric difference of the two frequency edges. Therefore
\[
F-\mathbb EF=L+A+B,
\tag{2.7}
\]
with
\[
L=2(m-1)\sum_a\varepsilon_a,
\tag{2.8}
\]
\[
A=4\sum_a\sum_{e<f\in E_a}\chi_{e\triangle f},
\tag{2.9}
\]
\[
B=4\sum_a\sum_{e<f\in E_a}
\varepsilon_a\chi_{e\triangle f}.
\tag{2.10}
\]
There is no hidden constant term in `A` or `B` because `e ne f`, while `e triangle f` has even size `2` or `4`. Also
\[
\mathbb EF=2m(m-1)=m(n-3).
\tag{2.11}
\]

The linear term is immediate:
\[
\|L\|_2^2=4m(m-1)^2=O(n^3).
\tag{2.12}
\]
It remains to bound the Walsh coefficient multiplicities in `A` and `B`.

For an unordered frequency edge `e={r,s}`, define its two design labels
\[
\mathcal L(e)=\{[r+s],[r-s]\}.
\tag{2.13}
\]
Then
\[
e\in E_a\iff a\in\mathcal L(e).
\tag{2.14}
\]
The two labels are distinct for odd `n` and `r ne s`.

For `A`, fix a Walsh support `R=e triangle f`.

- If `|R|=4`, the disjoint edges `e,f` form one of the three pairings of `R`, and their common design label lies in `L(e) cap L(f)`, which has size at most two. Thus there are at most six occurrences.
- If `|R|=2`, write `R={r,s}`. Then `e={v,r}`, `f={v,s}` for a common hidden vertex `v`. A common label requires one of the congruences
  \[
  [v\pm r]=[v\pm s].
  \]
  The same-sign branch would force `r=[s]`, impossible; the opposite-sign branch fixes `2v` as one of the four values `+-r+-s`. Because `n` is odd, `2` is invertible modulo `n`, so there are at most four hidden vertices, and for each at most two common labels. Thus the multiplicity is at most eight.

Hence every Walsh monomial in `A` has multiplicity at most an absolute constant. The number of indexed pairs `(a,{e,f})` is
\[
N=m\binom{m-1}{2}=O(n^3).
\tag{2.15}
\]
Walsh orthogonality therefore gives
\[
\boxed{\|A\|_2^2=O(n^3).}
\tag{2.16}
\]

For `B`, a resulting Walsh support has the form
\[
R=\{a\}\triangle e\triangle f,
\tag{2.17}
\]
and hence odd size `1,3`, or `5`. Its multiplicity is again universally bounded. Here is a direct case count.

If `a in R`, there are at most five choices for `a`; after removing it, `e triangle f` is fixed of size `2` or `4`, and the preceding argument gives only constantly many edge pairs carrying the prescribed label `a`. If `a notin R`, then `|R|=5` is impossible because `|e triangle f|<=4`. For `|R|=3`, the four-set `R union {a}` is partitioned into `e,f`; the edge containing the vertex `a` must itself have design label `a`, forcing `2a=+-s` for one of the three fixed vertices `s in R`, hence only constantly many `a`. For `|R|=1`, writing `R={s}`, the two edges share a hidden vertex and one endpoint is the label-vertex `a`; the condition that `{v,a}` has label `a` forces `v=[2a]`, and the second edge then gives either `a=+-s` or `3a=+-s`. Each congruence has at most three solutions for odd `n`. Thus every Walsh monomial in `B` also has absolute multiplicity bounded independently of `n`.

Using the same incidence count (2.15),
\[
\boxed{\|B\|_2^2=O(n^3).}
\tag{2.18}
\]
Finally
\[
\operatorname{Var}(F)
=\|L+A+B\|_2^2
\le3(\|L\|_2^2+\|A\|_2^2+\|B\|_2^2)
=O(n^3),
\]
which proves (2.3).

### From `F` to `Q_D`

The preceding report already proved the same-mask mean-removal estimate
\[
\boxed{
\mathbb E\frac{S^2}{d}=O(n),
}
\tag{2.19}
\]
with the convention `0` on `d=0`. Chebyshev applied to (2.3) gives, for fixed `epsilon>0`,
\[
\Pr\{|F-\mathbb EF|>\varepsilon n^2\}
=O_\varepsilon(n^{-1}),
\tag{2.20}
\]
while Markov and (2.19) give
\[
\Pr\left\{\frac{S^2}{d}>\varepsilon n^2\right\}
=O_\varepsilon(n^{-1}).
\tag{2.21}
\]
Since
\[
\frac{\mathbb EF}{n^2}
=\frac{(n-1)(n-3)}{2n^2}
=\frac12+O(n^{-1}),
\tag{2.22}
\]
(2.2), (2.20), and (2.21) prove (2.4), hence (2.5). `square`

### Consequence: high-probability scale sharpness

Define
\[
K_D^{(2)}
=\inf\{\|h\|_\infty:T_Dh=r_D''(0)\}.
\tag{2.23}
\]
The exact tight frame (1.7) says the minimum `L^2(q_0)` norm among such interpolants is
\[
\frac{\|r_D''(0)\|_2}{\sqrt{\lambda_n}}.
\tag{2.24}
\]
Since `||h||_infty>=||h||_2`, Theorem P07-B.22 improves the previous annealed lower bound to
\[
\boxed{
\Pr\left\{K_D^{(2)}<\frac1{16}-\varepsilon\right\}
=O_\varepsilon(n^{-1}).
}
\tag{2.25}
\]
Thus the constant-order quadratic interpolation cost is not merely an annealed phenomenon: it is forced on almost every source mask at the quantitative failure scale needed downstream.

---

# 3. New theorem: every bounded-collision adaptive direction is already harmless for `QBI`

For a transverse vector `z` supported on `D`, define
\[
f_z(j)=\sum_{a\in D}z_a\cos(2\pi aj/n),
\qquad
N(z):=\mathbb E_{q_0}|f_z|,
\tag{3.1}
\]
and its normalized fourth moment
\[
\mathcal K_4(z)
:=\frac{\mathbb E f_z^4}{(\mathbb E f_z^2)^2}.
\tag{3.2}
\]
The exact transverse frame gives
\[
\|f_z\|_2=\sqrt{\lambda_n}\|z\|_2.
\tag{3.3}
\]
Interpolation between `L^1,L^2,L^4` gives
\[
\|f_z\|_2^3\le\|f_z\|_1\|f_z\|_4^2,
\]
hence
\[
\boxed{
N(z)\ge\frac{\sqrt{\lambda_n}\|z\|_2}
{\sqrt{\mathcal K_4(z)}}.
}
\tag{3.4}
\]

## Theorem P07-B.23 — uniform adaptive bounded-collision control

For every fixed `K_0<infinity` and every fixed `epsilon>0`, outside an event of probability `O_epsilon(1/n)`, simultaneously for **all** mask-dependent transverse vectors `z=z(D)` with `K_4(z)<=K_0`,
\[
\boxed{
\frac{|\langle r_D''(0),z\rangle|}{N(z)}
\le
\frac{(1+\varepsilon)\sqrt{K_0}}{16}.
}
\tag{3.5}
\]
No independence between `z`, the selected set, and the quadratic field is used.

### Proof

Cauchy-Schwarz and (3.4) give deterministically
\[
\frac{|\langle r_D''(0),z\rangle|}{N(z)}
\le
\frac{\|r_D''(0)\|_2}{\sqrt{\lambda_n}}
\sqrt{\mathcal K_4(z)}.
\tag{3.6}
\]
By (2.5),
\[
\frac{\|r_D''(0)\|_2}{\sqrt{\lambda_n}}
\longrightarrow\frac1{16}
\tag{3.7}
\]
with `O_epsilon(1/n)` fixed-deviation failure. This proves (3.5) uniformly over the entire adaptive class. `square`

This is stronger than the preceding nonlinear Gibbs statement for bounded `K_4`: there the `L^2` residual had only a source-probability asymptotic with no quantitative `O(n^-1/2)` rate. At the quadratic level the target norm itself is now concentrated strongly enough to close the bounded-collision class at the required failure scale.

---

# 4. Explicit high-probability effective-support barrier for the quadratic target

The previous support barrier was `n^{1/2-o(1)}` because it passed through a truncated exponential. The pure quadratic target admits a cleaner logarithmic statement.

For each `a`, `U_a=W_a-1` is degree-two Rademacher chaos with
\[
\|U_a\|_2=\sqrt{2n-6}.
\tag{4.1}
\]
Bonami hypercontractivity gives, for every `p>=2`,
\[
\|U_a\|_p\le(p-1)\sqrt{2n-6}.
\tag{4.2}
\]
Taking `p=(A+3)log n`, Markov followed by a union bound over `m<n/2` frequencies yields, for every fixed `A>0`,
\[
\boxed{
\Pr\left\{\max_{a\in M}|U_a|>C_A\sqrt n\log n\right\}
=O(n^{-A}).
}
\tag{4.3}
\]
On this event,
\[
\|r_D''(0)\|_\infty
\le C_A\frac{\log n}{\sqrt n}.
\tag{4.4}
\]

For transverse `z`, define its coefficient effective support
\[
s_{\rm eff}(z)=\frac{\|z\|_1^2}{\|z\|_2^2}.
\tag{4.5}
\]
The deterministic inequality
\[
N(z)\ge
\lambda_n\frac{\|z\|_2^2}{\|z\|_1}
\tag{4.6}
\]
then gives
\[
\boxed{
\frac{|\langle r_D''(0),z\rangle|}{N(z)}
\le
C_A\frac{\log n}{\sqrt n}\,s_{\rm eff}(z)
}
\tag{4.7}
\]
simultaneously for every adaptive transverse `z`, with failure `O(n^{-A})`.

Hence every fixed-size quadratic obstruction must obey the explicit barrier
\[
\boxed{
s_{\rm eff}(z)\gtrsim\frac{\sqrt n}{\log n}.
}
\tag{4.8}
\]
In particular all directions with `s_eff<=sqrt(n)/(log n)^2` have quadratic dual ratio `o(1)` uniformly.

---

# 5. A finite tone-reservation obstruction — and why it does not obstruct this target

A literature check for the extension problem uncovered a directly relevant framework: H. Boche and U. J. Monich, *Tone Reservation for OFDM With Restricted Carrier Set*, IEEE Trans. Information Theory **65** (2019), 7935--7949, DOI `10.1109/TIT.2019.2932391`. Their Theorem 1 identifies uniform bounded extension with an `L^2/L^1` inequality for all information-frequency polynomials, while their Theorems 4--5 explain why positive-density and random information sets contain arithmetic-progression obstructions. This does **not** solve our target-specific random-circulant problem; it clarifies why the earlier global Kashin target was too strong.

For completeness, the finite cyclic obstruction needed here is elementary and can be proved directly.

## Proposition P07-B.24 — global transverse extension diverges on the source mask

With probability
\[
1-\exp\left(-\Omega\left(\frac{n^{2/3}}{\log n}\right)\right),
\tag{5.1}
\]
there is a transverse vector `z` supported on `D` such that
\[
\boxed{
\frac{\|f_z\|_2}{\|f_z\|_1}
\gtrsim
\frac{\sqrt{\log n}}{\log\log n}.
}
\tag{5.2}
\]
Thus no uniform constant Kashin/tone-reservation inequality can hold for all transverse directions of the dense random source mask.

### Proof

Let
\[
L=2\left\lfloor\frac16\log_2 n\right\rfloor.
\tag{5.3}
\]
Partition a fixed positive fraction of `M` into disjoint consecutive blocks of length `L`. Each block is entirely selected with probability `2^{-L}>=c n^{-1/3}`, independently across the blocks. There are `Theta(n/L)` blocks, so the probability that none is fully selected is at most the right side of (5.1).

On a fully selected block of length `L=2q`, put coefficient `+1` on its first `q` frequencies and `-1` on its last `q`. Then `sum z_a=0` and
\[
\|f_z\|_2=\sqrt{\lambda_nL}.
\tag{5.4}
\]
The corresponding complex exponential polynomial is a difference of two adjacent length-`q` Dirichlet kernels, so its absolute value is at most twice that of a length-`q` Dirichlet kernel. On the `n`-point cyclic grid,
\[
|D_q(2\pi j/n)|
\le C\min\left(q,\frac n{|j|_n}\right).
\tag{5.5}
\]
Splitting the average at `|j|_n=n/q` gives
\[
\|f_z\|_1\le C(1+\log q).
\tag{5.6}
\]
Combining (5.4)--(5.6) and `L asymp log n` proves (5.2). `square`

Crucially, this **global** obstruction is asymptotically invisible to our quadratic target. Its effective support is at most `L`, so (4.7) gives on the high-probability event (4.3)
\[
\boxed{
\frac{|\langle r_D''(0),z\rangle|}{N(z)}
=O\left(\frac{(\log n)^2}{\sqrt n}\right)=o(1).
}
\tag{5.7}
\]
Thus the classical tone-reservation bad directions really exist inside the same random mask, but they are not aligned with the source-generated quadratic residual. The theorem we need must be **target-specific**, not a uniform extension theorem.

---

# 6. Exact remaining quadratic lemma

The quadratic bounded-interpolation norm has the dual form
\[
K_D^{(2)}
=
\sup_{\substack{z\ne0\\z\perp\mathbf1\\\operatorname{supp}z\subset D}}
\frac{|\langle r_D''(0),z\rangle|}{N(z)}.
\tag{6.1}
\]
Fix any sufficiently large finite `K_0`. Sections 3 and 4 already control, at `O(n^{-1/2})` or better failure, the union of

- all directions with `K_4(z)<=K_0`, and
- all directions with `s_eff(z)<=sqrt(n)/log n`.

Therefore `QBI` is reduced to the following genuinely narrower statement.

## Missing lemma `QACHL(K_0)` — quadratic adaptive collision-rich leakage

Prove that for some fixed finite `K_0,C<infinity`,
\[
\boxed{
\Pr_D\left\{
\sup_{\substack{z\perp\mathbf1,\ \operatorname{supp}z\subset D\\
s_{\rm eff}(z)>\sqrt n/\log n\\
\mathcal K_4(z)>K_0}}
\frac{|\langle r_D''(0),z\rangle|}{N(z)}>C
\right\}
=O(n^{-1/2}).
}
\tag{6.2}
\]
Theorem P07-B.23 plus (4.7) show that `QACHL(K_0)` implies
\[
\boxed{K_D^{(2)}=O(1)}
\tag{6.3}
\]
with `O(n^{-1/2})` failure, i.e. the exact `QBI` target from the preceding report.

To remove the source iterated-log loss one still also needs the analytic remainder estimate already isolated in the `1508` report:
\[
\sup_{0<\beta\le\beta_0}
\frac1{\beta^3}
\inf\left\{\|h\|_\infty:
T_Dh=r_D(\beta)-\frac{\beta^2}{2}r_D''(0)
\right\}
=O(1)
\tag{6.4}
\]
with `O(n^{-1/2})` failure. `QACHL + (6.4)` yields `TRBI`, then
\[
\boxed{\mathbb E\vartheta(G_n)=O(\sqrt n),}
\tag{6.5}
\]
removing the entire published `sqrt(log log n)` factor. The leading constant `1` remains a strictly stronger subsequent problem.

---

# 7. What changed and the next attack

The headline theta exponent did not change, but the proof obligation did:

1. the quadratic target energy is now **quenched and concentrated**, not merely annealed;
2. `K_D^{(2)}>=1/16-o(1)` holds with `O(1/n)` fixed-deviation failure, so the constant scale is rigorously samplewise sharp;
3. every bounded-additive-collision adaptive direction is solved uniformly at `O(1/n)` failure;
4. every low-effective-support direction is solved with arbitrarily high polynomial probability;
5. the random mask nevertheless contains the classical arithmetic-progression directions that destroy any global extension theorem, and those directions are proved to be asymptotically invisible to the actual quadratic target.

The next proof attack should therefore stay on `QACHL`, not return to global Kashin inequalities or source admission. The collision identity from the `1439` report is
\[
\mathcal K_4(z)
=\frac{n-1}{n}
\frac{\|\nu*\nu\|_2^2}{\|\nu\|_2^4}.
\tag{7.1}
\]
A high-`K_4`, high-effective-support witness has genuine additive structure. The next useful step is a dyadic weighted Balog--Szemeredi/Freiman-type reduction of such a `nu` to a low-complexity high-energy level set, followed by the exact leave-one-frequency decomposition
\[
W_a=W_a^{(-a)}+O(1),
\tag{7.2}
\]
from the `1439` report. The goal is to make the fixed-test second-chaos estimate uniform only over those structured level sets, not over an exponential net of arbitrary dense vectors. This preserves the same-mask dependence instead of pretending the Fourier coordinates are independent.

**Handoff to P07-A:** The new source-high-probability fact
\[
Q_D/n^2\to1/2
\quad\text{with fixed-deviation failure }O(1/n)
\]
may be used as a quantitative input if useful for its complementary-frequency dispersion calculations. P07-A retains ownership of primal positivity / hinge repair; P07-B retains ownership of adaptive Fourier interpolation and `QACHL`. No peer or historical file is modified here.
