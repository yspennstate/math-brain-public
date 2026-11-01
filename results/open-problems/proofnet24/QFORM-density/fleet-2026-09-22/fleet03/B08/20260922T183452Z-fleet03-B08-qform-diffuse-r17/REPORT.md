# fleet03/B08 — tunable fine-scale ridge closure and near-coloop pair currency

**Run:** `20260922T183452Z-fleet03-B08-qform-diffuse-r17`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control used at start:** revision `2026-09-22.11`  
**Assignment:** Diffuse eigenvector case  
**Classification:** `PROVED SUPPORTING THEOREM / TUNABLE DIFFUSE-TO-NEAR-COLOOP REDUCTION / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and source discipline

The target remains the unrestricted statement: for every dimension, independent real coordinates with probability densities bounded by one, and every real symmetric matrix `A` with at least three eigenvalues of absolute value at least one, prove that `Q=X^T A X` has a density with one universal finite essential-supremum bound, or give a valid counterexample. No moment, Gaussian, log-concavity, compact-support, connected-support, or diagonal-basis hypothesis is added. Continuity is recorded separately from essential boundedness.

This run does **not** use the owner-message claims that an arbitrary bounded three-dimensional joint density obeys a rank-three coarea bound, or that worst conditioning on the scalar `Q_rest` is uniformly controlled. The live research state has source-valid counterexamples to both interfaces. It also does not use law-uniform pointwise quadratic-phase decay, independence after spectral rotation, or a reciprocal bound from one selected tiny minor.

The mathematical input from the preceding B08 run is the exact O0 transverse reserve. In the O0 cross-block calibration there is a scale `gamma>0`; after selecting one original physical row and making the arbitrary scalar Schur shear produced by completing the square in its physical coordinate, the actual residual cross block `H` has singular values `h_j` for which

`x_j := min(1,h_j^2/gamma^2)`

satisfy

`0<=x_j<=1`, `e_2(x)>=2/3`.                                    (1.1)

This is the shear-invariant content of `QFORM-TRANSVERSE-5/6-RIDGE-CLOSURE-v1`, canonical source

`yspennstate/math-open-problems@0e80922c4f26f72fe3bb2b06728dd7a40da0c765`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B08/20260922T174745Z-fleet03-B08-qform-diffuse-r15/REPORT.md`.

The preceding theorem used only the single scale `gamma/4`, obtaining ridge trace `>=16/9` and a `5/6` row-leverage gate. The present run changes the quantitative mechanism: it proves a **tunable all-scales consequence** of the same exterior two-volume reserve and then extracts a nearly-coloop alternative with a new aggregate two-row currency.

## 2. Tunable scalar lemma

### Lemma 2.1 — `QFORM-E2-TO-TUNABLE-RIDGE-v1`

Let finitely many numbers `x_j` satisfy `0<=x_j<=1` and

`e_2(x)=sum_{j<k} x_j x_k >=2/3`.                               (2.1)

Then for every `tau>0`,

`boxed( sum_j x_j/(tau^2+x_j) >= 2/(1+2 tau^2). )`              (2.2)

### Proof

Put `G={j:x_j>=1/2}`, `m=|G|`, and `T=sum_{j notin G}x_j`.

For `x>=1/2`,

`x/(tau^2+x) >= (1/2)/(tau^2+1/2)=1/(1+2tau^2)`.               (2.3)

For `0<=x<1/2`,

`x/(tau^2+x) >= x/(tau^2+1/2)=2x/(1+2tau^2)`.                  (2.4)

If `m>=2`, two terms from (2.3) give (2.2).

If `m=0`, then `e_2(x)<=T^2/2`, hence `T>=2/sqrt(3)>1`; by (2.4),

`sum_j x_j/(tau^2+x_j) >= 2T/(1+2tau^2)>2/(1+2tau^2)`.         (2.5)

If `m=1`, write the large coordinate as `x_*`. Since `x_*<=1` and the small-small pair sum is at most `T^2/2`,

`e_2(x)<=x_*T+T^2/2<=T+T^2/2`.                                 (2.6)

If `T<1/2`, the right side is `<1/2+1/8=5/8<2/3`, contradicting (2.1). Thus `T>=1/2`; (2.3)-(2.4) give

`sum_j x_j/(tau^2+x_j)
 >=1/(1+2tau^2)+2(1/2)/(1+2tau^2)
 =2/(1+2tau^2)`.

This proves the lemma. QED.

The previous `16/9` estimate is exactly the special case `tau=1/4`.

## 3. Shear-invariant tunable ridge trace

For `g=tau gamma`, define the residual row ridge kernel

`K_g(H)=H H^T (g^2 I+H H^T)^(-1)`

and its effective dimension

`theta_g(H)=tr K_g(H)=sum_j h_j^2/(g^2+h_j^2)`.                 (3.1)

Write `u_j=h_j^2/gamma^2`. Since `u_j>=x_j` and the map `u -> u/(tau^2+u)` is increasing,

`theta_(tau gamma)(H)
 =sum_j u_j/(tau^2+u_j)
 >=sum_j x_j/(tau^2+x_j)
 >=2/(1+2tau^2)`.                                                (3.2)

### Theorem 3.1 — `QFORM-SHEAR-INVARIANT-TUNABLE-RIDGE-v1`

In the calibrated O0 setup of the preceding B08 result, after **every** scalar Schur shear through the selected physical row and for every `tau>0`,

`boxed( theta_(tau gamma)(H) >= 2/(1+2tau^2). )`                (3.3)

Thus the guaranteed residual ridge dimension approaches two from below as the ridge scale is decreased, uniformly over the arbitrary Schur shear and without any moment or spectral-tail assumption.

A useful abstract corollary is this. Fix any `delta in (0,1/2)`. Choose `tau` so that

`tau^2 < delta/[2(1-delta)]`.                                   (3.4)

Then

`2(1-delta)<2/(1+2tau^2)<=theta_(tau gamma)(H)`.                (3.5)

Consequently the fractional ridge theorem can be run with any `q` strictly between `2(1-delta)` and the right side of (3.5). Its physical-row gate `max diag K<=q/2` can therefore be placed arbitrarily close to one, at the price of a worse but finite constant. This is a structural reduction, not a claim that the fine-scale leverage is smaller than the coarse-scale leverage; the fine-scale kernel is larger. Combined with the preceding `gamma/4` result, it says a previously unpaid coarse-heavy case can be pushed into a genuinely near-coloop fine-scale alternative.

## 4. Explicit 99-percent closure

Take

`tau=1/16`, `g=gamma/16`.                                       (4.1)

Theorem 3.1 gives

`theta_g(H)>=2/(1+2/256)=256/129`.                              (4.2)

Assume the selected physical scalar pivot is nonzero,

`a=A_ii !=0`,                                                    (4.3)

and the fine-scale residual row ridge leverage satisfies

`max_j (K_g(H))_jj <=99/100`.                                   (4.4)

Choose in the completed fractional ridge theorem

`q=99/50`, `s=999/500`, `p=s/(s-1)=999/499>2`.                 (4.5)

Condition (4.4) is exactly `max diag K_g<=q/2`. From (4.2),

`beta:=theta_g(H)/(2q)>=6400/12771`,                            (4.6)

and therefore

`beta s >=2368/2365>1`.                                        (4.7)

The ridge theorem gives a residual characteristic-function envelope

`|phi_R(t)| <= min(1,(t0/|t|)^beta)`                            (4.8)

with, after the standard determinant simplification used in the source theorem,

`t0 <= pi sqrt(2e/q)/(2g)
    =80 pi sqrt(e/99)/gamma`.                                   (4.9)

Since `x/(x-1)` decreases for `x>1`, (4.7) implies

`int_R |phi_R(t)|^s dt
 <=2 t0 * (beta s)/(beta s-1)
 <=(4736/3)t0`.                                                  (4.10)

Inverse Hausdorff-Young gives an `L^p` density for the residual:

`||p_R||_p <=(2pi)^(-1/s)(int |phi_R|^s)^(1/s)`.                (4.11)

Completing the square in the **original physical coordinate** gives

`Q=R+aV^2`,                                                      (4.12)

where, conditional on the residual variables and then on `R`, the variable `V` is a mixture of translations of the original independent coordinate law, hence retains conditional density at most one. No rotated independence is asserted.

The same elementary dependence-safe `L^p` Abel estimate as in the preceding B08 run states

`||p_Q||_infinity
 <=|a|^(-1/2)
   [(1-s/2)^(-1/s)+1]
   ||p_R||_p^(s/2)`.                                             (4.13)

Here `1-s/2=1/1000`. Combining (4.9)-(4.13) gives

`boxed(
 ||p_Q||_infinity
 <= C_99/sqrt(|a| gamma),

 C_99
 =(1000^(500/999)+1)
   sqrt[(189440/3) sqrt(e/99)]
 <3349.
)`                                                               (4.14)

### Theorem 4.1 — `QFORM-TRANSVERSE-99PCT-RIDGE-CLOSURE-v1`

Under the exact O0 transverse hypotheses inherited from the preceding B08 result, every nonzero-pivot branch satisfying the fine-scale gate (4.4) is absolutely continuous and has the essential-density bound (4.14).

This theorem does **not** claim a continuous representative: the final `L^p`-plus-square step yields absolute continuity and `L^infinity`, not continuity. It also does not by itself remove the factor `(|a|gamma)^(-1/2)`; the zero/near-zero-pivot problem remains a separate full-target debt.

Relative to the preceding B08 state, combine rather than replace the two tests. A branch that was not paid at scale `gamma/4` had residual leverage `>5/6` there. The new theorem pays it whenever the finer `gamma/16` kernel still has maximum row leverage `<=99/100`. Hence an unclosed quantitatively nonzero-pivot O0 case must now be genuinely nearly coordinate-localized at the fine scale.

## 5. New currency in the surviving near-coloop branch

Suppose (4.4) fails. Choose a residual physical row `j` with

`ell:=K_jj>99/100`,                                              (5.1)

where now `K=K_(gamma/16)(H)`. By (4.2), `theta=tr K>=256/129`.

Because `K` is a positive semidefinite contraction, `K^2<=K`. For the sum of all two-row principal determinants involving row `j`,

`sum_{k != j} det K[{j,k}]
 =sum_{k!=j}(K_jj K_kk-K_jk^2)
 =ell theta-(K^2)_jj
 >=ell(theta-1)`.                                                (5.2)

Using (5.1)-(4.2),

`boxed(
 sum_{k != j} det K[{j,k}] >
 (99/100)(127/129)=4191/4300.
)`                                                               (5.3)

This is a very strong aggregate pair reserve: the one almost-coloop row carries more than `0.97465` units of normalized two-row ridge volume with the remaining physical coordinates.

To translate (5.3) back to the actual original-coordinate cross block, put

`R_g=(g^2 I+H^T H)^(-1/2)`, `Z=H R_g`, so `K=ZZ^T`.             (5.4)

For every pair of residual physical rows,

`det K[{j,k}]=||z_j wedge z_k||^2
 <=||R_g||_op^4 ||h_j wedge h_k||^2
 <=g^(-4) det Gram(h_j,h_k)`.                                   (5.5)

Therefore, with `g=gamma/16`,

`boxed(
 sum_{k!=j} det Gram(h_j,h_k)
 > (4191/4300)(gamma/16)^4
 = (4191/281804800) gamma^4.
)`                                                               (5.6)

By Cauchy-Binet this is equivalently

`boxed(
 sum_{k!=j} sum_{r<s}
   det H[{j,k},{r,s}]^2
 > (4191/281804800) gamma^4.
)`                                                               (5.7)

Crucially, this aggregate is **exactly invariant under a second scalar Schur shear through row `j`**: replacing any row `h_k` by `h_k-d_k h_j` leaves

`h_j wedge (h_k-d_k h_j)=h_j wedge h_k`.                        (5.8)

### Theorem 5.1 — `QFORM-99PCT-NEAR-COLOOP-PAIR-CURRENCY-v1`

The only fine-scale residual alternative not paid by Theorem 4.1 carries the dimension-free, shear-invariant aggregate two-row currency (5.6)-(5.7). Thus the next localized-coordinate step does not start from one uncontrolled tiny minor; it starts from an almost-coloop physical row plus a fixed total amount of transverse two-volume spread across all other rows and all column pairs.

This interfaces directly with the newest fleet03/B07 two-row skeleton identity, which retains aggregate third-volume currency instead of choosing one reciprocal minor. The B07 r14 handoff records

`sum_{S superset J, |S|=3} det(B_S B_S^T)
 =det(B_J B_J^T)e_(3-|J|)(C_J C_J^T)` for `|J|=1,2`,             (5.9)

and identifies the nested-heavy/near-coloop branch as the current O0 obstruction. The present theorem supplies an independent fine-scale quantitative certificate for precisely that obstruction.

## 6. Compatible fleet04 mathematics applied

The designated current-QFORM partner path `fleet04/B08` was absent at the fresh source checks, so no partner theorem is fabricated. A completed compatible fleet04 result is nevertheless applied to the same scalar-pivot geometry: fleet04/B18 `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`, canonical source

`yspennstate/math-open-problems@0e80922c4f26f72fe3bb2b06728dd7a40da0c765`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T113729Z-fleet04-B18-qform-r1/REPORT.md`.

For any residual branch at any ridge scale `h` on which the completed ridge theorem yields an actual density cap

`M <= [sqrt(e)/(sqrt(2)h)] * theta/(theta-2)`                    (6.1)

under `max diag K_h<=1/2` and `theta=tr K_h>2`, the fleet04 theorem applies after the same original-coordinate square completion (4.12) and gives the concrete full-form inequality

`boxed(
 ||p_Q||_infinity
 <=2 [ sqrt(e)/(sqrt(2)|a|h) * theta/(theta-2) ]^(1/2).
)`                                                               (6.2)

The use is dependence-safe: after conditioning on `R`, the completed-square coordinate is only a mixture of translations of its original density, so the conditional density cap one required by fleet04/B18 is preserved. Equation (6.2) is an actual mathematical application, not merely a citation.

The main new 99-percent branch does not itself satisfy `theta>2` from the lower bound (4.2), so it correctly uses the fractional-`L^p` route rather than misapplying (6.2).

## 7. Corrections consumed and what remains open

The live source corrections applied here include:

1. arbitrary bounded joint three-dimensional density does **not** imply the proposed rank-three coarea bound;
2. positive moments of conditional spectral projection `L^infinity` norms can diverge;
3. `sup_b ||p_(Q3|Qrest=b)||_infinity` is not universally bounded, even when the full form is diagonal and globally bounded;
4. law-uniform pointwise quadratic-phase decay is false;
5. a single cross minor or a single heavy off-diagonal coefficient is not a universal certificate.

None of those interfaces is used in Theorems 3.1, 4.1, or 5.1.

The full conjecture remains **OPEN**. After this run, the O0 nested-heavy part has a sharper conditional architecture:

- coarse diffuse residual (`gamma/4`, leverage `<=5/6`): paid by the preceding B08 theorem;
- coarse-heavy but fine non-coloop residual (`gamma/16`, leverage `<=99/100`): paid by Theorem 4.1;
- fine near-coloop residual (`>99/100`): carries the shear-invariant pair currency (5.6)-(5.7);
- zero/near-zero first physical pivot remains unpaid;
- O1/O2/O3 aggregate overlap classes remain separate full-target debts.

The next B08 mechanism should combine the near-coloop pair currency with a product-preserving grouped-coordinate / rank-two affine half-Riesz payment, while treating the small-pivot branch separately. The key requirement is to consume the **aggregate** pair currency before any reciprocal-minor selection.

## 8. Status

- `QFORM-E2-TO-TUNABLE-RIDGE-v1`: **PROVED**.
- `QFORM-SHEAR-INVARIANT-TUNABLE-RIDGE-v1`: **PROVED**.
- `QFORM-TRANSVERSE-99PCT-RIDGE-CLOSURE-v1`: **PROVED SUPPORTING ANALYTIC THEOREM**; absolute continuity + essential boundedness in its stated branch, continuity not claimed.
- `QFORM-99PCT-NEAR-COLOOP-PAIR-CURRENCY-v1`: **PROVED STRUCTURAL LEMMA**.
- full universal QFORM theorem: **OPEN / not proved / not disproved**.
