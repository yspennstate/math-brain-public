Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED** — GPT-6 / maximum was requested as an owner preference, but this runtime exposes no authenticated completed-run effort telemetry or binding scheduler selector, so I do not claim otherwise.

# P07-B — damped Schur descent and a dependence-aware Fourier threshold-count law

**Native role:** `P07-B`, task `6aabe797a39081919acc889f29f4c556`  
**Repository / branch:** private `yspennstate/math-open-problems` / `master`  
**Captured start master:** `90765ce532a1e57a74d053836a1dc40b86745d91`  
**Fresh pre-write master:** `5a85790299e07c23d9b6a0d7620f700da6c4c295`  
**Previous own report:** `probability_campaigns/progress_first_2026-09-20/P07/fourier_dual/2026-09-20T0413+0300__active_set_schur_repair.md`  
**Newest complementary P07-A checkpoint read:** `probability_campaigns/progress_first_2026-09-20/P07/primal/2026-09-20T0445+0300__critical_householder_orthant.md`  
**Outside target:** Randomstrasse101, arXiv:2603.29571, Conjecture 18; primary partial-result paper arXiv:2502.16227.  
**Exact source endpoint:** for the dense random circulant source model on odd `n`,
\[
\mathbb E\,\vartheta(G_n)=(1+o(1))\sqrt n.
\]
**Inherited rigorous source bound:**
\[
\sqrt n\le \mathbb E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]
Thus the frozen full-source metric remains
\[
\boxed{\alpha_{LL}=1/2\to1/2.}
\]
Status: **OPEN / PROVED PARTIAL**. No improvement of the published exponent is claimed yet.

The mathematical progress this run is twofold.

1. The source Fourier field has an explicitly computable **bivariate dependence structure**. A fixed-level threshold set has asymptotic density `Q(2A)` and variance `O(n^{3/2})`, despite the Fourier coordinates being strongly dependent globally. In particular, at the sharp scale `A=1`, only about `2.275%` of the nonzero time coordinates are initial violations, with failure probability `O(n^{-1/2})` for any fixed larger density cutoff. Along prime orders this already makes the first Schur block invertible with `O(n^{-1/2})` failure, using full spark. This upgrades the previous report's easy `A=2` cardinality observation to the **critical constant scale**.
2. One-shot control of the maximum Schur leakage is not necessary. I prove a deterministic **damped Schur descent**: if each endogenous violation-set principal block has a fixed spectral margin `gamma>0`, then damping the exact interpolation by `gamma` contracts the total squared excess by the factor `1-gamma` at every step. After `O(log n)` steps this produces an explicit feasible Fourier-dual certificate at `O(n^{-1/2})` scale. This replaces the previous one-shot `ASL(0)` max-leakage target by an adaptive constant-conditioning target.

The second point is useful because the previous report showed that a single clipping correction can have coherent feedback, and a one-step cross vector should not be expected to have an `O(n^{-1/2})` maximum merely from its `L^2` energy. The new descent repairs newly created exceptional coordinates iteratively while keeping every correction in the exact feasible Fourier subspace.

---

## 1. Exact Fourier setup retained from the preceding reports

Let
\[
m=\frac{n-1}{2},\qquad \xi_a\in\{0,1\},\quad a=1,\dots,m,
\]
be independent fair source bits. Let `Q_a` be the rank-two real Fourier projector for the conjugate frequency pair `{a,-a}`. Put
\[
P_D=\sum_{a:\xi_a=1}Q_a,\qquad
P_C=\sum_{a:\xi_a=0}Q_a,\qquad
P_0=\frac1n\mathbf1\mathbf1^T,
\]
so
\[
P_0+P_D+P_C=I.
\]
Write
\[
x=P_De_0,
\qquad d=\operatorname{rank}(P_D),\qquad c=\operatorname{rank}(P_C).
\]
The exact completion parameter recovered earlier is
\[
\kappa_D=\inf_{q\in\operatorname{Ran}(P_C)}\max_j(x-q)_j,
\tag{1.1}
\]
and
\[
\vartheta(\overline{G_D})=1+n\kappa_D,
\qquad
\mathbb E\vartheta(G_D)=1+n\mathbb E\kappa_D,
\tag{1.2}
\]
because the fair source ensemble is invariant under complementing the frequency mask.

The previous report's exact active-set interpolation was the following. For a residual `r` and a threshold `tau`, if
\[
S=\{j:r(j)>\tau\},\qquad w=(r-\tau\mathbf1)|_S,
\]
and
\[
M_S=P_C[S,S]
\]
is invertible, then
\[
q^*=P_CE_SM_S^{-1}w\in\operatorname{Ran}(P_C),
\tag{1.3}
\]
with
\[
q^*|_S=w
\tag{1.4}
\]
and exact outside energy
\[
\boxed{
\|q^*_{S^c}\|_2^2
=w^T(M_S^{-1}-I)w.
}
\tag{1.5}
\]
Equation (1.5), rather than an independence fiction for Fourier coordinates, is the starting point below.

---

# 2. New deterministic theorem: damped Schur interpolation contracts total excess

The preceding report tried to control the **maximum** outside leakage of one exact interpolation. That is stronger than needed for an iterative certificate.

Fix any `tau>=0`. Suppose `r=x-q` for some already feasible accumulated correction
\[
q\in\operatorname{Ran}(P_C).
\]
Define the excess
\[
e=(r-\tau\mathbf1)_+,
\qquad
H=\|e\|_2^2,
\tag{2.1}
\]
and its strict violation set
\[
S=\{j:e(j)>0\}.
\tag{2.2}
\]
Then `w=e|_S` and `e` vanishes on `S^c`.

## Theorem P07-B.5 — damped Schur energy contraction

Assume `S` is nonempty and
\[
\lambda_{\min}(M_S)\ge\gamma
\qquad\text{for some }0<\gamma\le1.
\tag{2.3}
\]
Let `q^*` be the exact interpolant (1.3), and update the feasible correction by only the fraction `gamma`:
\[
q^+=q+\gamma q^*,
\qquad
r^+=x-q^+=r-\gamma q^*.
\tag{2.4}
\]
Then
\[
\boxed{
\|(r^+-\tau\mathbf1)_+\|_2^2
\le(1-\gamma)\,
\|(r-\tau\mathbf1)_+\|_2^2.
}
\tag{2.5}
\]

### Proof

On `S`, equation (1.4) gives `q^*=w=e`, hence
\[
(r^+-\tau\mathbf1)|_S
=(1-\gamma)e|_S.
\tag{2.6}
\]
Thus the squared positive excess remaining on `S` is exactly
\[
(1-\gamma)^2H.
\tag{2.7}
\]

On `S^c`, the old residual obeys `r-\tau\mathbf1<=0`, so any new positive excess can only come from a negative outside value of the correction:
\[
(r^+-\tau\mathbf1)_+|_{S^c}
\le\gamma(-q^*_{S^c})_+.
\tag{2.8}
\]
Therefore
\[
\|(r^+-\tau\mathbf1)_+|_{S^c}\|_2^2
\le\gamma^2\|q^*_{S^c}\|_2^2.
\tag{2.9}
\]
By the exact Schur identity (1.5) and (2.3),
\[
\|q^*_{S^c}\|_2^2
=w^T(M_S^{-1}-I)w
\le\left(\frac1\gamma-1\right)H.
\tag{2.10}
\]
The sets `S` and `S^c` are disjoint, so adding (2.7) and (2.9)-(2.10) gives
\[
H^+
\le
\left[(1-\gamma)^2
+\gamma^2\left(\frac1\gamma-1\right)\right]H
=(1-\gamma)H.
\]
This proves (2.5). ∎

### Why the damping `gamma` is canonical

More generally, if the interpolation is damped by `rho in [0,1]`, the same proof gives
\[
H^+\le
\left[(1-\rho)^2
+\rho^2\left(\frac1\gamma-1\right)\right]H.
\tag{2.11}
\]
The right side is minimized at
\[
\rho=\gamma,
\]
with minimum factor `1-gamma`. Thus the update in (2.4) is the optimal scalar damping available from only the spectral margin (2.3).

This is a genuine multiscale repair: the correction need not have a small `L^infinity` tail in one shot. Large newly created negative leakage simply appears in the next violation set and is repaired again.

---

# 3. Explicit dual certificate after `O(log n)` successful conditioning steps

Start with
\[
q_0=0,\qquad r_0=x.
\]
At step `k`, form
\[
e_k=(r_k-\tau\mathbf1)_+,
\quad S_k=\operatorname{supp}(e_k),
\quad M_k=P_C[S_k,S_k].
\tag{3.1}
\]
If `S_k` is empty, stop. Otherwise, when `lambda_min(M_k)>=gamma`, define
\[
q_k^*=P_CE_{S_k}M_k^{-1}(e_k|_{S_k}),
\tag{3.2}
\]
and set
\[
q_{k+1}=q_k+\gamma q_k^*,
\qquad
r_{k+1}=x-q_{k+1}.
\tag{3.3}
\]
Every `q_k` lies in `Ran(P_C)`, so every finite iterate is an exact feasible Fourier-dual correction for (1.1).

Iterating Theorem P07-B.5 gives
\[
\boxed{
\|e_K\|_2^2
\le(1-\gamma)^K\|e_0\|_2^2.
}
\tag{3.4}
\]
Since `tau>=0`,
\[
\|e_0\|_2\le\|x\|_2
=\sqrt{d/n}\le1.
\tag{3.5}
\]
Therefore
\[
\max_j r_K(j)
\le
\tau+(1-\gamma)^{K/2}.
\tag{3.6}
\]

Fix constants `A>0` and `eta>0` and put
\[
\tau=\frac A{\sqrt n}.
\tag{3.7}
\]
If
\[
K\ge
\frac{\log(n/\eta^2)}{-\log(1-\gamma)},
\tag{3.8}
\]
then
\[
(1-\gamma)^{K/2}\le\frac\eta{\sqrt n},
\]
and the accumulated explicit correction satisfies
\[
\boxed{
\kappa_D\le\frac{A+\eta}{\sqrt n}.
}
\tag{3.9}
\]

This is the key conceptual change from the one-shot `ASL(beta)` target: **constant principal-block conditioning along an adaptive chain is enough; one does not need an `O(n^{-1/2})` maximum bound for the first Schur leakage vector.**

---

# 4. Exact sufficient probabilistic lemma for log-loss removal, and for the sharp constant

The deterministic theorem isolates a new source-specific probabilistic bottleneck.

## Missing Adaptive Principal-Block Margin Lemma `APBM(A,gamma)`

For the actual random circulant source mask, run the endogenous iteration (3.1)-(3.3) at
\[
\tau=A/\sqrt n.
\]
Prove that for some fixed `gamma=gamma(A)>0`, with failure probability `p_n`, every nonempty principal block encountered before the iteration count (3.8) satisfies
\[
\boxed{
\lambda_{\min}\big(P_C[S_k,S_k]\big)\ge\gamma.
}
\tag{4.1}
\]
No independence between the sets `S_k` and the Fourier mask is assumed; they are generated by the same mask and previous corrections.

Then (3.9), `kappa_D<=1` on failure, and (1.2) give
\[
\mathbb E\vartheta(G_n)
\le
1+(A+\eta)\sqrt n+n p_n.
\tag{4.2}
\]
Consequently:

- if `p_n=O(n^{-1/2})` for any fixed finite `A,eta,gamma`, then
  \[
  \mathbb E\vartheta(G_n)=O(\sqrt n),
  \]
  which removes the published iterated-log loss;
- if for every fixed `epsilon>0` one can take
  \[
  A=1+\epsilon/2,\qquad \eta=\epsilon/2
  \]
  and prove
  \[
  p_n=o(n^{-1/2}),
  \tag{4.3}
  \]
  then
  \[
  \mathbb E\vartheta(G_n)
  \le(1+\epsilon)\sqrt n+o(\sqrt n).
  \]
  Combined with the known lower bound and then `epsilon downarrow 0`, this proves Conjecture 18.

Thus `APBM` is an exact theorem-sized target. It asks for a **constant spectral margin on only the `O(log n)` endogenous violation sets actually visited by the damped dual algorithm**, rather than a uniform RIP theorem over every set of the same cardinality and rather than independent Fourier-coordinate heuristics.

The rest of this report proves a first nontrivial part of that target: the *initial* violation set at the sharp constant scale is genuinely sparse in density, in a dependence-aware sense.

---

# 5. New dependence-aware small-ball theorem for the source Fourier field

For every nonzero time coordinate `j`, write
\[
\varepsilon_a=2\xi_a-1\in\{-1,+1\}.
\]
Since
\[
\sum_{a=1}^m\cos(2\pi aj/n)=-\frac12,
\]
we have the exact representation
\[
\boxed{
x(j)
=-\frac1{2n}
+\frac1n\sum_{a=1}^m
\varepsilon_a\cos(2\pi aj/n).
}
\tag{5.1}
\]
Define the centered normalized coordinate
\[
Y_j
:=\sqrt n\left(x(j)+\frac1{2n}\right)
=\frac1{\sqrt n}
\sum_{a=1}^m\varepsilon_a
\cos(2\pi aj/n).
\tag{5.2}
\]
The exact trigonometric orthogonality identities are
\[
\sum_{a=1}^m\cos^2(2\pi aj/n)=\frac{n-2}{4}
\qquad(j\ne0),
\tag{5.3}
\]
and, whenever `j,k` are nonzero and `k not congruent to +-j (mod n)`,
\[
\boxed{
\sum_{a=1}^m
\cos(2\pi aj/n)\cos(2\pi ak/n)
=-\frac12.
}
\tag{5.4}
\]
Hence
\[
\operatorname{Var}(Y_j)=\frac{n-2}{4n},
\tag{5.5}
\]
and for `k not congruent to +-j`,
\[
\boxed{
\operatorname{Cov}(Y_j,Y_k)=-\frac1{2n}.
}
\tag{5.6}
\]
In contrast, `Y_{-j}=Y_j` exactly. This is the dependence structure; the coordinates are **not independent**.

## Lemma P07-B.6 — uniform one- and two-coordinate Gaussian approximation

Fix a finite real `A`. Uniformly in nonzero `j`,
\[
\Pr\{x(j)>A/\sqrt n\}
=Q(2A)+O_A(n^{-1/2}),
\tag{5.7}
\]
where `Q=1-Phi` is the standard normal upper tail.

Uniformly in nonzero pairs `j,k` with `k not congruent to +-j`,
\[
\Pr\{x(j)>A/\sqrt n,\ x(k)>A/\sqrt n\}
=Q(2A)^2+O_A(n^{-1/2}).
\tag{5.8}
\]

### Proof

The univariate statement is the weighted-Rademacher Berry--Esseen estimate already used in the preceding report: the summands in (5.2) are bounded by `n^{-1/2}`, their total variance tends to `1/4` uniformly, and the sum of their third absolute moments is `O(n^{-1/2})`.

For (5.8), consider the independent two-dimensional summands
\[
Z_a=\frac{\varepsilon_a}{\sqrt n}
\left(
\cos(2\pi aj/n),
\cos(2\pi ak/n)
\right).
\tag{5.9}
\]
Their covariance matrix has diagonal `(n-2)/(4n)` and off-diagonal `-1/(2n)` by (5.3)-(5.4). Its eigenvalues are
\[
\frac14
\quad\text{and}\quad
\frac14-\frac1n,
\tag{5.10}
\]
so for all sufficiently large odd `n` it is uniformly nondegenerate. Moreover
\[
\sum_{a=1}^m\mathbb E\|Z_a\|_2^3
\le
\frac{2\sqrt2\,m}{n^{3/2}}
=O(n^{-1/2}).
\tag{5.11}
\]
The standard fixed-dimensional multivariate Berry--Esseen theorem for convex sets therefore gives an `O(n^{-1/2})` approximation, uniformly in `j,k`, to the centered Gaussian with this covariance. The upper-right quadrant is convex. Its covariance differs from `(1/4)I_2` by `O(1/n)`, and the deterministic `-1/(2n)` shift in (5.1) changes the normalized threshold by only `O(n^{-1/2})`. This yields (5.8). ∎

No step treats `Y_j,Y_k` as independent; the exact covariance (5.6), the exact equality `Y_{-j}=Y_j`, and a genuinely bivariate normal approximation are used.

---

# 6. Threshold-set law of large numbers with an explicit variance scale

For fixed `A>0`, let
\[
N_A
:=\#\left\{j\in\{1,\dots,n-1\}:
 x(j)>A/\sqrt n\right\}.
\tag{6.1}
\]
Put
\[
p_A=Q(2A).
\]

## Theorem P07-B.7 — source threshold-count concentration

For every fixed `A>0`,
\[
\boxed{
\mathbb E N_A=(n-1)p_A+O_A(\sqrt n),
}
\tag{6.2}
\]
and
\[
\boxed{
\operatorname{Var}(N_A)=O_A(n^{3/2}).
}
\tag{6.3}
\]
Consequently, for every fixed `delta>0`,
\[
\boxed{
\Pr\left\{
\left|\frac{N_A}{n-1}-p_A\right|>\delta
\right\}
=O_{A,\delta}(n^{-1/2}).
}
\tag{6.4}
\]

### Proof

Equation (6.2) follows immediately by summing (5.7) over the `n-1` nonzero coordinates.

For the variance, write `I_j=1_{x(j)>A/sqrt(n)}`. The diagonal contribution is `O(n)`. There are only `O(n)` ordered pairs with `k=-j`; for these `I_k=I_j` exactly, so their total covariance contribution is also `O(n)`. For every other ordered pair, (5.7)-(5.8) imply
\[
\operatorname{Cov}(I_j,I_k)=O_A(n^{-1/2}).
\]
There are `O(n^2)` such pairs, giving (6.3). Chebyshev then gives (6.4). ∎

Exactly the same argument applies to any fixed normalized band
\[
A<\sqrt n\,x(j)\le B,
\]
by expressing the two-coordinate band event as a finite linear combination of quadrant events. Thus, for fixed `A<B`, its empirical density converges at the same `O(n^{-1/2})` Chebyshev failure scale to
\[
\Phi(2B)-\Phi(2A).
\tag{6.5}
\]
This is the dependence-aware small-ball input needed for a future multiscale analysis: the number of coordinates in each **fixed normalized threshold band** is controlled without asserting independence of the Fourier field.

---

# 7. First `APBM` obligation solved at the critical scale: rank is not the issue

Take the sharp normalized threshold
\[
A=1,
\qquad
\tau=1/\sqrt n.
\]
Then
\[
p_1=Q(2)\approx0.0227501.
\tag{7.1}
\]
Let
\[
S_0=\{j:x(j)>1/\sqrt n\}.
\tag{7.2}
\]
The origin contributes at most one additional coordinate beyond `N_1`, so Theorem P07-B.7 implies, for example,
\[
\boxed{
\Pr\{|S_0|>n/8\}=O(n^{-1/2}).
}
\tag{7.3}
\]
(The constant `1/8` is deliberately very loose; any fixed number strictly above `Q(2)` works asymptotically.)

Independently of this estimate, the complementary Fourier rank is
\[
c=2\#\{a:\xi_a=0\},
\]
with `# {a:xi_a=0} ~ Bin(m,1/2)`. Hence a Chernoff bound gives
\[
\boxed{
\Pr\{c<n/4\}\le e^{-c_0 n}
}
\tag{7.4}
\]
for an absolute `c_0>0` and all sufficiently large odd `n`.

Combining (7.3)-(7.4),
\[
\boxed{
\Pr\{|S_0|\ge c\}=O(n^{-1/2}).
}
\tag{7.5}
\]
Thus, even at the source's sharp `A=1` scale, the initial exceptional set is not close to exhausting the available complementary Fourier dimension.

### Prime-order corollary

When `n` is prime, Chebotarev full spark for the complex Fourier matrix implies that every Fourier row/column minor of matching size is nonsingular. If `|S_0|<=c`, then the selected-row matrix `F_{C,S_0}` has full column rank, and
\[
M_{S_0}=\frac1nF_{C,S_0}^*F_{C,S_0}
\]
is positive definite. Therefore, along prime orders,
\[
\boxed{
\Pr\{M_{S_0}\text{ is singular}\}
=O(n^{-1/2}).
}
\tag{7.6}
\]

This is a strict improvement over the preceding P07-B report's easy `A=2` observation: the first exact Schur interpolation is now shown to be **well-defined at the critical constant scale `A=1` along prime orders**, with the expectation-relevant `O(n^{-1/2})` failure scale.

What (7.6) does **not** prove is a quantitative lower bound on `lambda_min(M_{S_0})`, and it does not cover composite odd orders. Those are genuine remaining obligations.

---

# 8. Relation to P07-A without duplicating its primal route

P07-A's newest report proves that the source constant `sqrt(n)` corresponds to an exact finite-`n` orthant point after a Householder change of coordinates, and that the source becomes row sampling from an explicit near-flat unitary. I do not duplicate that primal cone argument here.

The dual result above is complementary: at essentially the same constant scale, the **time-domain violation set feeding the Fourier completion algorithm has density**
\[
Q(2)\approx2.275\%,
\]
not density `1/2`. Thus the sharp constant is not obstructed by the raw number of dual exceptional coordinates. The obstacle is quantitative conditioning of an adaptive sequence of source-generated Fourier principal blocks.

Theorem P07-B.7 may also be useful to P07-A whenever its trimmed-simplex analysis needs an actual dependence-aware census of coordinates in a fixed Fourier threshold band. It should be reused there only with the exact normalization above; it does not make the row-sampled Fourier coordinates independent.

---

# 9. What failed, what changed, and the next attack

### Previous one-shot target

The preceding report formulated `ASL(0)`, asking directly for
\[
\mathbb E\|(-B_SM_S^{-1}w)_+\|_\infty=O(n^{-1/2})
\]
at a fixed source scale. That remains a sufficient statement, but it is unnecessarily strong. An `L^2`-small cross-leakage vector can still have a larger maximum, and a single stage need not absorb all exceptional coordinates.

### New route

Theorem P07-B.5 shows that the exact Schur energy identity already supplies a geometric contraction after the correct damping. The new missing theorem is therefore `APBM`: prove a constant spectral margin for the **actual adaptive violation sets**, for `O(log n)` stages, with source-valid failure probability.

### Strongest proved new source-specific inputs

1. `N_A/(n-1) -> Q(2A)` with variance `O(n^{3/2})`, proved by exact pair covariance plus bivariate Berry--Esseen, not independence.
2. At `A=1`, `|S_0|<c` with failure `O(n^{-1/2})`.
3. Along prime `n`, the first critical-scale Schur block is therefore invertible with failure `O(n^{-1/2})`.
4. Conditional on a fixed lower spectral margin at each stage, the damped certificate contracts squared excess by `1-gamma` and reaches `O(n^{-1/2})` maximum excess in `O(log n)` steps.

### Exact next mathematical attack

The next run should **not** repeat a maximum-leakage union bound. It should attack the first quantitative margin
\[
\lambda_{\min}\big(P_C[S_0,S_0]\big)
\tag{9.1}
\]
for
\[
S_0=\{x> A/\sqrt n\},\qquad A\in[1,2],
\]
using the newly proved small density of `S_0` together with source structure. Two concrete options are:

- a high-moment bound for the centered restricted involution
  \[
  P_C[S,S]-\tfrac12(I-P_0)[S,S],
  \]
  exploiting that threshold-set pair statistics are already controlled; or
- a leave-one-frequency / smoothed-threshold comparison that replaces the hard selector by a Lipschitz band and uses the exact `2/n` frame inequality from the preceding report to control the dependence error.

A proof of a constant first-step margin would be a real advance. The subsequent question is whether the same estimate is stable under the damped endogenous updates. If three substantive runs leave that margin unchanged, the mandated different attack should be a randomized reveal/multiscale frequency-block construction rather than another restatement of `APBM`.

---

# 10. Progress ledger

```yaml
ledger_delta:
  native_task_id: "6aabe797a39081919acc889f29f4c556"
  role: "P07-B Fourier dual / exceptional frequencies"
  target: "Randomstrasse101 Conjecture 18 / dense random circulant Lovasz theta"
  captured_start_master: "90765ce532a1e57a74d053836a1dc40b86745d91"
  fresh_prewrite_master: "5a85790299e07c23d9b6a0d7620f700da6c4c295"
  source_metric: "alpha_LL"
  metric_before: "1/2"
  metric_after: "1/2"
  inherited_bound: "sqrt(n) <= E theta(G_n) <= C sqrt(n log log n)"
  mathematical_status: "OPEN / PROVED PARTIAL"
  proved_this_run:
    - "damped exact Schur interpolation contracts squared threshold excess by factor 1-gamma whenever lambda_min(P_C[S,S])>=gamma"
    - "O(log n) successful conditioned steps give an explicit feasible dual correction with O(n^-1/2) maximum excess"
    - "exact APBM implication: O(n^-1/2) chain-failure removes loglog loss; o(n^-1/2) near A=1 would yield sharp leading constant"
    - "exact covariance of distinct non-antipodal normalized Fourier coordinates is -1/(2n), while antipodal coordinates are identical"
    - "uniform bivariate Berry-Esseen gives pair threshold probability Q(2A)^2+O(n^-1/2)"
    - "threshold count N_A has mean (n-1)Q(2A)+O(sqrt(n)) and variance O(n^(3/2))"
    - "at A=1 the initial violation set has size below complementary rank with O(n^-1/2) failure"
    - "for prime n, Chebotarev full spark therefore gives first critical-scale Schur-block invertibility with O(n^-1/2) failure"
  not_claimed:
    - "no quantitative constant lower bound on the first Schur eigenvalue yet"
    - "no composite-n invertibility theorem yet"
    - "no proof that adaptive later violation sets satisfy APBM"
    - "no improvement yet to alpha_LL=1/2"
  new_missing_lemma: "APBM(A,gamma): constant principal-block margin along O(log n) endogenous damped-Schur violation sets with expectation-relevant failure probability"
  next_attack: "prove a constant lower spectral margin for the first source-generated block at A in [1,2] using high moments or smoothed leave-one-frequency dependence control"
```
