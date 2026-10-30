SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet04, slot B20, 2026-09-23T04:17:25Z.
attacking: compile the newest exact-rank-three branches into a noncircular dependency graph and pay the leakage-free face of the first double-star/large-core survivor.

# fleet04/B20 — proof graph and leakage-free double-star payment

## Status

**ESSENTIAL_STEP_APPLIED / NEW TARGET-LEVEL SUBBRANCH / FULL QFORM OPEN.**

The full statement remains open: for arbitrary independent real variables with one-dimensional probability densities at most one and arbitrary real symmetric (A) with (s_3(A)ge1), no source-pinned argument currently proves a universal output-density cap, and no valid counterexample is known. Continuity is a separate conclusion.

All random variables below remain in original coordinates. There is no independence after rotation, moment or support assumption, arbitrary-joint coarea, worst conditional-density supremum, or deletion of a small random quadratic perturbation.

## 1. Source-pinned inputs

1. Claude baseline and corrections: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory
   `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.
   These are supporting inputs, not a full proof.

2. fleet01/B20 second-stage cascade:
   `yspennstate/math-open-problems@c71cc4db4e48ee51524175a57e323aba881d37bb`.
   Its live P2 order-two survivor in strict (N3(1/128)) is either already paid, or after exposing original row/column anchors has
   [
   |d|<1/32
   ]
   and one of
   [
   |c|_2|r|_2>rac1{2sqrt{194}},qquad
   |C|_F>rac{16}{sqrt{194}}. 	ag{1.1}
   ]

3. fleet03/B05 direct two-arm coarea:
   `yspennstate/math-open-problems@3045ac45b0937065a4d4931b6127dde1f287d701`.
   If (X,Y,Z,W) are independent cap-one scalars and
   [
   R=H(X,Y)+2eta(X-x_0)[Z+m(X,Y)]
      +2gamma(Y-y_0)[W+n(X,Y)],
   ]
   then
   [
   |p_R|_inftyle rac2{sqrt{|etagamma|}}. 	ag{1.2}
   ]
   Its original-bank version uses the sharp scalar product-marginal cap
   (|p_{bcdot U}|_inftylesqrt2/|b|_2).

4. fleet01/B20 anchored wedge compiler:
   `yspennstate/math-open-problems@f64266f079e502403ff19ff5ca9739a79c65ebcc`.
   On the current O3 star branch it gives
   [
   W_i=sum_{j
e i}|r_iwedge r_j|^2>rac1{41472}
   ]
   and the exact physical ledger (P_i+M_i+D_i=W_i).

The newest fleet01/B20 result is consumed below at the actual threshold in (1.1), not cited merely as context.

## 2. New theorem: leakage-free face of the P2 double-star survivor

### Theorem — `QFORM-P2-DOUBLESTAR-LEAKAGEFREE-PAYMENT-v1`

Let (X,Y), the original-coordinate banks (U,V), and an arbitrary remainder bank (T) be mutually independent; every scalar input density is at most one. Let (c,r) be nonzero coefficient vectors and assume
[
|c|_2|r|_2>rac1{2sqrt{194}}. 	ag{2.1}
]
For arbitrary Borel (H,m,n), and arbitrary measurable (G(T)), define
[
Q=G(T)+H(X,Y)
 +2X,[rcdot V+m(X,Y)]
 +2Y,[ccdot U+n(X,Y)]. 	ag{2.2}
]
Then (Q) is absolutely continuous and
[
oxed{ |p_Q|_infty<4,194^{1/4}
       =14.9283023963ldots }. 	ag{2.3}
]

The same bound holds with arbitrary deterministic translations of (X,Y), absorbed into (H,m,n). An independent direct-sum random remainder is allowed through (G(T)).

#### Proof

Put (s=|c|_2), (t=|r|_2). By the source-valid one-dimensional product-marginal theorem,
[
Z=rac{sqrt2}{t},rcdot V,qquad
W=rac{sqrt2}{s},ccdot U
]
have densities bounded by one. They are independent of each other and of (X,Y,T), since their banks are disjoint original-coordinate banks.

Condition first on (T). The term (G(T)) only translates the output. Equation (2.2) is then exactly the two-arm form (1.2) with
[
eta=t/sqrt2,qquad gamma=s/sqrt2.
]
Therefore
[
|p_{Qmid T}|_infty
 le rac2{sqrt{st/2}}
 =rac{2sqrt2}{sqrt{st}}. 	ag{2.4}
]
Averaging conditional densities preserves this cap. From (2.1),
[
rac1{sqrt{st}}<sqrt{2sqrt{194}},
]
and hence
[
|p_Q|_infty
 <2sqrt2,sqrt{2sqrt{194}}
 =4,194^{1/4}.
]
This proves (2.3). The coarea source proves absolute continuity. QED.

### Actual application to fleet01/B20

In the second-stage P2 cascade, the small-edge branch gives exactly the first alternative in (1.1). Whenever the residual same-bank/cross-bank curvature is absent from the two arm banks except through the displayed aggregates and translations, Theorem 2.1 applies and yields
[
oxed{|p_Q|_infty<14.929.} 	ag{2.5}
]
Thus the first unpaid P2 implication is strictly narrowed: the double-star branch is no longer unpaid in itself; only **dependent bank leakage** is unpaid.

This is a target-level statement for its matched source-coordinate branch. It is not a proof of the full conjecture and is not asserted when a residual term (U^	op D V), (U^	op B U), or (V^	op E V) uses the same arm banks.

## 3. Compact noncircular proof graph

The present source-pinned graph is a DAG; arrows mean “hypotheses of the child theorem are explicitly supplied by the parent.”

[
egin{array}{c}
s_3(A)ge1\
downarrow 	ext{current physical reductions (not yet globally exhaustive)}\
{	ext{large physical pivot/pair}, 	ext{P2}, 	ext{O3 star},
   	ext{exact-rank-three near-null/convex side},
   	ext{additional-spectrum interaction}}.
end{array}
]

Paid leaves currently include:

- physical pair / nonnull-pivot receivers, including fleet01/B20’s (|d|ge1/32) bound (<494.798);
- P2 first and second fractional mixed-volume gates, including (<72.220) and (<3344.877);
- exact-graph all-pivot and leverage-one deletion subbranches;
- ruled one-sheet side and positive Pluecker cross-cuts;
- diffuse low-shear Schur-isotropic cores;
- fleet04’s prior independent longitudinal/transverse-bank branch (<105.463);
- the new leakage-free P2 double-star leaf (2.5).

Open edges, with no circular reuse, are:

1. **P2 dependent-bank leakage**
   [
   |c|,|r|>rac1{2sqrt{194}}
   quad	ext{with}quad
   U^	op D V, U^	op B U, V^	op E V
   ]
   retained on the same arm banks.

2. **P2 large residual core**
   [
   |C|_F>rac{16}{sqrt{194}},
   ]
   without a justified robust rank-two or high-volume receiver.

3. **O3 anchored compound payment:** aggregate principal/one-overlap currency and diffuse disjoint (e_2) currency from the anchored wedge ledger.

4. **Exact-rank-three convex/two-sheet near-null collar:** the ruled theorem pays only the opposite one-sheet side; positive regression residual still requires an overlap-sensitive receiver.

5. **Additional spectrum:** transferring an exact-rank-three core estimate through arbitrary coupled outside spectrum remains unproved.

These are logically prior to any full theorem. In particular, a one-sided ruled estimate and the leakage-free theorem above cannot be composed to claim the convex side or arbitrary extra spectrum.

## 4. First remaining implication

The first analytic implication exposed by the new theorem is now precise:

`QFORM-DOUBLESTAR-DEPENDENT-BANK-LEAKAGE-v2`.

Given the two original independent pivots and disjoint original arm banks with
[
|c|,|r|>rac1{2sqrt{194}},
]
prove a dimension-free density bound after adding arbitrary quadratic terms on and between those same banks, while keeping all outside couplings. The proof must aggregate the two pivot Jacobians before inversion; taking a worst arm fiber or replacing the arm projections by an arbitrary joint bounded density is invalid.

The exact interpolation target is (2.4): a valid leakage receiver should reduce to
(2sqrt2/sqrt{|c||r|}) when the same-bank leakage is zero, and remain finite uniformly as the leakage matrix varies through the live P2 structural class.

## 5. Scope

- Full QFORM: **OPEN / not disproved**.
- Full continuity: **OPEN**.
- New branch (2.2): bounded absolutely continuous density, explicit cap (<14.929).
- No two independent end-to-end reviews exist because there is no full candidate proof. None are fabricated.
- Execution: `WITHOUT_VERIFIED_BRAIN`; repository transport is not native ingestion.
