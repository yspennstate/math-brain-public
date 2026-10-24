# Referee B (Claude Opus 5, 2026-09-15): Theorem 1.2 (the critical law) and source fidelity

Brief: the mathematics of the critical infinite-variance construction (Section 4), and every quotation and
citation in the paper. Everything re-derived independently from the definitions; the sources read in the
primary texts (Thevenin arXiv:1812.07365v2; Janson arXiv:1112.0510) and on the web.

## Part 1: the construction and the proof of Theorem 1.2

Re-derived and found correct:

1. Base law (5/8, 1/4, 1/8): mean 1/2, second moment 3/4, variance 1/2. Matches.
2. Induction hypothesis. The stage adds p_r at L_r^-, p_r at L_r^+, a_r at H_r and removes h_r from 0, so the
   mean rises by exactly p_r(L^- + L^+) + a_r H_r = Delta_r/2 by the definition of a_r (an identity, not an
   estimate; it is the Lean theorem `mean_update`). Hence 1 - Delta_r goes to 1 - Delta_r/2 = 1 - Delta_{r+1}.
3. Gate G1 gives the support chain (4.2): L^- >= N Delta - D - 1 >= n Delta - (D + Delta + 1) >= (1-eps) n Delta,
   and M_r <= eps n Delta < (1-eps) n Delta since eps <= 1/11. Also L^+ <= n Delta + D <= (1+eps) n Delta, and
   (1+eps_r) Delta_r <= (12/11)(1/2) = 6/11 < 1 gives L^+ < n_r < H_r. Three fresh atoms, none equal to 0, 1, 2.
4. Existence of admissible n. Lemma 2.2 is applied to the FIXED law Q^(r-1) with N going to infinity. The
   standardised target is exactly (k^± - N mu)/sqrt N -> ∓ D_r/sqrt N = ∓ V_r/(q Delta_r), since
   D_r(n) = V_r sqrt N/(q Delta_r). Lemma 2.2's limit is then exp(-a^2/(2V_r))/sqrt(2 pi V_r) with
   a^2/(2V_r) = V_r/(2 q^2 Delta_r^2), which is exactly c_r as defined. The conditional mean is gamma_r a/V_r
   with gamma_r = q(1 - mu) = q Delta_r, giving ∓1 exactly, and the variance is q(1-q) - q^2 Delta_r^2/V_r = v_r
   exactly. So G2 and G3 are asymptotically satisfiable; Polya's theorem turns the weak convergence of G3 into
   uniform convergence of distribution functions, which is what a Kolmogorov-distance gate needs. G4's exponent
   is linear in n at fixed r while eps_r w_r(n) decays like n^{-7/2}; and n^{-6}/w_r(n) = O(n^{-5/2}). All five
   gates hold for all large n. Correct.
5. "The least admissible n" is well defined once the set is non-empty; the paper does not claim it is decidable,
   and nothing downstream needs decidability. Acceptable as an existence statement.
6. The conditional laws in G3 are well defined: 0 <= k^± <= N because 0 < L^- < L^+ <= (1+eps) n Delta < n-1 for
   n >= 3, and k^± ones with N - k^± zeros is a positive-probability configuration since {0,1} is in the support.
7. Bounds on a_r: p_r(L^-+L^+) < 2 n_r^{-3} <= Delta_r/4 (needs n_r^3 >= 2^{r+3}, true since n_r >= 2^{8r}), so
   Delta_r/(4H_r) < a_r < Delta_r/(2H_r) and 0 < h_r < 3 n_r^{-4}. Then sum h_r < 4*256^{-4} < 1/8 and pi_0 > 1/2.
8. M_{r+1} = H_r = n_r^4, and G1 at the next stage forces n_{r+1} >= M_{r+1}/(eps Delta) >= n_r^4. Hence
   log n_r >= 4^{r-1} log 256, which is what the infinite-moment argument uses.
9. Proposition 4.1. Criticality by monotone convergence (the positive atoms increase to those of pi). For
   alpha > 1, a_r H_r^alpha > (Delta_r/4) H_r^{alpha-1} = 2^{-r-2} n_r^{4(alpha-1)}, which tends to infinity by
   item 8; no exponential moment follows. V_r >= a_{r-1}(H_{r-1}-1)^2, of order 2^{-r-1} n_{r-1}^4, tends to
   infinity, so v_r -> q(1-q) = 3/16. Span one since pi_0, pi_1 > 0. Correct.
10. Proof of Theorem 1.2. On the conditioning event every coordinate is at most n-1 < H_r, and every later atom
    exceeds n-1 (L_{r+1}^- >= ((1-eps)/eps) M_{r+1} = 10 H_r), so only A and L_r^± occur. The reweighting (4.3)
    is exact and multiplicative, with eta >= 1 - n tau/z >= 1 - 8 n^{-3} using tau < 4n^{-4} and z > 1/2. That
    form is the load-bearing one: an additive total-variation bound would not survive a conditioning event of
    probability n^{-7/2}. The type J = 0 is killed by Bernstein against the excess n Delta_r - 1 (the
    Q-variables have mean 1 - Delta_r, are bounded by M_r, total variance n V_r), which is G4. The types J >= 2
    are killed by the binomial factorial moment 2 n^2 p_r^2 = 2 n^{-6}, which is G5. The types J = 1 lie within
    [eta(1-eps), 1+eps] w_r(n) by G2, since n p_r = n^{-3}. Hence P(J=1|C) -> 1 and each sign -> 1/2. For the
    count of ones the density lies between eta and eta^{-1}, so the total variation is O(n^{-3}); G3 puts it
    within eps_r of N(∓1, v_r); v_r -> 3/16 and the Gaussians converge in Kolmogorov distance. Recentering as in
    Section 3. All correct.

One presentational gap: the final step needs d_K(N(∓1,v_r), N(∓1,3/16)) -> 0 in addition to eps_r + O(n^{-3}).
This follows from v_r -> 3/16 and continuity, and the paper states v_r -> 3/16 in the same sentence, so the
reader has it, but the three terms should be added up explicitly. Not an error.

Statement against proof: pi_1 = 1/4 and pi_2 = 1/8 (never touched after stage 0), pi_0 = 5/8 - sum h_r > 1/2,
E xi = 1, E xi^alpha = infinity for every alpha > 1 (hence infinite variance), span one, and T_n defined for all
n because pi_1 > 0. Every clause is proved.

Numerics (Part C of the script, independently re-derived): V_1 = 1/2 and Delta_1 = 1/2, so the displacement is
V_1/(q Delta_1) = 4 and v_1 = 3/16 - (1/16)(1/4)/(1/2) = 5/32, with c_1 = exp(-16)/sqrt(pi). The gates first pass
at n = 2^17, where L^± = floor(131071/2 ± 4 sqrt(131071)) = 64087 and 66983 (Lean `critical_stage_one`).
Consistent throughout.

## Part 2: source fidelity, where two real errors turned up

B1, an error of citation in the introduction. The paper attributed the central limit theorem for degree counts
in the critical finite-variance case to "Janson, Theorem 7.11". That theorem is the law of large numbers
(N_d/n -> pi_d in probability) and contains no central limit theorem. The central limit theorem is Kolchin,
Random Mappings, Theorem 2.3.1, quoted as (20.5) in Section 20.2 of the survey, and its variance is
sigma_d^2 = pi_d(1 - pi_d - (d-1)^2 pi_d/sigma^2), not pi_d(1 - pi_d). Fixed: the sentence now cites Kolchin
with the correct variance and points to (20.5)-(20.7) for the joint version under a third moment.

B2, an overclaim in the closing section. The paper said the first question of Problem 20.2 is settled because
"Janson's Theorem 7.11 already gives the central limit theorem under no moment condition beyond the second",
wrong on both counts. Reading Section 20.2 in order, (20.5) already holds for nu = 1 and sigma^2 finite by
Kolchin, while (20.7) needs a third moment and (20.8)-(20.9) need all moments, so the first question of Problem
20.2 is about the joint and moment versions. Fixed: the paragraph now says exactly that.

B3, a scope omission that mattered. The conjecture's own first sentence reads "We have seen that the conclusions
of Theorem 6.7 hold for mu with infinite variance in the domain of attraction of a stable law and for mu a
subcritical power law." So the critical infinite-variance case is already known inside the stable domain of
attraction, and any counterexample has to lie outside it. The law of Theorem 1.2 has E xi^alpha = infinity for
every alpha > 1 and is in the domain of attraction of no stable law, so it does. Fixed: both facts are stated.

B4, the mechanism of Theorem 6.7, now attributed. Thevenin's proof runs through Armendariz-Loulakis Theorem 1
(or Section 19 of Janson's survey): after removing the largest outdegree the others are asymptotically i.i.d.
with law mu, so the degree-count vector is asymptotically multinomial. That is exactly the step these examples
break, since with a lacunary tail the largest outdegree can absorb only two values and the rest stay conditioned
on their sum. Armendariz and Loulakis (Stochastic Process. Appl. 121 (2011), 1138-1147, arXiv:0912.1516) assume
subexponentiality. Fixed: the step and the citation are in the paper, and the Question of Section 6 is the
corresponding local-regularity hypothesis.

B5, the quotation of the conjecture is verbatim. Checked character by character against Section 6.2 of
arXiv:1812.07365v2, including the restriction to A a subset of Z_+.

B6, Theorem 6.7 is restated correctly: hypotheses (subcritical; mu_k ~ c k^{-beta} with c > 0 and beta > 2;
finitely many finite sets A_i), conclusion (joint convergence of the normalised counts), covariance
mu_{A_i cap A_j} - mu_{A_i} mu_{A_j}, and marginal variance mu_A(1 - mu_A). The theorem is genuinely not
contradicted, since the laws here are asymptotic to no positive power law.

B7, Problem 20.2 is described correctly, in its three questions and in that order.

B8, the remaining citations check out. Janson Theorem 7.11 for the law of large numbers, as now used; Section 15
of the survey for the allocation correspondence and Section 19 for condensation; Boucheron-Lugosi-Massart
Theorem 2.10 for Bernstein's inequality, where only the upper bound Z_i <= M is needed; Dvoretzky-Motzkin, Duke
Math. J. 14 (1947) 305-313; Jonsson-Stefansson, J. Stat. Phys. 142 (2011) 277-313; Kortchemski, AIHP 51 (2015)
489-511; Abraham-Delmas, Electron. J. Probab. 19 (2014) no. 56; Pitman, LNM 1875, Section 6.1 for the cycle
lemma; Thevenin, Electron. J. Probab. 25 (2020), paper no. 64.

## Verdict

Theorem 1.2 and its construction are correct as stated, and I found no mathematical gap in Section 4. The source
audit found two real citation errors (B1, B2), one scope omission (B3) and one missing attribution of the
mechanism (B4), all now fixed in the paper. After those fixes the sources are faithful.
