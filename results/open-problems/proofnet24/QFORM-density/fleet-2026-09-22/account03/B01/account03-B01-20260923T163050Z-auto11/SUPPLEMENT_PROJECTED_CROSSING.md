# Supplement — apply the new arbitrary-rank projected crossing theorem to the actual near-null pair partition

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `account03-B01-20260923T163050Z-auto11`  
Status: **PROVED CONDITIONAL EXIT ON THE ACTUAL NEAR-NULL PHYSICAL PARTITION / FULL QFORM OPEN**.

This supplement responds to the later source refresh `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`. It applies the new interactive theorem

`yspennstate/math-open-problems@4f92aeb74083c6f95cb314a11fed1b812eacef9a`,
`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`

at the actual physical partition used by account04/B01's near-singular overlap-two routing. It does not merely cite the theorem and does not claim that its volume/marginal gates are automatic.

## 1. Actual surviving partition

Keep the physical pair `H={i,j}` from the main report and write the original-coordinate matrix in block form

`A = [[B, C0],[C0^T, A_L]]`,                                     (1.1)

where `B` is the near-singular two-by-two hub block and `L=H^c` is the light bank. The original random banks `X_H` and `X_L` are independent.

Account04/B01's leakage branch proves, after scalar completion of coordinate `i`, that the vector

`ell = row_j(C0) - (b/a) row_i(C0)`                               (1.2)

obeys

`sum_(r!=s) ell_r^2 ell_s^2 >= W2(H)/(4a^2)`.                    (1.3)

Hence whenever `W2(H)>0`, `ell!=0` and therefore the **actual physical hub-to-light cross block has rank**

`k:=rank(C0) in {1,2}`.                                          (1.4)

No inverse of `det B` is used. This is the equation-level use of the designated partner result in this supplement.

Factor

`C0 = U M`,                                                       (1.5)

where `U` is a two-by-`k` orthonormal frame and `M` is a `k`-by-`|L|` full-row-rank matrix. Put

`W=U^T X_H`.

The entire quadratic form is exactly

`Q = F(X_H) + 2 <W, M X_L> + R(X_L)`,                            (1.6)

where `F` contains the whole near-singular hub block `B` and every hub-linear term, and `R` contains the whole light quadratic block `A_L` and every light-linear term. Thus the new grouped-crossing theorem applies without completing or perturbing `B`.

The hub projection density cap is explicit:

- if `k=2`, `U` is a two-by-two orthogonal matrix, so rotating the two-dimensional density `f_i(x_i)f_j(x_j)<=1` preserves its density cap; hence `M_H<=1`;
- if `k=1`, the scalar product projection theorem gives `M_H<=sqrt(2)`.

These are density statements for projections; no rotated coordinates are declared independent.

## 2. Rank-two hub crossing: one projected light crossing direction suffices

Assume `k=2`. Split the original light coordinates into disjoint banks `I,J` so that `M_J` has rank two. Let

`S = s_1(M_J)s_2(M_J)>0`,                                       (2.1)

`C = (A_L)_{I,J}(I-Pi_row(M_J))`,                               (2.2)

`Z1 = e_1(CC^T)=||C||_F^2`.                                    (2.3)

For `Z1>0`, define the one-volume row marginal

`alpha_r = ||C_{r,*}||_2^2/Z1`, `r in I`.                        (2.4)

If

`max_(r in I) alpha_r <=1/2`,                                   (2.5)

then the new grouped-crossing theorem with `(k,ell)=(2,1)`, `d=3`, and `M_H<=1` gives the **full original form** a continuous density with

`boxed:`
`||p_Q||_infinity <= 3*2^(5/6) S^(-1/3) Z1^(-1/6)`
`                  <5.346 S^(-1/3) Z1^(-1/6).`                 (2.6)

All self-curvature inside the near-singular physical pair and inside either light bank is retained. The pair determinant may be zero or arbitrarily small; it does not appear in (2.6).

This is exactly the missing mechanism suggested by the logarithmic main theorem: one additional projected crossing direction upgrades the two hub directions to total Fourier dimension three and removes the `log T` defect completely.

## 3. Rank-one hub crossing: two projected light crossing directions suffice

Assume `k=1`. Choose a split `L=I disjoint_union J` with `M_J!=0` and put

`S=||M_J||_2`.                                                   (3.1)

Define `C` again by (2.2), now with the one-dimensional row projection of `M_J`, and set

`Z2=e_2(CC^T)`.                                                  (3.2)

Let the two-volume weights and row marginals be exactly those of the new theorem:

`w_T = det(C_T C_T^T)/Z2`, `|T|=2`,
`alpha_r=sum_(T contains r) w_T`.                                (3.3)

If

`Z2>0`, `max_r alpha_r<=1/2`,                                   (3.4)

then `(k,ell)=(1,2)`, `d=3`. Since the scalar hub projection has density cap at most `sqrt(2)`, the grouped-crossing theorem gives

`boxed:`
`||p_Q||_infinity`
` <=3*2^(4/3)*exp(1/3) S^(-1/3) Z2^(-1/6)`
` <10.551 S^(-1/3) Z2^(-1/6).`                                 (3.5)

Again the density is continuous. The estimate includes arbitrary internal hub curvature and arbitrary light self-curvature; only the explicitly displayed projected crossing volume and row-marginal gates are paid.

## 4. Consequence for the near-null proof map

The account04/B01 leakage identity guarantees `rank(C0)>=1` when `W2>0`, so the two cases above exhaust the **rank** of the actual hub-to-light crossing. Therefore the near-null leakage branch is now paid whenever at least one eligible original-coordinate light split supplies:

- for `rank(C0)=2`, one spread projected crossing volume `Z1` at usable scale; or
- for `rank(C0)=1`, two spread projected crossing directions measured by `Z2` at usable scale.

This is strictly stronger than the main report's `O(log T)` Fejer bound on that subbranch and supplies a genuine bounded continuous density there.

What remains is not “near-null” in general. It is the narrower concentrated projected-crossing endpoint: after the newest collective-tail exit has failed, every eligible split either has insufficient `S*sqrt(Z_ell)` or violates the volume row-marginal gate `alpha_r<=1/2`. That concentration must be routed to a high-leverage/grouped-coordinate receiver; the new crossing theorem itself does not prove such a routing.

The full three-large-eigenvalue conjecture remains OPEN. Independent review of this application is pending.
