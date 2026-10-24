Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED** — GPT-6 / maximum was requested as an owner preference, but this runtime exposes no authenticated completed-run effort telemetry or binding model/effort selector, so I do not claim otherwise.

# P07-B — excluded-origin Gibbs tilt reaches the critical radial scale, with controlled exceptional frequencies

**Native role:** `P07-B`, task `6aabe797a39081919acc889f29f4c556`  
**Repository / branch:** private `yspennstate/math-open-problems` / `master`  
**Captured start master:** `67d34b96486242fb75349d3ae745a23ba4f43616`  
**Fresh pre-write master:** `4e2d5d8e5712cde99b916efa8667dc05918a22e2`  
**Previous own substantive report:** `probability_campaigns/progress_first_2026-09-20/P07/fourier_dual/2026-09-20T0832+0300__reciprocal_convolution_collision_energy.md`, creation commit `81fe31da43bb124a30e6a453185eee7d7f58155a`; preserve its separate equation-(4.11) erratum at commit `355ea7b12495afd46b97ba7a82225f76311ed513`.  
**Complementary P07-A checkpoint used:** `probability_campaigns/progress_first_2026-09-20/P07/primal/2026-09-20T0842+0300__unique_positive_cosine_basis_discrepancy.md`. P07-A owns the primal/positive-basis structure; this report stays on the Fourier-dual/moment-map side.  
**Outside target:** Randomstrasse101, arXiv:2603.29571, Conjecture 18; primary partial-result paper arXiv:2502.16227.  
**Exact source endpoint:** for the dense random undirected circulant source model,
\[
\mathbb E\vartheta(G_n)=(1+o(1))\sqrt n.
\]
**Inherited rigorous source bound:**
\[
\sqrt n\le \mathbb E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]
Thus the frozen full-source exponent metric remains
\[
\boxed{\alpha_{LL}=1/2\to1/2.}
\]
Status: **OPEN / PROVED PARTIAL**. No improved arbitrary-`n` theta upper bound is claimed yet.

The assignment-time source recovery, exact Fourier LP, and older TH18 attempts were already recovered in earlier P07-B reports. The exact static identity used below is
\[
\kappa_D=\frac1{n\delta_D},\qquad
\mathbb E\vartheta(G_n)=1+\mathbb E\frac1{\delta_D},
\tag{0.1}
\]
where
\[
\delta_D:=\max\left\{\delta\ge0:\exists\text{ symmetric probability }p\text{ on }\mathbb Z_n,
\ \mathbb E_p\cos(2\pi aJ/n)=-\delta\ \forall a\in D\right\}.
\tag{0.2}
\]
The old linear perturbation of the full uniform law fails because the origin forces only `delta=O(1/n)`. The new idea is to remove the origin **before** tilting, then use a nonlinear Gibbs law. This completely removes the coherent origin spike and reaches the correct `n^{-1/2}` radial scale. The remaining obstruction is no longer radial scale: it is transverse equalization of the selected Fourier moments.

No numerical experiment and no independence approximation between Fourier coordinates is used below.

---

## 1. Setup and exact cosine identities

Let `n` be odd and put
\[
M:=\{1,\dots,(n-1)/2\}.
\]
The source mask is
\[
D\subset M,
\]
with the indicators `xi_a=1_{a in D}` independent Bernoulli `(1/2)`. Put `d=|D|`. For `j in Z_n` define
\[
\phi_a(j):=\cos(2\pi aj/n),
\qquad
S_D(j):=\sum_{a\in D}\phi_a(j),
\qquad
X_D(j):=\frac{S_D(j)}{\sqrt n}.
\tag{1.1}
\]

For every nonzero `j mod n`, pairing the nonzero characters gives
\[
\boxed{\sum_{a\in M}\phi_a(j)=-\frac12.}
\tag{1.2}
\]
Using `cos^2 u=(1+cos 2u)/2` and the fact that `2j ne 0 mod n`, one also has
\[
\boxed{\sum_{a\in M}\phi_a(j)^2=\frac{n-2}{4}.}
\tag{1.3}
\]
Finally, if `j,k ne0` and `k ne plus/minus j mod n`, the product-to-sum identity gives
\[
\boxed{
\sum_{a\in M}\phi_a(j)\phi_a(k)=-\frac12.
}
\tag{1.4}
\]
These are deterministic identities. They are what permits dependence-aware second-moment estimates below.

---

# 2. The excluded-origin Gibbs law

Fix a real constant `beta`. Define the empirical partition function
\[
A_D(\beta):=\frac1{n-1}\sum_{j\ne0}e^{-\beta X_D(j)}
\tag{2.1}
\]
and the symmetric probability law
\[
p_{\beta,D}(0)=0,
\qquad
p_{\beta,D}(j)
:=\frac{e^{-\beta X_D(j)}}{\sum_{k\ne0}e^{-\beta X_D(k)}}
\quad(j\ne0).
\tag{2.2}
\]
Since `X_D(-j)=X_D(j)`, this law is symmetric. Write its cosine moments
\[
m_a(\beta):=\mathbb E_{p_{\beta,D}}\phi_a(J),
\qquad a\in M.
\tag{2.3}
\]

The point is that the old obstruction at `j=0` has vanished identically: the Gibbs law assigns that point zero mass, while still remaining an admissible symmetric probability in the moment-polytope formulation (0.2).

---

# 3. Dependence-aware annealed Gibbs limit

## Theorem P07-B.11 — radial Gibbs free energy

For every fixed real `beta`, as `n -> infinity` through odd integers,
\[
\boxed{
A_D(\beta)\longrightarrow e^{\beta^2/32}
}
\tag{3.1}
\]
in `L^2` with respect to the source mask, hence in probability. Moreover, on every fixed compact beta interval the same convergence holds after one or two beta derivatives. Consequently, if
\[
F_D(\beta):=\log A_D(\beta),
\]
then
\[
\boxed{
F_D'(\beta)\xrightarrow{\mathbb P}\frac{\beta}{16},
\qquad
F_D''(\beta)\xrightarrow{\mathbb P}\frac1{16}.
}
\tag{3.2}
\]
Equivalently,
\[
\boxed{
\mathbb E_{p_{\beta,D}}X_D(J)
=-\frac{\beta}{16}+o_{\mathbb P}(1),
}
\tag{3.3}
\]
and
\[
\boxed{
\operatorname{Var}_{p_{\beta,D}}X_D(J)
=\frac1{16}+o_{\mathbb P}(1).
}
\tag{3.4}
\]

### Proof

For a fixed nonzero `j`, independence of the **mask bits** (not of the Fourier coordinates) gives
\[
\mathbb E_D e^{-\beta X_D(j)}
=\prod_{a\in M}\frac{1+e^{-(\beta/\sqrt n)\phi_a(j)}}2.
\tag{3.5}
\]
For bounded complex `z`,
\[
\log\frac{1+e^{-z}}2
=-\frac z2+\frac{z^2}{8}+O(|z|^4).
\tag{3.6}
\]
Apply (3.6) with `z=(beta/sqrt(n)) phi_a(j)` and sum. By (1.2)--(1.3),
\[
\begin{aligned}
\log\mathbb E_D e^{-\beta X_D(j)}
&=\frac{\beta}{4\sqrt n}
+\frac{\beta^2(n-2)}{32n}
+O_\beta(n^{-1})\\
&=\frac{\beta^2}{32}+O_\beta(n^{-1/2}).
\end{aligned}
\tag{3.7}
\]
Thus each nonzero site has the required limiting annealed exponential moment.

Now take `j,k ne0` with `k ne plus/minus j`. Expanding the joint product as in (3.5), the only quadratic cross term in the logarithm is proportional to
\[
\frac1n\sum_{a\in M}\phi_a(j)\phi_a(k),
\]
which equals `-1/(2n)` by (1.4). Therefore, uniformly for bounded beta,
\[
\frac{
\mathbb E_D e^{-\beta(X_D(j)+X_D(k))}
}{
\mathbb E_D e^{-\beta X_D(j)}\,
\mathbb E_D e^{-\beta X_D(k)}
}
=1+O_\beta(n^{-1}).
\tag{3.8}
\]
The diagonal/antidiagonal pairs `k=plus/minus j` number only `O(n)` out of the `O(n^2)` pairs and have uniformly bounded second exponential moments. Hence
\[
\operatorname{Var}_D A_D(\beta)=O_\beta(n^{-1}).
\tag{3.9}
\]
Together with (3.7), this proves (3.1).

The product estimate above is analytic and uniform on a fixed complex neighborhood of a compact real beta interval. Applying the same second-moment estimate there and Cauchy's integral formula gives `L^2` convergence for the first two derivatives of `A_D`; dividing by `A_D`, which converges to a strictly positive limit, gives (3.2). Finally,
\[
F_D'(\beta)=-\mathbb E_{p_{\beta,D}}X_D,
\qquad
F_D''(\beta)=\operatorname{Var}_{p_{\beta,D}}X_D,
\]
which proves (3.3)--(3.4). `square`

### What this does and does not use

The values `X_D(j)` and `X_D(k)` are strongly dependent because they use the same random mask. The proof does not replace them by independent Gaussians. Their joint dependence enters explicitly through the exact cross identity (1.4).

---

# 4. The Gibbs law reaches the exact `1/sqrt(n)` radial moment scale

Because
\[
X_D(J)=\frac1{\sqrt n}\sum_{a\in D}\phi_a(J),
\]
(3.3) gives
\[
\sum_{a\in D}m_a(\beta)
=-\frac{\beta\sqrt n}{16}+o_{\mathbb P}(\sqrt n).
\tag{4.1}
\]
Also `d/n -> 1/4` with exponentially small fixed-density deviations. Hence the average selected moment obeys
\[
\boxed{
\overline m_D(\beta)
:=\frac1d\sum_{a\in D}m_a(\beta)
=-\frac{\beta}{4\sqrt n}+o_{\mathbb P}(n^{-1/2}).
}
\tag{4.2}
\]

This is the first genuinely critical-scale positive moment construction in this P07-B line: the nonlinear law (2.2) attains a negative average selected Fourier moment of order exactly `n^{-1/2}` while remaining a bona fide probability measure. The old full-uniform linear perturbation was limited to `O(n^{-1})` by the coherent origin spike.

The remaining issue is **flatness**: (0.2) requires every selected moment to equal the same negative number, while (4.2) gives the correct average.

---

# 5. Exact collision energy and near-flatness of the selected moments

The Gibbs law has a useful exact Fourier-energy identity. Since it is symmetric and `p(0)=0`, Parseval gives
\[
n\sum_jp_{\beta,D}(j)^2
=1+2\sum_{a\in M}m_a(\beta)^2.
\tag{5.1}
\]
On the other hand, directly from (2.1)--(2.2),
\[
n\sum_jp_{\beta,D}(j)^2
=\frac{n}{n-1}\frac{A_D(2\beta)}{A_D(\beta)^2}.
\tag{5.2}
\]
Theorem P07-B.11 therefore yields
\[
\boxed{
\sum_{a\in M}m_a(\beta)^2
\xrightarrow{\mathbb P}
\frac{e^{\beta^2/16}-1}{2}.
}
\tag{5.3}
\]

There is also an exact first-moment identity. Since every nonzero support point satisfies (1.2),
\[
\boxed{
\sum_{a\in M}m_a(\beta)=-\frac12.
}
\tag{5.4}
\]
Consequently, with `C=M\D`,
\[
\sum_{a\in C}m_a(\beta)
=\frac{\beta\sqrt n}{16}+o_{\mathbb P}(\sqrt n).
\tag{5.5}
\]

Define the within-group dispersions
\[
V_D:=\sum_{a\in D}(m_a-\overline m_D)^2,
\qquad
V_C:=\sum_{a\in C}(m_a-\overline m_C)^2.
\tag{5.6}
\]
Using (4.1), (5.3), (5.5), and `d/n,|C|/n ->1/4`, we obtain
\[
\boxed{
V_D+V_C
\xrightarrow{\mathbb P}
R(\beta)
:=\frac{e^{\beta^2/16}-1}{2}-\frac{\beta^2}{32}.
}
\tag{5.7}
\]
In particular,
\[
\boxed{V_D\le R(\beta)+o_{\mathbb P}(1).}
\tag{5.8}
\]
For small beta,
\[
\boxed{R(\beta)=\frac{\beta^4}{1024}+O(\beta^6).}
\tag{5.9}
\]
Thus the radial Gibbs tilt does more than hit the correct mean scale: its selected-moment residual from the desired flat direction has `l2` norm only `O(beta^2)` for small fixed beta.

---

# 6. Controlled exceptional selected frequencies

Fix `beta>0` and define
\[
B_D(\beta):=
\left\{a\in D:m_a(\beta)>-\frac{\beta}{8\sqrt n}\right\}.
\tag{6.1}
\]
By (4.2), every member of `B_D(beta)` differs from the selected mean by at least `(beta/8+o_P(1))/sqrt(n)`. Therefore (5.8) gives
\[
\boxed{
\frac{|B_D(\beta)|}{d}
\le
\frac{256R(\beta)}{\beta^2}+o_{\mathbb P}(1).
}
\tag{6.2}
\]
For small beta,
\[
\boxed{
\frac{|B_D(\beta)|}{d}
\le \frac{\beta^2}{4}+O(\beta^4)+o_{\mathbb P}(1).
}
\tag{6.3}
\]
So the first nonlinear dual construction already puts all but an `O(beta^2)` fraction of the source-selected frequencies on the correct negative `1/sqrt(n)` side. For orientation only, the rigorous limiting expression on the right of (6.2) is about `0.06283` at `beta=1/2` and `0.01565` at `beta=1/4`.

This is a source-generated exceptional-frequency estimate, not a claim that the exceptional indices are independent or uniformly random.

---

# 7. Covariance geometry: radial transversality and only a small bad eigenspace

Let
\[
H_D(\beta):=
\operatorname{Cov}_{p_{\beta,D}}
\big((\phi_a(J))_{a\in D}\big).
\tag{7.1}
\]
This is the Hessian of the selected-feature log-partition map.

## 7.1 Exact base-point spectrum

At `beta=0`, `p` is uniform on `Z_n\{0}`. Each feature has mean `-1/(n-1)`. Direct use of (1.2)--(1.4) gives diagonal covariance
\[
\frac{n-2}{2(n-1)}-\frac1{(n-1)^2}
\]
and off-diagonal covariance
\[
-\frac1{n-1}-\frac1{(n-1)^2}.
\]
Hence the all-ones direction has eigenvalue
\[
\boxed{
\lambda_{\rm rad}(0)
=\frac{n(n-1-2d)}{2(n-1)^2}
\xrightarrow{\mathbb P}\frac14,
}
\tag{7.2}
\]
while every transverse direction has the exact eigenvalue
\[
\boxed{
\lambda_\perp(0)=\frac{n}{2(n-1)}\longrightarrow\frac12.
}
\tag{7.3}
\]
Thus the relevant moment map starts uniformly transverse at the excluded-origin uniform law.

## 7.2 Radial direction remains nondegenerate after the critical tilt

Let `u=1_D/sqrt(d)`. Since `u dot phi(J)=S_D(J)/sqrt(d)`, (3.4) implies
\[
\boxed{
u^TH_D(\beta)u
=\frac{\operatorname{Var}_{p_{\beta,D}}S_D(J)}d
\xrightarrow{\mathbb P}\frac14.
}
\tag{7.4}
\]
So there is no radial covariance collapse at any fixed beta.

## 7.3 New spectral exceptional-dimension bound

Write the full symmetric Fourier coefficients of `p_{beta,D}` as `m_k`, with `m_0=1` and `m_{-k}=m_k`. Product-to-sum gives, for `a,b in D`,
\[
\mathbb E_p[\phi_a\phi_b]
=\frac12(m_{a-b}+m_{a+b}).
\tag{7.5}
\]
Therefore
\[
H_D(\beta)=\frac12I+K-mm^T,
\tag{7.6}
\]
where `m=(m_a)_{a in D}` and
\[
K_{ab}=\frac12(\widetilde m_{a-b}+m_{a+b}),
\qquad
\widetilde m_0=0,
\quad \widetilde m_k=m_k\ (k\ne0).
\tag{7.7}
\]
For each nonzero difference or sum frequency there are at most `d` ordered pairs `(a,b) in D^2` producing it. Hence
\[
\|K\|_F^2
\le d\sum_{k\ne0}m_k^2.
\tag{7.8}
\]
By Parseval and (5.2),
\[
\sum_{k\ne0}m_k^2
\xrightarrow{\mathbb P}e^{\beta^2/16}-1.
\tag{7.9}
\]
The rank-one term has Frobenius norm `||m||_2^2=O_P(1)`, so after division by `d` it is negligible compared with (7.8). Thus
\[
\boxed{
\frac1d\left\|H_D(\beta)-\frac12I\right\|_F^2
\le e^{\beta^2/16}-1+o_{\mathbb P}(1).
}
\tag{7.10}
\]
Consequently, for every fixed `tau>0`,
\[
\boxed{
\frac1d\#\left\{i:\lambda_i(H_D(\beta))\le\frac12-\tau\right\}
\le
\frac{e^{\beta^2/16}-1}{\tau^2}+o_{\mathbb P}(1).
}
\tag{7.11}
\]
For small beta this is
\[
\frac{\beta^2}{16\tau^2}+O(\beta^4)+o_{\mathbb P}(1).
\tag{7.12}
\]
Therefore the remaining covariance obstruction is confined to an `O(beta^2)` **fraction of spectral directions** for fixed spectral gap threshold. This does not prove a minimum-eigenvalue bound, but it sharply localizes where a multiscale repair must work.

---

# 8. Exact missing lemma that removes the iterated-log loss

The previous TH18 handoff asked for a covariance floor along a broad maximum-entropy path. Sections 3--7 reduce that substantially: the radial path is already under control, and the desired flat target is only `O(beta^2)` away in selected-moment `l2` norm.

For `lambda in R^D`, define
\[
\psi_D(\lambda)
:=\log\sum_{j\ne0}
\exp\left(\sum_{a\in D}\lambda_a\phi_a(j)\right).
\tag{8.1}
\]
Its gradient is the selected moment vector and its Hessian is the feature covariance. The Gibbs point above is
\[
\lambda^0=-\frac\beta{\sqrt n}\mathbf1_D.
\tag{8.2}
\]
Let
\[
m^0=\nabla\psi_D(\lambda^0),
\qquad
\bar m=\frac1d\mathbf1^Tm^0,
\qquad
r=m^0-\bar m\mathbf1.
\tag{8.3}
\]
By (5.8),
\[
\|r\|_2^2=V_D\le R(\beta)+o_{\mathbb P}(1)=O(\beta^4).
\tag{8.4}
\]

## Missing lemma `STCL(beta)` — small-tube transverse covariance

For some fixed sufficiently small `beta>0`, prove that there is a constant `c_beta>0` such that, with failure probability `O(n^{-1/2})`,
\[
\boxed{
\lambda_{\min}\nabla^2\psi_D(\lambda)\ge c_\beta
}
\tag{8.5}
\]
for every
\[
\boxed{
\|\lambda-\lambda^0\|_2
\le
\frac{2\sqrt{R(\beta)+o(1)}}{c_\beta}.
}
\tag{8.6}
\]
For small beta this tube has radius `O(beta^2)`, not order one.

### Why `STCL(beta)` is sufficient

Consider the convex function
\[
\Phi(\lambda)
=\psi_D(\lambda)-\bar m\,\mathbf1^T\lambda.
\tag{8.7}
\]
At `lambda^0`,
\[
\nabla\Phi(\lambda^0)=r.
\]
On a sphere of radius `R_0=2||r||_2/c_beta` inside the STCL tube, for `u=lambda-lambda^0`,
\[
\begin{aligned}
\langle\nabla\Phi(\lambda^0+u),u\rangle
&=\langle r,u\rangle
+\int_0^1u^T\nabla^2\psi_D(\lambda^0+tu)u\,dt\\
&\ge-\|r\|_2R_0+c_\beta R_0^2>0.
\end{aligned}
\tag{8.8}
\]
Thus the minimum of `Phi` on the closed ball cannot lie on its boundary. It has an interior minimizer `lambda*`, and there
\[
\nabla\psi_D(\lambda^*)=\bar m\mathbf1_D.
\tag{8.9}
\]
The corresponding symmetric Gibbs probability therefore has **exactly equal** selected cosine moments. By (4.2),
\[
\delta_D\ge-\bar m
=\frac\beta{4\sqrt n}+o_{\mathbb P}(n^{-1/2}).
\tag{8.10}
\]
On the STCL-good event,
\[
\frac1{\delta_D}\le\left(\frac4\beta+o(1)\right)\sqrt n.
\tag{8.11}
\]
On the failure event use the universal feasible law uniform on `Z_n\{0}`, which gives
\[
\delta_D\ge\frac1{n-1},
\qquad
\frac1{\delta_D}\le n-1.
\tag{8.12}
\]
Hence failure probability `O(n^{-1/2})` in STCL implies
\[
\boxed{
\mathbb E\frac1{\delta_D}=O(\sqrt n),
\qquad
\mathbb E\vartheta(G_n)=O(\sqrt n).
}
\tag{8.13}
\]
By (0.1), this proves
\[
\boxed{\alpha_{LL}=0,}
\]
i.e. it removes the published `sqrt(log log n)` loss completely. It would **not** by itself prove the sharp leading constant `1`. Reaching that constant would require a substantially sharper version, effectively controlling flat moment level near `1/sqrt(n)` rather than merely a fixed positive multiple of it.

This is the exact theorem-sized next lemma for P07-B.

---

# 9. Relation to P07-A and next attack

P07-A's newest prime-order theorem says the actual optimizer is a unique positive cosine basis whose selected edge rows all see one exact negative flat level. P07-B does not duplicate that support geometry. The new dual result instead constructs a full-support positive Gibbs law with:

1. the **correct critical radial level** `-beta/(4 sqrt(n))` on average;
2. only an `O(beta^2)` fraction of selected Fourier moments failing even half that negative level;
3. total selected flatness error `||r||_2=O(beta^2)`;
4. radial covariance tending to `1/4`; and
5. only an `O(beta^2)` fraction of covariance eigen-directions capable of being far below the natural `1/2` transverse scale.

The clean interface to P07-A is therefore: the primal exact flat-negative-level witness is now known to sit a small transverse moment-map correction away from a source-generated positive Gibbs witness, provided the small bad covariance subspace can be controlled.

### Next concrete attack

Prove `STCL(beta)` for one small fixed beta without treating the endogenous Fourier coordinates or the exceptional set as independent. The most promising decomposition from this run is multiscale:

- use (7.11) to split the covariance into a large well-conditioned subspace plus an `O(beta^2)d` bad spectral subspace;
- correct the well-conditioned component of `r` by one Newton/strong-convexity step;
- re-express the residual entirely inside the bad subspace and use the exact Fourier form (7.5)--(7.7) to expose a smaller source-coupled problem;
- iterate only if the bad dimension genuinely shrinks. A proof must track the same mask dependence throughout; a fresh-independent-mask assumption would be invalid.

A second route is a direct lower-small-ball estimate for `v dot phi(J)` under the Gibbs law, uniform only over vectors in the endogenous bad eigenspace. This is far narrower than a uniform all-vector RIP statement and is the dependence-aware small-ball target requested for this role.

---

## 10. Result status

- Full source conjecture: **OPEN**.
- Published-bound exponent: **`alpha_LL=1/2 -> 1/2`** in this report.
- Theorem P07-B.11 (annealed Gibbs free energy and radial variance): **PROVED PARTIAL**.
- Critical radial mean (4.2): **PROVED PARTIAL**.
- Moment collision energy / dispersion (5.3)--(5.9): **PROVED PARTIAL**.
- Controlled exceptional selected frequencies (6.2)--(6.3): **PROVED PARTIAL**.
- Covariance exceptional-dimension bound (7.10)--(7.12): **PROVED PARTIAL**.
- `STCL(beta)`: **CONJECTURAL MISSING LEMMA**; its implication (8.13) is proved conditionally.

No shared ledger, peer report, historical report, public endpoint, email, Drive file, permission, or workflow was modified in this run.