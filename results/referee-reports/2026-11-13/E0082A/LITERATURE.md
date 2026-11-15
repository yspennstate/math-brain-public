# Literature search, 13 November 2026

No printed exact solution to both parts of Open problem 2.3 was located. This is a bounded search, not a proof that no such work exists. The bridge constant below is built from established Slepian formulas; novelty is not claimed. The first-passage order proof reuses **internal E0081**, not a literature resolution.

## Source and published version

Jim Pitman and Wenpin Tang, *Patterns in random walks and Brownian motion*, [arXiv:1411.0041v3](https://arxiv.org/abs/1411.0041v3), revised 10 September 2015. Definitions: pp. 5–6. Matching matrix: equations (2.1)–(2.2), Theorem 2.1, equations (2.3)–(2.4), p. 7. Open problem 2.3: p. 13. Bridge scaling argument: Proposition 2.4 and Lemma 2.5, pp. 13–14. First-passage overlap count: equation (2.21), p. 12. First-passage bounds: Theorem 1.8(4), p. 6, give orders n and n^(5/4).

Published in *In Memoriam Marc Yor — Séminaire de Probabilités XLVII*, Lecture Notes in Mathematics 2137 (2015), pp. 49–88, [DOI](https://doi.org/10.1007/978-3-319-18585-9_4). Author-hosted published text saved as `sources/pitman_tang_published.txt`. Matching formula: Theorem 6, equations (8)–(9), **p. 57**; definitions start on p. 56. Open problem 2.3 is renumbered **Open Problem 1, p. 65**. On the same page, **Conjecture 1 (Peres), equation (30)**, explicitly predicts

    c_alpha n ln n <= E T(FP^{alpha,n}) <= C_alpha n ln n.

The published chapter therefore directly contradicts the task's premise of a known linear upper bound for FP. It does not give a sharp first-passage constant. Its Proposition 1 and Lemma 2, pp. 66–67, are the bridge scaling argument. Its Table 1 on p. 65 is not used as evidence: several entries violate the exact lower bound derived here.

## Citation trail, 2014–2026

OpenAlex DOI lookup W1851725789, retrieved during this run, returned four citing records. The raw responses are `data/openalex_source.json` and `data/openalex_citers.json`. Citation databases may omit works or split preprint and published records. Semantic Scholar returned HTTP 429. Title and phrase searches were also made without a date restriction, including the terms exact asymptotics, matching matrix, first passage, and n log n.

1. Pitman and Tang, *The Slepian zero set, and Brownian bridge embedded in Brownian motion by a spacetime shift*, EJP 20 (2015), paper 61, [arXiv:1411.0040](https://arxiv.org/abs/1411.0040). Proposition 2.1 (p. 4) restates bridge convergence. Section 3, equations (3.2)–(3.4), p. 6, records Shepp's determinant integrals for first Slepian zeros. It does not print the requested two sharp waiting-time asymptotics. In reproducing the noninteger formula use the original Shepp heat-kernel duration 1-theta in the second determinant.
2. Evans, Pitman and Tang, *The spans in Brownian motion*, AIHP 53 (2017), 1108–1135, [arXiv:1506.02021](https://arxiv.org/abs/1506.02021). Concerns possible Brownian loop lengths, not the two waiting-time equivalents. Full text saved and searched for waiting, matching, bridge, first passage, and asymptotics.
3. Pitman and Tang, *The argmin process of random walks, Brownian motion and Lévy processes*, EJP 23 (2018), paper 60, [arXiv:1610.01524](https://arxiv.org/abs/1610.01524). Gives the Markov argmin process and extrema decompositions, not these equivalents. Full text saved and searched with the same terms.
4. Wenpin Tang, *Continuous paths in Brownian motion and related problems*, Berkeley dissertation (2017), [repository record](https://escholarship.org/uc/item/51j6244c). Repository PDF retrieval returned 403, and a guessed author-hosted thesis URL returned 404. Search-index text confirms the earlier exponent-gap discussion. Internal E0081 reports Conjecture 2.5.2 in the thesis, but that numbering was **not independently verified here** and is not used as a literature theorem.

No relevant 2019–2026 resolution appeared in the title/phrase search. This negative result is limited by the index and access restrictions above.

## Classical and later family-pattern formulas

* Guibas and Odlyzko, *String overlaps, pattern matching, and nontransitive games*, JCTA 30 (1981), 183–208, [publisher](https://doi.org/10.1016/0097-3165(81)90005-4). Publisher abstract and author bibliography checked: correlation polynomials and finite forbidden-pattern generating functions. A guessed author PDF returned 404; no claim to have inspected its full text or verified a theorem number. These general identities do not themselves evaluate a growing bridge/first-passage family.
* S.-Y. R. Li, *A martingale approach to the study of occurrence of sequence patterns in repeated experiments*, Ann. Probab. 8 (1980), 1171–1176, [DOI](https://doi.org/10.1214/aop/1176994578). Original full text inaccessible through attempted Euclid endpoint. The family identity is independently available as Theorems 2.1–2.2, p. 4, of Pozdnyakov, Glaz, Kulldorff and Steele, *A martingale approach to scan statistics* (saved author manuscript): solve the leading-number system and sum the solution to obtain reciprocal mean; the transpose system gives first-hit probabilities. Ostaszewska–Zajkowski also explicitly attributes the stopping-probability system to Li's Theorem 3.1.
* Gerber and Li, *The occurrence of sequence patterns in repeated experiments and hitting times in a Markov chain*, SPA 11 (1981), 101–108. [Publisher abstract](https://doi.org/10.1016/0304-4149(81)90025-9) describes the finite-family/Markov-chain reduction. Bibliography verified from the source and publisher metadata; original theorem numbers not claimed.
* P. Tolstrup Nielsen, *On the expected duration of a search for a fixed pattern in random data*, IEEE Trans. Information Theory 19 (1973), 702–704. [Author/institution copy](https://backend.orbit.dtu.dk/ws/files/4640102/PNielsen.pdf), full text saved. Theorem I, p. 703, expresses the single-word mean through its bifix lengths. This is not a large-family asymptotic.
* Chen and Zame, *On fair coin-tossing games*, J. Multivariate Analysis 9 (1979), 150–156, [publisher](https://doi.org/10.1016/0047-259X(79)90073-3). Abstract/metadata checked; finite word races and Conway algorithm, not these asymptotics. Original full text not obtained; no theorem-number claim.
* Banjevic, *Pattern recognition in Markov chains*, in *Runs and Patterns in Probability* (1994), 213–230; and *Recursive relations for the distribution of waiting times in a Markov chain*, J. Appl. Probab. 33 (1996), 48–56, [publisher](https://doi.org/10.2307/3215263). Primary publisher abstract and references checked; recursive finite-chain formulas. Full text of the 1994 chapter not obtained.
* Breen, Waterman and Zhang, *Renewal theory for several patterns*, J. Appl. Probab. 22 (1985), 228–234. This is the explicit source cited by Pitman–Tang for Theorem 2.1. Bibliography checked in Pitman–Tang; original theorem numbering not verified.
* Ostaszewska and Zajkowski, *On the waiting time till some patterns occur in i.i.d. sequences*, [arXiv:1302.4859](https://arxiv.org/abs/1302.4859), full text saved. Theorem 2.3 and Corollary 2.4 give finite-family correlation/determinant formulas. No bridge or first-passage scaling equivalent is printed.
* Yoshida, *A simple proof of the formula of Solov'ev–Nielsen–Blom for the expected waiting time*, [arXiv:2410.13426](https://arxiv.org/abs/2410.13426), Theorem 1.1, p. 1: single-word bifix recursion. Full text saved; does not resolve the growing families.
* Kim, Kim and Kim, *Waiting Time Problems for Patterns in a Sequence of Multi-State Trials*, Mathematics 8 (2020), 1893, [publisher](https://www.mdpi.com/2227-7390/8/11/1893). Publisher full text inspected for scope: finite compound patterns in multi-state trials. No claimed BR/FP equivalent.

## Slepian boundary crossing

L. A. Shepp, *First passage time for a particular Gaussian process*, Ann. Math. Statist. 42 (1971), 946–951, [author-hosted copy](https://faculty.wharton.upenn.edu/wp-content/uploads/2012/04/First-passage-time_.pdf). Full text saved. Equations **(2.15)–(2.16), p. 949**, give the integer-time determinant; equations **(2.25)–(2.26), p. 950**, give noninteger time. These are exact continuum probabilities, not a printed theorem asserting the requested discrete equivalents. The report derives a convergent explicit integral series from them and proves the bridge mean limit.

Noonan and Zhigljavsky, *Approximating Shepp's constants for the Slepian process*, Stat. Probab. Lett. 153 (2019), 21–31, [publisher](https://doi.org/10.1016/j.spl.2019.05.001). Publisher abstract and introduction checked. These constants describe exponential decay as observation horizon tends to infinity, a different limit from n tending to infinity here.

## Internal prior work

Memory `e0081_pitman_tang_first_passage_pattern_n_log_n_proved_2026_11_12` was read in full. It concerns exactly FP^{alpha,n}, rather than a different related family. It supplies the record-range method reconstructed and proved in REPORT.md. This is cited only as internal prior work. No internal claim, review, or reported public upload is treated as a published literature theorem.
