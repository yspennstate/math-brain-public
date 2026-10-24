Actual runtime model: GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6/maximum was requested but no authenticated model/effort telemetry is exposed.

# P01 T06 idea before code — lift the conditional-degree secant method to arbitrary minimum offspring d>=3

Goal: obtain a genuinely new broad-support derivative-sign region beyond the He--Wang--Xiang low-parent-bias interval, complementary to NM13-05's adjacent/rare-defect coupling work.

Freeze parent-bias convention: at a vertex with k children, parent transition probability is lambda/(lambda+k) and each child has probability 1/(lambda+k). The historical child bias is beta=1/lambda. Work on a no-leaf Galton--Watson law with bounded support d<=nu<=D, d>=3, and 1<=lambda<d.

Inherited exact P01 reduction:

ell=(r-lambda)/(r+lambda),

ell'=2(lambda r'-r)/(r+lambda)^2,

r'=-Cov_mu(nu,q)=r E_mu q-E_mu[nu q],

q=[S+(lambda-1)U]/[S(lambda-1+S)],

where U=sum(-B_i') and mu is the Aidekon u-tilt.

Consume, rather than reprove, the R02 logarithmic escape cone

1/(D-lambda) <= (-B')/B <= 1/(d-lambda),

and the standard escape comparison

1-lambda/d <= B <= 1-lambda/D.

Conditional on nu=n these imply the degree-dependent pathwise interval

a_n(lambda) <= q <= b_n(lambda),

with

a_n=(D-1)/[(D-lambda)(n+lambda(D-n-1)/D)],

b_n=(d-1)/[(d-lambda)(n+lambda(d-n-1)/d)].

Let g_n=n a_n. For real x in [d,D], b_lambda(x) is decreasing convex and g_lambda(x) is increasing concave. Therefore, if B_lambda(r) is the chord through (d,b_d),(D,b_D) and G_lambda(r) the chord through (d,g_d),(D,g_D), then

r' <= r B_lambda(r)-G_lambda(r).

For a rectangle 1<=lambda<=L<d, b_lambda(n) increases in lambda. Also g_D(lambda) increases in lambda. For the candidate regions below, g_d(lambda) decreases on [1,L], because the denominator derivative

D-2d-1 - 2 lambda (D-d-1)/D

is positive at lambda=L. Thus one may form a uniform upper chord B*(r) from b_L(d),b_L(D), and a uniform lower chord G*(r) from g_L(d),g_1(D), obtaining

lambda r'-r <= Psi_{d,D,L}(r):=L[r B*(r)-G*(r)]-r

whenever the bracket is nonnegative, while if it is negative the desired sign is automatic. Equivalently, negativity of max Psi on [d,D] is a valid uniform certificate. Psi is a concave quadratic, so its exact maximum is attained at an endpoint or its explicit vertex.

Candidate source-level regions to certify exactly:

1. d=3, D=163, L=7/4. This is genuinely beyond the published d=3 endpoint theta_3=3/(1+sqrt(2/3))=1.6515..., while allowing arbitrary offspring laws on every integer degree 3,...,163. Preliminary exact arithmetic gives a negative quadratic maximum and an ell' margin larger than 1/3,000,000.

2. Breadth extension at the same minimum degree: d=3, D=760, L=17/10, again beyond theta_3, with preliminary ell' margin larger than 1/10,000,000,000.

3. Further breadth/depth tradeoff: d=3, D=8264, L=5/3, with preliminary ell' margin larger than 1/500,000,000,000.

These regions do not duplicate NM13-05: that worker now treats the adjacent {3,4} family, including rare tails up to lambda=2.99. The present attack is distribution-free over wide bounded support and targets a different obstruction: the environment-derivative covariance.

Next step: write an exact Fraction checker only for the quadratic constants, endpoint monotonicity and clean margins; then write the full proof and immutable run report.