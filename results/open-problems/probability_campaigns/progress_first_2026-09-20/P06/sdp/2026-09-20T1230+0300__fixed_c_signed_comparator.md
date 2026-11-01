Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but authenticated completed-run model/reasoning telemetry does not verify GPT-6 maximum, so I do not claim otherwise.**

# P06 complementary P07 iteration — fixed-c signed comparator and an absolute Newton-decrement bound

Status: **P06 SOURCE KNOWN / no novelty claim for Conjecture 17. P07 OPEN / PROVED PARTIAL new mathematics; publication novelty UNVERIFIED.**

Native role preserved: `6aa7b53b0858819196d923203522c996`.

Previous substantive checkpoint: `probability_campaigns/progress_first_2026-09-20/P06/sdp/2026-09-20T1130+0300__growing_degree_coarse_tail.md`, creation commit `017f0a3e351d3f8a76a7a9da3bc15a52794e8997`, readback blob `320e79f90dc84c5850870e4d2e958e7ca8d0d72e`.

The outside P07 source remains Bandeira--Blasiok--Dmitriev--Faure--Kireeva--Kunisky, arXiv:2502.16227. The inherited full-source bound remains

\[
\sqrt n\le \mathbf E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]

No full-source improvement is claimed here.

The previous run isolated **absolute coarse entry** as the missing bridge before the already-proved superlinear tail. This run obtains a source-coupled inverse-covariance estimate for a fixed-`c` Gibbs seed without using a global minimum-eigenvalue bound. The main theorem is

\[
\boxed{\nu_{c_*}^2\le 0.593984649+o_{\mathbf P}(1)}
\]

for the exact sharp target `-1/sqrt(n)` on the selected frequencies, with source-sufficient failure `o(1/sqrt(log n))`. Here

\[
c_*=1.720638836\ldots .
\]

Thus the actual Newton decrement of this explicit positive seed is at most

\[
\boxed{\nu_{c_*}\le0.7707040+o_{\mathbf P}(1).}
\]

This is not yet the absolute coarse basin required by the tail theorem, because the directional skew `Gamma` still has to be controlled. The point is that the difficult inverse covariance has now been bounded in the **actual residual direction** by an explicit signed-comparator argument; the remaining fixed-`c` task is a skew/higher-chaos estimate, not an inverse-eigenvalue problem.

---

# 1. Nonzero cyclic reference law

Assume `n` is odd. Let

\[
\Omega_n=\mathbb Z_n\setminus\{0\}
\]

and let `u_*` be the uniform law on `Omega_n`. Let `H` contain one representative of every pair `+/-a`, `a!=0`, and let `D subset H` be the random selected half-frequency mask. Put `m=|D|` and

\[
\phi_a(j)=\cos(2\pi aj/n),\qquad
\Phi_D(j)=(\phi_a(j))_{a\in D},
\]

\[
S_D(j)=\sum_{a\in D}\phi_a(j),
\qquad
X_D(j)={S_D(j)\over\sqrt n}.
\]

Under `u_*`, root orthogonality gives exactly

\[
\mu_*:=\mathbf E_*\Phi_D
=-{1\over n-1}\mathbf 1_D,
\tag{1.1}
\]

and

\[
\Sigma_*:=\operatorname{Cov}_*(\Phi_D)
={n\over2(n-1)}I
-{n\over(n-1)^2}J.
\tag{1.2}
\]

In particular, the all-ones eigenvalue is

\[
\lambda_{*,\parallel}
={n\over2(n-1)}-{nm\over(n-1)^2}
={n((n-1)-2m)\over2(n-1)^2}.
\tag{1.3}
\]

For the Bernoulli half-mask,

\[
m={n-1\over4}+O_{\mathbf P}(\sqrt n),
\tag{1.4}
\]

so

\[
\lambda_{*,\parallel}={1\over4}+o_{\mathbf P}(1).
\tag{1.5}
\]

The target in this report is the stronger sharp vector

\[
t_n=-{1\over\sqrt n}\mathbf 1_D.
\tag{1.6}
\]

A fixed-slack target `-d/sqrt(n)` with `d<1` is weaker, so a later positive repair to (1.6) is more than enough for every fixed source slack.

---

# 2. The exact signed target comparator

Define

\[
h_*:=\Sigma_*^{-1}(t_n-\mu_*).
\tag{2.1}
\]

Because both vectors on the right are parallel to `1_D`, there is a scalar `kappa_n` such that

\[
h_*=\kappa_n\mathbf 1_D,
\qquad
\kappa_n={-n^{-1/2}+(n-1)^{-1}\over\lambda_{*,\parallel}}.
\tag{2.2}
\]

On the mask-concentration event (1.4),

\[
\sqrt n\,\kappa_n=-4+o(1).
\tag{2.3}
\]

Now define the affine density

\[
L_n(j)
:=1+h_*^T(\Phi_D(j)-\mu_*).
\tag{2.4}
\]

This density is generally signed; positivity is not asserted or needed in the present comparator lemma. By construction,

\[
\mathbf E_*L_n=1
\tag{2.5}
\]

and

\[
\mathbf E_*[L_n\Phi_D]
=\mu_*+\Sigma_*h_*=t_n.
\tag{2.6}
\]

Since `h_*` is parallel to the all-ones vector,

\[
L_n(j)
=1+\kappa_n\left(S_D(j)+{m\over n-1}\right).
\tag{2.7}
\]

Consequently, in every fixed exponential moment,

\[
L_n=1-4X_D+o_{\mathbf P}(1)
\tag{2.8}
\]

in the precise sense used in Section 5 below.

The role of `L_n` is only to supply an exact signed law with the desired selected moments. It will be compared to a positive Gibbs seed.

---

# 3. Fixed-c positive Gibbs seed on the nonzero support

For fixed `c>0`, define

\[
M_D(s)
:={1\over n-1}\sum_{j\ne0}e^{sX_D(j)}
\tag{3.1}
\]

and the positive probability law

\[
p_{D,c}(j)
={1\over n-1}{e^{-cX_D(j)}\over M_D(-c)},
\qquad j\ne0.
\tag{3.2}
\]

The density relative to `u_*` is therefore

\[
f_{D,c}(j)={e^{-cX_D(j)}\over M_D(-c)}.
\tag{3.3}
\]

This law is symmetric under `j -> -j`, has no mass at the exceptional origin, and is a legitimate primal probability law. Excluding the origin is useful here: the old obstruction in `q^2/p` at `j=0` disappears completely, while the selected cosine moment constraints remain meaningful.

Let

\[
\mu_c=\mathbf E_{p_{D,c}}\Phi_D,
\qquad
r_c=\mu_c-t_n,
\qquad
\Sigma_c=\operatorname{Cov}_{p_{D,c}}(\Phi_D).
\tag{3.4}
\]

The actual Newton decrement is

\[
\nu_c^2=r_c^T\Sigma_c^{-1}r_c.
\tag{3.5}
\]

The point of the next lemma is that no lower bound on `lambda_min Sigma_c` is needed.

---

# 4. Exact source-coupled comparator lemma

## Lemma 4.1 — signed target law bounds the actual Newton decrement

Let `p=f u_*` be any strictly positive law on `Omega_n`, and let `L u_*` be any signed normalized law with the exact target moments `t_n`. Define

\[
g={L\over f}-1.
\tag{4.1}
\]

Then

\[
\mathbf E_p g=0,
\qquad
\mathbf E_p[g(\Phi_D-\mu_p)]=t_n-\mu_p=-r_p.
\tag{4.2}
\]

If `g_N=-r_p^T Sigma_p^{-1}(Phi_D-mu_p)` denotes the actual minimum-`L^2(p)` linear Newton score (equivalently `h_N=-Sigma_p^{-1}r_p` and `g_N=h_N^T(Phi_D-mu_p)`), then

\[
\boxed{
\nu_p^2=\mathbf E_p g_N^2\le\mathbf E_p g^2.
}
\tag{4.3}
\]

Moreover,

\[
\mathbf E_p g^2
=\mathbf E_*{L^2\over f}-1.
\tag{4.4}
\]

### Proof

Normalization gives

\[
E_pg=E_*(L-f)=0.
\]

Likewise,

\[
E_p[g\Phi_D]
=E_*[(L-f)\Phi_D]
=t_n-\mu_p.
\]

Because `E_p g=0`, centering `Phi_D` does not change this identity, proving (4.2).

For every centered feature-linear function `ell=v^T(Phi_D-mu_p)`,

\[
\langle g,\ell\rangle_{L^2(p)}
=-v^Tr_p.
\]

The actual Newton score `g_N` has exactly the same inner products with the whole centered feature span. Hence `g-g_N` is orthogonal to that span, while `g_N` belongs to it. Therefore `g_N` is the orthogonal projection of `g` and

\[
\|g_N\|_2^2\le\|g\|_2^2.
\]

Finally,

\[
E_pg^2
=E_*\left[f\left({L\over f}-1\right)^2\right]
=E_*{L^2\over f}-2E_*L+E_*f
=E_*{L^2\over f}-1.
\]

∎

For the Gibbs seed (3.3), (4.4) becomes the exact scalar identity

\[
\boxed{
\nu_c^2
\le
M_D(-c)\,\mathbf E_*\left[e^{cX_D}L_n^2\right]-1.
}
\tag{4.5}
\]

This is the key change from the old generic covariance-floor route: the inverse covariance has disappeared, replaced by scalar exponential moments of the already-studied random trigonometric sum.

---

# 5. Scalar exponential moments with polynomial insertions

The earlier Gibbs reports proved fixed-parameter self-averaging of the partition function. The same two-replica expansion gives the following strengthened version needed here.

## Lemma 5.1 — first two inserted moments

For every fixed real `s` and `k in {0,1,2}`,

\[
{1\over n-1}\sum_{j\ne0}
X_D(j)^k e^{sX_D(j)}
=
{d^k\over ds^k}e^{s^2/32}
+o_{\mathbf P}(1),
\tag{5.1}
\]

and the convergence can be taken outside failure `O_s(n^{-1/2})` after choosing an `n^{-1/4}` error window. In particular the failure is

\[
o(1/\sqrt{\log n}).
\tag{5.2}
\]

### Proof

The `k=0` statement is the fixed-`s` partition self-averaging calculation from the previous Gibbs line, unchanged by removing the single origin point. For `k=1,2`, either insert the factors `X_D` and `X_D^2` directly in the same two-replica expansion, or differentiate the finite exponential sum and apply the same bounded-complex-neighborhood moment estimate. Each insertion changes only a fixed number of collision slots. The disconnected diagrams give the Gaussian derivatives, while every connected two-copy diagram loses one free cyclic parameter, so the variance remains `O_s(1/n)`. Chebyshev with tolerance `n^{-1/4}` gives `O_s(n^{-1/2})` failure. ∎

Explicitly,

\[
M_D(s)=e^{s^2/32}+o_{\mathbf P}(1),
\tag{5.3}
\]

\[
E_*[X_De^{sX_D}]
={s\over16}e^{s^2/32}+o_{\mathbf P}(1),
\tag{5.4}
\]

and

\[
E_*[X_D^2e^{sX_D}]
=\left({1\over16}+{s^2\over256}\right)e^{s^2/32}
+o_{\mathbf P}(1).
\tag{5.5}
\]

Combining (2.3), (2.7) and the mask-size concentration with (5.3)--(5.5) yields

\[
M_D(-c)E_*[e^{cX_D}L_n^2]-1
=
V(c)+o_{\mathbf P}(1),
\tag{5.6}
\]

where

\[
\boxed{
V(c)
=e^{c^2/16}
\left[\left(1-{c\over4}\right)^2+1\right]-1.
}
\tag{5.7}
\]

More generally, if the comparator target is `-d/sqrt(n)`, the same calculation gives

\[
V(c,d)
=e^{c^2/16}
\left[\left(1-{cd\over4}\right)^2+d^2\right]-1.
\tag{5.8}
\]

The report uses `d=1`, because that target is stronger than every fixed source slack.

---

# 6. Optimize the fixed-c comparator

Put

\[
a={c\over4}.
\]

Then

\[
V(c)+1=e^{a^2}\big((1-a)^2+1\big).
\tag{6.1}
\]

Differentiating, the unique positive minimizer satisfies

\[
a\big((1-a)^2+1\big)=1-a,
\tag{6.2}
\]

or equivalently

\[
\boxed{a^3-2a^2+3a-1=0.}
\tag{6.3}
\]

Its real root is

\[
a_*=0.430159709001947\ldots,
\qquad
c_*=4a_*=1.72063883600779\ldots .
\tag{6.4}
\]

At this point

\[
V(c_*)
=0.593984648584427\ldots .
\tag{6.5}
\]

Therefore Lemma 4.1 and Section 5 prove:

## Theorem 6.1 — absolute source-coupled decrement bound

For the nonzero-support fixed-`c_*` Gibbs law and the exact selected-frequency target `t_n=-n^{-1/2}1_D`,

\[
\boxed{
\nu_{c_*}^2
\le0.593984649+o_{\mathbf P}(1),
}
\tag{6.6}
\]

hence

\[
\boxed{
\nu_{c_*}
\le0.7707040+o_{\mathbf P}(1).
}
\tag{6.7}
\]

The exceptional probability can be chosen `O(n^{-1/2})+exp[-Omega(n)]`, and therefore is `o(1/sqrt(log n))`.

This theorem is an actual finite-model high-probability statement. It is not a Gaussian-surrogate assertion and it does not use a generic lower bound on `lambda_min Sigma_c`.

---

# 7. What remains for absolute coarse entry

The old covariance-regularized square lemma uses

\[
A={\Gamma\beta\over2},
\qquad
\beta={\nu\over1+\sqrt{1-\nu^2}}.
\tag{7.1}
\]

At the worst decrement allowed by (6.7),

\[
\beta\le0.4710\ldots,
\tag{7.2}
\]

so an absolute bound approximately

\[
\boxed{\Gamma<2.12}
\tag{7.3}
\]

would already imply `A<1/2` and enter a genuine contracting coarse step. The previous superlinear-tail theorem would then take over after a finite absolute bridge.

Thus this run has reduced the coarse-entry theorem to a **single fixed-c directional-skew estimate**. The difficult inverse-covariance norm of the residual is no longer part of that gap.

---

# 8. Calibrated two-chaos benchmark for the remaining skew

This subsection is a proved calculation **inside the already-calibrated Gaussian/Hermite surrogate**, not yet a finite fixed-c theorem. It is included because it quantifies the available margin for the next attack.

Let `Z,W` be independent standard Gaussians and use the calibrated two-chaos feature pair

\[
X_1=Z,
\qquad
X_2={Z^2-1\over2}+{W\over\sqrt2}.
\tag{8.1}
\]

Under the normalized fixed-c tilt `exp(-aZ-a^2/2)`, write `Y=Z+a`, so `Y,W` are again independent standard Gaussians. The centered covariance of `(X_1,X_2)` is exactly

\[
C_a=
\begin{pmatrix}
1&-a\\
-a&1+a^2
\end{pmatrix},
\qquad
C_a^{-1}=
\begin{pmatrix}
1+a^2&a\\
a&1
\end{pmatrix}.
\tag{8.2}
\]

For the sharp target, the surrogate residual is

\[
r_a=\begin{pmatrix}1-a\\a^2/2\end{pmatrix}.
\tag{8.3}
\]

Hence the surrogate Newton decrement is

\[
\boxed{
\nu_{(2)}^2(a)
=r_a^TC_a^{-1}r_a
={\big(a^2-2a+2\big)^2\over4}.
}
\tag{8.4}
\]

At `a=a_*`,

\[
\nu_{(2)}^2(a_*)
=0.4387194166\ldots,
\qquad
\nu_{(2)}(a_*)=0.6623590\ldots .
\tag{8.5}
\]

The exact two-chaos Newton vector is

\[
h_1={a^3\over2}-a^2+a-1,
\qquad
h_2={a(a-2)\over2}.
\tag{8.6}
\]

A Wick calculation gives

\[
\tau_1=a(a-2)(a-1),
\tag{8.7}
\]

\[
\tau_2=-{3a^4-8a^3+8a-4\over4},
\tag{8.8}
\]

and therefore

\[
\boxed{
\Gamma_{(2)}^2(a)
={
 a^8-8a^7+48a^6-176a^5+344a^4-352a^3+192a^2-64a+16
\over
(a^2-2a+2)^4}.
}
\tag{8.9}
\]

At `a=a_*`,

\[
\Gamma_{(2)}^2=1.769312869\ldots,
\qquad
\Gamma_{(2)}=1.330155205\ldots .
\tag{8.10}
\]

This is comfortably below the finite-model threshold (7.3). Moreover the normalized Gaussian likelihood has Hermite tail beyond order two

\[
\sum_{k\ge3}{a_*^{2k}\over k!}
=e^{a_*^2}-1-a_*^2-{a_*^4\over2}
=0.001106622\ldots .
\tag{8.11}
\]

Its `L^2` size is only

\[
0.033266\ldots .
\tag{8.12}
\]

This does **not** by itself prove the finite fixed-c skew bound, because the selected Fourier projector is fixed and weighted by the Gibbs law. But it shows that the remaining problem is a quantitatively small higher-chaos leakage calculation, not a large-margin guess.

---

# 9. Failed/avoided routes and what they teach

1. **Global minimum eigenvalue.** The earlier bound
   \[
   \lambda_{\min}\Sigma_c\gtrsim e^{-(c/2)\sqrt{\log n}}
   \]
   is far too weak for an absolute coarse decrement. The signed-comparator projection lemma avoids it entirely.

2. **Using the all-site affine signed law.** If the comparator puts its affine mass at `j=0`, then `q^2/p_c` blows up because the Gibbs seed exponentially suppresses the origin. Moving both the seed and comparator to the nonzero support removes this artificial singularity exactly.

3. **Treating the two-chaos benchmark as a proof.** Equation (8.10) is only the calibrated low-chaos limit. The fixed selected projector can carry higher-chaos energy, so the next run must control that leakage with the established collision machinery rather than assuming a fresh independent projection.

---

# 10. Obligation ledger

| Obligation | Status after this run |
|---|---|
| P06 Randomstrasse Conj. 17 | KNOWN in later literature; `U_ER^cert=1`; not a novelty target |
| P07 full source bound | unchanged: `sqrt(n) <= E theta <= C sqrt(n log log n)` |
| positive fixed-c seed | **PROVED** on nonzero support |
| source-coupled inverse-covariance bound | **PROVED:** `nu^2 <= 0.593984649+o_P(1)` |
| source-sufficient failure | **PROVED:** `O(n^-1/2)+exp[-Omega(n)] = o(1/sqrt(log n))` |
| calibrated two-chaos fixed-c constants | **PROVED IN SURROGATE:** `nu_(2)^2=0.43872`, `Gamma_(2)=1.33016` at `c_*` |
| actual fixed-c `Gamma<2.12` | OPEN — now the isolated coarse-entry gap |
| absolute coarse basin | OPEN; would follow from the preceding skew estimate plus a finite bridge |
| superlinear coarse tail | inherited PROVED CONDITIONAL on coarse entry |
| exact/fixed-slack P07 certificate | OPEN |
| even cyclic order | OPEN; self-inverse frequency not treated |

---

# 11. Next concrete attack

Stay on the fixed-`c_*` seed and prove the remaining finite directional-skew estimate rather than returning to global eigenvalues.

Use the normalized likelihood expansion

\[
e^{-a_*Z-a_*^2/2}
=\sum_{k\ge0}{(-a_*)^k\over k!}H_k(Z).
\]

The order-`>=3` Gaussian `L^2` tail is only `0.001107`. Truncate at a fixed order (for example `R_0=8`), transport the weighted covariance, Newton score and third-cumulant columns through the already-proved fixed-degree Walsh/additive-collision dictionary, and control the analytic remainder using the fixed-parameter subgaussian exponential moments rather than a worst-case Fourier operator norm.

A decisive theorem is any source-sufficient bound

\[
\Gamma_{c_*}\le2.1+o(1),
\]

or a jointly sharper pair such as

\[
\nu_{c_*}\le0.70,
\qquad
\Gamma_{c_*}\le2.4,
\]

that still gives `A<1/2`. The calibrated values `(0.66236,1.33016)` leave substantial room. Once a genuine absolute contracting step is established, invoke the growing-degree superlinear tail from the previous report rather than rebuilding the near-boundary proof.

Keep expectation versus high probability explicit; no full P07 closure is claimed until the positive fixed-slack certificate is actually obtained.