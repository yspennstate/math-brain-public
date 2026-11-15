# Independent checks and attempted failures

## 1. The shell minimization by a second method

For fixed R<N, let w_k=(2k+1)^2. Lagrange multipliers for
sum w_k d_k^2 under sum d_k=1 give

    2w_k d_k=lambda,
    lambda=2/(sum w_k^(-1)),
    min sum w_k d_k^2 = 1/(sum w_k^(-1)).

This agrees with the Cauchy-Schwarz proof in PROOF.md. Strict convexity
gives uniqueness for each finite N. Negative differences cannot lower
the minimum. The finite-support requirement is respected before taking
N to infinity; the infinite tail profile itself need not be square summable.

Exact small case: R=2, N=4 gives weights 25 and 49. The optimizer has
d_2=49/74, d_3=25/74 and energy 1225/74. Direct substitution gives

    25(49/74)^2 + 49(25/74)^2 = 1225/74.

The earlier tent has energy 37/2, larger by 72/37. With R=1,N=2,
there is a single increment and the energy is 9, agreeing with the earlier
R=1 shell count. These are hand calculations, not computer output.

## 2. Recheck the rational identity and the correction coefficient

The numerator in F(k)-F(k+1) is 36k(k+1)-3. Put v=k(k+1).
Then

    (12k^2+1)(12(k+1)^2+1) = 144v^2+24v+13,
    [36v-3](2k+1)^2 = [36v-3](4v+1)
                    = 144v^2+24v-3.

Their difference is 16, confirming the sign and numerator in (9).
There is no missing endpoint term: F(N) tends to zero.

Independently of F, integrate x^(-2)/4 on each interval [k,k+1]:

    integral_k^(k+1) dx/(4x^2) = 1/[4k(k+1)],
    1/[4k(k+1)] - 1/(2k+1)^2
      = 1/[4k(k+1)(2k+1)^2]
      = 1/(16k^4)+O(k^(-5)).

Integral bounds on the two convergent power sums now give

    S_R = 1/(4R) - 1/(48R^3)+O(R^(-4)),
    1/S_R = 4R+1/(3R)+O(R^(-2)).

This separately confirms both coefficients 4 and 1/3. The telescoping
identity in the proof gives the stronger O(R^(-3)) remainder for 1/S_R.
It also proves A_R>4R; thus 4 is optimal within the specified shell class.
It does not prove a lower bound 4R on the actual cube capacity.

The old and new explicit bounds differ by

    (28R-1/R)/3 - [4R+1/(3R)] = (16R-2/R)/3 > 0

for every integer R>=1. This checks that the claimed improvement holds
at small R as well as asymptotically.

## 3. Independent probability comparison using optimized Holder

Let P=N(0,G), Q=N(-t1,G), D a fixed event, p=P(D), q=Q(D), and
s=t sqrt(1^T G^(-1)1). Under Q,

    E_Q[(dP/dQ)^r] = exp(r(r-1)s^2/2), r>1.

Holder gives

    p <= q^((r-1)/r) exp((r-1)s^2/2),
    q/p >= exp[-log(1/p)/(r-1)-r s^2/2].

For s>0 choose r-1=sqrt(2 log(1/p))/s. This proves directly

    q/p >= exp[-s sqrt(2 log(1/p))-s^2/2].              (A)

The case s=0 is immediate. This is stronger than the elementary normal-tail
bound used in the proof and confirms its leading coefficient independently.
For R<=c/(t^2 H), H=log(1/t), the worst allowed estimates are

    s^2 <= 4c/H+o(1/H),
    log(1/p_R(h_*)) <= (4+2epsilon)H.

Thus the limiting exponent in (A) is at most

    sqrt(4c * (8+4epsilon)) = 4 sqrt(c(2+epsilon)).

Setting epsilon to zero after taking the strict inequality gives
c<(log 2)^2/32. This re-derives the denominator 32 without conditional
normal means or the +2 estimate in PROOF.md.

## 4. Can the logarithmic loss disappear for general increasing events?

There is an explicit obstruction. For R>=2 let G=G_{B_R},
a_R=cap(B_R), e_R=G^(-1)1, and Z_R=e_R^T X/sqrt(a_R).
It is standard normal. Choose b_R>0 so Q(b_R)=R^(-2), and define the
fixed increasing event in the shifted coordinates y by

    D_R = {e_R^T y >= sqrt(a_R)b_R-h_* a_R}.

It is increasing because e_R is the nonnegative equilibrium measure.
Its level-dependent probability is exactly

    P(X-h1 in D_R) = Q(b_R+(h-h_*)sqrt(a_R)).

For any fixed delta>0 set t_R=delta/(b_R sqrt(a_R)). The ratio between
the probabilities at h_*+t_R and h_* is

    Q(b_R+delta/b_R)/Q(b_R) -> exp(-delta).             (B)

To check this limit, integration by parts and the first inequality below
give the elementary Mills bounds, for b>0,

    varphi(b)b/(b^2+1) <= Q(b) <= varphi(b)/b.

The upper bound follows by replacing 1 by z/b in the tail integral.
The lower bound follows by integration by parts, as in PROOF.md. Applying
both bounds at b and b+delta/b proves that the ratio is

    (1+o(1)) [b/(b+delta/b)]
      exp(-delta-delta^2/(2b^2)),

which proves (B). The same bounds give

    b_R^2 = 4 log R+O(log log R),
    t_R^2 a_R log R -> delta^2/4,
    t_R^2 a_R -> 0.

For delta>log 2 the ratio is eventually below 1/2, even though the squared
Gaussian displacement tends to zero. Thus an event-independent bound
claiming a half-ratio throughout t^2 cap(B_R)<=c, for any c>0 and all
increasing events, is false. The sqrt(log(1/p)) sensitivity is real for
half-spaces. These D_R are not connection events and do not establish
the actual scale of L_rel.

## 5. Other cases checked

- The optimization is over deterministic shell test functions; it supplies
  an upper bound on capacity and no event-specific improvement of the score.
- The critical arm bound used is a limsup statement. The proof retains
  epsilon>0 until the final limit and never uses q=4 in Muirhead's theorem.
- If theta(h_*)>0, all inequalities still hold. No step assumes critical
  nonpercolation or a positive one-arm exponent.
- The ratio defining L_rel need not be monotone in R. Uniform control of
  every smaller radius, plus finite-radius continuity, is essential.
- Floor errors vanish after multiplication by t^2 log(1/t). The endpoint
  constant is a liminf bound, not a finite-t equality.
- Constants refer to SRW Green covariance. Rescaling phi changes level
  differences and the displayed coefficient accordingly.

No numerical computation or simulation was run. All load-bearing constants
have been checked by two algebraic or probabilistic routes.
