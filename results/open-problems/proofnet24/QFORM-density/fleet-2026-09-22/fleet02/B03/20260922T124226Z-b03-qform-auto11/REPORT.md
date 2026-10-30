# fleet02/B03 — conditional sum/difference density blow-up in the decoupled collision route

**Run:** `20260922T124226Z-b03-qform-auto11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Decoupled time integral  
**Classification:** `ESSENTIAL_STEP_APPLIED + CANDIDATE_REFUTED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and source pins

The owner target is unchanged: for independent real coordinates with densities at most one and a real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal essential bound on the density of `Q=X^T A X`, or give a genuine counterexample. No moment, support, log-concavity, diagonal-basis, or post-rotation-independence assumption is used here.

Fresh control was read from `yspennstate/math-research-brain`; immediately before publication the observed main commit was `448c32ac4e1d41bc56f5782f6ce44b09b93f606a`, still at owner revision `2026-09-22.5` with no later stop.

The named partner result directly audited and applied is fleet03/B03:

- latest collision-hierarchy report: `yspennstate/math-open-problems@719c114f8dad72a6780b194cbea124cfa4cf6d44`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B03/20260922T123410Z-fleet03-B03-QFORM-r11b/REPORT.md`, blob `4d1e570b1cc016640845be8a943aeafc69c2cff5`;
- earlier source-valid square-crosspacket theorem: `yspennstate/math-open-problems@32ac33a81e5b3b17a0016463f67e544adc474280`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B03/20260922T121240Z-fleet03-B03-QFORM-r11/REPORT.md`, blob `928a26acebf976b0c2e024fc702ab2fc5a4b9499`.

The preceding fleet02/B03 overlap-collapse report, used below without rederivation, is `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B03/20260922T121352Z-b03-qform-auto11/REPORT.md`, blob `8963fbba2dfcba902a64e1659d5174a3de0643bf` on an accessible source commit `e06922bfa31bbd225cdce6ee6aea563254e62563`.

Live corrections retained: law-uniform pointwise Fresnel decay is false; spectral-fiber suprema can lose dimension; rotation does not preserve independence; a bare 2-by-2 cross minor is insufficient; and the generic two-sheet X-ray cap is insufficient. Nothing below uses those refuted premises.

## 2. First unpaid implication attacked early

The partner's latest report correctly introduces the positive all-copy collision hierarchy

`J_m(eps)=int p_eps(y)^m dy`,

where `p_eps` is the Gaussian mollification of the law of `Q`. It also proves that a universal density bound `||p_Q||_infinity<=B` is equivalent to the simultaneous exponential estimate

`J_m(eps)<=B^(m-1)` for every integer `m>=2` and every `eps>0`.

That is a useful exact reformulation. The first new two-copy step in the same report, however, attempts to condition the bilinearized identity

`Q(X)-Q(X')=(X+X')^T A (X-X') = U^T A V`

on every pair-coordinate except `U_I,V_J`, where `I,J` are disjoint triples, and then treats the active conditional coordinates as if their one-dimensional density caps were still at most one. The dependence inside each pair `(U_i,V_i)` makes that step invalid.

## 3. Exact counterexample to the conditional-density-cap step

Let `X,X'` be iid `Uniform[0,1]` and set

`U=X+X'`, `V=X-X'`.

The joint density is exactly

`g(u,v)=(1/2) 1_{|v|<=u<=2-|v|}`.

For `|v|<1`,

`p_V(v)=1-|v|`,

and therefore

`U | (V=v) ~ Uniform[|v|,2-|v|]`,

so

`boxed{ ||p_{U|V=v}||_infinity = 1/[2(1-|v|)] -> infinity as |v|->1. }`

Thus a marginal bound `||p_U||_infinity<=1` does **not** survive conditioning on the conjugate difference variable. The symmetric statement holds for `V|U=u`. Consequently the line "condition on all pair variables except `U_I,V_J`; the active variables retain density caps at most one" is false even for the simplest admissible input law.

This refutes a proof mechanism, not the partner's collision-hierarchy identity and not the QFORM conjecture.

## 4. The exact corrected conditional inequality

For a general one-dimensional input density `f<=1`, the sum/difference pair has density

`g(u,v)=(1/2) f((u+v)/2) f((u-v)/2)`.

Hence, wherever the denominators are positive,

`||p_{U|V=v}||_infinity <= 1/[2 p_V(v)]`,

`||p_{V|U=u}||_infinity <= 1/[2 p_U(u)]`.                         (4.1)

There is no law-uniform upper bound on the right sides.

Apply the partner's three-by-three bilinear density lemma correctly after conditioning. If `M=A[I,J]` is invertible, scale the three active `U_I` coordinates and three active `V_J` coordinates by their **conditional** density caps. The lemma then gives, pointwise in the conditioned conjugate variables,

`||p_W||_infinity`
` <= (C_bil/4) |det M|^(-1/3)`
`    * prod_{i in I} p_{V_i}(v_i)^(-1/3)`
`    * prod_{j in J} p_{U_j}(u_j)^(-1/3)`,                       (4.2)

where

`C_bil=(27 sqrt(3) pi/2)^(1/3)`.

Averaging the conditioned variables yields the repaired unconditional bound

`boxed{`
`||p_W||_infinity`
` <= (C_bil/4) |det M|^(-1/3)`
`    * prod_{i in I} [int p_{V_i}(v)^(2/3) dv]`
`    * prod_{j in J} [int p_{U_j}(u)^(2/3) du].`
`}`                                                                    (4.3)

The new factors are Rényi-spread quantities of order `2/3`. Under only `f<=1`, they need not be uniformly bounded.

## 5. A source-valid family making the repaired loss diverge

Fix an integer `N>=3`, put `ell=1/N`, choose centers `c_k=10^k`, and let

`f_N = 1_{ union_{k=1}^N [c_k,c_k+ell] }`.

This is an admissible probability density: it has total mass one and pointwise cap one. The exponential spacing makes all nonzero ordered differences `c_k-c_l` pairwise separated and all unordered sums `c_k+c_l` pairwise separated by much more than `2 ell`.

Write

`tau_ell(x)=(ell-|x|)_+`,

so

`int tau_ell(x)^(2/3) dx = (6/5) ell^(5/3)`.                     (5.1)

For `V=X-X'`, the `N` diagonal components coincide at zero, while the `N(N-1)` nonzero ordered-difference components are disjoint. Therefore exactly

`boxed{`
`R_V(N):=int p_V(v)^(2/3) dv`
` = (6/5)[N^(1/3)-N^(-2/3)+N^(-1)].`
`}`                                                                    (5.2)

For `U=X+X'`, there are `N` disjoint diagonal-sum components with multiplicity one and `N(N-1)/2` disjoint off-diagonal unordered-sum components with multiplicity two. Hence exactly

`boxed{`
`R_U(N):=int p_U(u)^(2/3) du`
` = (6/5)[2^(-1/3)N^(1/3)+(1-2^(-1/3))N^(-2/3)].`
`}`                                                                    (5.3)

In particular

`R_V(N) ~ (6/5) N^(1/3)`,
`R_U(N) ~ (6/5) 2^(-1/3) N^(1/3)`.

If the six active coordinates in (4.3) use this law, then the repaired conditioning proof incurs

`R_V(N)^3 R_U(N)^3 ~ const * N^2 -> infinity`.                  (5.4)

Therefore no law-uniform QFORM constant can be obtained from that conditioning strategy by merely replacing the false marginal caps with the correct conditional caps. The loss is structural, not a missing numerical constant.

## 6. Source-valid replacement: keep original product blocks through Plancherel

The correction does **not** destroy the disjoint 3-by-3 crosspacket branch, because the partner's earlier theorem proves it by a different route. For disjoint original-coordinate triples `I,J` with

`delta=|det A[I,J]|>0`,

`QFORM-SQUARE-CROSSPACKET-PLANCHEREL-v1` conditions only outside `I union J`, keeps the active original coordinate blocks independent, and uses Cauchy-Plancherel before any sum/difference conditioning. It gives

`boxed{ ||p_Q||_infinity <= 3 delta^(-1/3). }`                 (6.1)

Now apply the **latest** partner collision-hierarchy theorem to the actual inequality (6.1). For every `m>=2` and every Gaussian smoothing scale `eps>0`,

`boxed{ J_m(eps) <= [3 delta^(-1/3)]^(m-1). }`                 (6.2)

Thus the whole collision hierarchy is already paid in this branch. The new all-copy formalism is useful; the false step was only the later attempt to recover the same branch by conditioning conjugate sum/difference coordinates.

The same application closes all collision orders for the previous fleet02/B03 overlap-collapse family. That family has a source-valid overlap-aware grouped density bound

`B_* = 2 + 4*24^(1/3)`.

Therefore its Gaussian collision hierarchy satisfies uniformly in the overlap parameter,

`boxed{ J_m(eps) <= B_*^(m-1) for all m>=2, eps>0. }`           (6.3)

This is important: every disjoint rank-three cross determinant can collapse in that family, yet the all-order collision base stays uniformly bounded once overlap is grouped **before** reciprocal determinant cost is paid.

## 7. Corrected conditional end-to-end route and first remaining implication

A compact valid conditional route is now:

1. Work entirely in original product coordinates until a source-valid local smoother or aggregate is formed.
2. If a disjoint square 3-by-3 crosspacket has determinant bounded below, use (6.1), then (6.2).
3. If spectral mass overlaps through common physical coordinates, group that overlap first and use an overlapping principal / bilinear-plus-square / hyperbolic smoother; once a density bound `B` is proved, the partner hierarchy automatically gives `J_m<=B^(m-1)`.
4. If every admissible matrix can be routed by a dimension-free overlap-aware aggregation theorem into one of those branches, the full target follows.

The first unpaid implication is therefore **not** a new two-copy conditional-cap estimate. It is the following source-valid aggregation problem:

> Construct an overlap-aware original-coordinate decomposition, uniform over dimension and over the input laws, which spends the rank-three spectral mass before any reciprocal local determinant or conditional Rényi cost, and yields one local/aggregate density smoother with a universal base.

Equivalently in the decoupled-time language: obtain an `m`-independent exponential collision base while treating each `(U_i,V_i)` as a coupled pair (or avoiding the pair transform altogether), never conditioning `U_i` on `V_i` or vice versa without paying the exact factors (4.3).

This remains open for the arbitrary-matrix target, especially in the localized indefinite overlap branch and with arbitrary extra eigendirections.

## 8. Status and integrity

- `QFORM-FULL`: **OPEN**.
- `QFORM-COLLISION-HIERARCHY`: **USED AS SOURCE-PINNED PARTNER RESULT**.
- `QFORM-U/V-CONDITIONAL-MARGINAL-CAP-v1`: **REFUTED** by Section 3.
- Corrected conditional estimate (4.3): **PROVED**.
- Unbounded Rényi-spread family (5.2)-(5.4): **PROVED**.
- Earlier square-crosspacket theorem remains valid and gives the all-order consequence (6.2).
- Previous overlap-collapse family now has the all-order consequence (6.3).
- Full overlap-aware aggregation theorem: **OPEN**.

No numerical simulation is used. No post-rotation independence, pointwise Fresnel decay, moment/support assumption, public release, paid call, remote workflow, credential, scheduler identifier, machine path, benchmark material, or unrelated private datum appears in this report.
