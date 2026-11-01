# P0221 — research record, 2026-10-11

## Exact target and model distinctions

David Aldous, Omer Angel and Nathanael Berestycki, *Online Random Weight Minimal Spanning Trees and a Stochastic Coalescent*, draft June 16, 2008, pp. 2–4, is the source. Its author's open-problem page, retrieved today, still asks for existence and identification of the limit and says that a rigorous existence proof is absent.

The combinatorial model reveals each edge of K_n exactly once, in a uniformly random order independent of independent Uniform[0,1] weights. An online algorithm must irrevocably accept or reject at revelation, and must construct a spanning tree almost surely. Write C_n for the infimum of expected total cost.

The Poisson model has a Poisson process of intensity binomial(n,2) dt dw on [0,1] × [0,infinity); independent uniform edge marks. Equivalently, each unordered vertex pair has its own independent intensity-one Poisson offer process dt dw. Thus edges can be offered repeatedly, with unbounded weights. Write P_n for its optimum. For a current forest with component masses x=(x_1,...,x_k), sum x_i=n, write F(x) for the optimal additional cost with one unit of time remaining. For k=1, F=0. The source's Theorem 3 gives

    2 F(x) = sum_{i<j} x_i x_j (F(x)-F(x merged at i,j))^2,
    F(x) > F(x merged at i,j).

The source supplies existence and its verification theorem: a nonnegative strictly decreasing-under-mergers H, vanishing at k=1, satisfying

    H(x) <= (1/2) sum_{i<j} x_i x_j (H(x)-H(x merged at i,j))^2

is an upper bound on optimal cost. The proof of that theorem also works from an arbitrary starting forest, as explicitly stated in its proof on p. 5. We use this established finite theorem; we do not assume its conjectural infinite-dimensional limit. The conjecture on p. 7 concerns convergence of these value functions to a PDE solution, including continuity under coordinatewise convergence of empirical component distributions. That continuity is not supplied by the finite recursion.

The primary target is existence and value of lim C_n; existence/value of lim P_n is the associated Poisson question. The draft expressly lacks a complete proof that C_n-P_n tends to zero. No result below removes that gap.

## 1. Uniqueness and explicit branch of the finite Poisson recursion — proved

Consider a fixed state, its nonnegative child costs c_r, and positive weights w_r=x_i x_j, indexed by pairs r=(i,j). An admissible value f has f>max_r c_r and

    sum_r w_r (f-c_r)^2 = 2f.

It follows that f>0. Put S(f)=sum_r w_r(f-c_r). Since 0<=c_r<f, we have (f-c_r)^2<=f(f-c_r). After multiplying by w_r and summing, 2f<=f S(f), so S(f)>=2.

Suppose f and g are two admissible roots. Put A=sum w_r, B=sum w_r c_r, D=sum w_r c_r^2. Subtract their quadratic equations to obtain

    (f-g)[A(f+g)-2B-2]=0.

But the bracket is S(f)+S(g)-2>=2, so it cannot vanish. Hence f=g. This proves uniqueness at a state. Induction on the number of components, starting with the one-component value zero, proves uniqueness of the entire finite family satisfying the source's equality and strict merger inequalities. Existence is supplied by Theorem 3(a), not asserted for arbitrary nonnegative child data under the strict side conditions.

Since A>0, the quadratic is A f^2 -2(B+1)f+D=0. At its admissible root the derivative is 2(S(f)-1)>=2, so the admissible root is the larger root:

    f = [B+1 + sqrt((B+1)^2-A D)] / A.

The discriminant is strictly positive because the derivative at that root is positive. This resolves the finite uniqueness uncertainty explicitly noted on pp. 4–5 of the source; it does not resolve the conjectured PDE uniqueness or the limit.

Formalization: AlgebraCheck.lean contains the pointwise square inequality, the finite-sum slope inequality, and the factored quadratic uniqueness argument. The Lean 4 check completed with exit code zero, with only harmless unused-tactic linter warnings. These algebraic lemmas are kernel-checked; the entire stochastic argument is a written mathematical proof, not a Lean formalization.

## 2. An explicit reciprocal-component supersolution — proved

For every starting forest, define

    H(x) = (8/(3n)) (sum_i 1/x_i - 1/n).

For one component H=0, and otherwise H>0. For a merger of x and y its decrease is

    Delta H = (8/(3n)) [1/x+1/y-1/(x+y)] > 0.

Write k for the number of components and introduce

    q = n sum_i 1/x_i,
    T = sum_{i<j} x_i x_j/(x_i+x_j)^2,
    D = sum_{i<j} x_i x_j [1/x_i+1/x_j-1/(x_i+x_j)]^2.

All masses are positive. Direct algebra for each pair gives

    xy [1/x+1/y-1/(x+y)]^2 = x/y + y/x + xy/(x+y)^2.

Summing x_i/x_j+x_j/x_i over unordered pairs gives q-k, since the full ordered sum is (sum x_i)(sum 1/x_i)=q and its diagonal consists of k terms equal to one. Thus D=q-k+T. Also

    q = k + sum_{i<j}(x_i/x_j+x_j/x_i) >= k+2 binomial(k,2)=k^2,

because x/y+y/x-2=(x-y)^2/(xy)>=0.

We claim D >= (3/4)(q-1). For k>=3,

    D-(3/4)(q-1) = q/4-k+3/4+T
       >= (k^2-4k+3)/4+T
       = (k-1)(k-3)/4+T >= 0.

For k=2, q=(x+y)^2/(xy)>=4, and T=1/q. Hence

    D-(3/4)(q-1) = q/4-5/4+1/q
       = (q-1)(q-4)/(4q) >=0.

For k=1 both sides of the verification inequality are zero. For k>=2, with a=8/(3n),

    (1/2) sum x_i x_j (Delta H)^2
       = (a^2/2)D >= (a^2/2)(3/4)(q-1)
       = a(q-1)/n = H(x).

Thus all hypotheses of the source's verification theorem hold and

    F(x) <= (8/(3n)) (sum_i 1/x_i - 1/n).

In particular

    P_n <= (8/3)(1-1/n^2),   n>=1.

This improves the draft's explicit Poisson bound 4(n-1)/n for n>2. It is not claimed to be a new result in the whole literature, and it is not a bound for C_n without a model-transfer argument. At n=2 the bound is sharp. The factor 8/3 is the least possible uniform coefficient for this particular H=a/n*(sum 1/x_i-1/n) family: equality in the verification ratio occurs for two equal masses. This is optimality of a trial family, not optimality of the online algorithm.

## 2b. A stronger supersolution: limsup P_n <= 2 — proved

Define, for k components of total mass n,

    J(x) = (2/n) sum_i 1/x_i + (2/n^2)(k-2)
         = (2/n^2)(q+k-2),

where q=n sum_i 1/x_i as above. At k=1 this is zero. At k>=2 it is positive, and a merger of masses x,y decreases J by

    Delta J = (2/n)[1/x+1/y-1/(x+y)] + 2/n^2 > 0.

Put d_ij=1/x_i+1/x_j-1/(x_i+x_j), W=sum_{i<j} x_i x_j, and R=sum_{i<j} x_i x_j/(x_i+x_j). We already proved D=sum x_i x_j d_ij^2=q-k+T. Also

    E=sum_{i<j} x_i x_j d_ij
      =sum_{i<j}(x_i+x_j-x_i x_j/(x_i+x_j))
      =(k-1)n-R.

Consequently

    (1/2)sum x_i x_j (Delta J)^2 - J
      =(2/n^2)[D+2E/n+W/n^2-(q+k-2)]
      =(2/n^2)[T-2R/n+W/n^2]
      =(2/n^2)sum_{i<j} x_i x_j [1/(x_i+x_j)-1/n]^2 >=0.

All identities are finite sums; the pair sum is empty for k=1, where the assertion is again zero. Thus J satisfies the source's verification theorem and

    F(x) <= (2/n)sum_i 1/x_i + 2(k-2)/n^2,
    P_n <= 2+2/n-4/n^2,
    limsup_{n->infinity} P_n <= 2.

For exactly two components x+y=n, the verification remainder is zero, and J(x,y)=(2/n)(1/x+1/y)=2/(xy), the exact optimum. For three or more components every pair has x_i+x_j<n, so the verification remainder is strictly positive.

This is a stronger asymptotic bound than the reciprocal supersolution in section 2. It uses a component-count correction of order 1/n^2 per component. It is a Poisson result only. No novelty in the wider literature is asserted.

## 2c. A strict asymptotic improvement below 2 — proved

We can exploit the positive verification remainder of J during an initial interval. This gives the explicit bound

    limsup P_n <= (33-18 exp(1/3))/4 = 1.9697440871... .

Here is a full finite-time argument. Let elapsed time be s and remaining time t=1-s. Start from n singleton components and run the J-threshold algorithm up to elapsed time s_0=1-exp(-1/3). An offer between masses x,y is accepted if its weight is at most Delta J/t. For x,y>=1,

    d(x,y)=1/x+1/y-1/(x+y) <= 3/2.

Indeed its derivative in x is -1/x^2+1/(x+y)^2<0, and similarly in y, so its maximum on x,y>=1 is at x=y=1. Thus all accepted offers have weight at most b_n/t, where b_n=3/n+2/n^2.

Let N_n(s) count all offers of all vertex pairs in the deterministic region 0<=r<=s, 0<=w<=b_n/(1-r). It is Poisson with mean

    lambda_n(s)=binomial(n,2)*b_n*log(1/(1-s)).

Every accepted offer up to s is counted by N_n(s). Each merger eliminates at most two singleton components, so if M_n(s) is the number of current singleton components,

    M_n(s) >= n-2N_n(s),   and   M_n(s)>=0.

It follows that E M_n(s)>=max(0,n-2lambda_n(s)). Since Var(M_n(s))>=0 and M_n(s)<=n,

    E[M_n(s)(M_n(s)-1)]
      = (E M_n(s))^2 + Var(M_n(s)) - E M_n(s)
      >= max(0,n-2lambda_n(s))^2 - n.

Define the nonnegative remainder at a partition x by

    R_n(x) = (1/2)sum_{i<j} x_i x_j (Delta J)^2 - J(x)
           = (2/n^2)sum_{i<j} x_i x_j [1/(x_i+x_j)-1/n]^2.

Counting only singleton pairs gives

    E R_n(X(s)) >= (1/n^2)(1/2-1/n)^2
                       E[M_n(s)(M_n(s)-1)].

The right side can be negative for some n,s, which does not matter; R_n itself is nonnegative. For each fixed s, 2lambda_n(s)/n -> 3 log(1/(1-s)), and consequently

    liminf_n E R_n(X(s))
      >= (1/4)[max(0,1-3 log(1/(1-s)))]^2.

Now let S(s) be accumulated expenditure and consider Z(s)=S(s)+J(X(s))/(1-s). On the fixed interval [0,s_0], all thresholds are bounded, only finitely many relevant Poisson offers occur almost surely, and J/(1-s) and all accepted payments are bounded by deterministic constants depending on n,s_0. The standard finite-jump compensation calculation therefore applies with integrable terms. Between jumps J/t increases at rate J/t^2. A pair i,j has offer intensity x_i x_j dw ds, and accepting weight w changes Z by w-Delta J/t. Integration over 0<=w<=Delta J/t gives drift -x_i x_j (Delta J)^2/(2t^2). Hence

    E Z(s_0) = J(initial) - int_0^s_0 E R_n(X(s))/(1-s)^2 ds.

At s_0 switch to the optimal Poisson continuation. The future PPP is independent of the history, and scaling gives additional optimal mean F(X(s_0))/(1-s_0)<=J(X(s_0))/(1-s_0). This is a feasible spanning-tree policy and so

    P_n <= J(initial) - int_0^s_0 E R_n(X(s))/(1-s)^2 ds.

This avoids any need to pass the compensation formula to the singular terminal time t=0. Taking limsup, using J(initial)->2 and Fatou's lemma on the nonnegative integrand,

    limsup P_n <= 2 - (1/4)int_0^s_0
           [1-3 log(1/(1-s))]^2/(1-s)^2 ds.

Set u=log(1/(1-s)); then ds/(1-s)^2=e^u du and u runs from 0 to 1/3. An antiderivative of e^u(1-3u)^2 is e^u(9u^2-24u+25), as direct differentiation verifies. The improvement is

    (1/4)[18 exp(1/3)-25],

which is positive since exp(1/3)>1+1/3+1/18=25/18, with strict inequality from the remaining positive exponential terms. Subtracting this quantity from 2 proves the stated bound. No statement of convergence follows.

## 2d. Singleton hazard improves the bound to 39/20 — proved

The total-offer domination above can be sharpened without any limit-process theorem. Under the same J-threshold policy, the merger rate involving one specified singleton and an opposing component of mass y, in elapsed time s, is

    y(Delta J)/(1-s)
      = [(2/n)(y+1/(y+1))+2y/n^2]/(1-s).

Summing over all other components, their masses sum to n-1 and their reciprocal terms satisfy sum 1/(y+1) <= (n-1)/2, since there are at most n-1 such components and y>=1. Thus the disappearance hazard of each singleton is at most a_n/(1-s), where

    a_n = 3(n-1)/n + 2(n-1)/n^2 = 3-1/n-2/n^2.

If a merger joins two singletons, its contribution is counted in both singleton hazards, exactly matching the disappearance of two singleton components. Therefore for m_n(s)=E M_n(s), the finite-interval compensation formula gives

    m_n'(s) >= -a_n m_n(s)/(1-s),   m_n(0)=n,

at almost every s<1. The expectations are absolutely continuous on each compact subinterval because all rates are bounded there. Multiplying by (1-s)^(-a_n), the derivative of m_n(s)(1-s)^(-a_n) is nonnegative almost everywhere. Integrating yields

    m_n(s) >= n(1-s)^(a_n).

Using again E[M(M-1)]>=(EM)^2-n, the verification remainder satisfies

    E R_n(X(s)) >= (1/2-1/n)^2 [(1-s)^(2a_n)-1/n].

For each fixed s<1, it follows that liminf_n E R_n(X(s)) >= (1/4)(1-s)^6.

For any fixed remaining-time cutoff t_0 in (0,1), run this algorithm until s=1-t_0 and switch to the optimal continuation as above. Fatou's lemma gives

    limsup P_n <= 2 - (1/4)int_0^(1-t_0)(1-s)^4 ds
               = 2 - (1-t_0^5)/20.

This inequality holds for every fixed t_0>0. Let t_0 decrease to zero in the resulting deterministic bound (not in the finite-time stochastic compensation formula). We conclude

    limsup_{n->infinity} P_n <= 39/20 = 1.95.

For an additional check, integration of the finite-n remainder lower bound gives the explicit finite-n inequality, valid for n>=2 and every t_0 in (0,1),

    P_n <= 2+2/n-4/n^2
      - (1/2-1/n)^2 { [1-t_0^(2a_n-1)]/(2a_n-1)
                        - (1/n)(1/t_0-1) }.

Here 2a_n-1>=3>0. The braces may be negative for an unfortunate cutoff, making the bound weaker but still valid. Choosing t_0=n^(-1/(2a_n)) maximizes the braces, since their derivative is -t_0^(2a_n-2)+1/(n t_0^2), positive below that value and negative above it. This finite bound also directly tends to 39/20: t_0->0, t_0^(2a_n-1)->0 and 1/(n t_0)->0. All these estimates concern the Poisson model.

## 2e. A component-count comparison improves the asymptotic bound — proved

We obtain

    limsup P_n <= (63-3 exp(-4/3))/32 = 1.9440377683... .

Use logarithmic time u=-log(1-s). On each fixed interval 0<=u<=U, the J-threshold partition process is a finite-state continuous-time Markov chain, with merger rate

    x_i x_j Delta J = (2/n)x_i x_j d_ij + (2/n^2)x_i x_j.

Let K_n(u) and M_n(u) count its total components and singleton components. The total merger rate is lambda_K=2E/n+2W/n^2. For each pair, xy/(x+y)<=(x+y)/4, because (x-y)^2>=0. Summing gives R<=(k-1)n/4, so E=(k-1)n-R>=(3/4)(k-1)n. Therefore lambda_K>=(3/2)(k-1).

Let B_n(u) be the pure-death chain starting at n with death rate (3/2)(b-1). There is a coupling with K_n<=B_n at all times. When K<B, let B and the partition make their usual deaths independently; each decreases its count by one, preserving order. When K=B=k, make a shared death at rate (3/2)(k-1), choosing the partition's merging pair proportional to its merger rates. Make partition-only deaths at the nonnegative residual rate lambda_K-(3/2)(k-1), choosing the pair with the same probabilities. Each partition pair then has its original marginal merger rate, and B has its prescribed death rate. Order is preserved. This specifies a nonexplosive finite-state Markov coupling for each n. The no-death state k=1 is interpreted separately and is absorbing.

B_n-1 is the number of survivors of n-1 independent rate-3/2 exponential lifetimes. With p(u)=exp(-3u/2),

    E B_n=1+(n-1)p<=np+1,
    Var(B_n)=(n-1)p(1-p)<=n/4.

The disappearance hazard of a specified singleton in logarithmic time is at most

    (2/n)(n-1+(k-1)/2)+2(n-1)/n^2
      =2+(k-1)/n-2/n^2 <=2+k/n.

For m_n(u)=E M_n(u), v_n=m_n/n, compensation (with singleton-singleton deaths counted twice) gives, almost everywhere on any fixed finite interval,

    m_n' >= -2m_n - (1/n)E[M_n K_n]
          >= -2m_n - (1/n)E[M_n B_n].

Because 0<=M_n<=n, its variance is at most n E M_n-(E M_n)^2<=n^2/4. Cauchy–Schwarz for centered variables therefore implies

    E[M_n B_n] <= m_n E B_n + sqrt(Var(M_n)Var(B_n))
                <= m_n(np+1) + n sqrt(n)/4.

Dividing the differential inequality by n yields

    v_n' >= -(2+p+1/n)v_n -1/(4sqrt(n)),  v_n(0)=1.

Put H_n(u)=(2+1/n)u+(2/3)(1-exp(-3u/2)), with derivative 2+p+1/n. Multiplying by exp(H_n) and integrating gives

    v_n(u) >= exp(-H_n(u))
       [1-(1/(4sqrt(n)))int_0^u exp(H_n(r))dr].

For fixed u, the integral is uniformly bounded in n, so

    liminf_n v_n(u) >= v(u)
      :=exp[-2u-(2/3)(1-exp(-3u/2))]>0.

Using E[M(M-1)]>=m_n^2-n in the singleton-pair remainder, this proves

    liminf_n E R_n(X(u)) >= (1/4)v(u)^2.

The positive lower limit justifies squaring the lower bound. Run the trial policy only until time U and then switch to optimal continuation. Since ds/(1-s)^2=exp(u)du, the finite-time compensation and Fatou argument proves

    limsup P_n <=2-(1/4)int_0^U exp(u)v(u)^2du.

This holds for every finite U. Let U increase to infinity in the deterministic bound. The integral is convergent since its integrand is at most exp(-3u). For z=exp(-3u/2), a=4/3, its value is

    (1/4)int_0^infinity exp(u)v(u)^2du
      =(1/6)exp(-a)int_0^1 z exp(az)dz
      =(1/6)[a-1+exp(-a)]/a^2
      =1/32+(3/32)exp(-4/3).

The middle equality follows from the antiderivative exp(az)(az-1)/a^2, whose derivative is z exp(az). Subtracting this improvement from 2 proves the bound. The rounded decimal is presentation only; the exponential expression is the exact proved upper bound. No existence of an optimal-cost limit and no transfer to the combinatorial model is implied.

## 3. Small cases and a finite model mismatch — proved

With two Poisson components of masses x,y, the child value is zero, so 2f=xy f^2 with f>0, yielding F(x,y)=2/(xy). With three singletons all child values are F(2,1)=1, and 2f=3(f-1)^2. The unique admissible root is P_3=(4+sqrt(7))/3.

In the combinatorial n=2 model the only edge must be accepted, so C_2=1/2, whereas P_2=2.

For combinatorial n=3, suppose the first edge is accepted. One further edge must be selected from the two remaining edges; both connect the current two components. If the first of two independent Uniform[0,1] offers is rejected, the second must be accepted with mean cost 1/2. The optimal threshold is therefore 1/2, with continuation value

    int_0^(1/2) w dw + (1/2)*(1/2) = 3/8.

If the first edge of the triangle is rejected, both remaining edges must be purchased, with mean cost 1. Thus the first edge of weight w is accepted precisely when w+3/8<=1, i.e. w<=5/8. Its optimal expected cost is

    C_3 = int_0^(5/8)(w+3/8)dw + int_(5/8)^1 1 dw
        = 103/128.

This is an exhaustive backward decision analysis, independent of which first edge is revealed. Finite costs in the two models cannot be identified. Their finite mismatch alone does not disprove asymptotic equivalence.

## 4. Exact integer certification of finite values

finite_dp.py enumerates integer partitions for each n, in increasing number of parts. Repeated pair types are aggregated with their exact multiplicity. For x!=y that multiplicity is m_x*m_y; for x=y it is binomial(m_x,2). The weight of an aggregated transition is that multiplicity times xy.

Every value is bracketed by integers L,U divided by s=2^70. Given certified child intervals [l_r,u_r]/s, form A=sum w_r, B_l=sum w_r l_r, D_l=sum w_r l_r^2 and similarly B_u,D_u. The rescaled quadratic is

    h(m,c) = sum w_r(m-c_r)^2 - 2ms.

The integer floor of its larger root is computed exactly as

    floorroot(c) = [(B+s)+isqrt((B+s)^2-A D)] // A.

This formula is exact: replacing sqrt of the integer discriminant by its integer floor cannot change the integer floor of division by the positive integer A. Set L=floorroot(l), U=floorroot(u)+1. Independently verify, with integer arithmetic,

    L > max_r u_r,
    h(L,l)<=0, h(U,u)>=0, L<=U.

To justify the enclosure, for f>max child costs the ratio

    R(f,c)=sum w_r(f-c_r)^2/(2f)

is strictly increasing: each summand is (w_r/2)(f-2c_r+c_r^2/f), with derivative (w_r/2)(1-c_r^2/f^2)>0. At a root R=1. Since L/s exceeds every actual child, increasing a child decreases its square at L/s. Thus h(L,l)<=0 implies R(L/s,c_actual)<=1, so L/s<=F. If the actual root were greater than U/s, the inequality h(U,u)>=0 would imply R(U/s,c_actual)>=1 and contradict strict increase; thus F<=U/s. This establishes the induction and validates every saved interval. The strict comparison to all child upper endpoints is essential and is checked for every state.

The run certified all 43,818 integer partitions for n=2,...,32. Files certified_costs.json and finite_checks.json preserve the exact rational endpoints and all summary checks. Representative rounded midpoints:

| n | Poisson cost midpoint |
|---|---:|
| 2 | 2.000000000000000 |
| 3 | 2.215250437021530 |
| 4 | 2.233699936206815 |
| 10 | 2.107788674576358 |
| 20 | 2.016491331751182 |
| 24 | 1.998596992729661 |
| 32 | 1.975071282920428 |

Exact endpoint comparisons certify P_2<P_3<P_4 and P_4>P_5>...>P_32. These are finite statements; extrapolating them to eventual monotonicity or a limiting constant is unsupported.

## 5. The source's continuity claim at the zero empirical state — proved special case

For a partition of n, let y_i=(i/n)*number of size-i components, so sum_i y_i=1. Then the reciprocal bound can be written

    0 <= F_n(y) <= (8/3)[sum_i y_i/i^2 - 1/n^2]
                 <= (8/3)sum_i y_i/i^2.

Let y^(n) be any sequence of realizable empirical states with y_i^(n)->0 for every fixed i. For any positive integer M,

    sum_i y_i^(n)/i^2
       <= sum_{i=1}^M y_i^(n)/i^2 + 1/(M+1)^2,

because total mass in the tail is at most one. The finite sum tends to zero. Consequently limsup_n F_n(y^(n)) <= (8/3)/(M+1)^2. Letting M tend to infinity proves F_n(y^(n))->0.

In particular, if y^(n), z^(n) both converge coordinatewise to zero, then

    |F_n(y^(n))-F_n(z^(n))| <= F_n(y^(n))+F_n(z^(n)) ->0.

This proves exactly the zero-limit special case of the draft's continuity claim on p. 7. It allows a vanishing fraction of vertices in each fixed small component size; a minimum-component-size hypothesis is unnecessary. As a simpler quantitative consequence, if every component has size at least m, then sum_i y_i/i^2<=1/m^2, so F<=8/(3m^2).

This special case justifies the natural zero-state value, but the initial state for P_n has y_1=1. Continuity at zero therefore does not prove the target limit. No assertion here establishes continuity at a nonzero coordinatewise limit.

## Remaining gap

No proof here establishes convergence of C_n or P_n, evaluates a limit, or establishes C_n-P_n->0. The finite bound yields boundedness of P_n, hence subsequential limits by ordinary real compactness, but supplies no equality between those limits. The unique finite root does not imply uniqueness of a PDE limit: uniform regularity, compactness in the relevant empirical-state topology, and consistency/uniqueness of the infinite-dimensional problem are missing. Increasing finite partition computations cannot bridge those analytic gaps. In particular, the estimate near 1.9 remains uncertified.

The source's section 4 proposes the one-sided transfer C_n<=P_n+o(1) as Proposition 12, but explicitly marks the argument as missing details and the completion proof as sketchy. We have checked its text, not completed its proof. Thus we do not claim that the bound (63-3 exp(-4/3))/32 applies to C_n.

## Hostile-referee checks so far

- Normalization: source uses intensity one per unordered pair, not intensity 1/n. Our formula reproduces P_2=2 and the source's exact P_3.
- Strict side condition: uniqueness is proved only for roots greater than every child; the zero root of the two-component equation is excluded.
- Verification direction: the source uses H <= quadratic(H) for an upper bound. The reciprocal potential satisfies precisely that direction.
- All component counts: k=1 is separated, k=2 requires its own calculation, and k>=3 uses q>=k^2. No assertion relies on q>=k^2 alone for k=2.
- State space: computations aggregate isomorphic states only in the Poisson model, whose partition Markov property the source proves; combinatorial states generally also require unrevealed-edge information.
- Computation: exact integer sign checks validate the intervals; displayed decimals are merely rounded presentation.
- Novelty: the upper bound implements a trial potential suggested in the source. The literature search is limited and novelty is not certified.
- Literature coverage: OpenAlex was rate-limited, and a Semantic Scholar source lookup returned 404. These failures are logged, not construed as negative search evidence.
- Stronger supersolution: independent exact rational arithmetic confirmed its verification remainder for all 2,712 integer partitions with total mass 2 through 20, including equality for k=1,2 and strict positive slack for k>=3. The singleton hazard bound was checked exactly on all 2,086 of those states that have a singleton. Results are in referee_checks.json.
- Asymptotic bound: all stochastic compensation is applied on a fixed interval away from t=0; an optimal continuation then guarantees completion. The bound 39/20 follows from Fatou on nonnegative remainders, not from convergence of the optimal process.
- Hazard multiplicity: singleton-singleton mergers appear twice in total singleton hazards because they remove two singletons. All component-to-component rates include the factor xy from the source's per-pair intensity.
- Finite-cutoff check: the explicit upper bound in section 2d exceeds the certified finite values at n=2,3,4,8,16,32. At n=10^6 it is approximately 1.95000493. These comparisons test normalization and sign, but are not the proof.
- The tempting direct-model identification fails at n=2 and n=3. A Poisson intensity rescaling would change all computed constants, so it cannot repair this issue silently.
- An attempted path toward full convergence would require a uniform comparison of values after altering o(n) component masses. The elementary uniqueness argument is local in the finite recursion and gives no such uniform comparison. The source's given-kernel coagulation limit theorems do not apply directly because the optimal kernels depend on these unknown state values. We have only proved the zero-limit special case, not a reduction that closes this obstacle.
- Component comparison: the pure-death coupling is specified separately at K<B and K=B, so the slow comparison chain cannot cross below K. At equality its shared death rate is no greater than the actual total merger rate. Both marginal generators are preserved.
- Variance step: M and B are not independent. The proof explicitly includes their covariance through Cauchy–Schwarz; independence is used only for the exponential lifetimes that give the B marginal. The normalized covariance error is O(n^(-1/2)) on each fixed logarithmic-time interval.
- Order of limits: first n tends to infinity at fixed U, then U tends to infinity in a deterministic bound. No stochastic compensation is extended to the singular deadline.
- New exact rational checks: the component-count death-rate inequality was checked on all 2,712 partitions, and the sharper 2+k/n singleton-hazard inequality on all 2,086 singleton-containing states. These verify arithmetic cases of the proof; the full coupling and covariance argument is written in section 2e.
- Final formalization status: both AlgebraCheck.lean and SupersolutionCheck.lean passed Lean 4 with exit code zero. The latter's first run failed only because a tactic did not normalize inverse powers; denominator clearing under the positive-mass hypotheses corrected the formal proof. The key algebra is checked without proof holes or native decision evaluation. The stochastic compensation, coupling, expectation and limiting arguments are fully written mathematical proofs here; they are not claimed to be formalized in Lean.

## Final disposition

First-attempt disposition: STATE: DONE; VERDICT: PARTIAL. No full solution was found. The strongest proved Poisson asymptotic upper bound in this record is (63-3 exp(-4/3))/32, approximately 1.9440377683; it is a limsup bound, not an identified limiting optimal cost. Literature novelty of these partial results is not certified.

## Second attempt: quantitative one-sided model transfer (2026-10-11)

The complete second-attempt mathematics is saved in [SECOND_ATTEMPT.md](SECOND_ATTEMPT.md). It records two new approaches, the read-only brain queries about the gap, and full proofs of the pursued approach. An exact causal low-offer simulator, an all-cuts hypergeometric estimate and a stopped repair potential yield

    C_n <= P_n + O(n^(-1/6)).

Consequently the previous bound also applies to the source's combinatorial model:

    limsup C_n <= (63-3 exp(-4/3))/32 = 1.9440377683016505...

This supplies details and an explicit rate for the direction of the source's sketched Proposition 12. A subsequent reverse construction is proved in [REVERSE_TRANSFER.md](REVERSE_TRANSFER.md): routing physical candidates by equal-size bundle reassignments and controlling stopped phantom counts gives P_n<=C_n+O(n^(-1/100)). Together the two proofs yield |P_n-C_n|=O(n^(-1/100)). Thus the finite models have identical limiting subsequential costs and either converges exactly when the other does. Their finite-n costs still differ.

The remaining gap is convergence and determination of the common limiting cost. General nonzero-state continuity and convergence of the unknown optimal coagulation kernels remain unproved. Equivalence does not prove existence of a limit or certify the proposed value near 1.9. No bibliographic novelty is claimed.

Independent checks in second_checks.json cover 3,310 exact hypergeometric moment cases, all 1,098 graphs on 2 through 5 vertices, 21,808 good-graph partition cases and 2,016 exact repair-drift cases. Seeded 300,000 single-edge simulator trials check increments and marks; numerical checks are supporting evidence, not the point-process proof. reverse_checks.json adds 119,328 exact bundle/endpoint reassignments on every partition through n=6, including same-small-class cases. RepairCheck.lean checks selected algebraic identities separately; its execution result is recorded in VERIFICATION.md.
