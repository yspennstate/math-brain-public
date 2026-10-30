SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B04, 2026-09-23T14:44:27Z.
attacking: entropy-optimal third-volume reweighting via an exact Gibbs dual, with the first quantitative compound-hub implication and a dense rank-four stress family.

# Early substantive checkpoint

Let `M=A[I,J]` be an original-coordinate cross block. For every physical row triple `S`, define

`a_S = det(M_S M_S^T) = sum_{|T|=3} det(M[S,T])^2`.

For `h in [1/2,3/4)`, consider probability laws `mu` on supported row triples satisfying every physical row marginal `alpha_i(mu)<=h`, and lift them to full 3x3 minors by the canonical conditional column-volume law. The determinant/entropy currency is then

`G(mu)=exp(sum_S mu_S log(a_S/mu_S))`.

The first calculation of this run is the exact finite-dimensional dual

`G_h(M) = inf_{lambda_i>=0} exp(h sum_i lambda_i) * sum_S a_S exp(-sum_{i in S}lambda_i)`

whenever the marginal polytope is feasible (with the standard limiting interpretation at a boundary). This follows from the Gibbs variational identity and Lagrange duality. At an optimizer, the tilted law is

`mu_lambda(S) proportional to a_S exp(-sum_{i in S}lambda_i)`,

and every positive multiplier is attached to a saturated row marginal. Thus the current fleet's vague phrase 'poor determinant/entropy currency' is equivalent to a concrete soft hub potential.

For one hub `0`, if `Z1=sum_{S contains0}a_S`, `Z0=sum_{S not contains0}a_S`, and the other row constraints stay feasible after the tilt, the exact optimizer with hub marginal `h` is

`mu(S)=h a_S/Z1` on incident triples and `(1-h)a_S/Z0` off the hub,

with

`G_h=(Z1/h)^h (Z0/(1-h))^(1-h)=Z exp[-D_Ber(h||Z1/Z)]`.

This is the first essential missing implication attempted early: quantitative near-coloop behavior is converted into an exact Bernoulli entropy price, rather than a reciprocal tiny-minor selection. The final report will connect the recession directions of this dual to fleet02/B04's completed exact support-defect theorem and apply the resulting weight to a dense target-valid rank-four family.
