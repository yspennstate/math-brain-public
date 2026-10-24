# Gaussian T357: independent parent calculations and checkpoint

Date: 2026-10-23. Historical research checkpoint. Subsequent final proof 1469aad3c34b902a363fe66d32eff199c451adc28d2ae5ae4de6cbb716fd630b and independent review 7c9b8412cc8d38e184972b9256773d7854cf7878b2bb2e1df5a8eafda80fc73f establish the first-step and two-replica results described below as work in progress. The remainder preserves that earlier checkpoint wording. A26 and A28 are proving and auditing the convergence claims; A29 is deriving calibration consequences. The categorical theorem has separately passed review.

For Gaussian inputs, logistic teacher, tanh random features, and ratios n/d→α, m/d→γ, define a=E[G tanh(G)], b=E[tanh(G)^2], and μ=E[Z(σ(βZ)−1/2)]. The invariant first-step score is S=(cd/n)Σ_i(Y_i−1/2)K_m(X,X_i), where K_m=m^−1Σ_j tanh(f_j·X)tanh(f_j·X_i). Scaling the network weights differently changes the equivalent learning rate; the score formula is authoritative.

The parent and A26 independently obtained the candidate limit S=c(a²μ Z+τG), with independent standard normals Z,G and

τ²=μ²a²b/γ+(a⁴+b²/γ)/(4α).

This agreement is a consistency check, not a substitute for convergence proof. The parent initially suggested an incorrect learning-rate normalization in a collaboration message; A26 corrected it before any theorem claim. For features h/√m, mean-loss learning rate cd implements the displayed score; for raw features h, the equivalent rate is cd/m.

## Independent quadratic-form calculation

Let F have rows f_j and h=tanh(Fx). Conditional on a fresh x, write f_j=(G_j/√d)e+v_j, where e=x/||x|| and v_j are independent Gaussian orthogonal components. Put q=||x||/√d. Then h_j=tanh(qG_j), and

||Fᵀh||²=(Σ_j G_jh_j)²/d+||Σ_jv_jh_j||².

Scalar laws of large numbers and the conditional chi-square law suggest, and provide a direct route to proving,

(d/m²)||Fᵀh||²→a²+b/γ,
(d/m²)||h||²→b/γ.

If the required covariance approximation Σ_F=a²FFᵀ+(b−a²)I+o_op(1) is proved, it follows that (d/m²)hᵀΣ_Fh→a⁴+b²/γ. The covariance approximation must include row-norm-dependent first Hermite coefficients, as well as the cubic-and-higher remainder. Merely ignoring row-norm deviations is insufficient without an operator bound.

## Calibration consequences: quantifier safeguards

A one-fresh-point annealed joint limit alone does not prove convergence in probability of model-conditional calibration error. It can prove lower bounds on its expectation using bounded score-measurable witnesses. In particular, CE_d≥|E[(Y−σ(S_d))sign(S_d) | training, features]|. After taking expectations and using the joint limit, the expected CE has lower limit at least |B(c)|, where B(c)=E[(σ(βZ)−σ(cU))sign(U)] and U=a²μ Z+τG. The zero-probability event U=0 permits the sign witness in weak convergence.

For β>0, B(0+)>0, B decreases strictly, and B(∞)<0. Its unique zero does not establish calibration. A29 supplied a stronger continuous-witness argument: with g(u)=E[σ(βZ)|U=u] and d_c(u)=g(u)−σ(cu), use tanh(k d_c(u)) and then let k grow. This gives liminf E CE_d≥E|d_c(U)| without asserting convergence of conditional laws.

Expected log-loss convergence additionally needs uniform integrability. Its limiting Taylor bound is L(c)≤log(2)−c a²μ²+c²E[U²]/8, yielding nontrivial small-positive-step risk improvement. In-probability statements require further concentration, for example a two-fresh-point joint limit with shared training data and features. These obligations are being checked explicitly.

## Verified preservation checkpoint

The sixteen-file continuation checkpoint was saved and every file fetched back at each immutable commit with exact text comparison:

- Brain: 5a4f30e2377bae881fd92dc6fa846a86f83911d5.
- Math Brain: ec1a48eaec96b6fb1b32d3df2c9d2de5a80556ff.

Subsequent reports and this note require the next checkpoint. The original T228 package remains frozen. No official problem registry count or novelty status has been changed.
