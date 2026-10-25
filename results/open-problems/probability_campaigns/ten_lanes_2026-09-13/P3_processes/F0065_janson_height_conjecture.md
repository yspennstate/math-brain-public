# F0065 - Janson's height conjecture is not open: it was proved in 2022

Continuous-time stochastic processes, 13 September 2026. **This is a ledger correction.**

## The corpus entry

Corpus id `F0065`, source `janson_simply_generated_2012`, locator "Conjecture 20.5, Section 20.3,
PDF p. 136", last row `attempted_unsolved`, one attempt recorded reducing the conjecture to a
one-dimensional Sparre Andersen statement and noting it "may even fail for a contrived law". The
statement:

> Conjecture 20.5. If nu = 1 and sigma^2 = infinity, then H(T_n)/sqrt(n) -> 0 in probability.

for simply generated / conditioned Galton-Watson trees, H the height.

## The correction

The conjecture is **proved**, in the affirmative, and has been since January 2022.

> L. Addario-Berry and S. Donderwinkel, *Random trees have height O(sqrt(n))*, arXiv:2201.11773
> (submitted 27 Jan 2022); Annals of Probability **52** (2024), no. 6.

The abstract of arXiv:2201.11773v3, verbatim: "We obtain new non-asymptotic tail bounds for the height of uniformly random
trees with a given degree sequence, simply generated trees and conditioned Bienayme trees (the
family trees of branching processes), in the process settling three conjectures of Janson (2012) and
answering several other questions from the literature." Their Theorem 1, verbatim from the ar5iv
text: "Fix a probability distribution mu supported on N with |mu|_1 <= 1 and |mu|_2 = infinity.
Then, n^{-1/2} ht(T_{mu,n}) -> 0." That is exactly Conjecture 20.5 (the case |mu|_1 = 1) together
with Janson's Problem 20.7 (the case |mu|_1 < 1), in one statement, and the convergence is in
probability and in expectation. Their Theorem 19 extends it to simply generated trees with an
arbitrary weight sequence, and Theorem 20 gives sub-Gaussian tails, settling Janson's Problem 20.9.

Numbering note: the arXiv version of Janson's survey (arXiv:1112.0510)
numbers the statement 20.5, while Addario-Berry-Donderwinkel cite the published Probability Surveys
version, where the same statement is 21.5. Same conjecture.

A weaker precursor, useful to know about, is Addario-Berry, Brandenberger, Hamdan and Kerriou,
*Universal height and width bounds for random trees*, arXiv:2105.03195, which gets
ht(T_n)/(sqrt(n) log^3 n) -> 0 - the conjectured rate up to a log^3 factor - and is superseded.

The stable-domain sub-case was of course already known (Duquesne, Le Gall: height of order
n^{1-1/alpha} = o(sqrt(n)) for offspring in the domain of attraction of an alpha-stable law,
1 < alpha < 2). What Janson asked about and what was genuinely open is the general infinite-variance
case, including offspring laws in no domain of attraction at all. That is what the 2022 paper closes.

**Ledger disposition:** F0065 should move from `attempted_unsolved` to `literature_resolution`, with
resolution source arXiv:2201.11773 / Ann. Probab. 52(6) 2024, Theorem 1 (and Theorem 19 for the
simply generated version). Note also that the same paper closes `Problem 20.7` and `Problem 20.9` of
the same survey, so any sibling corpus rows drawn from Janson Section 20 should be re-checked.


## The correction is wider than F0065: five sibling rows are affected

Sweeping the corpus for rows keyed to Janson's survey turned up the whole Section 20 height/width
family, all of it still carried as open or partial:

| id | Janson | statement | current ledger row | actual status |
|---|---|---|---|---|
| F0065 | Conj. 20.5 | H(T_n)/sqrt(n) -> 0 when nu=1, sigma^2=inf | attempted_unsolved | **resolved**, ADD Thm 1 |
| F0066 | Conj. 20.6 | W(T_n)/sqrt(n) -> inf when nu=1, sigma^2=inf | partial_result, excluded | **resolved**, corollary below |
| F0067 | Prob. 20.7 | nu<1 implies H(T_n)/sqrt(n) -> 0 | attempted_unsolved | **resolved**, ADD Thm 1 |
| F0068 | Prob. 20.8 | nu<1 implies W(T_n)/sqrt(n) -> inf | partial_result, excluded | **resolved**, corollary below |
| F0069 | Prob. 20.9 | P(H(T_n) >= x sqrt(n)) <= C e^{-c x^2}, any weight sequence | attempted_unsolved | **resolved**, ADD Thm 20 |
| F0070 | Prob. 20.10 | growth rates of E H(T_n), E W(T_n) beyond finite variance | attempted_unsolved | **partly** settled (ADD give convergence in expectation and o(sqrt n); the exact rates are not claimed) |

ADD's Theorem 1 covers |mu|_1 <= 1 with |mu|_2 = infinity in one statement, which is 20.5 and 20.7
together, and their Theorem 19 does the same for general weight sequences. Theorem 20 gives the
sub-Gaussian tail bound of 20.9. The abstract's "three conjectures of Janson" fits: 20.5, 20.6 and
one more.

The two width statements need no new work at all once the height ones are in hand:

**Corollary (Conjecture 20.6 and Problem 20.8).** With H(T) = max{k : l_k(T) > 0} and
W(T) = max_k l_k(T), every tree satisfies n = |T| = sum_{k=0}^{H} l_k <= (H+1) W, so
W >= n/(H+1) and

    W(T_n)/sqrt(n) >= sqrt(n)/(H(T_n)+1).

If H(T_n)/sqrt(n) -> 0 in probability then the right-hand side tends to infinity in probability, so
W(T_n)/sqrt(n) -> infinity. Conjecture 20.6 is exactly this applied to nu = 1, sigma^2 = infinity,
and Problem 20.8 to nu < 1.                                                                  QED

That deterministic inequality is presumably how ADD get the width half too; either way, the corpus
rows F0066 and F0068 (currently `partial_result`, `admitted: false`) are settled and should be
re-dispositioned as literature resolutions rather than exclusions.

## Two elementary statements

Neither statement below is new. They are short, self-contained and correct, and the second shows
where the elementary approach stalls, which is of interest because the published proof needs a much
heavier method.

Notation: f(s) = E s^xi the offspring generating function, E xi = 1, xi non-degenerate; the key
object is

    g(u) := f(1-u) - (1-u) = sum_k p_k [ (1-u)^k - 1 + k u ]   for u in [0,1],

a sum of non-negative terms (so no cancellation), convex, increasing, with g(0) = 0 and
g'(u) = 1 - f'(1-u). Write K(u) := g(u)/u^2.

**Lemma 1.** sigma^2 = infinity if and only if K(u) -> infinity as u decreases to 0; and in that
case the survival probability q_n = P(Z_n > 0) of the critical Galton-Watson process satisfies
n q_n -> 0.

*Proof.* Each term of g satisfies h_k(u)/u^2 = [(1-u)^k - 1 + ku]/u^2 >= 0 and tends to k(k-1)/2 as
u decreases to 0, so Fatou gives liminf K(u) >= E[xi(xi-1)]/2, which is infinite exactly when
E xi^2 = infinity. For the survival probability, q_{n+1} = 1 - f(1-q_n) = q_n - g(q_n) and q_n
decreases to 0, so

    1/q_{n+1} - 1/q_n = g(q_n)/(q_n q_{n+1}) >= g(q_n)/q_n^2 = K(q_n) -> infinity,

hence 1/q_n grows faster than linearly, i.e. n q_n -> 0.                                     QED

This is classical - it is the infinite-variance half of Slack's 1968 theorem (R. S. Slack, *A
branching process with mean one and possibly infinite variance*, Z. Wahrsch. verw. Geb. 9 (1968)
139-145), the generalisation of Kolmogorov's n q_n -> 2/sigma^2.

**Lemma 2 (a quantitative height bound).** For every critical non-degenerate offspring law, every
n >= 1 and every 1 <= h <= 2n,

    P( H(T_n) >= h )  <=  exp( - sup_{0 < u < 1} [ h g'(u) - n g(u)/(1-u) ] ) / P(|T| = n),

and in particular, taking u = h/(4n),

    P( H(T_n) >= h )  <=  exp( - 2 n g(h/(4n)) ) / P(|T| = n).

*Proof.* Let F(x) = E x^{|T|} and F_h(x) = E[x^{|T|} 1{H < h}], so F_0 = 0 and
F_{h+1}(x) = x f(F_h(x)), and F(x) = x f(F(x)). Put D_h = F - F_h. Since f is convex and increasing
and F_h <= F,

    D_{h+1}(x) = x [ f(F(x)) - f(F_h(x)) ] <= x f'(F(x)) D_h(x) = lambda(x) D_h(x),

with lambda(x) = x f'(F(x)) < 1 for x < 1, so D_h(x) <= lambda(x)^h. Parametrise x by u in (0,1)
through y = 1 - u and x = y/f(y), which gives F(x) = y. Then f(y) = 1 - u + g(u), so

    log lambda(x) = log(1 - g'(u)) - log(1 + g(u)/(1-u)) <= -g'(u),
    log(1/x)      = log(1 + g(u)/(1-u)) <= g(u)/(1-u).

Since D_h has non-negative coefficients, P(H >= h, |T| = n) = [x^n] D_h <= D_h(x) x^{-n}, and
dividing by P(|T| = n) gives the first display. For the second, convexity gives g'(u) >= g(u)/u;
with u = h/(4n) <= 1/2 the exponent is at most g(u)(2n - 4n) = -2n g(h/(4n)).            QED

**Corollary.** Writing h = eps sqrt(n), the bound reads

    P( H(T_n) >= eps sqrt(n) ) <= exp( -(eps^2/8) K(eps/(4 sqrt(n))) ) / P(|T| = n),

so Conjecture 20.5 follows for any offspring law with
K(eps/sqrt(n)) / log(1/P(|T| = n)) -> infinity for every eps > 0. That covers every law in the
domain of attraction of an alpha-stable law with alpha < 2 (there K is regularly varying of index
alpha - 2 < 0, so K(1/sqrt(n)) is a positive power of n, while log(1/P(|T|=n)) = O(log n) by the
local limit theorem), but it does **not** cover the general case, and in particular not laws where
E xi^2 is only barely infinite.

**Where it stalls, and the calibration that shows the bound is the right shape.** In the
finite-variance case K -> sigma^2/2 and the bound becomes C n^{3/2} exp(-eps^2 sigma^2/16), whereas
the truth (Addario-Berry-Devroye-Janson 2013) is exp(-c eps^2). So the exponential factor is
correct and the whole loss is the polynomial prefactor 1/P(|T| = n), which comes from the crude step
[x^n] D_h <= D_h(x) x^{-n}. The clean remaining obligation for the elementary route is therefore:
prove P(|T| = n, H >= h) <= C exp(-c n g(h/(Cn))) * P(|T| = n) directly, i.e. get a coefficientwise
rather than a saddle-point comparison. The published proof takes a different and much more
substantial route (degree-sequence stochastic ordering).

## Machine check of Lemma 2

The inequality is not asymptotic, so it can be checked exactly. Using the coefficient recursion
F_{h+1} = x f(F_h) up to x^300 with the critical offspring law p_k proportional to k^{-3} truncated
at 400 (variance 7.67), I compared the exact conditional probability P(H >= h | |T| = n) with the
bound at n in {50, 100, 200, 300} and h in {5, 10, 20, 40}. In all 16 cells the bound holds, with
slack between 8e2 and 2e10 - exactly the polynomial-prefactor lossiness predicted above. No
violation. Lemma 1's conclusion n q_n -> 0 was also confirmed numerically on that law
(n q_n: 0.43 at n = 5, 0.31 at n = 50, 0.195 at n = 500, 0.144 at n = 4000, with the increments
1/q_n - 1/q_{n-1} rising steadily from 2.2 to 7.8, as Lemma 1 requires).

## Status

- Conjecture 20.5: **proved in the literature (2022/2024)**. F0065 is not an open problem.
- Lemma 1: **proved**; classical (Slack 1968).
- Lemma 2 and its corollary: **proved**, machine-checked, and **not new** - weaker than the
  published theorem. Recorded for the reduction it makes explicit, not as a result.

## Literature check

Searches run 2026-09-13: "Janson Conjecture 20.5" (returns nothing - the resolution cites it as
Conjecture 21.5, from the published numbering, which is why a naive search misses it), "height
conditioned Galton-Watson infinite variance", "Addario-Berry Donderwinkel random trees height",
"Kortchemski height conditioned Galton-Watson", "Slack 1968 branching process mean one infinite
variance". arXiv ids 2201.11773, 2105.03195 and 1710.08240 were each checked against their abstracts.
