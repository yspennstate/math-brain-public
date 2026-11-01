Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED** — GPT-6 / maximum was requested as an owner preference, but this runtime does not provide authenticated completed-run effort telemetry, so I do not claim otherwise.

# P07-A — the conjectured constant is an exact finite-n orthant point

**Native role:** `P07-A`, task `6aa7b46f70a8819184095c277974c256`  
**Repository / branch:** private `yspennstate/math-open-problems` / `master`  
**Captured pre-write master:** `dfc130cb94764f53a1afa8b1af8983f2673259dd`  
**Outside target:** Randomstrasse101, arXiv:2603.29571, Conjecture 18; primary partial-result paper *The Lovász number of random circulant graphs*, arXiv:2502.16227.  
**Exact endpoint:** in the source dense random circulant model,
\[
\mathbb E\,\vartheta(G_n)=(1+o(1))\sqrt n.
\]

**Inherited rigorous bound:**
\[
\sqrt n\le \mathbb E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]
The full-source metric remains `alpha_LL = 1/2 -> 1/2`. No arbitrary-`n` improvement of the published iterated-log exponent is claimed in this report. The progress is instead a new exact finite-dimensional normal form at the conjectured leading constant, an explicit near-flat unitary row-sampling formulation, and exact volume-sampling moment identities for the prime positive-circuit route.

I read `operations/progress_first_2026-09-20/OWNER_DIRECTIVE.md`, `REGISTRY.md`, the canonical claim `operations/claims/RS-2025-TH18.md`, the two preceding P07-A reports, and the newest P07-B report before doing the mathematics. The older source-owner package already contains projected-simplex viewpoints, so I do **not** claim novelty for projected-simplex language itself. The genuinely new contribution of this run to this repository is the critical Householder/orthant normal form and its consequences below. P07-B retains the Fourier-dual / exceptional-frequency route; I do not duplicate its active-set Schur repair.

The assignment/current-source check has already been performed in the canonical claim and the preceding P07 reports: the checked current source still states Conjecture 18 and the primary paper gives the `O(sqrt(n log log n))` upper scale. I found no repository evidence of a later full resolution. This is bounded continuity evidence, not a worldwide novelty certificate.

The predecessor `SRG69` work remains archived **OPEN / PARTIAL** under its old root. Nothing here overwrites, erases, or upgrades it.

---

## 1. Inherited exact primal cone

Let `n` be odd and let `E` be the source random symmetric set of nonzero Fourier differences: each conjugate pair `{d,-d}` is selected independently with probability `1/2`. Let `F` be the **unnormalized** DFT and
\[
L_E=\{z\in\mathbb R^n:\mathbf 1^Tz=0,\ (Fz)_d=0\text{ for every }d\in E\}.
\]
The preceding P07-A work proved
\[
\vartheta(G_E)=1+R_E,
\qquad
R_E=\sup_{0\ne z\in L_E}
\frac{\|z_+\|_\infty}{\|z_-\|_\infty}.
\tag{1.1}
\]
For `0<r<n-1`, define
\[
K_n(r)=\left\{z\in\mathbf 1^\perp:
 z_0\ge r\max_{j\ne0}(-z_j)_+\right\}.
\tag{1.2}
\]
By cyclic invariance,
\[
R_E\ge r\iff L_E\cap K_n(r)\ne\{0\}.
\tag{1.3}
\]
Thus the threshold `theta(G_E)>=t` is the cone-intersection event for `r=t-1`.

The previous report computed the asymptotic statistical dimension of `K_n(c sqrt(n))` and showed that the Haar half-dimensional threshold is `c=1`. The next theorem strengthens that asymptotic observation at the exact source constant.

---

# 2. New exact theorem: `K_n(sqrt(n)-1)` is an orthant

Put
\[
a=r+1,\qquad b=n-1-r=n-a.
\]
For `j=1,...,n-1`, define
\[
g_j(r)=a e_0+b e_j-\mathbf 1.
\tag{2.1}
\]
Let `G_r` be the `n x (n-1)` matrix with these columns.

### Theorem P07-A.5 — exact simplicial normal form
For every `0<r<n-1`,
\[
\boxed{K_n(r)=G_r\,\mathbb R_+^{n-1},}
\tag{2.2}
\]
and this nonnegative-coordinate representation is unique. Moreover
\[
\boxed{G_r^TG_r=b^2I_{n-1}+(a^2-n)J_{n-1}.}
\tag{2.3}
\]
In particular, at the exact theta threshold
\[
t_*=\sqrt n,\qquad r_*=\sqrt n-1,
\]
we have `a_*=sqrt(n)` and therefore
\[
\boxed{G_{r_*}^TG_{r_*}=(n-\sqrt n)^2I_{n-1}.}
\tag{2.4}
\]
Hence `K_n(sqrt(n)-1)` is exactly a rotated/scaled standard orthant in the `(n-1)`-dimensional zero-sum hyperplane.

### Proof
Take `z in K_n(r)`, `z != 0`, and put
\[
s=\frac{z_0}{r}.
\]
The cone inequalities give `z_j+s>=0` for every `j>=1`. Set
\[
x_j=\frac{z_j+s}{b}.
\]
Since `sum_{j>=1} z_j=-rs`,
\[
\sum_{j=1}^{n-1}x_j
=\frac{-rs+(n-1)s}{b}=s.
\]
Therefore, for every `j>=1`,
\[
(G_rx)_j=bx_j-\sum_i x_i=z_j,
\]
while
\[
(G_rx)_0=r\sum_i x_i=rs=z_0.
\]
So `z=G_rx` with `x>=0`. Conversely, if `x>=0` and `s=sum x_i`, then `z=G_rx` has `z_0=rs` and `z_j=bx_j-s>=-s=-z_0/r`, so `z in K_n(r)`. Uniqueness follows from `b>0` and the displayed recovery formula for `x_j`.

For the Gram matrix, if `i!=j`, direct expansion gives
\[
\langle g_i,g_j\rangle=a^2-n,
\]
and on the diagonal
\[
\|g_j\|_2^2=a^2+b^2-n.
\]
This is exactly (2.3). At `a=sqrt(n)`, the off-diagonal term vanishes, giving (2.4). ∎

### Consequence: exact finite-n statistical dimension at the source constant
Because statistical dimension is rotation- and positive-scale-invariant and `delta(R_+^N)=N/2`, (2.4) gives the finite-dimensional identity
\[
\boxed{
\delta\big(K_n(\sqrt n-1)\big)=\frac{n-1}{2}.
}
\tag{2.5}
\]
This is stronger than merely saying that `delta(K_n(sqrt(n)))/n -> 1/2`: after translating from `theta=1+R`, the conjectured theta constant corresponds to an **exact** orthant point.

This explains the leading constant geometrically with no asymptotic approximation: `sqrt(n)` is the value at which the `n-1` extreme rays of the exact primal ratio cone become mutually orthogonal.

---

# 3. Explicit Householder rotation and the source row-sampling matrix

Write
\[
s=\sqrt n,\qquad u=\frac1s\mathbf 1,
\qquad v=e_0-u,
\]
and let
\[
H=I-2\frac{vv^T}{v^Tv}
\tag{3.1}
\]
be the Householder reflection sending `e_0` to `u`. For `j>=1`,
\[
He_j=e_j+\frac{e_0-u}{s-1}.
\tag{3.2}
\]
Let
\[
O=[He_1\ \cdots\ He_{n-1}].
\]
Its columns form an orthonormal basis of `u^perp=1^perp`, and
\[
(n-s)He_j=g_j(s-1).
\tag{3.3}
\]
Thus
\[
\boxed{K_n(s-1)=O\mathbb R_+^{n-1}.}
\tag{3.4}
\]

Now use the **normalized** DFT `U=n^{-1/2}F`. Let `U_*` denote the matrix of all nonzero Fourier rows and set
\[
M=U_*O.
\tag{3.5}
\]
Since both `U_*^*` and `O` are isometries onto `1^perp`, `M` is an `(n-1)x(n-1)` unitary matrix. For every nonzero frequency `k` and every `j>=1`, (3.2) gives the exact entry formula
\[
\boxed{
M_{kj}=\frac1{\sqrt n}
\left(\omega^{kj}+\frac1{\sqrt n-1}\right),
}
\tag{3.6}
\]
where `omega` is the source DFT root of unity (the sign convention is immaterial here). Therefore
\[
\boxed{
\max_{k,j}|M_{kj}|\le\frac1{\sqrt n-1},
}
\tag{3.7}
\]
and the normalized coherence satisfies
\[
\sqrt{n-1}\max_{k,j}|M_{kj}|
\le\sqrt{\frac{\sqrt n+1}{\sqrt n-1}}
=1+O(n^{-1/2}).
\tag{3.8}
\]
So the exact critical change of coordinates turns the source into row sampling from an **asymptotically optimally flat unitary**.

There is a second exact identity:
\[
\boxed{M\mathbf 1=\mathbf 1.}
\tag{3.9}
\]
Indeed `O1=H(1-e_0)=s e_0-u`, whose every nonzero normalized Fourier coefficient equals one.

Let `M_E` denote the rows selected by the source set `E` (equivalently, use the real sine/cosine embedding by conjugate pairs; no parity information is discarded). Combining (1.3) and (3.4),
\[
\boxed{
\vartheta(G_E)\ge\sqrt n
\iff
\exists x\in\mathbb R_+^{n-1}\setminus\{0\}
\text{ such that }M_Ex=0.
}
\tag{3.10}
\]
Thus the sharp source constant is an **orthant-feasibility threshold for independent conjugate-pair row sampling of one explicit near-flat unitary**.

This is much narrower than the all-sparse-vector Fourier RIP problem that pays the iterated-log loss.

---

# 4. Above the critical value: an exact trimmed-simplex deformation

The same Householder basis also gives a closed form for every `t>=sqrt(n)`. Put
\[
r=t-1,\quad a=t,\quad b=n-t,
\quad q=\frac{t-\sqrt n}{\sqrt n-1}.
\]
A direct inner-product calculation using (2.3) gives
\[
\boxed{
G_{t-1}=O\,(bI+qJ).
}
\tag{4.1}
\]
Also
\[
b+q(n-1)=\sqrt n\,(t-1).
\tag{4.2}
\]
Since `b>0` for the relevant range,
\[
(bI+qJ)^{-1}
=\frac1b\left(I-\gamma_tJ\right),
\qquad
\boxed{
\gamma_t=\frac{t-\sqrt n}
{(\sqrt n-1)\sqrt n\,(t-1)}.
}
\tag{4.3}
\]
Therefore, in critical coordinates `z=Oy`, the cone condition is exactly
\[
\boxed{
y_i\ge\gamma_t\sum_jy_j\quad\text{for every }i.}
\tag{4.4}
\]
For a nonzero feasible `y`, its sum is positive. Normalize `sum y_i=1`. Then
\[
\boxed{
y_i\ge\gamma_t,\qquad i=1,...,n-1.}
\tag{4.5}
\]
Thus the supercritical cone is not an arbitrary perturbation of the orthant: it is exactly a **uniformly trimmed simplex cone**.

Let `N=n-1` and
\[
\eta_t=N\gamma_t
=\frac{(\sqrt n+1)(t-\sqrt n)}
{\sqrt n(t-1)}.
\tag{4.6}
\]
Every normalized `y` in (4.5) has the unique form
\[
y=\frac{\eta_t}{N}\mathbf1+(1-\eta_t)p,
\qquad p\in\Delta_{N-1}.
\tag{4.7}
\]
Using `M_E1=1_E`, the exact source event becomes
\[
\boxed{
\vartheta(G_E)\ge t
\iff
\exists p\in\Delta_{N-1}:\quad
M_Ep=-\lambda_t\mathbf1_E,
}
\tag{4.8}
\]
where
\[
\boxed{
\lambda_t=
\frac{t-\sqrt n}{(\sqrt n-1)(n-t)}.
}
\tag{4.9}
\]
For `t=c sqrt(n)` with fixed `c>1`,
\[
\eta_t\to\frac{c-1}{c}.
\tag{4.10}
\]
So the fixed-`epsilon` source upper tail is equivalent to asking whether a random conjugate-pair coordinate projection of this explicit near-flat unitary sends the standard simplex onto the tiny diagonal target `-lambda_t 1_E`, while the primal weights are forced to retain a positive uniform floor of asymptotic mass fraction `(c-1)/c`.

This is the most concrete source-specific comparison target I know from the present line.

---

# 5. Why generic subspace universality is unnecessary — and currently unavailable

The preceding report reduced the sharp expectation upper bound to showing, for every fixed `epsilon>0`,
\[
\Pr\{\vartheta(G_E)\ge(1+\epsilon)\sqrt n\}
=o(n^{-1/2}).
\tag{5.1}
\]
Equations (4.8)-(4.9) sharpen the object on which such a comparison must be proved.

A useful sufficient theorem would be:

> **Near-flat-unitary trimmed-simplex escape, source-specific version.** For the explicit unitary `M` in (3.6), Bernoulli-`1/2` sampling of conjugate row pairs has, for every fixed `c>1`, probability `o(n^{-1/2})` of satisfying the feasibility event (4.8) at `t=c sqrt(n)`.

This theorem would directly imply the fixed-`epsilon` tail needed for the sharp expectation upper bound. It asks for no RIP statement over all sparse vectors and no universality over all convex cones.

Oymak--Tropp-style universality is the nearest conceptual mechanism, but the theorem forms I checked require independent standardized matrix entries; independent **row selection from a deterministic Fourier/unitary matrix** is structured dependence and is not covered merely by citing that machinery. Accordingly this report records universality only as a route to port, not as an available proof.

A potentially useful distinction from P07-B is now clean:
- P07-B studies dual exceptional frequencies, principal blocks, and Schur leakage.
- P07-A can study **orthant/trimmed-simplex feasibility under row sampling of (3.6)** directly, via convex-hull geometry, oriented matroids, or a row-sampling invariance principle.

---

# 6. Prime-order circuit route: exact volume-sampling calibration at scale `1/sqrt(n)`

This section records a separate structural calculation. It does not by itself prove a tail bound, but it identifies exactly what an average-minor argument can and cannot deliver.

Assume `n=p` is prime. Fix a symmetric source frequency set `E` of size `m` and put
\[
R=\{0\}\cup E,\qquad k=m+1.
\]
Let `U` be the normalized DFT and `A=U_{R,:}`. The rows of `A` are orthonormal. For every `T subset [n]` with `|T|=k`, prime DFT full-spark/Chebotarev implies `A_T` is invertible. Define the unique circuit/basic solution supported on `T` by
\[
A_Tx_T=\frac1{\sqrt n}e_0.
\tag{6.1}
\]
It has total mass `1` and annihilates all frequencies in `E`. A primal vertex occurs exactly when `x_T` is entrywise nonnegative; this is the positive-circuit parametrization inherited from the first P07-A report.

Put
\[
w_T=|\det A_T|^2.
\tag{6.2}
\]
By Cauchy--Binet,
\[
\boxed{\sum_{|T|=k}w_T=1.}
\tag{6.3}
\]
The associated determinantal/volume sampling law has uniform leverage,
\[
\boxed{\sum_{T\ni j}w_T=\frac{k}{n}.}
\tag{6.4}
\]

### Theorem P07-A.6 — exact volume-weighted circuit moments
For every coordinate `j`,
\[
\boxed{
\sum_{T\ni j}w_Tx_T(j)=\frac1n,
}
\tag{6.5}
\]
and
\[
\boxed{
\sum_{T\ni j}w_Tx_T(j)^2
=\frac{n-m}{n^2}.
}
\tag{6.6}
\]
Consequently, under volume sampling conditioned on `j in T`,
\[
\boxed{
\mathbb E_{\rm vol}[x_T(j)\mid j\in T]=\frac1k,
\qquad
\mathbb E_{\rm vol}[x_T(j)^2\mid j\in T]
=\frac{n-m}{nk}.
}
\tag{6.7}
\]
For the dense source regime `m~n/2`, the conditional RMS coordinate is `(1+o(1))/sqrt(n)`.

### Proof
Translation of the column set `T` cyclically multiplies the nonzero Fourier rows by phases, so it preserves `w_T`, while the unique solution `x_T` translates with `T`. Hence the left side of (6.5) is independent of `j`. Summing over `j` gives
\[
\sum_j\sum_{T\ni j}w_Tx_T(j)
=\sum_Tw_T\sum_{j\in T}x_T(j)
=\sum_Tw_T=1,
\]
which proves (6.5).

For (6.6), Cramer's rule gives, for `j in T`,
\[
w_Tx_T(j)^2
=\frac1n\left|\det U_{E,T\setminus\{j\}}\right|^2.
\tag{6.8}
\]
Summing over `T` containing `j` is the same as summing all `m x m` minors of the matrix obtained from `U_E` after deleting column `j`. Cauchy--Binet yields
\[
\sum_{T\ni j}\left|\det U_{E,T\setminus\{j\}}\right|^2
=\det(I-b_jb_j^*),
\]
where `b_j=U_Ee_j`. Since every Fourier column has squared norm `m/n`, the rank-one determinant lemma gives
\[
\det(I-b_jb_j^*)=1-\frac mn=\frac{n-m}{n}.
\]
Multiplying by `1/n` proves (6.6). Dividing (6.5)-(6.6) by (6.4) gives (6.7). ∎

Summing (6.6) over `j` also gives
\[
\boxed{
\sum_Tw_T\|x_T\|_2^2=\frac{n-m}{n}.
}
\tag{6.9}
\]

### What this does and does not show
The exact second moment lands at the conjectured `1/sqrt(n)` atom scale. This is encouraging: the natural Fourier volume measure already knows the correct scale with no `log log` loss.

But it is **not** enough to control theta. The optimizer ranges only over **positive** circuits and can in principle be concentrated on very small-volume bases. Equations (6.3)-(6.9) average over all signed circuits. Therefore an average-minor or leverage argument needs a new anti-correlation statement between positivity/large atom and tiny determinant before it can prove the source conjecture.

This identifies a precise obstruction rather than hiding it behind a generic conditioning estimate.

---

# 7. A warning: flat leverage alone cannot imply the conjectured scale

The need for entrywise Fourier geometry is genuine. Constant diagonal/leverage of the sampled projection is not enough. For even dimension, consider the projection whose kernel is spanned by the disjoint vectors
\[
e_0+e_1,\ e_2+e_3,\ldots.
\]
Its diagonal leverage is exactly `1/2`, just as in a half-dimensional flat model, but the kernel contains the probability vector
\[
\frac12(e_0+e_1),
\]
whose largest atom is `1/2`, enormously larger than `1/sqrt(n)`.

Thus a proof cannot use only dimension, flat diagonal leverage, or volume identities. It must exploit at least one of:
1. the near-optimal **entry coherence** (3.7)-(3.8),
2. the arithmetic/oriented-matroid structure of the Fourier columns,
3. positivity-selected anti-concentration for the circuits, or
4. a source-specific row-sampling comparison for the trimmed simplex.

This is also why the Haar benchmark from the previous report was informative but not itself transferable by dimension alone.

---

# 8. Mathematical movement and remaining gap

### Inherited full-source metric
`alpha_LL = 1/2 -> 1/2` (unchanged).

### New proved partial results
1. **Exact simplicial cone:** `K_n(r)=G_r R_+^{n-1}` with explicit Gram (2.3).
2. **Exact critical orthant:** at `theta=sqrt(n)`, the cone rays are mutually orthogonal and `delta=(n-1)/2` exactly.
3. **Explicit critical unitary:** after one Householder transform, the source is conjugate-pair row sampling of the unitary (3.6), whose normalized coherence is `1+O(n^-1/2)`.
4. **Exact supercritical deformation:** `theta>=t` becomes trimmed-simplex feasibility (4.8) with explicit floor mass `eta_t` and target displacement `lambda_t`.
5. **Prime volume calibration:** exact volume-weighted first/second moments (6.5)-(6.9) put the natural circuit RMS at `1/sqrt(n)` and isolate positivity-versus-small-determinant correlation as the missing step.

All five items are **PROVED PARTIAL**. None is represented as a full solution.

### Remaining source gap
For each fixed `epsilon>0`, prove
\[
\Pr\{\exists p\in\Delta_{n-2}:\
M_Ep=-\lambda_{(1+\epsilon)\sqrt n}\mathbf1_E\}
=o(n^{-1/2}),
\tag{8.1}
\]
with `M` exactly (3.6) and `E` generated by independent conjugate-pair Bernoulli sampling. This would give the sharp expectation upper bound via the deterministic `theta<=n` tail truncation already recorded in the preceding report.

### Next concrete attack
Work directly on (8.1), not on all-sparse RIP:

- expose the random row pairs one at a time and seek a **cone-specific invariance/Lindeberg estimate** for the support function / distance of `-lambda_t 1_E` to `conv{M_E e_j}`;
- exploit the exact floor fraction `eta_t -> epsilon/(1+epsilon)` to show that any supercritical feasible point is a mixture with a macroscopically uniform component, drastically reducing admissible active-set entropy;
- on prime `n`, prove a positivity-conditioned tail bound of the form
  `P_vol(max_j x_T(j) >= (1+epsilon)/sqrt(n), x_T>=0)` that is stronger than the unconditional moment estimate because large positive atoms should force an atypically small Fourier minor.

The first item is the preferred route; the third is a structurally independent backup. Neither duplicates P07-B's dual exceptional-frequency analysis.

---

## Compact checkpoint

```yaml
native_task_id: "6aa7b46f70a8819184095c277974c256"
role: "P07-A primal / structural"
target: "Randomstrasse101 Conjecture 18 / dense random circulant Lovasz theta"
status: "OPEN / PROVED PARTIAL"
full_source_metric:
  name: "alpha_LL"
  before: "1/2"
  after: "1/2"
new_obligations_reduced:
  - "sharp constant converted exactly to orthant feasibility for an explicit near-flat unitary"
  - "fixed-c supercritical event converted exactly to trimmed-simplex feasibility"
  - "prime circuit volume law calibrated exactly at RMS 1/sqrt(n)"
remaining_gap: "o(n^-1/2) source-specific trimmed-simplex escape tail under conjugate-pair row sampling"
next_attack: "row-pair invariance / convex-hull distance for the explicit Householder-Fourier unitary; positivity-conditioned minor anti-concentration as backup"
complementary_owner: "P07-B keeps Fourier-dual / exceptional-frequency and Schur-leakage work"
predecessor_handoff: "SRG69 remains archived OPEN/PARTIAL and untouched"
```
