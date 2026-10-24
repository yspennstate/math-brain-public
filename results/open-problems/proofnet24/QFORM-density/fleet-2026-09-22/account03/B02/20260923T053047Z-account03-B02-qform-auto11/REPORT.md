SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B02, 2026-09-23T05:30:47Z.
attacking: the correction-safe true-Schur E2 branch left by r21: remove its 2/3 minor-marginal gate by feeding the unconditional pair-volume half-Riesz theorem into the indefinite-pair logarithmic receiver.

# account03/B02 QFORM auto11 — gate-free true-Schur E2 receiver

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Integrated Fourier estimate  
**Control at start:** brain `ededfb097f10d8ddcb0fe7555908ec9a8e00e5fa`, owner revision `2026-09-22.15`  
**Prepublication control refresh:** brain `bf8484488e0e489ec5a921ff4cf9dcfe2f87b2d3`, owner revision still `2026-09-22.15`  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`  
**Full QFORM target:** OPEN  
**Target-wide unweighted Fourier L1 criterion:** OPEN  
**Continuity:** not proved by the new pair receiver; only essential boundedness is claimed.

## 1. Exact target and correction boundary

The target remains: for every finite `n`, independent real ORIGINAL coordinates `X_i` with probability densities `0<=f_i<=1`, and every real symmetric matrix `A` having at least three eigenvalues of modulus at least one, prove that `Q=X^T A X` has a density with one universal finite essential-supremum bound, or give a valid counterexample. No moment, Gaussian, iid, compact-support, connected-support, log-concavity, sign, or spectral-coordinate-independence assumption is introduced.

The law-uniform scalar pointwise quadratic-phase decay remains false and is not used. The arbitrary-joint rank-three coarea lemma and positive conditional-projection-moment gates remain false and are not used. Every averaging step below retains literal original-coordinate product structure until an already proved product-preserving theorem is invoked.

The immediately preceding B02 report is

`yspennstate/math-open-problems@61ec1e9c84c7bd41323e0b87bfa84e45a828d81c`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260923T050329Z-account03-B02-qform-r21/REPORT.md`.

It proved the correction-safe rank-one repair between the cross-only anchored Schur packet and the TRUE physical-pair Schur packet. On failure of the q=4/3 third-volume marginal gate it obtained, for an anchor pair with cross coefficient `a`,

`max{ a^2 E2(T), correction_resource } > Z/12`,                    (1.1)

where `Z=E3(B)` is the physical cross-block third volume and `T` is the true residual cross block after completing the full physical pair. Its analytic payment of the first term required a residual E2 minor-marginal gate `<=2/3`. Removing that gate is the first implication attacked here.

## 2. Two completed inputs actually used

### 2.1 Unconditional pair-volume half-Riesz theorem

Account01/B01 proved `QFORM-PAIRVOLUME-HALF-RIESZ-UNCONDITIONAL-v1` at

`yspennstate/math-open-problems@1f3af9dc58afb9e902b972466d6da01cece89734`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B01/20260923T030821Z-account01-B01-qform-auto11/REPORT.md`.

For every quadratic-plus-affine residual `R` in independent cap-one ORIGINAL coordinates and every physical cross block `M` with

`Delta=E2(M)=e2(M^T M)>0`,

it proves, with arbitrary within-bank curvature and outside couplings retained,

`H_(1/2)(R):=sup_s E|R-s|^(-1/2)
 <= C_E2 Delta^(-1/8)`,                                           (2.1)

where

`C_E2 <= 12*2^(5/6)*e^(5/24)=26.334046180759735... .`            (2.2)

There is no leverage condition, no E2 minor-marginal condition and no selected-minor lower bound. The proof is an integrated-frequency argument: it aggregates the entire second compound before reciprocal payment and combines mixed determinant-order Fourier decay with random-slope Plancherel.

### 2.2 Indefinite physical-pair logarithmic envelope

The source-valid pair-log theorem is

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`,

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

Let `P` be an invertible indefinite `2x2` physical principal block, put

`D=|det P|`, `kappa=sigma_min(P)>0`,                               (2.3)

and after completing this physical pair write

`Q=((U,V)+m(Z))^T P ((U,V)+m(Z)) + R(Z)`,                          (2.4)

where `U,V` are the two independent original inputs and `Z` contains the remaining independent original coordinates. Then for every cutoff `rho>0` and almost every output `t`,

`p_Q(t)
 <= 2sqrt(2)/rho
   + D^(-1/2) E log_+(2rho^2/(kappa |t-R|)).`                     (2.5)

The shifts `m(Z)` may be arbitrarily dependent on `R(Z)`.

## 3. New bridge: half-Riesz residual directly smooths an indefinite pair

### Lemma 3.1 — `QFORM-PAIRLOG-HALFRIESZ-DIRECT-v1`

In the setup (2.3)-(2.5), suppose

`H:=sup_t E|R-t|^(-1/2)<infinity`.                                (3.1)

Then `Q` has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <= 4 sqrt(2/e) H^(1/2) (D kappa)^(-1/4).
}`                                                                  (3.2)

#### Proof

For every `y>=1`, elementary calculus gives

`log y <= (2/e) sqrt(y)`,                                          (3.3)

because `z e^(-z/2)` is maximized at `z=2`. Therefore, for `A,u>0`,

`log_+(A/u) <= (2/e) A^(1/2) u^(-1/2)`.                           (3.4)

Use `A=2rho^2/kappa` and `u=|t-R|` in (3.4), average, and apply (3.1):

`E log_+(2rho^2/(kappa|t-R|))
 <= (2sqrt(2)/e) rho kappa^(-1/2) H`.                             (3.5)

Insert (3.5) into (2.5):

`p_Q(t)
 <= 2sqrt(2)/rho
   +(2sqrt(2)/e) H (D kappa)^(-1/2) rho`.                         (3.6)

For positive `A0,B0`, `inf_(rho>0)(A0/rho+B0 rho)=2sqrt(A0B0)`. With

`A0=2sqrt(2)`,
`B0=(2sqrt(2)/e)H(Dkappa)^(-1/2)`,

this is exactly (3.2). QED.

This is stronger than first converting the half-Riesz estimate to a `sqrt(rho)` small-ball bound and then using the generic pair-log small-ball theorem; it uses the logarithm itself before losing information.

## 4. Main new theorem: gate-free true-Schur E2 receiver

### Theorem 4.1 — `QFORM-PAIR-TRUE-SCHUR-E2-UNCONDITIONAL-v1`

In (2.4), suppose the true Schur residual `R` contains disjoint original-coordinate banks whose physical cross block is `T` with

`Delta=E2(T)>0`.                                                   (4.1)

Then

`boxed:
 ||p_Q||_infinity
 <= C_pair (D kappa)^(-1/4) Delta^(-1/16),
}`                                                                  (4.2)

where

`C_pair=4 sqrt(2 C_E2/e)
 <=17.607047855003.`                                               (4.3)

There is **no E2 minor-marginal gate** in (4.2).

#### Proof

Apply the unconditional pair-volume theorem (2.1) to the literal physical cross block `T` inside the true Schur residual:

`H_(1/2)(R)<=C_E2 Delta^(-1/8)`.                                  (4.4)

Insert (4.4) into Lemma 3.1 and take the square root of its right side. This gives (4.2)-(4.3). All self curvature and affine leakage remain inside the scopes of the two completed source theorems. QED.

The theorem asserts essential boundedness. It does not assert that `phi_Q` is in `L1`, and it does not assert continuity.

## 5. Direct payment of the r21 concentrated-true-Schur branch

Retain the r21 q=4/3 third-volume setup. Let `Z=E3(B)>0` for the current physical cross block, and suppose both E3 marginal gates fail. The correction-safe compiler chooses physical anchors and, when `a!=0` and the anchor principal pair is invertible, gives (1.1).

Assume the pair is **indefinite** and the true-Schur term fires. Then

`a^2 Delta > Z/12`.                                                (5.1)

No matter how concentrated the squared `2x2` minor law of `T` is, Theorem 4.1 applies. From (5.1),

`Delta^(-1/16) < 12^(1/16)|a|^(1/8) Z^(-1/16)`.                   (5.2)

Hence

`boxed:
 ||p_Q||_infinity
 < C_gate |a|^(1/8)(D kappa)^(-1/4) Z^(-1/16),
}`                                                                  (5.3)

with

`C_gate=C_pair*12^(1/16)
 <=20.565315307531.`                                               (5.4)

This closes the **residual E2 concentration obstruction** listed as item 2 of r21 Section 10, on the invertible-indefinite physical-pair branch. The remaining difficulties are now elsewhere: the same-side correction packet, the singular physical-pair branch, and the structural control of tiny `D*kappa`/other overlap classes. No reciprocal individual `2x2` minor is paid.

For an invertible definite physical pair, the source pair-log report already records the elementary conditional ellipse bound `pi/sqrt(|det P|)`; the new theorem is specifically needed for the indefinite logarithmic pair.

## 6. Designated partner account04/B02 applied to an actual inequality

The designated partner theorem is `QFORM-ZERO-DIAGONAL-TRIPLE-CONTINUITY-v1`, source

`yspennstate/math-open-problems@0b11995430ce407a8852ac3bc5651491f2ee64f7`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B02/20260922T193108Z-account04-B02-QFORM-r2/REPORT.md`.

If the true Schur residual `R` contains a nonsingular physical `3x3` principal block `H0` with a zero diagonal entry, the partner gives the **continuous** residual density cap

`M_H=3*2^(2/3)|det H0|^(-1/3).`                                   (6.1)

For any probability density bounded by `M`, centered rearrangement gives the sharp elementary half-Riesz estimate

`sup_t int p(s)|s-t|^(-1/2) ds
 <= M int_(-1/(2M))^(1/(2M)) |u|^(-1/2)du
 =2sqrt(2M).`                                                      (6.2)

Thus the partner theorem yields an actual residual inequality

`H_(1/2)(R)
 <=2sqrt(2M_H).`                                                   (6.3)

Apply Lemma 3.1 to (6.3):

`boxed:
 ||p_Q||_infinity
 <= C_partner (D kappa)^(-1/4)|det H0|^(-1/12),
}`                                                                  (6.4)

where

`C_partner
 =4*3^(1/4)*2^(17/12)/sqrt(e)
 =8.524172398312... .`                                             (6.5)

This is a genuine equation-level use of the designated partner result. It is complementary to r21's earlier nested partner bound

`10.094557 D^(-1/6) kappa^(-1/3)|det H0|^(-1/9)`;                 (6.6)

neither power profile uniformly dominates the other. On the overlap one may take the minimum of (6.4) and (6.6). The partner residual itself is continuous; (6.4), after indefinite-pair smoothing, is recorded only as an essential-density bound.

## 7. Fourier status

The main new input (2.1) is itself an integrated-frequency/half-Riesz theorem and is exactly what removes the residual minor-marginal gate. But this run still has **no valid exact-target counterexample** to a universal unweighted

`int_R |E exp(it X^T A X)| dt`,

and it does not prove that criterion at full scope. The indefinite pair receiver converts finite half-Riesz Fourier information into a bounded density without establishing full `L1` Fourier inversion. The stronger target-wide Fourier criterion therefore remains OPEN rather than being declared false.

## 8. Remaining first implications

After this run, the r21 true-Schur E2 **minor-concentration** debt is paid on every invertible-indefinite pair. The sharp next B02 obligations are:

1. **same-side correction packet:** spend
   `(||a u-d c||^2 ||a v-e r||^2/delta^2) F^2`
   by a product-preserving mixed-slope/fractional-Fourier estimate;
2. **singular physical pair:** treat `a!=0, det P=0` without illegal inversion, likely through grouped-square/ridge geometry;
3. **aggregate structural closure:** route the remaining overlap-one/two/principal third-compound mass and tiny-`D*kappa` survivors into already paid diffuse/ridge/grouped-coordinate exits.

A full candidate theorem is **not** claimed. Full continuity is **not** claimed.

## 9. Constant verification

The constants were independently evaluated from the displayed exact formulas:

`C_E2 = 12*2^(5/6)*exp(5/24) = 26.334046180759735...`,

`C_pair = 4*sqrt(2*C_E2/e) = 17.607047855002474...`,

`C_gate = C_pair*12^(1/16) = 20.565315307530838...`,

`C_partner = 4*3^(1/4)*2^(17/12)/sqrt(e) = 8.524172398311938...`.

These numerical evaluations only check arithmetic; all mathematical inequalities are proved symbolically above.
