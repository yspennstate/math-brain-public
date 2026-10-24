# HARD7-06 route note — scalar cavity transform before checking

Written before any checker for this run.

Target remains F0095 (ordinary sparse Erdos--Renyi 3-colourability constant-location problem). The frozen metric carried into this run is `W_3=0.6565076662`; this route is aimed at structural progress, not decimal polishing.

Methods for this run: **B1 / B11 / B3**.

## B1 — change category: reparameterize the ACG q=3 message

For the ACG scalar message `alpha in [0,1]`, set

`lambda = (1-alpha)/(2+alpha) in [0,1/2]`, so `alpha=(1-2 lambda)/(1+lambda)`.

Then

`A(alpha)=(2+alpha)/3 = 1/(1+lambda)`,

`B(alpha)=(1+2alpha)/3 = (1-lambda)/(1+lambda)`.

If the Poisson incoming transformed messages are `lambda_i`, put

`r=prod_i(1-lambda_i)`, `s=prod_i(1-2lambda_i)`.

The ACG functional should collapse to

`Phi_d(mu) = E log(3-3r+s) - (d/2) E log(1+lambda+lambda'-2 lambda lambda')`,

where `mu` is the law of `lambda` and `lambda,lambda'` are iid from `mu`. The `E log(1+lambda)` factors cancel exactly. This is a cleaner cavity/Bethe form than the original alpha formula.

## B11 — dualize first-order stationarity into equality of laws

For an original-alpha insertion `z`, the previous contact calculation gives

`h_a(z)-h_a(0)=E log(1+z T)-E log(1+z Lambda)`,

with `Lambda~mu` and

`T=(1-2r+s)/(2-r)`.

I want to prove `T in [0,1/2]` exactly. If a local minimizer has infinite support, KKT contact equality holds at infinitely many support points with an accumulation point. The contact difference is analytic around `[0,1]`; hence it must vanish identically. Differentiating / expanding at zero then gives equality of every Hausdorff moment of `T` and `Lambda`, and compact moment determinacy yields the recursive distributional equation

`Law(T)=mu`.

Conversely this law equality makes the first variation vanish in every signed zero-mass direction (first-order stationarity only; it does not prove a minimum because the functional is nonconvex).

Thus the intended structural theorem is a dichotomy: **every local minimizer is either finitely supported or its transformed law is an exact cavity fixed point**.

## B3 — prove a stronger boundary consequence

Let `q=P(Lambda>0)` and let the number of positive incoming transformed messages be `K`. Poisson thinning gives `K~Pois(d q)`.

The numerator `delta=1-2r+s` obeys, after adding a new message `lambda`,

`delta_new = delta_old + 2 lambda (r_old-s_old)`.

Because `r_old>=s_old`, `delta>=0`; moreover `delta=0` iff at most one incoming lambda is positive. Therefore `T>0` iff `K>=2`. Any nontrivial cavity fixed point must satisfy the exact scalar atom equation

`q = 1-exp(-d q)(1+d q)`

or equivalently, for the boundary atom `p0=P(Lambda=0)=P(alpha=1)`,

`p0 = exp(-d(1-p0)) [1+d(1-p0)]`.

So every infinite-support local minimizer is forced to carry a positive atom at the compactification boundary `alpha=1` (unless it is the trivial delta_1 law, which is finite support). This gives an analytic explanation for the boundary atom found empirically/certifiably in the three-atom ACG witness.

Next: check the algebra exactly and bracket the nontrivial scalar atom roots at the current certified degree, but do not confuse those finite checks with proof of the functional theorem.