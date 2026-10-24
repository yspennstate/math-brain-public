SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B19, 2026-09-23T17:00:40.092131Z.
attacking: QFORM-2x2x2-PRODUCT-TRIANGLE-OR-HEAVY-ANCHOR-PAYMENT-v1 — force the two rank-two legs of the surviving three-bank triangle onto one common two-dimensional K-plane, paying transverse mismatch by the completed physical D3 theorem, then put the exact common-plane cycle into a canonical algebraic normal form.

# account03/B19 — common-plane compiler and exact 2x2x2 cycle normal form

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Universal proof assembly / quantitative inequalities  
Outcome: **NEW TARGET-LEVEL STRUCTURAL COMPILER + NEW EXACT CYCLE IDENTITY / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**  
Continuity: proved on the new D3-paid branch only; not asserted on the surviving common-plane cycle or the full target.

## 1. Fresh controls and premises

The fresh control branch was re-resolved immediately before publication at

`yspennstate/math-research-brain@5f2ff5c256f100ecd0291fcdbd84fc1f52b2be39`.

`AGENTS.md` still names `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`; OWNER CONTROL remains revision `2026-09-22.15`, QFORM is the sole research target, and no later stop/reassignment was present. The live `CORRECTION_INBOX.json` was reread. In particular this proof does **not** use post-rotation independence, arbitrary-joint coarea, conditional-density caps after sum/difference transformations, pointwise quadratic-phase decay, a uniformly good physical minor, moment bounds, or deletion of a small matrix coefficient as a small random perturbation.

The immediate B19 premise is the completed preceding report, read from

`yspennstate/math-open-problems@7ec58359c003dec92e28f330eef36423cd7fea8c`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260923T160411Z-account03-B19-QFORM-r37/REPORT.md`.

Its strong aligned STAR branch produces disjoint ORIGINAL-coordinate banks `D_1,D_2,K` and matrices

`C=A[D_1,D_2]`, `N_1=A[D_1,K]`, `N_2=A[D_2,K]`,

with

`||C||_F^2 >= F`,
`F=0.4537176735697731005/8 >0.0567147091962`,                    (1.1)

and

`s_1(N_r)s_2(N_r) >= Delta`, `r=1,2`,                           (1.2)

where, at the live constants

`tau=2^-20`,
`rho_* =63(1-tau)^2/16384
       =0.003845207509588222...`,
`Delta=(3/8)rho_*=0.0014419528160955833...`.                     (1.3)

More is available than (1.2). The balanced-cut proof is performed on the top-two left singular frame of the original `J-K` bicore. If `x_2=s_2(N)^2`, then

`x_2 > x2_* := (64/259)rho_*
              =0.0009501671066163947...`,                       (1.4)

and the two cut Gram matrices have minimum eigenvalue at least `3/8`. Restoring the orthogonal SVD tail is positive-semidefinite in the relevant Gram matrix. Consequently

`boxed: s_2(N_r)^2 >= sigma_*^2 :=(3/8)x2_*
      =0.000356312664981148..., r=1,2.}`                         (1.5)

The same predecessor proves that, unless a D3 packet is already visible, the self edge is confined to the top-two left planes `P_1,P_2` of `N_1,N_2`:

`||P_1 C P_2||_F^2 >= (9/16)F`.                                 (1.6)

The completed physical D3 theorem used below is the same source-pinned theorem already used in the predecessor: for an ORIGINAL-coordinate cross block `M`, with

`Z_3=e_3(MM^T)`,

if every natural row three-volume inclusion marginal is at most `1/2`, then the full ambient law has a continuous `C_0` density and

`||p_Q||_infinity <= 6 sqrt(e) Z_3^(-1/6)`.                     (1.7)

All same-side quadratic terms, affine terms and outside couplings are retained by that theorem. A failed marginal gate is recorded as a physical row anchor, not silently discarded.

The newest interactive projected-crossing theorem was also read at

`yspennstate/math-open-problems@4f92aeb74083c6f95cb314a11fed1b812eacef9a`,

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

Its `k+ell>2` grouped-hub estimate pays a transverse projected crossing but explicitly leaves the aligned/small-projected-crossing endpoint. The theorem below isolates precisely that endpoint rather than pretending its `Z_ell` gate is automatic.

## 2. The missing right-plane issue

The r37 finite-plane statement only aligned `C` with the two **left** top singular planes of the `D_r-K` legs. A genuine finite `2+2+2` receiver also needs both bicore legs to use one common two-dimensional subspace on the `K` side. This was not automatic: the top-two right singular planes of `N_1` and `N_2` could a priori be different.

Let `Q_r` denote the orthogonal projector onto the top-two **right** singular plane of `N_r`, and define the principal-angle defect

`delta_K := tr(Q_2(I-Q_1))
          = sin^2(theta_1)+sin^2(theta_2)`.                      (2.1)

Thus `delta_K=0` exactly when the two right planes coincide.

Form the literal physical cross block, oriented with rows on `K`,

`M_K := [N_1^T, N_2^T]`,                                       (2.2)

and put

`Z_K := e_3(M_K M_K^T)`.                                        (2.3)

No grouped or rotated random coordinates enter (2.2): it is an actual submatrix of the original coefficient matrix with columns in the disjoint physical banks `D_1 union D_2`.

## 3. New theorem: right-plane mismatch injects physical third volume

### Theorem 3.1 — `QFORM-TRIANGLE-COMMON-K-PLANE-COMPILER-v1`

Under (1.2) and (1.5),

`boxed: Z_K >= Delta^2 sigma_*^2 delta_K.}`                       (3.1)

In particular, set

`Z0 := Delta^2 sigma_*^2/64
    =1.1575863166387214e-11.`                                   (3.2)

Then at least one of the following holds.

1. **D3 payment.** `Z_K>=Z0` and all K-row three-volume marginals are at most `1/2`. Then

   `boxed: ||p_Q||_infinity <657.718<658,}`                       (3.3)

   and the density has a continuous `C_0` representative.

2. **Physical D3 anchor.** `Z_K>=Z0` and the D3 marginal gate fails. Then one actual original `K` coordinate carries more than

   `boxed: Z0/2 =5.787931583193607e-12}`                         (3.4)

   of the squared third-volume mass.

3. **Common-plane survivor.** `Z_K<Z0`. Then

   `boxed: delta_K<1/64,}`                                      (3.5)

   so

   `||Q_1-Q_2||_op <1/8`, `||Q_1-Q_2||_F^2<1/32`.               (3.6)

   With the single common K-plane `Q:=Q_1`, the two compressed legs satisfy

   `boxed: |det(P_1 N_1 Q)| >= Delta,}`                          (3.7)

   and

   `boxed: |det(P_2 N_2 Q)| > (63/64)Delta
          =0.00141942230334409... .}`                           (3.8)

   Determinants in (3.7)-(3.8) mean the absolute determinant of the induced map between the indicated two-dimensional Euclidean subspaces, hence are basis-independent.

#### Proof

Apply the exterior-volume injection lemma from the preceding B19 report to

`A=N_1^T`, `C=N_2^T`.                                            (3.9)

The top-two left plane of `N_1^T` is `Q_1`, and its top-two singular product is at least `Delta`, so

`Z_K >= Delta^2 ||(I-Q_1)N_2^T||_F^2`.                          (3.10)

Write a singular value decomposition

`N_2=sum_j s_j u_j q_j^T`,                                      (3.11)

where `q_1,q_2` span `Q_2`. Orthogonality of the left singular vectors gives the exact nonnegative decomposition

`||(I-Q_1)N_2^T||_F^2
 =sum_j s_j^2 ||(I-Q_1)q_j||^2
 >=s_2(N_2)^2 sum_(j=1)^2 ||(I-Q_1)q_j||^2`.                    (3.12)

The final sum is precisely `delta_K`, and (1.5) proves (3.1).

If `Z_K>=Z0`, apply the completed D3 theorem (1.7) under its row-marginal gate. Numerically

`6 sqrt(e) Z0^(-1/6)=657.7177976741568...`,                     (3.13)

which proves (3.3). If its gate fails, one physical row owns more than half of `Z_K`, proving (3.4).

Otherwise `Z_K<Z0`, and (3.1)-(3.2) imply (3.5). For rank-two orthogonal projections the principal-angle identities give

`||Q_1-Q_2||_F^2=2 delta_K`,
`||Q_1-Q_2||_op^2=max_i sin^2(theta_i)<=delta_K`,                (3.14)

proving (3.6).

For `N_1`, the compression `P_1N_1Q_1` is exactly its top-two SVD block, so (3.7) is (1.2). For `N_2`, restrict the domain to `Q_1`. The contribution of the top-two SVD block to the positive two-dimensional domain Gram matrix has determinant

`[s_1(N_2)s_2(N_2)]^2 cos^2(theta_1)cos^2(theta_2)`.             (3.15)

Every remaining singular direction adds a positive-semidefinite Gram contribution, so the determinant of the actual two-dimensional compressed Gram matrix can only increase. Since each `sin^2(theta_i)<=delta_K`,

`cos(theta_1)cos(theta_2)>=1-delta_K>63/64`.                     (3.16)

Combining (1.2), (3.15), and (3.16) yields (3.8). QED.

### Consequence

Together with (1.6), failure of the paid/anchor exits leaves **three fixed two-dimensional subspaces**

`E_1=P_1 R^{D_1}`, `E_2=P_2 R^{D_2}`, `E_3=Q_1 R^K`,             (3.17)

such that

`C_0=P_1 C P_2`, `N_0=P_1N_1Q`, `P_0=P_2N_2Q`                  (3.18)

obey

`||C_0||_F^2 >=(9/16)F >0.031901...`,                           (3.19)

`|det N_0|>=Delta`,
`|det P_0|>(63/64)Delta`.                                       (3.20)

The associated grouped random vectors are orthogonal projections of **three disjoint original product banks**, so the three groups are mutually independent. Inside each two-dimensional group the coordinates need not be independent, and I do not assume they are. This is the exact product provenance that must be retained by the final analytic receiver.

## 4. New exact algebra: canonical cycle invariant

The common-plane survivor has a useful exact invariant which was not recorded in the prior assembly.

### Theorem 4.1 — `QFORM-2x2x2-CYCLE-CONGRUENCE-v1`

Let `C,N,P` be real `2x2` matrices with `N,P` invertible and define the symmetric cross-only triangle

`H = [[0,C,N], [C^T,0,P], [N^T,P^T,0]]`.                        (4.1)

Put

`R=N^(-1) C P^(-T)`.                                             (4.2)

Then

`boxed: det H = det(N)^2 det(P)^2 det(R+R^T),}`                  (4.3)

and more strongly

`boxed: rank H = 4 + rank(R+R^T).}`                              (4.4)

Thus the cross-only six-dimensional skeleton has rank `4`, `5`, or `6` according as the symmetric part of `R` has rank `0`, `1`, or `2`.

#### Proof

Use the block-diagonal congruence

`T=diag(N^(-T),P^(-T),I_2)`.                                    (4.5)

It gives

`T^T H T = H_R := [[0,R,I],[R^T,0,I],[I,I,0]]`.                 (4.6)

A vector `(x,y,z)` lies in `ker H_R` iff

`Ry+z=0`, `R^T x+z=0`, `x+y=0`.                                 (4.7)

Hence `y=-x`, `z=Rx`, and the only remaining equation is

`(R+R^T)x=0`.                                                    (4.8)

Therefore

`ker H_R = {(x,-x,Rx): x in ker(R+R^T)}`,                       (4.9)

which proves (4.4), since congruence preserves rank.

For (4.3), the same elimination shows `det H_R=det(R+R^T)` in dimension two (equivalently take the determinant of (4.6) after the block row/column elimination encoded in (4.7)-(4.8)). Finally

`det H_R=det(T)^2 det H
         =det(N)^(-2)det(P)^(-2)det H`,                          (4.10)

which is (4.3). QED.

### Three-parameter normal form

Write

`R=S+aJ`, `S=S^T`, `J=[[0,1],[-1,0]]`.                          (4.11)

A simultaneous orthogonal basis change in the three already-grouped two-dimensional Euclidean spaces preserves the two identity legs in (4.6). Choosing that common basis to diagonalize `S` puts

`R = [[s,a],[-a,t]]`.                                            (4.12)

This is an algebraic basis choice inside already-grouped variables; no claim of coordinate independence is made or needed. Then

`det(R+R^T)=4st`,                                                (4.13)

so the skew parameter `a` does not control the rank defect:

- `st!=0`: cross skeleton rank six;
- exactly one of `s,t` is zero: rank five;
- `s=t=0`: pure-skew cycle, rank four.

In the current branch, (3.20) turns (4.3) into the quantitative identity

`|det H| > (63/64)^2 Delta^4 |det(R+R^T)|`.                      (4.14)

This is not yet a density estimate; it identifies the exact scalar matrix currency a final product-safe cycle receiver must exploit.

## 5. Why this is genuine progress but not closure

The broad r37 phrase "finite 2x2x2 alignment" concealed a real geometric defect: the two K-side singular planes could differ. Theorem 3.1 removes that defect. A mismatch above the fixed principal-angle scale is already an ORIGINAL-coordinate D3 cross volume and is either paid continuously or becomes an explicit physical D3 anchor. The only non-anchor survivor has one common K-plane and two uniformly invertible legs.

Theorem 4.1 then reduces the remaining cross geometry to one `2x2` matrix `R`, and after simultaneous orthogonal normalization to three real parameters `(s,t,a)`. This gives a concrete first missing analytic implication rather than an uncontrolled high-dimensional configuration:

`QFORM-COMMON-PLANE-TRILINEAR-PRODUCT-RECEIVER-v1`:

> For three independent grouped variables obtained as two-dimensional orthogonal projections of disjoint original cap-one product banks, prove a universal density/small-ball estimate for the quadratic form with pairwise cross matrices in the normalized cycle (4.6), while retaining arbitrary same-bank quadratic phases and any outside couplings already present. The estimate must use the original-product provenance inside the groups; a mere bounded joint-density replacement is not justified.

The new projected-crossing theorem does not automatically pay this endpoint: with exact common alignment, choosing one rank-two hub leg makes the residual projected crossing `Z_ell` vanish. This is precisely its stated small-leak limitation, not a contradiction.

The unrestricted QFORM theorem therefore remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity also remains **OPEN**.

## 6. Designated partner account04/B19 applied at an actual inequality

The newest account04/B19 r4 barrier was reread from

`yspennstate/math-open-problems@ac55b70485c4108c7073a75365127e00be3bc097`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B19/20260923T151700Z-account04-B19-QFORM-r4/REPORT.md`.

It proves that for every `0<epsilon<1` there is a cap-one **joint** triple independent of a scalar `X` for which

`T=4XY+Z^2-YW`, `||p_T||_infinity >=1/(9epsilon)`.                (6.1)

Thus any attempted successor which compresses a product-origin bank to an arbitrary joint cap and claims a constant `C_joint>1/18` fails by the explicit choice

`epsilon=1/(18 C_joint)`,                                       (6.2)

because then

`boxed: ||p_T||_infinity >=2 C_joint>C_joint.}`                  (6.3)

I use this only to forbid that invalid collapse; it is not a counterexample to the original independent-coordinate target and does not rule out a theorem for the three independent product-projection groups in Section 5.

The completed positive account04/B19 null-coloop result also remains an actual paid edge of the proof graph. In its exact residual-diffuse null-coloop scope,

`||p_Q||_infinity <34 sqrt(log(e/D_res))`.                        (6.4)

Hence on `e^-8<=D_res<=1`,

`boxed: ||p_Q||_infinity<102.}`                                  (6.5)

No extension of (6.4) is made to the common-plane cycle.

## 7. Verification and scope ledger

The checker recomputes all live constants, verifies (3.1) on 2000 random noncommuting matrix pairs, verifies the common-plane determinant-retention inequality, and checks (4.3) on 2000 random invertible edge triples. It terminates

`QFORM_B19_R38_COMMON_PLANE_CYCLE_CHECK_PASS`.

The numerical test is a regression check only; the proofs are the algebra above. All signs are allowed, repeated singular values are harmless (choose any top-two singular planes), and no distributional regularity beyond the target density caps is added. The D3 theorem is invoked only under its explicit marginal gate. Essential boundedness/continuity is claimed only on the displayed D3 and previously paid null-coloop branches.
