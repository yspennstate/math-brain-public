# F0066 - Janson, Conjecture 20.6 (arXiv v1) = Conjecture 21.6 (Probab. Surveys 2012)

Status: literature_resolved. The conjecture was proved in 2022 by Addario-Berry,
Brandenberger, Hamdan and Kerriou, and a second, independent proof follows from
Addario-Berry and Donderwinkel (2022/2024) by an elementary pigeonhole step. Nothing
here is new; this memo records the statement, the two published routes, what I
checked, and a small simulation that agrees with them.

## 1. The problem as the source states it

Janson, "Simply generated trees, conditioned Galton-Watson trees, random allocations
and condensation", arXiv 1112.0510 v1, Section 20.3, PDF page 136 (verbatim from the
extracted text; the published version, Probab. Surveys 9 (2012) 103-252, has one more
section and numbers the same items 21.5-21.8):

> (Recall that if T is a rooted tree, then the height H(T) := max{k : l_k(T) > 0},
> the maximum distance from the root, and the width W(T) := max_k{l_k(T)}, the
> largest size of a generation.) [...]
> In the case nu >= 1, sigma^2 < infinity [...] H(T_n)/sqrt n ->_d 2 sigma^{-1} X (20.10),
> W(T_n)/sqrt n ->_d sigma X (20.11), where X is [...] the maximum of a standard
> Brownian excursion [...]
> Nevertheless, we conjecture that (20.10) and (20.11) extend formally at least to the
> case nu = 1 and sigma^2 = infinity:
>
> Conjecture 20.5. If nu = 1 and sigma^2 = infinity, then H(T_n)/sqrt n ->_p 0.
>
> Conjecture 20.6. If nu = 1 and sigma^2 = infinity, then W(T_n)/sqrt n ->_p infinity.
>
> Problem 20.7. Does nu < 1 imply that H(T_n)/sqrt n ->_p 0?
> Problem 20.8. Does nu < 1 imply that W(T_n)/sqrt n ->_p infinity?

Here T_n is the simply generated tree of size n for a weight sequence w = (w_k) with
w_0 > 0 and w_k > 0 for some k >= 2; Phi(t) = sum w_k t^k with radius rho; Psi(t) =
t Phi'(t)/Phi(t); nu = Psi(rho); when nu >= 1 the offspring law is pi_k = w_k tau^k /
Phi(tau) with Psi(tau) = 1 (tau = rho when nu = 1), and sigma^2 = Var(xi) = tau Psi'(tau)
(Janson's Theorem 7.1). The ledger row quotes the statement correctly, with the right
direction ("-> infinity") and the right hypotheses (nu = 1, sigma^2 = infinity). The
ledger's numbering (20.6) is the arXiv v1 numbering; I confirmed by extracting the
published PDF (Janson's sj264.pdf) that its "Conjecture 21.6" has the identical text.

## 2. Finding

Conjecture 20.6 is a theorem. Two published routes:

Route A (direct, the one the integrator's hint pointed at). Addario-Berry, Brandenberger,
Hamdan, Kerriou, "Universal height and width bounds for random trees", Electron. J.
Probab. 27 (2022), paper 118, 1-24, doi:10.1214/22-EJP842 (arXiv 2105.03195). Their
Section 5 restates Janson's four items as "Conjecture 1 ([13])" with points (1)-(4) =
21.5, 21.6, 21.7, 21.8, in the full simply-generated generality (weight sequence w with
w_0 > 0 and some w_k > 0, k >= 2; sigma^2 = rho Psi'(rho)), and states after Corollary 5.3:

> "Corollary 5.3 implies that if nu < 1, or if nu = 1 and sigma^2 = infinity, then
> ht(T_n)/(n^{1/2} log^3 n) -> 0 and wid(T_n)/n^{1/2} -> infinity in probability. This
> proves the second and fourth points of the above conjecture and nearly proves the first
> and third points, up to the polylogarithmic factors."

The abstract says the same: "Our results allow us to prove a conjecture and settle an open
problem of Janson [13], and nearly prove another conjecture and settle another open
problem from the same work (up to a polylogarithmic factor)." The proved conjecture is
21.6 = our 20.6; the settled problem is 21.8; the "nearly" ones are 21.5 and 21.7.

Route B (through the height). Addario-Berry, Donderwinkel, "Random trees have height
O(sqrt n)", arXiv 2201.11773 (v3, March 2024; the PDF says "Submitted to the Annals of
Probability"; the arXiv page carries no journal-ref field, so I cite the arXiv version).
Their Theorem 19: "Let w = (w_k, k >= 0) be a weight sequence with w_0 > 0 and with
w_k > 0 for some k >= 2. If either sigma-hat^2 = infinity or nu < 1 then n^{-1/2} ht(T_{w,n})
-> 0, where the convergence is in both probability and expectation", with sigma-hat^2 =
tau Psi'(tau), tau = rho when nu <= 1, i.e. exactly Janson's sigma^2. The paper says "The
following theorem resolves Conjecture 21.5 and Problem 21.7 from [30]." Combined with the
deterministic inequality n <= (H(T_n)+1) W(T_n) (the n vertices lie on H+1 levels of size at
most W), H = o_p(sqrt n) gives W >= n/(H+1) >> sqrt n in probability, which is 20.6 again.
This is the reduction already recorded in attempt F0066-A001; what that attempt lacked was
the knowledge that 20.5 is now a theorem.

## 3. The argument of Route A, as I read it

I read the proof chain in the ABHK paper rather than the abstract alone. It has four steps.

(a) Conditionally on its degree statistics n = (n(c))_c (n(c) = number of vertices with c
children), a simply generated tree is uniform on the plane trees with those statistics,
because the weight prod_v w_{d(v)} depends only on n. So everything reduces to uniform
random trees with fixed degree statistics, plus control of the statistics themselves.

(b) Theorem 1.1 (the paper's core; Proposition 2.1 + Theorem 2.2): for a uniform (tree,
uniform node) pair (T, V) with degree statistics n, writing |n|_1 = sum c n(c) = n - 1 and
|n|_2^2 = sum c^2 n(c), for all beta > 17^{3/2},

  P( |V| > beta |n|_1 / (|n|_2^2 - n(1))^{1/2} )
     <= exp(-(beta^{1/3}/3) |n|_1/(|n|_2^2 - n(1))^{1/2}) + 2 exp(-beta^{2/3}/24).

The mechanism is the size-biased / ladder criterion the integrator's hint mentioned: the
degrees along the path from the root to a uniform node V are a random truncation of a
size-biased ordering D_1, D_2, ... of the multiset of degrees (Proposition 2.1: |V| has
the law of M - 1 where M = min{i : U_i <= (1 + sum_{j<i}(D_j - 1))/(n + 1 - i)}), and the
size-biased order front-loads large degrees, so sum_{j<i}(D_j - 1) grows at least like
i |n|_2^2/|n|_1 early on, which stops the path within order |n|_1/|n|_2 steps. (The paper
notes Marzouk, Proposition 5, strengthens this bound up to constants.)

(c) Corollary 5.3: if nu = 1 and sigma^2 = infinity then for every C > 0, with very high
probability |n_{T_n}|_2^2 >= C |n_{T_n}|_1. Proof: by Janson's Theorem 11.4 (their Theorem
5.1), n_{T_n}(k)/n -> pi(k) in probability for each fixed k, with exponentially small error
probabilities; since sum_k k^2 pi(k) = infinity, pick K with sum_{k<=K} k^2 pi(k) >= 2C, and
then sum_{k<=K} k^2 n_{T_n}(k)/n >= C with very high probability. (The nu < 1 case uses
instead that the mass above any fixed K is at least (1 - nu) n and hence contributes at
least K (1 - nu) n to |n|_2^2.)

(d) Width (proof of Theorem 1.2, page 8): by (b) and (c), for every eps > 0,
P(|V_n| >= eps n^{1/2}) <= eps for large n. Since V_n is uniform on the vertices,
P(|V_n| >= eps n^{1/2}) >= (1/2) P(#{u : |u| >= eps n^{1/2}} >= n/2), so with probability
at least 1 - 2 eps more than n/2 vertices sit in the first eps n^{1/2} levels, whence
wid(T_n) >= n^{1/2}/(2 eps). As eps is arbitrary, wid(T_n)/n^{1/2} -> infinity in
probability (and in expectation, by the moment version of the same bound).

Every step (a), (c), (d) is elementary and I checked it; (b) is the substance of a
peer-reviewed EJP paper, corroborated independently by Marzouk's Proposition 5 and by
Route B (a different method, the Foata-Fuchs line-breaking construction).

## 4. What is not done

Nothing on the conjecture itself remains. Two things for the campaign's records: the
height conjecture 20.5 was proved in full by Route B (Theorem 19), so it is also closed,
and the ledger row F0065 should be marked literature_resolved with that citation; Janson's
Problem 20.10 (growth rates of E H(T_n), E W(T_n) when sigma^2 = infinity or nu < 1) is
only bounded, not determined, in this generality - the sharp answers depend on the tail
(stable domain: n^{1-1/alpha} and n^{1/alpha}; Cauchy domain with condensation:
Kortchemski-Richier 2019, Addario-Berry-Donderwinkel-Kortchemski 2025).

The integrator's hint "max degree >> sqrt n when sigma^2 infinite" is not true in
general, and the proof does not use it: for a critical law with P(xi > x) ~ 1/(x^2 log x)
the variance is infinite but n P(xi > eps sqrt n) -> 0, so the largest of n i.i.d.
degrees is o(sqrt n). What is true, and what the proof uses, is the weaker
|n_{T_n}|_2^2 / n -> infinity (the empirical second moment of the degrees, not the
maximum). The equivalence "20.6 <=> 20.5 up to a log" from attempt A001 stands, but is
no longer needed.

## 5. Checks

1. Numbering and statement: extracted both the arXiv v1 PDF (source of the ledger) and
   the published PDF from Janson's page; the texts of 20.6 and 21.6 are identical.
2. Generality: ABHK's Conjecture 1 (2) is stated for weight sequences, with sigma^2 =
   rho Psi'(rho) for nu <= 1, matching Janson's Theorem 7.1 (sigma^2 = tau Psi'(tau),
   tau = rho when nu = 1); AD's sigma-hat^2 is the same quantity (their (3.1)-(3.2)).
   So neither paper proves only the Bienayme special case; both cover Janson's setting.
3. Independent simulation (sim_width_check.py, outputs sim_width_check_part1.out and
   _part2.out): size-conditioned critical trees sampled directly by the cycle lemma
   (Lukasiewicz walk + rotation at the minimum), 8-24 trees per size.
   - geometric (sigma^2 = 2): median W/sqrt n = 1.49, 1.76, 1.52 at n = 1000, 4000,
     16000; flat, consistent with the finite-variance limit (E W/sqrt n -> sigma sqrt(pi/2)
     = 1.77); |n|_2^2/n = 3.0 = E xi^2, flat.
   - p_k ~ k^{-5/2} (alpha = 3/2 stable domain): median W/sqrt n = 3.43, 4.26, 6.09 at
     n = 1000, 4000, 12000, growing; |n|_2^2/n = 11.8, 15.4, 24.3, growing.
     Second, independent check of the same numbers: the stable-tree scaling
     (Duquesne 2003) predicts W ~ n^{2/3}, i.e. W/sqrt n ~ n^{1/6} (ratio 12^{1/6} = 1.51
     between the end sizes; observed 1.78 with 8 trees at the top size, same direction,
     within the noise of the medians), and |n|_2^2/n ~ n^{2/alpha - 1} = n^{1/3}
     (predicted ratio 2.29, observed 2.05).
   - p_k ~ k^{-3} (variance infinite only logarithmically): median W/sqrt n = 1.42, 1.57,
     2.05 at n = 1000, 4000, 12000, growing slowly; |n|_2^2/n = 2.76, 3.11, 3.31, growing
     like log n as the truncated second moment should. This is the hard end of the
     conjecture (max degree is o(sqrt n) here: observed maxdeg/sqrt n = 0.65, 0.67, 0.63,
     flat) and the width still grows, exactly as the theorem says it must.
4. Lean: U_F0066.lean certifies the pigeonhole step of Route B, n <= (H+1) W and
   n/(H+1) <= W, for level counts l : Fin (H+1) -> N bounded by W and summing to n.
   Compiled clean on the first attempt; axioms: propext, Classical.choice, Quot.sound.

## 6. The strongest case that this is wrong

The way this report could be wrong is if the ABHK "Conjecture 21.6" were a different
statement from the ledger's 20.6 (a renumbering trap), or if their theorem covered only
Bienayme trees while Janson's conjecture is about simply generated trees. Both were
checked directly: the published text of 21.6 is word for word the arXiv 20.6, and ABHK's
Section 5 explicitly moves from Bienayme trees to weight sequences via Janson's Theorem
11.4 and proves the point "(2) If nu = 1 and sigma^2 = infinity then wid(T_n)/n^{1/2} ->
infinity in probability" in that generality. The residual risk is an error inside ABHK's
Theorem 1.1, which I did not re-derive; that risk is small because the width conclusion
also follows from the independent Addario-Berry-Donderwinkel height theorem plus the
Lean-certified pigeonhole, and the simulation at the logarithmic-variance edge agrees.

## 7. Prior art (search record)

Searches run 2026-09-09: "Janson conjecture width conditioned Galton-Watson infinite
variance sqrt n"; "Critical trees are neither too short nor too fat Addario-Berry
Donderwinkel Kortchemski Janson conjecture"; "Conjecture 20.6 OR Conjecture 20.5 Janson
simply generated trees height width"; "Most trees are short and fat Addario-Berry width
lower bound infinite variance Janson conjecture". The phrase that found it: "Conjecture
20.6" OR "Conjecture 20.5" Janson simply generated trees height width, which returned
arXiv 2105.03195 and 2201.11773 (both cite the published numbering 21.5-21.8).

- Addario-Berry, Brandenberger, Hamdan, Kerriou. Universal height and width bounds for
  random trees. Electron. J. Probab. 27 (2022), paper no. 118, 1-24. doi:10.1214/22-EJP842.
  arXiv 2105.03195. Proves 21.6 (= 20.6) and 21.8; 21.5 and 21.7 up to log^3 n.
- Addario-Berry, Donderwinkel. Random trees have height O(sqrt n). arXiv 2201.11773
  (v3, 2024), submitted to Ann. Probab. Theorem 19 proves 21.5 (= 20.5) and 21.7;
  Theorem 20 answers Problem 21.9 (sub-Gaussian height tails for every weight sequence).
- Addario-Berry. Most trees are short and fat. Probab. Theory Related Fields 175 (2019).
  H = O_p(sqrt n), W >= c sqrt n with tails, for every offspring law (the sqrt n
  bounds the conjectures say are not tight).
- Addario-Berry, Donderwinkel, Kortchemski. Critical trees are neither too short nor too
  fat. Ann. Henri Lebesgue 8 (2025) 113-149, arXiv 2311.06163. The opposite-direction
  bounds (height lower tail, width upper tail), optimal at that generality.
- Donderwinkel, Khanfir. Tight universal bounds on the height times the width of random
  trees. arXiv 2501.00458. H W = O(n log n) in probability.
- Marzouk, Proposition 5 (cited by ABHK as strengthening their Theorem 1.1 up to constants).

Files: memo.md (this), sim_width_check.py, sim_width_check_part1.out,
sim_width_check_part2.out, U_F0066.lean, prior_art_abhk_2105.03195_extracted.txt,
prior_art_ad_2201.11773_extracted.txt.
