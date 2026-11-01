Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but authenticated telemetry does not verify GPT-6 maximum, so I do not claim it.**

# P06 complementary P07 iteration — floor-preconditioned residual certificate removes the Schur inverse

Status: **P06 SOURCE KNOWN / preserve `U_ER^cert=1`. P07 OPEN / PROVED PARTIAL new mathematics; publication novelty UNVERIFIED.**

Native role preserved: `6aa7b53b0858819196d923203522c996`.

Previous substantive checkpoint: `probability_campaigns/progress_first_2026-09-20/P06/sdp/2026-09-20T1927+0300__galerkin_saturation_recurrence.md`, creation commit `30c9f1c3e13f9ef15f86cd5a4e6ef084e2e18ea9`, readback blob `e3d3eb50a26c8a07d09e754119819133d5defd15`.

Outside source for the complementary problem remains Bandeira--Blasiok--Dmitriev--Faure--Kireeva--Kunisky, arXiv:2502.16227 / Randomstrasse Conjecture 18. The inherited full-source bound remains

\[
\sqrt n\le \mathbf E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]

No full-source improvement is claimed in this report.

## 0. New result in one sentence

The preceding run reduced the growing-depth problem to the current-law Schur saturation gap

\[
\Delta_R=\zeta_R^T S_R^{-1}\zeta_R.
\]

The present run removes the inverse Schur complement from the quantity that must be estimated.  If the current law is obtained from the previous law by a positive reweighting `p_+=w p` with deterministic floor `w>=eta`, and `g_R` is any restricted Newton/Galerkin score under `p_+`, then the exact target mismatch

\[
D_R={dL\over dp}-w(1+g_R)
\]

satisfies

\[
\boxed{
\Delta_R
\le {1\over\eta}
\bigl\|P_{F_p\cap K_R^{\perp,p}}D_R\bigr\|_{L^2(p)}^2
\le {1\over\eta}\,\mathbf E_p D_R^2.
}
\tag{0.1}
\]

Thus the difficult source-specific inverse problem is replaced by the `L^2` energy of **one explicit old-law residual source**.  Combining (0.1) with the inherited exact-cost square lemma gives the two-floor recurrence

\[
\boxed{
\nu_{++}
\le
\sqrt{J_R(\eta')}
+{\|P_{F_p\cap K_R^{\perp,p}}D_R\|_{L^2(p)}
\over\sqrt{\eta\eta'}}.
}
\tag{0.2}
\]

This is stronger as a proof architecture than the preceding `\zeta^TS^{-1}\zeta` target: every term on the right of (0.2) is a scalar/source projection accessible to the existing fixed-projector collision machinery, and no current-law inverse covariance or global minimum eigenvalue appears.

At the explicit `p_3` state, using the inherited `eta_3=0.005`, degree-32 cost `J_{32}(0.01)<=7.0e-11+o_P(1)`, and a prospective fourth-step floor `eta_4=0.01`, one gets the completely explicit implication

\[
\boxed{
\nu_4
\le 8.37\times10^{-6}
+141.422\,\mathcal R_{32}^{1/2}
+o_P(1),
}
\tag{0.3}
\]

where

\[
\mathcal R_{32}
:=\bigl\|P_{F_{p_2}\cap K_{32}^{\perp,p_2}}D_{32}\bigr\|_{L^2(p_2)}^2.
\]

For example `mathcal R_32<=4.20e-13` already implies `nu_4<=1.0e-4+o_P(1)`, while `mathcal R_32<=2.35e-14` implies `nu_4<=3.0e-5+o_P(1)`.  The next finite-model calculation is therefore a single paired-copy residual-energy estimate, not a Schur inverse theorem.

---

# 1. Deterministic setup

Let `Omega` be a finite probability space.  Let `p` be a positive probability law and let

\[
\Phi:\Omega\to\mathbf R^m
\]

be the selected feature vector.  Write

\[
\mu=\mathbf E_p\Phi,
\qquad
\Sigma=\operatorname{Cov}_p(\Phi).
\]

All statements can be read on the active feature quotient if a redundant feature is present; in the odd-order random-circulant system used throughout this line the inherited Newton systems are nondegenerate on the selected quotient.

Let `L` be a signed law of mass one carrying the exact desired target moments `t`:

\[
L(\Omega)=1,
\qquad
\mathbf E_L\Phi=t.
\]

Write its density relative to `p` as

\[
\ell={dL\over dp},
\qquad
\mathbf E_p\ell=1.
\tag{1.1}
\]

Now make any positive normalized reweighting

\[
p_+=w p,
\qquad
\mathbf E_p w=1,
\qquad
w\ge\eta>0.
\tag{1.2}
\]

Let

\[
\mu_+=\mathbf E_{p_+}\Phi,
\qquad
\Sigma_+=\operatorname{Cov}_{p_+}(\Phi),
\qquad
r_+=t-\mu_+.
\tag{1.3}
\]

The full Newton coefficient is

\[
h_*:=\Sigma_+^{-1}r_+,
\tag{1.4}
\]

and the full decrement is

\[
\nu_+^2=r_+^T\Sigma_+^{-1}r_+.
\tag{1.5}
\]

Let `U_R subset R^m` be any finite Galerkin coefficient space.  Its restricted Newton coefficient `h_R in U_R` is defined by

\[
u^T\Sigma_+h_R=u^Tr_+
\qquad(u\in U_R).
\tag{1.6}
\]

Equivalently, the restricted score

\[
g_R=h_R^T(\Phi-\mu_+)
\tag{1.7}
\]

is the `L^2(p_+)` projection of any exact target score onto the corresponding centered feature subspace `K_R`.

Define

\[
\nu_R^2=h_R^T\Sigma_+h_R=r_+^Th_R.
\tag{1.8}
\]

The normal residual vector is

\[
\zeta_R:=r_+-\Sigma_+h_R.
\tag{1.9}
\]

By (1.6), `zeta_R` annihilates the Galerkin head `U_R`.

---

# 2. Exact energy-gap identity

Set

\[
e_R=h_*-h_R.
\]

Since

\[
\Sigma_+e_R=\zeta_R,
\tag{2.1}
\]

and the Galerkin normal equations give

\[
u^T\Sigma_+e_R=0
\qquad(u\in U_R),
\tag{2.2}
\]

we have the energy Pythagoras identity

\[
\begin{aligned}
\nu_+^2
&=h_*^T\Sigma_+h_*\\
&=h_R^T\Sigma_+h_R+e_R^T\Sigma_+e_R.
\end{aligned}
\]

Therefore

\[
\boxed{
\Delta_R:=\nu_+^2-\nu_R^2
=e_R^T\Sigma_+e_R
=\zeta_R^T\Sigma_+^{-1}\zeta_R.
}
\tag{2.3}
\]

This is the coordinate-free form of the Schur-complement identity from the preceding report.  If the features are split into the Galerkin head and its complement, (2.3) becomes exactly

\[
\Delta_R=\zeta_{R,\perp}^T S_+^{-1}\zeta_{R,\perp}.
\]

The new point is that the inverse in this formula is unnecessary.

---

# 3. A density floor compares centered covariances without a max-density bound

The only pointwise information required is the positive floor in (1.2).

For every coefficient vector `v`, variance has the variational representation

\[
v^T\Sigma_+v
=
\min_{c\in\mathbf R}
\mathbf E_{p_+}(v^T\Phi-c)^2.
\]

Using `p_+=wp` and `w>=eta`,

\[
\begin{aligned}
v^T\Sigma_+v
&=\min_c\mathbf E_p\bigl[w(v^T\Phi-c)^2\bigr]\\
&\ge
\eta\min_c\mathbf E_p(v^T\Phi-c)^2\\
&=\eta\,v^T\Sigma v.
\end{aligned}
\]

Hence

\[
\boxed{
\Sigma_+\succeq\eta\Sigma.
}
\tag{3.1}
\]

No upper bound on `w` is used.

Consequently, on the active feature quotient,

\[
\boxed{
\Sigma_+^{-1}\preceq\eta^{-1}\Sigma^{-1}.
}
\tag{3.2}
\]

Combining (2.3) and (3.2) already gives

\[
\Delta_R
\le {1\over\eta}\,
\zeta_R^T\Sigma^{-1}\zeta_R.
\tag{3.3}
\]

This is a previous-law preconditioning inequality.  It is source-specific because only the one vector `zeta_R` appears.

### Schur-complement version

For the same head/tail coefficient split, let `S` and `S_+` be the Schur complements of `Sigma` and `Sigma_+`.  Since

\[
z^TS_+z
=\min_x (x,z)^T\Sigma_+(x,z),
\]

(3.1) implies

\[
\boxed{S_+\succeq\eta S.}
\tag{3.4}
\]

Thus

\[
\zeta_{R,\perp}^T S_+^{-1}\zeta_{R,\perp}
\le
{1\over\eta}
\zeta_{R,\perp}^T S^{-1}\zeta_{R,\perp}.
\tag{3.5}
\]

So even if one keeps the Schur coordinates, the difficult inverse has been pushed back one positive step, where the residual has an explicit source representation.

---

# 4. The previous-law residual source

Define the signed density mismatch

\[
\boxed{
D_R
:=\ell-w(1+g_R).
}
\tag{4.1}
\]

This has a direct probabilistic meaning: `L` is the exact target signed law, while `p_+(1+g_R)=p w(1+g_R)` is the restricted Newton/Galerkin target approximation under the new positive law.

First,

\[
\mathbf E_pD_R
=
1-\mathbf E_{p_+}(1+g_R)
=0,
\tag{4.2}
\]

because `g_R` is centered under `p_+`.

Second,

\[
\begin{aligned}
\mathbf E_p[D_R\Phi]
&=t-\mathbf E_{p_+}[(1+g_R)\Phi]\\
&=t-\mu_+-\Sigma_+h_R\\
&=\boxed{\zeta_R}.
\end{aligned}
\tag{4.3}
\]

Third, if `u in U_R`, then Galerkin orthogonality gives

\[
\begin{aligned}
\mathbf E_p
\bigl[D_R\,u^T(\Phi-\mu)\bigr]
&=u^T\zeta_R\\
&=0.
\end{aligned}
\tag{4.4}
\]

The change from `mu_+` to `mu` is harmless because `E_pD_R=0`.  Hence **the old-law source `D_R` is already orthogonal to the entire Galerkin head**.  No second head subtraction is needed.

Let `F_p` denote the full centered selected-feature span in `L^2(p)`.  The `L^2(p)` projection of `D_R` onto `F_p` has coefficient vector `Sigma^{-1}zeta_R`; therefore

\[
\boxed{
\|P_{F_p}D_R\|_{L^2(p)}^2
=\zeta_R^T\Sigma^{-1}\zeta_R.
}
\tag{4.5}
\]

By (4.4), this projection lies in the old-law orthogonal complement of `K_R`.  Thus

\[
\boxed{
\|P_{F_p}D_R\|_{L^2(p)}^2
=
\|P_{F_p\cap K_R^{\perp,p}}D_R\|_{L^2(p)}^2.
}
\tag{4.6}
\]

Finally Bessel gives

\[
\|P_{F_p\cap K_R^{\perp,p}}D_R\|_2^2
\le \|D_R\|_2^2.
\tag{4.7}
\]

Combining (2.3), (3.3), and (4.5)--(4.7) proves the main theorem.

### Theorem 4.1 — floor-preconditioned residual certificate

Under (1.1)--(1.9),

\[
\boxed{
\Delta_R
\le
{1\over\eta}
\|P_{F_p\cap K_R^{\perp,p}}D_R\|_{L^2(p)}^2
\le
{1\over\eta}\mathbf E_pD_R^2.
}
\tag{4.8}
\]

This is deterministic.

The first inequality is the useful one for the random-circulant problem.  It says that the current-law inverse covariance never has to be estimated: pair the explicit residual source `D_R`, project only onto the old-law selected-feature tail, and pay the known density-floor factor `eta^{-1}`.

---

# 5. Combine with the exact-cost square lemma

The preceding report proved the current-law exact-cost update

\[
\nu_{++}
\le
\sqrt{J_R(\eta')}
+
\sqrt{{\Delta_R\over\eta'}},
\tag{5.1}
\]

where `eta'` is the floor of the next positive square and `J_R(eta')` is the scalar exact square cost of the restricted score `g_R` under `p_+`.

Insert (4.8):

\[
\boxed{
\nu_{++}
\le
\sqrt{J_R(\eta')}
+
{\|P_{F_p\cap K_R^{\perp,p}}D_R\|_{L^2(p)}
\over\sqrt{\eta\eta'}}.
}
\tag{5.2}
\]

The weaker but completely scalar form is

\[
\boxed{
\nu_{++}
\le
\sqrt{J_R(\eta')}
+
{\|D_R\|_{L^2(p)}\over\sqrt{\eta\eta'}}.
}
\tag{5.3}
\]

Equation (5.2) is the main structural progress of this run.

It replaces the old obligation

\[
\zeta_R^TS_+^{-1}\zeta_R\ \hbox{small}
\]

by the old-law source-energy obligation

\[
\|P_{F_p\cap K_R^{\perp,p}}D_R\|_2^2\ \hbox{small}.
\]

That is exactly the sort of object for which the fixed-projector Walsh/additive-collision machinery is designed: it is a paired-copy energy of one explicit canonical residual source, with no inverse matrix inside the diagram expansion.

---

# 6. Specialize to the actual `p_3` state

Retain all notation and actual finite-model statements from the previous two checkpoints.

At `p_2`, the degree-24 exact-cost square used

\[
\eta_3=0.005
\]

and produced

\[
p_3=p_2w_3,
\qquad
w_3\ge0.005.
\tag{6.1}
\]

The exact target signed law `L` is the same sharp target throughout the construction.  Relative to `p_2`, denote its explicit translated density by

\[
\ell_2={dL\over dp_2}.
\]

At the `p_3` state, take the inherited same-mask degree-32 Galerkin score `g_{32}`.  Define the **single residual source**

\[
\boxed{
D_{32}
:=\ell_2-w_3(1+g_{32}).
}
\tag{6.2}
\]

The degree-32 Galerkin equations imply

\[
D_{32}\perp_{L^2(p_2)}K_{32}.
\tag{6.3}
\]

Let

\[
\boxed{
\mathcal R_{32}
:=
\|P_{F_{p_2}\cap K_{32}^{\perp,p_2}}D_{32}\|_{L^2(p_2)}^2.
}
\tag{6.4}
\]

Then Theorem 4.1 gives the actual full-score saturation bound

\[
\boxed{
\Delta_{32,p_3}
\le 200\,\mathcal R_{32}.
}
\tag{6.5}
\]

No covariance inverse under `p_3` appears.

The preceding checkpoint already transported the degree-32 exact square cost

\[
J_{32,p_3}(0.01)
\le7.0\times10^{-11}+o_{\mathbf P}(1)
\tag{6.6}
\]

with source-sufficient failure.  Fix for the next square

\[
\eta_4=0.01.
\tag{6.7}
\]

Equations (5.2), (6.5), and (6.6) give

\[
\begin{aligned}
\nu_4
&\le
\sqrt{7.0\times10^{-11}}
+
\sqrt{{\mathcal R_{32}\over0.005\cdot0.01}}
+o_{\mathbf P}(1)\\
&<
\boxed{
8.37\times10^{-6}
+141.422\,\mathcal R_{32}^{1/2}
+o_{\mathbf P}(1).
}
\end{aligned}
\tag{6.8}
\]

This turns the next run into a concrete scalar target.  For example:

- If
  \[
  \mathcal R_{32}\le4.20\times10^{-13},
  \]
  then
  \[
  \nu_4\le1.0\times10^{-4}+o_{\mathbf P}(1).
  \]

- If
  \[
  \mathcal R_{32}\le8.67\times10^{-14},
  \]
  then
  \[
  \nu_4\le5.0\times10^{-5}+o_{\mathbf P}(1).
  \]

- If
  \[
  \mathcal R_{32}\le2.35\times10^{-14},
  \]
  then
  \[
  \nu_4\le3.0\times10^{-5}+o_{\mathbf P}(1).
  \]

These thresholds are deliberately stated for the **projected residual source energy** `mathcal R_32`, not for a worst-case operator norm.

For comparison, if one insists on the preceding report's `3/2` saturation criterion

\[
\Delta_{32}\le{1\over2}M_{32}\nu_{32}^4,
\]

then using `eta_3=0.005` and the reference value `nu_32^2≈1.26e-7` it is sufficient that

\[
\mathcal R_{32}
\le3.97\times10^{-17}M_{32}.
\tag{6.9}
\]

But (6.8) shows that **there is no reason to force this stronger relative criterion first**.  The exact-cost route can make another large absolute contraction from a much looser residual-energy bound.

---

# 7. Why this residual source is materially easier than the Schur inverse

The old target was

\[
\zeta_R^TS_+^{-1}\zeta_R.
\]

Even though only one vector `zeta_R` was involved, the inverse made every direct diagram expansion nonlocal in convolution degree.

The new object `D_R` has three simplifying properties.

### 7.1 It is explicit before inversion

At `p_3`, every factor in

\[
D_{32}=\ell_2-w_3(1+g_{32})
\]

is already part of the transported same-mask dictionary:

1. `ell_2` is the explicit translated sharp-target comparator from the degree-24 step;
2. `w_3` is a fixed quadratic polynomial of `g_24` with the fixed floor `0.005`;
3. `g_32` is a finite same-mask Galerkin score under the fixed law `p_3`.

Thus a fixed truncation of `D_32` is a finite canonical convolution word list.  The existing connected-collision theorem applies directly to its squared norm and pairings.

### 7.2 The head vanishes exactly

Equation (6.3) means every degree-32 Galerkin head coefficient cancels **before** any probabilistic estimate.  The residual energy begins in the source-specific orthogonal tail.  This is stronger than merely observing small shell increments numerically.

### 7.3 Pairing comes before inversion

To estimate `mathcal R_32`, one may first pair two copies of `D_32`, apply the old-law fixed-projector Parseval/Bessel decomposition, and only then count connected collision diagrams.  The matrix inverse that caused the preceding bottleneck is gone from the quantity being expanded.

This is the same favorable order of operations that made the earlier fixed-projector second-step theorem source-sufficient.

---

# 8. Uniform growing-depth form

The same argument is not tied to `p_3`.

Suppose at step `k` one has

\[
p_k=w_kp_{k-1},
\qquad
w_k\ge\eta_k>0,
\]

an exact sharp-target signed law `L`, and a finite Galerkin score `g_{R_k,k}` under `p_k`.  Define

\[
D_{R_k,k}
:={dL\over dp_{k-1}}
-w_k(1+g_{R_k,k}),
\tag{8.1}
\]

and the old-law projected residual energy

\[
\mathcal R_{R_k,k}
:=
\|P_{F_{p_{k-1}}\cap K_{R_k}^{\perp,p_{k-1}}}
D_{R_k,k}\|_{L^2(p_{k-1})}^2.
\tag{8.2}
\]

Then

\[
\boxed{
\Delta_{R_k,k}
\le {\mathcal R_{R_k,k}\over\eta_k}.
}
\tag{8.3}
\]

If the next exact-cost square uses floor `eta_{k+1}`, then

\[
\boxed{
\nu_{k+1}
\le
\sqrt{J_{R_k,k}(\eta_{k+1})}
+
\sqrt{{\mathcal R_{R_k,k}\over\eta_k\eta_{k+1}}}.
}
\tag{8.4}
\]

Therefore a superlinear tail follows from scalar/source estimates of the form

\[
J_{R_k,k}(\eta_{k+1})
\le C\nu_k^{2+\delta},
\tag{8.5}
\]

and

\[
\mathcal R_{R_k,k}
\le
C\eta_k\eta_{k+1}\nu_k^{2+\delta}.
\tag{8.6}
\]

No current-law `S^{-1}`, no full-score kurtosis, and no global minimum eigenvalue is required.

This is the uniform architecture to pursue.  The collision complexity is favorable: `D_{R_k,k}` is one explicit source, so its paired energy uses two source copies plus the fixed finite list of update insertions.  One does not need a worst-case estimate over all tail directions.

---

# 9. Expectation/high-probability bookkeeping

Nothing in this deterministic reduction changes the source-level probability requirement.

For each fixed source slack, all fixed analytic insertions and paired residual energies must be transported with common failure

\[
o(1/\sqrt{\log n}).
\]

The inherited published fallback remains

\[
\vartheta(G_n)\le1+4\sqrt{n\log n}
\]

outside probability at most `2/n`, followed by the trivial `theta<=n` bound on the final fallback event.  Thus, once the sharp-target one-sided certificate is obtained for each fixed slack, the expectation transfer remains available exactly as in the preceding checkpoints.

Odd cyclic order is still used.  The even-order self-inverse frequency is not treated here and no even-order extension is claimed.

---

# 10. Intermediate-obligation ledger

Full-source P07 metric remains unchanged:

\[
\sqrt n\le \mathbf E\vartheta(G_n)
\le C\sqrt{n\log\log n}.
\]

New proved partial obligations:

1. **Current-law energy gap identity**
   \[
   \Delta_R=\zeta_R^T\Sigma_+^{-1}\zeta_R.
   \]

2. **Floor covariance domination**
   \[
   \Sigma_+\succeq\eta\Sigma
   \]
   and the same domination for the corresponding Schur complements.

3. **Explicit residual-source representation**
   \[
   \zeta_R=\mathbf E_p[D_R\Phi],
   \qquad
   D_R\perp_p K_R.
   \]

4. **Inverse-free saturation certificate**
   \[
   \Delta_R
   \le\eta^{-1}
   \|P_{F_p\cap K_R^{\perp,p}}D_R\|_p^2.
   \]

5. **Two-floor exact-cost recurrence**
   \[
   \nu_{++}
   \le\sqrt{J_R(\eta')}
   +{\|P_{F_p\cap K_R^{\perp,p}}D_R\|_p
   \over\sqrt{\eta\eta'}}.
   \]

6. **Concrete `p_3` target**
   with `eta_3=0.005`, `eta_4=0.01`, and inherited `J_32<=7e-11`, it is enough to prove `mathcal R_32<=4.20e-13` to obtain another actual contraction to `nu_4<=1e-4`.

Still missing:

- the actual finite-model numerical bound on `mathcal R_32`;
- a uniform paired-residual estimate of the form (8.6);
- the final `O(log log n)` tail to the sharp fixed-slack certificate;
- explicit even-order self-inverse-frequency treatment.

---

# 11. Next attack

Spend the next useful iteration on the **paired residual source `D_32` itself**, not on a current-law inverse covariance.

1. Form
   \[
   D_{32}=\ell_2-w_3(1+g_{32})
   \]
   in the same fixed-projector coefficient dictionary already used for the degree-24 and degree-32 transports.

2. Use the exact Galerkin cancellation `D_32 perp K_32` before counting diagrams.

3. Pair two copies first and evaluate the old-law projected tail energy
   \[
   \mathcal R_{32}
   =\|P_{F_{p_2}\cap K_{32}^{\perp,p_2}}D_{32}\|_2^2.
   \]
   A direct fixed-degree evaluation is sufficient in the first pass.  There is no need for a uniform operator norm.

4. Transport the deterministic/reference value with the existing same-mask Walsh/additive-collision theorem and analytic-tail domination.  The first decisive threshold is `4.20e-13`; `8.67e-14` or `2.35e-14` gives a substantially stronger fourth bridge.

5. Once the fixed `p_3` residual energy is certified, abstract the diagram argument.  The correct uniform object is (8.2): two copies of a single exact residual source, with all Galerkin-head words canceled algebraically first.  Prove (8.6) for a polynomially growing same-mask degree list.

Do **not** return to generic `lambda_min`, max-score bounds, full-score kurtosis/Gamma, worst-case `2->4` norms, a frozen-Gibbs tail, or an independent projector model unless the residual-source route fails after a genuine attempt.

This is **PROVED PARTIAL**, not a full P07 solution.