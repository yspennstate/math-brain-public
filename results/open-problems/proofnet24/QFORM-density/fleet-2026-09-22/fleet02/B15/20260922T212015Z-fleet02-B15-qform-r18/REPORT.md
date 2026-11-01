SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B15, 2026-09-22T21:20:15Z.
attacking: direct physical-coordinate definite-pair density payment, with continuity treated separately via a third uncoupled quadratic coordinate.

# fleet02/B15 r18 — a definite physical pair pays the density directly

Status: supporting theorem proved below; full QFORM remains OPEN. This report does not use continuity to infer the L-infinity bound.

## Fresh source state and corrections


Completed assigned-partner result actually applied: fleet03/B15 run 20260922T202624Z-fleet03-B15-qform-r17, handoff blob c2461fc4dd2174c1c47003eaf26eb5ff64b34c5a, canonical proof yspennstate/math-open-problems@fd40f8241efcd355b798669de5a0421f8f25e1d0. Its exact spectral normalization says the sharp full constant equals the supremum on s_3(A)=1, and smooth generic boundary instances approximate the sharp constant. I use this only to identify what the present local theorem does and does not eliminate: exact algebraic zeros may be genericized away in an extremizing sequence, whereas uniformly positive physical 2x2 determinant is a quantitative open condition and remains meaningful.

## First unpaid implication

The full target asks for one finite C with

    sup_{target A, independent f_i<=1} ||p_{X^T A X}||_infinity <= C.

Absolute continuity alone does not pay this. The theorem below pays it directly on an exact structural branch, before any continuity argument.

## Lemma 1: two-dimensional definite shell bound

Let U,V be independent real variables with probability densities bounded by 1. Let

    Z = (U,V) B (U,V)^T + l_1 U + l_2 V + c,

where B is a real symmetric positive- or negative-definite 2x2 matrix. Then Z has a density satisfying

    ||p_Z||_infinity <= pi / sqrt(|det B|).                    (1)

Proof. Complete the square in R^2. Translation of (U,V) preserves independence and the density caps, while an output translation is irrelevant. After reflecting the output in the negative-definite case, it suffices to take B positive definite and Z=x^T Bx. The shifted joint density is at most 1 pointwise. For every interval I,

    P(Z in I) <= |{x in R^2 : x^T Bx in I}|.

The sublevel ellipse has area

    |{x:x^T Bx<=t}| = pi t / sqrt(det B),   t>=0.

Therefore every shell over an interval I has area at most pi|I|/sqrt(det B). Hence the pushforward measure is dominated by (pi/sqrt(det B)) times Lebesgue measure, which proves (1). No moment, support, smoothness, or rotated-independence assumption is used. QED.

## Theorem 2: direct full-matrix payment from one physical definite pair

Let X_1,...,X_n be independent with densities <=1 and A symmetric. Suppose some original-coordinate principal block

    B=A_{\{i,j\},\{i,j\}}

is definite. Then the FULL quadratic form Q=X^TAX has a density and

    ||p_Q||_infinity <= pi / sqrt(|det B|).                    (2)

In particular, if |det B|>=1, then ||p_Q||_infinity<=pi, independent of dimension and every other coefficient of A.

Proof. Condition on all coordinates W outside {i,j}. For each fixed W=w, Q is exactly a two-variable quadratic with quadratic part B and arbitrary affine terms induced by the cross couplings to W. The conditional law of (X_i,X_j) is still the original product law, so Lemma 1 gives the same bound (1), uniformly in w. Averaging the conditional measures preserves the domination by that same constant times Lebesgue measure. QED.

A useful special case is a same-sign uncoupled physical pair: if A_ij=0 and A_ii,A_jj have the same sign, then

    ||p_Q||_infinity <= pi / sqrt(|A_ii A_jj|).

Thus two same-sign physical diagonal curvatures of magnitude at least one already pay the full target height pi even when those coordinates are coupled arbitrarily to all outside coordinates. This strictly extends the separable pi argument to a nonseparable ambient matrix.

## Proposition 3: continuity is a separate extra conclusion

Assume Theorem 2 and, in addition, there is a third original coordinate k such that

    A_ik=A_jk=0,     A_kk != 0.

Then p_Q has a representative in C_0(R), while retaining the independent quantitative bound (2).

Proof. Condition on every coordinate outside {i,j,k}. For fixed outside data w, the selected quadratic splits as an independent sum H_w+G_w: H_w is the definite two-coordinate quadratic from Lemma 1, and G_w is a nondegenerate one-dimensional affine quadratic in X_k. The density h_w of H_w belongs to L^1 cap L^infinity with ||h_w||_infinity<=M:=pi/sqrt(|det B|). The scalar quadratic G_w is absolutely continuous, so its density g_w lies in L^1 with norm one.

For p_w=h_w*g_w, continuity follows from

    sup_t |p_w(t+s)-p_w(t)| <= ||h_w||_infinity ||tau_s g_w-g_w||_1 ->0.

Also p_w vanishes at infinity: approximate g_w in L^1 by a bounded compactly supported function; the convolution error is at most M times the L^1 approximation error, while convolution of an L^1 function h_w with a bounded compactly supported function tends to zero at infinity. Hence p_w is in C_0 and 0<=p_w<=M.

Finally p_Q(t)=E_w p_w(t). Dominated convergence with bound M gives continuity and vanishing at infinity after mixing over w. QED.

This order is intentional: (2) is proved first from shell volume; continuity is then derived separately and is not used to obtain the height bound.

## Exact implication ledger and controls

For every nonzero symmetric A and every absolutely continuous joint input law, q(x)=x^TAx has an absolutely continuous pushforward: by coarea on bounded boxes, the inverse image of a one-dimensional null set is null away from the critical space ker A, and ker A itself is Lebesgue-null. This is qualitative only.

The reverse implications fail in general. If X is Uniform[0,1], X^2 is absolutely continuous with unbounded density 1/(2 sqrt(t)). If X,Y are iid Uniform[0,1], X^2+Y^2 has bounded density but jumps from 0 to pi/4 at zero, so no continuous representative exists. These controls are lower-rank and are used only to separate the logical notions, not as target counterexamples.

Under the full three-large-eigenvalue target, the official current CLAIMS file still lists the universal L-infinity theorem OPEN and the full continuous-representative assertion OPEN. The present theorem therefore records only its proved structural scope.

## Why this does not close the spectral target

The spectral hypothesis does not force a uniformly conditioned physical definite pair. Let n=3m and

    A_m = diag(J_m/m, J_m/m, J_m/m).

Its nonzero spectrum is exactly {1,1,1}, so it is a target matrix. Every nonsingular definite 2x2 physical principal block uses coordinates from distinct blocks and has determinant 1/m^2; same-block 2x2 blocks are singular. Thus (2) yields only pi*m on this family. The family is not a QFORM counterexample; it exhibits the aggregate-before-inversion obstruction. Its three block sums are independent, so bank aggregation can restore a dimension-free bound by a different mechanism.

The partner's exact normalization strengthens this diagnosis: one may already work at s_3(A)=1, as A_m does. The remaining bridge is therefore not spectral rescaling or exact genericity; it is to replace reciprocal payment for one physical determinant by an aggregate product-coordinate bank payment that stays bounded when all local minors are O(m^-2).

## Result status

FULL-PROBLEM CHANGE: OPEN -> OPEN.
MECHANISM CHANGE: qualitative regularity / local-rank arguments -> direct two-coordinate definite shell-volume payment, with continuity proved only afterward under a distinct third-coordinate hypothesis.

New proved supporting lemma: (2), with constant pi/sqrt(|det B|), plus the stated C_0 upgrade. Remaining full implication: obtain a dimension-free aggregate replacement for 1/sqrt(|det B|) in the diffuse physical-minor regime without rotating away input independence.

Execution context: WITHOUT_VERIFIED_BRAIN (repository transport is not native learned-memory ingestion under the current protocol). Model self-report: GPT-5.6 Sol. Requested reasoning: maximum actually supported. Configured/known reasoning: UNKNOWN. Provider reasoning usage: not exposed.
