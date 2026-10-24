SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B10, 2026-09-22T20:47:29Z.
attacking: the heavy-null residual-diffuse overlap endpoint after whole-null-bank compression; force a product-preserving two-bank decomposition or a source-valid obstruction.

# account02/B10 — residual-diffuse two-bank paving and local-atom obstruction

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Rank-three coupled case  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Classification:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_LEMMA / LOCAL_CANDIDATE_REFUTED / FULL_TARGET_OPEN`

The full conjecture remains open. This report works only in the exact-rank-three heavy-null endpoint produced by the completed named-partner compression theorem. It does not assume independence after spectral rotation, does not use the refuted arbitrary-joint coarea lemma or positive conditional-density-moment gate, and does not replace product provenance by a conditional density cap.

## 1. First unpaid implication and source pins

The completed named partner `account03/B10`, run r15, source

`yspennstate/math-open-problems@a3dd62b198d84dc9b92653b8a9c77494fc6ed2d4`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B10/20260922T191739Z-account03-B10-QFORM-r15/REPORT.md`,

proved `QFORM-NULL-BANK-CAPONE-COMPRESSION-v1`. In its near-endpoint state `L>=7/8`, the original null-ray bank is replaced law-preservingly by one genuine independent cap-one physical coordinate with Parseval row

`u_0=sqrt(c) r`,

where

`c>=7/9`, `r^T M r=0`, `sigma_min(M)>=1/2`, `|det M|>=1/2`.             (1.1)

The preceding account02/B10 theorem, canonical source

`yspennstate/math-open-problems@b539c58ee7c0f4c09fe8a061b14a48ba279ae4`,

proved that if any complementary row has residual leverage

`h_j=||(I-r r^T)u_j||^2>1/2`,                                        (1.2)

then the branch is already paid by either a scalar-pivot or a uniformly indefinite physical-pair theorem. Therefore the first unpaid state may assume

`h_j<=1/2` for every complementary row.                              (1.3)

The new step below is to convert (1.3) into two **disjoint original-coordinate banks**, both carrying a uniformly nondegenerate two-dimensional residual projection. This is stronger than a conditional-cap statement because the two banks remain genuinely independent.

I also use, only in its proved scope, the product marginal theorem as source-pinned in account03/B09 r11,

`yspennstate/math-open-problems@41fc39eccdd44a0dcae6619676bf41f5ea21bb3e`,

which gives joint density at most `2` for every two-dimensional orthogonal projection of independent cap-one coordinates. The same source proves the exact Pluecker/random-split identities for rank-two product blocks.

## 2. Residual frame

Let

`P=I-r r^T`

be the orthogonal projection onto the two-dimensional residual plane. For every complementary physical row put

`v_j=P u_j`.

Since the full spectral frame is Parseval and `u_0=sqrt(c)r`,

`sum_j u_j u_j^T=I-c r r^T`                                         (2.1)

over the complementary rows. Projecting (2.1) to `r^perp` gives the exact two-dimensional Parseval identity

`sum_j v_j v_j^T=P`.                                                 (2.2)

After choosing any orthonormal basis of `r^perp`, identify `P` with `I_2`. Then

`sum_j v_j v_j^T=I_2`, `||v_j||^2=h_j<=1/2`.                         (2.3)

This is precisely the residual-diffuse geometry left unpaid by the preceding B10 run.

## 3. New deterministic two-bank paving lemma

### Theorem 3.1 — `QFORM-RESIDUAL-DIFFUSE-TWO-BANK-PAVING-v1`

Let `(v_j)` be any finite family in `R^2` satisfying

`sum_j v_j v_j^T=I_2`, `||v_j||^2<=1/2`.                             (3.1)

Then the indices can be partitioned into two disjoint sets `S,T` such that, with

`G_S=sum_(j in S) v_j v_j^T`, `G_T=sum_(j in T) v_j v_j^T=I_2-G_S`,

one has

`det G_S >= delta`, `det G_T >= delta`,                              (3.2)

where the explicit universal constant is

`delta=9/7168`.                                                       (3.3)

Consequently

`delta I_2 <= G_S,G_T <=(1-delta)I_2`.                              (3.4)

### Proof

For each unordered pair `e={j,k}` define the Pluecker edge weight

`w_jk=det(v_j,v_k)^2>=0`.                                            (3.5)

Cauchy--Binet applied to (3.1) gives

`sum_(j<k) w_jk=det I_2=1`.                                         (3.6)

Let the weighted degree of vertex `j` be

`d_j=sum_(k!=j)w_jk`.

Using the ninety-degree rotation matrix `J` and (3.1),

`d_j=sum_k <Jv_j,v_k>^2`
`   =v_j^T J^T (sum_k v_kv_k^T)Jv_j`
`   =||v_j||^2<=1/2`.                                                (3.7)

Also `sum_j d_j=2`.

Choose a random cut by putting each vertex independently in `S` or `T` with probability `1/2`. Cauchy--Binet gives

`det G_S=sum_(j<k) w_jk 1_{j,k in S}`,
`det G_T=sum_(j<k) w_jk 1_{j,k in T}`.                               (3.8)

The product contributes only from two vertex-disjoint edges. Therefore

`E[det G_S det G_T]
 =(1/16) D`,                                                         (3.9)

where

`D=sum_(e,f disjoint, ordered) w_e w_f`.

Since the total ordered edge-pair mass is one, while the mass of ordered pairs sharing at least one vertex is

`sum_j d_j^2-sum_e w_e^2`

(the identical pair is counted at both endpoints and must be corrected once),

`D=1-sum_j d_j^2+sum_e w_e^2`.                                      (3.10)

It remains to lower-bound `D` under `d_j<=1/2`, `sum d_j=2`.

Let

`L={j:d_j<1/4}`, `m=sum_(j in L)d_j`.

Then

`sum_j d_j^2
 <=(1/2)sum_(j notin L)d_j+(1/4)sum_(j in L)d_j`
` =1-m/4`.                                                          (3.11)

Hence

`D>=m/4+sum_e w_e^2`.                                                (3.12)

If `m>=1/4`, then `D>=1/16`.

If `m<1/4`, every edge incident to `L` has total weight at most `m`; hence the total edge weight carried entirely by the high-degree set `H=L^c` exceeds `3/4`. Since every vertex in `H` has degree at least `1/4` and the total degree is two, `|H|<=8`. Thus at most `C(8,2)=28` high-high edges carry mass greater than `3/4`, and Cauchy--Schwarz gives

`sum_e w_e^2 >= (3/4)^2/28=9/448`.                                  (3.13)

Combining the two cases,

`D>=9/448`.                                                         (3.14)

By (3.9),

`E[det G_S det G_T]>=9/7168=delta`.

Therefore some cut satisfies (3.2). Since `0<=G_S,G_T<=I_2`, both determinants are at most one, so their product lower bound forces each determinant to be at least `delta`. Each largest eigenvalue is at most one, hence each smallest eigenvalue is at least its determinant; using `G_T=I-G_S` gives the upper bounds in (3.4). QED.

### Numerical size

`delta=9/7168=0.001255580357142857...`, and

`2/sqrt(delta)=56.442694636...`.                                    (3.15)

No numerical computation is used in the proof.

## 4. Application to the named-partner heavy-null state

Apply Theorem 3.1 to the residual frame (2.3) obtained from the named partner's compressed row and the preceding B10 residual-heavy closure. We get disjoint sets `S,T` with (3.4).

Define the two residual bank projections

`Y_S=sum_(j in S) v_j X_j`, `Y_T=sum_(j in T) v_j X_j`.              (4.1)

The two vectors are genuinely independent because they use disjoint original-coordinate banks. Put

`Z_S=G_S^(-1/2)Y_S`, `Z_T=G_T^(-1/2)Y_T`.                           (4.2)

Within each bank, the two coefficient columns of the normalized projection are orthonormal. Hence the source-pinned two-dimensional product marginal theorem gives

`||p_(Z_S)||_infinity<=2`, `||p_(Z_T)||_infinity<=2`.                (4.3)

Scaling back and using (3.2),

`||p_(Y_S)||_infinity,
 ||p_(Y_T)||_infinity <=2/sqrt(delta)<56.443`.                        (4.4)

Thus the entire surviving residual-diffuse overlap state has been reduced to **two independent, uniformly nondegenerate two-dimensional product banks**, plus the already isolated heavy null coordinate. No projected-coordinate independence has been asserted inside either two-dimensional bank.

There is a second exact connection to the source-pinned account03/B09 Pluecker theorem. In its notation, the rank-two Pluecker masses of this cut are

`W_S=det G_S`, `W_T=det G_T`,

so

`W_S W_T>=delta^2`.                                                   (4.5)

Therefore, whenever a rank-two spectral component with eigenvalues `lambda_1,lambda_2` is exposed as a free cross block on this cut, account03/B09's exact cross-singular identity gives

`sigma_1 sigma_2
 =|lambda_1 lambda_2| sqrt(W_S W_T)
 >=delta |lambda_1 lambda_2|`.                                       (4.6)

Its direct bilinear theorem would then give the actual density inequality

`||p||_infinity
 <=2 sqrt(pi)/(sqrt(delta)*sqrt(|lambda_1 lambda_2|))`.              (4.7)

Equation (4.7) is conditional on exposing that free bilinear block; the current full rank-three form still has same-bank quadratic curvature, so I do **not** claim (4.7) closes the heavy-null branch. The new content is that the product-preserving bank geometry no longer degenerates with the number of physical coordinates.

## 5. Exact target-valid obstruction to returning to local atoms

The two-bank step is necessary: even after the named-partner compression and the residual-diffuse reduction, no uniformly good physical pivot, pair, or triple need exist.

Fix `m>=2`, set `c=7/9`, and take the Witt spectral matrix

`M=[[0,1,0],[1,0,0],[0,0,1]]`,                                     (5.1)

whose eigenvalues are `{1,-1,1}`. Construct a Parseval physical frame from four disjoint coordinate banks:

- one distinguished row `u_0=sqrt(7/9)e_1`;
- `m` longitudinal rows `sqrt(2/(9m)) e_1`;
- `m` rows `m^(-1/2)e_2`;
- `m` rows `m^(-1/2)e_3`.

Their outer products sum to `I_3`, so `A=UMU^T` has exactly the three nonzero eigenvalues `{1,-1,1}`. The distinguished row is an exact null pivot. Every complementary residual leverage is either zero or `1/m<=1/2`, so this family lies **inside the surviving residual-diffuse state**.

Nevertheless every nonzero scalar pivot has size at most `1/m`; every pair determinant involving the heavy null row and an `e_2` row has magnitude `(7/9)/m`; and every nonzero principal triple determinant is at most

`7/(9m^2)`.                                                         (5.2)

Thus every fixed local-pivot / local-pair / local-triple certificate degenerates as `m->infinity`. In particular the stronger candidate

> residual-diffuse heavy-null geometry forces one uniformly conditioned physical atom

is false inside the exact target class.

This is not a QFORM counterexample. Aggregate the first two `e_1` banks into

`Z_1=sqrt(7/9)X_0+sqrt(2/(9m)) sum_(a=1)^m X_a`,

and put

`Z_2=m^(-1/2)sum_(b=1)^m X_b`,
`Z_3=m^(-1/2)sum_(c=1)^m X_c`                                      (5.3)

on the two remaining disjoint banks. The three variables are genuinely independent normalized linear forms, each with density at most `sqrt(2)`, and

`Q=2Z_1Z_2+Z_3^2`.                                                   (5.4)

Applying the completed named-partner account03/B10 r13 cap-`K` hyperbolic-square theorem with `K=sqrt(2)`, joint pair cap `H=2`, and unit coefficients gives

`||p_Q||_infinity
 <=3*2^(5/3)
 <9.525`,                                                           (5.5)

uniformly in `m` and for every independent cap-one input law. So the family is paid exactly by bank aggregation while every local atom vanishes.

## 6. What this pays and what remains

**Proved in this run.** In the named partner's compressed near-endpoint branch, after the previous B10 theorem eliminates every residual-heavy row, the residual two-dimensional Parseval frame admits a partition into two disjoint original-coordinate banks whose Gram matrices are both bounded below by `delta I_2`, `delta=9/7168`. Each bank therefore yields a genuine two-dimensional product projection with density cap `<56.443`, and the two bank projections are independent. This removes dimension/cardinality loss from the residual-diffuse geometry.

**Refuted in this run.** The surviving residual-diffuse state does not force any one dimension-free physical pivot, pair, or triple. The explicit family in Section 5 has exact target spectrum `{1,-1,1}`, satisfies the heavy-null and residual-diffuse hypotheses, but all such local scales vanish with `m`; its full output nevertheless has the uniform aggregate bound (5.5).

**First unpaid implication.** The remaining step is now

`QFORM-NULLROW-TWOBANK-CURVATURE-ABSORPTION-v1`:

> Starting from the heavy independent null coordinate and the two independent uniformly nondegenerate residual banks furnished by Theorem 3.1, absorb the same-bank quadratic curvature and the small longitudinal residual components without collapsing to a scalar C4 contrast or a conditional-density supremum. Equivalently, prove a bank-level rank-three smoothing theorem that contains the free bilinear inequality (4.7) and the three-bank hyperbolic-square endpoint (5.5) as paid subcases.

This is the same structural obstruction identified independently in account03/B09's `QFORM-BILINEAR-BLOCK-ABSORPTION-v1` / later curved-bank work: a free rank-two cross block is paid at linear interval scale, but arbitrary same-bank quadratic terms cannot simply be discarded. The new B10 lemma supplies a universal product-preserving bank split specifically in the heavy-null residual-diffuse exact-rank-three geometry.

The unrestricted exact-rank-three case and the full arbitrary-rank QFORM conjecture remain **OPEN / NOT PROVED / NOT DISPROVED**. Continuity is not established here.
