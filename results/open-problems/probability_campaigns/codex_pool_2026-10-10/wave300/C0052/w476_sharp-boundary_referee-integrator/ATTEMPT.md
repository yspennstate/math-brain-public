# C0052 referee and boundary calculation

2026-10-10. This packet audits auxiliary claims and proves a one-dimensional special case. It does not solve C0052. Current openness of the three-dimensional target is UNKNOWN after the bounded source check.

## Exact target and quantifiers

Duminil-Copin, *Lectures on the Ising and Potts models on the hypercubic lattice*, printed p. 94, eqs. (7.1)-(7.2) and Conjecture 6, defines the signed coupling

    g_d(beta) = [sum_{x2,x3,x4} U4(0,x2,x3,x4)]/[chi(beta)^2 xi(beta)^d].

Here chi is the sum of the infinite-volume two-point function and xi is its inverse exponential decay rate along e1, for beta below beta_c. The 3D target is that g_3(beta) does not tend to zero as beta increases to beta_c. The four-point Ursell function is nonpositive in the ferromagnetic Ising model. Thus the operational target only asks for a subsequence along which -g_3 remains positive. A full positive liminf is stronger. The source's prose also discusses a non-Gaussian spin-field scaling limit; that prose does not by itself prove existence or uniqueness of such a limit.

The 2021 Aizenman--Duminil-Copin Annals paper proves Gaussian scaling limits for the separate 4D Ising case. It does not prove the 3D statement. The September intake C0052-A001 leaves the second moment of current intersections uncontrolled. Its dimension heuristic and asserted equivalence are not a proof.

## Own lemma: exact one-dimensional coupling

For the zero-field nearest-neighbor Ising model on Z at any finite beta>0, let t=tanh beta, q=e^(-2 beta)=(1-t)/(1+t), and use the same definitions of chi, xi and g with d=1. Then

    chi=1/q=(1+t)/(1-t),
    xi=1/(-log t),
    sum_{x2,x3,x4} U4(0,x2,x3,x4)=q^(-1)-3q^(-3),
    g_1(beta)=(-log t)(q-3/q),
    lim_{beta->infinity} g_1(beta)=-6.

Proof. The zero-field 1D two-point function is G(0,x)=t^|x|. Summing it and reading its exponential decay rate give chi and xi. Let f(h) be the infinite-volume pressure per site in a uniform external field, minus f(0). The leading transfer-matrix eigenvalue is

    lambda_+(h)=e^beta [cosh h+sqrt(sinh^2 h+q^2)].

Differentiating log lambda_+ gives the magnetization

    f'(h)=sinh h/sqrt(sinh^2 h+q^2)
         =h/q+(1/q-3/q^3)h^3/6+O(h^5).

At fixed beta, finite-state transfer-matrix analyticity and exponential mixing justify termwise fourth differentiation of pressure and the absolutely convergent cumulant sum. Hence f''''(0)=sum U4=q^(-1)-3q^(-3). Substitution yields the exact expression for g_1. Finally (-log t)/q=(-log t)(1+t)/(1-t) tends to 2 and (-log t)q tends to 0 as t increases to 1, so g_1 tends to -6. At beta=0, the cumulant density limit is -2, independently checking the algebra (xi is undefined exactly there).

This is a sharp, dimension-specific boundary case. It also shows that vanishing single-site/contact fractions do not force the whole coupling to vanish: the distinct-site contribution remains order one in this 1D scaling regime. The limit beta_c=+infinity in one dimension; no step transfers its value to finite-beta_c 3D Ising.

## Referee findings

REVIEW.jsonl records scoped KEEP verdicts for w474-L1 and w475's contact and sprinkling bridge claims. The bridge is an exact counterexample to a uniform reverse sprinkling comparison on all finite graphs; it is not a counterexample to nearest-neighbor critical Z^3. The hardest load-bearing gap remains a scale-uniform lower bound on the weighted distinct-site four-point/current-intersection observable relative to block variance squared, or a different route controlling its full limit. The owner memory `perceptron_proof_open_gaps_fleet_2026_07_12` warns that a completed pipeline or local sublemma is not proof completion; `proof_steps_need_derived_joint_structure_2026_09_09` warns against multiplying dependent conditional bounds. Both apply to the attempted second-moment route.

NEXT: Independent referee w479 should check the transfer-matrix lemma; then integrate only scoped source correction and reviewed auxiliary results into a draft math-brain bundle.
