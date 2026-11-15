# Joint Gaussian second- and fourth-moment gate

T067-GAUSSIAN-FOURTH-GATE-001 v1. Status: proof (unaudited).
This is a computer-assisted auxiliary inequality, conditional on the stated
global derivative lemmas; it alone is not a reconstruction theorem.

Let g(s) and U_G(s) be the three-state Gaussian posterior observables in
COMPENSATED-REPLACEMENT-001 v1, with mean s m0, m0=(3,-3/2,-3/2), and
covariance (9s/2)P. Define the exact constants at L=1/10

 fU=57480763247/209952000000, fM=619609/3600000,
 qU=584087821/21870000, qM=12978097/720000,
 alpha=(100-qU)/fU,
 B=81[(1-qU/100) fM/fU+qM/100].

For every real s in [1/10,2/3],

 E(s)=alpha(s-g(s))-B s^2-U_G(s) > 0.                 (1)

## Curvature bound

The heat-with-drift generator on the zero-sum plane is
L=m0 dot grad+(9/4)Delta_P. Hence d^2 E f(Z(s))/ds^2=E L^2 f(Z(s)).
Differentiation and Gaussian integration by parts are valid on s>0 because
the observables and their derivatives through order four are bounded.
Choose an orthonormal basis e,f of the plane. For any symmetric fourth
derivative tensor with |D4f[h^4]|<=c4||h||^4,

 12 D4f[e,e,f,f]=D4f[(e+f)^4]+D4f[(e-f)^4]
                         -2D4f[e^4]-2D4f[f^4].

Thus the orthogonal mixed entry is bounded by c4, and |Delta_P^2 f|<=4c4.
The drift has squared norm 27/2 and norm <15/4. For global constants c2,
c31,c4 as in FOURTH-DERIVATIVES-001, the absolute second signal derivative
is consequently at most

  (27/2)c2+(135/4)c31+(81/4)c4.                       (2)

For F_1, the reviewed constants (1/5,1/2,3/5) give 1269/40<32.
For Q the new constants (20,38,99) give 14229/4<3600.
It follows that |E''(s)|<=C=32alpha+2B+3600. No assumption that a radial
function has positive logit Hessian is used.

## Whole-Gaussian quadrature with rigorous tails

Represent the Gaussian with independent standard normals z1,z2 by logits

 (3s+sqrt(3s)z1,
  -3s/2-sqrt(3s)z1/2+3sqrt(s)z2/2,
  -3s/2-sqrt(3s)z1/2-3sqrt(s)z2/2).

Split each normal axis in [-6,6] into 96 bins of width 1/8. In a bin
[a,b] the exact mass, first raw moment and second raw moment are
w=Phi(b)-Phi(a), m1=phi(a)-phi(b), m2=w+a phi(a)-b phi(b).
Use the conditional mean m=m1/w, and unnormalised variance v=m2-m1^2/w.
Let P0 be the total retained one-dimensional mass and D0=sum v. Both are
positive, P0<1. The omitted square probability is exactly 1-P0^2.

The map from (z1,z2) to the plane logits has squared operator norm 9s/2.
Thus the Hessian norms in normal coordinates are at most 9s/10 for F_1 and
90s for Q. On each product bin the first Taylor term about its conditional
mean averages to zero. Taylor's Hessian remainder is bounded by half that
norm times the summed conditional variances. Summing over both dimensions
gives quadrature errors <=(9s/10)P0 D0 and <=90s P0 D0, respectively.
The full omitted tails are bounded by 1-P0^2 for F_1 and 36(1-P0^2) for Q,
because 0<=F_1<=1 and 0<=Q<=36 throughout the simplex.

All bin moments, exponential evaluations and sums use 160-bit Arb balls.
Directed lower and upper endpoints are exported as exact dyadics; display
strings never determine an inequality. Normal symmetry pairs cells in the
producer. The formula used for Q is exactly

  [9(1+2 exp(2c) cosh(2b))/(1+2 exp(c) cosh(b))^2-3]^2,
  c=-9s/2-3sqrt(3s)z1/2, b=3sqrt(s)z2/2.

The producer includes both Taylor error and whole tail before taking an
upper endpoint for g and U_G. No floating-point arithmetic enters the gate.

## Continuous cover and independent replay

The rational grid is s_i=10/(100-i), i=0,...,85. Every one of its 86 endpoint
lower bounds for E is positive. On each interval [a,b], the curvature bound
implies E(s) >= its endpoint lower chord minus C(s-a)(b-s)/2. Therefore

  E(s) >= min(E_lower(a),E_lower(b))-C(b-a)^2/8.

All 85 right-hand sides are strictly positive by exact rational comparisons.
The checker also verifies both extreme endpoints, not merely interior samples.

checks/gaussian_fourth_gate_replay.py imports neither producer formulas nor
its arithmetic helpers. From the raw directed quadrature sums, P0,D0 and tail
it recomputes looser conservative rational bounds and verifies all 85 interval
margins. It separately evaluates the original three logits on all 96^2 signed
product bins at endpoints 0,42,85 using 192-bit Arb, without the producer's
cosh or sign-pair formula. Both quadrature observables must overlap the stored
enclosures. This is a same-worker replay, not an external audit or formal kernel.

## Reproduction

  python -X utf8 checks/gaussian_fourth_gate_arb.py --seconds 85 --count 86
  python -X utf8 checks/gaussian_fourth_gate_replay.py

Input configuration and per-endpoint hashes are in
checks/gaussian_fourth_gate_v1/report.json; the separate replay receipt is
checks/gaussian_fourth_gate_replay.json. A command can resume only its matching
source/configuration. Each endpoint is saved immediately. Memory estimate is
below20MB, one CPU. Arb's outward rounding is a software trust premise; this
is not a Lean proof. The cutoff composition is a separate claim.
