SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B08, 2026-09-23T16:47:08.414018Z.
attacking: the balanced k=1 range-defect identity — force a true third physical cross direction from child/cross alignment, then spend the genuinely transverse diffuse branch with account02/B08's completed macroscopic half-cut receiver.

# account01/B08 r31 — balanced k=1 range defect and transverse half-cut payment

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner continuation consumed:** `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`  
**Role:** diffuse eigenvector case  
**Designated partner:** account02/B08  
**Classification:** `NEW EXACT STRUCTURAL INEQUALITY + COMPLETED PARTNER APPLIED / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

The unrestricted conjecture remains **OPEN**. Continuity is proved only on the explicit Fourier/volume branches stated below. No rotation of the random variables, moment assumption, support assumption, log-concavity, Gaussian input, or random-quadratic perturbation step is used.

## 1. Source refresh and premises

Fresh control was reread after the 2026-09-23 16:44 UTC owner continuation. The current owner continuation keeps all workers exclusively on QFORM and requires reading the current Claude continuation. I read:

- `yspennstate/math-research-brain@c46b048e944ba806a41456dd1d672170a43c8cfc`, `AGENTS.md`, `scheduled_tasks/README.md`, the live correction inbox and `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z.md`;
- Claude continuation `yspennstate/math-open-problems@c4c23b784395630c094ba299a50712209921d1ae`, `proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/README.md` and `single_hub_core/REPORT.md`. Its `(SP)` estimate is OPEN, so it is not used as a premise here;
- the new projected-crossing checkpoint `yspennstate/math-open-problems@4f92aeb74083c6f95cb314a11fed1b812eacef9a`, `proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`. It is not needed for the identity proved below;
- this slot's preceding gate `yspennstate/math-open-problems@014df00b32f2360c1b5c835434bb146cf57e1930`, `proofnet24/QFORM-density/fleet-2026-09-22/account01/B08/20260923T153626Z-account01-B08-qform-r30/REPORT.md`;
- completed partner report `yspennstate/math-open-problems@535ec99ca6cc7fd0667dcb3f22dfdca7ec7420ce`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/20260923T153836Z-account02-B08-qform-r28/REPORT.md`. A newer account02/B08 r30 item was only an early checkpoint at source refresh, not a completed theorem.

The live corrections prohibiting law-uniform pointwise quadratic-phase decay, rotated independence, arbitrary-joint coarea caps, and small-random-error inference from a small matrix error are all respected.

## 2. First missing implication attacked

The r30 energy ledger puts the balanced `k=1` state at

`R_I^T R_I >= (3/8) I_3`,

with one child direction in `C=A[I,I]`, and with the literal physical cross block `B=A[I,J]` satisfying

`s_2(B) > delta L`,    `delta=3/sqrt(40)=0.4743416490252569...`.

The remaining geometric question was whether the child top direction can lie almost inside the top-two left singular plane of `B` while `B` has essentially only two cross directions. The next theorem gives an exact obstruction.

## 3. Exact balanced range-defect theorem

Let `A` be real symmetric. Let `R in R^{n x 3}` have orthonormal columns and

`A R = R Lambda`,    `min_j |Lambda_jj| >= L >0`.

Take an ORIGINAL-coordinate partition `I disjoint_union J`, and write

`A = [[C,B],[B^T,D]]`.

Assume

`R_I^T R_I >= alpha I_3`,    `alpha>0`.

Let `(mu,r)` be a top-modulus eigenpair of the symmetric child block `C`, so `|mu|=s_1(C)` and `||r||=1`. Let `U` be the top-two left singular plane of `B`, let

`d = ||(I-UU^T)r||`,
`rho = ||R_I^T r||`,

and use the conventions `s_2(C)=0` or `s_3(B)=0` when the corresponding rank is too small.

### Theorem 3.1 — `QFORM-BALANCED-K1-RANGE-DEFECT-v1`

One has the exact deterministic inequality

`boxed:  sqrt(alpha) L <= |mu| rho d + s_2(C) + s_3(B).`        (3.1)

This keeps the complete complementary spectrum of `A`.

### Proof

Put

`C_1 = mu r r^T`

and let `B_2` be the top-rank-two singular truncation of `B`, with left range contained in `U`. The selected eigen-relation restricted to the physical bank `I` is

`R_I Lambda = C R_I + B R_J`.

Split this as

`R_I Lambda = T_0 + E`,
`T_0 = C_1 R_I + B_2 R_J`,
`E = (C-C_1)R_I + (B-B_2)R_J`.                                 (3.2)

Because `R` is an orthonormal frame, both coordinate restrictions have operator norm at most one. Hence

`||E||_op <= s_2(C)+s_3(B)`.                                    (3.3)

Let `P_U=UU^T`. The matrix `P_U T_0` has rank at most two. Therefore Eckart--Young gives

`s_3(T_0) <= ||(I-P_U)T_0||_op`.

The `B_2` term is killed by `I-P_U`, while

`(I-P_U) C_1 R_I
 = mu (I-P_U)r (r^T R_I)`.

Consequently

`s_3(T_0) <= |mu| d ||R_I^T r|| = |mu| rho d`.                  (3.4)

On the other hand,

`s_3(R_I Lambda)
 >= s_3(R_I) s_3(Lambda)
 >= sqrt(alpha) L`.                                               (3.5)

Weyl's singular-value perturbation inequality applied to (3.2), together with (3.3)--(3.5), proves (3.1). QED.

### Why this is useful

No coefficient outside the selected three-eigenvector relation is thrown away: it is already inside the literal blocks `C,B,D`. In particular, an arbitrarily large complementary eigenvalue is allowed. Repeated selected eigenvalues and all sign patterns are harmless because only singular values of `Lambda` enter.

## 4. Consequence on the actual balanced k=1 gate

The current gate uses

`alpha=3/8`,
`c=sqrt(3/20)=0.3872983346207417...`,

and on the side with child count `k=1`,

`s_2(C)<cL`.

Define

`eta = sqrt(3/8)-sqrt(3/20)
     =0.22507410107505277...`.                                  (4.1)

Then (3.1) gives

`boxed: |mu| rho d + s_3(B) > eta L.`                           (4.2)

Thus an exactly aligned child (`d=0`) cannot coexist with a rank-two cross block in this balanced gate: it forces

`s_3(B)>eta L`.                                                   (4.3)

More generally, whenever

`|mu| rho d <= (eta/2)L`,                                       (4.4)

one has

`s_3(B)>(eta/2)L =0.11253705053752638... L`.                    (4.5)

Apply the previously completed original-coordinate theorem `QFORM-S3-VOLUME-OR-BILATERAL-STAR-v1` from account01/B08 r24 (`yspennstate/math-open-problems@a11ebd02f863b82324e449b4a31d468ec654f080`). At `q=1`, (4.5) implies either the full ambient quadratic form has a continuous `C_0` density with

`boxed: ||p_Q||_infinity < 87.902851345/L`,                     (4.6)

or the literal cross block has both a physical row star and a physical column star larger than

`boxed: 0.045943058496 L`.                                      (4.7)

At exact alignment `d=0`, the corresponding numbers improve to

`||p_Q||_infinity <43.951425673/L`

or bilateral stars `>0.091886116992 L`.

This does not contradict account02/B08's target-valid aligned examples: it says such a zero-angle model cannot remain inside this *particular balanced selected-three-eigenvector k=1 gate* with `s_2(C)<cL` and small `s_3(B)`.

## 5. Required application of the completed account02/B08 result

The completed account02/B08 r28 theorem `QFORM-K1-MACROSCOPIC-3FRAME-HALFCUT-v1` is now applied to an actual inequality, not merely cited.

The r30 energy ledger strengthens the partner's old cross floor to

`s_2(B)>delta L`,    `delta=3/sqrt(40)=0.4743416490252569...`.   (5.1)

Let `B_2=U Sigma V^T` be the top-two SVD and, when `d>0`, put

`q=(I-UU^T)r/d`,    `W=[q,U]`,
`nu=max_i ||W_{i,*}||^2`.                                       (5.2)

In the partner proof, the parameter called `beta` is used only through `s_2(Sigma)>=beta L`; therefore the proved equations (4.9)--(4.34) may be instantiated with the stronger actual value `beta=delta`. Take the partner reference blocks

`C_0=mu r r^T`,    `B_0=B_2`,

so the literal deterministic error is exactly controlled by

`||E_C||_op=s_2(C)`,    `||E_B||_op=s_3(B)`.                    (5.3)

For `d>=1/2`, define

`kappa_* = c delta (1/2)^2 / [2 sqrt(c^2(1/2)^2+4 delta^2)]
         =0.023717082451262847...`.                              (5.4)

Hence if

`nu<=1/48`

and

`sqrt(s_2(C)^2+s_3(B)^2)
 <= (kappa_*/16)L
 =0.001482317653203928... L`,                                   (5.5)

then the partner's literal-cross-block volume-stability receiver gives the full ambient form a continuous `C_0` density with

`boxed: ||p_Q||_infinity < 23/(kappa_* L)
                         <969.766/L.`                           (5.6)

This is a direct partner application preserving arbitrary outside couplings and within-bank phases.

If (5.5) fails while `nu<=1/48`, then either

`s_2(C)>0.00104815686445 L`                                     (5.7)

or

`s_3(B)>0.00104815686445 L`.                                    (5.8)

The latter can again be spent by the robust-`s_3` theorem, giving either a continuous density `<9437.84/L` or bilateral physical stars `>0.000427908248 L`. Thus, on the genuinely transverse (`d>=1/2`) and three-frame-diffuse (`nu<=1/48`) branch, the only unpaid output after these existing receivers is a genuine second child singular direction (5.7).

If `nu>1/48`, the output is instead an explicit localized physical row of the augmented child/cross three-frame; it is not silently declared paid.

### Orthogonal endpoint

When `d=1`, the partner's stronger Section 4.2 calculation may again use (5.1). Since `delta>c/2`, its reference cross block has

`s_3(M_0)>=cL/4=0.0968245836552...L`.

Therefore

`sqrt(s_2(C)^2+s_3(B)^2)<=cL/64
 =0.00605153647845...L`

implies a continuous `C_0` density with

`boxed: ||p_Q||_infinity <92/(cL)<237.543/L.`                   (5.9)

## 6. What remains after this run

The first B08 missing implication is now

`QFORM-K1-HIGH-AMPLIFICATION-NEAR-ALIGNMENT-COMPILER-v1`:

> In the balanced k=1 gate, control the survivor
> `0<d<1/2` and `|mu| rho d >(eta/2)L`, while preserving the full complementary spectrum and arbitrary same-bank curvature. The transverse branch is already routed by Section 5; the weighted-near-aligned branch is already routed by Section 4. Any use of a grouped-hub/projected-crossing theorem must verify its row-marginal and product-provenance gates on the actual physical partition.

The Section 5 transverse branch also leaves the explicit second-child currency (5.7) and the localized three-frame row `nu>1/48` for the existing child/star compilers. These are structural outputs, not claims of full density control.

The newest Claude `(SP)` proposal is relevant to a later single-hub realization of the localized branch but is still an open estimate and was not used. The new arbitrary-rank projected-crossing theorem was also read; its hypotheses do not automatically follow from the high-amplification near-aligned state, so it is not promoted to a closure statement.

## 7. Sanity checks

A deterministic-seed numerical checker sampled symmetric matrices with an explicitly selected three-eigenvector frame and arbitrary complementary spectrum (including occasional very large complementary eigenvalues), physical coordinate cuts, and verified (3.1). It also recomputed every displayed constant. The checker is only a finite sanity test; the proof of (3.1) is the exact argument in Section 3.

## 8. Status

- Full universal bounded-density conjecture: **OPEN**.
- Full-target continuous representative: **OPEN**.
- New theorem (3.1): exact deterministic supporting result.
- Continuous density: proved only on the paid branches (4.6), (5.6), (5.9), and the robust-`s_3` alternatives cited above.
- Native brain ingestion: **WITHOUT_VERIFIED_BRAIN**; GitHub retrieval/write is not native learned-memory ingestion.
