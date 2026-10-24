# account01/B13 handoff — common-sign entropic Booleanity

**Programme:** FEI-ALL-TEAM-20260922T095941Z  
**Control revision:** 2026-09-22.3  
**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

Full source:
`yspennstate/math-open-problems@b68d5296c4bc8e74241ff8211552f272dda67972:proofnet24/P03-fei/fleet-2026-09-22/account01/B13/20260922T105801Z-common-sign-kl-projection/REPORT.md`

## New theorem

For fixed product bias, output mean/variance and original-coordinate spectral occurrence marginals `r`, let `Q_r` be the maximum-entropy nonempty I-projection. Let `B(p,q,r)` be the laws `R` with marginals `r` for which **one common Fourier sign vector** makes all biased Boolean multiplication equations hold simultaneously. Define

\[
K_{\rm com}(p,q,r)=\inf_{R\in B(p,q,r)}D_2(R\Vert Q_r).
\]

Then for every actual Boolean gate

\[
K_{\rm occ}\ge K_{\rm com}
\ge {1\over4v\ln2}\max_{U\ne\varnothing}{g_U^2\over L_U^2}.
\]

The first inequality is exact feasibility of the actual source; the second uses the same-sign comparison to `Q_r` plus Hellinger-to-KL. Unlike the old max-gap certificate, signs are not reoptimized independently for each equation.

## Decisive sparse-suspension calculation

For
\[
F_m(y,x)=y(1-2\mathbf1_{x=0}),\qquad p=2^{1-m},
\]
the occurrence condition forces the fresh coordinate always active and all old influences equal `p`. Any common-sign feasible Boolean source factors as `chi_y h(x)`. Each old direction has exactly one bichromatic edge. Cube edge-isoperimetry then forces the smaller sign class of `h` to have size one. Hence the magnitude law is uniquely the one-point-defect spectrum and

\[
K_{\rm com}=K_{\rm occ}=m h_2(p)-H(P_m).
\]

For `m>=5`,
\[
K_{\rm com}\ge (m-1)(m-5)p,
\qquad I(F_m)-1=mp.
\]
Thus `K_com/(I-1)` grows linearly.

By contrast, for every individual Booleanity equation the independent-sign gap satisfies `g_U^2<=4p`, so the old max-gap certificate is at most `p/ln2` and its ratio to `I-1` is at most `1/(m ln2)->0`. Therefore the common-sign entropic certificate provably retains the rare-event logarithm that independent sign minimization and unweighted L2 lose.

## Partner result actually applied

Consumed account02/B13:
`yspennstate/math-open-problems@a1b98a69cf168e8005c06190b71e76b456ad2cc9:proofnet24/P03-fei/fleet-2026-09-22/account02/B13/20260922T105348Z-selector-conditional-booleanity/REPORT.md`.

For its physical selector `j` of bias `t`, the new child banks satisfy
\[
(1-t)v_0K_0+t v_1K_1
\ge (1-t)v_0K_{{\rm com},0}+t v_1K_{{\rm com},1}
\]
and the right side still dominates the partner paired gap
\[
{1\over4\ln2}\max_U {c_{j,U}^2\over L_U^2},
\]
without reintroducing the selector condition-number factor. Safe-direction currency can be added unchanged.

## Next unpaid implication

Lower-bound `K_com` by the actual negative first-moment Bellman residual for every gate/bias of a surviving candidate, or prove that selector recursion plus the child `K_com` banks necessarily supplies that payment. Any tractable relaxation must lose at most `O(I)` on sparse suspensions; a fixed unweighted quadratic compression cannot suffice.

Full FEI remains OPEN / NOT PROVED.
