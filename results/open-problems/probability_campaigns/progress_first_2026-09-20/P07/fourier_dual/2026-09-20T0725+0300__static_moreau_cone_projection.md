Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED** — GPT-6 / maximum was requested as an owner preference, but this runtime exposes no authenticated completed-run effort telemetry or binding scheduler selector, so I do not claim otherwise.

# P07-B — static Moreau cone projection and supercritical obstruction transversality

**Native role:** `P07-B`, task `6aabe797a39081919acc889f29f4c556`  
**Repository / branch:** private `yspennstate/math-open-problems` / `master`  
**Captured start master:** `a0d19fb1b24c2668c9aced21b0c74444fcb6a62b`  
**Fresh pre-write master:** `d0f01b30734640999817ea4de2466f5206ccdf43`  
**Previous own report:** `probability_campaigns/progress_first_2026-09-20/P07/fourier_dual/2026-09-20T0610+0300__projected_hinge_directional_margin.md`  
**Complementary P07-A checkpoint read:** `probability_campaigns/progress_first_2026-09-20/P07/primal/2026-09-20T0603+0300__reciprocal_dispersion_support_entropy.md`  
**Outside target:** Randomstrasse101, arXiv:2603.29571, Conjecture 18; partial-result paper arXiv:2502.16227.  
**Source endpoint:** for the dense random circulant source model,
\[
\mathbb E\vartheta(G_n)=(1+o(1))\sqrt n.
\]
**Inherited rigorous source bound:**
\[
\sqrt n\le \mathbb E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]
Hence the frozen full-source metric remains
\[
\boxed{\alpha_{LL}=1/2\to1/2.}
\]
Status: **OPEN / PROVED PARTIAL**. No improvement of the published exponent is claimed in this report.

The assignment-time source recovery, exact Fourier LP, prior TH18 history and current-status check were already completed in earlier P07-B reports. This run does not repeat that screening. It starts from the exact one-sided Fourier completion and attacks the mathematical bottleneck.

The main change is conceptual but exact: the projected-hinge trajectory from the preceding report is the gradient algorithm for a **static cone-distance problem**. Its possible nonzero stall is not an algorithmic defect; it is the unique Moreau residual of the thresholded completion problem. This permits replacing the cumulative-trajectory condition `CDL` by a static random-cone projection quantity. I then prove that every nonzero obstruction above a fixed supercritical threshold `A/sqrt(n)`, `A>1`, has a deterministic positive fraction of its energy in the selected nonzero Fourier modes. This is a dependence-aware transversality statement and does not treat Fourier coordinates as independent.

No numerical code is used below; the idea and proofs are exact.

---

## 1. Retained exact completion normalization

Let `n` be odd and let the nonzero conjugate Fourier pairs be partitioned by the source mask into `D` and `C`. Write
\[
P_D=\sum_{a\in D}Q_a,\qquad
P_C=\sum_{a\in C}Q_a,\qquad
P_0=\frac1n\mathbf1\mathbf1^T,
\]
so
\[
P_0+P_D+P_C=I.
\]
Let `delta_0` denote the coordinate spike at zero and put
\[
x=P_D\delta_0.
\]
The exact one-sided completion parameter recovered previously is
\[
\boxed{
\kappa_D=\inf_{q\in\operatorname{Ran}(P_C)}\max_j(x-q)_j.
}
\tag{1.1}
\]
For the corresponding complementary circulant graph,
\[
\vartheta(\overline{G_D})=1+n\kappa_D,
\tag{1.2}
\]
and the fair source ensemble is complement invariant, so expectation statements transfer to the original source target.

The preceding report studied, for a threshold `tau`, the projected-hinge iteration
\[
q_{k+1}=q_k+P_Ce_k,
\qquad
e_k=(x-q_k-\tau\mathbf1)_+,
\tag{1.3}
\]
and proved the exact descent inequality
\[
\|e_{k+1}\|_2^2\le
\|e_k\|_2^2-\|P_Ce_k\|_2^2.
\tag{1.4}
\]
The new point is to identify exactly what (1.3) is minimizing.

---

# 2. New exact reduction: move all mask dependence into the free Fourier subspace

Because
\[
P_D\delta_0
=\delta_0-P_0\delta_0-P_C\delta_0
=\delta_0-\frac1n\mathbf1-P_C\delta_0,
\]
we may set
\[
w=q+P_C\delta_0\in\operatorname{Ran}(P_C).
\]
Then (1.1) becomes
\[
\boxed{
\kappa_D
=\inf_{w\in\operatorname{Ran}(P_C)}
\max_j\left(\delta_0(j)-\frac1n-w_j\right).
}
\tag{2.1}
\]
Thus the vector that must be completed is deterministic: the centered spike
\[
\delta_0-\frac1n\mathbf1.
\]
The random mask appears only through the random half-Fourier subspace `Ran(P_C)`.

This shift is useful because it removes the source-generated random field `x=P_D delta_0` from the threshold vector. In particular, no independence claim between `x` and the mask is needed in the static formulation below.

For `tau>=0` define
\[
v_\tau:=\delta_0-\left(\tau+\frac1n\right)\mathbf1
\tag{2.2}
\]
and the threshold residual
\[
\boxed{
d_D(\tau):=
\inf_{w\in\operatorname{Ran}(P_C)}
\|(v_\tau-w)_+\|_2.
}
\tag{2.3}
\]

---

# 3. New theorem: `d_D(tau)` is an exact Moreau projection onto the positive source Fourier cone

Let
\[
\mathcal S_D:=\operatorname{Ran}(P_C)+\mathbb R_-^n.
\tag{3.1}
\]
This is a closed polyhedral cone. For fixed `w`, the nearest point to `v_tau-w` in the negative orthant is its coordinatewise negative part, hence
\[
\operatorname{dist}(v_\tau,\mathcal S_D)
=
\inf_{w\in\operatorname{Ran}(P_C)}
\|(v_\tau-w)_+\|_2
=d_D(\tau).
\tag{3.2}
\]
Its polar cone is
\[
\mathcal K_D
:=\mathcal S_D^\circ
=\operatorname{Ran}(P_0+P_D)\cap\mathbb R_+^n.
\tag{3.3}
\]
Indeed the polar of `Ran(P_C)` is its orthogonal complement `Ran(P_0+P_D)`, and the polar of `R_-^n` is `R_+^n`.

## Theorem P07-B.8 — static Moreau residual and regularized primal formula

Let
\[
e_\tau:=\Pi_{\mathcal K_D}v_\tau.
\tag{3.4}
\]
Then
\[
\boxed{d_D(\tau)=\|e_\tau\|_2,}
\tag{3.5}
\]
with the exact support formula
\[
\boxed{
d_D(\tau)
=
\max_{\substack{u\in\mathcal K_D\\ \|u\|_2\le1}}
\langle v_\tau,u\rangle.
}
\tag{3.6}
\]
Moreover
\[
\boxed{
d_D(\tau)=0\iff \kappa_D\le\tau,}
\tag{3.7}
\]
and always
\[
\boxed{
\kappa_D\le\tau+d_D(\tau).
}
\tag{3.8}
\]

### Proof

Equation (3.5) is Moreau decomposition for the polar pair `(S_D,K_D)`, using (3.2). The support identity (3.6) follows because for a closed convex cone `S`,
\[
\operatorname{dist}(v,S)
=
\max_{u\in S^\circ,\ \|u\|_2\le1}\langle v,u\rangle.
\]

Now `d_D(tau)=0` iff there is `w in Ran(P_C)` with `v_tau-w<=0` coordinatewise, which is exactly
\[
\max_j\left(\delta_0(j)-\frac1n-w_j\right)\le\tau.
\]
By (2.1), this is equivalent to `kappa_D<=tau`, proving (3.7).

Finally take a minimizing `w` in (2.3). Then
\[
\max_j\left(\delta_0(j)-\frac1n-w_j\right)
\le
\tau+\|(v_\tau-w)_+\|_\infty
\le
\tau+d_D(\tau).
\]
Taking the infimum in (2.1) gives (3.8). ∎

### Exact simplex form

Define the positive Fourier simplex
\[
\mathcal F_D:=
\{p\in\mathbb R_+^n:\ \mathbf1^Tp=1,\ P_Cp=0\}.
\tag{3.9}
\]
This is the frequency-primal feasible simplex associated with the same complementary graph as (1.1). Every nonzero `u in K_D` can be uniquely normalized along its ray as
\[
p=u/\|u\|_1\in\mathcal F_D.
\]
Applying this normalization to (3.6) yields the exact identity
\[
\boxed{
d_D(\tau)
=
\max_{p\in\mathcal F_D}
\frac{\bigl(p_0-\frac1n-\tau\bigr)_+}{\|p\|_2}.
}
\tag{3.10}
\]
Thus `d_D(tau)` is a **norm-regularized primal overshoot** above the threshold. In particular, the projected-hinge algorithm from the preceding report is simply projected gradient descent for the convex objective
\[
\frac12\|(v_\tau-w)_+\|_2^2,
\qquad w\in\operatorname{Ran}(P_C),
\tag{3.11}
\]
and its global minimum is `d_D(tau)^2/2`.

This corrects the interpretation of a nonzero exact stall. A stationary residual `e` with `P_Ce=0` is not merely an algorithmic pathology: it is precisely a KKT/Moreau obstruction in the positive Fourier cone. The preceding report's “stall gives a primal witness” identity is therefore the endpoint geometry of the whole convex problem.

---

# 4. A static lemma sufficient to remove the iterated-log loss

From (3.8), for every deterministic threshold `tau`,
\[
\mathbb E\kappa_D\le\tau+\mathbb E d_D(\tau).
\tag{4.1}
\]
Using (1.2) and complement invariance gives the following exact sufficient target.

## Missing Static Positive-Cone Projection Lemma `SPCP(A)`

For a fixed `A>1`, set
\[
\tau=\frac A{\sqrt n}.
\]
Prove
\[
\boxed{
\mathbb E_D d_D(A/\sqrt n)=O(n^{-1/2}).
}
\tag{4.2}
\]
Then
\[
\mathbb E\vartheta(G_n)=O(\sqrt n),
\]
so the published `sqrt(log log n)` loss disappears and `alpha_LL=0`.

For the sharp constant, it is enough to prove the stronger statement: for every fixed `epsilon>0`, with `A=1+epsilon`,
\[
\boxed{
\mathbb E_D d_D((1+\epsilon)/\sqrt n)=o(n^{-1/2}).
}
\tag{4.3}
\]
Indeed (4.1) then gives
\[
\mathbb E\vartheta(G_n)
\le(1+\epsilon)\sqrt n+o(\sqrt n),
\]
and the known lower bound followed by `epsilon downarrow0` yields Conjecture 18.

This is a static, source-exact condition. It requires no assertion that dependent Fourier coordinates are independent and no uniform RIP over all vectors. It also avoids having to prove that the endogenous projected-hinge trajectory accumulates `Theta(log n)` directional leakage. The trajectory can converge slowly; only the static Moreau residual must be small.

A high-probability variant is also sufficient: since `d_D(tau)<=||v_tau||_2=O(1)` for fixed `A`, the bound
\[
\Pr\{d_D(A/\sqrt n)>0\}=O(n^{-1/2})
\tag{4.4}
\]
already implies (4.2), while `o(n^{-1/2})` implies the sharp fixed-`A` version. This is stronger than necessary but gives a clean source-level target.

---

# 5. New deterministic theorem: every supercritical static obstruction is Fourier-transverse

The static formulation gives a structural fact unavailable from the raw hinge trajectory.

Fix `tau>=0` and suppose
\[
e:=e_\tau=\Pi_{\mathcal K_D}v_\tau\ne0.
\]
Write
\[
H:=\|e\|_2^2,
\qquad
s:=\|e\|_1,
\qquad
b:=\tau+\frac1n.
\tag{5.1}
\]

### Step 1: exact projection identity

Moreau orthogonality gives
\[
\langle v_\tau,e\rangle=\|e\|_2^2=H.
\]
Since `v_tau=delta_0-b1`,
\[
\boxed{
e_0-bs=H,}
\qquad\text{equivalently}\qquad
\boxed{e_0=H+bs.}
\tag{5.2}
\]

### Step 2: the distinguished coordinate is the largest coordinate

The cone `K_D` is invariant under cyclic coordinate shifts: both the nonnegative orthant and the Fourier subspace `Ran(P_0+P_D)` are shift invariant. The projection `e` is equivalently the unique maximizer over `u in K_D` of
\[
\langle v_\tau,u\rangle-\frac12\|u\|_2^2.
\tag{5.3}
\]
If a cyclic shift places `e_j` at coordinate zero, its norm and coordinate sum are unchanged, while the linear objective changes by `e_j-e_0`. Maximality of `e` therefore implies
\[
\boxed{e_0=\|e\|_\infty.}
\tag{5.4}
\]

Combining (5.2), (5.4), and `e_0<=sqrt(H)` gives
\[
H+bs\le\sqrt H.
\tag{5.5}
\]
In particular,
\[
\boxed{
\frac{s^2}{H}\le\frac1{b^2}.
}
\tag{5.6}
\]

### Step 3: exact nonzero-Fourier energy lower bound

Because `e in Ran(P_0+P_D)`,
\[
P_Ce=0,
\qquad
P_0e=\frac{s}{n}\mathbf1.
\]
Hence
\[
\|P_De\|_2^2
=H-\frac{s^2}{n}.
\tag{5.7}
\]
Using (5.6),
\[
\boxed{
\frac{\|P_De\|_2^2}{\|e\|_2^2}
\ge
1-\frac1{n(\tau+1/n)^2}.
}
\tag{5.8}
\]
At the source scale `tau=A/sqrt(n)`, this becomes
\[
\boxed{
\frac{\|P_De\|_2^2}{\|e\|_2^2}
\ge
1-\frac1{(A+n^{-1/2})^2}.
}
\tag{5.9}
\]
Therefore for every fixed `A>1`, **every nonzero static obstruction** has at least
\[
1-A^{-2}-o(1)
\]
of its squared `ell_2` energy in the selected nonzero Fourier modes `D`.

This is deterministic conditional on the mask and uses no independence approximation.

## Equivalent effective-support statement

Normalize the obstruction to a probability vector
\[
p=e/s\in\mathcal F_D.
\]
Then (5.6) says
\[
\boxed{
\|p\|_2\ge\tau+\frac1n.
}
\tag{5.10}
\]
Thus its Rényi-2 effective support obeys
\[
\boxed{
\frac1{\|p\|_2^2}
\le
\frac1{(\tau+1/n)^2}.
}
\tag{5.11}
\]
At `tau=A/sqrt(n)`,
\[
\boxed{
\frac1{\|p\|_2^2}
\le
\frac{n}{(A+n^{-1/2})^2}.
}
\tag{5.12}
\]
So a supercritical obstruction is not an arbitrary positive Fourier witness: it must be quantitatively more concentrated than the uniform law, with effective support at most about `n/A^2`.

Finally, dividing (5.2) by `s` gives the exact witness identity
\[
\boxed{
p_0-\frac1n
=\tau+\frac{H}{s}.}
\tag{5.13}
\]
Since `d_D(tau)=sqrt(H)` and `||p||_2=sqrt(H)/s`,
\[
\boxed{
d_D(\tau)
=\frac{p_0-1/n-\tau}{\|p\|_2},}
\tag{5.14}
\]
realizing the maximizer in (3.10).

### Why (5.9) is useful

The missing source theorem is no longer “show every mask-dependent positive residual has complement energy.” At a fixed supercritical threshold, a nonzero obstruction is forced to have a **constant nonzero selected-frequency energy fraction**. Any dependence-aware small-ball or conic comparison may therefore condition on this transversality instead of handling almost-constant positive vectors. This is exactly the regime where the primary signed-RIP method loses too much by controlling all vectors uniformly.

---

# 6. Exact bridge to P07-A without duplicating the primal route

P07-A has proved two facts that should be retained rather than reproved here:

1. the exact primal orthant-ratio geometry for the source Fourier kernel; and
2. the Haar half-dimensional cone threshold occurs at the conjectured constant `1`.

The present report adds a quantitative margin observable to that picture. Eventwise,
\[
d_D(A/\sqrt n)>0
\iff
\kappa_D>A/\sqrt n,
\tag{6.1}
\]
so it is the same supercritical cone-intersection event after the complement normalization. But `d_D` records **how far** the deterministic centered spike lies outside the feasible completion cone, and its expectation directly upper-bounds the expectation excess through (4.1).

The normalized maximizer in (5.12) gives P07-A a sharper class to count if it pursues its support/entropy route: only source-feasible positive witnesses with effective support at most `n/(A+o(1))^2` can realize the static projection at level `A/sqrt(n)`.

I do **not** make the earlier `ell_2` one-sided modulus `beta` the next target. P07-A already proved that this surrogate is too strong to preserve the sharp Haar threshold. The effective-support/transversality statements above are properties of the actual static obstruction, not uniform inequalities over the whole kernel.

---

# 7. Failed multiscale idea: naive fresh-frequency golfing cannot by itself supply `log n` contraction

The deterministic-spike shift makes a disjoint-frequency reveal tempting: reveal independent source frequency pairs in stages and use only freshly exposed frequencies to repair the residual. There is, however, a simple quantitative obstruction to the naive version.

Suppose unresolved pairs are assigned to `D` in stages with conditional hazards `p_1,p_2,...,p_L`, and after all stages a pair has the correct source probability `1/2` of belonging to `D`. Then
\[
\prod_{\ell=1}^L(1-p_\ell)=\frac12.
\]
Therefore
\[
\sum_{\ell=1}^L -\log(1-p_\ell)=\log2,
\]
and since `p<=-log(1-p)`,
\[
\boxed{
\sum_{\ell=1}^L p_\ell\le\log2.
}
\tag{7.1}
\]
Thus any staged argument whose only guaranteed contraction at stage `ell` is proportional to the fresh inclusion hazard `p_ell` has only `O(1)` total contraction budget. It cannot by itself generate the `Theta(log n)` cumulative leakage demanded by the preceding dynamic `CDL` route.

This does **not** rule out a multiscale proof using geometry, threshold changes, reuse of revealed frequencies, or a static cone margin. It rules out only the simplest “fresh independent slice gives proportional contraction” golfing architecture. This failure is one reason to pursue the static Moreau residual instead of forcing the dynamic path-length argument.

---

# 8. Exact next attack

The next proof target is `SPCP(A)`, but the useful intermediate statement should exploit (5.9) rather than attack arbitrary positive Fourier vectors.

A concrete dependence-aware target is:

> **Localized static-cone small-ball lemma.** For each fixed `A>1`, prove that the probability (or expected Moreau norm) of a nonzero `e in Ran(P_0+P_D) cap R_+^n` satisfying the projection KKT identities
> \[
> e_0=\|e\|_\infty=\|e\|_2^2+(A/\sqrt n+1/n)\|e\|_1
> \]
> and the transversality bound
> \[
> \|P_De\|_2^2\ge(1-A^{-2}-o(1))\|e\|_2^2
> \]
> is small enough to imply (4.2), ideally (4.3).

This is a **single deterministic-vector / random-positive-cone distance problem**, not an all-sign RIP estimate and not an independence model for the Fourier coordinates. The most promising next tool is a leave-one-frequency or Lindeberg replacement applied to the smoothed support function in (3.6), while keeping the KKT-generated concentration condition (5.12). A successful comparison only at this one cone projection would be weaker than a uniform partial-Fourier-versus-Haar theorem and therefore more plausible.

---

## 9. Progress ledger

```yaml
ledger_delta:
  native_task_id: "6aabe797a39081919acc889f29f4c556"
  role: "P07-B Fourier dual"
  source: "Randomstrasse101 arXiv:2603.29571 Conjecture 18; partial arXiv:2502.16227"
  captured_start_master: "a0d19fb1b24c2668c9aced21b0c74444fcb6a62b"
  fresh_prewrite_master: "d0f01b30734640999817ea4de2466f5206ccdf43"
  metric: "alpha_LL"
  metric_before: "1/2"
  metric_after: "1/2"
  mathematical_status: "OPEN / PROVED PARTIAL"
  proved_new:
    - "deterministic centered-spike completion shift"
    - "exact Moreau cone projection formula for threshold residual"
    - "exact norm-regularized positive-primal formula"
    - "projection peak identity e_0=||e||_infty"
    - "supercritical selected-Fourier energy lower bound"
    - "supercritical effective-support upper bound"
    - "naive fresh-hazard golfing has only O(1) total hazard"
  corrected_bottleneck:
    - "nonzero projected-hinge stall is the global Moreau/KKT residual, not merely an algorithmic defect"
    - "replace dynamic cumulative-leakage requirement by static SPCP(A) expectation/margin target"
  source_solution_claimed: false
  next_attack: "dependence-aware one-vector positive-cone small-ball / Lindeberg comparison using KKT transversality"
```
