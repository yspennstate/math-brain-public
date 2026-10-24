SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B08, 2026-09-23T02:06:20.291113Z.
attacking: the remaining actual-spectral hybrid after the diffuse curvature-transfer gate, using completed 3-volume/5-volume Fourier payments to isolate only low-cross-rank or two-sided anchored survivors.

# account02/B08 — diffuse hybrid volume-tail ladder

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Diffuse eigenvector case  
**Result:** `QFORM-DIFFUSE-HYBRID-VOLUME-TAIL-LADDER-v1`  
**Classification:** `ESSENTIAL_STEP_APPLIED / PROVED SUPPORTING STRUCTURAL THEOREM / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture is not proved here. The result below is a quantitative original-coordinate reduction of the diffuse `k=0,1,2` child-curvature hybrids. It introduces no moments, support assumptions, log-concavity, iid hypothesis, diagonal-basis reduction, or independence after spectral rotation. Arbitrary same-side blocks and arbitrary complementary spectrum remain in the actual matrix throughout.

## 1. Source pins actually used

### 1.1 Designated partner account03/B08

I use the completed account03/B08 theorem `QFORM-DIFFUSE-CURVATURE-TRANSFER-LADDER-v1`, commit

`b588302bae921f92fa9f1af9c04f44ad113facb8`.

Let `R` be three genuine orthonormal eigenvectors of `A`, with eigenvalues of magnitude at least `L`. If their maximum original-coordinate row leverage is at most `1/48`, the partner theorem supplies a balanced physical cut `I|J`. Put

`c0=(L/2)sqrt(3/5)`,
`beta=(3L/16)sqrt(3/5)=0.145236875482778... L`.                 (1.1)

If `k_I` is the number, capped at three, of ACTUAL eigenvalues of `A[I,I]` with modulus at least `c0`, then for `k_I=0,1,2` the ACTUAL cross block

`B=A[I,J]`

satisfies respectively

`s_3(B)>beta`, `s_2(B)>beta`, `s_1(B)>beta`.                    (1.2)

No uncancelled rank-three component is substituted for `B`.

### 1.2 Newest-Claude completed Fourier package

At the owner-requested source snapshot

`e5f71d79eff325201dd0274053d20268ce65b837`

I use two proved results from `RESULTS.md` / `FOURIER_ROUTE_REPORT.md`.

**D' (three-volume):** if `Z_3=e_3(B^T B)` and, in one orientation, every squared-3-minor row marginal is at most `h<3/4`, then

`||p_Q||_inf <= C_D(h) Z_3^(-1/6)`,
`C_D(h)=6 sqrt(e)(2h)^(-1/2)(3-4h)^(-1)`.                       (1.3)

The full ambient same-side quadratic blocks and affine terms are arbitrary. I use

`h=5/8`, `C_D(5/8)=24 sqrt(e)/sqrt(5)=17.6959336187...`.        (1.4)

**D_5 (five-volume):** with `Z_5=e_5(B^T B)`, with no marginal condition at all,

`||p_Q||_inf <= 5 sqrt(2e) Z_5^(-1/10)`.                       (1.5)

Both are characteristic-function estimates in the original product coordinates and give a continuous density.

### 1.3 Latest collective-tail continuation

I also read the current `PEER_TAIL_EXTENSION.md` at

`c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`.

Its stronger two-leading-directions plus collective-tail theorem is useful as an optional sharpening, but its source says independent review is pending. The main theorem below therefore does **not** depend on it: the high-stable-rank tail is instead paid using the already completed D_5 theorem.

## 2. A no-marginal two-cross compiler

This is the first new implication of the run.

Let the singular values of an arbitrary physical cross block `B` be

`s_1>=s_2>=s_3>=...>=0`.

Assume

`s_2>=b>0`.                                                       (2.1)

Put

`T_2=sum_(j>=3) s_j^2`,                                         (2.2)

and fix `0<theta<=1`.

### Theorem 2.1 — `QFORM-TWO-CROSS-VOLUME-TAIL-COMPILER-v1`

At least one of the following occurs.

**(TUBE2)**

`T_2<theta^2 b^2`,                                               (2.3)

so the best rank-two truncation `B_2` satisfies

`||B-B_2||_F<theta b`.                                           (2.4)

**(D5-TAIL)**

The full ambient form has a continuous density with

`||p_Q||_inf
 <= K_5 /(b theta^(3/5)),`                                      (2.5)

where

`K_5=5 sqrt(2e)(225/37)^(1/10)=13.9646585917...`.               (2.6)

**(D3-VOLUME)**

The full ambient form has a continuous density with

`||p_Q||_inf
 <= [C_D(5/8) 15^(1/3)]/[b theta^(1/3)]`.                       (2.7)

**(BICOLOP)**

For the canonical squared-3-minor probability law

`w_(S,T)=det(B[S,T])^2/Z_3`,                                    (2.8)

there are an original physical row `i` and original physical column `j` such that

`P_w(i in S)>5/8`, `P_w(j in T)>5/8`,                           (2.9)

and therefore

`P_w(i in S and j in T)>1/4`.                                  (2.10)

Thus more than one quarter of the complete squared three-volume is incident simultaneously to one physical row and one physical column.

### Proof

Assume (TUBE2) fails, so

`T_2>=theta^2 b^2`.                                              (2.11)

First suppose

`s_3^2<=T_2/225`.                                                (2.12)

Let `x_j=s_j^2`, `j>=3`, and `S=T_2`. Then `max x_j<=S/225` and

`sum x_j^2 <= (S/225)S=S^2/225`.

The elementary identity

`6 e_3(x)=S^3-3S sum x_j^2+2 sum x_j^3`                          (2.13)

therefore gives

`e_3(x)>= (37/225)S^3`.                                         (2.14)

The full five-volume contains the positive subset consisting of the top two singular values and three tail singular values:

`Z_5=e_5(B^T B)
 >= s_1^2 s_2^2 e_3(x)
 >= b^4 (37/225) T_2^3
 >= (37/225) theta^6 b^10`.                                     (2.15)

D_5 gives (2.5).

Now suppose instead

`s_3^2>T_2/225`.                                                 (2.16)

Then by (2.11),

`s_3>theta b/15`.                                                (2.17)

Hence

`Z_3=e_3(B^T B)
 >=s_1^2s_2^2s_3^2
 >theta^2 b^6/225`.                                              (2.18)

If the left 3-volume marginals are all at most `5/8`, apply D' directly. If not, transpose `B`; if the right marginals are all at most `5/8`, apply D' after transposition. In either case (1.3), (1.4), and (2.18) give (2.7).

The only remaining possibility is that a left row marginal and a right column marginal both exceed `5/8`. For those `i,j`, the union bound under the same probability law `w` gives

`P_w(i in S,j in T)
 >=P_w(i in S)+P_w(j in T)-1
 >1/4`,                                                         (2.19)

which is (BICOLOP). These cases exhaust all possibilities. QED.

### Clean scale

With `theta=1/8`, (2.5) and (2.7) become respectively

`||p_Q||_inf <334.817/beta_scale`,
`||p_Q||_inf <600.976/beta_scale`,                               (2.20)

when `b=beta_scale`. More precisely the displayed numerical constants multiply `beta/b` if `beta_scale=beta`.

The key gain over the preceding run is that the high-stable-rank collective tail no longer needs any top-two coordinate-leverage gate: D_5 pays it before a heavy coordinate is selected.

## 3. One-cross high-tail compiler

The `k_I=2` hybrid supplies only one uniformly strong individual cross singular value. A second finite step still reduces it to the preceding theorem or a genuinely low-rank tube.

Assume

`s_1>=b>0`,                                                      (3.1)

and put

`T_1=sum_(j>=2)s_j^2`.                                          (3.2)

Fix `0<theta<=1`.

If

`T_1<theta^2 b^2`,                                               (3.3)

then the best rank-one truncation obeys

`dist_F(B,{rank<=1})<theta b`.                                  (3.4)

Assume (3.3) fails. If

`s_2^2<=T_1/225`,                                                (3.5)

write the tail squared singular values as `x_j=s_j^2`, `j>=2`, with sum `S=T_1` and maximum at most `S/225`. The recurrence

`r e_r(x)
 =sum_(|E|=r-1) product_(i in E)x_i [S-sum_(i in E)x_i]`          (3.6)

gives

`e_4(x)>=c_4 S^4`,                                               (3.7)

where

`c_4=[(1-1/225)(1-2/225)(1-3/225)]/24
    =0.0405645871056...`.                                        (3.8)

Therefore

`Z_5>=s_1^2e_4(x)
 >=c_4 theta^8 b^10`,                                            (3.9)

and D_5 gives

`||p_Q||_inf
 <=K_4/(b theta^(4/5)),`                                        (3.10)

with

`K_4=5sqrt(2e)c_4^(-1/10)=16.0626626053...`.                    (3.11)

If (3.5) fails, then

`s_2>sqrt(T_1)/15>=theta b/15`,                                  (3.12)

so Theorem 2.1 applies with the guaranteed second-cross scale

`b_2=theta b/15`.                                                (3.13)

This proves an exhaustive one-cross-to-two-cross reduction with no perturbative deletion of the tail.

## 4. Apply the compilers to the actual spectral gate

Return to the designated-partner cut (1.1)-(1.2), and take

`theta=1/8`.                                                      (4.1)

### 4.1 `k_I=0`: no child direction

The partner theorem gives `s_3(B)>beta`, hence

`Z_3>beta^6`.                                                     (4.2)

If either orientation has all 3-volume marginals at most `5/8`, D' gives

`boxed: ||p_Q||_inf <121.842/L.`                                 (4.3)

Otherwise (BICOLOP) holds, now with anchored squared-three-volume greater than `Z_3/4>beta^6/4`.

### 4.2 `k_I=1`: one child direction + two cross directions

The partner theorem gives `s_2(B)>beta`. Apply Theorem 2.1 with `b=beta`, `theta=1/8`.

Thus at least one of:

1. `dist_F(B,{rank<=2})<beta/8=0.0181546094353... L`;             (4.4)
2. `||p_Q||_inf<334.817/L` by D_5;                               (4.5)
3. `||p_Q||_inf<600.976/L` by D';                               (4.6)
4. a physical row/column pair carries more than one quarter of the complete squared three-volume. (4.7)

So the former undifferentiated one-child/two-cross hybrid is now paid except for a quantitatively tight near-rank-two tube or a two-sided physical volume anchor.

### 4.3 `k_I=2`: two child directions + one cross direction

The partner theorem gives `s_1(B)>beta`.

Apply Section 3 with `b=beta`, `theta=1/8`.

If the first tail is small,

`dist_F(B,{rank<=1})<beta/8`.                                    (4.8)

If the first tail has stable rank at least `225`, (3.10) gives

`boxed: ||p_Q||_inf<583.731/L.`                                  (4.9)

Otherwise (3.12) yields

`s_2(B)>beta/120`.                                                (4.10)

Apply Theorem 2.1 a second time, now at `b=beta/120` and with its own parameter `theta_2=1`. Then at least one of:

`dist_F(B,{rank<=2})<beta/120
 =0.00121030729569... L`,                                       (4.11)

or a continuous density bound

`||p_Q||_inf<11538.110/L`                                       (4.12)

from D_5, or

`boxed: ||p_Q||_inf<36058.550/L`                                (4.13)

from D', or the same two-sided BICOLOP condition (2.9)-(2.10).

Hence the full `k_I=2` hybrid is paid outside only:

* a `beta/8` Frobenius tube around rank one;
* a `beta/120` Frobenius tube around rank two; or
* a two-sided physical 3-volume anchor.

No dimension enters any threshold.

## 5. Exact identity on the two-sided anchored survivor

The BICOLOP branch can be passed to the Schur/grouped-coordinate workers without selecting one good minor.

Fix the physical anchor row `i` and column `j` and write the actual cross block as

`B=[[z,a^T],[b,C]]`,                                             (5.1)

where `z=B_ij`.

Define the anchored third-volume bank

`W_ij^(3)
 =sum_(K subset I\{i}, |K|=2)
   sum_(T subset J\{j}, |T|=2)
   det B[{i} union K,{j} union T]^2`.                            (5.2)

The BICOLOP conclusion is

`W_ij^(3)>Z_3/4`.                                                (5.3)

### Proposition 5.1 — `QFORM-HYBRID-BICOLOP-SCHUR-E2-IDENTITY-v1`

If `z!=0`, let

`S=C-ba^T/z`                                                     (5.4)

be the exact scalar Schur cross residual. Then

`boxed: W_ij^(3)=z^2 e_2(S^T S).}`                               (5.5)

Indeed, for every two-row set `K` and two-column set `T`, the scalar block determinant formula gives

`det B[{i} union K,{j} union T]
 =z det S[K,T]`.                                                 (5.6)

Square and sum; Cauchy--Binet identifies the sum of squared `2x2` minors of `S` with `e_2(S^T S)`. QED.

Thus the anchored survivor has an exact aggregate Schur currency:

`z^2e_2(S^TS)>Z_3/4`.                                           (5.7)

This is precisely aggregate-before-inversion. A very small nonzero anchor does not destroy the certificate; it forces the Schur residual's second exterior energy to increase. The exact-zero anchor `z=0` remains a distinct star-type branch and is not silently replaced by a nonzero pivot.

For the `k_I=1` concentrated-tail branch, (2.18) and (5.7) give explicitly

`z^2e_2(S^TS)>theta^2 beta^6/900`.                              (5.8)

At `theta=1/8`, this is `>beta^6/57600`.

## 6. Source-valid witnesses show the low-rank survivors are genuine

Let `m` be a sufficiently large power of two and let `U` be any three normalized Sylvester-Hadamard columns in `R^m`. For `k=1` or `2`, put

`P_k=diag(1-delta,...,1-delta,1/5,...,1/5)`,                    (6.1)

with exactly `k` entries `1-delta`, and define

`C=UP_kU^T`,
`B=U(I-P_k)U^T`,
`A=[[C,B],[B,C]]`.                                               (6.2)

For `0<delta<=1/10`, the six nonzero spectral values are

`1,1,1`, together with `k` copies of `1-2delta` and `3-k` copies of `-3/5`. (6.3)

Therefore `A` has exactly three eigenvalues of modulus at least one. The selected three large eigenvectors are `(u_j,u_j)/sqrt(2)` and have maximum original-coordinate leverage

`3/(2m) ->0`.                                                     (6.4)

The child `C` has exactly `k` eigenvalues above the actual gate `c0`, while the cross singular values are

* `k=1`: `4/5,4/5,delta`;
* `k=2`: `4/5,delta,delta`.                                      (6.5)

Thus arbitrarily strong selected-eigenvector delocalization does **not** eliminate either the near-rank-two `k=1` survivor or the near-rank-one `k=2` survivor. They are genuine structural branches, not artifacts of loose constants.

They are not counterexamples to QFORM. The same family has full nonzero-range coordinate leverage `3/m<=1/2`; applying the completed rank-six Fresnel--Brascamp--Lieb theorem F from the owner-requested `e5f71d79...` package gives

`||p_Q||_inf
 <=6[(1-2delta)^k(3/5)^(3-k)]^(-1/6)`.                         (6.6)

For `delta<=1/10`, this is at most

`7.383334` for `k=1`, and `7.037678` for `k=2`.                 (6.7)

This real inequality explains the surviving difficulty correctly: the witnesses themselves are paid because their **whole** nonzero spectral range is diffuse. The unrestricted theorem permits an arbitrary additional spectral remainder that can make the whole-range projection completely localized while leaving only the selected three large eigenvectors diffuse. A valid mixed compiler must therefore retain that remainder rather than invoking (6.6) abstractly.

## 7. N3 interpretation

At the standard earlier B08 no-pivot scale `tau0=1/8192`, the physical diagonal/pair gates imply every off-diagonal coefficient obeys

`|A_ij|<eps0=sqrt(tau0+tau0^2)=0.0110492177850...`.             (7.1)

The present theorem does not need this entry cap. It is nevertheless useful for interpreting a future anchored/hub payment: a physical cross row of Euclidean norm `>beta/sqrt(2)` would require more than

`beta^2/(2eps0^2)=86.3894544...`                                 (7.2)

cap-sized entries at `L=1`, hence at least 87 nonzero coordinates. So the high-coordinate geometry is necessarily a grouped/broad bank, not a hidden one-pair localized certificate.

## 8. Exact remaining obligation

This run removes all diffuse-hybrid configurations except three sharply source-valid survivors:

1. **LOW-RANK-1:** in the two-child branch, an actual physical cross block within `beta/8` in Frobenius norm of rank one;
2. **LOW-RANK-2:** in the one-child branch, or after the second step of the two-child branch, an actual physical cross block within `beta/8` or `beta/120` of rank two;
3. **BICOLOP:** more than one quarter of all squared physical `3x3` cross-minor volume passes through one actual row and one actual column, with the exact nonzero-anchor identity (5.5).

The first unpaid implication is therefore

**`QFORM-DIFFUSE-LOWRANK-OR-BICOLOP-PAYMENT-v1` — OPEN.**

Use the retained actual child eigendirection(s) together with a near-rank-one/two cross bank, or use the exact anchored Schur `e_2` currency (5.5), to obtain a product-preserving density estimate without perturbatively deleting the small tail. The `z=0` anchored branch must remain separate. A naive continuity argument in the small quadratic tail is invalid for unrestricted cap-one sources.

The three-child `k_I=3` branch is also not declared solved by recursive descent: repeatedly accepting the fixed principal scale loss would accumulate a non-universal constant. It belongs to the partner's multiscale curvature-ledger obligation.

## 9. Checks and status

The accompanying deterministic checker verifies the constants, the Hadamard spectral formulas, the gate counts, and the low-rank thresholds. No simulation of the input laws is used.

Main status: `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_STRUCTURAL_THEOREM`.

Full target: `OPEN`.

Continuity: supplied in every D'/D_5/Theorem-F paid branch; not asserted for the unresolved low-rank or anchored survivors.
