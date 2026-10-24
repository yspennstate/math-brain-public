# P0334 literature verification — 2026-10-12

## Verified source

Eustasio del Barrio, Alberto González-Sanz, Jean-Michel Loubes, David Rodríguez-Vítores, *Distributional Limit Theory for Optimal Transport*, arXiv:2505.19104v2, updated 13 July 2026. Downloaded `source.pdf` (43 PDF pages), extracted `source.txt`.

Problem 2, PDF p.29, states: “Can we find necessary and sufficient conditions for the weak convergence of the quantile process” followed by `v_n(t) = sqrt(n)(F_n^{-1}(t) - F^{-1}(t)), 0 < t < 1`, and “as a random element in Lp(0, 1)?”

Theorem 2.4, PDF p.9, assumes a continuous density f, continuous f composed with F inverse on (0,1), monotonicity near both endpoints, and J_p(P)<infinity. The limit is B(t)/f(F inverse(t)). The surrounding paragraph says endpoint monotonicity might be unnecessary and that p=1 is resolved by [9]. The open question itself does not restrict to smooth densities.

Brendan K. Beare and Tetsuya Kaji, *A necessary and sufficient condition for convergence in distribution of the quantile process in L^1(0,1)*, arXiv:2502.01254v4, 16 April 2026 (PDF dated 17 April), accepted in Bernoulli. Downloaded `search_beare_pdf.pdf`, extracted `beare.txt`. Property Q, p.1: local absolute continuity of Q and integral sqrt(u(1-u)) dQ(u)<infinity. This solves only p=1 and is an ingredient, not a literature solution of p>1.

Sergey G. Bobkov and Michel Ledoux, *One-dimensional empirical measures, order statistics, and Kantorovich transport distances*, Memoirs AMS 261 (2019), no.1259, DOI 10.1090/memo/1259. The original author-hosted 140-page PDF was retrieved from https://perso.math.univ-toulouse.fr/ledoux/files/2016/12/MEMO.pdf and saved as `bobkov_ledoux.pdf`. Theorem 5.3, PDF/printed p.46, gives E W_p(mu_n,mu)^p <= (5p/sqrt(n+2))^p J_p(mu), for all p>=1,n>=1. It has no endpoint monotonicity hypothesis. Corollary A.22, p.109, identifies J_p with the weighted quantile derivative integral for locally absolutely continuous quantiles, including measures with singular components. Proposition A.17, p.104, and Lemma 5.8, p.51, explicitly use local absolute continuity. Proposition B.13, p.125, provides the underlying derivative bound for all absolutely continuous functions. Corollary 5.10, p.54, is the rate characterization paraphrased by the survey.

This theorem does not itself assert L^p weak convergence. The new signed-envelope approximation argument in ATTEMPT.md supplies that implication. Thus the result proved here is labeled SOLVED, not SOLVED_IN_LITERATURE.

## Search record and limitations

All network requests use Python requests; raw responses and exact URLs, dates, HTTP statuses are in `search_log.json`, `search_more_log.json`, `search_literature.py`, and `search_more.py`. Queries on 2026-10-12:

- arXiv API: all:quantile AND all:process AND all:Lp; exact phrase “quantile process”, latest updates, up to 80 results; id_list=2505.19104,2502.01254; title “One-dimensional empirical measures”; au:Bobkov AND au:Ledoux. First narrow query was unhelpful; broader phrase query returns the p=1 theorem but no exact p>1 solution in titles/abstracts inspected.
- OpenAlex: search “quantile process Lp”; search “Distributional Limit Theory for Optimal Transport”; title.search filter for source. All returned HTTP 429. Citing-works lookup remains unavailable without identifying a work ID; report this coverage limitation.
- Crossref: “quantile process Lp” (20); title query “Necessary and sufficient conditions quantile process” (15); book title query (3). Responses saved.
- Semantic Scholar: search “quantile process Lp” returned 429; direct ARXIV:2505.19104 with citation fields succeeded. Six citations listed: arXiv:2609.22240 (adversarial training), 2608.29565 (convex-order Wasserstein projection), 2607.18191 (regularized OT), 2606.25947 (finite-sample regularized OT), 2604.12940 (entropic OT), 2408.06534 (Monge–Ampère). These are leads only; no title directly addresses the target.
- GitHub repositories: quantile+process+Lp (zero); exact phrase “quantile process” (response saved).
- Author page request: https://perso.math.univ-toulouse.fr/ledoux/publications/ .
- Book PDF guess https://perso.math.univ-toulouse.fr/ledoux/files/2019/03/MEMO.pdf returned 404.
- Crossref book-title lookup succeeded and supplied DOI 10.1090/memo/1259 and AMS PDF URL. https://www.ams.org/memo/1259/memo1259.pdf returned 403. https://www.math.univ-toulouse.fr/~ledoux/ProbaTransport.pdf returned 404. The author's old root returned 200 (91 bytes).
- Author books page https://perso.math.univ-toulouse.fr/ledoux/books/ returned 200 and supplied the exact uppercase MEMO.pdf link in /2016/12/. Guesses /2016/12/Memo.pdf and /2016/12/Transport.pdf returned 404. Guess /2019/03/transport.pdf returned 200 but was not used as the book. The exact /2016/12/MEMO.pdf returned 200 and was fully identified before use.
- OpenAlex citing-works attempt: https://api.openalex.org/works?filter=cites:https%3A%2F%2Farxiv.org%2Fabs%2F2505.19104&per-page=30 returned 400: an arXiv URL is not a valid OpenAlex ID. Since the source-ID lookup was rate-limited, a correct OpenAlex citing-works enumeration could not be completed. The rate-limit body says the shared unauthenticated daily budget is exhausted. No credentials were accessed. The successful Semantic Scholar direct citation enumeration supplies partial citation coverage.
- Mistaken PDF guess arXiv:1407.0938 returned an unrelated gravity paper. Its identity was checked and it is excluded from all arguments.

No SOLVED_IN_LITERATURE verdict is justified by these searches.

The 66 records returned by the broader arXiv phrase query were screened by title; the recent relevant abstracts, the direct source-citation results and repository descriptions were inspected. No exact p>1 solution was identified. This is a bounded search, not a proof that no such paper exists. The July 2026 paper *Weighted Gaussian Approximations for Increments of the Uniform Empirical and Quantile Processes: Fixed-Endpoint Extensions to the Finite-Count Scale*, arXiv:2606.28222v2, is a related lead concerning uniform increments, not the same L^p criterion. The GitHub phrase query returned Zhongjun-Qu/Quantile-Process (conditional partially linear models) and liuqiaochu/QPLoF (a lack-of-fit R package), neither a solution of this question.

Beare–Kaji's exact theorem references used in the proof are Theorem 3.1 (sufficiency and identification) and Theorem 3.2 (necessity), both p.16. The Property Q definition is p.1. Their p=1 scope was respected throughout.

## Read-only prior work

Math recall: “quantile process Lp J_p del Barrio”; linked attempt card claim_53bf4ebf896e62666f6a92fbd6142e74b82fa6f035977b76dbb91a7d0f77dade read in full. Prior result: necessary J_p for smooth density via Gaussian limit and Tonelli; no endpoint tightness proof.
Brain recall: “quantile process endpoint tightness mistakes”; “quantile process Lp”. Mostly unrelated hits; treated as hints only.
Intake: rg P0334 across jsonl files in 06_math_research found the October 10 list entry. Read-only git ls-tree origin/master, filtered for P0334, found no matching path. No repository writes.


Additional arXiv citation-abstract query (2026-10-12), HTTP 200: https://export.arxiv.org/api/query?id_list=2609.22240,2608.29565,2607.18191,2606.25947,2604.12940,2408.06534,2606.28222 . Raw response: search_citation_abstracts.xml. All seven abstracts were inspected; they concern other models or uniform increments, not the full target criterion. Exact references follow.

- Alberto González-Sanz, Marcel Nutz, Austin J. Stromme, *Finite-sample bounds for regularized optimal transport*, http://arxiv.org/abs/2606.25947v1, updated 2026-06-24T15:22:57Z. Lead only; abstract does not assert the target theorem.

- Yuanlong Ruan, *Central limit theorem for Wasserstein projection - the case of convex order*, http://arxiv.org/abs/2608.29565v1, updated 2026-08-30T05:21:21Z. Lead only; abstract does not assert the target theorem.

- Alberto González-Sanz, Shunan Sheng, *Linearization of Monge-Ampère Equations and Statistical Applications*, http://arxiv.org/abs/2408.06534v4, updated 2025-11-26T22:22:44Z. Lead only; abstract does not assert the target theorem.

- Carlos Cardoso-Perelló, Alberto González-Sanz, Marcel Nutz, *Sharp Asymptotics for Regularized Optimal Transport*, http://arxiv.org/abs/2607.18191v1, updated 2026-07-20T17:30:33Z. Lead only; abstract does not assert the target theorem.

- Kim Jakwang, Kwon Dohyun, *Statistical Inference for Adversarial Training: Central Limit Theorems via Optimal Transport*, http://arxiv.org/abs/2609.22240v1, updated 2026-09-04T03:14:00Z. Lead only; abstract does not assert the target theorem.

- Abdelhakim Necir, *Weighted Gaussian Approximations for Increments of the Uniform Empirical and Quantile Processes: Fixed-Endpoint Extensions to the Finite-Count Scale*, http://arxiv.org/abs/2606.28222v2, updated 2026-07-03T21:31:52Z. Lead only; abstract does not assert the target theorem.

- Santiago Arenas-Velilla, Axel Munk, Luis-Alberto Rodríguez, *Distributional Convergence of Empirical Entropic Optimal Transport and Statistical Applications*, http://arxiv.org/abs/2604.12940v1, updated 2026-04-14T16:34:33Z. Lead only; abstract does not assert the target theorem.


Standard theorem references used in the written proof: A. W. van der Vaart and J. A. Wellner, *Weak Convergence and Empirical Processes*, Springer Series in Statistics, Springer, 1996 (Donsker and empirical-process asymptotic equicontinuity); Xavier Fernique, “Intégrabilité des vecteurs gaussiens”, C. R. Acad. Sci. Paris Sér. A-B 270 (1970), A1698–A1699 (Gaussian Banach-space integrability). These are invoked as standard ingredients, not claimed as the p>1 solution.
