Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED** — GPT-6 / maximum was requested as an owner preference, but this runtime does not expose authenticated completed-run effort telemetry, so I do not claim otherwise.

# P07-A — exact profiled-Gibbs homotopy from the uniform law to the optimal flat theta certificate

**Native role:** `P07-A`, task `6aa7b46f70a8819184095c277974c256`  
**Repository / branch:** private `yspennstate/math-open-problems` / `master`  
**Captured pre-write master:** `8c15f27e5ee986d0864cf75b73439fc8c7fd8bf9`  
**Previous own checkpoint:** `probability_campaigns/progress_first_2026-09-20/P07/primal/2026-09-20T0842+0300__unique_positive_cosine_basis_discrepancy.md`, blob `4dfb7147a3d6202a1115b752666933aea1571e63`.  
**Complementary checkpoint used:** P07-B `probability_campaigns/progress_first_2026-09-20/P07/fourier_dual/2026-09-20T0927+0300__gibbs_radial_exceptional_frequencies.md`, blob `795e8913ebe7c8d8e44c560b2f48de277caf98d3`. P07-B owns the Fourier-dual / exceptional-frequency route. This report imports its radial Gibbs construction and exact moment-polytope normalization only, then solves a different primal problem: how to force **all** selected moments to be equal without abandoning positivity.

**Outside target:** Randomstrasse101, arXiv:2603.29571, Conjecture 18; primary partial-result paper *The Lovasz number of random circulant graphs*, arXiv:2502.16227. The source model is the odd-`n` dense random circulant model with `m=(n-1)/2` independent Bernoulli choices on conjugate nonzero difference pairs. The endpoint is
\[
\mathbb E\,\vartheta(G_n)=(1+o(1))\sqrt n.
\]
The current primary text still gives
\[
\sqrt n\le \mathbb E\vartheta(G_n)\le C\sqrt{n\log\log n}
\]
and explicitly notes that its RIP-based upper-bound argument omits positivity. No later source-matching resolution was found in the bounded assignment/current check. This run does **not** improve that arbitrary-`n` asymptotic bound, so the fixed full-source metric remains
\[
\boxed{\alpha_{LL}=1/2\to1/2.}
\]
Status: **OPEN / PROVED PARTIAL**. External novelty of the information-geometric formulation below is **UNVERIFIED**.

The substantive advance is an exact feasible-certificate construction valid for every odd `n` and every nontrivial proper selected pair set `D`: an exponential family can be profiled in the transverse directions so that its selected cosine moments are **exactly flat**. As the scalar tilt grows, these certificates increase monotonically from the trivial uniform certificate all the way to the exact moment-polytope optimum. The profile derivative is an explicit Schur complement of the covariance, and the cost of repairing P07-B's radial Gibbs law to exact flatness is exactly a KL divergence. Thus the remaining source problem is reduced to a concrete concentration/curvature question rather than a generic RIP statement.

---

## 0. Concise predecessor preservation: SRG69 remains OPEN / PARTIAL

The reassigned predecessor is preserved and is not called solved. Its historical handoff remains under

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-13/rotations/SHPECTOROV-ZHAO-2026-SRG69/`

with frozen `R_SRG69=1`, status **OPEN / PARTIAL**. Preserve the no-Cayley theorem, exact rooted `L/B/C` system, centered spectral transfer, endpoint/cycle restrictions, block-moment and Gram reductions, and star-complement handoff. This report does not edit that root.

---

# 1. Exact moment-polytope normalization inherited from the canonical TH18 work

Let `n` be odd,
\[
M=\{1,\ldots,(n-1)/2\},
\]
and let `D\subset M` be the selected source pair set, with
\[
0<d:=|D|<|M|.
\]
(The two excluded deterministic masks have exponentially small source probability and can be handled separately.)

For `a\in D` and `j\in\mathbb Z_n`, set
\[
\phi_a(j)=\cos(2\pi aj/n),
\qquad
\Phi(j)=(\phi_a(j))_{a\in D}\in\mathbb R^d.
\tag{1.1}
\]
The exact moment-polytope parameter recovered in the earlier TH18 line is
\[
\delta_D:=\max\left\{\delta\ge0:\exists\text{ symmetric probability }w\text{ on }\mathbb Z_n,
\ \mathbb E_w\Phi=-\delta\mathbf1_D\right\}.
\tag{1.2}
\]
It satisfies
\[
\kappa_D=\frac1{n\delta_D},
\qquad
\vartheta(\bar G_D)=1+n\kappa_D=1+\frac1{\delta_D}.
\tag{1.3}
\]
By complement-invariance of the fair source law,
\[
\mathbb E\vartheta(G_n)=1+\mathbb E\frac1{\delta_D}.
\tag{1.4}
\]
Thus the sharp source endpoint is a sharp **radial-depth** statement for the random cosine moment polytope.

The uniform probability on `Z_n\setminus\{0\}` gives every nonzero cosine moment `-1/(n-1)`, hence always
\[
\delta_D\ge\frac1{n-1}.
\tag{1.5}
\]
The point of the construction below is to turn this one certificate into a canonical monotone family converging to `delta_D`.

---

# 2. The profiled exponential family

Put
\[
u:=d^{-1/2}\mathbf1_D,
\qquad
P:=I-uu^\top,
\tag{2.1}
\]
so `P` is orthogonal projection onto the transverse space `u^\perp`.

For `lambda\in\mathbb R^d`, define
\[
Z(\lambda)=\sum_{j\ne0}\exp(-\langle\lambda,\Phi(j)\rangle),
\qquad
\psi(\lambda)=\log Z(\lambda),
\tag{2.2}
\]
and the symmetric full-support probability on `Z_n\setminus\{0\}`
\[
p_\lambda(j)=\frac{\exp(-\langle\lambda,\Phi(j)\rangle)}{Z(\lambda)}.
\tag{2.3}
\]
Write
\[
m(\lambda):=\mathbb E_{p_\lambda}\Phi=-\nabla\psi(\lambda),
\qquad
\Sigma(\lambda):=\operatorname{Cov}_{p_\lambda}(\Phi)=\nabla^2\psi(\lambda).
\tag{2.4}
\]

For a scalar `s\in\mathbb R`, profile out all transverse directions:
\[
\boxed{
\varphi(s):=\min_{\eta\in u^\perp}\psi(su+\eta),
\qquad
\eta_s:=\arg\min_{\eta\in u^\perp}\psi(su+\eta).
}
\tag{2.5}
\]

The radial family `eta=0` is exactly P07-B's excluded-origin Gibbs law after the parameter conversion
\[
s=\beta\sqrt{d/n},
\tag{2.6}
\]
because `su=(beta/sqrt(n)) 1_D`.

---

# 3. Main new theorem: exact flatness and monotone convergence to the optimal certificate

## Theorem P07-A.20 — profiled Gibbs flat-certificate homotopy

For every odd `n` and every `D\subset M` with `0<d<|M|`, the following hold.

1. For every real `s`, the minimizer `eta_s` in (2.5) exists and is unique.
2. The selected moments under `p_{su+eta_s}` are exactly equal:
   \[
   \boxed{
   \mathbb E_{p_{su+\eta_s}}\phi_a
   =-\delta(s)\qquad\forall a\in D,
   }
   \tag{3.1}
   \]
   where
   \[
   \delta(s):=-\frac{u^\top m(su+\eta_s)}{\sqrt d}.
   \tag{3.2}
   \]
   Hence each `s>=0` gives an **exact feasible moment-polytope / theta certificate**.
3. `delta(0)=1/(n-1)`, `delta(s)` is strictly increasing, and
   \[
   \boxed{
   \delta(s)\uparrow\delta_D\quad\text{as }s\to+\infty.
   }
   \tag{3.3}
   \]
4. Consequently the explicit upper certificates
   \[
   \boxed{
   \vartheta(\bar G_D)\le1+\frac1{\delta(s)}
   }
   \tag{3.4}
   \]
   decrease monotonically to the exact optimum `theta(bar G_D)`.

### Proof of existence and uniqueness

Fix `s`. On `u^\perp`, the Hessian of `eta -> psi(su+eta)` in a direction `z\in u^\perp` is
\[
z^\top\Sigma(su+\eta)z
=\operatorname{Var}_{p_{su+\eta}}\langle z,\Phi(J)\rangle.
\tag{3.5}
\]
This is strictly positive for `z ne0`. Indeed, variance zero would mean the cosine polynomial
\[
f_z(j)=\sum_{a\in D}z_a\cos(2\pi aj/n)
\]
is constant on every `j ne0`. Because `z\perp u`, its average over `j ne0` is zero, so that constant is zero. Distinct cosine characters are linearly independent, hence `z=0`, contradiction. Thus the transverse objective is strictly convex.

It is also coercive. For nonzero `z\in u^\perp`, the average of `f_z(j)` over `j ne0` is zero and `f_z` is nonconstant, so it takes both signs. Hence along either ray `t z`, the log-sum-exp contains a term growing linearly as `|t|->infinity`. Compactness of the transverse unit sphere makes this growth uniform. Therefore a unique minimizer exists.

### Proof of exact flatness

The first-order condition at `eta_s` is
\[
P\nabla\psi(su+\eta_s)=0.
\]
Using `m=-nabla psi`, this is
\[
Pm(su+\eta_s)=0.
\tag{3.6}
\]
Therefore `m` is parallel to `u`, i.e. all `d` selected cosine moments are identical. This proves (3.1).

At `s=0`, `eta=0` already satisfies the first-order condition because the uniform law on `j ne0` has every selected moment `-1/(n-1)`. Uniqueness gives `eta_0=0` and
\[
\delta(0)=\frac1{n-1}.
\tag{3.7}
\]

### Proof that the profile reaches the exact optimum

Let `q_0` be the uniform law on `Z_n\setminus\{0\}`. The Gibbs variational principle says, for any `lambda`,
\[
\psi(\lambda)-\log(n-1)
=\sup_w\{-\lambda^\top m(w)-D_{KL}(w\|q_0)\}.
\tag{3.8}
\]
For a probability `w` with `Pm(w)=0`, define
\[
\delta(w):=-\frac{u^\top m(w)}{\sqrt d}.
\]
Then the `eta` term vanishes, so (3.8) gives the lower bound
\[
\varphi(s)-\log(n-1)
\ge s\sqrt d\,\delta(w)-D_{KL}(w\|q_0).
\tag{3.9}
\]
Conversely, the profiled Gibbs law `w_s=p_{su+eta_s}` itself has `Pm(w_s)=0`, and equality in the Gibbs variational principle at its own parameter gives
\[
\varphi(s)-\log(n-1)
=s\sqrt d\,\delta(s)-D_{KL}(w_s\|q_0).
\tag{3.10}
\]
Hence, exactly,
\[
\boxed{
\varphi(s)-\log(n-1)
=\sup_{w:\,Pm(w)=0}
\{s\sqrt d\,\delta(w)-D_{KL}(w\|q_0)\}.
}
\tag{3.11}
\]
Symmetrizing `w` under `j -> -j` preserves all cosine moments and cannot increase relative entropy, so the supremum is unchanged if restricted to symmetric probabilities. Its maximal possible `delta(w)` is therefore exactly `delta_D` from (1.2).

Since `0<=D_KL(w||q_0)<=log(n-1)` for a probability supported on `n-1` sites, (3.11) implies
\[
\lim_{s\to\infty}\frac{\varphi(s)}s=\sqrt d\,\delta_D.
\tag{3.12}
\]
By the envelope theorem,
\[
\varphi'(s)=u^\top\nabla\psi(su+\eta_s)
=-u^\top m(su+\eta_s)
=\sqrt d\,\delta(s).
\tag{3.13}
\]
The profile `varphi` is convex, so `delta(s)` is nondecreasing. Its derivative limit must equal the asymptotic slope in (3.12), proving `delta(s) -> delta_D`. Strict monotonicity follows from the positive Schur-complement formula in the next section. This proves the theorem. `square`

### Interpretation

The theta optimum is no longer merely characterized by an existential LP. It is the zero-temperature limit of a **one-parameter positive exponential family whose every member already obeys all equal-moment constraints exactly**. This is a source-specific feasible-certificate construction; finite values of `s` are valid certificates, not numerical guesses.

---

# 4. Exact differential identity: the remaining obstruction is a covariance Schur complement

Because the transverse Hessian is positive definite, `eta_s` is smooth. Let
\[
\Sigma_s:=\Sigma(su+\eta_s),
\qquad
A_s:=(P\Sigma_sP)|_{u^\perp}.
\tag{4.1}
\]
Differentiating the flatness condition `Pm=0` gives
\[
\boxed{
\eta_s'=-A_s^{-1}P\Sigma_su.
}
\tag{4.2}
\]
Therefore
\[
\begin{aligned}
\delta'(s)
&=\frac1{\sqrt d}
\left(
 u^\top\Sigma_su
-u^\top\Sigma_sP A_s^{-1}P\Sigma_su
\right).
\end{aligned}
\tag{4.3}
\]
The bracket is the Schur complement of the transverse covariance block. Since `D` is proper, the full covariance is positive definite, so equivalently
\[
\boxed{
\delta'(s)
=\frac1{\sqrt d\;u^\top\Sigma_s^{-1}u}>0.
}
\tag{4.4}
\]

This is the main quantitative reduction. The exact moment-polytope radius satisfies
\[
\boxed{
\delta_D
=\frac1{n-1}
+\frac1{\sqrt d}\int_0^\infty
\frac{ds}{u^\top\Sigma_s^{-1}u}.
}
\tag{4.5}
\]
No independence among Fourier coordinates is asserted. The entire sharp-constant problem has become a lower bound on a **one-dimensional effective covariance along an endogenous positive Gibbs path**.

---

# 5. Exact initial curvature and normalization check against P07-B

At `s=0`, the law is uniform on `j ne0`. Direct cosine orthogonality gives, for `a ne b`,
\[
\mathbb E\phi_a=-\frac1{n-1},
\quad
\mathbb E\phi_a^2=\frac{n-2}{2(n-1)},
\quad
\mathbb E\phi_a\phi_b=-\frac1{n-1}.
\]
Thus
\[
\boxed{
\Sigma_0=
\frac{n}{2(n-1)}I_d
-\frac{n}{(n-1)^2}J_d.
}
\tag{5.1}
\]
The transverse eigenvalue is `n/[2(n-1)]`, while the radial eigenvalue is
\[
\lambda_{\parallel}(0)
=\frac{n}{2(n-1)}
\left(1-\frac{2d}{n-1}\right).
\tag{5.2}
\]
There is no radial/transverse covariance at `s=0`, so
\[
\boxed{
\delta'(0)
=\frac{n}{2(n-1)\sqrt d}
\left(1-\frac{2d}{n-1}\right).
}
\tag{5.3}
\]
For the fair source, `d/n -> 1/4` in probability, hence
\[
\sqrt n\,\delta'(0)\to\frac12.
\tag{5.4}
\]

Now use the P07-B radial parameter `beta`, for which `s=beta sqrt(d/n)`. Then
\[
\left.\frac{d\delta}{d\beta}\right|_{0}
=\delta'(0)\sqrt{d/n}
=\frac1{4\sqrt n}+o(n^{-1/2}),
\tag{5.5}
\]
exactly matching P07-B's small-`beta` radial average-moment slope. This independently checks the Fourier normalization and the source pair-count factor.

At source-typical density, the desired sharp scale is `delta_D~n^{-1/2}`. Equation (5.3) shows that the profiled path starts in precisely the correct direction and at the correct scale; what remains is to prevent the effective covariance in (4.4) from collapsing too quickly before the path accumulates order `n^{-1/2}` radial depth.

---

# 6. Exact bridge to P07-B: flatness repair cost equals KL information projection

For the same scalar `s`, let
\[
p_s^{rad}:=p_{su},
\qquad
p_s^{flat}:=p_{su+\eta_s}.
\]
Define the profiling loss
\[
L_D(s):=\psi(su)-\varphi(s)\ge0.
\tag{6.1}
\]

## Lemma P07-A.21 — exact information-projection identity

\[
\boxed{
L_D(s)=D_{KL}(p_s^{flat}\|p_s^{rad}).
}
\tag{6.2}
\]

### Proof

From the exponential-family definition,
\[
\log\frac{p_s^{flat}(j)}{p_s^{rad}(j)}
=-\langle\eta_s,\Phi(j)\rangle
-\varphi(s)+\psi(su).
\]
Taking expectation under `p_s^{flat}`, the first term vanishes because `eta_s perp u` while its exact moment vector is parallel to `u`. The remaining terms are (6.2). `square`

This gives a clean division of labor between the two P07 roles. P07-B controls the radial partition function and the residual dispersion of its selected moments. P07-A identifies the **exact information cost of correcting that radial law to perfect flatness**.

There is also a deterministic comparison lemma. Let
\[
r_s:=P\,m(su)
\tag{6.3}
\]
be the transverse moment residual of the radial Gibbs law. Suppose that along the segment `su+t eta_s`, `0<=t<=1`, the transverse covariance obeys
\[
(P\Sigma(su+t\eta_s)P)|_{u^\perp}\succeq\mu I
\tag{6.4}
\]
for some `mu>0`. Strong convexity then gives
\[
\boxed{
L_D(s)\le\frac{\|r_s\|_2^2}{2\mu}.
}
\tag{6.5}
\]
P07-B's latest report proves, at fixed radial `beta`, a source-probabilistic bound on precisely `||r_s||_2^2` (its selected within-group dispersion `V_D`), with small-`beta` scale `O(beta^4)`. Thus a source-specific lower bound on the relevant transverse covariance — not a global RIP theorem — would immediately convert its radial construction into exact flat feasible certificates.

Equation (6.5) is a reduction, not a claim that `mu` is already bounded below uniformly at the needed tilt.

---

# 7. What moved, what did not, and why this is a different method

**Fixed full-source metric:**
\[
\boxed{\alpha_{LL}=1/2\to1/2.}
\]
No arbitrary-`n` asymptotic theta improvement is claimed in this report.

**New proved partial results:**

1. A canonical exact-flat exponential-family certificate `p_s^{flat}` for every scalar tilt `s` and every nontrivial proper source mask `D`.
2. Monotone convergence `delta(s) up to delta_D`: the family reaches the exact moment-polytope optimum in the zero-temperature limit.
3. Exact differential formula (4.4), reducing progress to a covariance Schur complement along this one-dimensional path.
4. Exact initial covariance and slope, reproducing the source `n^{-1/2}` normalization with the correct pair-count factor.
5. Exact KL identity (6.2): the cost of repairing P07-B's radial Gibbs law to exact moment flatness is an information projection.
6. Conditional but exact strong-convexity bridge (6.5) from P07-B's already-controlled radial residual to a genuine flat theta certificate.

This is materially different from the preceding prime-only positive-basis/discrepancy route. It does not require prime `n`, Chebotarev minors, support enumeration, or a generic all-sign RIP estimate.

**Not proved:**

- no lower bound yet on the effective covariance in (4.4) for the source-random profiled path at the tilt needed for the constant `1`;
- no uniform lower bound on `mu` in (6.4);
- no movement of the published `sqrt(log log n)` factor yet;
- no claim that a finite-`n` numerical theta calculation implies an arbitrary-`n` theorem;
- no source closure or novelty certificate.

---

# 8. Remaining gap and next concrete attack

The useful next obligation is now narrow:

> **Profile-curvature target.** For the fair random pair mask `D`, prove enough lower control on
> \[
> \sigma_{eff}(s):=
> u^\top\Sigma_su-u^\top\Sigma_sP(P\Sigma_sP)^{-1}P\Sigma_su
> \]
> over a fixed `s`-interval to force `delta(s)>=(1-o(1))/sqrt(n)` with the expectation/tail strength required by (1.4).

Three concrete primal routes are available without duplicating P07-B's exceptional-frequency program:

1. **Information-projection route.** Bound `L_D(s)` directly, using P07-B's exact radial free energy plus a source-specific lower bound on transverse covariance only in the residual direction generated by the mask. Full spectral conditioning of the whole Fourier matrix is unnecessary.
2. **Low-order covariance expansion.** Differentiate the Schur complement at `s=0`. Its coefficients are explicit random additive counts in `D`. Prove concentration for the first nontrivial terms and a controlled remainder on a fixed interval. This attacks the sharp constant through the actual profiled path rather than all sparse directions.
3. **Primal convex-geometric route.** Interpret `p_s^{flat}` as the information projection of the uniform measure onto the affine flat-moment slice and seek a direct lower bound on its entropy / effective support. If the entropy stays sufficiently high until radial depth `~1/sqrt(n)`, covariance collapse is impossible.

The most promising immediate step is route 1 because P07-B has already produced the radial free-energy and `l2` residual estimates needed on one side of (6.5). The new missing lemma is precisely a **transverse information-projection stability estimate**, not another exceptional-frequency count.

No checker is created in this run: the new claims are theorem-sized identities and reductions with written proofs, and no finite computation is being promoted to source-level progress.