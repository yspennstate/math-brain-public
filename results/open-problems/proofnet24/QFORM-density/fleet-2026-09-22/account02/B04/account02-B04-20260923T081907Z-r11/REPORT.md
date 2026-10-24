SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B04, 2026-09-23T08:19:07Z.
attacking: delocalized independent rank-one square plus unconditional pair-volume half-Riesz smoothing for the two-sided-curvature rank-two residual; optimize the competing three-volume gate and compare direct ridge on the same physical matrix.

# account02/B04 — delocalized-square / pair-volume splice

Programme `QFORM-DENSITY-3EIG-20260922`. Full conjecture: **OPEN**. Outcome of this run: **ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / SOURCE-VALID VOLUME-RIDGE OBSTRUCTION**. The new theorem below is source-complete and not an end-to-end solution.

## 1. First unpaid implication, early

The analytic endpoint paid here is a third large direction which is a rank-one quadratic form on a **disjoint original-coordinate bank**, not necessarily a single physical coordinate. It can be arbitrarily delocalized over that bank. The residual may have arbitrary quadratic curvature on both active banks and is paid only through aggregate pair-volume `E2`.

The next structural debt is

`QFORM-DISJOINT-AGGREGATE-SQUARE-OR-HUB-ROUTING-v1`:

from the bare three-large-eigenvalue hypothesis in the low-cross-rank/no-large-pivot survivor, force either (i) a disjoint original-coordinate rank-one quadratic direction of target scale together with a residual physical cross packet of target-scale `E2`, or (ii) an already completed volume/ridge/grouped-hub/pair endpoint. The genuinely unpaid case is when the third spectral direction is inseparably entangled with the same physical coordinates that carry the two-sided rank-two residual.

This changes mechanism from the preceding B04 coefficient-projected clean-star attempt: no clean bank or exact projected star is assumed.

## 2. Source-pinned premises and corrections

All variables are original independent real coordinates with densities at most one. No moment, support, log-concavity, post-rotation independence, arbitrary-joint coarea, positive conditional projection-cap moment, worst fiber supremum, uniformly good physical minor, or law-uniform pointwise quadratic-phase decay is used.

Required Claude source consumed and actually applied:

- `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`, especially `RESULTS.md` Theorem D and `FOURIER_ROUTE_REPORT.md`. The arbitrary-weight determinant/entropy form says a supported law on nonzero `3x3` physical minors must satisfy the constrained-side row-marginal gate; the exact stress cut in Section 6 has target-scale `E3` but **no admissible supported weight at any allowed fractional exponent**.

Completed unconditional pair-volume half-Riesz input:

- account01/B01 `QFORM-PAIRVOLUME-HALF-RIESZ-UNCONDITIONAL-v1`, `yspennstate/math-open-problems@1f3af9dc58afb9e902b972466d6da01cece89734`, `proofnet24/QFORM-density/fleet-2026-09-22/account01/B01/20260923T030821Z-account01-B01-qform-auto11/REPORT.md`, Theorem 8.1. If a quadratic residual has a disjoint physical cross block `M` with
  `E2=e2(M^T M)>0`, then

  `H_(1/2)(R):=sup_s E|R-s|^(-1/2) <= C_E2 E2^(-1/8)`,

  with

  `C_E2 <= 12*2^(5/6)*e^(5/24)=26.3340461807597...`.

This theorem explicitly permits arbitrary two-sided quadratic leakage.

Designated partner `account03/B04` latest completed handoff r27, canonical report `yspennstate/math-open-problems@62ea4dbfd636b7c4a019fec8b428fc5450f4a5fc`, source-pins the same unconditional pair-volume theorem and its physical-scalar square splice. I apply that physical-scalar comparator to the actual family in Section 8. The partner's own clean-bank row-star theorem is not misapplied: the stress family below has nonzero self curvature on both residual banks.

For a scalar linear projection of a disjoint product bank I use the completed product-projection estimate already source-pinned in account03/B04 r20/r27 and account02/B04:

`||p_(c^T Z)||_inf <= sqrt(2)/||c||_2`.                          (2.1)

## 3. New theorem: a delocalized product-bank square is a full square smoother

Let `K,I,J,W` be pairwise disjoint sets of original coordinates. Let `Z=(Z_k)_(k in K)` be the `K`-bank and let the residual variables be all coordinates outside `K`. Let `c in R^K`, `c!=0`, `a!=0`, and let `m` be an arbitrary measurable function of the residual variables. Let `R` be an arbitrary quadratic polynomial in those residual variables. Suppose one disjoint original-coordinate cross block `M=R[I,J]` has

`E2=e2(M^T M)>0`.                                                (3.1)

Define

`Q = a[c^T Z + m]^2 + R`.                                       (3.2)

### Theorem 3.1 — `QFORM-DELOCALIZED-SQUARE-PAIRVOLUME-SPLICE-v1`

`Q` is absolutely continuous and

`boxed:
 ||p_Q||_infinity
 <= sqrt(2) C_E2 (|a| ||c||_2^2)^(-1/2) E2^(-1/8)
 <= 12*2^(4/3)*e^(5/24)
    (|a| ||c||_2^2)^(-1/2) E2^(-1/8).`                          (3.3)

Numerically the universal coefficient in the second line is

`37.2419652609898...`.                                          (3.4)

The shift `m` may reuse every residual coordinate. No physical coordinate in the square bank must have a target-size diagonal coefficient.

### Proof

Put `S=c^T Z`. By (2.1), `S` has a density `f_S` with

`L:=||f_S||_infinity <= sqrt(2)/||c||_2`.                       (3.5)

Fix all residual variables. Translation by `m` does not change this cap. For `u` on the allowed half-line, the two roots of

`a(S+m)^2=u`

show that the conditional density of the square is bounded by

`k(u) <= L / sqrt(|a| |u|)`.                                    (3.6)

Indeed each root contributes at most `L/(2 sqrt(|a||u|))`, and there are at most two roots. Therefore, for almost every `t`,

`p_Q(t)
 <= L |a|^(-1/2) E |t-R|^(-1/2).`                              (3.7)

The unconditional pair-volume theorem gives

`sup_t E |t-R|^(-1/2) <= C_E2 E2^(-1/8)`.                       (3.8)

Combine (3.5)-(3.8). A mixture of the absolutely continuous conditional square laws is absolutely continuous. This proves (3.3). No pointwise characteristic-function decay has been invoked. QED.

### Interpretation

If `c` is normalized, the cost of the entire square bank is a universal constant even when every physical diagonal entry of `a cc^T` tends to zero. The currency is the nonzero eigenvalue `|a| ||c||^2` of the rank-one bank, not the largest physical diagonal.

## 4. Genuinely rotated indefinite target family with vanishing physical diagonals

Fix an even integer `m>=4`. Let

`c_m=m^(-1/2)(1,...,1) in R^m`,
`delta_m=1/m`,

and

`M=[[5/4,3/4],[3/4,5/4]].`                                      (4.1)

The two eigenvalues/singular values of `M` are exactly

`2, 1/2`,                                                        (4.2)

so

`det M=1`, `E2(M)=det(M^T M)=1`.                                (4.3)

For mutually independent original-coordinate product banks `Z in R^m`, `X in R^2`, `Y in R^2`, define

`Q_m=(c_m^T Z)^2
    + delta_m ||X||_2^2
    - delta_m ||Y||_2^2
    + 2 X^T M Y`.                                                (4.4)

Both residual banks carry nonzero self curvature. Every entry of the physical `X-Y` cross block is nonzero. The square direction is spread over all `m` original `Z` coordinates.

The symmetric matrix is the direct sum of `c_m c_m^T` and

`S_m=[[delta_m I_2, M],
      [M, -delta_m I_2]].`                                      (4.5)

Since `M` is symmetric, diagonalize it only for the deterministic spectral calculation. Each singular value `s in {2,1/2}` produces the `2x2` matrix

`[[delta_m,s],[s,-delta_m]]`

with eigenvalues `+-sqrt(s^2+delta_m^2)`. Hence the exact spectrum of the full physical matrix is

`{1,
  +-sqrt(4+m^(-2)),
  +-sqrt(1/4+m^(-2)),
  0^(m-1)}.`                                                     (4.6)

For every `m>=4`,

`sqrt(1/4+m^(-2))<1`,                                           (4.7)

so exactly three eigenvalues have modulus at least one: `1` and the pair `+-sqrt(4+m^(-2))`. The form is indefinite and genuinely non-diagonal in the original product coordinates. Also **every physical diagonal entry has magnitude exactly `1/m`**.

Theorem 3.1, with `a=1`, `||c_m||=1`, `E2=1`, gives the all-input-law estimate

`boxed: ||p_(Q_m)||_infinity <= 37.2419652609898...`             (4.8)

uniformly in `m`.

Continuity is not asserted here; the theorem proves absolute continuity and essential boundedness in its stated scope.

## 5. What a single physical square pays on the same matrix

For every physical square-bank coordinate `Z_i`,

`(c_m^T Z)^2
 = (1/m) ( Z_i + sum_(k!=i) Z_k )^2`.                            (5.1)

Thus the usual physical scalar-square peel sees coefficient

`a_i=1/m`.                                                       (5.2)

After completing that square, the Schur residual from the rank-one `Z` block is zero; the remaining nontrivial residual is exactly

`R_m=delta_m||X||^2-delta_m||Y||^2+2X^T M Y`,                   (5.3)

whose cross pair-volume is still `E2(M)=1`.

Applying the physical-scalar splice recorded in designated partner account03/B04 r27 to this actual inequality gives

`||p_(Q_m)||_infinity
 <= C_E2 |a_i|^(-1/2) E2(M)^(-1/8)
 <= 26.3340461807597... sqrt(m).`                               (5.4)

Thus the new aggregate square theorem improves this **same-matrix implementation** by the factor

`sqrt(m/2)`.                                                     (5.5)

This does not claim every other completed QFORM mechanism loses on this family; it isolates the cost of selecting one physical pivot instead of using the full independent product-bank projection.

## 6. Exact optimization of the e5 third-volume gate on the same matrix

Split the square bank into equal halves `Z_L,Z_R`, each of size `m/2`, and take the original-coordinate cut

`I=Z_L union {X_1,X_2}`,
`J=Z_R union {Y_1,Y_2}`.                                        (6.1)

Its physical cross block is the block direct sum

`B_m=(c_L c_R^T) direct_sum M`.                                 (6.2)

The nonzero singular values are exactly

`2, 1/2, 1/2`,                                                   (6.3)

because `||c_L||=||c_R||=1/sqrt(2)`. Therefore

`E3(B_m^T B_m)=4*(1/4)*(1/4)=1/4`.                              (6.4)

So the raw third volume is target-scale; the obstruction is purely the physical minor support.

A nonzero `3x3` minor must choose exactly one `Z_L` row, one `Z_R` column, **both** `X` rows and **both** `Y` columns. Since `det M=1`, every such nonzero minor has

`|det B_m[S,T]|=1/m`.                                           (6.5)

Consequently, for **every** probability weight `w` supported on nonzero `3x3` minors,

`alpha_(X_1)=alpha_(X_2)=1`.                                    (6.6)

This completely solves the admissible-weight optimization for this cut:

- e5 Theorem D (`alpha_i<=1/2`) has no feasible supported weight;
- its proved D' extension (`max alpha_i<h<3/4`) has no feasible supported weight;
- the sharp fractional weighted extension with `1<=q<3/2` has no feasible supported weight because `q/2<3/4<1`;
- allowing positive weight on zero minors makes `E_w log det^2=-infinity`, so the entropy-adjusted volume `G(w)` is zero.

Equivalently,

`boxed: sup{G(w): w admissible for q<3/2}=0`.                    (6.7)

Thus `E3=1/4` by itself does not imply finite-KL repairability of the physical third-volume law. This is an **obstruction to that intermediate volume route**, not a counterexample to QFORM.

The completed e5 `D_5` theorem does not alter this conclusion on the cut because `rank(B_m)=3`, hence `E5=0`.

## 7. Direct ridge certificate on the same cut: impossible at every scale

Let `g=gamma^2>0` and

`K_gamma=B_m B_m^T (gamma^2 I+B_m B_m^T)^(-1)`.                 (7.1)

For the strong singular direction `2`, put

`k=4/(g+4)`,                                                     (7.2)

and for each of the two singular directions `1/2`, put

`h=(1/4)/(g+1/4)=1/(4g+1)`.                                    (7.3)

The `M` left singular vectors are the two Hadamard directions on the physical `X` pair, so each `X` row has ridge leverage

`(k+h)/2`.                                                       (7.4)

The square-bank left singular vector is flat on `m/2` rows, so each `Z_L` row has ridge leverage

`2h/m <= h/2`                                                    (7.5)

for `m>=4`. Hence

`L_gamma:=max_i (K_gamma)_(ii)=(k+h)/2`,
`theta_gamma:=tr K_gamma=k+2h`.                                 (7.6)

The completed direct ridge theorem requires, for some admissible exponent `q`,

`L_gamma<=q/2`, `theta_gamma>2q`.                               (7.7)

But the first inequality forces

`q>=k+h`,                                                        (7.8)

and therefore

`theta_gamma-2q
 <= k+2h-2(k+h)
 = -k <0`.                                                       (7.9)

Thus

`boxed: the direct ridge theorem has no certificate on this cut for any gamma>0 and any q satisfying its leverage gate.` (7.10)

Because the stress `M` is symmetric and the square split is symmetric, reversing the row/column orientation of this particular cut gives the same calculation.

Again this is a theorem-interface obstruction, not a claim that every possible QFORM branch fails on `Q_m`.

## 8. Same-matrix mechanism comparison

For every even `m>=4`, the single target-valid physical matrix (4.4) has:

1. **New aggregate-square / pair-volume splice:**
   `||p_Q||_inf <=37.24196526099`, independent of `m`.

2. **Designated-partner-compatible physical scalar square implementation:**
   `||p_Q||_inf <=26.33404618076 sqrt(m)` using any `Z_i` as the outer scalar square.

3. **e5 arbitrary third-volume weights on the natural three-direction cut:** no admissible supported weight at any `1<=q<3/2`, despite exact `E3=1/4`; global admissible `G` equals zero.

4. **Direct ridge on that same cut:** no certificate at any regularization scale, by (7.9).

So the useful currency is neither a physical scalar pivot nor raw third volume nor direct-ridge effective dimension in this geometry. It is the **product-bank rank-one eigenvalue times aggregate residual pair-volume**, paid through decreasing-rearrangement / mixed-order Fourier half-Riesz control before any vanishing local coefficient is inverted.

For clarity, this family is not claimed to evade every other completed theorem. The purpose is to prove the new delocalized-square endpoint and to give a source-valid separation of the requested volume, ridge and physical-pivot implementations on one genuinely rotated indefinite target form.

## 9. Remaining connection to the full conjecture

Theorem 3.1 closes a genuine no-large-physical-pivot endpoint whenever the third quadratic direction can be isolated on a disjoint original-coordinate bank. It does **not** justify rotating a general spectral vector into such a bank, and it does not prove that every low-rank survivor admits this separation.

The first unpaid implication is therefore the structural `QFORM-DISJOINT-AGGREGATE-SQUARE-OR-HUB-ROUTING-v1` stated in Section 1: either preserve a target-scale independent aggregate square while retaining residual `E2`, or route the entangled survivor to an already completed mixed-hub/ridge/volume/pair mechanism without post-rotation independence or a vanishing local minor.

Full QFORM remains OPEN.
