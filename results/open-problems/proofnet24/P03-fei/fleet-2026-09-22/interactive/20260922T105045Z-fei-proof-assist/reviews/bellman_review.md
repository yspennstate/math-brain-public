# Mathematical review: occurrence credit and the phase bank

**Date:** 2026-09-22 UTC  
**Reviewed material:** `../path_a/REPORT.md`, `../path_a/CHECK.py`  
**Disposition:** No mathematical blocker found for the stated uniform-cube theorems. Full FEI remains open.  
**Review scope:** Independent review of the occurrence-credit arguments and their combination with the phase bank. The reviewer contributed the companion phase-bank derivation, so this is not an independent second authorship-free verification of that component. This is a mathematical review with a finite numerical replay, not a proof-assistant certificate or a novelty audit.

## 1. The signed occurrence-credit identity is sound

The reference used after erasing the selector must remain the marginal of the **parent** reference. The report preserves this distinction and retains its cost through

\[
T_{\rm reference}=M\sum_a\omega_a D_2(Q_a\Vert Q_*).
\]

The parent nonempty law first splits into the singleton-selector event and its complement. On the complement, the conditional-product reference factors into the nonempty residual reference and an independent selector. KL chain rule therefore gives the singleton term, mean-selector term, selector/residual mutual information, and residual KL. The mixture-KL identity and the occurrence-matching Pythagorean identity then give

\[
\Xi=E_{\rm singleton}+E_{\rm mean}+L_{\rm occ}+T_{\rm reference}
      -M\operatorname{JS}_{\omega}(P_0,P_1).
\]

In particular, the sole negative term is a genuine information quantity, not a reference correction of undetermined sign. The full-child information chain rule supplies

\[
\operatorname{JS}_{\alpha}(U_0,U_1)
 =\operatorname{JS}_{\alpha}(\operatorname{Ber}v_0,\operatorname{Ber}v_1)
   +M\operatorname{JS}_{\omega}(P_0,P_1).
\]

Both exact equalities were checked algebraically in addition to the numerical replay.

The additional full-spectrum proof is also valid. The maximum-entropy family with a prescribed empty atom and prescribed occurrence marginals is closed under deleting a coordinate: on nonempty residual sets, summing over the deleted coordinate changes only the common normalizing factor. The empty atom remains independently adjustable. Data processing and Pythagoras consequently give \(\mathcal C(U)\ge\mathcal C(E)\), where \(E\) is the erased actual law. Concavity of the maximum attainable entropy in its constraint vector then gives

\[
\mathcal C(E)\ge\sum_a\alpha_a\mathcal C(U_a)
  -\operatorname{JS}_{\alpha}(U_0,U_1).
\]

This establishes the one-sided generation payment independently of the four-term parametrization. It does not replace the parametrization when asserting the sharper nonempty-JS bound or the exact six-term drift.

## 2. The combined bank and its tree budget are valid

For uniform physical restrictions the companion phase theorem gives

\[
\mathcal P(f)-\tfrac12\sum_a\mathcal P(f_a)
 =\operatorname{JS}_{1/2}(U_0,U_1)+B^{\rm phase},
\qquad B^{\rm phase}\ge0.
\]

Adding this equality to the signed occurrence-credit identity cancels the nonempty-child JS term. This produces exactly the report's six nonnegative terms: singleton KL, mean-selector KL, selector/residual mutual information, reference-transfer KL, variance-indicator JS, and phase refund. Thus \(\mathcal M=\mathcal C+\mathcal P\) is nonnegative and a supermartingale under physical coordinate restriction.

The strong-concavity refund uses the correct coefficient:

\[
B^{\rm phase}\ge
\frac{2}{3\ln2}\operatorname{Var}_{e}(q)
+\frac{1}{6\ln2}\sum_{k\ne i}
  [I_k(f_0)-I_k(f_1)]^2.
\]

The second coefficient is one quarter of the first because an equally weighted pair has variance one quarter of its squared difference.

For every finite adaptive restriction tree, multiplying local identities by actual reach probabilities gives the claimed telescoping identities without any independence assumption on the coordinate-selection policy. Each path queries at most the original number of coordinates, so no unbounded optional-stopping argument is required. The generation budget counts positive **conditional expected drifts** of credit. It does not claim to bound the positive variation of individual realized paths. The report explicitly makes this necessary distinction.

In particular,

\[
\sum_v\pi_v[-\Xi_v]_+
\le\mathcal P(f)-\mathbb E\mathcal P(F_L)
       -\sum_v\pi_v B_v^{\rm phase}
\le\frac{2}{\ln2}J(f)
\]

is valid. The corresponding positive-transfer budget must retain the initial occurrence credit, and the report does so.

## 3. Boundary cases do not invalidate these identities

If the residual mass \(M\) is zero, both children are constants and the parent depends on at most the selector. All occurrence-credit terms vanish. If only one child has zero variance, its zero-weight conditional law is omitted. Constants and uniform-cube characters have both credit and phase zero.

For nonempty laws, the marginal polytope is the cube with the empty vertex removed: in addition to coordinate facets, it has the facet \(\sum_i r_i=1\). On that last facet all mass is on singleton sets. Thus singular cases include the singleton face as well as forced zero and forced one coordinates. The report's actual-support and relative-interior-limit conventions cover these cases. The KL comparisons cannot introduce positive actual mass outside the reference support: a forced face is shared by every feasible law with the same occurrence constraints, and positive-weight children lie inside the parent residual reference's support.

## 4. Both fixed-fraction obstructions have the stated scope

For depth-\(m\) recursive majority of three, disjoint balanced composition gives exactly

\[
I_m=(3/2)^m,\qquad H_m=4(I_m-1),\qquad
r_m=2^{-m},\qquad n_m=3^m.
\]

Writing its nonempty product-reference parameters as \(\zeta r_m\) gives

\[
H_{\max}
=mI_m-(I_m-1)\log_2\zeta
  -(n_m-I_m)\log_2(1-\zeta r_m)\ge mI_m.
\]

Consequently \(\mathcal C(R_m)/I_m\ge m-4+4/I_m\) diverges. This is a valid Boolean obstruction to an influence-only upper bound on initial occurrence credit, despite \(H_m/I_m<4\). It also rules out every universal positive constant reserve fraction at a finite center.

The sparse-suspension calculation and Taylor coefficients were separately checked. They imply that the normalized augmented defects \(a_m\) eventually decrease strictly to minus infinity. This justifies the simultaneous comparison with **all** earlier \(a_r\), not merely with \(a_{m-1}\), and proves failure of every old-coordinate root block. Blocks containing the suspension coordinate use the expressly stated hypothesis that the ordinary potential is valid on all remaining AND/OR children. That hypothesis is necessary for the particular every-block conclusion and is not silently assumed to follow from a finite center.

The report correctly distinguishes these examples. Sparse suspension proves the fixed-reserve and every-block obstruction, but its ordinary influence tends to one; it does not establish unbounded \(\mathcal C/I\). Recursive majority establishes the latter statement. Also, \(\mathcal P\ge0\) immediately transfers failure of a universally nonnegative reserve to \(\lambda(\mathcal C+\mathcal P)\); by itself it does not transfer an every-block drift comparison. The final text explicitly makes this scope distinction; the requested clarification is resolved.

## 5. Independent finite replay

The supplied checker was copied to a temporary directory and executed there, leaving the source report, source checker, and author's result file untouched. Results are recorded in `bellman_replay.json` with source hashes.

| Check | Replay result |
|---|---:|
| Boolean functions | 1,307 |
| Local physical selectors | 25,874 |
| Complete adaptive trees | 1,195 |
| Largest signed-identity error | \(1.45\times10^{-15}\) |
| Largest JS-split error | \(1.23\times10^{-15}\) |
| Largest six-term identity error | \(1.34\times10^{-15}\) |
| Largest tree-identity error | \(1.78\times10^{-15}\) |
| Minimum phase-refund margin | 0 |
| Depth-two recursive-majority entropy | 5 |
| Depth-two recursive-majority influence | 2.25 |
| Depth-two recursive-majority credit | 2.170812831054787 |

The 160-digit sparse-family check also reproduces the reported negative root defect and negative normalized drift for all old-coordinate block sizes at \(c=7,\lambda=0.1,m=100\). The checker properly leaves blocks containing the suspension coordinate to the analytic conditional theorem. Numerical entropy and numerical I-projection computations are sanity checks; the arbitrary-dimension conclusions depend on the proofs.

The optional biased corollary uses a previously cited weighted two-point inequality. This review checked the algebraic reduction and telescoping, but did not independently re-audit that external theorem. The final text defines \(V_s=4s(1-s)\) and the physical disagreement probability \(d=\Pr[f_0\ne f_1]\), so \(\operatorname{It}_i=V_s d\); the requested notation clarification is resolved.

## 6. Unresolved mathematical step

The combined bank pays for newly generated occurrence credit and exposes where its releases go. It does not show that rare-event packet entropy is paid at influence cost, and it does not construct a universally valid state-dependent reserve or stopping policy. An arbitrarily large initial occurrence credit also prevents interpreting this bank as an influence-bounded total resource. The report states these limitations accurately. Nothing reviewed here establishes full FEI, a formal certificate, or external novelty.
