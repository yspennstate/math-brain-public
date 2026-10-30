SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B19, 2026-09-22T22:10:19Z.
attacking: translation-uniform fractional-trace / near-span synthesis — convert the new aggregate O3 near-span packet into a source-realizable rank-three cross cut whenever the normalized complement frame is diffuse.

# fleet02/B19 r20 — normalized-complement MSS payment for the near-span aggregate branch

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control consumed before publication:** revision `2026-09-22.15`  
**Assignment:** Universal proof assembly / SYNTHESIS  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING THEOREM PROVED / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The exact owner target remains unrestricted: independent original-coordinate real inputs with marginal densities at most one, arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, and no moment/support/log-concavity/diagonal-basis/post-rotation-independence assumption.

## 1. Fresh dependencies and correction boundary

The live correction inbox was reread before this report. The argument below does **not** use arbitrary-joint rank-three coarea, positive conditional projection-density moments, conditional-cap-as-independence, a fixed good local minor, law-uniform pointwise Fresnel decay, or deletion of a small coefficient under unrestricted supports.

The current named partner is fleet03/B19 r18, canonical mathematics

`yspennstate/math-open-problems@4caa949abfce263bcfdcdf7fe175a4a999ae35b5`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B19/20260922T210216Z-fleet03-B19-QFORM-r18/`.

Its theorem `QFORM-SEQUENTIAL-TWO-PIVOT-THIRD-SOURCE-v1` pays every quantitative two-original-coordinate Schur-pivot state by

`||p_Q||_inf <= [4 sqrt(2)/sqrt(|a d|)] [2+log_+((5/sqrt(2))(|d|/s_3(A))^(1/4))]`.

I use it in the conditional proof below to remove the nonnull quantitative two-pivot states before entering the exact-null near-span chamber.

The immediate compatible near-span input is fleet03/B10 r19, source snapshot

`yspennstate/math-open-problems@bb2a985a44425ae3cbfd222da9c42fee8486cf51`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B10/20260922T214631Z-fleet03-B10-QFORM-r19/REPORT.md`.

It proves `QFORM-NEARSPAN-TO-O3-AGGREGATE-v1`: in the compressed exact-rank-three heavy-null state described below, if the two B19 leakage residuals obey `tau_J+tau_K<=1/32`, then either `c<=61/64` and one mixed original-coordinate principal-triple bank has aggregate determinant mass at least `1/256`, or `c>61/64` and the heavy-null principal-triple bank has aggregate determinant mass greater than `61/128`. This removes every inverse power of the small leakage residual from the **structural** reduction, but leaves the diffuse aggregate-bank payment open.

Two older completed inputs are used literally:

1. fleet01/B08 r16 records the Marcus--Spielman--Srivastava two-part frame partition: if a Parseval frame has row norms squared at most `epsilon`, then it admits an original-coordinate bipartition whose two partial Gram matrices are each bounded below by

`delta(epsilon) I`,  `delta(epsilon)=1/2-epsilon-sqrt(2 epsilon)`,

provided `delta(epsilon)>0`.

2. fleet03/B19 r16, `QFORM-EXACT-CROSS-RANK-L2-v1`, canonical source `yspennstate/math-open-problems@9d55d9ca5a7beaed6f693a57bd32b5fc9949b981`, says that a disjoint original-coordinate cross block `C` of exact rank three has a bounded continuous density with

`||p_Q||_inf <= 3e Pi_3(C)^(-1/3)`,

with arbitrary self terms, outside coordinates, and couplings retained.

## 2. Exact compressed state

Work in the source-valid heavy-null exact-rank-three compression

`A=R M R^T`,  `R^T R=I_3`,  `D=|det M|>=1/2`.

There is one distinguished original-coordinate heavy null row

`u_0=sqrt(c) r`,  `r^T M r=0`,  `c>=7/9`.

In an orthonormal spectral basis whose first vector is `r`, Parseval gives the complementary-row Gram matrix

`H := sum_(j!=0) u_j u_j^T = I_3-u_0u_0^T = diag(1-c,1,1)`.      (2.1)

On the `c<=61/64` half of the new B10 near-span dichotomy, `H` is positive definite and

`det H = 1-c >=3/64`.                                             (2.2)

Define the **normalized complement rows**

`z_j=H^(-1/2)u_j`, `j!=0`.                                      (2.3)

Then

`sum_(j!=0) z_j z_j^T=I_3`.                                     (2.4)

Their normalized leverages are

`ell_j=||z_j||^2=u_j^T H^(-1)u_j`.                               (2.5)

This normalization is spectral algebra only; it is not a rotation of the random inputs. Every partition below is a partition of original coordinate indices.

## 3. New theorem — diffuse normalized complement gives a constant cross-rank-three payment

### Theorem 3.1 — `QFORM-NEARSPAN-NORMALIZED-COMPLEMENT-MSS-v1`

Assume the compressed state (2.1), with `c<1`. Let

`epsilon_*=(1-1/sqrt(2))^2=0.0857864376...`.

If for some `0<epsilon<epsilon_*`

`max_(j!=0) ell_j <=epsilon`,                                    (3.1)

put

`delta=1/2-epsilon-sqrt(2epsilon)>0`.                            (3.2)

Then there is a partition of the complementary **original-coordinate** indices into disjoint banks `P,Q` such that the physical cross block

`C=A[P,Q]`

has exact rank three and

`Pi_3(C) >= D(1-c) delta^3`.                                    (3.3)

Consequently

`boxed: ||p_(X^TAX)||_inf <= 3e [D(1-c)]^(-1/3) delta^(-1),`     (3.4)

and the density is continuous.

In particular, on the B10 near-span subbranch `D>=1/2`, `c<=61/64`, if

`max ell_j <=1/16`,                                              (3.5)

then

`delta=7/16-1/(2sqrt(2))=0.0839466094...`

and

`boxed: ||p_Q||_inf <339.450.`                                  (3.6)

This bound is independent of `tau_J,tau_K`, dimension, the input laws, and how the aggregate principal-triple mass is distributed.

### Proof

By (2.4), the `z_j` form a Parseval frame in `R^3`. Apply the completed MSS two-part frame theorem to (3.1). There is a partition `P,Q` such that

`G_P:=sum_(j in P) z_jz_j^T <= beta I`,
`G_Q:=sum_(j in Q) z_jz_j^T <= beta I`,

where

`beta=(1/sqrt(2)+sqrt(epsilon))^2
     =1/2+epsilon+sqrt(2epsilon)=1-delta`.                        (3.7)

Since `G_P+G_Q=I`, the upper bound for one part is a lower bound for the other. Hence simultaneously

`delta I <=G_P,G_Q <=(1-delta)I`.                                (3.8)

Return to the unnormalized spectral rows. If `U_P,U_Q` are the physical-row matrices with rows `u_j`, then

`U_P^T U_P=H^(1/2)G_P H^(1/2)`,
`U_Q^T U_Q=H^(1/2)G_Q H^(1/2)`.                                 (3.9)

Therefore both matrices are positive definite and

`det(U_P^TU_P), det(U_Q^TU_Q) >= delta^3 det H
                                   =delta^3(1-c)`.                (3.10)

The physical cross block is

`C=A[P,Q]=U_P M U_Q^T`.                                         (3.11)

Both `U_P,U_Q` have column rank three and `M` is invertible, so `C` has exact rank three. The standard thin-polar determinant identity gives

`Pi_3(C)
 =D sqrt(det(U_P^TU_P)det(U_Q^TU_Q))
 >=D delta^3(1-c)`,                                             (3.12)

which is (3.3). Applying the completed fleet03/B19 exact-cross-rank theorem gives (3.4), with continuity.

For `epsilon=1/16`, (3.2) gives the displayed value of `delta`. Using `D>=1/2` and `1-c>=3/64`,

`3e[D(1-c)]^(-1/3)delta^(-1)
 <=3e(128/3)^(1/3)delta^(-1)
 =339.4497411778...`,                                           (3.13)

which proves (3.6). QED.

## 4. Why the leverage hypothesis cannot simply be omitted

A constant aggregate principal-triple bank by itself does **not** force a rank-three bipartite cross block. Take normalized complement rows exactly `e_1,e_2,e_3`. Their total three-volume is one, but every nontrivial bipartition has one side of cardinality at most one, hence every cross block factors through rank at most one on that side.

This is not a QFORM counterexample: in the physical heavy-null family

`u_0=sqrt(c)e_1`, `u_1=sqrt(1-c)e_1`, `u_2=e_2`, `u_3=e_3`,

with `M=[[0,1,0],[1,0,0],[0,0,1]]`, the complement principal triple has determinant `1-c`, so for `c<=61/64` it is already paid by the localized physical-triple theorem. The example only shows that **aggregate O3 mass -> balanced rank-three cut** needs either a diffuseness hypothesis or a separate high-leverage/local mechanism. This is exactly the split in Theorem 3.1.

## 5. Updated conditional end-to-end proof

The strongest source-valid synthesis is now:

1. Basis-invariant diffuse high-spectral-window forms are paid by the completed ridge-window/MSS theorem.
2. Quantitative nonnull two-pivot states are paid by the **current named partner fleet03/B19 r18**, with no small ordinary pair-eigenvalue loss.
3. The exact-null heavy residual branch is compressed to the B19 two-bank state. B19 r19 pays the exact span endpoint and every leakage residual bounded away from zero.
4. fleet03/B10 r19 removes the `tau ->0` structural discontinuity: `tau_J+tau_K<=1/32` always carries a constant original-coordinate O3 determinant bank, split at `c=61/64`.
5. **This run pays the entire `c<=61/64` near-span chamber whenever the normalized complement frame is MSS-diffuse**, by an actual rank-three physical cross cut, with no reciprocal `tau` loss.
6. Localized atoms of the O3 bank remain paid by the existing physical-principal-triple theorem.

Thus the first unpaid implication has become strictly narrower.

### `QFORM-NEARSPAN-HIGH-NORMALIZED-LEVERAGE-OR-NEARUNIT-v1` — OPEN

In the compressed exact-rank-three heavy-null state with the B19 two-bank partition and

`tau_J+tau_K<=1/32`,                                             (5.1)

prove a universal density bound in the remaining states where either

**(A)** `c<=61/64` and

`max_(j!=0) u_j^T H^(-1)u_j >= epsilon_*=(1-1/sqrt(2))^2`,       (5.2)

or

**(B)** `c>61/64`,                                                (5.3)

unless an already-paid localized principal triple, quantitative two-pivot packet, ridge packet, exact-cross-rank packet, or generated-span hyperbolic-square packet is present.

Case (A) is now a finite/high-leverage physical-row problem rather than a diffuse aggregate-bank problem. Case (B) is the genuinely near-unit heavy-null O3 bank from B10 r19. A future payment must remain product-preserving; coefficient smallness cannot be treated as a small random error under unrestricted supports.

This exact-rank-three narrowing does not by itself remove the separate arbitrary-additional-spectrum debt in the full conjecture.

## 6. Verification and status

`CHECK.py` in this run directory verifies the threshold `epsilon_*`, the MSS `delta` at `epsilon=1/16`, the lower bound in (3.12) under `D=1/2,c=61/64`, and the numerical density constant in (3.13). Its saved output terminates `QFORM_B19_R20_MSS_CROSSCUT_CHECK_PASS`. The numerical check is regression evidence only; the proof is the exact algebra above plus the pinned MSS and exact-cross-rank theorems.

**New result:** `QFORM-NEARSPAN-NORMALIZED-COMPLEMENT-MSS-v1` — PROVED SUPPORTING THEOREM, target-level in its stated branch.  
**Full exact-rank-three QFORM:** OPEN.  
**Full arbitrary-matrix QFORM:** OPEN.  
**Full-target continuity:** OPEN.
