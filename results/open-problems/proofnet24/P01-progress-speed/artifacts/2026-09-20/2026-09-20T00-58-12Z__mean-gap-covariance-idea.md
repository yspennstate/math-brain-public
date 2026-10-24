# P01 T06 idea before checker — mean-gap covariance instead of range×range

Actual runtime model: GPT-5.6 Sol. Reasoning level: UNVERIFIED. GPT-6/maximum was requested but is not claimed.

Target: T06/P0066, parent-bias speed derivative for no-leaf Galton–Watson trees. Convention: parent edge has weight lambda, each child weight 1; reciprocal child bias beta=1/lambda.

Previous P01 theorem rewrote Aidekon's speed formula as

ell_lambda=(r-lambda)/(r+lambda),   r=E_mu[nu],

and proved

r'=-Cov_mu(nu,q),

with, for bounded offspring d<=nu<=D and 1<=lambda<d,

q_-(lambda)=1/(D-lambda/D) <= q <= q_+(lambda)=(d-1)/((d-lambda)(d-lambda/d)).

The previous run used Gruss/Popoviciu:

-Cov(nu,q) <= (D-d)(q_+-q_-)/4,

which paid for the full offspring width even when the tilted mean r sits near one endpoint.

New route: condition on N=nu under mu. If m_n=E_mu[q|N=n] and pi_n=mu(N=n), then

r' = sum_{n<m} pi_n pi_m (m-n)(m_n-m_m).

Since every m_n lies in [q_-,q_+],

r' <= Q * sum_{n<m} pi_n pi_m (m-n)
   = Q * (1/2) E|N-N'|,

Q=q_+-q_-.

But N,N' are iid in [d,D], so simultaneously

(1/2)E|N-N'| <= r-d,
(1/2)E|N-N'| <= D-r.

Therefore

r' <= Q min(r-d,D-r).

This is the key gain: the measure-change cost is charged to distance of the tilted mean from the nearer offspring endpoint, rather than to a product of two global ranges.

For a whole rectangle 1<=lambda<=L<d, use monotonicity of the envelope functions:

q <= q_+(L),
q >= q_-(1)=1/(D-1/D).

Define

Q* = q_+(L)-q_-(1),
c = L Q*.

Then

lambda r' - r <= c min(r-d,D-r)-r.

The right side is maximized at r=d if c<=1, and at r=(d+D)/2 if c>1. Thus, with

M(d,D,L)=min{ d, [D+d-c(D-d)]/2 },

condition c(D-d)<D+d gives the uniform sign margin

ell'_lambda <= -2 M(d,D,L)/(D+L)^2 <0

for every 1<=lambda<=L.

This should strictly improve the previous D<=10 result. Candidate exact checkpoints to verify after writing this idea:

- d=2,D=74,L=6/5: expected positive but very small margin;
- d=2,D=12,L=4/3: expected larger new bias extension;
- d=2,D=20,L=5/4: intermediate breadth/depth point.

This route is complementary to NM13-05: it uses no two-point p(1-p) rarity factor and applies uniformly to every offspring law in the bounded support interval.