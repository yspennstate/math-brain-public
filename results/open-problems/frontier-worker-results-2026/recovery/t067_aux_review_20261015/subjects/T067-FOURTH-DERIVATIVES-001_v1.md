# Global derivative bounds for the three-state radial fourth observable

Claim T067-FOURTH-DERIVATIVES-001 v1. Status: proof (unaudited).
This is an auxiliary analytic bound. No improved reconstruction cutoff, novelty,
or priority is asserted. Two local algorithms are not two independent auditors.

For z in R^3 let p_i=exp(z_i)/sum_j exp(z_j), P=I-11^T/3,
A=||3p-1||^2=9 sum_i p_i^2-3, Q=A^2, v_i=(e_i-1/3)/2.
For all h,r in R^3 the following bounds hold:

  |D Q[v_i]| <= 8;
  |D^2 Q[h,h]| <= 20 ||Ph||^2;
  |D^3 Q[h,h,h]| <= 38 ||Ph||^3;
  |D^3 Q[r,h,h]| <= 38 ||Pr|| ||Ph||^2;
  |D^4 Q[h,h,h,h]| <= 99 ||Ph||^4.

## Reduction to exact polynomial inequalities

Q is symmetric under simultaneous permutation of coordinates and unchanged
by adding a constant to z. Each derivative therefore sees only projected
directions. Any nonconstant direction, after permutation, translation and
positive rescaling, is h=(0,t,1), 0<=t<=1. Its projected squared norm is
N=2(1-t+t^2)/3>0. The identically constant direction gives zero derivatives.
The closed simplex is covered by p=(u,(1-u)v,(1-u)(1-v)), u,v in [0,1].
Working first with independent p0=a,p1=b,p2=1-a-b, define

  D_h f = a(h0-m) partial_a f + b(h1-m) partial_b f,
  m=sum_i p_i h_i.

This is exactly the derivative under softmax logit translation z -> z+epsilon h,
by differentiating p_i. Iterating gives d_k=D_h^k Q. Define
V_j=D_{e_j} d_2. The V_j sum to zero, and D^3 Q[r,h,h]=sum_j r_j V_j.
Thus ||V||<=38 N implies the mixed bound by Cauchy-Schwarz and V perpendicular
to 1. Also DQ[v_i]=D_{e_i}Q/2; symmetry reduces all i to i=0.

It remains to check these eight polynomials on the closed cube:

  8 +/- D_{e0}Q/2;
  20 N +/- d_2;
  99 N^2 +/- d_4;
  38^2 N^3 - d_3^2;
  38^2 N^2 - sum_j V_j^2.

The producer forms these polynomials by repeated differentiation. Each is
converted exactly from power to tensor Bernstein coefficients on [0,1]^3.
On each box, nonnegative coefficients imply nonnegative polynomial values
because Bernstein basis functions are nonnegative. Unresolved boxes are split
at their dyadic midpoints, cyclically in u,v,t, using exact de Casteljau sums.
For every polynomial the accepted paths are prefix-free and have total dyadic
volume one. Therefore the closed cube is covered. All 124 leaves pass; there
are no unresolved boxes. Counts in the recorded order are 9,17,18,9,18,19,17,17.
Zeros on boundary faces are allowed. All arithmetic is integer or rational.

## Independent local derivation and replay

checks/fourth_derivative_replay.py imports neither the producer nor its engine.
It expands p_i exp(epsilon h_i)/sum_j p_j exp(epsilon h_j) to order four by
coefficient division, forms A and Q by convolution, and multiplies the nth
coefficient by n!. All eight resulting polynomials equal the producer's saved
power polynomials exactly. A separate Fraction-based power-to-Bernstein
conversion and integer de Casteljau replay checks all 124 boxes and exact cover.
A deliberately zero Hessian bound is rejected at p=(1/2,1/2,0), h=(0,1,1).
This algebraic replay is verification by the same worker, not an external audit.

## Reproduction and limits

  python -X utf8 checks/fourth_derivative_certificate.py --seconds 65
  python -X utf8 checks/fourth_derivative_replay.py

The producer is resumable and final receipts are frozen. A fresh reproduction
uses a separate copy of these scripts and the Bernstein engine. The script's
memory guard requires 2 GB free; working memory is estimated below 500 MB,
one CPU. Neither floating quadrature nor sampled derivative extrema is used.
Passing these inequalities alone supplies neither a fourth-order replacement
lemma nor a bound on the Gaussian posterior fourth moment. Those remain open.

## Frozen evidence hashes

- checks\fourth_derivative_v1\report.json: `ea392acae0bb563dbc963e902f17423b2387a589a3bd337763740d874a5c27bf`
- checks\fourth_derivative_replay.json: `dba52639ad83694ad7bffb2b351ee1c4e057cf65838d3ea17f2a79d459a39149`
- checks\fourth_derivative_certificate.py: `59cd7bfc64083904abe5e6328c324760cbe0d380dee504316e6ef851f4cffed3`
- checks\fourth_derivative_replay.py: `1e12900a72679e1aa7fd1071ce61b09c05983ae7da14e3fe9f14dd945bf3a3f7`
- checks\softmax_derivative_certificate.py: `2ada8227b14bf773c4023dbd3c5651967aa439aaa286f7736b8bcab34f786d75`
