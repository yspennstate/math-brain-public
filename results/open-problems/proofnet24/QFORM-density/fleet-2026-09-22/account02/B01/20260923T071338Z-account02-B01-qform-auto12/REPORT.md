SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B01, 2026-09-23T07:13:38Z.
attacking: the exact d=g=0 boundary of the newest rank-two center receiver, by synchronizing physical self-determinant and aggregate cross-area cofactors and routing the same physical pair to a two-hub averaged-frequency packet before any near-null curvature is inverted.

# account02/B01 auto12 — kernel-cofactor synchronization and a two-hub bridge at the rank-two center endpoint

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Oscillatory replacement  
**Classification:** `ESSENTIAL_STRUCTURAL_STEP + SOURCE-VALID TARGET FAMILY / FULL QFORM OPEN`  
**Independent review:** pending  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (authenticated repository retrieval occurred; no native learned-memory receiver use was established)  
**Continuity:** claimed only on the source Theorem-H branch below, where the characteristic function is integrable.

## 1. Sources actually used


The required newest Claude source was read both at the owner-pinned snapshot `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` and at its compatible current state, directory

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

The result used at an equation is **Theorem H** (physical hubs plus a diagonal/low-rank leaf block). In its rank-zero leaf-curvature case with two physical hubs, if

`G=A_{I,H}^T A_{I,H}`

and every leaf leverage is at most `1/2`, then

`|phi_Q(t)| <= 4 pi^2 det(G)^(-1/2) |t|^(-2)`,

hence

`||p_Q||_inf <= 4 det(G)^(-1/4)`.                                 (1.1)

All hub self-curvature, hub-to-conditioned coordinates, leaf-to-conditioned coordinates, and conditioned self-curvature are arbitrary. This is a joint averaged-frequency estimate; it does not assert a scalar law-uniform Fresnel envelope.

The designated partner was also applied from its immutable report

`yspennstate/math-open-problems@c65e53a795f4f47c223a21698549857342bd1b5f`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260923T052757Z-auto11/REPORT.md`.

For three ORIGINAL center coordinates `I`, a disjoint bank `J`, `rank K=2`, unit `v in ker K^T`,

`Delta=sigma_1(K)sigma_2(K)`, `d=|v^T Bv|>0`,

it proves

`||p_Q||_inf <= (135e/32) Delta^(-1/2)
                  [4+log_+(sqrt(Delta)/d)]`.                       (1.2)

It also identifies the only intrinsic rank-two-center state not paid by (1.2) or the complementary linear-slice receiver: `d=g=0`, equivalently `Bv=0`. The present run attacks exactly that boundary rather than another endpoint limit in (1.2).

For the nonzero physical-pair branch below I use the completed determinant-only indefinite-pair theorem at

`yspennstate/math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371`

`proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/GEOMETRIC_SYNTHESIS.md`:
if `s_3(A)>=1` and an ORIGINAL indefinite principal pair has `D=|det B_pair|>0`, then

`||p_Q||_inf <= D^(-1/2)[9.2+log_+(10000 sqrt(D))]`.               (1.3)

No condition-number factor is present and every remaining block/coupling is arbitrary.

## 2. Exact kernel-cofactor synchronization

Take a three-original-coordinate center `I={1,2,3}` and a disjoint original-coordinate bank `J`. After conditioning every other original coordinate, write the quadratic part as

`Q = X_I^T B X_I + 2 X_I^T K X_J + (arbitrary terms in X_J and affine terms)`,   (2.1)

where `B=B^T` is `3x3`, `K` is `3 x |J|`, and

`rank K=2`.                                                         (2.2)

Let `v` be a unit generator of `ker K^T`, and put

`Delta=sigma_1(K)sigma_2(K)>0`.                                    (2.3)

Assume the exact partner boundary

`Bv=0`.                                                            (2.4)

Because `B` is symmetric, (2.4) makes `rank B<=2`. Define the signed two-dimensional pseudo-determinant

`c = lambda_1(B|_{v^perp}) lambda_2(B|_{v^perp})` if `rank B=2`,
`c = 0` if `rank B<=1`.                                            (2.5)

For `k=1,2,3`, let `hat k` denote deletion of center coordinate `k`, and define

`D_k = |det B_{hat k,hat k}|`,
`Gamma_k = sqrt(det(K_{hat k,*} K_{hat k,*}^T))`.                  (2.6)

### Theorem 2.1 — `QFORM-KERNEL-COFACTOR-SYNCHRONIZATION-v1`

Under (2.2)-(2.5), for every `k`,

`det B_{hat k,hat k} = c v_k^2`,                                  (2.7)
`Gamma_k^2 = Delta^2 v_k^2`.                                      (2.8)

Consequently there is a **single physical deletion** `k_*` such that

`v_{k_*}^2 >= 1/3`,
`D_{k_*} >= |c|/3`,
`Gamma_{k_*} >= Delta/sqrt(3)`.                                   (2.9)

#### Proof

If `rank B=2`, choose an orthonormal basis `(a,b,v)` with

`B=lambda_1 aa^T+lambda_2 bb^T`.

In this basis `adj(B)=diag(0,0,lambda_1 lambda_2)`, and orthogonal conjugation gives

`adj(B)=c vv^T`.                                                   (2.10)

If `rank B<=1`, both sides of (2.10) vanish. The `(k,k)` cofactor of `B` is exactly the principal determinant after deleting coordinate `k`, proving (2.7).

Likewise `KK^T` is positive semidefinite of rank two, has kernel `v`, and has nonzero eigenvalues `sigma_1(K)^2,sigma_2(K)^2`. Hence

`adj(KK^T)=Delta^2 vv^T`.                                         (2.11)

Its `(k,k)` cofactor is

`det((KK^T)_{hat k,hat k})
 =det(K_{hat k,*}K_{hat k,*}^T)=Gamma_k^2`,

which proves (2.8). Since `sum_k v_k^2=1`, one index has squared coordinate at least `1/3`, and (2.9) follows. QED.

The point is not the factor `1/3`; it is that **the same original physical pair** simultaneously carries a fixed fraction of the center pseudo-determinant and a fixed fraction of the entire rank-two cross area. These two currencies cannot drift to unrelated coordinate pairs at the exact `Bv=0` endpoint.

## 3. Immediate routing consequences

Let `H=I\{k_*}` be the synchronized physical pair from Theorem 2.1, and retain the full ambient matrix.

### 3.1 Nonzero center pseudo-determinant

If `c>0`, then `B_HH` is definite and `det B_HH>=c/3`. Conditioning every other original coordinate leaves two independent cap-one physical coordinates. Completing the affine square and making the ordinary two-dimensional linear change of variables gives the area bound

`||p_Q||_inf <= pi / sqrt(det B_HH)
             <= pi sqrt(3/c)`.                                    (3.1)

No independence after rotation is used; the two-dimensional joint physical density is at most one before the deterministic Jacobian change.

If `c<0`, then `B_HH` is indefinite and `D=|det B_HH|>=|c|/3`. Applying the determinant-only pair theorem (1.3) and its stated monotonicity in the lower determinant threshold gives

`||p_Q||_inf
 <= sqrt(3/|c|)
    [9.2+log_+(10000 sqrt(|c|/3))]`.                              (3.2)

Thus any endpoint packet with `|c|` bounded below by a universal constant is already paid, with all outside curvature and coupling retained.

Inside strict N3, however, every physical pair determinant is small. Equation (2.7) then forces `|c|` small as well: for the maximizing index `k_*`, `|c|/3<=D_{k_*}<tau`, hence

`|c|<3 tau`.                                                       (3.3)

So the true N3 boundary is not a mysterious three-coordinate state: it is specifically **small center pseudo-determinant plus surviving two-hub cross area**.

### 3.2 Averaged-frequency two-hub exit

Suppose, for the synchronized pair `H`, there is an active outside leaf set `L` such that

1. `A_LL` is diagonal (the rank-zero leaf-curvature case of source Theorem H),
2. `G=A_{L,H}^T A_{L,H}` is nonsingular,
3. every normalized leaf leverage `r_j^T G^{-1}r_j<=1/2`, where `r_j=(A_{jh})_{h in H}`.

All remaining coordinates go into Theorem H's unrestricted `J` set. Then (1.1) gives

`||p_Q||_inf <=4 det(G)^(-1/4)`.                                  (3.4)

If `L` is the entire cross bank of (2.1), then `G=K_{H,*}K_{H,*}^T`, so by (2.9)

`det(G)^(1/2)=Gamma_{k_*}>=Delta/sqrt(3)`.

Therefore

`boxed:
 ||p_Q||_inf <= 4*3^(1/4) Delta^(-1/2) <5.265 Delta^(-1/2).`       (3.5)

This estimate is completely independent of `c`, `d`, or a physical pair condition number. It is precisely the kind of joint averaged-frequency replacement requested by B01: two original hubs are integrated jointly, and no forbidden scalar law-uniform quadratic-phase decay is asserted.

The remaining issue is equally precise: when `|c|` is tiny and the outside self-curvature prevents a Theorem-H-compatible leaf set from carrying a fixed fraction of `Gamma_{k_*}`, one still needs a matrix-level route to another paid receiver. The cofactor lemma removes the ambiguity about which physical pair must be used.

## 4. A strict-N3 target family on which paying local d first is nonuniform

The following family is an exact stress test for the routing order.

Let

`v=(1,1,1)/sqrt(3)`,
`u1=(1,-1,0)/sqrt(2)`,
`u2=(1,1,-2)/sqrt(6)`,
`U=[u1 u2]`.                                                       (4.1)

For even `m>=4`, let `V_m` be the `m x 2` orthonormal-column matrix whose first column is constant `1/sqrt(m)` and whose second column is `+1/sqrt(m)` on the first `m/2` leaves and `-1/sqrt(m)` on the last `m/2`. Hence

`V_m^T V_m=I_2`, `||(V_m)_{j,*}||^2=2/m`.                         (4.2)

Set

`K=U V_m^T`,
`B_{eps,delta}=eps u1u1^T + delta vv^T`,
`A_{m,eps,delta}=[[B_{eps,delta},K],[K^T,0_m]]`,                   (4.3)

with `eps>=0`, `delta>=0`.

### 4.1 Exact spectrum

The `u1` / first-leaf-mode plane has matrix

`[[eps,1],[1,0]]`,

with eigenvalues

`lambda_+ = (eps+sqrt(eps^2+4))/2 >=1`,
`lambda_- = (eps-sqrt(eps^2+4))/2 in [-1,0)`.                     (4.4)

The `u2` / second-leaf-mode plane contributes `+1,-1`, while the center direction `v` contributes `delta`. Thus the nonzero spectrum is

`{lambda_+,lambda_-,1,-1,delta}`.                                 (4.5)

For every `eps,delta>=0`, the matrix has at least three eigenvalues of absolute value at least one: `lambda_+`, `1`, and `-1`. Therefore this is a genuine full-target family, not a two-eigenvalue local counterexample.

### 4.2 Strict N3

The leaf diagonals vanish. On the center,

`max_i |B_ii| <= eps/2 + delta/3`.                                (4.6)

The center-center pair determinants equal `eps delta (u2)_k^2` after deleting `k`, hence are at most

`(2/3) eps delta`.                                                 (4.7)

Every center-leaf principal determinant is `-K_ij^2`, and Cauchy-Schwarz with center-row leverage `2/3` and leaf-row leverage `2/m` gives

`|K_ij|^2 <=4/(3m)`.                                              (4.8)

Leaf-leaf determinants vanish. Consequently, for any fixed `tau in (0,1]`, taking

`eps<=tau`, `delta<=tau`, `m>4/(3tau)`                            (4.9)

puts the family in the strict no-pivot N3 class:

`max_i |A_ii|<tau`, `max_{i<j}|det A[{i,j}]|<tau`.                (4.10)

### 4.3 The newest partner receiver is valid but certificate-nonuniform

For the three-center / leaf-bank packet, `K` has singular values `1,1`, so

`Delta=1`, `ker K^T=span(v)`.                                     (4.11)

Moreover

`B_{eps,delta}v=delta v`,
`d=|v^TBv|=delta`,
`g=||(I-vv^T)Bv||=0`.                                             (4.12)

For every `delta>0`, the completed partner theorem (1.2) therefore gives the actual inequality

`||p_Q||_inf
 <= (135e/32)[4+log_+(1/delta)]`.                             (4.13)

As `delta->0`, this bound diverges logarithmically. That is not a defect in the partner theorem: its own two-large-eigenvalue example shows the logarithm can be sharp at its local scope. Rather, (4.13) proves that a full-QFORM architecture which **always pays the nonzero local d before checking for a joint hub route cannot yield a universal constant** on this exact target family.

At `delta=0`, the packet enters the intrinsic `d=g=0` state and `Bv=0`; here `B` has rank one and `c=0`, exactly the endpoint left unpaid by the local transverse-curvature receivers.

### 4.4 The newest joint hub theorem pays the same family uniformly

Delete any one center coordinate; because every `|v_k|=1/sqrt(3)`, Theorem 2.1 gives

`Gamma=sqrt(det(K_H K_H^T))=1/sqrt(3)`.                            (4.14)

Use the remaining two original center coordinates as Theorem-H hubs, all `m` leaves as its active `I` set, and the deleted center coordinate as its unrestricted `J` set. The leaf self block is zero. Since `K_H=U_H V_m^T` with invertible `U_H`, each normalized leaf leverage is exactly

`||(V_m)_{j,*}||^2=2/m<=1/2`.                                    (4.15)

The source theorem applies with **the entire hub block and all couplings to the deleted center retained**. Equation (3.5) gives

`boxed:
 sup_{m>=4, eps>=0, delta>=0}
 ||p_{X^T A_{m,eps,delta} X}||_inf
 <=4*3^(1/4)=5.2642960518...`                                    (4.16)

for every product of independent cap-one input laws.

Thus a target-valid strict-N3 family can have `d->0` (and at the endpoint `d=g=c=0`) while remaining uniformly paid by a two-hub averaged-frequency mechanism. The correct proof order is to route/aggregate first and invert the local transverse curvature only if no such joint packet is available.

The finite checker in this directory is auxiliary algebraic evidence only. At `m=100`, `eps=0.01`, `delta=10^-6`, it reports singular values of `K` equal to `1,1`, nonzero spectrum approximately

`{-1,-0.9950125,10^-6,1,1.0050125}`,

selected `Gamma=0.577350269...`, leaf leverage `0.02`, source Theorem-H bound `5.2642960518`, and partner logarithmic certificate `204.3038473`; it ends `status=PASS`.

## 5. Relation to the newest volume-stability package

The owner continuation also supplies the newer three-volume/tail stability theorem. On the designated center-to-leaf block of (4.3), however, `rank K=2` exactly, so its third singular value and collective tail beyond the first two are zero. The three-volume currency of that block is therefore identically zero. This is a concrete complementary regime rather than a competing estimate: the two-hub packet spends rank-two cross area plus physical hub provenance, precisely where a rank-three cross-volume theorem has no currency to spend.

## 6. What changed in the proof map

Before this run, the newest partner ledger ended with the state

`d=g=0 <=> Bv=0`

and the instruction that it must be connected to a third product-preserving packet or routed to a hub/null/grouped mechanism.

Theorem 2.1 now gives an exact algebraic connector at that endpoint:

* one physical pair carries at least `1/3` of the center pseudo-determinant;
* the **same** physical pair carries at least `1/sqrt(3)` of the rank-two cross area;
* if the pseudo-determinant is substantial, a physical-pair theorem pays it;
* if it is small, strict N3 forces exactly that situation, but the paired cross area survives and can be spent by Theorem H whenever a compatible leaf packet is present.

This is stronger than merely observing that some two-row submatrix of `K` has rank two; it synchronizes the self and cross currencies on the same original pair and therefore removes one combinatorial mismatch from the N3 routing problem.

## 7. First unpaid implication

`QFORM-KERNEL-COFACTOR-TO-CURVED-LEAF-ROUTING-v1`:

In strict N3, suppose a three-center rank-two packet reaches the intrinsic endpoint `Bv=0`, so Theorem 2.1 supplies a physical pair `H` with `Gamma_H>=Delta/sqrt(3)` while the center pseudo-determinant is small. Prove a dimension-free product-preserving alternative that either

1. extracts from the outside self-curvature a Theorem-H-compatible diagonal/low-rank leaf set carrying a fixed fraction of `Gamma_H`, or
2. routes the same pair to an already-paid bilateral curved-bank, volume/ridge, grouped-square, exact-null, or determinant-only receiver,

**before** paying any reciprocal tiny `d`, `c`, or physical determinant.

The stress family (4.3) proves this routing order is necessary at certificate level: the local logarithmic receiver diverges as `delta->0` while the joint hub bound stays `<5.265`.

No unrestricted routing theorem is proved here. Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. The supporting cofactor theorem and its applications have not received two independent end-to-end reviews.
