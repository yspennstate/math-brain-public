# The largest box in a sparse random allocation is O(log n / log(n/m)), so Janson's Conjecture 18.4 holds

Settled 2026-09-09. Ledger id F0055 (intake F, source `janson_simply_generated_2012`).

## The problem as the source states it

Janson, *Simply generated trees, conditioned Galton-Watson trees, random allocations and
condensation*, Probability Surveys 9 (2012), Section 18.1. A weight sequence w = (w_k) with
w_0 > 0 and w_k > 0 for some k >= 1 defines the random allocation B_{m,n} of m balls in n boxes,
P(Y = y) proportional to prod_i w_{y_i} over compositions y of m into n parts; Phi(t) = sum w_k t^k
has radius rho; Y(1) is the largest box. Theorem 18.3 gives, for m/n -> lambda in (0, nu),
Y(1) <= log n / log(rho/tau) + o_p(log n) with Psi(tau) = lambda. Then:

> We conjecture that Theorem 18.3 holds also for lambda = 0. Since then tau = 0, this means the
> following. (This seems almost obvious given the result for positive lambda in Theorem 18.3, where
> the constant 1/log(rho/tau) -> 0 as lambda -> 0 and thus tau -> 0, but there is no general
> monotonicity and we leave this as an open problem.)
> Conjecture 18.4. If rho > 0 and m/n -> 0, then Y(1) = o_p(log n).

## Theorem

Let w_0 > 0, w_1 > 0 and rho > 0, and let m = m(n) with m/n -> 0. Fix any 0 < r < rho and put
gamma = min(1, w_1/w_0). Then for every delta > 0, with high probability

    Y(1) <= (1 + delta) log n / log( gamma r n / (2m) ).

In particular Y(1) = O_p(log n / log(n/m)) = o_p(log n), which is Conjecture 18.4. The general case
w_1 = 0 (span 1) is handled at the end with the same argument and a weaker constant.

## Proof

Write Z_{k,N} = [t^k] Phi(t)^N for the partition function of k balls in N boxes. By exchangeability
of the boxes and the product form of the weight,

    P(Y_1 = j) = w_j Z_{m-j, n-1} / Z_{m,n},          P(Y(1) >= k) <= n sum_{j >= k} P(Y_1 = j).      (1)

**The comparison.** Fix 1 <= j <= m and suppose m <= n/4. Consider the relation between
configurations y of m - j balls in n - 1 boxes and configurations z of m balls in n boxes given
by: z is obtained from y by choosing a set J of j indices i <= n - 1 with y_i = 0, setting z_i = 1
for i in J, z_i = y_i otherwise, and appending an empty box z_n = 0. The weight changes by the
factor w_0 (w_1/w_0)^j (j empty boxes become singletons, one empty box is added). Each y has at
least C(E(y), j) images, where E(y), the number of empty boxes of y, is at least (n - 1) - (m - j)
>= n - 1 - m; each z has at most C(S(z), j) preimages, where S(z) <= m is the number of singleton
boxes of z (the preimage is determined by which singletons are removed). Summing the weight over
the relation in both orders,

    C(n-1-m, j) w_0 (w_1/w_0)^j Z_{m-j,n-1} <= sum_{(y,z)} W(z) <= C(m, j) Z_{m,n},

so, with N = n - 1 - m >= n/2 and using C(m,j)/C(N,j) = prod_{i<j} (m-i)/(N-i) <= (m/N)^j for
j <= m <= N,

    Z_{m-j,n-1}/Z_{m,n} <= (1/w_0) (w_0/w_1)^j (2m/n)^j,
    P(Y_1 = j) <= (w_j/w_0) (2m/(gamma n))^j.                                                        (2)

(For j > m both sides of (1) vanish. If j > n/4 the bound is not needed since j <= m <= n/4.)

**The tail.** Since Phi(r) < infinity, w_j <= C_r r^{-j} for all j with C_r = Phi(r). Put
q_n = 2m/(gamma r n), which tends to 0. Then (2) gives P(Y_1 = j) <= (C_r/w_0) q_n^j, and by (1),
for q_n < 1,

    P(Y(1) >= k) <= n (C_r/w_0) q_n^k / (1 - q_n).

Take k = k_n = ceil((1 + delta) log n / log(1/q_n)). Then n q_n^{k_n} <= n^{-delta}, so
P(Y(1) >= k_n) -> 0, and k_n = o(log n) because log(1/q_n) -> infinity. That is the theorem.

**Why no monotonicity was needed.** Theorem 18.3 estimates P(Y_1 = j) through the i.i.d.
representation with the tilt tau(lambda) and a local limit theorem, which degenerates as
lambda -> 0; the source's obstacle was that Y(1) is not known to be monotone in m for general
weights. The comparison (2) never tilts: it moves the j balls of one box into j of the many empty
boxes, and the only input is that empty boxes outnumber singletons by a factor n/(2m). The constant
in Theorem 18.3, 1/log(rho/tau), and the constant here, 1/log(gamma rho n/(2m)) (letting r -> rho),
agree in order since tau(lambda) is of order lambda for small lambda (Psi(t) ~ (w_1/w_0) t at 0), so
the theorem is the lambda = 0 case of Theorem 18.3 with the same log n/log(1/tau) scaling.

**The case w_1 = 0.** Let D = {k >= 1 : w_k > 0}. If gcd(D) = d > 1, only m divisible by d occur
and dividing all box counts by d reduces to gcd 1 with the weight sequence (w_{dk})_k, which has
radius rho^d > 0. So assume gcd(D) = 1: then there are a finite F subset of D, K = max F, and j_0
such that every j >= j_0 is a sum of elements of F; fix one such representation for each j, with
p(j) >= j/K parts. Replace "j singletons" in the comparison by "p(j) boxes carrying the parts of
j", assigned to the chosen empty boxes in a canonical order. The weight factor is at least
w_0 gamma_F^{p(j)} with gamma_F = min(1, min_{f in F} w_f/w_0), the image count is at least
C(n-1-m, p(j)), the preimage count at most C(m, p(j)), and (2) becomes
P(Y_1 = j) <= (w_j/w_0) (2m/(gamma_F n))^{p(j)} <= (w_j/w_0) q'^j with q' = (2m/(gamma_F n))^{1/K},
for j >= j_0. The tail argument is unchanged and gives Y(1) = O_p(log n / log(n/m)) again, with
constant K/log(gamma_F r^K n/(2m)).

## Remarks

* The bound is the right order. For the Poisson weights w_k = 1/k! the allocation is uniform
  multinomial, and the classical maximum load with m = o(n) balls is of order
  log n / log(n log n / m) (Gonnet; Raab and Steger), matching log n / log(n/m) up to the
  log log factor absorbed by delta.
* Nothing in the argument uses sigma^2 < infinity or a local limit theorem, so it also covers
  weight sequences for which Theorem 18.7's machinery is unavailable at lambda = 0.

## Checks

Exact computation (mpmath, 30 digits; f0055.py) of P(Y_1 = j) = w_j Z_{m-j,n-1}/Z_{m,n} for
j = 1..m and of P(Y(1) >= k) = 1 - Z^{(<k)}_{m,n}/Z_{m,n} (truncated weights), in the five cases
the run completed before the machine's compute governor cut it off: Poisson weights w_k = 1/k! at
(n, m) = (2000, 44), (20000, 141), (100000, 316) and uniform weights w_k = 1 at (2000, 44),
(20000, 141) (m about sqrt n). The ratio of P(Y_1 = j) to the bound (2), maximised over j, is
0.489, 0.497, 0.498, 0.479, 0.493 (never above 1/2), and P(Y(1) >= log n) is at most 5e-11 in every
case while P(Y(1) >= (log n)/4) is 0.38 to 0.63 - the log n / log(n/m) scale, as the theorem says.
The geometric, linear and w_1 = 0 families in the script were not reached and are unchecked.

Lean 4 (Prob1000/F0055.lean): the binomial-ratio inequality prod_{i<p}(m-i) N^p <= m^p prod_{i<p}(N-i)
for 0 <= p <= m <= N, and the union-bound tail sum_{j in [k,J)} P_j <= A q^k/(1-q) from
P_j <= A q^j, on standard axioms.

## Prior art

The web-search budget for the session was exhausted before this problem; the source's own
status ("we leave this as an open problem", 2012) is the record, and the ledger's intake search
of 2026-09-08 found nothing later on the largest box at m = o(n). The comparison argument is
elementary and may well be known in the balls-in-boxes literature for specific weights (it is
the standard way to bound the maximum load in the multinomial case); its application to general
weight sequences, and the observation that it removes the monotonicity obstacle Janson names, is
what this note records. A citation search is the remaining step.
