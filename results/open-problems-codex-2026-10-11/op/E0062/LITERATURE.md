
## API searches, 2026-10-12

Status conclusion: **no full solution verified**. This bounded search does
not establish that no solution exists. In particular, inaccessible recent
papers below remain leads. Nothing here qualifies for SOLVED_IN_LITERATURE.
The attempt now independently proves opposing every-point behaviour for
two matrices with identical signs and zeros; this is a partial result, not
a full answer in print. No novelty is claimed for the special-case proofs.

Fetch-validation correction: the Saburov 2015 URL returned HTTP 200 but its
1052-byte body is an Incapsula denial page, not the article PDF. PyMuPDF
accepted the HTML as a one-page document and extracted only “Request
unsuccessful.” The Springer 2026 article page likewise returned a browser
challenge. The automatic log's “OK ... bytes” means transport success only;
neither full article was obtained or checked. Metadata was obtained from
the bibliographic APIs. The two arXiv PDFs were substantive article text.

## Exact source and load-bearing literature

1. R. N. Ganikhodzhaev and U. A. Rozikov, *Quadratic Stochastic Operators:
Results and Open Problems*, arXiv:0902.4207v2, 12 March 2009.
Fetched https://arxiv.org/pdf/0902.4207 to source.pdf and extracted source.txt.
Equation (7) and bounds |a_ij|≤1 occur on PDF p. 2; Problem 5 on PDF p. 4.
It says, word for word (mathematical typesetting normalized):
“Find necessary and sufficient conditions on matrix A of Volterra QSO under
which the ergodic theorem is true for the Volterra QSO on S^{m−1}, m ≥ 2.”
This question has no transversality or nonzero-entry assumption.

2. N. N. Ganikhodzhaev and D. V. Zanin, *On a necessary condition for the
ergodicity of quadratic operators defined on a two-dimensional simplex*,
Russian Mathematical Surveys **59** (2004), no. 3, 571–572,
DOI 10.1070/RM2004v059n03ABEH000744. Source reference [3].
The theorem we use is stated explicitly as Theorem 3 in the source, PDF p. 4:
“If the parameters a, b, c for the Volterra QSO (9) have the same sign
and each is non-zero, then the ergodic theorem will fail for this operator.”
This gives only the cyclic-three-species obstruction. Section 2 of ATTEMPT.md
maps its parameters to a directed-triangle face line by line. It does not
solve Problem 5, and we do not attribute a sufficiency theorem to this note.
The original note was checked in earlier brain work; in this run the
published survey's exact theorem is the directly fetched dependency.

3. M. Saburov, *On Regularity, Transitivity, and Ergodic Principle for
Quadratic Stochastic Volterra Operators*, arXiv:1111.3101 (2011).
Fetched regularity2011.pdf and regularity2011.txt.
PDF p. 4 explicitly states: “In the sequel, we will only consider transversal
quadratic stochastic Volterra operators without mentioning transversality.”
The unnumbered main theorem, PDF p. 5, equates regularity, transitivity,
the Ergodic principle, and |V^{n+1}x−V^n x|→0. The Ergodic principle,
defined on PDF p. 4, is |V^n x−V^n y|→0 for equal-support x,y.
This is a different condition from convergence of time averages, and
transversality excludes the zero-entry matrices crucial to Problem 5.
It is relevant prior art for our nonzero-entry special case, not a full answer.

4. N. N. Ganikhodjaev and D. V. Zanin, *Ergodic Volterra quadratic
transformations of symplex*, arXiv:1205.3841 (2012, Russian).
Fetched gz2012.pdf and gz2012.txt. PDF p. 1 says it concerns the
three-dimensional simplex, i.e. four types. Definition 1, PDF p. 2,
uses generic initial points and arbitrary continuous observables. The
earlier repository memo identifies its standing exclusion of zero entries.
Thus neither its dimension nor its quantifier covers E0062 as posed.
Do not infer every-point ergodicity from generic-point ergodicity: faces
with cyclic triples supply explicit obstructions to that inference.

5. N. N. Ganikhodjaev and D. V. Zanin, *Ergodic Volterra Quadratic
Mappings of the Simplex*, in *Networks, Games, and Dynamics*, Trends in
Mathematics, Springer (2025), DOI 10.1007/978-3-032-09176-5_9.
Crossref page range: 233–246.
Crossref metadata fetched in gz2025.response confirms this recent chapter.
The earlier memo calls it an English republication of the preceding work.
We have not independently checked the full chapter; its title or metadata
alone cannot establish a solution to the general every-point question.

6. M. Saburov, *On divergence of any order Cesàro mean of Lotka–Volterra
operators*, Annals of Functional Analysis **6** (2015), no. 4, 247–254,
DOI 10.15352/afa/06-4-247. OpenAlex identifies an open PDF at Project Euclid;
fetch outcome recorded under the targeted follow-up below. A class of
nonergodic operators and higher-order divergence are leads; neither a
title nor the earlier memo establishes a general necessary-and-sufficient
matrix criterion.

7. M. Saburov, *A class of nonergodic Lotka–Volterra operators*,
Mathematical Notes (2015), DOI 10.1134/S0001434615050107.
OpenAlex abstract says it provides a nonergodic class including prior
examples; full text not checked. C. H. Pah and A. Rosli, *On a Class of
Non-Ergodic Lotka–Volterra Operator*, Lobachevskii Journal of Mathematics
(2022), DOI 10.1134/S1995080222120228, likewise concerns a particular class.
Both are leads, not verified full characterizations.

8. M. Saburov and Kh. Saburov, *Ganikhodjaev’s Conjecture on Mean
Ergodicity of Quadratic Stochastic Operators*, Lobachevskii Journal of
Mathematics (2020), DOI 10.1134/S1995080220060165; a 2019 version has
DOI 10.56017/2181-1318.1032. The abstract explicitly describes counterexamples
for properly non-Volterra operators, a different question.

9. R. N. Ganikhodzhaev, S. I. Masharipov and J. X. Bekturdiyeva,
*DEGENERATE CASES IN LOTKA–VOLTERRA SYSTEMS ACTING IN THE SIMPLEX S^3*,
Journal of Mathematical Sciences (2026), DOI 10.1007/s10958-026-08340-3.
Found among the 2011 survey's citations. Full theorem not checked;
four-type degeneracy is potentially useful but is not the arbitrary-m answer.
K. Solijanova, *DEGENERATE FIXED-POINT CONFIGURATIONS OF A DISCRETE
LOTKA–VOLTERRA OPERATOR*, Journal of Mathematical Sciences (2026),
DOI 10.1007/s10958-026-08610-0; Crossref metadata fetched. Fixed-point
classification does not by itself prove convergence of averages.
Its references also give useful 2025 leads:
R. N. Ganikhodzhaev, D. B. Eshmamatova, D. Akhmedova and U. R. Muminov,
*Linear homogeneous inequalities and trajectory routes of the degenerate
Lotka–Volterra operators*, Lobachevskii J. Math. **46** (2025), no. 3,
1257–1265, DOI 10.1134/S1995080225605272; and U. R. Muminov,
D. B. Eshmamatova, L. D. Sharipova and Y. A. Islamov, *Dynamics of
degenerate quadratic Lotka–Volterra mappings acting in a four-dimensional
simplex and bigraphs*, J. Quality Measurement and Analysis **21** (2025),
no. 2, 79–92, DOI 10.17576/jqma.2102.2025.07. These references have not
been read in full and remain follow-up leads.

## Local brain and prior-work searches (all 2026-10-12)

Continuation recall, 2026-10-12: math_recall.py query
“Volterra degenerate four cycle Cesaro ergodic”. The returned relevant
cards were the previously known E0061 three-species sufficiency and its
citation warning; the remaining matches were off-topic. No new theorem
addressing the general zero-entry criterion was returned. Treated as hints
only, and the source Theorem 3 dependency remains explicit.

Additional arXiv lead: N. N. Ganikhodjaev, U. U. Jamilov and
R. T. Mukhitdinov, *Hamiltonian Cycle on the Set of Genotypes and
Non-Ergodic Quadratic Stochastic Operators*, arXiv:1204.1809 (2012).
The fetched arXiv API abstract explicitly restricts the proved result to
m=2,3,4. The earlier memo additionally identifies extremal coefficients
and generic-point conventions. We did not verify the full paper in this
run; it is not a general arbitrary-m every-point zero-entry solution.

- brain.py recall: “Volterra quadratic stochastic operators ergodic theorem”.
- brain.py recall: “Volterra ergodic theorem mistakes”.
- math_recall.py: “Volterra ergodic tournament”.
- brain.py node: volterra_qso_ergodic_theorem_sufficiency_proved_2026_09_08.
- rg search for E0062|E0061 in probability_1000_intake_* and codex_pool_2026_10_10.
  The first wildcard-path command failed under Windows; reran by enumerating
  intake directories, yielding the E0062-A001 and E0061-A001/A002/A003 records.
- git ls-tree origin/master, then filename filter E0062|volterra|E0061.
- git show origin/master:prob1000_lean_20260908/ultracode_20260909/E0062/memo.md.
  Read only; its numerical claims were not promoted to proofs.
- Local extracted-paper searches for Theorem, transversality, ergodicity,
  transitivity and author names. API response files, search_log.json,
  literature_search_output.txt, followup_output.txt and targeted_output.txt
  retain raw evidence and reproducible queries.

## API search log

- OpenAlex; query: `Volterra quadratic stochastic operators ergodic theorem`; URL: https://api.openalex.org/works?search=Volterra%20quadratic%20stochastic%20operators%20ergodic%20theorem&per-page=30; OK 453416 bytes; saved openalex_0.response

- Crossref; query: `Volterra quadratic stochastic operators ergodic theorem`; URL: https://api.crossref.org/works?query=Volterra%20quadratic%20stochastic%20operators%20ergodic%20theorem&rows=15; OK 76753 bytes; saved crossref_0.response

- Semantic Scholar; query: `Volterra quadratic stochastic operators ergodic theorem`; URL: https://api.semanticscholar.org/graph/v1/paper/search?query=Volterra%20quadratic%20stochastic%20operators%20ergodic%20theorem&limit=20&fields=title,authors,year,url,abstract,externalIds; ERROR HTTPError: HTTP Error 429: 

- GitHub; query: `Volterra quadratic stochastic operators ergodic theorem`; URL: https://api.github.com/search/repositories?q=Volterra%20quadratic%20stochastic%20operators%20ergodic%20theorem&per_page=10; OK 55 bytes; saved github_0.response

- OpenAlex; query: `Volterra quadratic stochastic operators transitive ergodicity`; URL: https://api.openalex.org/works?search=Volterra%20quadratic%20stochastic%20operators%20transitive%20ergodicity&per-page=30; OK 466072 bytes; saved openalex_1.response

- Crossref; query: `Volterra quadratic stochastic operators transitive ergodicity`; URL: https://api.crossref.org/works?query=Volterra%20quadratic%20stochastic%20operators%20transitive%20ergodicity&rows=15; OK 105276 bytes; saved crossref_1.response

- Semantic Scholar; query: `Volterra quadratic stochastic operators transitive ergodicity`; URL: https://api.semanticscholar.org/graph/v1/paper/search?query=Volterra%20quadratic%20stochastic%20operators%20transitive%20ergodicity&limit=20&fields=title,authors,year,url,abstract,externalIds; OK 21194 bytes; saved semantic_1.response

- GitHub; query: `Volterra quadratic stochastic operators transitive ergodicity`; URL: https://api.github.com/search/repositories?q=Volterra%20quadratic%20stochastic%20operators%20transitive%20ergodicity&per_page=10; ERROR HTTPError: HTTP Error 403: rate limit exceeded

- OpenAlex; query: `Volterra operators Ulam ergodic necessary sufficient`; URL: https://api.openalex.org/works?search=Volterra%20operators%20Ulam%20ergodic%20necessary%20sufficient&per-page=30; OK 491154 bytes; saved openalex_2.response

- Crossref; query: `Volterra operators Ulam ergodic necessary sufficient`; URL: https://api.crossref.org/works?query=Volterra%20operators%20Ulam%20ergodic%20necessary%20sufficient&rows=15; OK 135540 bytes; saved crossref_2.response

- Semantic Scholar; query: `Volterra operators Ulam ergodic necessary sufficient`; URL: https://api.semanticscholar.org/graph/v1/paper/search?query=Volterra%20operators%20Ulam%20ergodic%20necessary%20sufficient&limit=20&fields=title,authors,year,url,abstract,externalIds; ERROR HTTPError: HTTP Error 429: 

- GitHub; query: `Volterra operators Ulam ergodic necessary sufficient`; URL: https://api.github.com/search/repositories?q=Volterra%20operators%20Ulam%20ergodic%20necessary%20sufficient&per_page=10; ERROR HTTPError: HTTP Error 403: rate limit exceeded

- arXiv; query: `all:Volterra AND (all:ergodic OR all:ergodicity)`; URL: http://export.arxiv.org/api/query?search_query=all%3AVolterra%20AND%20%28all%3Aergodic%20OR%20all%3Aergodicity%29&start=0&max_results=50; OK 45185 bytes; saved arxiv.response

- arXiv; query: `all:Volterra AND (all:ergodic OR all:ergodicity)`; URL: https://export.arxiv.org/api/query?search_query=all%3AVolterra%20AND%20%28all%3Aergodic%20OR%20all%3Aergodicity%29&start=0&max_results=50; OK 45185 bytes; saved arxiv_https.response

- OpenAlex; query: `Quadratic stochastic operators results and open problems`; URL: https://api.openalex.org/works?search=Quadratic%20stochastic%20operators%20results%20and%20open%20problems&per-page=10; OK 148518 bytes; saved source_lookup.response

## Source citation searches and paper fetches

- 2026-10-12; paper; query: arXiv:1111.3101; URL: https://arxiv.org/pdf/1111.3101; OK 230968 bytes
- 2026-10-12; paper; query: arXiv:1205.3841; URL: https://arxiv.org/pdf/1205.3841; OK 146266 bytes
- 2026-10-12; OpenAlex; query: works citing W1544252356, page 1; URL: https://api.openalex.org/works?filter=cites:W1544252356&per-page=100&page=1&select=id,title,publication_year,doi,authorships,open_access,primary_location,abstract_inverted_index; OK 114643 bytes
- 2026-10-12; OpenAlex; query: works citing W2081343974, page 1; URL: https://api.openalex.org/works?filter=cites:W2081343974&per-page=100&page=1&select=id,title,publication_year,doi,authorships,open_access,primary_location,abstract_inverted_index; OK 447100 bytes
- 2026-10-12; OpenAlex; query: works citing W2081343974, page 2; URL: https://api.openalex.org/works?filter=cites:W2081343974&per-page=100&page=2&select=id,title,publication_year,doi,authorships,open_access,primary_location,abstract_inverted_index; OK 456520 bytes
- 2026-10-12; OpenAlex; query: works citing W2081343974, page 3; URL: https://api.openalex.org/works?filter=cites:W2081343974&per-page=100&page=3&select=id,title,publication_year,doi,authorships,open_access,primary_location,abstract_inverted_index; OK 146534 bytes

## Targeted follow-up

- 2026-10-12; paper; query: Saburov 2015 higher-order means; URL: https://projecteuclid.org/journals/annals-of-functional-analysis/volume-6/issue-4/On-divergence-of-any-order-Ces%c3%a0ro-mean-of-Lotka/10.15352/afa/06-4-247.pdf; OK 1052 bytes
- 2026-10-12; Crossref; query: DOI 10.1007/s10958-026-08610-0; URL: https://api.crossref.org/works/10.1007/s10958-026-08610-0; OK 9447 bytes
- 2026-10-12; publisher; query: DEGENERATE FIXED-POINT CONFIGURATIONS OF A DISCRETE LOTKA–VOLTERRA OPERATOR; URL: https://link.springer.com/article/10.1007/s10958-026-08610-0; OK 3038 bytes
- 2026-10-12; Crossref; query: DOI 10.1007/978-3-032-09176-5_9; URL: https://api.crossref.org/works/10.1007%2F978-3-032-09176-5_9; OK 7898 bytes
- 2026-10-12; OpenAlex; query: Volterra quadratic stochastic four cycle zero coefficients ergodic; URL: https://api.openalex.org/works?search=Volterra%20quadratic%20stochastic%20four%20cycle%20zero%20coefficients%20ergodic&per-page=20; OK 411131 bytes
- 2026-10-12; OpenAlex; query: Volterra ergodic theorem necessary sufficient 2025 2026; URL: https://api.openalex.org/works?search=Volterra%20ergodic%20theorem%20necessary%20sufficient%202025%202026&per-page=20; OK 341615 bytes
- 2026-10-12; OpenAlex; query: Volterra quadratic stochastic operators product Lyapunov four species; URL: https://api.openalex.org/works?search=Volterra%20quadratic%20stochastic%20operators%20product%20Lyapunov%20four%20species&per-page=20; OK 394276 bytes

## Additional on-topic bibliographic leads from API results

The following are metadata leads, not full-text theorem verifications. Duplicated versions can have distinct API identifiers. None is classified as a literature solution.

- Utkir Abdulloevich Rozikov; N. B. Shamsiddinov. *On Non-Volterra Quadratic Stochastic Operators Generated by a Product Measure* (2006). https://doi.org/10.48550/arxiv.math/0608201.
- Farrukh Maksutovich Mukhamedov; Mansoor Khajibaevich Saburov. *Stability and monotonicity of Lotka-Volterra type operators* (2009). https://doi.org/10.48550/arxiv.0912.3321.
- Mansoor Khajibaevich Saburov. *On Regularity, Transitivity, and Ergodic Principle for Quadratic Stochastic Volterra Operators* (2011). https://doi.org/10.48550/arxiv.1111.3101.
- Mansoor Khajibaevich Saburov. *Some Strange Properties of Quadratic Stochastic Volterra Operators* (2013). https://openalex.org/W1510704178.
- Malaysian Mathematical; Farrukh Maksutovich Mukhamedov; Mansoor Khajibaevich Saburov. *On Dynamics of Lotka-Volterra Type Operators* (2014). https://openalex.org/W128428155.
- Mansoor Khajibaevich Saburov. *A class of nonergodic Lotka-Volterra operators* (2015). https://doi.org/10.1134/s0001434615050107.
- Uygun Umurovich Jamilov; M. Ladra. *Non-Ergodicity of Uniform Quadratic Stochastic Operators* (2015). https://doi.org/10.1007/s12346-015-0145-0.
- Mansoor Khajibaevich Saburov. *On divergence of any order Cesàro mean of Lotka--Volterra operators* (2015). https://doi.org/10.15352/afa/06-4-247.
- Farrukh Maksutovich Mukhamedov; Nasir Ganikhodjaev. *Quantum Quadratic Stochastic Processes and Their Ergodic Properties* (2015). https://doi.org/10.1007/978-3-319-22837-2_8.
- Farrukh Maksutovich Mukhamedov; Muhammad Hafizuddin Bin Mohd Taha. *On Volterra and orthogonality preserving quadratic stochastic operators* (2016). https://doi.org/10.18514/mmn.2016.1090.
- Uygun Umurovich Jamilov. *On a Family of Strictly Non-Volterra Quadratic Stochastic Operators* (2016). https://doi.org/10.1088/1742-6596/697/1/012013.
- Uygun Umurovich Jamilov; M. Ladra; R. T. Mukhitdinov. *On the Equiprobable Strictly Non-Volterra Quadratic Stochastic Operators* (2016). https://doi.org/10.1007/s12346-016-0209-9.
- Farrukh Maksutovich Mukhamedov; Mansoor Khajibaevich Saburov. *Stability and Monotonicity of Lotka–Volterra Type Operators* (2016). https://doi.org/10.1007/s12346-016-0190-3.
- Farrukh Maksutovich Mukhamedov; Ahmad Fadillah Embong. *On Lyapunov Functions for Infinite Dimensional Volterra Quadratic Stochastic Operators* (2017). https://doi.org/10.1088/1742-6596/949/1/012022.
- Abigail Hardin; Utkir Abdulloevich Rozikov. *A quasi-strictly non-volterra quadratic stochastic operator* (2018). https://doi.org/10.48550/arxiv.1808.00229.
- Octavio Castaños; Uygun Umurovich Jamilov; Utkir Abdulloevich Rozikov. *On Volterra quadratic stochastic operators of a two-sex population on $S^1\times S^1$* (2018). https://doi.org/10.48550/arxiv.1808.01812.
- Nur Zatul Akmar Hamzah; Nasir Ganikhodjaev. *On non-ergodic Gaussian quadratic stochastic operators* (2018). https://doi.org/10.1063/1.5041665.
- Nasir Ganikhodjaev; Siti Hasanah Jusoo. *Strictly non-Volterra quadratic stochastic operator (QSO) on 3-dimensional simplex* (2018). https://doi.org/10.1063/1.5041664.
- Abigail Hardin; Utkir Abdulloevich Rozikov. *A Quasi-strictly Non-volterra Quadratic Stochastic Operator* (2019). https://doi.org/10.1007/s12346-019-00325-9.
- Mansoor Khajibaevich Saburov. *Ergodicity of non-homogeneous $$\mathbf {p}$$-majorizing quadratic stochastic operators* (2019). https://doi.org/10.1007/s11117-019-00727-8.
- Mansoor Khajibaevich Saburov; Khikmat Khajibaevich Saburov. *Ganikhodjaev's conjecture on mean ergodicity of quadratic stochastic operators* (2019). https://doi.org/10.56017/2181-1318.1032.
- Farrukh Maksutovich Mukhamedov; Uygun Umurovich Jamilov; Abror Pirnapasov. *On Nonergodic Uniform Lotka–Volterra Operators* (2019). https://doi.org/10.1134/s0001434619010280.
- A. Yu. Khamrayev. *On the Dynamics of a Quasistrictly Non-Volterra Quadratic Stochastic Operator* (2019). https://doi.org/10.1007/s11253-019-01712-w.
- Mansoor Khajibaevich Saburov; Khikmat Khajibaevich Saburov. *Ganikhodjaev’s Conjecture on Mean Ergodicity of Quadratic Stochastic Operators* (2020). https://doi.org/10.1134/s1995080220060165.
- Siti Nurlaili Karim; Nur Zatul Akmar Hamzah; Nasir Ganikhodjaev. *Regularity of Geometric quadratic stochastic operator generated by 2-partition of infinite points* (2020). https://doi.org/10.11113/mjfas.v16n3.1737.
- M. A. Tadzhieva; Dilfuza Eshmamatova; Rasul Ganikhodzhaev. *Volterra-type Quadratic Stochastic Operators with a Homogeneous Tournament* (2021). https://doi.org/10.22363/2413-3639-2021-67-4-783-794.
- Uygun Umurovich Jamilov; B. J. Mamurov. *Asymptotical Behavior of Trajectories of Non-Volterra Quadratic Stochastic Operators* (2022). https://doi.org/10.1134/s1995080222140165.
- Chin Hee Pah; Azizi Rosli. *Bijectivity of a Class of Lotka-Volterra Operators Defined on 2D-Simplex* (2022). https://doi.org/10.1007/978-3-031-06170-7_20.
- Ahmad Fadillah Embong. *Compatible Linear Lypunov Function for Infinite Dimensional Volterra Quadratic Stochastic Operators* (2022). https://doi.org/10.1007/978-3-031-06170-7_19.
- Chin Hee Pah; Azizi Rosli. *On a Class of Non-Ergodic Lotka–Volterra Operator* (2022). https://doi.org/10.1134/s1995080222120228.
- Uygun Umurovich Jamilov; K. A. Aralova. *The Dynamics of Superposition of Non-Volterra Quadratic Stochastic Operators on $$S^2$$* (2022). https://doi.org/10.1007/978-3-031-06170-7_23.
- K. A. Aralova; Uygun Umurovich Jamilov. *The dynamics of superposition of non-Volterra quadratic stochastic operators* (2022). https://doi.org/10.1080/10236198.2022.2126316.
- Farrukh Maksutovich Mukhamedov; Pah Chin Hee; Azizi Rosli. *A class of bijective Lotka–Volterra operators and its application* (2023). https://doi.org/10.1002/mma.9088.
- Farrukh Maksutovich Mukhamedov; Chin Hee Pah; Azizi Rosli. *On a convex combination of Lotka–Volterra operators* (2023). https://doi.org/10.1016/j.exco.2023.100133.
- A. Yu. Khamrayev. *Periodic and Regular Trajectories of Non-Volterra Quadratic Stochastic Operators* (2023). https://doi.org/10.1134/s1995080223100219.
- Siti Nurlaili Karim; Nur Zatul Akmar Hamzah; Nurfazatul Hazirah A. Rahman; Muhammad Fairuz Zulkefli; Nasir Ganikhodjaev. *Regularity of 2-partition Poisson quadratic stochastic operator with three different parameters* (2023). https://doi.org/10.1063/5.0124307.
- Ahmad Fadillah Embong;  Nur Natasha Lim Boon Chye @ Mohd Hairie Lim. *A Class of Two-Sex Population Quadratic Stochastic Operators: b-Bistochastic-Volterra* (2024). https://doi.org/10.17576/jqma.2001.2024.15.
- B. J. Mamurov. *Convergence of Trajectories of a Non-Volterra Quadratic Stochastic Operator* (2024). https://doi.org/10.3103/s1066369x24700786.
- B. J. Mamurov. *Convergence of the trajectories of a non-Volterra quadratic stochastic operator* (2024). https://doi.org/10.26907/0021-3446-2024-10-45-50.
- Farrukh Maksutovich Mukhamedov; Uygun Umurovich Jamilov; Mahammadjon Ibragimov. *Genetic algebras associated with permuted Lotka-Volterra operators* (2024). https://doi.org/10.1080/00927872.2024.2367758.
- K. A. Aralova; Uygun Umurovich Jamilov. *On a Superposition of Volterra and Permuted Volterra Quadratic Stochastic Operators* (2024). https://doi.org/10.1134/s1995080224600535.
- B. J. Mamurov. *On convergence of trajectories of a non-volterra quadratic stochastic operator* (2024). https://doi.org/10.1063/5.0199878.
- M. A. Tadzhieva; Dilfuza Eshmamatova; Rasul Ganikhodzhaev. *Volterra-Type Quadratic Stochastic Operators with a Homogeneous Tournament* (2024). https://doi.org/10.1007/s10958-024-06937-0.
- Uygun Umurovich Jamilov; R. T. Mukhitdinov. *Dynamics of a Convex Combination and Superposition of Non-Volterra Quadratic Stochastic Operators* (2025). https://doi.org/10.68381/jca32052.
- Nasir Ganikhodjaev. *Quadratic Stochastic Operators: Ergodic Properties and Their Applications to Evolutionary Games and Economic Models* (2025). https://doi.org/10.1007/978-3-032-09176-5_8.
- R. N. Ganikhodzhaev; S. I. Masharipov; J. X. Bekturdiyeva. *DEGENERATE CASES IN LOTKA–VOLTERRA SYSTEMS ACTING IN THE SIMPLEX $$S^3$$* (2026). https://doi.org/10.1007/s10958-026-08340-3.
- Kamola Solijanova. *DEGENERATE FIXED-POINT CONFIGURATIONS OF A DISCRETE LOTKA–VOLTERRA OPERATOR* (2026). https://doi.org/10.1007/s10958-026-08610-0.
- Sh. B. Abdurakhimova. *Dynamic Systems of a Volterra Quadratic Stochastic Operator with Variable Coefficients* (2026). https://doi.org/10.1134/s1055134426010013.
