SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B06, 2026-09-23T10:38:46Z.
attacking: the transverse-curvature cut-or-hub gap from r29 — aggregate the whole bordered third-compound packet before selecting a physical cut, then feed a certified cut into the existing volume-sampling receiver.

# account01/B06 r30 — exact bordered compound identity and random-cut receiver

## Status

**Status:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_STRUCTURAL_THEOREM_PROVED / CERTIFIED_TRANSVERSE-CURVATURE_SUBBRANCH_CLOSED / FULL_TARGET_OPEN`.

The unrestricted owner target is not proved or disproved here. This report closes a new dimension-free subbranch of the zero-anchor two-hub survivor from r29. Global continuity remains open. On the two branches actually paid below, continuity follows from the completed partner receiver and the integrated-Fourier volume receiver respectively.

All probabilistic conditioning and independence statements use ORIGINAL coordinates. Orthogonal maps below are used only to establish deterministic compound-matrix identities; they are never used to assert independence of rotated random coordinates.

Execution label: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source boundary and completed inputs actually used


A newer correction is especially relevant: `QFORM-N3-LOCAL-COLLISION-BEFORE-AGGREGATION-FALSE-v1` shows that an exhaustive proof cannot force every target matrix into a disjoint cross-volume or one-local-pivot branch. The result below therefore claims only a certified **low-collision transverse-compound branch**. High compound collision is kept as an explicit unpaid bank/hub aggregation regime.

### 1.1 Designated partner account02/B06

Canonical source:

`yspennstate/math-open-problems@2fdec7c0b085cb5acf5a09847b293b5bcb296b80`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260923T083202Z-7358ab1fe71c/REPORT.md`.

Its completed theorem `QFORM-SHARED-COEFFICIENT-MAX-RECIPROCAL-v1` says: if `X,Y` are independent cap-one scalars, independent of a background product bank `Z`, and

`U=a.Z+u0`, `V=b.Z+v0`,

then with

`Delta(a,b)=sqrt(||a||^2||b||^2-(a.b)^2)>0`,

the joint affine-product projection has density cap at most `e/Delta`, and therefore

`boxed: ||p_(2XU+2YV+R(Z))||_infinity <= 2 sqrt(e/Delta).`       (1.1)

The partner proves continuity as well. This theorem is applied below at a concrete inequality.

### 1.2 r29 transverse-curvature budget

The preceding account01/B06 report is

`yspennstate/math-open-problems@4df53c175ff07a2a30226d946da66a74da47d7fd`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B06/20260923T093709Z-account01-B06-QFORM-r29/REPORT.md`.

In the zero-anchor chamber

`A=[[0,0,a^T],[0,0,b^T],[a,b,C]]`,                                (1.2)

write `s=s_3(A)`. If

`b=lambda a+epsilon`, `epsilon perp a`, `P_a=P_(a^perp)`,          (1.3)

then r29 proves

`boxed: s <= ||epsilon||+||P_a C P_a||op.`                         (1.4)

Thus curvature confined to the central `a` row/column cannot pay the third singular direction.

### 1.3 Existing volume-sampling receiver D'

The completed integrated-Fourier theorem D' is in

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`.

For an ORIGINAL-coordinate cross block `M`, put

`E_3(M)=e_3(MM^T)=sum_(|R|=|T|=3) det(M[R,T])^2`.                  (1.5)

Let `alpha_i` be the row marginals of squared-minor volume sampling. If

`max_i alpha_i <= h < 3/4`,                                       (1.6)

then the full ambient quadratic-affine form, with arbitrary same-side blocks and outside conditioning retained, has continuous density

`boxed: ||p_Q||infinity <= C_h E_3(M)^(-1/6),`                     (1.7)

where

`C_h=6 sqrt(e) (2h)^(-1/2)(3-4h)^(-1).`                           (1.8)

In particular `C_(1/2)=6 sqrt(e)` and `C_(2/3)=9 sqrt(3e)`.

## 2. Main deterministic theorem: the entire bordered compound packet

Let `a,b in R^m` be nonzero and let `C` be an arbitrary real `m x m` matrix. For two-element sets `R,T subset {1,...,m}`, define the bordered minor

`D_(R,T)=det [[0,a_T^T],[b_R,C_(R,T)]].`                           (2.1)

Define its total squared packet

`W(a,b,C)=sum_(|R|=|T|=2) D_(R,T)^2.`                              (2.2)

Let

`P_a=P_(a^perp), P_b=P_(b^perp).`                                 (2.3)

### Theorem 2.1 — `QFORM-BORDERED-COMPOUND-IDENTITY-v1`

One has the exact identity

`boxed:
 W(a,b,C)
 =||a||^2 ||b||^2 ||P_b C P_a||_F^2.`                             (2.4)

#### Proof

Consider the square bordered matrix

`M=[[0,a^T],[b,C]].`                                                (2.5)

The left side of (2.4) is the squared Frobenius norm of the block of `wedge^3 M` whose row and column wedge basis vectors both contain the distinguished hub coordinate. It is therefore invariant under independent orthogonal changes in the background row and background column spaces.

Rotate deterministically so that

`b=||b|| e_1`, `a=||a|| e_1`.                                     (2.6)

A bordered minor in (2.1) vanishes unless both `R` and `T` contain coordinate `1`. For `r,t>=2`,

`D_({1,r},{1,t})=-||a|| ||b|| C'_(r,t),`                           (2.7)

where the residual `(m-1)x(m-1)` block of `C'` is exactly a matrix representation of `P_b C P_a`. Summing the squares of (2.7) gives (2.4). QED.

This is stronger than selecting one bordered minor: an arbitrarily diffuse transverse curvature packet retains its full mass before any reciprocal is paid.

## 3. Random physical cuts spend the disjoint part of the packet exactly

The same physical background coordinates occur on both sides, so not every bordered minor can be placed into one disjoint cross block. This is the precise place where the current collision correction matters.

Define the **disjoint packet**

`W_disj=sum_(|R|=|T|=2, R cap T=empty) D_(R,T)^2`                  (3.1)

and, when `W>0`, the collision ratio

`chi=1-W_disj/W in [0,1].`                                         (3.2)

Choose a random physical partition `{1,...,m}=S sqcup T0` by independent fair coins. Form the genuine ORIGINAL-coordinate cross block

`M_(S,T0)= [[0,a_(T0)^T],[b_S,C_(S,T0)]].`                         (3.3)

### Theorem 3.1 — `QFORM-BORDERED-RANDOM-CUT-v1`

For the random cut,

`boxed:
 E_cut E_3(M_(S,T0)) >= W_disj/16.`                                (3.4)

Consequently some physical cut satisfies

`boxed: E_3(M_(S,T0)) >= W_disj/16.`                               (3.5)

If `chi<=eta<1`, then some cut satisfies

`E_3(M_(S,T0)) >= (1-eta)W/16.`                                   (3.6)

#### Proof

Fix disjoint two-sets `R,T`. If `R subset S` and `T subset T0`, then the three rows consisting of the left hub and `R`, together with the three columns consisting of the right hub and `T`, form a `3x3` minor of (3.3), and that minor is exactly `D_(R,T)`. Since four distinct coordinates receive prescribed independent coin values,

`P(R subset S, T subset T0)=2^(-4)=1/16.`                          (3.7)

The sum defining `E_3` contains all these nonnegative squares and possibly many more. Taking expectations and using (3.7) proves (3.4); (3.5)-(3.6) follow by averaging. QED.

This theorem does **not** claim that `W_disj` is always a fixed fraction of `W`. That stronger statement would conflict with the live local-collision correction. High `chi` is retained as a separate structural regime.

## 4. Certified transverse-curvature branch in the r29 zero-anchor survivor

Return to (1.2). Relabel the two physical hubs if needed so that

`||a|| >= ||b||.`                                                   (4.1)

Let `B=[a^T;b^T]`. We first dispose of the already-paid coefficient-area branch.

Assume

`s_1(B)>s/2.`                                                       (4.2)

Then

`||a|| >= ||B||_F/sqrt(2) >= s_1(B)/sqrt(2)>s/(2sqrt(2)).`         (4.3)

Set

`delta=1/(8sqrt(2)).`                                               (4.4)

### Branch A: coefficient-plane area is not tiny

If

`Delta(a,b)>=delta s^2`,                                           (4.5)

then applying the designated partner theorem (1.1) at this actual coefficient pair gives

`||p_Q||infinity
 <=2 sqrt(e/Delta)
 <=[2 sqrt(e) sqrt(8sqrt(2))]/s
 <11.092/s.`                                                        (4.6)

This is a continuous-density branch.

### Branch B: tiny area forces transverse background curvature

Suppose instead

`Delta(a,b)<delta s^2.`                                             (4.7)

In the decomposition (1.3),

`Delta(a,b)=||a|| ||epsilon||`.                                    (4.8)

By (4.3)-(4.4),

`||epsilon||<s/4.`                                                  (4.9)

The r29 budget (1.4) therefore yields

`boxed: ||P_a C P_a||op>3s/4.`                                    (4.10)

Let `theta` be the angle between `a` and nonzero `b`. Since the operator norm of the difference of the two rank-one orthogonal-complement projections is

`||P_b-P_a||op=sin(theta)`,                                        (4.11)

we have

`||P_b C P_a||_F
 >=||P_b C P_a||op
 >=||P_a C P_a||op-sin(theta)||C||op.`                             (4.12)

Hence on the **rotation-stable transverse branch**

`sin(theta)||C||op <= s/4`                                         (4.13)

one obtains

`boxed: ||P_b C P_a||_F>s/2.`                                     (4.14)

Now impose the concrete lower-star gate

`||b||>=s/2.`                                                       (4.15)

Combining (4.3), (4.14), (4.15) with Theorem 2.1 gives

`W(a,b,C)
 =||a||^2||b||^2||P_b C P_a||_F^2
 > (s^2/8)(s^2/4)(s^2/4)
 =s^6/128.`                                                        (4.16)

If additionally the compound collision is at most one half,

`chi<=1/2`,                                                         (4.17)

Theorem 3.1 supplies a physical cut with

`E_3(M_(S,T0))
 >=W_disj/16
 >=W/32
 >s^6/4096
 =2^(-12)s^6.`                                                      (4.18)

### Feed the resulting literal physical block into D'

If the cut furnished by (4.18) has volume row marginals satisfying

`max_i alpha_i<=1/2`,                                               (4.19)

then (1.7) gives

`||p_Q||infinity
 <6sqrt(e) (2^(-12)s^6)^(-1/6)
 =boxed: 24sqrt(e)/s
 <39.570/s.`                                                        (4.20)

More generally, under the weaker gate

`max_i alpha_i<=2/3`,                                               (4.21)

D' gives

`||p_Q||infinity
 <9sqrt(3e) (2^(-12)s^6)^(-1/6)
 =boxed: 36sqrt(3e)/s
 <102.805/s.`                                                       (4.22)

The integrated-Fourier source gives a continuous density on these D' branches.

Thus a substantial portion of the formerly opaque near-collinear/transverse-curvature regime is now paid without selecting an individual physical third minor.

## 5. Exact remaining geometry after this run

This report deliberately does not overstate the random-cut lemma. After the previous r29 exits and the new branch above, the still-unpaid near-collinear geometry must enter at least one of the following concrete failure modes:

1. **background spectral recursion:** `s_1(B)<=s/2`, where r29 already forces `s_3(C)>=s/2`;
2. **one-hub asymmetry:** after relabeling, the smaller star satisfies `||b||<s/2`;
3. **high-amplification transverse rotation:** `sin(theta)||C||op>s/4`;
4. **compound collision:** `chi>1/2`, so most bordered third-compound mass reuses physical indices and cannot be exposed by a disjoint cut before aggregation;
5. **volume hub:** every cut carrying the guaranteed disjoint `E_3` packet has a squared-minor row marginal above the chosen D' threshold.

Modes 4-5 are exactly where one should use grouped-bank/hub structure rather than insist on another local minor. The correction `QFORM-N3-LOCAL-COLLISION-BEFORE-AGGREGATION-FALSE-v1` makes this distinction necessary, not cosmetic.

The first unpaid implication for B06 is therefore

`QFORM-COLLIDING-BORDERED-COMPOUND-OR-VOLUME-HUB-v1`:

> Starting from target-scale `W=||a||^2||b||^2||P_b C P_a||_F^2`, prove that high compound collision or heavy volume marginals feed one of the already source-valid grouped-hub/ridge/square receivers at target scale, without conditioning away product provenance; otherwise extract a low-marginal disjoint cut and apply D'.

This is narrower than r29's generic cut-or-hub statement: the exact obstruction is now quantified by `chi` and the volume-sampling marginals.

## 6. Exact finite checks

A standard-library exact-arithmetic checker accompanies this report. It verifies on several nontrivial integer examples that:

1. the identity (2.4) holds exactly as a rational equality;
2. exhaustive averaging over all `2^m` physical cuts gives exactly `W_disj/16` for the restricted family of hub-containing minors used in Theorem 3.1;
3. the constants are
   `24sqrt(e)=39.5693104968...`,
   `36sqrt(3e)=102.804084301...`, and
   `2sqrt(e)sqrt(8sqrt(2))=11.0912304503...`.

These checks support the algebra only; they are not substitutes for the proofs above.

## 7. Target status

- Full arbitrary-dimensional QFORM conjecture: **OPEN**.
- Valid counterexample to the target: **none produced**.
- Global continuity: **OPEN**.
- Continuity on Branch A and the D' certified branch: **PROVED by the cited completed inputs**.
- Independent end-to-end review of the new Theorems 2.1 and 3.1: **not yet performed**.
