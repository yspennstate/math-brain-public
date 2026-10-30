# fleet03/B08 — shear-invariant transverse ridge reserve after a physical pivot

**Run:** `20260922T172009Z-fleet03-B08-qform-diffuse-r14`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Fresh owner control used before publication:** revision `2026-09-22.8`, main observed at `cb34492bcab21f4efa77797b4a56d569675d8f4c`  
**Assignment:** Diffuse eigenvector case  
**Classification:** `PROVED SUPPORTING THEOREM / TARGET-RELEVANT O0-HEAVY BRIDGE / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and first missing implication

The owner target is unchanged: for every dimension, every independent real coordinate family with probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove one universal finite essential-density bound for `Q=X^TAX`, or give a target-valid counterexample. Continuity is separately requested.

This run changes mechanism from the preceding B08 fractional-ridge/pivot threshold calculation. The new input is fleet03/B07's full-matrix third-compound reduction. Its O0 branch produces an original-coordinate cross block `B=A[L,R]` with nonzero third-minor mass, then chooses a ridge scale `gamma>0` satisfying

`theta_gamma(B)=tr[B B^T (gamma^2 I+B B^T)^(-1)] = 8/3`.

If all ridge row leverages are at most `1/2`, the existing ridge theorem pays that branch directly. If not, B07 returns a physical ridge-heavy row and asks how to pass it through a genuine scalar Schur pivot without losing the remaining diffuse curvature.

The obstruction is that completing a physical square shears every other row of the cross block by a multiple of the pivot row. A crude rank-one perturbation estimate can lose one full effective direction and does not reach the square-smoothing threshold uniformly. The theorem below identifies a two-direction reserve that is **exactly invariant under this Schur shear**.

No post-rotation independence, law-uniform pointwise stationary phase, unrestricted fiber supremum, or one-good-minor assertion is used.

## 2. Sources actually used

1. **Full-matrix O0 reduction.** fleet03/B07, `QFORM-THIRD-COMPOUND-OVERLAP-REDUCTION-v1` and `QFORM-O0-RIDGE-PAYMENT-v1`, canonical report
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260922T163733Z-fleet03-B07-qform-r12/REPORT.md`.
   It proves that the O0 cross block may be calibrated by `theta=8/3`, and identifies the ridge-heavy-row branch as an unresolved product-preserving interface.

2. **Ridge Fourier theorem.** `QFORM-RIDGE-DENSITY-v1`, canonical report
   `proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.
   For an original-coordinate cross block `H`, scale `g`, and `q=1`, if
   `max diag K_g(H)<=1/2`, it gives
   `|phi_R(t)| <= min(1,(t0/|t|)^(theta/2))`, with
   `t0=pi e sqrt(2)/(2g) D^(-1/(2theta))`,
   where `theta=tr K_g(H)`, `D=det(I+HH^T/g^2)`.

3. **Previous B08 fractional endpoint.** The preceding B08 report proves that if the ridge exponent is large enough only for an `L^s` Fourier integral, one may first obtain an `L^p`, `p>2`, residual density and then spend one genuine original-coordinate square to reach `L^infinity`. The needed statement is rederived below at the chosen numerical exponent, so the present theorem is not merely a citation.

4. **Completed fleet04 mathematics actually applied.** The designated partner `fleet04/B08` still had no completed current-QFORM canonical directory or shared handoff at the fresh source check; no theorem is fabricated for that slot. The compatible completed fleet04 result used below is fleet04/B18 `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`, scientific commit `441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`, path
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T113729Z-fleet04-B18-qform-r1/REPORT.md`.

## 3. A normalized third-volume reserve at effective dimension 8/3

Let `B` be a real `p x m` matrix and fix `gamma>0`. Put

`R=(gamma^2 I+B^T B)^(-1/2)`,
`Z=BR`,
`K=ZZ^T=B B^T(gamma^2 I+B B^T)^(-1)`.

Assume

`tr K = 8/3`.                                                   (3.1)

Every eigenvalue `kappa_j` of `K` lies in `[0,1)`. Fix a row index `i` with normalized row `z_i!=0`, and put

`k=K_ii=||z_i||^2`.

Define the total normalized three-volume through row `i` by

`T_i = sum_{j<l, j,l != i} det K[{i,j,l},{i,j,l}].`            (3.2)

### Lemma 3.1 — `QFORM-RIDGE-THREEVOLUME-THROUGH-ROW-v1`

Under (3.1), every nonzero normalized row satisfies

`boxed( T_i >= (2/3) K_ii. )`                                  (3.3)

#### Proof

Let `e_1,e_2` denote the first two elementary symmetric functions of the eigenvalues of `K`. The third Newton transformation gives the exact coordinate identity

`T_i = [ K ( e_2 I - e_1 K + K^2 ) ]_ii`.                     (3.4)

To see the lower bound, diagonalize `K=U diag(kappa_1,...,kappa_r)U^T`. Then

`T_i = sum_a |U_ia|^2 kappa_a e_2(kappa_1,...,hat{kappa_a},...,kappa_r).` (3.5)

Fix `a` and write `x=kappa_a`. The sum of the remaining eigenvalues is

`S=8/3-x`, with `0<=x<=1`, hence `5/3<=S<=8/3`.                 (3.6)

Among numbers in `[0,1]` with fixed sum `S`, `e_2=(S^2-sum y_j^2)/2` is minimized by concentrating mass into as many ones as possible. If `S<=2`, the minimum is `S-1>=2/3`. If `S>=2`, the minimum is `2S-3>=1`. Thus in every case

`e_2(kappa_{!=a}) >=2/3`.                                      (3.7)

Substituting into (3.5) gives

`T_i >=(2/3) sum_a |U_ia|^2 kappa_a=(2/3)K_ii`.
QED.

The notable point is that the lower bound survives division by the size of the chosen row: every nonzero row sees a dimensionless transverse two-volume reserve.

## 4. Exact invariance under an arbitrary Schur shear

Write the selected row of `B` as `b`, and the remaining rows as `C`, so

`B=[b; C]`.

Let `d` be an arbitrary real column vector of compatible length and define the sheared block

`H=C-d b`.                                                       (4.1)

This is exactly the form of the cross block produced after a scalar Schur completion: if the physical pivot is `a=A_ii!=0`, and `u=A[L\{i},i]`, then the residual cross block between `L\{i}` and `R` is `H=C-(u/a)b`.

Let

`z=bR`,
`P=I-z^T z/||z||^2`,
`D=H R P`.                                                       (4.2)

Because `zP=0`,

`D=(C-d b)RP = C R P`;                                         (4.3)

therefore `D` is completely independent of the shear vector `d`.

### Lemma 4.1 — `QFORM-SCHUR-SHEAR-TRANSVERSE-E2-v1`

Under (3.1), for every `d`,

`boxed( e_2(D D^T) >=2/3, )`                                   (4.4)

and

`||D||_op <=1`,
`||D||_F^2 >=2/sqrt(3)`.                                       (4.5)

#### Proof

Subtracting a multiple of `z` from either of two other row vectors does not change their three-dimensional volume together with `z`. Hence for every pair `j<l`,

`|| z wedge (CR)_j wedge (CR)_l ||^2
 =|| z wedge (HR)_j wedge (HR)_l ||^2`.

Projecting the last two vectors orthogonally to `z` gives

`|| z wedge (HR)_j wedge (HR)_l ||^2
 =||z||^2 || D_j wedge D_l ||^2`.                              (4.6)

Summing (4.6) over pairs and using the Gram/Cauchy-Binet identity yields

`T_i = K_ii e_2(D D^T)`.                                       (4.7)

Lemma 3.1 now gives (4.4).

Next, `CR` is a row deletion of `Z=BR`. Since the singular values of `Z` are `s_j(B)/sqrt(gamma^2+s_j(B)^2)`, `||Z||op<1`; row deletion and right multiplication by the projection `P` cannot increase operator norm. Thus `||D||op<=1`.

If `delta_j` are the singular values of `D`, then

`e_2(DD^T)=sum_{j<l} delta_j^2 delta_l^2
 <= (1/2)(sum_j delta_j^2)^2`.

Combining this with (4.4) gives

`sum_j delta_j^2 >= sqrt(4/3)=2/sqrt(3)`,
which is (4.5). QED.

## 5. Transferring the reserve to the actual Schur cross block

The preceding reserve is measured after the old right regularizer `R` and the harmless transverse projection `P`. It still forces a genuine ridge-effective-dimension lower bound for the actual sheared block `H`.

### Theorem 5.1 — `QFORM-SHEAR-INVARIANT-TRANSVERSE-RIDGE-v1`

Under (3.1), for every row `i` with `b!=0` and every shear `d`, the actual block `H=C-db` satisfies

`boxed(
 theta_(gamma/4)(H)
 :=tr[H H^T((gamma/4)^2 I+H H^T)^(-1)]
 >= 32/(17 sqrt(3)) >1.
)`                                                               (5.1)

#### Proof

Let `h_j` and `delta_j` be the singular values of `H` and `D`, ordered decreasingly and padded by zeros. Since

`D=H R P`,
`||RP||op<=1/gamma`,

singular-value monotonicity gives

`delta_j <= h_j/gamma`.                                        (5.2)

Lemma 4.1 also gives `delta_j<=1`. Therefore

`delta_j^2 <= min(1,h_j^2/gamma^2)`.                            (5.3)

For every `x>=0`,

`x^2/(1/16+x^2) >= (16/17) min(1,x^2)`.                        (5.4)

Applying (5.4) with `x=h_j/gamma`, then (5.3), and summing gives

`theta_(gamma/4)(H)
 =sum_j h_j^2/((gamma/4)^2+h_j^2)
 >=(16/17)sum_j delta_j^2
 >=(16/17)(2/sqrt(3))
 =32/(17sqrt(3)).`

Finally `32/(17sqrt(3))>1` because `32^2=1024>3*17^2=867`. QED.

This is the main new structural payment. The Schur completion may use an arbitrarily large vector `d=u/a`; it cannot erase the normalized transverse two-direction reserve, because the shear is exactly parallel to the pivot row and is annihilated by `P`.

## 6. Density consequence: a nonzero pivot plus diffuse transverse Schur ridge

Now return to the quadratic form. Take an original physical pivot `i` with

`a=A_ii !=0`.

Let `L|R` be a physical cross-block partition with `i in L`, write `B=A[L,R]=[b;C]`, and suppose a scale `gamma` has been chosen so that

`theta_gamma(B)=8/3`,
`b!=0`.                                                        (6.1)

Complete the square in the original coordinate `X_i`. The residual Schur form has cross block

`H=C-(u/a)b`,                                                  (6.2)

where `u=A[L\{i},i]`. Theorem 5.1 gives

`theta:=theta_(gamma/4)(H) >= T:=32/(17sqrt(3)).`              (6.3)

Assume only the **residual diffuse gate**

`max_j [H H^T((gamma/4)^2 I+H H^T)^(-1)]_jj <=1/2.             (6.4)

### Theorem 6.1 — `QFORM-PIVOT-TRANSVERSE-LP-CLOSURE-v1`

Under (6.1)-(6.4), for every independent cap-one product input law, `Q=X^TAX` has an essentially bounded density with

`boxed(
 ||p_Q||_infinity
 <= C_* / sqrt(|a| gamma),

 C_* = 10 sqrt( 2 sqrt(2e) * 768/(768-425sqrt(3)) )
 <107.
)`                                                              (6.5)

The argument proves absolute continuity and essential boundedness. It does **not** by itself prove a continuous representative.

#### Proof

Apply the ridge characteristic-function theorem to the residual Schur form with cross block `H`, scale

`g=gamma/4`,

and `q=1`. Condition (6.4) is exactly its ridge-leverage gate. It gives

`|phi_R(t)| <= min(1,(t0/|t|)^beta)`,
`beta=theta/2`,
`t0=pi e sqrt(2)/(2g) D^(-1/(2theta))`,                        (6.6)

where `D=det(I+HH^T/g^2)`. The elementary inequality `log D>=theta` gives

`t0 <= pi sqrt(2e)/(2g)=2pi sqrt(2e)/gamma`.                   (6.7)

Choose

`s=48/25`, `p=s/(s-1)=48/23`.

By (6.3),

`beta s >= (T/2)(48/25)=768/(425sqrt(3))>1`,                   (6.8)

because `768^2=589824>3*425^2=541875`. Thus

`int |phi_R(t)|^s dt
 <=2 t0 [beta s/(beta s-1)].`                                  (6.9)

Inverse Hausdorff-Young yields an `L^p`, `p>2`, density for the Schur residual. The sharp Beckner factor is at most one, so

`||p_R||_p
 <=(2pi)^(-1/s)
   [2t0 beta s/(beta s-1)]^(1/s).`                             (6.10)

Completing the genuine physical square writes

`Q=R+aV^2`,

where conditional on `R=r`, the variable `V` has a density bounded by one: it is a mixture of translations of the original independent density of `X_i`. The `L^p` dependent-square estimate from the preceding B08 proof gives, with the conjugate exponent `s`,

`||p_Q||infinity
 <=2 |a|^(-1/2)(1-s/2)^(-1/2)||p_R||_p^(s/2).`                (6.11)

Here `1-s/2=1/25`. Substitute (6.7)-(6.10) into (6.11). Since `x/(x-1)` decreases for `x>1`, (6.8) gives

`beta s/(beta s-1)
 <= [768/(425sqrt3)]/[768/(425sqrt3)-1]
 =768/(768-425sqrt3).`                                        (6.12)

After cancellation of the Fourier `pi` factors,

`||p_Q||infinity
 <=10 sqrt(2 sqrt(2e) * 768/(768-425sqrt3))
       /sqrt(|a|gamma),`
which is (6.5).

For a fully rational certificate of the displayed `<107`, use `e<11/4`, hence `sqrt(2e)<47/20`, and `sqrt(3)<8661/5000` (its square exceeds `3`). Then

`768/(768-425sqrt3) < 51200/2121`,

so

`C_*^2
 <200*(47/20)*(51200/2121)
 =24064000/2121
 <11449=107^2`.
QED.

### Target-relevant reading

In the B07 O0 ridge-heavy branch, the heavy row has `b!=0`. Therefore, whenever that same row also has a nonzero diagonal pivot and its Schur residual satisfies (6.4), the diffuse mechanism does not collapse after square completion. Quantitatively, if in addition

`|A_ii| gamma >=rho>0`,

then

`||p_Q||infinity <107/sqrt(rho)`.                                (6.13)

Thus the remaining universal O0-heavy debt is forced into one of two more rigid mechanisms:

1. a zero/near-zero **scale-normalized physical pivot**, `|A_ii|gamma` small; or
2. a second localized row in the **Schur residual ridge kernel** at scale `gamma/4`.

This is precisely the kind of diffuse/localized handoff requested by the assignment. No small physical principal minor is selected.

## 7. Literal application of completed fleet04 mathematics

The designated partner `fleet04/B08` still has no completed current-programme artifact. To apply completed compatible fleet04 mathematics rather than only cite it, consider the stronger subbranch of Theorem 6.1 in which

`theta_(gamma/4)(H)>2`

in addition to (6.4). The source ridge theorem then gives a direct residual density cap

`M <= [sqrt(e)/(sqrt(2)(gamma/4))]
       * theta/(theta-2)
 = [2sqrt(2e)/gamma] * theta/(theta-2).`                        (7.1)

Fleet04/B18 `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1` applies to the exact same completed-square identity `Q=R+aV^2` and gives the actual inequality

`boxed(
 ||p_Q||infinity
 <=2 sqrt(M/|a|)
 <=2 sqrt( [2sqrt(2e)/( |a| gamma)] * theta/(theta-2) ).
)`                                                               (7.2)

This is a literal mathematical use of the completed fleet04 theorem. It is sharper than routing through the fractional `L^p` endpoint whenever the residual effective dimension already exceeds two. The new Theorem 6.1 is needed in the genuinely harder range `1<theta<=2` forced by the shear-invariant reserve.

## 8. Why this does not overclaim the full target

The full universal QFORM conjecture is still **OPEN**. Theorem 6.1 contains two quantitative gates not implied yet by the bare three-large-eigenvalue hypothesis:

- a universal lower payment for `|A_ii| gamma`; and
- the residual Schur ridge-leverage gate (6.4).

The result does, however, remove a real structural obstruction: arbitrary same-side couplings can no longer be blamed for destroying all diffuse cross curvature after square completion. At calibrated effective dimension `8/3`, an invariant two-direction reserve survives every Schur shear and already crosses the fractional square-smoothing threshold.

The next B08 step should therefore attack the **second-localization branch** produced by failure of (6.4): iterate the normalized transverse-reserve construction on that localized Schur row, or route the resulting two-row packet into the completed grouped-rank-two / bank mechanisms. In parallel, the near-zero scale-normalized pivot branch should be handed to the zero-pivot/hyperbolic workers. Repeating the old small-operator-remainder perturbation would not address these two remaining gates.

## 9. Status

- `QFORM-RIDGE-THREEVOLUME-THROUGH-ROW-v1`: **PROVED**.
- `QFORM-SCHUR-SHEAR-TRANSVERSE-E2-v1`: **PROVED**.
- `QFORM-SHEAR-INVARIANT-TRANSVERSE-RIDGE-v1`: **PROVED**.
- `QFORM-PIVOT-TRANSVERSE-LP-CLOSURE-v1`: **PROVED SUPPORTING DENSITY THEOREM**, essential boundedness; continuity not established by this endpoint.
- Completed fleet04/B18 square-smoothing theorem: **APPLIED** in (7.2).
- Full universal QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.
- Full continuity: **OPEN**.
