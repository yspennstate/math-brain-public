SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B19, 2026-09-23T07:13:20Z.
attacking: the rank-two-cross near-coloop stability gate by an exact product-preserving repartition of the physical coordinate banks.

# account02/B19 — diffuse near-coloop repartition

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** Universal proof assembly / SYNTHESIS / complementary constructions and source-valid counterexamples  
**Control:** fresh owner control revision `2026-09-22.15`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository retrieval is not native learned-memory ingestion.  
**Status:** `ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREM / FULL QFORM OPEN`.

The unrestricted conjecture remains open. This run proves a product-preserving structural/payment theorem for the current exact-rank-three rank-two-cross near-coloop survivor. It uses no moments, support bounds, log-concavity, Gaussianity, post-rotation independence, arbitrary-joint coarea estimate, coefficient-continuity argument, or deletion of a small quadratic perturbation.

## 1. Source-pinned proof state

The current designated partner is account03/B19 r27:

`yspennstate/math-open-problems@a2c543d935168ec8996535219d8c0c25ae261763`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260923T062711Z-account03-B19-QFORM-r27/REPORT.md`.

In the exact-rank-three representation

`A = R M R^T`, `R^T R = I_3`,                                   (1.1)

with `M=M^T` invertible and every eigenvalue of `M` of absolute value at least one, take a genuine partition of the ORIGINAL coordinates `I union J`. Write

`P=R_I`, `S=R_J`, `G=P^T P`, `H=S^T S=I-G`.                    (1.2)

Assume `rank(P)=3` and the physical cross block

`C=A_IJ=P M S^T`                                                (1.3)

has exact rank two. Then `rank(S)=2`. If `u` spans `ker H`, `W=u^perp`, and the two eigenvalues of `G|_W` are `g1,g2`, the partner proves the exact identity

`rho R_perp = |det M| Theta`,                                   (1.4)

where

`rho=s1(C)s2(C)`,
`Theta=sqrt(g1 g2 (1-g1)(1-g2))`,
`R_perp=||B r||`, `B=A_II`,                                    (1.5)

and `r` is the unit vector in `range(P)` transverse to `range(C)`. The current compound-energy route supplies

`rho >= rho0 := sqrt(29/3072)`.                                (1.6)

The partner combines (1.4) with account01/B19's completed receiver and pays `Theta>=2^-12` by a continuous density bound `<96`; therefore every unpaid survivor has

`min{g1,g2,1-g1,1-g2}<1/64`.                                   (1.7)

The analytic receiver used there is account01/B19:

`yspennstate/math-open-problems@d72be34399b8d0325c715973e7af3a37df7ce227`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B19/20260923T060843Z-account01-B19-QFORM-auto11/REPORT.md`.

In its precise original-product scope, for a rank-two cross block with singular product `rho'`, a three-dimensional source space containing all source self curvature, and transverse source row norm `R'>0`, it proves

`||p_Q||_infinity <= C_* (R')^(-1/4) (rho')^(-3/8)`,            (1.8)

with continuous density and

`C_* = 2^(15/4) 3^(-3/8) < 8.912`.                             (1.9)

The required newest-Claude source `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` is also used at equation level below. Its proved D5 theorem states that for any genuine physical cross block `N`,

`||p_Q||_infinity <= 5 sqrt(2e) e_5(N^T N)^(-1/10)`             (1.10)

with no volume-marginal condition. Hence

`s5(N)>=1/64  =>  e5(N^T N)>=64^(-10)
                 => ||p_Q||_infinity <= 320 sqrt(2e)
                 =746.126074... <746.127`.                     (1.11)

Thus a source-valid full proof graph may remove every such fifth-cross-direction exit before reaching the rank-two-cross collar treated here. This is a real inequality application of the required source, not a relabeling of its theorem.

Two fresh corrections were consumed before this proof. `QFORM-UNIFORM-MATRIX-PERTURBATION-CONTINUITY-FALSE-v1` forbids deleting a small matrix component for arbitrary unbounded/fragmented product laws; `QFORM-NEARNULL-JOINT-PAIR-CAP-FALSE-v1` forbids replacing original-product provenance by an arbitrary dependent pair with a density cap. The argument below avoids both: it changes only which ORIGINAL coordinate indices are assigned to the two banks, and then applies (1.8) to the exact unreduced quadratic form.

## 2. New theorem

### Theorem 2.1 — `QFORM-RANK2-CROSS-DIFFUSE-J-REPARTITION-v1`

Assume (1.1)-(1.3), `rank(P)=3`, `rank(C)=2`. Let `u` span `ker H` and `W=u^perp`. Since `H=sum_{j in J}s_j s_j^T` has kernel `u`, every row `s_j` of `S` lies in `W`.

Suppose

`lambda_min(H|_W) >= 1/64`.                                    (2.1)

For each `j in J` define its normalized `J`-frame leverage

`ell_j := s_j^T (H|_W)^(-1) s_j`.                              (2.2)

If

`max_{j in J} ell_j <= 1/16`,                                  (2.3)

then there is a subset `K subset J` such that, after the exact ORIGINAL-coordinate repartition

`I' = I union K`, `J' = J \ K`,                                (2.4)

the same quadratic form `A` has a continuous density satisfying

`boxed: ||p_Q||_infinity < 776.`                                (2.5)

More precisely, with

`eta := 7/128`,                                                  (2.6)

the new partition satisfies

`R_{I'}^T R_{I'} >= eta I_3`,                                  (2.7)

`lambda_min^+(R_{J'}^T R_{J'}) >= eta/64`,                     (2.8)

and its physical cross block `C'=A[I',J']` has exact rank two and

`s2(C') >= eta/8`,
`s1(C')s2(C') >= eta^2/64`.                                    (2.9)

The source self block `B'=A[I',I']` has smallest nonzero singular value at least `eta`; hence its transverse row norm in the receiver (1.8) is at least `eta`.

### Proof

#### Step 1: normalize the two-dimensional `J` frame

On `W`, put

`v_j=(H|_W)^(-1/2)s_j`.                                        (2.10)

Then

`sum_{j in J} v_j v_j^T = I_W`,                                (2.11)

so `(v_j)` is a two-dimensional Parseval frame, and

`||v_j||^2=ell_j<=epsilon:=1/16`,
`sum_j ell_j=2`.                                                (2.12)

For every unordered pair `T={i,k}` define

`d_T = det(v_i,v_k)^2`.                                        (2.13)

By Cauchy-Binet applied to (2.11),

`sum_T d_T = 1`.                                                (2.14)

There is also an exact marginal identity

`sum_{T: j in T} d_T = ell_j`.                                 (2.15)

Indeed,

`sum_k det(v_j,v_k)^2
 = ||v_j||^2 sum_k ||v_k||^2
   - v_j^T (sum_k v_kv_k^T) v_j
 = 2||v_j||^2-||v_j||^2
 = ell_j`.                                                      (2.16)

#### Step 2: a disjoint two-basis split

Choose a random subset `K subset J` by putting each index into `K` independently with probability `1/2`. Define

`V_K=sum_{j in K}v_jv_j^T`,
`V_{K^c}=I_W-V_K`.                                              (2.17)

Again by Cauchy-Binet,

`det V_K = sum_{T subset K, |T|=2} d_T`,
`det V_{K^c} = sum_{U subset K^c, |U|=2} d_U`.                  (2.18)

Therefore

`E[det V_K det V_{K^c}]
 = (1/16) sum_{T cap U = empty} d_T d_U`.                       (2.19)

The ordered mass of intersecting pair-pairs is bounded using (2.15):

`sum_{T cap U != empty}d_Td_U
 <= sum_j (sum_{T: j in T}d_T)^2
 = sum_j ell_j^2
 <= epsilon sum_j ell_j
 =2epsilon
 =1/8`.                                                        (2.20)

Since the total ordered pair-pair mass equals one by (2.14),

`E[det V_K det V_{K^c}] >= (1/16)(1-1/8)=7/128=eta`.            (2.21)

Hence for some deterministic `K`,

`det V_K det V_{K^c} >= eta`.                                  (2.22)

Both `V_K` and `V_{K^c}` are positive semidefinite contractions, so each determinant is at most one. Consequently both determinants are at least `eta`. For a two-dimensional positive semidefinite contraction `T`,

`lambda_min(T)=det(T)/lambda_max(T) >= det(T)`.                 (2.23)

Thus

`eta I_W <= V_K,V_{K^c} <= (1-eta)I_W`.                        (2.24)

#### Step 3: undo the normalization and repartition physical coordinates

Let

`H_K=sum_{j in K}s_js_j^T`,
`H_{K^c}=sum_{j in K^c}s_js_j^T`.                              (2.25)

Conjugating (2.24) by `(H|_W)^(1/2)` gives

`eta H <= H_K,H_{K^c} <= (1-eta)H` on W.                       (2.26)

Take `J'=K^c` and `I'=I union K`. Then

`H':=R_{J'}^T R_{J'}=H_{K^c}`,
`G':=R_{I'}^T R_{I'}=I-H'`.                                   (2.27)

Because `H'<= (1-eta)H <= (1-eta)I` on `W`, while `H'u=0`,

`G'>=eta I_3`.                                                   (2.28)

Also, by (2.1) and (2.26),

`lambda_min^+(H') >= eta lambda_min(H|_W) >= eta/64`.           (2.29)

In particular `rank R_{I'}=3` and `rank R_{J'}=2`.

#### Step 4: quantitative cross and source-self lower bounds

Write `P'=R_{I'}`, `S'=R_{J'}`. The new cross block is

`C'=P'MS'^T`.                                                    (2.30)

Because `P'M` is injective and `S'^T` has rank two,

`ker C'=ker S'^T`,                                              (2.31)

so `C'` has exact rank two. On the orthogonal complement of that kernel,

`||C'x||
 >= s_min(P') s_min(M) ||S'^T x||
 >= sqrt(eta) * 1 * sqrt(eta/64) ||x||`.                        (2.32)

Therefore

`s2(C') >= eta/8`,                                              (2.33)

and since `s1(C')>=s2(C')`,

`rho':=s1(C')s2(C') >= eta^2/64`.                              (2.34)

The source self block is

`B'=P'MP'^T`.                                                    (2.35)

Let `Q'=P'(G')^(-1/2)`, so `Q'^TQ'=I_3`. On `range(P')`, `B'` is orthogonally represented by

`(G')^(1/2) M (G')^(1/2)`.                                     (2.36)

Hence

`s_min^+(B')
 >= lambda_min(G') s_min(M)
 >= eta`.                                                       (2.37)

For the unit vector `r'` transverse to `range(C')` inside `range(P')`, the receiver's full transverse source-row norm therefore satisfies

`R':=||B'r'|| >= eta`.                                          (2.38)

#### Step 5: pay the repartitioned branch

The hypotheses of account01/B19's product-safe receiver (1.8) now hold with the exact same random quadratic form, merely regrouped into the two original-coordinate banks `I',J'`. Equations (2.34) and (2.38) give

`||p_Q||_infinity
 <= C_* eta^(-1/4) (eta^2/64)^(-3/8)
 = 8192/[7*3^(3/8)]
 = 775.124444... <776`.                                        (2.39)

The receiver also yields continuity and vanishing at infinity in this branch. QED.

## 3. Structural consequence for the current near-coloop gate

The theorem gives a correction-safe dichotomy. In the exact-rank-three rank-two-cross survivor of account03/B19 r27, if the `J`-side rank-two frame is not already quantitatively close to rank one,

`lambda_min(H|_W) >=1/64`,                                     (3.1)

then every unpaid state must violate (2.3), so some ORIGINAL coordinate satisfies

`ell_j=s_j^T(H|_W)^(-1)s_j >1/16`.                             (3.2)

But `sum_j ell_j=2`. Therefore the number of such normalized-heavy rows is strictly less than `32`, hence at most `31`. Thus the former undifferentiated near-coloop stability debt is narrowed to the explicit alternatives

`(NR)  lambda_min(H|_W)<1/64`,                                 (3.3)

or

`(HC)  there is a normalized-heavy physical core of at most 31 J-rows carrying all rows with ell_j>1/16`.  (3.4)

No small coefficient has been discarded. The `NR` branch is a genuine punctured line-bank / near-rank-drop geometry. The `HC` branch is a universal finite-cardinality heavy normalized core plus an exactly retained diffuse remainder.

## 4. Conditional proof graph after this run

A compact source-pinned graph now reads as follows.

1. The owner/newest-Claude synthesis keeps the unrestricted theorem reduced to the still-open no-pivot/N3 structural problem; the full theorem has not been proved.
2. Whenever a genuine physical cross cut has `s5>=1/64`, newest-Claude D5 pays it by (1.11), `<746.127`.
3. In the exact-rank-three aggregate rank-two-cross chamber with `rho>=rho0`, account03/B19 r27 plus account01/B19 pays the balanced frame `Theta>=2^-12` by `<96`.
4. In the remaining frame-near-coloop chamber, Theorem 2.1 of this run pays every state with `lambda_min(H|W)>=1/64` and normalized `J` leverage at most `1/16` by `<776`.
5. Consequently the first exact-rank-three rank-two-cross debt is now only `(NR)` or `(HC)` in (3.3)-(3.4). Existing exact-null-coloop/grouped-coordinate theorems can be applied only at their proved endpoints; no continuity bridge is inferred.
6. Arbitrary-extra-spectrum descent from the global N3/no-pivot class into these exact-rank-three chambers remains a separate full-target debt.

## 5. First unpaid implication, with exact quantifiers

`QFORM-RANK2-CROSS-J-NEARRANKDROP-OR-HEAVYCORE-v1`:

There should be a universal `C<infinity` such that the following holds. For every finite `n`, every product law of independent real coordinates with scalar densities at most one, and every exact-rank-three symmetric matrix `A=RMR^T` with `R^TR=I_3` and all three eigenvalues of `M` of modulus at least one, consider an ORIGINAL-coordinate partition `I union J` satisfying `rank(R_I)=3`, `rank(A_IJ)=2` and the current aggregate cross threshold `s1(A_IJ)s2(A_IJ)>=sqrt(29/3072)`. After excluding all already-paid balanced-frame, fifth-cross-volume, physical-pivot/pair, ridge/volume-stability and exact grouped-coordinate exits, prove `||p_{X^TAX}||_infinity<=C` whenever either

(a) `lambda_min((R_J^TR_J)|_W)<1/64`, with `W=(ker R_J^TR_J)^perp`, or

(b) `(R_J^TR_J)|_W` is invertible and its normalized row leverages contain a heavy core `H0={j: ell_j>1/16}` of cardinality at most `31`,

or give a product-preserving structural descent from these alternatives to an already-paid branch.

The proof may not delete the near-rank-one frame component as a small random perturbation, and may not replace the product bank by a generic dependent projected pair. Those two shortcuts are explicitly refuted by the live correction set.

## 6. Status

- `QFORM-RANK2-CROSS-DIFFUSE-J-REPARTITION-v1`: **PROVED**.
- Diffuse, quantitatively rank-two `J` near-coloop chamber: **PAID**, continuous density `<776`.
- Required newest-Claude D5 was applied at the concrete threshold `s5>=1/64`, giving `<746.127`.
- Remaining exact-rank-three rank-two-cross debt: **near-rankdrop or <=31 normalized-heavy rows**.
- Arbitrary-extra-spectrum/N3 splice: **OPEN**.
- Full QFORM theorem: **OPEN / NOT PROVED / NOT DISPROVED**.
- Full-target continuity: **OPEN**.
- Two independent end-to-end reviews: **NOT AVAILABLE**.
