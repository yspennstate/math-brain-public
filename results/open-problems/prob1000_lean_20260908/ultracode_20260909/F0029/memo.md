# F0029 - Jarai, Conjecture 3.7: the toppling-probability exponent eta(d), 2 <= d <= 4

Worked 2026-09-09 (about two hours). Output directory:
`~/<private-repo>/06_math_research/prob1000_lean_20260908/ultracode_20260909/F0029/`.

## 1. The problem as the source states it

Jarai, "Sandpile models" (arXiv 1401.0354, Probab. Surveys 2018), Section 3.3.2, PDF p. 19, verbatim:

> Theorem 3.6. [41] For all d >= 5 there are constants c = c(d), C = C(d) > 0 such that
> c/|x|^{d-2} <= nu[x in Av_o] <= C/|x|^{d-2}, x != 0. (19)
> Note that the upper bound follows easily from Dhar's formula (18) and Markov's inequality, so the real content of the theorem is the lower bound.
>
> Conjecture 3.7. For 2 <= d <= 4 there exists eta = eta(d) >= 0 such that
> nu[x in Av_o] = 1 / |x|^{d-2+eta+o(1)} as |x| -> infinity.
>
> We have intentionally written the exponent in the form d - 2 + eta, in order to highlight the comparison with (19) and (10). Upper bounds for the exponent eta in dimensions d = 2, 3, 4 were recently proved in [5].

Here nu is the infinite-volume sandpile measure on Z^d, a particle is added at the origin o, and Av_o = {x : n(o,x) > 0} is the set of vertices that topple. The ledger row transcribes this correctly (all quantifiers and the direction of every inequality agree with the source).

## 2. Findings

Three things, in decreasing order of solidity.

(A) The d = 4 case is already a theorem. Bhupatiraju, Hanson and Jarai (EJP 22 (2017) no. 85, arXiv 1602.06475, Theorem 1.1(iii)) prove nu(z in Av) >= c |z|^{-2} (log |z|)^{-1/3} for all z in Z^4, and Dhar's formula gives nu(z in Av) <= C |z|^{-2}. So nu(x in Av_o) = |x|^{-2+o(1)}: Conjecture 3.7 holds in d = 4 with eta(4) = 0. BHJ say so themselves ("Theorem 1.1(iii) establishes that theta = 0 when d = 4, with at most a logarithmic correction"). The survey's sentence "upper bounds for eta ... in d = 2, 3, 4" understates this: the upper bound in d = 4 is 0, which settles that case. So the conjecture is open only for d = 2 and d = 3.

(B) The May 2026 paper of Li, Liu and Shiraishi, "Tail exponents of the three-dimensional uniform spanning tree and Abelian sandpile" (arXiv 2605.19419), does not treat the toppling probability, and its sandpile lower bounds rest on a lemma that is false. Their Lemma 2.14 asserts that for every finite K containing 0 and its neighbours and every event A of vertex sets all of which contain a neighbour of 0,

    nu_K(W_{1,K} in A) = G_K(0,0) nu^{(0)}_K(T_K in A),

where W_1 is the first wave of the avalanche at 0 and T_K is the 0-component of a uniform two-component spanning forest of K (roots 0 and the wired boundary). Their proof claims that "the first wave of [the configuration with height 2d-1 at 0] is exactly T_K(xi)" and that every first wave containing a neighbour of 0 arises uniquely this way. What is true (Ivashkevich-Ktitarev-Priezzhev 1994; BHJ Lemma 2.7 and Section 2.5; Hutchcroft's (9.3)) is the all-waves identity

    sum_k nu_K(W_{k,K} in A) = G_K(0,0) nu^{(0)}_K(T_K in A)   for every A,

because the intermediate configurations of all waves of all recurrent configurations partition R'_K \ R_K (equivalently R_{K minus 0}), and the wave of an intermediate configuration is the 0-tree of its two-component forest. Lemma 2.14 therefore holds if and only if no later wave (k >= 2) ever contains a neighbour of 0. That is false as soon as K is a box of side at least 5: the maximal configuration (all heights 2d-1) is recurrent on every finite K, and its second wave from the centre contains every neighbour of the centre (`maximal_config_waves.py`: on the 5x5x5 box the waves have sizes 125, 27, 1, and waves 1 and 2 both contain all six neighbours).

Exhaustive enumeration (`waves_enum.py`, output in `waves_enum_output.txt`) on the paths of 3, 5, 7, 9 vertices and on the 3x3 box checks all of this from scratch: Dhar's formula E n(o,x) = G_K(o,x) holds for every x; the multiset of all waves equals the multiset of 0-components of all two-component forests (so the all-waves identity is verified as an equality of multisets, not just of counts); and the first-wave count differs from the forest count exactly by the number of later waves containing a neighbour of o (5 vs 8 on the 5-path, 7 vs 15 on the 7-path, 9 vs 24 on the 9-path). On the 3x3 box the two counts agree (28032 = 28032) because that box is too small for a second wave to reach a neighbour of the centre - which is why a small-box sanity check would not have caught the error. A 3D Monte Carlo at L = 9 (`waves_mc3d.py`, output `mc3d_L9_output.txt`; sandpile Markov chain with 10^5 burn-in additions, 15000 avalanches, 15000 Wilson forests) reproduces Dhar (E N = 0.2381 vs G_K(o,o) = 0.2387) and the all-waves identity (0.1840 vs 0.1846), and shows the first-wave probability below both (0.1817); in three dimensions the second wave is rare (P(N >= 2) = 0.0055), so the lemma fails by about one percent in total mass there. The exponent question is whether the first wave's share of large 0-trees stays bounded below, and nothing in LLS addresses that.

Consequences for the record. LLS Theorem 1.5 lower bound (P(diam Av_C >= R) >= c R^{-1}) and Theorem 1.6 lower bound (P(|Av_C| >= n) >= c n^{-1/3-eps}) are derived from Lemma 2.15 = the infinite-volume form of Lemma 2.14, so they are not proved there. Their upper bounds (P(diam >= R) <= C R^{-1+eps}, P(Av >= n) <= C n^{-1/3+eps}) use the sound union-bound form of the all-waves identity (BHJ Lemma 2.6 / Hutchcroft (9.3)) plus their UST Proposition 4.2 and Dhar's formula; I have not checked Proposition 4.2 but the sandpile step there is fine. The best proved lower bounds in d = 3 therefore remain BHJ's last-wave bounds: nu(x in Av) >= c |x|^{-1-alpha}, nu(rad >= R) >= c R^{-1-alpha}, nu(|Av| >= n) >= c n^{-(1+alpha)/3}, where alpha in [1/3, 1) is the LERW two-arm (escape) exponent (BHJ write 2 zeta for alpha; alpha is approximately 0.376, alpha = 2 - beta with beta the 3D LERW growth exponent).

Why the false lemma should have looked suspicious: if it were true, then (as I show in (C)) the value of eta(3) would follow at once - it would be 0 - contrary to what BHJ and Jarai-Sun expect and to Jarai-Sun's numerics.

(C) An exact relation in d = 3 between eta and the avalanche-size exponent, and what it says about the value of eta(3). Let A(R) := sum_{|x| <= R} nu(x in Av) = E|Av intersect B(R)|. Dhar gives A(R) <= C R^2. Write rad = max{|x| : x in Av}.

Proposition. Let d = 3 and suppose nu(rad >= R) <= R^{-1+o(1)} (LLS Theorem 1.5 upper bound; the only input from that paper).
(i) If nu(|Av| >= n) >= n^{-1/3-o(1)} then A(R) >= R^{2-o(1)}.
(ii) If A(R) >= R^{2-o(1)} then limsup_n log nu(|Av| >= n) / log n >= -1/3 (with no radius assumption).
(iii) If Conjecture 3.7 holds in d = 3 with exponent eta, then nu(|Av| >= n) <= n^{-1/(3-eta)+o(1)}. In particular, if Conjecture 3.7 holds and nu(|Av| >= n) >= n^{-1/3-o(1)} (the LLS claim), then eta(3) = 0. With only BHJ's radius bound R^{-1/6} in place of R^{-1}, (iii) reads nu(|Av| >= n) <= n^{-1/(13-6 eta)+o(1)}.

So in d = 3 the three statements "eta(3) = 0 on average" (A(R) = R^{2-o(1)}), "the avalanche-cluster size tail is n^{-1/3-o(1)}", and (assuming the conjectured power law) "eta(3) = 0" are the same statement, given the radius tail R^{-1+o(1)}. The Grassberger-Manna observation quoted by Jarai-Sun (average number of distinct toppled sites in a box of side L scaling like L^2 in 3D, with at most a logarithmic correction) is the averaged form eta = 0; Jarai-Sun's own one-point estimate eta(3) approximately 0.09-0.1 is the pointwise form eta > 0; under Conjecture 3.7 the two cannot both be right asymptotically, since A(R) is by definition the sum of the one-point function. Jarai-Sun noticed the tension ("the reason why this positive exponent does not affect the average number of topplings could be that the averages are dominated by very large avalanches"), but that explanation cannot work for the number of distinct sites, which is exactly A(R). The question of eta(3) is thus sharpened to: is the mean number of distinct sites toppled within distance R of the origin R^{2-o(1)} (eta = 0) or R^{2-eta} with eta > 0? Equivalently, in wave language: conditional on x toppling, is the mean number of waves reaching x bounded, or does it grow like |x|^eta?

## 3. Proofs

Setting: d = 3, Av = Av_o finite nu-a.s. (Jarai-Redig), G(o,x) the Green function, A(R) as above.

(i) On {rad <= R} we have Av subset of B(R), so |Av intersect B(R)| >= |Av| 1{rad <= R}. Hence for every M,
  A(R) >= E[|Av|; rad <= R] = sum_{m >= 1} nu(|Av| >= m, rad <= R) >= sum_{m=1}^{M} [nu(|Av| >= m) - nu(rad > R)].
Fix eps in (0, 1/10). For m >= m_0(eps), nu(|Av| >= m) >= m^{-1/3-eps}; and nu(rad > R) <= C R^{-1+eps} for R >= 1. Take M = R^{3-delta} with delta = 13 eps. Then sum_{m <= M} m^{-1/3-eps} >= c M^{2/3-eps} = c R^{(3-delta)(2/3-eps)} while M nu(rad > R) <= C R^{2-delta+eps}, and (3-delta)(2/3-eps) > 2 - delta + eps (Lean: `F0029_step_i`). So A(R) >= c' R^{(3-13 eps)(2/3-eps)} for large R, and since eps is arbitrary, A(R) >= R^{2-o(1)}.

(ii) A(R) = E|Av intersect B(R)| <= E min(|Av|, |B(R)|) = sum_{m=1}^{|B(R)|} nu(|Av| >= m). If nu(|Av| >= m) <= m^{-1/3-delta} for all large m, the right side is O(R^{3(2/3-delta)}) = O(R^{2-3delta}), contradicting A(R) >= R^{2-o(1)}.

(iii) Under the conjecture, for every eps > 0 and |x| large, nu(x in Av) <= |x|^{-1-eta+eps}, so A(R) <= C_eps R^{2-eta+eps}. Then for n >= 1 and any R,
  nu(|Av| >= n) <= nu(rad > R) + nu(|Av intersect B(R)| >= n) <= C R^{-1+eps} + A(R)/n <= C R^{-(1-eps)} + C_eps R^{2-eta+eps}/n.
With R = n^{1/(3-eta)} both terms equal n^{-(1-eps)/(3-eta)} (Lean: `F0029_step_iii`, an exact identity of real powers), so nu(|Av| >= n) <= C n^{-(1-eps)/(3-eta)} and, eps being arbitrary, nu(|Av| >= n) <= n^{-1/(3-eta)+o(1)}. If also nu(|Av| >= n) >= n^{-1/3-o(1)}, then 1/(3-eta) <= 1/3, so eta <= 0, and eta >= 0 by Dhar, so eta = 0. The variant with radius exponent rho in place of 1 gives R^{2-eta+rho} = n and the bound n^{-rho/(2-eta+rho)}; rho = 1/6 (BHJ Theorem 1.2(ii)) gives n^{-1/(13-6eta)}.

The argument for (B) is in Section 2; the only non-elementary input is the all-waves partition of BHJ Lemma 2.7 (with W(eta_k) = T_o(phi'(eta_k)) in their Section 2.5), which the enumeration verifies independently on five graphs as a multiset identity.

## 4. What is not done

- Conjecture 3.7 in d = 2 and d = 3 stays open. I did not prove or refute the power law itself.
- The proposition ties eta(3) to the size exponent but does not determine either. The unconditional lower bound on A(R) is only BHJ's R^{2-alpha}.
- I have not checked LLS Proposition 4.2 (0-tree diameter upper bound R^{-1+eps} in the 0-wired USF), on which the sound half of their sandpile theorems and the radius input to (i) and (iii) depend. If it also failed, (iii) falls back to the BHJ-radius version and (i) gives nothing.
- No repair of LLS Lemma 2.14 was found. A correct first-wave statement would need a lower bound on the share of first waves among large 0-trees; that is essentially the eta(3) = 0 question again.
- The 3D Monte Carlo is at L = 9 and says nothing about exponents; it is only a check of the identities.

## 5. Checks

- Dhar's formula reproduced exactly (enumeration, five graphs) and to 0.3 percent (Monte Carlo, L = 9).
- All-waves identity verified as an equality of multisets on five graphs, and numerically in 3D (0.1840 vs 0.1846, 15000 samples).
- The failure of LLS Lemma 2.14 checked two independent ways: exhaustive counts (paths 5, 7, 9) and the deterministic maximal-configuration example on 5x5, 7x7, 5x5x5, 7x7x7 boxes; the Monte Carlo shows the gap in 3D (0.1817 vs 0.1846; about 35 of 15000 avalanches have a later wave reaching a neighbour).
- Strongest case that I am wrong about (B): that LLS's nu^{(0)}_K is some non-uniform law on forests under which the first-wave identity holds. Their text defines it as the uniform measure on R_{K minus 0} (the count formula |R_{K minus 0}|/|R_K|), so the identity is a statement about counts, and the counts differ. The check that would confirm me wrong is a K of side >= 5 on which no later wave contains a neighbour of 0; the maximal configuration rules that out on every such box.
- Strongest case that I am wrong about (C): a subtlety in passing from "n^{-1/3-o(1)} for all n" to the sum. I wrote the sum with the explicit choice M = R^{3-13 eps} and checked the exponent inequality in Lean. The step nu(rad > R) <= R^{-1+eps} is LLS's upper bound, whose sandpile half is the correct union bound. The step E|Av intersect B(R)| = A(R) is Fubini.
- Lean: `U_F0029.lean` compiles clean (axioms: propext, Classical.choice, Quot.sound) and certifies the two arithmetic steps of (i) and (iii). It does not formalize the probabilistic argument.

## 6. Prior art

- Jarai-Redig-Saada (Theorem 3.6 of the source; JRS 2015): d >= 5, eta = 0.
- Bhupatiraju-Hanson-Jarai, EJP 2017: Theorem 1.1: nu(z in Av) >= |z|^{-3/4+o(1)} (d = 2), >= c|z|^{-2 zeta - 1} with zeta < 1/2 (d = 3), >= c|z|^{-2}(log|z|)^{-1/3} (d = 4); table of exponent intervals; the last wave is the tool; they "expect theta positive in dimensions two and three". Their Lemma 2.7 (all waves partition R'_H \ R_H) and Section 2.5 (wave = 0-tree of the intermediate configuration) are the correct form of the wave/forest correspondence.
- Hutchcroft, PTRF 2020 (arXiv 1804.04120): mean-field exponents for d > 4; his (9.3) is the union-bound form of the all-waves identity.
- Jarai-Sun, J. Stat. Mech. 2019, 113204 (Bath repository copy `jarai_sun_simulation_revision.pdf`): exact-sampling numerics; conjectures nu[x topples] = |x|^{-eta+o(1)} with eta(2) = 0.40 +- 0.03 and |x|^{-1-eta+o(1)} with eta(3) approximately 0.1 (0.09); notes the average number of distinct sites toppled in 3D is close to L^2 (Grassberger-Manna) and that the positive exponent "does not affect the average number of topplings".
- Li-Liu-Shiraishi, arXiv 2605.19419 (19 May 2026): sharp tails for the past of the origin in the 3D UST (extrinsic exponent 1+alpha, intrinsic (1+alpha)/(2-alpha), volume (1+alpha)/3) and for the 0-tree of the 0-wired USF (extrinsic 1, volume 1/3); sandpile Theorems 1.5-1.6 (radius exponent 1, size exponent 1/3); no result on the one-point toppling probability; Lemma 2.14 false as discussed. They state that the two-dimensional case is out of reach of their method and that a.s. finiteness of 2D avalanches is open.
- Search phrases that found these: "Inequalities for critical exponents in d-dimensional sandpiles"; "Tail exponents of the three-dimensional uniform spanning tree and Abelian sandpile"; "Toppling and height probabilities in sandpiles". The web-search budget of this session ran out after the first round; the Jarai author page and arXiv API were not reachable; the Jarai-Sun text came from the Bath repository PDF.
