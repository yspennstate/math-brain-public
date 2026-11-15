# A quadratic certificate for approximate continuation rules

Fix a finite horizon n. Smaller observations have better ranks. This note proves a conversion from uniform continuation-value error to expected-rank regret. It does not determine the limiting value V or claim priority for the conversion.

## 1. State and value functions

Let h=(h_1,...,h_k) be rejected observations, and let r=n-k independent Uniform(0,1) observations remain to be seen. Let W_r(h) be the infimum expected final rank when selection must occur among those r observations. Ranks count both the rejected history and all r remaining observations. Past values can coincide; only comparisons between a future observation and a past value matter.

If the next value is x, the expected rank on immediate selection is

    S_r(h,x) = 1 + sum_i 1{h_i < x} + (r-1)x.

For r>=2 the optimal continuation cost is

    C_r(h,x) = W_{r-1}(h,x).

Here (h,x) means append x to the rejected history. At the last observation selection is compulsory, and

    W_1(h) = 1 + sum_i (1-h_i).

Backward induction gives

    W_r(h) = integral_0^1 min{S_r(h,x), C_r(h,x)} dx.       (1)

All functions can be taken Borel measurable. Indeed S is Borel, W_1 is continuous, and integration and taking a minimum preserve measurability in the finite backward recursion. The action attaining the minimum gives an optimal measurable rule, with ties settled arbitrarily.

## 2. Monotonicity and a modulus in the rejected history

For two histories h and g of the same length, with g_i>=h_i for every i,

    0 <= W_r(h)-W_r(g) <= r sum_i (g_i-h_i).              (2)

To prove this, use the same stopping functional of the future observations in both problems. The class of such functionals is the same for either fixed history. On each future sample path, raising a rejected observation from h_i to g_i can only decrease the selected rank. Its decrease is 1 exactly when the selected future value lies between those endpoints (endpoints have probability zero). The probability of that event is at most the probability that at least one of the r future observations lies there, which is

    1-(1-(g_i-h_i))^r <= r(g_i-h_i).

Sum over i. The expected costs of any fixed stopping functional in the two problems therefore differ by a number in [0, r sum_i(g_i-h_i)]. Taking infima over the common class of functionals proves both inequalities in (2). For histories with coordinates moving in both directions, the same argument using absolute differences proves

    |W_r(h)-W_r(g)| <= r sum_i |h_i-g_i|.                (3)

In particular, x -> C_r(h,x) is nonincreasing. Define the advantage of continuing over stopping by

    D_r(h,x) = S_r(h,x)-C_r(h,x).

For x<y, the history-count term is nondecreasing and C_r is nonincreasing, so

    D_r(h,y)-D_r(h,x) >= (r-1)(y-x).                    (4)

For r=2 the terminal formula is stronger:

    C_2(h,x) = 2 + sum_i(1-h_i) - x,

so

    D_2(h,y)-D_2(h,x) >= 2(y-x).                        (5)

Write a_2=2 and a_r=r-1 for r>=3. Thus (4)-(5) say D(y)-D(x)>=a_r(y-x). The optimal stopping set is an initial interval, up to boundary conventions. Upward jumps of D at historical observations are allowed throughout.

## 3. A one-step integral bound

Let D:[0,1]->R be measurable and satisfy D(y)-D(x)>=a(y-x) for x<y, where a>0. For any real interval I of length L, its inverse image under D has length at most L/a: any two points x<y in that inverse image satisfy a(y-x)<=L. Let mu be the image of Lebesgue measure under D. The preceding inequality implies mu(I)<=|I|/a. Covering any Borel set by open intervals, then taking the infimum of the total covering lengths, gives

    mu(B) <= Lebesgue(B)/a

for every Borel B. Integrating nonnegative simple functions and then increasing limits gives, in particular,

    integral_{0<D(x)<=e} D(x) dx <= e^2/(2a),
    integral_{-e<=D(x)<0} |D(x)| dx <= e^2/(2a).         (6)

This proof neither differentiates D nor assumes that D crosses zero continuously. It remains valid if a jump skips zero or either integration set is empty.

## 4. Policy certificate

For each r>=2 let Chat_r(h,x) approximate the TRUE optimal continuation C_r(h,x), uniformly over all histories of length n-r and x, with

    |Chat_r(h,x)-C_r(h,x)| <= e_r.                      (7)

The implemented rule pi selects x when

    S_r(h,x) <= Chat_r(h,x),                           (8)

and otherwise continues using the same approximate rule at later times. At r=1 it selects compulsorily. In particular the history-count term in S_r is exact.

Then

    0 <= E[rank selected by pi] - V_n
       <= sum_{r=2}^n e_r^2/a_r.                       (9)

If at each r the error has one sign uniformly over h,x, the sharper bound is

    E[rank selected by pi] - V_n
       <= (1/2) sum_{r=2}^n e_r^2/a_r.                 (10)

The sign can differ between stages. The bound (10) also holds for two-sided errors if x -> Chat_r(h,x) is nonincreasing for every h.

Proof. At a state (h,x), charge the chosen action its cost assuming optimal play after a decision to continue. Its excess over min{S,C} is a nonnegative local residual d_r(h,x). If (8) chooses the optimal action, d=0. If it chooses the wrong action, d=|D|.

If D>0, stopping is wrong; (8) can stop only if Chat-C>=D, and hence 0<D<=e_r. If D<0, continuing is wrong; it can continue only if Chat-C<D, and hence -e_r<=D<0. The two inequalities in (6) therefore give

    integral_0^1 d_r(h,x) dx <= e_r^2/a_r.              (11)

If Chat<=C everywhere, only erroneous continuation is possible; if Chat>=C everywhere, only erroneous stopping is possible. Only one of the two integrals in (6) is then needed, giving half of (11).

For the monotone-Chat assertion, S-Chat is strictly increasing, so the implemented stopping set is also an initial interval. Two initial intervals are nested. For each fixed h, the optimal and implemented rules can therefore disagree in at most one direction. Again only one integral in (6) is needed. Which direction occurs can depend on h.

It remains to account for later mistakes. Let J_r(h) be the true expected rank under pi, and B_r(h)=J_r(h)-W_r(h). On stopping, the excess equals the local residual; on continuing, it equals that residual plus B_{r-1}(h,x). Substituting in the integral recursion gives the EXACT identity

    B_r(h) = integral_0^1 [d_r(h,x)
                 + 1{pi continues at (h,x)} B_{r-1}(h,x)] dx.    (12)

At r=1, B_1=0. Induction in (12), using (11) and the bound 1{continue}<=1, proves (9), and using its halved form proves (10). This also shows why no assumption about the distribution of reached histories is needed. Conditional on any reached history, the next observation is still independent Uniform(0,1).

For a common e_r=e and n>=2 the right side of (9) is

    e^2 (H_{n-1}-1/2),                                 (13)

where H_m=sum_{j=1}^m 1/j. The one-sided or monotone case has half that constant. For n=1 the regret is zero.

If the implemented policy's expected rank J is independently enclosed in [L,U], and B is the applicable right side of (9) or (10), then

    L-B <= V_n <= U.                                   (14a)

Indeed J-B<=V_n<=J. Thus the certificate can turn a rigorous policy evaluation into a two-sided enclosure of the optimum; an ordinary Monte Carlo estimate alone is not a rigorous enclosure.

## 5. An explicit rounding corollary

Let delta=1/M for a positive integer M. Round each REJECTED history coordinate upward to the next grid node, writing g_i=ceil(M h_i)/M. Retain x exactly, and use

    Chat_r(h,x) = W_{r-1}(g,x).                        (14)

Evaluate S_r from the exact history. From (2), with k=n-r,

    0 <= C_r(h,x)-Chat_r(h,x) <= (r-1)k delta.          (15)

Consequently, this rule has regret at most A_n delta^2, where for n>=2

    A_n = (1/2) sum_{r=2}^n ((r-1)^2 (n-r)^2)/a_r
        = ((n-1)^2 ((n-1)^2-1))/24 - (n-2)^2/4.        (16)

For the closed form, put m=n-1 and j=r-1. Without the improved a_2, the sum is (1/2)sum_{j=1}^m j(m-j)^2. Expanding into sums of first, second, and third powers gives sum_{j=1}^m j(m-j)^2=m^2(m^2-1)/12. Replacing a_2=1 by a_2=2 subtracts (m-1)^2/4, proving (16).

In particular A_2=0, A_3=1/4, A_4=2, A_5=31/4. Thus for n=5 and M=100 the regret bound is exactly 31/40000 = 0.000775.

Formula (14) uses exact optimal continuation functions at rounded histories. It is a reduction, not an algorithm for evaluating those functions. If numerical approximations are substituted, their independently established uniform error must be included in (7); one-sided certification or monotonicity is required to retain the factor 1/2. This policy is not a rule using only binned observations: it retains exact comparisons for S_r and the exact current x. The result is for fixed n, and A_n grows on the order of n^4; no uniform-in-n approximation or bound on V follows.

## 6. Exact checks and a limitation

For n=2 there is no rejected history,

    S_2(x)=1+x, C_2(x)=2-x, D_2(x)=2x-1, V_2=5/4.

For 0<e<1, use Chat=C+e when D>0 and Chat=C-e when D<0. The rule is wrong on both sides of 1/2 over intervals of length e/2. Each triangle has base e/2 and height e, so total regret is e^2/2. Directly integrating the chosen stopping and continuation costs gives 5/4+e^2/2. Thus the coefficient 1/a_2=1/2 in (9) is attained without a monotonicity constraint on Chat.

Using Chat=C-e instead changes the stopping threshold to (1-e)/2. There is one such triangle; the regret is e^2/4, attaining the one-sided constant in (10). At e=1/4 these regrets are 1/32 and 1/64, respectively.

The requirement to retain the exact history-count term matters. Consider r=2 and h=(1/2). The true D equals 2x-3/2 for x<1/2 and 2x-1/2 for x>1/2. The optimal threshold is pinned at 1/2 by a jump; the one-sided limits of D there are -1/2 and +1/2. Moving a decision threshold from 1/2 to 1/2+delta, for 0<delta<1/2, has regret

    integral_{1/2}^{1/2+delta} (2x-1/2) dx
      = delta/2 + delta^2.                             (17)

That is linear to first order. A small threshold displacement alone therefore does not imply a quadratic certificate. Equations (7)-(8), which use the exact S_r, prevent this error.
