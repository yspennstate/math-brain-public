SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B20, 2026-09-23T04:46:30Z.
attacking: the r25 adjusted-diagonal collar debt by a rank-five finite-exception compiler, then the designated account04/B20 conditioned-whitened theorem, with every remaining failure converted to a quantitative original-coordinate anchored compound packet.

# account03/B20 r26 — adjusted diagonal collapses to diffuse payment or anchored compound

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Proof closure and keeper  
**Classification:** `ESSENTIAL_STEP_APPLIED / FIRST REMAINING COLLAR IMPLICATION ROUTED / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository access is not native receiver-memory ingestion.  
**Continuity:** proved only in the conditioned-whitened paid subbranch below; not proved for the unrestricted target.

## 1. Source boundary and exact debt

Fresh source control at start is `yspennstate/math-research-brain@fe7ef8cf19c40214a6fedc5a4f6b5102e2a59b71`, OWNER CONTROL revision `2026-09-22.15`, QFORM only.

The immediate source is account03/B20 r25, canonical

`yspennstate/math-open-problems@cc4ea683eab18deb0c991021278760487f176b0a`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B20/20260923T041231Z-account03-B20-QFORM-r25/REPORT.md`.

In its nondominant-star exact-rank-three collar, after an original physical hub is fixed one has

`A = L + D_* + E_*`,                                                (1.1)

where

- `rank(L)<=2`;
- `D_*` is diagonal in the ORIGINAL physical coordinates;
- `E_*` has zero diagonal and is the aligned off-diagonal error;
- `rank(A)=3`, and the three nonzero eigenvalues of `A` have absolute value at least one.

The r25 compiler proves that either

`||D_*||_op > 1/2`                                                  (1.2)

or a fixed aggregate two-gradient packet is present. Its first unpaid implication explicitly includes paying/routing (1.2). This report attacks exactly (1.2).

The designated partner actually used below is account04/B20 r2,

`yspennstate/math-open-problems@94bf446b8547b1124a37033e940ef594c460b64f`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B20/20260922T141640Z-account04-B20-QFORM-r2/REPORT.md`.

It proves: for `A=U Lambda U^T`, after conditioning an ORIGINAL coordinate set `F`, put

`S=I-U_F^T U_F`, `delta=lambda_min(S)`.

If `delta>0` and every remaining original row satisfies

`u_k^T S^(-1)u_k <= 1/32`,                                        (1.3)

then the full law has a **continuous** density

`||p_Q||_infinity < 27/delta`.                                     (1.4)

The other completed theorem used is account01/B20's anchored-wedge identity,

`yspennstate/math-open-problems@f64266f079e502403ff19ff5ca9739a79c65ebcc`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B20/20260923T031910Z-account01-B20-QFORM-auto11/ADDENDUM_ANCHORED_WEDGE.md`.

For an exact-rank-three matrix with spectral floor `delta_0`, every physical row `r_j` satisfies

`W_j:=sum_(k!=j)||r_j wedge r_k||^2 >= 2 delta_0^2 ||r_j||^2`,       (1.5)

and the exact original-coordinate channel decomposition is

`W_j=P_j+M_j+D_j`,                                                   (1.6)

with principal, one-overlap, and fully-disjoint compound currencies, all nonnegative.

No random coordinates are rotated in this report.

## 2. Rank-five finite-exception compiler

Assume the adjusted-diagonal branch (1.2). First split according to the size of the aligned error.

If

`||E_*||_op >= 1/2`,                                                (2.1)

then r25's proof already gives its aggregate two-gradient alternative, because

`1/4 <= ||E_*||_op^2 <= ||E_*||_F^2`

and the stable-alignment inequality converts this to the fixed total `Delta_j^2` lower bound. Thus the only genuinely new part of (1.2) is

`||E_*||_op < 1/2`.                                                 (2.2)

Put

`B_*=D_*+E_*=A-L`.                                                  (2.3)

Since `rank(A)=3` and `rank(L)<=2`,

`rank(B_*) <= 5`.                                                   (2.4)

Define the exceptional set of physical coordinates

`F={j: |(D_*)_jj|>1/2}`.                                           (2.5)

Because (1.2) is strict, `F` is nonempty.

### Lemma 2.1 — at most five adjusted-diagonal exceptions

Under (2.2),

`boxed: 1 <= |F| <= 5.`                                            (2.6)

### Proof

Let `s_k(T)` denote singular values in decreasing order. Since `rank(B_*)<=5`,

`s_6(B_*)=0`.

The singular-value perturbation inequality gives

`s_6(D_*) <= s_6(B_*)+||E_*||_op <1/2`.                            (2.7)

But the singular values of a diagonal matrix are the decreasing rearrangement of the absolute diagonal entries. Six entries of modulus `>1/2` would force `s_6(D_*)>1/2`, contradicting (2.7). QED.

This is dimension-free and uses only the exact rank-three collar and the r25 rank-two aligned model.

## 3. Apply account04/B20 to the entire exceptional set

Write the exact-rank-three spectral representation

`A=U Lambda U^T`, `U^T U=I_3`,                                    (3.1)

where all three eigenvalues of `Lambda` have modulus at least one. Let `u_j^T` be physical row `j` of `U` and `c_j=||u_j||^2`.

Condition on the ORIGINAL coordinates indexed by the finite set `F`. Put

`S=I-U_F^T U_F`.                                                    (3.2)

Suppose first that

`||U_F^T U_F||_op <= 3/4`.                                         (3.3)

Then

`delta=lambda_min(S)>=1/4`.                                        (3.4)

If in addition

`max_(k notin F) c_k <= 1/128`,                                    (3.5)

then for every residual physical row

`u_k^T S^(-1)u_k <= c_k/delta <= (1/128)/(1/4)=1/32`.              (3.6)

This is exactly the designated partner hypothesis (1.3), not an enlarged surrogate. Therefore

`boxed: ||p_Q||_infinity < 27/delta <=108`,                        (3.7)

and the density is continuous.

This is the required equation-level application of account04/B20 to the new finite-exception set produced by Lemma 2.1.

## 4. Every failure of the partner gate creates a strong physical compound resource

We now show that failure of (3.3) or (3.5) does not return to an abstract adjusted-diagonal obstruction.

### 4.1 Residual-leverage failure

Assume (3.3) but (3.5) fails. Then some ORIGINAL residual coordinate `j notin F` has

`c_j>1/128`.                                                        (4.1)

Because `|lambda_l|>=1`, its actual physical matrix row `r_j=e_j^T A` satisfies

`||r_j||^2=(A^2)_jj=u_j^T Lambda^2 u_j >= c_j >1/128`.             (4.2)

If `|A_jj|>=1/32`, the completed exact-rank-three physical-pivot theorem used in r25 gives

`||p_Q||_infinity
 <=128 [c_j |A_jj| |det Lambda|]^(-1/4)
 <128 (4096)^(1/4)=1024`.                                          (4.3)

So an unpaid state must have `|A_jj|<1/32`; in particular its physical star obeys

`||A[j,-j]||^2
 =||r_j||^2-A_jj^2
 >1/128-1/1024=7/1024`.                                            (4.4)

More importantly, apply the exact anchored-wedge inequality (1.5) with spectral floor `delta_0=1`:

`W_j >=2||r_j||^2 >1/64`.                                         (4.5)

Using (1.6),

`boxed: max(P_j,M_j,D_j)>1/192`.                                  (4.6)

Thus residual nondiffuseness becomes a fixed original-coordinate anchored compound packet.

### 4.2 Exceptional-set spectral concentration

Assume instead that (3.3) fails:

`||U_F^T U_F||_op>3/4`.                                            (4.7)

Choose a unit spectral vector `v` realizing the Rayleigh quotient. Then

`sum_(j in F) <u_j,v>^2 >3/4`.                                    (4.8)

Lemma 2.1 gives `|F|<=5`, hence for some `j in F`,

`<u_j,v>^2 > (3/4)/5=3/20`.                                       (4.9)

Therefore

`c_j=||u_j||^2>3/20`                                               (4.10)

at a physical coordinate distinct from the small collar hub (the hub diagonal in r25 has modulus `<1/64`, so it cannot lie in `F`). Consequently

`||r_j||^2>=c_j>3/20`,                                             (4.11)

and (1.5)-(1.6) imply the much stronger packet

`W_j>3/10`,

`boxed: max(P_j,M_j,D_j)>1/10`.                                   (4.12)

Again, if `|A_jj|>=1/32`, the exact-rank-three physical-pivot theorem already pays the branch by the finite bound (4.3), now with still more slack. If not, (4.12) is a very strong physical compound resource.

## 5. New closure theorem for the r25 adjusted-diagonal alternative

Collecting Sections 2--4 gives the main result of this run.

### Theorem 5.1 — `QFORM-COLLAR-ADJUSTED-DIAGONAL-TO-COMPOUND-v1`

In the nondominant-star exact-rank-three collar of account03/B20 r25, suppose

`||D_*||_op>1/2`.

Then at least one of the following source-valid alternatives holds:

1. `||E_*||_op>=1/2`, hence the already-recorded r25 aggregate two-gradient packet is present;
2. the full law has a **continuous** density with `||p_Q||_infinity<108` by conditioning a nonempty set `F` of at most five ORIGINAL coordinates and applying account04/B20 r2;
3. a physical scalar-pivot branch is paid with `||p_Q||_infinity<1024`;
4. there is an ORIGINAL physical anchor `j` with

   `max(P_j,M_j,D_j)>1/192`.                                       (5.1)

Moreover, if the failure comes from spectral concentration on the finite exceptional set, the stronger bound

`max(P_j,M_j,D_j)>1/10`                                            (5.2)

holds.

No individual tiny physical minor is selected from diffuse compound mass. The output is either an actual density payment or an aggregate original-coordinate packet already recognized by the fleet's current O3 anchored-compound frontier.

### Consequence for the proof tree

The standalone adjusted-diagonal debt in r25 is removed. It need no longer appear as a primitive unresolved geometry. Its only unpaid descendants are now:

- the pre-existing r25 aggregate two-gradient / low-cross-rank-localized branch; and
- `QFORM-O3-ANCHORED-COMPOUND-PAYMENT-v1`, now reached with the much larger currency `>1/192` (or `>1/10` on the finite-set concentration subbranch).

This is a strict narrowing of `QFORM-COLLAR-ALIGNED-DIAGONAL-OR-LOWRANK-LOCALIZED-PAYMENT-v1`.

## 6. Scope audit

The proof conditions only sets of ORIGINAL independent coordinates. Spectral coordinates are used only in deterministic matrix inequalities. It does not use:

- pointwise law-uniform van der Corput decay;
- independence after rotation;
- arbitrary-joint three-dimensional coarea;
- normalized conditional projection-density caps;
- worst-fiber suprema;
- one-good-minor extraction from aggregate Pluecker mass.

The finite-exception step is pure rank/singular-value algebra. The partner theorem is applied exactly through its whitened leverage condition. The anchored compound output remains aggregate.

## 7. Remaining full-target debt

The unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. The owner-requested global continuity statement also remains open.

After this run, the first collar-level analytic debt is no longer `||D_*||>1/2` itself. It is the payment of the resulting fixed-strength anchored compound packet, together with the separate r25 low-cross-rank/localized aggregate-cut residue. The most promising next mechanism is to spend `P_j,M_j,D_j` before taking reciprocal local determinants, using the existing two-gradient `2/3` receiver on concentrated disjoint mass and a bank/ridge transducer on diffuse mass.
