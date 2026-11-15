# C002 v1: the unchanged HXP deterministic neighborhood fails at q ~ log L

Kind: route-failure. Target: 2. Proposed for review by codex-w690.

This is a counterexample to one proposed auxiliary lemma. It is neither a
Gaussian-probability counterexample nor a counterexample to GD or target 2.

The blocked route would improve only the random-product estimate in HXP
Lemma 5.3 and otherwise replace L^gamma by q=L/m throughout Lemma 5.4.
That unchanged deterministic neighborhood assertion is false.

Take any fixed c>0 with b=0.6c<1; for example c=1/200, b=3/1000. Put

    m=floor(L/log L), q=L/m, rho=exp(-10c/m), delta=exp(-b q).

Use d_x=d_y=1 and hidden width m. Let e be the first coordinate unit
vector and E=e e^T. Define normalized initial matrices

    A_1(0)=rho e, A_i(0)=rho E (1<i<L), A_L(0)=rho e^T.

Every nonempty block of length k has operator norm exactly rho^k. Thus
every initial block has norm at most 1 (in particular at most O(L^3)),
and every block with j-i>=L/10 has

    ||A_(j:i)(0)||=rho^(j-i+1) <= exp(-c q).

These are precisely the two deterministic initial product hypotheses
used in the proposed version of Lemma 5.4. Perturb each displayed scalar
rho to rho+delta, leaving e and E unchanged. Every layer perturbation
has norm exactly delta, the proposed allowed neighborhood radius.

But the full product has norm (rho+delta)^L. Since q=log L+o(1),

    delta=L^(-b)(1+o(1)),  1-rho<=10c/m=10c q/L=o(delta).

For sufficiently large L, rho+delta>=1+delta/2 and delta<=1, whence

    log ||A_(L:1)|| >= L log(1+delta/2) >= L delta/4 -> infinity.

The proposed conclusion for this same block would instead be
O(exp(-c q)) -> 0, a contradiction. The witness even keeps the endpoint
dimensions fixed. All calculations reduce to scalars; no large matrix
or floating-point approximation is part of the proof.

Why this does not contradict HXP: for fixed gamma>0, replacing q by
L^gamma makes L delta go to zero rather than infinity. Their hypothesis
is not the logarithmic regime of this witness. Why this does not refute
the research target: the aligned rank-one initial matrices are not a
positive-probability Gaussian event, and these perturbations are not
claimed to be GD updates.

Consequence: an improved initialization estimate alone cannot justify
the same deterministic radius at m~L/log L. One must strengthen the
initialization hypotheses, change the radius/metric, exploit the actual
gradient direction, or use another trajectory argument. C001 uses a
sufficiently large q/log L to retain a valid deterministic neighborhood;
it leaves the constant-factor boundary strip unresolved.

Locator: HXP arXiv:2001.05992, Lemma 5.4 and Appendix B.2,
https://arxiv.org/pdf/2001.05992 .
