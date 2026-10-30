SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B09, 2026-09-24T08:15:56Z.
attacking: promotion determinant versus coloop exit for the mixed-frame bilinear mechanism, with a mechanism change to triangle-localized physical crossings after source audit.

# fleet01/B09 r33 — triangle-localized crossing compiler after promotion-cascade audit

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: B09 bilinear block mechanism  
Status: **NEW SUPPORTING STRUCTURAL LEMMA / REQUIRED PARTNER RESULT APPLIED / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**.

The unrestricted conjecture remains OPEN. This run does not claim a full proof or counterexample. It changes mechanism on the exact r32 debt after a source audit showed that a uniform determinant lower bound from bounded-threshold leverage peeling is already ruled out by an earlier cascade construction. The new positive step converts the small-disjointness triangle endpoint of the rank-one fixed-hub mixed frame into a macroscopic sum of **literal disjoint 2x2 physical crossing determinants**. This is the quantity that the bilinear rank-two `L^p` ladder can use before a third smoothing resource is spent.

All random variables remain literal original independent coordinates with one-dimensional densities bounded by one. No post-rotation independence, moment/support/log-concavity assumption, law-uniform pointwise Fresnel decay, conditional projection cap, or probability squaring is used.

## 1. Fresh source boundary and the mechanism change


The direct predecessor is fleet01/B09 r32,

`yspennstate/math-open-problems@dd2f429f6135ce79e5801d58eca341a82d736527`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B09/20260924T065224Z-fleet01-B09-QFORM-auto11-r32/REPORT.md`.

It proved the promoted-leaf retained-hub theorem and the exact determinant update

`det(G-x_i x_i^T)=det(G)(1-ell_i)`.

Its stated successor was to prove enough residual determinant after repeated promotion, or route a coloop/localized endpoint.

A fresh source search found that the first possibility cannot be pursued as a universal bounded-depth or bounded-loss statement. Fleet02/B10 had already proved, before r32,

`QFORM-ARBITRARY-THRESHOLD-NULL-CASCADE-v1`,

`yspennstate/math-open-problems@6d467b74b34bb3ab34ab2f32cdfd9eab2e75af64`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B10/20260922T234658Z-fleet02-B10-QFORM-auto11/REPORT.md`.

Its geometric ray weights make the next normalized leverage equal to an arbitrary fixed `theta<1` for arbitrarily many successive peelings. Thus even keeping every peeled leverage bounded away from one does not force bounded peeling depth or a universal surviving determinant. This source matches the exact proposed peeling-only scope closely enough that I do not re-claim the same no-go as new mathematics.

The replacement mechanism is the already-proved weighted two-frame EKR stability theorem of fleet03/B09 r27,

`QFORM-WEIGHTED-EKR-2FRAME-STABILITY-v1`,

`yspennstate/math-open-problems@8b902bf20457a12c8ad394ece3808c9a0130a95b`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B09/20260923T091354Z-fleet03-B09-QFORM-r27/REPORT.md`.

For a probability law `mu` on physical two-element bases and disjointness probability `rho<1/4`, with `tau=(rho/2)^(1/3)`, it proves either

`max_i d_i >= 1-rho-tau`,

or some physical triple `S` carries pair-basis mass

`t_S >= 1-rho-tau/(1-tau)`.

At `rho<1/512`, the quoted numerical thresholds are respectively `>0.8988` and `>0.8879`.

The present run uses the **triangle alternative** to manufacture actual rank-two physical cross blocks.

## 2. Rank-one fixed-hub packet and notation

Consider the fixed literal hub `h` and a leaf bank `L` in the rank-one completed-curvature form

`A_LL = D + lambda v v^T`,                                      (2.1)

where `D` is arbitrary diagonal in the original physical coordinates and `lambda!=0`. Let

`c=A[L,h]`.                                                       (2.2)

Assume `v` and a unit vector `z` are orthonormal and write

`c=mu v + theta z`, `theta!=0`.                                  (2.3)

Equivalently the normalized two-frame has physical rows

`u_i=(v_i,z_i) in R^2`,

`sum_i u_i u_i^T = I_2`.                                        (2.4)

Put

`Delta_ij=v_i z_j-v_j z_i`,
`w_ij=Delta_ij^2`,
`d_i=v_i^2+z_i^2`.                                               (2.5)

Then `sum_(i<j) w_ij=1`, so `w` is the physical Pluecker basis law. Let `rho` denote the probability that two iid `w`-distributed physical pairs are disjoint.

The r31 fixed-hub Pluecker smoother already pays the positive-disjointness branch. The issue here is what the EKR **triangle** endpoint buys in literal bilinear crossing currency.

## 3. New exact identity: a physical triangle generates three disjoint 2x2 crossings

Fix a literal leaf triple

`S={i,j,k}`.                                                     (3.1)

For the split

`{h,i} | {j,k}`,                                                 (3.2)

the physical `2x2` cross block is

`C_i = [[c_j,c_k],
        [lambda v_i v_j, lambda v_i v_k]]`.                      (3.3)

The physical diagonal `D` contributes no off-diagonal entry because `i,j,k` are distinct. Hence

`det C_i
 = lambda v_i(c_j v_k-c_k v_j)
 = -lambda theta v_i Delta_jk`.                                 (3.4)

Cycling the distinguished leaf gives three literal disjoint-bank crossings. Define

`R_S := sum_(i in S) |det C_i|^2`.                               (3.5)

If

`n_S=(Delta_jk,-Delta_ik,Delta_ij)`                              (3.6)

with the natural cyclic signs, then

`boxed: R_S = lambda^2 theta^2 sum_(i in S) v_i^2 (n_S)_i^2.`    (3.7)

This identity is exact and invariant under arbitrary values of the physical diagonal coefficients `D_i` and the hub scalar `A_hh`. It is a physical-coordinate crossing statement, not a rotated-coordinate independence assertion.

## 4. New quantitative lemma: triangle mass plus no heavy row forces macroscopic crossing volume

Let

`H_S=sum_(i in S)u_i u_i^T`,
`t=det H_S=sum_({a,b} subset S) Delta_ab^2`.                     (4.1)

Thus `t` is exactly the Pluecker basis mass carried by the three edges of `S`.

### Theorem — `QFORM-TRIANGLE-CYCLIC-CROSSING-v1`

Assume

`max_(i in S) d_i <= eta < t`.                                  (4.2)

Then

`boxed: R_S >= lambda^2 theta^2 t(t-eta).`                       (4.3)

Consequently at least one cyclic literal `2x2` crossing satisfies

`boxed:
 |det C_i| >= |lambda theta| sqrt[t(t-eta)/3].`                  (4.4)

#### Proof

Let `U_S` be the `3x2` matrix whose rows are the `u_i`, `i in S`. Since the global two-frame is Parseval,

`0 <= H_S=U_S^T U_S <= I_2`.                                    (4.5)

Its two eigenvalues are at most one and have product `t`; hence each eigenvalue is at least `t`, so

`H_S >= t I_2`,
`H_S^(-1) <= t^(-1) I_2`.                                      (4.6)

The normalized cross-product vector

`nu=n_S/sqrt(t)`                                                 (4.7)

spans the one-dimensional kernel of `U_S^T`. Therefore the orthogonal projector onto `range(U_S)` has diagonal

`ell_i^(S)=u_i^T H_S^(-1)u_i=1-nu_i^2`.                        (4.8)

Using (4.6) and the global row leverage `d_i=||u_i||^2`,

`ell_i^(S) <= d_i/t <= eta/t`.                                  (4.9)

Thus

`(n_S)_i^2=t(1-ell_i^(S)) >= t-eta`                             (4.10)

for every `i in S`. Also

`sum_(i in S)v_i^2 = e_1^T H_S e_1 >= t`.                       (4.11)

Insert (4.10)--(4.11) into the exact identity (3.7):

`R_S/(lambda^2 theta^2)
 =sum_i v_i^2(n_S)_i^2
 >=(t-eta)sum_i v_i^2
 >=t(t-eta).`                                                    (4.12)

This proves (4.3); (4.4) follows because one of the three nonnegative summands is at least one third of their sum. QED.

This is the first step in this branch that turns the weighted-EKR **triangle** certificate into the literal bilinear-block currency of the B09 assignment.

## 5. Concrete compiler at `rho<1/512`

Apply the completed weighted-EKR theorem with `rho<1/512`. Put

`tau_0=(1/1024)^(1/3)=0.0992125657...`,

`t_0=1-1/512-tau_0/(1-tau_0)
   =0.8879070551... .`                                          (5.1)

Then one of the following holds:

1. a literal row has leverage `d_i>0.8988`; or
2. a literal triangle `S` has `t>=t_0`.

In the second branch, if no row in that triangle has leverage above `3/4`, Theorem 4 with `eta=3/4` gives

`t_0(t_0-3/4)=0.1224486472... .`                                (5.2)

Therefore

`boxed:
 R_S >= 0.1224486472 lambda^2 theta^2,`                          (5.3)

and some literal two-by-two crossing obeys

`boxed:
 |det C_i| >= 0.202030... |lambda theta|.`                      (5.4)

So after the mechanism change, the low-disjointness rank-one packet has the sharp three-way structural compiler

`positive disjointness payment`
`OR high physical leverage`
`OR macroscopic literal rank-two crossing.`                     (5.5)

The third outcome is genuinely new information: it is not merely “three coordinates capture the Pluecker mass”; it produces a determinant of an actual cross block between **disjoint original-coordinate banks**.

The remaining high-leverage branch is not declared solved here. The earlier r32 promoted-hub theorem remains the correct analytic tool there, but the fleet02/B10 cascade shows that one must combine it with localization/whole-bank structure rather than seek a universal residual determinant from repeated peeling alone.

## 6. How the new crossing connects to an `O(|I|)` endpoint

A rank-two cross block by itself has only the completed `L^p`, `p<infinity`, smoothing and need not have bounded density. This is a source-validated correction, not a defect in (5.4).

The completed designated-partner fleet02/B09 r2 theorem

`QFORM-RANK2-SCHUR-PIVOT-v1`,

source

`yspennstate/math-open-problems@b3922fe080467f7f34a7dd248460fa2478bc03d2`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B09/20260922T124417Z-fleet02-B09-QFORM-r2/REPORT.md`,

shows exactly how a genuine third physical pivot upgrades such a crossing to `L^infinity`: if a literal scalar pivot has coefficient `d!=0` and the corresponding Schur cross block has singular-value product `Delta_S`, then

`||p_Q||_infinity <= 4 sqrt(6)|d|^(-1/2) Delta_S^(-1/4)`,       (6.1)

with the identical coefficient in the interval estimate.

Thus whenever one of the cyclic crossings (5.4) survives as the Schur cross after a clean/disjoint physical pivot, the triangle branch immediately becomes

`P{Q in I}
 <=4 sqrt(6)|d|^(-1/2)
   [0.202030... |lambda theta|]^(-1/4)|I|`.                      (6.2)

The unresolved target-level implication is now precise: in the high-leverage or triangle-crossing chamber, either preserve a comparable rank-two crossing through an available third pivot, or route the pivot-cancellation geometry to one of the already-paid finite-core/singular-pair/mixed-frame receivers. What is no longer missing is a source-coordinate rank-two crossing certificate in the non-heavy triangle endpoint.

## 7. Required application of a completed fleet02/B09 result to an actual target inequality

Use the newer completed fleet02/B09 r19 theorem `QFORM-TWOHUB-DOUBLE-RETENTION-v1`. It states, in the normalized two-hub/one-square setting with its augmented source-row gate, that

`||p_Q||_infinity <= 6 |lambda|^(-1/3)`                         (7.1)

with a continuous density and the same coefficient times interval length.

Take literal independent cap-one coordinates

`U,V,Y0,Y1,Z1,Z2`

and define

`Q_* = 2(U+V)^2 + 2 U Y0 + 2 V Y1
      +4 ((Z1+Z2)/sqrt(2))^2.`                                 (7.2)

Use `H={U,V}` and the one square mode

`q=(Z1+Z2)/sqrt(2)`, `lambda=4`.                                (7.3)

The mixed rows are

`rho_(Y0)=(0,1,0)`,
`rho_(Y1)=(0,0,1)`,
`rho_(Z1)=rho_(Z2)=(1/sqrt(2),0,0)`.                            (7.4)

Hence their Gram is `I_3`. Under the r19 augmented metric `diag(1,1/2,1/2)`, every one of the four physical leaf rows has leverage exactly `1/2`; the theorem applies at the endpoint of its gate. Therefore

`boxed:
 ||p_(Q_*)||_infinity <= 6*4^(-1/3)
 =3.7797631497... <3.780,`                                      (7.5)

and

`boxed:
 P{Q_* in I} <3.780 |I|`                                       (7.6)

for every interval `I`; the density is continuous.

For deterministic spectral bookkeeping, in the orthonormal coefficient basis `(U,V,Y0,Y1,q)` the active matrix has spectrum

`{2+sqrt(5), 2-sqrt(5), 1, -1, 4}`.                             (7.7)

Thus the example has at least four eigenvalues of modulus at least one and is an actual instance of the owner's full target class. This is a direct application of the designated fleet02/B09 result, not just a citation.

## 8. Deterministic checks

The accompanying `CHECKS.md` records:

- a random numerical verification of (3.4)--(3.7) to `3e-17` absolute error;
- the constants `t_0=0.8879070551...`, `t_0(t_0-3/4)=0.1224486472...`;
- the exact spectrum (7.7);
- the partner bound `6*4^(-1/3)=3.7797631497...`.

No numerical check is used as proof of a universal statement.

## 9. Updated B09 frontier

The peeling-only successor from r32 is retired as a universal mechanism because the earlier source-matching null cascade already refutes bounded-depth/bounded-loss heavy-row deletion. The next B09 implication is

`QFORM-TRIANGLE-CROSSING-PIVOT-CANCELLATION-OR-HIGHLEVERAGE-EXIT-v1`:

> Starting from the low-disjointness compiler above, pay either (a) the high-leverage physical-row branch without demanding a universal residual determinant after repeated peeling, or (b) the macroscopic cyclic rank-two crossing branch by proving that one crossing survives a third source-coordinate pivot/curvature resource, with cancellation routed to an already-paid singular-pair, finite-core, grouped-crossing, or retained-hub endpoint.

The full conjecture remains OPEN. The full-target continuous-density conclusion remains OPEN.
