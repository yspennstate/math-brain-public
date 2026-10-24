Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but authenticated completed-run model/reasoning telemetry is unavailable, so I do not claim otherwise.**

# P06 complementary P07 iteration — vanishing-tilt initial decrement and transverse-skew reduction

Status: **P06 SOURCE KNOWN / no novelty claim for Conjecture 17. P07 OPEN / PROVED PARTIAL new mathematics; publication novelty UNVERIFIED.**

Native role preserved: `6aa7b53b0858819196d923203522c996`.  
Captured pre-write `master`: `b77247874fa28680ca4aa15ff694dd22dd33b763`.  
No P07-A/P07-B canonical claim, peer report, or historical artifact is modified.

The full-source random-circulant bound remains

\[
\sqrt n\le \mathbf E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]

Thus the source headline metric does **not** move in this run. The movement is on the square-Newton obligation ledger: for every fixed source-sufficient slack `epsilon>0`, the missing initial Newton-decrement margin is now proved with failure far smaller than the `o(1/sqrt(log n))` required for expectation transfer. The remaining obstruction is entirely the **transverse** part of the square-Newton third-cumulant vector.

No finite SDP computation is used.

---

## 1. Inherited positive square-Newton criterion

Let `p` be a law on a finite set, `Phi` a feature vector, `t` a target moment vector,

\[
\mu=\mathbf E_p\Phi,\qquad r=\mu-t,\qquad
\Sigma=\operatorname{Cov}_p(\Phi),
\]

and

\[
h=-\Sigma^{-1}r,\qquad g=h^T(\Phi-\mu),\qquad
\nu^2=\mathbf E_pg^2=r^T\Sigma^{-1}r.
\]

The previous run proved that the positive square update

\[
p_\alpha^+\propto p(1+\alpha g)^2
\]

has an exact residual formula, and that if `nu^2<1` then the choice

\[
\alpha_*={1\over1+\sqrt{1-\nu^2}}
\]

cancels the old residual exactly, leaving only a third-cumulant vector

\[
\tau=\mathbf E_p[(\Phi-\mu)g^2].
\]

With

\[
\Gamma={\|\tau\|_{\Sigma^{-1}}\over \nu^2},\qquad
A={\Gamma\nu\over2(1+\sqrt{1-\nu^2})},
\]

a covariance-regularized square step contracts whenever `A<1/2`.

The assigned next attack was to prove an initial fixed margin `nu_0^2<=1-c_epsilon` and then control `A_0`.

The fixed-`c` Gibbs point is not needed for the first half. A more favorable seed is a **vanishing tilt that still kills the singular time point `j=0`**.

---

# 2. Source setup and the vanishing-tilt seed

Let `n` be odd and

\[
H=\{1,\ldots,(n-1)/2\}.
\]

Let `(xi_a)_{a in H}` be independent Bernoulli-`1/2` variables and

\[
D=\{a\in H:xi_a=1\},\qquad M=|D|.
\]

For `j in Z_n`, write

\[
\phi_a(j)=\cos(2\pi aj/n),\qquad
\Phi_D(j)=(\phi_a(j))_{a\in D},
\]

and

\[
S_D(j)=\sum_{a\in D}\phi_a(j).
\]

Fix `epsilon>0` and put

\[
d={1\over1+\epsilon}\in(0,1),\qquad
 t=-{d\over\sqrt n}{\bf1}_D.
\tag{2.1}
\]

Exact feasibility of (2.1) is already source-sufficient because it gives

\[
\vartheta(G_D)\le1+(1+\epsilon)\sqrt n.
\]

Now choose the deterministic vanishing tilt

\[
\boxed{c_n=n^{-1/3}.}
\tag{2.2}
\]

Define

\[
p_n(j)=
{\exp(-c_nS_D(j)/\sqrt n)\over
 \sum_{k\in\mathbb Z_n}\exp(-c_nS_D(k)/\sqrt n)}.
\tag{2.3}
\]

Let `mu_n`, `Sigma_n`, `r_n`, `h_n`, `g_n`, and `nu_n` be the moment, covariance, target residual, Newton vector, Newton score, and Newton decrement for `(p_n,Phi_D,t)`.

The role of (2.2) is two-sided:

- at the origin, `S_D(0)=M=Theta(n)`, so `c_nS_D(0)/sqrt(n)=Theta(n^{1/6})` and the singular point is exponentially suppressed;
- uniformly over every nonzero time coordinate, `S_D(j)=O(sqrt(n log n))` with overwhelming probability, so the Gibbs density differs from uniform-on-nonzero-points by only `o(1)` multiplicatively.

That produces an explicit limiting covariance whose smallest relevant eigenvalue is constant, and the target slack `d<1` then gives the required decrement margin.

---

# 3. Exact nonzero-uniform covariance

Let `u_*` denote the uniform law on

\[
J_*:=\mathbb Z_n\setminus\{0\}.
\]

The usual root-of-unity identities, valid for every odd `n`, give for every `a in H`

\[
\mathbf E_{u_*}\phi_a=-{1\over n-1}.
\tag{3.1}
\]

For `a=b`,

\[
\mathbf E_{u_*}\phi_a^2={n-2\over2(n-1)},
\]

while for distinct `a,b in H`, since `a not congruent +/-b mod n`,

\[
\mathbf E_{u_*}\phi_a\phi_b=-{1\over n-1}.
\]

Therefore the covariance on the selected coordinates is exactly

\[
\boxed{
\Sigma_*={n\over2(n-1)}I_M-{n\over(n-1)^2}J_M.
}
\tag{3.2}
\]

Its eigenvalues are

\[
\lambda_\perp={n\over2(n-1)}
\tag{3.3}
\]

on `1_D^perp`, and

\[
\boxed{
\lambda_\parallel
={n\bigl((n-1)/2-M\bigr)\over(n-1)^2}
}
\tag{3.4}
\]

on the span of `1_D`.

On the source-typical event `M/n->1/4`,

\[
\lambda_\perp\to{1\over2},\qquad
\lambda_\parallel\to{1\over4}.
\tag{3.5}
\]

This `1/4` longitudinal eigenvalue is exactly the constant that makes the slack target critical: the limiting decrement will be `d^2`, not `d^2/2`.

---

# 4. A strong event on which the Gibbs law is uniformly bulk-flat

For every `j!=0`,

\[
\mathbf E_D S_D(j)
={1\over2}\sum_{a\in H}\cos(2\pi aj/n)
=-{1\over4},
\tag{4.1}
\]

and

\[
\sum_{a\in H}\cos^2(2\pi aj/n)={n-2\over4}.
\tag{4.2}
\]

Hoeffding therefore gives

\[
\Pr_D\left(
|S_D(j)+1/4|>\sqrt{n\log n}
\right)
\le 2n^{-8+o(1)}.
\]

A union bound over `j!=0` gives

\[
\Pr_D\left(
\max_{j\ne0}|S_D(j)+1/4|>\sqrt{n\log n}
\right)
=O(n^{-7}).
\tag{4.3}
\]

Also, by a standard binomial Hoeffding bound,

\[
\Pr_D\left(
\left|M-{n-1\over4}\right|>n^{2/3}
\right)
\le 2e^{-\Omega(n^{1/3})}.
\tag{4.4}
\]

Let `E_n` be the intersection of the events in (4.3)-(4.4). Then

\[
\boxed{
\Pr(E_n^c)=O(n^{-7})+e^{-\Omega(n^{1/3})}.
}
\tag{4.5}
\]

On `E_n`, put

\[
\delta_n:=n^{-1/3}\sqrt{\log n}.
\]

For all `j!=0`,

\[
\left|{c_nS_D(j)\over\sqrt n}\right|
=O(\delta_n),
\tag{4.6}
\]

whereas at the origin

\[
{c_nS_D(0)\over\sqrt n}
={n^{-1/3}M\over\sqrt n}
\ge {1\over8}n^{1/6}
\tag{4.7}
\]

for all sufficiently large `n` on `E_n`.

Hence the origin mass satisfies

\[
p_n(0)\le {2\over n}e^{-n^{1/6}/8},
\tag{4.8}
\]

while, after conditioning `p_n` on `J_*`, its density `q_n` relative to `u_*` obeys uniformly

\[
\boxed{
{q_n(j)\over u_*(j)}=1+O(\delta_n),\qquad j\ne0.
}
\tag{4.9}
\]

The constants here are deterministic on `E_n`.

---

# 5. Covariance equivalence in Loewner order

The variance identity

\[
\operatorname{Var}_q(Y)=\min_a\mathbf E_q(Y-a)^2
\]

turns the pointwise density comparison (4.9) directly into a matrix comparison. For every vector `v in R^D`, on `E_n`,

\[
(1-O(\delta_n))v^T\Sigma_*v
\le v^T\Sigma_{q_n}v
\le(1+O(\delta_n))v^T\Sigma_*v.
\tag{5.1}
\]

Writing `p_n=(1-p_n(0))q_n+p_n(0)delta_0`, the covariance-of-mixtures formula adds only a positive semidefinite between-means term. Its operator norm is at most

\[
O(p_n(0)M)=e^{-\Omega(n^{1/6})}.
\]

Consequently

\[
\boxed{
(1-O(\delta_n))\Sigma_*
\preceq \Sigma_n
\preceq(1+O(\delta_n))\Sigma_*.
}
\tag{5.2}
\]

On `E_n`, (3.4) and `M=(n-1)/4+O(n^{2/3})` give

\[
\lambda_{\min}(\Sigma_*)\ge {1\over5}
\]

for all sufficiently large `n`. Hence both `Sigma_n` and `Sigma_*` are uniformly invertible and

\[
\boxed{
\|\Sigma_n^{-1}-\Sigma_*^{-1}\|_{op}=O(\delta_n).
}
\tag{5.3}
\]

This is much stronger, for this vanishing-tilt seed, than the earlier fixed-`c` generic floor `exp[-(c/2)sqrt(log n)]`.

---

# 6. The Gibbs mean moves only `O(c_n)` in Euclidean norm

Let `q_s` be the nonzero-point Gibbs law with parameter `s in [0,c_n]`:

\[
q_s(j)\propto \exp(-sS_D(j)/\sqrt n),\qquad j\ne0.
\]

By (4.6), every `q_s` has density ratio `1+O(delta_n)` relative to `u_*`, uniformly in `s<=c_n`. Thus its covariance operator is uniformly `O(1)`.

If `mu(s)=E_{q_s}Phi_D`, exponential-family differentiation gives

\[
{d\mu(s)\over ds}
=-{1\over\sqrt n}\Sigma_{q_s}{\bf1}_D.
\tag{6.1}
\]

Since `||1_D||_2=sqrt(M)=O(sqrt n)`, (6.1) yields

\[
\left\|{d\mu(s)\over ds}\right\|_2=O(1).
\]

Integrating from `0` to `c_n`, using

\[
\mu(0)=-{1\over n-1}{\bf1}_D,
\]

gives

\[
\boxed{
\|\mu(c_n)\|_2=O(c_n)+O(n^{-1/2})=O(n^{-1/3}).
}
\tag{6.2}
\]

Adding back the exponentially small origin mass changes the mean by `o(n^{-100})` on `E_n`, so (6.2) also holds for the full `p_n` mean `mu_n`.

---

# 7. Main theorem: the initial Newton decrement converges to `d^2`

Set

\[
x_n={d\over\sqrt n}{\bf1}_D,
\qquad r_n=x_n+\mu_n.
\tag{7.1}
\]

From (6.2),

\[
\|r_n-x_n\|_2=O(n^{-1/3}).
\tag{7.2}
\]

Because `x_n` is exactly longitudinal for `Sigma_*`, (3.4) gives

\[
\begin{aligned}
x_n^T\Sigma_*^{-1}x_n
&={d^2\over n}{M\over\lambda_\parallel}\\
&=
 d^2\,{M(n-1)^2\over
 n^2((n-1)/2-M)}.
\end{aligned}
\tag{7.3}
\]

On `E_n`, `M/n=1/4+O(n^{-1/3})`, so

\[
\boxed{
x_n^T\Sigma_*^{-1}x_n=d^2+O(n^{-1/3}).}
\tag{7.4}
\]

Using the uniform inverse bound, (5.3), and (7.2),

\[
\begin{aligned}
\nu_n^2
&=r_n^T\Sigma_n^{-1}r_n\\
&=x_n^T\Sigma_*^{-1}x_n+O(\delta_n)+O(c_n)\\
&=d^2+O(n^{-1/3}\sqrt{\log n}).
\end{aligned}
\tag{7.5}
\]

Therefore:

## Theorem 7.1 — source-sufficient initial decrement margin

For every fixed `epsilon>0`, with `d=(1+epsilon)^{-1}` and the vanishing-tilt seed `c_n=n^{-1/3}`,

\[
\boxed{
\nu_n^2=d^2+O(n^{-1/3}\sqrt{\log n})
}
\tag{7.6}
\]

outside an event of probability

\[
\boxed{
O(n^{-7})+e^{-\Omega(n^{1/3})}.
}
\tag{7.7}
\]

In particular, putting

\[
\kappa_\epsilon={1-d^2\over2}>0,
\]

for all sufficiently large `n`,

\[
\boxed{
\nu_n^2\le1-\kappa_\epsilon
}
\tag{7.8}
\]

with the failure bound (7.7).

Since (7.7) is much smaller than `o(1/sqrt(log n))`, the **first** probabilistic condition requested by the square-Newton source-closing route is now proved at every fixed source-sufficient slack.

This is the main mathematical progress of the run.

---

# 8. The actual Newton direction becomes asymptotically flat

Define the explicit nonzero-uniform Newton vector

\[
h_*=-\Sigma_*^{-1}x_n
=-{d\over\sqrt n\,\lambda_\parallel}{\bf1}_D.
\tag{8.1}
\]

By (5.3), (6.2), and `||x_n||=O(1)`, the actual Newton vector obeys

\[
\boxed{
\|h_n-h_*\|_2
=O(n^{-1/3}\sqrt{\log n}).
}
\tag{8.2}
\]

Moreover

\[
{d\over\sqrt n\,\lambda_\parallel}
={4d+o(1)\over\sqrt n}.
\tag{8.3}
\]

Thus the actual source-coupled Newton score is asymptotically the scalar bulk score

\[
-4d\,{S_D(J)-\mathbf E S_D(J)\over\sqrt n}.
\]

The approximation is strong enough in `L^4`, not merely in `L^2`. Indeed for any coefficient error `e`, on the nonzero set

\[
\|e^T\Phi_D\|_\infty\le \sqrt M\|e\|_2,
\]

while its second moment is `O(||e||_2^2)`. Hence

\[
\mathbf E|e^T\Phi_D|^4
\le O(n\|e\|_2^4).
\tag{8.4}
\]

With `e=h_n-h_*` and (8.2),

\[
n\|e\|_2^4
=O(n^{-1/3}(\log n)^2)=o(1).
\tag{8.5}
\]

The exponentially small origin mass is harmless. Therefore the actual Newton score is `o_P(1)` away in `L^4(p_n)` from the flat scalar score.

---

# 9. Bulk Gaussian law, Newton-score kurtosis, and longitudinal skew

The earlier partition proof discarded the origin because a positive fixed Gibbs tilt suppresses it. Here it is useful to isolate the bulk explicitly.

For fixed real `s`, define the **nonzero empirical mgf**

\[
A_D(s)={1\over n-1}\sum_{j\ne0}
\exp\left(-{sS_D(j)\over\sqrt n}\right).
\tag{9.1}
\]

The same first/second-moment calculation used in the earlier partition lemma works for every real `s` once `j=0` is excluded: for generic nonzero pairs `j,k` with `k!=+/-j`, the exact root sums give factorization up to relative `O_s(1/n)`, and only `O(n)` nongeneric pairs remain. Hence

\[
\boxed{
A_D(s)\xrightarrow{P}e^{s^2/32},
\qquad
\operatorname{Var}_D A_D(s)=O_s(n^{-1}).
}
\tag{9.2}
\]

This argument uses only odd-order root orthogonality; primality is unnecessary for (9.2).

Consequently the empirical bulk law of

\[
Y_D(j)={S_D(j)\over\sqrt n},\qquad j\ne0,
\]
converges in probability, with exponential uniform integrability on every fixed compact mgf interval, to

\[
\boxed{N(0,1/16).}
\tag{9.3}
\]

Because `p_n` is uniformly `1+o(1)` relative to `u_*` on the nonzero set, (9.3) is unchanged under `p_n`. Combining (8.2)-(8.5) with (9.3) gives

\[
\boxed{
\mathbf E_{p_n}g_n^2\to d^2,
\quad
\mathbf E_{p_n}g_n^3\to0,
\quad
\mathbf E_{p_n}g_n^4\to3d^4
}
\tag{9.4}
\]

in probability. The first limit is consistent with the stronger quantified decrement theorem (7.6).

Therefore the actual-score kurtosis satisfies

\[
\boxed{K_n={\mathbf E g_n^4\over(\mathbf E g_n^2)^2}\xrightarrow{P}3.}
\tag{9.5}
\]

This has two consequences.

First, the generic kurtosis shortcut

\[
\sqrt K\,\nu<1+\sqrt{1-\nu^2}
\]

is enough for a strict first square-Newton contraction only when, asymptotically,

\[
\sqrt3\,d<1+\sqrt{1-d^2},
\]

i.e.

\[
\boxed{d<\sqrt3/2}
\tag{9.6}
\]

or `epsilon>2/sqrt(3)-1≈0.1547`. Thus the **kurtosis bound alone cannot close the sharp source limit `epsilon downarrow0`**. That route is now rigorously diagnosed rather than merely suspected.

Second, the scalar/longitudinal part of the true third-cumulant obstruction vanishes. Since

\[
h_n^T\tau_n=\mathbf E g_n^3,
\]
(9.4) gives

\[
\boxed{h_n^T\tau_n=o_P(1).}
\tag{9.7}
\]

Equivalently, after whitening by `Sigma_n`, the normalized skew vector is asymptotically orthogonal to the Newton direction. The remaining obstruction to `A_n<1/2` is therefore **transverse skew energy**, not scalar skewness of the Newton score.

This is a sharper target than the previous undifferentiated `Gamma` bound.

---

# 10. What moved and what did not

## Fixed full-source bound

Unchanged:

\[
\sqrt n\le \mathbf E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]

No full P07 solution is claimed.

## Intermediate obligation ledger

1. **Initial fixed-slack Newton margin**  
   Before: open.  
   After: **PROVED** for every fixed `epsilon>0`, with
   \[
   \nu_n^2=d^2+O(n^{-1/3}\sqrt{\log n})<1-\kappa_\epsilon
   \]
   outside probability `O(n^-7)+exp[-Omega(n^(1/3))]`.

2. **Actual Newton direction**  
   Before: uncontrolled high-dimensional inverse-covariance direction.  
   After: **PROVED** `l2`-flat:
   \[
   h_n=-{4d+o(1)\over\sqrt n}{\bf1}_D
   +O_{l2}(n^{-1/3}\sqrt{\log n}).
   \]

3. **Actual-score fourth moment**  
   Before: only the generic inequality `Gamma<=sqrt(K)`.  
   After: **PROVED PARTIAL**
   \[
   K_n\to_P3.
   \]
   This proves contraction only for the coarse-slack range `d<sqrt(3)/2`, and also proves that the kurtosis shortcut by itself cannot reach arbitrarily small `epsilon`.

4. **Third-cumulant geometry**  
   Before: full `tau` unknown.  
   After: its longitudinal component vanishes:
   \[
   h_n^T\tau_n=o_P(1).
   \]
   The source-closing obstruction is now the transverse norm
   \[
   \|\Pi_{h_n}^{\perp}\Sigma_n^{-1/2}\tau_n\|_2.
   \]

5. **Prime restriction**  
   The new vanishing-tilt decrement and bulk-mgf lemmas use only odd cyclic root orthogonality, not primality. This removes the prime restriction for these components only. It does **not** by itself remove any prime restriction in earlier fixed-`c` arguments or prove the full source statement for every order.

---

# 11. Remaining gap and next attack

For arbitrary fixed `epsilon>0`, the decrement condition is no longer the problem. The remaining source-coupled quantity is

\[
\Gamma_n^2
={\tau_n^T\Sigma_n^{-1}\tau_n\over\nu_n^4}.
\]

The scalar projection along the Newton direction is `o_P(1)` by (9.7). Since `Sigma_n` is asymptotic to the explicit compound-symmetry matrix `Sigma_*`, the next attack should compute the **transverse Fourier energy of `g_n^2`**.

At the vanishing tilt,

\[
g_n(j)=-4d\,{S_D(j)-\mathbf E S_D\over\sqrt n}+o_{L^4}(1).
\]

Thus, up to a proved negligible error, `tau_n` is the selected-frequency cosine transform of the centered square

\[
{16d^2\over n}
\left[(S_D-\mathbf ES_D)^2-\mathbf E(S_D-\mathbf ES_D)^2\right].
\]

The decisive next theorem is a same-mask four-replica/additive-convolution estimate for the selected half of this square-energy. The natural target suggested by Parseval is

\[
\Gamma_n^2\le1+o_P(1)
\]

with failure `o(1/sqrt(log n))`. If proved, then for every fixed `d<1`,

\[
A_n
\le {d+o(1)\over2(1+\sqrt{1-d^2})}<1/2,
\]
which would establish a strict first covariance-regularized square-Newton contraction at **every** source-sufficient slack. The subsequent task would be to propagate that transverse-skew bound through the square/mixing update.

The required combinatorial object is explicit: for the symmetric frequency set `A=+/-D`, analyze fluctuations of the convolution counts

\[
N_a=|\{(b,c)\in A^2:b+c=a\}|,
\]
centered by the nonzero-point subtraction. A variance/concentration theorem for the aggregate selected energy of these `N_a` is preferable to coordinatewise union bounds.

That is the next mathematical attack. Do not return to a worst-case `max|g|` estimate or generic covariance floor unless the convolution route is proved obstructed.

---

## Result label

**PROVED PARTIAL.** The run proves a source-sufficient initial Newton-decrement margin with strong failure probability at every fixed slack, identifies the asymptotically flat actual Newton direction, proves actual-score kurtosis `K->3`, and removes longitudinal skew. It does **not** yet control the transverse skew norm required for arbitrary-small-slack square-Newton contraction, and therefore does not claim the full P07 conjecture.