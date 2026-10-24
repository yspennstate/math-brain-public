# Three problems from the end of Janson's survey that the campaign's ledgers never recorded, two of them answered

New ledger rows I0020, I0021, I0022 (intake I). Source: S. Janson, *Simply generated trees, conditioned Galton–Watson trees, random allocations and condensation*, Probability Surveys 9 (2012), Problems 20.3, 20.4 and 20.11. Written 14 September 2026, about 08:00.

## How they were found

Sweeping the survey for every numbered `Problem` or `Conjecture` turns up nineteen. Intake F carries sixteen of them, as rows F0055 to F0070. The other three are Problems 20.3, 20.4 and 20.11, and none of the seven ledgers carries any of them: searching every row's locator, title and statement for either numbering, the arXiv one or the journal one, returns nothing for these three while the same search returns the rows for Problems 20.2, 20.5 and 20.7, which is the control that the search works. Two of the three are one step from Problem 20.2, which was answered earlier tonight, and that answer settles them.

## Problem 20.3

*"Extend this to the more general case of balls-in-boxes as in Theorem 10.4. (We guess that the case $0 < \lambda < \nu$ is easy by the methods in the references above, in particular [55] and [33, Section 3.2.1], but we have not checked the details.)"* Here "this" is the asymptotic normality of the counts $N_d$ of boxes with $d$ balls, and Theorem 10.4 is the law of large numbers $N_d(B_{m,n})/n \to_p \pi_d$ for $m/n \to \lambda$, with $\tau$ solving $\Psi(\tau) = \lambda$ when $\lambda \le \nu$ and $\tau = \rho$ when $\lambda > \nu$, so that $\pi$ has mean $\mu = \min(\lambda,\nu)$ and variance $\sigma^2 = \tau\Psi'(\tau) \le \infty$.

**Answer.** The extension holds, in the following form, exactly when the conditioning sits at the mean of the tilted law and that law has finite variance.

*(a) $0 \le \lambda < \nu$.* Yes, with no extra hypothesis, and Janson's guess is right. Choose $\tau_n$ with $n\Psi(\tau_n) = m + O(1)$, so the allocation is $n$ i.i.d. copies of $\xi \sim \pi^{(n)}$ conditioned on $S_n = m$ with $m - n\mu = O(1)$. Since $\tau < \rho$, the tilted law has a finite exponential moment, so for any finite set of degrees the vector $\big(\sum_i \mathbf 1\{\xi_i = d\}\big)_{d \in D}$ together with $S_n$ obeys a multivariate local limit theorem; conditioning the limiting Gaussian on its last coordinate gives
$$\frac{N_d - n\pi_d}{\sqrt n} \longrightarrow N\big(0,\ \sigma_d^2\big), \qquad \sigma_d^2 = \pi_d(1-\pi_d) - \frac{(d-\mu)^2\pi_d^2}{\sigma^2},$$
jointly in $d$, with $\mathrm{Cov} = -\pi_d\pi_e - (d-\mu)(e-\mu)\pi_d\pi_e/\sigma^2$ for $d \ne e$. At $\mu = 1$ this is Kolchin's (20.6) and Janson's (20.7), so the tree case is the special case $\lambda = \mu = 1$.

*(b) $\lambda = \nu$, $\sigma^2 < \infty$.* Yes, by the same argument: the tilted law at $\tau = \rho$ need not have an exponential moment, but a finite covariance matrix is all the lattice local limit theorem needs.

*(c) $\lambda = \nu$, $\sigma^2 = \infty$.* The formula would read $\sigma_d^2 = \pi_d(1-\pi_d)$. That holds under regular variation and fails in general: Theorem B of the memo on Problem 20.2 constructs a law with $\nu = 1$, $\sigma^2 = \infty$ along which $(N_1 - n\pi_1)/\sqrt n$ converges to a two-point mixture of Gaussians, not to a Gaussian.

*(d) $\lambda > \nu$.* Again the formula would read $\pi_d(1-\pi_d)$, the constraint being absorbed by the condensate rather than by the bulk. That holds under regular variation, by the argument of Thévenin's Theorem 6.7, and fails in general: Theorem A of the same memo is exactly a case $\lambda > \nu$, a subcritical law conditioned at $\lambda = 1 > \nu$, along which $(N_1 - n\pi_1)/\sqrt n$ is asymptotically a two-point law.

So Problem 20.3 is answered: yes in the two regimes where the conditioning is at the mean of a finite-variance tilted law, no in the other two, with the dividing line being local flatness of the tail at the scale the conditioning has to supply.

## Problem 20.4

*"Extend this to the subtree counts in Theorem 7.12."* Theorem 7.12 is the law of large numbers $N_T/n \to_p \mathbb{P}(\mathcal T = T)$ for the number of fringe subtrees of $T_n$ equal to a fixed tree $T$.

**Answer.** For $\nu \ge 1$ with $\sigma^2 < \infty$ this was settled by the author of the problem four years after stating it: S. Janson, *Asymptotic normality of fringe subtrees and additive functionals in conditioned Galton–Watson trees*, Random Structures Algorithms 48 (2016), whose Theorem 1.5 gives asymptotic normality of the number of fringe subtrees isomorphic to any given tree, and jointly for several, assuming only mean one and finite variance. So the row should be marked resolved by that paper.

Outside that regime the answer is no, and the counterexamples need no new work: the fringe subtree consisting of a single vertex is a leaf, so $N_\bullet = N_0$, and in both constructions of the Problem 20.2 memo the bulk is carried by the two degrees $0$ and $1$, so the leaf count is $n - N_1 + O(1)$ and inherits the two-point behaviour of $N_1$. Hence for $\nu = 1$ with $\sigma^2 = \infty$, and for $\nu < 1$, the fringe subtree counts are not asymptotically normal in general.

## Problem 20.11

*"Is there some kind of similar limiting object in the case $\nu < 1$ (after suitable scaling)?"* — that is, a counterpart of the continuum random tree or the stable trees for the condensation regime.

**Status, not an answer.** Kortchemski, *Limit theorems for conditioned non-generic Galton–Watson trees*, Ann. Inst. Henri Poincaré 51 (2015) 489–511, settles the shape question for non-generic weights with a power-law tail: a unique vertex of macroscopic degree appears, the rest is a forest of subcritical trees, and the height grows logarithmically in the size, so there is no metric scaling limit of the $\sqrt n$ kind, and the natural limit object is the condensation structure rather than a continuum tree. Local limits in the condensation case are in Abraham and Delmas (2014), and the critical Cauchy boundary case in Kortchemski's later work. What is not settled, as far as a bounded search shows, is the general $\nu<1$ weight sequence without a regularly varying tail, which is the same gap that F0058, F0064 and part (d) above open up: the lacunary laws have no scaling limit of any of these kinds, because the size of the condensate is itself not asymptotically determined.

## Status

Problems 20.3 and 20.4 answered, the second half of 20.4 by citation to the survey's own author. Problem 20.11 given a literature status and a precise remaining gap. All three were missing from the corpus and are now rows I0020, I0021, I0022 of intake I. Verification: author checked; the proof in (a) and (b) is the standard conditioned multivariate local limit theorem and reproduces Kolchin's variance as a special case, which is the control; (c) and (d) are the constructions of the Problem 20.2 memo, which carry their own exact numerical check. Prior art: Janson 2016 for 20.4 in the critical finite-variance case, Thévenin 2020 for the regularly varying cases, Kortchemski 2015 for 20.11; a bounded search found nothing addressing 20.3 as stated. Not a clearance.

## New open problem

The four-way answer to Problem 20.3 says the counts are asymptotically normal exactly when the conditioning sits at the mean of a finite-variance tilted law, and otherwise only under a regularity condition on the tail. State and prove the regularity condition that is necessary and sufficient. The candidate, from F0064, is local flatness at the relevant scale: $\pi_{k+j}/\pi_k \to 1$ uniformly for $|j| \le C\sqrt k$ along the scale $k$ that the conditioning has to supply, which is $(\lambda - \nu)n$ when $\lambda > \nu$ and the size of the largest fluctuation when $\lambda = \nu$, $\sigma^2 = \infty$.
