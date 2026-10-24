# account02/B13 — selector-conditional transport of biased Booleanity

**Assignment:** FEI-20260922-account02-B13, “Biased conditional Booleanity”.  
**Classification:** `PROVED_AUXILIARY / SOURCE-EXACT_SELECTOR_IDENTITY / CONDITIONAL_KL_CREDIT`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Source state and first missing implication

Startup control head was `yspennstate/math-research-brain@44927cd22ee7400eac02d182a370cc21db27f283`, owner revision `2026-09-22.3`; the prepublication refresh reached `01a20e14899387e8d0029d2b5ad90d65b0152ba3` with the same owner revision and an empty correction inbox. The all-team state keeps full uniform-cube FEI open and retires the fixed-potential, raw-U4, unweighted-L2 and fixed-depth-KL shortcuts at their stated scopes.

The exact assignment asks for the biased multiplication equations to survive a genuine physical selector restriction with all conditional signs intact, and for a quantitative consequence that does not pay the global selector operator norm. The first missing implication was therefore:

> Given a selector coordinate `j`, can the parent quadratic Booleanity equations be reorganized exactly into the two actual child Booleanity systems, and can the resulting child dependence KL be inserted into the spectral entropy recursion without the extra factor `L_j^2=max(t,1-t)/min(t,1-t)`?

The answer is yes. The theorem below is auxiliary rather than FEI closure: it produces a source-exact conditional Booleanity/KL bank, but does not yet prove that this bank pays every surviving Bellman deficit.

## 1. Sources consumed

The base Booleanity theorem is account04/B17,

`yspennstate/math-open-problems@603b35e74227d1c2d8ee34c0c527c439c686e30:proofnet24/P03-fei/fleet-2026-09-21/account04/B17/20260922T092422Z-biased-booleanity-gap/REPORT.md`.

For product bias `p`, normalized basis `phi_i=(x_i-p_i)/sqrt(p_i(1-p_i))`, and multiplication matrices `M_U`, it proves for every Boolean gate

`a^T M_U a=0` for nonempty `U`, and for the nonempty spectral I-projection `Q_r`

\[
K_{\rm occ}\ge {\mathfrak g_U^2\over 4vL_U^2\ln2},
\qquad
L_U=\prod_{i\in U}\sqrt{\max(p_i,1-p_i)\over\min(p_i,1-p_i)}.
\tag{1.1}
\]

The exact I-projection identity is account02/B15,

`yspennstate/math-open-problems@4bd6d05f1eb8325d665f2748f4d74dcee2550a04:proofnet24/P03-fei/fleet-2026-09-21/account02/B15/20260922T0829Z-influence-iprojection-kl/REPORT.md`,

which gives `K_occ=H_max(r)-H(P)` for the actual nonempty spectral law with its original-coordinate occurrence marginals.

The named completed **other-account partner** result actually used is account03/B13,

`yspennstate/math-open-problems@a04dec15aa083216c437d1327aba981f5c8dbab8:proofnet24/P03-fei/fleet-2026-09-21/account03/B13/20260922T093915Z-safe-direction-coercivity/REPORT.md`.

It proves for the universally safe direction

\[
\eta(p)=2V_p-V_p^2-\varepsilon V_p^3,
\qquad \varepsilon={113009\over5000000},
\tag{1.2}
\]

a physical-selector local currency `L_j` satisfying, with selector disagreement `delta=Pr(G_0!=G_1)`,

\[
L_j\ge r_0V_t\,\delta(1-\delta),
\qquad
r_0={1999313322941\over16492674416640000000}>0.
\tag{1.3}
\]

Equation (1.3) is used below on the same selector as the new conditional KL bank.

## 2. Exact selector restriction identity

Fix a physical selector `j` with interior bias

\[
t=p_j,\qquad q=1-t,
\]

and residual product bias `p'`. Let `G_0,G_1` be the two **actual Boolean restrictions**. Write their biased Fourier coefficient vectors over residual subsets as

\[
u=(u_S),\qquad v=(v_S).
\]

If the parent coefficients are split into the coefficient without `j`, `x_S`, and with `j`, `y_S`, direct evaluation of the normalized one-bit basis gives

\[
\boxed{x_S=qu_S+tv_S,\qquad y_S=\sqrt{tq}\,(v_S-u_S).}
\tag{2.1}
\]

For every residual subset `U`, define the normalized multiplication defect

\[
E_U(z):=z^TM_Uz-\mathbf 1_{U=\varnothing}.
\tag{2.2}
\]

Thus a unit coefficient vector is Boolean exactly when `E_U=0` for every `U` (the empty equation is normalization, the nonempty equations are the Boolean multiplication equations).

### Theorem 2.1 — exact two-child transport

For every residual `U` including `U=empty`,

\[
\boxed{E_U(G)=qE_U(u)+tE_U(v),}
\tag{2.3}
\]

where on the left `U` is viewed as not containing `j`, and

\[
\boxed{E_{U\cup\{j\}}(G)=\sqrt{tq}\,[E_U(v)-E_U(u)].}
\tag{2.4}
\]

Consequently

\[
\boxed{
E_U(G)^2+E_{U\cup\{j\}}(G)^2
=qE_U(u)^2+tE_U(v)^2.
}
\tag{2.5}
\]

In particular, the parent Booleanity system is equivalent to the simultaneous Booleanity systems of the two physical children; no sign-free relaxation is used.

### Proof

For a residual target `U`, the selector tensor factor of `M_U` is the identity. Substituting (2.1) and cancelling the cross terms yields

\[
x^TM_Ux+y^TM_Uy=q\,u^TM_Uu+t\,v^TM_Uv,
\]
which is (2.3), including the normalization subtraction for `U=empty`.

For `U union {j}`, the selector factor is

\[
A_j=\begin{pmatrix}0&1\\1&\kappa_j\end{pmatrix},
\qquad
\kappa_j={1-2t\over\sqrt{tq}}.
\]

Hence the parent quadratic form is

\[
2x^TM_Uy+\kappa_jy^TM_Uy.
\]
Substitution of (2.1) simplifies exactly to

\[
\sqrt{tq}\,(v^TM_Uv-u^TM_Uu),
\]
which is (2.4); the constants cancel when `U=empty`. Finally (2.5) is the scalar variance identity

\[
(qe_0+te_1)^2+tq(e_1-e_0)^2=qe_0^2+te_1^2.
\]
QED.

The point of (2.5) is that the average equation and the selector-difference equation must be kept **together**. Treating only one of them permits cancellation of the two child violations; their squared pair recovers the branch-weighted child energy exactly.

## 3. Quantitative conditional Booleanity credit with no selector norm inflation

For child `b in {0,1}`, let

\[
\mu_b=u^{(b)}_\varnothing,\qquad
v_b=1-\mu_b^2.
\]

When `v_b>0`, let `P_b` be its actual nonempty spectral law, `Q_b` the B15 maximum-entropy I-projection with the same occurrence marginals, and

\[
K_b=D_{\rm KL,2}(P_b\Vert Q_b).
\]

For a residual nonempty `U`, define the child signed reference gap exactly as in account04/B17,

\[
g_{b,U}:=\min_{\sigma}
\left|(b_b^\sigma)^TM_Ub_b^\sigma\right|,
\tag{3.1}
\]

where the empty coefficient is the **actual signed** child mean and the nonempty magnitudes are `sqrt(v_b Q_b(S))`. If a child is constant, set `v_bK_b=g_{b,U}=0`.

Build a parent reference from any pair of child sign choices using the same physical selector transform (2.1). Let its two parent residuals at `U` and `U union {j}` be `A_U,B_U`, and define the paired selector gap

\[
\mathfrak c_{j,U}^2:=
\min_{\sigma_0,\sigma_1}(A_U^2+B_U^2).
\tag{3.2}
\]

By (2.5), the minimization separates exactly:

\[
\boxed{
\mathfrak c_{j,U}^2=qg_{0,U}^2+tg_{1,U}^2.
}
\tag{3.3}
\]

Multiplying the source inequality (1.1) by each child variance and averaging gives the main quantitative consequence.

### Theorem 3.1 — selector-conditional KL bank

For every genuine Boolean selector restriction, every interior selector bias and every residual nonempty `U`,

\[
\boxed{
qv_0K_0+tv_1K_1
\ge
{\mathfrak c_{j,U}^2\over4L_U^2\ln2}.
}
\tag{3.4}
\]

Therefore

\[
\boxed{
qv_0K_0+tv_1K_1
\ge {1\over4\ln2}
\max_{U\ne\varnothing}{\mathfrak c_{j,U}^2\over L_U^2}.
}
\tag{3.5}
\]

The crucial normalization fact is that **`L_U`, not `L_{U union {j}}`, appears**. A direct application of the parent theorem to a selector-containing equation would pay

\[
L_{U\cup\{j\}}^2
=L_U^2{\max(t,q)\over\min(t,q)},
\]
which diverges at a rare selector bias. Conditionalizing first removes that artificial selector operator-norm inflation; only the physical branch weights `q,t` remain.

This does **not** identify the left side with the parent `K_occ`. It is the exact dependence-KL already present inside the two child defects of the physical restriction recursion. That distinction is essential.

## 4. Exact spectral conditional-entropy recursion

The same selector transform gives an entropy identity that inserts (3.4) without discarding the child signs.

For each residual spectral label `S`, put

\[
m_S=qu_S^2+tv_S^2,
\quad
\theta_S={tv_S^2\over m_S},
\quad
\psi_S={tq(v_S-u_S)^2\over m_S}
\tag{4.1}
\]
when `m_S>0`. Define two joint laws with common `S` marginal `m_S`:

\[
R(B=0,S)=qu_S^2,\qquad R(B=1,S)=tv_S^2,
\]

and

\[
P(J=0,S)=x_S^2,\qquad P(J=1,S)=y_S^2.
\]

The `J` law is exactly the parent squared biased-Fourier law. The quantity `psi_S` contains the signed interference term `-2u_Sv_S`; this is where the conditional Fourier signs are retained.

Let `Htilde` denote spectral entropy in the normalized biased basis. Since the selector transform is orthogonal on each two-dimensional fibre,

\[
\boxed{
\widetilde H(G)
=h_2(t)+q\widetilde H(G_0)+t\widetilde H(G_1)
+H(J\mid S)-H(B\mid S).
}
\tag{4.2}
\]

This is an equality, not a continuity bound.

For each nonconstant child,

\[
\widetilde H(G_b)
=h_2(v_b)+v_bH(P_b)
=h_2(v_b)+v_bH_{\max}(r_b)-v_bK_b.
\tag{4.3}
\]

Combining (4.2), (4.3) and (3.5) gives the requested arbitrary-bias entropy credit:

\[
\boxed{
\begin{aligned}
\widetilde H(G)
\le{}& h_2(t)
+q\,[h_2(v_0)+v_0H_{\max}(r_0)]
+t\,[h_2(v_1)+v_1H_{\max}(r_1)]\\
&+H(J\mid S)-H(B\mid S)\\
&-{1\over4\ln2}
\max_{U\ne\varnothing}{\mathfrak c_{j,U}^2\over L_U^2}.
\end{aligned}
}
\tag{4.4}
\]

No ambient dimension, selector condition number, affine gauge or sign-free relaxation appears. The signed conditional term `H(J|S)-H(B|S)` is kept exactly; it is not replaced by its absolute value.

## 5. Substantive use of the named account03/B13 partner theorem

Apply account03/B13's safe-direction theorem to **the same physical selector**. Their displayed local lower bound and its one-variable minimization give

\[
L_j\ge r_0V_t\delta(1-\delta),
\qquad
\delta=\Pr(G_0\ne G_1).
\tag{5.1}
\]

Therefore whenever a gate argument augments a candidate by `lambda eta`, the exact selector recursion retains two independent nonnegative reserves:

1. the weighted child dependence KL from (3.5), and
2. the local safe-direction currency `lambda L_j`.

For every residual nonempty `U`,

\[
\boxed{
qv_0K_0+tv_1K_1+\lambda L_j
\ge
{\mathfrak c_{j,U}^2\over4L_U^2\ln2}
+\lambda r_0V_t\delta(1-\delta).
}
\tag{5.2}
\]

This is the exact expression from the partner result that changes the present target: a rare selector no longer forces a choice between an operator-norm-damped Booleanity certificate and the safe-direction reserve. Both live on the same physical restriction and can be retained simultaneously.

Equation (5.2) is still auxiliary. It does not assert that the current shaped candidate is universally nonnegative, and it does not prove FEI.

## 6. Deterministic sanity check

`CHECK.py` is standard-library only. It exhausts all `256` Boolean functions of three variables, treats the first variable as the physical selector, uses residual biases `(0.29,0.63)` and selector biases `0.17,0.37,0.81`, and checks the coefficient transform, both defect identities, the Pythagorean identity, the conditional entropy identity, and the conditional KL lower bound with brute-force sign minimization of the two child reference gaps.

Captured output:

```
PASS
identity_cases 768
credit_cases 2304
max_transform_error 3.331e-16
max_defect_energy_error 6.661e-16
max_entropy_identity_error 1.332e-15
max_credit_violation 8.219e-17
```

The analytic proof does not depend on this finite check.

## 7. What changed and the next unpaid implication

**Target-level change:** the exact selector restriction now transports the entire arbitrary-bias quadratic Booleanity system to both actual children, with a Pythagorean no-cancellation identity. The child I-projection dependence credits enter the parent entropy recursion with the quantitative bank (3.5), and the extra selector condition number is eliminated.

**Mechanism-level change:** instead of applying a single parent quadratic equation with its global operator norm, this run conditions on the physical selector, uses the two parent equations as an orthogonal pair, and performs the entropy/KL decomposition inside the two genuine Boolean children before reassembling them.

**Still unpaid:** prove that the retained bank in (4.4), together with the exact first-moment/potential and hierarchy terms, pays every negative all-gate Bellman residual, or construct a genuine Boolean gate/bias showing that even this selector-conditional bank is quantitatively insufficient. In particular, the remaining issue is a **reference-change / deficit-comparison theorem**, not transport of Booleanity through restriction and not selector norm inflation.

Full uniform-cube FEI remains **OPEN / NOT PROVED**.
