# Formentin-Kuelske Conjecture 2.13 at q = 3: audit of the 24 Oct proof

Agent an agent, 10 Nov 2026, from 09:36 laptop clock. Status: PROVISIONAL. First audit of the analytic
chain; the certificate link (step C below) and the second audit are still owed. Nothing is posted.

Object audited: `T067_COMPLETE_PROOF.md` (313 lines) from research-repo
`research_pushes/2026-10-24-t067-completion-audit-8129eedabc36/`. Statement: for the three-state symmetric
(Potts) channel with second eigenvalue lambda in (0,1) on a Galton-Watson tree whose offspring law has finite
mean d, d lambda^2 <= 1 gives nonreconstruction almost surely, and d lambda^2 > 1 gives reconstruction almost
surely on survival. The conjecture (Formentin and Kuelske, SPA 119 (2009) 2992-3005, Conjecture 2.13, eq. (45))
asks for the strict case d lambda^2 < 1; the theorem includes equality.

## What was checked, and how

A. Sections 2 to 4 (three states), read line by line and re-derived.

1. Joint law of two conditionally independent observations: density z = q sum p_i r_i against the product of the
   marginals. Correct. The law of the posterior is invariant under S_3, so averaging a symmetric functional over
   the six relative permutations is legitimate.
2. Edge map p -> u + lambda (p - u). With x = (1/6) sum (3p_i - 1)^2, y = (1/6) sum (3p_i - 1)^3 and
   H = y - x^2/2: x scales by lambda^2, y by lambda^3, so H(edge) = lambda^3 H + (1/2) lambda^3 (1 - lambda) x^2
   >= lambda^3 H. The cone {E H >= 0} is preserved by the edge.
3. Integrating (3.4) against two laws in the cone, with G = 1 - x >= 0: E H of the product is at least
   E H G' + E G H' + E x E x'/1000 >= 0. The cone is preserved by conditional products.
4. Integrating (3.3), with F = (3/2) x - y >= x/2 >= 0 and E H >= 0: m(mu * nu) <= m(mu) + m(nu) - m(mu) m(nu)/1000.
5. A nonempty partial product of child messages has mean information at least b = lambda^2 m_n (more
   observations, convex functional). Hence E[x(p_{n+1}) | D = k] <= k b - (k-1)_+ b^2/1000 and
   m_{n+1} <= d lambda^2 m_n - c_3 m_n^2, c_3 = delta lambda^4/1000, delta = E (D-1)_+.
6. delta = d - P(D >= 1) >= d - 1 > 0 when d lambda^2 = 1 and lambda < 1. No second moment is used.
7. c_3 m_n <= 1/1000, so 1/m_{n+1} >= 1/m_n + c_3 and m_n <= 1/(1 + c_3 n) with m_0 = 1; TV <= sqrt(x/2).
8. Quenched statement: a_n(T) is nonnegative and nonincreasing in n, E a_n(T) -> 0, so a_n(T) -> 0 almost surely.

Sanity check of the size of the saving: the classical second-order expansion at q = 3 on the d-ary tree has
drift -(3/4) lambda^4 d (d-1) x^2, so a quadratic saving is the right order and 1/1000 is far inside it.

B. The two pair inequalities as stated, by exact rational sampling (not a proof).

    [z x(P)] <= x(p) + x(r) - H(p) F(r) - F(p) H(r) - x(p) x(r)/1000          (3.3)
    [z H(P)] >= H(p) G(r) + G(p) H(r) + x(p) x(r)/1000                        (3.4)

`tools/sample_pair_exact.py`, seed 20261110, 60,000 pairs in exact fractions drawn from four families (uniform
on the simplex, near the uniform point at scales 1e-1 to 1e-6, near a vertex, near an edge): no violation. The
smallest slack divided by x(p) x(r) was 0.1175 for (3.3) and 0.1241 for (3.4), so the constant 1/1000 is not
tight on the sample. A first floating-point run reported large negative numbers; they were the normalisation
dividing a rounding error of 1e-16 by 1e-300 at r exactly uniform, where both sides are equal. The exact run
replaces it.

C. The certificate for (3.3) and (3.4), checked 09:50-09:53 in two parts.

1. The reduction (`analytic/Q3_CONE_CERTIFICATE_AUDIT.md`), read and verified. Both sides are invariant under
   separate permutations of p and r, so both may be taken ordered; an ordered posterior is a convex combination
   of e = (1,0,0), v = (1/2,1/2,0), u = (1/3,1/3,1/3). With U_i = 3 p_i r_sigma(i), Z = sum U_i, V_i = 3U_i - Z,
   X = (1/6) sum V_i^2, Y = (1/6) sum V_i^3, N = YZ - X^2/2: Z x(P) = X/Z and Z H(P) = N/Z^3. Multiplying (3.3)
   by 6 prod Z_sigma and (3.4) by 6 prod Z_sigma^3 gives

       T_A = 6 D_A K_A - sum_sigma X_sigma prod_{tau != sigma} Z_tau            bidegree (10,10)
       T_B = 6 D_B K_B + sum_sigma N_sigma prod_{tau != sigma} Z_tau^3          bidegree (22,22)

   in the barycentric coordinates of the two triangles. Degrees: D_A (6,6), K_A (4,4); D_B (18,18), K_B (4,4);
   the fusion sums have bidegree (7,7) and (19,19) and are raised by (s t)^3. A polynomial with nonnegative
   monomial coefficients in nonnegative variables is nonnegative, and for strictly positive p, r every Z_sigma is
   positive, so division returns (3.3) and (3.4). On the boundary Z x(P) = X/Z and Z H(P) = N/Z^3 extend
   continuously by 0 (X <= C Z^2, |N| <= C Z^4), so the inequalities pass to the closure.
2. The coefficients, recomputed from the definitions above with a program written for this audit and sharing no
   code with the 24 Oct sources (`tools/recompute_certificates.py`, python-flint polynomials over Q, six
   variables, about 6 seconds):

       T_A: 4,356 monomials, 3,873 positive, 483 zero, 0 negative
       T_B: 76,176 monomials, 71,627 positive, 4,549 zero, 0 negative

   which are the counts of the 24 Oct record. Each polynomial was also compared with the direct Bayes-fusion
   expression at 12 exact rational points (equal). Negative control: with the constant 1/1000 replaced by 1/20,
   1/8, 1/2 the same program reports 4, 14, 995 negative coefficients in T_A and 91, 482, 13,689 in T_B, so the
   sign count does respond to the inequality being tested. (Coefficient positivity is sufficient, not necessary:
   the sampled slack in B suggests the true constant is larger than 1/20.)

D. Section 5 (four states), read and re-derived given the imported inequality
   E_{mu * nu} A <= a + b - a b (a + b)/1000 on the OpenAI cone: each further merge saves at least 2 b^3/1000,
   M_{n+1} <= d lambda^2 M_n - c_4 M_n^3 with c_4 = delta lambda^6/500, 1/M_{n+1}^2 >= 1/M_n^2 + 2 c_4 (from
   (1-u)^{-2} >= 1 + 2u), M_0 = 3, TV <= (1/2) sqrt(A). Correct as a deduction. The imported inequality itself was
   not audited here; in the paper the four-state statement is credited to the OpenAI preprint.

E. Section 6 (reconstruction above the threshold with a first moment only), read and re-derived.

1. Truncation to at most L children with mu = E min(D, L), mu lambda^2 > 1, by monotone convergence.
2. Z_n = (mu lambda)^{-n} sum f(sigma_v) over the retained level; E[Z_n | sigma_root] = f(sigma_root) because
   every mean-zero f is an eigenfunction of the channel with eigenvalue lambda and the tree is independent of
   the spins.
3. Second moment: N_{n+1} = N_n/(mu lambda^2) + E[D_L (D_L - 1)]/mu^2. Diagonal term mu N_n/(mu lambda)^2; two
   distinct children have E f(sigma_c) f(sigma_c') = lambda^2. Bounded since mu lambda^2 > 1.
4. 1 = E[eta_n Z_n] <= sqrt(E eta_n^2 C); |eta| <= 2 sqrt(q-1) TV; hence a_n >= 1/(2 (q-1) C).
5. The retained subtree must be chosen without looking at the spins. With the Ulam-Harris order, or with
   independent marks, Z_n is a function of the observations and of randomness independent of the spins, and
   conditioning on that randomness does not change the posterior. This is the ordering point raised in the
   3 Nov review; either choice closes it and the paper should state one.
6. Zero-one step: on a locally finite tree the root reconstructs if and only if some child subtree does.
   Forward: I(X; Y_1..Y_k) <= sum I(X; Y_i) for Y_i conditionally independent given X, then data processing
   along the edge. Converse: the parent posterior from one child subtree is u + lambda (p_c - u), lambda != 0,
   and further observations do not lower the expected distance. So s_R = 1 - E (1 - s_R)^D; d > 1 forces
   P(D >= 2) > 0, the generating function is strictly convex, the only fixed points are extinction and 1;
   s_R > 0 from step 4 and bounded convergence. Hence reconstruction almost surely on survival.

No flaw found in A, D or E.

## Priority, as of 10 Nov 2026

- github.com/openai/math at HEAD 4eaee875 (30 Oct 2026): family 229 has three preprints (three-state threshold
  on regular and Poisson Galton-Watson trees, 25 Sep; four-state ferromagnetic threshold, 5 Oct; four-state
  capacity criterion on bounded-degree deterministic trees, 5 Oct). None states a three-state theorem for a
  general offspring law.
- Two web searches (three-state Potts reconstruction, Galton-Watson, general offspring, Kesten-Stigum tight)
  found no paper that contains the statement.
- The OpenAI three-state preprint (introduction read 09:55): its theorem is stated for the regular tree with
  b >= 2 children and for Poisson(d) offspring, d > 1, both signs of lambda. At positive equality it works at
  a limiting fixed point of the posterior recursion and compares two expressions for the change of an entropy
  functional (the symmetrised-entropy identity of Formentin and Kuelske plus a radial inequality giving a
  positive multiple of E x^2). General offspring laws are not stated there. The paper here should say exactly
  that: regular and Poisson trees are in the OpenAI preprint; the statement for an arbitrary offspring law with
  finite mean, which is the form of the conjecture, follows from a pair inequality that never uses the
  offspring law.
- Two further searches at 09:55 (one restricted to arxiv.org) returned nothing from 2026. The closest earlier
  result is Mossel, Sly and Sohn, arXiv 2212.03362: for q = 3, 4 the bound is sharp on Galton-Watson trees
  when the mean offspring d exceeds a constant d_0. It must be cited with Sly (regular trees, large degree).
- Before the paper: re-read the statement of Conjecture 2.13 in the source (Formentin and Kuelske, On the
  purity of the free boundary condition Potts measure on random trees, SPA 119 (2009) 2992-3005) and quote
  its hypotheses exactly; a web search is not a listing search, so one pass through the arXiv math.PR and
  cs.IT listings for October and November 2026 is still owed.

## The conjecture as printed (checked 10:05-10:10)

Formentin and Kuelske, On the purity of the free boundary condition Potts measure on random trees, Stochastic
Processes and their Applications 119 (2009) 2992-3005, DOI 10.1016/j.spa.2009.03.008, arXiv 0810.0677.
Section 1.2 (p. 2994): the tree is a Galton-Watson tree whose vertices have independent numbers of children
with law Q. Conjecture 2.13 with equation (45), p. 3003: for q <= 4 there is Q-almost surely no reconstruction
if Q(d_0) (2 theta/(q - (q-2) theta))^2 < 1, where theta = tanh beta and Q(d_0) is the mean of Q. With
off-diagonal transition probability 1/(e^{2 beta} + q - 1) the second eigenvalue is
lambda = (e^{2 beta} - 1)/(e^{2 beta} + q - 1) = 2 theta/(q - (q-2) theta), so the hypothesis is d lambda^2 < 1,
strict. Conjecture 2.8 of the same paper is a different statement (about an entropy optimiser) and is not
touched here. For q = 2 the statement is the theorem of Evans, Kenyon, Peres and Schulman; for q = 4 it follows
from the pair inequality of the OpenAI four-state preprint by the deduction of part D and has to be credited
there; q = 3 with a general offspring law is the case with new content.

Why the OpenAI three-state argument does not give it by a change of notation (from the 24 Oct prior-art file,
agreed with the introduction read at 09:55): its positive-channel proof uses alpha = E[D(D-1)]/d^2 <= 1, treats
regular partial products and Poisson thinning separately and uses a Poisson survival bound. The laws
P(D=1) = 99/100, P(D=101) = 1/100 (alpha = 101/4) and P(D=k) = k^-3/zeta(3) (E D^2 infinite) lie outside it,
and the second lies outside the exponential-moment hypothesis of Mossel, Sly and Sohn (Theorem 1.12) as well.
The 24 Oct reduction addendum also shows that a same-mean Blackwell comparison with the regular or the Poisson
tree is false (D = 0 w.p. 4/5, 10 w.p. 1/5 against D = 2 and Poisson(2) at lambda = 2^{-1/2}, payoff
(max p_i - s_9)_+).

Recent papers that state the three-state case as open or restricted: Gu, arXiv 2606.21699 (19 Jun 2026),
Section 7; Lee, arXiv 2609.33263 (27 Sep 2026), Section 1.1; Jiang and Lang, arXiv 2607.05138. Two searches
at 10:09 (arXiv only; the conjecture by name) returned no paper of 2026 with the statement. The paper already
posted from this project (potts-kesten-stigum-small-degree) is for regular trees only and uses a different
method, so the new paper does not repeat it.

## Remaining 24 Oct files (read 10:05-10:08)

`INDEPENDENT_CHALLENGE.md` (117 lines), `Q3_SAME_THRESHOLD_REDUCTION_ADDENDUM.md`, `FINAL_LITERAL_SCOPE_CHECK.md`
and the rest of `FULL_FINITE_MEAN_GW_AUDIT.md`: they agree with parts A, D and E above step for step, raise the
same ordering point in the pruning (Ulam-Harris order or independent marks), and limit the claim on five or
more states to the regular-tree contrast of Sly. No new gap. A draft manuscript exists in the same folder
(`paper/`, about 1,200 lines of TeX); it is source material, to be rewritten in the house form.

## Second audit: population dynamics (from 10:08)

`tools/population_dynamics.py` simulates the law of the root posterior directly (posteriors sampled given the
root colour; each step draws D, a colour per child, a member of the population per child, the edge, the
product) and tests three consequences of the argument on heavy-tailed offspring laws at d lambda^2 = 1: the
cone E H >= 0, the drift m_{n+1} <= d lambda^2 m_n - c_3 m_n^2, and the decrease of m_n. The Nishimori identity
E p(root colour) = (2 m + 1)/3 checks the simulation itself. Controls: d lambda^2 = 1.3, and an
antiferromagnetic channel (lambda = -0.447), where a short run already gave E H < 0 and a negative drift
margin at the first step, so both tests can fail. Results of the full run: see below.

### The sampler

A first run drew each child's posterior from the population and relabelled it so that the stored "true colour"
sat at the child's colour. That sampler is not usable near the threshold: a deviation of E p(true colour) from
E sum p_i^2 is multiplied by d lambda per generation, and past depth 25 the run's own Nishimori check drifted
(gap -1.2e-2 for the 1-or-101 law) and m_n turned upward. Its output is not used. The program now treats the
population as a sample of the symmetric law: for a child of colour c a member p is drawn, a coordinate j is
drawn from p itself and placed at c, and the other two coordinates go in random order. This keeps the identity
exact in expectation at every step. `python population_dynamics.py 400000 80` (the old sampler: add `plain`).

### Results (N = 400,000, depth 80, d lambda^2 = 1, 451 s)

| offspring law | d | lambda | m_20 | m_40 | m_60 | m_80 | smallest drift margin | smallest E H / se |
|---|---|---|---|---|---|---|---|---|
| P(D=k) = k^-3/zeta(3) | 1.3684 | 0.8548 | 0.076395 | 0.031461 | 0.019390 | 0.013150 | +1.87e-04 | +95.0 |
| D = 1 (99/100), 101 (1/100) | 2 | 0.7071 | 0.004232 | 0.001779 | 0.001062 | 0.000760 | -1.35e-05 | +23.3 |
| D = 0 (4/5), 10 (1/5) | 2 | 0.7071 | 0.015154 | 0.007830 | 0.005461 | 0.004179 | -5.33e-06 | +59.6 |
| D = 2 | 2 | 0.7071 | 0.113246 | 0.063139 | 0.044977 | 0.034986 | +3.45e-04 | +201.8 |

Controls. Above the threshold (zeta law, d lambda^2 = 1.3): m_80 = 0.7152, no decay. Antiferromagnetic channel
(D = 2, lambda = -0.4472): E H = -1.58e-04 at n = 4, which is 15.5 standard errors below zero, and the drift
margin is -6.4e-02 at the first step (m_1 = 0.464 > d lambda^2 = 0.4). Both tests fail where they should.

What this does and does not show.

- Cone: E H is positive at every depth for all four laws, by at least 23 standard errors. The antiferromagnetic
  control shows the same statistic going negative.
- Decay: m_n decreases at every printed depth for all four laws, at the rate of order 1/n that a drift
  m - c m^2 gives (for D = 2, m_n n is 2.26, 2.53, 2.70, 2.80 at n = 20, 40, 60, 80).
- Drift inequality: the margin is positive throughout for the zeta law and for D = 2. For the two laws with
  d = 2 and a rare large family the smallest margins are -1.35e-05 and -5.33e-06. These are not violations in
  any usable sense: at m of order 1e-3 the term c_3 m^2 is of order 1e-10, so the margin equals m_{n-1} - m_n
  up to that, and the standard error of m_n at N = 400,000 is of order 1e-5. The drift test has no power at
  these sizes of m; it has power only in the first depths, where the margin is positive for every law.
- The simulation is a consistency check on the conclusions of the argument. It is not a proof and cannot
  detect a failure smaller than its noise.

## State after the two audits (10:22)

Every step of the three-state argument has been checked by this agent, the certificate has been recomputed by
a second program with a negative control, the conjecture has been read in the source, every 24 Oct file has
been read, and the conclusions have been tested by simulation on heavy-tailed laws with two controls. With the
3 Nov certificate replay by an agent (memory
`t067_q3_certificate_replayed_exactly_q4_traversal_unrun_2026_11_03`) there are two audits by separate
sessions on record. Next: the paper (three states as the theorem; four states as a corollary of the OpenAI
four-state pair inequality; two states Evans-Kenyon-Peres-Schulman), public repository first.
