# account04/B18 — mixed volume sampling closes the moderate isotropic-shear core

**Run:** `20260923T001857Z-account04-B18-QFORM-r3`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Status:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_TARGET_LEVEL_BRANCH / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target and source ledger

The target remains the unrestricted statement for independent real original-coordinate variables with probability densities at most one and an arbitrary real symmetric matrix having at least three eigenvalues of absolute value at least one. No moment, support, smoothness, sign, or post-rotation independence hypothesis is added. Continuity is tracked separately.

Fresh control was read from `yspennstate/math-research-brain@acaf4b916ac9f26963e4799e6a7fbfdd4e48335e`. The required Claude packet was consumed beginning at `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, including the later review corrections. The scientific base immediately before this write was `yspennstate/math-open-problems@19d9434e07142e6b9fe19b4a88bbd46ccec8eeee`.

The completed designated result applied below is account01/B18 r19, `QFORM-FRESNEL-CAPPED-BASIS-WEIGHTS-v1`, at

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B18/20260922T225705Z-qform-B18-a01-r19/REPORT.md`.

Its exact primary inputs are Beckner's sharp Hausdorff--Young inequality (Ann. Math. 102 (1975), DOI `10.2307/1970980`) and the Gaussian-exhaustion form of rank-one Brascamp--Lieb due to Lieb, as formulated by Bennett--Carbery--Christ--Tao (arXiv `math/0505065`). At weights `alpha_i<=1/2`, the theorem keeps the original product characteristic function and proves

`||p_(X^T L^T D L X)||_infinity
 <= 3 e (|det D| Z_w)^(-1/3)`,                         (1.1)

where `w` is a probability law on nonsingular three-column bases, every coordinate marginal of `w` is at most `1/2`, and

`Z_w=exp(H(w)+sum_S w_S log det(L_S)^2)`.              (1.2)

The proof gives a continuous density. This report uses (1.1) at precisely that scope; it does not replace the product projection by an arbitrary joint density.

## 2. Live Schur-isotropic shear core

The still-unpaid exact-rank-three zero-pivot case from account02/B18 has the exact form

`Q=(Y+u X_0)^T D (Y+u X_0)`,                            (2.1)

where `X_0` is an original coordinate, `Y=V^T X'`, `X_0` is independent of all coordinates in `X'`, `V^T V=I_3`, `D=D^T` is nonsingular, and

`u^T D u=0`.                                             (2.2)

Writing the rows of `V` as `v_j^T`, the original-coordinate coefficient matrix is

`L=[u,v_1,...,v_m]`, `LL^T=I+uu^T`.                     (2.3)

The partner's exact pseudodeterminant ledger is

`pdet(L^T D L)=det(D)(1+||u||^2)`.                       (2.4)

Thus target normalization implies `|det D|(1+||u||^2)>=1`.

## 3. New mixed-volume certificate

Put `r=||u||>0`, `n=u/r`, and for every residual physical row define

`p_j=||v_j||^2`,
`q_j=||(I-nn^T)v_j||^2`.                                 (3.1)

### Theorem — `QFORM-ISOTROPIC-SHEAR-MIXED-VOLUME-v1`

Assume

`p_j+q_j<=1` for every residual physical coordinate `j`. (3.2)

Then (2.1) has a bounded continuous density and

`boxed:
 ||p_Q||_infinity
 <=3e(2r|det D|)^(-1/3)
 <=3e((1+r^2)/(2r))^(1/3).`                              (3.3)

In particular, if `1/2<=r<=2`,

`boxed: ||p_Q||_infinity
 <=3e(5/4)^(1/3)<8.785.`                                 (3.4)

This closes a quantitative part of the Schur-isotropic projected-product core left open by the earlier zero-pivot trichotomy.

### Proof

There are two canonical volume-sampling laws.

First, for residual triples `S`, set

`mu_S=det(V_S)^2`.                                       (3.5)

Cauchy--Binet and `V^T V=I_3` give `sum_S mu_S=1`. The coordinate marginals of `mu` are the rank-three leverages

`sum_(S contains j) mu_S=p_j`.                            (3.6)

Second, for residual pairs `{j,k}`, set

`nu_jk=det[u,v_j,v_k]^2/r^2`.                            (3.7)

Projecting onto `n^perp` reduces this to ordinary rank-two volume sampling. Since

`sum_j (I-nn^T)v_jv_j^T(I-nn^T)=I-nn^T`,                (3.8)

Cauchy--Binet gives `sum_(j<k) nu_jk=1`, and its coordinate marginals are

`sum_(k!=j) nu_jk=q_j`.                                  (3.9)

Define a basis law `w` for the full coefficient matrix `L` by placing half its mass on each bank:

`w_S=mu_S/2` for residual triples,
`w_{0jk}=nu_jk/2` for bases containing the shear coordinate. (3.10)

The shear-coordinate marginal is exactly `1/2`; every residual marginal equals `(p_j+q_j)/2<=1/2`. Thus the exact capped-marginal gate of account01/B18 holds.

The determinant-entropy score is explicit. On a residual triple,

`det(L_S)^2/w_S=2`,

while on a shear pair basis,

`det(L_{0jk})^2/w_{0jk}=2r^2`.

Each bank has total mass one half, hence

`log Z_w=(1/2)log 2+(1/2)log(2r^2)=log(2r)`,

so

`Z_w=2r`.                                                 (3.11)

Substitution in (1.1) proves the first inequality in (3.3). Equation (2.4) proves the second. Finally `(r+r^(-1))/2<=5/4` on `[1/2,2]`, giving (3.4). Continuity is inherited from the integrable characteristic-function majorant in account01/B18. QED.

## 4. Concrete target-level application beyond natural leverage

Let `e_1,e_2,e_3` be the Euclidean basis, put

`n=(e_1+e_3)/sqrt(2)`, `u=2n`, `D=diag(1,1,-1)`,          (4.1)

and let the six residual rows be two copies each of

`e_1/sqrt(2)`, `e_2/sqrt(2)`, `e_3/sqrt(2)`.              (4.2)

Then `V^T V=I_3`, `u^T D u=0`, and the full matrix `A=L^T D L` is an exact-rank-three physical zero-pivot Schur-isotropic instance. Since

`LL^T=I+4nn^T`,

the three nonzero eigenvalues of `A` are those of `(I+4nn^T)D`, namely

`{sqrt(5),1,-sqrt(5)}`.                                   (4.3)

Thus this is a genuine target matrix. Its natural leverage at the shear coordinate is `4/5`, so the usual natural-leverage `<=1/2` Fresnel gate fails.

For every residual row `p_j=1/2`. For the four `e_1,e_3` rows, `q_j=1/4`; for the two `e_2` rows, `q_j=1/2`. Hence (3.2) holds. Here `r=2`, `|det D|=1`, and (3.11) gives `Z_w=4`. Therefore every independent cap-one product input satisfies

`boxed:
 ||p_(X^T A X)||_infinity
 <=3e/4^(1/3)
 =5.1372307428... .`                                      (4.4)

The density is continuous. This applies the completed account01/B18 theorem to an actual matrix in the live missing Schur-isotropic class, not merely to an abstract certificate.

## 5. Exact remaining implication

The full conjecture remains open. The new theorem pays the moderate-shear region when the combined rank-three/rank-two row leverage condition (3.2) holds. The first remaining part of this exact core is therefore either

1. `r` outside `[1/2,2]`, where the determinant-entropy balance `2r/(1+r^2)` degenerates; or
2. a residual coordinate with `p_j+q_j>1`, i.e. a genuinely localized row simultaneously heavy for the three-dimensional residual frame and its transverse two-dimensional frame.

That second alternative is now a concrete physical-coordinate localization event and should be routed to the already developed heavy-pivot/hub/ruled-side mechanisms. No such exhaustive routing is asserted here. Arbitrary additional spectrum also remains an independent interaction problem.

## 6. Correction audit

- No independence is claimed among the projected coordinates of `Y`.
- No arbitrary-joint coarea estimate is used.
- No worst conditional-density supremum or positive conditional-height moment is used.
- No coefficient perturbation, near-zero-as-zero replacement, desmoothing, or moment/support hypothesis is used.
- All determinant identities are exact in the original-coordinate coefficient matrix.

Accordingly this is a substantive supporting branch, not a proof of the unrestricted conjecture and not a counterexample.
