# fleet02/B15 — rough ruled passage, definite-pair closure, and diffuse obstruction

Run: `20260923T022111Z-fleet02-B15-QFORM-auto11`
Programme: `QFORM-DENSITY-3EIG-20260922`
Role: absolute continuity and regularity; complementary constructions/source-valid counterexamples
Status: `SUPPORTING_THEOREM_PROVED / ROUGH_TRACE_BRIDGE_CHECKED`
Full universal QFORM theorem: **OPEN**.

## 1. First unpaid implication

The central target remains one universal finite constant for the essential density height of `Q=X^TAX` under independent one-dimensional densities `f_i<=1` and at least three eigenvalues of `A` of modulus at least one. Continuity is separate.

For exact rank three of signature `(+,+,-)`, the completed ruled estimate in
`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`
pays the majority-sign one-sheet side. This report gives the missing rough-law limiting justification in a form that never takes a trace of a rough projection density, then applies the latest compatible fleet03/B15 heat certificate to isolate the still-unpaid two-sheet functional.

The latest compatible partner result used is fleet03/B15 r23,
`math-open-problems@0d6589d347490912ece0ea097eebb63e0e017d9a:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B15/20260923T012829Z-fleet03-B15-qform-r23/REPORT.md`.
It proves for every probability law `mu`

`D(mu)=sup_{k>=1,m in Z} int gamma_{2^{-k}}(x-m 2^{-3k}) dmu(x)`, 

where `D(mu)` is the essential density height, with value `+infinity` if no bounded density exists.

## 2. Rough-law one-sheet theorem with no trace assumption

Let `R` be an `n x 3` matrix with orthonormal columns and put `Y=R^T X`. Let `lambda_1,lambda_2,mu >=1`, `a in R^3`, and `c in R`. Define

`Q = lambda_1 (Y_1-a_1)^2 + lambda_2 (Y_2-a_2)^2 - mu (Y_3-a_3)^2 + c`.

Let `nu_+` be the output submeasure restricted to `{Q>=c}`. Then

`nu_+(I) <= C_+ |I|` for every interval `I`,

with

`C_+ = (lambda_1 lambda_2 mu)^(-1/2) int_0^{2pi} [sin^2(theta)/lambda_1 + cos^2(theta)/lambda_2 + 1/mu]^(-1/2) dtheta <= pi sqrt(2)`.

Consequently `nu_+ <= C_+ Leb` and its essential density is bounded by `C_+`. No continuity of the input or output density is asserted or used.

### Proof

First remove `a` without rotating the product source. Replacing `X` by `X-Ra` is a deterministic translation in the original physical coordinates, so independence and the cap `f_i<=1` are preserved. The constant `c` only translates the output. It therefore suffices to take `a=0,c=0`.

For `delta>0`, let `G=(G_1,...,G_n)` be standard Gaussian independent of `X`, and set `X^(delta)=X+delta G`. Each physical marginal has density `f_i * gamma_delta`, still bounded by one, and the coordinates remain independent. Moreover

`|| product_i(f_i*gamma_delta) - product_i f_i ||_1 <= sum_i ||f_i*gamma_delta-f_i||_1 ->0`.

Thus the product laws converge in total variation. Pushforward by any measurable map contracts total variation, and restriction to a fixed Borel set contracts it again. Hence it is enough to prove the claimed interval bound for every padded law with a constant independent of `delta` and then pass to the limit. This already avoids every rough trace issue.

For a padded law the three-dimensional projection `Y^(delta)=R^T X^(delta)` is the original projection convolved with a nondegenerate three-dimensional Gaussian and has a smooth density. Put

`D=diag(sqrt(lambda_1),sqrt(lambda_2),sqrt(mu))`, `Z=D Y^(delta)`.

Then `q(Z)=Z_1^2+Z_2^2-Z_3^2`. For `s>0`, write

`F(s,theta,t)=sqrt(s) e_theta + t(e_theta^perp+e_3)`.

This parametrizes the one-sheet region `q>0`, and a direct determinant computation gives

`|det dF/d(s,theta,t)|=1/2`.

Let `v_theta=e_theta^perp+e_3` and

`w_theta=D^{-1}v_theta=(-sin(theta)/sqrt(lambda_1), cos(theta)/sqrt(lambda_2), 1/sqrt(mu))`.

If `rho_Y` is the padded density of `Y`, then `rho_Z(z)=rho_Y(D^{-1}z)/sqrt(lambda_1 lambda_2 mu)`. Along a ruling,

`int_R rho_Z(F(s,theta,t)) dt
 = [sqrt(lambda_1 lambda_2 mu)]^{-1} int_R rho_Y(y_0+t w_theta) dt`.

After arclength parametrization the last integral is `|w_theta|^{-1}` times the density, at the corresponding point, of the orthogonal two-dimensional projection of `Y` to `w_theta^perp`. Such a projection is a two-dimensional orthogonal projection of the original product source. The completed projection-density theorem used in the pinned Claude package gives cap `2`. For the Gaussian-padded law the projected density is continuous, so the essential cap is pointwise. Therefore

`int_R rho_Z(F(s,theta,t)) dt <= 2/[sqrt(lambda_1 lambda_2 mu) |w_theta|]`.

Integrating the exact Jacobian over `s in I subset (0,infinity)` gives

`P(q(Z) in I) <= |I| [sqrt(lambda_1 lambda_2 mu)]^{-1} int_0^{2pi} |w_theta|^{-1} dtheta = C_+ |I|`.

The same inequality holds for intervals meeting zero by monotone approximation. Since `lambda_1,lambda_2,mu>=1`,

`lambda_1 lambda_2 mu |w_theta|^2 = lambda_2 mu sin^2(theta)+lambda_1 mu cos^2(theta)+lambda_1 lambda_2 >=2`,

so `C_+<=pi sqrt(2)`.

Finally, total-variation convergence of the padded product laws implies total-variation convergence of the restricted output submeasures. Passing the interval inequality to the limit yields it for the original rough inputs. No output continuity, no boundary trace, and no separate no-atom argument are needed. Interval domination extends to all Borel sets by regularity, proving `nu_+<=C_+ Leb`.

## 3. Application of fleet03/B15 r23: exact remaining two-sheet heat obligation

Write the full exact-rank-three output law as `nu=nu_+ + nu_-`, where `nu_-` is restricted to `{Q<c}`. For every Gaussian heat test in the partner's countable grid,

`H_{k,m}(nu)=H_{k,m}(nu_+)+H_{k,m}(nu_-) <= C_+ + H_{k,m}(nu_-)`,

because convolution of the dominated submeasure `nu_+<=C_+ Leb` with a probability kernel is at most `C_+`. The partner identity therefore gives the concrete reduction

`D(nu) <= C_+ + sup_{k,m} H_{k,m}(nu_-) <= pi sqrt(2) + sup_{k,m} H_{k,m}(nu_-)`.

Thus, for exact rank-three signature `(+,+,-)`, the first unpaid implication is precisely a universal bound on the **countable Gaussian heat tests of the minority-sign/two-sheet submeasure**. The majority-sign side is paid for arbitrary rough product laws. This uses the partner result at a real inequality and does not infer height from continuity.

The sign-reversed statement handles signature `(-,-,+)` with the corresponding majority-sign side.

## 4. A full rough-law closure whenever one physical definite pair is quantitatively good

A second elementary branch clarifies where the two-sheet difficulty can remain. Let `I={i,j}` be two original coordinates and suppose the physical principal block `B=A_II` is positive or negative definite. Put `D=|det B|>0`. Conditioning on all other original coordinates gives

`Q(z,w)=z^T B z + 2 ell(w)^T z + c(w)`.

The conditional joint density of `z=(X_i,X_j)` is `f_i(z_1)f_j(z_2)<=1`. Completing the square is only a translation in this physical two-plane. If `B>0`, the Euclidean area of

`{z: z^T B z in [u,u+h]}`

is at most `pi h/sqrt(det B)`; for `B<0` apply this to `-B`. Therefore, for every interval `J`,

`P(Q in J | X_{I^c}) <= pi |J|/sqrt(D)`

uniformly in the conditioning. Averaging yields

`||p_Q||_infinity <= pi/sqrt(D)`.

This is an essential-boundedness statement valid for arbitrary rough cap-one inputs, arbitrary remaining spectrum, arbitrary outside couplings, and the affine terms generated by conditioning. It proves no continuity by itself.

Consequently the exact-rank-three two-sheet problem is already closed whenever some original-coordinate definite pair has determinant bounded below. The genuinely hard branch must allow every such physical definite pair to be arbitrarily ill-conditioned or absent.

## 5. Source-valid obstruction: a single definite physical pair cannot be the universal bridge

For `m>=2`, let

`A_m = diag(J_m/m, J_m/m, -J_m/m)`

on `R^{3m}`, where `J_m` is the all-ones matrix. Its nonzero spectrum is exactly `{1,1,-1}`, so it is a valid target matrix.

Every positive-definite physical `2x2` principal block uses one coordinate from each of the two positive banks and equals `diag(1/m,1/m)`, hence has determinant `1/m^2`. Pairs within one bank have determinant zero, and no negative-definite physical pair exists because the negative bank is rank one. Thus the definite-pair certificate above deteriorates to `pi m` and cannot be a universal structural reduction.

This deterioration is not an output-density counterexample. Apply the completed Theorem F from the pinned `FOURIER_ROUTE_REPORT.md` at `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`. The exact rank-three eigenframe for `A_m` has every row leverage equal to `1/m<=1/2`; with eigenvalues `1,1,-1`, Theorem F gives directly

`||p_{X^T A_m X}||_infinity <=12`

for **every** independent cap-one product input. Hence the local definite-pair mechanism and the diffuse Fresnel/Brascamp-Lieb mechanism are genuinely complementary. Any exhaustive proof must switch before paying a reciprocal local determinant in this diffuse family.

## 6. Implication ledger and remaining gap

The conclusions used here are deliberately separated.

- The rough ruled argument proves essential boundedness of the one-sheet submeasure; it does not prove continuity of the original output.
- The physical definite-pair argument proves a full essential density bound in its stated branch, again without continuity.
- Separate fixed-matrix rank-at-least-three `C_0` results may establish continuity, but no such statement is used to obtain either height estimate above.
- The full arbitrary-matrix QFORM conjecture remains open. For exact rank three, after the one-sheet payment the live geometric obligation is the product-provenance-sensitive two-sheet heat/interval bound in the regime with no quantitatively good physical definite pair. For higher rank, this must still be joined to the current no-pivot/hybrid structural reduction rather than assuming an exact rank-three decomposition.

No moments, support bounds, log-concavity, identical laws, independence after spectral rotation, or pointwise law-uniform oscillatory decay entered the argument.
