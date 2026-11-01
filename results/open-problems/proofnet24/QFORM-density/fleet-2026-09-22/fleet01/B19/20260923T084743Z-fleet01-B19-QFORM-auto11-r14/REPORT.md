SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 01, slot B19, 2026-09-23T08:47:43Z.
attacking: the partner r30 thin-line STAR residue: preserve the heavy thin-line receiver row, move an aggregate complementary subset of original receiver coordinates, and recover both source conditioning and cross two-volume without deleting the near-coloop coefficient.

# fleet01/B19 r14 — aggregate complementary repartition closes the thin-line STAR residue

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Universal proof assembly / SYNTHESIS  
**Fresh owner control:** revision `2026-09-22.15`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** `ESSENTIAL_STEP_APPLIED / NEW PAID SUBBRANCH / FULL QFORM OPEN`.

The unrestricted theorem remains OPEN. This report proves a new exact-rank-three payment inside the latest designated-partner residue and sharpens the first unpaid implication in that chamber. It keeps every random coefficient exactly, uses only literal regrouping of ORIGINAL independent coordinates, and does not use post-rotation independence, arbitrary-joint coarea, conditional-density-as-independence, pointwise law-uniform stationary phase, or small-matrix perturbation continuity.

## 1. Fresh source-pinned input actually used

The current designated partner is fleet02/B19 r30:

`yspennstate/math-open-problems@6c86c298328a72930d9f61b2cef4e3922155439e`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B19/20260923T083941Z-fleet02-B19-QFORM-r30/REPORT.md`.

Its exact-rank-three chamber is

`A=R M R^T`, `R^T R=I_3`, `M=M^T`, `s_min(M)>=1`,                 (1.1)

with an ORIGINAL-coordinate partition `I union J`,

`G=R_I^T R_I`, `H=R_J^T R_J=I-G`,                               (1.2)

`rank(R_I)=3`, `rank(H)=2`, and exact-rank-two physical cross block

`C=A[I,J]`, `rho=s_1(C)s_2(C)>=rho_0`,                           (1.3)

where

`rho_0=sqrt(29/3072)=0.097160198469675...`.                       (1.4)

Let `W=range(H)`. If `0<h_1<=h_2<1` are the two eigenvalues of `H|_W`, the still-unpaid near-rankdrop chamber has

`h_1<1/64`, `h_2>63/64`.                                         (1.5)

For each physical receiver row `s_k` define the whitened row

`v_k=(H|_W)^(-1/2)s_k`,                                          (1.6)

so

`sum_{k in J} v_k v_k^T=I_W`.                                    (1.7)

Write `ell_k=||v_k||^2`. The partner r30, after the fleet03/B19 weighted-matching compiler, leaves STAR or one explicit TRIANGLE residue. In STAR there is an actual physical row `j` with

`ell_j>47/64`.                                                     (1.8)

Choose an orthonormal eigenbasis `(e_1,e_2)` of `H|_W`, with `e_1` the thin `h_1` direction and `e_2` the thick `h_2` direction, and write

`v_k=(v_{k1},v_{k2})`.                                            (1.9)

The partner proves that if a STAR row satisfies

`ell_j<=63/64`, `v_{j2}^2>=1/64`,                                (1.10)

then moving that one ORIGINAL coordinate to the source bank gives a continuous density bound `<133`. Therefore every STAR survivor of r30 satisfies at least one of

(A) `ell_j>63/64`,

or

(B) `v_{j2}^2<1/64`, `v_{j1}^2>23/32`, and the physical/global spectral leverage is `<1/32`.       (1.11)

The same partner supplies the exact cross-product identity under any product-preserving repartition. If `G',H'` are the new source/receiver Grams and `rho'` is the new rank-two cross singular product, then on the fixed plane `W`,

`(rho')^2 = det(H'|_W) det((M G' M)|_W)`.                         (1.12)

The completed product-safe analytic receiver used below is fleet01/B19:

`yspennstate/math-open-problems@d72be34399b8d0325c715973e7af3a37df7ce227`,

`QFORM-RANK2-CROSS-TRANSVERSE-UNIFORM-NEARNULL-v1`. In the exact three-dimensional source / rank-two-cross scope it gives

`||p_Q||_infinity <= C_* R_perp^(-1/4) (rho')^(-3/8)`,           (1.13)

where

`C_*=2^(15/4)3^(-3/8)=8.911319467025...`,                         (1.14)

and `R_perp` is the norm of the source self block on the unit direction transverse to the cross range. The density is continuous and vanishes at infinity in this branch.

## 2. New theorem

### Theorem 2.1 — `QFORM-THINLINE-STAR-AGGREGATE-REPARTITION-v1`

Assume (1.1)-(1.9), the double-coloop inequalities (1.5), and suppose there is a STAR row `j` satisfying the thin-line alternative

`v_{j2}^2<1/64`, `v_{j1}^2>23/32`.                                (2.1)

Assume no receiver row is an extreme normalized coloop:

`ell_k<=63/64` for every `k in J`.                                (2.2)

Assume also that the state has survived the partner r30 single-row angle compiler. Then there is a subset

`K subset J\{j}`                                                  (2.3)

such that after the exact ORIGINAL-coordinate repartition

`I'=I union K`, `J'=J\K`,                                        (2.4)

the same full quadratic form has a continuous density satisfying

`boxed: ||p_Q||_infinity <62.49.`                                 (2.5)

Consequently, after combining with partner r30, **every still-unpaid STAR state contains an actual receiver row with**

`boxed: ell_k>63/64.`                                             (2.6)

Thus the partner's thin-line alternative (B) is no longer an independent debt: if it occurs without an extreme coloop, it is paid by (2.5).

### Proof

#### Step 1: select a complementary thick-direction packet without selecting a reciprocal minor

Put

`w_k=v_{k2}^2`, `k in J`.                                        (2.7)

By Parseval,

`sum_{k in J} w_k=1`.                                             (2.8)

For the distinguished thin-line row `j`, (2.1) gives `w_j<1/64`, hence

`sum_{k!=j} w_k>63/64`.                                          (2.9)

Because the state has survived the partner r30 theorem and (2.2) excludes alternative (A), every row with `w_k>=1/64` must satisfy

`ell_k<=47/64`;                                                   (2.10)

otherwise it would itself be a STAR row with `ell_k<=63/64` and `w_k>=1/64`, and the partner would already pay it by `<133`. Therefore every such `w_k` is at most `47/64`.

Now greedily add indices from `J\{j}` until their thick-direction mass first reaches `1/8`. Since the available mass is greater than `63/64`, this stops. Let `K` be the selected set and

`s=sum_{k in K}w_k`.                                              (2.11)

If the last increment is `<1/64`, then `s<1/8+1/64`. If it is at least `1/64`, (2.10) bounds that last increment by `47/64`. In either case

`boxed: 1/8 <= s <55/64.`                                        (2.12)

This is aggregation before inversion: no individual small determinant or coefficient is paid reciprocally.

Define the normalized covariance of the moved packet and its retained complement,

`T_K=sum_{k in K}v_kv_k^T`,
`R_K=I_W-T_K`.                                                    (2.13)

Let

`T_rest=sum_{k in J\(K union {j})}v_kv_k^T`,                     (2.14)

so

`R_K=v_jv_j^T+T_rest`.                                           (2.15)

Write `v_j=(a,b)`. By (2.1),

`a^2>23/32`, `b^2<1/64`.                                         (2.16)

The `e_2` mass in `T_rest` obeys, by (2.8), (2.12), and (2.16),

`(T_rest)_{22}=1-s-b^2>1-55/64-1/64=1/8`.                       (2.17)

The `e_1` mass satisfies

`(T_rest)_{11}<=1-a^2<9/32`.                                     (2.18)

For a two-dimensional PSD matrix `T`, `|T_12|<=sqrt(T_11 T_22)`. Also

`det(vv^T+T)=det T+v_perp^T T v_perp`,                            (2.19)

where `v_perp=(-b,a)`. Hence

`det R_K`
`>=(-b,a) T_rest (-b,a)^T`
`>=( |a| sqrt((T_rest)_{22})-|b|sqrt((T_rest)_{11}) )^2`          (2.20)

and therefore

`det R_K >= c_0`,                                                 (2.21)

with the universal constant

`c_0=(sqrt(23)/16-3/(32sqrt(2)))^2`
`   =0.05449806650512538...`.                                    (2.22)

In particular `R_K` is positive definite. This lower bound is the key: the retained thin-line STAR row supplies one direction and the retained aggregate thick mass supplies the other.

#### Step 2: exact repartition and source conditioning

Move the ORIGINAL coordinates in `K` from receiver to source. In spectral-frame coordinates the new Grams are exactly

`H'=H^(1/2) R_K H^(1/2)`,
`G'=I-H'=G+H^(1/2)T_KH^(1/2)`.                                   (2.23)

No random variable is changed or approximated.

On `W`, use the eigenbasis of `H`. Since

`G|_W=diag(1-h_1,1-h_2)`,                                       (2.24)

a direct 2x2 determinant expansion gives

`det(G'|_W)`
`=(1-h_1)(1-h_2)`
` +(1-h_2)h_1(T_K)_{11}`
` +(1-h_1)h_2(T_K)_{22}`
` +h_1h_2 det(T_K)`.                                             (2.25)

All four terms are nonnegative. Since `(T_K)_{22}=s`, (1.5), and (2.12),

`det(G'|_W)`
`> (63/64)(63/64)(1/8)`
`=: eta_G`
`=3969/32768`
`=0.121124267578125.`                                            (2.26)

Because `H'>=0`, one has `G'=I-H'<=I`, so the larger eigenvalue of `G'|_W` is at most one. Thus

`lambda_min(G'|_W)>=det(G'|_W)>=eta_G`.                          (2.27)

On the one-dimensional kernel of `H`, `G'` acts as the identity. Consequently

`boxed: G'>=eta_G I_3.`                                          (2.28)

Let `P'=R_{I'}`. The source self block is

`B'=P'MP'^T`.                                                     (2.29)

On `range(P')` it is orthogonally represented by

`(G')^(1/2)M(G')^(1/2)`.                                         (2.30)

Since `s_min(M)>=1`,

`s_min^+(B')>=eta_G`.                                             (2.31)

Therefore the transverse source-row norm required by (1.13) obeys

`R_perp>=eta_G`.                                                   (2.32)

#### Step 3: retain a constant fraction of the cross two-volume despite h_1 ->0

Equation (2.23) and (2.21) give

`det(H'|_W)=det(H|_W)det(R_K)>=c_0 det(H|_W)`.                    (2.33)

Moreover `G'>=G`, hence, because `M` is symmetric,

`MG'M-MGM=M(G'-G)M>=0`.                                          (2.34)

Compression to `W` preserves PSD order. The original cross product `rho>0` implies the relevant compressed matrices are positive definite, and determinant is monotone on positive-definite 2x2 matrices. Using the partner identity (1.12),

`(rho')^2`
`=det(H'|_W)det((MG'M)|_W)`
`>=c_0 det(H|_W)det((MGM)|_W)`
`=c_0 rho^2`.                                                     (2.35)

Therefore

`boxed: rho'>=sqrt(c_0) rho>=sqrt(c_0)rho_0`,                    (2.36)

where

`sqrt(c_0)=0.23344820947080613...`,
`sqrt(c_0)rho_0=0.02268187436457382...`.                          (2.37)

This is why the argument is uniform even though `h_1` may tend to zero: it never lower-bounds the new cross product by the smallest receiver-frame eigenvalue in isolation. It transfers a fixed **relative determinant fraction** before inversion.

#### Step 4: apply the completed analytic receiver to the actual new partition

The source bank `I'` still contains all its exact self curvature in the three-dimensional physical range `range(P')`; the new cross block has exact rank two because `H'|_W` is positive definite; and the opposite-bank self curvature remains arbitrary. Thus (1.13) applies to the exact quadratic form and gives

`||p_Q||_infinity`
`<=C_* eta_G^(-1/4)(sqrt(c_0)rho_0)^(-3/8)`
`=62.4819564088...`
`<62.49`.                                                         (2.38)

The imported receiver also gives an integrable characteristic function, hence a continuous density vanishing at infinity in this paid branch. QED.

## 3. Direct application to the designated partner r30 residue

The partner r30 STAR compiler leaves precisely (A) or (B) in (1.11). Apply Theorem 2.1 to (B).

If no extreme normalized coloop exists, i.e. if every `ell_k<=63/64`, then all hypotheses of Theorem 2.1 hold and the form is paid by `<62.49`. Therefore an unpaid STAR state cannot satisfy (B) alone. If (B) coexists with a row satisfying (A), classify the state under (A).

Hence the r30 STAR residue sharpens from

`(A) extreme coloop OR (B) thin-line globally-light STAR`

to the single condition

`boxed: (A) there exists an actual receiver row k with ell_k>63/64.`  (3.1)

This is an equation-level use of the designated partner: its threshold `47/64`, its single-row `<133` compiler, its double-coloop inequalities, and its exact cross determinant identity are all used in the proof above.

## 4. Compact conditional proof graph after this run

The source-correct proof graph is now:

1. The global synthesis reported by partner r30 reduces the unrestricted theorem, via its completed transfer, to a fixed strict no-pivot statement `N3(tau)`; **N3 itself remains open**. No extra-spectrum component is deleted.
2. Existing physical scalar/pair pivots, ridge/window packets, sufficiently diffuse cross-volume packets, semidefinite exact-rank-three forms, and the paid side of the exact-rank-three indefinite geometry remain available only at their source-pinned hypotheses.
3. In the current exact-rank-three aggregate rank-two-cross chamber, fleet03/B19 r28 reduces the small-disjoint-basis-mass state to STAR or TRIANGLE, paying its nondegenerate triangle branches.
4. Partner fleet02/B19 r30 pays every STAR row with `ell<=63/64` and thick whitened mass `>=1/64`, leaving extreme coloop or thin-line STAR.
5. **Theorem 2.1 of this run pays every thin-line STAR state unless an extreme coloop already exists.** Thus the STAR branch has only one remaining geometry: `ell>63/64`.
6. The only other exact-rank-three residue carried from r30 is its small-pivot TRIANGLE packet: global row leverage `>21/64`, physical diagonal `<1/64`, and off-diagonal star energy `>1343/4096`.
7. Arbitrary-extra-spectrum descent from the global no-pivot class into an exhaustive set of these paid exact-rank-three chambers is still a separate debt.

Therefore the first unpaid implication **inside the present exact-rank-three rank-two-cross chamber** is sharpened to

`QFORM-EXTREME-COLOOP-OR-SMALLPIVOT-TRIANGLE-v2`:

> uniformly pay, with original-coordinate product provenance and no coefficient deletion, either
> 
> (A) a STAR receiver row with normalized leverage `ell>63/64`, or
> 
> (C) the r28/r30 TRIANGLE residue with global row leverage `>21/64`, physical diagonal `<1/64`, and off-diagonal star energy `>1343/4096`.

Globally the first unpaid implication remains `N3(tau)` plus its arbitrary-extra-spectrum structural descent.

## 5. First attack on the now-isolated extreme-coloop endpoint

The extreme-coloop alternative has an exact additional structure that should be used rather than inverted. If `v` is a normalized receiver row with

`ell=||v||^2>63/64`,                                               (5.1)

put `n=v/sqrt(ell)`. The covariance of all other normalized receiver rows is exactly

`T_rest=I-vv^T`.                                                   (5.2)

Hence

`n^T T_rest n=1-ell<1/64`,                                       (5.3)

whereas for the orthogonal unit vector `n_perp`,

`n_perp^T T_rest n_perp=1`.                                      (5.4)

Thus the remaining receiver bank is quantitatively a **complementary line bank**: all of its normalized leakage along the coloop direction is `<1/64`, while it carries unit mass in the perpendicular direction. This is exact, not perturbative. It strongly suggests that the next payment should be a two-hub / grouped-line-bank transducer that keeps the coloop row in the receiver bank, rather than moving it and paying a factor `(1-ell)^(-alpha)`.

The obstacle is equally explicit: after translating this normalized statement back by `H^(1/2)`, the physical line geometry is anisotropically distorted by `h_1<1/64<h_2`; a valid receiver must combine that distortion with the fixed cross product `rho>=rho_0` before taking any reciprocal local coefficient. The aggregate determinant transfer used in Theorem 2.1 is the model for that next step.

## 6. Signs, degeneracies, arbitrary laws, and continuity

All signs of `M` are allowed. Repeated eigenvalues are allowed. The proof uses only `s_min(M)>=1` and PSD Gram identities; no definiteness of `M` is assumed. Every input coordinate may have an arbitrary probability density bounded by one, with unbounded support, disconnected support, no moments, and no regularity. No independence is asserted after a spectral rotation. Independence is preserved only because `I'` and `J'` are literal disjoint sets of original coordinates.

The new paid branch has a continuous `C_0` density by the imported receiver. The full-target continuity conclusion remains OPEN separately from essential boundedness.

## 7. Status

- `QFORM-THINLINE-STAR-AGGREGATE-REPARTITION-v1`: **PROVED**.
- Partner r30 thin-line STAR residue without an extreme coloop: **PAID**, continuous density `<62.49`.
- Partner r30 STAR residue after this run: **extreme normalized coloop only**.
- Small-pivot TRIANGLE residue: **OPEN**.
- Global strict no-pivot `N3(tau)` / arbitrary-extra-spectrum structural descent: **OPEN**.
- Full QFORM theorem: **OPEN / NOT PROVED / NOT DISPROVED**.
- Full-target continuity: **OPEN**.
- Two independent end-to-end reviews of a full proof: **not available**.
