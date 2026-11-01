Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED** — GPT-6 / maximum was requested as an owner preference, but this runtime does not provide authenticated completed-run effort telemetry, so I do not claim otherwise.

# P07-A — exact orthant cone has Haar threshold constant 1

**Native role:** `P07-A`, task `6aa7b46f70a8819184095c277974c256`  
**Repository / branch:** private `yspennstate/math-open-problems` / `master`  
**Captured pre-research master:** `b46fbcb68200e07fbad3932bde31d93f8697d121`  
**Outside target:** Randomstrasse101, arXiv:2603.29571, Conjecture 18; primary partial-result paper Bandeira–Błasiok–Dmitriev–Faure–Kireeva–Kunisky, *The Lovász number of random circulant graphs*, arXiv:2502.16227.  
**Exact endpoint:** for the source dense random circulant model on odd `n`, prove

\[
\mathbb E\,\vartheta(G_n)=(1+o(1))\sqrt n.
\]

**Inherited rigorous bound:**

\[
\sqrt n\le \mathbb E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]

The full-source loss metric `alpha_LL=1/2` therefore remains `1/2 -> 1/2`. This run nevertheless makes substantive structural progress: it identifies the **exact primal cone** whose half-dimensional Haar phase transition occurs at the conjectured constant `1`, proves the phase transition analytically, and shows that the previous `ell_2` one-sided surrogate is too strong even for Haar subspaces. The remaining source gap becomes a single cone-specific partial-Fourier-versus-Haar comparison at tail probability `o(n^{-1/2})`.

The prior P07-A report `2026-09-20T0246+0300__orthant_margin_positive_circuits.md` and the complementary P07-B report `2026-09-20T0328+0300__zero_diagonal_exceptional_certificate.md` were read first. I inherit, rather than re-prove, the exact identity `theta=1+R_E`, the prime positive-circuit parametrization, and P07-B's exact bridge `R_C=n kappa_D=1/delta_D`. I do not duplicate P07-B's exceptional-frequency dual construction.

The assignment-time source/current check was already done once in the preceding P07 reports. No source-status claim is upgraded here.

---

## 1. Source parity and exact ratio cone

Let `n` be odd. The source chooses independently, with probability `1/2`, each unordered nonzero frequency pair

\[
\{d,-d\},\qquad 1\le d\le (n-1)/2,
\]

and includes both members of a chosen pair in the symmetric edge-difference set `E`. With the **unnormalized** DFT `F`, define

\[
L_E:=\{z\in\mathbb R^n:\mathbf 1^Tz=0,\ (Fz)_d=0\ \forall d\in E\}.
\]

If `s` conjugate pairs are selected, then `|E|=2s` and

\[
\dim L_E=n-1-2s.
\]

Thus in the dense source model `dim(L_E)/(n-1) -> 1/2` in probability. The exact primal identity from the previous P07-A run is

\[
\vartheta(G_E)=1+R_E,
\qquad
R_E:=\sup_{0\ne z\in L_E}
\frac{\|z_+\|_\infty}{\|z_-\|_\infty}.
\tag{1.1}
\]

For `r>0` define, inside the zero-sum hyperplane `H_n=1^perp`, the fixed-coordinate polyhedral cone

\[
K_n(r):=
\left\{
 z\in H_n:\ z_0\ge r\max_{1\le j\le n-1}(-z_j)_+
\right\}.
\tag{1.2}
\]

Because `L_E` is invariant under cyclic coordinate shifts, we have the exact equivalence

\[
\boxed{
R_E\ge r
\iff
L_E\cap K_n(r)\ne\{0\}.
}
\tag{1.3}
\]

### Proof

If `R_E>=r`, choose `z in L_E` whose ratio is at least `r` and cyclically shift a coordinate attaining `||z_+||_infty` to coordinate `0`. The shift stays in `L_E`, and then `z_0>=r||z_-||_infty`, so `z in K_n(r)`. Conversely any nonzero `z in L_E cap K_n(r)` has

\[
\frac{\|z_+\|_\infty}{\|z_-\|_\infty}
\ge
\frac{z_0}{\|z_-\|_\infty}
\ge r.
\]

This cone, not the `ell_2` surrogate from the preceding report, is the exact source geometry.

---

# 2. New theorem: exact statistical dimension of the sharp-scale cone

Let `phi` and `Phi` denote the standard normal density and CDF, and `Q(h)=1-Phi(h)`. Define

\[
A(h):=\mathbb E(G-h)_+
=\phi(h)-hQ(h),
\tag{2.1}
\]

\[
B(h):=\mathbb E(h-G)_+
=\phi(h)+h\Phi(h),
\tag{2.2}
\]

for `G~N(0,1)`. Note the exact identity

\[
B(h)-A(h)=h.
\tag{2.3}
\]

For every `c>0`, let `h_c` be the unique real solution of

\[
\boxed{
\frac{B(h_c)}{A(h_c)}=c^2.
}
\tag{2.4}
\]

Uniqueness is immediate because

\[
\frac{B(h)}{A(h)}=1+\frac{h}{A(h)},
\qquad
\frac{d}{dh}\frac{B(h)}{A(h)}
=\frac{\phi(h)}{A(h)^2}>0,
\tag{2.5}
\]

and the ratio runs from `0` to `+infinity`. In particular,

\[
h_1=0.
\tag{2.6}
\]

### Theorem P07-A.4 — sharp-cone statistical dimension

For fixed `c>0` and

\[
r_n=c\sqrt n,
\]

let `delta` denote statistical dimension in the ambient Euclidean structure of `H_n`. Then

\[
\boxed{
\frac{\delta(K_n(c\sqrt n))}{n}
\longrightarrow
Q(h_c).
}
\tag{2.7}
\]

In particular,

\[
\boxed{
\frac{\delta(K_n(\sqrt n))}{n}\to\frac12.
}
\tag{2.8}
\]

So the constant `1` in the source conjecture is exactly the half-dimensional Haar conic threshold for the **same one-sided ratio cone** appearing in (1.3).

## Proof

Let `g=(g_0,...,g_{n-1})` have iid standard normal coordinates. Since `K_n(r) subset H_n`, minimizing distance from `g` to the cone is equivalent to minimizing distance from the standard Gaussian `P_{H_n}g` in `H_n`; the discarded constant component contributes an additive distance independent of the cone point. Hence

\[
\delta(K_n(r))
=\mathbb E\|\Pi_{K_n(r)}g\|_2^2.
\tag{2.9}
\]

Write a candidate cone point as

\[
z_0=r a,\qquad a\ge0.
\]

The cone inequalities are

\[
z_j\ge-a\quad(j\ne0),
\]

and the zero-sum constraint is

\[
\sum_{j=1}^{n-1}z_j=-ra.
\tag{2.10}
\]

For fixed `a`, Euclidean projection of `(g_1,...,g_{n-1})` onto this lower-truncated affine hyperplane has the water-filling form

\[
 z_j=(g_j-h)_+-a
\tag{2.11}
\]

for a scalar threshold `h`, with the exact mass equation

\[
\sum_{j=1}^{n-1}(g_j-h)_+
=a(n-1-r).
\tag{2.12}
\]

This is just the KKT formula `z_j=max(g_j-lambda,-a)` after writing `h=lambda-a`.

At an interior optimum in `a`, the multiplier on an active floor coordinate is `(h-g_j)_+`; stationarity in the distinguished coordinate gives

\[
ra-g_0+h+a
-\frac1r\sum_{j=1}^{n-1}(h-g_j)_+
=0.
\tag{2.13}
\]

For `r=c sqrt(n)`, divide (2.12) by `n` and (2.13) by `sqrt(n)`. The empirical laws of the iid `g_j`, together with convexity/uniqueness of the projection, force every subsequential limit `(a,h)` to satisfy

\[
a=A(h),
\qquad
B(h)=c^2a.
\tag{2.14}
\]

Thus `h=h_c` uniquely and `a=A(h_c)`. (The terms `g_0/sqrt(n)`, `h/sqrt(n)`, `a/sqrt(n)` vanish; `r/(n-1)->0`. Standard Gaussian uniform integrability upgrades the empirical convergence needed here from compact threshold ranges to the minimizing sequence. The normalized convex objective is coercive, so the minimizing thresholds cannot escape to infinity.)

Now compute the projected norm. From (2.11),

\[
\frac1n\|\Pi_{K_n(r)}g\|_2^2
=
\frac{r^2a^2}{n}
+
\frac1n\sum_{j=1}^{n-1}
\big((g_j-h)_+-a\big)^2.
\tag{2.15}
\]

Passing to the limit gives

\[
c^2A(h)^2
+\mathbb E(G-h)_+^2
-2A(h)^2+A(h)^2.
\tag{2.16}
\]

Since `B=c^2A` and `B-A=h`, this is

\[
\mathbb E(G-h)_+^2+hA(h).
\tag{2.17}
\]

The Gaussian identities

\[
\mathbb E(G-h)_+^2
=(1+h^2)Q(h)-h\phi(h),
\]

\[
hA(h)=h\phi(h)-h^2Q(h)
\]

reduce (2.17) exactly to

\[
Q(h).
\tag{2.18}
\]

Finally `||Pi_K g||<=||g||` gives uniform integrability of the normalized squared norms, so convergence in probability of (2.15) implies convergence of expectations. This proves (2.7). Equation (2.8) follows from `h_1=0`. ∎

**Status:** `PROVED PARTIAL`. This theorem is about the Haar benchmark geometry of the exact source cone; it is not yet a theorem for the structured random Fourier kernel.

---

# 3. Corollary: the Haar analogue has the exact conjectured constant

Let `V_{n,d}` be a Haar-uniform `d`-dimensional subspace of `H_n`, with

\[
\frac d{n-1}\to\frac12.
\]

For a subspace `V` define

\[
R(V):=\sup_{0\ne z\in V}
\frac{\|z_+\|_\infty}{\|z_-\|_\infty}.
\]

The approximate conic kinematic theorem of Amelunxen--Lotz--McCoy--Tropp applies to a fixed coordinate cone. By (2.7):

- if `c>1`, then `h_c>0`, hence `Q(h_c)<1/2`, so `V_{n,d}` misses `K_n(c sqrt(n))` with exponentially high probability;
- if `c<1`, then `h_c<0`, hence `Q(h_c)>1/2`, so `V_{n,d}` meets a fixed coordinate cone with probability tending to one.

For the upper tail of `R(V)`, union bound over the `n` congruent coordinate cones. The kinematic gap is linear in `n` for fixed `c>1`, so the extra factor `n` is negligible. Therefore

\[
\boxed{
\frac{R(V_{n,d})}{\sqrt n}\to1
\quad\text{in probability}.
}
\tag{3.1}
\]

There is also a deterministic bound

\[
R(V)\le n-1,
\tag{3.2}
\]

because for every zero-sum vector, if `M=max z_i` and `m=max(-z_i)`, then total negative mass is at most `(n-1)m` and at least `M`. The exponentially small Haar upper tail therefore upgrades (3.1) to

\[
\boxed{
\mathbb E R(V_{n,d})=(1+o(1))\sqrt n.
}
\tag{3.3}
\]

This is the exact Haar counterpart of Randomstrasse101 Conjecture 18.

The standard external ingredient used here is the conic kinematic/statistical-dimension theory of Amelunxen, Lotz, McCoy and Tropp, *Living on the edge* (arXiv:1303.6672; Information and Inference 3 (2014), 224--294). The cone-specific statistical-dimension calculation (2.7) is proved above.

---

# 4. Important correction: the previous `beta` surrogate cannot retain constant 1

The preceding P07-A report introduced the sufficient modulus

\[
\beta(E)=\inf_{0\ne z\in L_E}
\frac{\|z_-\|_2}{\|z_+\|_\infty}
\]

and observed that `E beta(E)^(-1)=1+o(1)` would prove the source conjecture. That remains algebraically true, but the present calculation shows that this target is **too strong as a probabilistic geometry principle**.

Indeed consider the surrogate cone

\[
D_n(t):=\{z\in H_n:\|z_-\|_2\le t z_0\}.
\]

The same projection/KKT calculation gives, for fixed `t`, an asymptotic statistical-dimension fraction

\[
\Psi_t
=
M_+(\lambda)
+\gamma M_-(\lambda),
\qquad
\gamma=\frac{t^2}{1+t^2},
\tag{4.1}
\]

where

\[
A(\lambda)=\gamma B(\lambda),
\]

and `M_+`, `M_-` are the two truncated second moments of `G-lambda`. At `t=1`, `gamma=1/2`, so

\[
\Psi_1
=\frac12(M_++M_-)+\frac12M_+
=\frac12(1+\lambda^2)+\frac12M_+
>\frac12.
\tag{4.2}
\]

Therefore even a Haar half-dimensional subspace intersects `D_n(1)` with high probability. In particular, a Haar comparison cannot prove `beta>=1-o(1)`; the `ell_2` relaxation has already lost the sharp constant before any Fourier-specific difficulty appears.

This is useful negative progress: **the exact `ell_infinity` floor in (1.2) is essential.** The new route should compare the source kernel to Haar only for `K_n(c sqrt(n))`, not for the stronger `ell_2` surrogate.

---

# 5. Exact source-level reduction to one cone-tail estimate

Return to the actual random Fourier kernel `L_E`. From (1.1)--(1.3), for every fixed `epsilon>0`,

\[
\Pr\{\vartheta(G_E)>1+(1+\epsilon)\sqrt n\}
=
\Pr\{L_E\cap K_n((1+\epsilon)\sqrt n)\ne\{0\}\}.
\tag{5.1}
\]

Since always `R_E<=n-1`, the single tail estimate

\[
\boxed{
\Pr\{L_E\cap K_n((1+\epsilon)\sqrt n)\ne\{0\}\}
=o(n^{-1/2})
\quad\text{for every fixed }\epsilon>0
}
\tag{5.2}
\]

is enough for the sharp **expectation** upper bound. Indeed

\[
\mathbb E R_E
\le
(1+\epsilon)\sqrt n
+(n-1)\Pr\{R_E>(1+\epsilon)\sqrt n\},
\tag{5.3}
\]

so (5.2) implies

\[
\limsup_n\frac{\mathbb E R_E}{\sqrt n}\le1+\epsilon.
\]

Let `epsilon downarrow0`, then combine with the inherited source lower bound.

This is strictly more focused than an all-sign RIP theorem. We do **not** need a uniform isometry on every sparse vector, nor a worldwide universality theorem for all cones. We need a one-sided escape estimate for the single explicit polyhedral family `K_n(c sqrt(n))`, at a tail smaller than `n^{-1/2}`.

The source's random dimension causes no constant-level problem. Conditional on selecting `s` conjugate frequency pairs,

\[
\dim L_E=n-1-2s,
\]

and `s` is binomial with mean `(n-1)/4`. For fixed `epsilon>0`, the Haar statistical-dimension gap at `c=1+epsilon` is linear in `n`, whereas the source dimension fluctuates only on the `sqrt(n)` scale. Thus a successful cone-specific comparison can first condition on the overwhelmingly likely central range of `s`.

---

# 6. Exact handoff to P07-B without duplicating its route

P07-B proved for complementary source masks `D,C`

\[
R_C=n\kappa_D=\frac1{\delta_D}.
\]

Combining that identity with (1.3) gives the exact three-way event equivalence

\[
\boxed{
L_C\cap K_n(r)\ne\{0\}
\iff
R_C\ge r
\iff
\kappa_D\ge\frac r n
\iff
\delta_D\le\frac1r.
}
\tag{6.1}
\]

Thus the new Haar benchmark says that, at a formal half-dimensional isotropic benchmark, the dual completion threshold `kappa ~ n^{-1/2}` and moment-depth threshold `delta ~ n^{-1/2}` have leading constant `1` for exactly the same geometric reason. P07-B can use (6.1) as a target calibration; all exceptional-frequency certificate construction remains its responsibility.

---

# 7. Literature comparison relevant to the next step

Two external frameworks are nearby but do not presently close the source gap:

1. ALMT's conic kinematic theorem gives the Haar result once the statistical dimension is known; it does not apply directly to a random coordinate subspace of the deterministic Fourier basis.
2. Oymak--Tropp, *Universality laws for randomized dimension reduction, with applications* (arXiv:1511.09433), proves broad universality for random maps with independent standardized entries. The source measurement operator here is instead **Bernoulli row selection from a fixed real Fourier basis with conjugate-pair coupling**. That dependence is exactly what must be handled; I do not claim their theorem applies off the shelf.

A useful future theorem would therefore be much narrower than general partial-Fourier RIP: a Lindeberg/invariance or restricted-minimum-singular-value comparison specifically for `K_n((1+epsilon)sqrt(n)) cap S(H_n)` under random conjugate-pair Fourier row selection.

---

# 8. What changed, remaining gap, next attack

### Proved this run

1. Exact source event reformulation `R_E>=r iff L_E cap K_n(r) != {0}` for the sharp polyhedral ratio cone.
2. Exact asymptotic statistical dimension
   `delta(K_n(c sqrt(n)))/n -> Q(h_c)`, with `B(h_c)/A(h_c)=c^2`.
3. The half-dimensional Haar transition occurs **exactly at `c=1`**.
4. The Haar analogue satisfies `E R=(1+o(1))sqrt(n)`.
5. The previous `ell_2` surrogate is provably supercritical at `t=1` under Haar and therefore cannot preserve the sharp constant through a Haar comparison.
6. The source conjecture's upper bound reduces to the single cone-tail estimate (5.2), only `o(n^{-1/2})` rather than an exponential bound.
7. Exact cross-track event calibration (6.1).

### Not proved

- No source-level improvement of `alpha_LL=1/2` yet.
- No claim that the structured random Fourier kernel is Haar-like globally.
- No claim that Oymak--Tropp universality applies to the source row-selection model.
- No replacement of expectation by high-probability without the explicit tail integration in (5.3).
- No finite-`n` numerical theta value is treated as asymptotic progress.

### Remaining gap

Prove, for every fixed `epsilon>0`, the source-specific one-cone escape estimate

\[
\Pr\{L_E\cap K_n((1+\epsilon)\sqrt n)\ne\{0\}\}=o(n^{-1/2}).
\]

### Next primal/structural attack

1. Write the restricted minimum singular value
   `inf_{z in K_n((1+eps)sqrt(n)) cap S(H_n)} ||P_E F z||_2`
   as a source-exact min-max with conjugate-pair Bernoulli sampling, then test an invariance replacement **for this cone only** rather than for all sparse vectors.
2. Exploit the polyhedral description `z_j>=-z_0/r`: condition on an active floor set and seek a union bound whose entropy is paid by the positive cone geometry, not by signed RIP covering numbers.
3. On prime orders, combine the cone threshold with the positive-circuit parametrization from the preceding report: a violating positive circuit has barycentric weight `y_0>(1+eps)/sqrt(p)`. Seek an anti-concentration bound conditional on cofactor positivity. This remains P07-A; exceptional-frequency dual clipping remains P07-B.

External novelty of the cone formula/statistical-dimension calculation is **UNVERIFIED** and requires later independent review.

---

## 9. Progress ledger

```yaml
ledger_delta:
  native_task_id: "6aa7b46f70a8819184095c277974c256"
  role: "P07-A primal/structural"
  target: "Randomstrasse101 Conjecture 18 / dense random-circulant Lovasz theta"
  source_claim_owner: "existing RS-2025-TH18 claim preserved; complementary role only"
  captured_master: "b46fbcb68200e07fbad3932bde31d93f8697d121"
  source_metric: "alpha_LL"
  metric_before: "1/2"
  metric_after: "1/2"
  source_status: "OPEN / PROVED PARTIAL"
  inherited_bound: "sqrt(n) <= E theta(G_n) <= C sqrt(n log log n)"
  proved_this_run:
    - "exact sharp ratio-cone intersection formulation"
    - "statistical dimension delta(K_n(c sqrt n))/n -> Q(h_c)"
    - "half-dimensional Haar threshold constant exactly 1"
    - "Haar analogue E R=(1+o(1)) sqrt(n)"
    - "ell_2 beta surrogate shown too strong for sharp Haar comparison"
    - "source upper bound reduced to o(n^-1/2) one-cone intersection tail"
    - "exact primal/dual event calibration for P07-B"
  remaining_gap: "cone-specific random partial-Fourier versus Haar escape comparison"
  next_attack: "source-exact min-max invariance for K_n((1+eps)sqrt n), then active-floor-set entropy and prime positive-circuit anti-concentration"
  predecessor_handoff: "SRG69 remains archived OPEN/PARTIAL and untouched"
```
