# Audit of the amplification lemma

## Posterior law, derived two ways

Write X for an original edge indicator and Y for its refreshed indicator. Directly from the transition rule,

    P(X=1,Y=0)=p delta(1-p),   P(Y=0)=1-p,

so P(X=1|Y=0)=delta p.

Independently, conditional expectation gives E[Y|X]=(1-delta)X+delta p, hence Cov(X,Y)=(1-delta)p(1-p). Therefore

    E[XY]=p^2+(1-delta)p(1-p),
    P(X=1,Y=0)=p-E[XY]=delta p(1-p).

The verifier checks forward Bayes' formula against the reversed transition kernel for all 4096 ordered graph pairs on four vertices. It then sums that posterior over all possible original graphs for each permissible (H,I), rather than inserting a presumed binomial formula. All 225 resulting distributions match the claimed binomial distribution exactly as rational numbers.

This law would generally fail if the rule choosing I were allowed to inspect G. The algorithm chooses and truncates I using only H and fresh solver bits. The repair step inspects G only afterward.

## Negative exponents and rare success

The analytic input concerns negative q as well as 0<q<p<1. Corollary 1.11 was checked in the primary-source PDF, page 5. The edge bias p=d/n has no lower bound uniform in n; this is precisely why the dimension-free, atom-independent result is used.

The semigroup time condition is checked explicitly in PROOF.md. The sign change is essential:

    ||Q||_(-r) >= v^(1/r)

implies E[Q^(-r)]<=1/v, because raising to -r reverses the inequality. Markov then gives P(Q<u)<=u^r/v.

A second derivation of this last tail bound is a direct lower bound on the moment contribution from the bad set. If beta=P(Q<u), then E[Q^(-r)]>=beta u^(-r). Combining this with the negative-moment bound gives beta<=u^r/v. This independently checks the direction and exponent, but uses the same imported analytic theorem; it is not an independent proof of reverse hypercontractivity.

The verifier checks all 255 nonempty events on three coordinates for each of twelve (bias, refresh) pairs, including bias 1/100. It also checks all 80 nonzero functions with values in {0,1/2,1} on two coordinates. These are floating-point sanity checks, marked as such in the log and data.

## Exponential repair bound, derived two ways

The proof uses E[2^X]<=(exp mu) and threshold eta n/2 with mu<=eta n/4, yielding

    kappa eta n = (eta n/4)(2 log 2-1).

Alternatively, start with the general moment-generating-function estimate E[exp(lambda X)]<=exp(mu(exp(lambda)-1)). Optimizing at exp(lambda)=t/mu, for t>mu, yields

    P(X>=t)<=exp(-[t log(t/mu)-t+mu]).

The bracket decreases as mu increases to eta n/4, with t=eta n/2. At that endpoint it equals (eta n/4)(2 log 2-1), the same exponent. This gives an independent optimization check on the constant, rather than merely evaluating the same displayed formula twice.

The numerical value

    kappa=0.09657359027997265470861606072908828403775006718012762706034

was computed using Decimal.log. An independent exact-rational series

    log 2 = 2 sum_{j>=0} (1/3)^(2j+1)/(2j+1)

was truncated after 65 terms with its tail bounded geometrically. It agrees to the recorded precision. The sign also follows without numerics from integral_1^2 1/x dx>1/2.

## Trial selection and dependence

Simply conditioning on the first solver success and asserting a fresh binomial repair law could introduce a selection bias through the shared G. The proof does not use that assertion. It bounds the unconditional bad-repair event for each predetermined trial and unions over all M trials. Independence across trials is used only after conditioning on G to bound the event of no solver success. The final union bound does not require unconditional trial independence.

Repeating the original solver with new coins alone would not prove this theorem: some input graphs might have conditional solver success zero. Refreshing the graph and using the negative-moment bound is what addresses this obstruction.

## Edge cases and computational model

- The solver may be deterministic, discontinuous, label-dependent, and highly unstable. Nothing in the proof bounds output changes.
- The solver may sometimes return malformed output or a set with internal edges; verification rejects it.
- Oversized valid outputs are truncated before consulting G.
- Marking the smaller endpoint of each original internal edge deletes at most one vertex per edge, even when marks repeat. Every internal edge is covered by a mark.
- a=1 is allowed. The finite checks include it.
- The inequalities use k=ceil(a n), not a n. The loss budget is at least eta n-1, and the theorem explicitly requires n>=2/eta.
- n>d ensures 0<p<1. n>=1/a controls the additive rounding term in the expected repair cost.
- The theorem is stated for rational d,a,b so that sampling and thresholds have an ordinary finite-bit implementation. It applies to all fixed integer d, which suffices for the displayed overlap-scale corollary. The logarithmic target is bracketed by rational densities.
- The Bernoulli approximation is coupled over all trials, not only over one trial. Its error is bounded by M n^2 2^(-w). The proof uses an integer-valued bit budget.
- The runtime exponent may be very large when the density slack is small. It remains a constant because d,a,b,s,L are fixed before n tends to infinity. No uniform polynomial guarantee for d growing with n is claimed.
- The theorem needs an eventual success lower bound. It preserves the quantitative bound on any subsequence where the hypothesis happens to hold, but does not fill the gaps between such n.
- The theorem gives fixed positive density slack. Taking b=a, or taking a-b to zero with n, is not justified by its polynomial-time bound.

## What this audit does not establish

The finite computation does not show that any solver reaches the desired density. The cited analytic theorem is not reproved here. There is no reduction from planted clique, random SAT, or another named average-case hardness assumption. There is no universal OGP-hardness implication. The original all-polynomial-time barrier remains open in this work.
