PARTIAL

E0022: orthogonal projections and Hunt's hypothesis

No general proof or counterexample is claimed. Literature was checked before the proof work. The source supplies conditional affirmative answers. Searches through 13 November 2026 found no printed resolution of Question 1; this is a search result, not a certification of absence from the literature.

1. Source and exact question

Ze-Chun Hu and Wei Sun, *Hunt's Hypothesis (H) for Markov Processes: Survey and Beyond*, [arXiv:1908.06825v1](https://arxiv.org/abs/1908.06825v1), 19 August 2019, 27 pages; later published in *Acta Mathematica Sinica* 37 (2021), 491–508, [doi:10.1007/s10114-021-9343-7](https://doi.org/10.1007/s10114-021-9343-7). All survey pages below mean **2019 PDF pages**, also its printed page numbers, not the journal pagination. The publisher record was located, but attempts to retrieve the 2021 full text were blocked; the theorem inventory is specifically a direct read of the 2019 version.

Question 1, §3.2, p.15, with mathematical typography restored:

> Question 1. If for any nonempty proper subspace A of R^n, the projection process X_A of X on A satisfies (H), does X satisfy (H)?

Section 3 assumes n>1 (p.13). Here X_A(t)=P_A X_t, with P_A the orthogonal projection, and state space A. Lemma 3.4, pp.14–15, explicitly calculates Y_t=P_2 X_t. For z∈A, ψ_A(z)=ψ(z); in scalar coordinates on a line with unit direction e, ψ_e(u)=ψ(ue). This is projection of each position, not conditioning on staying in A.

The reverse direction is known: **Lemma 3.1, p.13**, citing the sums paper's Lemma 3.4, proves that (H) for X implies (H) for every proper projection.

2. Survey inventory: sums, products, projections and subordination

These are mathematical restatements. Use

    E exp(i⟨z,X_t⟩)=exp(−tψ(z)),
    ψ(z)=i⟨a,z⟩+½⟨z,Qz⟩
          +∫[1−exp(i⟨z,x⟩)+i⟨z,x⟩1_{|x|<1}]ν(dx).

Put G=range(√Q)=range(Q). In the sums results, condition (S) means ν(G^c)<∞ and d_G∈G, where d_G=−a−∫_{G^c,|x|<1}xν(dx). The sign follows from the displayed exponent convention. A compound Poisson process here has zero uncompensated deterministic drift.

| Result; PDF page | Statement, including required hypotheses |
|---|---|
| Theorem 2.5, p.5 | Full-rank Q gives (H), a Kanda–Forst bound, and the same polar sets for X and X−X̄, where X̄ is an independent copy. |
| Theorem 2.6, p.5 | If ν(G^c)<∞, (H), d_G∈G, and the Kanda–Forst bound are equivalent. No density assumption is imposed. |
| Proposition 2.7, p.6 | Bounded continuous transition densities and equality of polar sets for X and its independent symmetrization imply (H). |
| Theorem 2.14, p.8 | If independent X₁ has (H) and X₂ is compound Poisson, X₁+X₂ has (H), without a density assumption. |
| Theorem 2.15, p.8 | If two independent summands satisfy (S), their sum has (H). |
| Theorem 2.16, p.8 | Assume X₁+X₂ and X₁ have Lebesgue resolvent densities, X₁ has (H), every finite positive measure of finite 1-energy for the sum has finite 1-energy for X₁, and |Im ψ₂|≤c(1+Re ψ₁+Re ψ₂). Then the sum has (H). |
| Theorem 2.17, p.9 | Remove a finite Lévy submeasure ν₁≤ν and change a to a+∫_{|x|<1}xν₁(dx). Semipolar sets and Lebesgue-essentially polar sets are unchanged; (H) is equivalent for the two processes, as is (H_m). This includes removal of big jumps. |
| Proposition 2.24, p.11 | A subordinator satisfying (H) has zero drift coefficient. The converse is not stated for general subordinators. |
| Theorem 2.25, p.11 | For a special subordinator, (H) holds iff its drift is zero. Here “special” means its potential measure restricted to (0,∞) has a decreasing Lebesgue density. |
| Proposition 2.27, p.11 | A locally quasi-stable subordinator has (H): it has zero drift, and near 0 its Lévy measure is bounded above and below by positive multiples of a stable subordinator's Lévy measure, allowing finite-measure errors on each side (Definition 2.26, p.11). |
| Theorem 2.29, p.11 | A driftless subordinator of type (α,β), 0<α<β<1, decomposes into two independent driftless subordinators of the same type, each with (H). The type assumption is a Lévy density between c⁻¹x^(−1−α) and cx^(−1−β) on (0,1]. The theorem does not establish (H) for their sum. |
| Theorem 2.30, pp.12–13 | For standard processes in the common canonical setup there, local absolute continuity of Y's path laws with respect to X's, at every starting point and finite time before lifetime, transfers (H) from X to Y. It also transfers (H_m). |
| Theorem 2.31, p.13, Glover–Rao | If an independent subordinator τ has (H), X_τ has (H) for any standard X. X need not have (H). |
| Theorem 2.32, p.13, Hu–Sun–Wang | X has (H) iff X_τ has (H) for some, hence any, independent subordinator with strictly positive drift coefficient. Also true for (H_m). |
| Lemma 3.1, p.13 | (H) passes from X to every orthogonal projection. |
| Proposition 3.2, p.14 | If Q=0 and ∫(1∧|x|)ν(dx)<∞, (H) forces the uncompensated drift d=−a−∫_{|x|<1}xν(dx) to vanish. |
| Proposition 3.3, p.14 | If Q is degenerate and the G^⊥ projection has finite-variation jump measure, (H) for X forces that projection's uncompensated drift to vanish. |
| Lemma 3.4, pp.14–15 | For P=P_{G^⊥}, the projected triplet is (a_P,0,ν_P), with a_P=Pa+∫Px(1_{|x|<1}−1_{|Px|<1})ν(dx). ν_P is the image Lévy measure away from 0; mass mapped to 0 is discarded. |
| Example 3.5, p.16 | Gaussian covariance [[2,2],[2,2]], drift (1,−1): coordinate projections have (H), but projection onto span(1,−1) is nonzero deterministic motion. Every other line projection has (H). This answers Question 3, not Question 1. |
| Theorem 3.6, pp.16–17 | Under degenerate Q and ν(G^c)<∞, equivalent are: X has (H); every line projection has (H); the G^⊥ projection has (H). For Q=0 the last projection is X itself. |
| Theorem 3.7, pp.17–18 | If G⊊S⊊R^n and ν(S^c)<∞, equivalent are: X has (H); every proper projection has (H); the S and S^⊥ projections have (H). Those projections need not be independent. |
| Remark 3.8, p.18 | Corrects Lemma 3.5 of the earlier sums paper: the hypothesis that the S^⊥ projection has (H) must be added. Its Lemma 3.6 and Theorem 3.1 remain true. |
| Proposition 3.9, p.19 | If independent X₁ has (H) and X₂ is compound Poisson, the product (X₁,X₂) has (H). |
| Proposition 3.10, p.19 | If independent factors both satisfy (S), their product has (H). |
| Theorem 4.1, p.20, Kanda–Rao | With resolvent densities, if a finite measure charges no semipolar set and has finite λ-energy, its energy tends to zero as λ→∞. |
| Theorem 4.2, p.20 | With resolvent densities, (H) is equivalent to that zero-energy limit for every finite positive measure of finite 1-energy. |
| Theorem 4.3, p.20, Kanda | For X with transition densities and its space-time process (t,X_t), a compactly supported positive measure of finite space-time λ-energy has an X-marginal of finite λ-energy. A singular time marginal forces its X-marginal to charge no semipolar set. For a product η⊗ξ of finite space-time energy, ξ carried by a semipolar set forces η to have an L² density. Conversely, compactly supported ξ of finite X-energy charging no semipolar set admits a singular compactly supported η giving finite product space-time energy. |
| Corollary 4.4, p.20 | With transition densities, a closed B is semipolar iff X, from every starting point, avoids B at every time in each fixed Lebesgue-null subset of (0,∞). |
| Proposition 4.5, p.21 | For independent X,Y and Z=(X,Y), assume all three have resolvent densities. A compactly supported finite positive measure of finite Z λ-energy has marginals of finite X and Y λ-energy. |
| Proposition 4.6, p.21 | In that setup, if η⊗ξ has compact support and finite Z-energy, ξ carried by a Y-semipolar set forces η to have an L² density. The other assertion interchanges factors. |
| Corollary 4.7, p.21 | In the same product-measure setup, singular η implies ξ charges no Y-semipolar set; singular ξ implies η charges no X-semipolar set. |
| Proposition 4.8, p.21; proof pp.24–25 | Assume all three resolvent densities, X has (H), Y satisfies a Kanda–Forst bound, and a compactly supported **product** measure has finite Z-energy. Its Z λ-energy tends to zero. The statement's μ/ν mismatch is a typographical error; the proof concerns the specified product measure. |

The unrestricted independent-product question is Question 4/4′, pp.15,18; the unrestricted sum question is Question 7, p.25. They remain among the survey's open questions. Remark 5.1, p.25, shows that a general positive product answer would imply a positive sum answer by projection. Neither unrestricted closure rule may be assumed. Proposition 4.8 does not cover arbitrary measures on the product space.

There is a further caution in reading Remark 3.8 literally: the earlier printed Lemma 3.5 also lacks the Gaussian-range containment used in Theorem 3.7. Adding only the complementary projection's (H) hypothesis to that literal statement is still insufficient. Indeed Example 3.5, with S a coordinate axis, has ν(S^c)=0 and both complementary projections satisfying (H), yet X fails (H). The valid finite-off-subspace result used here explicitly retains range(Q)⊆S; the proof below checks it. No claim is made that the remark alone repairs every missing hypothesis of the earlier lemma.

3. Literature verification and limits of the search

Only plain source texts were saved. Each has PDF-page markers; data/sources.jsonl records URLs, retrieval times, page counts and hashes of the PDF inputs, which existed only in memory. The following locators distinguish direct reads from results verified through the survey.

| Work | Verification and exact locator |
|---|---|
| Hu–Sun, SPA 122 (2012), 2319–2328 | [arXiv:1101.3038](https://arxiv.org/abs/1101.3038), text read. Theorems 1.1–1.2, preprint p.3: nondegenerate Gaussian part and finite-off-Gaussian-range equivalence. Proposition 1.5, p.3: symmetrization criterion; Proposition 1.6, p.4: subordinator drift obstruction. |
| Hu–Sun, *Further study*, Science China Math. 59 (2016), 2205–2226 | [arXiv:1406.2013](https://arxiv.org/abs/1406.2013), text read. Propositions 2.1–2.2 and Theorems 2.3–2.4, preprint p.5: energy and logarithmic criteria. |
| Hu–Sun, *Sum of Two Independent Lévy Processes*, Comm. Math. Stat. 6 (2018), 227–247 | [arXiv:1702.07396](https://arxiv.org/abs/1702.07396), text read. Theorems 3.1–3.2, p.11; projection Lemma 3.4 and subsequently corrected Lemma 3.5, p.12; Theorem 4.1 and Proposition 4.2, p.14. Theorem 2.1, p.5, restates Bretagnolle's classification. |
| Hu–Sun–Zhang, *New results*, Potential Anal. 42 (2015), 585–605 | [arXiv:1210.2016](https://arxiv.org/abs/1210.2016), text read. Theorem 2.1, preprint p.5: finite-jump comparison under the density assumptions stated there. Theorem 4.5, p.13: extended Kanda–Forst–Rao criterion. Theorem 5.1, p.22: energy characterization. The strengthened comparison in the survey uses later work. |
| Hu–Sun–Wang, *Two Theorems*, 2019 preprint, subsequently Potential Analysis | [arXiv:1903.00050](https://arxiv.org/abs/1903.00050), text read. Theorem 1.1, p.3: local absolute continuity; Theorem 1.3, p.4: positive-drift subordination; Proposition 4.11, p.16: strengthened finite-jump comparison; Proposition 5.3, p.21: finite-variation drift obstruction. |
| Kanda (1976,1978); Forst (1975) | Statements checked in survey Theorems 2.1–2.2, p.4. Kanda's papers: Z. Wahrscheinlichkeitstheorie verw. Gebiete 35, 159–165 and 42, 141–154. Forst: *The definition of energy in non-symmetric translation invariant Dirichlet spaces*, Math. Ann. 216, 165–172. Originals not obtained; no internal original-page locator is invented. |
| Rao (1977,1987,1988) | The 1977 paper is *On a result of M. Kanda*, 41, 35–37. *On polar sets for Lévy processes* is JLMS (2) 35, 569–576 **(1987)**. *Hunt's hypothesis for Lévy processes* is PAMS 104, 621–624 (1988), [publisher PDF](https://www.ams.org/journals/proc/1988-104-02/S0002-9939-1988-0962838-6/S0002-9939-1988-0962838-6.pdf), directly read as text: Theorems 1–2, printed p.622; proof p.623; Corollary 3 on nondegenerate asymmetric Cauchy processes, p.624. |
| Glover–Rao | *Hunt's hypothesis (H) and Getoor's conjecture*, Ann. Probab. 14 (1986), 1085–1087, [doi:10.1214/aop/1176992463](https://doi.org/10.1214/aop/1176992463). Subordination statement verified through survey Theorem 2.31 and Hu–Sun–Wang Theorem 1.2, p.3. The 1988 *Nonsymmetric Markov processes and hypothesis (H)*, J. Theor. Probab. 1, 371–380, is discussed on survey p.12. Original full texts not obtained. |
| Blumenthal–Getoor; Hawkes; Fitzsimmons; Silverstein | Survey Theorem 1.1, p.2, gives the bounded-potential-principle equivalences. Survey p.4 cites Hawkes Theorem 2.1 for resolvent densities iff lower semicontinuity of all 1-excessive functions; [publisher record](https://doi.org/10.1112/plms/s3-38.2.335), PLMS (3) 38 (1979), 335–352. Survey p.12 discusses Silverstein's quasi/essential polarity theorem, 41, 13–33 (1977), and Fitzsimmons' extensions. These originals were not obtained. |
| Kesten–Bretagnolle | Kesten's 1969 AMS Memoir 93; Bretagnolle's *Résultats de Kesten sur les processus à accroissements indépendants*, Séminaire de Probabilités V (1971), 21–36, [original text source](https://www.numdam.org/article/SPS_1971__5__21_0.pdf), obtained. Survey p.4 equation (2.1) and sums paper Theorem 2.1, p.5, distinguish hitting points from regularity for points. |
| Jacob | Hu–Sun (2012), Remark 1.3(ii), preprint p.3, cites Jacob, *Pseudo-Differential Operators and Markov Processes*, vol.1 (2001), Example 4.7.32, for the Dirichlet-form connection in the finite-off-Gaussian-range class. Book page/example not independently obtained. No projection-converse theorem by Jacob was located. |

Searches used the requested author/title names, straight and curly apostrophes, “Hunt hypothesis”, “semipolar”, “Getoor conjecture”, “projection”, “Lévy/Levy”, and year terms 2019–2026. Later results located include the 2021 journal versions and Liping Li's [arXiv:2107.06163](https://arxiv.org/abs/2107.06163), on general one-dimensional diffusions, not this multidimensional Lévy question. A 2026 paper by Zhen-Qing Chen and Jie-Ming Wang, [arXiv:2608.13976](https://arxiv.org/abs/2608.13976), *Boundary Harnack principle for diffusion with jumps on metric measure spaces*, was obtained as text: assumption (A1), p.4, assumes (H). Remark 1.8, p.7, says this assumption can be omitted for a restricted boundary-Harnack formulation; it does not establish (H) from projections. The examples on pp.25,30,34 verify (H) in particular classes using prior symmetry or change-of-measure results. None answers Question 1. The [IMAR seminar listing](https://www.imar.ro/ro/seminar/38) records Wang's February–March 2026 talks on measure change and subordination; seminar titles are not projection-converse theorems. No located later result answers Question 1.

Getoor's conjecture is called open on survey p.2; §5, p.25, explicitly retains Questions 1,2,4. “Essentially all” or “nice” is not a formal assertion that every Lévy process satisfies (H); deterministic motion already disproves that assertion. No located later paper closes it in general.

4. Analytic criteria and proof work

The literature inventory above was saved before completing the following sections. The conditional results proved here are consequences or rederivations of the cited theory; no novelty is asserted.

Let T_D=inf{t>0:X_t∈D}. A set is thin if it has a nearly Borel hull C such that P^x(T_C=0)=0 for every x. A semipolar set is contained in a countable union of thin sets. A polar set has a nearly Borel hull never hit at a positive time, from any starting point (survey pp.1–2). These definitions are used throughout. The proposed shorthand “finely thin everywhere except a polar set” is not substituted for the countable-union definition. For example, for X_t=t on R, Q is a countable union of thin singletons but T_Q=0 from every starting point.

In the analytic statements below assume X has Lebesgue resolvent densities. By Hawkes' result cited on survey p.4 this is equivalent to lower semicontinuity of every 1-excessive function. It is a substantive hypothesis, not a consequence asserted here of the projection assumption.

Write r(z)=Re ψ(z), I(z)=Im ψ(z), A(z)=1+r(z), B(z)=|1+ψ(z)|, and for a finite positive measure μ set

    μ̂(z)=∫exp(i⟨z,x⟩)μ(dx),
    E_λ(μ)=∫ [λ+r(z)]/[(λ+r(z))²+I(z)²] |μ̂(z)|² dz.

Finite 1-energy means E_1(μ)=∫A B⁻²|μ̂|²<∞. A normalization factor (2π)^−n, if included, changes neither finiteness nor zero-limit criteria.

**Sufficient analytic conditions.**

- Kanda–Forst: |I|≤M A with a finite constant M. The original transition-density version is survey Theorem 2.1, p.4; Rao's resolvent-density version is stated immediately after it. The stronger homogeneous sector inequality r≥c|I| implies this bound, but the conventional bound includes 1+r.
- Rao: B≤A f(A), where f is positive increasing and ∫_N^∞du/[u f(u)]=∞. Survey Theorem 2.3, p.4; original Rao (1988), Theorem 2, p.622. A bound |I|≤A g(A) with the corresponding divergent integral is enough after replacing f by 1+g. Examples include a constant, C(1+log u), and C(1+log u)(1+log log(eu)).
- Extended Kanda–Forst–Rao: I=h+g, |h|≤A f(A), and ∫|g(z)|/B(z)² dz<∞, with f as above. Survey Theorem 2.8, p.6, citing Hu–Sun–Zhang Theorem 4.5.
- Full-rank Q implies bounded continuous transition densities and a Kanda–Forst bound, hence (H): survey Theorem 2.5, p.5. The special finite-off-Gaussian-range class has the exact characterization in Theorem 2.6.
- In dimension one, sufficient conditions beyond pointwise sector control include liminf_{ε↓0}[∫_{−ε}^ε x²ν(dx)]/[ε/|log ε|]>0 (Theorem 2.19, p.9) and liminf_{|z|→∞}Re ψ(z)/[|z|/log|z|]>0 (Proposition 2.22, p.10). The latter is recorded here only in the one-dimensional setting of that subsection. Theorem 2.19's original locator in the survey repeats Theorem 2.2; the sums preprint actually labels it Theorem 2.3, p.7.

**Necessary and sufficient analytic conditions.** Under the resolvent-density hypothesis:

    (H) ⇔ E_λ(μ)→0 for every finite positive μ with E_1(μ)<∞.       (E)

This is survey Theorem 4.2, p.20, citing Hu–Sun–Zhang Theorem 5.1. Also,

    (H) ⇔ ∫ λ/[λ²+B(z)²] |μ̂(z)|² dz →0
           for every finite positive μ with E_1(μ)<∞.             (F)

This is survey Proposition 2.13, p.8, and Hu–Sun *Further study*, Proposition 2.2, p.5. The quantifier over all finite-energy measures is indispensable. The related exceptional-region criterion is Proposition 2.20, p.10: for any positive increasing f with the divergent integral above, (F) need only be checked on {B>A f(A)}. Survey Theorems 2.11–2.12, pp.7–8, give further necessary-and-sufficient logarithmic shell criteria; their sequences and constants can depend on μ. None asserts a uniform bound over directions from (H).

Another exact criterion, under bounded continuous transition densities, is Kanda's capacity characterization (survey Theorem 2.2, p.4): failure of (H) is equivalent to existence of a nonpolar compact set whose α-capacities remain bounded as α→∞. This quantifies a potential-theoretic obstruction; it is not a sector inequality.

For an explicit second check of (E)⇔(F), put

    D₁=(λ+r)²+I²,   D₂=λ²+(1+r)²+I²,   λ≥1.

One has D₂/2≤D₁≤2D₂: 2D₁−D₂=λ²−1+(4λ−2)r+r²+I²≥0, and 2D₂−D₁=(λ−r)²+4r+I²+2≥0. Consequently the integrals with kernels λ/D₁ and λ/D₂ vanish together. The remaining r/D₁ term of E_λ tends to zero by dominated convergence, since r/D₁≤A/B² and it tends to zero pointwise. This verifies the equivalence of the zero-limit criteria without confusing E_λ with just its λ numerator term.

**What is actually necessary.** A sector bound is not necessary in general. For a one-dimensional asymmetric Cauchy exponent

    ψ(u)=|u|+iκ u log|u|,   0<|κ|<2/π,

with ψ(0)=0, the sector ratio grows like |κ|log|u|. Nevertheless Re ψ=|u| gives bounded continuous densities, and B≤C A(1+log A), so Rao's theorem gives (H). This is also the class in Rao's Corollary 3, p.624. Failure of a sector inequality therefore cannot establish a counterexample.

The drift obstructions in Propositions 3.2–3.3 are necessary. If Q=0, ∫(1∧|x|)ν(dx)<∞, and all line projections satisfy (H), then d=−a−∫_{|x|<1}xν(dx)=0: the uncompensated projected drift is ⟨e,d⟩; applying Proposition 3.2 in dimension one and taking e=d/|d| rules out d≠0. This eliminates finite-variation candidates with a surviving deterministic drift. Zero drift alone is not asserted sufficient for every driftless jump process.

For a non-compound-Poisson process on R, the Kesten–Bretagnolle test is

    a singleton is nonpolar ⇔ ∫₀^∞ Re[1/(1+ψ(u))] du<∞.

Survey p.4, equation (2.1); Bretagnolle Theorem 7, printed p.32, PDF p.13. This is a hitting criterion, not (H). Bretagnolle Theorem 8, printed p.33, PDF p.14 (also sums paper Theorem 2.1, p.5) adds: with a Gaussian component, points are regular; in the infinite-variation pure-jump case, points are either polar or regular; in the finite-variation case with nonzero uncompensated drift, points can be hit but are not regular, so (H) fails. Compound Poisson processes have holding intervals, so every point is regular and their only semipolar set is empty. More generally, if every point is regular for itself, every nonempty set contains a regular point and no nonempty thin set exists; (H) follows. Merely being able to hit points is insufficient: pure drift is the simplest failure.

The proposed description in terms of X and its **dual** having the same polar sets plus unspecified “quasi-continuity” is not used as an equivalence. The source gives a precise different statement: bounded regularity of potentials is equivalent to (H) under its regularity assumptions (Theorem 1.1, p.2). Its Proposition 2.7 compares X with the **independent symmetrization** X−X̄, not the dual −X. For X_t=t and its dual −t on R, both have no nonempty polar set, yet both fail (H). Equality of polar sets with the dual alone thus proves nothing of the required kind.

5. Complete proofs of conditional affirmative answers

**A. Uniform directional sector theorem.** Assume X has Lebesgue resolvent densities. If there is M<∞ such that for every unit e and every real u,

    |Im ψ_e(u)|≤M[1+Re ψ_e(u)],

then X satisfies (H). Thus Question 1 has an affirmative answer under this extra quantitative hypothesis and the density assumption. In fact the directional (H) assumption becomes redundant under these stronger hypotheses.

Proof. Since ψ_e(u)=ψ(ue), take e=z/|z| and u=|z| for z≠0. At z=0 the inequality is automatic. Hence |I(z)|≤M A(z) globally and B²≤(1+M²)A². For λ≥1,

    0≤[λ+r]/[(λ+r)²+I²]≤1/(λ+r)≤1/A
      ≤(1+M²)A/B².

For each fixed z the left-hand kernel tends to zero. Multiplication by |μ̂|² and dominated convergence give E_λ(μ)→0 for every finite-energy μ. Criterion (E) gives (H). This also supplies a proof of the needed sector implication, instead of simply naming it. □

The same restriction identity turns a uniform directional Rao inequality

    |1+ψ_e(u)|≤[1+Re ψ_e(u)] f(1+Re ψ_e(u))

with a single admissible f into Rao's global hypothesis. That version follows immediately from the precisely cited Rao theorem.

A useful way to supply the density assumption is Re ψ(z)≥c|z|^α for |z|≥R, with c,α>0: exp(−t Re ψ) is integrable for every t>0, so Fourier inversion gives a bounded continuous transition density. Integrating these densities against exp(−λt)dt gives a resolvent density. Thus the directional-sector conclusion with this additional lower bound needs no unverified density assumption.

**B. Finite jumps outside a subspace.** Let 0<dim S<n, range(Q)⊆S and ν(S^c)<∞. If the two orthogonal projections X_S and X_{S^⊥} satisfy (H), then X satisfies (H). The converse follows from projection inheritance. In particular the original all-proper-projections assumption suffices in this class. This is the combination of survey Theorems 3.6–3.7, with the equality range(Q)=S included, not a general answer.

Here is a proof including the finite-jump and embedding steps. We use the standard reduction that a standard process has (H) if every **Borel thin** set is polar (Hu–Sun–Wang Lemma 2.1, pp.4–5); it handles the nearly Borel hulls in the definition.

First, if J is a zero-drift compound Poisson process independent of a Lévy process Y, then

    Y has (H) ⇔ Y+J has (H).                                    (CP)

For a Borel D, Y and Y+J have identical immediate hitting behavior from each start: their paths agree up to the first J-jump, which is strictly positive almost surely. In particular they have the same Borel thin sets.

Suppose Y has (H), and D is Borel thin for Y+J. It is polar for Y. Every translate D−j is also Y-polar, by spatial homogeneity. Condition on the entire J path; its jump times 0<T₁<T₂<⋯ are deterministic under this conditioning, with no finite accumulation. On each open interval between successive jumps, the Lévy Markov property of Y at the now fixed left endpoint, and polarity from every starting point, show that Y+J cannot enter D. This includes the interval (0,T₁). At a jump time T_k>0,

    P^x(Y_{T_k}+J_{T_k}∈D | J)=0,

because, for the conditioned positive time and shift, Y has zero probability of being in the translated polar set. Countably many intervals and jump endpoints exhaust all positive times. Thus D is polar for Y+J. This proves the forward implication of (CP).

Conversely, if Y+J has (H) and D is Borel thin for Y, it is polar for Y+J. If J's total jump rate is c, independence and the event of no jump before an integer m give

    exp(−cm) P^x(Y_t∈D for some 0<t≤m)
       ≤P^x(Y_t+J_t∈D for some 0<t≤m)=0.

Every m gives avoidance, so D is polar for Y. This proves the reverse implication. The rate-zero case is immediate. □

Second, embedding a Lévy process Y taking values in S as a process on R^n preserves (H). To see the needed direction, let D be ambient Borel thin. Every path started at x stays in the affine leaf x+S. The section (D−x)∩S is Borel thin for Y on S, since immediate hitting from every point in that leaf is zero. If Y on S has (H), this section is polar. Thus from every ambient starting point x, the process avoids D at positive times. The Borel-thin reduction proves (H) on R^n. The opposite direction follows in the same way or from projection inheritance.

Third, a nonzero deterministic motion bt fails (H) in every positive dimension. The singleton {0} is thin: from each starting point it can only be hit at one isolated positive time, or never, so the first positive hitting time is never zero. It is nonpolar because the start −b reaches it at time 1. The zero motion has (H), since every nonempty set contains a point where the process holds. By (CP), deterministic motion plus independent compound Poisson jumps has (H) exactly when its deterministic drift is zero.

Now remove the jumps in S^c from X using Lévy–Itô decomposition. Their intensity is finite. Thus X=Y+J with Y,J independent, J compound Poisson with Lévy measure ν|_{S^c}, and Y having covariance Q, jumps in S, and exponent drift a_Y=a+∫_{S^c,|x|<1}xν(dx). Its projection onto S^⊥ is deterministic motion with velocity

    P_{S^⊥}d_S,   d_S=−a−∫_{S^c,|x|<1}xν(dx).

Since X_{S^⊥}=P_{S^⊥}Y+P_{S^⊥}J has (H), (CP) and the deterministic-motion observation force P_{S^⊥}d_S=0. Hence Y actually takes values in S. On S, X_S=Y+P_S J; this has (H), so the reverse implication of (CP) gives (H) for Y on S. Embed Y in R^n and use the forward implication of (CP) to conclude (H) for X. No independence of X_S and X_{S^⊥} was assumed. □

For range(Q)=G with 0<dim G<n and ν(G^c)<∞, the all-line hypothesis alone forces P_{G^⊥}d_G=0: choose a line in G^⊥ in its direction if it is nonzero. That line projection would be deterministic motion plus compound Poisson and fail (H). Once d_G∈G, Y on G has a full-rank Gaussian component and (H) by Theorem 2.5; embedding and (CP) finish. If Q=0 and ν is finite, the same argument forces d_G=0 and X is compound Poisson. This reproves the all-lines part of Theorem 3.6, including its rank-zero case.

**C. A complete check of symmetric stable noise plus drift and finite jumps.** Let S be a full-dimensional symmetric α-stable Lévy process, 0<α≤2, and assume its real exponent q is continuous, homogeneous q(rz)=r^αq(z), and positive for z≠0. Let X_t=S_t+bt+J_t with independent zero-drift compound Poisson J.

If α≥1, X has (H) for every b. If 0<α<1, X has (H) exactly when b=0; when b≠0, at least one line projection fails (H). Consequently this family gives no counterexample to Question 1.

Proof. Positivity and compactness of the unit sphere give q(z)≥c|z|^α with c>0. The characteristic functions are integrable and the preceding Fourier argument supplies transition/resolvent densities. For α≥1, r/(1+cr^α) is bounded on [0,∞), so |⟨b,z⟩|≤C[1+q(z)]. J contributes at most its finite total rate in absolute imaginary part and contributes a nonnegative real part. Theorem A gives (H). For b=0 the same argument works for every α>0.

For α<1 the symmetric stable process has finite-variation paths and zero uncompensated drift: its stable Lévy measure has finite ∫_{|x|<1}|x|ν(dx), by ∫₀¹r·r^(−1−α)dr<∞; symmetry cancels the drift. Adding zero-drift J preserves this property. If b≠0, project onto e=b/|b|. This is a one-dimensional finite-variation Lévy process with nonzero uncompensated drift |b|. Proposition 3.2, or Bretagnolle's classification above, excludes (H) for that projection. Projection inheritance also excludes (H) for X. □

For completeness the radial sector factor has supremum 1/c when α=1, and (α−1)^((α−1)/α)/(α c^(1/α)) when α>1, found by differentiating r/(1+cr^α). When α<1 this factor diverges, consistent with the drift obstruction. This checks both the high-frequency sign and the limiting case α=1.

6. Counterexample attempts and numerical evidence

**Correlated Gaussian motion.** The exact exponent for survey Example 3.5 is

    ψ₀(z₁,z₂)=(z₁+z₂)²−i(z₁−z₂).

Indeed Q=[[2,2],[2,2]], and the physical velocity (1,−1) contributes the negative imaginary term. Along a unit direction e=(cos θ,sin θ), put p=cos θ+sin θ and q=cos θ−sin θ. Then

    ψ_e(u)=p²u²−iqu.

When p≠0 the projected Gaussian variance is 2p²>0 and it has (H). At p=0, the projection is nonzero deterministic motion and fails (H). The ambient failure can also be checked directly without an analytic criterion: F={x₁=x₂} is thin because x₁(t)−x₂(t)=x₁(0)−x₂(0)+2t crosses 0 at at most one positive time, never immediately. Starting at (−1,1) hits F at time 1 with probability one. Thus F is thin and nonpolar. This provides a second, set-theoretic check of the failure.

For p≠0 the exact sector supremum on the ray is

    sup_{u∈R} |qu|/(1+p²u²)=|q|/(2|p|),

attained at |u|=1/|p|. Near θ=−π/4+δ this is |cot δ|/2. At δ=0 it is infinite. A finite list of directions can therefore miss the failing projection entirely. Even knowing (H) on all but one line is insufficient.

**Adding transverse Gaussian noise.** The regularized exponent

    ψ_ε(z)=(z₁+z₂)²+ε(z₁−z₂)²−i(z₁−z₂),   ε>0,

has Q_ε=2[[1+ε,1−ε],[1−ε,1+ε]], eigenvalues 4 and 4ε. It has (H) by the full-rank theorem. Its exact global sector supremum is 1/(2√ε): on a ray the supremum is |q|/[2√(p²+εq²)], bounded by that value and attaining it at p=0. It diverges as ε↓0. These processes converge to ψ₀, which fails (H); (H) must not be assumed closed under this limit.

**Stable noise and finite jumps.** Theorem C checks the full family in the question's suggested direction, including its finite-variation drift. Adding finite jumps cannot hide the exceptional deterministic projection, by (CP). Adding full-dimensional Brownian noise makes (H) true for the entire process. Adding full-dimensional symmetric stable noise of index at least one likewise gives (H). Stable noise below index one leaves a nonzero drift obstruction visible in a line projection. A nonlinear support curve for a Lévy measure is not itself a proof that the resulting Lévy paths have a thin nonpolar range; such a construction would require a specified fixed set and hitting/regularity proof. No such candidate was established here.

The script code/sector_checks.py uses standard-library arithmetic, one thread, inherited nice 10. It checks 196 covariance identities with exact rational arithmetic, then ray maximization identities numerically in 3,600 offset directions for each of ε=0,10⁻⁸,10⁻⁴,1. It separately includes the exact exceptional direction and compares the near-exceptional formula with |cot δ|/2 down to δ=10⁻⁶. It also evaluates five isotropic stable-plus-drift/compound-Poisson cases on 720 directions and 121 logarithmic radii from 10⁻⁶ to 10¹². The finite-jump measure there is 0.7 δ_(1,2). Large-frequency trigonometric evaluations use ordinary floating-point arithmetic; they are illustrations, not certified enclosures.

| ε | Largest ray supremum on offset grid | Exact global supremum |
|---|---:|---:|
| 0 | 4065.040629913476 | ∞ |
| 10⁻⁸ | 3154.150413151065 | 5000 |
| 10⁻⁴ | 49.996218179070226 | 50 |
| 1 | 0.49999999621775004 | 0.5 |

At the exceptional direction with ε=0 the measured ratios at radii 1,100,10⁴,10⁶ are √2 times those radii, agreeing with the exact linear divergence. Maximum relative error of the radial identity in the four direction grids was below 1.1×10⁻¹³. A separate exact-rational check verified the two energy-kernel identities and inequalities in 80 parameter cases (code/check_energy_identities.py, data/energy_identity_checks.json). These cases check arithmetic; the proof above establishes the inequalities for all parameters. Peak resident memory reported by the numerical script was 19,021,824 bytes on this run. Raw results are in data/sector_results.json and data/gaussian_direction_checks.csv. The analytic formulas, not the grids, establish the global statements.

7. What the projection assumption still does not give

The restriction ψ_e(u)=ψ(ue) supplies pointwise access to ψ but not a common sector constant, a common Rao function, or a bound on arbitrary ambient finite-energy measures. In particular, individual (H) statements do not even imply individual sector bounds, as the asymmetric Cauchy example shows. Compactness of the unit sphere does not turn an unspecified (H) criterion into a uniform estimate over the unbounded frequency variable u.

There is a concrete integration obstruction to a naive use of criterion (E). Polar coordinates introduce the weight |u|^(n−1) in the ambient frequency integral. A measure μ of finite ambient energy does give finite energy of its projected measure on almost every line (the extra weight only strengthens tail integrability). However, the projected (H) statement controls the **unweighted** one-dimensional energy limit. It supplies neither the radial weight needed for the ambient limit nor an angular dominating function. Interchanging the limit with these weighted integrals is an unproved step. No such interchange is used in this report.

Likewise, the two orthogonal projections need not be independent. Replacing their joint law by an independent product changes ψ. Even the independent-product problem with merely (H) factors is left open in the source. The finite-off-subspace proof avoids that replacement by decomposing the Lévy jump measure, where independence is justified by disjoint parts of the Poisson random measure.

The general question remains unresolved by this work. The result is PARTIAL because there are complete conditional proofs, an audited literature inventory, and exclusions of the proposed elementary counterexample families, but no proof under the original hypothesis alone and no process meeting that hypothesis while failing (H).

8. Verification and reproduction

Run `python3 -B code/sector_checks.py` to reproduce the numerical evidence, and `python3 -B code/check_energy_identities.py` for the exact energy-identity checks. Run `python3 -B code/audit_sources.py` for an independent extraction with pdftotext of survey pp.15–18, hash comparison with the original input, key statement/page checks, and a check that sources/ contains only UTF-8 text. `python3 -B code/fetch_text.py URL STEM` retrieves a source as plain text using pypdf; no PDF is written. The extractor caps downloaded inputs at 25 MiB. The numerical work uses one thread and is far below 4 GB. No publication, pushes, external messages or subagents were used.

The audit distinguishes exact rational identities, mathematical proofs using explicitly cited theorems, and finite floating-point evidence. Some historical originals and Jacob's book were unavailable; their statements are attributed to the survey, with that limitation recorded above. Selected raw search responses are retained in data/web_search_results.json; they are not a complete bibliographic database.

Task: “Open problem E0022” — 13 November 2026, intake recorded at 10:56 Asia/Tbilisi (workspace intake time; no timestamp was supplied in the request text).
