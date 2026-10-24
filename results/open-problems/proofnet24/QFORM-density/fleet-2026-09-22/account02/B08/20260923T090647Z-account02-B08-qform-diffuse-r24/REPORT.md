SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B08, 2026-09-23T09:06:47.163270Z.
attacking: choose a legitimate tiny fixed no-pivot gate, apply the newest account03/B08 crisscross theorem to eliminate its aligned double-nest branch, amplify the surviving determinant-core branch, and test the one-/two-child hybrid inside that same gate.

# account02/B08 r24 — tiny-N3 pruning of crisscross concentration and sharp hybrid survival

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control:** revision `2026-09-22.15`  
**Assignment:** diffuse eigenvector case / complementary constructions and source-valid counterexamples  
**Classification:** `NEW SUPPORTING STRUCTURAL THEOREM + QUANTITATIVE CORE AMPLIFICATION + TARGET-VALID HYBRID STRESS FAMILY / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and source pins

The target remains open: for arbitrary independent ORIGINAL coordinates with probability densities at most one and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal essential density bound for `X^TAX`, or give a valid counterexample. No moments, support regularity, log-concavity, post-rotation independence, pointwise law-uniform Fresnel decay, arbitrary-joint coarea, conditional-height moments, or single-good-minor principle is used.

The current full-to-N3 reduction is `math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371`, `proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/GEOMETRIC_SYNTHESIS.md`, Theorem 5.1. For every fixed `tau in (0,1]`, a universal density theorem for the no-`tau`-pivot class with three target-large eigenvalues implies the full conjecture. Hence one may choose a convenient fixed positive `tau`; making it small only worsens the eventual universal transfer constant, not the logical reduction.

The newest completed designated partner is account03/B08 r33, canonical source `math-open-problems@6f8e99aec5b12f0e3a5f13d60e7da490ce491647`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260923T090721Z-account03-B08-qform-diffuse-r33/REPORT.md`. It inherits from r31 the aligned double-nest certificate containing an ACTUAL physical cross coefficient

`|a| > L/(600 sqrt(3))`,                                      (1.1)

where `L>=1` is the selected-large-eigenvalue scale. It further pays one Dodgson child at the half-Riesz / `L^3` level and routes the other to calibrated ridge/coloop geometry. I use its actual coefficient (1.1) below rather than merely citing the branch labels.

The newest-Claude fixed source actually applied to an output inequality is `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`, Theorem F. For a diagonal-plus-rank-`r` actual spectral representation whose rank frame has row leverage at most `1/2`, it gives for `r>=3`

`||p_Q||_infinity <= [4r/(r-2)] (prod |lambda_j|)^(-1/r)`,       (1.2)

with a continuous `C_0` density; arbitrary cap-one product sources and affine terms are allowed.

I also retain the earlier B08 actual spectral gate, `math-open-problems@9fb59f9549a85af6173ade505fd53bc035c611ba`, which for selected-frame leverage at most `1/48` gives

`c_L=(L/2)sqrt(3/5)`, `beta_L=(3L/16)sqrt(3/5)`,               (1.3)

and, if a physical child has only `k<3` actual eigenvalues of modulus at least `c_L`, forces at least `3-k` singular values of the ACTUAL cross block above `beta_L`.

## 2. First unpaid implication, before the calculation

The previous proof tree still had two qualitatively different obstacles: concentrated high-third-volume descendants (large star / double nest / core) and the genuinely rank-deficient `k=1,2` child-cross hybrids. The question here is whether the latest account03/B08 aligned crisscross descendant is a genuine part of the single N3 statement, or only an artifact of working at a comparatively coarse no-pivot scale.

It is the latter. A sufficiently small but still fixed N3 gate eliminates the entire aligned crisscross descendant. The determinant-core sibling survives, but the same gate amplifies its residual Frobenius norm by more than three orders of magnitude. The `k=1,2` hybrid, however, survives even this tiny gate, so it remains a real structural debt.

## 3. Tiny no-pivot lemma and elimination of the aligned crisscross branch

Say `A` is no-`tau`-pivot when

`|A_ii|<tau`,                                                    (3.1)
`|A_ii A_jj-A_ij^2|<tau` for every `i!=j`.                     (3.2)

Then, exactly,

`A_ij^2 <= |A_ii A_jj|+|A_ii A_jj-A_ij^2| < tau^2+tau`,        (3.3)

hence

`|A_ij| < eps_tau := sqrt(tau+tau^2)`.                          (3.4)

The partner coefficient floor (1.1) is incompatible with (3.4) whenever

`tau+tau^2 < 1/(600^2*3)=1/1080000`.                            (3.5)

The exact positive endpoint is

`tau_cr = [sqrt(1+1/270000)-1]/2
        = 9.25925068617... * 10^(-7)`.                          (3.6)

Fix from now on the clean value

`boxed: tau_* = 1/4000000 = 2.5 * 10^(-7)`.                    (3.7)

Then

`eps_* = sqrt(tau_*+tau_*^2)
       = 0.000500000062499996...`,                              (3.8)

whereas

`1/(600sqrt(3))=0.000962250448649376...`.                       (3.9)

### Theorem 3.1 — `QFORM-N3-TINY-GATE-CRISSCROSS-EXCLUSION-v1`

Inside `N3(tau_*)`, no state in the r31/r33 **aligned double-nest** branch can occur at any target scale `L>=1`.

**Proof.** The r31/r33 branch contains an ACTUAL original-coordinate cross entry `a` satisfying (1.1), so `|a|>1/(600sqrt(3))`. But every off-diagonal entry of a no-`tau_*`-pivot matrix obeys (3.8), which is strictly smaller. Contradiction. No probability estimate and no spectral-coordinate conditioning is involved. QED.

Because Theorem 5.1 of the N3 synthesis permits any fixed `tau>0`, this is a legitimate pruning of the one no-pivot statement sufficient for the full conjecture; it is not a change of target.

This is also an actual use of the newest account03/B08 result: its physical coefficient certificate (not a rotated/SVD coefficient) is what makes the contradiction source-valid.

## 4. The surviving determinant-core sibling is quantitatively amplified

The r30 double-nested degree drop, immediately before the aligned branch, has

`D > L^6/16875`                                                  (4.1)

and the exhaustive alternative

`|det C| ||N||_F > sqrt(D)/2`                                   (4.2)

or the aligned branch just excluded. Here `C` is the actual `2x2` cross anchor and `N` the actual residual physical cross block.

In `N3(tau_*)`, every entry of `C` has modulus `<eps_*`, so

`|det C| < 2 eps_*^2 = 2(tau_*+tau_*^2)`.                       (4.3)

Since `sqrt(16875)=75sqrt(3)`, (4.1)-(4.3) force

`boxed:
 G:=||N||_F
 > L^3/[300sqrt(3)(tau_*+tau_*^2)]
 = 7698.00166469459... L^3.
`                                                                    (4.4)

Thus, after the tiny-N3 reduction, a no-large-star double-nest cannot terminate in a moderate residual core: it must carry enormous aggregate cross mass.

Feed (4.4) into the completed physical-core quadrichotomy already applied in account03/B08 r30. In its VOL branch,

`||p_Q||_infinity < (27e/2) G^(-1)
 < 4050 e sqrt(3)(tau_*+tau_*^2)L^(-3)
 = 0.00476705595590... L^(-3).`                                 (4.5)

In the remaining branches, the same input yields the explicit strengthened reserves

`R1: dist_F(N,rank<=1)<G/2`, with `G>7698.00166 L^3`;          (4.6)

`E2: E_2(N)>=3G^4/16 >6.58435555556*10^14 L^12`;              (4.7)

`matching reserve >=3G^4/256 >4.11522222222*10^13 L^12`;       (4.8)

`BICORE: one actual row and one actual column star each
 >sqrt(2/27)G >2095.13067973 L^3`.                              (4.9)

These are structural currencies, not yet universal `L^infinity` payments in the non-VOL branches. Their significance is that the r30/r31 concentration tree has become sharply one-sided inside the sufficient tiny-N3 problem: the aligned physical-pivot route is gone, and the surviving route has a huge actual residual core.

## 5. The genuine one-/two-child hybrid survives the tiny gate

The preceding pruning does **not** remove the actual spectral hybrid. Let `m=2^q`, let `U` be the first three normalized Sylvester-Hadamard columns, and for `k in {1,2}`, `0<delta<=1/10`, let `P=P_(k,delta)` have exactly `k` diagonal entries `1-delta` and the remaining `3-k` entries `1/5`. Define

`A_(m,k,delta)= [[ UPU^T,       U(I-P)U^T ],
                  [ U(I-P)U^T, UPU^T       ]]`.                (5.1)

Exactly as in the source-pinned r18 construction:

* on `(Uv,Uv)/sqrt(2)`, the three eigenvalues are exactly `1`;
* on `(Uv,-Uv)/sqrt(2)`, the eigenvalues are `1-2delta` in the first `k` directions and `-3/5` in the others;
* every remaining eigenvalue is zero.

Hence (5.1) has **exactly three** eigenvalues of modulus at least one. The selected three-frame has leverage `3/(2m)`. Each actual physical child has exactly `k` eigenvalues above `c_1=(1/2)sqrt(3/5)`, while the actual cross block has singular values `delta` in those `k` directions and `4/5` in the other `3-k` directions. Thus the gate count `k child directions + (3-k) cross directions` is exact, and the unused cross singular values can tend to zero.

Every entry of (5.1) has modulus at most `3/m`, so every physical principal `2x2` determinant has modulus at most `18/m^2`. For the explicit Hadamard order

`m=2^24=16777216`,                                              (5.2)

`3/m=1.78813934326*10^(-7)<tau_*`,
`18/m^2=6.39488462184*10^(-14)<tau_*`.                          (5.3)

Therefore this exact-three-large-eigenvalue, arbitrarily diffuse `k=1,2` hybrid lies **inside the same strict `N3(tau_*)` class**. Tiny-pivot pruning cannot erase it.

### Proposition 5.1 — `QFORM-N3-TINY-GATE-HYBRID-SHARPNESS-v1`

For each `k=1,2` and every `0<delta<=1/10`, (5.1) at `m=2^24` is a target-valid member of `N3(tau_*)`, has selected leverage `3/(2m)<1/48`, realizes exactly `k` actual child directions above `c_1`, exactly `3-k` cross singular directions above `beta_1`, and permits its other `k` cross singular values to tend to zero.

Thus the remaining hybrid is not a finite-pivot artifact and not removable by choosing the N3 gate smaller.

## 6. Required newest-Claude theorem applied to an actual inequality

The same stress family is **not** a QFORM counterexample. Its entire nonzero six-dimensional spectral range is diffuse: the six eigenvectors `(U;U)/sqrt(2)` and `(U;-U)/sqrt(2)` have full-range row leverage `3/m<1/2`.

Apply the completed `e5f71d79...` Theorem F, (1.2), with `r=6`. The product of the six nonzero eigenvalue magnitudes is

`(1-2delta)^k (3/5)^(3-k)
 >=(4/5)^k(3/5)^(3-k)`.                                        (6.1)

Hence, for **every** independent cap-one product input law,

`boxed:
 ||p_(X^T A_(m,k,delta) X)||_infinity
 <=6[(4/5)^k(3/5)^(3-k)]^(-1/6).
`                                                                    (6.2)

Numerically,

`k=1: ||p||_infinity <=7.38333378529...`,                       (6.3)
`k=2: ||p||_infinity <=7.03767779409...`.                       (6.4)

The density is continuous and vanishes at infinity by the theorem's integrable characteristic-function bound. This is an actual inequality on a target-valid tiny-N3 hybrid, not a heuristic or a rotated-independence argument.

The diagnosis is therefore precise: the exact hybrid is easy when the **whole six-dimensional nonzero spectral range** is diffuse. The open arbitrary-matrix case is the stability of a mixed child-cross payment under an unrestricted complementary spectral remainder; that remainder cannot simply be deleted, diagonalized while retaining product structure, or treated as a uniformly small random perturbation.

## 7. Updated proof tree and first unpaid implication

Within the sufficient fixed class `N3(tau_*)`:

1. the newest partner's aligned crisscross/Dodgson descendant is impossible by Theorem 3.1;
2. the determinant-times-core sibling has the amplified floor (4.4), with its VOL subbranch already bounded by (4.5) and only R1/E2/BICORE-type rigid descendants remaining;
3. large physical-star descendants remain possible because many individually tiny entries can have large Euclidean norm;
4. the actual spectral `k=1,2` low-rank cross tubes remain unavoidable by Proposition 5.1.

The first unpaid implication is now

**`QFORM-N3-TINY-GATE-HYBRID-CORE-RECEIVER-v1` — OPEN.**  
In `N3(tau_*)`, obtain a full ambient `L^infinity` payment for either (a) the amplified determinant-core R1/E2/BICORE descendants, or (b) the `k=1,2` actual child-plus-low-rank-cross tubes, while retaining arbitrary same-bank curvature, all complementary spectrum, and the original-coordinate product law. The Hadamard witnesses show the correct compiler must reduce to the whole-range Fresnel payment when the complementary range is itself diffuse, but it cannot assume such a representation for arbitrary `A`.

This is narrower than the preceding aligned-double-nest debt and preserves every live correction. The unrestricted conjecture and global continuity remain OPEN.

## 8. Verification

`CHECKS.py` and `CHECKS.txt` beside this report verify the exact tiny-N3 inequality, the critical `tau` root, the `m=2^24` no-pivot inequalities, the spectral-gate constants, the amplified residual-core constants, and the two Theorem-F bounds. The executed output terminates `QFORM_B08_R24_CHECK_PASS`.

Repository transport is not native learned-memory ingestion. No FEI, installation, benchmark, task/schedule, notification/email, permission, paid-call, remote-workflow, cross-account-authentication, or public-release mutation is part of this result.
