# Hyperexponential counterexamples for every number of servers

2 October 2026. Standalone extension of the audited two-server result. The arguments below concern the full stochastic waiting-time assertion in Whitt's 1983 Conjecture 1.1; they do not settle the weaker mean waiting-time conjecture. Historical priority has not been established.

## Theorem

Fix an integer c>=2. Let a_1,...,a_k>0 and p_1,...,p_k>0, with sum p_i=1. Define the service law S=a_I E, where P(I=i)=p_i and E is an independent exponential random variable of mean one. Set

    m=sum_i p_i a_i,  B=max_i a_i.

Suppose that the a_i are not all equal. Define a second service law U that is zero with probability 1-m/B and is BE with probability m/B. Then S<=cx U. In stationary FCFS M/G/c queues with the same Poisson arrival rate lambda,

    P(W_S>0)>P(W_U>0)

for every sufficiently small positive lambda. Thus the implication from convex ordering of services to usual stochastic ordering of stationary waiting times fails for every c>=2.

The same assertion holds with a strictly positive, two-component hyperexponential replacement U_epsilon, whose component means are epsilon and B, for a sufficiently small explicit epsilon>0 given below.

## Analytic light-traffic coefficient

Let A_1,...,A_(c+1) be iid size-biased class means:

    P(A_j=a_i)=p_i a_i/m.

Write n=c+1, X_j=1/A_j, S_X=sum_j X_j, y_j=X_j/S_X, and r_j=y_j/(1-y_j). Define

    T_c=(1/n)sum_(i != j) r_i r_j,
    K_c=(m^(c+1)/c!) E[T_c].

The stationary probability of delay has the expansion

    P(W_S>0)=m^c lambda^c/c!
      +(K_c-m^(c+1)/c!)lambda^(c+1)+O(lambda^(c+2)).       (1)

Here c is fixed; the remainder is the Taylor remainder of an analytic function in a neighborhood of zero, rather than a simulation or a finite-capacity approximation.

### Why the infinite queue has these finite Taylor coefficients

For a finite hyperexponential law, use a Markov chain whose phase records the class counts of the c jobs in service. Service classes of waiting jobs may be sampled when they start service, since their own pre-service waits do not depend on their independent service marks. Above the all-busy level, this is a finite-phase QBD. Let M_0 be the positive diagonal matrix of total completion rates and D the matrix of completion rates followed by replacement with an independent service class. Its row-oriented rate matrix satisfies

    R=(lambda I+R^2 D)(M_0+lambda I)^(-1).              (2)

At (lambda,R)=(0,0), the derivative of the right side with respect to R is zero. The analytic implicit-function theorem gives an analytic branch R(lambda)=O(lambda). For sufficiently small positive lambda, the right side is a contraction on a nonnegative ball of radius O(lambda); iteration from zero converges to that branch. It is therefore the nonnegative minimal stationary rate matrix. Its row sums are less than one for sufficiently small lambda.

Explicitly, set a_min=min_i a_i and use the maximum row-sum norm. Since ||D||<=c/a_min and ||(M_0+lambda I)^(-1)||<=B/c for real lambda>=0, the nonnegative ball ||R||<=2lambda B/c is invariant whenever lambda<=c a_min/(4B^2). Its Lipschitz constant is at most4lambda B^2/(c a_min), which is strictly below one after making that inequality strict. Monotone iteration from zero is thus sufficient to identify the branch, without assuming positivity from the implicit-function theorem alone.

The finite boundary equations at lambda=0 describe a pure-death chain with empty as its unique closed state. Their augmented stationary linear system is invertible after imposing normalization. Consequently the boundary masses are analytic. Recursion by population size gives probability O(lambda^j) at population j<=c. In particular the stationary all-busy boundary row is O(lambda^c). Multiplying it by R^q shows that population c+q has probability O(lambda^(c+q)). The entire omitted tail above capacity c+1 is an analytic O(lambda^(c+2)) quantity, obtained by summing the matrix geometric series involving R^2(I-R)^(-1).

Restrict the infinite stationary row to populations 0,...,c+1. In the capacity-(c+1) chain, the balance residual consists only of rejected-arrival flux out of population c+1 and returning-completion flux from population c+2. Both are O(lambda^(c+2)). The normalization residual has the same order. The augmented finite stationary system has a bounded analytic inverse near zero. Hence the restricted infinite stationary row and the capacity-(c+1) stationary row agree through degree c+1. This justifies calculating (1) in the latter finite chain.

### Compare capacity c+1 with the loss chain of capacity c

Embed the capacity-c loss chain into the same finite state set by assigning its extra population-(c+1) states zero stationary mass. Write the two generators as

    Q_wait=Q_0+lambda A_wait,
    Q_loss=Q_0+lambda A_loss.

Q_0 is their common pure-death generator. The arrival matrices differ only in rows at population c: the waiting system adds a waiting customer, and the loss system rejects it. At lambda=0 both chains have the same unique stationary row concentrated at empty.

The loss chain has the exact stationary weights

    lambda^j product_i (p_i a_i)^(k_i)/k_i!,
    j=sum_i k_i<=c,

normalized by Z_c(lambda m)=sum_(j=0)^c (lambda m)^j/j!. Its all-busy probability is the Erlang-B expression. For c>=2,

    P_loss(busy)=m^c lambda^c/c! -m^(c+1)lambda^(c+1)/c!
                  +O(lambda^(c+2)).                 (3)

The two stationary Taylor series agree through degree c. To see this formally, their order-j stationary coefficients have support only at populations <=j. Inductively the coefficient equations have identical sources through degree c, because A_wait-A_loss vanishes below population c. The augmented pure-death stationary system is invertible, so the coefficients agree.

Let delta be the difference of their degree-(c+1) stationary coefficient rows. Let tau be the leading all-busy loss coefficient, with phase-count weights

    tau(k)=product_i (p_i a_i)^(k_i)/k_i!, sum_i k_i=c.

Then

    delta Q_0=-tau(A_wait-A_loss),  delta 1=0.        (4)

For the busy reward f(state)=1{population>=c}, define h(state) to be the expected total future busy time under Q_0, with h(empty)=0. Thus Q_0 h=-f. For a full phase containing means a_1,...,a_c and total completion rate r=sum_j 1/a_j,

    h(full)=1/r,
    h(full plus one waiting)=1/r+E[h(new full phase)].

The first completion removes job i with probability (1/a_i)/r; the waiting job then starts with an independent original service class. Multiplying (4) by h shows

    delta f=tau[h(full plus one waiting)-h(full)] = K_c.   (5)

Together (3) and (5) give (1).

### Derive the symmetric formula for K_c

The normalized tau phase law consists of c independent size-biased class means, since sum tau=m^c/c!. Conditional on their reciprocals X_1,...,X_c, job i is removed first with probability X_i/(sum_(j=1)^c X_j). Let C be the newly started original class mean. Its ensuing full-phase busy duration is

    1/(1/C+sum_(j != i) X_j).

Changing the original C law to its size-biased law multiplies this expression by m/C. Writing X_(c+1)=1/C consequently gives

    K_c=m^(c+1)/c! E[sum_(i=1)^c
       X_i X_(c+1)/((S_X-X_(c+1))(S_X-X_i))].

All c+1 reciprocal means are now iid. Averaging which index is designated the new job yields precisely

    K_c=m^(c+1)/(c! (c+1)) E[sum_(i != j) r_i r_j].

## A deterministic inequality giving the strict sign

For n>=3 and positive y_1,...,y_n summing to one, put r_i=y_i/(1-y_i). Then

    n/[2(n-1)] <= sum_(i<j) r_i r_j <= 1.            (6)

The first inequality is strict unless all the y_i are equal.

Here is a direct proof. Fix two coordinates x,y with t=x+y<1, z=xy, and let R be the sum of the other odds. The part of the pair sum depending on x,y is

    [z+R(t-2z)]/(1-t+z).

Its derivative with respect to z is

    [(1-t)-R(2-t)]/(1-t+z)^2 < 0,

because R>=sum_(other i)y_i=1-t and 2-t>1. Therefore replacing x,y by their average, which increases z, strictly decreases the pair sum unless x=y. Repeatedly average a maximal and a minimal coordinate. These averages stay within the original positive coordinate range and converge to the uniform vector: their squared deviations from 1/n decrease by half the squared maximal-minimal difference at each step. Continuity gives the lower bound in (6), with value n/[2(n-1)] at the uniform vector, and strictness follows after the first unequal averaging.

For the upper bound, merge any two coordinates by replacing (x,y) with (x+y,0) while at least one other coordinate remains positive. This reduces z to zero and increases the pair sum. Repeat until two positive coordinates remain; their two odds have product one. This proves the upper bound in (6).

Consequently

    1/c <= T_c <= 2/(c+1),
    Delta_c := K_c-m^(c+1)/(c! c) > 0.              (7)

The strict expectation follows because a nondegenerate iid class law has positive probability of producing unequal reciprocal means among c+1 draws.

## Convex ordering and the competing delay probability

Conditional on the original class i and E, replace a_i E by BE with probability a_i/B and by zero otherwise. Its conditional mean is a_i E. The unconditional positive probability is m/B, so the resulting law is U, and conditional Jensen gives S<=cx U.

Zero-service jobs add no workload; they can still wait for service to begin. Deleting them from the workload process leaves a thinned M/M/c queue with arrival rate lambda m/B and individual service rate 1/B. All original arrivals see its stationary all-busy probability by PASTA. Its offered load is lambda m. Erlang C therefore gives

    P(W_U>0)=m^c lambda^c/c!
       -(c-1)m^(c+1)lambda^(c+1)/(c! c)
       +O(lambda^(c+2)).                            (8)

Subtracting (8) from (1) gives

    P(W_S>0)-P(W_U>0)=Delta_c lambda^(c+1)
                           +O(lambda^(c+2)) > 0

for all sufficiently small positive lambda. Stability is automatic in that range; one may also dominate all services by BE and require lambda B<c.

## Strictly positive service counterexamples with an explicit epsilon

For 0<epsilon<min_i a_i, replace a_i E by epsilon E or BE with respective conditional probabilities

    (B-a_i)/(B-epsilon),  (a_i-epsilon)/(B-epsilon).

The conditional mean is again a_i E. The unconditional new law U_epsilon has short-class probability (B-m)/(B-epsilon), and S<=cx U_epsilon. Its size-biased short-class probability is

    r_epsilon=epsilon(B-m)/(m(B-epsilon)).

In the symmetric coefficient formula, T_c=1/c when all c+1 sampled classes are long, and T_c<=2/(c+1) always. The union bound therefore gives

    0<=Delta_c(U_epsilon)
      <=m^c(c-1)epsilon(B-m)/(c! c(B-epsilon)).      (9)

Choose

    epsilon=min{ min_i a_i/2,
                 Delta_c c! c B/[8m^c(c-1)(B-m)] }.

Nondegeneracy ensures B>m and Delta_c>0, so this is positive. It also satisfies epsilon<=B/2. Equation (9) then gives Delta_c(U_epsilon)<=Delta_c/4. The two laws have the same leading delay coefficient, and their next-coefficient difference is at least 3Delta_c/4>0. They consequently satisfy the same reversed delay probability inequality for every sufficiently small arrival rate. If the original means and probabilities are rational, every quantity in this construction, including epsilon, is rational.

## Exact checks and limitations

`whitt_all_servers_light_traffic.py` independently constructs finite capacity-(c+1) generators, recursively solves all stationary Taylor equations in exact Fraction arithmetic, and compares the resulting coefficient with the size-biased symmetric formula. It checks nondegenerate two-class examples for c=2,...,10, a three-class example for c=2,...,6, and a degenerate equal-means control. The general proof, rather than those finite checks, establishes the assertion for every c>=2.

This all-server theorem is an extension of the standalone nine-state exact finite-rate counterexample in `whitt_nine_state_proof.md`. It proves an existence interval of small rates, without giving an explicit rate bound from the analytic remainder. The nine-state certificate separately supplies a completely explicit rate lambda=1/10 and literal integer stationary certificate. Historical priority and external expert review remain unestablished.
