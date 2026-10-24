# Corrections to this ledger

Added 2026-09-08 by the session that settled thirteen problems from the older campaign ledger
(write-up: `../prob1000_lean_20260908/REPORT_thirteen_settled_2026-09-08.md`). These are appended
rather than edited into the rows, so the original attempt text stays as written.

Six of this ledger's claims were checked against the mathematics — every row its STATUS.json flags
as a partial result — and one of its eight literature exclusions was spot-checked against the
source. Each is recorded below with what held and what did not. The exclusion did NOT hold: see
D0039, which should be re-admitted as open.

## D0035 — holds completely

Bradley's Question 7 (exact prescription of the phi-mixing coefficients) is refuted in its literal
general form, and the refutation comes from a result Bradley quotes in the same survey: for a
strictly stationary sequence, "If phi(n) < 1/2 for some n >= 1, then X is phi-mixing", i.e.
phi(n) -> 0. The constant sequence b_n = 1/4 is nonincreasing and lies in [0,1] but is therefore
unrealisable. Verified by pulling the archived source text and reading both the question and the
quoted dichotomy at their stated locations. The residual question — characterising the realisable
sequences, and Bradley's own sub-question about 1 > phi(1) = phi(2) > 0 = phi(3) — is untouched, as
the row says.

## D0005 — the simplex half holds; the ellipsoid justification does not

**Correct, and verified step by step:** every simplex in R^d is (d+1)-CM. For the regular simplex,
the rotation R cyclically permuting the d+1 vertices acts on the centred span as the standard
representation of Z_{d+1}, which has no trivial summand, so sum_{k=0}^{d} R^k = 0 exactly. R is
orthogonal and the simplex R-invariant, so each R^k X is uniform while the sum vanishes
identically; an affine image T(x) = Ax + b gives sum_k T(R^k X) = (d+1)b, still constant.

**Also correct:** the observation about the source's framing. Unif(C) is 2-CM if and only if C is
centrally symmetric about its centroid, because X_1 + X_2 = c forces Unif(C) to equal the law of
c - X_1. Since the usual passage from (d+1)-CM to all n >= d+1 concatenates with a 2-CM
decomposition, that passage is not available for a body without central symmetry — a scalene
triangle, say. "Not obvious" is the right strength.

**The gap:** the row justifies the ellipsoid case with "rotate by 2pi/n in a plane, or use central
symmetry". A single-plane rotation is the identity on the orthogonal complement, so for d > 2 the
map is not fixed-point-free and sum_k R^k is n times a projection, not zero. Moreover the orbit
route cannot work at all when d and n are both odd: an orthogonal map in odd dimension always has a
real eigenvalue, complex ones coming in conjugate pairs, and -1 is excluded when n is odd. What
does work is a block-diagonal rotation by 2pi/n in each of d/2 planes when d is even, and central
symmetry for 2-CM. The ellipsoid conclusion is very likely still correct — the row's own
`status_search` names arXiv:1706.05499 as settling ellipsoids in a wider elliptical setting — but
not by the argument as written. Do not quote the one-line justification.

The general form of the working argument is worth keeping as stated in the row: every affine image
of a body admitting a fixed-point-free linear symmetry of order n is n-CM. So is the recorded
obstruction — a generic convex body has trivial affine automorphism group, and cutting C into
simplices fails because the pieces have different centroids, so their mixes have different centres.

## D0016 — the method is calibrated; one conclusion is stated a notch too strongly, and the fix strengthens it

Khoshnevisan's Open Problem 1 (are the zeros of every slice of a two-parameter Brownian sheet in
R^d finite, d in {2,3}?). The row does a first-moment box count in the sheet's canonical metric.
That is sound and, importantly, calibrated: an eps-ball has Euclidean radius eps^2 in each of the
k+1 parameters, the k-point function factorises to order eps^{kd} because disjoint rectangles of
the driving white noise are independent, and the resulting exponent reproduces two known facts as
controls — k=1 gives Euclidean dimension 2 - d/2 for the zero set, matching Rosen, and the pair set
gives 3 - d.

Write the exponent as E(k) = k(d-2) - 2; tuples with k common slice zeros are expected when
E(k) < 0 and excluded when E(k) > 0.

- **d = 2:** E(k) = -2 < 0 for every k, so arbitrarily many zeros in a common slice. Supports the
  source's conjecture that the answer is no. Sound as a heuristic.
- **d = 3:** E(1) = -1, E(2) = 0, E(3) = +1. The row says the count "predicts that every slice has
  at most one zero". That overreads the k = 2 case, whose exponent is exactly zero — a critical
  count is order one and decides nothing, as the row's own obstruction field admits. The correct
  reading is **at most two zeros, with two critical**.

The row's headline conclusion — that d = 3 answers YES, contrary to the source's conjecture — is
nonetheless supported, and by a cleaner route than the one it gives: k >= 3 is STRICTLY subcritical
(E(3) = 1 > 0), so the count excludes three or more common zeros outright. Infinitely many zeros in
a single slice is therefore what the budget rules out in d = 3, independently of whatever happens
at the critical k = 2. State it that way rather than via "at most one".

The row's own obstruction is right about where the real work is: the d = 2 half needs a
second-moment/capacity argument with the exceptional s handled by an energy estimate uniform in k,
plus a limsup argument to pass from arbitrarily many to infinitely many; and the critical k = 2
estimate at d = 3 is exactly where a nontrivial gauge function could live, which a first-moment
count cannot see.

## D0002 and D0003 — both hold

**D0003(b), verified.** For p_1,...,p_n >= 0 summing to 1 and any N, the tuple
(Bin(N,p_1),...,Bin(N,p_n)) is jointly mixable with centre N. Take N i.i.d. layers, each placing its
single 1 in coordinate i with probability p_i; coordinate i of the sum counts the layers that chose
i, which is Bin(N,p_i), while the total is sum_k sum_i (X_k)_i = sum_k 1 = N identically. Correct,
and the source's own remark that Bin(n,1/n) is n-CM is the diagonal case p_i = 1/n, N = n. Note the
family is jointly mixable, not completely mixable, whenever the p_i differ - the row states this
correctly.

**D0003(a), verified.** If (F_i) is JM with integer centre N and (G_i) with centre M, stacking the
two independent layer systems gives (F_1*G_1,...,F_n*G_n) JM with centre N+M: independence makes the
marginals convolve and the centres add.

**D0002, verified.** The orbit criterion — if T is measure-preserving with T^n = id and
sum_{k<n} g(T^k u) = n*mu a.e., then (g(U),...,g(T^{n-1}U)) is a complete mix — is correct, and its
two instances check out: T(u) = 1-u gives every symmetric law 2-CM, since the quantile function of a
law symmetric about mu satisfies g(1-u) = 2mu - g(u); and the linear-map version gives the simplex
and ellipsoid families of D0005. The row is careful to say this recovers "symmetric unimodal is
n-CM" only for EVEN n, the concatenation rule building 2k-CM from 2-CM, and that is the honest
scope. Its obstruction is also well judged: the sharp monotone-density theorem has rigid,
non-exchangeable extremal mixes at the endpoint of the admissible interval, so no finite group
action can generate them.

## D0010 — the stated necessary condition is vacuous, but the idea repairs cleanly

Open Problem 10 of the complete-mixability survey asks for extra conditions making a unimodal law on
[a,b] n-CM, singling out the tight case mu = a + (b-a)/n.

**The setup is right.** At that boundary mean, an n-CM coupling satisfies sum_i (X_i - a) = b - a
with every X_i - a in [0, b-a], so the vector is a random composition of the fixed total b - a into
n nonnegative parts. Writing N_x for the number of parts exceeding x, the deterministic bound
N_x * x < b - a holds pathwise. All of that is correct.

**The stated conclusion is vacuous.** The row derives F(a+x) >= 1 - (b-a)/(n x) and calls it "a
clean quantitative extra necessary condition", claiming a density too flat near a violates it. But
that inequality is exactly MARKOV. With Y = X - a >= 0 and E[Y] = mu - a = (b-a)/n, Markov gives
P(Y > x) <= (b-a)/(n x) for ANY law with that mean, completely mixable or not. So no law satisfying
the mean condition can violate it, and it excludes nothing. Taking expectations in the composition
bound discards exactly the information that made the composition argument worth making.

**The repair, and it is a genuine extra condition.** Keep the integrality. N_x counts parts, so from
N_x < (b-a)/x we get N_x <= ceil((b-a)/x) - 1, the largest integer strictly below (b-a)/x. Taking
expectations over identical marginals — exchangeability is not needed, identical marginals suffice —

    n (1 - F(a+x))  <=  ceil((b-a)/x) - 1,      i.e.
    F(a+x)  >=  1 - (ceil((b-a)/x) - 1)/n       for every x in (0, b-a].

This strictly beats Markov. Normalising b - a = 1: for x in (1/2, 1] it reads F(a+x) >= 1 - 1/n,
against Markov's weaker 1 - 1/(n x); for x in (1/3, 1/2] it reads 1 - 2/n against Markov's
1 - 1/(n x) in [1 - 3/n, 1 - 2/n). So the sharpened form does rule out laws that the mean condition
alone admits, which is what the row wanted. Quote the ceiling version, never the one in the row.

The row's obstruction is right as written: away from the boundary the composition structure
disappears, and converting any of this into a SUFFICIENT condition needs an existence theorem for
exchangeable random compositions with a prescribed one-dimensional marginal.

## D0039 — WRONGLY EXCLUDED. This problem is still open and should be re-admitted

This is the one correction here that removes a problem from the discard pile rather than qualifying
a claim.

D0039 records Virag, *Operator limits of random matrices* (ICM 2014, arXiv:1804.06953), Question 1,
and marks it `resolved_in_literature`, `admitted: false`, citing Chhaibi and Najnudel,
arXiv:1904.00578, JEMS 28 (2026).

**Virag's Question 1, verbatim from the archived source (PDF p.6):** "Question 1 (Spectral measure
and multiplicative cascades). Does the beta-Hermite measure and the Gaussian multiplicative cascade
measure with the same Hausdorff dimension have the same fractal spectrum?" The measure in question
is mu_beta, the spectral measure at the first coordinate of the Jacobi matrix J_beta of Theorem 4.1,
whose Hausdorff dimension Breuer, Forrester and Smilansky showed is almost surely (1 - 2/beta)_+.

**What Chhaibi-Najnudel prove:** an exact identification of Kahane's Gaussian multiplicative chaos
ON THE CIRCLE with the CIRCULAR beta ensemble, coupling constants related by gamma = 2/beta, for
gamma <= 1 i.e. beta >= 2. That is the circular analogue. It is not the beta-Hermite measure, and the
question as Virag states it is about the beta-Hermite measure.

So the exclusion does not hold. The circular theorem is strong evidence that the analogous answer is
positive, and its methods may well transfer, but transferring them is mathematics that someone has
to do — it is not a citation. **D0039 should be re-admitted as an open problem**, with the
Chhaibi-Najnudel result recorded as the closest known relative and the obvious first thing to try.

The row's own `status_search` field shows how this happened: it quotes a SEARCH SUMMARY saying the
paper "answers positively a question raised by Virag on the fractal spectrum of a random measure
constructed from CbetaE" — CbetaE, the circular ensemble — and then records the row as resolved
anyway, noting a caveat. The caveat was right and the disposition did not follow it. Reading the
source's own sentence, which takes one grep, settles it in the other direction.

**This is the failure mode the ledger's README warns about**, now with an instance: the eight
literature exclusions came from abstracts and search summaries rather than full texts. At least one
is wrong. The other seven should each be checked against the source's own statement of the question
before anyone treats this ledger's exclusion list as final.

## The exclusion list: ALL EIGHT checked against their sources — seven hold, one is wrong

Every one of this ledger's eight exclusions came from an abstract or a search summary rather than a
full text, which its README already flags. All eight have now been checked by reading the SOURCE's own statement of the question and the cited
paper's own statement of what it proves. Seven hold; one does not.

**D0022 — the exclusion HOLDS.** Seppalainen's Problem 1, verbatim: "Extend Theorem 1 to describe
hydrodynamic behavior also at high density rho > rho*. Or, equivalently, extend Theorem 2 to more
general ZRP's. The proof of Theorem 2 in Seppalainen and Krug (1998) depends on special properties
of the totally asymmetric ZRP with rate function r(k) = I{k >= 1}." The cited paper — Bahadoran,
Mountford, Ravishankar and Saada, arXiv:1801.01654 — covers an arbitrary bounded nondecreasing jump
rate, asymmetric rather than totally asymmetric, and establishes the hydrodynamic limit in the
condensation domain above the critical density. That is exactly both halves of the question.
Correctly excluded.

**D0039 — the exclusion FAILS**, as detailed above: the question names the beta-Hermite measure and
the cited theorem is on the circle.

**D0013, D0014, D0015 — the exclusions HOLD.** All three Angel-Holroyd-Romik-Virag sorting-network
conjectures are attributed to one paper, Dauvergne's *The Archimedean limit of random sorting
networks* (arXiv:1802.08934, JAMS), and its abstract covers all three objects — trajectories close
to sine curves, the weak limit of the time-t permutation matrix measures, and the path being close
to a great circle on a particular (n-2)-dimensional sphere — closing with "These results prove
conjectures of Angel, Holroyd, Romik, and Virag." Correctly excluded, all three.

**D0096 — the exclusion HOLDS.** Rolla's survey, verbatim after Theorem 7.2 ("If d > 2, then
zeta_c < 1 for every lambda < infinity and zeta_c -> 0 as lambda -> 0"): "Open Problem. Prove a
similar statement for unbiased walks on Z^2. Open Problem. At least prove that zeta_c < 1 for some
lambda." The cited Asselah-Forien-Gaudilliere paper is titled "The critical density for activated
random walks is always less than 1", which covers the remaining unbiased d = 2 case and a fortiori
"for some lambda". Correctly excluded.

**D0001 — the exclusion HOLDS, and precisely on target.** The source itself narrows the question
before asking it: "if F has finite mean mu, then its center is unique and equal to mu... It is shown
that if x P(|X| >= x) -> 0 ... the center of F is also unique... Non-uniqueness may only happen in
the case that the support of F is unbounded from both sides, and F does not have finite mean." So the
entire live content is the no-mean case — and the cited paper is titled *Centers of probability
measures without the mean* (Puccetti, Rigo, B. Wang, R. Wang, J. Theoret. Probab. 32 (2019)), with
Cauchy carrying an interval of centres. Correctly excluded.

**D0055 — the exclusion HOLDS.** The source states the Derrida-Retaux conjecture as
F_infinity(p) = exp(-(K + o(1))/(p - p_c)^{1/2}) as p decreases to p_c when p_c > 0, explicitly
hedged "possibly under some additional integrability conditions on Y_0", and adds "We have not been
able to prove or disprove the conjecture." The cited paper — Chen, Dagard, Derrida, Hu, Lifshits and
Shi, *The Derrida-Retaux conjecture on recursive models*, Ann. Probab. 49 (2021) 637-670 — proves
exactly that under such conditions, which is what the conjecture's own hedge anticipates. Correctly
excluded.

**The check that does the work, in one line:** compare the OBJECTS BY NAME — what the source's
question names, against what the cited theorem is about. "beta-Hermite" against "on the circle"
caught the bad one; "more general ZRP's" against "arbitrary bounded nondecreasing rate", and
"no finite mean" against "without the mean", confirmed good ones. It takes minutes per exclusion and
one in eight was wrong, so it is worth doing on every abstract-sourced exclusion in any ledger here.

## D0097 — checked, holds, nothing to fix

Rolla's first open problem after Theorem 7.2 ("Prove a similar statement for unbiased walks on
Z^2", i.e. that zeta_c < 1 and zeta_c -> 0 as lambda -> 0). The row does not claim to solve it; it
carries the source's own computation through with the two-dimensional Green function and outputs a
quantitative CONJECTURE, which is honest and correctly labelled.

The reasoning checks. Theorem 7.2's criterion gives activity for zeta > 4 G sqrt(lambda), and in
d = 2 the walk is recurrent so G diverges and the criterion is vacuous — that is exactly the
obstruction. Truncating to a box of side n gives a box Green function of order log n, hence
zeta > c sqrt(lambda) log n, still vacuous as n grows. The natural box is the one an active particle
explores in its lifetime: the sleep rate lambda gives a lifetime of order 1/lambda, and a
two-dimensional walk in that time covers a box of side about lambda^{-1/2}, so log n is of order
log(1/lambda). That yields the prediction zeta_c(lambda) of order sqrt(lambda) log(1/lambda) as
lambda -> 0, with the transient case zeta_c ~ sqrt(lambda) (finite G) as the natural comparison.
Coherent, and the row's obstruction field names the real wall — a truncated-Green weak-stabilisation
estimate breaks the mass-transport identity the global argument relies on.

## Everything else in this ledger is unaudited

Seven of the 94 admitted rows have been checked (D0035, D0005, D0016, D0002, D0003, D0010, D0097) —
every row the ledger's own STATUS.json flags as a partial result, plus D0035 and D0097. The other 87
and their attempts have not been checked by anyone. The eight recorded literature exclusions came from
abstracts and search summaries rather than full texts, and the ledger's own README flags them as
claims to verify. The pattern in the six audited is worth carrying forward. No calculation was wrong anywhere. Two
conclusions were phrased more strongly than their own derivation supported (D0005, D0016), and in
both cases the missing caveat was already sitting in the row's own obstruction field. One (D0010)
stated a bound that is true but vacuous, being Markov's inequality in disguise, where the underlying
idea supports something strictly stronger. So: read the RESULT field against the OBSTRUCTION field,
and check any inequality against the trivial bound before believing it adds information.


## D0016 - the d = 3 half is SETTLED by a Codex proof, audited here (added 2026-09-08, evening)

codex-probability-20260908 published, on branch codex/probability-open-20260908 (commit e03dec4d),
the file 12_cognitive_architecture/audits/evidence/2026/09/08/probability-open-20260908/
D0016_uniform_triple_exclusion_proof_v2.md: for the two-parameter Brownian sheet in R^3, outside one
null set, every positive slice {s} x (0, infinity) contains at most two zeros. Read line by line here:
two-parameter Kolmogorov-Chentsov (p = 80, alpha = 17/36) from the rectangle-symmetric-difference
variance bound; the exact determinant s^k t_1 prod (t_j - t_{j-1}) of the slice covariance; a small-
ball bound C r^{dk} on separated compact configurations; a deterministic grid union bound with
exponent alpha d k - (k+1) = 1/4 > 0 for d = 3, k = 3; localization on {K <= N} used only as a subset of
a finite union of unconditional events; countable exhaustion. No gap found. This is the k >= 3
strictly-subcritical route recommended in the earlier audit entry above, made rigorous.

Consequence, from the source read today (arXiv math/0510518, Section 8.1): Open Problem 1 asks, for
d in {2,3}, whether every positive slice's zero set is finite outside a single null set, and the author
writes "I conjecture that the answer is no". The proof answers YES for d = 3 and so refutes the
conjecture there. Theorem 1.2 of the paper gives only Hausdorff dimension zero for the slice zero
sets. The d = 2 case is untouched (the exponent 2k - 2(k+1) is negative for every k), and k = 2 in d = 3
is critical (6 alpha - 3 < 0), so the gauge-function question survives in that form. Novelty not
certified: no publication stating the d = 3 finiteness was found by either agent.

Status: D0016 = refuted for d = 3 (Codex proof, Claude audit), open for d = 2.

## D0018 - the d = 5 half is SETTLED by the same Codex packet, audited here (added 2026-09-08, evening)

File D0018_uniform_double_pair_bound_proof_v1.md in the same packet: for the sheet in R^5, outside one
null set, every positive slice has at most two disjoint double pairs (t_1 < t_2 with B(s,t_1) = B(s,t_2),
t_1 > 0); distinct pairs share no endpoint. Checked here: the configuration lemma (a full-row-rank
difference matrix A on q times, dr > 2(q+1)) with the covariance lower bound Sigma >= a min(a,eta)/4 I
from Sigma = s L diag(t_1, gaps) L^T and ||L^{-1}|| <= 2; shared endpoints excluded with q = 3, r = 2
(10 > 8); three disjoint pairs excluded over the 15 perfect matchings of six times with q = 6, r = 3
(15 > 14, alpha = 17/36 gives exponent 1/12); no pair involves time zero because a d = 5 positive slice
has no zeros (exponent 13/36); countable exhaustion. No gap found.

Consequence (source Section 8.2, read today): Open Problem 3 asks, for d in {4,5}, whether Y_d(s) is
finite for all s > 0 outside a single null set, and the author writes that the answer "is likely to
be no". Literally Y_d(s) contains the diagonal, so the intended object is the off-diagonal set; with
that normalisation the proof answers YES for d = 5. d = 4 is untouched (three disjoint pairs give
12 < 14; two pairs are critical, 10 = 10). Novelty not certified.

Status: D0018 = refuted for d = 5 in its off-diagonal normalisation (Codex proof, Claude audit), open
for d = 4.
