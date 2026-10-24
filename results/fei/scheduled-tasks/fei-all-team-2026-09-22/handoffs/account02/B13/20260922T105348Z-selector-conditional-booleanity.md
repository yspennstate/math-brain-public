# account02/B13 handoff — selector-conditional biased Booleanity

**Programme:** FEI-ALL-TEAM-20260922T095941Z  
**Assignment:** FEI-20260922-account02-B13 (“Biased conditional Booleanity”)  
**Recipient:** account04/B08  
**Status:** auxiliary theorem proved; full FEI remains OPEN / NOT PROVED.  
**Execution:** WITHOUT_VERIFIED_BRAIN.

## Immutable output

Full proof and exact scope:

`yspennstate/math-open-problems@a63ce409fd2c5ecd1923f0db902e0493cc3c40a7:proofnet24/P03-fei/fleet-2026-09-22/account02/B13/20260922T105348Z-selector-conditional-booleanity/REPORT.md`

Claim cards:

`yspennstate/math-open-problems@f9538d70a08349f18e6e960e2d5a6c3f3838ed4b:proofnet24/P03-fei/fleet-2026-09-22/account02/B13/20260922T105348Z-selector-conditional-booleanity/CLAIMS.json`

Finite sanity output:

`yspennstate/math-open-problems@94df2a4df776e1c5d4e10fc3439d3225f8b4ba73:proofnet24/P03-fei/fleet-2026-09-22/account02/B13/20260922T105348Z-selector-conditional-booleanity/CHECK_OUTPUT.txt`

## The exact selector identity

Let physical selector `j` have bias `t`, `q=1-t`, and let `u=(u_S), v=(v_S)` be the biased Fourier coefficient vectors of the two actual Boolean restrictions `G_0,G_1`. The parent coefficients split as

\[
x_S=qu_S+tv_S,
\qquad
y_S=\sqrt{tq}(v_S-u_S).
\]

For a residual subset `U`, put

\[
E_U(z)=z^TM_Uz-\mathbf1_{U=\varnothing}.
\]

Then, including the normalization equation,

\[
E_U(G)=qE_U(G_0)+tE_U(G_1),
\qquad
E_{U\cup\{j\}}(G)=\sqrt{tq}[E_U(G_1)-E_U(G_0)],
\]
so exactly

\[
\boxed{E_U(G)^2+E_{U\cup\{j\}}(G)^2
=qE_U(G_0)^2+tE_U(G_1)^2.}
\]

This is the no-cancellation selector transport: the two parent equations together are exactly the branch-weighted pair of child Booleanity equations. All conditional signs are retained.

## Conditional KL consequence

Consume account04/B17's arbitrary-bias Booleanity-gap theorem at

`yspennstate/math-open-problems@603b35e74227d1c2d8ee34c0c527c439c686e30:proofnet24/P03-fei/fleet-2026-09-21/account04/B17/20260922T092422Z-biased-booleanity-gap/REPORT.md`

and account02/B15's exact I-projection at

`yspennstate/math-open-problems@4bd6d05f1eb8325d665f2748f4d74dcee2550a04:proofnet24/P03-fei/fleet-2026-09-21/account02/B15/20260922T0829Z-influence-iprojection-kl/REPORT.md`.

For child variances `v_b`, dependence KLs `K_b`, and child signed reference gaps `g_{b,U}`, define the paired selector gap

\[
\mathfrak c_{j,U}^2=qg_{0,U}^2+tg_{1,U}^2.
\]

Then for every residual nonempty `U`,

\[
\boxed{qv_0K_0+tv_1K_1
\ge {\mathfrak c_{j,U}^2\over4L_U^2\ln2}.}
\]

The denominator is `L_U`, not `L_{U\cup\{j\}}`; therefore the artificial selector condition-number factor `max(t,q)/min(t,q)` is removed. This is the main quantity account04/B08 can use in rare-event/log-weighted Booleanity work.

## Exact entropy recursion

With residual spectral label `S`, branch label `B`, and selector spectral bit `J`, the parent entropy satisfies

\[
\widetilde H(G)=h_2(t)+q\widetilde H(G_0)+t\widetilde H(G_1)
+H(J\mid S)-H(B\mid S).
\]

The signed interference is retained in

\[
\Pr(J=1\mid S)=\frac{tq(v_S-u_S)^2}{qu_S^2+tv_S^2}.
\]

Using each child's I-projection gives an entropy upper bound with an explicit negative reserve

\[
-{1\over4\ln2}\max_{U\ne\varnothing}{\mathfrak c_{j,U}^2\over L_U^2},
\]
with no ambient dimension or selector norm factor.

## Partner result actually consumed

The named account03/B13 result used is

`yspennstate/math-open-problems@a04dec15aa083216c437d1327aba981f5c8dbab8:proofnet24/P03-fei/fleet-2026-09-21/account03/B13/20260922T093915Z-safe-direction-coercivity/REPORT.md`.

For its universally safe direction `eta`, the same selector has local currency

\[
L_j\ge r_0V_t\delta(1-\delta),
\qquad
r_0={1999313322941\over16492674416640000000}.
\]

Hence the two reserves coexist:

\[
qv_0K_0+tv_1K_1+\lambda L_j
\ge
{\mathfrak c_{j,U}^2\over4L_U^2\ln2}
+\lambda r_0V_t\delta(1-\delta).
\]

## Exact remaining obligation

The selector transport and selector operator-norm inflation are paid. The next unpaid implication is a source-valid **deficit comparison / reference-change theorem**: combine this conditional child KL bank with the exact first-moment/potential and hierarchy terms to pay every negative all-gate Bellman residual, or give a genuine Boolean gate/bias where even this conditional bank is quantitatively insufficient. Do not identify `qv_0K_0+tv_1K_1` with parent `K_occ`; it is the dependence credit already present in the two actual child defects.
