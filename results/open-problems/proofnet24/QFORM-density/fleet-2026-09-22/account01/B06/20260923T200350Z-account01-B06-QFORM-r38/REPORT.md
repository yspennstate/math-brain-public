SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B06, 2026-09-23T20:03:50Z.
attacking: remove the old shared-index E2 row-marginal obstruction by splicing the newest account02/B06 half-Riesz theorem into the physical square-pivot argument; then identify the exact residual diagonal shared-index geometry.

# account01/B06 r38 — row-gate-free shared-index curved-pivot receiver

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T200350Z-account01-B06-QFORM-r38`  
Role: curved fiber integration  
Status: **PROVED SUPPORTING DENSITY THEOREM / DESIGNATED PARTNER APPLIED / OLD ROW-GATE OBSTRUCTION CLOSED / NEW EXACT DIAGONAL-PACKET NORMAL FORM / FULL TARGET OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains OPEN. This report proves a dimension-free density branch in the live high-collision shared-index chamber, and removes one explicit obstruction left by r32. It does not add moments, compact support, iid structure, log-concavity, connected support, Gaussianity, or independence after rotation. Continuity is not claimed for the new square-peel/half-Riesz branch.

## 1. Fresh source boundary


Corrections retained include: no law-uniform pointwise quadratic-phase decay; no post-rotation product independence; no arbitrary-joint rank-three coarea cap; no positive moment of worst conditional projection caps; no dimension-free unrestricted spectral-fiber supremum; and no inference of one uniformly good physical minor from aggregate compound mass.

The own source being sharpened is r32:

`yspennstate/math-open-problems@c2ce876df8b5483a00802170001d4144bb4cdbfa`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B06/20260923T124109Z-account01-B06-QFORM-r32/PIVOT_RECEIVER.md`.

The designated partner result actually applied is the newest account02/B06 theorem

`QFORM-E2-HALFRIESZ-ROW-GATE-FREE-v1`,

canonical commit

`yspennstate/math-open-problems@b38a9627f059b13d532f5c208c30579ec2d2d362`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260923T192839Z-auto11/REPORT.md`.

It states: if `S` is any quadratic-affine polynomial in independent ORIGINAL coordinates of one-dimensional density at most one, and a literal disjoint physical cross block `M` has

`Z_2=e_2(M^T M)=sum_(|R|=|T|=2) det(M[R,T])^2>0`,

then, with no natural volume-row-marginal assumption,

`boxed: H_(1/2)(S):=sup_t E|S-t|^(-1/2)
        <= 8 e^(1/4) Z_2^(-1/8).`                                  (1.1)

The theorem retains arbitrary same-bank quadratic curvature, arbitrary additional cross singular directions, affine terms, and conditioned outside coordinates. It is a fractional-potential result, not by itself an L-infinity theorem.

## 2. Physical square peel

Let `i` be an ORIGINAL physical coordinate with scalar pivot

`c=A_ii !=0`.                                                       (2.1)

Complete the square only in this genuine independent scalar. After conditioning nothing else, one can write

`Q=c(X_i+Psi(X_-i))^2+S(X_-i)`,                                    (2.2)

where `S` is the exact Schur-complement quadratic-affine form in the remaining original product coordinates.

For a cap-one scalar density, the conditional density of `c(X_i+psi)^2` is bounded by

`|c|^(-1/2)|u|^(-1/2)`                                             (2.3)

on its proper half-line. Therefore, uniformly in the shift `Psi`,

`boxed: ||p_Q||_infinity <= |c|^(-1/2) H_(1/2)(S).`                (2.4)

This is the curved square kernel retained exactly; no fiber maximum is taken.

## 3. Shared-index bordered packet becomes literal E2 after the pivot

Return to the r32 zero-anchor two-hub chamber and its bordered third minors

`D_(R,T)=det [[0,a_T^T],[b_R,C_(R,T)]],    |R|=|T|=2.`             (3.1)

For a fixed background pivot `i`, define the off-diagonal double-incidence mass

`S_i^off = sum_(j!=k; j,k!=i) D_({i,j},{i,k})^2.`                  (3.2)

R32 proved the exact shared-index Schur-minor identity

`D_({i,j},{i,k})
 = c det A^(i)[{X,j},{Y,k}]`                                       (3.3)

up to the fixed row/column ordering sign, where `A^(i)` is the Schur complement after pivoting `i`.

Now randomly partition every remaining background coordinate into `L union R`, each with probability one half, keep hub `X` on the left and hub `Y` on the right, and let

`M_cut=A^(i)[{X} union L,{Y} union R]`.                             (3.4)

For each ordered `j!=k`, the minor in (3.3) occurs in `E_2(M_cut)` when `j in L` and `k in R`, probability `1/4`. Hence

`E_cut E_2(M_cut) >= S_i^off/(4c^2)`.                              (3.5)

Therefore some actual ORIGINAL-coordinate disjoint cut satisfies

`boxed: Z_2:=E_2(M_cut) >= S_i^off/(4c^2).`                        (3.6)

The important point is that the full packet is aggregated before inversion or reciprocal payment.

## 4. Main theorem: the r32 E2 row gate disappears

### Theorem 4.1 — `QFORM-SHARED-INDEX-PIVOT-E2-ROW-GATE-FREE-v1`

In the setup of Sections 2-3, if `c!=0` and `S_i^off>0`, then

`boxed:
 ||p_Q||_infinity
 <= 8(2e)^(1/4) |c|^(-1/4) (S_i^off)^(-1/8).`                     (4.1)

Numerically,

`8(2e)^(1/4)=12.215777290955...`.                                  (4.2)

There is **no** natural E2 row-marginal hypothesis in (4.1).

### Proof

Take the physical cut from (3.6). Apply the designated partner theorem (1.1) to the exact Schur form `S` and this literal disjoint cross block. It gives

`H_(1/2)(S)
 <=8e^(1/4) Z_2^(-1/8)
 <=8e^(1/4) [S_i^off/(4c^2)]^(-1/8).`                              (4.3)

Insert (4.3) into the exact physical square peel (2.4):

`||p_Q||_infinity
 <=|c|^(-1/2) 8e^(1/4)
    (S_i^off)^(-1/8) 4^(1/8)|c|^(1/4)
 =8(2e)^(1/4)|c|^(-1/4)(S_i^off)^(-1/8).`                          (4.4)

QED.

This closes obstruction 4 in r32 `PIVOT_RECEIVER.md`: a cut carrying the packet may have a heavy natural rank-two volume row, but the fresh account02/B06 theorem handles that heavy-row complement internally.

## 5. Scale-invariant target corollary

Let `s=s_3(A)>0`. If

`|c|>=kappa s`,
`S_i^off>=theta s^6`,                                               (5.1)

then Theorem 4.1 gives

`boxed:
 ||p_Q||_infinity
 <=8(2e)^(1/4) kappa^(-1/4) theta^(-1/8) s^(-1).`                 (5.2)

The scaling is exact: `c` has one quadratic scale and `S_i^off` is a sum of squares of third-order minors.

## 6. Actual live r30/r32 branch closed with an explicit constant

Inside the r30/r32 high-collision, low-tail transverse-curvature chamber, r32 proves that one physical coordinate `i` carries

`W_i^L >= (81/65536) W`,                                          (6.1)

while the preceding transverse branch has

`W > s^6/128`.                                                      (6.2)

Suppose the same actual coordinate also satisfies the concrete subbranch

`S_i^off >= (1/2) W_i^L`,
`|c| >= s/16`.                                                      (6.3)

Then

`S_i^off > (1/2)(81/65536)(s^6/128)
          =81 s^6/2^24.`                                           (6.4)

Applying (4.1),

`boxed:
 ||p_Q||_infinity
 < 8(2e)^(1/4) (1/16)^(-1/4)(81/2^24)^(-1/8) s^(-1)
 <112.845/s.`                                                       (6.5)

Thus this entire target-scale off-diagonal shared-index branch is now paid independently of how concentrated the induced E2 volume sampling law is.

## 7. Exact normal form for the remaining diagonal shared-index packet

The only packet-level failure of (6.3), once a usable pivot `c` exists, is that much of `W_i^L` is concentrated on the terms

`D_({i,j},{i,j})`.                                                   (7.1)

There is a useful exact algebraic normal form for this residual.

After pivoting `i`, write the two hub coordinates as a two-vector and let the hub-hub Schur block be

`H_0=-(1/c) p p^T`,                                                  (7.2)

where `p=(a_i,b_i)^T`. Let `g_j` be the two-vector of hub-to-`j` couplings in the Schur complement and let `d_j` be its physical `j,j` entry. Define the symmetric two-by-two cofactor matrix

`K_j=d_j H_0-g_j g_j^T`.                                            (7.3)

Then

`delta_j:=D_({i,j},{i,j})/c`                                       (7.4)

is, up to the fixed cofactor sign, the off-diagonal entry of `K_j`. Consequently

`||K_j||_F^2 >=2 delta_j^2`.                                        (7.5)

For `p!=0`, make a deterministic orthogonal change of basis **only to evaluate this matrix identity**, sending `p/||p||` to the first hub axis. No probabilistic independence is asserted after this rotation. Put

`rho=||p||^2/c`,
`O g_j=(m_j,n_j)^T`.                                                 (7.6)

Then

`O K_j O^T
 =-[ [rho d_j+m_j^2, m_j n_j],
      [m_j n_j,         n_j^2] ]`,                                 (7.7)

and therefore

`boxed:
 sum_j[(rho d_j+m_j^2)^2+2m_j^2n_j^2+n_j^4]
 >=2 sum_j delta_j^2.`                                              (7.8)

In particular at least one of the three aggregate currencies obeys

`sum_j (rho d_j+m_j^2)^2 >= (1/2)sum_j delta_j^2`,                 (7.9a)

or

`sum_j m_j^2n_j^2 >= (1/2)sum_j delta_j^2`,                        (7.9b)

or

`sum_j n_j^4 >= (1/2)sum_j delta_j^2`.                             (7.9c)

The proof of the last assertion is immediate: if all three were strictly below half the diagonal-packet mass, then the left side of (7.8), with weights `1,2,1`, would be strictly below twice that mass.

This is a deterministic structural reduction, not a density theorem. It shows that the unpaid diagonal-incidence state has only three exact mechanisms: aggregate physical-pair determinant currency, same-coordinate product-star currency, or a transverse fourth-power star. It prevents the residual from being described merely as “shared indices collide.”

If `p=0`, then `H_0=0` and `K_j=-g_jg_j^T`; the same statement follows directly after choosing any orthonormal hub basis, with `rho=0`.

## 8. What remains open after r38

The old r32 row-marginal obstruction is gone. The first local unpaid implication in this chamber is now

`QFORM-SHARED-INDEX-DIAGONAL-PACKET-OR-SMALL-PIVOT-v1`:

> In the target-scale high-collision packet, if the selected physical pivot is small or if the diagonal shared-index mass dominates `W_i^L`, spend one of the exact aggregate currencies (7.9a)-(7.9c) through a product-preserving two-pivot/grouped-hub/curved receiver, without selecting one tiny minor and without conditioning on rotated hub coordinates.

The separate r36 small-nonzero-beta overlapping curved-section gap also remains open; this run deliberately changed mechanism rather than repeating that same interface. The new account02/B06 theorem made the older shared-index obstruction immediately actionable.

## 9. Quantifiers and regularity

Every probability step in Theorem 4.1 uses original-coordinate independence only. Deterministic rotations in Section 7 are used solely to prove matrix identities and do not create probabilistic independence. The full arbitrary-dimensional conjecture remains **OPEN**, no valid target counterexample is produced, and global continuity remains **OPEN**. The new branch proves essential boundedness only.
