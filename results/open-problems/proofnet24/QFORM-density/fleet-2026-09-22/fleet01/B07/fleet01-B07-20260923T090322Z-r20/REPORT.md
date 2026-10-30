SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B07, 2026-09-23T09:03:22Z.
attacking: coordinate-minor selection via a determinant-weighted anchored compound recursion intended to absorb the remaining rank-four Schur tube without choosing one tiny pivot.

# fleet01/B07 r20 — mixed-order determinant packets and a one-sided compiler for double-anchored third volume

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: coordinate minor selection / GEOMETRY  
Status: `ESSENTIAL_STEP_APPLIED / NEW MIXED E3-E2 FOURIER RECEIVER + DOUBLE-ANCHOR ONE-SIDED CORE COMPILER / FULL QFORM OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`.

## 1. Scope, corrections, and actual dependencies

The target remains unrestricted: for every `n`, independent original-coordinate real random variables with probability densities `f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove that `Q=X^TAX` has a density bounded by one universal constant, or give a valid target-level counterexample. No moment, support, iid, Gaussian, log-concavity, connected-support, or post-rotation independence assumption is introduced. Continuity is tracked separately.


Completed sources actually used:

1. Designated partner fleet02/B07, `QFORM-CROSS-FIBER-PLANCHEREL-v1`:
   `yspennstate/math-open-problems@5266d24ea98d9bb5902c51a92eca0e3e38112e39`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B07/20260922T193347Z-b07-639234ec/REPORT.md`.
   Its one-sided exact-rank-three form is applied at an actual inequality in Section 3.
2. The current fractional-volume Fourier proof:
   `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,
   `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.
   Section 2 below extends its determinant-expansion/BL mechanism to a geometric mean of *different compound orders* rather than invoking it as a black box.
3. Fresh fleet03/B07 r29 four-hub transducer:
   `yspennstate/math-open-problems@0e842117ca7ec8472538faa120677507f16b5c17`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260923T084007Z-fleet03-B07-qform-r29/REPORT.md`.
   Its live double-anchor third-volume lower bound is compiled in Section 4.

Full QFORM and global continuity remain OPEN.

## 2. New theorem: mix a third-volume packet with a second-volume packet before inversion

Let `I,J` be disjoint ORIGINAL-coordinate banks and let `M=A[I,J]`. Let `P_3` be any nonempty collection of `3 x 3` row/column minor pairs and `P_2` any nonempty collection of `2 x 2` row/column minor pairs. Put

`Z_3 = sum_((S,T) in P_3) det M[S,T]^2 > 0`,
`Z_2 = sum_((S,T) in P_2) det M[S,T]^2 > 0`.                 (2.1)

Normalize the squared determinants in each packet separately. Denote the corresponding row inclusion marginals by

`alpha_i^(3), alpha_i^(2)`

and the column inclusion marginals by

`beta_j^(3), beta_j^(2)`.

Thus

`sum_i alpha_i^(3)=sum_j beta_j^(3)=3`,
`sum_i alpha_i^(2)=sum_j beta_j^(2)=2`.                       (2.2)

Fix a mixing weight `0<w<1` and define

`r = 3w+2(1-w)=2+w`,                                          (2.3)
`p_i = w alpha_i^(3)+(1-w)alpha_i^(2)`,
`b_j = w beta_j^(3)+(1-w)beta_j^(2)`,
`c_j = 1-b_j`.                                                 (2.4)

Then `sum_i p_i=r` and `sum_j b_j=r`.

### Theorem 2.1 — `QFORM-MIXED-32-FRACTIONAL-COMPOUND-BL-v1`

Let `1<=q<r/2`. If

`max_i p_i <= q/2`,                                            (2.5)

then for the full ambient quadratic form, including arbitrary within-bank quadratic terms, all outside couplings, affine terms, signs and additional spectrum, the law has a continuous density satisfying

`boxed:
 ||p_Q||_infinity
 <= [ e r / ((r-2q)sqrt(q)) ]
    K_w^(-1/(2r)),
`                                                                  (2.6)

where

`K_w = w^(-w)(1-w)^(-(1-w)) Z_3^w Z_2^(1-w).`                 (2.7)

The same conclusion holds if the analogous gate is valid on the column side, by transposing `M`.

At the symmetric weight `w=1/2`, `r=5/2`. With `q=1`, (2.6) becomes

`boxed:
 ||p_Q||_infinity
 <= 5 e 2^(-1/5) (Z_3 Z_2)^(-1/10).
`                                                                  (2.8)

This theorem uses determinant *packets*, not one selected minor. It is useful precisely when a third-volume packet has a physical anchor that can be avoided by a complementary second-volume packet: the two packets jointly have effective compound order `2+w>2`, enough for an integrable Fourier envelope.

### Proof

Condition on all original coordinates outside `I union J`. The conditional phase can be written

`F(X_I)+2 X_I^T M X_J+G(X_J)`,                                (2.9)

where `F,G` are arbitrary real measurable functions finite almost surely; this includes all self blocks, conditioned outside couplings and affine terms.

Take an independent copy `X_J'` and write `D=X_J-X_J'`. Exactly as in the product-preserving decoupling argument of the fractional-volume theorem,

`|phi_Q(t)|^2
 <= integral [prod_i |psi_i(2t(Md)_i)|]
             [prod_j g_j(d_j)] dd,`                            (2.10)

where `psi_i` is the characteristic function of the original `i`th coordinate and `g_j=f_j*tilde f_j` has mass one and satisfies `0<=g_j<=1`.

We now derive a new Brascamp--Lieb determinant certificate from the two compound orders. Let `D_I=diag(d_i)` and `D_J=diag(e_j)` be positive Gaussian parameters. The standard diagonal-plus-Gram determinant expansion is

`det(D_J+M^T D_I M)
 = sum_(k>=0) sum_(|S|=|T|=k)
     det M[S,T]^2 prod_(i in S)d_i prod_(j notin T)e_j.`       (2.11)

Keep only the packet-3 and packet-2 sums and call them `S_3,S_2`. Weighted AM--GM with the normalized squared determinants gives

`S_3 >= Z_3 prod_i d_i^(alpha_i^(3))
              prod_j e_j^(1-beta_j^(3)),`                     (2.12)
`S_2 >= Z_2 prod_i d_i^(alpha_i^(2))
              prod_j e_j^(1-beta_j^(2)).`                     (2.13)

For positive `x,y`, weighted AM--GM gives

`x+y >= w^(-w)(1-w)^(-(1-w)) x^w y^(1-w).`                    (2.14)

Therefore

`det(D_J+M^T D_I M)
 >= K_w prod_i d_i^(p_i) prod_j e_j^(c_j).`                    (2.15)

Lieb's Gaussian-exhaustion theorem for BL data then yields the BL constant bound

`C_BL <= K_w^(-1/2)
          prod_i p_i^(-p_i/2)
          prod_j c_j^(-c_j/2),`                               (2.16)

with zero exponents interpreted by continuity and omitted. The determinant certificate also proves finiteness of the datum.

Now apply Jensen to (2.10): if `H(d)=prod_i |psi_i(2t(Md)_i)|`, then

`E H <= (E H^q)^(1/q)`.                                      (2.17)

Apply the BL inequality to `H^q prod_j g_j`. For a row exponent `p_i>0`, the scalar factor is

`( integral |psi_i(2tu)|^(q/p_i) du )^(p_i).`                 (2.18)

The gate `p_i<=q/2` makes the output exponent `q/p_i>=2`, so sharp Hausdorff--Young applies. Since `f_i<=1` and has mass one, all required `L^s` norms of `f_i` are at most one. The exact scalar estimate is

`(2.18)
 <= (pi/|t|)^(p_i)
    (p_i/q)^(p_i/2)
    (1-p_i/q)^(-(q-p_i)/2).`                                  (2.19)

The coordinate factors satisfy

`(integral g_j^(1/c_j))^(c_j) <=1`                            (2.20)

because `g_j<=1` and has mass one. Multiplying (2.16)--(2.20), the powers of `p_i` cancel. The remaining entropy factors obey

`prod_i (1-p_i/q)^(-(q-p_i)/2) <= exp(r/2)`,                  (2.21)
`prod_j c_j^(-c_j/2) <= exp(r/2)`,                            (2.22)

because `-(1-x)log(1-x)<=x`, `-c log c<=1-c`, and the sums in (2.3)-(2.4) equal `r`. Hence

`E H^q
 <= e^r q^(-r/2) K_w^(-1/2)
    (pi/|t|)^r.`                                               (2.23)

Combining with (2.10) and (2.17),

`|phi_Q(t)|
 <= min(1,
        e^(r/(2q)) q^(-r/(4q)) K_w^(-1/(4q))
        pi^(r/(2q)) |t|^(-r/(2q))).`                           (2.24)

Since `q<r/2`, the exponent `r/(2q)` is strictly greater than one. Let

`t_0=pi e q^(-1/2) K_w^(-1/(2r)).`                            (2.25)

This is exactly the frequency where the two terms in (2.24) meet. Direct integration of the envelope gives

`integral_R |phi_Q(t)| dt
 <= 2 t_0 r/(r-2q).`                                           (2.26)

Fourier inversion therefore yields (2.6). The same `L^1` characteristic-function bound gives a continuous density vanishing at infinity. QED.

### Why order 2 is the exact complementary level for a fixed third-volume anchor

If the third-volume packet has a fixed physical row, its marginal there is one. A complementary packet avoiding that row can reduce the mixed marginal to `w`. A first-volume packet would give effective order `1+2w`; integrability requires `w>1/2`, while the Hausdorff--Young endpoint at the fixed anchor forces `w<=1/2` when `q=1`, so that route is critical/nonintegrable. A second-volume packet gives effective order `2+w>2` for every `w>0`. This is the first compound order that can pay a fixed third-volume anchor by joint averaging rather than reciprocal pivot selection.

The theorem does **not** assert that a suitable `Z_2` packet with the gate (2.5) is automatically present under the bare spectral hypothesis. That is now a precise structural obligation rather than an analytic gap.

## 3. New deterministic compiler: a double-anchored E3 bank is either one-sided paid or genuinely diffuse on both sides

The fresh fleet03/B07 r29 branch produces a fixed physical row and column carrying a third-volume bank. The following lemma extracts exactly what can be paid without selecting a column triple.

Let `M` be a physical cross block between disjoint original-coordinate banks. Fix a row `i` and column `a`, and put

`G = G_3^(i,a)(M)
  = sum_(|R|=|C|=3, i in R, a in C) det M[R,C]^2 >0.`          (3.1)

Normalize the terms in (3.1) to a probability law. For residual rows `k!=i` and columns `l!=a`, let

`rho_k=P(k in R)`, `sigma_l=P(l in C)`.                        (3.2)

Then

`sum_(k!=i) rho_k = sum_(l!=a) sigma_l =2.`                   (3.3)

Define the heavy residual sets

`R_*={k:rho_k>2/3}`, `C_*={l:sigma_l>2/3}`,                   (3.4)

and tails

`delta_R=sum_(k notin R_*)rho_k`,
`delta_C=sum_(l notin C_*)sigma_l`.                            (3.5)

### Theorem 3.1 — `QFORM-DOUBLE-ANCHOR-ONESIDED-CORE-OR-DIFFUSE-v1`

If `delta_R<=1/2`, there is one physical row triple `I_*` containing `i` for which

`det(M[I_*,:] M[I_*,:]^T) >= G/2`,                            (3.6)

and therefore, by the completed designated-partner fleet02/B07 theorem,

`boxed:
 ||p_Q||_infinity
 <= 3 sqrt(e) (2/G)^(1/6).
`                                                                  (3.7)

The density is continuous. The symmetric statement holds if `delta_C<=1/2`.

Consequently an unpaid double-anchor survivor must satisfy

`delta_R>1/2` and `delta_C>1/2`.                               (3.8)

In that survivor, more than `G/4` of the original determinant-square mass uses at least one residual row with marginal at most `2/3`, and more than `G/4` uses at least one residual column with marginal at most `2/3`. No simultaneous row-and-column light-event lower bound is claimed.

### Proof

Because the residual row marginals sum to two, `|R_*|<=2`. If `delta_R<=1/2`, the heavy marginal sum is at least `3/2`; a single row has marginal at most one, so in fact `|R_*|=2`. Write `R_*={u,v}`. The residual row pair has size exactly two. If it is not `{u,v}`, at least one light residual row is selected. Hence

`P({residual rows} != {u,v})
 <= E[# selected light residual rows]
 =delta_R<=1/2.`                                                (3.9)

Thus the fixed row triple `I_*={i,u,v}` carries at least half of the bank:

`sum_(C: |C|=3, a in C) det M[I_*,C]^2 >= G/2.`               (3.10)

Cauchy--Binet, now summing over *all* column triples, gives

`det(M[I_*,:]M[I_*,:]^T)
 =sum_(|C|=3) det M[I_*,C]^2
 >=G/2.`                                                        (3.11)

Therefore `M[I_*,:]` has full row rank three. Apply the designated partner theorem `QFORM-CROSS-FIBER-PLANCHEREL-v1`, its one-sided `r=3` estimate,

`||p_Q||_infinity
 <=3 sqrt(e) det(M[I_*,:]M[I_*,:]^T)^(-1/6),`                  (3.12)

which gives (3.7). That theorem retains arbitrary self blocks, outside couplings, affine terms, signs, and extra ambient spectrum and proves continuity.

The column statement follows by transposition. If both tails exceed `1/2`, let `Y_R` be the number of selected light residual rows. Then `0<=Y_R<=2` and `E Y_R=delta_R>1/2`, so

`P(Y_R>=1) >= E Y_R/2 >1/4.`                                  (3.13)

Multiplying by total bank mass `G` proves the final row-light statement, and similarly for columns. QED.

This is an actual equation-level use of the designated partner result: the partner theorem is applied to the Gram determinant lower bound (3.11), not merely cited.

## 4. Apply Theorem 3.1 to the fresh r29 four-hub survivor

Fleet03/B07 r29 proves, at its standard collar `theta=1/16`, `delta=1/4`, `tau=1/16`, that after its already-paid transverse-star, rank-two-tube, and volume-diffuse exits, the remaining branch has physical anchors `(i,a)` satisfying

`G_3^(i,a)(N)
 > F^6 / 12824703626379264.`                                  (4.1)

Apply Theorem 3.1 to this *actual* bank. If either residual marginal tail is at most `1/2`, then the full ambient quadratic form has a continuous density with

`||p_Q||_infinity
 < 3 sqrt(e) (2*12824703626379264)^(1/6) F^(-1)
 = 2686.0538668... F^(-1).`                                   (4.2)

No claim is made here that `F` itself has a universal lower bound absent the inherited enclosing collar; (4.2) is the correct scale-sensitive payment of this subbranch.

Thus the genuinely new r29 `H3` debt can be sharpened from “double anchored” to:

`boxed: both residual determinant marginals have tail >1/2 outside their >2/3-heavy sets.` (4.3)

Equivalently, each side has a determinant-mass packet `>G/4` that genuinely touches a light residual coordinate. This removes every one-sided concentrated instance of the r29 double-anchor branch.

## 5. How the mixed E3/E2 theorem meets the surviving geometry

The survivor (4.3) explains why a second-compound packet is the correct next currency. Suppose, for example, that one can produce a second-volume packet `P_2` on the same physical cross block which avoids the fixed row anchor `i`. Then its anchor marginal is `alpha_i^(2)=0`; at `w=1/2` the mixed anchor exponent is exactly `p_i=1/2`, the sharp Hausdorff--Young endpoint.

More generally, if a compatible `P_2` satisfies the mixed gate (2.5), Theorem 2.1 pays the full form continuously without any reciprocal minor. At `w=1/2,q=1` this is (2.8). If a modestly larger gate is needed, one may choose any `1<q<5/4`; for instance `q=6/5` permits mixed row marginals up to `3/5` and yields

`||p_Q||_infinity
 <= [25e/sqrt(6/5)] [2 sqrt(Z_3 Z_2)]^(-1/5)
 = 54.0054847... (Z_3 Z_2)^(-1/10).`                          (5.1)

The important point is not this numeric constant but the exact analytic interface: **a compatible second-volume packet converts the fixed-anchor third-volume branch into an integrable effective order `5/2` estimate.**

There is also a simple deterministic source of the next split. For any far physical core `D`, the compound-tail inequality at order one gives

`T_1(D) E_1(D) <= 2 E_2(D).`                                  (5.2)

Therefore for every `eta>0`, either

`T_1(D) <= eta ||D||_F^2`                                     (5.3)

(a quantitative rank-one tube), or

`E_2(D) >= (eta/2)||D||_F^4.`                                 (5.4)

So the r29 hub-times-far-core route now has a natural next compiler: turn far-core energy into a genuine residual second-volume packet unless the far core is rank-one-close, and then test the mixed marginal gate (2.5). What remains is to preserve a dimension-free *scale lower bound* for the compatible `Z_2` packet and handle its heavy-marginal failure without deleting the nonzero tail.

## 6. Exact status and first unpaid implication

This run proves two supporting results:

- `QFORM-MIXED-32-FRACTIONAL-COMPOUND-BL-v1`: a continuous-density Fourier receiver that geometrically mixes determinant packets of orders three and two before reciprocal inversion;
- `QFORM-DOUBLE-ANCHOR-ONESIDED-CORE-OR-DIFFUSE-v1`: every one-sided concentrated double-anchor E3 bank is continuously paid using the designated partner's one-sided cross-fiber theorem.

They do **not** prove the full QFORM conjecture. The first remaining B07 implication is now

`QFORM-DOUBLE-ANCHOR-COMPATIBLE-E2-COMPILER-v1`:

> In the two-sided residual-diffuse state (3.8)/(4.3), construct a dimension-free second-volume packet `Z_2` with enough scale and a row or column mixed-marginal gate for Theorem 2.1, or else force a product-preserving rank-one/rank-two tube or an already-paid finite-core/volume-stability branch. The construction must average determinant currency before any reciprocal local pivot and retain arbitrary same-bank curvature and the true nonzero tail.

The separate genuine rank-two tube in fleet03/B07 r29 also remains unpaid. Global continuity remains OPEN; continuity is proved in the two new paid branches stated above.

## 7. Deterministic checks

The constants used above satisfy

`3 sqrt(e) (2*12824703626379264)^(1/6) = 2686.053866799886...`,

and for `w=1/2,q=6/5`,

`[ e r/((r-2q)sqrt(q)) ] 2^(-1/(2r)) = 54.0054847234...`,

with `r=5/2`. These arithmetic checks are not a substitute for the proofs in Sections 2--4.
