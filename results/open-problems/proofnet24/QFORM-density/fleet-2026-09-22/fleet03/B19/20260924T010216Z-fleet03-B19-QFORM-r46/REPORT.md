SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B19, 2026-09-24T01:02:16Z.
attacking: `QFORM-TWOSTAR-TO-ALIGNED-R2-OR-E3-v1` — convert the r45 physical two-star residue, including coincident anchors, into either a source-valid physical E3 payment or a quantitatively star-aligned rank-two interbank collar.

# fleet03/B19 r46 — physical two-star packet collapses to E3 or a star-aligned rank-two collar

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Universal proof assembly / SYNTHESIS  
Status: **NEW STRUCTURAL CLOSURE + LIVE E3 PAYMENT / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`.  
Full-target continuity: **OPEN**.

## 1. Exact target, control boundary, and fresh inputs

The target remains the unrestricted owner statement: independent real ORIGINAL coordinates `X_i` with one-dimensional probability densities `0<=f_i<=1`, arbitrary real symmetric `A`, and at least three eigenvalues of absolute value at least one. No Gaussian, log-concave, moment, compact-support, connected-support, iid, centered, smoothness, diagonal-basis, or post-rotation independence assumption is used.

The same-hour canonical fleet03/B19 login already existed at

`scheduled_tasks/status/fleet03/logins/2026-09-24T01Z/B19.json`

with run id `20260924T010216Z-fleet03-B19-QFORM-r46`; it was preserved rather than overwritten, as required by `PROTOCOL.md`.

The fresh proof graph consumed here is:

1. **fleet03/B19 r45 local synthesis**: `yspennstate/math-open-problems@73b00e5e496973ec5936c2c31e9d44894d221f2c`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B19/20260924T000337Z-fleet03-B19-QFORM-r45/REPORT.md`. After already-paid diagonal/principal-triple/disjoint-E3/strong-shared-edge branches, one residual packet is a literal physical two-star

   `||A[R,p]||_2 ||A[q,C]||_2 >= 2/9`,                         (1.1)

   where `R,C` are disjoint original-coordinate banks, `p,q` lie outside them, and `p=q` is explicitly allowed.

2. **fleet01/B02 physical E3 receiver**, source used by its corrected r41 frontier: `yspennstate/math-open-problems@aeaba9e3351623ead11450857c2d014b43664aef`. For every literal original-coordinate cross block `M`, if

   `E3(M):=e_3(MM^T)>0`,

   then the full ambient quadratic form has a continuous `C_0` density and

   `||p_Q||_infinity <= 10.345084 E3(M)^(-1/6)`.                (1.2)

   Hence the concrete gate `E3(M)>=2^(-18)` pays by

   `||p_Q||_infinity <=82.760672`.                               (1.3)

   Arbitrary same-bank curvature, outside coordinates/couplings, signs, and affine terms remain in that theorem.

3. **fleet03/B20 r43 E2 funnel**, `yspennstate/math-open-problems@97af54ab6c7f082493cfa539508780275ebf9a39`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B20/20260924T004659Z-fleet03-B20-QFORM-r43/REPORT.md`. It proves the deterministic inequality

   `T_2 E2(M) <=3 E3(M)`,                                         (1.4)

   where `T_2=dist_F(M,{rank<=2})^2`, and refines the live `E2>4/9` branch to a continuous E3 payment or an ultra-thin robust-rank-two / giant-rank-one literal crossing.

4. **fleet04/B19 designated partner barrier**, `yspennstate/math-open-problems@ac55b70485c4108c7073a75365127e00be3bc097`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B19/20260923T151700Z-fleet04-B19-QFORM-r4/REPORT.md`. Its moving-ridge construction shows that a mere bounded JOINT density after compression cannot replace original-product provenance.

The active corrections are respected: no law-uniform scalar quadratic van-der-Corput estimate, no arbitrary-joint coarea cap, no conditional-projection cap as independence, no fiber supremum, no one-good-minor extraction from aggregate volume, no deletion of a nonzero coefficient tail, and no independence claim after a nontrivial rotation.

## 2. Exterior identity for a physical appended star

Let `N` be an `r x c` real matrix and `u in R^r`, `u!=0`. Put

`M_u=[N  u]`.                                                       (2.1)

Let `P_u` be orthogonal projection onto `span(u)` and `P_u^perp=I-P_u`.

### Lemma 2.1 — `QFORM-APPENDED-STAR-THIRD-VOLUME-IDENTITY-v1`

The sum of squares of the `3 x 3` minors of `M_u` that use the appended column is exactly

`boxed:
 sum_{|I|=3, |J|=2} det M_u[I,J union {star}]^2
 = ||u||_2^2 e_2((P_u^perp N)(P_u^perp N)^T).`                    (2.2)

In particular,

`E3(M_u) >= ||u||_2^2 e_2((P_u^perp N)(P_u^perp N)^T).`           (2.3)

There is a row-dual identity: for `v in R^c`,

`M_v=[N; v^T]`,

`E3(M_v) >= ||v||_2^2 e_2((N P_v^perp)(N P_v^perp)^T).`           (2.4)

#### Proof

Apply a deterministic orthogonal change of basis in the ROW SPACE only for the purpose of computing Euclidean exterior volume, sending `u` to `||u|| e_1`. This is not a change of random coordinates and makes no independence assertion. Total squared minors are invariant under this orthogonal row change. A `3 x 3` minor using the appended column vanishes unless its selected row triple contains row 1; expansion along the appended column then gives `||u||` times a `2 x 2` minor of the rows `2,...,r` of the transformed `N`. Cauchy--Binet sums their squares to the `e_2` term in (2.2). The row-dual statement follows by transposition. QED.

## 3. Rank-one tail inequality used by the compiler

For any real matrix `W` with squared singular values `x_1>=x_2>=...>=0`, write

`E=||W||_F^2=sum_i x_i`, `E2=e_2(WW^T)`.

Then

`E^2=sum_i x_i^2+2E2 <= x_1 E+2E2`,

so, whenever `E>0`,

`boxed:
 dist_F(W,{rank<=1})^2=E-x_1 <= 2E2/E.`                            (3.1)

This is dimension-free and deterministic.

## 4. Main theorem: two-star to physical E3 or star-aligned rank two

Let `R,C` be disjoint original-coordinate banks. Let `p,q` be original coordinates outside `R union C`; **they may coincide**. Put

`N=A[R,C]`,
`u=A[R,p]`,
`v=A[q,C]`,
`delta=||u||_2 ||v||_2>0`.                                        (4.1)

Choose the stronger physical star. If `||u||>=||v||`, define the literal disjoint physical cross block

`M_*:=A[R,C union {p}]=[N u]`.                                    (4.2)

If `||v||>||u||`, define instead

`M_*:=A[R union {q},C]=[N;v^T]`.                                  (4.3)

Both are genuine original-coordinate cross blocks even when `p=q`, because the selected row and column banks are disjoint.

### Theorem 4.1 — `QFORM-TWOSTAR-TO-ALIGNED-R2-OR-E3-v1`

Let `Z=E3(M_*)`. There exists a rank-at-most-two matrix `N_2` such that

`boxed:
 ||N-N_2||_F <= (2Z/delta)^(1/4).`                                (4.4)

Moreover the rank-two approximant contains the stronger **physical star direction exactly**:

- if `||u||>=||v||`, one may take
  `N_2=u a^T+b c^T`;                                               (4.5)
- if `||v||>||u||`, one may take
  `N_2=a v^T+b c^T`.                                               (4.6)

Thus every two-star packet has an exact, product-coordinate-safe dichotomy at every `zeta>0`:

1. `E3(M_*)>=zeta`, so any valid physical-E3 receiver may be applied to the FULL law; or
2. the interbank block lies in the star-aligned rank-two collar

   `dist_F(N,{rank<=2 aligned with the stronger physical star})
    <(2zeta/delta)^(1/4)`.                                        (4.7)

#### Proof

Assume `||u||>=||v||`; the other case is the transpose. Set

`L=||u||`, `W=P_u^perp N`, `E=||W||_F^2`.

Because `L=max(||u||,||v||)`,

`L^2>=||u||||v||=delta`.                                          (4.8)

By Lemma 2.1,

`e_2(WW^T) <= Z/L^2 <= Z/delta`.                                  (4.9)

Put

`a_0=(2Z/delta)^(1/4)`, so `a_0^4=2Z/delta`.                       (4.10)

If `E<=a_0^2`, take `W_1=0`; then `||W-W_1||_F<=a_0`. If `E>a_0^2`, let `W_1` be a best rank-one approximation. By (3.1) and (4.9),

`||W-W_1||_F^2
 <=2 e_2(WW^T)/E
 <=2Z/(delta E)
 <2Z/(delta a_0^2)=a_0^2`.                                       (4.11)

In both cases `W_1` has rank at most one and the error is at most `a_0`. Since

`N=P_u N+W`,                                                       (4.12)

`P_u N=u a^T` has rank at most one with left factor exactly the physical star `u`. Therefore

`N_2=P_uN+W_1=u a^T+b c^T`                                       (4.13)

has rank at most two and satisfies (4.4). QED.

The proof is entirely deterministic until the final E3 receiver is invoked. No projected random coordinate is called independent.

## 5. Apply the theorem to the live r45 physical two-star packet

The r45 packet has

`delta=||A[R,p]||_2 ||A[q,C]||_2 >=2/9`.                          (5.1)

Take the already-source-valid physical-E3 gate

`zeta=2^(-18)`.                                                    (5.2)

### Paid branch

If `E3(M_*)>=2^(-18)`, (1.2) gives for the ORIGINAL FULL quadratic form

`boxed: ||p_Q||_infinity <=82.760672,`                             (5.3)

and the density is continuous and vanishes at infinity.

### Surviving branch

If `E3(M_*)<2^(-18)`, Theorem 4.1 and (5.1) give

`||N-N_2||_F
 <(2*2^(-18)/(2/9))^(1/4)
 =(9*2^(-18))^(1/4)
 =0.07654655446197431... .`                                       (5.4)

Hence every still-unpaid r45 two-star state satisfies the genuinely stronger packet

`boxed:
 ||A[R,p]|| ||A[q,C]|| >=2/9,
 A[R,C]=N_2+E,
 rank(N_2)<=2,
 ||E||_F<0.076547,`                                                (5.5)

with `N_2` containing the stronger actual physical star as one of its two rank-one factors. This is valid for `p=q` and `p!=q` alike.

The `0.076547` coefficient is a deterministic geometric collar only. The nonzero tail `E` is retained in the actual quadratic form and is **not** deleted as a small random perturbation.

## 6. Splice with the fresh r45/B20 global frontier

The r45 local compiler and the B20 r43 refinement can now be assembled into a narrower correction-safe frontier.

After the already-paid diagonal, principal-triple, strong-shared-edge and physical-E3 branches, every remaining state is routed into one of the following literal original-coordinate mechanisms:

1. **disjoint `E2>4/9` block:** B20 r43 says it is either continuously paid when `E3>=2^-18`, or is an ultra-thin robust-rank-two crossing

   `sigma_2>=1/8`, `dist_F(rank<=2)<3sqrt(3)/1024=0.00507437...`,

   or a giant near-rank-one crossing

   `sigma_1>5.32894`, `dist_F(rank<=1)<0.125103`;

2. **one-anchor packet:** `||A[j,C]||||A[R,j]||||A[R,C]||_F>=1/96`;

3. **physical two-star packet:** by this run, either paid by (5.3) or reduced to the aligned rank-two collar (5.5);

4. **the stronger giant near-rank-one crossing already produced directly by r45:** `sigma_1>17.0665`, `dist_F(rank<=1)<5sqrt(2)/128=0.055243`.

Therefore the former unrestricted physical two-star packet is no longer an amorphous branch. Its entire remaining content is a two-latent-direction collar with one latent direction fixed by an actual original-coordinate star.

The first local missing implication becomes

`QFORM-ALIGNED-R2-STAR-OR-ONEANCHOR-PAYMENT-v1`:

> uniformly pay the star-aligned rank-two collar (5.5), together with the one-anchor / giant-rank-one collars, while retaining the genuine nonzero tail and arbitrary same-bank curvature; or force one of the already-paid physical E3, ridge, square-bank, pair-log, grouped-hub, or inductive principal-block exits.

This is strictly narrower than the r45 `QFORM-LOCAL-E2-OR-RANK1-OR-TWOSTAR-PAYMENT-v1` debt.

## 7. Designated fleet04/B19 result applied at an actual inequality

The latest designated partner result `QFORM-MOVING-RIDGE-JOINT-CAP-BARRIER-v1` is not a positive receiver; it is a sharp correction boundary. It is directly applicable to the tempting shortcut for (5.5).

A false closure attempt would compress the original-product leaf bank to a three-dimensional statistic `(Y,Z,W)` with only a JOINT density cap `||rho||_infinity<=1`, keep an independent scalar `X`, and assert a universal estimate

`||p_[4XY+Z^2-YW]||_infinity <=K`                                 (7.1)

for one finite `K` depending only on the joint cap.

The partner theorem gives, for every `epsilon in (0,1)`, an admissible joint density with `||rho||_infinity<=1` for which

`||p_[4XY+Z^2-YW]||_infinity >=1/(9epsilon)`.                     (7.2)

Apply it at the actual numerical value

`epsilon=2^(-20)`.                                                 (7.3)

Then

`boxed:
 ||rho||_infinity<=1,
 ||p_[4XY+Z^2-YW]||_infinity >=2^20/9
 =116508.444444... .}`                                             (7.4)

Since `epsilon` is arbitrary, (7.1) has no universal finite `K`. Thus the new aligned-rank-two collar may **not** be closed by replacing its latent physical projections by an arbitrary bounded joint law. Any valid next receiver must keep the fact that they arise as linear images of independent cap-one ORIGINAL coordinates, or must use another physical-coordinate mechanism. This is an equation-level application of the designated partner result to the exact kind of inequality suggested by the new collar.

For comparison, the partner's earlier exact-null-coloop positive theorem remains valid on its own scope; nothing here extends it to a merely near-null or near-rank-two row.

## 8. Quantitative verification

The identity (2.2) was independently tested on 3,000 noncommuting random rectangular matrices of dimensions between 3 and 8. The maximum normalized residual between the direct sum of squared appended-column `3 x 3` minors and the right side of (2.2) was

`4.016462764296098e-15`,

with zero violations at tolerance `1e-9`.

The constructive bound (4.4) was tested on 5,000 random `N,u,v` instances with star norms spanning two orders of magnitude. The maximum observed ratio

`||N-N_2||_F / (2E3(M_*)/delta)^(1/4)`

was `0.8479258486787247`, with zero violations. These tests are diagnostic only; Sections 2--4 are exact proofs.

Exact live constants:

- two-star threshold: `delta_0=2/9`;
- physical-E3 split: `zeta=2^-18`;
- aligned rank-two tail: `(2zeta/delta_0)^(1/4)=0.07654655446197431...`;
- partner moving-ridge lower bound at `epsilon=2^-20`: `2^20/9=116508.444444...`.

## 9. Status

`QFORM-APPENDED-STAR-THIRD-VOLUME-IDENTITY-v1`: **PROVED supporting identity**.  
`QFORM-TWOSTAR-TO-ALIGNED-R2-OR-E3-v1`: **PROVED structural closure**.  
The `E3>=2^-18` branch is **PAID continuously** by `<82.760672`.  
The aligned rank-two survivor is **NOT YET PAID**.  
Full QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.  
Full-target continuity: **OPEN**.

No task identity, schedule, cadence, enabled/paused state, notification, email, permission, public release, paid model/API call, installation, or cross-account authentication was changed by this run.
