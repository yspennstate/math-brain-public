# The squared coefficient of variation of a Markov-modulated Poisson process is at least one

Settled 2026-09-08. Ledger id E0077 (intake E, source `map_processes_open_2019`).

## The problem as the source states it

Asanjarani and Nazarathy, *Stationary Markovian arrival processes: results and open problems*,
arXiv:1905.01736 (ANZIAM J.), Section 4:

> We embarked on this research due to the folklore assumption that for MMPP, c^2 >= 1 (III).
> Initially we believed that it is easy to verify, however to date there isn't a known proof
> for an arbitrary irreducible MMPP. ... Conjecture 4.1. For an irreducible MMPP, c^2 >= 1.
> Conjecture 4.2. For an irreducible MMPP, T_1^pi >=_st T_1^alpha.

Here c^2 = Var(T_1^alpha)/E[T_1^alpha]^2 with T_1^alpha the event-stationary inter-event time,
and T_1^pi the time-stationary one (the forward recurrence time). The same authors had posted a
proof in 2018 (arXiv:1802.08400, *The squared coefficient of variation for MMPP is greater than
unity*) and withdrew it in May 2019 with the comment "There's a problem in the proof of Theorem
3.1". That attempt argued the stochastic order (IV) by a sign-pattern argument on the vector
(pi - alpha)(-C)^{-1}, entirely inside matrix-analytic methods. In the conclusion of the 2018 note
they also conjecture the statement for a general Cox process on the line whenever E[(T^alpha)^2]
is finite, remarking that establishing it "would clearly use different methods than the matrix
analytic methods used in this note", and they record the belief that c^2 = 1 forces all lambda_i
equal, without proof.

## Theorem

Let N be a stationary Cox process on the line directed by a stationary, almost surely diffuse
random measure Lambda with intensity lambda* = E Lambda(0,1] in (0, infinity) and with
Lambda(R) = infinity almost surely (so N has infinitely many points on each side almost surely;
this is automatic for an ergodic directing measure, and for an MMPP), and let T^alpha be its
Palm (event-stationary) inter-event time. Then c^2(T^alpha) >= 1, with equality if and only
if N is a Poisson process (Lambda = lambda* Leb a.s.). In particular Conjecture 4.1 holds for
every irreducible MMPP, and c^2 = 1 for an MMPP if and only if all lambda_i are equal.

## Proof

Write S(t) = P(N(0,t] = 0) for the time-stationary void probability. Conditional on Lambda the
process is Poisson, so

    S(t) = E[ exp(-Lambda(0,t]) ].

Since exp is convex, Jensen's inequality gives

    S(t) >= exp(-E Lambda(0,t]) = exp(-lambda* t)          for every t >= 0,        (1)

using only that E Lambda(0,t] = lambda* t, which is stationarity of the directing measure.
The forward recurrence time T^pi has P(T^pi > t) = S(t), so integrating (1),

    E[T^pi] = integral_0^infinity S(t) dt >= 1/lambda* = E[T^alpha].                  (2)

For any stationary simple point process with finite positive intensity the Palm inversion
formula (Daley and Vere-Jones, vol. II, eq. (3.4.17); the source's Lemma 2.1) reads
E[T^pi] = lambda* E[(T^alpha)^2]/2, and E[T^alpha] = 1/lambda*. Hence

    c^2 = E[(T^alpha)^2]/E[T^alpha]^2 - 1 = 2 lambda* E[T^pi] - 1 >= 1.                (3)

If E[(T^alpha)^2] is infinite then c^2 is infinite and there is nothing to prove.

The hypothesis Lambda(R) = infinity a.s. is needed and not decorative: if with probability p_0 > 0
the directing measure is zero (an empty process mixed with a Poisson process of rate
lambda*/(1 - p_0), say), the intensity is still lambda* but the Palm inversion formula reads
E[T^pi; T^pi < infinity] = lambda* E[(T^alpha)^2]/2 with T^pi = infinity on the empty event, and
E[T^alpha] = (1 - p_0)/lambda*, so (3) fails as written. This was pointed out by a Codex agent
auditing the note (audits/evidence/2026/09/08/overnight-mmpp-exact/COX_CONVEX_ORDER.md).

Equality. If c^2 = 1 then (2) is an equality; since the integrand S(t) - exp(-lambda* t) is
nonnegative and continuous, it vanishes identically, so (1) is an equality for every t, and
Jensen's equality case (exp is strictly convex) makes Lambda(0,t] almost surely equal to
lambda* t for every t. Then Lambda = lambda* Leb a.s. (the two measures agree on all rational
intervals), and N is Poisson. Conversely Poisson has c^2 = 1.

For an MMPP with modulating generator Q, stationary law pi and rates lambda_i, the directing
measure is Lambda(0,t] = integral_0^t lambda(X_s) ds, so E Lambda(0,t] = t sum_i pi_i lambda_i
= lambda* t, and (1) reads pi e^{(Q-D)t} 1 >= exp(-lambda* t). Equality forces lambda(X_s)
constant a.s.; irreducibility gives pi_i > 0 for every i, so all lambda_i are equal. That is the
second belief of the 2018 note.

## Why this was open

The reduction (3) was known to the authors (their Lemma 2.1 and equation (13):
c^2 >= 1 iff pi C 1 . pi C^{-1} 1 >= 1). Every attempt then stayed inside the matrix
identity, where the non-reversible modulating chain makes the deviation matrix non-symmetric
and the quadratic form has no sign a priori. The Cox representation is used in the source only
for the overdispersion of counts (their Proposition 3.1), never for the inter-event time. The
step nobody took is that the time-stationary void probability is the expectation of a convex
function of the directing measure. No reversibility, no spectral argument, no matrix inversion
is needed; the inequality is one line once the object is written that way.

## What the argument does not give

Conjecture 4.2 (T^pi >=_st T^alpha) does not follow. Jensen gives P(T^pi > t) >= exp(-lambda* t),
but T^alpha, having c^2 >= 1 with the same mean, generally has a heavier tail than Exp(lambda*),
so exp(-lambda* t) does not dominate P(T^alpha > t). The order (IV) would need a comparison of the
two initial phase laws pi and alpha under the same convex functional, which is a different
question.

A natural strengthening is false. One might hope log S is convex (T^pi has decreasing hazard),
which would give (1) with room to spare. It is not: on the three-state cycle with lambda =
(0.001, 140.65, 0.001) the second difference of log S reaches -0.63 on a grid of step 0.05.
The survey's Figure 1 shows the analogous failure for T^alpha. The proof needs only the chord
inequality at each t, not convexity along t.

## Checks

* The matrix formula c^2 + 1 = 2 (pi C 1)(pi C^{-1} 1) of the source's equation (6) and the form
  c^2 = 2 lambda* E[T^pi] - 1 used here agree to 1.1e-13 on 600 random MMPPs of orders 2 to 8,
  a third of them one-directional cycles (the maximally non-reversible case) and a third with a
  single hot state (`e0077d.py`).
* On the same 600 instances the bound (1), pi e^{(Q-D)t} 1 >= exp(-lambda* t), holds at every
  grid point t in (0, 30] where the survival is representable in double precision, with no
  violation at any tolerance.
* Earlier in the campaign: 240,000 random MMPPs, minimum c^2 exactly 1.00000000, and the
  reduction to Cov_pi(lambda, h) <= 0 confirmed sign-for-sign on 140,000 (memory
  `mmpp_c_squared_conjecture_reduced_to_negative_correlation_2026_09_08`). That reduction is
  the same statement as (2): h = (D-Q)^{-1} 1 is the vector of mean waits and pi h = E[T^pi].

## Lean

`Prob1000/E0077.lean` in the campaign's Lean tree (Lean 4.33.1, Mathlib as pinned by
formal-conjectures) proves: the Jensen step exp(-E Lambda) <= E exp(-Lambda) on an arbitrary
probability space (`void_prob_ge`, from Mathlib's `ConvexOn.map_integral_le`); the integral
comparison 1/r <= integral_0^infinity f whenever f >= exp(-r t) (`integral_ge_inv`); the
algebraic step from Palm inversion to c^2 >= 1 (`scv_ge_one`); their assembly into the
Cox-process theorem with the representation facts as hypotheses (`cox_scv_ge_one`); and, for the
MMPP form, the identity pi D (D-Q)^{-1} = pi from pi Q = 0 and the resulting
c^2 = 2 lambda* pi (D-Q)^{-1} 1 - 1 (`vecMul_D_A`, `mmpp_scv_formula`). Axioms:
`propext`, `Classical.choice`, `Quot.sound` only; no `sorry`. The Cox conditioning identity,
stationarity of the directing measure, and the Palm inversion formula are hypotheses of the
assembly theorem, not formalised; they are standard (Daley and Vere-Jones vol. II; Kingman,
*Poisson Processes*, Chapter 6).

## Prior art

Checked 2026-09-08: the source and its withdrawn predecessor, a web search for later proofs
(none found; the E-ledger intake search on the same day found none), and the fact that the
overdispersion of counts for Cox processes is classical (Kingman Ch. 6) while the inter-event
statement is what the source calls open. The inequality (1) itself, void probabilities of a Cox
process dominating those of the Poisson process with the same mean measure, is elementary and
may well appear in the Cox-process literature under another name; what appears not to have been
done is to combine it with the Palm inversion to answer the c^2 question. A citation search in
Grandell, *Doubly Stochastic Poisson Processes*, and in Daley and Vere-Jones for the void
probability inequality is the remaining step before calling this new rather than folklore made
explicit.
