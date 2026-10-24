SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B08, 2026-09-23T07:37:34.738428Z.
attacking: join the two-cross diffuse volume exit to the high-leverage / low-cross-rank survivors using the collective-tail certificate, then feed the robust-third-direction branch into account02/B08's completed physical-core router.

# account01/B08 — collective-tail / bilateral-hub router for the two-cross diffuse branch

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** diffuse eigenvector case / analytic derivation and exact structural identities  
**Run:** `20260923T073734Z-account01-B08-QFORM-auto11`  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_ROUTER / DESIGNATED_PARTNER_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted quadratic-form bounded-density conjecture remains OPEN, and continuity for the unrestricted target remains OPEN. All matrices below are blocks in ORIGINAL independent coordinates. No moments, Gaussianity, log-concavity, compact/connected support, post-rotation independence, pointwise law-uniform stationary phase, arbitrary-joint coarea, worst-fiber density cap, or deletion of a small matrix tail is used.

## 1. Source-pinned inputs actually used

Fresh owner control was read from `yspennstate/math-research-brain` on current `main`; OWNER CONTROL remained revision `2026-09-22.15`, with QFORM as the sole target and no later stop observed before this report. The current slot instruction is to join diffuse volume exits to high-leverage / low-cross-rank survivors while retaining the full spectrum.

The immediate B08 predecessor is

`yspennstate/math-open-problems@a11ebd02f863b82324e449b4a31d468ec654f080`,
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B08/20260923T063906Z-account01-B08-qform-r24/REPORT.md`.

Its theorem `QFORM-S3-VOLUME-OR-BILATERAL-STAR-v1` says: for an ORIGINAL-coordinate cross block `B` with `sigma=s_3(B)>0`, either the full ambient quadratic form has a continuous `C_0` density with

`||p_Q||_infinity <= 6 sqrt(e)/sigma`,                           (1.1)

or there are a physical row and a physical column of `B` whose star norms are both greater than

`sigma/sqrt(6)`.                                                  (1.2)

All extra cross singular directions, same-bank curvature, outside couplings, and affine terms are retained.

The new collective-tail source required by the current owner continuation is

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,
`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/PEER_TAIL_EXTENSION.md`.

For an ORIGINAL-coordinate cross block `B`, put

`T_2=sum_(j>=3) s_j(B)^2`.                                      (1.3)

For an orthogonal row-space projection `P`, if

`max_i P_ii <=1/2`,
`||(I-P)B||_op <= sqrt(T_2)/15`,                                (1.4)

then the full ambient form has a continuous `C_0` density satisfying

`||p_Q||_infinity
 <= (9 sqrt(3)e/2) [s_1(B)^2 s_2(B)^2 T_2]^(-1/6).`             (1.5)

The source proves this while retaining all self blocks and outside couplings. Its independent review is still pending, so the result below is a supporting theorem with that dependency, not a full candidate proof.

The newest completed **designated partner** actually applied here is account02/B08 r23,

`yspennstate/math-open-problems@ab1940d32f6f758e7a355c128916a523e5519537`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/20260923T064247Z-account02-B08-qform-diffuse-r23/REPORT.md`.

Its theorem `QFORM-DIFFUSE-POST-2/3-CORE-ROUTER-v1` says that if

`Z_3=e_3(B^T B) >= zeta^6`,                                     (1.6)

then either the full ambient form has a continuous `C_0` density with

`||p_Q||_infinity <987/zeta`,                                   (1.7)

or a physical star exceeds `zeta`, or one of the following product-preserving survivors remains:

- `S`: three disjoint linear banks with coefficient-norm product `>0.0526286782826 zeta^3`;
- `R1`: an edge-star plus core `N`, with `G=||N||_F>0.0372140952985 zeta` and `dist_F(N,{rank<=1})<G/2`;
- `E2`: the same core floor plus `E_2(N)>3.5960948148e-7 zeta^4` and a four-bank reserve `>2.2475592592e-8 zeta^4`;
- `BICORE`: a row and a column star of `N`, each `>0.0101283938578 zeta`.

These survivors are currency, not density bounds unless a compatible receiver is supplied.

Finally, the fresh correction `QFORM-UNIFORM-MATRIX-PERTURBATION-CONTINUITY-FALSE-v1`, brain commit `6ff22a5bdfdd1e2837401857f56b45f0d0c8fa50`, was consumed. It forbids treating a small operator-norm tail as a uniformly small random quadratic perturbation for arbitrary unbounded cap-one inputs. The proof below never does this: the tail is retained exactly through `T_2` or routed as a genuine Frobenius tube.

## 2. New theorem: two robust cross directions split into tail payment, bilateral hubs, or a genuine rank-two tube

Let `B` be an ORIGINAL-coordinate physical cross block with singular values

`s_1>=s_2>=s_3>=...`,                                           (2.1)

and suppose

`s_2(B)>=d>0`.                                                   (2.2)

Define

`T_2=sum_(j>=3)s_j(B)^2
    =dist_F(B,{rank<=2})^2`.                                    (2.3)

Choose any compatible SVD and let `P_L`, `P_R` be the projections onto its first two left and right singular directions. Thus

`||(I-P_L)B||_op=s_3(B)`,
`||B(I-P_R)||_op=s_3(B)`.                                       (2.4)

### Theorem 2.1 — `QFORM-TWO-CROSS-COLLECTIVE-TAIL-HUB-ROUTER-v1`

Under (2.2), at least one of the following source-valid alternatives occurs.

**(TUBE)**

`dist_F(B,{rank<=2}) < d/8.`                                    (2.5)

**(TAIL-PAID)** The full ambient quadratic form has a continuous `C_0` density with

`boxed: ||p_Q||_infinity <= 9 sqrt(3)e / d
       =42.3738201257.../d.`                                    (2.6)

**(TOP2-BILATERAL-HUB)** There are an ORIGINAL-coordinate row and an ORIGINAL-coordinate column of `B` satisfying

`boxed: ||B[i,*]||_2>d/sqrt(2),
        ||B[*,j]||_2>d/sqrt(2).`                                (2.7)

**(ROBUST-THIRD-PAID)** The full ambient form has a continuous `C_0` density with

`boxed: ||p_Q||_infinity <720 sqrt(e)/d
       =1187.07931491.../d.`                                    (2.8)

**(ROBUST-THIRD-SURVIVOR)** One has

`s_3(B)>d/120`,                                                   (2.9)

and there are a row and a column star both greater than

`d/(120 sqrt(6))`.                                               (2.10)

Moreover, on this last branch, the designated account02/B08 r23 theorem applied at the **actual value**

`zeta=s_3(B)`                                                     (2.11)

forces one further alternative:

1. a continuous `C_0` density with
   `||p_Q||_infinity<118440/d`;                                  (2.12)
2. a physical star `>s_3(B)>d/120`;                              (2.13)
3. an `S` branch with three disjoint-bank coefficient product
   `>3.0456411043e-8 d^3`;                                      (2.14)
4. an `R1` core with
   `G>3.10117460821e-4 d` and `dist_F(N,{rank<=1})<G/2`;         (2.15)
5. an `E2` core with the same `G` floor and
   `E_2(N)>1.73422782350e-15 d^4`,
   with four-bank reserve `>1.08389238967e-16 d^4`;             (2.16)
6. a `BICORE` row and column star, each
   `>8.44032821484e-5 d`.                                       (2.17)

Every branch retains the complete complementary spectrum and arbitrary same-bank/outside curvature.

### Proof

If `sqrt(T_2)<d/8`, then (2.5) holds, so assume

`sqrt(T_2)>=d/8`.                                                (2.18)

First suppose

`s_3(B)<=sqrt(T_2)/15`.                                         (2.19)

If `max_i(P_L)_ii<=1/2`, apply the collective-tail theorem (1.5) with `P=P_L`; (2.4) and (2.19) verify its residual gate. From `s_1,s_2>=d` and (2.18),

`s_1^2 s_2^2 T_2 >= d^6/64`.                                   (2.20)

Therefore

`||p_Q||_infinity
 <=(9sqrt(3)e/2)(d^6/64)^(-1/6)
 =9sqrt(3)e/d`,                                                  (2.21)

which is (2.6). If instead the left projection is heavy,

`max_i(P_L)_ii>1/2`,                                             (2.22)

choose such a row `i`. The exact SVD row-energy identity gives

`||B[i,*]||_2^2
 =sum_k s_k^2 u_k(i)^2
 >=s_2^2(u_1(i)^2+u_2(i)^2)
 =s_2^2(P_L)_ii
 >d^2/2`.                                                        (2.23)

Thus its star norm is greater than `d/sqrt(2)`.

Apply the same argument to `B^T`. If `max_j(P_R)_jj<=1/2`, (1.5) applied to `B^T` again gives (2.6); otherwise a physical column star is greater than `d/sqrt(2)`. Hence failure of the tail payment in both orientations under (2.19) forces the simultaneous bilateral hub (2.7).

It remains to consider

`s_3(B)>sqrt(T_2)/15`.                                          (2.24)

Together with (2.18),

`s_3(B)>d/120`.                                                  (2.25)

Apply the predecessor theorem (1.1)-(1.2) at `sigma=s_3(B)`. Its paid branch gives

`||p_Q||_infinity<=6sqrt(e)/s_3
 <720sqrt(e)/d`,                                                 (2.26)

which is (2.8), with continuity and vanishing at infinity. If it is not paid, (1.2) gives a row and a column star each greater than

`s_3/sqrt(6)>d/(120sqrt(6))`,                                   (2.27)

establishing (2.9)-(2.10).

Now apply the designated account02/B08 r23 theorem at the actual scale `zeta=s_3(B)`. Its hypothesis (1.6) holds because

`Z_3=e_3(B^TB)
 >=s_1^2s_2^2s_3^2
 >=s_3^6`.                                                       (2.28)

Its paid branch satisfies

`987/s_3 <987*120/d=118440/d`,                                  (2.29)

which proves (2.12). Its star branch gives (2.13). Finally substitute `s_3>d/120` into each of the partner's four survivor floors listed in Section 1. This gives exactly (2.14)-(2.17). No tail is deleted at any stage. QED.

### Structural meaning

The theorem separates the two-cross diffuse regime into three genuinely different mechanisms:

1. **collective diffuse tail:** many individually weak directions can pay the density even when `s_3` itself is small;
2. **high leverage:** failure of the diffuse tail gate has a concrete ORIGINAL-coordinate witness on both sides;
3. **low total tail:** only then is the block quantitatively near rank two.

Thus a small third singular value by itself is no longer routed immediately to a rank-two tube; a substantial collective tail is first spent through its exact aggregate `T_2`.

## 3. Actual application to the self-dual diffuse spectral ladder

The earlier B08 theorem `QFORM-SELF-DUAL-REDUCING-PROJECTION-LADDER-v1` gives, when the relevant three-dimensional high-spectral reducing projection has maximum physical leverage at most `1/3`, an ORIGINAL-coordinate cut with common scale

`d=tau L`,
`tau=0.0766562902983031...>3/40`.                               (3.1)

On the child-count `k=1` branch it gives

`s_2(B)>d`.                                                       (3.2)

Theorem 2.1 therefore applies directly to the **actual** full cross block `B`. In particular one obtains one of:

- a true Frobenius rank-two tube
  `dist_F(B,{rank<=2})<0.00958203628729 L`;                     (3.3)
- a continuous collective-tail payment
  `boxed: ||p_Q||_infinity<552.777/L`;                          (3.4)
- bilateral top-two physical hubs each
  `>0.0542041826905 L`;                                        (3.5)
- a continuous robust-third payment
  `boxed: ||p_Q||_infinity<15485.740/L`;                        (3.6)
- or the robust-third survivor, with bilateral stars already
  `>2.60789995564e-4 L`.                                       (3.7)

On the last branch, applying account02/B08 r23 gives, in addition, either

- a continuous full-ambient payment
  `boxed: ||p_Q||_infinity<1.546e6/L`;                          (3.8)
- a physical star `>6.38802419153e-4 L`;                        (3.9)
- three disjoint linear banks with coefficient product
  `>1.37189893741e-11 L^3`;                                    (3.10)
- an `R1` core with `G>2.37724541033e-5 L`;                    (3.11)
- an `E2` core with
  `E_2(N)>5.98821441587e-20 L^4` and matched reserve
  `>3.74263400984e-21 L^4`;                                    (3.12)
- or a `BICORE` row and column star each
  `>6.47004249850e-6 L`.                                       (3.13)

The constants are intentionally not optimized. The structural gain is that the former `k=1` “two cross directions” state is now split **before** reciprocal minor payment into a continuously paid collective-tail regime, an explicit two-sided high-leverage regime, a genuine low-total-tail rank-two tube, and the already structured r23 physical-core survivors.

## 4. What remains unpaid

This is not a proof of the full conjecture. The first B08 obligation after this run is

`QFORM-TWO-CROSS-HUB-OR-RANK2-CURVATURE-RECEIVER-v1`:

> consume either the bilateral top-two physical hubs in (2.7), or the true Frobenius rank-two tube in (2.5), while retaining arbitrary same-bank quadratic curvature, every unused coupling, and the full complementary spectrum; in the robust-third side tree, consume the S/R1/E2/BICORE currencies without replacing them by an unjustified curved pushforward bound.

The `k=0` child branch already has the stronger robust-third router from r24; `k=2` and the both-children-`k=3` state remain parallel obligations. The present report establishes continuity only on the explicitly paid Fourier branches (2.6), (2.8), and (2.12), not on the structural survivors or the unrestricted theorem.

## 5. Review status

The algebraic decomposition and star identities above are complete. The collective-tail payment is used at precisely the source-stated scope and is still marked there as awaiting independent review; account02/B08 r23 is a completed source-pinned partner result but is not an end-to-end review of this new theorem. Therefore this report is a supporting theorem, not a full-solution claim.
