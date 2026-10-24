SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B11, 2026-09-23T16:15:36Z.
attacking: the finite-heavy / exact-projective endpoint left by the newest null-ruling cross-cut compiler; aggregate each exact source ray before paying a principal-triple determinant.

# account01/B11 — arbitrary projective-bank compiler for indefinite exact rank three

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260923T161536Z-account01-B11-QFORM-r11`  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / PARTNER_RESULT_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** essential boundedness only in the new theorem.

## 1. Exact target and why this step is not the full theorem

The owner target is the unrestricted statement for arbitrary independent real coordinates with density caps one and arbitrary symmetric `A` having at least three eigenvalues of modulus at least one. This report proves a source-product-safe theorem for an exact-rank-three chamber whose spectral rows occupy finitely many projective lines. It does **not** replace an approximately collinear bank by an exact ray, and it does not handle arbitrary additional nonseparable spectrum.

The point of the new theorem is that reciprocal physical minors are paid only **after every exact projective source bank has been aggregated**. Thus a bank may contain arbitrarily many tiny original-coordinate rows and arbitrarily fragmented/unbounded cap-one input laws.

The result is sign-independent and hence applies in particular to both B11 signatures `(+, +, -)` and `(+, -, -)`.

## 2. Completed sources used at their exact scopes

### 2.1 Product-safe principal triple theorem

From account03/B14 r16, canonical source

`yspennstate/math-open-problems@89e6481f4f7ed7d49a77cfcb989ee93572d5d5cd`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B14/20260922T190524Z-account03-B14-QFORM-r16/REPORT.md`,

for three independent cap-one ORIGINAL variables, every nonsingular symmetric `3 x 3` coefficient matrix `B`, and arbitrary affine term,

`||p||_infinity <= 32 sqrt(10) |det B|^(-1/3)`.                    (2.1)

The same theorem is valid after conditioning all outside original coordinates; the outside values create only an affine term.

### 2.2 One-dimensional product projection

The source-valid Rogozin--Ball projection consequence used throughout the current QFORM package says that every normalized linear form of independent cap-one variables has density cap at most `sqrt(2)`. One pinned source recording exactly this input is

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

No support, moment, log-concavity, centering or connectedness hypothesis is attached to this projection bound.

### 2.3 Newest designated partner state

The newest completed account02/B11 report consumed is available at

`yspennstate/math-open-problems@8d6e85d072cd7a4c0fa9a37abe995a64109079e0`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B11/20260923T145222Z-account02-B11-QFORM-auto11b/REPORT.md`.

Its theorem `QFORM-NULL-RULING-LIGHT-CROSSCUT-v1` pays the diffuse approximate-null-ruling branch by constructing an actual original-coordinate rank-three cross cut. Failure is reduced to a bounded-cardinality heavy-spike near-null branch rather than being declared harmless.

I also use the immediately preceding completed assigned-partner theorem

`yspennstate/math-open-problems@8ae1a16002c77879645875d1e3b9a9d136365289`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B11/20260923T141910Z-account02-B11-QFORM-auto11/REPORT.md`.

For its four special projective rays it proves:

* arbitrary invertible spectral `M`, minimum eigenvalue modulus `s`, and diffuse split-side weights: `||p_Q||_infinity <=24/s`;
* for the target matrix `M_*=[[1,0,0],[0,0,1],[0,1,0]]`, `spec(M_*)={1,1,-1}`, arbitrary weights and multiplicities: `||p_Q||_infinity<232` (and likewise after reflection).

These partner inequalities are applied in Section 6 below.

## 3. Exact projective-bank reduction

Let

`A=R M R^T`, `R^T R=I_3`,                                      (3.1)

have exact rank three, and assume

`s:=min_j |lambda_j(M)|>0`.                                    (3.2)

Suppose the nonzero spectral rows of `R` lie on `k` projective lines. Partition the ORIGINAL coordinate set into the corresponding nonempty disjoint banks

`I_1 sqcup ... sqcup I_k`.

Choose a unit representative `q_a in R^3` for line `a` and write

`r_i=c_i q_a`, `i in I_a`.                                     (3.3)

Define

`h_a=sum_(i in I_a)c_i^2>0`,
`u_a=sqrt(h_a) q_a`,
`Y_a=h_a^(-1/2) sum_(i in I_a)c_i X_i`.                         (3.4)

Because the banks are disjoint sets of ORIGINAL coordinates, the `Y_a` are mutually independent. Their coefficient vectors have Euclidean norm one, so

`||p_(Y_a)||_infinity <=sqrt(2)`.                               (3.5)

Let `U` be the `k x 3` matrix whose `a`th row is `u_a^T`. Then

`U^T U=sum_a h_a q_a q_a^T=sum_i r_i r_i^T=I_3`,               (3.6)

and the spectral coordinate is exactly

`R^T X=sum_a u_a Y_a=U^T Y`.                                   (3.7)

Hence, with no approximation,

`boxed: Q=X^TAX=Y^T U M U^T Y.`                                (3.8)

This is the aggregate-before-inversion identity.

## 4. Main theorem — projective-bank triple compiler

For a three-element bank set `J={a,b,c}`, let `U_J` be the corresponding `3 x 3` row submatrix and put

`w_J=det(U_J)^2`.                                                (4.1)

Define

`omega=max_(|J|=3) w_J`.                                        (4.2)

### Theorem `QFORM-PROJECTIVE-BANK-TRIPLE-COMPILER-v1`

Under (3.1)--(3.3),

`boxed:
 ||p_Q||_infinity
 <=64 sqrt(10) s^(-1) omega^(-1/3).`                            (4.3)

In particular, by Cauchy--Binet,

`sum_(|J|=3) w_J=det(U^T U)=1`,                                 (4.4)

so

`omega>=1/binom(k,3)`                                           (4.5)

and therefore

`boxed:
 ||p_Q||_infinity
 <=64 sqrt(10) binom(k,3)^(1/3) / s.`                           (4.6)

For example,

`k=4: ||p_Q||_infinity <321.268/s`,
`k=5: ||p_Q||_infinity <436.027/s`.                              (4.7)

No ray is required to be null, no ray weight is required to be diffuse, and no sign assumption on `M` is needed.

### Proof

Choose `J` attaining `omega`. Condition on all aggregate bank variables `Y_d`, `d notin J`. Because the banks are independent, the three selected bank variables remain independent with the same one-dimensional density caps (3.5). The conditional output has the form

`Y_J^T B_J Y_J + ell^T Y_J+c`,                                  (4.8)

where

`B_J=U_J M U_J^T`.                                              (4.9)

Since `U_J` is square,

`det B_J=det(M) det(U_J)^2`,                                    (4.10)

hence

`|det B_J|>=s^3 omega`.                                         (4.11)

To apply (2.1), put `Z=sqrt(2)Y_J`. Each `Z` coordinate now has density cap at most one and

`Y_J^T B_JY_J+ell^TY_J+c
 =Z^T(B_J/2)Z+2^(-1/2)ell^T Z+c`.                              (4.12)

Equation (2.1) gives, uniformly in every conditioned bank value,

`||p_(Q | Y_(J^c))||_infinity
 <=32 sqrt(10) |det(B_J/2)|^(-1/3)`
` =64 sqrt(10) |det B_J|^(-1/3)`
` <=64 sqrt(10) s^(-1) omega^(-1/3).`                          (4.13)

Averaging the conditional laws proves (4.3). Cauchy--Binet and (3.6) prove (4.4), and (4.5)--(4.6) follow. QED.

### Nonuniform density-cap version

The same proof gives a useful sharper bookkeeping statement. If selected normalized bank variables have density caps `L_a,L_b,L_c`, then

`||p_Q||_infinity
 <=32 sqrt(10) (L_a L_b L_c)^(2/3)
   s^(-1) w_J^(-1/3).`                                         (4.14)

Thus singleton heavy banks pay cap one rather than `sqrt(2)`; the theorem does not artificially charge them a diffuse projection constant.

## 5. How the third direction removes the rank-two logarithm in this compiler

The opposite-sign rank-two obstruction remains genuine. For independent

`X,Y ~ Uniform[-1/2,1/2]`,

`p_(2XY)(t)=log(1/(2|t|)),  0<|t|<1/2`.                        (5.1)

Two projective source banks span at most two spectral directions, so there is no nonzero three-volume `w_J` to spend. The logarithmic saddle can therefore survive.

With three genuinely spanning projective banks, `w_J>0`. The exact bank Hessian satisfies

`|det B_J|=|det M| w_J`,                                        (5.2)

so the third direction is precisely the nonzero projective three-volume. The product-safe physical-triple theorem then bounds the whole three-variable pushforward, including the opposite-sign saddle and arbitrary affine translations generated by every other bank. In this branch the third direction removes the logarithmic endpoint by turning the selected aggregate Hessian from rank two into a determinant-nondegenerate rank-three quadratic form; no spectral-coordinate independence is asserted.

## 6. Required account02/B11 result applied to actual inequalities

Apply the new theorem to the four-ray geometry in the completed account02/B11 run `20260923T141910Z`. Its aggregate rows are

`u_(S+)=(1/sqrt(2))(1,sqrt(rho),0)`,
`u_(S-)=(1/sqrt(2))(1,-sqrt(rho),0)`,
`u_(T+)=(1/sqrt(2))(0,sqrt(1-rho),1)`,
`u_(T-)=(1/sqrt(2))(0,sqrt(1-rho),-1)`.                        (6.1)

The four squared triple volumes are exactly

`rho/2, rho/2, (1-rho)/2, (1-rho)/2`,                          (6.2)

so

`omega=max(rho,1-rho)/2`.                                      (6.3)

For arbitrary invertible spectral `M` with minimum eigenvalue modulus `s`, (4.3) gives the actual all-weight inequality

`boxed:
 ||p_Q||_infinity
 <=64 sqrt(10) [2/max(rho,1-rho)]^(1/3)/s
 <=321.268/s.`                                                  (6.4)

Now apply the completed designated-partner theorem at its exact scope. If the pair of rays that must be split has no squared amplitude exceeding `1/4`, account02/B11 gives

`boxed: ||p_Q||_infinity <=24/s,`                               (6.5)

which strictly sharpens (6.4) on that diffuse subbranch.

For the partner target matrix

`M_*=[[1,0,0],[0,0,1],[0,1,0]]`, `spec(M_*)={1,1,-1}`,          (6.6)

the same completed account02/B11 report pays **all** weights, including the heavy-row branch, by

`boxed: ||p_Q||_infinity<232.`                                  (6.7)

After replacing `M_*` by `s M_*`, output scaling gives the concrete inequality

`boxed: ||p_Q||_infinity<232/s.`                                (6.8)

Thus the assigned partner is used twice at actual inequalities: (6.5) improves the new generic arbitrary-`M` four-ray compiler on the diffuse side, and (6.8) improves its worst-case constant for the target-valid special spectral matrix even when a ray contains a heavy original coordinate.

## 7. Relation to the newest heavy-spike null-ruling remainder

The latest account02/B11 theorem `QFORM-NULL-RULING-LIGHT-CROSSCUT-v1` proves a continuous density bound when each approximate null-ruling cluster contains enough low-leverage actual rows. Its failure forces a bounded-cardinality set of high-leverage original rows carrying definite projected mass on one of the null-ruling clusters.

The theorem here closes the **exact projective-collapse endpoint** of that remainder: if, after all exact source rows are retained, the rank-three frame is supported on a fixed finite number `k` of actual projective lines, the form is paid by (4.6), regardless of how the mass is distributed among heavy and light rows.

What it does **not** do is replace a near-ray by its projection. In the actual remaining partner branch the high-leverage rows may carry transverse/tangent components. With unbounded supports, an operator-small or coefficient-small transverse component is not a uniformly small random perturbation. The next implication must therefore retain those transverse statistics exactly.

## 8. First unpaid implication

The sharpened B11 debt is

`QFORM-HEAVY-NEAR-RAY-TRANSVERSE-BANK-COMPILER-v1`:

> In the finite-heavy-spike branch of `QFORM-NULL-RULING-LIGHT-CROSSCUT-v1`, combine the bounded number of high-leverage original rows with the remaining diffuse null-ruling banks while retaining every transverse/tangent coefficient. Either recover a dimension-free actual three-volume / physical-pair / mixed-hub exit, or prove a product-preserving vector-bank estimate stable under the exact tangent leakage. Do not project the random quadratic form onto the ideal rays and do not condition on a statistic merely because its marginal density is bounded.

The new theorem says that the exact-ray endpoint itself is no longer a debt; only the transverse leakage is.

Arbitrary additional nonseparable spectrum beyond exact rank three remains a separate interface to the full owner target.

## 9. Verification and status

`VERIFY.py` and `VERIFY_OUTPUT.txt` in this immutable run directory check:

1. Cauchy--Binet `sum_J det(U_J)^2=1` on deterministic orthonormal-column frames;
2. `det(U_J M U_J^T)=det(M)det(U_J)^2` numerically;
3. the four special-ray weights (6.2);
4. the constants in (4.7) and (6.4).

The checker is regression evidence only; the proof is the exact argument above.

**Continuity:** not proved by `QFORM-PROJECTIVE-BANK-TRIPLE-COMPILER-v1`; it proves an essentially bounded density.  
**Full QFORM:** OPEN.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.
