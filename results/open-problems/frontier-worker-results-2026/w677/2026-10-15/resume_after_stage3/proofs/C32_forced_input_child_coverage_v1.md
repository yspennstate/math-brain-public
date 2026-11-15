# C32 v1: child coverage by deterministically supplied inputs

Status: proof (unaudited). Kind: special. Target: 1.
This is an elementary ingredient for a possible input-delivery bootstrap.
Novelty is unassessed. It does not supply that bootstrap or prove recurrence.
The hardest open piece is a positive exact-law linear mean lower bound in C30.

## Statement and precise restrictions

Use the finite-horizon, retained-path model of independently audited C31 v1.
Fix d>=2, 0<p<1/2, q=(1-p)/d and beta=p/(1-p). At an internal vertex v,
prescribe a DETERMINISTIC number k>=1 of waking-enabled incoming inputs,
serially into the same fresh environment. Its resident wakes exactly once.
Each child edge has a finite positive enabled-entry budget B. Quotas, ordinary
motion and suppression have exactly C31's meanings. In particular a suppressed
excursion retains its walk, and its suppression clears on returning to v.
Let N_c be the total number of enabled entries into a specified child c during
this forced response query. Set

    r = q / (1-(d-1)*q*beta).

There is a coupling with S_c distributed as Binomial(k+1,r) such that

    N_c >= min(B,S_c).

Consequently, for 1<=ell<=B,

    P(N_c<ell) <= sum_(i=0)^(ell-1) binom(k+1,i) r^i (1-r)^(k+1-i).

The probability that some child receives no enabled entry is at most
min(1,d*(1-r)^(k+1)). Indicators for DIFFERENT children need not be independent.
These are laws of prescribed fresh queries, NOT conditional bounds given a
random number of inputs produced by an ancestor in the actual exploration.

## 1. One original path

Start an ordinary frog at v and absorb it at v's parent. Before absorption or
escape, the probability that it ever enters c is r. Its first step enters c
with probability q, enters the absorbing parent with probability p, or enters
one of d-1 other children with total probability (d-1)q. After an entry into
another child it returns to v with probability beta; on returning, its future
has the original law. Thus the first-step equation is

    r=q+(d-1)*q*beta*r.

The coefficient (d-1)q beta is less than p<1, giving the displayed solution.
Moreover denominator-q=p+(d-1)q(1-beta)>0, so 0<r<1. The value beta follows
from the finite gambler's-ruin calculation in C31 section 1. No independence
between different visited children has been used.

## 2. Coupling the k inputs and one resident

Give each prescribed input and the one resident its independent ordinary
personal path, stopped on first hitting v's parent. These are k+1 independent
fresh path segments, even if a physical frog supplies a later input after an
earlier retirement: the new future is fresh by the strong Markov property.
The deterministic forced-query experiment supplies every one of these inputs;
it does not condition on the actual dynamics delivering them.

Let I_i(c) indicate that path i ever enters c before its absorption or escape.
The preceding calculation and independent personal paths give independent
Bernoulli(r) indicators over i; hence S_c=sum_i I_i(c) has the binomial law.
The retained-path coupling in C31 does not remove any of these motions.
An input starts enabled at v. If it enters another child while suppressed,
it cannot reach c without returning to v, where its suppression clears.
At its first entry into c, therefore, either that edge already has B enabled
entries, or this entry is itself enabled. Distinct contributing paths use
distinct entries. If fewer than B enabled entries occur in total, every one
of the S_c first hits is enabled; otherwise the desired inequality is already
true. This proves N_c>=min(B,S_c). This reasoning also applies to the resident.

For ell<=B, the event N_c<ell implies S_c<ell, proving the tail bound. Apply
the union bound to the d events N_c=0 to obtain the final assertion. Their
mutual independence is neither asserted nor required. Other activated frogs
can increase N_c; the proof does not need to count their contributions.

## 3. Exact ordinary-T3 consequence and its limitations

At p=q=1/4 and beta=1/3, r=3/10. Write a=7/10. For the hypothetical forced
queries with k=K_j^(alpha), where

    K_j^(alpha)=min{K>=1:4^K >= (j+2)^alpha},

the all-children coverage failure bound is 3*a^(K_j^(alpha)+1). For alpha=4
or 8 this sequence of bounds is summable. Indeed put n=j+2 and group n into
[2^m,2^(m+1)), m>=1. This group has 2^m integers and
K_j^(alpha)>=(alpha/2)*m. Its summed bounds are at most

    3*a*(2*a^(alpha/2))^m.

For alpha=4 the ratio is 49/50; for alpha=8 it is 2401/5000. Both are below
one. In particular for alpha=8 the tail from j>=62 is at most

    (21/10)*(2401/5000)^6/(1-2401/5000) < 1/20.

This concerns forced-query bounds only. It does NOT show that the real
exploration supplies K_j^(alpha) inputs at depth j, that the relevant good
events persist conditionally on an adaptive history, or that one initial
frog initiates a successful cascade. Even summable unconditional errors
cannot supply those missing statements.

There is a quantitative reason this ingredient alone is insufficient. For
adjacent logarithmic quotas B=K_(j+1)^(alpha), k=K_j^(alpha), one has B/k->1,
while S_c has mean (3/10)(k+1). For all sufficiently large k, Chebyshev gives

    P(S_c>=B) <= ((k+1)*(3/10)*(7/10)) / (B-(3/10)*(k+1))^2 -> 0.

Thus the k+1 original paths do not themselves give a high-probability
certificate of the NEXT child's full input quota. Returns from newly
activated residents must provide the missing amplification. This is a gap
in this proposed bootstrap, not an upper bound ruling out the actual model.

## 4. Validation and dependencies

`check_c32_exact.py` checks the exact rational first-step identity, finite
gambler's-ruin approximants, binomial normalization/means, dyadic quota
inequalities and the 1/20 tail. These controls use Python Fraction and integer
powers; no floating-point step is used. They do not independently audit the
probabilistic path coupling. C31 v1's PASS supplies the retained-path model;
C30 v1's PASS states the remaining sufficient linear-growth criterion.
No recurrence threshold or new lower-model simulation is claimed.
