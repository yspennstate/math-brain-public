# Three-state softmax directional derivative bounds

Claim: T067-SOFTMAX-DERIVATIVES-001, version 1.
Status: proof (unaudited). No novelty or priority assertion.

Let F(z)=exp(z_1)/(exp(z_1)+exp(z_2)+exp(z_3)) on R^3, and let
P=I-11^t/3 be the orthogonal projection onto the zero-sum plane. For every
z,h in R^3,

    |D^2F(z)[h,h]| <= (1/5)||Ph||^2,
    |D^3F(z)[h,h,h]| <= (2/5)||Ph||^3,
    |D^4F(z)[h,h,h,h]| <= (3/5)||Ph||^4.                 (1)

In particular these also hold with ||h|| on the right. Moreover

    |D^3F(z)[r,h,h]| <= (1/2)||Pr|| ||Ph||^2.          (2)

The hardest finite step is the ten polynomial inequalities below. It is
certified with exact integer Bernstein coefficients and independently replayed
using rational arithmetic. No sampling, floating-point estimate, or unchecked
rounding is used for (1). The certificates prove only these derivative bounds,
not a reconstruction result or a sharpened Lindeberg remainder by themselves.

1. Derivative polynomials.

Write p_i=softmax(z)_i, m=sum_i p_i h_i, r=h_1-m, and

    k2=sum_i p_i(h_i-m)^2,
    k3=sum_i p_i(h_i-m)^3,
    k4=sum_i p_i(h_i-m)^4-3*k2^2.

The exponential tilt p_i(t)=p_i exp(t h_i)/sum_j p_j exp(t h_j) satisfies
p_i'=p_i(h_i-sum_j p_j h_j). Differentiating this identity, or differentiating
the logarithm of the denominator, gives

    D2=p_1(r^2-k2),
    D3=p_1(r^3-3 r k2-k3),
    D4=p_1(r^4-6 r^2 k2-4 r k3+3 k2^2-k4).           (3)

The producer differentiates by the polynomial operator sum_i p_i(h_i-m)d/dp_i
four times and checks (3) symbolically. The separate replay constructs (3)
directly from the centered moments and compares every power coefficient.

2. Reduction to ten polynomials on a cube.

Adding a constant to h does not change any derivative or Ph. A zero direction
is trivial. Otherwise translate and scale the direction to have minimum 0
and maximum 1. Replacing h by -h and interchanging indices 2 and 3 reduces
to exactly the two cases

    h=(0,t,1), or h=(t,0,1),             0<=t<=1.

The first case covers an endpoint value of h_1 (the upper endpoint is reversed
by -h); the second covers an intermediate value. Both have

    N=||Ph||^2=(2/3)(1-t+t^2)>=1/2.

Every probability triple is represented by

    p=(u,(1-u)v,(1-u)(1-v)),             0<=u,v<=1.

This includes all boundary faces, including p_1=1. Thus it suffices, in each
direction case, to prove on [0,1]^3 the five inequalities

    (1/5)N + D2 >= 0,     (1/5)N - D2 >= 0,
    (4/25)N^3 - D3^2 >= 0,
    (3/5)N^2 + D4 >= 0,   (3/5)N^2 - D4 >= 0.        (4)

All quantities in (4) are polynomials with rational coefficients. Taking a
nonnegative square root in the third one is valid since N>0. Scaling back
proves (1).

3. Exact finite certificate and its verification.

The producer is checks/softmax_derivative_certificate.py and the complete
certificate is checks/softmax_derivative_v1/report.json. For a power polynomial
sum_e a_e x^e of coordinate degrees n=(n_1,n_2,n_3), its Bernstein coefficients
on the cube are exactly

    b_k = sum_(e<=k) a_e product_j binom(k_j,e_j)/binom(n_j,e_j).       (5)

The Bernstein basis consists of nonnegative functions on the cube which sum
to one. A nonnegative coefficient list therefore proves a nonnegative
polynomial on that cube. Formula (5) is applied using common integer
denominators. Cubes with a negative coefficient are bisected at their midpoint
in the coordinate depth modulo 3. Exact de Casteljau subdivision gives the
coefficients on both children; denominators are powers of two times the root
denominator. A negative coefficient alone is never treated as a counterexample.

The saved certificate has 10 roots, 68 accepted leaves, and 126 visited nodes.
Every leaf coefficient is nonnegative. Each leaf includes its full binary path,
minimum and maximum integer coefficient, and hash of the complete ordered
coefficient list. The independent replay rebuilds all ten polynomials from (3),
converts their coefficients by direct Fraction evaluation of (5), and subdivides
with rational averages. It compares every leaf list through its hash and exact
extrema, and verifies that every non-leaf has both children. Consequently the
accepted leaves cover the entire cube, with no missing region. Hashes protect
the recorded coefficient lists; the nonnegativity argument is (5) and the
explicit rational replay, not a hash alone.

Run checks/softmax_derivative_independent.py to recompute the verification from
scratch. Its receipt checks/softmax_derivative_independent.json records the
producer, certificate, and replay source hashes. To regenerate the producer
without deleting its existing checkpoint, run replay_softmax_from_scratch.py;
it copies the unchanged producer into a new directory inside checks/ and
compares all mathematical certificate fields from a fresh run.

Negative controls prevent a vacuous norm check. At p=(1/4,0,3/4) and
h=(0,1/2,1), N=1/2, |D2|=3/32, and |D4|=15/128. Thus replacing 1/5 by 1/10
in (1), or 3/5 by 2/5, fails at that exact point. At p=(1/2,0,1/2) and the same
h, |D3|=1/8, which rejects the smaller constant 1/5 for the third derivative.
These controls are exact rational checks, not certificates for the positive
statements by themselves.

4. Mixed derivative corollary.

All arguments can first be projected by P. Let B=D^3F(z). It is a symmetric
trilinear form and |B[w,w,w]| <= K||w||^3 with K=2/5. For unit vectors r,h,
polarization with t=1/2 gives

    3 B[h,h,r] = B[h+r/2]^3 - B[h-r/2]^3 - (1/4)B[r]^3,

where B[w]^3 denotes B[w,w,w]. The sum
||h+r/2||^3+||h-r/2||^3 is at most 7/2: it is an even convex function of
<h,r> in [-1,1], hence maximized at an endpoint, where it equals
(3/2)^3+(1/2)^3=7/2. The right side is consequently at most
K*(7/2+1/4)=15K/4 in absolute value. Dividing by 3 gives 5K/4=1/2.
Homogeneity and the zero-vector cases prove (2).

NEXT: Use these bounds in a separately versioned analytic Lindeberg proof;
retain all existing signed-comparison and d0=1981 submissions unchanged.
