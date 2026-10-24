# account03/B08 — 5/6-leverage closure from the full transverse e2 reserve

**Run:** `20260922T174745Z-account03-B08-qform-diffuse-r15`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Final owner control used before publication:** revision `2026-09-22.10`  
**Assignment:** Diffuse eigenvector case  
**Classification:** `PROVED SUPPORTING THEOREM / STRONGER O0-HEAVY BRIDGE / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target and mechanism change

The target remains: for every dimension, independent real coordinates with probability densities bounded by one, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal finite essential-density bound for `Q=X^T A X`, or give a valid counterexample. Continuity is a separate requested conclusion.

This run stays on the O0-heavy interface from the full-matrix third-compound reduction but changes the quantitative mechanism. The preceding B08 run used only the Frobenius consequence of a shear-invariant transverse two-volume reserve and therefore reached a residual ridge-leverage gate `<=1/2`. Here the complete `e_2` reserve is retained. A simple threshold argument upgrades the guaranteed residual ridge effective dimension enough to run the fractional ridge theorem at `q=5/3`, increasing the admissible residual physical-row leverage all the way to `5/6`.

No post-rotation independence, law-uniform pointwise stationary-phase estimate, unrestricted fiber supremum, or selection of one reciprocal tiny minor is used.

## 2. Sources actually used

1. **account03/B07 full-matrix O0 reduction.** `QFORM-THIRD-COMPOUND-OVERLAP-REDUCTION-v1` and `QFORM-O0-RIDGE-PAYMENT-v1`, canonical report
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260922T163733Z-account03-B07-qform-r12/REPORT.md`.
   In its O0 branch there is an original-coordinate cross block `B=A[L,R]` and a scale `gamma>0` with
   `theta_gamma(B)=8/3`. If all row ridge leverages are at most `1/2`, that branch is already paid; otherwise it returns a physical ridge-heavy row.

2. **Previous account03/B08 shear-invariant reserve.** Run `20260922T172009Z-account03-B08-qform-diffuse-r14`, report
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260922T172009Z-account03-B08-qform-diffuse-r14/REPORT.md`.
   Its exact statements used below are: after selecting a row and making an arbitrary scalar-Schur shear, a transverse matrix `D` satisfies `e_2(D D^T)>=2/3` and `||D||op<=1`; moreover its singular values are bounded by the corresponding actual Schur cross singular values divided by `gamma`.

3. **Fractional ridge Fourier theorem.** `QFORM-RIDGE-DENSITY-v1`, canonical report
   `proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.
   At ridge scale `g`, exponent `q in [1,2]`, if `max diag K_g(H)<=q/2`, it gives
   `|phi_R(t)| <= min(1,(t0/|t|)^(theta/(2q)))`, where
   `theta=tr K_g(H)` and
   `t0=(pi e sqrt(2/q)/(2g)) D^(-1/(2theta))`.
   Since `log D>=theta`,
   `t0 <= pi sqrt(2e/q)/(2g)`.

4. **Completed account04 mathematics actually applied.** The designated partner `account04/B08` still had no completed current-QFORM handoff or canonical current-QFORM directory at the fresh check, so no partner theorem is fabricated. The compatible completed account04 result applied below is account04/B18 `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`, scientific source
   `proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T113729Z-account04-B18-qform-r1/REPORT.md`.
   If a residual variable has density cap `M`, and conditionally a translated physical coordinate still has density cap one, then adding `aV^2` gives density cap `2 sqrt(M/|a|)`.

The live corrections were also respected: pointwise law-uniform quadratic-phase decay is false; one heavy off-diagonal coefficient plus one square alone is insufficient; and independence is never asserted after spectral rotation.

## 3. Setup: exact Schur-shear transverse reserve

Let `B` be the O0 cross block, with calibrated `gamma>0`, and write one selected physical row separately:

`B=[b; C]`,

`R=(gamma^2 I+B^T B)^(-1/2)`,

`z=bR`,

`P=I-z^T z/||z||^2`.

For an arbitrary shear vector `d`, put

`H=C-d b`,

`D=H R P=C R P`.

The equality follows from `zP=0`, so the transverse object `D` is exactly invariant under the arbitrary Schur shear. The previous B08 theorem gives

`e_2(D D^T)>=2/3`,                                             (3.1)

`||D||op<=1`.                                                   (3.2)

Let `h_j` be the singular values of the actual Schur cross block `H`, and `delta_j` those of `D`. Since `||RP||op<=1/gamma`, singular-value monotonicity gives

`delta_j <= h_j/gamma`.                                        (3.3)

Together with (3.2),

`delta_j^2 <= x_j := min(1,h_j^2/gamma^2) <=1`.                (3.4)

Because the second elementary symmetric function is coordinatewise increasing on the nonnegative orthant, (3.1)-(3.4) imply

`e_2(x_1,x_2,...) >=2/3`.                                      (3.5)

The previous run used only `sum delta_j^2>=2/sqrt(3)`. The improvement below uses the full information (3.5).

## 4. Scalar lemma: e2 forces ridge trace 16/9

### Lemma 4.1 — `QFORM-E2-TO-ONE-SIXTEENTH-RIDGE-v1`

If `0<=x_j<=1` and `e_2(x)>=2/3`, then

`boxed( sum_j x_j/(1/16+x_j) >=16/9. )`                         (4.1)

### Proof

Let

`G={j:x_j>=1/2}`, `m=|G|`, `T=sum_{j notin G} x_j`.

For `x>=1/2`,

`x/(1/16+x) >= (1/2)/(9/16)=8/9`.                              (4.2)

For `0<=x<1/2`,

`x/(1/16+x) >= x/(9/16)=16x/9`.                                (4.3)

If `m>=2`, two terms from (4.2) already give `16/9`.

If `m=0`, then `T=sum x_j` and

`e_2(x) <= T^2/2`.

Hence `T>=2/sqrt(3)>1`, and (4.3) gives

`sum_j x_j/(1/16+x_j) >= (16/9)T
 >=32/(9sqrt(3)) >16/9`.                                       (4.4)

If `m=1`, write the unique large coordinate as `x_*`. Since `x_*<=1` and the small-small pair sum is at most `T^2/2`,

`e_2(x) <= x_* T+T^2/2 <= T+T^2/2`.                            (4.5)

Were `T<1/2`, the right side would be `<1/2+1/8=5/8<2/3`, contradicting (3.5). Thus `T>=1/2`. Equations (4.2)-(4.3) give

`sum_j x_j/(1/16+x_j)
 >=8/9+(16/9)(1/2)=16/9`.

This proves the lemma. QED.

## 5. Main structural upgrade: residual ridge trace at least 16/9

Set

`g=gamma/4`.

Then

`theta_g(H)
 =sum_j h_j^2/(g^2+h_j^2)
 =sum_j u_j/(1/16+u_j)`,

where `u_j=h_j^2/gamma^2`. Since `x_j=min(1,u_j)` and the scalar map `u -> u/(1/16+u)` is increasing,

`theta_g(H) >= sum_j x_j/(1/16+x_j) >=16/9`.                   (5.1)

### Theorem 5.1 — `QFORM-SHEAR-INVARIANT-TRANSVERSE-RIDGE-16/9-v1`

In the calibrated O0 setup `theta_gamma(B)=8/3`, after **any** scalar Schur shear through a nonzero selected row,

`boxed( theta_(gamma/4)(H) >=16/9. )`                           (5.2)

This improves the previous guaranteed value `32/(17sqrt(3))>1` to `16/9` without changing the scale or adding a spectral/moment assumption.

## 6. Fractional-ridge closure up to residual leverage 5/6

Return to the quadratic form and assume a genuine original-coordinate pivot

`a=A_ii !=0`.

Completing the square in the physical coordinate `X_i` writes

`Q=R_0+aV^2`,                                                   (6.1)

where `R_0` is the Schur-residual quadratic form on the other original coordinates, and, conditionally on the residual variables (hence also after disintegrating over `R_0`), `V` is a mixture of translations of the original `X_i` density. Therefore its conditional density remains at most one.

Assume the only residual diffuse gate

`max_j [H H^T(g^2 I+H H^T)^(-1)]_jj <=5/6`,

with `g=gamma/4`.                                                (6.2)

Choose

`q=5/3`, `s=19/10`, `p=s/(s-1)=19/9>2`.                        (6.3)

Condition (6.2) is exactly the fractional-ridge admissibility condition `max diag K_g<=q/2`. By (5.2),

`beta:=theta_g(H)/(2q) >= (16/9)/(10/3)=8/15`,                 (6.4)

so

`beta s >= (8/15)(19/10)=76/75>1`.                             (6.5)

The ridge theorem yields

`|phi_R0(t)| <= min(1,(t0/|t|)^beta)`                          (6.6)

and, using `log D>=theta`,

`t0 <= pi sqrt(2e/q)/(2g)
    = 2 pi sqrt(6e/5)/gamma`.                                  (6.7)

Thus

`int_R |phi_R0(t)|^s dt
 <=2 t0 * (beta s)/(beta s-1)
 <=152 t0`,                                                     (6.8)

because `x/(x-1)` decreases on `(1,infinity)` and its value at `76/75` is `76`.

Inverse Hausdorff-Young gives an `L^p` residual density with

`||p_R0||_p
 <=(2pi)^(-1/s) [int |phi_R0|^s]^(1/s)`,                     (6.9)

where dropping Beckner's factor only weakens the inequality.

For completeness, the dependence-safe `L^p` square step used now is elementary. For `a>0`, from (6.1),

`p_Q(t)
 <= |a|^(-1/2) int_0^infinity p_R0(t-u) u^(-1/2) du`;           (6.10)

the sign `a<0` is identical after reflection. Split the integral at

`U=||p_R0||_p^(-s)`.

Hölder on `[0,U]` and mass one on `[U,infinity)` give

`||p_Q||_infinity
 <= |a|^(-1/2)
    [(1-s/2)^(-1/s)+1]
    ||p_R0||_p^(s/2).`                                         (6.11)

Combining (6.7)-(6.11), with `1-s/2=1/20`, gives

`boxed(
 ||p_Q||_infinity
 <= C_(5/6) / sqrt(|a| gamma),

 C_(5/6)
 = (20^(10/19)+1) sqrt(152 sqrt(6e/5))
 <97.
)`                                                              (6.12)

### Theorem 6.1 — `QFORM-TRANSVERSE-5/6-RIDGE-CLOSURE-v1`

Under the O0 calibration `theta_gamma(B)=8/3`, if a selected physical row admits a nonzero scalar pivot `a`, then after its arbitrary Schur shear the entire branch is paid whenever the residual ridge row leverage at scale `gamma/4` is at most `5/6`, with the explicit essential-density bound (6.12).

The proof establishes absolute continuity and an essentially bounded density. **It does not, from this `L^p` square argument alone, prove a continuous representative.**

This is materially stronger than the preceding B08 gate `1/2`: a surviving O0-heavy configuration with quantitative `|a|gamma` must now produce a second original physical row carrying more than `5/6` of its residual ridge leverage.

## 7. Completed account04 theorem applied to an actual inequality

The designated `account04/B08` result is unavailable, but account04/B18's completed dependent-square theorem can be applied exactly whenever the residual ridge branch reaches `L^infinity` before the square.

At any residual scale `g` satisfying

`max diag K_g(H)<=1/2`, `theta=tr K_g(H)>2`,                    (7.1)

the `q=1` ridge theorem gives a continuous residual density with

`M:=||p_R0||_infinity
 <= sqrt(e)/(sqrt(2) g) * theta/(theta-2).`                     (7.2)

Applying account04/B18 `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1` to (6.1) yields the concrete inequality

`boxed(
 ||p_Q||_infinity
 <=2 [ sqrt(e)/(sqrt(2)|a|g) * theta/(theta-2) ]^(1/2).
)`                                                               (7.3)

This use is legitimate even though `V` and `R_0` are dependent after completing the square, because the theorem requires only the conditional cap-one translation-mixture property. Equation (7.3) is a genuine mathematical application of completed account04 work, not a citation-only handoff.

## 8. Implication for the full proof architecture

Combine B07 and the present theorem in the O0 branch:

- B07 pays the calibrated O0 branch directly when the original ridge rows are all at most `1/2`.
- If there is a ridge-heavy physical row and it has a usable nonzero pivot, the Schur shear cannot destroy the transverse `e_2` reserve.
- The present theorem pays the residual whenever its new maximum ridge row leverage is at most `5/6`.

Consequently, after this run the genuinely unpaid O0-heavy geometry is narrower: one must confront a small/zero physical pivot or a **nested residual localization** in which another physical row has ridge leverage greater than `5/6` at scale `gamma/4`. That is precisely the kind of near-coordinate concentration that grouped-coordinate/localized mechanisms can exploit; it is no longer enough for the residual simply to fail a `1/2` diffuse gate.

A useful quantitative conditional statement is: for every `eta>0`, every such O0-heavy instance with `|a| gamma>=eta` and residual maximum ridge leverage `<=5/6` satisfies

`||p_Q||infinity <97/sqrt(eta)`.                                (8.1)

The remaining task is to pay the nested `>5/6` row (or the zero/near-zero pivot) using the original-coordinate grouped structure without losing arbitrary self blocks or additional spectral components.

## 9. Status

- `QFORM-E2-TO-ONE-SIXTEENTH-RIDGE-v1`: **PROVED**.
- `QFORM-SHEAR-INVARIANT-TRANSVERSE-RIDGE-16/9-v1`: **PROVED**.
- `QFORM-TRANSVERSE-5/6-RIDGE-CLOSURE-v1`: **PROVED supporting target-relevant branch**; essential boundedness, not continuity.
- account04/B18 dependent-square theorem: **APPLIED** to (7.3).
- designated `account04/B08` current-QFORM output: **NOT FOUND at fresh source check; not fabricated**.
- full universal QFORM theorem: **OPEN / NOT PROVED / NOT DISPROVED**.

No task/schedule/enabled-state/quiet-delivery setting, email, Drive, public release, paid model/API/Codex call, credential, or cross-account native action was changed or used in producing this report.
