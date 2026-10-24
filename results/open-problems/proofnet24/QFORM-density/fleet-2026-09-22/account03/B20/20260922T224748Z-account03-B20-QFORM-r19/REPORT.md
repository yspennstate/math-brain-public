# account03/B20 QFORM r19 — double-anchor Schur-compound compression

Run: `20260922T224748Z-account03-B20-QFORM-r19`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: proof closure and keeper  
Classification: **ESSENTIAL_STEP_APPLIED / O0-DOUBLE-ANCHOR-COMPACT-RESOURCE / FULL_TARGET_OPEN**  
Execution label: `WITHOUT_VERIFIED_BRAIN` (`full_brain_connected=false`).

## 1. Target and correction discipline

The target is unchanged: for every finite `n`, every independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove that `Q=X^T A X` has a density with one universal finite essential-supremum bound, or give a valid counterexample. Continuity is tracked separately.

No Gaussian, moment, log-concavity, compact-support, connected-support, iid, diagonal-basis, or post-rotation-independence assumption is introduced. The argument below does not use the refuted law-uniform pointwise quadratic-phase decay, arbitrary-joint rank-three coarea, conditional projection-density supremum/moment, unrestricted fiber-supremum, or a bare inference from global spectrum to one good coordinate minor.

The fresh proof frontier consumed here is account01/B20 r21, canonical source `yspennstate/math-open-problems@1c48a0b1da1bccc41b5768524d08db8f3d2308dc`, report `proofnet24/QFORM-density/fleet-2026-09-22/account01/B20/20260922T222136Z-account01-B20-QFORM-r21/REPORT.md`. Its fractional volume-sampling Brascamp--Lieb theorem pays the O0 third-compound branch whenever either orientation has maximum third-minor volume marginal at most `2/3`. Therefore every unpaid O0 state admits a physical cross block `B=A[L,R]`, with

`Z:=E_3(B)=sum_{|S|=|T|=3} det(B[S,T])^2 >=1/256`,

and physical anchors `i in L`, `a in R` satisfying row/column volume marginals

`alpha_i>2/3`, `beta_a>2/3`.

Consequently the squared third-minor mass through both anchors obeys

`Z_ia:=sum_{S contains i,T contains a} det(B[S,T])^2 > Z/3 >=1/768`.   (1.1)

The point of this run is to compress that two-anchor/four-bank packet into a sharper exact algebraic resource before any reciprocal or local minor is paid.

## 2. Anchored block notation

Permute the chosen physical row `i` and physical column `a` to the first positions and write

`B = [[b, r^T], [c, D]]`,                                             (2.1)

where `b=B_ia`, `r` is the remainder of the anchor row, `c` the remainder of the anchor column, and `D` the residual physical cross block. All coordinates remain original physical coordinates; this is only a permutation.

For any real matrix `M`, write

`E_k(M)=sum_{|I|=|J|=k} det(M[I,J])^2`.

By Cauchy--Binet, `E_k(M)=e_k(sigma_1(M)^2,sigma_2(M)^2,...)`.

## 3. New theorem: exact double-anchor Schur-compound compression

### Theorem `QFORM-O0-DOUBLEANCHOR-SCHUR-COMPOUND-v1`

Assume (1.1).

### (A) Nonzero anchor edge

If `b!=0`, define the rectangular Schur bank

`S := D - c r^T/b`.                                                  (3.1)

Then for every residual two-row set `J` and two-column set `K`,

`det B[{i} union J,{a} union K] = b det S[J,K]`.                      (3.2)

Hence

`boxed( Z_ia = b^2 E_2(S) >1/768. )`                                 (3.3)

In particular

`boxed( |b| sqrt(E_2(S)) > 1/sqrt(768) =0.0360843918... . )`          (3.4)

Since `E_2(S)<=||S||_F^4/2`, also

`boxed( |b| ||S||_F^2 >1/sqrt(384)=0.0510310363... . )`               (3.5)

Thus, for example,

`|b|<=1/8  =>  E_2(S)>1/12`.                                         (3.6)

Moreover the exact third-minor volume law conditioned on the two outer anchors becomes the exact second-minor volume law of `S`:

`P(J,K | i in S_3, a in T_3)= det(S[J,K])^2/E_2(S)`.                 (3.7)

Here `S_3,T_3` denote the random row/column triples in the original third-minor volume law; the overloaded matrix symbol `S` in (3.7) is distinguished by context.

### (B) Zero anchor edge

If `b=0`, then

`boxed( Z_ia <= ||c||_2^2 ||r||_2^2 ||D||_F^2. )`                    (3.8)

Consequently every unpaid zero-anchor state satisfies the dimension-free three-resource product

`boxed( ||c||_2 ||r||_2 ||D||_F >1/sqrt(768). )`                     (3.9)

Thus the fresh O0 double-anchor obstruction is reduced exactly to either a nonzero physical anchor edge times a **second compound** Schur resource, or a zero-edge **two-star times residual-bank** resource.

### Proof of (A)

For fixed residual `J,K` of cardinality two, the selected `3x3` block is

`[[b, r_K^T],[c_J,D_JK]]`.

Because `b!=0`, the scalar Schur determinant formula gives

`det [[b,r_K^T],[c_J,D_JK]]
 = b det(D_JK-c_J r_K^T/b)
 = b det S[J,K]`,

which is (3.2). Squaring and summing over all residual `J,K` gives (3.3). Equation (3.4) is immediate from (1.1).

For nonnegative squared singular values `u_nu=sigma_nu(S)^2`,

`E_2(S)=sum_{mu<nu}u_mu u_nu
       <= (1/2)(sum_nu u_nu)^2
       =(1/2)||S||_F^4`,

so (3.5) follows from (3.3); (3.6) is the specialization `b^2<=1/64`.

Finally, conditioning the original volume weights on the event that the chosen row and column anchors occur cancels the common factor `b^2` in (3.2), proving (3.7). No probabilistic independence claim is made about Schur-rotated variables; (3.7) is only a statement about the deterministic squared-minor measure.

### Proof of (B)

For `b=0`, the anchor-containing minor array can be written invariantly as the Hilbert--Schmidt tensor obtained by wedging `D` with `c` on the row side and with `r` on the column side. Concretely, for residual rows `j<k` and columns `p<q`,

`det [[0,r_p,r_q],[c_j,D_jp,D_jq],[c_k,D_kp,D_kq]]`

is the `(j wedge k,p wedge q)` coefficient of

`(c wedge) D (r wedge)^*`.                                           (3.10)

The wedge maps have operator norms `||c||_2` and `||r||_2`. Therefore the Hilbert--Schmidt ideal inequality gives

`Z_ia
 =||(c wedge)D(r wedge)^*||_HS^2
 <=||c||_2^2 ||D||_F^2 ||r||_2^2`,

which is (3.8). Combining with (1.1) proves (3.9). QED.

## 4. A second exact compression when the conditional two-volume law is concentrated

The nonzero-anchor branch has more structure. Let `mu` be the conditional second-minor law (3.7), and let `alpha'_j,beta'_k` be its row/column inclusion marginals. Thus `sum alpha'=sum beta'=2`.

If either orientation has maximum marginal at most `2/3`, retain that state as the **nested diffuse two-volume branch**. Suppose instead there are residual physical anchors `j,k` with

`alpha'_j>2/3`, `beta'_k>2/3`.                                      (4.1)

Then by the union bound under the *same joint second-minor law*,

`mu(j in J,k in K)>1/3`.                                             (4.2)

Define the incident second-minor matrix

`M_{ell m}=det S[{j,ell},{k,m}]`,                                   (4.3)

for residual `ell!=j,m!=k`. From (4.2),

`||M||_F^2 > E_2(S)/3`,

and after multiplying by (3.3),

`boxed( b^2 ||M||_F^2 >1/2304. )`                                  (4.4)

Write the second anchored decomposition

`S=[[s,u^T],[v,T_0]]`.                                               (4.5)

If `s=0`, then exactly

`M=-v u^T`,

so

`boxed( |b| ||v||_2 ||u||_2 >1/48. )`                               (4.6)

If `s!=0`, define the second rectangular Schur bank

`T=T_0-vu^T/s`.                                                      (4.7)

Then the `2x2` Sylvester identity gives `M=sT`, and therefore

`boxed( |b s| ||T||_F >1/48. )`                                     (4.8)

The factor `bs` is itself the genuine original-coordinate physical `2x2` cross minor

`b s = det B[{i,j},{a,k}]`.                                         (4.9)

Hence the concentrated nonzero-anchor survivor obeys the explicit dichotomy

`boxed( |det B[{i,j},{a,k}]|>1/48  or  ||T||_F>1. )`                 (4.10)

The second alternative follows whenever the first determinant is at most `1/48`, because their product is strictly larger than `1/48` by (4.8).

This is **not** the corrected-away claim that global spectral information directly selects one good physical minor. The physical `2x2` minor in (4.9) appears only after: (i) the source-valid O0 third-compound certificate, (ii) two heavy physical anchors under its exact third-minor volume law, and (iii) two further heavy anchors under the induced exact second-minor volume law.

## 5. Direct use of designated partner account04/B20

The newest completed designated-partner result remains account04/B20 r3, canonical source `yspennstate/math-open-problems@25ad8faaac5064b6814d51ae63d894fe97c1eac4`, theorem `QFORM-CROSS-DOMINATED-SECOND-SCHUR-CLOSURE-v1`.

Its exact scope is a source-valid physical outer pivot `|a|>=tau>=1/4` followed by an exact second-Schur row `(d,c)` satisfying

`||c||_2>|d|`, `||c||_2>tau/9`.

The current proof tree also has the complementary diagonal-dominated closure. Therefore whenever the new upstream O0 compression exits into a localized state with

`max{|d|,||c||_2}>tau/9`,                                           (5.1)

the cross-dominated half of (5.1) obeys

`||c||_2>|d|  =>  ||c||_2>tau/9`,

so the account04/B20 theorem applies at the actual inequality and yields

`boxed( ||p_Q||_infinity <5262. )`                                  (5.2)

The diagonal-dominated half is already paid by the completed complementary result. Thus no work should return to that downstream high-window state; the remaining debt is genuinely upstream in the new compact O0 resources (3.3)/(3.9)/(4.6)/(4.8). I do not extend the account04 theorem outside its stated pivot hypotheses.

## 6. What this run changes

Account01/B20 r21 replaced the older O0 singleton-plus-five-bank state by a two-anchor/four-bank packet. The present theorem compresses that packet further without a coloring loss:

1. **nonzero outer anchor edge:** exact resource `b^2 E_2(S)>1/768` and exact conditional `E_2` volume law;
2. **zero outer anchor edge:** exact source-valid product lower bound `||c||||r||||D||_F>1/sqrt(768)`;
3. **nonzero edge + doubly concentrated conditional `E_2` law:** either a zero-second-anchor two-star product `|b|||u||||v||>1/48`, or a genuine physical `2x2` cross minor times a second Schur-bank Frobenius norm `>1/48`.

This is a structural/proof-interface advance, not yet the final density theorem. It preserves every arbitrary same-side block and the original-coordinate provenance; no Schur-complement coordinate is treated as an independent random variable.

## 7. First unpaid implication

The first unpaid synthesis target is now

`QFORM-O0-ANCHOR-SHEAR-PAYMENT-v1`:

pay, without post-shear independence, the compact alternatives above:

- the zero-anchor `||c||||r||||D||_F>1/sqrt(768)` state;
- the nonzero-anchor `b^2 E_2(S)>1/768` state when the induced `E_2` volume law is diffuse on at least one side;
- the nested endpoints (4.6)/(4.8), preferably by an integrated-Fourier or conditional-shear estimate that spends the aggregate bank before any reciprocal local minor.

Any source-valid localization satisfying (5.1) is already removed by the account04/account01 second-Schur closures and should not be re-audited.

The unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. This run proves no new full-target continuity statement. The new result is deterministic matrix/proof-interface mathematics; continuity remains only on previously completed branches with genuinely integrable characteristic-function estimates.
