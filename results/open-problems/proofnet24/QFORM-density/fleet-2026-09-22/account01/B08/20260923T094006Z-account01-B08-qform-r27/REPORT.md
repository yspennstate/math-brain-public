SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B08, 2026-09-23T09:40:06.130900Z.
attacking: a wide two-eigenvalue diffuse half-Riesz window, then apply it to the account02/B08 one-/two-child hybrid and convert failure into a genuine physical child star.

# account01/B08 r27 — wide two-eigenvalue half-Riesz window and mixed-hybrid router

Programme `QFORM-DENSITY-3EIG-20260922`; OWNER CONTROL revision `2026-09-22.15`.

Status: **ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_ANALYTIC THEOREM / DESIGNATED PARTNER APPLIED / FULL TARGET OPEN**.

Execution label: **WITHOUT_VERIFIED_BRAIN**. Repository retrieval was used; no claim of native learned-memory ingestion is made.

The unrestricted conjecture remains OPEN. The additional full-target continuity conclusion remains OPEN. The new density corollary below establishes essential boundedness in its stated scalar-pivot/diffuse-Schur scope; continuity is not claimed there.

## 1. Exact scope and source-pinned inputs

The target is the owner target: independent ORIGINAL real coordinates with marginal probability densities at most one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. No Gaussianity, moment assumption, log-concavity, compact/connected support, post-rotation independence, arbitrary-joint coarea bound, conditional projection-height moment, law-uniform pointwise Fresnel decay, or random-smallness consequence of a small spectral tail is used.

The current control and live correction ledger were reread on fresh `yspennstate/math-research-brain/main`. The full conjecture and continuity claim remain open there.

The first analytic input is the completed translation-uniform two-cross theorem

`yspennstate/math-open-problems@ad7e5daa036cc8330b1432285ad40fec611d37dd`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260922T184648Z-account03-B09-QFORM-r15/REPORT.md`,
Theorem `QFORM-HALFRIESZ-TWO-CROSS-v1`.

For any full quadratic-affine form in a cap-one original-coordinate product law, if some physical cross block `B` has two singular values `s_1(B),s_2(B)>0`, then

`H_{1/2}(Q):=sup_t E|Q-t|^{-1/2}
 <= 8 [s_1(B)s_2(B)]^{-1/4}.`                                      (1.1)

All same-side quadratic blocks, affine terms, outside couplings and extra spectrum are retained.

The frame-partition calculation is the same one used in my preceding completed r26 report,

`yspennstate/math-open-problems@c9113f2c63b8a57b3a3b6c1c8ad3772258f802fc`,
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B08/20260923T091119Z-account01-B08-qform-r26/REPORT.md`.

For a Parseval frame with row norms squared at most `delta`, the two-part MSS partition supplies physical banks `I,J` whose Gram matrices are both bounded below by

`g(delta) I`, where
`g(delta)=1/2-delta-sqrt(2 delta)`.                                (1.2)

The scalar-pivot density lift and large-eigenvalue inheritance are source-pinned in the completed Fresnel/Schur package

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.

After completing a nonzero original-coordinate scalar pivot `a`, the Schur remainder retains at least two eigenvalues of modulus at least one when the ambient matrix has three; and

`||p_Q||_infinity <= |a|^{-1/2} H_{1/2}(R)`.                    (1.3)

The designated partner actually applied in Section 5 is the newest completed account02/B08 result

`yspennstate/math-open-problems@40f8dac6ff53147322d492a56ffd8f382a5dce83`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/20260923T090647Z-account02-B08-qform-diffuse-r24/REPORT.md`.

Its inherited selected-three diffuse gate uses

`c_L=(L/2)sqrt(3/5)`, `beta_L=(3L/16)sqrt(3/5)`,               (1.4)

and says: if selected-three leverage is at most `1/48` and a physical child has only `k<3` eigenvalues of modulus at least `c_L`, the actual child/complement cross block has at least `3-k` singular values at least `beta_L`. Its same report fixes the sufficient tiny no-pivot class `N3(tau_*)` with

`tau_*=1/4000000`.                                                (1.5)

## 2. Main theorem: a wide two-eigenvalue diffuse window

Let `S=S^T` have at least two eigenvalues of modulus at least `L>0`. Fix `0<kappa<1`. Let

`P=P_{|S|>=kappa L}`, `delta=max_i P_ii`,                       (2.1)

where the projection includes every eigenspace of `S` with eigenvalue magnitude at least `kappa L`. Put

`g=1/2-delta-sqrt(2 delta)`.                                     (2.2)

### Theorem 2.1 — `QFORM-WIDE-TWOEIG-HALFRIESZ-v1`

If

`g>kappa`,                                                        (2.3)

then for every independent cap-one original-coordinate product input, and every affine perturbation,

`F(Y)=Y^T S Y+b^T Y+c`

satisfies

`boxed:
 H_{1/2}(F)
 <= 8 [(g-kappa)L]^(-1/2).
`                                                                    (2.4)

Consequently

`P{|F-t|<=epsilon}
 <= 8 [(g-kappa)L]^(-1/2) sqrt(epsilon)`                         (2.5)

for every `t` and `epsilon>0`.

No condition is imposed on the signs, number, or orientation of the remaining eigenvalues.

### Proof

Write the true spectral split

`S=S_H+E`, `S_H=U Lambda U^T`,                                   (2.6)

where the columns of `U` span `P`. Then

`U^T U=I`, `||u_i||^2=P_ii<=delta`, `||E||<kappa L`,             (2.7)

and, because the original matrix has at least two eigenvalues of modulus at least `L`,

`s_2(Lambda)>=L`.                                                 (2.8)

Apply the two-part MSS frame partition to the rows of `U`. There is a partition of the ORIGINAL coordinates into `I union J` such that

`G_I=U_I^T U_I >= g I`,
`G_J=U_J^T U_J >= g I`.                                         (2.9)

The assumption `g>kappa>0` makes both Grams invertible. Put

`V_I=U_I G_I^{-1/2}`, `V_J=U_J G_J^{-1/2}`.                     (2.10)

Both `V_I,V_J` have orthonormal columns. For the high-window physical cross block,

`B_0=(S_H)[I,J]
    =V_I [G_I^{1/2} Lambda G_J^{1/2}] V_J^T`.                   (2.11)

Hence its nonzero singular values are exactly those of the square middle matrix. The standard singular-value inequality gives

`s_2(B_0)
 >= s_min(G_I^{1/2}) s_2(Lambda) s_min(G_J^{1/2})
 >= g L`.                                                        (2.12)

The full physical cross block is

`B=S[I,J]=B_0+E[I,J]`.                                           (2.13)

Compression does not increase operator norm, so `||E[I,J]||<kappa L`. Weyl's singular-value inequality therefore gives

`s_2(B) >= (g-kappa)L`.                                          (2.14)

In particular `s_1(B)>=s_2(B)`. Applying (1.1) to the FULL quadratic-affine form, not to a spectrally truncated random form, gives

`H_{1/2}(F)
 <=8[s_1(B)s_2(B)]^{-1/4}
 <=8[(g-kappa)L]^(-1/2)`.                                       (2.15)

This is (2.4). The small-ball estimate follows from

`1{|x|<=epsilon} <= sqrt(epsilon)|x|^{-1/2}`.

The low spectral tail was never deleted probabilistically; it remains inside the actual physical cross block through (2.13). QED.

## 3. Quantitative leverage range

At fixed `kappa`, condition (2.3) is equivalent to

`delta < delta_*(kappa)
 := (sqrt(2(1-kappa))-1)^2/2`.                                  (3.1)

For `kappa=1/1000`,

`delta_*(1/1000)=0.0854937212732304...`.                         (3.2)

Thus this two-eigenvalue fractional-potential mechanism works almost up to leverage `0.0855`. This is a mechanism threshold, not a full-target threshold.

A clean rational point is

`delta=17/200=0.085`, `kappa=1/1000`.                            (3.3)

Then

`g-kappa
 =207/500-sqrt(17)/10
 =0.00168943743823391...`.                                       (3.4)

The exact rational comparison

`(10(207/500-64/38025))^2-17
 =3020989/5783602500 >0`                                         (3.5)

shows

`g-kappa > (8/195)^2`.

Therefore:

### Corollary 3.1 — `QFORM-TWOEIG-WINDOW085-HALFRIESZ-v1`

If `S` has two eigenvalues of modulus at least `L` and

`max_i (P_{|S|>=L/1000})_ii <=17/200`,                          (3.6)

then

`boxed:
 H_{1/2}(Y^T S Y+b^T Y+c)
 <195 L^{-1/2}.
`                                                                    (3.7)

The exact numerical bound from (2.4) is `194.634099447... L^{-1/2}`.

This strictly enlarges the earlier convenient two-eigenvalue half-Riesz spectral-window scope `delta<=1/32`; the price is a larger but still universal constant.

## 4. Target-level scalar-pivot compiler

Suppose the ambient target matrix `A` has at least three eigenvalues of modulus at least one and some ORIGINAL coordinate has nonzero scalar pivot

`a=A_ii !=0`.                                                     (4.1)

Complete that physical square:

`Q=a(X_i+m(Y))^2+R(Y)`,                                          (4.2)

where the quadratic matrix `S` of `R` is the scalar Schur complement and all induced linear terms are retained.

The completed Schur-inheritance lemma gives at least two eigenvalues of `S` of modulus at least one. Hence, if

`max_j (P_{|S|>=1/1000})_jj <=17/200`,                           (4.3)

Corollary 3.1 and the square peel (1.3) give

`boxed:
 ||p_Q||_infinity
 <195 |a|^{-1/2}.
`                                                                    (4.4)

This establishes an essentially bounded density. I do **not** claim continuity from this half-Riesz/square-peel endpoint.

At the partner's convenient fixed scale `tau_*=1/4000000`, any such scalar pivot with `|a|>=tau_*` is therefore paid by

`||p_Q||_infinity <390000`                                       (4.5)

whenever its Schur residual satisfies (4.3). The remaining scalar-pivot debt is thus pushed into a genuinely localized Schur-window coordinate with leverage `>0.085`.

## 5. Designated account02/B08 result applied to actual inequalities

Now apply account02/B08 r24's selected-three diffuse child/cross gate (1.4), rather than merely citing it.

### k=1 hybrid

If the physical child has only one eigenvalue of modulus at least `c_L`, the partner gate supplies at least two singular values of the ACTUAL child/complement cross block at least

`beta_L=(3/16)sqrt(3/5)L`.                                       (5.1)

Apply the completed two-cross theorem (1.1) directly to the full ambient form:

`H_{1/2}(Q)
 <=8 beta_L^{-1/2}
 =20.9918898268... L^{-1/2}
 <21 L^{-1/2}.`                                                  (5.2)

All same-bank curvature and complementary spectrum are retained.

### k=2 hybrid

If the physical child `C` has two eigenvalues of modulus at least

`c_L=(1/2)sqrt(3/5)L`,                                           (5.3)

condition every ORIGINAL coordinate outside that child. The conditional form on the child bank has quadratic part `C` and an arbitrary affine term, exactly the scope of Theorem 2.1.

Let

`P_C=P_{|C|>=c_L/1000}`.                                         (5.4)

If

`max_i (P_C)_ii <=17/200`,                                       (5.5)

then (3.7), uniformly in all conditioning values, yields

`H_{1/2}(Q)
 <195 c_L^{-1/2}
 =313.337083388... L^{-1/2}
 <314 L^{-1/2}.`                                                 (5.6)

Thus the genuine `k=2` child-plus-one-cross hybrid no longer needs a new diffuse fractional-potential theorem: its diffuse-child half-Riesz currency is already paid.

### If the k=2 child window is not diffuse inside N3(tau_*)

Assume in addition the partner's tiny no-pivot class `N3(tau_*)`, so every physical diagonal satisfies `|C_ii|<tau_*`, with `tau_*=1/4000000`.

If (5.5) fails, choose an ORIGINAL child coordinate `i` with `(P_C)_ii>17/200`. Spectrally,

`||C e_i||_2^2
 =e_i^T C^2 e_i
 >= (c_L/1000)^2 (P_C)_ii
 > (17/200)(c_L/1000)^2.`                                       (5.7)

Subtracting the physical diagonal and using `L>=1` gives

`||C[i,-i]||_2^2
 > L^2[(17/200)(1/1000)^2(3/20)-tau_*^2].`                      (5.8)

The coefficient is exactly

`203999/16000000000000 > 1/9000^2`.                             (5.9)

Hence

`boxed:
 ||C[i,-i]||_2 > L/9000.
`                                                                    (5.10)

This is a genuine original-coordinate child star, not a rotated-coordinate statement.

Combining (5.2), (5.6), and (5.10) gives the new router:

### Theorem 5.1 — `QFORM-N3-K12-HYBRID-HALFRIESZ-OR-STAR-v1`

Inside the account02/B08 selected-three diffuse gate (leverage `<=1/48`) and `N3(tau_*)`, the mixed `k=1,2` child/cross states satisfy:

* `k=1`: the full form has `H_{1/2}(Q)<21 L^{-1/2}`;
* `k=2`: either the full form has `H_{1/2}(Q)<314 L^{-1/2}`, or the actual child contains an original-coordinate off-diagonal row star of norm `>L/9000`.

This is a direct application of the designated partner's completed structural result to actual analytic inequalities.

## 6. Check on the partner's exact Hadamard stress family

Account02/B08 r24 also gives a target-valid tiny-N3 family with `m=2^24`.

For its `k=1` member, the actual cross singular values include two copies of `4/5`, so (1.1) gives the literal full-form inequality

`H_{1/2}(Q) <=8/sqrt(4/5)=4sqrt(5)
 =8.94427191...`.                                                 (6.1)

For its `k=2` member, the child has two eigenvalues at least `9/10`, while its high-window projector is `UU^T` with maximum diagonal exactly `3/m`. Theorem 2.1 with `L=9/10`, `kappa=1/1000`, `delta=3/m` gives, after conditioning the opposite bank,

`H_{1/2}(Q) <11.944802`.                                         (6.2)

These do not replace the partner's stronger whole-range bounded-density estimates for this special family; they verify that the new mixed fractional receiver behaves correctly on the exact stress configuration.

## 7. What is actually new and what remains

The proved advance is not a full density theorem for every mixed hybrid. It is a product-preserving bridge:

1. a two-large-eigenvalue principal child can be **much less diffuse** than the previous `1/32` window and still supplies a universal translation-uniform half-Riesz bound;
2. in the partner's `k=1` mixed state the robust two-cross directions already supply the same kind of half-Riesz currency;
3. in the partner's `k=2` state, failure of that diffuse fractional payment becomes a concrete physical child star `>L/9000` inside the sufficient tiny-N3 problem.

The first unpaid implication is therefore narrowed to

**`QFORM-N3-HALFRIESZ-PLUS-STAR-LINF-COMPILER-v1` — OPEN.**

Inside the tiny-N3 proof tree, convert either the paid mixed-state half-Riesz currency or the `>L/9000` physical child star, together with the remaining third global spectral direction / determinant-core reserves, into a full ambient `L^infinity` density estimate while retaining arbitrary complementary spectrum and original-coordinate product provenance.

A scalar physical square of fixed size already performs this lift by Section 4; the hard no-pivot branch lacks such a fixed-size scalar square. No claim to have solved that final compiler is made.

## 8. Verification and integrity

`CHECKS.py` and its executed output `CHECKS.txt` beside this report verify:
* the exact rational certificate for the clean `17/200` leverage point;
* the fixed-`kappa` leverage threshold;
* the partner `k=1` and `k=2` constants;
* the exact `N3(tau_*)` physical-star coefficient;
* the two exact stress-family half-Riesz constants.

The checker is a constant/algebra sanity check, not the proof.

Changed-file scope is limited to this worker's immutable math bundle and authorized B08 run/handoff/memory records. A narrow manual secret/privacy scan found only mathematical constants, repository source pins and nonsecret run metadata. No scheduler state, cadence, task identity, notification/email setting, permission, public release, installation, remote workflow, or paid model/API setting is changed.
