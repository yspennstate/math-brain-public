Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but the exposed runtime provides no authenticated reasoning-effort telemetry, so I do not claim otherwise.**

# P06 complementary P07 iteration — exact Gibbs Fourier-energy identity, O(1) coordinate anisotropy, and a quantitative covariance floor

Status: **P06 SOURCE KNOWN / no novelty claim for Conjecture 17. P07 PROVED PARTIAL new mathematics; publication novelty UNVERIFIED.**

Native role preserved: `6aa7b53b0858819196d923203522c996`.  
Captured input `master`: `aac80d8ab5a7c0d5ce7dc447f8a7ed9a60fb7540`.  
No P07-A/P07-B canonical ownership or report is modified. This is a complementary lemma package only.

## 1. Fixed source state and inherited bottleneck

P06 / Randomstrasse Conjecture 17 remains a **KNOWN** endpoint in later literature. The fixed source metric stays

`U_ER^cert = 1`.

This run does not re-screen or rediscover it.

For P07 / Randomstrasse Conjecture 18, the strongest recovered primary global theorem remains

\[
\sqrt n\le \mathbb E\vartheta(G_n)\le C\sqrt{n\log\log n},
\]

so the full-source iterated-log loss is unchanged.

The preceding complementary report proved, for odd prime `n`, a random half-frequency mask `D\subset H={1,...,(n-1)/2}`, and

\[
S_D(j)=\sum_{a\in D}\cos(2\pi aj/n),
\qquad
p_{D,c}(j)=\frac{e^{-cS_D(j)/\sqrt n}}{nZ_D(c)},
\]

that for fixed `c>=0`,

\[
Z_D(c)=e^{c^2/32}+o_{\mathbb P}(1),
\qquad
\frac1{\sqrt n}\,\mathbb E_{p_{D,c}}S_D\to_{\mathbb P}-\frac c{16}.
\]

Writing

\[
\mu_a(c):=\mathbb E_{p_{D,c}}\cos(2\pi aJ/n),
\qquad
\bar\mu_D(c):=\frac1{|D|}\sum_{a\in D}\mu_a(c),
\]

this gives

\[
\bar\mu_D(c)=-\frac{c/4+o_{\mathbb P}(1)}{\sqrt n}.
\]

At `c=4`, the **average** selected moment is therefore at the exact target scale `-1/sqrt(n)`. The missing implication was coordinatewise control plus a covariance lower bound sufficient for a multivariate correction.

The present run moves both obligations.

---

# 2. Exact identity: Gibbs collision probability equals total Fourier energy

Let

\[
\widehat p_{D,c}(k)=\sum_{j\in\mathbb Z_n}p_{D,c}(j)e^{2\pi i kj/n}.
\]

Because `S_D(j)=S_D(-j)`, the Gibbs law is symmetric, so for every `a\in H`,

\[
\widehat p_{D,c}(a)=\widehat p_{D,c}(n-a)=\mu_a(c)\in\mathbb R,
\]

and `\widehat p(0)=1`.

Parseval for the nonunitary Fourier transform gives the exact identity

\[
1+2\sum_{a\in H}\mu_a(c)^2
=n\sum_j p_{D,c}(j)^2.
\tag{2.1}
\]

But

\[
\begin{aligned}
n\sum_jp_{D,c}(j)^2
&=n\sum_j\frac{e^{-2cS_D(j)/\sqrt n}}{n^2Z_D(c)^2}\\
&=\frac{Z_D(2c)}{Z_D(c)^2}.
\end{aligned}
\]

Hence, **for every realization `D` and every `c`**, not just asymptotically,

\[
\boxed{
\sum_{a\in H}\mu_a(c)^2
=\frac12\left(\frac{Z_D(2c)}{Z_D(c)^2}-1\right).
}
\tag{2.2}
\]

Using the already-proved self-averaging simultaneously at the two fixed parameters `c` and `2c`,

\[
\frac{Z_D(2c)}{Z_D(c)^2}
\to_{\mathbb P}
\exp\left(\frac{(2c)^2-2c^2}{32}\right)
=e^{c^2/16}.
\]

Therefore

\[
\boxed{
\sum_{a\in H}\mu_a(c)^2
\to_{\mathbb P}
\frac12\big(e^{c^2/16}-1\big).
}
\tag{2.3}
\]

At the target `c=4`,

\[
\boxed{
\sum_{a\in H}\mu_a(4)^2
\to_{\mathbb P}\frac{e-1}{2}.
}
\tag{2.4}
\]

This is a useful exact replacement for trying to estimate every Fourier coefficient separately: the entire nonzero Fourier energy of the positive Gibbs density is order one and is explicitly pinned by the collision probability.

---

# 3. New coordinate-anisotropy theorem at the sharp scale

Define

\[
A_D(c):=\sum_{a\in D}\big(\mu_a(c)-\bar\mu_D(c)\big)^2.
\]

Then

\[
A_D(c)
=\sum_{a\in D}\mu_a(c)^2-|D|\bar\mu_D(c)^2
\le
\sum_{a\in H}\mu_a(c)^2-|D|\bar\mu_D(c)^2.
\tag{3.1}
\]

The inherited aggregate-moment theorem and `|D|/n\to 1/4` give

\[
|D|\bar\mu_D(c)^2
\to_{\mathbb P}\frac{c^2}{64}.
\tag{3.2}
\]

Combining (2.3) and (3.2),

\[
\boxed{
\limsup_{n\to\infty}^{\mathbb P}A_D(c)
\le
\frac12\big(e^{c^2/16}-1\big)-\frac{c^2}{64}.
}
\tag{3.3}
\]

Here `limsup^P X_n <= L` means that for every `epsilon>0`, `P(X_n>L+epsilon)->0`.

In particular, at `c=4`,

\[
\boxed{
A_D(4)\le \frac{2e-3}{4}+o_{\mathbb P}(1)
=0.6091409\ldots+o_{\mathbb P}(1).
}
\tag{3.4}
\]

Thus the requested nontrivial anisotropy bound is proved:

\[
\boxed{A_D(4)=O_{\mathbb P}(1).}
\]

More directly, define the target residual vector on selected frequencies

\[
r_a:=\mu_a(4)+\frac1{\sqrt n},\qquad a\in D.
\]

Since

\[
\sum_{a\in D}r_a^2
=A_D(4)+|D|\left(\bar\mu_D(4)+\frac1{\sqrt n}\right)^2
\]

and the second term is `o_P(1)`, (3.4) yields

\[
\boxed{
\|r\|_2^2\le\frac{2e-3}{4}+o_{\mathbb P}(1),
\qquad
\|r\|_2\le0.780475\ldots+o_{\mathbb P}(1).
}
\tag{3.5}
\]

This is genuine movement of the coordinatewise obligation: the target moment vector is now rigorously within a **dimension-free Euclidean distance** of the positive Gibbs moment vector. It is not yet `o(1)`, so it does not by itself give an exact certificate.

A useful corollary is a sparse-large-error census. For every deterministic `u_n>0`,

\[
\#\{a\in D:|r_a|>u_n\}
\le\frac{(2e-3)/4+o_{\mathbb P}(1)}{u_n^2}.
\tag{3.6}
\]

For example, only `O_P(sqrt(n))` selected coordinates can have error larger than `n^{-1/4}`. This is not the final `n^{-1/2}` control, but it may be useful for a two-stage correction separating a small exceptional set from the bulk.

---

# 4. New quantitative covariance floor at the Gibbs point

The second obligation is a lower bound on

\[
\Sigma_D(\lambda)
=\operatorname{Cov}_{p_\lambda}(\Phi_D),
\qquad
\Phi_D(j)=(\cos(2\pi aj/n))_{a\in D},
\]

near

\[
\lambda_0=-\frac4{\sqrt n}\mathbf1_D.
\]

A constant lower bound is still open, but one can prove a nontrivial full-dimensional floor with polynomially small failure probability.

Let `U_*` be the uniform law on `Z_n\setminus{0}`. For `a,b\in H`, Fourier orthogonality gives

\[
\mathbb E_{U_*}c_a=-\frac1{n-1},
\]

and

\[
\mathbb E_{U_*}[c_ac_b]
=\frac{(n/2)\mathbf1_{a=b}-1}{n-1}.
\]

Therefore, on the selected coordinate set `D`,

\[
\operatorname{Cov}_{U_*}(\Phi_D)
=
\frac{n}{2(n-1)}I
-
\frac{n}{(n-1)^2}J.
\tag{4.1}
\]

Its transverse eigenvalue is `n/[2(n-1)]`; its all-ones eigenvalue is

\[
\frac{n}{2(n-1)}-rac{n|D|}{(n-1)^2}
=
\frac{n((n-1)/2-|D|)}{(n-1)^2}.
\tag{4.2}
\]

Hence on the overwhelmingly likely event

\[
|D|\le\frac{3(n-1)}8,
\]

we have

\[
\lambda_{\min}(\operatorname{Cov}_{U_*}(\Phi_D))
\ge\frac{n}{8(n-1)}.
\tag{4.3}
\]

Now write `p_0=p_{D,4}` and

\[
q_*(D):=\min_{j\ne0}np_0(j)
=\frac{\exp[-4\max_{j\ne0}S_D(j)/\sqrt n]}{Z_D(4)}.
\tag{4.4}
\]

For any vector `x\in R^D`, putting `f_x(j)=x\cdot\Phi_D(j)` and using the variational characterization of variance,

\[
\begin{aligned}
x^T\Sigma_D(\lambda_0)x
&=\min_b\sum_jp_0(j)(f_x(j)-b)^2\\
&\ge \frac{q_*}{n}\min_b\sum_{j\ne0}(f_x(j)-b)^2\\
&=q_*\frac{n-1}{n}\operatorname{Var}_{U_*}(f_x).
\end{aligned}
\]

Combining with (4.3),

\[
\boxed{
\lambda_{\min}\Sigma_D(\lambda_0)\ge\frac{q_*(D)}8
}
\tag{4.5}
\]

on `|D|<=3(n-1)/8`.

It remains to lower-bound `q_*`. For each fixed nonzero `j`,

\[
\mathbb E_D S_D(j)=-\frac14,
\qquad
\sum_{a\in H}c_a(j)^2=\frac{n-2}{4}.
\]

Hoeffding therefore gives

\[
\mathbb P\left(
S_D(j)+\frac14\ge t
\right)
\le
\exp\left(-\frac{8t^2}{n-2}\right).
\tag{4.6}
\]

Taking

\[
t=\frac12\sqrt{(n-2)\log n}
\]

and union-bounding over `j\ne0`,

\[
\mathbb P\left(
\max_{j\ne0}S_D(j)>-\frac14+\frac12\sqrt{(n-2)\log n}
\right)
\le\frac1n.
\tag{4.7}
\]

The inherited partition theorem has `Var Z_D(4)=O(1/n)` and `E Z_D(4)->e^{1/2}`, so Chebyshev yields

\[
\mathbb P\big(Z_D(4)>2e^{1/2}\big)=O(1/n).
\tag{4.8}
\]

The binomial size event in (4.3) fails with probability `e^{-Omega(n)}`. Thus, with probability `1-O(1/n)`,

\[
q_*(D)
\ge
\frac{e^{-2\sqrt{\log n}}}{2e^{1/2}}
\]

for all sufficiently large prime `n`, and hence

\[
\boxed{
\lambda_{\min}\Sigma_D(\lambda_0)
\ge
\frac{e^{-2\sqrt{\log n}}}{16e^{1/2}}
}
\tag{4.9}
\]

with failure probability `O(1/n)`.

This is much weaker than the desired constant transversality, but it is a rigorous **full-dimensional** covariance lower bound at the correct Gibbs point, with a failure probability already far below the expectation-transfer threshold `o(1/sqrt(log n))`.

---

# 5. Tube extension: exact stability under l1-bounded parameter corrections

The covariance floor extends deterministically to an `l1` parameter tube.

Let `lambda=lambda_0+h`. Since every feature coordinate lies in `[-1,1]`,

\[
|h\cdot\Phi_D(j)|\le\|h\|_1.
\]

If `\|h\|_1\le\rho`, then

\[
\frac{p_{\lambda}(j)}{p_{\lambda_0}(j)}
=\frac{e^{h\cdot\Phi_D(j)}}{\mathbb E_{p_{\lambda_0}}e^{h\cdot\Phi_D}}
\ge e^{-2\rho}.
\]

For every `x`, again using `Var_p(f)=min_b E_p(f-b)^2`,

\[
x^T\Sigma_D(\lambda)x
\ge e^{-2\rho}x^T\Sigma_D(\lambda_0)x.
\]

Therefore

\[
\boxed{
\inf_{\|\lambda-\lambda_0\|_1\le\rho}
\lambda_{\min}\Sigma_D(\lambda)
\ge
 e^{-2\rho}\lambda_{\min}\Sigma_D(\lambda_0).
}
\tag{5.1}
\]

Combining with (4.9), with failure `O(1/n)`,

\[
\boxed{
\inf_{\|\lambda-\lambda_0\|_1\le\rho}
\lambda_{\min}\Sigma_D(\lambda)
\ge
\frac{e^{-2\rho-2\sqrt{\log n}}}{16e^{1/2}}.
}
\tag{5.2}
\]

This is a genuine tube theorem, but in the wrong quantitative regime for a direct Newton closure: (3.5) only gives an `O(1)` Euclidean residual, while the inverse of (4.9) is `e^{2sqrt(log n)}`. The resulting worst-case correction estimate is too large, and converting an `l2` correction to the required `l1` tube loses another `sqrt(n)`.

So the new mathematics identifies the next obstruction more sharply: **the issue is no longer whether the Hessian is singular; it is whether the source-coupled correction direction enjoys much better anti-concentration than the worst-case nonzero-site density floor.**

---

# 6. Fixed full-source metric and intermediate obligation ledger

Full-source P07 theorem remains unchanged:

\[
\sqrt n\le \mathbb E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]

No sharp-constant closure is claimed.

Intermediate obligations now read:

1. **Positive Gibbs reaches average target radius:** PROVED previously.
2. **Selected-coordinate anisotropy `O_P(1)`: PROVED here**, with explicit ceiling `(2e-3)/4+o_P(1)`.
3. **Target residual has dimension-free l2 norm:** PROVED here, `||r||_2<=0.780475...+o_P(1)`.
4. **Full covariance is strictly nondegenerate at the Gibbs point:** PROVED here at scale `exp(-2sqrt(log n))`, failure `O(1/n)`.
5. **Covariance lower bound on a correction tube:** PROVED here for fixed `l1` radius, with the same subpolynomial floor up to `e^{-2rho}`.
6. **Constant-order transversality / source-coupled Newton control:** OPEN and now the decisive gap.
7. **Composite odd `n`:** OPEN; all new Fourier/Gibbs statements in this complementary line remain prime-order until a real gcd/resonance analysis is supplied.

---

# 7. Exact probabilistic estimate sufficient for the expectation theorem

A future exact-certificate theorem does **not** need exponentially small failure probability. It is enough to prove an event `Good_n` on which a positive distribution has all selected moments

\[
\mu_a=-(1+o(1))/\sqrt n
\]

(or the corresponding source-normalized exact corrected certificate), with

\[
q_n:=\mathbb P(Good_n^c)=o(1/\sqrt{\log n}).
\tag{7.1}
\]

Indeed the primary random-circulant paper supplies a fallback upper bound of order

\[
1+4\sqrt{n\log n}
\]

outside an event of probability at most `2/n`. Therefore the contribution of `Good_n^c` on the fallback event is

\[
O(q_n\sqrt{n\log n})=o(\sqrt n),
\]

and the `2/n` exceptional contribution is `o(sqrt(n))` even under the trivial bound `theta<=n`.

Thus the next transversality theorem should be engineered to reach (7.1), not an unnecessarily stronger tail target.

---

# 8. Next attack

The cleanest next route is now **source-coupled rather than worst-case Hessian control**.

Let

\[
r=\mu(\lambda_0)+n^{-1/2}\mathbf1_D,
\qquad
h_N=-\Sigma_D(\lambda_0)^{-1}r.
\]

A sufficient next lemma is not merely `lambda_min Sigma >= constant`. It is enough to prove, with failure `o(1/sqrt(log n))`, that the *specific Newton direction* satisfies simultaneously

\[
\max_j|h_N\cdot\Phi_D(j)|=O(1),
\tag{8.1}
\]

and

\[
\|\mu(\lambda_0+h_N)+n^{-1/2}\mathbf1_D\|_2=o(1),
\tag{8.2}
\]

with the segment `lambda_0+t h_N` retaining a constant or at least sufficiently strong covariance floor. Equation (8.1) would replace the disastrous generic `||h||_1` comparison by a bounded **actual log-density distortion**, which is exactly what the Gibbs geometry needs.

The Parseval identity (2.2) suggests attacking (8.1) through a two-replica / leave-one-frequency expansion for the source-coupled pair `(r,Sigma^{-1}r)` rather than through a uniform minimum-eigenvalue theorem over all directions.

A second, potentially compatible route uses (3.6): correct the `O_P(sqrt(n))` coordinates above the `n^{-1/4}` error scale separately, then prove a bulk covariance estimate for the remaining coordinates. Any such split must be proved asymptotically; finite SDP experiments may only suggest the threshold.

No repeated partition-function proof should be done next unless it is strengthened specifically to control the source-coupled Newton direction.

---

## ledger_delta

```yaml
ledger_delta:
  native_task_id: "6aa7b53b0858819196d923203522c996"
  role: "P06 complementary P07 Gibbs/transversality"
  input_master: "aac80d8ab5a7c0d5ce7dc447f8a7ed9a60fb7540"
  p06_source_status: "KNOWN"
  p06_metric: "U_ER^cert"
  p06_metric_before: 1
  p06_metric_after: 1
  p07_source_status: "OPEN / PARTIAL"
  p07_full_bound_before: "sqrt(n) <= E theta <= C sqrt(n log log n)"
  p07_full_bound_after: "unchanged"
  new_result_1: "exact total Gibbs Fourier-energy identity via Parseval and collision probability"
  new_result_2: "A_D(4) <= (2e-3)/4 + o_P(1)"
  new_result_3: "target selected-moment residual l2 <= 0.780475... + o_P(1)"
  new_result_4: "lambda_min Sigma(lambda0) >= exp(-2 sqrt(log n))/(16 e^(1/2)) with failure O(1/n)"
  new_result_5: "l1 tube covariance floor loses only factor exp(-2 rho)"
  prime_restriction: true
  mathematical_status: "PROVED PARTIAL"
  publication_novelty: "UNVERIFIED"
  next_attack: "source-coupled Newton direction anti-concentration / bounded actual log-density distortion"
```
