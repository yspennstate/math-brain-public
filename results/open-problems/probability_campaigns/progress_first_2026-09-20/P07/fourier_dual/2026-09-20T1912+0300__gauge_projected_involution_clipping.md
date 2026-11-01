Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED** — GPT-6 / maximum reasoning was requested as an owner preference, but this runtime exposes no authenticated completed-run effort telemetry or binding scheduler selector, so I do not claim otherwise.

# P07-B — gauge-projected involution clipping and exponential first-tail compression

**Status:** **OPEN / PROVED PARTIAL** on Randomstrasse101 Conjecture 18.  
**Native role:** `P07-B`, task `6aabe797a39081919acc889f29f4c556`.  
**Repository / branch:** private `yspennstate/math-open-problems` / `master`.  
**Fresh pre-write master:** `d0c6f0d97222ce3bc3725768ee1527e8e51257d1`.  
**Previous own substantive checkpoint:** `probability_campaigns/progress_first_2026-09-20/P07/fourier_dual/2026-09-20T1830+0300__adaptive_quadratic_tilt_mean_QBI.md`.  
**Latest complementary P07-A checkpoint read:** `probability_campaigns/progress_first_2026-09-20/P07/primal/2026-09-20T1845+0300__orthogonal_core_mass_variance_bridge.md`. P07-A now owns the orthogonal-core mass / variance / influence route to the sharp constant. This report does not duplicate that argument; it stays on the Fourier-dual bounded-interpolation problem.

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
so the fixed full-source metric remains
\[
\boxed{\alpha_{LL}=1/2\to1/2.}
\]
No new arbitrary-`n` theta asymptotic is claimed here.

The exact Fourier LP, source normalization, and assignment-time repository attempts were already recovered in earlier P07-B runs and are not screened again. For continuity, the source-equivalent frequency LPs are
\[
\max n y_0
\quad\text{s.t.}\quad
 y_k=y_{n-k},\ \|y\|_1=1,\ y\ge0,\ \langle y,f_k\rangle=0
\ \text{on selected edge differences},
\]
and
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
The previous run proved an exact positive quadratic certificate showing that the single mean bound
\[
\boxed{\mathbb E[K_D^{(2)}\mathbf1_{\mathcal B_n}]=O(1)}
\tag{Mean-QBI}
\]
with
\[
\mathcal B_n=\{n/8\le |D|\le3n/8\}
\]
already implies
\[
\mathbb E\vartheta(G_n)=O(\sqrt n),
\]
thereby removing the published `sqrt(log log n)` loss. The purpose of this run is to replace `Mean-QBI` by a more structured same-mask multiscale statement and to prove the first nontrivial contraction step.

---

## 1. Full-group normalization and the quadratic target

Let
\[
M=\{1,\dots,(n-1)/2\},\qquad
\varepsilon_a=2\mathbf1_{\{a\in D\}}-1,
\]
extend the mask evenly to `Z_n` by
\[
Y(0)=0,\qquad Y(\pm a)=\varepsilon_a,
\]
and define the physical Fourier field
\[
G=G_D:=\frac{\widehat Y}{\sqrt n}.
\tag{1.1}
\]
Let `mu` denote uniform measure on all of `Z_n`, and put
\[
\langle u,v\rangle:=\mathbb E_\mu[uv],
\qquad
\|u\|_p:=\bigl(\mathbb E_\mu|u|^p\bigr)^{1/p}.
\]
For a transverse selected-frequency vector `z`,
\[
\operatorname{supp}z\subset D,\qquad \sum_{a\in D}z_a=0,
\]
write
\[
f_z(j)=\sum_{a\in D}z_a\cos(2\pi aj/n).
\tag{1.2}
\]
Then `f_z(0)=0`. Hence switching between the excluded-origin law `q_0` and `mu` multiplies both the numerator and denominator of every interpolation quotient by the same factor `n/(n-1)`.

The previous physical-space theorem therefore becomes
\[
\boxed{
K_D^{(2)}
=
\sup_{z\ne0,\ z\perp\mathbf1}
\frac{|\langle f_z,w\rangle|}{\|f_z\|_1},
\qquad
w:=\frac{G^2}{16}.
}
\tag{1.3}
\]
Equivalently, any bounded even `h` satisfying
\[
\langle f_z,h\rangle=\langle f_z,w\rangle
\qquad\text{for every transverse selected }f_z
\tag{1.4}
\]
is an exact interpolant for the quadratic target and proves
\[
K_D^{(2)}\le\|h\|_\infty.
\tag{1.5}
\]
This is the object to construct below.

---

# 2. New theorem: the dangerous radial/origin cycle is a free gauge

Use unnormalized cyclic convolution in time and define
\[
\boxed{
\mathcal K f:=\frac1{\sqrt n}G*f.
}
\tag{2.1}
\]
The inherited exact identities are
\[
\mathcal K f_z=f_z
\tag{2.2}
\]
for every selected test, and
\[
(G*G)(j)=
\begin{cases}
n-1,&j=0,\\
-1,&j\ne0.
\end{cases}
\tag{2.3}
\]
Thus `K` is self-adjoint on `L^2(mu)` and an `L^2` contraction; on the zero-mean subspace its Fourier multiplier is `Y` and has modulus one.

Let `delta_0` be the indicator of the origin and define
\[
\boxed{
\mathcal A_D:=\operatorname{span}\{\mathbf1,G,\delta_0\}.
}
\tag{2.4}
\]

## Theorem P07-B.28 — transverse annihilator and invariant gauge space

For every realized source mask and every transverse selected test `f_z`,
\[
\boxed{
f_z\perp\mathcal A_D.}
\tag{2.5}
\]
Moreover `A_D` is invariant under `K`:
\[
\boxed{
\mathcal K\mathbf1=0,\qquad
\mathcal K\delta_0=\frac1{\sqrt n}G,\qquad
\mathcal K G=\sqrt n\,\delta_0-\frac1{\sqrt n}\mathbf1.
}
\tag{2.6}
\]
Consequently, if `Q_D` denotes orthogonal projection onto `A_D^perp`, then for every `u`,
\[
\boxed{
\langle f_z,Q_D\mathcal K u\rangle
=
\langle f_z,u\rangle.
}
\tag{2.7}
\]

### Proof

The constant is annihilated because every nonzero character has zero full-group mean. Also `f_z(0)=sum z_a=0`, so `f_z perp delta_0`. The previous same-mask cancellation gives `E_{q_0}[f_zG]=0`; since `f_z(0)=0`, this is equivalent to `langle f_z,G rangle_mu=0`. This proves (2.5).

The first equality in (2.6) follows from `sum_j G(j)=0`, the second directly from convolution with `delta_0`, and the third from (2.3). Thus `A_D` is invariant. Finally, using self-adjointness, (2.2), and `Q_D f_z=f_z`,
\[
\langle f_z,Q_D\mathcal K u\rangle
=\langle Q_D f_z,\mathcal K u\rangle
=\langle\mathcal K f_z,u\rangle
=\langle f_z,u\rangle.
\]
QED.

### Why the projection matters

There is an explicit concentration cycle which a naive iterative proof would have to fight: `delta_0` is sent to `G`, while `G` is sent back to an origin spike plus a constant. But all three directions are invisible to the transverse interpolation target. Equation (2.7) says they can be projected away **for free at every scale**. This is a source-exact use of the dependence, not an independent-frequency approximation.

---

# 3. New deterministic certificate: gauge-projected multiscale clipping

For `b>0` write
\[
C_b(x)=\operatorname{sgn}(x)\min\{|x|,b\},
\qquad
R_b(x)=x-C_b(x).
\tag{3.1}
\]
Thus `||C_b(v)||_infty<=b` and `R_b(v)` is the discarded tail.

Fix a first absolute threshold `B>0`. Since `w=G^2/16>=0`, define
\[
h_0=\min\{w,B\},\qquad r_0=(w-B)_+,
\tag{3.2}
\]
and then
\[
\boxed{v_1=Q_D\mathcal K r_0.}
\tag{3.3}
\]
For `k>=1`, choose arbitrary positive thresholds `b_k`, and recursively set
\[
h_k=C_{b_k}(v_k),\qquad
r_k=R_{b_k}(v_k),\qquad
\boxed{v_{k+1}=Q_D\mathcal K r_k.}
\tag{3.4}
\]

## Theorem P07-B.29 — exact clipping-involution interpolation

For every `L>=1` and every transverse selected test,
\[
\boxed{
\langle f_z,w\rangle
=\left\langle f_z,\sum_{k=0}^{L-1}h_k\right\rangle
+\langle f_z,v_L\rangle.
}
\tag{3.5}
\]
Hence, if
\[
\sum_{k>=1}b_k<\infty,
\qquad
\|v_k\|_2\to0,
\tag{3.6}
\]
then
\[
h:=\sum_{k>=0}h_k
\tag{3.7}
\]
converges uniformly, is an exact bounded interpolant, and
\[
\boxed{
K_D^{(2)}\le B+\sum_{k>=1}b_k.
}
\tag{3.8}
\]

### Proof

Since `w=h_0+r_0`, Theorem P07-B.28 gives
\[
\langle f_z,w\rangle
=\langle f_z,h_0\rangle+\langle f_z,v_1\rangle.
\]
At every later step, `v_k=h_k+r_k` and (2.7) gives
\[
\langle f_z,v_k\rangle
=\langle f_z,h_k\rangle+\langle f_z,v_{k+1}\rangle.
\]
Telescoping proves (3.5). Under (3.6), the tail pairing tends to zero by Cauchy-Schwarz, while the bounded pieces converge uniformly because `sum b_k<infinity`. Equation (1.4) then holds for the limit. Restricting the resulting even function to the nonzero sites recovers the original `q_0` interpolation problem without changing any transverse moment. QED.

This is a constructive Fourier-dual certificate. It does not ask for a global Kashin theorem, which earlier P07-B work showed is false for random masks because logarithmic arithmetic-progressions support Dirichlet-type bad directions. Only the actual source-generated orbit in (3.3)--(3.4) must be controlled.

---

# 4. New probabilistic theorem: the first exceptional layer has exponentially small mean energy

The first layer can be controlled sharply from the **underlying independent mask bits** while retaining all dependence among Fourier coordinates.

For every nonzero time site `j`,
\[
G(j)=\sum_{a\in M}c_a(j)\varepsilon_a,
\qquad
c_a(j)=\frac2{\sqrt n}\cos(2\pi aj/n),
\tag{4.1}
\]
and folded cosine orthogonality gives exactly
\[
\boxed{
\sum_{a\in M}c_a(j)^2=\frac{n-2}{n}<1
\qquad(j\ne0).
}
\tag{4.2}
\]
Therefore Hoeffding's inequality for the independent source bits gives, for every fixed nonzero `j`,
\[
\boxed{
\Pr_D\{|G(j)|>t\}\le2e^{-t^2/2}.
}
\tag{4.3}
\]
No claim of independence between distinct values `G(j)` is made or needed.

## Theorem P07-B.30 — exponential first-tail compression

For the first residual (3.3),
\[
\boxed{
\mathbb E_D\|v_1\|_2^2\le\frac1{16}e^{-8B}.
}
\tag{4.4}
\]
In particular,
\[
\boxed{
\mathbb E_D\|v_1\|_2\le\frac14e^{-4B}.
}
\tag{4.5}
\]

### Proof

For `j ne 0`, set `X=G(j)^2` and `a=16B`. From (4.3),
\[
\Pr\{X>s\}\le2e^{-s/2}.
\]
The layer-cake identity gives
\[
\begin{aligned}
\mathbb E(X-a)_+^2
&=\int_a^\infty2(s-a)\Pr\{X>s\}\,ds\\
&\le4e^{-a/2}\int_0^\infty u e^{-u/2}\,du\\
&=16e^{-a/2}.
\end{aligned}
\]
Since `r_0=(G^2-16B)_+/16`,
\[
\mathbb E_D r_0(j)^2\le\frac1{16}e^{-8B}
\qquad(j\ne0).
\tag{4.6}
\]
The origin requires no tail estimate at all. Writing `r_0^*=r_0-r_0(0)delta_0`, equation (2.6) gives
\[
Q_D\mathcal K(r_0-r_0^*)=0,
\]
so `v_1=Q_D K r_0^*`. Both `Q_D` and `K` are `L^2` contractions, hence
\[
\|v_1\|_2^2\le\|r_0^*\|_2^2
=\frac1n\sum_{j\ne0}r_0(j)^2.
\]
Average over the mask and use (4.6). This proves (4.4); Jensen gives (4.5). QED.

### Interpretation

A single bounded correction of cost `B` converts the exact quadratic target into a same-mask residual whose mean square energy is exponentially small in `B`. The remaining obstruction is therefore not the first set of large physical Fourier values. It is whether the same-mask involution can repeatedly **re-spread** the clipped tail after the free radial/origin cycle has been removed.

---

# 5. Exact new missing lemma: an orbit-specific fourth-moment contraction

Set
\[
\sigma_k:=\|v_k\|_2,
\]
and, for `sigma_k>0`,
\[
\kappa_k:=\frac{\|v_k\|_4^4}{\sigma_k^4}.
\tag{5.1}
\]
For a fixed `A>0`, use the adaptive thresholds
\[
\boxed{b_k=A\sigma_k\qquad(k>=1).}
\tag{5.2}
\]
Deterministically,
\[
\begin{aligned}
\sigma_{k+1}^2
&\le\|R_{A\sigma_k}(v_k)\|_2^2\\
&\le\mathbb E_\mu\left[v_k^2\mathbf1_{\{|v_k|>A\sigma_k\}}\right]\\
&\le\frac{\|v_k\|_4^4}{A^2\sigma_k^2}
=\frac{\kappa_k}{A^2}\sigma_k^2.
\end{aligned}
\tag{5.3}
\]
This suggests a weighted statement on the **actual endogenous orbit**, not a uniform fourth-moment theorem over all vectors.

## Missing lemma `GQOK4` — gauge-quotient orbit kurtosis

Prove that there exist absolute constants `A<infinity` and `C_4<A^2` such that the recursion (3.3)--(3.4), (5.2) satisfies, for every `k>=1`,
\[
\boxed{
\mathbb E_D\!\left[
\kappa_k\sigma_k^2\,\mathbf1_{\mathcal B_n}
\right]
\le
C_4\,
\mathbb E_D\!\left[
\sigma_k^2\,\mathbf1_{\mathcal B_n}
\right].
}
\tag{GQOK4}
\]
Here `v_k`, `K`, `Q_D`, and the mask are all generated from the **same** `D`. No conditional independence between them is asserted.

Let
\[
\rho:=\sqrt{C_4}/A<1.
\]
Then (5.3) and `GQOK4` give
\[
\mathbb E[\sigma_{k+1}^2;\mathcal B_n]
\le\rho^2\mathbb E[\sigma_k^2;\mathcal B_n].
\tag{5.4}
\]
By Cauchy-Schwarz,
\[
\mathbb E[\sigma_k;\mathcal B_n]
\le\rho^{k-1}
\bigl(\mathbb E\sigma_1^2\bigr)^{1/2}.
\tag{5.5}
\]
Consequently Theorem P07-B.29 and (4.4) yield the explicit mean bound
\[
\boxed{
\mathbb E[K_D^{(2)};\mathcal B_n]
\le
B+rac{A}{4(1-\rho)}e^{-4B}.
}
\tag{5.6}
\]
Thus `GQOK4` proves `Mean-QBI`, and the exact adaptive positive quadratic certificate from the preceding run then proves
\[
\boxed{\mathbb E\vartheta(G_n)=O(\sqrt n).}
\tag{5.7}
\]
This would remove the complete published `sqrt(log log n)` loss.

A slightly weaker, equally sufficient formulation is the direct orbit-sum statement
\[
\boxed{
\mathbb E_D\left[
\mathbf1_{\mathcal B_n}\sum_{k>=1}\sigma_k
\right]=O(1).
}
\tag{GQOS}
\]
Indeed (3.8) with `b_k=A sigma_k` immediately gives `Mean-QBI`. `GQOK4` is singled out because (5.3) turns it into a concrete dependence-aware small-ball/fourth-moment problem.

Neither `GQOK4` nor `GQOS` is proved in this report. They are strictly orbit-specific; demanding the analogous estimate uniformly for every selected-frequency vector would return to the false global Kashin route already ruled out by the logarithmic-interval counterexamples.

---

# 6. What changed, what did not, and next attack

### PROVED PARTIAL this run

1. The three-dimensional space
   \[
   \operatorname{span}\{1,G_D,\delta_0\}
   \]
   is an exact annihilator of all transverse selected tests and is invariant under the same-mask convolution operator. The explicit `delta_0 <-> G_D` concentration cycle can therefore be removed at no interpolation cost.
2. Gauge-projected multiscale clipping gives an exact constructive bounded dual certificate whenever its adaptive tail energies are summable:
   \[
   K_D^{(2)}\le B+\sum_{k>=1}b_k.
   \]
3. The first clipped exceptional layer satisfies the source-valid bound
   \[
   \mathbb E\|v_1\|_2^2\le16^{-1}e^{-8B},
   \]
   using only independence of the underlying Bernoulli mask bits. No dependent physical Fourier coordinates were treated as independent.
4. `Mean-QBI` is reduced further to the same-mask orbit statement `GQOK4` (or the weaker direct `GQOS`).

### Still open

- `GQOK4` / `GQOS` is not proved.
- Therefore the arbitrary-`n` improvement `E theta=O(sqrt n)` is still conditional, not an established new source bound.
- The sharp leading constant `1` in Conjecture 18 remains open on this route. P07-A's new orthogonal-core variance criterion is a complementary sharp-constant route and is not duplicated here.
- A finite LP experiment would remain evidence only and is not used as an asymptotic theorem.

### Failed / avoided attack

A uniform restricted-norm or global Kashin theorem would make the recursion easy, but previous P07-B work already produced source masks with logarithmic selected intervals carrying Dirichlet-type high-collision witnesses. Reintroducing that uniform theorem would ignore a certified obstruction. The present quotient projection and orbit-specific expectation are designed precisely to avoid it.

### Next concrete proof attack

Prove `GQOK4` first for `k=1` and then inductively for the gauge-projected orbit. The first target is the source-valid inequality
\[
\mathbb E\bigl[\|v_1\|_4^4;\mathcal B_n\bigr]
\le C\,\mathbb E\bigl[\|v_1\|_2^4;\mathcal B_n\bigr]
\tag{6.1}
\]
with an absolute `C`, where
\[
v_1=Q_D\mathcal K_D(G_D^2/16-B)_+.
\]
The proof should expose one mask bit at a time or use a leave-one-frequency decomposition of the **same** mask, keeping the projection `Q_D` in place so that the exact radial/origin two-cycle is absent. If (6.1) survives one clipping step with an energy-weighted constant, iterate it through (5.3) rather than union-bounding all Fourier coordinates. This is now the narrowest identified Fourier-dual bottleneck for removing the iterated-log loss.

---

## P07-A handoff

P07-A need not reproduce any clipping argument. The useful shared fact is: P07-B now has an exact bounded-certificate recursion in which the explicit origin/radial concentration cycle is quotiented out for free, and an orbit-sum estimate implies `E theta=O(sqrt n)`. Conversely, this report does not use or claim P07-A's orthogonal-core variance criterion, positive-basis structure, or influence bounds.

Former R7-02 admission/CLOSABLE history and all peer/canonical ownership remain untouched.