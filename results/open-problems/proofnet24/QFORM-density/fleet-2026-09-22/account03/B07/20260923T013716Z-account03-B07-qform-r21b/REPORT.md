SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B07, 2026-09-23T01:37:16Z.
attacking: finite-bank overlap receiver: remove determinant cancellation by a permutation-monomial bank ledger, then factor the singular shared-pair branch into an exact zero-self physical star.

# account03/B07 r21b — overlap permutation motifs and singular-pair star factorization

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Coordinate minor selection / GEOMETRY  
**Owner control:** revision `2026-09-22.15` at startup  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (`full_brain_connected=false`)  
**Status:** `NEW SUPPORTING STRUCTURAL THEOREMS + PARTNER INEQUALITY / FULL TARGET OPEN`.

## 1. Target and correction boundary

The target remains the unrestricted statement: independent original real coordinates with one-dimensional probability densities bounded by one, arbitrary dimension, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one. No moment, support, Gaussian, log-concavity, connected-support, iid, or post-rotation-independence assumption is introduced. Full continuity is tracked separately.

The live correction state was refreshed before this work. In particular the argument below does **not** infer a uniformly useful single local minor from aggregate third-compound mass; does not use a bounded projected joint-density cap as a substitute for product provenance; does not use the false arbitrary-joint coarea bound; and does not replace a small nonzero pivot by zero.

The direct input is the preceding B07 theorem

`QFORM-THIRD-COMPOUND-OVERLAP-COLORING-v1`

from

`yspennstate/math-open-problems@391688138f7f481a2c8688c2d27f9508db7af6af`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260923T000734Z-account03-B07-qform-r20/REPORT.md`.

It selects, from the total third-compound mass, one of four finite original-coordinate packets. In the four overlap classes `q=0,1,2,3` those packets obey respectively

`P0 >= 1/5184`, `P1 >= 1/3125`, `P2 >= 1/512`, `P3 >= 1/18`.      (1.1)

This run attacks the next obstruction: a large determinant packet can still be produced by cancellation among its six determinant monomials. The point is to remove that cancellation **before** any reciprocal payment and obtain a positive physical-bank motif.

## 2. A determinant-to-positive-motif compiler

For a real `3 x 3` matrix `M=(m_ab)`,

`det M = sum_(pi in S3) sgn(pi) product_(a=1)^3 m_(a,pi(a))`.

By Cauchy--Schwarz,

`|det M|^2 <= 6 sum_(pi in S3) product_a |m_(a,pi(a))|^2`.       (2.1)

The key point is that after summing (2.1) over one of the colored packets, every right-hand term is a **nonnegative original-coordinate bank energy**. Thus cancellation disappears without selecting a minor.

### Theorem 2.1 — `QFORM-OVERLAP-PERMUTATION-MOTIF-LEDGER-v1`

For each colored packet `Pq` from the preceding overlap-coloring theorem, there are six positive permutation-motif slots `M_(q,pi)` such that

`Pq <= 6 sum_(pi in S3) M_(q,pi)`.                               (2.2)

Consequently some permutation motif satisfies

`M_(q,pi) >= Pq/36`.                                               (2.3)

Under the target-level packet alternatives (1.1), at least one of the following positive physical-bank certificates therefore holds:

`q=0: M >= 1/186624`,
`q=1: M >= 1/112500`,
`q=2: M >= 1/18432`,
`q=3: M >= 1/648`.                                                 (2.4)

No determinant, inverse, or local conditioning number appears in (2.4).

### Proof

Apply (2.1) to each minor in the applicable colored packet and sum. Interchange the finite/nonnegative sums. This gives (2.2). There are six permutation slots, so if all six were below `Pq/36`, then the right side of (2.2) would be strictly below `Pq`. Hence (2.3). Substituting (1.1) gives (2.4). QED.

The usefulness is not merely the constant: every motif below has a direct product-bank interpretation.

## 3. Explicit motifs in all four overlap classes

Write

`F(U,V)=sum_(u in U,v in V) A_uv^2`,
`D(H)=sum_(h in H) A_hh^2`.                                      (3.1)

### 3.1 Disjoint triples, `q=0`

The banks are `L1,L2,L3,R1,R2,R3`. For each `pi in S3`,

`M_(0,pi)= product_(a=1)^3 F(La,R_(pi(a))).`                      (3.2)

Thus `q=0` always yields three pairwise bank-disjoint physical cross energies whose product is at least `1/186624`. This recovers the earlier rainbow matching-product certificate directly from determinant expansion, now as one member of a uniform overlap ledger.

### 3.2 One shared coordinate, `q=1`

The banks are `H,R1,R2,C1,C2`. For `h in H` define

`R_a(h)=sum_(r in Ra) A_hr^2`,
`C_b(h)=sum_(c in Cb) A_hc^2`,
`S_ab=sum_(h in H) R_a(h) C_b(h)`.                               (3.3)

Put `F_ab=F(Ra,Cb)` and `D=D(H)`. The six permutation motifs are

`D F_11 F_22`,
`D F_12 F_21`,
`S_11 F_22`,
`S_22 F_11`,
`S_21 F_12`,
`S_12 F_21`.                                                       (3.4)

So the shared-one packet forces either a diagonal-square bank times two cross-bank energies, or a positive two-sided hub-star correlation times one cross-bank energy. One of (3.4) is at least `1/112500`.

### 3.3 Two shared coordinates, `q=2`

The banks are `H1,H2,R,C`. Write

`D1=sum_(i in H1) A_ii^2`, `D2=sum_(j in H2) A_jj^2`,
`F=F(R,C)`,
`G=sum_(i in H1,j in H2) A_ij^4`,
`R_i=sum_(r in R) A_ir^2`, `C_i=sum_(c in C) A_ic^2`.             (3.5)

The six positive motifs are

`M1=D1 D2 F`,
`M2=G F`,
`M3=D1 sum_(j in H2) R_j C_j`,
`M4=D2 sum_(i in H1) R_i C_i`,
`M5=sum_(i in H1,j in H2) A_ij^2 R_i C_j`,
`M6=sum_(i in H1,j in H2) A_ij^2 C_i R_j`.                        (3.6)

One of these is at least `1/18432` whenever the `q=2` packet is the active target branch.

For clarity, for a single tuple `(i,j,r,c)` put

`a=A_ii`, `d=A_jj`, `b=A_ij`, `x=A_ic`, `y=A_jc`,
`u=A_ri`, `v=A_rj`, `z=A_rc`.

Then the relevant mixed determinant is exactly

`a d z - a v y - b^2 z + b u y + b v x - d u x`.                 (3.7)

Squaring and applying (2.1), then summing, gives precisely (3.6). Thus (3.6) is not a heuristic grouping; it is the complete six-permutation ledger.

### 3.4 Principal triples, `q=3`

The banks are `H1,H2,H3`. Let

`Da=sum_(i in Ha) A_ii^2`,
`G_ab=sum_(i in Ha,j in Hb) A_ij^4`,
`T=sum_(i in H1,j in H2,k in H3) A_ij^2 A_jk^2 A_ki^2`.          (3.8)

The six permutation slots are

`D1 D2 D3`, `G12 D3`, `G13 D2`, `G23 D1`, `T`, `T`.             (3.9)

Hence the principal-triple packet forces one of a three-diagonal product, a diagonal-times-fourth-power edge bank, or a physical triangle-energy bank to be at least `1/648`.

Equations (3.2)--(3.9) turn all four overlap classes into finitely many **positive** original-coordinate motifs. This removes determinant cancellation as a separate structural obstruction.

## 4. Singular shared pair: exact factorization into a zero-self star

The `q=2` Schur ledger from the preceding run split physical pairs into invertible and singular principal pairs. The singular branch admits an exact original-coordinate factorization.

### Theorem 4.1 — `QFORM-Q2-SINGULAR-PAIR-STAR-FACTORIZATION-v1`

Fix a physical pair `H={i,j}` and suppose its principal matrix

`B=[[a,b],[b,d]]`

is singular and nonzero. After possibly exchanging `i,j`, choose the diagonal with larger absolute value, so `a!=0`, `|a|>=|d|`, and therefore

`d=b^2/a`, `|b/a|<=1`.                                           (4.1)

For every outside physical coordinate `k`, define the **physical scalar-Schur star coefficient**

`s_k=A_jk-(b/a)A_ik`.                                             (4.2)

Then the residual diagonal at `j` after the original-coordinate pivot `i` is exactly zero, and for every `r,c` outside `H`,

`boxed:
 det A[{i,j,r},{i,j,c}] = -a s_r s_c.
`                                                                       (4.3)

Consequently for any disjoint outside banks `R,C`, the entire pair packet factors as

`boxed:
 W_ij(R,C)
 :=sum_(r in R,c in C) det A[{i,j,r},{i,j,c}]^2
 =a^2 (sum_(r in R)s_r^2)(sum_(c in C)s_c^2).
`                                                                       (4.4)

If `B=0`, every determinant in (4.3) is zero, so a positive `q=2` singular packet can only come from rank-one physical pairs.

### Proof

Singularity gives `ad-b^2=0`. Since a nonzero symmetric rank-one `2 x 2` matrix has a nonzero diagonal, the stated relabeling is possible. Equation (4.1) follows immediately.

Perform the scalar Schur elimination on the original physical coordinate `i`. The residual `jj` entry is `d-b^2/a=0`; its `jk` entry is exactly (4.2). Applying the block determinant identity to rows `{i,j,r}` and columns `{i,j,c}` gives

`det = a det [[0,s_c],[s_r,*]] = -a s_r s_c`,

which is (4.3). Squaring and summing over `R x C` gives (4.4). If `B=0`, the first two rows of every displayed mixed `3 x 3` minor are supported in only the outside column, so the determinant vanishes. QED.

This is a useful repair of the singular-pair branch: singularity is not an analytic dead end. It creates an **exact zero-self physical star after one genuine original-coordinate pivot**, with the determinant weight preserved exactly.

## 5. Completed account04 result applied to an actual inequality

The designated `account04/B07` still had no completed current-QFORM handoff at the fresh source lookup, so none is fabricated. I apply the compatible completed account04/B18 sharp product-projection result, canonical source

`yspennstate/math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T182500Z-account04-B18-QFORM-r2/REPORT.md`.

Its one-dimensional product-projection consequence is the sharp cap

`||p_(u^T X)||_infinity <= sqrt(2)/||u||_2`                       (5.1)

for independent cap-one original coordinates. In the exact-zero physical-star receiver this yields the previously source-checked inequality

`H_(1/2)(R) <= 2^(11/4) beta^(-1/2)`,                             (5.2)

where `beta` is the Euclidean norm of the zero-self row's physical outside coefficients; arbitrary quadratic curvature on the other coordinates remains present.

Apply (5.2) to the exact star (4.2). Put

`U=sum_(r in R)s_r^2`, `V=sum_(c in C)s_c^2`,
`w=W_ij(R,C)=a^2 U V`.                                            (5.3)

The full residual row norm satisfies

`beta^2 >= U+V >= 2 sqrt(UV)`.                                   (5.4)

Therefore (5.2) gives the actual determinant-weight inequality

`boxed:
 H_(1/2)(R)
 <= 2^(5/2) (UV)^(-1/8)
 = 2^(5/2) w^(-1/8) |a|^(1/4).
`                                                                       (5.5)

Completing the outer physical square on coordinate `i` then gives

`boxed:
 ||p_Q||_infinity
 <= |a|^(-1/2) H_(1/2)(R)
 <= 2^(5/2) w^(-1/8) |a|^(-1/4).
`                                                                       (5.6)

Thus any singular shared-pair subpacket with `|a|>=delta>0` and its **actual pair packet weight** `w>=omega>0` is fully paid by

`||p_Q||_infinity <= 2^(5/2) omega^(-1/8) delta^(-1/4)`.          (5.7)

For example, at the already-used quantitative pivot collar `delta=1/512` and a local packet weight `omega=1/18432`, (5.7) is `<91.853`. This numerical line is only a conditional collar; the aggregate bank theorem does **not** assert that one pair has weight `1/18432`.

That last distinction is exactly the coordinate-selection issue: (4.4)--(5.7) provide the correct analytic receiver for a singular pair once its weight is available, but a dimension-free passage from the **sum over many singular pairs** to that receiver must still aggregate before reciprocal localization.

## 6. What is newly removed, and what remains

The previous finite-bank reduction had two different structural losses:

1. determinant cancellation inside each colored third minor;
2. singular physical shared pairs in the `q=2` Schur split.

This run removes both as standalone mysteries.

* Cancellation is replaced by the finite positive motif list (3.2)--(3.9), with explicit target-level constants (2.4).
* A singular `q=2` physical pair is exactly a zero-self star after one original-coordinate scalar pivot, with packet weight identity (4.4); account04/B18 gives the exact payment (5.6) whenever the pair weight and pivot scale are quantitatively available.

The full theorem is **not** thereby proved. The first unpaid B07 implication is now

`QFORM-POSITIVE-MOTIF-BANK-RECEIVER-v1`:

> Pay the positive motifs (3.4), (3.6), and (3.9) at the aggregate bank level, without selecting one hub/pair whose weight may vanish with dimension. In the q=2 singular branch, sum the exact rank-one star factorizations (4.4) by a product-preserving grouped-coordinate or fractional-potential mechanism before any reciprocal `|a|` or local packet payment. In the invertible q=2 branch, use the pair-Schur first-compound currency together with the already completed two-pivot/pair-log mechanisms. Retain arbitrary extra spectrum and all signs.

The `q=0` positive motif is already the known three-matching-bank resource; its fully curved analytic transducer remains a separate receiver issue. The `q=1` and `q=3` positive motifs are now finite and cancellation-free but still need product-preserving smoothing.

**Full QFORM:** OPEN / NOT PROVED / NOT DISPROVED.  
**Full continuous-density conclusion:** OPEN.  
The branch payment (5.6) proves essential boundedness only in its stated singular-pair collar; no new global continuity claim is made.
