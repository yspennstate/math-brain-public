SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B02, 2026-09-23T13:37:27Z.
attacking: the first unpaid dominant-pivot-star collar by compiling transport failure into a fixed double-anchor packet, then applying sharp-HY D5 and the existing grouped Fourier receivers without any reciprocal single-minor extraction.

# fleet02/B02 r12 — heavy-star strip concentration to a second double anchor

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Integrated Fourier estimate  
**Status:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Execution context:** `VERIFIED_BRAIN` in the protocol sense: authenticated repository retrieval and actual receiver-memory use occurred in this invocation. `full_brain_connected=false`; no native learned-memory population is claimed.  
**Continuity:** proved on the Fourier-L1 exits stated below; full-target continuity remains open.  
**Target-wide unweighted Fourier L1:** `OPEN_NOT_REFUTED`.

The full target remains the arbitrary product-law statement: independent real coordinates with densities at most one and an arbitrary real symmetric matrix having at least three eigenvalues of modulus at least one. No moments, support, log-concavity, iid assumption, diagonal-basis independence, or post-rotation independence is used.

## 1. Source map and the first unpaid implication

Fresh owner control remained QFORM-only, revision `2026-09-22.15`. The required Claude package was reread at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`.

I use its physical-cross-block volume-sampling theorem, especially the D5 mechanism, together with the reviewed sharp Hausdorff--Young coefficient from

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`:

for a physical cross block `M`,

`||p_Q||inf <= (5e/sqrt(2)) E5(M)^(-1/10)`.                    (1.1)

The newest compatible designated partner is `fleet03/B02` r30,

`yspennstate/math-open-problems@cb55a355bc5c623eb5a98c1db8a0ebaa58ff1027`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260923T125927Z-fleet03-B02-qform-r30/REPORT.md`.

For any ORIGINAL-coordinate physical cross block `B` with `Z=E3(B)>0`, at `q=4/3` it proves the exact dichotomy

`||p_Q||inf <= (9 sqrt(3)e/2) Z^(-1/6)`                        (1.2)

with `phi_Q in L1`, or there are a physical row anchor `i` and column anchor `j` with joint incident third-volume

`J_ij > Z/3`.                                                   (1.3)

This run attacks the second branch, specifically the transport-failure geometry left by the preceding fleet02/B02 run.

## 2. Main theorem — `QFORM-HEAVYSTAR-STRIP-TO-DOUBLEANCHOR-v1`

Normalize the squared `3 x 3` determinants counted by `J_ij` to a probability law on residual row pairs `R` and residual column pairs `T`:

`mu(R,T)=det B[{i} union R,{j} union T]^2/J_ij`.               (2.1)

Let `H` and `K` be fixed two-element physical row/column sets, disjoint from `i,j`. Define the avoidance probabilities

`delta_R=P_mu(R cap H=empty)`,
`delta_C=P_mu(T cap K=empty)`.                                 (2.2)

These are exactly the quantities appearing when the previous incident-(3+2) Fourier transport theorem tries to pair the incident third-volume packet with a fixed physical `2 x 2` pivot on `H x K`.

### Theorem 2.1

If

`delta_R<1/4`, `delta_C<1/4`,                                  (2.3)

then there are `h in H`, `k in K` such that the fixed double-anchor packet

`G_{ih;jk}
 :=sum_{p notin {i,h}, q notin {j,k}}
   det B[{i,h,p},{j,k,q}]^2`                                   (2.4)

satisfies

`boxed: G_{ih;jk} > J_ij/8 > Z/24.`                            (2.5)

Moreover the fixed `2 x 2` physical cross block

`P0=B[{i,h},{j,k}]`                                             (2.6)

has rank at least one. Exactly one of the following holds.

**(A) Invertible second anchor.** If `P0` is invertible, let

`S0=M0-C0 P0^(-1) R0`                                         (2.7)

be its algebraic cross-Schur residual after reordering the same original coordinates. Then

`boxed: |det P0|^2 ||S0||_F^2 = G_{ih;jk} > Z/24.`             (2.8)

**(B) Rank-one second anchor.** If `rank(P0)=1`, choose any genuinely nonzero scalar physical entry `p` of `P0` and form the corresponding scalar cross-Schur residual `S1`. Then

`boxed: p^2 E2(S1) >= G_{ih;jk} > Z/24.`                       (2.9)

No assertion of independence after either Schur shear is made.

### Proof

Under (2.3), inclusion-exclusion gives

`P_mu(R cap H !=empty AND T cap K !=empty)>1/2`.               (2.10)

For every determinant in this event, at least one of the four pairs `(h,k) in H x K` is simultaneously present. Therefore

`sum_{h in H,k in K} G_{ih;jk}
 >= J_ij P_mu(R cap H !=empty,T cap K !=empty)
 > J_ij/2`.                                                     (2.11)

One of the four summands is greater than `J_ij/8`, proving (2.5), and (1.3) gives `>Z/24`.

If `P0=0`, any `3 x 3` matrix containing it as the indicated upper-left `2 x 2` block has its first two rows supported on the single remaining column, hence determinant zero. This contradicts `G_{ih;jk}>0`. Thus `rank(P0)>=1`.

If `P0` is invertible, every determinant in (2.4) obeys the exact block determinant identity

`det [[P0,r_q],[c_p,m_pq]] = det(P0) (S0)_{pq}`.               (2.12)

Squaring and summing proves (2.8).

If `rank(P0)=1`, select a nonzero scalar entry `p` and pivot only on that original row/column. Every determinant in (2.4) becomes `p` times a physical `2 x 2` minor of the scalar cross-Schur residual; those minors are a subset of the Cauchy--Binet family defining `E2(S1)`. Hence (2.9). QED.

This theorem is deliberately aggregate: it never infers a uniformly good single minor from large exterior mass, so it does not violate `QFORM-CROSSMINOR-ALONE-FALSE`.

## 3. Two endpoint branches are already paid by genuine L1 Fourier estimates

The existing fleet02/B02 grouped cross-Schur theorem applies to the packet (2.8) without declaring the sheared variables independent.

If `P0` is invertible and `rank(S0)=1`, its `k=2,r=1,d=3` specialization gives

`||p_Q||inf
 <=3 e^(1/3) (|det P0| ||S0||_F)^(-1/3)
 =3 e^(1/3) G_{ih;jk}^(-1/6)`.                                (3.1)

Using (2.5),

`boxed: ||p_Q||inf <7.110847 Z^(-1/6).`                         (3.2)

The characteristic function is in `L1`.

If `rank(P0)=1` and the scalar Schur residual in (2.9) has exact rank two, then the scalar-pivot/exact-rank-two grouped theorem gives

`||p_Q||inf <=3 e^(2/3) (p^2 E2(S1))^(-1/6)`,                 (3.3)

and therefore

`boxed: ||p_Q||inf <9.923986 Z^(-1/6).`                         (3.4)

Again `phi_Q in L1` and the density is continuous and vanishes at infinity.

Thus transport failure is not a dead end: after one finite pigeonhole it lands on a second physical anchor, and both lowest-rank algebraic endpoints are already completely paid.

## 4. Sharp-HY D5 applied to the new invertible double-anchor packet

The fixed-source D5 theorem now applies to an actual new inequality, rather than only being listed as an available tool.

Assume branch (A), put

`D0=|det P0|`, `T=||S0||_F^2`, `rho=sr(S0)=T/||S0||op^2`.      (4.1)

When `rho>3`, writing the squared singular values of `S0` as `x_m` gives `x_m<=T/rho`. Newton's identity yields

`E3(S0)=e3(x)
 =(T^3-3T sum x_m^2+2 sum x_m^3)/6
 >=(rho-3)/(6rho) T^3`.                                       (4.2)

Every `5 x 5` minor obtained by adjoining three residual rows/columns to the fixed `2 x 2` anchor contributes to `E5(B)`, so

`E5(B)>=D0^2 E3(S0)
 >=[(rho-3)/(6rho)] G_{ih;jk}^3/D0^4`.                         (4.3)

Insert this into the reviewed sharp-HY D5 estimate (1.1):

`boxed:
 ||p_Q||inf
 <=(5e/sqrt(2))[6rho/(rho-3)]^(1/10)
   D0^(2/5) G_{ih;jk}^(-3/10).
}`                                                              (4.4)

For `rho>=4`,

`||p_Q||inf
 <13.205980 D0^(2/5)G_{ih;jk}^(-3/10)
 <34.263679 D0^(2/5)Z^(-3/10).`                                (4.5)

The last display is not claimed universal because the positive `D0` power still has to be routed against the remaining geometry. Its value is that the high-stable-rank part of the new second-anchor residue is now an explicit D5 Fourier branch; the genuinely unpaid collar is low stable rank or a singular-rank-one anchor with residual rank at least three.

## 5. Source-valid stress witness: singular second anchors really occur

The stronger inference “a positive double-anchor packet forces an invertible `2 x 2` anchor” is false, even inside the exact spectral target. Take

`B0=[[1,0,0],[0,0,1],[0,1,0]]`,
`A0=[[0,B0],[B0^T,0]]`.                                       (5.1)

`B0` is orthogonal, so `A0` has eigenvalues `+1,+1,+1,-1,-1,-1`; this is an exact-target matrix. Its only `3 x 3` determinant has modulus one, hence D' fails maximally and D5 is unavailable because `rank(B0)=3`.

For the first two rows and columns,

`P0=[[1,0],[0,0]]`                                             (5.2)

has rank one while the containing `3 x 3` determinant is nonzero. Choosing the scalar pivot `p=1` leaves

`S1=[[0,1],[1,0]]`, `E2(S1)=1`.                               (5.3)

So the rank-one alternative in Theorem 2.1 is necessary, and (3.3) pays this exact-target witness uniformly for every admissible product input law:

`||p_Q||inf <=3e^(2/3)<5.844`.                                 (5.4)

This is an obstruction to an intermediate invertible-anchor shortcut, not a counterexample to QFORM.

## 6. What changed in the live proof map

Combining fleet03/B02 r30 with the previous incident-(3+2) transport theorem and Theorem 2.1 gives the following physical-coordinate route for any live block with `Z=E3(B)>0` and a fixed disjoint `2 x 2` pivot `H x K`:

1. the sharp-HY D' gate holds on a bank, and (1.2) pays the branch; or
2. r30 gives `J_ij>Z/3`; if either incident avoidance probability is at least `1/4`, the existing transport-L1 theorem applies; or
3. if both avoidance probabilities are below `1/4`, Theorem 2.1 produces a fixed second double-anchor packet `G>Z/24`; its exact-rank-one and singular/exact-rank-two endpoints are paid by (3.2) and (3.4), while its high-stable-rank invertible part has the D5 inequality (4.4).

The remaining case is therefore no longer “diffuse high leverage.” It is the concrete second-anchor collar:

`QFORM-SECONDANCHOR-LOWSTABLERANK-RECEIVER-v1`:

- invertible `P0`, `G=D0^2||S0||_F^2>Z/24`, with `rank(S0)>=2` and low stable rank not already paid by D5; or
- rank-one `P0`, `p^2E2(S1)>Z/24`, with `rank(S1)>=3`;
- plus the earlier literal pivot/outer-anchor overlap case when the fixed original pivot is not disjoint from the r30 anchors.

A valid next mechanism must spend these aggregate packets by grouped hub/star, another exterior-volume transport, or a TRUE symmetric Schur/pair theorem. It may not choose a tiny local minor, delete a small matrix tail on unbounded inputs, or assert independence after a shear.

## 7. Checks and correction boundary

A deterministic regression with seed `20260923` checked (2.8) on 200 random `6 x 6` matrices; maximum relative error was `9.55e-16`. On 100 matrices with the selected `2 x 2` anchor forced to rank one, (2.9) had zero violations; the smallest observed ratio `p^2E2(S1)/G` was `2.54755`. These checks are diagnostic only; the proof above is algebraic/combinatorial.

All live corrections remain respected, including the false pointwise-decay route, loss of independence after rotation/shear, false arbitrary-joint coarea and conditional-cap interfaces, false fixed-cross-minor inference, false local rank-three dichotomy, and the prohibition on treating a small matrix perturbation as a uniformly small random quadratic error.

No exact-target counterexample to the stronger target-wide statement

`integral_R |E exp(it X^T A X)| dt <= C`

was found. That criterion remains `OPEN_NOT_REFUTED`; the unrestricted bounded-density conjecture remains OPEN.
