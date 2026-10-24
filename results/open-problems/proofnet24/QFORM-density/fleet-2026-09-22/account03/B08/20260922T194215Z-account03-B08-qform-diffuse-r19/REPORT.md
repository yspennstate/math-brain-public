# account03/B08 — symmetric fine-scale ridge closure and a two-sided near-coloop bank

**Run:** `20260922T194215Z-account03-B08-qform-diffuse-r19`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control at run start:** revision `2026-09-22.15`  
**Assignment:** Diffuse eigenvector case  
**Classification:** `PROVED SUPPORTING THEOREM / EXHAUSTIVE NONZERO-PIVOT RIDGE-OR-BICOLOOP TRICHOTOMY / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B08, 2026-09-22T19:42:15Z.
attacking: symmetrize the fine-scale diffuse ridge closure across both physical sides, then force a quantitative two-sided near-coloop exterior-volume certificate in the only surviving nonzero-pivot branch.

## 1. Exact target and correction discipline

The parent target remains the unrestricted statement: for every dimension, every independent real input vector `X=(X_i)` whose coordinate probability densities satisfy `0<=f_i<=1`, and every real symmetric matrix `A` with at least three eigenvalues of modulus at least one, prove that `Q=X^T A X` has a density with one universal finite essential-supremum bound, or construct a target-valid counterexample. No Gaussian, moment, compact-support, log-concavity, connected-support, or spectral-coordinate-independence assumption is introduced. Continuity is tracked separately from essential boundedness.

The live correction state is respected. In particular, this report does **not** use:

* law-uniform pointwise `|t|^{-1/2}` decay for one-dimensional quadratic phases;
* independence after an orthogonal spectral rotation;
* a dimension-free unrestricted fiber supremum;
* the refuted arbitrary-joint rank-three coarea inequality;
* the refuted positive conditional projection-density moment;
* a reciprocal estimate obtained by selecting one possibly tiny physical minor.

The owner-message mathematical suggestions are treated as research hypotheses unless independently proved in a source-valid report. The only analytic inputs used below are the completed ridge-window graph estimate, the already proved B08 fine-scale transverse reserve, elementary Hausdorff-Young/Holder manipulations already proved in the preceding B08 run, and the completed account04/B18 dependent-square smoothing lemma at its exact scope.

## 2. Inherited O0 residual geometry

The preceding B08 run

`yspennstate/math-open-problems@04fb94f2b622e0423272e1aefa1aaf0af59f305f`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260922T183452Z-account03-B08-qform-diffuse-r17/REPORT.md`

starts from the shear-invariant transverse reserve supplied by the earlier O0 calibration. In that structural branch there is a scale `gamma>0` and, after completing the square in a selected **original physical coordinate**, an actual residual original-coordinate cross block `H` with singular values `h_nu` such that

`x_nu := min(1,h_nu^2/gamma^2)`

satisfies

`e_2(x)=sum_(mu<nu) x_mu x_nu >= 2/3`.                         (2.1)

The same source proves for every `tau>0`

`theta_(tau gamma)(H)
 := tr[H H^T((tau gamma)^2 I+H H^T)^(-1)]
 >= 2/(1+2 tau^2).`                                           (2.2)

Take throughout

`g=gamma/16`.                                                   (2.3)

Then

`theta := theta_g(H) >= 256/129 = 1.984496124...`.             (2.4)

Define the two ridge kernels on the two **physical** sides of `H`:

`K_L = H H^T(g^2 I+H H^T)^(-1),`

`K_R = H^T H(g^2 I+H^T H)^(-1).`                              (2.5)

They have the same nonzero eigenvalues

`mu_nu=h_nu^2/(g^2+h_nu^2) in [0,1)`,                          (2.6)

and hence

`tr K_L=tr K_R=theta`.                                         (2.7)

The previous run paid a branch if the left-side ridge leverage obeyed

`max_i (K_L)_ii <=99/100`,                                    (2.8)

obtaining

`||p_Q||_infinity <3349/sqrt(|a| gamma)`                       (2.9)

for a nonzero original physical scalar pivot `a`. It did not explicitly exploit the completely symmetric possibility of orienting the graph inequality from the **right** side, and it left a one-sided near-coloop branch. The present run closes that asymmetry and quantifies the geometry that remains if both sides are near-coloops.

The full target is not reduced to (2.1) in this report; (2.1) is a supporting structural branch. All conclusions below are therefore stated at exactly that scope.

## 3. The ridge characteristic-function envelope at arbitrary exponent

The completed ridge-window report is

`yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`

`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

Its graph calculation, before imposing time-integrability, gives the following. Let `R` be any residual quadratic form whose original-coordinate cut has cross block `H`. At the fixed scale `g`, for `q in [1,2]`, if the relevant side's ridge diagonal satisfies

`max diag K <=q/2`,                                             (3.1)

then

`|phi_R(t)|
 <= D^(-1/(4q)) [L_q/(2g|t|)]^(theta/(2q)),`                  (3.2)

where

`D=det(I+H H^T/g^2),`
`L_q=pi e sqrt(2/q).`                                          (3.3)

The same theorem explicitly permits interchanging the two physical sides, so (3.1) may be checked on either `K_L` or `K_R`. All within-block quadratic phases, outside coordinates, induced affine terms and outside couplings are retained.

Since

`log D=sum_nu log(1+h_nu^2/g^2)
     >=sum_nu h_nu^2/(g^2+h_nu^2)=theta`,                     (3.4)

write

`beta=theta/(2q)`,
`t_0=L_q/(2g) D^(-1/(2theta))
    <= pi sqrt(e) sqrt(2/q)/(2g).`                             (3.5)

Then

`|phi_R(t)| <= min(1,(t_0/|t|)^beta).`                        (3.6)

Formula (3.6) is useful even when `beta<=1`, where direct `L^1` Fourier inversion cannot be used.

## 4. New branch I: effective ridge dimension just above two needs no leverage gate

### Theorem 4.1 — `QFORM-Q2-ABOVE-TWO-SQUARE-CLOSURE-v1`

In the setting of Section 2, assume the original physical scalar pivot satisfies `a!=0`. If

`theta >=201/100`,                                               (4.1)

then the full quadratic form has an absolutely continuous, essentially bounded law with

`boxed(
 ||p_Q||_infinity
 <= C_hi/sqrt(|a| gamma),
 C_hi=(400^(200/399)+1)e^(1/4)
       sqrt(8*80199/199)
 <1543.
)`                                                              (4.2)

No row- or column-leverage assumption on `H` is required.

### Proof

Use (3.2) with `q=2`. The condition `max diag K<=q/2=1` is automatic because every ridge kernel is a positive semidefinite contraction. Thus

`beta=theta/4 >=201/400`.                                      (4.3)

Choose

`s=399/200<2`,
`p=s/(s-1)=399/199>2`.                                        (4.4)

Then

`beta s >=(201/400)(399/200)=80199/80000>1`.                  (4.5)

For `q=2`, (3.5) gives

`t_0<=pi sqrt(e)/(2g)`.                                       (4.6)

Raise (3.6) to the `s` power and integrate:

`int_R |phi_R(t)|^s dt
 <=2t_0 (beta s)/(beta s-1)
 <=2t_0 *80199/199.`                                          (4.7)

Inverse Hausdorff-Young therefore gives an `L^p` density for `R` with

`||p_R||_p
 <=(2pi)^(-1/s)
   (int |phi_R|^s)^(1/s).`                                    (4.8)

Now complete the square only in the original independent pivot coordinate. The full form has the exact representation

`Q=R+a V^2`,                                                   (4.9)

where, conditional on all remaining original coordinates, `V` is a translate of the pivot input. Hence, conditional on `R=r`, `V` is a mixture of such translates and has density at most one. This is a dependence-safe statement; no convolution independence is asserted.

For completeness, the one-sided Abel estimate used in the preceding B08 run is rederived. Conditional square-pushforward gives

`p_Q(t)
 <=|a|^(-1/2)
   int_0^infinity p_R(t-sign(a)y)y^(-1/2)dy.`                 (4.10)

For any `rho>0`, Holder on `(0,rho)` with conjugate exponent `s` and the mass-one bound on `(rho,infinity)` give

`p_Q(t)
 <=|a|^(-1/2)
   [(1-s/2)^(-1/s)||p_R||_p rho^(1/s-1/2)
      +rho^(-1/2)].`                                          (4.11)

Choose `rho=||p_R||_p^(-s)`. Then

`||p_Q||_infinity
 <=|a|^(-1/2)
   [(1-s/2)^(-1/s)+1]
   ||p_R||_p^(s/2).`                                          (4.12)

Using (4.7)-(4.8),

`||p_R||_p^(s/2)
 <=(2pi)^(-1/2)
   [2t_0(80199/199)]^(1/2).`                                  (4.13)

Since `1-s/2=1/400`, combine (4.6), (4.12), (4.13), and `g=gamma/16` to obtain exactly (4.2). QED.

The theorem proves absolute continuity and essential boundedness. The final dependence-safe `L^p` Abel step is not used here to assert continuity.

This theorem is structurally important: once the fine-scale effective dimension has a fixed margin above two, **all** ridge leverage localization becomes irrelevant.

## 5. New branch II: the previous 99-percent closure is symmetric between the two physical sides

Suppose now

`theta <201/100`.                                               (5.1)

The inherited lower bound (2.4) still holds. Put

`q=99/50`,
`s=999/500`.                                                   (5.2)

If either

`max_i (K_L)_ii <=99/100`                                     (5.3L)

or

`max_j (K_R)_jj <=99/100`,                                    (5.3R)

then orient the graph inequality from that side. Condition (3.1) is exactly satisfied because `q/2=99/100`. From (2.4),

`beta=theta/(2q)>=6400/12771`,
`beta s>=2368/2365>1`.                                        (5.4)

The same `L^s -> L^p -> physical-square` calculation from the preceding run gives

`boxed(
 ||p_Q||_infinity
 <= C_99/sqrt(|a| gamma),

 C_99=(1000^(500/999)+1)
      sqrt[(189440/3)sqrt(e/99)]
 <3349.
)`                                                             (5.5)

This yields the genuinely new symmetric conclusion:

> In an unpaid nonzero-pivot branch with `theta<201/100`, **both** physical sides of the fine-scale ridge matrix must contain a row/column of leverage greater than `99/100`.

The proof is not a rotation of the independent input law; it merely interchanges the two original-coordinate blocks in the already proved graph inequality.

## 6. New branch III: a two-sided near-coloop forces an intersection exterior-volume bank

We now analyze exactly the only branch not paid by Sections 4-5. Thus

`256/129 <=theta<201/100`,                                    (6.1)

and there exist a physical row index `j` and physical column index `r` with

`ell:=(K_L)_jj>99/100`,
`m:=(K_R)_rr>99/100`.                                         (6.2)

Set

`Z=H(g^2 I+H^T H)^(-1/2)`.

By the singular-value functional calculus,

`Z=(g^2 I+H H^T)^(-1/2)H`,                                   (6.3)

and therefore

`K_L=ZZ^T`, `K_R=Z^T Z`.                                      (6.4)

The indices of `Z` remain the original physical row and column indices.

For row index `j`, define the normalized row-incidence exterior mass

`A_j=
 sum_(k!=j) sum_(u<v)
   det Z[{j,k},{u,v}]^2.`                                     (6.5)

Cauchy-Binet gives

`A_j=sum_(k!=j) det K_L[{j,k}]
    =ell theta-(K_L^2)_jj.`                                   (6.6)

Since `0<=K_L<=I`, `K_L^2<=K_L`, so

`A_j>=ell(theta-1).`                                          (6.7)

Similarly, for the heavy physical column `r`,

`B_r=
 sum_(i<k) sum_(s!=r)
   det Z[{i,k},{r,s}]^2
 >=m(theta-1).`                                                (6.8)

Let the total normalized two-volume be

`E_2(Z)=
 sum_(i<k) sum_(u<v) det Z[{i,k},{u,v}]^2.`                   (6.9)

If `mu_nu` are the eigenvalues in (2.6), Cauchy-Binet gives

`E_2(Z)=e_2(mu)
       =(theta^2-tr K_L^2)/2.`                                (6.10)

Moreover

`tr K_L^2 >=(K_L^2)_jj>=ell^2>(99/100)^2`,                   (6.11)

so

`E_2(Z)<[theta^2-(99/100)^2]/2.`                              (6.12)

Finally define the **intersection** bank, consisting only of normalized `2x2` minors that simultaneously contain the heavy physical row and heavy physical column:

`C_jr=
 sum_(k!=j) sum_(s!=r)
   det Z[{j,k},{r,s}]^2.`                                     (6.13)

The union of the minors counted by `A_j` and `B_r` is a subset of all minors counted by `E_2(Z)`. Hence elementary inclusion-exclusion yields

`C_jr >=A_j+B_r-E_2(Z).`                                      (6.14)

Put `p=99/100`. From (6.2), (6.7), (6.8), (6.12),

`C_jr>
 2p(theta-1)-[theta^2-p^2]/2
 =:F(theta).`                                                  (6.15)

Now

`F'(theta)=2p-theta=99/50-theta<0`                            (6.16)

throughout the interval (6.1), because

`256/129-99/50=29/6450>0`.                                   (6.17)

Therefore the worst value is the upper endpoint `201/100`, and exact arithmetic gives

`F(201/100)
 =2(99/100)(101/100)
  -[(201/100)^2-(99/100)^2]/2
 =2349/5000.`                                                  (6.18)

We have proved:

### Theorem 6.1 — `QFORM-TWO-SIDED-NEAR-COLOOP-INTERSECTION-v1`

In the only nonzero-pivot fine-scale branch not paid by Sections 4-5,

`boxed(
 sum_(k!=j) sum_(s!=r)
 det Z[{j,k},{r,s}]^2
 >2349/5000=0.4698.
)`                                                             (6.19)

Thus the surviving case is not merely “one heavy row.” It contains a **specific heavy physical row and a specific heavy physical column joined by more than 0.4698 units of regularized two-dimensional determinant mass**. This is an aggregate-before-inversion certificate and does not select a tiny minor.

## 7. Pulling simultaneous one-sided currency back to the actual cross block

The normalized intersection bank (6.19) is useful at the ridge/DPP level. In addition, each heavy side supplies a large actual-`H` exterior reserve.

From (6.7), (2.4), and `ell>99/100`,

`A_j>
 (99/100)(256/129-1)
 =4191/4300.`                                                  (7.1)

Write

`R_g=(g^2I+H^T H)^(-1/2)`, so `Z=H R_g` and `||R_g||<=1/g`.
For every physical row pair,

`||z_j wedge z_k||^2
 <=g^(-4)||h_j wedge h_k||^2.`                                (7.2)

Summing and using `g=gamma/16` yields

`boxed(
 sum_(k!=j) ||h_j wedge h_k||^2
 > (4191/281804800) gamma^4.
)`                                                             (7.3)

Equivalently,

`sum_(k!=j) sum_(u<v)
 det H[{j,k},{u,v}]^2
 > (4191/281804800) gamma^4.`                                  (7.4)

Use the second representation in (6.3) and transpose the argument. The heavy column `r` also gives

`boxed(
 sum_(s!=r) ||c_r wedge c_s||^2
 > (4191/281804800) gamma^4,
)`                                                             (7.5)

where `c_s` denotes column `s` of the actual physical cross block `H`. Equivalently,

`sum_(s!=r) sum_(i<k)
 det H[{i,k},{r,s}]^2
 > (4191/281804800) gamma^4.`                                  (7.6)

The row currency (7.3) is unchanged if arbitrary other rows are sheared by multiples of row `j`, because

`h_j wedge(h_k-d_k h_j)=h_j wedge h_k`.                       (7.7)

The column currency (7.5) has the dual invariance under arbitrary column shears through column `r`. Hence the surviving branch carries **simultaneous left and right shear-invariant transverse two-volume**.

This is stronger structural information than the previous one-sided near-coloop certificate and is tailored to the fleet's current grouped-coordinate / aggregate-determinant program.

## 8. Combined exhaustive nonzero-pivot theorem

Sections 4-7 combine into the following exact trichotomy.

### Theorem 8.1 — `QFORM-SYMMETRIC-RIDGE-OR-BICOLOOP-v1`

Assume the inherited O0 transverse reserve (2.1), take `g=gamma/16`, and let the selected original physical scalar pivot satisfy `a!=0`. Then **at least one** of the following holds:

1. **Above-two ridge branch:** `theta>=201/100`, and

   `||p_Q||_infinity <1543/sqrt(|a|gamma)`.

2. **One-side diffuse branch:** `theta<201/100` and at least one of `K_L,K_R` has maximum diagonal at most `99/100`; then

   `||p_Q||_infinity <3349/sqrt(|a|gamma)`.

3. **Two-sided near-coloop bank:** `theta<201/100`, and there are a physical row `j` and physical column `r` with ridge leverages above `99/100` for which the normalized intersection bank satisfies (6.19), while the actual cross block simultaneously satisfies (7.3) and (7.5).

The first two branches establish absolute continuity and essential boundedness. Continuity is **not** claimed from their final dependence-safe `L^p` square step. The third branch is a quantitative structural reduction, not yet a density bound.

This is exhaustive inside the inherited nonzero-pivot O0 branch. It narrows the remaining mechanism to a genuinely **two-sided** near-coloop grouped bank instead of a generic localized residual.

## 9. Compatible completed account04 mathematics applied to an actual inequality

The designated `account04/B08` current-QFORM handoff and canonical math directory were absent at the fresh source checks in this run, so no designated-partner result is fabricated.

A completed compatible account04 theorem was nevertheless applied at an actual inequality, as required by the cross-worker protocol. The source is account04/B18:

`yspennstate/math-open-problems@0e80922c4f26f72fe3bb2b06728dd7a40da0c765`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T113729Z-account04-B18-qform-r1/REPORT.md`.

Its `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1` says that if a base residual has density cap `M` and the completed physical square has coefficient `a!=0`, with conditional translated-coordinate density cap one, then

`||p_Q||_infinity <=2 sqrt(M/|a|).`                            (9.1)

At any ridge scale `h`, the completed ridge theorem with `q=2` gives, whenever `theta_h>4`,

`M<=sqrt(e)/(2h) * theta_h/(theta_h-4).`                       (9.2)

Combining (9.1)-(9.2) gives the concrete full-form inequality

`boxed(
 ||p_Q||_infinity
 <=2 [sqrt(e)/(2|a|h)
       *theta_h/(theta_h-4)]^(1/2).
)`                                                             (9.3)

For example, at the present fine scale `h=g=gamma/16`, if `theta_g>=5`,

`boxed(
 ||p_Q||_infinity
 <=4 sqrt(10)e^(1/4)/sqrt(|a|gamma)
 <16.25/sqrt(|a|gamma).
)`                                                             (9.4)

This is a genuine mathematical use of completed account04 work on the same original-coordinate pivot geometry. It is not needed for Theorem 8.1's near-two threshold, because account04/B18 starts from an `L^infinity` residual while Theorem 4.1 deliberately uses an `L^p` residual with effective dimension only slightly above two.

## 10. What remains and why this is target-relevant

The full QFORM conjecture remains **OPEN / not proved / not disproved**.

Within this B08 structural line, the nonzero-pivot O0 debt is now sharply localized. A branch can fail both quantitative density mechanisms only if it has:

* effective ridge dimension in the narrow interval
  `256/129 <=theta<201/100`;
* a left physical ridge coloop above `99%`;
* a right physical ridge coloop above `99%`;
* normalized `2x2` determinant mass above `2349/5000` simultaneously incident to those two heavy indices;
* actual shear-invariant row and column exterior reserves each at least
  `(4191/281804800)gamma^4`.

This is precisely the kind of grouped two-coordinate bank that the rank-two affine half-Riesz theorem and the fleet's aggregate-before-inversion mechanisms can potentially consume. The next B08 mechanism should therefore **not** continue lowering the leverage threshold. It should attack the bank (6.19) directly: group the minors incident to `(j,r)` before any reciprocal determinant is taken, preserve the original coordinate product law, and feed the resulting rank-two fractional potential into the physical square. The zero/near-zero first-pivot branch remains a separate debt; the newer conditional `L^4 * L^(4/3)` null-coloop theorem is the appropriate endpoint input there.

No claim is made that a single minor in (6.19) is uniformly large. Such a claim would reintroduce the dimension-loss mechanism already refuted elsewhere. The advance is the dimension-free **aggregate** itself.

## 11. Exact arithmetic check

The standard-library script `verify.py` beside this report verifies the rational thresholds and displayed numerical constants. In particular it checks

* `theta_min=256/129>99/50`;
* `(201/400)(399/200)=80199/80000>1`;
* the Fourier tail ratio is exactly `80199/199`;
* the two-sided intersection reserve is exactly `2349/5000`;
* the normalized one-sided reserve is exactly `4191/4300`;
* after `g=gamma/16`, the actual-`H` coefficient is exactly `4191/281804800`;
* `C_hi=1542.062070218...<1543`;
* `C_99=3348.239468358...<3349`;
* the account04/B18 `theta>=5` constant is `16.241779561...<16.25`.

The captured output terminates with

`QFORM_SYMMETRIC_RIDGE_BICOLOOP_CHECK_PASS`.

The checker validates arithmetic only; the universal mathematical proof is the exact derivation above.
