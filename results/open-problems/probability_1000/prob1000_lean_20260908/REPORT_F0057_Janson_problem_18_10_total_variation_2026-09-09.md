# Total variation approximation of the j-th largest box: Janson's Problem 18.10

Settled 2026-09-09. Ledger id F0057 (intake F, source `janson_simply_generated_2012`).

## The problem as the source states it

Janson, *Simply generated trees, conditioned Galton-Watson trees, random allocations and
condensation*, Probability Surveys 9 (2012), Section 18.2, after Theorem 18.7 (Problem 18.10 in
the arXiv numbering; the published version numbers the section 19):

> The total variation approximation in (vi) is stronger than the Kolmogorov distance
> approximation in (v), and our proof is considerably longer, but for many purposes (v) is
> enough. We conjecture that total variation approximation holds for every Y(j), and not just
> for Y(1); presumably this can be shown by a modification of the proof for Y(1) below, but we
> have not checked the details and leave this as an open problem. Furthermore, we believe that
> the result extends to the joint distribution of finitely many Y(j).
> Problem 18.10. Does d_TV(Y(j), xi_(j)) -> 0 hold for every fixed j, under the assumptions of
> Theorem 18.7?

Theorem 18.7's assumptions: w_0 > 0, omega = infinity, m = lambda n + o(sqrt n) with
0 < lambda <= nu, sigma^2 = Var xi < infinity, xi the size-biased law pi_k = w_k tau^k/Phi(tau)
with E xi = lambda; Y(1) >= Y(2) >= ... the ordered box counts of the allocation B_{m,n} and
xi_(1) >= xi_(2) >= ... the order statistics of n i.i.d. copies of xi. Its conclusions include
(v) d_K(Y(j), xi_(j)) -> 0 for every fixed j and (vi) d_TV(Y(1), xi_(1)) -> 0.

## Theorem

Under the assumptions of Theorem 18.7, d_TV(Y(j), xi_(j)) -> 0 for every fixed j >= 1. The
same holds in the xi^(n) version (lambda < nu, m/n -> lambda).

## Proof

The proof is Janson's proof of (vi) with two changes: the count events that sandwich
{Y(j) in A_l} must allow up to j - 1 boxes above the interval, and the resulting extra error is
of product form and sums to something small. I follow his notation and reuse, without reproving,
the three inputs his proof establishes on pages 89-93:

(F1) There is B(n) = o(sqrt n) with Y(1) < B(n) and xi_(1) < B(n) w.h.p. (his (18.19)-(18.20)).
(F2) For disjoint sets S_1, ..., S_q of integers below B(n) with n P(xi in S_i) -> alpha_i in
     [0, infinity] along a subsequence, the counts N_{S_i} = |{i' : Y_{i'} in S_i}| converge
     jointly to independent Po(alpha_i), and so do the i.i.d. counts N-bar_{S_i} (his joint
     factorial-moment argument on page 91 and the remark on page 93 "the proof extends easily
     (using joint factorial moments)"; a limit alpha_i = infinity means the count tends to
     infinity in probability).
(F3) d_K(Y(j), xi_(j)) -> 0 (his (v)).

Fix j. Let A = A(n) = {i : P(Y(j) = i) > P(xi_(j) = i)}, so that (Lemma 18.5(vi))

    d_TV(Y(j), xi_(j)) = P(Y(j) in A) - P(xi_(j) in A).

Fix delta > 0 and D > 0. Partition [0, B(n)) exactly as Janson partitions N_0, but with xi_(j)
in place of xi_(1): every i with P(xi_(j) = i) >= delta/2 is a singleton (at most 2/delta of
them), and the remaining intervals are chopped into intervals J_l with P(xi_(j) in J_l) <= delta
so that all but at most 2/delta + 1 of them have mass > delta/2. So L <= 4/delta + 1 intervals
J_l = [a_l, b_l]; call J_l fat if P(xi_(j) in J_l) > delta (then it is a singleton), thin
otherwise; good if n P(xi >= a_l) <= D, bad otherwise. Goodness is monotone: if J_l is good so is
every interval to its right. Write A_l = A cap J_l, A_l^c = J_l \ A_l, B_l = (b_l, B(n)), and
alpha_l = n P(xi in A_l), gamma_l = n P(xi in A_l^c), beta_l = n P(xi in B_l).

**Fat intervals.** J_l = {a_l} and A_l is J_l or empty, so by (F3)

    |P(Y(j) in A_l) - P(xi_(j) in A_l)| <= 2 d_K(Y(j), xi_(j)) = o(1).                          (1)

**Thin good intervals: the sandwich.** For 0 <= b <= j - 1,

    {Y(j) in A_l}  is contained in  union over b of {N_{B_l} = b, N_{A_l} >= 1, N_{A_l} + N_{A_l^c} >= j - b},
    union over b of {N-bar_{B_l} = b, N-bar_{A_l^c} = 0, N-bar_{A_l} >= j - b}  is contained in  {xi_(j) in A_l}.

First inclusion: if Y(j) in A_l then Y(j) <= b_l, so b := N_{B_l} <= j - 1 boxes exceed b_l; the
boxes ranked b + 1, ..., j lie in J_l, so N_{J_l} >= j - b; and the j-th itself lies in A_l, so
N_{A_l} >= 1. Second: if b <= j - 1 values exceed b_l, none lies in A_l^c, and at least j - b lie
in A_l, then the values ranked b + 1, ..., j are the largest values in J_l, all of them in A_l,
so the j-th is in A_l. The events on the right are disjoint in b.

**Thin good intervals: the estimate.** I claim that, uniformly over thin good intervals,

    P(Y(j) in A_l) - P(xi_(j) in A_l) <= (delta + eta) gamma_l + o(1),                            (2)

where eta = eta(delta, D, j) := (delta j! e^{2D})^{1/j}. Suppose not: then there are eps > 0
and, for n in a subsequence, a thin good interval J_l(n) violating (2) by eps. Pass to a
sub-subsequence along which alpha_l, beta_l, gamma_l converge to alpha, beta, gamma in
[0, D] (they are bounded by n P(xi >= a_l) <= D). Let X ~ Po(alpha), Y ~ Po(gamma),
Z ~ Po(beta) be independent. By (F2) and the sandwich,

    limsup P(Y(j) in A_l) <= sum_b P(Z = b) P(X >= 1, X + Y >= j - b),
    liminf P(xi_(j) in A_l) >= sum_b P(Z = b) e^{-gamma} P(X >= j - b),

so the limsup of the difference is at most

    sum_b P(Z = b) [ P(1 <= X < j - b, X + Y >= j - b) + (1 - e^{-gamma}) P(X >= j - b) ]
    <= P(X >= 1) P(Y >= 1) + gamma sum_b P(Z = b) P(X + Y >= j - b)
    <= alpha gamma + gamma lim P(xi_(j) in J_l)
    <= alpha gamma + gamma delta,

using P(X >= 1) <= alpha, P(Y >= 1) <= gamma, 1 - e^{-gamma} <= gamma, and, for the last line,
that {N-bar_{B_l} = b, N-bar_{J_l} >= j - b} is exactly {xi_(j) in J_l} with N-bar_{B_l} = b, so
sum_b P(Z = b) P(X + Y >= j - b) = lim P(xi_(j) in J_l) <= delta by thinness. Finally alpha is
small: thinness gives, with s = alpha + gamma,

    delta >= lim P(xi_(j) in J_l) >= P(Z = 0) P(X + Y >= j) >= e^{-D} e^{-s} s^j / j!,

so s^j <= delta j! e^{D + s} <= delta j! e^{2D}, i.e. alpha <= s <= eta. Hence the limsup of the
difference is at most (eta + delta) gamma, which contradicts the violation of (2) by eps once n
is large along the sub-subsequence (gamma_l -> gamma). This proves (2).

Summing (2) over the thin good intervals, whose union is contained in [a*, B(n)) for the
leftmost good left endpoint a*, with n P(xi >= a*) <= D:

    sum over thin good l of [P(Y(j) in A_l) - P(xi_(j) in A_l)] <= (delta + eta) D + L o(1).      (3)

**Bad intervals.** Let J_r = [a_r, b_r] be the rightmost bad interval, n P(xi >= a_r) > D; all
bad intervals lie in [0, b_r]. Then

    P(Y(j) in A cap [0, b_r]) - P(xi_(j) in A cap [0, b_r]) <= P(Y(j) <= b_r) = P(N_{(b_r, B(n))} <= j - 1)

(using (F1) to ignore boxes above B(n)). Put beta' = n P(b_r < xi < B(n)) <= D (the next interval
is good, or b_r + 1 = B(n)). Along any subsequence with beta' -> beta:
if beta >= D/2, then by (F2) P(N_{(b_r, B(n))} <= j - 1) -> P(Po(beta) <= j - 1) <=
P(Po(D/2) <= j - 1) =: eps_1(D), and eps_1(D) -> 0 as D -> infinity.
If beta < D/2, then n P(xi in J_r) = n P(xi >= a_r) - beta' > D/2 for large n, so by (F2)
liminf P(xi_(j) in J_r) >= P(Z' = 0) P(X' >= j) with Z' ~ Po(beta), X' ~ Po(s') and s' >= D/2
(if n P(xi in J_r) -> infinity the second factor tends to 1), which is at least
c(D, j) := e^{-D/2} P(Po(D/2) >= j) > 0. If J_r is thin this contradicts P(xi_(j) in J_r) <= delta
as soon as delta < c(D, j); so for such delta only the first case occurs and
P(Y(j) <= b_r) <= eps_1(D) + o(1). If J_r is fat it is the singleton {a_r}; (1) handles A_r, and
the intervals to its left are covered by P(Y(j) < a_r) = P(N_{[a_r, B(n))} <= j - 1) ->
P(Po(>= D) <= j - 1) <= eps_1(D) by (F2). Either way

    sum over bad l of [P(Y(j) in A_l) - P(xi_(j) in A_l)] <= eps_1(D) + o(1).                    (4)

**Conclusion.** By (1), (3), (4), for delta < c(D, j),

    d_TV(Y(j), xi_(j)) <= (delta + eta(delta, D, j)) D + eps_1(D) + o(1).

Given eps > 0 choose D with eps_1(D) < eps, then delta so small that delta < c(D, j) and
(delta + eta(delta, D, j)) D < eps, then n large. So d_TV(Y(j), xi_(j)) -> 0.

The xi^(n) version (lambda < nu, m/n -> lambda, xi replaced by xi^(n)) goes through unchanged,
exactly as Janson notes for (vi): the inputs (F1)-(F3) are stated by him in that version too.

## Remarks

* For j = 1 the sandwich reduces to Janson's ({N_A >= 1, N_B = 0} above, {N_A >= 1, N_B = 0,
  N_{A^c} = 0} below) and the estimate (2) reduces to his (18.30); the new term alpha gamma is
  the price of the boxes ranked below j but above the interval landing in A_l^c, and it is
  small because both alpha and gamma are small on a thin interval.
* Janson's second belief, total variation convergence of the joint law of (Y(1), ..., Y(J)),
  should follow by the same scheme with a product partition of N_0^J and the count events
  read coordinatewise; I have not written that out and do not claim it.
* No new probabilistic input is needed: the joint Poisson approximation of the counts, the
  truncation at B(n), and the Kolmogorov bound (v) are all in the source. This is what Janson
  predicted ("presumably this can be shown by a modification of the proof for Y(1)"), and the
  modification is the two displayed inclusions plus the inequality
  P(1 <= X < k, X + Y >= k) <= P(X >= 1) P(Y >= 1).

## Checks

The argument was checked against the source text line by line (Janson's pages 89-94, read in
full). The only new inequalities are P(X >= 1) <= alpha, P(Y >= 1) <= gamma, 1 - e^{-gamma} <=
gamma, and the two inclusions, each verified by direct reasoning above. No numerics were run: the
statement is a limit theorem whose finite-n behaviour is not the question, and the machine was
under a compute-distress flag at the time of writing. No Lean file for the same reason; the
inequalities used are elementary.

## Prior art

Not searched (web-search budget exhausted for the session); the intake's 2026-09-08 search on
Janson's large-box results found Addario-Berry's work on heights and widths but nothing on the
total variation question. Whether someone has written this modification down since 2012 is the
remaining check.
