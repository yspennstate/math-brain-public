SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B08, 2026-09-23T17:39:57Z.
attacking: fixed-frame diffuse closure — turn simultaneous near-rank-one child blocks plus a near-rank-two physical cross block into one balanced original-coordinate half-cut with a robust third cross singular value, independent of child/cross alignment.

# account01/B08 r32 — fixed-frame diffuse closure of the low-rank k=1 chamber

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** diffuse eigenvector case  
**Designated partner:** `account02/B08`  
**Classification:** `PROVED SUPPORTING STRUCTURAL/ANALYTIC THEOREM + DESIGNATED PARTNER APPLIED / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

The unrestricted owner target remains **OPEN**. The theorem below gives a continuous `C_0` density only on an explicit diffuse fixed-frame chamber. No moment, support, log-concavity, iid, Gaussian, or post-rotation independence assumption is used.

## 1. The missing implication attacked

The preceding B08 run left a `k=1` near-aligned high-amplification survivor: one child direction and two physical cross directions can become almost aligned on one side, so a one-sided three-frame recoloring loses a factor of the sine-angle. The point of the present run is that **alignment is not itself an obstruction when both child blocks are simultaneously near rank one and the cross block is near rank two**. In that chamber the entire non-diagonal coefficient matrix lies near a fixed frame of dimension at most six. A single macroscopic physical half-cut then produces a true third cross singular direction with a uniform constant.

The resulting router is angle-free. If the combined six-frame is diffuse and

`max{s_2(C),s_2(D)} + s_3(B) <= L/65`,

the full ambient form has a continuous density `<83/L`. Thus any unpaid diffuse `k=1` survivor must instead have a genuine second child direction, a genuine third cross direction, or a heavy physical coordinate in the combined frame.

## 2. Source-pinned premises

### 2.1 Full ambient cross-block stability theorem

I use the complete theorem at

`yspennstate/math-open-problems`,
`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`,
read on current `master` (blob `f9efb2a4c89b81707d720b88db35ebdea2013f74`).

Its exact scope is: for disjoint ORIGINAL coordinate banks and a literal physical cross block

`M=M_0+E`,

if

`s_3(M_0)>=a>0`,
`max_i (P_range(M_0))_ii <=1/2`,
`||E||op<=a/16`,

then the **full ambient quadratic-plus-affine form**, with arbitrary within-bank measurable phases and arbitrary outside couplings, has a continuous `C_0` density satisfying

`||p_Q||infinity <23/a`.

This is a coefficient-matrix perturbation statement for the actual cross block, not a small-random-variable perturbation argument.

### 2.2 Completed designated-partner theorem actually applied

The completed `account02/B08` r28 report is

`yspennstate/math-open-problems@66582bd87d50634f3525a57c87acffdbde97aea1`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/20260923T153836Z-account02-B08-qform-r28/REPORT.md`.

Its `QFORM-K1-MACROSCOPIC-3FRAME-HALFCUT-v1` says, in the one-sided transverse `k=1` chamber, that if the augmented physical three-frame has leverage at most `1/48`, the child/cross sine-angle is at least `1/2`, and the child/cross operator leakage is at most `kappa(1/2)L/16`, then the full ambient form has a continuous density `<23/[kappa(1/2)L]`.

The earlier B08 squared-energy ledger gives the stronger actual cross scale

`beta = s_2(B)/L >= 3/sqrt(40)=0.4743416490252569...`

instead of the partner report's older `beta=(3/16)sqrt(3/5)`. With

`c=sqrt(3/20)=0.3872983346207417...`, `delta_angle=1/2`,

the partner formula gives

`kappa = c beta delta_angle^2 / [2 sqrt(c^2 delta_angle^2 + 4 beta^2)]`
`      =0.023717082451262847...`.

Therefore, on that actual transverse branch,

`sqrt(s_2(C)^2+s_3(B)^2) <=0.001482317653203928 L`

implies

`||p_Q||infinity <969.765149118303/L`

with a continuous `C_0` density. This remains useful when the opposite child block is completely uncontrolled; the new theorem below instead treats the two-sided low-rank chamber and removes the angle condition entirely.

## 3. Balanced-cut lemma for a diffuse fixed frame

Let `R` be an `n x r` matrix with orthonormal columns and physical row vectors `R_i`. Put

`nu=max_i ||R_i||_2^2`.

For a subset `S` of original coordinates define

`G_S=R_S^T R_S`, `G_T=I-G_S`, `T=S^c`.

### Lemma 3.1 — deterministic balanced half-cut from squared Frobenius averaging

There exists an original-coordinate cut `S|T` such that

`||G_S-(1/2)I_r||op <= (1/2)sqrt(r nu)`.

Consequently, with

`a_r,nu := (1-sqrt(r nu))/2`,

if `r nu<1` then

`G_S >= a_r,nu I_r`, `G_T >= a_r,nu I_r`.

#### Proof

Choose independent Rademacher signs `eps_i` and put `S={i:eps_i=1}`. Then

`G_S-(1/2)I_r=(1/2) sum_i eps_i R_i^T R_i`,

where `R_i^T R_i` denotes the rank-one outer product of the physical row. Independence and centering give

`E ||G_S-(1/2)I_r||_F^2`
` =(1/4) sum_i ||R_i^T R_i||_F^2`
` =(1/4) sum_i ||R_i||_2^4`
` <=(nu/4) sum_i ||R_i||_2^2`
` = r nu/4`.

Hence at least one sign choice has Frobenius norm squared at most `r nu/4`. The operator norm is no larger than the Frobenius norm, proving the claim. Since `G_T=I-G_S`, the same lower bound holds for `G_T`. QED.

This avoids the Markov slack used in a cruder half-cut estimate and is exact enough to improve the final constant.

## 4. Main theorem: a fixed-frame diffuse closure

### Theorem 4.1 — `QFORM-FIXED-FRAME-HALFCUT-v1`

Let `A` be a real symmetric `n x n` matrix with

`s_3(A)>=L>0`.

Assume that, in the ORIGINAL coordinate basis,

`A = D_0 + R K R^T + E`,

where

- `D_0` is diagonal;
- `R^T R=I_r` with `r>=3`;
- `K` is real symmetric `r x r`;
- `||D_0||op <= d L`;
- `||E||op <= eps L`;
- `nu=max_i ||R_i||^2`;
- `r nu<1`.

Put

`a=(1-sqrt(r nu))/2`.

Assume further

`nu/a <=1/2`,

and

`eps <= a(1-d-eps)/16`.                                      (4.1)

Then for every independent real input vector with one-dimensional densities bounded by one, and for every additional affine term, the full quadratic form has a continuous `C_0` density and

`boxed: ||p_Q||infinity < 23/[a(1-d-eps)L].`                 (4.2)

#### Proof

By Weyl,

`s_3(R K R^T) >= s_3(A)-||D_0+E||op`
`               >= (1-d-eps)L`.                              (4.3)

Because `R` is an isometry on coefficient space, the nonzero singular values of `R K R^T` equal those of `K`; therefore

`s_3(K)>=(1-d-eps)L`.                                         (4.4)

Apply Lemma 3.1 and choose an original-coordinate cut `S|T` with

`G_S,G_T >= a I_r`.                                           (4.5)

The diagonal term contributes no cross entries. Define

`M_0=(R K R^T)[S,T]=R_S K R_T^T`,
`M=A[S,T]=M_0+E[S,T]`.                                        (4.6)

Since `G_S,G_T` are positive definite, write polar factorizations

`R_S=U_S G_S^(1/2)`, `R_T=U_T G_T^(1/2)`

with `U_S,U_T` having orthonormal columns. Hence the nonzero singular values of `M_0` are those of

`G_S^(1/2) K G_T^(1/2)`.

The min-max inequality gives

`s_3(M_0) >= sqrt(lambda_min(G_S)) s_3(K) sqrt(lambda_min(G_T))`
`          >= a(1-d-eps)L`.                                   (4.7)

Next, `range(M_0)` is contained in `range(R_S)`. The orthogonal projection onto `range(R_S)` is

`P_S=R_S G_S^(-1) R_S^T`.

For a physical row `i in S`,

`(P_S)_{ii}=R_i G_S^(-1) R_i^T <= ||R_i||^2/a <=nu/a<=1/2`. (4.8)

For `i notin S` it is zero. Therefore the same `1/2` leverage bound holds for `P_range(M_0)`.

Finally,

`||E[S,T]||op <= ||E||op <=eps L`

and (4.1),(4.7) give

`||E[S,T]||op <= s_3(M_0)/16`.                                (4.9)

The complete cross-block stability theorem from Section 2.1 now applies to the **actual** physical cross block `M`, while retaining every same-bank term and every outside coupling. It yields (4.2), continuity, and vanishing at infinity. QED.

## 5. Angle-free two-child/rank-two-cross corollary

Split the ORIGINAL coordinates into `I disjoint union J` and write

`A=[[C,B],[B^T,D]]`.

Let `C_1` and `D_1` be best rank-one spectral truncations of the symmetric child blocks, so

`||C-C_1||op=s_2(C)`, `||D-D_1||op=s_2(D)`.

Let `B_2` be the best rank-two SVD truncation of the physical cross block, so

`||B-B_2||op=s_3(B)`.

Let `W_I` be an orthonormal basis of the physical subspace

`range(C_1)+range(B_2)`

and `W_J` an orthonormal basis of

`range(D_1)+range(B_2^T)`.

Each has dimension at most three. Put

`R=diag(W_I,W_J)`,

so `r=rank(R)<=6`, and let

`nu=max physical row leverage of range(R)`.

The structured matrix

`A_0=[[C_1,B_2],[B_2^T,D_1]]`

lies exactly in `range(R)`, so `A_0=R K R^T` for a symmetric `K`. The remainder is

`E=A-A_0`
` =diag(C-C_1,D-D_1)+[[0,B-B_2],[(B-B_2)^T,0]]`.

Therefore

`||E||op <= max{s_2(C),s_2(D)} + s_3(B)`.                     (5.1)

### Corollary 5.1 — `QFORM-TWOCHILD-RANK2-CROSS-DIFFUSE-CLOSURE-v1`

If

`s_3(A)>=L`,
`nu<=1/32`,
`max{s_2(C),s_2(D)}+s_3(B) <= L/65`,                           (5.2)

then the full ambient quadratic form has a continuous `C_0` density and

`boxed: ||p_Q||infinity <83/L.`                               (5.3)

#### Proof

If the structured frame had rank below three, (5.1),(5.2) and Weyl would contradict `s_3(A)>=L`, so `3<=r<=6`.

Since `r<=6` and `nu<=1/32`,

`a=(1-sqrt(r nu))/2 >= (1-sqrt(6/32))/2`
`  =(4-sqrt(3))/8`
`  =0.28349364905389035...`.                                  (5.4)

Also

`nu/a <= (1/32)/0.28349... <1/2`.                             (5.5)

Take `D_0=0` and `eps=1/65`. Because `a>1/4`,

`eps=1/65 <= a(1-eps)/16`

is immediate from `16<=64a`. Thus Theorem 4.1 gives

`||p_Q||infinity`
` <23/[a(64/65)L]`
` <=1495/[8(4-sqrt(3))] * 1/L`
` =82.3982303588.../L <83/L`.                                 (5.6)

QED.

### Corollary 5.2 — explicit survivor router

Under `s_3(A)>=L`, for every original cut `I|J`, form the two-child/rank-two-cross frame above. If its physical leverage is at most `1/32`, then either

`||p_Q||infinity <83/L` with a continuous `C_0` density,

or at least one of

`s_2(C) > L/130`,
`s_2(D) > L/130`,
`s_3(B) > L/130`                                               (5.7)

holds.

Indeed, if all three quantities were at most `L/130`, then

`max{s_2(C),s_2(D)}+s_3(B)<=L/65`

and Corollary 5.1 would apply.

This is the useful B08 conclusion: in the genuinely diffuse chamber, **near alignment of a child with the top-two cross plane is no longer an unpaid endpoint**. If no second child direction and no third cross direction exists at scale `L/130`, the entire low-rank geometry can be paid by a macroscopic half-cut. The remaining alternative is a heavy physical coordinate of the combined at-most-six-dimensional frame, which is precisely the localized-coordinate side of the global dichotomy.

## 6. Relation to the designated partner result

The new theorem and the completed account02/B08 theorem are complementary, not duplicates.

- Partner r28 is **one-sided**: it permits the opposite child bank and the rest of the ambient matrix to be arbitrary, but requires a transverse child/cross angle, a diffuse three-frame, and very small one-sided leakage. After inserting the stronger actual cross scale `3/sqrt(40)L`, it gives the concrete bound `<969.766/L` whenever

  `d_angle>=1/2`, `nu_3<=1/48`,
  `sqrt(s_2(C)^2+s_3(B)^2)<=0.001482317653203928 L`.

- Corollary 5.1 is **two-sided low-rank**: it allows every angle, including exact alignment, and a much larger total residual `L/65=0.0153846...L`, but requires the opposite child also to be near rank one and the combined at-most-six-dimensional frame to be diffuse.

Thus the current `k=1` compiler can route as follows. A transverse one-sided state can use the completed partner theorem even if the opposite child is wild. A near-aligned state with both child blocks near rank one and the cross block near rank two can use Corollary 5.1 regardless of angle. Failure of the latter exposes either a genuine next singular direction at scale `>L/130` or a localized physical row.

## 7. Remaining implication

The full target is not proved. The first remaining B08 implication is now

`QFORM-SIXFRAME-HEAVYROW-OR-NEXTDIRECTION-RECEIVER-v1`:

> Starting from the router (5.7), pay either (i) a physical coordinate with combined six-frame leverage `>1/32`, or (ii) a genuine second child / third cross singular direction `>L/130`, while retaining arbitrary same-bank curvature, affine terms induced by conditioning, and the full complementary spectrum.

The heavy-row branch is intended to feed localized-coordinate conditioning/pivot machinery; the next-direction branch should feed the existing robust-third-cross or multi-child receivers. No claim is made here that either receiver is automatic under only (5.7).

## 8. Finite check

A deterministic numerical sanity check was run separately on random orthonormal six-frames. For each sampled frame a random physical half-cut satisfying the balanced Gram inequalities was found; for random symmetric `K`, the observed ratio

`s_3(R_S K R_T^T)/s_3(K)`

stayed above the theorem's lower threshold `a`. This is only a finite check of the matrix inequalities, not a proof. The proof is Sections 3–5.

## 9. Status

- Full universal bounded-density conjecture: **OPEN**.
- Full continuity statement: **OPEN**.
- Theorem 4.1 and Corollaries 5.1–5.2: proved supporting results under their explicit fixed-frame/diffuse hypotheses.
- No rotation of random inputs, no moment assumption, no probabilistic small-perturbation shortcut.
- Repository transport is not native learned-memory ingestion: `WITHOUT_VERIFIED_BRAIN`.
